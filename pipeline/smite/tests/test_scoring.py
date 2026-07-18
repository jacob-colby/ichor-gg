import pytest

from smite import scoring


def test_load_weights_missing_file_returns_defaults(tmp_path):
    w = scoring.load_weights(tmp_path / "nope.yaml")
    assert w["signals"]["efficiency"] == 0.35
    assert w["signals"]["win"] == 0.30
    assert w["signals"]["pick"] == 0.15
    assert w["signals"]["fit"] == 0.20


def test_load_weights_file_overrides_defaults(tmp_path):
    p = tmp_path / "_weights.yaml"
    p.write_text("signals:\n  efficiency: 0.5\n", encoding="utf-8")
    w = scoring.load_weights(p)
    assert w["signals"]["efficiency"] == 0.5
    # unspecified keys fall back to defaults
    assert w["signals"]["win"] == 0.30


def test_load_tags_missing_file_returns_empty(tmp_path):
    assert scoring.load_tags(tmp_path / "nope.yaml") == {}


def test_load_tags_reads_mapping(tmp_path):
    p = tmp_path / "_tags.yaml"
    p.write_text("Brawler's Ruin:\n  - anti-heal\n", encoding="utf-8")
    assert scoring.load_tags(p) == {"Brawler's Ruin": ["anti-heal"]}


def _god(name, damage_type, role, specs):
    return {"name": name, "damage_type": damage_type, "role": role, "specializations": specs}


def test_item_damage_type_from_primary_stat():
    assert scoring.item_damage_type({"stats": {"Strength": "40"}}) == "physical"
    assert scoring.item_damage_type({"stats": {"Intelligence": "70"}}) == "magical"
    assert scoring.item_damage_type({"stats": {"Physical Protection": "50"}}) == "neutral"


def test_item_damage_type_basic_attack_stats_are_physical():
    # Basic-attack items (attack speed / crit / raw attack damage) are physical
    # even without a literal Strength stat — a mage never builds them.
    assert scoring.item_damage_type({"stats": {"Attack Speed": "15", "Attack Damage": "20"}}) == "physical"
    assert scoring.item_damage_type({"stats": {"Critical Chance": "20%"}}) == "physical"
    # A hybrid converter that also carries Intelligence stays magical.
    assert scoring.item_damage_type({"stats": {"Intelligence": "30", "Attack Speed": "10"}}) == "magical"
    # Pure utility/protection stays neutral (buildable by anyone).
    assert scoring.item_damage_type({"stats": {"Cooldown Rate": "10"}}) == "neutral"


def test_passes_damage_filter_excludes_mismatched_offense():
    phys_god = _god("Ullr", "physical", "Hunter", ["Hunter"])
    int_item = {"stats": {"Intelligence": "70"}}
    str_item = {"stats": {"Strength": "40"}}
    neutral_item = {"stats": {"Physical Protection": "50"}}
    assert scoring.passes_damage_filter(str_item, phys_god)
    assert not scoring.passes_damage_filter(int_item, phys_god)
    assert scoring.passes_damage_filter(neutral_item, phys_god)  # neutral always passes


def test_god_fit_rewards_role_relevant_stats():
    weights = scoring.load_weights_default()
    sharpshooter = _god("Chiron", "physical", "Carry", ["Sharpshooter"])
    crit_item = {"stats": {"Critical Chance": "20%", "Attack Speed": "15"}}
    off_stat_item = {"stats": {"Magical Protection": "50"}}
    assert scoring.god_fit_score(crit_item, sharpshooter, weights, []) > \
        scoring.god_fit_score(off_stat_item, sharpshooter, weights, [])


def _community_build(*slots):
    # slots: (name, pick_rate, win_rate)
    return {"builds": [{"source": "community",
                        "slot_order": [{"name": n, "pick_rate": p, "win_rate": w}
                                       for (n, p, w) in slots]}]}


def test_lookup_rates_from_community_entry():
    build = _community_build(("Transcendence", 0.9, 0.55))
    assert scoring.lookup_rates(build, "Transcendence") == (0.9, 0.55)
    assert scoring.lookup_rates(build, "Missing") == (0.0, None)


def test_signal_score_combines_all_four_signals():
    weights = scoring.load_weights_default()
    god = _god("Chiron", "physical", "Carry", ["Sharpshooter"])
    item = {"name": "Deathbringer", "stats": {"Critical Chance": "20%", "Strength": "45"}}
    build = _community_build(("Deathbringer", 0.5, 0.6))
    row = scoring.signal_score(item, god, build, eff_score=0.8, weights=weights, item_tags=[])
    w = weights["signals"]
    expected = (w["efficiency"] * row["efficiency"] + w["win"] * row["win"]
                + w["pick"] * row["pick"] + w["fit"] * row["fit"])
    assert row["total"] == pytest.approx(expected)
    assert row["pick"] == 0.5 and row["win"] == 0.6


def test_mark_underrated_flags_top_quality_low_pick():
    weights = scoring.load_weights_default()  # top_quality_frac 0.30, max_pick 0.15
    rows = [
        {"quality": 0.90, "pick": 0.05},  # top-quality + unpicked -> underrated
        {"quality": 0.85, "pick": 0.50},  # top-quality but popular -> no
        {"quality": 0.40, "pick": 0.02},  # unpicked but not top-quality -> no
        {"quality": 0.30, "pick": 0.01},
        {"quality": 0.20, "pick": 0.01},
    ]
    scoring.mark_underrated(rows, weights)
    flags = {r["quality"]: r["underrated"] for r in rows}
    assert flags[0.90] is True
    assert flags[0.85] is False   # popular despite high quality
    assert flags[0.40] is False   # low pick but not top-quality


def test_mark_underrated_empty_is_safe():
    assert scoring.mark_underrated([], scoring.load_weights_default()) == []


def test_score_god_items_excludes_components_and_wrong_damage_type():
    god = _god("Chiron", "physical", "Carry", ["Sharpshooter"])
    items = [
        {"name": "Final", "tier": 3, "stats": {"Strength": "40"}},
        {"name": "Active", "tier": None, "stats": {"Strength": "40"}},
        {"name": "Component", "tier": 2, "stats": {"Strength": "40"}},
        {"name": "WrongType", "tier": 3, "stats": {"Intelligence": "70"}},
    ]
    build = _community_build()
    eff = {n: {"score": 0.5, "tier": "fair"} for n in ["Final", "Active", "Component", "WrongType"]}
    rows = scoring.score_god_items(god, items, build, eff, scoring.load_weights_default(), {})
    names = {r["item"] for r in rows}
    assert names == {"Final", "Active"}   # component + wrong-damage excluded


def test_eligible_flavors_gates_by_damage_type_and_tokens():
    weights = scoring.load_weights_default()
    weights["flavors"] = {
        "crit": {"damage_types": ["physical"], "match_any": ["Carry", "Sharpshooter"]},
        "burst": {"damage_types": None, "match_any": ["Nuker", "Burst", "Slayer", "Sniper", "Mid"]},
        "bruiser": {"damage_types": None, "match_any": None},
        "anti-tank": {"damage_types": None, "match_any": None},
    }
    chiron = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
              "specializations": ["Sharpshooter", "Nuker"]}
    ra = {"name": "Ra", "damage_type": "magical", "role": "Mid",
          "specializations": ["Sniper", "Healing"]}
    herc = {"name": "Hercules", "damage_type": "physical", "role": "Solo",
            "specializations": ["Tank", "Brawler", "Lockdown"]}
    assert set(scoring.eligible_flavors(chiron, weights)) == {"crit", "burst", "bruiser", "anti-tank"}
    assert set(scoring.eligible_flavors(ra, weights)) == {"burst", "bruiser", "anti-tank"}
    assert set(scoring.eligible_flavors(herc, weights)) == {"bruiser", "anti-tank"}
