"""Write `docs/CURRENT.md`: the `docs/STATE.md` §7 figures a daily community
refresh moves, generated so that nobody has to re-take them by hand.

WHY IT EXISTS (2026-11-09). From 2026-11-08 the daily refresh lands on `main`
by itself, as an auto-merged pull request, and it never edits a document. §7
carried every figure that refresh moves as hand-written prose, so
`doc_audit --check` went red on `main` after each refresh, and every session's
merge gate inherited the rows: #124 alone moved seven of them, and #125 and
#127 stayed open until Jacob ruled that inherited, attributed rows don't block.
A §7 re-take (#118, #128) cleared it for one day at a time. This is the
lasting fix, and it is the documentary twin of PR #123's rule for tests
(`tests/live_window.py`): A VALUE THE WINDOW MOVES DAILY IS NEVER PINNED BY
HAND. #123 turned such pins into invariants; a document cannot hold an
invariant, so here the value is generated instead.

WHICH FIGURES, AND THE EVIDENCE THAT THEY ARE DAILY. Every `doc_audit` figure
falls into one of three classes, measured rather than assumed:

  DAILY   moves on an ordinary community refresh. GENERATED HERE.
  PATCH   moves at a patch boundary, a stats refresh, or when `new_entities`
          adds a god or item. Hand-kept and checked; moving one is a
          declaration, as `live_window.py`'s patch-boundary pins were until a
          new community window began landing by itself (2026-11-09).
  CODE    moves only when a commit changes code or a hand-kept file (test
          counts, the §4 register, expert claims). Hand-kept and checked, and
          it FAILS LOUDLY: those are the rows sessions most often forget.

All 85 commits that touched `data/_community_items.json` from 2026-07-27 to
2026-11-08 were compared against their own parents. Every refresh commit
sampled touches only `data/` and `viewer/public/`, so a figure that differs
across such a pair moved on that refresh and nothing else. Cheap figures, read
off the shipped `index.json` at each commit:

    Community sample       moved on 83 of 85
    Cap overflow           66 of 85
    Items placed           65 of 85
    Conquest gods placed   20 of 85, all in the days after a window reset
    Build flavors          12 of 85, every one of them `hybrid`: it is
                           emitted only when a hybrid swap fires, so it drops
                           out the first day after each reset and is back
                           within one to three days
    Gods tracked, Build groups   1 of 85 (2026-11-04: Nox, added by
                           `new_entities` inside the job)   -> PATCH
    Items, buildable count, Joust/Arena placed   0 of 85    -> PATCH

The three model figures need a run, so seven refresh-only pairs (2026-08-24,
09-16, 10-14, 10-28, 10-29, 10-30 and 11-08) were recomputed in a throwaway
worktree. The Headline gate moved on 7 of 7 and Gods at 0% coverage on 7 of 7
(on 11-08 from six gods to three DIFFERENT ones). Leakage-free moved on 7 of 7:
the probe on 6 and the eff 0.45 split on 7. On 11-08 the Headline gate went
47.6% / 51.6% -> 51.2% / 54.4% and Leakage-free 39.2% / 36.4% -> 41.7% /
38.3%, on the refresh alone.

WHAT A HUMAN STILL DECIDES. `doc_audit`'s docstring argues that a regenerator
would delete the prose worth more than the numbers, and the moment where a
human decides whether a number moving is expected. This module answers both
without contradicting either:

  * It writes ONE file, and that file holds no prose. §7's rows keep every
    word: each one now opens with a link here, and what used to read as its
    current figure reads as its newest dated reading. `doc_audit` still never
    rewrites anything.
  * For a DATA move there was never a decision to make. Seven re-takes in a
    row wrote the same sentence, "moved by the refresh alone, which changed no
    code, weights or tags", and the pairs above say it is true of every
    refresh commit by construction. The refresh's own commit now records it:
    `git log -p docs/CURRENT.md` is the history of every figure here, each
    daily move under `chore(data): daily community refresh`.
  * For a CODE move the decision is kept, and it lands on the right pull
    request. A branch whose code or weights move a figure fails `doc_audit`
    with the old and new value, regenerates with `--write`, and the move
    appears in that PR's diff for its description to explain. On 2026-11-08
    #127's five base relics moved Items placed 203 -> 208 with no data move;
    under this file that is #127's own red gate, not the next session's.

THE STAMP, AND WHY THE MODEL FIGURES ARE NOT RE-RUN ON AN UNCHANGED TREE. The
file carries a machine-readable stamp: the input fingerprint
(`calibrate.input_fingerprint`), a hash of the pipeline's code, a hash of the
shipped outputs (`index.json` and `data/builds/`), and a checksum of the body.
The figures are a pure function of those, so when all four match the tree the
figures are current by construction, and `doc_audit` does not re-run
`validate` or `calibrate` to say so. That is cheaper (seconds, not ~25s), and
it keeps a file written by the Linux runner checkable on a Windows session:
nothing that could round differently is recomputed. When any part differs,
`doc_audit` re-derives every figure and fails on any that moved. The cheap
figures are always re-derived, because they cost nothing.

    python -m smite.doc_figures           # print what --write would write
    python -m smite.doc_figures --write   # write docs/CURRENT.md (the daily job runs this)
    python -m smite.doc_figures --check   # re-derive everything, exit 1 on any difference
"""
import argparse
import datetime as dt
import functools
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from . import calibrate, efficiency, scoring, validate

REPO_ROOT = Path(__file__).resolve().parents[2]
PIPELINE_ROOT = REPO_ROOT / "pipeline"
SMITE_ROOT = PIPELINE_ROOT / "smite"
DATA_ROOT = REPO_ROOT / "data"
INDEX_PATH = REPO_ROOT / "viewer" / "public" / "index.json"
BUILDS_DIR = DATA_ROOT / "builds"
COMMUNITY_PATH = DATA_ROOT / "_community_items.json"
WEIGHTS_PATH = DATA_ROOT / "_weights.yaml"
CURRENT_PATH = REPO_ROOT / "docs" / "CURRENT.md"

#: Hex characters kept from each sha256, matching `calibrate.FINGERPRINT_LEN`.
HASH_LEN = calibrate.FINGERPRINT_LEN

#: The fixed split the leakage-free figure reports beside the probe. It is
#: `calibrate.CONTROL_SPLITS`'s second row, held fixed for the same reason the
#: control holds it: an argmax moves with the data.
REPORTED_SPLIT = calibrate.CONTROL_SPLITS[1]

STAMP_RE = re.compile(
    r"^<!-- stamp inputs=(?P<inputs>[0-9a-f]+) code=(?P<code>[0-9a-f]+) "
    r"outputs=(?P<outputs>[0-9a-f]+) sha=(?P<sha>[0-9a-f]+) -->$", re.M)


class Uncomputable(Exception):
    """Raised by a figure that cannot honestly produce a value.

    `doc_audit` turns it into a finding, never a pass; `--write` refuses to
    write a file with a hole in it."""


# ── the tree's own numbers ────────────────────────────────────────────────

class Facts:
    """Everything the generated figures read, computed at most once and only
    if asked. `doc_audit.Facts` extends this with what only its hand-kept
    checks read, so both modules derive a figure through the same code.

    Laziness is what makes a stamp check cheap: when the stamp vouches for the
    model figures, `validation` and `control` are never touched.
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
    def community_table(self) -> dict:
        """`data/_community_items.json`, for the window's NAME, which the
        index's `community_source` does not carry."""
        return json.loads(COMMUNITY_PATH.read_text(encoding="utf-8"))

    @functools.cached_property
    def validation(self):
        """`validate.compute()` — the headline gate and every god's coverage."""
        return validate.compute()

    @functools.cached_property
    def fixture(self):
        return calibrate._Fixture()

    @functools.cached_property
    def fingerprint(self) -> str:
        """Hashed before `control` evaluates anything, as `calibrate.control`
        itself insists, so the stamp describes the inputs as loaded."""
        return calibrate.input_fingerprint(self.fixture)

    @functools.cached_property
    def control(self) -> dict:
        """`calibrate.control`: the random-core baseline and the two fixed
        splits. The first split is exactly the leakage probe's `model only`
        corner (efficiency 0.7, fit 0.3), so this one ~7s call is everything
        the leakage-free figure needs."""
        self.fingerprint                                  # noqa: B018 — order matters
        return calibrate.control(self.fixture)

    @functools.cached_property
    def code_hash(self) -> str:
        return code_hash()

    @functools.cached_property
    def outputs_hash(self) -> str:
        return outputs_hash()


def _tree_hash(paths, root: Path) -> str:
    """sha256 over (relative path, content) in byte order of the path.

    CRLF is folded to LF, because a Windows checkout with `core.autocrlf` holds
    the same blobs as the runner with different line endings, and a stamp that
    differed across them would re-derive on every Windows session — the exact
    case the stamp exists to avoid.
    """
    h = hashlib.sha256()
    keyed = sorted(((p.relative_to(root).as_posix(), p) for p in paths),
                   key=lambda kv: kv[0].encode("utf-8"))
    for rel, path in keyed:
        h.update(rel.encode("utf-8") + b"\0")
        h.update(path.read_bytes().replace(b"\r\n", b"\n") + b"\0")
    return h.hexdigest()[:HASH_LEN]


def code_hash(root: Path = SMITE_ROOT) -> str:
    """The pipeline's code, tests excluded: a test changes no figure."""
    files = [p for p in root.rglob("*.py")
             if "tests" not in p.relative_to(root).parts]
    return _tree_hash(files, root.parent)


def outputs_hash(index_path: Path = INDEX_PATH, builds_dir: Path = BUILDS_DIR) -> str:
    """The shipped outputs the figures read: `index.json` for the cheap ones,
    the build notes for `validate`. Both are generated, so neither is in the
    input fingerprint, which hashes only the community half of a build note."""
    return _tree_hash([index_path, *builds_dir.glob("*.md")], REPO_ROOT)


# ── the figures ───────────────────────────────────────────────────────────

def placed(entries) -> int:
    """Tier-list entries that were given a band. `None` means unranked.

    This counts every banded entry, buildable or not: `tierlist.item_rankings`
    bands any item with community win data and has no `is_buildable` filter.
    77 unbuildable items (starters, relics, Genie's Lamp, the acorns) were
    already counted this way at `a3975ab9`, before #127 added five base relics
    and Items placed rose by exactly five with no data move. Whether an
    unbuildable item should count as placed is an open question, not a known
    defect; this records the convention and does not change it.
    """
    return sum(1 for e in entries if e.get("tier_score") is not None)


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


#: Decimals a figure is rounded to BEFORE it is formatted. The runner (Python
#: 3.12, whose `sum()` of floats is compensated) and a Windows session (3.10,
#: whose is not) agree on every per-god value and differ only in the last ulp
#: of a mean: on 15 trees measured 2026-11-09, 0 of 75 displayed readings
#: differed, but a mean sitting exactly on a .x5 boundary would round to
#: different digits. Rounding to 1e-6 first folds that ulp away on both.
STABLE_DECIMALS = 6


def _stable(value: float, decimals: int = 1) -> str:
    return f"{round(value, STABLE_DECIMALS):.{decimals}f}"


def _pct(value: float) -> str:
    return _stable(value * 100)


def emitted_flavors(facts: Facts) -> list:
    return sorted({b["archetype"] for b in facts.suggested if b.get("archetype")})


def zero_coverage(facts: Facts) -> list:
    per_god, _agg = facts.validation
    return sorted(god for god, row in per_god.items() if row["coverage"] == 0)


def _flavors(f: Facts) -> str:
    names = emitted_flavors(f)
    return f"{len(names)} — {', '.join(names)}"


def _conquest_placed(f: Facts) -> str:
    gods = f.index["tierlist"]["conquest"]["gods"]
    return f"{placed(gods)} / {len(gods)}"


def _items_placed(f: Facts) -> str:
    return f"{placed(f.index['tierlist']['items'])} / {len(f.index['items'])}"


def _community_sample(f: Facts) -> str:
    source = f.index["community_source"]
    end = dt.date.fromisoformat(source["window_end"])
    window = f.community_table.get("window")
    if not window:
        raise Uncomputable("`_community_items.json` names no window")
    return (f"{source['matches_analyzed']:,} {source['division'].capitalize()}+ "
            f"Conquest matches, {_day(source['window_start'])} – "
            f"{_day(source['window_end'])} {end.year} (window `{window}`)")


def _cap_overflow(f: Facts) -> str:
    over, total = over_penetration_cap(f)
    hybrid = sum(1 for b in f.suggested if b.get("archetype") == "hybrid")
    return (f"{over} of {total} builds over the penetration cap "
            f"({hybrid} of the {total} are `hybrid`)")


def _headline(f: Facts) -> str:
    _per_god, agg = f.validation
    return (f"coverage {_pct(agg['mean_coverage'])}%, "
            f"win-weighted {_pct(agg['mean_win_weighted'])}%")


def _zero(f: Facts) -> str:
    gods = zero_coverage(f)
    return f"{len(gods)} — {', '.join(gods) if gods else 'none'}"


def _leakage_free(f: Facts) -> str:
    control = f.control
    splits = {round(s["efficiency"], 2): s["coverage"] for s in control["splits"]}
    probe = splits[round(calibrate.CONTROL_SPLITS[0][0], 2)]
    at_split = splits[round(REPORTED_SPLIT[0], 2)]
    chance = control["baseline"]
    low, high = sorted((probe / chance, at_split / chance))
    return (f"{_pct(probe)}% probe · {_pct(at_split)}% at eff {REPORTED_SPLIT[0]:.2f}, "
            f"vs {_pct(chance)}% chance = {_stable(low)}–{_stable(high)}×")


@dataclass(frozen=True)
class Figure:
    """One generated figure: the live value of the §7 row named `label`.

    `tier` is `doc_audit`'s: 'cheap' reads the shipped index and is always
    re-derived; 'model' re-runs `validate` or `calibrate` and is re-derived
    only when the stamp says the tree changed.
    """
    label: str
    render: Callable[[Facts], str]
    tier: str = "cheap"


#: In §7's own order. Every label is a §7 row, and only DAILY rows belong here:
#: `doc_audit` fails if a figure here names a row that does not link to this
#: file, and a test fails if any CODE figure is ever added.
FIGURES = [
    Figure("Build flavors", _flavors),
    Figure("Conquest gods placed", _conquest_placed),
    Figure("Items placed", _items_placed),
    Figure("Community sample", _community_sample),
    Figure("Headline gate", _headline, tier="model"),
    Figure("Leakage-free", _leakage_free, tier="model"),
    Figure("Cap overflow", _cap_overflow),
    Figure("Gods at 0% coverage", _zero, tier="model"),
]


# ── the file ──────────────────────────────────────────────────────────────

HEADER = """# Current figures

<!-- GENERATED by `python -m smite.doc_figures --write`. Do not edit by hand:
the daily refresh rewrites this file in its data pull request, and
`python -m smite.doc_audit --check` fails if it does not match the tree. -->
"""

PREAMBLE = """
The figures of [`docs/STATE.md` §7](STATE.md#7-current-numbers) that move on an
ordinary daily community refresh. §7 keeps the prose: what each figure means,
what it is not evidence of, and its dated history. This file keeps the live
value, and `git log -p docs/CURRENT.md` is the history of every figure in it.
Why these and only these is in `pipeline/smite/doc_figures.py`.

If `doc_audit` says a figure here moved on your branch, your code or weights
moved it: run `python -m smite.doc_figures --write` and say why in the pull
request. On a merge conflict in this file, take either side and regenerate.
"""


def _sha(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()[:HASH_LEN]


def render_body(facts: Facts) -> str:
    """Everything below the stamp. Deterministic: no clock, no paths, nothing
    but the tree, so regenerating an unchanged tree rewrites nothing."""
    source = facts.index["community_source"]
    end = dt.date.fromisoformat(source["window_end"])
    window = facts.community_table.get("window") or "?"
    lines = [
        PREAMBLE,
        f"**Inputs.** Community window `{window}`, {_day(source['window_start'])} – "
        f"{_day(source['window_end'])} {end.year}, "
        f"{source['matches_analyzed']:,} matches · data patch "
        f"{facts.index.get('data_patch') or '?'} · input fingerprint "
        f"`{facts.fingerprint}` · code `{facts.code_hash}` · shipped outputs "
        f"`{facts.outputs_hash}`",
        "",
        "| Figure | Value |",
        "|---|---|",
    ]
    for figure in FIGURES:
        value = figure.render(facts)
        if "|" in value or "\n" in value:
            raise Uncomputable(f"{figure.label} rendered a value a table cell "
                               f"cannot hold: {value!r}")
        lines.append(f"| {figure.label} | {value} |")
    return "\n".join(lines) + "\n"


def render(facts: Facts) -> str:
    body = render_body(facts)
    stamp = (f"<!-- stamp inputs={facts.fingerprint} code={facts.code_hash} "
             f"outputs={facts.outputs_hash} sha={_sha(body)} -->")
    return f"{HEADER}{stamp}\n{body}"


@dataclass(frozen=True)
class Stamp:
    inputs: str
    code: str
    outputs: str
    sha: str
    body_sha: str            # what the body in the file actually hashes to


def parse_stamp(text: str):
    """The stamp in a written file, or None when it has none."""
    match = STAMP_RE.search(text or "")
    if not match:
        return None
    body = text[match.end() + 1:]
    return Stamp(match["inputs"], match["code"], match["outputs"], match["sha"],
                 _sha(body))


def current_rows(text: str) -> dict:
    """`{label: value}` for the figures table. The header row is not a figure."""
    rows = {}
    for line in (text or "").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 2:
            raise Uncomputable(f"CURRENT.md row is not two cells: {line!r}")
        label = cells[0]
        if not label or label == "Figure" or set(label) <= set("-: "):
            continue
        rows[label] = cells[1]
    return rows


def stale_parts(facts: Facts, text: str):
    """Why the stamp cannot vouch for this tree, or None when it can.

    Order is cheapest first, so a hand edit or a code change is reported
    without paying for the input fingerprint.
    """
    stamp = parse_stamp(text)
    if stamp is None:
        return "the file carries no stamp"
    if stamp.sha != stamp.body_sha:
        return "its body was edited by hand (the checksum does not match)"
    parts = []
    if stamp.code != facts.code_hash:
        parts.append("the pipeline code")
    if stamp.outputs != facts.outputs_hash:
        parts.append("the shipped index or build notes")
    if stamp.inputs != facts.fingerprint:
        parts.append("the input fingerprint")
    if parts:
        return " and ".join(parts) + " differ from the tree it was generated on"
    return None


def write(facts: Facts = None, path: Path = CURRENT_PATH) -> bool:
    """Write the file; True when its content changed."""
    facts = facts if facts is not None else Facts()
    text = render(facts)
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old is not None and old.replace("\r\n", "\n") == text:
        return False
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def main(argv=None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true",
                      help=f"write {CURRENT_PATH.relative_to(REPO_ROOT).as_posix()}")
    mode.add_argument("--check", action="store_true",
                      help="re-derive every figure; exit 1 if the file differs")
    args = ap.parse_args(argv)

    facts = Facts()
    if args.write:
        changed = write(facts)
        rel = CURRENT_PATH.relative_to(REPO_ROOT).as_posix()
        print(f"{rel}: {'rewritten' if changed else 'unchanged'}")
        return 0
    text = render(facts)
    if not args.check:
        print(text, end="")
        return 0
    old = CURRENT_PATH.read_text(encoding="utf-8") if CURRENT_PATH.exists() else ""
    have, want = current_rows(old), current_rows(text)
    moved = [label for label in want if have.get(label) != want[label]]
    for label in moved:
        print(f"MOVED  {label}\n        file:     {have.get(label)}\n"
              f"        computed: {want[label]}")
    stamp_moved = parse_stamp(old) != parse_stamp(text)
    if stamp_moved and not moved:
        print("STAMP  the figures are current; the stamp describes another tree")
    if moved or stamp_moved:
        return 1
    print(f"{len(want)} figure(s), stamp and all, match the tree.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
