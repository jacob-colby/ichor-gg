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


def test_tier1_starters_excluded_from_gold_fit_and_scoring():
    # Starters (tier 1) are passive-priced: their gold buys an ability/adaptive
    # passive, not their token stats. Regressing 600g onto "1 Health Regen"
    # would poison the gold-per-stat fit, so tier-1 items must sit out both the
    # fit and the scored set (they keep their cost for display/audit).
    core = [
        {"name": "A", "tier": 3, "cost": 3000, "stats": {"Strength": "60"}},
        {"name": "B", "tier": 3, "cost": 2000, "stats": {"Strength": "40"}},
        {"name": "C", "tier": 2, "cost": 1200, "stats": {"Intelligence": "45"}},
    ]
    starter = {"name": "S", "tier": 1, "cost": 600, "stats": {"Health Regen": "1"}}
    gold_without, _ = efficiency.fit_gold_values(core)
    gold_with, _ = efficiency.fit_gold_values(core + [starter])
    assert gold_with == gold_without  # the starter did not perturb the fit
    scores, _ = efficiency.efficiency_scores(core + [starter])
    assert "S" not in scores  # tier-1 starter is not scored
    assert {"A", "B", "C"} <= set(scores)  # real items still scored


def test_components_stay_in_the_fit_and_sharpen_it():
    """A tier-2 component is scored and does move the fit — it is the evidence
    that lets a stat's price be identified apart from the bundles it always
    ships in. Narrowing this pool to finished items only cost the validation
    gate 3.3 points of coverage; see `efficiency_pool`."""
    finished = [
        {"name": "A", "tier": 3, "cost": 3000, "stats": {"Strength": "60"}},
        {"name": "B", "tier": 3, "cost": 2000, "stats": {"Strength": "40"}},
    ]
    component = {"name": "Sickle", "tier": 2, "cost": 1200, "stats": {"Strength": "10"}}
    assert component in efficiency.efficiency_pool(finished + [component])
    scores, _ = efficiency.efficiency_scores(finished + [component])
    assert "Sickle" in scores


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


# ── Units are part of a stat's identity ───────────────────────────────────

def test_percent_and_flat_of_the_same_stat_are_priced_separately():
    """Penetration ships both ways. Regressed into one column, `10` and `10%`
    are charged the same gold — against a 300-protection target they're worth
    10 and 30. The split is not cosmetic: it moves every build that values
    penetration."""
    flat = {"name": "Flat", "cost": 2000, "tier": 3, "stats": {"Penetration": "20"}}
    pct = {"name": "Pct", "cost": 3000, "tier": 3, "stats": {"Penetration": "20%"}}
    names = efficiency.collect_stat_names([flat, pct])
    assert names == ["Penetration", "Penetration %"]
    assert efficiency.item_stat_values(flat) == {"Penetration": 20.0}
    assert efficiency.item_stat_values(pct) == {"Penetration %": 20.0}


def test_stat_key_leaves_unambiguous_stats_alone():
    assert efficiency.stat_key("Strength", "40") == "Strength"
    assert efficiency.stat_key("Lifesteal", "7.5%") == "Lifesteal %"


def test_predicted_cost_reads_the_same_columns_the_fit_wrote():
    """A price looked up under the bare name would silently read the wrong
    column — the failure mode the split exists to prevent."""
    pct = {"name": "Pct", "cost": 3000, "tier": 3, "stats": {"Penetration": "10%"}}
    gold = {"Penetration": 1.0, "Penetration %": 50.0, efficiency.INTERCEPT_KEY: 100.0}
    assert efficiency.predicted_cost(pct, gold) == 100.0 + 10 * 50.0


def test_shipped_penetration_columns_disagree_by_a_lot():
    """Guards the real fit: if these ever converge, either the split broke or
    the item data changed shape, and both are worth knowing about."""
    from pathlib import Path
    from smite import notes, recommend
    items = [notes.read_note(p)[0] for p in (recommend.DATA_ROOT / "Items").glob("*.md")]
    gold, _ = efficiency.fit_gold_values([i for i in items if i.get("name")])
    assert gold["Penetration %"] > 2 * gold["Penetration"]
