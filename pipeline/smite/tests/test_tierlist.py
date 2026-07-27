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


def _community_entry(aspect_win_rate=None, aspect_pick_rate=0.45):
    """The default pick rate is a confidently-played aspect: these fixtures
    exist to test plumbing, and should not be silently filtered by the
    confidence guard. Tests that care about the guard set it explicitly."""
    return {
        "source": "community",
        "aspect_win_rate": aspect_win_rate,
        "aspect_pick_rate": aspect_pick_rate,
    }


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

    # Discounted for how much the aspect is actually played, never raw.
    assert result[0]["community"] == pytest.approx(
        tierlist.confident_win_rate(0.51, 0.45))
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
# god_rankings — mode parameter (Task R2: per-mode tier list)
# ---------------------------------------------------------------------------

def test_god_rankings_mode_defaults_to_conquest():
    # Calling with no mode arg must behave exactly like mode="Conquest" —
    # existing callers (and the tests above) rely on this default.
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    core = _core_entry({"A": {"total": 0.8}})
    builds = [_build_group("Chiron", mode="Conquest", builds=[core])]

    default_result = tierlist.god_rankings(gods, builds)
    explicit_result = tierlist.god_rankings(gods, builds, mode="Conquest")

    assert default_result == explicit_result == [{
        "name": "Chiron", "role": "Hunter", "damage_type": "Physical",
        "ours": pytest.approx(0.8), "community": None,
    }]


def test_god_rankings_joust_mode_reads_joust_builds_not_conquest():
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    conquest_core = _core_entry({"A": {"total": 0.2}})
    joust_core = _core_entry({"B": {"total": 0.9}})
    builds = [
        _build_group("Chiron", mode="Conquest", builds=[conquest_core]),
        _build_group("Chiron", mode="Joust", builds=[joust_core]),
    ]

    conquest_result = tierlist.god_rankings(gods, builds, mode="Conquest")
    joust_result = tierlist.god_rankings(gods, builds, mode="Joust")

    assert conquest_result[0]["ours"] == pytest.approx(0.2)
    assert joust_result[0]["ours"] == pytest.approx(0.9)


def test_god_rankings_joust_community_is_none_when_god_has_no_joust_community_entry():
    # SmiteBrain has no Joust win/pick data, so the honest, non-fabricated
    # behaviour for a god whose Joust build note carries only a "suggested"
    # entry (no "community" entry at all) is an unranked (None) community
    # signal for that mode — exactly like the pre-existing Conquest gap.
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    joust_core = _core_entry({"A": {"total": 0.5}})
    builds = [_build_group("Chiron", mode="Joust", builds=[joust_core])]  # no community entry

    result = tierlist.god_rankings(gods, builds, mode="Joust")

    assert result[0]["community"] is None
    assert result[0]["ours"] == pytest.approx(0.5)


def test_god_rankings_god_with_only_a_conquest_build_is_unranked_in_joust():
    # A god that has never had its Joust data scraped at all (no Joust build
    # group in the input whatsoever) must still appear in the Joust ranking
    # — unranked (ours/community both None), not silently dropped from the
    # list.
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    conquest_core = _core_entry({"A": {"total": 0.7}})
    builds = [_build_group("Chiron", mode="Conquest", builds=[conquest_core])]

    result = tierlist.god_rankings(gods, builds, mode="Joust")

    assert result == [{
        "name": "Chiron", "role": "Hunter", "damage_type": "Physical",
        "ours": None, "community": None,
    }]


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

    # Legacy top-level shape (Task 4.1) still resolves — the existing viewer
    # reads data.tierlist.gods / .items directly and must not break.
    assert {"gods", "items"} <= set(result)
    assert result["gods"][0]["name"] == "Chiron"
    assert result["gods"][0]["tier_ours"] == "S"
    assert result["gods"][0]["tier_community"] == "S"
    assert result["items"][0]["name"] == "Deathbringer"
    assert result["items"][0]["tier_ours"] == "S"
    assert result["items"][0]["tier_community"] == "S"


def test_build_tierlist_empty_inputs():
    result = tierlist.build_tierlist([], [], [], {})
    assert result == {
        "gods": [], "items": [],
        "conquest": {"gods": [], "items": []},
        "joust": {"gods": [], "items": []},
    }


# ---------------------------------------------------------------------------
# build_tierlist — per-mode shape (Task R2: Conquest + Joust tier list)
# ---------------------------------------------------------------------------

def test_build_tierlist_emits_conquest_and_joust_keys():
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    core = _core_entry({"A": {"total": 0.6}})
    builds = [_build_group("Chiron", mode="Conquest", builds=[core])]
    items = [{"name": "Deathbringer", "tier": 3, "efficiency_tier": "undervalued"}]
    eff = {"Deathbringer": {"score": 0.81}}

    result = tierlist.build_tierlist(gods, builds, items, eff)

    assert {"gods", "items", "conquest", "joust"} <= set(result)
    for mode_key in ("conquest", "joust"):
        assert set(result[mode_key]) == {"gods", "items"}
        assert [g["name"] for g in result[mode_key]["gods"]] == ["Chiron"]
        assert [i["name"] for i in result[mode_key]["items"]] == ["Deathbringer"]


def test_build_tierlist_legacy_top_level_matches_conquest():
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    core = _core_entry({"A": {"total": 0.6}})
    builds = [_build_group("Chiron", mode="Conquest", builds=[core])]
    items = [{"name": "Deathbringer", "tier": 3, "efficiency_tier": "undervalued"}]
    eff = {"Deathbringer": {"score": 0.81}}

    result = tierlist.build_tierlist(gods, builds, items, eff)

    assert result["gods"] == result["conquest"]["gods"]
    assert result["items"] == result["conquest"]["items"]


def test_build_tierlist_conquest_and_joust_computed_independently():
    # Same god, deliberately different scores per mode, so a bug that
    # accidentally shared state (or always read Conquest) would be caught.
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    conquest_core = _core_entry({"A": {"total": 0.9}})
    joust_core = _core_entry({"A": {"total": 0.1}})
    builds = [
        _build_group("Chiron", mode="Conquest", builds=[conquest_core]),
        _build_group("Chiron", mode="Joust", builds=[joust_core]),
    ]

    result = tierlist.build_tierlist(gods, builds, [], {})

    conquest_chiron = result["conquest"]["gods"][0]
    joust_chiron = result["joust"]["gods"][0]
    assert conquest_chiron["ours"] == pytest.approx(0.9)
    assert joust_chiron["ours"] == pytest.approx(0.1)
    assert conquest_chiron["tier_ours"] == "S"  # sole ranked entry per mode
    assert joust_chiron["tier_ours"] == "S"


def test_build_tierlist_god_with_only_conquest_build_is_unranked_not_absent_in_joust():
    gods = [
        {"name": "Chiron", "role": "Hunter", "damage_type": "Physical"},
        {"name": "Zeus", "role": "Mid", "damage_type": "Magical"},
    ]
    chiron_core = _core_entry({"A": {"total": 0.9}})
    zeus_conquest_core = _core_entry({"A": {"total": 0.5}})
    zeus_joust_core = _core_entry({"A": {"total": 0.4}})
    builds = [
        # Chiron: Conquest only — never scraped for Joust.
        _build_group("Chiron", mode="Conquest", builds=[chiron_core]),
        _build_group("Zeus", mode="Conquest", builds=[zeus_conquest_core]),
        _build_group("Zeus", mode="Joust", builds=[zeus_joust_core]),
    ]

    result = tierlist.build_tierlist(gods, builds, [], {})

    joust_gods = {g["name"]: g for g in result["joust"]["gods"]}
    # Honest behaviour: Chiron is present (not dropped from the list) but
    # unranked, since he genuinely has no Joust data at all.
    assert "Chiron" in joust_gods
    assert joust_gods["Chiron"]["ours"] is None
    assert joust_gods["Chiron"]["tier_ours"] is None
    # Zeus genuinely has Joust data, so he IS ranked.
    assert joust_gods["Zeus"]["ours"] == pytest.approx(0.4)
    assert joust_gods["Zeus"]["tier_ours"] is not None


# ---------------------------------------------------------------------------
# confident_win_rate
#
# Every community score is one aspect's win rate, and aspects differ hugely in
# how much they are played. Raw, the signal was least trustworthy exactly where
# the viewer leaned hardest on it: it ranks "biggest disagreement first", and
# the biggest gaps came from the thinnest samples.
# ---------------------------------------------------------------------------

def test_confident_win_rate_drops_a_barely_played_aspect():
    # 2% pick: the number is a rumour. Unranked, never ranked badly — the same
    # rule assign_tiers uses for a missing score.
    assert tierlist.confident_win_rate(0.36, 0.02) is None
    assert tierlist.confident_win_rate(0.68, 0.02) is None


def test_confident_win_rate_keeps_a_widely_played_aspect_nearly_intact():
    adjusted = tierlist.confident_win_rate(0.64, 0.65)
    # 0.5 + 0.14 * (0.65/0.80) = 0.6138 — most of its distance from even.
    assert adjusted == pytest.approx(0.6138, abs=1e-4)
    assert adjusted > 0.60


def test_confident_win_rate_pulls_a_thin_sample_toward_even():
    # Cupid's real numbers: a 68% win rate on a 5%-pick aspect was the single
    # loudest claim on the home page.
    adjusted = tierlist.confident_win_rate(0.68, 0.05)
    assert adjusted == pytest.approx(0.545, abs=1e-4)
    # Still above even — the signal is discounted, not discarded or inverted.
    assert 0.5 < adjusted < 0.68


def test_confident_win_rate_preserves_direction_and_ordering():
    """Shrinkage must not reorder two aspects of equal confidence."""
    a = tierlist.confident_win_rate(0.60, 0.40)
    b = tierlist.confident_win_rate(0.55, 0.40)
    assert a > b > 0.5
    assert tierlist.confident_win_rate(0.40, 0.40) < 0.5


def test_confident_win_rate_treats_a_missing_pick_rate_as_unusable():
    # Notes predating pick-rate scraping must not be assumed confident.
    assert tierlist.confident_win_rate(0.62, None) is None
    assert tierlist.confident_win_rate(None, 0.40) is None


def test_god_rankings_leaves_a_thinly_played_god_unranked():
    gods = [{"name": "Geb", "role": "Guardian", "damage_type": "Magical"}]
    core = _core_entry({"Gauntlet of Thebes": {"total": 0.51}})
    community = _community_entry(aspect_win_rate=0.36, aspect_pick_rate=0.02)
    builds = [_build_group("Geb", builds=[community, core])]

    result = tierlist.god_rankings(gods, builds)

    assert result[0]["community"] is None
    # Our own score survives: the god is still ranked by the model, it just
    # has nothing trustworthy to be compared against.
    assert result[0]["ours"] == pytest.approx(0.51)
