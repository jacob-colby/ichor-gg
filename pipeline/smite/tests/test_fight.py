"""The side-by-side's FIGHT block: takedowns, an enemy on our god, actives,
and the game clock for stacks (2026-11-02).

Every expected number is hand-computed from a TOY god (81 attack power, 1.0
swings/s, 2000 health, no protection — `test_side_by_side.toy_god`) and the
item TEXT frozen in `fixtures/frozen/side_by_side/` (`items.json` from PR #77,
`fight_items.json` for the actives it did not hold, 2026-11-03). Each test
that relies on a text asserts the clause it reads first, so a wiki change
shows up as a text failure rather than as a silently different number.
"""
import json
from pathlib import Path

import pytest

from smite import passive_sim as ps, side_by_side as sbs
from smite.tests.test_side_by_side import FROZEN, frozen_items, item, target, toy_ability, toy_god

TESTS = Path(__file__).resolve().parent


def fight_items():
    return {it["name"]: it for it in
            json.loads((FROZEN / "fight_items.json").read_text(encoding="utf-8"))}


def armed(t, phys_dps=0.0, mag_dps=0.0, attack_every=1.0, ability_every=2.0):
    """A toy target that hits back: raw DPS per type and the two cadences."""
    t = dict(t)
    t["attacker"] = {"raw_dps": {"physical": phys_dps, "magical": mag_dps},
                     "interval": {"attack": attack_every, "ability": ability_every},
                     "n": {"attack": 1, "ability": 1}}
    return t


def text(name):
    items = dict(frozen_items(), **fight_items())
    return items[name]["passive"]


# ── Takedowns ─────────────────────────────────────────────────────────────

def test_a_kill_is_the_hit_that_reaches_max_health_and_only_one_per_fight():
    # 81 a swing at t = 0, 1, 2 ...: 405 >= 400 on the fifth swing (t=4).
    # 810 in the window is two max healths, but one fight has one target.
    s = sbs.Sim(toy_god(), [], {}, target(base_health=400.0))
    s.run_window()
    assert s.kill_times == [4.0] and s.kills == 1


def test_a_longer_run_is_consecutive_fights_each_with_one_kill_and_an_assist():
    s = sbs.Sim(toy_god(), [], {}, target(base_health=400.0), window=30.0)
    s.run_window()
    assert s.kill_times == [4.0, 14.0, 24.0]
    assert s.assists == 3          # at 5, 15, 25 (ASSIST_FIRST, ASSIST_INTERVAL)


def test_a_burst_has_no_takedowns():
    s = sbs.Sim(toy_god(), [], {}, target(base_health=50.0), window=None)
    s.run_burst()
    assert s.kills == 0 and s.assists == 0


def test_jotunns_assist_takes_one_second_off_and_five_off_the_ultimate():
    assert "-1s Cooldown for Non-Ultimate Abilities -5s Cooldown for Ultimate" in text("Jotunn's Revenge")
    god = toy_god([toy_ability(cooldown=6), toy_ability(name="Ult", cooldown=90, ult=True)])
    items = {"Jotunn's Revenge": item("Jotunn's Revenge")}
    s = sbs.Sim(god, ["Jotunn's Revenge"], items, target(base_health=1e6))
    s.run_window()
    # Assist at 5: the 6s ability (due at 6) comes up at 5; the ult 90 -> 85.
    assert [t for t, n in s.casts if n == "Nuke"] == [0.0, 5.0]
    assert s.nxt[1] == pytest.approx(85.0)
    off = sbs.Sim(god, ["Jotunn's Revenge"], items, target(base_health=1e6), disabled={"Jotunn's Revenge"})
    off.run_window()
    assert [t for t, n in off.casts if n == "Nuke"] == [0.0, 6.0]


def test_spear_of_desolation_pays_three_on_a_kill_and_one_and_a_half_on_an_assist():
    assert "God Kill: -3s Non Ultimate Cooldowns" in text("Spear of Desolation")
    assert "God Assist: -1.5s Non Ultimate Cooldowns" in text("Spear of Desolation")
    god = toy_god([toy_ability(damage=100, cooldown=8)])
    items = {"Spear of Desolation": item("Spear of Desolation")}
    # t=0: Nuke 100 + 0.5 x 10 = 105, then the swing 81 + 10 = 91: 196 >= 150,
    # a kill at t=0 -> the Nuke (due 8) is due at 5. Cast at 5 (abilities
    # resolve before the assist at the same instant), due 13; assist -> 11.5.
    s = sbs.Sim(god, ["Spear of Desolation"], items, target(base_health=150.0))
    s.run_window()
    assert s.kill_times == [0.0]
    assert [t for t, _ in s.casts] == [0.0, 5.0]
    assert s.nxt[0] == pytest.approx(11.5)


def test_timed_stacks_fall_off_one_at_a_time():
    st = {"stacks": 5, "expires": 10.0}
    assert ps.timed_stacks(st, 9.9, 10.0) == 5
    assert ps.timed_stacks(st, 10.0, 10.0) == 4 and st["expires"] == 20.0
    assert ps.timed_stacks(st, 25.0, 10.0) == 3


def test_doom_orb_gives_forty_intelligence_for_ten_seconds_then_decays():
    assert "Kill or Assist a God: +5 Stacks. Per Stack: +8 Intelligence Max 5 Stacks" in text("Doom Orb")
    items = {"Doom Orb": item("Doom Orb", {"Intelligence": "70"})}
    s = sbs.Sim(toy_god(), ["Doom Orb"], items, target())
    assert s.stat("Intelligence") == 70.0
    s._takedown("assist")
    assert s.stat("Intelligence") == 110.0
    s.t = 10.0
    assert s.stat("Intelligence") == 102.0


def test_rage_counts_earlier_fights_on_the_game_clock_then_window_takedowns():
    assert "+4% Critical Strike Chance (Max 20%) After 5 God Kills or Assists: +10%" in text("Rage")
    assert [ps.rage_crit(n) for n in (0, 1, 4, 5, 9)] == [0.0, 4.0, 16.0, 30.0, 30.0]
    items = {"Rage": item("Rage", {"Critical Chance": "20%"})}
    s = sbs.Sim(toy_god(), ["Rage"], items, target(), stacks={"Rage": 0.6})   # 3 stacks held
    assert s.crit_chance() == pytest.approx(0.32)
    s._takedown("kill")
    assert s.crit_chance() == pytest.approx(0.36)
    s._takedown("assist")
    assert s.crit_chance() == pytest.approx(0.50)


def test_reaper_heals_land_in_effective_health():
    assert "Assist a God: Heal +7.5% of Slain God's Max Health" in text("The Reaper")
    # 100 raw physical a second, no protection: 2000 health dies at 2000 raw.
    # Assists at 5 and 15 heal 7.5% of the 2000-health target = 150 each; the
    # toy deals 810 a fight, never 2000, so no kill. 2000 + 150 + 150.
    t = armed(target(), phys_dps=100.0)
    items = {"The Reaper": item("The Reaper", {"Strength": "0"})}
    p, _, _ = sbs.fight_ehp(toy_god(), ["The Reaper"], items, {"squishy": t})
    assert p == pytest.approx(2300.0)


def test_fight_ehp_equals_static_when_nothing_moves():
    items = {"Jotunn's Revenge": item("Jotunn's Revenge", {"Max Health": "500",
                                                           "Physical Protection": "50"})}
    t = armed(target(), phys_dps=300.0, mag_dps=300.0)
    fight = sbs.fight_ehp(toy_god(), ["Jotunn's Revenge"], items, {"squishy": t})
    static = sbs.effective_health(toy_god(), ["Jotunn's Revenge"], items)
    assert fight[0] == pytest.approx(static[0]) == pytest.approx(2500 * 1.5)
    assert fight[1] == pytest.approx(static[1]) == pytest.approx(2500)


def test_fight_ehp_keeps_the_health_gated_integral_exact():
    items = {"Freya's Tears": item("Freya's Tears", {"Max Health": "0"}),
             "Jotunn's Revenge": item("Jotunn's Revenge", {"Strength": "0"})}
    t = armed(target(), phys_dps=170.0, mag_dps=170.0)
    fight = sbs.fight_ehp(toy_god(), list(items), items, {"squishy": t})
    static = sbs.effective_health(toy_god(), list(items), items)
    assert fight[0] == pytest.approx(static[0])


# ── The enemy on our god ─────────────────────────────────────────────────

def test_kinetic_cuirass_charges_on_every_third_attack_taken_and_fires_on_our_next_swing():
    assert "Damaged by 3 Attacks from gods: Gain Kinetic. Stacks up to 2 times." in text("Kinetic Cuirass")
    assert "40 (+4% of your Health) Physical Damage" in text("Kinetic Cuirass")
    items = {"Kinetic Cuirass": item("Kinetic Cuirass", {"Max Health": "300"})}
    # Attacks taken every 0.5s from t=0 ("both": 15 raw at 50%). Charges after
    # the 3rd, 6th ... 18th: t = 1.0, 2.5, 4.0, 5.5, 7.0, 8.5. Our swings at
    # whole seconds spend one each: 2, 3, 5, 6, 8, 9 -> six shockwaves of
    # 40 + 4% x 2300.
    t = armed(target(base_health=1e6), phys_dps=30.0, attack_every=0.5)
    s = sbs.Sim(toy_god(), ["Kinetic Cuirass"], items, t, enemy="both")
    s.run_window()
    assert ps.kinetic_shockwave(2300.0) == pytest.approx(132.0)
    assert s.by_item["Kinetic Cuirass"] == pytest.approx(6 * 132.0)


def test_genjis_guard_refunds_on_a_magical_ability_hit_once_per_twenty_seconds():
    assert "Hit by Magical Ability Damage: -3s Cooldowns. Cooldown: 20s" in text("Genji's Guard")
    god = toy_god([toy_ability(cooldown=8)])
    items = {"Genji's Guard": item("Genji's Guard")}
    t = armed(target(base_health=1e6), mag_dps=50.0, ability_every=2.0)
    s = sbs.Sim(god, ["Genji's Guard"], items, t, enemy="both")
    s.run_window()
    # Our cast at 0 first, then the magical hit at 0: due 8 -> 5. The hits at
    # 2, 4, 6, 8 are inside Genji's 20s cooldown.
    assert [t for t, _ in s.casts] == [0.0, 5.0]


def test_breastplate_refunds_a_second_per_thousand_health_lost_at_level_twenty():
    assert "On 500 (+25 per Level) Health lost: -1s Ability Cooldowns." in text("Breastplate of Valor")
    assert ps.breastplate_threshold(20) == 1000.0
    god = toy_god([toy_ability(cooldown=8)])
    items = {"Breastplate of Valor": item("Breastplate of Valor", {"Strength": "0"})}
    # 200 raw a second, no protection: 1000 lost on the hit at t=4 -> due 7.
    t = armed(target(base_health=1e6), phys_dps=200.0)
    s = sbs.Sim(god, ["Breastplate of Valor"], items, t, enemy="physical")
    s.run_window()
    assert [t for t, _ in s.casts] == [0.0, 7.0]
    assert s.health_lost == pytest.approx(2000.0)


def test_draconic_scale_stacks_after_each_hit_and_counts_in_effective_health():
    assert "Gain 4 Protections against that God's damage type Stacks last 1.5s (max 7)" in text("Draconic Scale")
    items = {"Draconic Scale": item("Draconic Scale", {"Strength": "0"})}
    # 100 raw every 0.5s: hit k lands at 4 x min(k, 7) protection (the stack
    # comes AFTER the hit; 0.5s < 1.5s, so nothing decays).
    t = armed(target(), phys_dps=200.0, attack_every=0.5)
    p, _, _ = sbs.fight_ehp(toy_god(), ["Draconic Scale"], items, {"squishy": t})
    health, raw, k = 2000.0, 0.0, 0
    while health > 0:
        m = 1 + 4 * min(k, 7) / 100
        take = min(100.0, health * m)
        health -= take / m
        raw += take
        k += 1
    assert p == pytest.approx(raw)


def test_berserker_triggers_below_sixty_percent_for_eight_seconds():
    assert "When falling below 60% Health: Become Berserk for 8s" in text("Berserker's Shield")
    items = {"Berserker's Shield": item("Berserker's Shield", {"Strength": "0"})}
    s = sbs.Sim(toy_god(), ["Berserker's Shield"], items, armed(target(), phys_dps=1.0), enemy="physical")
    s.hp = 1100.0                          # 55%
    s._current_item = "Berserker's Shield"
    ps._berserk_taken(s, {"kind": "attack", "dtype": "physical", "raw": 0})
    assert s.prot_now("physical") == 15.0 and s.stat("Attack Speed %") == 25.0
    s.t = 8.0
    assert s.prot_now("physical") == 0.0 and s.stat("Attack Speed %") == 0.0


# ── Actives ───────────────────────────────────────────────────────────────

def test_dagger_of_frenzy_buffs_six_attacks():
    assert "+10 (+4 per Level) Attack Damage +20% (+1% per Level) Attack Speed Buff lasts 6 Attacks." \
        in text("Dagger of Frenzy")
    items = {"Dagger of Frenzy": item("Dagger of Frenzy", {"Strength": "0"})}
    s = sbs.Sim(toy_god(), ["Dagger of Frenzy"], items, target(base_health=1e6))
    s.run_window()
    # Six swings of 81 + 90 at 1.4/s (t = 0 ... 3.57), then 1.0/s from 4.57:
    # six more by 9.57. Cooldown 15s: one press.
    assert s.by_channel["attack"] == pytest.approx(6 * 171 + 6 * 81)


def test_a_kill_refreshes_dagger_of_frenzy():
    items = {"Dagger of Frenzy": item("Dagger of Frenzy", {"Strength": "0"})}
    s = sbs.Sim(toy_god(), ["Dagger of Frenzy"], items, target(base_health=171.0))
    s.run_window()
    # The first buffed swing kills (171 >= 171); the press is ready again at
    # once, so a fresh six follows it: 7 buffed swings at 1.4/s (t = 0 ...
    # 4.29), then 1.0/s from 5.29: five more by 9.29.
    assert s.kill_times == [0.0]
    assert s.state["Dagger of Frenzy"]["left"] == 0
    assert s.by_channel["attack"] == pytest.approx(7 * 171 + 5 * 81)


def test_avatars_parashu_and_dreamers_idol_are_a_quarter_of_the_stat_for_ten_seconds():
    assert "+25% Strength and Immune to Displacement for 10s" in text("Avatar's Parashu")
    assert "+25% Intelligence Become Immune to Displacement Buff lasts 10s" in text("Dreamer's Idol")
    items = {"Avatar's Parashu": item("Avatar's Parashu", {"Strength": "100"})}
    b = sbs.Sim(toy_god(), ["Avatar's Parashu"], items, target(), window=None)
    assert b.run_burst() == pytest.approx(81 + 125)
    assert b.stat("Strength") == 125.0
    b.t = 10.0
    assert b.stat("Strength") == 100.0


def test_death_metal_is_pressed_only_by_a_physical_god():
    assert "Lose all Intelligence. Gain 66% of it as Strength. +25% Crit Chance Buff lasts 6s." in text("Death Metal")
    items = {"Death Metal": item("Death Metal", {"Strength": "35", "Intelligence": "40",
                                                 "Critical Chance": "20%"})}
    s = sbs.Sim(toy_god(), ["Death Metal"], items, target(), window=None)
    s._press("start")
    assert s.stat("Strength") == pytest.approx(35 + 0.66 * 40)
    assert s.stat("Intelligence") == 0.0 and s.crit_chance() == pytest.approx(0.45)
    mage = dict(toy_god(), damage_type="Magical")
    m = sbs.Sim(mage, ["Death Metal"], items, target(), window=None)
    m._press("start")
    assert "Death Metal" not in m.state and m.stat("Intelligence") == 40.0


def test_lernaean_bow_is_three_arrows_of_forty_percent_of_the_swing():
    assert "Fire 3 arrows" in text("Lernaean Bow") and "40% of your Attack Damage" in text("Lernaean Bow")
    items = {"Lernaean Bow": item("Lernaean Bow", {"Strength": "40"})}
    s = sbs.Sim(toy_god(), ["Lernaean Bow"], items, target(), window=None)
    s.run_burst()
    assert s.by_item["Lernaean Bow"] == pytest.approx(3 * 0.40 * (81 + 40))


def test_shield_splitter_is_true_damage_and_erebus_is_fifteen_percent_max_health():
    assert "+40 (+5 per Level) True Damage" in text("Shield Splitter")
    assert "Magical Damage equal to 15% of Enemy Max Health" in text("Eye of Erebus")
    items = {"Shield Splitter": item("Shield Splitter"), "Eye of Erebus": item("Eye of Erebus")}
    s = sbs.Sim(toy_god(), list(items), items, target(prot=100.0), window=None)
    s.run_burst()
    assert s.by_item["Shield Splitter"] == pytest.approx(140.0)          # past 100 protection
    assert s.by_item["Eye of Erebus"] == pytest.approx(0.15 * 2000 / 2)  # 100 magical protection


def test_pendulum_blade_is_pressed_after_the_opening_casts():
    assert "On Use: -4s Ability Cooldowns. Cooldown: 40s" in text("Pendulum Blade")
    god = toy_god([toy_ability(cooldown=8)])
    items = {"Pendulum Blade": item("Pendulum Blade")}
    s = sbs.Sim(god, ["Pendulum Blade"], items, target(base_health=1e6))
    s.run_window()
    assert [t for t, _ in s.casts] == [0.0, 4.0]


def test_chronos_ticks_at_five_seconds_then_every_ten():
    assert "Every 10s: -1s Ability Cooldowns." in text("Chronos' Pendant")
    god = toy_god([toy_ability(cooldown=8)])
    items = {"Chronos' Pendant": item("Chronos' Pendant")}
    s = sbs.Sim(god, ["Chronos' Pendant"], items, target(base_health=1e6))
    s.run_window()
    assert [t for t, _ in s.casts] == [0.0, 7.0]


def test_blood_bound_book_shield_and_penetration_while_it_holds():
    assert "Shield = 7.5% Max Health & 75% Intelligence from Items" in text("Blood-Bound Book")
    items = {"Blood-Bound Book": item("Blood-Bound Book", {"Intelligence": "80"})}
    s = sbs.Sim(toy_god(), ["Blood-Bound Book"], items, target(), window=None)
    s._press("start")
    assert s.shields["Blood-Bound Book"][0] == pytest.approx(0.075 * 2000 + 0.75 * 80)
    assert s.stat("Penetration %") == 10.0
    s.t = 6.0
    assert s.stat("Penetration %") == 0.0


def test_amanita_heals_three_times_and_each_heal_cuts_the_next_hit():
    assert "+3% Health Heal every 1.5s +1 Stack of Damage Reduction per Heal" in text("Amanita Charm")
    items = {"Amanita Charm": item("Amanita Charm", {"Strength": "0"})}
    # Pressed at the hit at t=0; heals at 1.5, 3, 4.5 (60 each) land before
    # the hits at 2, 3, 5, each of which takes 10% off. 2000 + 180 health;
    # three hits deal 90 for 100 raw: 2180 + 30 raw.
    t = armed(target(), phys_dps=100.0)
    p, _, _ = sbs.fight_ehp(toy_god(), ["Amanita Charm"], items, {"squishy": t})
    assert p == pytest.approx(2210.0)


def test_hide_reflects_forty_percent_of_attacks_for_four_seconds():
    assert "Reflect: 40% of pre-mitigated Attack Damage" in text("Hide of the Nemean Lion")
    items = {"Hide of the Nemean Lion": item("Hide of the Nemean Lion", {"Strength": "0"})}
    t = armed(target(base_health=1e6), phys_dps=100.0)
    s = sbs.Sim(toy_god(), ["Hide of the Nemean Lion"], items, t, enemy="physical")
    s.run_window()
    assert s.by_item["Hide of the Nemean Lion"] == pytest.approx(4 * 40.0)   # hits at 0, 1, 2, 3


def test_shell_of_rebuke_field_and_shield():
    assert "mitigates 25% Damage, up to 300 (+40 Per Level)" in text("Shell of Rebuke")
    assert ps.shell_field_cap(20) == 1100.0
    items = {"Shell of Rebuke": item("Shell of Rebuke", {"Strength": "0"})}
    # 2000 raw a hit. Hit 1: 500 cut, 300 shield, 1200 health. Hit 2: 500 cut
    # (600 of the field left), 800 health -> dead. 2000 + 1300 raw.
    t = armed(target(), phys_dps=2000.0)
    p, _, _ = sbs.fight_ehp(toy_god(), ["Shell of Rebuke"], items, {"squishy": t})
    assert p == pytest.approx(3300.0)


def test_stampede_and_doublet_stay_refused_with_a_reason():
    for name in ("Stampede", "Doublet of Binding", "Tekko-Kagi"):
        p = ps.REGISTRY[name]
        assert p.status == ps.NOT_SIMULATED and p.assumptions


# ── Passives the fight made simulable ─────────────────────────────────────

def test_crusher_is_one_point_three_three_within_three_seconds_of_the_last():
    assert "Subsequent hits on the same target deal 33% bonus Damage, over 3s." in text("The Crusher")
    god = toy_god([toy_ability(damage=0, cooldown=2, scaling="0% Strength")])
    items = {"The Crusher": item("The Crusher", {"Strength": "100"})}
    s = sbs.Sim(god, ["The Crusher"], items, target(base_health=1e6), window=4.5)
    s.run_window()
    # Casts at 0, 2, 4: 35, then 2 x 1.33 x 35.
    assert s.by_item["The Crusher"] == pytest.approx(35 + 2 * 1.33 * 35)


def test_soul_gem_heals_on_the_fourth_ability_hit():
    items = {"Soul Gem": item("Soul Gem", {"Intelligence": "60"})}
    s = sbs.Sim(toy_god(), ["Soul Gem"], items, target())
    s.hp = 1000.0
    ev = sbs.Event(0.0, "ability", "x", 0.0)
    for _ in range(4):
        ps._soul_gem(s, ev)
    assert s.hp == pytest.approx(1140.0)


def test_bancroft_is_linear_in_missing_health_to_forty_percent():
    items = {"Bancroft's Talon": item("Bancroft's Talon", {"Intelligence": "55"})}
    s = sbs.Sim(toy_god(), ["Bancroft's Talon"], items, target())
    assert s.stat("Intelligence") == 55.0
    s.hp = 1400.0
    assert s.stat("Intelligence") == pytest.approx(85.0)
    s.hp = 400.0
    assert s.stat("Intelligence") == pytest.approx(115.0)


def test_demon_blade_uptime_is_the_chance_of_a_crit_in_the_last_three_seconds():
    assert ps.demon_blade_uptime(0.5, 2) == pytest.approx(0.75)
    assert ps.demon_blade_uptime(0.0, 9) == 0.0


def test_sanguine_lash_active_ticks_every_third_of_a_second_for_four_seconds():
    assert "On Use: Now damages every 0.33s for 4s." in text("Sanguine Lash")
    items = {"Sanguine Lash": item("Sanguine Lash", {"Strength": "0"})}
    s = sbs.Sim(toy_god(), ["Sanguine Lash"], items, target(base_health=1e6))
    s.run_window()
    per_tick = min(200.0, 0.005 * 1e6)
    # 12 ticks at 0.33 ... 3.96, then whole seconds 4 ... 10: 19 ticks.
    assert s.by_item["Sanguine Lash"] == pytest.approx(19 * per_tick)


def test_brawlers_protection_stacks_in_the_fight():
    items = {"Brawler’s Beat Stick": item("Brawler’s Beat Stick", {"Physical Protection": "100"})}
    s = sbs.Sim(toy_god(), ["Brawler’s Beat Stick"], items, target())
    s.t = 4.5
    assert s.prot_now("physical") == pytest.approx(100 * 1.06)


# ── The game clock for stacks ─────────────────────────────────────────────

def test_stack_state_is_minutes_held_over_minutes_to_full():
    st = sbs.stack_state(["A", "B", "C", "D"], 4)
    assert st == {"A": 1.0, "B": 1.0, "C": 0.5, "D": 0.0}
    assert sbs.stack_state(["A", "B"], 2, minutes_to_full=20.0) == {"A": 0.25, "B": 0.0}


def test_partial_stacks_stop_short_of_the_evolution():
    ctx = ps.StatContext(items={}, stats={}, level=20, stacks={"Devourer's Gauntlet": 0.5})
    assert ps._devourers(ctx) == {"Strength": pytest.approx(14.8), "Lifesteal %": pytest.approx(1.85)}
    ctx = ps.StatContext(items={}, stats={}, level=20, stacks={"Gauntlet of Thebes": 0.5})
    assert ps._thebes(ctx) == {"Max Health": 300.0}


# ── Criterion 5 ───────────────────────────────────────────────────────────

def test_live_tests_are_skipped_by_default_and_selectable():
    ini = (TESTS / "pytest.ini").read_text(encoding="utf-8")
    assert 'addopts = -m "not live"' in ini
    assert "live:" in ini
