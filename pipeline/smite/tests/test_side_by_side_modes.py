"""The side-by-side per mode (2026-11-03): Joust and Arena against the
BORROWED Conquest community six, under each mode's own fight settings."""
import pytest

from smite import side_by_side as sbs
from smite.tests.test_side_by_side import item, target, toy_god


def test_mode_settings_are_the_documented_and_derived_ones():
    assert sbs.MODE_SETTINGS["Conquest"] == {"ENEMIES": 5, "KILL_TIME": 10.0, "WINDOW": 10.0}
    j = sbs.MODE_SETTINGS["Joust"]
    assert j["ENEMIES"] == 3
    assert j["KILL_TIME"] == pytest.approx(10.0 * 5 / 3) == pytest.approx(j["WINDOW"])
    a = sbs.MODE_SETTINGS["Arena"]
    assert a["ENEMIES"] == 5 and a["KILL_TIME"] == 10.0 and a["WINDOW"] > 10.0


def test_use_mode_sets_and_restores_the_globals():
    before = (sbs.WINDOW, sbs.ENEMIES, sbs.KILL_TIME, sbs.ASSIST_INTERVAL, sbs.ASSIST_FIRST, sbs.MODE)
    with sbs.use_mode("Joust"):
        assert sbs.MODE == "Joust" and sbs.ENEMIES == 3
        assert sbs.ASSIST_INTERVAL == pytest.approx(sbs.WINDOW)
        assert sbs.ASSIST_FIRST == pytest.approx(sbs.WINDOW / 2)
        # A Sim built inside the mode reads its fight length NOW, not at import.
        s = sbs.Sim(toy_god(), [], {}, target(base_health=1e6))
        assert s.window == pytest.approx(10.0 * 5 / 3)
    assert (sbs.WINDOW, sbs.ENEMIES, sbs.KILL_TIME, sbs.ASSIST_INTERVAL,
            sbs.ASSIST_FIRST, sbs.MODE) == before


def test_one_kill_per_joust_fight_is_one_per_sixteen_point_seven_seconds():
    with sbs.use_mode("Joust"):
        s = sbs.Sim(toy_god(), [], {}, target(base_health=400.0), window=40.0)
        s.run_window()
    # 81 a swing, swings on whole seconds: the fifth swing inside each fight
    # kills. Fights start at 0, 16.67 and 33.33, so swings 0-4, 17-21, 34-38.
    assert s.kill_times == [4.0, 21.0, 38.0]


def test_a_three_seat_team_draws_anti_heal_from_the_pooled_share():
    cuts = {"Solo": [0.4, 0.0], "Mid": [0.0, 0.0]}   # 1 in 4 sixes
    assert sbs.team_anti_heal(cuts, 3) == pytest.approx(0.4 * (1 - 0.75 ** 3))
    assert sbs.team_anti_heal(cuts, 5) == pytest.approx(0.4 * 0.5)   # per-role product


def test_minutes_per_item_comes_from_the_mode_economy():
    items = {f"I{i}": item(f"I{i}", cost=2500) for i in range(6)}
    slots = [{"name": f"I{i}", "pick_rate": 0.5} for i in range(6)]
    builds = {"Toy": {"builds": [{"source": "community", "slot_order": slots}]}}
    weights = {"modes": {"joust": {"economy": {"start_gold": 1250, "gold_per_min": 690}}}}
    got = sbs.mode_minutes_per_item("Joust", weights, builds, items, [toy_god()])
    assert got == pytest.approx((15000 - 1250) / (6 * 690))
    assert sbs.mode_minutes_per_item("Conquest", weights, builds, items, [toy_god()]) is None


def test_an_item_the_modes_shop_lacks_is_dropped_from_the_borrowed_six():
    names = [f"I{i}" for i in range(6)] + ["Eye of Erebus"]
    items = {n: item(n) for n in names}
    slots = [{"name": "Eye of Erebus", "pick_rate": 0.4,
              "alternates": [{"name": "I5", "pick_rate": 0.3}]}] + [
        {"name": f"I{i}", "pick_rate": 0.5} for i in range(5)]
    note = {"builds": [{"source": "community", "slot_order": slots}]}
    shop = {n: it for n, it in items.items() if n != "Eye of Erebus"}
    six, fills = sbs.community_six(toy_god(), note, shop)
    assert "Eye of Erebus" not in six and "I5" in six and len(six) == 6


def test_the_report_labels_a_borrowed_comparison():
    with sbs.use_mode("Joust"):
        lines = sbs.report_lines([], [], {"squishy": target(role="Mid", n=1), "tank": target(role="Support", n=1)},
                                 "test")
    head = "\n".join(lines[:3])
    assert "Joust" in head and "BORROWED FROM CONQUEST" in head
