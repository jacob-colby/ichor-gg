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


def test_build_suggested_entries_shape():
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
           "specializations": ["Sharpshooter"]}
    items = [
        {"name": "A", "tier": 3, "cost": 2000, "stats": {"Strength": "40", "Critical Chance": "20%"}},
        {"name": "Boots", "tier": 3, "cost": 1200, "stats": {"Movement Speed": "18"}},
        {"name": "C", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "D", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "E", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "F", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "G", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
    ]
    build = {"builds": [{"source": "community", "slot_order": []}]}
    weights = scoring.load_weights_default()
    entries = recommend.build_suggested_entries(god, items, build, weights, tags_map={})
    assert entries and entries[0]["source"] == "suggested"
    assert entries[0]["archetype"] == "core"
    assert isinstance(entries[0]["slot_order"], list) and entries[0]["slot_order"]
    assert "rationale" in entries[0]
    tags = {s["vs_tag"] for s in entries[0]["situational_swaps"]}
    assert {"heavy_cc", "magic_heavy", "physical_heavy", "sustain"} <= tags


def test_build_suggested_entries_emits_core_plus_flavors():
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
           "specializations": ["Sharpshooter", "Nuker"]}
    items = [
        {"name": "Crit1", "tier": 3, "cost": 2000, "stats": {"Critical Chance": "20%", "Strength": "40"}},
        {"name": "Pen1", "tier": 3, "cost": 2000, "stats": {"Strength": "40", "Penetration": "15"}},
        {"name": "A", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "B", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "C", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "D", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "E", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
    ]
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    entries = recommend.build_suggested_entries(god, items, {"builds": []}, weights, {}, "Conquest")
    archetypes = [e["archetype"] for e in entries]
    assert archetypes[0] == "core"
    assert set(archetypes) >= {"core", "crit", "burst", "bruiser", "anti-tank"}
    assert all(e["source"] == "suggested" and e["slot_order"] for e in entries)


def test_build_suggested_entries_joust_omits_underrated_and_labels():
    god = {"name": "Ra", "damage_type": "magical", "role": "Mid", "specializations": ["Sniper"]}
    items = [{"name": f"I{i}", "tier": 3, "cost": 2500, "stats": {"Intelligence": "70"}} for i in range(7)]
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    entries = recommend.build_suggested_entries(god, items, {"builds": []}, weights, {}, "Joust")
    core = next(e for e in entries if e["archetype"] == "core")
    assert "Underrated" not in core["rationale"]
    assert "no meta" in core["rationale"].lower()
    assert "crit" not in [e["archetype"] for e in entries]
