from smite import recommend


def test_efficiency_report_ranks_undervalued_first():
    items = [
        {"name": "OnCurve", "cost": 2000, "stats": {"Strength": "100"}},
        {"name": "OnCurve2", "cost": 2000, "stats": {"Strength": "100"}},
        {"name": "OnCurve3", "cost": 2000, "stats": {"Strength": "100"}},
        {"name": "Bargain", "cost": 1000, "stats": {"Strength": "100"}},
    ]
    report = recommend.efficiency_report(items)
    assert "Bargain" in report
    assert "undervalued" in report
    # Bargain's row appears before the on-curve rows (sorted best value first).
    assert report.index("Bargain") < report.index("OnCurve3")


def test_efficiency_report_skips_items_without_score():
    items = [
        {"name": "A", "cost": 2000, "stats": {"Strength": "100"}},
        {"name": "B", "cost": 1000, "stats": {"Strength": "100"}},
        {"name": "NoCost", "cost": None, "stats": {"Strength": "40"}},
    ]
    report = recommend.efficiency_report(items)  # must not raise
    assert "NoCost" not in report
    assert "A" in report and "B" in report
