"""Criterion 2's side-by-side, and the passive simulators it runs.

Arithmetic tests read a TOY god (every number chosen so the hand computation
is one line) or the files frozen in `fixtures/frozen/side_by_side/` on
2026-11-02 (items, Medusa and her Conquest note at Open Beta 46). Never
regenerate those to make a test pass. The invariants at the bottom read the
live data.
"""
import ast
import json
import math
from pathlib import Path

import pytest

from smite import combat, passive_sim as ps, side_by_side as sbs

FROZEN = Path(__file__).resolve().parent / "fixtures" / "frozen" / "side_by_side"
PIPELINE = Path(__file__).resolve().parents[1]


def frozen_items():
    return {it["name"]: it for it in json.loads((FROZEN / "items.json").read_text(encoding="utf-8"))}


def toy_god(abilities=(), melee=False, attack_speed=1.0):
    """Level-20 attack power 0.81 x 100 = 81, no growth, 1.0 swings/s."""
    details = ["Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage",
               f"Range: {1.92 if melee else 8.8} meters"]
    return {"name": "Toy", "damage_type": "physical", "role": "Carry",
            "base_stats": {"health": {"base": 2000.0, "per_level": 0.0},
                           "physical_prot": {"base": 0.0, "per_level": 0.0},
                           "magical_prot": {"base": 0.0, "per_level": 0.0},
                           "attack_speed": {"base": attack_speed, "per_level": 0.0},
                           "attack_power": {"base": 100.0, "per_level": 0.0}},
            "abilities": [{"slot": "Basic Attack", "name": "Toy Basic Attack", "details": details}]
            + list(abilities)}


def toy_ability(name="Nuke", damage=100, cooldown=4, ult=False, scaling="50% Strength"):
    return {"slot": "Ultimate" if ult else "1", "name": name, "cooldown": [cooldown],
            "details": [f"Damage: {damage}", f"Damage Scaling: {scaling}"]}


def target(prot=0.0, base_health=2000.0, item_health=0.0, **kw):
    t = {"base_health": base_health, "item_health": item_health,
         "physical_prot": prot, "magical_prot": prot, "plating": 0.0, "dampening": 0.0}
    t.update(kw)
    t["max_health"] = t["base_health"] + t["item_health"]
    return t


def item(name, stats=None, passive="", cost=2500, tier=3):
    return {"name": name, "stats": stats or {"Strength": "10"}, "passive": passive,
            "cost": cost, "tier": tier}


def ctx(items, stats=None, stacks="full"):
    return ps.StatContext(items=items, stats=stats or dict(items), level=20, stacks=stacks)


# ── Stat hooks, hand-computed off each item's text ────────────────────────

def test_devourers_full_stacks_is_75_stacks_plus_the_evolution():
    assert ps._devourers(ctx({})) == {"Strength": 40.0, "Lifesteal %": 6.75, "Penetration": 5.0}
    assert ps._devourers(ctx({}, stacks="none")) == {}


def test_thebes_full_is_600_plus_100_health_and_ten_protections():
    assert ps._thebes(ctx({})) == {"Max Health": 700, "Physical Protection": 10.0,
                                   "Magical Protection": 10.0}


def test_book_of_thoth_reads_item_mana_and_its_own_stacks():
    # 350 item mana + 500 stack mana + 100 evolved = 950, at 7% = 66.5.
    assert ps._thoth_converts(ctx({"Max Mana": 350.0})) == {"Intelligence": pytest.approx(66.5)}
    # Unstacked: 350 at 5%.
    assert ps._thoth_converts(ctx({"Max Mana": 350.0}, stacks="none")) == {
        "Intelligence": pytest.approx(17.5)}


def test_transcendence_is_three_percent_with_no_evolved_increase():
    assert ps._transcendence_converts(ctx({"Max Mana": 250.0})) == {"Strength": pytest.approx(25.5)}
    assert ps._transcendence_grants(ctx({})) == {"Penetration": 10.0}


def test_nimble_ring_counts_whole_tens_of_intelligence():
    assert ps._nimble(ctx({}, {"Intelligence": 139.0})) == {"Attack Damage": 13.0, "Attack Speed %": 13.0}


def test_adaptive_takes_the_higher_printed_item_stat_and_strength_on_a_tie():
    g = ps._adaptive(30.0, 55.0)
    assert g(ctx({"Strength": 50.0, "Intelligence": 60.0})) == {"Intelligence": 55.0}
    assert g(ctx({"Strength": 60.0, "Intelligence": 60.0})) == {"Strength": 30.0}


def test_rod_of_tahuti_adds_a_quarter_of_item_intelligence_after_grants():
    real = {"Rod of Tahuti": item("Rod of Tahuti", {"Intelligence": "85"}),
            "Nimble Ring": item("Nimble Ring", {"Intelligence": "35"})}
    stats, _, _ = sbs.build_stats(list(real), real)
    # converts run in build order: Tahuti sees 120 -> +30 = 150; Nimble sees 150.
    assert stats["Intelligence"] == pytest.approx(150.0)
    assert stats["Attack Damage"] == pytest.approx(15.0)


# ── The clock ─────────────────────────────────────────────────────────────

def test_a_bare_swing_is_hand_computable():
    # 81 attack power, no items, 1.0/s, 0 protection: hits at t=0..9 -> 10 x 81.
    s = sbs.Sim(toy_god(), [], {}, target())
    assert s.run_window() == pytest.approx(810.0)


def test_mitigation_matches_combat_exactly_when_no_passive_adds_anything():
    s = sbs.Sim(toy_god(), [], {}, target(prot=70.0))
    expect = combat.damage_dealt(100.0, 70.0)
    assert s.mitigated(100.0, "physical", 0.0, kind="ability") == pytest.approx(expect)


def test_uncapped_penetration_stacks_past_the_cap():
    items = {"Pen": item("Pen", {"Penetration": "60%"})}
    s = sbs.Sim(toy_god(), ["Pen"], items, target(prot=100.0))
    # Capped at 40%, plus 20% uncapped -> 60% off 100 -> 40 protection.
    assert s.mitigated(100.0, "physical", 0.0, kind="proc", uncapped=0.20) == pytest.approx(100 * 100 / 140)


def test_abilities_recast_on_effective_cooldown_and_resolve_before_the_swing():
    god = toy_god([toy_ability(damage=100, cooldown=4)])
    s = sbs.Sim(god, [], {}, target())
    s.run_window()
    # Casts at 0, 4, 8 -> 3 x 100 (no Strength); 10 swings x 81.
    assert s.by_channel["ability"] == pytest.approx(300.0)
    assert s.by_channel["attack"] == pytest.approx(810.0)


def test_cooldown_rate_and_world_stone_shorten_the_clock():
    god = toy_god([toy_ability(cooldown=90, ult=True)])
    items = {"The World Stone": item("The World Stone", {"Cooldown Rate": "25"})}
    s = sbs.Sim(god, ["The World Stone"], items, target())
    assert s.rotation[0]["effective_cooldown"] == pytest.approx(90 * 0.75 * 100 / 125)


def test_burst_is_every_ability_once_then_one_swing():
    god = toy_god([toy_ability(damage=100), toy_ability(name="Two", damage=50)])
    assert sbs.Sim(god, [], {}, target(), window=None).run_burst() == pytest.approx(231.0)


# ── On-hit and on-ability passives through the clock ─────────────────────

def test_odysseus_reads_attack_damage_as_the_swing_and_hits_the_target_three_times():
    items = {"Odysseus' Bow": item("Odysseus' Bow", {"Attack Damage": "20"})}
    s = sbs.Sim(toy_god(), ["Odysseus' Bow"], items, target())
    s.run_window()
    # Swing = 81 attack power + 100% x 20 Attack Damage = 101. Swings 4 and 8
    # of 10, each 3 chain hits on the lone target of 15 + 0.6 x 101.
    assert s.by_item["Odysseus' Bow"] == pytest.approx(2 * 3 * (15 + 0.6 * 101))


def test_frozen_odysseus_text_and_value_on_medusa():
    """Frozen OB46 item text and Medusa: the proc is 15 + 60% of HER swing
    (81.564 attack power, no other stat), never 15 + 60% of a 0 stat."""
    items = frozen_items()
    text = items["Odysseus' Bow"]["passive"]
    assert "Every fourth Attack Hit" in text and "15 (+60% Attack Damage)" in text
    assert "Can hit the same target more than once" in text
    assert ps.ODYSSEUS_HITS_ON_TARGET == 3
    god = json.loads((FROZEN / "gods.json").read_text(encoding="utf-8"))["Medusa"]
    s = sbs.Sim(god, ["Odysseus' Bow"], items, target())
    assert s.attack_power == pytest.approx(81.564)
    assert s.attacks_per_second() == pytest.approx(1.8357, abs=1e-4)
    s.run_window()
    # 19 swings in 10s at 1.8357/s -> procs on swings 4, 8, 12, 16.
    assert s.by_item["Odysseus' Bow"] == pytest.approx(4 * 3 * (15 + 0.6 * 81.564))
    assert round(s.by_item["Odysseus' Bow"], 2) == 767.26


def test_silverbranch_arrows_count_whole_attacks_per_second():
    items = {"Silverbranch Bow": item("Silverbranch Bow", {"Attack Speed": "100%"})}
    s = sbs.Sim(toy_god(), ["Silverbranch Bow"], items, target())
    s.run_window()
    # 2.0/s -> 20 swings, every third -> 6 procs, 2 arrows x 25% x 81 each.
    assert s.by_item["Silverbranch Bow"] == pytest.approx(6 * 2 * 0.25 * 81.0)


def test_executioner_shred_lands_after_the_hit_and_caps_at_four():
    items = {"The Executioner": item("The Executioner", {"Attack Speed": "0%"})}
    s = sbs.Sim(toy_god(), ["The Executioner"], items, target(prot=100.0))
    s.run_window()
    # Adaptive +30 Strength -> swing 111. Hits see 0,1,2,3,4,4,... stacks of 7%.
    expect = sum(111.0 * 100 / (100 + 100 * (1 - 0.07 * min(k, 4)))  for k in range(10))
    assert s.by_channel["attack"] == pytest.approx(expect)


def test_soul_reaver_is_four_ticks_once_per_ability():
    god = toy_god([toy_ability(cooldown=4)])
    items = {"Soul Reaver": item("Soul Reaver", {"Intelligence": "0"})}
    t = target(base_health=2000.0, item_health=500.0)
    s = sbs.Sim(god, ["Soul Reaver"], items, t)
    s.run_window()
    assert s.by_item["Soul Reaver"] == pytest.approx(4 * (0.012 * 2000 + 0.03 * 500))


def test_heartseeker_is_two_percent_of_strength_as_percent_max_health():
    god = toy_god([toy_ability(cooldown=100)])
    items = {"Heartseeker": item("Heartseeker", {"Strength": "100"})}
    s = sbs.Sim(god, ["Heartseeker"], items, target(base_health=3000.0), window=None)
    s.run_burst()
    assert s.by_item["Heartseeker"] == pytest.approx(0.02 * 100 / 100 * 3000)


def test_shattering_is_shared_and_fires_once_per_ten_seconds():
    god = toy_god([toy_ability(damage=100, cooldown=4, scaling="0% Strength")])
    items = {"Titan's Bane": item("Titan's Bane", {"Strength": "0"}),
             "Obsidian Shard": item("Obsidian Shard", {"Intelligence": "0"})}
    s = sbs.Sim(god, list(items), items, target(prot=100.0))
    s.run_window()
    # Casts at 0, 4, 8; only the first gets 20% -> 80 protection.
    assert s.by_channel["ability"] == pytest.approx(100 * 100 / 180 + 2 * 50.0)


def test_tyrfing_caps_at_six_stacks_at_level_twenty():
    items = {"Tyrfing": item("Tyrfing", {"Strength": "0"})}
    s = sbs.Sim(toy_god(), ["Tyrfing"], items, target())
    s.run_window()
    assert s.by_item["Tyrfing"] == pytest.approx(sum(15 + 15 * min(k, 6) for k in range(10)))


def test_hydra_reads_melee_from_the_scraped_range():
    god = toy_god([toy_ability(cooldown=100, scaling="0% Strength")], melee=True)
    items = {"Hydra's Lament": item("Hydra's Lament", {"Strength": "0"})}
    s = sbs.Sim(god, list(items), items, target(), window=None)
    s.run_burst()
    assert s.by_channel["attack"] == pytest.approx(81.0 * 1.30)


def test_barbed_carver_stacks_after_the_ability_and_repeats_a_share_of_each_hit():
    god = toy_god([toy_ability(damage=100, cooldown=100, scaling="0% Strength")])
    items = {"Barbed Carver": item("Barbed Carver", {"Lifesteal": "0%"})}
    s = sbs.Sim(god, list(items), items, target(), window=None)
    s.run_burst()
    # The ability applies one stack and gets none; the swing gets 8% of 81.
    assert s.by_item["Barbed Carver"] == pytest.approx(0.08 * 81.0)


def test_spear_of_the_magus_marks_from_the_next_hit_including_inside_a_burst():
    god = toy_god([toy_ability(damage=100, cooldown=100, scaling="0% Strength")])
    items = {"Spear of the Magus": item("Spear of the Magus", {"Intelligence": "0"})}
    s = sbs.Sim(god, list(items), items, target(), window=None)
    s.run_burst()
    assert s.by_channel["ability"] == pytest.approx(100.0)
    assert s.by_channel["attack"] == pytest.approx(81.0 * 1.05)


def test_disabling_a_passive_keeps_its_printed_stats():
    items = {"Tyrfing": item("Tyrfing", {"Strength": "25"})}
    on = sbs.Sim(toy_god(), ["Tyrfing"], items, target())
    off = sbs.Sim(toy_god(), ["Tyrfing"], items, target(), disabled={"Tyrfing"})
    assert on.run_window() > off.run_window() == pytest.approx(10 * 106.0)


# ── Effective health ──────────────────────────────────────────────────────

def test_health_gated_protection_is_integrated_over_the_bar():
    items = {"Berserker's Shield": item("Berserker's Shield", {"Max Health": "0"})}
    p, m, h = sbs.effective_health(toy_god(), ["Berserker's Shield"], items)
    assert p == pytest.approx(0.4 * 2000 + 0.6 * 2000 * 1.15)
    assert m == pytest.approx(p)


def test_freya_and_berserker_overlap_slice_by_slice():
    items = {"Berserker's Shield": item("Berserker's Shield", {"Max Health": "0"}),
             "Freya's Tears": item("Freya's Tears", {"Max Health": "0"})}
    p, _, _ = sbs.effective_health(toy_god(), list(items), items)
    expect = 2000 * (0.25 * 1.0 + 0.15 * 1.15 + 0.10 * 1.30 + 0.50 * 1.45)
    assert p == pytest.approx(expect)


# ── Cleaning, rates, verdict ──────────────────────────────────────────────

def test_community_six_replaces_components_from_the_record_never_from_us():
    note = json.loads((FROZEN / "medusa_conquest.json").read_text(encoding="utf-8"))
    god = json.loads((FROZEN / "gods.json").read_text(encoding="utf-8"))["Medusa"]
    six, subs = sbs.community_six(god, note, frozen_items())
    assert six == ["Devourer's Gauntlet", "Dagger of Frenzy", "Dominance", "Riptalon",
                   "Silverbranch Bow", "The Executioner"]
    assert subs == [{"slot": 6, "dropped": "Manchu Bow", "class": "unfinished",
                     "used": "The Executioner", "position": 6,
                     "note": "most-picked finished alternate in the record"}]


def test_one_cleanup_rule_drop_then_fill_appended():
    """The side-by-side and `community_target` agree on what the community
    CHOSE (the scored slots, in order); the fill comes after them and is
    never a slot choice."""
    from smite import community_target as ct
    items = {n: item(n) for n in ("A", "B", "C", "D", "E", "F", "G")}
    items["Comp"] = item("Comp", tier=2)
    items["Relic"] = dict(item("Relic", tier=None), stats={})
    slots = [{"name": "A"}, {"name": "Comp", "alternates": [{"name": "B", "pick_rate": 0.1},
                                                            {"name": "F", "pick_rate": 0.3}]},
             {"name": "C"}, {"name": "Relic"}, {"name": "D"}, {"name": "E",
             "alternates": [{"name": "G", "pick_rate": 0.2}]}]
    six, fills = ct.comparison_six(slots, items)
    assert ct.target(slots, items) == ["A", "C", "D", "E"]
    assert six == ["A", "C", "D", "E", "F", "G"]            # scored first, fills appended
    assert [(f["dropped"], f["class"], f["used"], f["position"]) for f in fills] == [
        ("Comp", "unfinished", "F", 5), ("Relic", "unscoreable", "G", 6)]


def test_community_rates_prefer_the_slot_pick_over_an_alternate():
    note = json.loads((FROZEN / "medusa_conquest.json").read_text(encoding="utf-8"))
    assert sbs.community_rates(note, "Riptalon") == {"pick_rate": 0.28, "win_rate": 0.53,
                                                     "where": "slot 4"}
    assert sbs.community_rates(note, "The Executioner")["where"] == "slot 4 alternate"


@pytest.mark.parametrize("d,s,expect", [
    (1.10, 1.00, "Ichor better"), (1.00, 1.06, "Ichor better"),
    (0.90, 1.00, "community better"), (1.04, 0.94, "community better"),
    (1.10, 0.90, "trade-off"), (0.90, 1.10, "trade-off"),
    (1.04, 0.96, "level"),
])
def test_verdict_rule(d, s, expect):
    assert sbs.verdict(d, s) == expect


def test_frozen_medusa_reproduces_the_worked_example():
    items = frozen_items()
    god = json.loads((FROZEN / "gods.json").read_text(encoding="utf-8"))["Medusa"]
    t = target(prot=70.0, base_health=2212.6)
    six = ["Devourer's Gauntlet", "Dagger of Frenzy", "Dominance", "Riptalon",
           "Silverbranch Bow", "The Executioner"]
    s = sbs.Sim(god, six, items, t, disabled={"Dagger of Frenzy"})
    s.run_window()
    # 145 Strength (35 + 40 full-stack Devourer's + 40 Dominance + 30 adaptive),
    # 2.66 swings/s; pinned so a change to the clock is a visible diff. With
    # Dagger of Frenzy's active off (its only effect), PR #77's figure stands:
    # nothing else in the clock moved when the FIGHT block was added (this
    # toy target carries no enemy, and no other item here reacts to a takedown).
    assert s.stat("Strength") == pytest.approx(145.0)
    assert s.attacks_per_second() == pytest.approx(2.6586, abs=1e-4)
    assert round(s.total()) == 8854
    # The active on (2026-11-02): pressed at t=0, +90 Attack Damage and +40%
    # attack speed for 6 attacks, 15s cooldown, refreshed by the one kill.
    on = sbs.Sim(god, six, items, t)
    on.run_window()
    assert on.kills == 1 and on.assists == 1
    assert round(on.total()) == 10445


# ── Invariants over the live data ─────────────────────────────────────────

FIFTEEN = ("Devourer's Gauntlet", "Gauntlet of Thebes", "The Executioner", "Barbed Carver",
           "Book of Thoth", "Magi's Cloak", "Soul Reaver", "Brawler’s Beat Stick", "Nimble Ring",
           "Odysseus' Bow", "Polynomicon", "Bancroft's Talon", "Ethereal Staff",
           "Transcendence", "Gem of Isolation")


def test_every_item_the_analysis_named_has_a_decision():
    for name in FIFTEEN:
        p = ps.REGISTRY[name]
        assert p.status in (ps.SIMULATED, ps.PARTIAL, ps.NOT_SIMULATED)
        if p.status != ps.SIMULATED:
            assert p.assumptions, f"{name} is {p.status} and must say why"


def test_every_registry_name_is_a_live_item():
    from smite import recommend
    live = {it["name"] for it in recommend.load_items()}
    assert sorted(set(ps.REGISTRY) - live) == []


def test_nothing_in_the_model_imports_the_diagnostic():
    for mod in ("scoring", "assemble", "recommend", "build_index", "efficiency"):
        tree = ast.parse((PIPELINE / f"{mod}.py").read_text(encoding="utf-8"))
        names = {a.name for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))
                 for a in n.names}
        assert not names & {"side_by_side", "passive_sim", "smite.side_by_side", "smite.passive_sim"}


# ── Aspect matching ───────────────────────────────────────────────────────

def _note(aspect, rate):
    return {"builds": [{"source": "community", "aspect": aspect, "aspect_pick_rate": rate,
                        "aspect_win_rate": 0.55, "slot_order": []}]}


def test_an_aspect_played_by_most_of_the_community_is_the_kit():
    k = sbs.kit_for(_note("Aspect of Heartbreak", 0.79))
    assert (k["kit"], k["simulated"]) == ("Aspect of Heartbreak", False)


def test_a_minority_or_exactly_half_aspect_leaves_the_base_kit():
    assert sbs.kit_for(_note("Aspect of X", 0.50))["kit"] == "base"
    assert sbs.kit_for(_note("Aspect of X", 0.20)) ["simulated"] is True
    assert sbs.kit_for(_note(None, None))["kit"] == "base"


def test_an_unsimulated_aspect_god_gets_no_verdict_and_no_count():
    flat = lambda d, s: {k: (d, s) for k in sbs.BREAKPOINTS}
    rows = [{"role": "Mid", "damage_axis": 0.5, "survival_axis": 2.0,
             "verdict": sbs.ASPECT_NOT_SIMULATED, "coverage": {"ok": True},
             "breakpoint_axes": flat(0.5, 2.0),
             "kit": {"aspect": "A", "pick_rate": 0.8, "kit": "A", "simulated": False}},
            {"role": "Mid", "damage_axis": 1.2, "survival_axis": 1.0, "verdict": "Ichor better",
             "coverage": {"ok": True}, "breakpoint_axes": flat(1.2, 1.0),
             "kit": {"aspect": None, "pick_rate": None, "kit": "base", "simulated": True}}]
    assert sbs.verdict_counts(rows) == {"Mid": {"Ichor better": 1}}
    assert [r["kit"]["aspect"] for r in sbs.aspect_excluded(rows)] == ["A"]


def test_the_frozen_medusa_note_is_on_the_base_kit():
    note = json.loads((FROZEN / "medusa_conquest.json").read_text(encoding="utf-8"))
    assert sbs.kit_for(note)["kit"] == "base"


# ── Fairness: coverage, the 2/4/6 rule, phase labels ─────────────────────

def test_simulated_share_counts_only_fully_simulated_or_passiveless_gold():
    items = {"Riptalon": item("Riptalon", cost=3000),             # simulated
             "Plain": item("Plain", cost=1000),                   # no passive
             "Tekko-Kagi": item("Tekko-Kagi", passive="x", cost=2000),   # not simulated
             "Ethereal Staff": item("Ethereal Staff", passive="x", cost=2000)}   # partial
    assert sbs.simulated_share(list(items), items) == pytest.approx(4000 / 8000)


@pytest.mark.parametrize("ours,theirs,ok", [
    (0.80, 0.70, True), (0.49, 0.49, False), (0.90, 0.75, False), (0.64, 0.50, True)])
def test_coverage_check_threshold_and_gap(ours, theirs, ok):
    assert sbs.coverage_check(ours, theirs)[0] is ok


def test_the_coverage_gap_is_the_band_over_one_median_passive():
    # One item is ~1/6 of a build's gold; the median simulated passive is
    # worth 5.8% on the damage axis (module comment). The gap is the share
    # at which that stand-in moves the axis by exactly the band.
    assert sbs.COVERAGE_GAP == pytest.approx(sbs.BAND / (6 * 0.058), abs=0.005)


def test_weighted_axes_are_the_weighted_geometric_mean():
    bp = {2: (1.21, 1.0), 4: (1.0, 1.0), 6: (0.81, 1.0)}
    d, s = sbs.weighted_axes(bp)
    assert d == pytest.approx((1.21 * 0.81) ** (1 / 3))
    assert s == pytest.approx(1.0)
    assert sum(sbs.BREAKPOINT_WEIGHTS.values()) == pytest.approx(1.0)


def _row(bp, cov_ok=True, simulated=True):
    return {"kit": {"simulated": simulated}, "coverage": {"ok": cov_ok},
            "breakpoint_axes": bp, "damage_axis": bp[6][0], "survival_axis": bp[6][1]}


def test_ahead_early_behind_at_six_is_an_early_game_build_not_a_loss():
    bp = {2: (1.19, 1.0), 4: (1.08, 1.0), 6: (0.69, 1.0)}     # Medusa's shape
    assert sbs.judge_six_only(_row(bp)) == "community better"
    assert sbs.judge(_row(bp)) == sbs.EARLY_GAME
    late = {2: (0.85, 1.0), 4: (0.9, 1.0), 6: (1.2, 1.0)}
    assert sbs.judge(_row(late)) == sbs.LATE_GAME


def test_coverage_withholds_before_any_win_or_loss_and_aspect_comes_first():
    bp = {2: (1.3, 1.0), 4: (1.3, 1.0), 6: (1.3, 1.0)}
    assert sbs.judge(_row(bp)) == "Ichor better"
    assert sbs.judge(_row(bp, cov_ok=False)) == sbs.NOT_ENOUGH_SIMULATED
    assert sbs.judge(_row(bp, cov_ok=False), withhold=False) == "Ichor better"
    assert sbs.judge(_row(bp, cov_ok=False, simulated=False)) == sbs.ASPECT_NOT_SIMULATED
