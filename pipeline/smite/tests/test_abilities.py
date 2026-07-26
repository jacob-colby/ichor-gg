from smite import abilities

_WEIGHTS = {"abilities": {"ult_levels": [5, 9, 13, 17], "early_points": 1, "max_levels": 20}}


def _ability(slot, *details):
    return {"slot": slot, "details": list(details)}


def _god(ability_list):
    return {"name": "X", "abilities": ability_list}


def _skewed_god():
    # 1st Ability has by far the highest parsed scaling; 2nd and 3rd are close
    # but clearly lower, so the ranking is unambiguous.
    return _god([
        _ability("Basic Attack", "Damage Scaling: 100% Strength"),
        _ability("Passive", "Damage Scaling: 6% Intelligence"),
        _ability("1st Ability", "Damage Scaling: 90% Intelligence"),
        _ability("2nd Ability", "Damage Scaling: 20% Intelligence"),
        _ability("3rd Ability", "Damage Scaling: 10% Intelligence"),
        _ability("Ultimate", "Damage Scaling: 120% Intelligence"),
    ])


def _nth_occurrence(order, slot, n):
    idxs = [i for i, s in enumerate(order) if s == slot]
    return idxs[n - 1]


def test_ult_appears_at_exactly_the_configured_levels():
    order = abilities.ability_order(_skewed_god(), _WEIGHTS)
    for lvl in _WEIGHTS["abilities"]["ult_levels"]:
        assert order[lvl - 1] == "Ultimate"
    assert order.count("Ultimate") == len(_WEIGHTS["abilities"]["ult_levels"])


def test_each_non_ult_ability_gets_its_early_point_before_any_second_point():
    order = abilities.ability_order(_skewed_god(), _WEIGHTS)
    non_ult_slots = ["1st Ability", "2nd Ability", "3rd Ability"]
    first_seen = {s: order.index(s) for s in non_ult_slots}
    for slot in non_ult_slots:
        occurrences = [i for i, s in enumerate(order) if s == slot]
        if len(occurrences) < 2:
            continue
        second_index = occurrences[1]
        for other in non_ult_slots:
            assert first_seen[other] < second_index, (
                f"{other}'s first point should land before {slot}'s second point")


def test_highest_scaling_ability_is_maxed_first():
    order = abilities.ability_order(_skewed_god(), _WEIGHTS)
    # 1st Ability's scaling dwarfs 2nd/3rd, so it should reach rank 2 (and
    # beyond) strictly before either of them does.
    assert _nth_occurrence(order, "1st Ability", 2) < _nth_occurrence(order, "2nd Ability", 2)
    assert _nth_occurrence(order, "1st Ability", 2) < _nth_occurrence(order, "3rd Ability", 2)
    assert order.count("1st Ability") > order.count("2nd Ability")
    assert order.count("1st Ability") > order.count("3rd Ability")


def test_order_is_20_levels_of_only_real_ability_slots():
    order = abilities.ability_order(_skewed_god(), _WEIGHTS)
    assert len(order) == 20
    real_slots = {"1st Ability", "2nd Ability", "3rd Ability", "Ultimate"}
    assert set(order) <= real_slots
    assert "Passive" not in order
    assert "Basic Attack" not in order


def test_no_parseable_scaling_still_returns_20_valid_levels():
    god = _god([
        _ability("Basic Attack"),
        _ability("Passive"),
        _ability("1st Ability"),
        _ability("2nd Ability"),
        _ability("3rd Ability"),
        _ability("Ultimate"),
    ])
    order = abilities.ability_order(god, _WEIGHTS)
    assert len(order) == 20
    assert order.count("Ultimate") == 4
    for slot in ("1st Ability", "2nd Ability", "3rd Ability"):
        assert slot in order


def test_god_with_no_abilities_key_never_raises():
    order = abilities.ability_order({"name": "NoKit"}, _WEIGHTS)
    assert len(order) == 20


def test_defaults_used_when_weights_omit_abilities_block():
    order = abilities.ability_order(_skewed_god(), {})
    assert len(order) == 20
    assert order.count("Ultimate") == 4
    for lvl in (5, 9, 13, 17):
        assert order[lvl - 1] == "Ultimate"


def test_summary_reports_max_order_and_ult_levels():
    order = abilities.ability_order(_skewed_god(), _WEIGHTS)
    s = abilities.summary(order, _WEIGHTS)
    assert s["ult_levels"] == [5, 9, 13, 17]
    assert s["max_order"][0] == "1st Ability"
    assert set(s["max_order"]) == {"1st Ability", "2nd Ability", "3rd Ability"}
