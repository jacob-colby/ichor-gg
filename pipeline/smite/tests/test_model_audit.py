"""The model audit harness (`smite.model_audit`) and the whole-model sanity
invariants it carries as tests.

Everything here reads the FROZEN reference inputs
(`fixtures/frozen/reference/`, Open Beta 47, captured 2026-11-03) with the
LIVE code and `_weights.yaml`, so a red test here means the MODEL moved, never
that the data refreshed — `stats_gate` rejects a refresh that turns a test red
(STATE.md §6), and a test that pinned live data would block every patch.
"""
import copy
import math

import pytest

from smite import model_audit as ma
from smite import passive_sim, recommend, scoring, side_by_side as sbs


@pytest.fixture(scope="module")
def frozen():
    return ma.load_frozen()


@pytest.fixture(scope="module")
def weights():
    return scoring.load_weights(recommend.WEIGHTS_PATH)


@pytest.fixture(scope="module")
def tags_map():
    return scoring.load_tags(recommend.TAGS_PATH)


@pytest.fixture(scope="module")
def ibn(frozen):
    return {it["name"]: it for it in frozen["items"]}


@pytest.fixture(scope="module")
def snapshot():
    return ma.read_snapshot()


@pytest.fixture(scope="module")
def recomputed(frozen, weights, tags_map):
    return ma.compute_reference(frozen, weights, tags_map)


# ── 1. Reference builds ──────────────────────────────────────────────────

def test_reference_builds_and_verdicts_unchanged(snapshot, recomputed):
    changes = ma.diff_reference(snapshot, recomputed)
    assert not changes, (
        "The model's reference builds or verdicts moved:\n  " + "\n  ".join(changes) +
        "\nIf this is intended, run `python -m smite.model_audit reference --write` and explain "
        "every line above in the PR description.")


def test_reference_is_two_gods_per_role(frozen):
    from smite import build_quality as bq
    for role, names in ma.REFERENCE_GODS.items():
        assert len(names) == 2
        for n in names:
            assert bq.primary_role(frozen["gods"][n]) == role, n


def test_snapshot_covers_every_mode_and_has_a_model_build(snapshot):
    assert set(snapshot) == set(ma.reference_names())
    for god, row in snapshot.items():
        for mode in ma.MODES:
            assert "core" in row[mode]["builds"] and "model" in row[mode]["builds"], (god, mode)


def test_diff_reference_names_what_moved():
    old = {"X": {"Conquest": {"builds": {"core": ["a", "b"]}, "verdict": "level"}}}
    new = {"X": {"Conquest": {"builds": {"core": ["a", "c"]}, "verdict": "Ichor better"}}}
    lines = ma.diff_reference(old, new)
    assert "X / Conquest verdict: level -> Ichor better" in lines
    assert "X / Conquest / core: -['b'] +['c']" in lines
    assert ma.diff_reference(old, old) == []


# ── 2. Held-out split ────────────────────────────────────────────────────

def test_split_is_a_fixed_function_of_the_name():
    # Pinned: if these move, every held-out comparison ever reported moved.
    assert ma.split_of("Medusa") == "heldout"
    assert ma.split_of("Zeus") == "tuning"
    assert ma.split_of("Thor") == "heldout"
    assert ma.split_of("Agni") == "tuning"


def test_split_share_is_near_the_target_on_the_live_roster():
    names = [g["name"] for g in recommend.load_gods()]
    share = sum(ma.split_of(n) == "heldout" for n in names) / len(names)
    assert 0.15 <= share <= 0.45


def test_split_metrics_partitions_the_gods():
    per_god = {n: {"coverage": 0.5, "win_weighted": 0.5, "pairs": [(1.0, 0.5), (2.0, 0.6)]}
               for n in ("Medusa", "Zeus", "Thor", "Agni")}
    m = ma.split_metrics(per_god)
    assert m["heldout"]["gods"] + m["tuning"]["gods"] == 4
    assert m["heldout"]["gods"] == 2


def test_heldout_report_flags_a_lower_heldout_score():
    head = {"tuning": {"gods": 1, "win_weighted": .5, "spearman": .3, "coverage": .5},
            "heldout": {"gods": 1, "win_weighted": .4, "spearman": .3, "coverage": .4}}
    base = copy.deepcopy(head)
    _, ok = ma.heldout_report(head, base)
    assert ok
    base["heldout"]["win_weighted"] = 0.41
    _, ok = ma.heldout_report(head, base)
    assert not ok


# ── 3. Passive firing ────────────────────────────────────────────────────

def test_an_ability_proc_fires_and_a_dead_kit_never_fires_it(frozen, ibn, weights):
    tg = ma._targets(frozen["context"])["Conquest"]
    agni = frozen["gods"]["Agni"]
    six = ["Soul Gem", "Spear of the Magus", "Obsidian Shard", "Rod of Tahuti",
           "Book of Thoth", "Spear of Desolation"]
    with ma.pricing(weights):
        live = ma.classify_build(agni, six, ibn, tg)
        assert live["Soul Gem"][0] == ma.FIRES and live["Soul Gem"][1] > 0
        # No damaging ability parsed (Ares on OB47): nothing triggers an ability-hit passive.
        dead = dict(agni, abilities=[a for a in agni["abilities"] if "Basic Attack" in (a.get("slot") or "")])
        melee = {"ally_support": None, "melee": "test"}   # so Soul Gem's ally rider is reachable
        assert ma.classify_build(dead, six, ibn, tg, melee)["Soul Gem"][0] == ma.NEVER


def test_lotus_sickle_is_kit_blocked_on_agni_and_not_on_a_supporting_kit(frozen, ibn, weights):
    from smite import kit_fit
    tg = ma._targets(frozen["context"])["Conquest"]
    six = ["Lotus Sickle", "Spear of the Magus", "Obsidian Shard", "Rod of Tahuti",
           "Book of Thoth", "Soul Gem"]
    with ma.pricing(weights):
        out = ma.classify_build(frozen["gods"]["Agni"], six, ibn, tg)
        assert out["Lotus Sickle"][0] == ma.KIT_BLOCKED
        caps = {"ally_support": "test", "melee": None}
        assert ma.classify_build(frozen["gods"]["Agni"], six, ibn, tg, caps)["Lotus Sickle"][0] == ma.UNSIMULATED
    assert kit_fit.item_needs(ibn["Lotus Sickle"]) == {"ally_support"}


def test_firing_report_lists_flagged_items():
    rows = [{"mode": "Joust", "god": "Agni", "build": "core", "item": "Lotus Sickle",
             "class": ma.KIT_BLOCKED, "fires": 0},
            {"mode": "Joust", "god": "Agni", "build": "core", "item": "Soul Gem",
             "class": ma.FIRES, "fires": 9, "ally_rider": True}]
    text = "\n".join(ma.firing_lines(rows))
    assert "| Lotus Sickle | 1 | 0 | 0 | 1 |" in text
    assert "| Soul Gem | 1 |" in text


# ── 4. Weight sensitivity (the machinery; the sweep itself is slow) ─────────

def test_every_nudge_finds_its_weight(weights):
    for label, apply in ma.NUDGES:
        w = copy.deepcopy(weights)
        assert apply(w, 1.2), f"{label} is not in _weights.yaml any more"
        assert w != weights, label


def test_nudge_scales_only_its_target(weights):
    w = copy.deepcopy(weights)
    dict(ma.NUDGES)["kit_blend"](w, 0.8)
    assert w["kit_blend"] == pytest.approx(weights["kit_blend"] * 0.8)
    assert w["signals"] == weights["signals"]


# ── 5. Coverage ──────────────────────────────────────────────────────────

def test_coverage_counts_are_consistent(frozen, weights):
    gods = list(frozen["gods"].values())
    c = ma.coverage(frozen["items"], gods, weights)
    i = c["items"]
    assert i["simulated"] + i["partial"] + i["not_simulated"] == i["with_passive"] <= i["buildable"]
    assert c["aspects"]["simulated"] == len(sbs.SIMULATED_ASPECTS)
    assert c["aspects"]["tuned"] <= c["aspects"]["total"]
    assert 0 < c["gods"]["self_heals_simulated"] <= c["gods"]["tracked"] == len(gods)
    assert "# Model coverage" in "\n".join(ma.coverage_lines(c))


# ── Sanity invariants over the whole model ───────────────────────────────

def _builds(snapshot, mode="Conquest", archetypes=("core", "model")):
    for god in ma.reference_names():
        for arch in archetypes:
            yield god, arch, snapshot[god][mode]["builds"][arch]


def test_adding_an_item_never_lowers_a_stat_it_grants(frozen, ibn, snapshot):
    pool = [it["name"] for it in frozen["items"] if scoring.is_buildable(it)]
    own = {n: sbs.printed_totals([n], ibn)[0] for n in pool}
    bad, checks = [], 0
    for god, arch, six in _builds(snapshot):
        for k in range(6):
            pre = six[:k]
            before, _, _ = sbs.build_stats(pre, ibn)
            for x in pool:
                if x in pre:
                    continue
                after, _, _ = sbs.build_stats(pre + [x], ibn)
                for stat, v in own[x].items():
                    if v > 0:
                        checks += 1
                        if after.get(stat, 0.0) < before.get(stat, 0.0) - 1e-9:
                            bad.append((god, arch, k, x, stat))
    assert checks > 10_000
    assert not bad, bad[:10]


#: Breakpoints where a figure FALLS from 2 to 4 or 4 to 6 items, on the frozen
#: inputs. Reviewed 2026-11-03, NOT fixed (the audit session changes no model);
#: each is a finding in the PR. Two causes:
#:   * ehp_*: the fight run's lifesteal and kill-heals only land on a LIVE
#:     target, and one kill per 10s fight is the rule, so more damage kills the
#:     squishy sooner and heals less: offence lowers fight EHP (Thanatos 6704
#:     -> 5457 physical from 4 to 6 items while static EHP is flat).
#:   * Bellona sustained_*: Berserker's Shield reads the fight's health bar, so
#:     Hussar's Wings' 500 health keeps her above its threshold longer.
#: A NEW entry fails the test; one that stops occurring is reported stale.
KNOWN_POWER_DROPS = {
    ("Zeus", "core", "ehp_physical"), ("Zeus", "core", "ehp_magical"),
    ("Zeus", "model", "ehp_physical"), ("Zeus", "model", "ehp_magical"),
    ("Bellona", "core", "sustained_squishy"), ("Bellona", "core", "sustained_tank"),
    ("Fenrir", "model", "ehp_physical"), ("Fenrir", "model", "ehp_magical"),
    ("Thanatos", "core", "ehp_physical"), ("Thanatos", "core", "ehp_magical"),
    ("Thanatos", "model", "ehp_physical"), ("Thanatos", "model", "ehp_magical"),
}


@pytest.fixture(scope="module")
def breakpoint_power(frozen, ibn, snapshot):
    tg = ma._targets(frozen["context"])["Conquest"]
    return {(god, arch): {k: sbs.power(frozen["gods"][god], six[:k], ibn, tg) for k in (2, 4, 6)}
            for god, arch, six in _builds(snapshot)}


def test_power_rises_from_two_to_four_to_six_items(breakpoint_power):
    drops = set()
    for (god, arch), pw in breakpoint_power.items():
        for key in sbs.DAMAGE_KEYS + sbs.SURVIVAL_KEYS:
            a, b, c = (pw[k][key] for k in (2, 4, 6))
            if a > b + 1e-6 or b > c + 1e-6:
                drops.add((god, arch, key))
    assert not drops - KNOWN_POWER_DROPS, f"new power drops: {sorted(drops - KNOWN_POWER_DROPS)}"
    assert not KNOWN_POWER_DROPS - drops, f"stale (fixed?): {sorted(KNOWN_POWER_DROPS - drops)}"


def test_composite_power_rises_with_no_exceptions(breakpoint_power):
    def composite(pw):
        d = math.prod(pw[k] for k in sbs.DAMAGE_KEYS) ** (1 / len(sbs.DAMAGE_KEYS))
        s = math.prod(pw[k] for k in sbs.SURVIVAL_KEYS) ** (1 / len(sbs.SURVIVAL_KEYS))
        return math.sqrt(d * s)
    for key, pw in breakpoint_power.items():
        a, b, c = (composite(pw[k]) for k in (2, 4, 6))
        assert a < b < c, (key, a, b, c)


def test_power_figures_are_finite_and_positive(breakpoint_power):
    for key, pw in breakpoint_power.items():
        for k, figs in pw.items():
            for m in sbs.DAMAGE_KEYS + sbs.SURVIVAL_KEYS:
                assert math.isfinite(figs[m]) and figs[m] > 0, (key, k, m, figs[m])


def test_no_score_is_nan_or_accidentally_zero(frozen, weights, tags_map):
    from smite import efficiency
    with ma.pricing(weights):
        eff, _ = efficiency.efficiency_scores(frozen["items"])
        for v in eff.values():
            assert math.isfinite(v["score"]) and 0.0 <= v["score"] <= 1.0
        for god in ma.reference_names():
            for mode in ma.MODES:
                gb = frozen["notes"][god] if mode == "Conquest" else {"builds": []}
                rows = scoring.score_god_items(frozen["gods"][god], frozen["items"], gb, eff, weights,
                                               tags_map, scoring.resolve_profile(weights, mode))
                assert rows
                for r in rows:
                    for k, v in r.items():
                        if isinstance(v, float):
                            assert math.isfinite(v), (god, mode, r["item"], k)
                    # Zero is allowed only for a reason: no stat on this god's map
                    # (fit 0, and `offmap_efficiency` charges the rest).
                    if r["quality"] == 0.0:
                        assert r["fit"] == 0.0, (god, mode, r["item"], r)
                    assert r["total"] >= 0.0


def _strip_modes(weights):
    w = copy.deepcopy(weights)
    w.pop("modes", None)
    (w.get("team_tags") or {}).pop("share", None)
    return w


def test_modes_differ_only_through_mode_rules(frozen, weights, tags_map):
    """With the `modes` block (and the per-mode team-tag shares) removed, the
    same god on the same community record gets the same builds in all three
    modes: no code path branches on the mode's NAME."""
    stripped = _strip_modes(weights)
    for god in ("Agni", "Thanatos", "Atlas"):
        g = frozen["gods"][god]
        with ma.pricing(stripped):
            per_mode = {m: recommend.build_suggested_entries(g, frozen["items"], {"builds": []},
                                                             stripped, tags_map, m)
                        for m in ma.MODES}
        assert per_mode["Conquest"] == per_mode["Joust"] == per_mode["Arena"], god


def test_a_mode_that_sets_every_signal_ignores_the_base_signals(frozen, weights, tags_map):
    """Joust and Arena override all four signals, so the base `signals` block
    (Conquest's) must not reach them by ANY path. The strip-modes test above
    cannot see a leak from the base weights — it deletes the modes, not the
    base — and one shipped: `assemble.conversion_args` / `overflow_args` read
    base efficiency (0.35) in place of the mode's 0.5 (PR #96, finding 4).
    Perturbing the base must leave those modes' builds exactly as they were."""
    full = {m for m in ("joust", "arena")
            if set((weights["modes"][m] or {}).get("signals") or {}) >= set(weights["signals"])}
    assert full == {"joust", "arena"}, "the premise moved: a mode no longer sets every signal"
    moved = copy.deepcopy(weights)
    moved["signals"] = {k: (v * 3.0 if k == "efficiency" else v * 0.5)
                        for k, v in weights["signals"].items()}
    for god in ma.reference_names():
        g = frozen["gods"][god]
        for mode in ("Joust", "Arena"):
            with ma.pricing(weights):
                a = recommend.build_suggested_entries(g, frozen["items"], {"builds": []},
                                                      weights, tags_map, mode)
            with ma.pricing(moved):
                b = recommend.build_suggested_entries(g, frozen["items"], {"builds": []},
                                                      moved, tags_map, mode)
            assert a == b, (god, mode)


def test_the_mode_rules_do_change_builds(snapshot):
    """The control for the test above: with the rules in, modes differ."""
    moved = sum(snapshot[g]["Conquest"]["builds"]["core"] != snapshot[g]["Joust"]["builds"]["core"]
                for g in snapshot)
    assert moved >= 3
