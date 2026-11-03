"""The side-by-side's HEALING block (2026-11-03): a healing-received channel
on both sides, lifesteal, heal-on-hit items and anti-heal.

Hand-computed off the TOY god (81 a swing, 1.0 swings/s, 2000 health, no
protection) against toy targets, the way `test_fight.py` is.
"""
import pytest

from smite import calibrate_combat, combat, passive_sim as ps, side_by_side as sbs
from smite.tests.test_fight import armed, text
from smite.tests.test_side_by_side import item, target, toy_ability, toy_god


def lifesteal_item(pct=10):
    return {"LS": item("LS", stats={"Lifesteal": f"{pct}%"})}


# ── The arithmetic ────────────────────────────────────────────────────────

def test_healing_reduction_takes_the_strongest_and_does_not_stack():
    assert "Healing Reduction does not stack with other similar effects" in text("Brawler’s Beat Stick")
    assert combat.healing_received(100.0) == 100.0
    assert combat.healing_received(100.0, (0.40,)) == pytest.approx(60.0)
    assert combat.healing_received(100.0, (0.40, 0.40)) == pytest.approx(60.0)
    assert combat.healing_received(100.0, (0.10, 0.40)) == pytest.approx(60.0)


def test_every_anti_heal_item_is_read_off_its_text():
    for name in ("Toxic Blade", "Divine Ruin", "Brawler’s Beat Stick"):
        assert "40% Healing Reduction" in text(name) and "5s" in text(name)
        assert ps.ANTI_HEAL[name][:2] == (0.40, 5.0)
    assert "Hit a God with an Attack" in text("Toxic Blade")
    assert ps.ANTI_HEAL["Toxic Blade"][2] == "attack"


def test_the_healing_calibration_rows_pass():
    assert calibrate_combat.main([]) == 0
    rows = calibrate_combat.load_healing(calibrate_combat.DEFAULT_PATH)
    assert len(rows) >= 5
    assert combat.calibrate_healing_report(rows)["worst_rel_error"] == 0.0


def test_team_anti_heal_is_the_chance_anyone_on_the_team_holds_it():
    # One Solo in four holds it, nobody else: 40% x 1/4.
    assert sbs.team_anti_heal({"Solo": [0.4, 0, 0, 0], "Mid": [0, 0]}) == pytest.approx(0.10)
    # Two roles at a half each: 1 - 0.5 x 0.5 = 0.75 of teams.
    assert sbs.team_anti_heal({"Solo": [0.4, 0], "Jungle": [0, 0.4]}) == pytest.approx(0.30)
    assert sbs.team_anti_heal({}) == 0.0


# ── Our god heals ─────────────────────────────────────────────────────────

def test_lifesteal_heals_our_god_off_damage_to_a_live_target():
    # t=0: we swing 81 at full health (heal wasted), the enemy hits 100 -> 1900.
    # t=1: we swing 81, 10% of it heals 8.1 -> 1908.1, the enemy hits -> 1808.1.
    s = sbs.Sim(toy_god(), ["LS"], lifesteal_item(10), armed(target(), phys_dps=100.0),
                window=2.0, enemy="physical")
    s.run_window()
    assert s.hp == pytest.approx(1808.1)
    assert s.healed == pytest.approx(8.1)
    assert s.heal_by_item == {"Lifesteal": pytest.approx(8.1)}


def test_lifesteal_off_a_dead_target_heals_nothing():
    # 50-health target dies to the first swing; the second swing hits a corpse.
    s = sbs.Sim(toy_god(), ["LS"], lifesteal_item(10), armed(target(base_health=50.0), phys_dps=100.0),
                window=2.0, enemy="physical")
    s.run_window()
    assert s.hp == pytest.approx(1800.0) and s.healed == 0.0


def test_the_enemy_teams_anti_heal_cuts_our_heals():
    t = armed(target(), phys_dps=100.0)
    t["attacker"]["anti_heal"] = 0.40
    s = sbs.Sim(toy_god(), ["LS"], lifesteal_item(10), t, window=2.0, enemy="physical")
    s.run_window()
    assert s.healed == pytest.approx(8.1 * 0.6)


def test_lifesteal_raises_fight_effective_health_and_off_restores_static():
    tg = {"squishy": armed(target(base_health=1e6), phys_dps=200.0, mag_dps=200.0)}
    assert sbs.moves_in_a_fight(["LS"], lifesteal_item(30))
    on = sbs.fight_ehp(toy_god(), ["LS"], lifesteal_item(30), tg)
    static = sbs.effective_health(toy_god(), ["LS"], lifesteal_item(30))
    assert on[0] > static[0] + 100
    saved, sbs.HEALING = sbs.HEALING, False
    try:
        assert not sbs.moves_in_a_fight(["LS"], lifesteal_item(30))
        assert sbs.fight_ehp(toy_god(), ["LS"], lifesteal_item(30), tg)[:2] == static[:2]
    finally:
        sbs.HEALING = saved


def test_heal_until_bounds_healing_to_the_first_fight():
    tg = armed(target(base_health=1e6), phys_dps=300.0)
    saved, sbs.HEAL_UNTIL = sbs.HEAL_UNTIL, sbs.WINDOW
    try:
        s = sbs.Sim(toy_god(), ["LS"], lifesteal_item(50), tg, window=30.0, enemy="physical")
        s.run_window()
        late = s.heal_by_item.get("Lifesteal", 0.0)
    finally:
        sbs.HEAL_UNTIL = saved
    s2 = sbs.Sim(toy_god(), ["LS"], lifesteal_item(50), tg, window=30.0, enemy="physical")
    s2.run_window()
    assert 0 < late < s2.healed


def test_shield_of_the_phoenix_heals_one_and_a_half_percent_per_ability_hit():
    assert "Ability Hit a God: +1.5% Health Heal" in text("Shield of the Phoenix")
    god = toy_god([toy_ability(cooldown=1)])
    items = {"Shield of the Phoenix": item("Shield of the Phoenix", stats={"Mana": "1"})}
    s = sbs.Sim(god, ["Shield of the Phoenix"], items, target())
    s.hp = 1000.0
    s._ability(0.0, s.rotation[0])
    assert s.hp == pytest.approx(1000.0 + 0.015 * 2000.0)
    assert ps.lookup(items["Shield of the Phoenix"]).status == ps.SIMULATED


def test_gluttonous_grimoire_stores_65_percent_at_full_health_and_spends_it_on_the_next_attack():
    assert "Store 50% of your Lifesteal healing" in text("Gluttonous Grimoire")
    assert "If at full Health: Store 65% instead" in text("Gluttonous Grimoire")
    items = {"Gluttonous Grimoire": item("Gluttonous Grimoire", stats={"Lifesteal": "10%"})}
    s = sbs.Sim(toy_god(), ["Gluttonous Grimoire"], items, target(base_health=1e6), window=1.5)
    s.run_window()
    # Swing 1 (t=0): 81, nothing stored yet; stores 0.65 x 8.1 = 5.265.
    # Swing 2 (t=1): 81 + a 5.265 magical proc; then stores 0.65 x 8.1 again
    # (the proc's own lifesteal is at full health too: 0.65 x 0.5265).
    assert s.by_item["Gluttonous Grimoire"] == pytest.approx(5.265)
    assert s.state["Gluttonous Grimoire"]["stored"] == pytest.approx(0.65 * (8.1 + 0.5265))
    assert ps.gluttonous_cap(2000.0, 100.0) == pytest.approx(250.0)


def test_bloodforge_shield_and_its_lifesteal_while_it_holds():
    items = {"Bloodforge": item("Bloodforge", stats={"Strength": "40", "Lifesteal": "7.5%"})}
    s = sbs.Sim(toy_god(), ["Bloodforge"], items, target())
    s._press("start")
    assert s.shields["Bloodforge"][0] == pytest.approx(0.10 * 2000.0 + 1.5 * 40.0)
    assert s.stat("Lifesteal %") == pytest.approx(17.5)
    s.t = 6.5
    assert s.stat("Lifesteal %") == pytest.approx(7.5)


# ── The target heals, and our anti-heal cuts it ───────────────────────────

def test_the_target_lifesteals_off_its_hits_and_sustained_damage_is_net():
    # Two of our swings (162 dealt); the enemy's two 100 hits heal it 10 each.
    t = armed(target(lifesteal=10.0), phys_dps=100.0)
    s = sbs.Sim(toy_god(), [], {}, t, window=2.0, enemy="physical")
    assert s.run_window() == pytest.approx(162.0 - 20.0)
    assert s.target_healed == pytest.approx(20.0)


def test_our_anti_heal_cuts_the_targets_healing_by_forty_percent():
    t = armed(target(lifesteal=10.0), phys_dps=100.0)
    items = {"Divine Ruin": item("Divine Ruin", stats={"Mana": "1"})}
    s = sbs.Sim(toy_god(), ["Divine Ruin"], items, t, window=2.0, enemy="physical")
    assert s.run_window() == pytest.approx(162.0 - 12.0)
    # Toxic Blade's trigger is an attack; the toy god only attacks, so the same.
    tox = {"Toxic Blade": item("Toxic Blade", stats={"Mana": "1"})}
    s2 = sbs.Sim(toy_god(), ["Toxic Blade"], tox, t, window=2.0, enemy="physical")
    s2.run_window()
    assert s2.target_healed == pytest.approx(12.0)


def test_two_anti_heal_items_cut_no_more_than_one():
    t = armed(target(lifesteal=10.0), phys_dps=100.0)
    items = {n: item(n, stats={"Mana": "1"}) for n in ("Divine Ruin", "Toxic Blade")}
    s = sbs.Sim(toy_god(), list(items), items, t, window=2.0, enemy="physical")
    s.run_window()
    assert s.target_healed == pytest.approx(12.0)


def test_healing_off_is_the_old_sustained_figure():
    t = armed(target(lifesteal=10.0), phys_dps=100.0)
    saved, sbs.HEALING = sbs.HEALING, False
    try:
        s = sbs.Sim(toy_god(), ["LS"], lifesteal_item(10), t, window=2.0, enemy="physical")
        assert s.run_window() == pytest.approx(162.0)
        assert s.healed == 0.0 and s.target_healed == 0.0
    finally:
        sbs.HEALING = saved


def test_the_heal_items_are_no_longer_refused_for_want_of_healing():
    for name in ("Gluttonous Grimoire", "Shield of the Phoenix", "Bloodforge", "Divine Ruin"):
        assert ps.lookup({"name": name}).status == ps.SIMULATED, name
    for name in ("Toxic Blade", "Stygian Anchor"):
        assert ps.lookup({"name": name}).status == ps.PARTIAL, name
    for p in ps.REGISTRY.values():
        assert "no healing modelled" not in p.assumptions
