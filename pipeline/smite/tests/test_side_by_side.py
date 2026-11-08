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
from datetime import date, datetime
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
    # 8854 until 2026-11-04, when the per-ability label rule put Viper Shot
    # (`Damage Scaling Per Tick:`) into the rotation. Re-derived by hand: one
    # cast in the 10s window, raw 30 + 8% x 145 Strength = 41.6, through
    # 70 x (1 - 0.20) - 5 = 51 protection -> x 100/151 = 27.55. The ability
    # channel moves by exactly that; attack and proc are unchanged to the digit.
    assert round(s.total()) == 8882
    # The active on (2026-11-02): pressed at t=0, +90 Attack Damage and +40%
    # attack speed for 6 attacks, 15s cooldown, refreshed by the one kill.
    on = sbs.Sim(god, six, items, t)
    on.run_window()
    assert on.kills == 1 and on.assists == 1
    assert round(on.total()) == 10473          # 10445 + the same 27.55


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


# ── The community window the page is labelled with (2026-11-05) ──────────
#
# `_meta.json`'s `data` string used to read BOTH halves off `data/_patch.json`,
# which records the current GAME patch — so its community half asserted
# something nothing had checked. It read "community window Open Beta 47"
# identically at 5e960b76 (a healthy Open Beta 46 window), at 6158066f (the
# one-day window that deleted 55 comparison pages, 166 items behind it) and at
# dc03ded4 (restored, 67,532 matches). A reader could not tell the three apart,
# and that is the one blind spot of the four a person would have caught the
# incident with.


def _items_table(window, played_use):
    return {"division": "obsidian", "window": window, "matches_analyzed": None,
            "window_start": "", "window_end": "",
            "items": {n: {"matches_played": p, "use_rate": u, "win_rate": 0.5,
                          "matches_won": p // 2}
                      for n, (p, u) in played_use.items()}}


def test_the_label_names_the_window_that_was_read_not_the_current_patch(tmp_path):
    """The regression this exists for: an Open Beta 46 table must not be
    labelled Open Beta 47 just because that is the live patch. This fixture
    has `matches_analyzed` null, as every file written before 2026-11-05 does,
    so the label falls back to the derivation and says BUILDS."""
    p = tmp_path / "_community_items.json"
    p.write_text(json.dumps(_items_table("ob46", {"Adroit Ring": (399, 0.005908310134454777)})),
                 encoding="utf-8")
    assert sbs.community_window_label(p) == "Open Beta 46, 67,532 builds"


def test_the_label_says_matches_once_the_file_carries_the_match_count(tmp_path):
    """And the same table with the field populated, which is what
    `refresh.window_provenance` writes from 2026-11-05: 14,667 MATCHES, the
    figure STATE.md section 7's "Community sample" row has always carried,
    against 67,532 builds in the same window."""
    table = _items_table("ob46", {"Adroit Ring": (399, 0.005908310134454777)})
    table["matches_analyzed"] = 14667
    p = tmp_path / "_community_items.json"
    p.write_text(json.dumps(table), encoding="utf-8")
    assert sbs.community_window_label(p) == "Open Beta 46, 14,667 matches"


def test_a_thin_window_is_visible_in_the_label(tmp_path):
    """The one-day Open Beta 47 window, as the 2026-11-04 refresh read it: the
    count is what makes it obvious, so it has to be in the string."""
    p = tmp_path / "_community_items.json"
    p.write_text(json.dumps(_items_table("ob47", {"Adroit Ring": (1, 0.005154639175257732)})),
                 encoding="utf-8")
    label = sbs.community_window_label(p)
    assert label == "Open Beta 47, 194 builds"
    assert label != sbs.community_window_label.__doc__   # not a constant


def test_the_derivation_counts_builds_and_every_item_agrees():
    """`matches_played / use_rate` is the source's own denominator and is
    exact — every item gives the same integer — but it is a share of BUILDS,
    so the denominator is god-builds observed and NOT the match count. PR #109
    labelled it "matches"; it is ~4.5x the real figure, because the god index
    records about 4.5 of a match's ten seats.

    What it asserts is that builds and matches are DIFFERENT quantities, and
    that the gap between them is one the game allows — NOT a figure to one
    decimal. It pinned `round(builds / matches, 1) == 4.5` until 2026-11-07,
    and that ratio moves every day, not just at a boundary: 4.468 on the 11-06
    table and 4.533 on 11-07, inside one window, against 4.604 for the whole
    of Open Beta 46. 11-06 sat 0.018 from rounding to 4.4. The bounds that
    replace it are physical, not fitted: above 1, because #109's conflation
    makes the two the same number; at most 10, because a Conquest match has
    ten seats, so more builds than that per match means one of the counts is
    not what it says. `live_window.py` has the convention."""
    table = json.loads(sbs.COMMUNITY_ITEMS_PATH.read_text(encoding="utf-8"))
    derived = {round(r["matches_played"] / r["use_rate"])
               for r in table["items"].values() if r.get("use_rate")}
    assert len(derived) == 1, sorted(derived)
    builds = derived.pop()
    assert sbs.community_sample(dict(table, matches_analyzed=None)) == (builds, "builds")
    # And the two really are different quantities on the shipped table.
    matches, unit = sbs.community_sample(table)
    assert unit == "matches" and matches < builds
    assert 1 < builds / matches <= 10, (builds, matches, round(builds / matches, 3))


def test_the_stated_match_count_wins_over_the_derivation():
    """The file's own figure is authoritative when it has one; the derivation
    is the fallback for the files that do not (everything before 2026-11-05)."""
    table = _items_table("ob46", {"Adroit Ring": (399, 0.005908310134454777)})
    table["matches_analyzed"] = 12345
    assert sbs.community_sample(table) == (12345, "matches")
    assert sbs.community_sample(dict(table, matches_analyzed=None))[1] == "builds"


def test_the_label_degrades_rather_than_lying(tmp_path):
    missing = tmp_path / "nope.json"
    assert sbs.community_window_label(missing) == "unknown window"
    no_window = tmp_path / "no_window.json"
    no_window.write_text(json.dumps({"items": {}}), encoding="utf-8")
    assert sbs.community_window_label(no_window) == "unknown window"
    odd = tmp_path / "odd.json"
    odd.write_text(json.dumps(_items_table("1m", {"X": (10, 0.5)})), encoding="utf-8")
    assert sbs.community_window_label(odd) == "1m, 20 builds"


def test_the_items_and_gods_half_still_tracks_the_current_patch():
    """Only the community half was wrong. The wiki IS re-scraped on patch day,
    so `data_patch`'s first half reads `_patch.json` as it always did."""
    patch = json.loads((sbs.REPO_ROOT / "data" / "_patch.json").read_text(encoding="utf-8"))
    label = sbs.data_patch()
    assert label.startswith(f"items/gods {patch['data_patch']},")
    assert f"community window {sbs.community_window_label()}" in label


def test_the_shipped_label_names_the_community_window_and_its_real_size():
    """The live assertion, pinned to the shipped WINDOW: Open Beta 47. That
    half fires on every patch boundary, so updating it declares the new window
    established rather than tidying a test.

    The SIZE half is derived, not pinned. It read "2,859 matches" and refused
    "12,774" until 2026-11-07, and both of those are one day's figures: the
    11-07 table is 4,089 matches over 18,535 builds in the same window, so the
    pins would have blocked every day's data. What they caught still fails
    here, on any day: the label must carry the table's own MATCH count, and
    must not carry its derived BUILDS count. `live_window.py` has the
    convention.

    It failed against the pre-#109 code, which read `_patch.json` for both
    halves and said "community window Open Beta 47" over an Open Beta 46
    table; the count was then corrected from that window's 67,532 builds to
    its 14,667 MATCHES (2026-11-05).

    NOTE: both halves now read Open Beta 47, so this test can no longer catch
    the community half copying the item patch by itself. That structural
    check lives in `test_the_items_and_gods_half_still_tracks_the_current_patch`,
    which derives both halves instead of pinning them. The unit half of #109
    is still caught here, by refusing the derived builds figure."""
    table = json.loads(sbs.COMMUNITY_ITEMS_PATH.read_text(encoding="utf-8"))
    matches, unit = sbs.community_sample(table)
    builds, builds_unit = sbs.community_sample(dict(table, matches_analyzed=None))
    assert (unit, builds_unit) == ("matches", "builds") and matches != builds
    label = sbs.data_patch()
    assert "community window Open Beta 47, " in label, label
    assert f"community window Open Beta 47, {matches:,} matches" in label, label
    assert f"{builds:,}" not in label, (builds, label)


def test_the_shipped_match_count_agrees_with_the_documented_community_sample():
    """The cross-check that would have caught #109's unit error: STATE.md
    section 7 has carried the match count all along.

    Until 2026-11-07 it asserted the row held the shipped count EXACTLY. The
    row is written by hand and the nightly refresh never touches docs, so that
    went red on the first refresh after every edit to the row (2,859 written
    on 11-06, 4,089 shipped on 11-07) — with the data arriving as a pull
    request, it would have blocked every day's data. `doc_audit` reports that
    drift for a human to read, which is the job it was built for.

    What is asserted now holds on every day of a healthy window. PATCH-BOUNDARY:
    the row describes the shipped window, by its start date, so this still
    fires at a boundary until the row is updated as part of declaring the new
    window. DAILY, as invariants: the row's figure is a match count of this
    window recorded on some earlier day, so it can be no larger than the
    shipped count and its end no later than the shipped end. #109's own
    failure, a builds count reported as matches, is caught on any day by
    `test_the_derivation_counts_builds_and_every_item_agrees` and the label
    test above. `live_window.py` has the convention."""
    import re
    from smite import doc_audit
    state = (sbs.REPO_ROOT / "docs" / "STATE.md").read_text(encoding="utf-8")
    row = re.search(r"\|\s*Community sample\s*\|([^|]*)\|", state).group(1)
    table = json.loads(sbs.COMMUNITY_ITEMS_PATH.read_text(encoding="utf-8"))
    count, unit = sbs.community_sample(table)
    assert unit == "matches"
    doc = re.search(r"([\d,]+) (\w+)\+ Conquest matches, (\d+ \w+) – (\d+ \w+)", row)
    assert doc, row[:120]
    doc_count, _, doc_start, doc_end = doc.groups()
    assert doc_start == doc_audit._day(table["window_start"]), (
        f"STATE.md's Community sample row starts {doc_start}, the shipped window "
        f"{table['window_start']}: declare the new window and update the row")
    assert int(doc_count.replace(",", "")) <= count, (doc_count, count)
    # The row names day and month only. Read it in the window's own year,
    # rolling into the next for a window that crosses New Year.
    start = date.fromisoformat(table["window_start"])
    end = datetime.strptime(f"{doc_end} {start.year}", "%d %b %Y").date()
    if end < start:
        end = end.replace(year=start.year + 1)
    assert start <= end <= date.fromisoformat(table["window_end"]), (doc_end, table["window_end"])
