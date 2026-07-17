from smite import efficiency


def test_parse_stat_value_plain_number():
    assert efficiency.parse_stat_value("45") == 45.0


def test_parse_stat_value_percent_suffix():
    assert efficiency.parse_stat_value("20%") == 20.0


def test_parse_stat_value_whitespace():
    assert efficiency.parse_stat_value(" 10 ") == 10.0


def test_parse_stat_value_none_returns_none():
    assert efficiency.parse_stat_value(None) is None


def test_parse_stat_value_non_numeric_returns_none():
    assert efficiency.parse_stat_value("Aura") is None


import pytest


def _item(name, cost, **stats):
    return {"name": name, "cost": cost, "stats": {k: str(v) for k, v in stats.items()}}


def test_fit_gold_values_recovers_planted_coefficients():
    # cost = 20*Strength + 30*Intelligence exactly, no intercept.
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 3000, Intelligence=100),
        _item("C", 2600, Strength=40, Intelligence=60),
        _item("D", 1000, Strength=50),
        _item("E", 1500, Intelligence=50),
    ]
    gold, stat_names = efficiency.fit_gold_values(items)
    assert gold["Strength"] == pytest.approx(20.0, abs=0.5)
    assert gold["Intelligence"] == pytest.approx(30.0, abs=0.5)
    assert set(stat_names) == {"Strength", "Intelligence"}


def test_fit_gold_values_coefficients_never_negative():
    items = [
        _item("A", 100, Strength=50, Intelligence=50),
        _item("B", 100, Strength=50, Intelligence=10),
        _item("C", 100, Strength=10, Intelligence=50),
    ]
    gold, _ = efficiency.fit_gold_values(items)
    assert all(v >= 0 for v in gold.values())


def test_fit_gold_values_ignores_items_with_missing_cost():
    # Real data has component items with cost: null (e.g. Evil Eye). They carry
    # no cost signal and must be excluded from the fit, not crash it.
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 1000, Strength=50),
        {"name": "NoCost", "cost": None, "stats": {"Strength": "40"}},
    ]
    gold, stat_names = efficiency.fit_gold_values(items)
    assert gold["Strength"] == pytest.approx(20.0, abs=1.0)


def test_efficiency_scores_flags_underpriced_as_undervalued():
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 2000, Strength=100),
        _item("C", 2000, Strength=100),
        _item("Fair", 2000, Strength=100),
        _item("Underpriced", 1000, Strength=100),
    ]
    scores, _gold = efficiency.efficiency_scores(items)
    assert scores["Underpriced"]["tier"] == "undervalued"
    assert scores["Underpriced"]["score"] > scores["Fair"]["score"]


def test_efficiency_scores_flags_passive_heavy_as_premium():
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 2000, Strength=100),
        _item("C", 2000, Strength=100),
        _item("D", 2000, Strength=100),
        _item("PassiveHeavy", 3000, Strength=5),
    ]
    scores, _ = efficiency.efficiency_scores(items)
    assert scores["PassiveHeavy"]["tier"] == "premium"
    assert scores["PassiveHeavy"]["score"] < 0.5


def test_efficiency_scores_returns_score_in_unit_range():
    items = [_item("A", 2000, Strength=100), _item("B", 1000, Strength=100)]
    scores, _ = efficiency.efficiency_scores(items)
    for s in scores.values():
        assert 0.0 <= s["score"] <= 1.0


def test_efficiency_scores_skips_null_cost_items():
    # Component items with cost: null cannot get a residual; they must be absent
    # from the result, not crash it.
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 1000, Strength=50),
        {"name": "NoCost", "cost": None, "stats": {"Strength": "40"}},
    ]
    scores, _ = efficiency.efficiency_scores(items)
    assert "NoCost" not in scores
    assert "A" in scores and "B" in scores
