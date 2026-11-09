"""The failure paths matter more than the passing one.

A staleness gate that quietly passes when it cannot derive a value turns a
green tick into evidence of nothing, so most of what is asserted here is that
`doc_audit` FAILS — on an ambiguous anchor, a vanished sentence, a row nobody
claims, a computation that raises. `test_superseded_figures_do_not_match` is
the specific regression this module was written around: the real leakage-free
row is checked against the real patterns, with all seven of its numbers in
place, to prove the anchors cannot pick up a retired one.
"""
import dataclasses
import re
import subprocess

import pytest

from smite import doc_audit, doc_figures


# ── fixtures ──────────────────────────────────────────────────────────────

def _state(rows, section="7. Current numbers"):
    body = "\n".join(f"| {label} | {value} |" for label, value in rows)
    return f"## 1. Something\n\ntext\n\n## {section}\n\n| | |\n|---|---|\n{body}\n"


def _check(row, pattern, compute, **kw):
    return doc_audit.Check(row, pattern, compute, **kw)


def _run(rows, checks, **kw):
    return doc_audit.run(checks=checks, facts=object(),
                         texts={"state": _state(rows)}, ungated={}, **kw)


def _statuses(results):
    return {r["check"].row: r["status"] for r in results}


# ── the happy path, and drift ─────────────────────────────────────────────

def test_matching_figure_is_ok():
    results, _ = _run([("Items", "226")],
                      [_check("Items", r"^(\d+)$", lambda f, d: ("226",))])
    assert _statuses(results) == {"Items": "ok"}


def test_drift_reports_doc_and_computed_side_by_side():
    results, _ = _run([("Items placed", "220 / 220")],
                      [_check("Items placed", r"(\d+) / (\d+)",
                              lambda f, d: ("206", "226"))])
    (result,) = results
    assert result["status"] == "drift"
    assert result["doc"] == "220 / 220"
    assert result["computed"] == "206 / 226"


def test_computed_keeps_the_doc_s_own_phrasing():
    # The failure is read as a diff, so the two lines must differ only where
    # the numbers do — not in wording, spacing or punctuation.
    results, _ = _run(
        [("Community sample", "17,490 Obsidian+ Conquest matches, 28 Jul – 10 Aug")],
        [_check("Community sample",
                r"([\d,]+) (\w+)\+ Conquest matches, (\d+ \w+) – (\d+ \w+)",
                lambda f, d: ("12,786", "Obsidian", "11 Aug", "21 Aug"))])
    assert results[0]["computed"] == (
        "12,786 Obsidian+ Conquest matches, 11 Aug – 21 Aug")


def test_a_readonly_group_feeds_the_computation_without_being_asserted():
    # The leakage-free row states which split it reports; that split is an
    # INPUT to the lookup, not a figure to check against itself.
    seen = {}

    def compute(_facts, doc):
        seen["split"] = doc[1]
        return ("38.4", None)

    results, _ = _run([("Leakage-free", "38.4% at eff 0.45")],
                      [_check("Leakage-free", r"(\d+\.\d+)% at eff (\d\.\d+)", compute)])
    assert seen["split"] == "0.45"
    assert results[0]["status"] == "ok"


# ── the anchor rules ──────────────────────────────────────────────────────

REAL_LEAKAGE_FREE_ROW = (
    "**37.7% probe · 38.4% at eff 0.45, vs 5.7% chance = 6.6–6.7×** — re-run "
    "2026-08-21 on post-refresh data. The previous row (35.5 · 36.7 vs 5.8) was "
    "generated before `chore(data): daily community refresh` and the committed "
    "`_calibration.md` had gone stale with it; the shift is the DATA, measured "
    "by re-running the old weights against it and getting the new numbers "
    "exactly. Earlier history: the eff 0.45 split rose from 34.8% on the "
    "effect-tag pass (see `offense_tags` in `_weights.yaml`); the 37.5% before "
    "that was paid relics entering the denominator (see `is_buildable`)"
)


#: The label-anchored pattern the Leakage-free row was checked with until its
#: figure moved to CURRENT.md (2026-11-09). Kept here because the mechanism it
#: proves — anchor on the figure's own words, never on "the number in this row"
#: — is still what every hand-kept row relies on.
LEAKAGE_FREE_PATTERN = (r"(\d+\.\d+)% probe · (\d+\.\d+)% at eff (\d\.\d+), vs "
                        r"(\d+\.\d+)% chance = (\d+\.\d+)–(\d+\.\d+)×")


def test_superseded_figures_do_not_match():
    """The row holds 35.5, 36.7, 5.8, 34.8 and 37.5 as history. None may win.

    This is the whole reason the patterns anchor on label words rather than on
    "the number in this row": a naive matcher finds 35.5 here and fails a
    document that is perfectly correct.
    """
    results, _ = _run([("Leakage-free", REAL_LEAKAGE_FREE_ROW)],
                      [_check("Leakage-free", LEAKAGE_FREE_PATTERN,
                              lambda f, d: ("37.7", "38.4", None, "5.7", "6.6", "6.7"))])
    assert results[0]["status"] == "ok"
    assert results[0]["doc"].startswith("37.7% probe")


def test_a_second_match_is_ambiguous_and_fails():
    results, _ = _run([("Headline gate", "coverage 47.4%, and once coverage 48.6%")],
                      [_check("Headline gate", r"coverage (\d+\.\d+)%",
                              lambda f, d: ("47.4",))])
    (result,) = results
    assert result["status"] == "ambiguous"
    assert "will not guess" in result["note"]
    assert "<!--now-->" in result["note"]


def test_a_vanished_sentence_is_unlocatable_and_fails():
    results, _ = _run([("Headline gate", "the row was rewritten")],
                      [_check("Headline gate", r"coverage (\d+\.\d+)%",
                              lambda f, d: ("47.4",))])
    assert _statuses(results) == {"Headline gate": "unlocatable"}


def test_a_renamed_row_is_unlocatable_and_fails():
    results, _ = _run([("Gods on roster", "89 of 89")],
                      [_check("Gods tracked", r"(\d+) of (\d+)",
                              lambda f, d: ("89", "89"))])
    assert _statuses(results)["Gods tracked"] == "unlocatable"


def test_the_now_fence_narrows_an_ambiguous_row():
    row = ("<!--now-->coverage 47.4%<!--/now--> — the coverage 48.6% this row "
           "carried was stale")
    results, _ = _run([("Headline gate", row)],
                      [_check("Headline gate", r"coverage (\d+\.\d+)%",
                              lambda f, d: ("47.4",))])
    assert _statuses(results) == {"Headline gate": "ok"}


def test_prose_patterns_span_a_markdown_line_wrap():
    # CLAUDE.md is hard-wrapped and breaks this sentence mid-phrase. Without
    # `prose` the check reports `unlocatable` on a sentence that is right there.
    wrapped = "**Check the register first.** Eleven correct-looking\n   improvements have been implemented, measured, and shipped off."
    pattern = doc_audit.prose(
        r"(\w+) correct-looking improvements have been implemented")
    assert re.search(pattern, wrapped).group(1) == "Eleven"


def test_the_claude_md_check_finds_the_wrapped_sentence():
    check = next(c for c in doc_audit.CHECKS if c.source == "claude")
    text = doc_audit.CLAUDE_PATH.read_text(encoding="utf-8")
    assert len(re.findall(check.pattern, text, re.M)) == 1


# ── nothing is ever quietly dropped ───────────────────────────────────────

def test_uncomputable_becomes_a_finding_not_a_pass():
    def compute(_facts, _doc):
        raise doc_audit.Uncomputable("no observations on disk")

    results, _ = _run([("Combat model", "0.0% worst case")],
                      [_check("Combat model", r"(\d+\.\d+)% worst case", compute)])
    (result,) = results
    assert result["status"] == "uncomputable"
    assert "no observations on disk" in result["note"]


def test_an_unforeseen_exception_becomes_a_finding_not_a_pass():
    def compute(_facts, _doc):
        raise KeyError("community_source")

    results, _ = _run([("Community sample", "17,490 matches")],
                      [_check("Community sample", r"([\d,]+) matches", compute)])
    (result,) = results
    assert result["status"] == "uncomputable"
    assert "KeyError" in result["note"]


def test_a_compute_returning_the_wrong_number_of_values_is_a_finding():
    # `zip` would compare the prefix and pass, leaving the third figure
    # unchecked behind a green tick.
    results, _ = _run([("Build groups", "267 (89 gods × 3 modes)")],
                      [_check("Build groups", r"(\d+) \((\d+) gods × (\d+) modes\)",
                              lambda f, d: ("267", "89"))])
    (result,) = results
    assert result["status"] == "uncomputable"
    assert "drifted apart" in result["note"]


def test_every_failing_status_is_treated_as_a_failure():
    # The one place a new status could be added and silently pass.
    assert set(doc_audit.FAILING) == {
        "drift", "unlocatable", "ambiguous", "uncomputable", "uncovered"}


# ── row coverage ──────────────────────────────────────────────────────────

def test_a_row_no_check_claims_is_reported():
    results, _ = _run([("Items", "226"), ("Brand new row", "17")],
                      [_check("Items", r"^(\d+)$", lambda f, d: ("226",))])
    assert _statuses(results)["Brand new row"] == "uncovered"


def test_an_ungated_row_is_not_reported_as_uncovered():
    results, _ = doc_audit.run(
        checks=[], facts=object(),
        texts={"state": _state([("Cap overflow", "47 -> 29")])},
        ungated={"Cap overflow": "the 47 arm is a counterfactual"})
    assert results == []


def test_ungated_naming_a_row_that_no_longer_exists_is_reported():
    results, _ = doc_audit.run(
        checks=[], facts=object(), texts={"state": _state([("Items", "226")])},
        ungated={"Retired row": "was a judgement"})
    statuses = _statuses(results)
    assert statuses["Retired row"] == "uncovered"
    assert statuses["Items"] == "uncovered"


def test_every_shipped_check_names_a_row_that_exists():
    rows = doc_audit.state_rows(doc_audit.STATE_PATH.read_text(encoding="utf-8"))
    missing = [c.row for c in doc_audit.CHECKS
               if c.in_section_7 and c.row not in rows]
    assert missing == []


def test_a_file_scoped_state_check_is_not_looked_up_as_a_row():
    # §6 states the pipeline test count a second time. It is a STATE.md check
    # but not a §7 row, so row lookup must not claim it is unlocatable.
    text = _state([("Items", "226")]) + "\nTests: smite/tests -q` (691)\n"
    check = _check("§6 test commands", r"-q` \((\d+)\)",
                   lambda f, d: ("691",), scope="file")
    results, _ = doc_audit.run(checks=[check], facts=object(),
                               texts={"state": text}, ungated={})
    assert _statuses(results)["§6 test commands"] == "ok"


def test_a_file_scoped_check_does_not_claim_a_section_7_row():
    # ...and it must not silence the coverage rule for a row of the same name.
    check = _check("Items", r"nothing here (\d+)", lambda f, d: ("1",), scope="file")
    results, _ = doc_audit.run(checks=[check], facts=object(),
                               texts={"state": _state([("Items", "226")])},
                               ungated={})
    assert _statuses(results)["Items"] in {"unlocatable", "uncovered"}
    assert "uncovered" in set(_statuses(results).values())


def test_every_ungated_entry_names_a_row_that_exists():
    rows = doc_audit.state_rows(doc_audit.STATE_PATH.read_text(encoding="utf-8"))
    assert [row for row in doc_audit.UNGATED if row not in rows] == []


def test_the_real_section_7_is_fully_claimed():
    rows = doc_audit.state_rows(doc_audit.STATE_PATH.read_text(encoding="utf-8"))
    claimed = {c.row for c in doc_audit.CHECKS if c.source == "state"}
    assert [r for r in rows if r not in claimed and r not in doc_audit.UNGATED] == []


# ── --skip-model ──────────────────────────────────────────────────────────

def test_skip_model_names_what_it_skipped():
    checks = [_check("Items", r"^(\d+)$", lambda f, d: ("226",)),
              _check("Headline gate", r"coverage (\d+\.\d+)%",
                     lambda f, d: ("47.4",), tier="model")]
    results, skipped = _run([("Items", "226"), ("Headline gate", "coverage 47.4%")],
                            checks, skip_model=True)
    assert [c.row for c in skipped] == ["Headline gate"]
    assert _statuses(results) == {"Items": "ok"}


def test_skip_model_does_not_judge_row_coverage():
    # A model-tier row would otherwise be reported as uncovered purely because
    # its check was filtered out — a false finding is as bad as a missed one.
    results, _ = _run([("Items", "226"), ("Unclaimed", "9")],
                      [_check("Items", r"^(\d+)$", lambda f, d: ("226",))],
                      skip_model=True)
    assert "Unclaimed" not in _statuses(results)


# ── set comparison ────────────────────────────────────────────────────────

def test_flavor_order_is_not_drift():
    results, _ = _run([("Build flavors", "core, model, hybrid")],
                      [_check("Build flavors", r"^(.+)$",
                              lambda f, d: ("hybrid, core, model",), compare="set")])
    assert _statuses(results) == {"Build flavors": "ok"}


def test_an_added_flavor_is_drift():
    results, _ = _run([("Build flavors", "core, model")],
                      [_check("Build flavors", r"^(.+)$",
                              lambda f, d: ("core, model, crit",), compare="set")])
    assert _statuses(results) == {"Build flavors": "drift"}


# ── parsing §7 ────────────────────────────────────────────────────────────

def test_a_bolded_label_is_the_same_row():
    rows = doc_audit.state_rows(_state([("**Leakage-free**", "37.7% probe")]))
    assert rows == {"Leakage-free": "37.7% probe"}


def test_the_header_and_separator_are_not_rows():
    rows = doc_audit.state_rows(_state([("Items", "226")]))
    assert list(rows) == ["Items"]


def test_a_malformed_row_raises_rather_than_being_skipped():
    text = "## 7. Current numbers\n\n| | |\n|---|---|\n| a | b | c |\n"
    with pytest.raises(doc_audit.Uncomputable):
        doc_audit.state_rows(text)


def test_a_missing_section_raises():
    with pytest.raises(doc_audit.Uncomputable):
        doc_audit.state_rows("## 6. Operating it\n\nnothing here\n")


def test_section_7_stops_at_the_next_heading():
    text = _state([("Items", "226")]) + "\n## 8. Later\n\n| Not a row | 9 |\n"
    assert list(doc_audit.state_rows(text)) == ["Items"]


# ── derivations that are their own hazard ─────────────────────────────────

def test_register_entries_counts_the_numbered_list():
    text = ("## 4. Negative results\n\n"
            "1. **One** thing.\n2. **Two** things.\n"
            "   Not an entry.\n11. **Eleven** things.\n\n## 5. Next\n")
    assert doc_audit.register_entries(text) == 3


def test_register_word_matches_the_shipped_register():
    count = doc_audit.register_entries(
        doc_audit.STATE_PATH.read_text(encoding="utf-8"))
    assert doc_audit._register_word(None, ()) == (doc_audit.NUMBER_WORDS[count],)


def test_static_viewer_count_refuses_a_table_driven_test(tmp_path):
    (tmp_path / "a.test.ts").write_text(
        "it.each([[1],[2]])('x', () => {})\n", encoding="utf-8")
    with pytest.raises(doc_audit.Uncomputable, match="each"):
        doc_audit.static_viewer_test_count(tmp_path)


def test_static_viewer_count_refuses_a_modified_declaration(tmp_path):
    (tmp_path / "a.test.ts").write_text("it.skip('x', () => {})\n", encoding="utf-8")
    with pytest.raises(doc_audit.Uncomputable, match="modifiers"):
        doc_audit.static_viewer_test_count(tmp_path)


def test_static_viewer_count_refuses_an_empty_tree(tmp_path):
    with pytest.raises(doc_audit.Uncomputable, match="no viewer test files"):
        doc_audit.static_viewer_test_count(tmp_path)


def test_static_viewer_count_counts_plain_declarations(tmp_path):
    (tmp_path / "a.test.tsx").write_text(
        "describe('g', () => {\n  it('one', () => {})\n  test('two', () => {})\n})\n",
        encoding="utf-8")
    assert doc_audit.static_viewer_test_count(tmp_path) == 2


# `vitest` is the authority; the parser is the fallback. These fix the
# PRECEDENCE, which is the part that decides whether one table-driven file can
# make the gate unusable — one did, for the whole of 2026-09-02.

def test_viewer_count_prefers_vitest_over_the_parser(tmp_path, monkeypatch):
    """The regression: a file the parser MUST refuse still yields a number."""
    (tmp_path / "a.test.tsx").write_text(
        "it.each([[1],[2]])('x', () => {})\n", encoding="utf-8")
    monkeypatch.setattr(doc_audit, "vitest_test_count", lambda _root=None: 18)
    assert doc_audit.viewer_test_count(tmp_path) == 18


def test_viewer_count_falls_back_to_the_parser_without_vitest(tmp_path, monkeypatch):
    (tmp_path / "a.test.tsx").write_text(
        "it('one', () => {})\ntest('two', () => {})\n", encoding="utf-8")
    monkeypatch.setattr(doc_audit, "vitest_test_count", lambda _root=None: None)
    assert doc_audit.viewer_test_count(tmp_path) == 2


def test_viewer_count_still_refuses_when_neither_can_speak(tmp_path, monkeypatch):
    """No vitest AND source the parser does not model: a finding, not a guess."""
    (tmp_path / "a.test.tsx").write_text(
        "it.each([[1],[2]])('x', () => {})\n", encoding="utf-8")
    monkeypatch.setattr(doc_audit, "vitest_test_count", lambda _root=None: None)
    with pytest.raises(doc_audit.Uncomputable, match="each"):
        doc_audit.viewer_test_count(tmp_path)


def test_vitest_count_is_none_when_it_is_not_installed(tmp_path):
    assert doc_audit.vitest_test_count(tmp_path) is None


def test_vitest_count_raises_when_collection_is_broken(tmp_path, monkeypatch):
    """An installed vitest that cannot collect must NOT fall through to the
    parser: that would report a number for a tree whose collection is broken.
    """
    entry = tmp_path / doc_audit.VITEST_ENTRY
    entry.parent.mkdir(parents=True)
    entry.write_text("", encoding="utf-8")
    monkeypatch.setattr(
        doc_audit.subprocess, "run",
        lambda *a, **k: subprocess.CompletedProcess(a, 1, "", "boom"))
    with pytest.raises(doc_audit.Uncomputable, match="collection is broken"):
        doc_audit.vitest_test_count(tmp_path)


def test_placed_counts_only_banded_entries():
    entries = [{"tier_score": "S"}, {"tier_score": None}, {"tier_score": "C"}]
    assert doc_audit.placed(entries) == 2


def test_joust_and_arena_diverging_is_uncomputable():
    facts = type("F", (), {"index": {"tierlist": {
        "joust": {"gods": [{"tier_score": None}, {"tier_score": "A"}]},
        "arena": {"gods": [{"tier_score": None}, {"tier_score": None}]}}}})()
    with pytest.raises(doc_audit.Uncomputable, match="no longer agree"):
        doc_audit._joust_arena(facts, ())


# ── the self-reference ────────────────────────────────────────────────────

def test_the_tests_row_says_why_it_moved():
    """It counts tests, so a commit that adds tests moves it. Say so.

    Three sessions are adding tests in parallel, so this failure will land for
    real — and without the note it reads as the gate being broken on its first
    run rather than as the row and the tests belonging in one commit.
    """
    note = doc_audit._tests_note(("652", "660"), ("661", "660"))
    assert "same commit" in note
    assert "not a bug in the gate" in note


def test_the_tests_note_is_silent_when_the_pipeline_count_held():
    assert doc_audit._tests_note(("652", "660"), ("652", "655")) == ""


# ── classes: DAILY is generated, PATCH and CODE are hand-kept (2026-11-09) ─

def _shipped(row, source="state"):
    return next(c for c in doc_audit.CHECKS if c.row == row and c.source == source)


def test_every_shipped_check_carries_a_class():
    assert {c.cls for c in doc_audit.CHECKS} <= set(doc_audit.CLASSES)
    assert all(c.cls for c in doc_audit.CHECKS)


def test_no_code_figure_is_ever_generated():
    """CODE rows are the ones sessions most often forget. A generator that
    wrote one would make forgetting it free, so none may be generated: every
    CURRENT.md figure is DAILY, and no CODE row's label is a generated one."""
    generated = {f.label for f in doc_figures.FIGURES}
    code = {c.row for c in doc_audit.CHECKS if c.cls == "code"}
    assert code and not code & generated
    assert {"Tests", "Expert claims", "Combat model"} <= code
    for check in doc_audit.CHECKS:
        if check.source == "current":
            assert check.cls == "daily", check.row
        if check.cls in ("code", "patch"):
            assert check.source != "current" and check.vouch is None, check.row


def test_a_code_row_still_fails_loudly():
    tests = dataclasses.replace(_shipped("Tests"), compute=lambda f, d: ("1491", "1016"))
    results, _ = _run([("Tests", "1490 pipeline · 1016 viewer")], [tests])
    (result,) = results
    assert result["status"] == "drift"
    assert "same commit" in result["note"]
    assert result["status"] in doc_audit.FAILING


def test_a_drift_without_its_own_note_says_its_class():
    claims = dataclasses.replace(_shipped("Expert claims"),
                                 compute=lambda f, d: ("5", "3", "2"))
    results, _ = _run([("Expert claims", "4 recorded · 3 resolved · 1 open")], [claims])
    assert results[0]["status"] == "drift"
    assert results[0]["note"] == doc_audit.CLASS_NOTES["code"]


def test_every_generated_figure_is_a_daily_row_that_links_to_it():
    """Both halves, for every figure: §7 has the row and it links here, and
    CURRENT.md is checked for the value. Either alone could rot."""
    rows = doc_audit.state_rows(doc_audit.STATE_PATH.read_text(encoding="utf-8"))
    for figure in doc_figures.FIGURES:
        link = _shipped(figure.label)
        assert link.cls == "daily" and link.pattern == doc_audit.LIVE_LEAD
        assert len(re.findall(link.pattern, rows[figure.label])) == 1, figure.label
        value = _shipped(figure.label, source="current")
        assert value.tier == figure.tier
        assert (value.vouch is not None) == (figure.tier == "model")


def test_a_daily_row_that_loses_its_link_is_unlocatable():
    link = _shipped("Items placed")
    results, _ = _run([("Items placed", "208 / 233 (2026-11-09)")], [link])
    assert results[0]["status"] == "unlocatable"
    assert "CURRENT.md" in results[0]["note"]


def test_the_items_row_survives_a_note_after_its_figure():
    """#127 wrote "233 (2026-11-08: the five base relics …, Was 228)", and
    `^(\\d+)$` then matched nothing."""
    items = dataclasses.replace(_shipped("Items"), compute=lambda f, d: ("233",))
    cell = "233 (2026-11-08: the five base relics … none is buildable. Was 228)"
    results, _ = _run([("Items", cell)], [items])
    assert results[0]["status"] == "ok" and results[0]["doc"] == "233"


def test_the_product_md_sentence_links_to_the_live_figure():
    check = _shipped("leakage-free measure", source="product")
    text = doc_audit.PRODUCT_PATH.read_text(encoding="utf-8")
    assert check.cls == "daily"
    assert len(re.findall(check.pattern, text, re.M)) == 1


# ── CURRENT.md, and the stamp that vouches for it ─────────────────────────

CURRENT = "| Figure | Value |\n|---|---|\n| Headline gate | coverage 51.2% |\n"


def _figure(compute, vouch=None, tier="model", row="Headline gate"):
    return _check(row, r"^(.+)$", compute, source="current", tier=tier,
                  cls="daily", vouch=vouch)


def _run_current(checks, current=CURRENT, **kw):
    return doc_audit.run(checks=checks, facts=object(), ungated={},
                         texts={"state": _state([]), "current": current}, **kw)


def test_a_matching_stamp_vouches_without_re_deriving():
    def compute(_f, _d):
        raise AssertionError("re-derived a figure the stamp vouched for")

    results, _ = _run_current([_figure(compute, vouch=lambda f, t: None)])
    (result,) = results
    assert (result["status"], result["note"]) == ("ok", "current by stamp")


def test_a_stale_stamp_re_derives_and_says_why():
    results, _ = _run_current([_figure(lambda f, d: ("coverage 50.0%",),
                                       vouch=lambda f, t: "the pipeline code differs")])
    (result,) = results
    assert result["status"] == "drift"
    assert result["computed"] == "coverage 50.0%"
    assert "Re-derived because the pipeline code differs" in result["note"]
    assert result["note"].startswith("DAILY")


def test_a_stale_stamp_whose_figures_held_is_ok():
    results, _ = _run_current([_figure(lambda f, d: ("coverage 51.2%",),
                                       vouch=lambda f, t: "the pipeline code differs")])
    assert results[0]["status"] == "ok"


def test_a_stamp_that_cannot_be_verified_vouches_for_nothing():
    def vouch(_f, _t):
        raise OSError("index.json is unreadable")

    results, _ = _run_current([_figure(lambda f, d: ("coverage 50.0%",), vouch=vouch)])
    assert results[0]["status"] == "drift"
    assert "could not be verified" in results[0]["note"]


def test_skip_model_still_reports_what_the_stamp_vouches_for():
    vouched = _figure(lambda f, d: ("x",), vouch=lambda f, t: None)
    results, skipped = _run_current([vouched], skip_model=True)
    assert skipped == [] and results[0]["status"] == "ok"


def test_skip_model_skips_a_figure_the_stamp_cannot_vouch_for():
    stale = _figure(lambda f, d: ("x",), vouch=lambda f, t: "the code differs")
    results, skipped = _run_current([stale], skip_model=True)
    assert [c.row for c in skipped] == ["Headline gate"] and results == []


def test_a_missing_current_file_is_a_finding_not_a_crash():
    results, _ = _run_current([_figure(lambda f, d: ("x",), tier="cheap")], current=None)
    assert results[0]["status"] == "unlocatable"
    assert "does not exist" in results[0]["note"]


def test_a_row_no_generated_figure_writes_is_uncovered():
    typed = CURRENT + "| Typed by hand | 7 |\n"
    results, _ = _run_current([_figure(lambda f, d: ("coverage 51.2%",), tier="cheap")],
                              current=typed)
    assert _statuses(results)["Typed by hand"] == "uncovered"
