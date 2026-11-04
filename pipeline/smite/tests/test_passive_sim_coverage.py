"""The coverage pass: every `efficiency_pool` item's passive decided (the coverage pass, PR #104).

`passive_sim` covered 67 of the 193 scored items because that is all
`side_by_side`'s comparisons ever asked for. The other 84 read "no simulator
written yet" — a GAP, which is why PR #104 could not price passives inside
`efficiency` honestly: an absent item is zeroed by ABSENCE, which lowers its
predicted cost and makes it look more premium, so pricing from a partial table
replaces §4.31's asymmetry with a bigger one.

Each of the 84 now has a decision and a test. Every ARITHMETIC test reads the
TOY god from `test_side_by_side` (numbers chosen so the hand computation is one
line) and every READING test reads the item text frozen in
`fixtures/frozen/passive_coverage/items.json` on 2026-11-05 (Open Beta 46, the
same scrape `data/Items` carried that day). **Never regenerate that fixture to
make a test pass** — if the wiki text moves under a simulator, the frozen text
is what says so, and the simulator has to be re-read against the new text.

The refusals are tested as hard as the simulators, because three of their
reasons are measured properties of this clock rather than a shrug, and a later
session "fixing" one of them would be undoing a proof:

  * the enemy's attack speed (and its Strength) set a SCHEDULE, not a source
  * the enemy deals no critical strikes
  * Echo is an expected multiplier here, with no countable instance
"""
import json
from pathlib import Path

import pytest

from smite import combat, efficiency, passive_sim as ps, recommend, side_by_side as sbs
from smite.tests.test_side_by_side import item, target, toy_ability, toy_god

FROZEN = Path(__file__).resolve().parent / "fixtures" / "frozen" / "passive_coverage"


def frozen():
    return {it["name"]: it for it in json.loads((FROZEN / "items.json").read_text(encoding="utf-8"))}


def text(name):
    return frozen()[name]["passive"]


def sim(names, items, god=None, tgt=None, **kw):
    return sbs.Sim(god or toy_god(), names, items, tgt or target(), **kw)


def one(name, stats=None, **kw):
    """One item on the toy god, run for the whole window."""
    items = {name: item(name, stats, passive=text(name))}
    s = sim([name], items, **kw)
    s.run_window()
    return s


# ── The invariant this pass exists for ───────────────────────────────────

def test_no_scored_item_carries_a_passive_this_module_has_not_decided():
    """THE point of the pass. Every item `efficiency` scores either has a
    simulator, is explicitly refused, or has no passive text at all. Nothing
    reads "no simulator written yet", which is the status that cannot be
    priced honestly because absence is not a decision."""
    pool = efficiency.efficiency_pool(recommend.load_items())
    gaps = [it["name"] for it in pool
            if ps.lookup(it).status != ps.NO_PASSIVE and it["name"] not in ps.REGISTRY]
    assert gaps == []


def test_the_frozen_eighty_four_are_all_in_the_registry():
    missing = sorted(n for n in frozen() if n not in ps.REGISTRY)
    assert len(frozen()) == 84
    assert missing == []


def test_the_split_is_thirty_three_simulated_eight_partial_forty_three_refused():
    """The counts PR #104 reports. A refusal is a good outcome and these are not
    a target — but if the split moves, the entry that quotes it is stale."""
    got = {}
    for name in frozen():
        got[ps.REGISTRY[name].status] = got.get(ps.REGISTRY[name].status, 0) + 1
    assert got == {ps.SIMULATED: 33, ps.PARTIAL: 8, ps.NOT_SIMULATED: 43}


def test_every_refusal_states_a_reason_and_every_simulator_a_summary():
    for name, p in ((n, ps.REGISTRY[n]) for n in frozen()):
        assert p.summary, name
        if p.status in (ps.NOT_SIMULATED, ps.PARTIAL):
            assert p.assumptions, name


def test_a_partial_does_not_count_toward_coverage_and_a_simulated_one_does():
    """`simulated_share` counts SIMULATED and NO_PASSIVE only, so the eight
    PARTIAL entries still read as uncovered gold. That is deliberate: they get
    a VALUE for pricing and do not claim the clock models them whole."""
    items = {"Void Shield": item("Void Shield", cost=1000, passive=text("Void Shield")),
             "Agility Greaves": item("Agility Greaves", cost=1000, passive=text("Agility Greaves"))}
    assert sbs.simulated_share(["Void Shield"], items) == 1.0
    assert sbs.simulated_share(["Agility Greaves"], items) == 0.0


# ── Ability-hit damage ───────────────────────────────────────────────────

def test_ancient_signet_is_twenty_plus_twelve_per_level_once_in_fifteen_seconds():
    assert "+20 (+12 per Level) bonus Magical Damage" in text("Ancient Signet")
    assert "Cooldown: 15s" in text("Ancient Signet")
    s = one("Ancient Signet", god=toy_god([toy_ability(cooldown=4)]))
    # Casts at 0, 4, 8; the 15s cooldown lets only the first proc.
    assert s.by_item["Ancient Signet"] == pytest.approx(20.0 + 12.0 * 20)


def test_archmage_gem_reads_the_ampersand_as_both_terms():
    assert "40% of your Intelligence & 50% of your Strength" in text("Archmage's Gem")
    assert "+60 Strength or +90 Intelligence" in text("Archmage's Gem")
    s = one("Archmage's Gem", {"Strength": "10"}, god=toy_god([toy_ability(cooldown=4)]))
    # Adaptive picks Strength (10 item Strength beats 0 Intelligence): 70 total.
    assert s.stat("Strength") == pytest.approx(70.0)
    assert s.by_item["Archmage's Gem"] == pytest.approx(0.40 * 0.0 + 0.50 * 70.0)


def test_bluestone_reads_their_current_health_as_the_target_bar_in_this_fight():
    assert "7.5% of their current Health" in text("Bluestone Brooch")
    s = one("Bluestone Brooch", {"Strength": "10"},
            god=toy_god([toy_ability(damage=0, cooldown=20, scaling="0% Strength")]))
    # One cast at t=0, target at a full 2000 bar: 100 + 7.5% x 2000.
    assert s.by_item["Bluestone Brooch"] == pytest.approx(100.0 + 0.075 * 2000.0)


def test_bluestone_subsequent_hit_inside_three_seconds_is_half_again():
    assert "Subsequent hits on the same target: 50% bonus damage for 3s" in text("Bluestone Brooch")
    s = sim(["Bluestone Brooch"], {"Bluestone Brooch": item("Bluestone Brooch", {"Strength": "10"})})
    first, second, late = [sbs.Event(t, "ability", "Nuke", 0.0) for t in (0.0, 2.0, 9.0)]
    for ev in (first, second, late):
        ps._bluestone(s, ev)
    base = 100.0 + 0.075 * 2000.0
    assert first.procs[0][0] == pytest.approx(base)
    assert second.procs[0][0] == pytest.approx(1.5 * base)     # 2s after the first
    assert late.procs[0][0] == pytest.approx(base)             # 7s after: not subsequent


def test_gladiators_shield_reads_item_protections_like_golden_blade():
    assert "+10 + 40% of your Item Protections" in text("Gladiator's Shield")
    s = one("Gladiator's Shield", {"Physical Protection": "25", "Magical Protection": "15"},
            god=toy_god([toy_ability(cooldown=4)]))
    # Casts at 0, 4, 8 -> three procs of 10 + 40% x (25 + 15).
    assert s.by_item["Gladiator's Shield"] == pytest.approx(3 * (10.0 + 0.40 * 40.0))


def test_blood_soaked_shroud_heals_one_percent_of_max_health_per_ability():
    assert "+1% Max Health Heal" in text("Blood-soaked Shroud")
    assert "Max Mana" in text("Blood-soaked Shroud")   # the clause that is not modelled
    items = {"Blood-soaked Shroud": item("Blood-soaked Shroud", {"Strength": "10"})}
    s = sim(["Blood-soaked Shroud"], items, god=toy_god([toy_ability(cooldown=4)]))
    s.hp = s.max_health - 1000.0       # a full bar would overheal every tick away
    s.run_window()
    assert s.heal_by_item["Blood-soaked Shroud"] == pytest.approx(3 * 0.01 * 2000.0)


def test_oath_sworn_spear_is_a_flat_protection_reduction_not_a_percentage():
    assert "Physical Protection is reduced by 5 for 4s" in text("Oath-Sworn Spear")
    assert "caps at 20 total Physical Protection reduction" in text("Oath-Sworn Spear")
    s = one("Oath-Sworn Spear", {"Strength": "0"},
            god=toy_god([toy_ability(damage=100, cooldown=20, scaling="0% Strength")]),
            tgt=target(prot=100.0))
    # One cast at t=0 shreds 5 flat; the shred lands AFTER that hit, so the
    # swings from t=1 on meet 95 protection and the ability met 100.
    assert s.flat_shred_at(1.0, "physical") == pytest.approx(5.0)
    assert s.flat_shred_at(5.0, "physical") == pytest.approx(0.0)     # 4s duration
    assert s.shred_at(1.0) == pytest.approx(0.0)                      # not a percentage


def test_oath_sworn_growth_per_takedown_stops_at_twenty():
    s = sim(["Oath-Sworn Spear"], {"Oath-Sworn Spear": item("Oath-Sworn Spear")})
    for _ in range(40):
        ps._oath_sworn_takedown(s, "assist")
    assert s.state["Oath-Sworn Spear"]["points"] == pytest.approx(20.0)


def test_sundering_axe_is_true_damage_and_a_heal_on_one_eight_second_timer():
    assert "+150 (+10% of your Item Protections) Bonus True Damage +125 Heal" in text("Sundering Axe")
    assert "Cooldown: 8s" in text("Sundering Axe")
    items = {"Sundering Axe": item("Sundering Axe", {"Physical Protection": "30",
                                                     "Magical Protection": "30"})}
    s = sim(["Sundering Axe"], items, god=toy_god([toy_ability(cooldown=4)]))
    s.hp = s.max_health - 1000.0
    s.run_window()
    # The attack and ability channels share the timer, so it fires at t=0 and
    # t=8, never twice in one 8s span.
    assert s.by_item["Sundering Axe"] == pytest.approx(2 * (150.0 + 0.10 * 60.0))
    assert s.heal_by_item["Sundering Axe"] == pytest.approx(2 * 125.0)


# ── Attack-hit effects ──────────────────────────────────────────────────

def test_deaths_embrace_heals_and_refunds_a_third_of_a_second_per_swing():
    assert "+1% Max Health Heal +2% Max Mana Restore -0.33s Non Ultimate Cooldowns" in \
        text("Death's Embrace")
    items = {"Death's Embrace": item("Death's Embrace", {"Strength": "10"})}
    s = sim(["Death's Embrace"], items)
    s.hp = s.max_health - 1000.0
    s.run_window()
    assert s.heal_by_item["Death's Embrace"] == pytest.approx(10 * 0.01 * 2000.0)


def test_contagion_spends_its_stacks_on_an_attack_at_one_percent_of_our_max_health_each():
    assert "Deal Magical Damage = 1% Max Health per stack" in text("Contagion")
    items = {"Contagion": item("Contagion", {"Max Health": "0"})}
    s = sim(["Contagion"], items)
    for _ in range(3):
        ps._contagion_taken(s, {"raw": 1.0, "dtype": "physical", "kind": "attack"})
    assert s.state["Contagion"]["stacks"] == 3
    ev = sbs.Event(0.0, "attack", "Basic Attack", 0.0)
    ps._contagion_attack(s, ev)
    assert ev.procs[0][0] == pytest.approx(3 * 0.01 * 2000.0)
    assert s.state["Contagion"]["stacks"] == 0


def test_contagion_reads_the_enemy_lifesteal_clause_in_whole_hundreds():
    assert "If an enemy Lifesteals 100 Health from you: Apply +5 Stacks" in text("Contagion")
    s = sim(["Contagion"], {"Contagion": item("Contagion")})
    s.target_healed = 250.0
    ps._contagion_taken(s, {"raw": 1.0, "dtype": "physical", "kind": "attack"})
    assert s.state["Contagion"]["stacks"] == 1 + 5 * 2      # two whole hundreds
    ps._contagion_taken(s, {"raw": 1.0, "dtype": "physical", "kind": "attack"})
    assert s.state["Contagion"]["stacks"] == 12             # the same 250 is not re-counted


# ── Standing grants ─────────────────────────────────────────────────────

def test_tritons_conch_grants_only_our_own_half_of_the_aura():
    assert "You and allies within 8.8m: +5 (+0.5 per Level) Strength +5 (+1 per Level)" in \
        text("Triton's Conch")
    s = one("Triton's Conch", {"Strength": "25", "Intelligence": "40"})
    # Printed 25/40 plus the passive's 5 + 0.5x20 = 15 and 5 + 1x20 = 25.
    assert s.stat("Strength") == pytest.approx(40.0)
    assert s.stat("Intelligence") == pytest.approx(65.0)


def test_shoguns_ofuda_twenty_percent_is_on_top_of_its_printed_fifteen():
    assert "+20% Attack Speed for you and allies within 8.8m" in text("Shogun's Ofuda")
    assert frozen()["Shogun's Ofuda"]["stats"]["Attack Speed"] == "15%"
    s = one("Shogun's Ofuda", {"Attack Speed": "15%"})
    assert s.stat("Attack Speed %") == pytest.approx(35.0)


def test_hunters_cowl_takes_the_near_a_god_branch_because_the_target_always_is():
    assert "Within 8.8m of a God: +30% Attack Speed, +5% Lifesteal" in text("Hunter's Cowl")
    assert "Alone:" in text("Hunter's Cowl")
    s = one("Hunter's Cowl", {"Strength": "10", "Lifesteal": "5%"})
    assert s.stat("Attack Speed %") == pytest.approx(30.0)
    assert s.stat("Lifesteal %") == pytest.approx(10.0)      # printed 5 + the passive's 5
    assert s.stat("Strength") == pytest.approx(65.0)         # 10 printed + adaptive 55


def test_pendulum_of_the_ages_reads_full_mana_as_ten_steps():
    assert "+3 Strength or +7 Intelligence (based on highest item stat) per 10% of available Mana" in \
        text("Pendulum of the Ages")
    s = one("Pendulum of the Ages", {"Intelligence": "10"})
    # Intelligence is the highest item stat: 45 + 10 x 7 = 115 on top of 10.
    assert s.stat("Intelligence") == pytest.approx(10.0 + 70.0 + 70.0)


def test_adamantine_sickle_reads_the_fights_health_bar():
    assert "While Below 50% Health: +10 Strength" in text("Adamantine Sickle")
    items = {"Adamantine Sickle": item("Adamantine Sickle", {"Strength": "10"})}
    s = sim(["Adamantine Sickle"], items)
    assert s.stat("Strength") == pytest.approx(10.0)         # full bar: nothing
    s.hp = 0.49 * s.max_health
    assert s.stat("Strength") == pytest.approx(20.0)


def test_oni_hunters_garb_reads_one_enemy_god_as_one_stack():
    assert "For each enemy god within 8.8m: +4% Damage Mitigation Max 3 stacks" in \
        text("Oni Hunter's Garb")
    s = sim(["Oni Hunter's Garb"], {"Oni Hunter's Garb": item("Oni Hunter's Garb")})
    assert ps._oni_reduce(s, {"raw": 100.0, "dtype": "physical", "kind": "attack"}) == \
        pytest.approx(0.96)


def test_talisman_of_purification_is_shell_of_rebukes_clause_at_the_same_rate():
    assert "+7.5% of all Stats from Items" in text("Talisman of Purification")
    s = one("Talisman of Purification", {"Strength": "100", "Max Health": "200"})
    assert s.stat("Strength") == pytest.approx(107.5)
    assert s.stat("Max Health") == pytest.approx(215.0)


# ── Auras and per-second effects ────────────────────────────────────────

def test_mystical_mail_ticks_once_a_second_at_the_unscaled_number():
    assert "15 (+1 per Level) Magical Damage" in text("Mystical Mail")
    assert "+50% at Close Range -50% at Maximum Range" in text("Mystical Mail")
    s = one("Mystical Mail", {"Max Health": "0"})
    # Whole seconds 1..10 inclusive, as the aura slot already ticked for
    # Sanguine Lash: 10 ticks of 15 + 1 x 20.
    assert s.by_item["Mystical Mail"] == pytest.approx(10 * 35.0)


def test_void_shield_and_void_stone_shred_only_their_own_protection_type():
    assert "-10% Physical Protection" in text("Void Shield")
    assert "-10% Magical Protection" in text("Void Stone")
    items = {"Void Shield": item("Void Shield", {"Physical Protection": "55"}),
             "Void Stone": item("Void Stone", {"Magical Protection": "60"})}
    s = sim(["Void Shield"], items, tgt=target(prot=100.0))
    assert s.aura_shred == {"physical": 0.10}
    # A physical god against 100 protection now meets 90.
    assert s.mitigated(100.0, "physical", 0.0, kind="attack") == \
        pytest.approx(100.0 * combat.mitigation(90.0))
    assert s.mitigated(100.0, "magical", 0.0, kind="ability") == \
        pytest.approx(100.0 * combat.mitigation(100.0))
    assert sim(["Void Stone"], items).aura_shred == {"magical": 0.10}


def test_an_aura_shred_holds_in_the_burst_too_because_the_target_is_always_in_range():
    items = {"Void Shield": item("Void Shield", {"Physical Protection": "0"})}
    s = sim(["Void Shield"], items, god=toy_god([toy_ability(cooldown=4)]), tgt=target(prot=100.0))
    burst = s.run_burst()
    plain = sim(["Plain"], {"Plain": item("Plain", {"Physical Protection": "0"})},
                god=toy_god([toy_ability(cooldown=4)]), tgt=target(prot=100.0)).run_burst()
    assert burst > plain


def test_yogis_necklace_heals_half_a_percent_of_max_health_each_second():
    assert "Heal +0.5% of your Max Health per second" in text("Yogi's Necklace")
    items = {"Yogi's Necklace": item("Yogi's Necklace", {"Max Health": "0"})}
    s = sim(["Yogi's Necklace"], items)
    s.hp = s.max_health - 1000.0
    s.run_window()
    assert s.heal_by_item["Yogi's Necklace"] == pytest.approx(10 * 0.005 * 2000.0)


def test_sphere_of_negation_grants_two_percent_every_three_seconds_up_to_fourteen():
    assert "+2% Max Health Magical Shield every 3s, up to a maximum of +14% Max Health" in \
        text("Sphere of Negation")
    items = {"Sphere of Negation": item("Sphere of Negation", {"Max Health": "0"})}
    s = sim(["Sphere of Negation"], items)
    s.run_window()
    # Whole seconds 3, 6, 9 inside a 10s window: three grants of 2%.
    assert s.state["Sphere of Negation"]["granted"] == pytest.approx(0.06)
    assert s.shields["Sphere of Negation"][0] == pytest.approx(0.06 * 2000.0)


def test_sphere_of_negation_stops_at_the_stated_cap():
    items = {"Sphere of Negation": item("Sphere of Negation", {"Max Health": "0"})}
    s = sim(["Sphere of Negation"], items)
    for t in range(3, 100, 3):
        s.t = float(t)
        ps._sphere(s, float(t))
    assert s.state["Sphere of Negation"]["granted"] == pytest.approx(0.14)


# ── Hits taken ──────────────────────────────────────────────────────────

def test_helm_of_radiance_stacks_only_on_physical_damage_and_caps_at_four():
    assert "Take Physical Damage: +7 Physical Protection for 6s. Stacks up to 4 times" in \
        text("Helm of Radiance")
    s = sim(["Helm of Radiance"], {"Helm of Radiance": item("Helm of Radiance")})
    for _ in range(6):
        ps._helm_radiance_taken(s, {"raw": 1.0, "dtype": "physical", "kind": "attack"})
    assert ps._helm_radiance_prot(s, "physical") == pytest.approx(28.0)   # 4 x 7
    assert ps._helm_radiance_prot(s, "magical") == pytest.approx(0.0)
    ps._helm_radiance_taken(s, {"raw": 1.0, "dtype": "magical", "kind": "ability"})
    assert ps._helm_radiance_prot(s, "magical") == pytest.approx(0.0)


def test_leviathans_hide_refunds_half_a_second_once_per_ten():
    assert "Damaged by Enemy God: -0.5s once per Ability Cast or Attack. Cooldown: 10s." in \
        text("Leviathan's Hide")
    s = sim(["Leviathan's Hide"], {"Leviathan's Hide": item("Leviathan's Hide")},
            god=toy_god([toy_ability(cooldown=8)]))
    s.nxt = {0: 8.0}
    s.t = 1.0
    ps._leviathan_taken(s, {"raw": 1.0, "dtype": "physical", "kind": "attack"})
    assert s.nxt[0] == pytest.approx(7.5)
    s.t = 2.0
    ps._leviathan_taken(s, {"raw": 1.0, "dtype": "physical", "kind": "attack"})
    assert s.nxt[0] == pytest.approx(7.5)      # still inside the 10s cooldown


# ── Takedowns ───────────────────────────────────────────────────────────

def test_necronomicon_is_thirty_intelligence_per_takedown_to_six():
    assert "+1 Stack of: +30 Intelligence Stacks up to 6 times" in text("Necronomicon")
    s = sim(["Necronomicon"], {"Necronomicon": item("Necronomicon", {"Intelligence": "50"})})
    for _ in range(9):
        ps._necronomicon(s, "assist")
    assert s.stat("Intelligence") == pytest.approx(50.0 + 6 * 30.0)


def test_odigba_pays_five_percent_of_max_health_by_the_second():
    assert "God Kill or Assist: Heal +5% Max Health over 6s" in text("Odigba")
    items = {"Odigba": item("Odigba", {"Max Health": "0"})}
    s = sim(["Odigba"], items)
    s.hp, s.t = s.max_health - 1000.0, 0.0
    ps._odigba_takedown(s, "assist")
    for t in range(1, 11):
        ps._odigba_tick(s, float(t))
    # Live for 6s from t=0, so ticks 1..6 pay a sixth of 5% each.
    assert s.heal_by_item["Odigba"] == pytest.approx(6 * 0.05 * 2000.0 / 6.0)


# ── Our own ability healed us ───────────────────────────────────────────

def test_daybreak_gavel_stacks_on_a_healing_cast_and_spends_them_on_a_plain_one():
    assert "Healed yourself with a Healing Ability: +1 Stack (max 3)" in text("Daybreak Gavel")
    assert "+10 Strength or +15 Intelligence (based on highest item stat) for 8s per Stack" in \
        text("Daybreak Gavel")
    items = {"Daybreak Gavel": item("Daybreak Gavel", {"Strength": "10"})}
    s = sim(["Daybreak Gavel"], items, god=toy_god([toy_ability(cooldown=4)]))
    for _ in range(4):
        ps._daybreak_heal(s, "Mend")
    assert s.state["Daybreak Gavel"]["stacks"] == 3       # the stated cap
    s.t = 0.0
    ps._daybreak_ability(s, sbs.Event(0.0, "ability", "Nuke", 0.0))
    assert s.stat("Strength") == pytest.approx(10.0 + 40.0 + 3 * 10.0)
    s.t = 9.0
    assert s.stat("Strength") == pytest.approx(50.0)      # the 8s buff has gone


def test_daybreak_gavel_does_not_spend_its_stacks_on_a_healing_ability():
    items = {"Daybreak Gavel": item("Daybreak Gavel", {"Strength": "10"})}
    s = sim(["Daybreak Gavel"], items, god=toy_god([toy_ability(cooldown=4)]))
    s.self_heals = {"Nuke": {}}
    ps._daybreak_heal(s, "Nuke")
    ps._daybreak_ability(s, sbs.Event(0.0, "ability", "Nuke", 0.0))
    assert s.state["Daybreak Gavel"]["stacks"] == 1
    assert not s.state["Daybreak Gavel"]["buff"]


def test_vital_amplifier_reads_the_melee_branch_for_a_melee_god():
    assert "+7.5% Attack Speed +5% Attack Damage (Ranged) +10% Attack Damage (Melee)" in \
        text("Vital Amplifier")
    items = {"Vital Amplifier": item("Vital Amplifier", {"Attack Damage": "100"})}
    for melee, pct in ((True, 0.10), (False, 0.05)):
        s = sim(["Vital Amplifier"], items, god=toy_god(melee=melee))
        ps._vital_heal(s, "Mend")
        ps._vital_heal(s, "Mend")
        assert s.stat("Attack Speed %") == pytest.approx(2 * 7.5)
        assert s.stat("Attack Damage") == pytest.approx(100.0 * (1.0 + 2 * pct))


def test_regrowth_striders_heals_through_the_movement_buff_it_grants_itself():
    assert "Gain any Movement Speed buff: +5% Health Heal over 10s" in text("Regrowth Striders")
    items = {"Regrowth Striders": item("Regrowth Striders", {"Physical Protection": "45"})}
    s = sim(["Regrowth Striders"], items)
    s.hp, s.t = s.max_health - 1000.0, 0.0
    ps._regrowth_heal(s, "Mend")
    for t in range(1, 11):
        ps._regrowth_tick(s, float(t))
    assert s.heal_by_item["Regrowth Striders"] == pytest.approx(10 * 0.05 * 2000.0 / 10.0)


# ── Damage dealt ────────────────────────────────────────────────────────

def test_prophetic_cloak_stacks_once_every_five_seconds_and_evolves_at_fifteen():
    assert "Damage a God: +1 Protection Stack against the damage type they deal. Cooldown: 5s." in \
        text("Prophetic Cloak")
    assert "+6% Damage Mitigation (or +12% if total Protections > 300)" in text("Prophetic Cloak")
    s = sim(["Prophetic Cloak"], {"Prophetic Cloak": item("Prophetic Cloak")})
    hit = {"raw": 100.0, "dtype": "physical", "kind": "attack"}
    assert ps._prophetic_reduce(s, hit) == pytest.approx(1.0)        # not evolved
    for k in range(20):
        ps._prophetic_hit(s, sbs.Event(float(k), "attack", "Basic Attack", 0.0))
    assert s.state["Prophetic Cloak"]["stacks"] == pytest.approx(15.0)
    assert ps._prophetic_prot(s, "physical") == pytest.approx(25.0)   # 15 stacks + the 10
    assert ps._prophetic_reduce(s, hit) == pytest.approx(1.0 - 0.06)


def test_prophetic_cloak_reads_twelve_percent_over_three_hundred_protections():
    items = {"Prophetic Cloak": item("Prophetic Cloak", {"Physical Protection": "200",
                                                         "Magical Protection": "200"})}
    s = sim(["Prophetic Cloak"], items)
    s.item_state("Prophetic Cloak", stacks=0.0)["stacks"] = 15.0
    assert ps._prophetic_reduce(s, {"raw": 1.0, "dtype": "physical", "kind": "attack"}) == \
        pytest.approx(1.0 - 0.12)


def test_prophetic_cloak_shares_one_five_second_timer_across_both_channels():
    s = sim(["Prophetic Cloak"], {"Prophetic Cloak": item("Prophetic Cloak")})
    ps.REGISTRY["Prophetic Cloak"].on_attack(s, sbs.Event(0.0, "attack", "Basic Attack", 0.0))
    ps.REGISTRY["Prophetic Cloak"].on_ability(s, sbs.Event(1.0, "ability", "Nuke", 0.0))
    assert s.state["Prophetic Cloak"]["stacks"] == pytest.approx(1.0)


# ── Actives ─────────────────────────────────────────────────────────────

def test_arondight_pays_once_per_reveal():
    assert "First time you damage a revealed God: +50 (+50% Strength) Physical Damage" in \
        text("Arondight")
    s = one("Arondight", {"Strength": "100"}, god=toy_god([toy_ability(cooldown=4)]))
    # Pressed at t=0, 60s cooldown, so one reveal and one payment in the window.
    assert s.by_item["Arondight"] == pytest.approx(50.0 + 0.50 * 100.0)


def test_glorious_pridwen_explodes_twice_and_shields_in_between():
    assert "Deal Magical Damage (40% of Protections)" in text("Glorious Pridwen")
    assert "Gain a Shield (125% of Protections) for 5s" in text("Glorious Pridwen")
    assert "Explode again: Deal Magic Damage (70% of your Protections)" in text("Glorious Pridwen")
    s = one("Glorious Pridwen", {"Physical Protection": "20", "Magical Protection": "20"})
    # Toy god carries no base protection: 40 total, both explosions off it.
    assert s.by_item["Glorious Pridwen"] == pytest.approx((0.40 + 0.70) * 40.0)
    assert s.state["Glorious Pridwen"]["prot"] == pytest.approx(40.0)


def test_phoenix_feather_takes_the_literal_reading_of_an_unmarked_number():
    assert "Heal = +75 Health +7.5 Missing Health" in text("Phoenix Feather")
    assert "True Damage = +3% Max Health from Items" in text("Phoenix Feather")
    items = {"Phoenix Feather": item("Phoenix Feather", {"Max Health": "300"})}
    s = sim(["Phoenix Feather"], items)
    s.hp = s.max_health - 1000.0
    s.run_window()
    assert s.heal_by_item["Phoenix Feather"] == pytest.approx(3 * (75.0 + 7.5))
    assert s.by_item["Phoenix Feather"] == pytest.approx(3 * 0.03 * 300.0)


def test_staff_of_myrddin_makes_the_next_non_ultimate_cast_free():
    assert "Next non-Ultimate Ability used will have no cooldown" in text("Staff of Myrddin")
    god = toy_god([toy_ability(name="Nuke", damage=100, cooldown=9)])
    items = {"Staff of Myrddin": item("Staff of Myrddin", {"Intelligence": "0"})}
    plain = sim(["Plain"], {"Plain": item("Plain", {"Intelligence": "0"})}, god=god)
    plain.run_window()
    s = sim(["Staff of Myrddin"], items, god=god)
    s.run_window()
    # A 9s cooldown fits one cast in 10s; the free cast buys a second.
    assert [n for _, n in plain.casts] == ["Nuke", "Nuke"]
    assert len(s.casts) > len(plain.casts)


def test_staff_of_myrddin_never_frees_an_ultimate():
    god = toy_god([toy_ability(name="Big", damage=100, cooldown=9, ult=True)])
    items = {"Staff of Myrddin": item("Staff of Myrddin")}
    s = sim(["Staff of Myrddin"], items, god=god)
    s.run_window()
    assert s._free_cast or len(s.casts) == 2


def test_screeching_gargoyle_shreds_ten_percent_and_leaves_the_silence_alone():
    assert "Silenced for 1s -10% Protections for 4s" in text("Screeching Gargoyle")
    s = one("Screeching Gargoyle", {"Magical Protection": "50"}, tgt=target(prot=100.0))
    assert s.shred_at(1.0) == pytest.approx(0.10)
    assert s.shred_at(5.0) == pytest.approx(0.0)


def test_lifebinder_deals_its_projectile_and_nothing_for_the_ally_half():
    assert "deals 60 (+8 per Level) Magic Damage" in text("Lifebinder")
    assert "First ally to damage a Marked target" in text("Lifebinder")
    s = one("Lifebinder", {"Intelligence": "40"})
    # Pressed at t=0 and every 20s: once in a 10s window.
    assert s.by_item["Lifebinder"] == pytest.approx(60.0 + 8.0 * 20)


def test_bumba_hammer_pays_the_cooldown_and_heal_clause_not_the_splash():
    assert "Next Attack deals +60 True Damage to enemies within 1.92m of the target" in \
        text("Bumba's Hammer")
    assert "Hit this Attack: -0.66s Cooldowns, +60 Heal" in text("Bumba's Hammer")
    items = {"Bumba's Hammer": item("Bumba's Hammer", {"Strength": "10"})}
    s = sim(["Bumba's Hammer"], items, god=toy_god([toy_ability(cooldown=4)]))
    s.hp = s.max_health - 1000.0
    s.run_window()
    assert s.heal_by_item["Bumba's Hammer"] == pytest.approx(3 * 60.0)
    assert "Bumba's Hammer" not in s.by_item       # the splash has no second enemy


# ── PARTIAL: the simulated half, and the named missing one ──────────────

def test_agility_greaves_is_shells_clause_and_the_dash_is_not_simulated():
    assert "+7.5% of all Stats from Items" in text("Agility Greaves")
    assert "On Use: Dash" in text("Agility Greaves")
    assert ps.REGISTRY["Agility Greaves"].status == ps.PARTIAL
    s = one("Agility Greaves", {"Strength": "100"})
    assert s.stat("Strength") == pytest.approx(107.5)


def test_time_lock_aegis_is_six_percent_and_the_stasis_is_not_simulated():
    assert "+6% of all Stats from Items" in text("Time-lock Aegis")
    assert ps.REGISTRY["Time-lock Aegis"].status == ps.PARTIAL
    s = one("Time-lock Aegis", {"Strength": "100"})
    assert s.stat("Strength") == pytest.approx(106.0)


def test_dwarven_plate_grants_the_printed_orientation_on_top_of_its_stats():
    assert "+15 Physical Protections +35 Magical Protections" in text("Dwarven Plate")
    assert frozen()["Dwarven Plate"]["stats"] == {"Physical Protection": "35",
                                                  "Magical Protection": "35"}
    s = one("Dwarven Plate", {"Physical Protection": "35", "Magical Protection": "35"})
    assert s.stat("Physical Protection") == pytest.approx(50.0)
    assert s.stat("Magical Protection") == pytest.approx(70.0)


@pytest.mark.parametrize("name,strength,intelligence", [
    ("Mercury's Talaria", 40.0, 70.0),
    ("Bumba's Spear", 35.0, 60.0),
])
def test_a_partial_still_pays_its_adaptive_clause(name, strength, intelligence):
    assert ps.REGISTRY[name].status == ps.PARTIAL
    s = one(name, {"Strength": "10"})
    assert s.stat("Strength") == pytest.approx(10.0 + strength)
    s = one(name, {"Intelligence": "10"})
    assert s.stat("Intelligence") == pytest.approx(10.0 + intelligence)


# ── The refusals, and the three measured reasons behind them ────────────

@pytest.mark.parametrize("name", [
    "Gem of Focus", "Kopesh", "Damaru", "Helm of Darkness", "Ragnarok's Wake",
    "Circe's Hexstone", "Sharpshooter's Arrow"])
def test_movement_and_distance_refusals_say_so(name):
    p = ps.REGISTRY[name]
    assert p.status == ps.NOT_SIMULATED
    assert any("movement" in a or "distance" in a for a in p.assumptions), p.assumptions


@pytest.mark.parametrize("name", [
    "Ancile", "Caestus", "Jade Scepter", "Resolute Mantle", "Ring of Dispel",
    "Scepter of Dominion", "Shroud of Vengeance", "Spirit Robe", "Stone of Binding",
    "Mantle Of Discord"])
def test_crowd_control_refusals_match_magis_cloaks_reason(name):
    p = ps.REGISTRY[name]
    assert p.status == ps.NOT_SIMULATED
    assert any("crowd control" in a for a in p.assumptions), p.assumptions


@pytest.mark.parametrize("name", [
    "Chandra's Grace", "Eros' Bow", "Heartwood Charm", "Lotus Sickle", "Radiant Bulwark",
    "Rod of Asclepius", "Soul Locket", "Umbral Link", "Heroism", "War Banner"])
def test_ally_refusals_match_doublet_of_bindings_reason(name):
    p = ps.REGISTRY[name]
    assert p.status == ps.NOT_SIMULATED
    assert any("no ally" in a or "contains no ally" in a for a in p.assumptions), p.assumptions


@pytest.mark.parametrize("name", ["Infused Axe", "Oracle Staff"])
def test_mana_only_passives_are_refused_and_cite_the_mana_refusal(name):
    p = ps.REGISTRY[name]
    assert p.status == ps.NOT_SIMULATED
    assert any("mana" in a and "§4.16" in a for a in p.assumptions), p.assumptions


@pytest.mark.parametrize("name", [
    "Eye of the Storm", "Omen Drum", "The Cosmic Horror", "Totem of Death"])
def test_echo_items_are_refused_because_echo_is_an_expectation_here(name):
    p = ps.REGISTRY[name]
    assert p.status == ps.NOT_SIMULATED
    assert any("echo_multiplier" in a for a in p.assumptions), p.assumptions
    assert "Each time you Echo" in text(name) or "each time you Echo" in text(name).lower()


def test_echo_really_is_an_expected_multiplier_with_no_countable_instance():
    """The reason those four are refused, held as a fact rather than a claim:
    `combat.echo_multiplier` is linear in the stat, so there is no Echo EVENT
    for "each time you Echo" to count."""
    assert combat.echo_multiplier(0.0) == pytest.approx(1.0)
    assert combat.echo_multiplier(30.0) > 1.0
    assert combat.echo_multiplier(60.0) - 1.0 == pytest.approx(2 * (combat.echo_multiplier(30.0) - 1.0))
    gods = {g["name"]: g for g in recommend.load_gods()}
    for name in ("Ix Chel", "Nut"):
        rotation, _ = sbs.bq.ability_rotation(gods[name])
        assert not any("echo" in a["name"].lower() for a in rotation)


def test_the_enemys_cadence_is_a_schedule_not_a_source_of_damage():
    """Midgardian Mail and Pharaoh's Curse are refused on this. The attacker's
    raw damage per hit is `raw_dps x share x step`, so halving the interval
    halves each hit: a debuff on the enemy's attack speed cannot move any
    damage in this comparison."""
    prof = {"raw_dps": {"physical": 100.0, "magical": 100.0},
            "interval": {"attack": 1.0, "ability": 1.0}, "anti_heal": 0.0}
    items = {"Plain": item("Plain", {"Strength": "0"})}
    totals = []
    for step in (1.0, 0.5):
        prof["interval"] = {"attack": step, "ability": step}
        s = sim(["Plain"], items, tgt=target(attacker=dict(prof)), enemy="physical")
        s.run_window()
        totals.append(s.absorbed)
    assert totals[0] == pytest.approx(totals[1])


def test_nothing_on_the_enemy_profile_crits():
    """Spectral Armor's whole passive reads the enemy's critical strikes."""
    assert "You take -30% Damage from Critical Strikes" in text("Spectral Armor")
    prof = {"raw_dps": {"physical": 100.0, "magical": 100.0},
            "interval": {"attack": 1.0, "ability": 1.0}, "anti_heal": 0.0}
    s = sim(["Plain"], {"Plain": item("Plain")}, tgt=target(attacker=prof), enemy="physical")
    assert "crit" not in json.dumps(s.target["attacker"])
    assert ps.REGISTRY["Spectral Armor"].status == ps.NOT_SIMULATED


@pytest.mark.parametrize("name", ["Wyrmskin Hide", "Mantle Of Discord", "Alchemist Coat"])
def test_our_own_dampening_is_refused_on_the_register_entry_that_measured_it(name):
    p = ps.REGISTRY[name]
    assert p.status == ps.NOT_SIMULATED
    assert any("§4.19" in a for a in p.assumptions), p.assumptions
    assert "Dampening" in ("Plating", "Dampening") and \
        "Dampening" in __import__("smite.build_quality", fromlist=["x"]).TARGET_SIDE_ONLY


@pytest.mark.parametrize("name", ["Ashwhorl Acorn", "Briskberry Acorn", "Thistlethorn Acorn"])
def test_the_acorns_are_refused_and_their_stat_lines_are_already_counted(name):
    p = ps.REGISTRY[name]
    assert p.status == ps.NOT_SIMULATED
    assert any("ability's shape" in a for a in p.assumptions), p.assumptions
    # "Non-Aspect: 45 Strength ..." in the passive text is the printed stat
    # block restated, so granting it would double count.
    assert frozen()[name]["stats"]["Strength"] == "45"
    assert "45 Strength" in text(name) or "Non-Aspect" in text(name)


def test_xibalban_effigy_is_refused_whole_rather_than_credited_with_its_good_half():
    """The PR #104 failure mode pointing the other way: `reduce_hit` would
    simulate the 50% cut in two lines, and the clock has no channel for the
    payback, so the item would be booked with its upside alone."""
    assert "Take 50% Damage for 4s" in text("Xibalban Effigy")
    assert "After: Take Physical Damage equal to mitigated Damage" in text("Xibalban Effigy")
    p = ps.REGISTRY["Xibalban Effigy"]
    assert p.status == ps.NOT_SIMULATED
    assert p.reduce_hit is None
    assert any("damaging itself" in a for a in p.assumptions), p.assumptions


def test_typhons_heart_is_refused_for_the_summon_and_the_minions():
    name = next(n for n in frozen() if n.startswith("Typhon"))
    p = ps.REGISTRY[name]
    assert p.status == ps.NOT_SIMULATED
    assert any("summons" in a for a in p.assumptions), p.assumptions


# ── The new channels are identities when no new item is held ────────────

def test_the_flat_and_aura_shred_channels_read_zero_for_a_build_without_them():
    """The one thing that must not have changed: `mitigated` for every build
    that holds none of these items."""
    items = {"Plain": item("Plain", {"Strength": "10"})}
    s = sim(["Plain"], items, tgt=target(prot=100.0))
    assert s.aura_shred == {} and s.flat_shreds == {}
    assert s.flat_shred_at(0.0, "physical") == 0.0
    assert s.mitigated(100.0, "physical", 0.0, kind="attack") == \
        pytest.approx(100.0 * combat.mitigation(100.0))


def test_a_tick_hook_fires_once_per_whole_second_even_under_sanguines_fast_aura():
    """Sanguine Lash's active drives the same slot every 0.33s. An item whose
    text says "per 1s" must not tick three times inside one second."""
    items = {"Sanguine Lash": item("Sanguine Lash", {"Lifesteal": "0%"},
                                   passive="Enemy gods Within 4m"),
             "Mystical Mail": item("Mystical Mail", {"Max Health": "0"},
                                   passive=text("Mystical Mail"))}
    s = sim(["Sanguine Lash", "Mystical Mail"], items)
    s.run_window()
    assert s.by_item["Mystical Mail"] == pytest.approx(10 * 35.0)


def test_a_self_heal_hook_sees_the_gods_own_ability_and_not_lifesteal():
    """`on_self_heal` is fired from the two `ability_heals` sites only, so
    lifesteal and item heals cannot stack Daybreak Gavel or Vital Amplifier."""
    items = {"Daybreak Gavel": item("Daybreak Gavel", {"Strength": "10", "Lifesteal": "25%"})}
    s = sim(["Daybreak Gavel"], items)
    s.hp = s.max_health - 1000.0
    s.run_window()
    assert s.healed > 0                                      # lifesteal did heal
    assert not s.state.get("Daybreak Gavel", {}).get("stacks")
