"""Check the derivable numbers in `docs/STATE.md` §7 — and the handful of
claims `PRODUCT.md` and `CLAUDE.md` repeat — against the tree they describe.

WHY IT EXISTS. §7 is the project's own summary of where it stands, and it went
stale four times in three weeks, each time caught only because a session
happened to notice: "87 of 89 gods" for weeks after both gods were scraped,
"Six correct-looking improvements" against a register holding eleven, test
counts wrong after most sessions that added tests, a zero-coverage god list
naming three gods the refresh had replaced with two others, and the headline
and leakage-free rows both carrying pre-refresh figures. On the day this was
written three more rows were stale (Community sample, Items placed, Expert
claims), which is the argument for a gate rather than for more diligence.

IT CHECKS. IT DOES NOT REWRITE. Several §7 rows carry prose worth more than
the number in them — the leakage-free row explains that a shift was the DATA
and not a change, names the commit responsible, and keeps the superseded
figures so the history is legible. A regenerator that owns the table would
delete exactly that, and would also delete the moment where a human decides
whether a number moving is expected. So this module only ever reads: it names
the row, prints what the doc says and what the tree says, and stops.

THE FIGURES A DAILY REFRESH MOVES ARE GENERATED, AND THIS STILL ONLY READS
(2026-11-09). From 2026-11-08 the daily community refresh lands on `main` by
itself and edits no document, so every §7 figure it moves went red on `main`
the same morning and every session's merge gate inherited it (#124 moved
seven; #125 and #127 were held open by rows they had not touched). Every check
below therefore carries a CLASS, measured off the snapshot history in
`smite.doc_figures`'s docstring:

  DAILY   moves on an ordinary refresh. Its live value is GENERATED into
          `docs/CURRENT.md` by `smite.doc_figures`, which the refresh runs in
          its own data pull request. Here, the §7 row is only required to link
          to that file, and the file is checked against the tree.
  PATCH   moves at a patch boundary, a stats refresh or a new god or item.
          Hand-kept, checked exactly; moving one declares something.
  CODE    moves only when a commit changes code or a hand-kept file. Hand-kept,
          checked exactly, and loud — the test counts are here, and they are
          the rows sessions most often forget. No CODE figure may be generated;
          a test pins that.

The two objections above are answered rather than overruled. `doc_figures`
writes one file and that file holds no prose, so nothing a human wrote is ever
rewritten: §7's prose stays, and its old "current" figures read as dated
readings. And the human decision survives where there is one to make. A data
move never needed one — the same "moved by the refresh alone" sentence was
written seven times — but a CODE move still fails here, on the branch that
caused it, with the old and new value side by side, until that branch
regenerates the file and its pull request says why.

CURRENT.md's model figures are re-derived only when its stamp — input
fingerprint, code hash, shipped-outputs hash, body checksum — no longer
matches the tree (`doc_figures.stale_parts`). When it matches, the figures are
current by construction and the result reads `current by stamp`. That makes
the common case cheap, and it keeps a file the Linux runner wrote checkable on
a Windows session without recomputing anything that could round differently.

FINDING THE CURRENT FIGURE IN PROSE THAT HOLDS SUPERSEDED ONES. The naive
"grab the number in this row" fails on exactly the rows worth gating: the
leakage-free row contains 37.7, 38.4, 5.7, 35.5, 36.7, 5.8 and 34.8, and only
the first four are current. Three rules make it safe:

  1. Every pattern is ANCHORED ON THE FIGURE'S OWN LABEL WORDS — `% probe`,
     `% at eff 0.45`, `vs % chance` — never on the row. The superseded figures
     sit in prose as `(35.5 · 36.7 vs 5.8)` and `rose from 34.8% on the
     effect-tag pass`, carrying no anchor, so they cannot match.
  2. A pattern must match EXACTLY ONCE in its scope. Zero matches is
     `unlocatable`, two or more is `ambiguous`, and BOTH FAIL. The gate never
     picks between candidates; a row whose prose grows a second matching
     figure stops the build instead of silently reporting the wrong one.
  3. When a row does become ambiguous, the fix is `<!--now-->…<!--/now-->`
     around the current figure. It is invisible in rendered Markdown, it does
     not duplicate the value — the number still lives exactly once, in the
     prose — and this module narrows its search to the fence when one is
     present. No row needs it today; the `ambiguous` message names it.

FAILING LOUDLY IS THE WHOLE POINT. A staleness gate that passes when it could
not derive a value converts a green tick into evidence of nothing, which is
the bug `expert_review.regressions` shipped on an unrecognised `last_verdict`
and its docstring is about. So: a row this module does not claim is a finding
(`uncovered`); an UNGATED entry naming a row that no longer exists is a
finding; a computation that raises is a finding (`uncomputable`) and is never
swallowed; and `--skip-model` prints the rows it skipped by name.

THE TESTS ROW COUNTS TESTS, INCLUDING ITS OWN. A commit that adds tests must
therefore also bump that row, in the same commit. That is the correct
behaviour and not a defect in the gate — three sessions running in parallel
all add tests, so it will fire for real — and `_tests_note` says so in the
failure output, because it otherwise reads as the gate being broken.

COUNTED BY THE THING THAT GENERATES THEM. Both test counts come from a
COLLECTION — `pytest --collect-only`, `vitest list` — and never from a regex
over source, because a regex cannot see a case a table generates. It was
tried: a static viewer counter was exact until `methodSeam.test.tsx` arrived
with an `it.each`, at which point the counter correctly REFUSED, which left
three rows unverifiable and the gate red on every run. While it was blind the
viewer figure drifted to 681 against an actual 765 and two sessions
rediscovered that independently. `static_viewer_test_count` survives only as
the fallback for a worktree with no `node_modules`, keeping its refusals;
`vitest_test_count` goes first wherever it can run.

ONE DATED READING IS READ, FOR ITS WINDOW ONLY, AND IT CAN ONLY WARN
(2026-11-09). A new patch's community window lands with the daily refresh and
nobody declares it (Jacob, 2026-11-08), so §7's hand-written Community sample
row can be a window behind the data for as long as nobody writes the new
window's first reading. That is not drift: the live figure is in CURRENT.md,
in the same pull request as the data. So the check on the row's NEWEST reading
(the first figure after its link) asks only which window it describes. The
shipped one is `ok`, and its consistency with the table is `test_side_by_side`'s,
which keeps #123's checks for exactly that case. An OLDER one is a `warning`,
printed by `--check` and never failing it. A NEWER one is drift, because the
doc then claims data the tree does not have. A `warning` is the only status
that does not fail, and only a check raising `Advisory` produces one.

WHAT IS DELIBERATELY NOT GATED is in `UNGATED`, with a reason each. The short
version: counterfactuals that cannot be re-derived without flipping a weight
and re-running (the `47 ->` arm of Cap overflow), judgements rather than
measurements (`1 open by decision`), facts about the world rather than about
this tree (`no outcome data exists`), and all explanatory prose — which, in a
DAILY row, now includes every dated reading. PRODUCT.md's "~7x better than
chance" is a rounded claim, not a figure, and is not gated; the sentence is
required to link to the live figure instead.

    python -m smite.doc_audit               # every row: doc value beside computed value
    python -m smite.doc_audit --check       # failures and warnings; non-zero exit on drift only
    python -m smite.doc_audit --skip-model  # cheap rows only; skipped rows named, never silent
"""
import argparse
import datetime as dt
import functools
import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import yaml

from . import calibrate_combat, combat, data_audit, doc_figures, scoring
# Re-exported: these were defined here before the DAILY figures moved to
# `doc_figures`, and other modules and tests still reach them through here.
from .doc_figures import (  # noqa: F401
    CURRENT_PATH, INDEX_PATH, PIPELINE_ROOT, REPO_ROOT, WEIGHTS_PATH, _day, _pct,
    over_penetration_cap, placed)

STATE_PATH = REPO_ROOT / "docs" / "STATE.md"
PRODUCT_PATH = REPO_ROOT / "PRODUCT.md"
CLAUDE_PATH = REPO_ROOT / "CLAUDE.md"
VIEWER_ROOT = REPO_ROOT / "viewer"
VIEWER_SRC = VIEWER_ROOT / "src"
TAGS_PATH = REPO_ROOT / "data" / "_tags.yaml"
REVIEWS_PATH = REPO_ROOT / "data" / "_expert_reviews.yaml"

#: The classes every check carries; see the module docstring.
CLASSES = ("daily", "patch", "code")

#: Said on a finding, so the reader knows what kind of move it is before
#: deciding what to do about it.
CLASS_NOTES = {
    "daily": ("DAILY: generated into docs/CURRENT.md by `python -m "
              "smite.doc_figures --write`, never typed. If this branch changed "
              "code or weights, your change moved it: regenerate, and say why in "
              "the pull request. If it did not, the data commit that put this "
              "tree here skipped the generator."),
    "patch": ("PATCH: moves at a patch boundary, a stats refresh, or when a god "
              "or item is added. Re-take it by hand. If `origin/main` shows the "
              "same finding, it arrived with that data commit, not this branch."),
    "code": ("CODE: moves only when a commit changes code or a hand-kept file; "
             "the commit that moved it updates this row in the same commit."),
}

#: What a DAILY §7 row must open with: a link to where its live figure lives.
LIVE_LEAD = r"\*\*Live in \[CURRENT\.md\]\(CURRENT\.md\)\.\*\*"

#: §7's Community sample row, its NEWEST dated reading: the first figure after
#: the live lead, because the row's readings run newest first. Anchored there,
#: not searched for, so the older readings behind it, written in the same
#: words, can never make it ambiguous.
COMMUNITY_READING = (LIVE_LEAD + r"[^0-9|]*?([\d,]+) (\w+)\+ Conquest matches, "
                     r"(\d+ \w+) – (\d+ \w+)")


def community_reading(cell: str):
    """`(count, division, start, end)` of the Community sample row's newest
    reading as written, e.g. `('5,119', 'Obsidian', '3 Nov', '8 Nov')`, or None."""
    match = re.search(COMMUNITY_READING, cell or "")
    return match.groups() if match else None


def day_near(day_month: str, anchor: dt.date) -> dt.date:
    """A `d Mon` a row writes without a year, in the year that puts it nearest
    `anchor`. Patch windows are 14 days long, so the choice is never close,
    and a window that crosses New Year reads right."""
    candidates = [dt.datetime.strptime(f"{day_month} {year}", "%d %b %Y").date()
                  for year in (anchor.year - 1, anchor.year, anchor.year + 1)]
    return min(candidates, key=lambda d: abs((d - anchor).days))

#: Narrows a row's search scope. Absent from every row today; see the module
#: docstring for when to add one.
NOW_FENCE = re.compile(r"<!--now-->(.*?)<!--/now-->", re.S)

NUMBER_WORDS = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
    7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
    13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
    17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
    21: "Twenty-one", 22: "Twenty-two", 23: "Twenty-three", 24: "Twenty-four",
    25: "Twenty-five", 26: "Twenty-six", 27: "Twenty-seven",
    28: "Twenty-eight", 29: "Twenty-nine", 30: "Thirty",
    31: "Thirty-one", 32: "Thirty-two", 33: "Thirty-three",
    34: "Thirty-four", 35: "Thirty-five", 36: "Thirty-six",
    37: "Thirty-seven", 38: "Thirty-eight", 39: "Thirty-nine", 40: "Forty",
}
# Above twenty the word is hyphenated, so the two register checks below read
# `[\w-]+` rather than `\w+` — with `\w+` a doc saying "Twenty-one" audited as
# "one" and drifted against itself (2026-09-02, the day the register reached 21).

#: §7 rows, and parts of rows, that are deliberately not checked. Every entry
#: names a row that must exist — an entry for a row that has been renamed or
#: deleted is itself a finding, so this list cannot rot into an alibi.
UNGATED = {
    "Adaptive pricing": (
        "a record of what `price_adaptive` did on the day it shipped — 8 items "
        "repriced, 83 of 89 cores changed. Re-deriving it needs the flag "
        "flipped and assembly re-run against a build set that no longer "
        "exists, so it is history rather than current state."),
    "Cap overflow": (
        "the `47 ->` arm is the count with `cap_overflow` OFF — a counterfactual "
        "that cannot be re-derived without flipping a weight and re-running "
        "assembly, and a historical before rather than current state. The "
        "current count is DAILY and is generated into CURRENT.md."),
    "Joust / Arena gods placed": (
        "`no outcome data exists` is a fact about the world, not a measurement "
        "of this tree. The `0 / 89` IS checked."),
    "Expert claims": (
        "`(1 open by decision)` is a judgement about WHY a claim is open. The "
        "three counts ARE checked."),
    "Headline gate": (
        "every dated reading and its attribution is prose about a past state. "
        "The two current figures are DAILY and are generated into CURRENT.md."),
    "Leakage-free": (
        "the re-run dates, the named commits, the dated readings, the OB47 "
        "first look and the caveats are the reason this row is worth reading. "
        "The four current figures are DAILY and are generated into CURRENT.md."),
    "Gods at 0% coverage": (
        "each dated list, and who left or joined it, is history. The current "
        "count and names are DAILY and are generated into CURRENT.md."),
}


#: Raised by a `compute` when it cannot honestly produce a value. Never caught
#: anywhere that would turn it into a pass: `run` converts it into a finding,
#: which fails `--check` exactly like a mismatch does. One class shared with
#: `doc_figures`, so a figure computed there is refused here the same way.
Uncomputable = doc_figures.Uncomputable


class Advisory(Exception):
    """Raised by a `compute` for what a reader should know that is not drift:
    the doc is not wrong, only behind. `run` makes it a `warning`, which
    `--check` prints and never fails on. See "ONE DATED READING" above."""


# ── the tree's own numbers ────────────────────────────────────────────────

class Facts(doc_figures.Facts):
    """Everything the checks read, computed at most once and only if asked.

    The index, the validation run, the control and the stamp hashes come from
    `doc_figures.Facts`, so a generated figure and its check are derived by
    the same code. Laziness is what makes `--skip-model` and a matching stamp
    cost nothing: the expensive properties are never touched when nothing
    asks for them.
    """

    @functools.cached_property
    def combat_result(self) -> dict:
        real, _examples, _pending = calibrate_combat.load_observations(
            calibrate_combat.DEFAULT_PATH)
        if not real:
            raise Uncomputable(
                f"no real observations in {calibrate_combat.DEFAULT_PATH.name}")
        return combat.calibrate_report(real)

    @functools.cached_property
    def reviews(self) -> list:
        doc = yaml.safe_load(REVIEWS_PATH.read_text(encoding="utf-8")) or {}
        return doc.get("reviews") or []

    @functools.cached_property
    def tag_audit(self):
        items = self.index["items"]
        findings, reviewed_empty = data_audit.audit_tags(
            items, scoring.load_tags(TAGS_PATH))
        buildable = sum(1 for it in items if scoring.is_buildable(it))
        untagged = sum(1 for f in findings if f["issue"] == "untagged-item")
        return {"buildable": buildable, "reviewed_empty": reviewed_empty,
                "untagged": untagged,
                "tagged": buildable - reviewed_empty - untagged}


def register_entries(state_text: str) -> int:
    """Numbered entries in the §4 negative-results register.

    Counted off the register itself rather than kept as a number anywhere,
    because the drift this catches — CLAUDE.md saying "Six" and PRODUCT.md
    saying "Nine" against a register holding eleven — is precisely a number
    kept in a second place.
    """
    section = _section(state_text, "4")
    return len(re.findall(r"^\d+\. \*\*", section, re.M))


def pipeline_test_count() -> int:
    """`pytest --collect-only` — the real number, not a regex over source.

    Shells out rather than importing pytest's collector so that running this
    module's own tests under pytest cannot recurse.
    """
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "smite/tests", "-q", "--collect-only"],
        cwd=PIPELINE_ROOT, capture_output=True, text=True)
    match = re.search(r"(\d+) tests? collected", proc.stdout)
    if proc.returncode != 0 or not match:
        raise Uncomputable(
            "pytest --collect-only did not report a count "
            f"(exit {proc.returncode}); collection is broken, fix that first")
    return int(match.group(1))


#: A bare `it(` / `test(` at the start of a line. Anything fancier is refused
#: rather than guessed at — see `static_viewer_test_count`.
VIEWER_TEST = re.compile(r"^[ \t]*(?:it|test)\s*\(", re.M)
VIEWER_TEST_MODIFIER = re.compile(r"^[ \t]*(?:it|test)\.[a-zA-Z]+\s*\(", re.M)
VIEWER_TEST_FILE = re.compile(r"\.test\.[a-z]+$")


def _short(path: Path) -> str:
    """Repo-relative when it can be, absolute otherwise (a tmp_path in tests)."""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def static_viewer_test_count(root: Path = VIEWER_SRC) -> int:
    """Viewer tests, counted statically off the source. The FALLBACK.

    `vitest` is the authority and `vitest_test_count` asks it. This exists for
    the tree that cannot be asked — a fresh worktree has no `node_modules` —
    so the gate still says something where the toolchain is absent.

    Exact only while every declaration is a bare one. It stops being exact the
    moment a table-driven or modified declaration appears, so both are REFUSED
    rather than miscounted: `it.each` generates a row per case and `it.skip`
    still counts as collected, so either would make this number quietly wrong,
    and a quietly wrong staleness gate is worse than none. Refusing is what
    kept the count honest between 2026-09-02 and this commit; what it could
    not do was produce the number, which is why the authority now goes first.
    """
    total, files = 0, 0
    for path in sorted(root.rglob("*")):
        if not VIEWER_TEST_FILE.search(path.name):
            continue
        files += 1
        text = path.read_text(encoding="utf-8")
        if ".each" in text:
            raise Uncomputable(
                f"{_short(path)} uses a `.each` table — this static count cannot "
                "see how many cases it generates, and `vitest` — which can — is "
                f"not installed under {_short(VIEWER_ROOT)}. Run `npm ci` there "
                "and the count is exact; do not let this one guess.")
        modifier = VIEWER_TEST_MODIFIER.search(text)
        if modifier:
            raise Uncomputable(
                f"{_short(path)} uses `{modifier.group(0).strip()}` — this static "
                "count does not model modifiers. See above.")
        total += len(VIEWER_TEST.findall(text))
    if not files:
        raise Uncomputable(f"no viewer test files under {root}")
    return total


#: `vitest`'s own entry point, relative to the viewer. Invoked through `node`
#: rather than through `node_modules/.bin`, whose shim is a shell script on
#: POSIX and a `.cmd` on Windows; `node` on the module runs the same either way.
VITEST_ENTRY = Path("node_modules") / "vitest" / "vitest.mjs"


@functools.cache
def vitest_test_count(viewer_root: Path = VIEWER_ROOT) -> int | None:
    """What `vitest` itself collects, or `None` where it cannot be asked.

    THE AUTHORITY, and the counterpart of `pipeline_test_count` above: `vitest
    list` COLLECTS without running, exactly as `pytest --collect-only` does, so
    this costs a collection and not a suite. It sees table-driven cases because
    it is the thing that generates them.

    Returns `None` rather than raising when `vitest` is not installed, because
    that is the bare-worktree case `static_viewer_test_count` exists to cover
    and not a broken tree. A `vitest` that IS installed and then fails to
    collect is a finding, for the same reason a broken `pytest --collect-only`
    is one: falling back there would report a number for a tree whose
    collection does not work.

    Cached because three rows check this figure and each collection is seconds.
    """
    if not (viewer_root / VITEST_ENTRY).exists():
        return None
    with tempfile.TemporaryDirectory() as tmp:
        listing = Path(tmp) / "tests.json"
        try:
            proc = subprocess.run(
                ["node", str(VITEST_ENTRY), "list", f"--json={listing}"],
                cwd=viewer_root, capture_output=True, text=True)
        except OSError:
            return None                    # no `node` on PATH: also unaskable
        if proc.returncode != 0 or not listing.exists():
            raise Uncomputable(
                f"`vitest list` did not collect (exit {proc.returncode}); "
                "viewer collection is broken, fix that first — "
                + " ".join((proc.stderr or proc.stdout).split())[-300:])
        return len(json.loads(listing.read_text(encoding="utf-8")))


def viewer_test_count(root: Path = VIEWER_SRC,
                      viewer_root: Path = VIEWER_ROOT) -> int:
    """Viewer tests: `vitest`'s number where it can be had, the parser's where
    it cannot, and a refusal where neither can speak.

    The two counters answer different questions and the precedence is the whole
    point. `vitest` is definitionally right; the parser is right only about
    source it fully models, and says so. Neither ever guesses, so the gate can
    still only be green on a number something measured.
    """
    counted = vitest_test_count(viewer_root)
    return static_viewer_test_count(root) if counted is None else counted


def _tests_note(doc: tuple, computed: tuple) -> str:
    """Said out loud because this failure reads as the gate being broken.

    It is not: this check counts tests, so a commit that adds tests moves the
    number it is checking. The row and the tests belong in the same commit.
    """
    if doc[0] == computed[0]:
        return ""
    return ("this check counts tests, so a commit that ADDS tests must update "
            "this row in the same commit — that is intended, not a bug in the gate")


# ── the checks ────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Check:
    """One figure (or group of figures) in one row.

    `pattern` must match its scope exactly once — see the module docstring.
    `compute` receives the groups the doc gave and returns what they should
    be; a `None` in the returned tuple means "read, not checked", which is how
    an input like the reported eff split feeds the computation without being
    asserted against itself.

    `cls` is DAILY, PATCH or CODE (see the module docstring), and says on a
    finding what kind of move it is. `vouch`, when set, is asked before
    `compute`: it returns None when the figure is current by construction (a
    CURRENT.md stamp that still matches the tree), in which case nothing is
    re-derived, or the reason it cannot vouch, in which case it is. `hint`
    is said when the pattern cannot be found.
    """
    row: str
    pattern: str
    compute: Callable[[Facts, tuple], tuple]
    source: str = "state"           # 'state' | 'current' | 'product' | 'claude'
    tier: str = "cheap"
    compare: str = "exact"          # 'exact' | 'set'
    scope: str = "row"              # 'row' (a §7 or CURRENT.md cell) | 'file'
    note: Callable[[tuple, tuple], str] = field(default=lambda doc, got: "")
    cls: str = ""
    vouch: Callable[[Facts, str], object] = None
    hint: str = ""

    @property
    def in_section_7(self) -> bool:
        return self.source == "state" and self.scope == "row"

    @property
    def in_current(self) -> bool:
        return self.source == "current" and self.scope == "row"

    @property
    def where(self) -> str:
        if self.source == "state":
            return "STATE.md §7" if self.scope == "row" else "STATE.md"
        return {"current": "CURRENT.md", "product": "PRODUCT.md",
                "claude": "CLAUDE.md"}[self.source]


def prose(pattern: str) -> str:
    """Let a pattern span a Markdown line wrap.

    A §7 row is one line, but `CLAUDE.md` is hard-wrapped at 78 columns and its
    register claim breaks between "correct-looking" and "improvements". A
    pattern with a literal space there matches nothing, and `unlocatable` is
    the right failure only when the sentence is really gone — not when it moved
    a word onto the next line.
    """
    return re.sub(r" ", r"\\s+", pattern)


def _joust_arena(facts: Facts, _doc: tuple) -> tuple:
    tierlist = facts.index["tierlist"]
    counts = {mode: placed(tierlist[mode]["gods"]) for mode in ("joust", "arena")}
    totals = {mode: len(tierlist[mode]["gods"]) for mode in ("joust", "arena")}
    if len(set(counts.values())) != 1 or len(set(totals.values())) != 1:
        raise Uncomputable(
            f"Joust and Arena no longer agree ({counts}, of {totals}) — the row "
            "states one figure for both and can no longer be derived as one")
    return (str(counts["joust"]), str(totals["joust"]))


def _register_word(_facts: Facts, _doc: tuple) -> tuple:
    """The §4 register's own entry count, spelled the way the prose spells it.

    Both `CLAUDE.md` and `PRODUCT.md` state this number in words, and both have
    been wrong about it — "Six" and "Nine" against a register holding eleven.
    """
    count = register_entries(STATE_PATH.read_text(encoding="utf-8"))
    if count not in NUMBER_WORDS:
        raise Uncomputable(
            f"the register holds {count} entries and NUMBER_WORDS stops at "
            f"{max(NUMBER_WORDS)} — extend it")
    return (NUMBER_WORDS[count],)


def _live_lead(label: str) -> "Check":
    """A DAILY §7 row: it must open by linking to its live figure.

    The figure itself is checked in CURRENT.md, so here there is nothing to
    compare — the pattern has no groups — only something that must be found
    exactly once. A row that loses its link is `unlocatable`, and a row that
    nobody claims is `uncovered`, so a DAILY row cannot quietly become a
    hand-kept one again and start going stale.
    """
    return Check(label, LIVE_LEAD, lambda f, d: (), cls="daily",
                 hint=("this row's live figure is generated into docs/CURRENT.md; "
                       "the row must open with `**Live in [CURRENT.md](CURRENT.md).**`"))


def _community_window(facts: Facts, doc: tuple) -> tuple:
    """PATCH. Which window §7's newest Community sample reading describes,
    against the window the shipped table is: the same is `ok`, an older one a
    warning (`Advisory`), a newer one drift. See "ONE DATED READING" in the
    module docstring."""
    _count, _division, start, _end = doc
    table = facts.community_table
    shipped = dt.date.fromisoformat(table["window_start"])
    row = day_near(start, shipped)
    if row == shipped:
        return (None, None, None, None)
    if row < shipped:
        raise Advisory(
            f"not drift: the newest reading is the window that started {start}; "
            f"the shipped window `{table.get('window')}` started "
            f"{_day(table['window_start'])}. The live figure is in CURRENT.md and "
            f"is current. A new window lands by itself (Jacob, 2026-11-08); give "
            f"this row a dated reading of it when you next touch the row.")
    return (None, None, _day(table["window_start"]), None)


def _generated(figure: doc_figures.Figure) -> "Check":
    """One CURRENT.md figure, re-derived exactly as `doc_figures` derives it.

    Model-tier figures are vouched for by the stamp when it still matches the
    tree; cheap ones are always re-derived, because they cost nothing and a
    hand edit is then caught however the stamp reads.
    """
    return Check(figure.label, r"^(.+)$",
                 lambda f, d, figure=figure: (figure.render(f),),
                 source="current", tier=figure.tier, cls="daily",
                 vouch=doc_figures.stale_parts if figure.tier == "model" else None,
                 hint="run `python -m smite.doc_figures --write`")


CHECKS = [
    Check("Gods tracked", r"(\d+) of (\d+) on the roster",
          lambda f, d: (str(len(f.index["gods"])), str(len(f.index["roster"]))),
          cls="patch"),
    # `\b`, not `$`: #127 annotated this cell ("233 (2026-11-08: the five base
    # relics …)"), and the figure must survive a note after it.
    Check("Items", r"^(\d+)\b",
          lambda f, d: (str(len(f.index["items"])),), cls="patch"),
    Check("Build groups", r"(\d+) \((\d+) gods × (\d+) modes\)",
          lambda f, d: (str(len(f.index["builds"])), str(len(f.index["gods"])),
                        str(len(f.index["modes"]))),
          cls="patch"),
    Check("Joust / Arena gods placed", r"(\d+) / (\d+)", _joust_arena, cls="patch"),
    Check("Combat model", r"(\d+\.\d+)% worst case over (\d+) observations",
          lambda f, d: (f"{f.combat_result['worst_rel_error'] * 100:.1f}",
                        str(f.combat_result["n"])),
          cls="code"),
    Check("Expert claims", r"(\d+) recorded · (\d+) resolved · (\d+) open",
          lambda f, d: (
              str(len(f.reviews)),
              str(sum(1 for r in f.reviews if r.get("status") == "resolved")),
              str(sum(1 for r in f.reviews if r.get("status") == "open"))),
          cls="code"),
    # PATCH, because a new item arrives untagged and a stats refresh can flip
    # buildability; a session tagging an item moves it too.
    Check("Item effect-tag coverage",
          r"(\d+) of (\d+) buildable tagged · (\d+) reviewed, no tag warranted "
          r"· (\d+) unreviewed",
          lambda f, d: (str(f.tag_audit["tagged"]), str(f.tag_audit["buildable"]),
                        str(f.tag_audit["reviewed_empty"]),
                        str(f.tag_audit["untagged"])),
          cls="patch"),
    Check("Tests", r"(\d+) pipeline · (\d+) viewer",
          lambda f, d: (str(pipeline_test_count()), str(viewer_test_count())),
          note=_tests_note, cls="code"),

    # ── DAILY: §7 links to the live figure; CURRENT.md holds it ──────────
    *[_live_lead(figure.label) for figure in doc_figures.FIGURES],
    *[_generated(figure) for figure in doc_figures.FIGURES],
    # After the DAILY block, so the row's first check is still its live lead.
    Check("Community sample", COMMUNITY_READING, _community_window, cls="patch",
          note=lambda doc, got: (
              "the newest reading describes a window that starts AFTER the shipped "
              "one: the doc claims data the tree does not have. A window behind "
              "would only warn; this one is a finding."),
          hint=("the row's newest reading must follow its link, as "
                "`N Obsidian+ Conquest matches, d Mon – d Mon`")),

    # ── the same facts, where the docs repeat them outside §7 ────────────
    # §6 states the pipeline count a second time, in the command that produces
    # it. A number kept in two places is the drift this module exists for, so
    # the second place is gated too rather than trusted to stay in step.
    Check("§6 test commands",
          prose(r"python -m pytest smite/tests -q` \((\d+)\) ·[\s\n]*`cd viewer "
                r"&& npm test -- --run` \((\d+)\)"),
          lambda f, d: (str(pipeline_test_count()), str(viewer_test_count())),
          scope="file", note=_tests_note, cls="code"),

    # ── the same facts, where PRODUCT.md and CLAUDE.md repeat them ────────
    Check("gods on the roster", prose(r"Covers all (\d+) gods on the roster"),
          lambda f, d: (str(len(f.index["gods"])),), source="product", cls="patch"),
    Check("test counts",
          prose(r"(\d+) Python tests \(`pipeline/smite/tests`\), (\d+) viewer tests"),
          lambda f, d: (str(pipeline_test_count()), str(viewer_test_count())),
          source="product", note=_tests_note, cls="code"),
    Check("negative-results register",
          prose(r"([\w-]+) correct-looking improvements have been measured"),
          _register_word, source="product", cls="code"),
    # DAILY, so PRODUCT.md no longer types the figure: the sentence links to it.
    Check("leakage-free measure",
          prose(r"~7x better than chance \(the live figures, re-measured on every "
                r"daily refresh, are in \[`docs/CURRENT\.md`\]\(docs/CURRENT\.md\)\)"),
          lambda f, d: (), source="product", cls="daily",
          hint="PRODUCT.md's leakage-free sentence must link to docs/CURRENT.md"),
    Check("negative-results register",
          prose(r"([\w-]+) correct-looking improvements have been implemented"),
          _register_word, source="claude", cls="code"),
]


# ── reading the doc ───────────────────────────────────────────────────────

def _section(text: str, number: str) -> str:
    """The body of `## <number>. ...`, up to the next `## `."""
    match = re.search(rf"^## {re.escape(number)}\. .*$", text, re.M)
    if not match:
        raise Uncomputable(f"{STATE_PATH.name} has no section {number}")
    rest = text[match.end():]
    following = re.search(r"^## ", rest, re.M)
    return rest[:following.start()] if following else rest


def state_rows(text: str) -> dict:
    """`{label: cell}` for the §7 table.

    Labels are unbolded, so `**Leakage-free**` and `Leakage-free` are one row.
    A line that is not a two-cell row raises rather than being skipped — a
    malformed table would otherwise silently drop the rows below it.
    """
    rows = {}
    for line in _section(text, "7").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 2:
            raise Uncomputable(f"§7 row is not two cells: {line!r}")
        label = cells[0].strip("*").strip()
        if not label or set(label) <= set("-: "):
            continue
        rows[label] = cells[1]
    return rows


def scope_for(cell: str) -> str:
    """The text a pattern searches: the fenced part if fenced, else the cell."""
    fence = NOW_FENCE.search(cell)
    return fence.group(1) if fence else cell


# ── running them ──────────────────────────────────────────────────────────

def _rewrite(match: re.Match, expected: tuple) -> str:
    """The matched text with each checked group replaced by its computed value.

    Reconstructing the doc's own phrasing is what makes the failure readable:
    the two lines differ only where the numbers do.
    """
    text, base, out = match.group(0), match.start(), match.group(0)
    for i in range(len(expected), 0, -1):
        if expected[i - 1] is None:
            continue
        start, end = match.span(i)
        out = out[:start - base] + expected[i - 1] + out[end - base:]
    return text if not expected else out


def _as_set(value: str) -> set:
    return {part.strip() for part in (value or "").split(",") if part.strip()}


def _compare(check: Check, doc: tuple, expected: tuple) -> bool:
    """Raises on an arity mismatch rather than comparing a prefix.

    `zip` would silently truncate, so a compute that returned two values for a
    three-group pattern would pass on the two it did return — a green tick
    covering an unchecked figure, which is the one outcome this module must
    not produce.
    """
    if len(doc) != len(expected):
        raise Uncomputable(
            f"pattern captures {len(doc)} group(s) but compute returned "
            f"{len(expected)} — the two have drifted apart")
    if check.compare == "set":
        return all(e is None or _as_set(d) == _as_set(e)
                   for d, e in zip(doc, expected))
    return all(e is None or d == e for d, e in zip(doc, expected))


def run(checks=None, facts=None, skip_model=False, texts=None, ungated=None) -> tuple:
    """`(results, skipped)`.

    A result is `{check, status, doc, computed, note}` with status one of
    `ok`, `drift`, `unlocatable`, `ambiguous`, `uncomputable`, `uncovered`.
    Everything that is not `ok` fails `--check`; nothing is ever quietly
    dropped.

    `texts` and `ungated` exist so a test can drive the whole mechanism
    against a three-line fixture doc instead of the real one, which is the
    only way to exercise the failure paths that must never silently pass.
    """
    checks = CHECKS if checks is None else checks
    facts = facts if facts is not None else Facts()
    ungated = UNGATED if ungated is None else ungated
    paths = {"state": STATE_PATH, "product": PRODUCT_PATH, "claude": CLAUDE_PATH,
             "current": CURRENT_PATH}
    # CURRENT.md is read only when something asks for it, and a missing one is
    # a finding per figure rather than a crash: it is the file most likely to
    # be absent, in a worktree cut before it existed.
    needed = {c.source for c in checks} | {"state"}
    loaded = {k: (p.read_text(encoding="utf-8") if p.exists() else None)
              for k, p in paths.items() if k in needed and k not in (texts or {})}
    loaded.update(texts or {})
    rows = state_rows(loaded["state"])
    current = (doc_figures.current_rows(loaded["current"])
               if loaded.get("current") is not None else None)

    results, skipped = [], []
    for check in checks:
        reason = None
        if check.vouch is not None:
            try:
                reason = check.vouch(facts, loaded.get(check.source))
            except Exception as exc:                   # noqa: BLE001 — re-derive
                # A stamp that cannot be verified vouches for nothing; the
                # figure is then re-derived, never passed on trust.
                reason = f"the stamp could not be verified ({type(exc).__name__}: {exc})"
        vouched = check.vouch is not None and reason is None
        if skip_model and check.tier == "model" and not vouched:
            skipped.append(check)
            continue
        if check.in_section_7 or check.in_current:
            table, name = (rows, "§7") if check.in_section_7 else (current, "CURRENT.md")
            if table is None:
                results.append({"check": check, "status": "unlocatable",
                                "doc": None, "computed": None,
                                "note": f"{_short(CURRENT_PATH)} does not exist — "
                                        f"{check.hint}"})
                continue
            if check.row not in table:
                results.append({"check": check, "status": "unlocatable",
                                "doc": None, "computed": None,
                                "note": " — ".join(filter(None, (
                                    f"{name} has no row with this label", check.hint)))})
                continue
            scope = scope_for(table[check.row])
        else:
            scope = loaded[check.source]

        found = list(re.finditer(check.pattern, scope, re.M))
        if not found:
            results.append({"check": check, "status": "unlocatable",
                            "doc": None, "computed": None,
                            "note": " — ".join(filter(None, (
                                f"pattern {check.pattern!r} matched nothing",
                                check.hint)))})
            continue
        if len(found) > 1:
            results.append({
                "check": check, "status": "ambiguous", "doc": None,
                "computed": None,
                "note": (f"pattern {check.pattern!r} matched {len(found)} times — the "
                         "gate will not guess which is current. Tighten the anchor, "
                         "or wrap the current figure in <!--now-->…<!--/now-->")})
            continue

        match = found[0]
        doc = match.groups()
        if vouched:
            results.append({"check": check, "status": "ok", "doc": match.group(0),
                            "computed": match.group(0), "note": "current by stamp"})
            continue
        try:
            expected = check.compute(facts, doc)
            ok = _compare(check, doc, expected)
        except Advisory as exc:
            results.append({"check": check, "status": "warning", "doc": match.group(0),
                            "computed": None, "note": str(exc)})
            continue
        except Uncomputable as exc:
            results.append({"check": check, "status": "uncomputable", "doc": None,
                            "computed": None, "note": str(exc)})
            continue
        except Exception as exc:                       # noqa: BLE001 — see below
            # Deliberately broad. A check that raises for an unforeseen reason
            # must become a visible finding, never a skipped row that leaves
            # the run green — that is the failure mode this module exists to
            # stop the doc from having.
            results.append({"check": check, "status": "uncomputable", "doc": None,
                            "computed": None,
                            "note": f"{type(exc).__name__}: {exc}"})
            continue

        note = ""
        if not ok:
            note = check.note(doc, expected) or CLASS_NOTES.get(check.cls, "")
            if reason:
                note += f" (Re-derived because {reason}.)"
        results.append({
            "check": check, "status": "ok" if ok else "drift",
            "doc": match.group(0), "computed": _rewrite(match, expected),
            "note": note})

    results.extend(_coverage_findings(rows, checks, skip_model, ungated))
    if current is not None and any(c.in_current for c in checks) and not skip_model:
        results.extend(_current_coverage(current, checks))
    return results, skipped


def _current_coverage(current: dict, checks) -> list:
    """A CURRENT.md row no figure claims is a finding.

    The file is generated, so a row only `doc_figures` did not write — typed in
    by hand, or left over from a figure that was removed — would otherwise sit
    there looking checked.
    """
    claimed = {c.row for c in checks if c.in_current}
    return [{"check": Check(row, "", lambda f, d: (), source="current"),
             "status": "uncovered", "doc": None, "computed": None,
             "note": ("no generated figure writes this row — regenerate with "
                      "`python -m smite.doc_figures --write`")}
            for row in current if row not in claimed]


def _coverage_findings(rows: dict, checks, skip_model: bool, ungated=None) -> list:
    """Rows nobody claimed, and UNGATED entries naming rows that are gone.

    Without the first, a new §7 row is unchecked and nothing says so — the
    gate would keep passing while the doc grew a fresh place to go stale.
    Without the second, UNGATED becomes an alibi list that outlives its rows.
    """
    if skip_model:
        return []                       # a partial run cannot judge coverage
    ungated = UNGATED if ungated is None else ungated
    claimed = {c.row for c in checks if c.in_section_7}
    out = []
    for row in rows:
        if row in claimed or row in ungated:
            continue
        out.append({"check": Check(row, "", lambda f, d: ()), "status": "uncovered",
                    "doc": None, "computed": None,
                    "note": ("no check claims this row — add one, or add it to "
                             "UNGATED with the reason it is not a measurement")})
    for row in ungated:
        if row not in rows:
            out.append({"check": Check(row, "", lambda f, d: ()), "status": "uncovered",
                        "doc": None, "computed": None,
                        "note": "UNGATED names a §7 row that no longer exists"})
    return out


FAILING = ("drift", "unlocatable", "ambiguous", "uncomputable", "uncovered")


def format_failure(result: dict) -> list:
    check = result["check"]
    lines = [f"{result['status'].upper()}  {check.where} · {check.row}"]
    if result["doc"] is not None:
        lines.append(f"        doc:      {result['doc']}")
        if result["computed"] is not None:       # a warning computes nothing
            lines.append(f"        computed: {result['computed']}")
    if result["note"]:
        lines.append(f"        {result['note']}")
    return lines


def main(argv=None) -> int:
    # The failure output is a diff of two Markdown fragments, so it carries the
    # doc's own `§ · × –` verbatim. On a cp1252 console those become `?` and a
    # diff of two mangled lines is much harder to read than one of two clean
    # ones, so ask for UTF-8 first; `errors="replace"` is the fallback that
    # keeps a redirected or exotic stdout from crashing the gate outright.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        try:
            sys.stdout.reconfigure(errors="replace")
        except Exception:
            pass

    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if any gated figure has drifted")
    ap.add_argument("--skip-model", action="store_true",
                    help="cheap rows only; the skipped rows are named, never silent")
    args = ap.parse_args(argv)

    results, skipped = run(skip_model=args.skip_model)
    failures = [r for r in results if r["status"] in FAILING]
    warnings = [r for r in results if r["status"] == "warning"]

    if not args.check:
        for result in results:
            check = result["check"]
            if result["status"] == "ok":
                by_stamp = "  (current by stamp)" if result["note"] else ""
                print(f"ok      {check.where} · {check.row}: {result['doc']}{by_stamp}")
            else:
                print("\n".join(format_failure(result)))
    else:
        for result in failures + warnings:
            print("\n".join(format_failure(result)))

    if skipped:
        print("\nNOT CHECKED (--skip-model), these rows may be stale:")
        for check in skipped:
            print(f"  {check.where} · {check.row}")
        print("  Row coverage is not judged on a partial run either.")

    if failures:
        print(f"\n{len(failures)} finding(s). "
              "Update a hand-kept row by hand — this gate never rewrites it, "
              "because deciding whether a number moving is expected is the point.")
        if any(r["check"].source == "current" for r in failures):
            print("A CURRENT.md figure is generated: run `python -m smite.doc_figures "
                  "--write`, and say in the pull request why your change moved it.")
        return 1 if args.check else 0
    said = f" ({len(warnings)} warning(s), above; they never fail)" if warnings else ""
    print(f"\n{len(results)} figure(s) checked, no drift{said}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
