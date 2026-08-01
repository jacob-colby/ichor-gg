from smite import rank_diff


def _index(gods):
    return {"tierlist": {"gods": [
        {"name": n, "tier_ours": o, "tier_community": c} for n, o, c in gods]}}


def test_reports_movement_in_both_directions_with_signed_rungs():
    old = _index([("Geb", "A", "C"), ("Cupid", "C", "S")])
    new = _index([("Geb", "S", "C"), ("Cupid", "C", "A")])
    r = rank_diff.diff(old, new)
    assert r["ours"] == [("Geb", "A", "S", 1)]
    # Positive is upward: S is the best rung, so S -> A is a fall of one.
    assert r["community"] == [("Cupid", "S", "A", -1)]


def test_orders_by_size_of_move_then_name():
    old = _index([("Big", "C", "C"), ("Small", "B", "C"), ("Also", "B", "C")])
    new = _index([("Big", "S", "C"), ("Small", "A", "C"), ("Also", "A", "C")])
    assert [r[0] for r in rank_diff.diff(old, new)["ours"]] == ["Big", "Also", "Small"]


def test_an_arrival_is_not_a_movement():
    """A god newly ranked has not 'moved up from C' — it had no placement."""
    r = rank_diff.diff(_index([]), _index([("Hades", "S", "S")]))
    assert r["arrived"] == ["Hades"]
    assert r["ours"] == [] and r["community"] == []


def test_a_departure_is_not_a_movement():
    r = rank_diff.diff(_index([("Hades", "S", "S")]), _index([]))
    assert r["departed"] == ["Hades"]
    assert r["ours"] == []


def test_losing_a_community_placement_is_not_scored_as_a_fall():
    """Going unranked means the source stopped covering it, not that it got
    worse — scoring it as a drop would invent a verdict."""
    old = _index([("Chaac", "B", "A")])
    new = _index([("Chaac", "B", None)])
    r = rank_diff.diff(old, new)
    assert r["community"] == []
    assert r["ours"] == []


def test_unchanged_placements_are_silent():
    same = _index([("Ymir", "A", "B")])
    r = rank_diff.diff(same, same)
    assert r["ours"] == [] and r["community"] == []
    assert r["arrived"] == [] and r["departed"] == []


def test_items_are_a_separate_subject():
    old = {"tierlist": {"gods": [], "items": [
        {"name": "Rage", "tier_ours": "B", "tier_community": "B"}]}}
    new = {"tierlist": {"gods": [], "items": [
        {"name": "Rage", "tier_ours": "S", "tier_community": "B"}]}}
    assert rank_diff.diff(old, new, "items")["ours"] == [("Rage", "B", "S", 2)]
    assert rank_diff.diff(old, new, "gods")["ours"] == []


def test_a_missing_tierlist_yields_no_movement_rather_than_raising():
    assert rank_diff.diff({}, {}) == {
        "ours": [], "community": [], "arrived": [], "departed": []}
