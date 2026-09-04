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

WHAT IS DELIBERATELY NOT GATED is in `UNGATED`, with a reason each. The short
version: counterfactuals that cannot be re-derived without flipping a weight
and re-running (the `47 ->` arm of Cap overflow), judgements rather than
measurements (`1 open by decision`), facts about the world rather than about
this tree (`no outcome data exists`), and all explanatory prose.

    python -m smite.doc_audit               # every row: doc value beside computed value
    python -m smite.doc_audit --check       # failures only, non-zero exit on drift
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

from . import calibrate, calibrate_combat, combat, data_audit, efficiency, scoring, validate

REPO_ROOT = Path(__file__).resolve().parents[2]
PIPELINE_ROOT = REPO_ROOT / "pipeline"
STATE_PATH = REPO_ROOT / "docs" / "STATE.md"
PRODUCT_PATH = REPO_ROOT / "PRODUCT.md"
CLAUDE_PATH = REPO_ROOT / "CLAUDE.md"
INDEX_PATH = REPO_ROOT / "viewer" / "public" / "index.json"
VIEWER_ROOT = REPO_ROOT / "viewer"
VIEWER_SRC = VIEWER_ROOT / "src"
TAGS_PATH = REPO_ROOT / "data" / "_tags.yaml"
WEIGHTS_PATH = REPO_ROOT / "data" / "_weights.yaml"
REVIEWS_PATH = REPO_ROOT / "data" / "_expert_reviews.yaml"

#: Float-equality epsilon for finding the sweep row the doc names. WHICH split
#: the leakage-free row reports is read out of the doc rather than fixed here,
#: so moving the reported split stays a doc edit — see `_leakage_free`.
SWEEP_TOLERANCE = 1e-9

#: Narrows a row's search scope. Absent from every row today; see the module
#: docstring for when to add one.
NOW_FENCE = re.compile(r"<!--now-->(.*?)<!--/now-->", re.S)

NUMBER_WORDS = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
    7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
    13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
    17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
    21: "Twenty-one", 22: "Twenty-two", 23: "Twenty-three", 24: "Twenty-four",
    25: "Twenty-five",
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
        "`29 of 2423` arm IS checked."),
    "Joust / Arena gods placed": (
        "`no outcome data exists` is a fact about the world, not a measurement "
        "of this tree. The `0 / 89` IS checked."),
    "Expert claims": (
        "`(1 open by decision)` is a judgement about WHY a claim is open. The "
        "three counts ARE checked."),
    "Headline gate": (
        "the `+0.2pp/+0.3pp` attribution and the stale-row history are prose "
        "about a past change. The two current figures ARE checked."),
    "Leakage-free": (
        "the re-run date, the named commit, the superseded figures and the "
        "earlier history are the reason this row is worth reading. The four "
        "current figures ARE checked."),
    "Gods at 0% coverage": (
        "`the list is identical with cap_overflow on and off` is a "
        "counterfactual. The count and the named gods ARE checked."),
}


class Uncomputable(Exception):
    """Raised by a `compute` when it cannot honestly produce a value.

    Never caught anywhere that would turn it into a pass. `run` converts it
    into a finding, which fails `--check` exactly like a mismatch does.
    """


# ── the tree's own numbers ────────────────────────────────────────────────

class Facts:
    """Everything the checks read, computed at most once and only if asked.

    Laziness is what makes `--skip-model` cost nothing: the expensive
    properties are never touched when their checks are filtered out.
    """

    @functools.cached_property
    def index(self) -> dict:
        return json.loads(INDEX_PATH.read_text(encoding="utf-8"))

    @functools.cached_property
    def suggested(self) -> list:
        return [b for group in self.index["builds"] for b in group["builds"]
                if b.get("source") == "suggested"]

    @functools.cached_property
    def items_by_name(self) -> dict:
        return {i["name"]: i for i in self.index["items"]}

    @functools.cached_property
    def validation(self):
        """`validate.compute()` — the headline gate and every god's coverage."""
        return validate.compute()

    @functools.cached_property
    def calibration(self) -> dict:
        """The leakage-free measure: probe, random-core baseline, sweep.

        These are the three `smite.calibrate` library calls its `main` makes,
        without the guardrailed weight grid or the report write, which is what
        takes it from ~17s to minutes. `python -m smite.calibrate --control`
        (08-21 B) is expected to wrap the same three functions; when it lands
        this can shell out to it instead without any number moving.
        """
        fx = calibrate._Fixture()
        return {
            "probe": calibrate.leakage_probe(fx),
            "baseline": calibrate.random_core_baseline(fx),
            "sweep": calibrate.model_signal_sweep(fx),
        }

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


def placed(entries) -> int:
    """Tier-list entries that were given a band. `None` means unranked."""
    return sum(1 for e in entries if e.get("tier_score") is not None)


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


def over_penetration_cap(facts: Facts) -> tuple:
    """`(builds over the percentage-penetration cap, suggested builds)`.

    Sums `Penetration %` across each shipped core using `efficiency.stat_key`,
    so the percentage and flat budgets stay separate — they are different goods
    at different prices (52.6 and 33.2 gold a point), which is why summing them
    would be a units error rather than a rounding one. The cap comes from
    `stat_caps` in `_weights.yaml` rather than being repeated here.
    """
    weights = scoring.load_weights(WEIGHTS_PATH)
    caps = weights.get("stat_caps") or {}
    cap = caps.get("Penetration %")
    if cap is None:
        raise Uncomputable(
            "`stat_caps` has no `Penetration %` — the row's cap moved or was "
            "removed; re-derive the row rather than checking it against a guess")
    over = 0
    for build in facts.suggested:
        total = 0.0
        for name in build.get("slot_order") or []:
            item = facts.items_by_name.get(name)
            if not item:
                continue
            for stat, raw in (item.get("stats") or {}).items():
                if efficiency.stat_key(stat, raw) == "Penetration %":
                    total += efficiency.parse_stat_value(raw)
        if total > cap:
            over += 1
    return over, len(facts.suggested)


def _day(iso: str) -> str:
    date = dt.date.fromisoformat(iso)
    return f"{date.day} {date.strftime('%b')}"


def _pct(value: float) -> str:
    return f"{value * 100:.1f}"


def _sweep_at(facts: Facts, eff: float) -> float:
    for row in facts.calibration["sweep"]:
        if abs(row["efficiency"] - eff) < SWEEP_TOLERANCE:
            return row["coverage"]
    raise Uncomputable(
        f"the sweep has no row at efficiency {eff} — the row reports a split "
        "`model_signal_sweep` no longer produces")


def _probe(facts: Facts, label_contains: str) -> float:
    rows = [r for r in facts.calibration["probe"] if label_contains in r["label"]]
    if len(rows) != 1:
        raise Uncomputable(
            f"{len(rows)} probe rows match {label_contains!r}, expected exactly one")
    return rows[0]["agg"]["mean_coverage"]


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
    """
    row: str
    pattern: str
    compute: Callable[[Facts, tuple], tuple]
    source: str = "state"
    tier: str = "cheap"
    compare: str = "exact"          # 'exact' | 'set'
    scope: str = "row"              # 'row' (a §7 cell) | 'file' (the whole doc)
    note: Callable[[tuple, tuple], str] = field(default=lambda doc, got: "")

    @property
    def in_section_7(self) -> bool:
        return self.source == "state" and self.scope == "row"

    @property
    def where(self) -> str:
        if self.source == "state":
            return "STATE.md §7" if self.scope == "row" else "STATE.md"
        return {"product": "PRODUCT.md", "claude": "CLAUDE.md"}[self.source]


def prose(pattern: str) -> str:
    """Let a pattern span a Markdown line wrap.

    A §7 row is one line, but `CLAUDE.md` is hard-wrapped at 78 columns and its
    register claim breaks between "correct-looking" and "improvements". A
    pattern with a literal space there matches nothing, and `unlocatable` is
    the right failure only when the sentence is really gone — not when it moved
    a word onto the next line.
    """
    return re.sub(r" ", r"\\s+", pattern)


def _flavors(facts: Facts, _doc: tuple) -> tuple:
    emitted = sorted({b["archetype"] for b in facts.suggested if b.get("archetype")})
    return (", ".join(emitted),)


def _joust_arena(facts: Facts, _doc: tuple) -> tuple:
    tierlist = facts.index["tierlist"]
    counts = {mode: placed(tierlist[mode]["gods"]) for mode in ("joust", "arena")}
    totals = {mode: len(tierlist[mode]["gods"]) for mode in ("joust", "arena")}
    if len(set(counts.values())) != 1 or len(set(totals.values())) != 1:
        raise Uncomputable(
            f"Joust and Arena no longer agree ({counts}, of {totals}) — the row "
            "states one figure for both and can no longer be derived as one")
    return (str(counts["joust"]), str(totals["joust"]))


def _zero_coverage(facts: Facts, _doc: tuple) -> tuple:
    per_god, _agg = facts.validation
    zero = sorted(god for god, row in per_god.items() if row["coverage"] == 0)
    return (str(len(zero)), ", ".join(zero))


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


def _leakage_free(facts: Facts, doc: tuple) -> tuple:
    probe = _probe(facts, "model only")
    at_split = _sweep_at(facts, float(doc[2]))
    chance = facts.calibration["baseline"]["mean"]
    low, high = sorted((probe / chance, at_split / chance))
    return (_pct(probe), _pct(at_split), None, _pct(chance),
            f"{low:.1f}", f"{high:.1f}")


CHECKS = [
    Check("Gods tracked", r"(\d+) of (\d+) on the roster",
          lambda f, d: (str(len(f.index["gods"])), str(len(f.index["roster"])))),
    Check("Items", r"^(\d+)$",
          lambda f, d: (str(len(f.index["items"])),)),
    Check("Build groups", r"(\d+) \((\d+) gods × (\d+) modes\)",
          lambda f, d: (str(len(f.index["builds"])), str(len(f.index["gods"])),
                        str(len(f.index["modes"])))),
    Check("Build flavors", r"^(.+)$", _flavors, compare="set"),
    Check("Conquest gods placed", r"(\d+) / (\d+)",
          lambda f, d: (str(placed(f.index["tierlist"]["conquest"]["gods"])),
                        str(len(f.index["tierlist"]["conquest"]["gods"])))),
    Check("Joust / Arena gods placed", r"(\d+) / (\d+)", _joust_arena),
    Check("Items placed", r"(\d+) / (\d+)",
          lambda f, d: (str(placed(f.index["tierlist"]["items"])),
                        str(len(f.index["items"])))),
    Check("Community sample",
          r"([\d,]+) (\w+)\+ Conquest matches, (\d+ \w+) – (\d+ \w+)",
          lambda f, d: (
              f"{f.index['community_source']['matches_analyzed']:,}",
              f.index["community_source"]["division"].capitalize(),
              _day(f.index["community_source"]["window_start"]),
              _day(f.index["community_source"]["window_end"]))),
    Check("Cap overflow", r"-> (\d+) of (\d+) builds over the penetration cap",
          lambda f, d: tuple(str(x) for x in over_penetration_cap(f))),
    Check("Combat model", r"(\d+\.\d+)% worst case over (\d+) observations",
          lambda f, d: (f"{f.combat_result['worst_rel_error'] * 100:.1f}",
                        str(f.combat_result["n"]))),
    Check("Expert claims", r"(\d+) recorded · (\d+) resolved · (\d+) open",
          lambda f, d: (
              str(len(f.reviews)),
              str(sum(1 for r in f.reviews if r.get("status") == "resolved")),
              str(sum(1 for r in f.reviews if r.get("status") == "open")))),
    Check("Item effect-tag coverage",
          r"(\d+) of (\d+) buildable tagged · (\d+) reviewed, no tag warranted "
          r"· (\d+) unreviewed",
          lambda f, d: (str(f.tag_audit["tagged"]), str(f.tag_audit["buildable"]),
                        str(f.tag_audit["reviewed_empty"]),
                        str(f.tag_audit["untagged"]))),
    Check("Tests", r"(\d+) pipeline · (\d+) viewer",
          lambda f, d: (str(pipeline_test_count()), str(viewer_test_count())),
          note=_tests_note),

    # ── model tier ────────────────────────────────────────────────────────
    Check("Headline gate", r"coverage (\d+\.\d+)%, win-weighted (\d+\.\d+)%",
          lambda f, d: (_pct(f.validation[1]["mean_coverage"]),
                        _pct(f.validation[1]["mean_win_weighted"])),
          tier="model"),
    Check("Gods at 0% coverage", r"^(\d+) — ([^.]+)\.", _zero_coverage,
          tier="model"),
    Check("Leakage-free",
          r"(\d+\.\d+)% probe · (\d+\.\d+)% at eff (\d\.\d+), vs (\d+\.\d+)% "
          r"chance = (\d+\.\d+)–(\d+\.\d+)×",
          _leakage_free, tier="model"),

    # ── the same facts, where the docs repeat them outside §7 ────────────
    # §6 states the pipeline count a second time, in the command that produces
    # it. A number kept in two places is the drift this module exists for, so
    # the second place is gated too rather than trusted to stay in step.
    Check("§6 test commands",
          prose(r"python -m pytest smite/tests -q` \((\d+)\) ·[\s\n]*`cd viewer "
                r"&& npm test -- --run` \((\d+)\)"),
          lambda f, d: (str(pipeline_test_count()), str(viewer_test_count())),
          scope="file", note=_tests_note),

    # ── the same facts, where PRODUCT.md and CLAUDE.md repeat them ────────
    Check("gods on the roster", prose(r"Covers all (\d+) gods on the roster"),
          lambda f, d: (str(len(f.index["gods"])),), source="product"),
    Check("test counts",
          prose(r"(\d+) Python tests \(`pipeline/smite/tests`\), (\d+) viewer tests"),
          lambda f, d: (str(pipeline_test_count()), str(viewer_test_count())),
          source="product", note=_tests_note),
    Check("negative-results register",
          prose(r"([\w-]+) correct-looking improvements have been measured"),
          _register_word, source="product"),
    Check("leakage-free measure",
          prose(r"\((\d+\.\d+)% against a (\d+\.\d+)% random core\)"),
          lambda f, d: (_pct(_probe(f, "model only")),
                        _pct(f.calibration["baseline"]["mean"])),
          source="product", tier="model"),
    Check("negative-results register",
          prose(r"([\w-]+) correct-looking improvements have been implemented"),
          _register_word, source="claude"),
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
    paths = {"state": STATE_PATH, "product": PRODUCT_PATH, "claude": CLAUDE_PATH}
    loaded = {k: p.read_text(encoding="utf-8") for k, p in paths.items()}
    loaded.update(texts or {})
    rows = state_rows(loaded["state"])

    results, skipped = [], []
    for check in checks:
        if skip_model and check.tier == "model":
            skipped.append(check)
            continue
        if check.in_section_7:
            if check.row not in rows:
                results.append({"check": check, "status": "unlocatable",
                                "doc": None, "computed": None,
                                "note": "§7 has no row with this label"})
                continue
            scope = scope_for(rows[check.row])
        else:
            scope = loaded[check.source]

        found = list(re.finditer(check.pattern, scope, re.M))
        if not found:
            results.append({"check": check, "status": "unlocatable",
                            "doc": None, "computed": None,
                            "note": f"pattern {check.pattern!r} matched nothing"})
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
        try:
            expected = check.compute(facts, doc)
            ok = _compare(check, doc, expected)
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

        results.append({
            "check": check, "status": "ok" if ok else "drift",
            "doc": match.group(0), "computed": _rewrite(match, expected),
            "note": "" if ok else check.note(doc, expected)})

    results.extend(_coverage_findings(rows, checks, skip_model, ungated))
    return results, skipped


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

    if not args.check:
        for result in results:
            check = result["check"]
            if result["status"] == "ok":
                print(f"ok      {check.where} · {check.row}: {result['doc']}")
            else:
                print("\n".join(format_failure(result)))
    else:
        for result in failures:
            print("\n".join(format_failure(result)))

    if skipped:
        print("\nNOT CHECKED (--skip-model), these rows may be stale:")
        for check in skipped:
            print(f"  {check.where} · {check.row}")
        print("  Row coverage is not judged on a partial run either.")

    if failures:
        print(f"\n{len(failures)} finding(s). "
              "Update the doc by hand — this gate never rewrites it, because "
              "deciding whether a number moving is expected is the point.")
        return 1 if args.check else 0
    print(f"\n{len(results)} figure(s) checked, no drift.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
