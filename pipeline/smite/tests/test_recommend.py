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


from smite import scoring


def test_god_report_marks_underrated_items():
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
           "specializations": ["Sharpshooter"]}
    items = [
        {"name": "Sleeper", "tier": 3, "cost": 1000, "stats": {"Strength": "100", "Critical Chance": "20%"}},
        {"name": "Popular", "tier": 3, "cost": 2600, "stats": {"Strength": "60"}},
        {"name": "Filler", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "Filler2", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
    ]
    build = {"builds": [{"source": "community", "slot_order": [
        {"name": "Popular", "pick_rate": 0.8, "win_rate": 0.55}]}]}
    weights = scoring.load_weights_default()
    report = recommend.god_report(god, items, build, weights, tags_map={})
    assert "Chiron" in report
    assert "Sleeper" in report
    assert "UNDERRATED" in report.upper()
