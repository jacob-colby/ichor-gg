"""`docs/CURRENT.md` is generated; what is asserted is that it can be trusted.

Two properties carry the design. The STAMP must mean what it says — a file
whose inputs, code or outputs differ from the tree must never be vouched for,
and the same tree must stamp identically on the Linux runner and on a Windows
checkout, or every Windows session re-derives and the platform question comes
back. And the SHIPPED FILE must be structurally what `doc_figures` writes.

Nothing here pins a figure's value: those move daily, and `tests/live_window.py`
forbids it. `doc_audit` checks the values against the tree.
"""
import types

import pytest

from smite import doc_audit, doc_figures


# ── hashing: platform-neutral, and only over what can move a figure ───────

def test_a_crlf_checkout_hashes_like_the_runner(tmp_path):
    lf, crlf = tmp_path / "lf", tmp_path / "crlf"
    for root, newline in ((lf, b"\n"), (crlf, b"\r\n")):
        (root / "smite").mkdir(parents=True)
        (root / "smite" / "a.py").write_bytes(b"x = 1" + newline + b"y = 2" + newline)
    assert doc_figures.code_hash(lf / "smite") == doc_figures.code_hash(crlf / "smite")


def test_a_code_change_moves_the_code_hash_and_a_test_change_does_not(tmp_path):
    smite = tmp_path / "smite"
    (smite / "tests").mkdir(parents=True)
    (smite / "a.py").write_text("x = 1\n", encoding="utf-8")
    (smite / "tests" / "test_a.py").write_text("t = 1\n", encoding="utf-8")
    before = doc_figures.code_hash(smite)
    (smite / "tests" / "test_a.py").write_text("t = 2\n", encoding="utf-8")
    assert doc_figures.code_hash(smite) == before
    (smite / "a.py").write_text("x = 2\n", encoding="utf-8")
    assert doc_figures.code_hash(smite) != before


def test_a_renamed_file_moves_the_hash(tmp_path):
    smite = tmp_path / "smite"
    smite.mkdir()
    (smite / "a.py").write_text("x = 1\n", encoding="utf-8")
    before = doc_figures.code_hash(smite)
    (smite / "a.py").rename(smite / "b.py")
    assert doc_figures.code_hash(smite) != before


# ── the stamp ─────────────────────────────────────────────────────────────

def _facts(**kw):
    base = dict(fingerprint="a" * 12, code_hash="b" * 12, outputs_hash="c" * 12)
    return types.SimpleNamespace(**{**base, **kw})


def _file(facts, body="| Figure | Value |\n|---|---|\n| Items placed | 1 / 2 |\n"):
    sha = doc_figures._sha(body)
    return (f"{doc_figures.HEADER}<!-- stamp inputs={facts.fingerprint} "
            f"code={facts.code_hash} outputs={facts.outputs_hash} sha={sha} -->\n{body}")


def test_a_stamp_that_matches_the_tree_vouches():
    facts = _facts()
    assert doc_figures.stale_parts(facts, _file(facts)) is None


@pytest.mark.parametrize("field, words", [
    ("code_hash", "pipeline code"),
    ("outputs_hash", "shipped index or build notes"),
    ("fingerprint", "input fingerprint"),
])
def test_each_part_of_a_stale_stamp_is_named(field, words):
    written = _file(_facts())
    reason = doc_figures.stale_parts(_facts(**{field: "f" * 12}), written)
    assert reason and words in reason


def test_a_hand_edited_figure_loses_the_stamp():
    """Otherwise a typed model figure would sit under a stamp that still
    matches, and be vouched for without being re-derived."""
    facts = _facts()
    edited = _file(facts).replace("| 1 / 2 |", "| 9 / 9 |")
    assert "edited by hand" in doc_figures.stale_parts(facts, edited)


def test_a_file_without_a_stamp_vouches_for_nothing():
    assert doc_figures.stale_parts(_facts(), "| Figure | Value |\n") is not None
    assert doc_figures.stale_parts(_facts(), None) is not None


def test_a_hand_edit_is_noticed_before_the_fingerprint_is_paid_for():
    class Facts(types.SimpleNamespace):
        @property
        def fingerprint(self):
            raise AssertionError("loaded the fixture to report a hand edit")

    facts = Facts(code_hash="b" * 12, outputs_hash="c" * 12)
    written = _file(_facts()).replace("| 1 / 2 |", "| 9 / 9 |")
    assert "edited by hand" in doc_figures.stale_parts(facts, written)


# ── rendering ─────────────────────────────────────────────────────────────

def _render_facts():
    facts = _facts()
    facts.index = {"community_source": {"division": "obsidian",
                                        "window_start": "2026-11-03",
                                        "window_end": "2026-11-08",
                                        "matches_analyzed": 5119},
                   "data_patch": "Open Beta 47"}
    facts.community_table = {"window": "ob47"}
    return facts


def test_what_is_written_reads_back_and_vouches(monkeypatch):
    monkeypatch.setattr(doc_figures, "FIGURES", [
        doc_figures.Figure("Items placed", lambda f: "1 / 2"),
        doc_figures.Figure("Headline gate", lambda f: "coverage 3.0%", tier="model")])
    facts = _render_facts()
    text = doc_figures.render(facts)
    assert doc_figures.current_rows(text) == {"Items placed": "1 / 2",
                                              "Headline gate": "coverage 3.0%"}
    assert doc_figures.stale_parts(facts, text) is None
    assert "Community window `ob47`, 3 Nov – 8 Nov 2026, 5,119 matches" in text


def test_rendering_is_deterministic(monkeypatch):
    """No clock and no paths: regenerating an unchanged tree rewrites nothing,
    so a data PR on a day the window did not move carries no CURRENT.md diff."""
    monkeypatch.setattr(doc_figures, "FIGURES",
                        [doc_figures.Figure("Items placed", lambda f: "1 / 2")])
    assert doc_figures.render(_render_facts()) == doc_figures.render(_render_facts())


def test_a_value_a_table_cell_cannot_hold_is_refused(monkeypatch):
    monkeypatch.setattr(doc_figures, "FIGURES",
                        [doc_figures.Figure("Items placed", lambda f: "1 | 2")])
    with pytest.raises(doc_figures.Uncomputable, match="table cell"):
        doc_figures.render(_render_facts())


def test_write_leaves_an_unchanged_file_alone(tmp_path, monkeypatch):
    monkeypatch.setattr(doc_figures, "FIGURES",
                        [doc_figures.Figure("Items placed", lambda f: "1 / 2")])
    path = tmp_path / "CURRENT.md"
    assert doc_figures.write(_render_facts(), path) is True
    assert doc_figures.write(_render_facts(), path) is False
    assert b"\r\n" not in path.read_bytes()


@pytest.mark.parametrize("value", [0.5124999999999999, 0.5125, 0.5125000000000001])
def test_a_mean_on_a_rounding_boundary_rounds_the_same_on_both_platforms(value):
    """Python 3.12 (the runner) sums floats with compensation and 3.10 does
    not, so the same mean can differ in its last ulp. On a .x5 boundary that
    used to be a different digit."""
    assert doc_figures._pct(value) == doc_figures._pct(0.5125)


# ── the shipped file ──────────────────────────────────────────────────────

def test_the_shipped_file_holds_every_figure_in_order_and_nothing_else():
    text = doc_figures.CURRENT_PATH.read_text(encoding="utf-8")
    assert list(doc_figures.current_rows(text)) == [f.label for f in doc_figures.FIGURES]


def test_the_shipped_file_was_not_edited_by_hand():
    stamp = doc_figures.parse_stamp(doc_figures.CURRENT_PATH.read_text(encoding="utf-8"))
    assert stamp is not None
    assert stamp.sha == stamp.body_sha, (
        "docs/CURRENT.md was edited by hand; run `python -m smite.doc_figures --write`")


def test_every_figure_names_a_section_7_row():
    rows = doc_audit.state_rows(doc_audit.STATE_PATH.read_text(encoding="utf-8"))
    assert [f.label for f in doc_figures.FIGURES if f.label not in rows] == []


def test_the_leakage_free_figure_reads_the_controls_fixed_splits():
    """The probe's `model only` corner IS the control's first split, so one
    `calibrate.control` call is the whole figure. If either moves, this
    stops being true and the figure would quietly change meaning."""
    from smite import calibrate

    class Recording:
        def evaluate(self, signals):
            return {}, {"mean_coverage": 0.0}

    probe = calibrate.leakage_probe(Recording())
    (corner,) = [row["signals"] for row in probe if "model only" in row["label"]]
    assert (corner["win"], corner["pick"]) == (0.0, 0.0)
    assert calibrate.CONTROL_SPLITS[0] == (corner["efficiency"], corner["fit"])
    assert doc_figures.REPORTED_SPLIT == (0.45, 0.55)
