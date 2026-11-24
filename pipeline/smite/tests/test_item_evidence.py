"""The community record's label for an item only the community buys."""
import ast
from pathlib import Path

import pytest

from smite import hybrid, item_evidence as ie, tierlist

PIPELINE = Path(__file__).resolve().parents[1]


def _entry(played=200, god_win=0.50):
    return {"source": "community", "god_matches_played": played, "god_win_rate": god_win}


def test_under_thirty_estimated_matches_is_too_few_whatever_it_won():
    out = ie.label({"pick_rate": 0.14, "win_rate": 0.90}, _entry())   # ~28 matches
    assert out["matches"] == 28 and out["label"] == ie.TOO_FEW
    assert out["matches_estimated"] is True


def test_under_the_gods_rate_is_below_even_with_a_big_sample():
    assert ie.label({"pick_rate": 0.9, "win_rate": 0.49}, _entry())["label"] == ie.BELOW


def test_at_or_above_with_the_wilson_bound_under_is_not_confident():
    out = ie.label({"pick_rate": 0.5, "win_rate": 0.50}, _entry())    # exactly the god's rate
    assert out["label"] == ie.ABOVE_UNSURE
    assert out["confidence"] == pytest.approx(tierlist.wilson_lower_bound(50, 100))


def test_a_wilson_bound_at_or_above_the_gods_rate_is_confident():
    out = ie.label({"pick_rate": 0.5, "win_rate": 0.75}, _entry())
    assert out["confidence"] >= 0.50 and out["label"] == ie.CONFIDENT


def test_the_estimate_and_bound_are_hybrids_not_a_second_copy():
    out = ie.label({"pick_rate": 0.37, "win_rate": 0.61}, _entry(played=413, god_win=0.55))
    rec = hybrid.item_record(0.61, 0.37, 413)
    assert (out["matches"], out["confidence"]) == (rec["matches"], rec["confidence"])


def test_hybrid_records_are_unchanged_by_the_shared_helper():
    entry = {**_entry(400), "slot_order": [{"name": "X", "win_rate": 0.6, "pick_rate": 1.0}]}
    assert hybrid.community_records(entry)["X"] == {
        "win_rate": 0.6, "pick_rate": 1.0, "matches": 400,
        "confidence": tierlist.wilson_lower_bound(240, 400)}


@pytest.mark.parametrize("rates,entry", [
    ({"pick_rate": 0.0, "win_rate": None}, _entry()),          # "not in the record"
    ({"pick_rate": 0.4, "win_rate": 0.6}, None),
    ({"pick_rate": 0.4, "win_rate": 0.6}, {"god_matches_played": 100}),
])
def test_no_record_is_said_rather_than_guessed(rates, entry):
    assert ie.label(rates, entry)["label"] == ie.NO_RECORD


def test_label_counts_lists_every_label():
    counts = ie.label_counts([{"label": ie.BELOW}, {"label": ie.BELOW}])
    assert counts[ie.BELOW] == 2 and set(counts) == {*ie.LABELS, ie.NO_RECORD}


# ── The boundary: it explains, it never ranks (Jacob, 2026-11-06) ──────────

def _imported_names(path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            names |= {a.name for a in n.names}
        elif isinstance(n, ast.ImportFrom):
            names |= {a.name for a in n.names} | {n.module or ""}
    return names


def test_nothing_in_the_model_imports_this():
    for mod in ("scoring", "assemble", "recommend", "build_index", "efficiency", "hybrid"):
        names = _imported_names(PIPELINE / f"{mod}.py")
        assert not names & {"item_evidence", "smite.item_evidence"}, mod


def test_the_import_guard_still_catches_a_real_import(tmp_path):
    for src in ("from smite import item_evidence", "import smite.item_evidence",
                "from smite.item_evidence import label", "from smite import scoring, item_evidence"):
        f = tmp_path / "m.py"
        f.write_text(src, encoding="utf-8")
        assert _imported_names(f) & {"item_evidence", "smite.item_evidence"}, src
