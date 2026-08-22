"""Tests for the build-quality diagnostic.

Most of these pin the worked example: Medusa was computed by hand on
2026-08-21 and the module has to reproduce every figure. The rest pin the four
places the arithmetic is easy to get wrong, the caveat the report must print
before any verdict, and the import boundary that keeps this a diagnostic.
"""
import ast
import inspect
import re

import pytest

from smite import (assemble, build_index, build_quality as bq, combat, efficiency,
                   notes, recommend, scoring)


@pytest.fixture(scope="module")
def items_by_name():
    return {it["name"]: it for it in recommend.load_items()}


def _god(name):
    return notes.read_note(recommend.DATA_ROOT / "Gods" / f"{name}.md")[0]


@pytest.fixture(autouse=True)
def printed_stat_lines():
    """Every test reads printed stat lines, whatever another test left on."""
    before = efficiency.apply_pricing_flags({})
    yield
    efficiency.restore_pricing_flags(before)


MEDUSA_COMMUNITY = ["Tyrfing", "Odysseus' Bow", "Silverbranch Bow", "Riptalon",
                    "The Executioner", "Manchu Bow"]
MEDUSA_OURS = ["Berserker's Shield", "Jotunn's Revenge", "Nimble Ring", "Death Metal",
               "Rod of Tahuti", "Soul Gem"]


# ── The worked example ────────────────────────────────────────────────────

def test_medusa_reproduces_the_hand_computation(items_by_name):
    """Computed by hand on 2026-08-21, before the module existed. Every figure
    to 0.1 — a module that differs has misread one of the four traps below."""
    god = _god("Medusa")
    community = bq.profile(god, MEDUSA_COMMUNITY, items_by_name)
    ours = bq.profile(god, MEDUSA_OURS, items_by_name)

    assert community["cost"] == 13750
    assert ours["cost"] == 15400
    assert community["stats"] == {"Attack Speed %": 133.0, "Attack Damage": 80.0,
                                  "Strength": 25.0, "Penetration %": 20.0,
                                  "Lifesteal %": 7.5}

    expect = [
        (community, 70, 352.8, 35.9, 388.6),
        (community, 170, 233.2, 23.7, 256.9),
        (ours, 70, 242.4, 72.4, 314.8),
        (ours, 170, 150.8, 45.1, 195.9),
    ]
    for prof, prot, basic, ability, total in expect:
        assert prof["basic_dps"][prot] == pytest.approx(basic, abs=0.05)
        assert prof["ability_dps"][prot] == pytest.approx(ability, abs=0.05)
        assert prof["total_dps"][prot] == pytest.approx(total, abs=0.1)


def test_medusa_viper_shot_is_skipped_by_the_shared_parser_not_by_special_case(items_by_name):
    """The hand computation excluded Viper Shot. So does the module — because
    its scaling line reads `Damage Scaling Per Tick:`, which
    `damage_value.ability_damage_components` does not accept, and an ability
    with ranks and no scaling is skipped everywhere. No Medusa-shaped rule."""
    counted, dropped = bq.ability_rotation(_god("Medusa"))
    assert [a["name"] for a in counted] == ["Acid Spray", "Lacerate", "Petrify"]
    assert dropped == []
    code = inspect.getsource(bq).split('"""', 2)[2]   # past the module docstring
    assert "Viper" not in code


def test_medusa_per_1000g_divides_by_the_builds_own_gold(items_by_name):
    ours = bq.profile(_god("Medusa"), MEDUSA_OURS, items_by_name)
    assert ours["per_1000g"]["total_dps"][70] == pytest.approx(314.8 / 15.4, abs=0.05)
    assert ours["per_1000g"]["ehp_physical"] == pytest.approx(ours["ehp_physical"] / 15.4)


# ── The four traps ────────────────────────────────────────────────────────

def test_attack_speed_per_level_is_a_percent():
    """Medusa: 1.0 base at 1.4 per level is 1.266 at level 20, not 27.6."""
    assert bq.base_attack_speed(_god("Medusa"), 20) == pytest.approx(1.266)
    assert bq.base_attack_speed(_god("Medusa"), 1) == pytest.approx(1.0)


def test_attack_power_correction_is_combats_not_reimplemented(items_by_name):
    """0.81 on the base only, never on per-level growth — the module calls
    `combat.god_attack_power` rather than carrying its own copy."""
    god = _god("Medusa")
    prof = bq.profile(god, MEDUSA_COMMUNITY, items_by_name)
    assert prof["attack_power"] == pytest.approx(combat.god_attack_power(god, 20))
    assert prof["attack_power"] == pytest.approx(44.4 * 0.81 + 2.4 * 19)
    assert "ATTACK_POWER_SCALE" not in inspect.getsource(bq).split('"""', 2)[2]


def test_flat_and_percent_penetration_are_never_summed(items_by_name):
    """10 flat and 10% are different goods. Against 170 protection the pair is
    worth (170 x 0.9) - 10 = 143 effective, not 150 (as 20 flat) and not
    136 (as 20%)."""
    god = _god("Medusa")
    flat = {"name": "flat", "cost": 1000, "stats": {"Penetration": "10"}, "tier": 3}
    pct = {"name": "pct", "cost": 1000, "stats": {"Penetration": "10%"}, "tier": 3}
    pool = dict(items_by_name, flat=flat, pct=pct)
    both = bq.profile(god, ["flat", "pct"], pool)
    assert both["stats"] == {"Penetration": 10.0, "Penetration %": 10.0}
    expected_prot = combat.effective_protection(170, flat_pen=10, pct_pen=0.10)
    assert expected_prot == pytest.approx(143.0)
    none = bq.profile(god, [], pool)
    ratio = both["basic_dps"][170] / none["basic_dps"][170]
    assert ratio == pytest.approx(combat.mitigation(143.0) / combat.mitigation(170.0))


def test_a_chain_god_swings_at_the_chains_mean(items_by_name):
    """Thanatos's 1 / 0.75 / 1.5 chain averages 1.0833 per swing; the
    multipliers apply to swing time too, so neither the first hit nor the
    sum is the sustained figure."""
    god = _god("Thanatos")
    prof = bq.profile(god, [], items_by_name)
    assert prof["mean_swing"] == pytest.approx(1.0833, abs=1e-3)
    assert prof["raw_basic"] == pytest.approx(combat.god_attack_power(god, 20) * prof["mean_swing"])


# ── What else the profile has to get right ────────────────────────────────

def test_deathbringer_is_the_one_passive_combat_reads(items_by_name):
    assert bq.crit_multiplier_for(["Deathbringer"]) == pytest.approx(1.85)
    assert bq.crit_multiplier_for(["Death Metal"]) == pytest.approx(1.5)


def test_effective_health_is_level_20_base_plus_items(items_by_name):
    """EHP = HP x (1 + prot/100) off the scraped base at level 20 and the
    build's Max Health / protections — `combat.effective_health`, not a
    reimplementation."""
    god = _god("Medusa")
    prof = bq.profile(god, ["Berserker's Shield"], items_by_name)
    health = 569.48 + 86.48 * 19 + 200
    phys = 18.76 + 2.76 * 19 + 40
    assert prof["health"] == pytest.approx(health)
    assert prof["ehp_physical"] == pytest.approx(combat.effective_health(health, phys))
    assert prof["ehp_magical"] == pytest.approx(combat.effective_health(health, 25.3 + 1.38 * 19))


def test_an_ability_without_a_cooldown_is_dropped_and_named(items_by_name):
    """Never imputed — the same rule `damage_value._base_cooldown` applies."""
    god = {"name": "x", "base_stats": {}, "abilities": [
        {"slot": "1st Ability", "name": "has cd", "cooldown": [10, 8],
         "details": ["Damage: 100 | 200", "Damage Scaling: 50% Strength"]},
        {"slot": "2nd Ability", "name": "line only",
         "details": ["Damage: 50 | 60", "Damage Scaling: 50% Strength",
                     "Cooldown: 20 | 15 seconds"]},
        {"slot": "3rd Ability", "name": "no cd",
         "details": ["Damage: 50 | 60", "Damage Scaling: 50% Strength"]},
    ]}
    counted, dropped = bq.ability_rotation(god)
    assert [(a["name"], a["cooldown"], a["base"]) for a in counted] == [
        ("has cd", 8.0, 200.0), ("line only", 15.0, 60.0)]
    assert dropped == ["no cd"]
    prof = bq.profile(god, [], items_by_name)
    assert prof["dropped"] == ["no cd"]
    assert prof["ability_dps"][70] == pytest.approx(
        combat.damage_dealt(200, 70) / 8 + combat.damage_dealt(60, 70) / 15)


def test_an_unknown_item_raises_rather_than_reading_as_a_weaker_build(items_by_name):
    with pytest.raises(KeyError):
        bq.build_totals(["No Such Item"], items_by_name)


# ── Which builds ──────────────────────────────────────────────────────────

def test_community_core_is_the_first_entry_aspect_or_not():
    """Achilles's first community entry carries `Aspect of Prowess`; it is
    still the one `validate._community_slots` scores against, so it is the
    one compared here."""
    note = recommend.load_build_note("Achilles")
    assert note["builds"][0].get("aspect")
    assert bq.community_core(note)[0] == note["builds"][0]["slot_order"][0]["name"]


def test_suggested_core_takes_the_base_kit_model_entry():
    note = recommend.load_build_note("Medusa")
    assert bq.suggested_core(note) == MEDUSA_OURS
    assert bq.suggested_core(note, "core") != MEDUSA_OURS
    assert bq.suggested_core({"builds": [
        {"source": "suggested", "archetype": "model", "aspect": "X", "slot_order": ["a"] * 6},
    ]}) == []


def test_a_short_or_unknown_build_is_skipped_not_padded(items_by_name):
    god = _god("Medusa")
    note = {"builds": [
        {"source": "community", "slot_order": [{"name": n} for n in MEDUSA_COMMUNITY[:5]]},
        {"source": "suggested", "archetype": "model", "slot_order": MEDUSA_OURS},
    ]}
    assert bq.compare(god, note, items_by_name) is None
    note["builds"][0]["slot_order"].append({"name": "Not An Item"})
    assert bq.compare(god, note, items_by_name) is None


def test_primary_role_collapses_dual_labels():
    assert bq.primary_role({"role": "Solo Jungle"}) == "Solo"
    assert bq.primary_role({"role": "Carry"}) == "Carry"


# ── Distribution ──────────────────────────────────────────────────────────

def _row(god, role, theirs, mine):
    def prof(v):
        return {"total_dps": {70: v, 170: v}, "per_1000g": {"total_dps": {70: v, 170: v},
                "ehp_physical": v, "ehp_magical": v}, "ehp_physical": v, "ehp_magical": v}
    return {"god": god, "role": role, "primary_role": role.split()[0],
            "community": prof(theirs), "ours": prof(mine)}


def test_distribution_counts_ahead_behind_and_level_as_a_ratio():
    """A ratio, so a 400-DPS Carry and a 150-DPS Support weigh the same; a
    delta inside ±0.5% is level rather than a win by rounding."""
    rows = [_row("a", "Carry", 100, 120), _row("b", "Mid", 100, 80),
            _row("c", "Solo", 100, 100.2), _row("d", "Support", 50, 100)]
    d = bq.distribution(rows, "dps_70")
    assert (d["n"], d["ahead"], d["behind"], d["level"]) == (4, 2, 1, 1)
    assert d["quantiles"][0] == pytest.approx(-20.0)
    assert d["quantiles"][100] == pytest.approx(100.0)
    roles = bq.by_role(rows, "dps_70")
    assert list(roles) == ["Carry", "Mid", "Solo", "Support"]
    assert roles["Support"]["ahead"] == 1


def test_flips_names_gods_whose_sign_changes_between_runs():
    a = [_row("x", "Mid", 100, 110), _row("y", "Mid", 100, 90)]
    b = [_row("x", "Mid", 100, 95), _row("y", "Mid", 100, 90)]
    assert [g for g, _, _ in bq.flips(a, b)] == ["x"]


# ── The blind spot ────────────────────────────────────────────────────────

def test_blind_means_passive_text_the_pricing_flags_do_not_read():
    """Deathbringer's passive is priced (crit multiplier), so it is not blind;
    an item with passive prose and no priced grant is; an item with no passive
    is not, whatever the flags say."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    items = [
        {"name": "Deathbringer", "tier": 3, "cost": 2900,
         "stats": {"Strength": "45", "Critical Chance": "20%"},
         "passive": "+35% Critical Strike Damage."},
        {"name": "Prose", "tier": 3, "cost": 2500, "stats": {"Strength": "40"},
         "passive": "On hit: something the model cannot read."},
        {"name": "Plain", "tier": 3, "cost": 2000, "stats": {"Strength": "30"}, "passive": ""},
    ]
    gods = [{"name": "g"}]
    builds = {"g": {"builds": [
        {"source": "community", "slot_order": [{"name": "Prose"}, {"name": "Plain"}]},
        {"source": "suggested", "archetype": "model", "slot_order": ["Deathbringer"]},
    ]}}
    blind = bq.passive_blind_spot(items, gods, builds, weights)
    assert blind["buildable"] == 3 and blind["with_passive"] == 2
    assert blind["priced"] == ["Deathbringer"]
    assert blind["blind"] == 1
    assert blind["community"]["blind"] == 1 and blind["community"]["slots"] == 2
    assert blind["community"]["top_blind"] == [("Prose", 1)]
    assert blind["ours"]["blind"] == 0
    assert efficiency.PRICE_ADAPTIVE is False   # flags put back afterwards


def test_the_real_pool_is_mostly_blind():
    """The fact the caveat exists for. Pinned loosely — the exact share moves
    with the item set — but a pool that reads as mostly visible means the
    definition broke, not that passives got priced."""
    items = recommend.load_items()
    gods = recommend.load_gods()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    builds = {g["name"]: recommend.load_build_note(g["name"]) for g in gods}
    blind = bq.passive_blind_spot(items, gods, builds, weights)
    assert blind["blind_share"] > 0.8
    assert blind["community"]["share"] > 0.6
    assert "Deathbringer" in blind["priced"]


# ── The report ────────────────────────────────────────────────────────────

def test_the_report_states_the_caveat_before_any_verdict(tmp_path, items_by_name):
    """A report that states a winner without the blind spot is worse than no
    report. The caveat and every assumption have to precede the first table."""
    god = _god("Medusa")
    note = recommend.load_build_note("Medusa")
    row = bq.compare(god, note, items_by_name)
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    blind = bq.passive_blind_spot(recommend.load_items(), [god], {"Medusa": note}, weights)
    out = tmp_path / "report.md"
    bq.write_report([row], [], [row], [], [row], [], blind, "abc123", out)
    text = out.read_text(encoding="utf-8")
    first_table = text.index("\n|")
    caveat = text.index("READ THIS BEFORE ANY NUMBER BELOW")
    assert caveat < first_table
    for phrase in ("cannot see", "verdict in our favour is the one to distrust",
                   "full ability uptime", "no relic", "single target",
                   "no lifesteal sustain", "no crowd control", "no wave clear"):
        assert phrase in text[:first_table], phrase
    assert "Input fingerprint: `abc123`" in text
    assert "| COMMUNITY vs squishy (70) | 352.8 | 35.9 | **388.6** |" in text
    assert "| Medusa | Carry | 13,750 / 15,400 |" in text


def test_the_report_is_deterministic(tmp_path, items_by_name):
    """Like `_calibration.md`: byte-identical on the same inputs, so its diff
    is a record of what a commit did to the builds."""
    god = _god("Medusa")
    note = recommend.load_build_note("Medusa")
    row = bq.compare(god, note, items_by_name)
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    blind = bq.passive_blind_spot(recommend.load_items(), [god], {"Medusa": note}, weights)
    a, b = tmp_path / "a.md", tmp_path / "b.md"
    bq.write_report([row], [], [row], [], [row], [], blind, "f", a)
    bq.write_report([row], [], [row], [], [row], [], blind, "f", b)
    assert a.read_bytes() == b.read_bytes()


def test_priced_run_restores_the_pricing_flags(items_by_name):
    """The sensitivity run flips the module globals and must put them back —
    and must never price the crit multiplier twice."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    god = _god("Medusa")
    builds = {"Medusa": recommend.load_build_note("Medusa")}
    rows, _ = bq.run([god], recommend.load_items(), builds, weights, priced=True)
    # The Executioner's Adaptive Stat lands as Strength under the shipped flags.
    assert rows[0]["community"]["stats"]["Strength"] == pytest.approx(25 + 30)
    assert efficiency.PRICE_ADAPTIVE is False
    assert efficiency.PRICE_CRIT_MULTIPLIERS is False


def test_cli_prints_one_god(capsys):
    assert bq.main(["--god", "Medusa"]) == 0
    out = capsys.readouterr().out
    assert "352.8" in out and "314.8" in out
    assert bq.main(["--god", "Nobody"]) == 1


# A figure, as a reader meets one: a decimal, a percentage, a gold amount, or
# an ahead/behind count. The fingerprint (bare hex) and the title carry none.
_FIGURE = re.compile(r"\d+\.\d|\d+%|\d[\d,]*g|DPS|ahead|behind")
_CAVEAT = "READ THIS BEFORE ANY NUMBER BELOW"


def _caveat_precedes_every_figure(text, where):
    figure = _FIGURE.search(text)
    if figure is None:
        return
    caveat = text.find(_CAVEAT)
    assert caveat != -1, f"{where}: prints a figure and never states the blind spot"
    assert caveat < figure.start(), (
        f"{where}: first figure {figure.group()!r} at {figure.start()} precedes the caveat at {caveat}")


def _cli_invocations(parser, tmp_path):
    """One invocation per option the parser knows, discovered from the parser
    itself so a flag added tomorrow is exercised without anyone remembering
    to list it here. An option this cannot drive fails the test rather than
    going quietly untested."""
    base = ["--out", str(tmp_path / "report.md")]
    yield "(no flags)", base
    for action in parser._actions:
        if not action.option_strings or action.dest in ("help", "out"):
            continue
        flag = action.option_strings[-1]
        if action.nargs == 0:
            yield flag, base + [flag]
        elif action.choices:
            for choice in action.choices:
                yield f"{flag} {choice}", base + [flag, str(choice)]
        elif action.dest == "god":
            yield f"{flag} Medusa", base + [flag, "Medusa"]
        elif action.dest == "archetype":
            for archetype in ("model", "core"):
                yield f"{flag} {archetype}", base + [flag, archetype]
        else:
            pytest.fail(f"{flag}: this test does not know a value to drive it with — "
                        "teach it one, so the new path is checked for the caveat")


def test_every_cli_path_states_the_caveat_before_its_first_figure(tmp_path, capsys):
    """`--god Medusa` is the invocation STATE.md §6 recommends and it once
    printed a DPS table with no caveat at all (2026-08-21) — `main` returned
    before the blind spot was measured. The full run's stdout had the same
    fault in a softer form: the ahead/behind counts came first and the blind
    spot after. This drives every path the parser exposes, reads everything
    each one printed or wrote, and requires the caveat before the first
    figure in each."""
    parser = bq.build_parser()
    for where, argv in _cli_invocations(parser, tmp_path):
        for stale in tmp_path.iterdir():
            stale.unlink()
        assert bq.main(argv) == 0, where
        _caveat_precedes_every_figure(capsys.readouterr().out, f"{where} stdout")
        for written in tmp_path.iterdir():
            _caveat_precedes_every_figure(written.read_text(encoding="utf-8"),
                                          f"{where} -> {written.name}")


def test_the_only_way_out_of_the_module_is_the_caveated_sink():
    """Every print and every file write in `build_quality.py` lives inside
    `emit`, which puts the caveat first. A new `--flag` that prints its own
    table cannot bypass the caveat, because it has no way to print."""
    tree = ast.parse(inspect.getsource(bq))
    parents = {}
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            parents[child] = node

    def enclosing_function(node):
        while node in parents:
            node = parents[node]
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                return node.name
        return None

    offenders = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        f = node.func
        name = f.id if isinstance(f, ast.Name) else f.attr if isinstance(f, ast.Attribute) else None
        if name not in ("print", "write", "write_text", "write_bytes", "open", "writelines"):
            continue
        if name == "print" and any(k.arg == "file" for k in node.keywords):
            continue   # stderr diagnostics ("Nobody: not compared") carry no figure
        if enclosing_function(node) != "emit":
            offenders.append(f"{name} at line {node.lineno} in {enclosing_function(node)}")
    assert not offenders, offenders


# ── The boundary ──────────────────────────────────────────────────────────

def test_nothing_in_the_model_imports_this():
    """A diagnostic, not a scoring input. Register §4.4 is what happens when a
    damage measure becomes a fit signal; this pins the import boundary."""
    for mod in (scoring, assemble, recommend, build_index, efficiency):
        assert "build_quality" not in inspect.getsource(mod), mod.__name__
