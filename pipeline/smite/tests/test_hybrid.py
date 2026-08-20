import pytest

from smite import hybrid


def _rows(**quality):
    """Score rows carrying only what hybrid reads: item name and quality."""
    return [{"item": name, "quality": q, "total": q, "tags": []}
            for name, q in sorted(quality.items(), key=lambda kv: -kv[1])]


def _community(god_win_rate=0.50, played=1000, **items):
    """A community entry. `items` maps name -> (win_rate, pick_rate)."""
    return {
        "source": "community",
        "god_win_rate": god_win_rate,
        "god_matches_played": played,
        "slot_order": [{"name": n, "win_rate": w, "pick_rate": p}
                       for n, (w, p) in items.items()],
    }


ITEMS = {n: {"name": n, "stats": {}} for n in
         ("A", "B", "C", "D", "E", "F", "Community", "Weak")}
WEIGHTS = {"hybrid": {"indifference": 0.03, "min_edge": 0.0, "max_swaps": 3}}


# ---------------------------------------------------------------------------
# community_records
# ---------------------------------------------------------------------------

def test_records_derive_a_denominator_from_pick_rate():
    """The source gives no per-item match count, so it is derived."""
    entry = _community(played=1000, Community=(0.60, 0.40))
    rec = hybrid.community_records(entry)["Community"]
    assert rec["matches"] == 400
    assert rec["confidence"] == pytest.approx(
        hybrid.tierlist.wilson_lower_bound(240, 400))


def test_records_are_empty_without_a_denominator():
    """No god match count means nothing can be weighed."""
    assert hybrid.community_records({"slot_order": [{"name": "X", "win_rate": 0.9,
                                                     "pick_rate": 0.9}]}) == {}
    assert hybrid.community_records(None) == {}


def test_records_ignore_a_flat_name_list():
    """A suggested-style entry carries strings, not records."""
    assert hybrid.community_records(
        {"god_matches_played": 500, "slot_order": ["A", "B"]}) == {}


def test_a_thinly_played_item_gets_no_confidence():
    # 1% of 1000 is 10 matches — under the Wilson floor.
    rec = hybrid.community_records(_community(played=1000, Community=(0.90, 0.01)))
    assert rec["Community"]["confidence"] is None


# ---------------------------------------------------------------------------
# hybrid_core
# ---------------------------------------------------------------------------

def test_swaps_in_a_confident_community_pick_the_model_was_indifferent_about():
    core = ["A", "B", "C", "D", "E", "F"]
    rows = _rows(A=.9, B=.8, C=.7, D=.6, E=.5, F=.40, Community=.39)
    entry = _community(god_win_rate=0.50, played=1000, Community=(0.62, 0.50))

    got, swaps = hybrid.hybrid_core(core, rows, entry, ITEMS, WEIGHTS)

    assert "Community" in got
    assert len(swaps) == 1
    assert swaps[0]["added"] == "Community" and swaps[0]["removed"] == "F"
    # The reason has to name the evidence, not just assert a swap happened.
    assert "62%" in swaps[0]["reason"] and "500" in swaps[0]["reason"]


def test_the_models_protected_picks_are_never_overridden():
    """Evidence fills the model's uncertainty, it does not overrule its
    convictions. With 6 slots and protected=3, only the bottom 3 are open — so
    at most 3 swaps can ever land, however much evidence is on offer."""
    core = ["A", "B", "C", "D", "E", "F"]
    rows = _rows(A=.9, B=.8, C=.7, D=.6, E=.5, F=.4,
                 C1=.39, C2=.38, C3=.37, C4=.36, C5=.35)
    items = {**ITEMS, **{n: {"name": n, "stats": {}} for n in ("C1", "C2", "C3", "C4", "C5")}}
    entry = _community(god_win_rate=0.50, played=1000,
                       C1=(0.62, 0.5), C2=(0.62, 0.5), C3=(0.62, 0.5),
                       C4=(0.62, 0.5), C5=(0.62, 0.5))

    got, swaps = hybrid.hybrid_core(core, rows, entry, items,
                                    {"hybrid": {"protected": 3, "max_swaps": 99}})

    assert len(swaps) == 3, "more than the open slots were taken"
    # The model's three strongest picks survive untouched.
    for conviction in ("A", "B", "C"):
        assert conviction in got
    assert {s["removed"] for s in swaps} == {"D", "E", "F"}


def test_protecting_the_whole_core_forbids_every_swap():
    core = ["A", "B", "C", "D", "E", "F"]
    rows = _rows(A=.9, B=.8, C=.7, D=.6, E=.5, F=.4, Community=.39)
    entry = _community(god_win_rate=0.50, played=1000, Community=(0.62, 0.50))

    got, swaps = hybrid.hybrid_core(core, rows, entry, ITEMS, {"hybrid": {"protected": 6}})
    assert got == core and swaps == []


def test_refuses_when_the_item_only_beats_a_fixed_bar_not_the_god():
    """62% is strong on a 50% god and unremarkable on a 65% one. A constant
    threshold cannot tell those apart; the god's own rate can."""
    core = ["A", "B", "C", "D", "E", "F"]
    rows = _rows(A=.9, B=.8, C=.7, D=.6, E=.5, F=.40, Community=.39)

    weak_god = _community(god_win_rate=0.50, played=1000, Community=(0.62, 0.50))
    strong_god = _community(god_win_rate=0.65, played=1000, Community=(0.62, 0.50))

    assert hybrid.hybrid_core(core, rows, weak_god, ITEMS, WEIGHTS)[1] != []
    assert hybrid.hybrid_core(core, rows, strong_god, ITEMS, WEIGHTS)[1] == []


def test_popularity_alone_never_earns_a_swap():
    """A heavily-played item with a losing record must not override anything."""
    core = ["A", "B", "C", "D", "E", "F"]
    rows = _rows(A=.9, B=.8, C=.7, D=.6, E=.5, F=.40, Community=.39)
    entry = _community(god_win_rate=0.50, played=1000, Community=(0.45, 0.95))

    assert hybrid.hybrid_core(core, rows, entry, ITEMS, WEIGHTS)[1] == []


def test_no_community_entry_returns_the_model_core_untouched():
    """Every Joust build takes this path."""
    core = ["A", "B", "C"]
    rows = _rows(A=.9, B=.8, C=.7)
    got, swaps = hybrid.hybrid_core(core, rows, None, ITEMS, WEIGHTS)
    assert got == core and swaps == []


def test_max_swaps_keeps_it_a_correction_not_a_replacement():
    core = ["A", "B", "C", "D", "E", "F"]
    rows = _rows(A=.9, B=.5, C=.5, D=.5, E=.5, F=.5,
                 C1=.5, C2=.5, C3=.5, C4=.5)
    items = {**ITEMS, **{n: {"name": n, "stats": {}} for n in ("C1", "C2", "C3", "C4")}}
    entry = _community(god_win_rate=0.50, played=1000,
                       C1=(0.62, 0.5), C2=(0.62, 0.5), C3=(0.62, 0.5), C4=(0.62, 0.5))

    _, swaps = hybrid.hybrid_core(core, rows, entry, items, {"hybrid": {"max_swaps": 2}})
    assert len(swaps) == 2


def test_assembly_constraints_survive_the_swaps():
    """Boots are capped at one, before and after a correction."""
    core = ["A", "B", "C", "D", "E", "Boots1"]
    rows = _rows(A=.9, B=.8, C=.7, D=.6, E=.5, Boots1=.40, Boots2=.39)
    items = {**ITEMS,
             "Boots1": {"name": "Boots1", "stats": {"Movement Speed": "18"}},
             "Boots2": {"name": "Boots2", "stats": {"Movement Speed": "18"}}}
    entry = _community(god_win_rate=0.50, played=1000, Boots2=(0.62, 0.50))

    got, _ = hybrid.hybrid_core(core, rows, entry, items, WEIGHTS)
    assert sum(1 for n in got if n.startswith("Boots")) <= 1


# ---------------------------------------------------------------------------
# Borrowed evidence (Joust / Arena have no community record of their own)
# ---------------------------------------------------------------------------

def _borrow_items():
    return {n: {"name": n, "stats": {}} for n in ("A", "B", "C", "D", "E", "F", "Late", "Ward", "Fine")}


def test_a_rejected_tag_is_never_swapped_in():
    """Conquest's record is the best evidence about an item, but it is evidence
    about a 30-minute game. `stacking` pays off too late for Arena's ~17.5
    minutes and `ward-economy` answers a problem Arena does not have — so those
    candidates are dropped however good their Conquest record is."""
    rows = _rows(A=0.9, B=0.8, C=0.7, D=0.6, E=0.5, F=0.4,
                 Late=0.1, Ward=0.1, Fine=0.1)
    model = ["A", "B", "C", "D", "E", "F"]
    community = _community(god_win_rate=0.50,
                           Late=(0.70, 0.5), Ward=(0.70, 0.5), Fine=(0.70, 0.5))
    core, swaps = hybrid.hybrid_core(
        model, rows, community, _borrow_items(), WEIGHTS,
        reject_tags=["stacking", "ward-economy"],
        tags_map={"Late": ["stacking"], "Ward": ["ward-economy", "aura"]})
    added = {s["added"] for s in swaps}
    assert "Late" not in added and "Ward" not in added
    assert "Fine" in added, "an untagged candidate with the same record must still fire"


def test_no_reject_list_leaves_every_candidate_eligible():
    """Conquest passes no reject list, so its own behaviour is unchanged."""
    rows = _rows(A=0.9, B=0.8, C=0.7, D=0.6, E=0.5, F=0.4, Late=0.1)
    model = ["A", "B", "C", "D", "E", "F"]
    community = _community(god_win_rate=0.50, Late=(0.70, 0.5))
    _core, swaps = hybrid.hybrid_core(model, rows, community, _borrow_items(), WEIGHTS,
                                      tags_map={"Late": ["stacking"]})
    assert {s["added"] for s in swaps} == {"Late"}


def test_a_borrowed_swap_names_the_mode_the_record_came_from():
    """A Joust build reading "community 63% win over 44 matches" without saying
    whose community would present Conquest's record as if it were measured in
    Joust. That is the one thing this project does not do with unmeasured
    modes."""
    rows = _rows(A=0.9, B=0.8, C=0.7, D=0.6, E=0.5, F=0.4, Fine=0.1)
    model = ["A", "B", "C", "D", "E", "F"]
    community = _community(god_win_rate=0.50, Fine=(0.70, 0.5))
    _core, swaps = hybrid.hybrid_core(model, rows, community, _borrow_items(), WEIGHTS,
                                      borrowed_from="Conquest")
    assert swaps and swaps[0]["reason"].startswith("Conquest community ")
    # ...and an unborrowed one still reads as it always did.
    _c2, s2 = hybrid.hybrid_core(model, rows, community, _borrow_items(), WEIGHTS)
    assert s2[0]["reason"].startswith("community ")


def test_every_mode_that_borrows_names_a_source_that_has_data():
    """`borrow_community.from` pointing at a mode with no community record of
    its own would be a silent no-op."""
    from smite import recommend, scoring
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    modes = weights.get("modes") or {}
    borrowing = {m: cfg["borrow_community"] for m, cfg in modes.items()
                 if (cfg or {}).get("borrow_community")}
    assert borrowing, "expected at least one mode to borrow"
    for mode, cfg in borrowing.items():
        source = cfg.get("from")
        assert source and source.lower() != mode, (mode, source)
        note = recommend.load_build_note("Achilles", source)
        assert any(b.get("source") == "community" for b in note.get("builds", [])), \
            f"{mode} borrows from {source}, which has no community entry"
