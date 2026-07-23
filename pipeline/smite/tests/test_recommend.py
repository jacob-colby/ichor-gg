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


def test_build_suggested_entries_stamps_starter():
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
           "specializations": ["Sharpshooter"]}
    items = [{"name": f"I{i}", "tier": 3, "cost": 2500, "stats": {"Strength": "50"}} for i in range(7)]
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    entries = recommend.build_suggested_entries(god, items, {"builds": []}, weights, {}, "Conquest")
    assert entries[0]["starter"]["base"] == "Gilded Arrow"
    assert entries[0]["starter"]["upgrade"] == "Sharpshooter's Arrow"
    assert all("starter" in e for e in entries)


def test_stamp_community_starter_sets_starter_on_community(tmp_path):
    from smite import recommend, notes
    path = tmp_path / "Chiron-Conquest.md"
    notes.write_note(path, {"type": "smite-build", "god": "Chiron", "mode": "Conquest",
        "builds": [{"source": "community", "slot_order": [{"name": "X", "pick_rate": 0.5, "win_rate": 0.5}]}]}, "")
    recommend._stamp_community_starter(path, {"base": "Gilded Arrow", "upgrade": "Sharpshooter's Arrow"})
    fm, _ = notes.read_note(path)
    comm = next(b for b in fm["builds"] if b["source"] == "community")
    assert comm["starter"] == {"base": "Gilded Arrow", "upgrade": "Sharpshooter's Arrow"}


def test_suggested_entries_have_buy_order_flex_and_crit_core():
    from smite import recommend, scoring
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags = scoring.load_tags(recommend.TAGS_PATH)
    items_by_name = {it["name"]: it for it in items}
    god = next(g for g in recommend.load_gods() if g["name"] == "Chiron")  # physical carry
    build = recommend.load_build_note("Chiron")
    entries = recommend.build_suggested_entries(god, items, build, weights, tags, "Conquest")
    crit = next((e for e in entries if e["archetype"] == "crit"), None)
    assert crit is not None
    ncrit = sum(1 for n in crit["slot_order"]
                if "Critical Chance" in (items_by_name.get(n, {}).get("stats") or {}))
    assert ncrit >= 3
    for e in entries:
        assert e.get("flex_slots"), f"{e['archetype']} missing flex_slots"
        assert set(e["flex_slots"]) <= set(e["slot_order"])


def test_aspect_god_emits_base_and_aspect_sets():
    from smite import recommend, scoring
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags = scoring.load_tags(recommend.TAGS_PATH)
    herc = next(g for g in recommend.load_gods() if g["name"] == "Hercules")
    build = recommend.load_build_note("Hercules")
    entries = recommend.build_suggested_entries(herc, items, build, weights, tags, "Conquest")
    base_cores = [e for e in entries if e["archetype"] == "core" and not e.get("aspect")]
    aspect_cores = [e for e in entries if e["archetype"] == "core" and e.get("aspect")]
    assert len(base_cores) == 1 and len(aspect_cores) == 1
    assert aspect_cores[0]["aspect"] == herc["aspects"][0]["name"]
    assert aspect_cores[0].get("flex_slots") and aspect_cores[0]["slot_order"]


def test_non_aspect_god_emits_only_base():
    from smite import recommend, scoring
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags = scoring.load_tags(recommend.TAGS_PATH)
    susano = next(g for g in recommend.load_gods() if g["name"] == "Susano")
    entries = recommend.build_suggested_entries(susano, items, recommend.load_build_note("Susano"),
                                                weights, tags, "Conquest")
    assert all(not e.get("aspect") for e in entries)


import pytest


@pytest.fixture
def tmp_items():
    return [
        {"name": "Crit1", "tier": 3, "cost": 2500, "stats": {"Critical Chance": "25%", "Attack Speed": "15"}},
        {"name": "Crit2", "tier": 3, "cost": 2600, "stats": {"Critical Chance": "20%", "Strength": "40"}},
        {"name": "Crit3", "tier": 3, "cost": 2400, "stats": {"Critical Chance": "25%", "Attack Speed": "20"}},
        {"name": "Blade", "tier": 3, "cost": 2500, "stats": {"Strength": "55", "Attack Speed": "10"}},
        {"name": "Fists", "tier": 3, "cost": 2500, "stats": {"Strength": "60"}},
        {"name": "Tome", "tier": 3, "cost": 2500, "stats": {"Intelligence": "80"}},
        {"name": "Wall", "tier": 3, "cost": 2300, "stats": {"Physical Protection": "60", "Health": "200"}},
        {"name": "Bulwark", "tier": 3, "cost": 2300, "stats": {"Magical Protection": "60", "Health": "200"}},
    ]


def _fun_weights():
    w = scoring.load_weights_default()
    w["flavors"] = {
        "crit": {"damage_types": ["physical"], "match_any": ["Carry", "Sharpshooter"],
                 "stats": {"Critical Chance": 1.5}, "require": {"stat": "Critical Chance", "min": 3}},
        "fun-crit": {"fun": True, "bypass": ["damage_filter", "archetype_fit"],
                     "redundant_with": "crit", "damage_types": None, "match_any": None,
                     "stats": {"Critical Chance": 1.5, "Attack Speed": 1.2, "Strength": 0.8},
                     "require": {"stat": "Critical Chance", "min": 3}},
    }
    return w


def test_fun_entry_emitted_for_offclass_god_with_flag_and_honest_rationale(tmp_items):
    ymir = {"name": "Ymir", "damage_type": "magical", "role": "Support",
            "specializations": ["Tank"], "abilities": []}
    entries = recommend.build_suggested_entries(ymir, tmp_items, {"builds": []},
                                                _fun_weights(), {})
    fun = [e for e in entries if e.get("fun")]
    assert len(fun) == 1 and fun[0]["archetype"] == "fun-crit"
    assert "fun" in fun[0]["rationale"].lower()


def test_fun_crit_skipped_when_serious_crit_applies(tmp_items):
    chiron = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
              "specializations": ["Sharpshooter"], "abilities": []}
    entries = recommend.build_suggested_entries(chiron, tmp_items, {"builds": []},
                                                _fun_weights(), {})
    assert not [e for e in entries if e.get("fun")]          # redundant_with: crit
    assert [e for e in entries if e["archetype"] == "crit"]  # serious crit still there
