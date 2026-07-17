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


def test_underrated_flag_fires_only_high_score_low_pick():
    weights = scoring.load_weights_default()  # min_score 0.6, max_pick 0.15
    assert scoring.is_underrated({"total": 0.7, "pick": 0.1}, weights)
    assert not scoring.is_underrated({"total": 0.7, "pick": 0.5}, weights)   # popular
    assert not scoring.is_underrated({"total": 0.3, "pick": 0.1}, weights)   # weak


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
