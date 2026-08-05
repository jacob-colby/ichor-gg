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

def _indexed(won=200, played=400, analysed=4000):
    """A community entry carrying the god-level record the index publishes."""
    return {
        "source": "community",
        "god_matches_won": won,
        "god_matches_played": played,
        "god_matches_analyzed": analysed,
    }


def test_god_rankings_score_is_the_wilson_bound_on_real_matches():
    """The ranking comes from outcomes, and nothing this project models goes
    into it. It used to be the mean blended score of the six items we picked
    for the god — a number that measured -0.117 against real god strength."""
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    # A core with a very high internal score, which must not reach the output.
    core = _core_entry({"Jotunn's Revenge": {"total": 0.99}})
    builds = [_build_group("Chiron", builds=[_indexed(won=220, played=400), core])]

    result = tierlist.god_rankings(gods, builds)

    assert result == [{
        "name": "Chiron", "role": "Hunter", "damage_type": "Physical",
        "score": pytest.approx(tierlist.wilson_lower_bound(220, 400)),
        "win_rate": pytest.approx(0.55),
        "matches": 400,
        "play_share": pytest.approx(0.1),
    }]


def test_god_rankings_ships_the_raw_rate_beside_the_bound():
    """Both, so a reader can see what confidence cost. The bound is always the
    more conservative of the two."""
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    builds = [_build_group("Chiron", builds=[_indexed(won=220, played=400)])]

    row = tierlist.god_rankings(gods, builds)[0]

    assert row["win_rate"] == pytest.approx(0.55)
    assert row["score"] < row["win_rate"]


def test_god_rankings_falls_back_to_the_aspect_rate_before_the_index_existed():
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    community = _community_entry(aspect_win_rate=0.51)
    builds = [_build_group("Chiron", builds=[community])]

    row = tierlist.god_rankings(gods, builds)[0]

    # Discounted for how much the aspect is actually played, never raw.
    assert row["score"] == pytest.approx(tierlist.confident_win_rate(0.51, 0.45))
    # No denominator to report from the fallback, so none is invented.
    assert row["matches"] is None
    assert row["play_share"] is None


def test_god_rankings_god_with_no_builds_at_all_is_all_none():
    gods = [{"name": "Solo", "role": "Mid", "damage_type": "Magical"}]
    result = tierlist.god_rankings(gods, builds=[])
    assert result == [{
        "name": "Solo", "role": "Mid", "damage_type": "Magical",
        "score": None, "win_rate": None, "matches": None, "play_share": None,
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
    builds = [_build_group("Chiron", mode="Joust", builds=[_indexed()])]

    result = tierlist.god_rankings(gods, builds)

    assert result[0]["score"] is None


# ---------------------------------------------------------------------------
# god_rankings — mode parameter (Task R2: per-mode tier list)
# ---------------------------------------------------------------------------

def test_god_rankings_mode_defaults_to_conquest():
    # Calling with no mode arg must behave exactly like mode="Conquest" —
    # existing callers (and the tests above) rely on this default.
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    builds = [_build_group("Chiron", mode="Conquest", builds=[_indexed()])]

    default_result = tierlist.god_rankings(gods, builds)
    explicit_result = tierlist.god_rankings(gods, builds, mode="Conquest")

    assert default_result == explicit_result
    assert default_result[0]["matches"] == 400


def test_god_rankings_joust_mode_reads_joust_builds_not_conquest():
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    builds = [
        _build_group("Chiron", mode="Conquest", builds=[_indexed(played=400)]),
        _build_group("Chiron", mode="Joust", builds=[_indexed(played=900)]),
    ]

    assert tierlist.god_rankings(gods, builds, mode="Conquest")[0]["matches"] == 400
    assert tierlist.god_rankings(gods, builds, mode="Joust")[0]["matches"] == 900


def test_god_rankings_joust_is_unranked_without_a_community_entry():
    """SmiteBrain publishes no Joust results, so the honest answer for a god
    whose Joust note carries only a suggested build is no placement at all.

    This is the correction: Joust and Arena used to be ranked on the model's
    own score, which is the signal measured at -0.117 against real strength.
    """
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    joust_core = _core_entry({"A": {"total": 0.5}})
    builds = [_build_group("Chiron", mode="Joust", builds=[joust_core])]

    result = tierlist.god_rankings(gods, builds, mode="Joust")

    assert result[0]["score"] is None


def test_god_rankings_god_with_only_a_conquest_build_is_unranked_in_joust():
    # A god that has never had its Joust data scraped at all must still appear
    # in the Joust ranking — unranked, not silently dropped.
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    builds = [_build_group("Chiron", mode="Conquest", builds=[_indexed()])]

    result = tierlist.god_rankings(gods, builds, mode="Joust")

    assert result == [{
        "name": "Chiron", "role": "Hunter", "damage_type": "Physical",
        "score": None, "win_rate": None, "matches": None, "play_share": None,
    }]


# ---------------------------------------------------------------------------
# item_rankings
# ---------------------------------------------------------------------------

def test_item_rankings_ranks_on_the_record_and_carries_value_alongside():
    """`value` is a property of the item, not a competing ranking. Ranked
    against the record it correlated -0.267 with item win rate."""
    items = [
        {"name": "Deathbringer", "tier": 3, "efficiency_tier": "undervalued",
         "meta": {"win_avg": 0.53, "matches": 2000, "matches_won": 1060}},
    ]
    eff = {"Deathbringer": {"score": 0.81}}

    result = tierlist.item_rankings(items, eff)

    assert result == [{
        "name": "Deathbringer", "tier": 3, "efficiency_tier": "undervalued",
        "score": pytest.approx(tierlist.wilson_lower_bound(1060, 2000)),
        "win_rate": 0.53, "matches": 2000, "value": 0.81,
    }]


def test_item_rankings_missing_meta_is_none_score():
    items = [{"name": "Bumba's Spear", "tier": 2, "efficiency_tier": "fair"}]
    eff = {"Bumba's Spear": {"score": 0.4}}

    result = tierlist.item_rankings(items, eff)

    assert result[0]["score"] is None
    assert result[0]["matches"] is None
    # The value figure survives the absence of a record — different question.
    assert result[0]["value"] == 0.4


def test_item_rankings_unpriced_item_has_no_value():
    # e.g. a tier-1 starter, deliberately excluded from the efficiency model
    items = [{"name": "Gilded Arrow", "tier": 1, "efficiency_tier": None}]

    result = tierlist.item_rankings(items, {})

    assert result[0]["value"] is None


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
    assert result["gods"][0]["tier_score"] == "S"
    assert result["items"][0]["name"] == "Deathbringer"
    assert result["items"][0]["tier_score"] == "S"
    # One ranking, from outcomes. The model's own score used to sit beside it
    # as `tier_ours` and lead the site; it measured -0.117 against real god
    # strength, so it is gone rather than demoted.
    assert "tier_ours" not in result["gods"][0]
    assert "ours" not in result["gods"][0]


def test_build_tierlist_empty_inputs():
    from smite import recommend
    result = tierlist.build_tierlist([], [], [], {})
    # Legacy top level, plus one slice per shipped mode. Asserting the mode set
    # against MODES rather than a literal keeps adding a mode from silently
    # shipping a tier list that omits it.
    assert set(result) == {"gods", "items"} | {m.lower() for m in recommend.MODES}
    assert result["gods"] == [] and result["items"] == []
    assert all(result[m.lower()] == {"gods": [], "items": []} for m in recommend.MODES)


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
    # Same god, deliberately different records per mode, so a bug that
    # accidentally shared state (or always read Conquest) would be caught.
    gods = [{"name": "Chiron", "role": "Hunter", "damage_type": "Physical"}]
    builds = [
        _build_group("Chiron", mode="Conquest", builds=[_indexed(won=250, played=400)]),
        _build_group("Chiron", mode="Joust", builds=[_indexed(won=150, played=400)]),
    ]

    result = tierlist.build_tierlist(gods, builds, [], {})

    conquest_chiron = result["conquest"]["gods"][0]
    joust_chiron = result["joust"]["gods"][0]
    assert conquest_chiron["win_rate"] == pytest.approx(0.625)
    assert joust_chiron["win_rate"] == pytest.approx(0.375)
    assert conquest_chiron["tier_score"] == "S"  # sole ranked entry per mode
    assert joust_chiron["tier_score"] == "S"


def test_build_tierlist_god_with_only_conquest_build_is_unranked_not_absent_in_joust():
    gods = [
        {"name": "Chiron", "role": "Hunter", "damage_type": "Physical"},
        {"name": "Zeus", "role": "Mid", "damage_type": "Magical"},
    ]
    builds = [
        # Chiron: Conquest only — never scraped for Joust.
        _build_group("Chiron", mode="Conquest", builds=[_indexed()]),
        _build_group("Zeus", mode="Conquest", builds=[_indexed()]),
        _build_group("Zeus", mode="Joust", builds=[_indexed(won=180, played=400)]),
    ]

    result = tierlist.build_tierlist(gods, builds, [], {})

    joust_gods = {g["name"]: g for g in result["joust"]["gods"]}
    assert set(joust_gods) == {"Chiron", "Zeus"}      # present, not dropped
    assert joust_gods["Chiron"]["score"] is None      # unranked
    assert joust_gods["Chiron"]["tier_score"] is None
    assert joust_gods["Zeus"]["tier_score"] == "S"


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

    # Unranked, never ranked badly: "no usable data" and "bad" are different
    # facts. There is no second score to fall back on any more, and that is
    # the point — the one that used to fill this gap measured -0.117 against
    # real god strength.
    assert result[0]["score"] is None


# ---------------------------------------------------------------------------
# wilson_lower_bound / community_score
#
# The god index publishes wins and losses, so confidence stops being proxied
# by pick rate and starts being measured.
# ---------------------------------------------------------------------------

def test_wilson_bound_ranks_a_big_sample_over_a_lucky_small_one():
    """The whole point: 62% over 2,000 games is a stronger claim than 75%
    over 40, and the raw rate said the opposite."""
    big = tierlist.wilson_lower_bound(1240, 2000)     # 62.0%
    lucky = tierlist.wilson_lower_bound(30, 40)       # 75.0%
    assert big > lucky


def test_wilson_bound_rises_toward_the_observed_rate_as_evidence_accumulates():
    small = tierlist.wilson_lower_bound(62, 100)
    large = tierlist.wilson_lower_bound(6200, 10000)
    assert small < large < 0.62


def test_wilson_bound_refuses_an_unusable_sample():
    assert tierlist.wilson_lower_bound(5, 10) is None        # under MIN_MATCHES
    assert tierlist.wilson_lower_bound(None, 500) is None
    assert tierlist.wilson_lower_bound(500, None) is None
    # Impossible records are dropped, never clamped into a plausible number.
    assert tierlist.wilson_lower_bound(600, 500) is None
    assert tierlist.wilson_lower_bound(-1, 500) is None


def test_community_score_prefers_god_level_wins_over_the_aspect_proxy():
    entry = {
        "god_matches_won": 445, "god_matches_played": 703,
        # A wildly different aspect figure, which must be ignored outright.
        "aspect_win_rate": 0.95, "aspect_pick_rate": 0.90,
    }
    assert tierlist.community_score(entry) == pytest.approx(
        tierlist.wilson_lower_bound(445, 703))


def test_community_score_falls_back_when_the_index_never_ran():
    """A note written before the index scrape still yields something."""
    entry = {"aspect_win_rate": 0.64, "aspect_pick_rate": 0.65}
    assert tierlist.community_score(entry) == pytest.approx(
        tierlist.confident_win_rate(0.64, 0.65))


def test_community_score_of_nothing_is_none():
    assert tierlist.community_score(None) is None
    assert tierlist.community_score({}) is None


def test_god_rankings_uses_the_index_record_when_present():
    gods = [{"name": "Hades", "role": "Mid", "damage_type": "Magical"}]
    core = _core_entry({"Book of Thoth": {"total": 0.52}})
    community = {
        "source": "community",
        "god_matches_won": 445, "god_matches_played": 703,
        "aspect_win_rate": None, "aspect_pick_rate": None,
    }
    builds = [_build_group("Hades", builds=[community, core])]

    result = tierlist.god_rankings(gods, builds)

    # A god with no aspect at all is now ranked — the per-god scrape skipped
    # 18 of these entirely.
    assert result[0]["score"] == pytest.approx(tierlist.wilson_lower_bound(445, 703))


# ---------------------------------------------------------------------------
# _item_community
#
# The old item signal was the mean of per-god win rates over gods whose
# community build happened to list the item: unweighted, so an item in two
# builds counted as loudly as one in forty, and built on the same aspect
# figures the god path moved away from.
# ---------------------------------------------------------------------------

def test_item_community_weighs_the_indexed_record_by_its_denominator():
    big = tierlist._item_community({"win_avg": 0.62, "matches": 20000})
    lucky = tierlist._item_community({"win_avg": 0.70, "matches": 40})
    assert big > lucky


def test_item_community_derives_wins_when_the_source_gives_only_a_rate():
    """Items report win_rate and matches_played but no matches_won."""
    derived = tierlist._item_community({"win_avg": 0.55, "matches": 1000})
    assert derived == pytest.approx(tierlist.wilson_lower_bound(550, 1000))


def test_item_community_prefers_an_explicit_win_count_over_the_rounded_rate():
    meta = {"win_avg": 0.55, "matches": 1000, "matches_won": 553}
    assert tierlist._item_community(meta) == pytest.approx(
        tierlist.wilson_lower_bound(553, 1000))


def test_item_community_passes_the_legacy_average_through_unweighted():
    # No denominator exists to weigh it by, and dropping the item would lose
    # more than it protects.
    assert tierlist._item_community({"win_avg": 0.53, "gods": 29}) == 0.53


def test_item_community_of_nothing_is_none():
    assert tierlist._item_community(None) is None
    assert tierlist._item_community({}) is None
    assert tierlist._item_community({"gods": 4}) is None


def test_item_rankings_uses_the_weighed_score():
    items = [{"name": "Rage", "tier": 3, "efficiency_tier": "fair",
              "meta": {"win_avg": 0.62, "matches": 20000}}]
    result = tierlist.item_rankings(items, {"Rage": {"score": 0.8}})
    assert result[0]["score"] == pytest.approx(
        tierlist.wilson_lower_bound(round(0.62 * 20000), 20000))
