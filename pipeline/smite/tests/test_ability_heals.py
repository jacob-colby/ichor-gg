"""`ability_heals`: self-heals in a god's abilities, and their landing in the
fight's heal channel (2026-11-03)."""
import pytest

from smite import ability_heals as ah, recommend, side_by_side as sbs
from smite.tests.test_fight import armed
from smite.tests.test_side_by_side import target, toy_god


def _gods():
    return {g["name"]: g for g in recommend.load_gods()}


def _ab(god, name):
    return next(a for a in god["abilities"] if a["name"] == name)


def test_flat_heals_read_the_last_rank_and_tick_counts():
    g = _gods()
    hm = ah.self_heal(_ab(g["Hua Mulan"], "Spear Thrust"))
    assert hm["per"]["flat"] == 45.0 and hm["ticks"] == 1
    ch = ah.self_heal(_ab(g["Chaac"], "Rain Dance"))
    assert ch["ticks"] == 8 and ch["per"] == {"flat": 20.0, "Intelligence": 0.05}


def test_percent_terms_are_read():
    g = _gods()
    sol = ah.self_heal(_ab(g["Sol"], "Radiance"))
    assert sol["ticks"] == 6 and sol["per"]["missing_health"] == pytest.approx(0.025)
    mor = ah.self_heal(_ab(g["Mordred"], "Cruel Strikes"))
    assert mor["per"]["protections"] == pytest.approx(0.45)


def test_an_ally_only_heal_is_skipped():
    ab = {"name": "X", "description": "Heal allies in the area", "details": ["Heal: 50"]}
    assert ah.self_heal(ab) is None


def test_amount_adds_every_term_and_multiplies_by_ticks():
    h = {"ticks": 2, "per": {"flat": 10.0, "max_health": 0.01, "missing_health": 0.1,
                             "protections": 0.5, "Intelligence": 0.1}}
    got = ah.amount(h, max_health=2000.0, hp=1500.0, protections=40.0, stats={"Intelligence": 100.0})
    assert got == pytest.approx(2 * (10 + 20 + 50 + 20 + 10))


def test_a_heal_only_ability_casts_at_the_first_hit_taken_then_on_cooldown():
    god = toy_god()
    god["abilities"].append({"slot": "1st Ability", "name": "Mend", "description": "Heal yourself",
                             "details": ["Heal: 100", "Cooldown: 4 seconds"]})
    s = sbs.Sim(god, [], {}, armed(target(base_health=1e6), phys_dps=300.0), window=6.0, enemy="physical")
    s.run_window()
    # Hits at 0..5 (300 each); heals at t=0 (after the first hit) and t=4.
    assert s.heal_by_item["ability: Mend"] == pytest.approx(200.0)


def test_ability_heals_off_reproduces_the_old_run():
    god = toy_god()
    god["abilities"].append({"slot": "1st Ability", "name": "Mend", "description": "Heal yourself",
                             "details": ["Heal: 100", "Cooldown: 4 seconds"]})
    saved, sbs.ABILITY_HEALS = sbs.ABILITY_HEALS, False
    try:
        s = sbs.Sim(god, [], {}, armed(target(base_health=1e6), phys_dps=300.0), window=6.0, enemy="physical")
        s.run_window()
        assert s.healed == 0.0
    finally:
        sbs.ABILITY_HEALS = saved


def test_roster_count():
    assert sum(1 for g in recommend.load_gods() if ah.god_self_heals(g)) >= 25
