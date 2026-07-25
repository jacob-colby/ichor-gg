import pytest

from smite import tierlist


def _build_group(god, mode="Conquest", builds=None):
    return {"god": god, "mode": mode, "builds": builds or []}


def _core_entry(slot_scores, archetype="core"):
    return {
        "source": "suggested",
        "archetype": archetype,
        "slot_order": list(slot_scores),
        "slot_scores": slot_scores,
    }


def _community_entry(aspect_win_rate=None):
    return {"source": "community", "aspect_win_rate": aspect_win_rate}


# ---------------------------------------------------------------------------
# god_rankings
# ---------------------------------------------------------------------------

def test_god_rankings_ours_is_mean_of_core_slot_scores():
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    core = _core_entry({
        "Jotunn's Revenge": {"total": 0.6},
        "Tyrfing": {"total": 0.4},
    })
    builds = [_build_group("Chiron", builds=[core])]

    result = tierlist.god_rankings(gods, builds)

    assert result == [{
        "name": "Chiron", "role": "Hunter", "damage_type": "Physical",
        "ours": pytest.approx(0.5), "community": None,
    }]


def test_god_rankings_community_reads_aspect_win_rate():
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    core = _core_entry({"Jotunn's Revenge": {"total": 0.6}})
    community = _community_entry(aspect_win_rate=0.51)
    builds = [_build_group("Chiron", builds=[community, core])]

    result = tierlist.god_rankings(gods, builds)

    assert result[0]["community"] == 0.51
    assert result[0]["ours"] == pytest.approx(0.6)


def test_god_rankings_no_suggested_core_returns_none_ours():
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    # only a non-core archetype, no "core" build present
    builds = [_build_group("Chiron", builds=[_core_entry({"A": {"total": 0.5}}, archetype="crit")])]

    result = tierlist.god_rankings(gods, builds)

    assert result[0]["ours"] is None


def test_god_rankings_god_with_no_builds_at_all_is_all_none():
    gods = [{"name": "Solo", "role": "Mid", "damage_type": "Magical"}]
    result = tierlist.god_rankings(gods, builds=[])
    assert result == [{
        "name": "Solo", "role": "Mid", "damage_type": "Magical",
        "ours": None, "community": None,
    }]


def test_god_rankings_deterministic_order_by_name():
    gods = [
        {"name": "Zeus", "role": "Mid", "damage_type": "Magical"},
        {"name": "Anubis", "role": "Mid", "damage_type": "Magical"},
    ]
    result = tierlist.god_rankings(gods, builds=[])
    assert [g["name"] for g in result] == ["Anubis", "Zeus"]


def test_god_rankings_ignores_non_conquest_builds():
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    core = _core_entry({"A": {"total": 0.9}})
    builds = [_build_group("Chiron", mode="Joust", builds=[core])]

    result = tierlist.god_rankings(gods, builds)

    assert result[0]["ours"] is None


# ---------------------------------------------------------------------------
# item_rankings
# ---------------------------------------------------------------------------

def test_item_rankings_ours_and_community_mapping():
    items = [
        {"name": "Deathbringer", "tier": 3, "efficiency_tier": "undervalued",
         "meta": {"win_avg": 0.53, "gods": 4}},
    ]
    eff = {"Deathbringer": {"score": 0.81}}

    result = tierlist.item_rankings(items, eff)

    assert result == [{
        "name": "Deathbringer", "tier": 3, "efficiency_tier": "undervalued",
        "ours": 0.81, "community": 0.53,
    }]


def test_item_rankings_missing_meta_is_none_community():
    items = [{"name": "Bumba's Spear", "tier": 2, "efficiency_tier": "fair"}]
    eff = {"Bumba's Spear": {"score": 0.4}}

    result = tierlist.item_rankings(items, eff)

    assert result[0]["community"] is None


def test_item_rankings_unscored_item_is_none_ours():
    # e.g. a tier-1 starter, deliberately excluded from the efficiency model
    items = [{"name": "Gilded Arrow", "tier": 1, "efficiency_tier": None}]
    eff = {}

    result = tierlist.item_rankings(items, eff)

    assert result[0]["ours"] is None


def test_item_rankings_deterministic_order_by_name():
    items = [
        {"name": "Zeal", "tier": 2, "efficiency_tier": "fair"},
        {"name": "Aegis", "tier": 2, "efficiency_tier": "fair"},
    ]
    result = tierlist.item_rankings(items, {})
    assert [i["name"] for i in result] == ["Aegis", "Zeal"]


# ---------------------------------------------------------------------------
# assign_tiers
# ---------------------------------------------------------------------------

def _scored_entries(n):
    # descending scores 1.00, 0.99, ... so rank order == input order
    return [{"name": f"e{i:02d}", "score": round(1.0 - i * 0.01, 2)} for i in range(n)]


def test_assign_tiers_percentile_bucket_sizes_for_20_entries():
    entries = _scored_entries(20)

    result = tierlist.assign_tiers(entries, "score")

    tiers = [e["tier_score"] for e in result]
    assert tiers.count("S") == 2   # top 10%
    assert tiers.count("A") == 4   # next 20%
    assert tiers.count("B") == 8   # next 40%
    assert tiers.count("C") == 6   # remaining 30%


def test_assign_tiers_top_scorer_is_s_lowest_is_c():
    entries = _scored_entries(20)

    result = tierlist.assign_tiers(entries, "score")
    by_name = {e["name"]: e for e in result}

    assert by_name["e00"]["tier_score"] == "S"
    assert by_name["e19"]["tier_score"] == "C"


def test_assign_tiers_missing_score_is_unranked_not_c():
    entries = _scored_entries(5) + [{"name": "no-score", "score": None}]

    result = tierlist.assign_tiers(entries, "score")
    by_name = {e["name"]: e for e in result}

    assert by_name["no-score"]["tier_score"] is None
    assert "C" not in {by_name["no-score"]["tier_score"]}


def test_assign_tiers_does_not_mutate_input():
    entries = _scored_entries(3)
    original = [dict(e) for e in entries]

    tierlist.assign_tiers(entries, "score")

    assert entries == original


def test_assign_tiers_deterministic_on_ties():
    entries = [
        {"name": "Zebra", "score": 0.5},
        {"name": "Apple", "score": 0.5},
        {"name": "Mango", "score": 0.5},
    ]

    result1 = tierlist.assign_tiers(entries, "score")
    result2 = tierlist.assign_tiers(entries, "score")

    assert [e["name"] for e in result1] == [e["name"] for e in result2]
    # tie-break is alphabetical by name
    assert [e["name"] for e in result1] == ["Apple", "Mango", "Zebra"]


def test_assign_tiers_single_scored_entry_is_s():
    entries = [{"name": "Solo", "score": 0.7}]

    result = tierlist.assign_tiers(entries, "score")

    assert result == [{"name": "Solo", "score": 0.7, "tier_score": "S"}]


def test_assign_tiers_empty_list():
    assert tierlist.assign_tiers([], "score") == []


def test_assign_tiers_all_unranked():
    entries = [{"name": "A", "score": None}, {"name": "B", "score": None}]

    result = tierlist.assign_tiers(entries, "score")

    assert all(e["tier_score"] is None for e in result)


# ---------------------------------------------------------------------------
# build_tierlist
# ---------------------------------------------------------------------------

def test_build_tierlist_shape_has_gods_and_items_with_both_tiers():
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    core = _core_entry({"Jotunn's Revenge": {"total": 0.6}})
    community = _community_entry(aspect_win_rate=0.51)
    builds = [_build_group("Chiron", builds=[community, core])]
    items = [{"name": "Deathbringer", "tier": 3, "efficiency_tier": "undervalued",
              "meta": {"win_avg": 0.53, "gods": 4}}]
    eff = {"Deathbringer": {"score": 0.81}}

    result = tierlist.build_tierlist(gods, builds, items, eff)

    assert set(result) == {"gods", "items"}
    assert result["gods"][0]["name"] == "Chiron"
    assert result["gods"][0]["tier_ours"] == "S"
    assert result["gods"][0]["tier_community"] == "S"
    assert result["items"][0]["name"] == "Deathbringer"
    assert result["items"][0]["tier_ours"] == "S"
    assert result["items"][0]["tier_community"] == "S"


def test_build_tierlist_empty_inputs():
    result = tierlist.build_tierlist([], [], [], {})
    assert result == {"gods": [], "items": []}
