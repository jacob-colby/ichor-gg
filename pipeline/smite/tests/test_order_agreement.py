"""The positional buy-order signal and the diagnostic that measures it.

Three things are pinned here and they are different kinds of claim:

  * `scoring.slot_positions` reads the record correctly — slot-reach
    conditioned, both halves separable — which is arithmetic;
  * `assemble.build_order` degrades to the heuristic wherever there is no
    record and is an EXACT no-op at `community_weight` 0.0, which is the
    §4.10 discipline applied to a new flag;
  * `order_agreement` stays a diagnostic and never becomes an input, which is
    the §4.4 discipline applied to a new report.
"""
import ast
import inspect
import re

import pytest

from smite import assemble, build_index, efficiency, order_agreement, recommend, scoring


# -- The record, read positionally -----------------------------------------

def _entry(slots):
    """A community build entry from `[(name, rate, [(alt, rate), ...])]`."""
    return {"source": "community", "slot_order": [
        {"name": name, "pick_rate": rate, "win_rate": 0.5,
         "alternates": [{"name": a, "pick_rate": r, "win_rate": 0.5} for a, r in alts]}
        for name, rate, alts in slots]}


def _note(slots):
    return {"builds": [_entry(slots)]}


def test_slot_positions_puts_a_slot_one_item_at_slot_one():
    pos = scoring.slot_positions(_note([("Tyrfing", 0.51, [])]))
    centroid, mass = pos["Tyrfing"]
    assert centroid == 1.0
    assert mass == pytest.approx(0.51)


def test_an_item_seen_in_several_slots_lands_between_them():
    """The whole reason the data was worth keeping: the same item appears in
    several slots at different rates, and the flattening in
    `build_index.popular_items` throws that away."""
    pos = scoring.slot_positions(_note([
        ("A", 0.5, []), ("B", 0.4, []), ("C", 0.3, [("A", 0.3)]),
    ]))
    centroid, _ = pos["A"]
    assert 1.0 < centroid < 3.0


def test_a_late_sighting_is_conditioned_on_reaching_the_slot():
    """`SLOT_REACH` decays 1.0 -> 0.325, so an uncorrected centroid is pulled
    EARLIER by attrition rather than by preference. Two items bought by the
    same share of the players who got that far must read the same mass."""
    pos = scoring.slot_positions(_note([
        ("Early", scoring.SLOT_REACH[1] * 0.4, []),
        ("B", 0.1, []), ("C", 0.1, []), ("D", 0.1, []), ("E", 0.1, []),
        ("Late", scoring.SLOT_REACH[6] * 0.4, []),
    ]))
    assert pos["Early"][1] == pytest.approx(pos["Late"][1], abs=1e-6)
    assert pos["Late"][0] == pytest.approx(6.0)


def test_the_record_splits_into_picks_and_alternates():
    """The held-out check needs the two halves disjoint, or it is scoring an
    ordering against its own input."""
    note = _note([("Pick", 0.5, [("Alt", 0.2)])])
    assert set(scoring.slot_positions(note, include_alternates=False)) == {"Pick"}
    assert set(scoring.slot_positions(note, include_picks=False)) == {"Alt"}
    assert set(scoring.slot_positions(note)) == {"Pick", "Alt"}


def test_no_community_entry_is_an_empty_record_not_an_error():
    """Joust and Arena notes carry no community entry at all — 180 of the 270
    build groups — and that is the path `build_order` falls back on."""
    assert scoring.slot_positions({"builds": [{"source": "suggested", "slot_order": ["A"]}]}) == {}
    assert scoring.slot_positions({}) == {}


# -- build_order -----------------------------------------------------------

ITEMS = {n: {"name": n, "cost": c, "stats": {}} for n, c in
         [("Cheap", 1000), ("Mid", 2400), ("Dear", 2650)]}
TAGS = {"Cheap": [], "Mid": [], "Dear": []}


def _weights(strength):
    return {"build_order": {"default_stage": 0, "cost_weight": 0.0004,
                            "tag_stage": {}, "community_weight": strength}}


def test_zero_strength_is_the_heuristic_itself_not_arithmetic_that_agrees():
    """§4.10 is what happens when a strength is applied where nothing reads
    it. At 0.0 this returns the heuristic list object's contents unchanged,
    with a record present and contradicting it in every position."""
    positions = {"Dear": (1.0, 1.0), "Cheap": (6.0, 1.0)}
    assert assemble.build_order(list(ITEMS), ITEMS, TAGS, _weights(0.0), positions) \
        == ["Cheap", "Mid", "Dear"]


def test_no_record_leaves_the_heuristic_alone_at_full_strength():
    for positions in (None, {}):
        assert assemble.build_order(list(ITEMS), ITEMS, TAGS, _weights(1.0), positions) \
            == ["Cheap", "Mid", "Dear"]


def test_a_confidently_recorded_item_moves_to_its_own_centroid():
    """The shipped case, and the shape of every offender in the report:
    Shifter's Shield is 2650g and bought FIRST, Genji's Guard is 2350g and
    bought THIRD, and cost-order had them the other way round."""
    positions = {"Dear": (1.0, 1.0), "Cheap": (3.0, 1.0)}
    assert assemble.build_order(list(ITEMS), ITEMS, TAGS, _weights(1.0), positions) \
        == ["Dear", "Mid", "Cheap"]


def test_a_thinly_seen_item_barely_moves():
    """`min(1.0, mass)` is the confidence and is not a free parameter: three
    players trying an item must not outrank the heuristic."""
    positions = {"Dear": (1.0, 0.02)}
    assert assemble.build_order(list(ITEMS), ITEMS, TAGS, _weights(1.0), positions) \
        == ["Cheap", "Mid", "Dear"]


def test_order_never_changes_membership():
    """The claim the whole change rests on. `build_order` receives an already
    assembled core and returns a permutation of it — coverage measures
    membership, so an ordering change that moved membership would be moving a
    gate it has no business touching."""
    core = list(ITEMS)
    positions = {"Dear": (1.0, 1.0), "Cheap": (6.0, 1.0), "Mid": (2.0, 0.5)}
    for strength in (0.0, 0.25, 0.5, 0.75, 1.0):
        out = assemble.build_order(core, ITEMS, TAGS, _weights(strength), positions)
        assert sorted(out) == sorted(core)


def test_community_ordered_is_empty_at_zero_strength():
    """The provenance stamp reads "this position came from the record", and at
    0.0 no position did. Without the gate the flag's no-op would stop being
    one: same order, plus a list naming items nothing had used."""
    positions = {"Dear": (1.0, 1.0)}
    assert assemble.community_ordered(["Dear", "Cheap"], positions, _weights(0.0)) == []
    assert assemble.community_ordered(["Dear", "Cheap"], positions, _weights(1.0)) == ["Dear"]
    assert assemble.community_ordered(["Dear", "Cheap"], {}, _weights(1.0)) == []


# -- The diagnostic --------------------------------------------------------

def test_inversions_counts_a_reversed_pair_and_ignores_an_undecided_one():
    positions = {"First": (1.0, 1.0), "Last": (5.0, 1.0)}
    inverted, orderable, *_ = order_agreement.inversions(["Last", "First"], positions)
    assert (inverted, orderable) == (1, 1)
    assert order_agreement.inversions(["First", "Last"], positions)[0] == 0
    # Centroids closer than a whole slot: the community expressed no preference,
    # so neither order can contradict it.
    close = {"A": (2.0, 1.0), "B": (2.5, 1.0)}
    assert order_agreement.inversions(["B", "A"], close)[1] == 0


def test_inversions_ignores_items_only_one_side_builds():
    """Immunity to membership is what makes this the headline reading rather
    than displacement."""
    positions = {"Ours": (1.0, 1.0)}
    assert order_agreement.inversions(["Ours", "TheirsOnly"], positions)[1] == 0


def test_displacement_is_signed_our_slot_minus_theirs():
    rows = order_agreement.displacements(["A", "B"], {"B": (1.0, 0.8)})
    assert rows == [{"item": "B", "ours": 2, "community": 1.0, "mass": 0.8, "d": 1.0}]


def test_every_report_path_prints_the_caveat_first(capsys):
    """`build_quality` does the same thing for the same reason: the number is
    not the finding, the number under its caveat is."""
    order_agreement.emit(["## a section"])
    out = capsys.readouterr().out
    assert out.startswith("> ")
    assert "NOT a claim about outcomes" in out.splitlines()[0]


_IMPORTS_ORDER_AGREEMENT = re.compile(
    r"^[ \t]*(?:from[ \t]+[\w.]+[ \t]+import[ \t]+[^#]*\border_agreement\b"
    r"|(?:from|import)[ \t]+[\w.]*\border_agreement\b)", re.M)


def test_nothing_in_the_model_imports_the_diagnostic():
    """A report a human reads. `scoring.slot_positions` names it in prose to
    say what the split is for, which is a citation and not a dependency."""
    for mod in (scoring, assemble, recommend, build_index, efficiency):
        assert not _IMPORTS_ORDER_AGREEMENT.search(inspect.getsource(mod)), mod.__name__


def test_the_import_guard_still_catches_a_real_import():
    for src in ("from smite import order_agreement",
                "from smite import scoring, order_agreement",
                "import smite.order_agreement"):
        assert _IMPORTS_ORDER_AGREEMENT.search(src), src
    assert not _IMPORTS_ORDER_AGREEMENT.search(
        "    # see `order_agreement.held_out` for the split")


def test_the_diagnostic_writes_nothing_the_model_reads():
    """It has one file-writing path and it is `--out`. A diagnostic that
    quietly rewrote a build note would be a scoring input with extra steps."""
    tree = ast.parse(inspect.getsource(order_agreement))
    writers = {n.func.attr for n in ast.walk(tree)
               if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
               and n.func.attr in ("write_text", "write_note", "write_bytes", "merge_build_note")}
    assert writers <= {"write_text"}
