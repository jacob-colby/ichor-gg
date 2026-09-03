"""Replay recorded expert judgements against the current builds.

THE POINT. Every other gate in this project is made of the community's own
build data, and `docs/STATE.md` §1 shows why that cannot settle the model's
central claims: both of `validate.compute`'s targets are also model inputs, so
the objective is maximised by deleting the model. §5 calls the missing
non-circular feedback loop the highest-value thing left. A strong player's
reading of a build is not circular — it is not derived from pick rates, win
rates, or anything else the recommender consumes.

WHAT IT IS NOT. This is not a statistical test and must never be quoted as one.
The sample is one reviewer and a handful of claims, chosen because they looked
wrong rather than at random, which is exactly the sampling that makes a
percentage meaningless. It answers "did the specific thing they objected to
change?" and nothing else. `smite.calibrate` remains the measure; this is a
regression net for judgements that measure could never express.

A claim going green is also not automatically a win. `item-overweighted`
clearing because the item left the build is the intended outcome; it clearing
because the whole build churned underneath is a coincidence wearing the same
colour. The report prints the current core beside every verdict so that
difference stays visible, and `status:` in the YAML is only ever set by hand.

    python -m smite.expert_review          # report
    python -m smite.expert_review --check   # non-zero exit if a resolved claim regressed

THE VOCABULARY, AND WHY IT HAS THE SHAPES IT HAS (2026-09-03). Until then the
checker understood two kinds, and both were item MEMBERSHIP in one god's core.
Of the four claims on file, the two `narrative` ones were inert — recorded,
never checked — because the vocabulary had no shape for what they said. Four
kinds were added. Each was admitted on one bar: it is checkable TODAY from
what `index.json` already carries, and it can go `holds`. A kind that needs
evidence the repo does not have is a wish, and a kind that cannot fail is
decoration.

  buy-order         "Transcendence first on Ullr." The core's `slot_order` is
                    what the viewer labels the buy order, and it is the part
                    of the output with the LEAST evidence behind it:
                    `assemble.build_order` is a tag-and-cost heuristic whose
                    own docstring says there is no build-path data. An expert
                    is the only instrument that can grade it.
  situational-swap  "Against heavy CC he should bring Parashu." The build
                    ships one swap row per situation the model knows
                    (`KNOWN_SITUATIONS`, mirrored from `assemble._SITUATIONS`).
                    Only those four are checkable; "against a tanky comp" is
                    not one of them and is refused rather than recorded.
  composition       "Carries shouldn't buy protections." "Build him as a
                    bruiser." A floor and/or ceiling on how many core items
                    carry a stat or an effect tag. STATE.md §5 recorded
                    exactly this shape from the model's own diagnosis
                    (Berserker's Shield on 17 of 18 Carry cores) before any
                    reviewer said it, so it is a shape the repo has needed
                    once already.
  pairing           "Transcendence only works with mana items." The concrete
                    form of the build-coherence narrative claim, checked as
                    co-membership in ONE core. True pairing as a statistic
                    needs a joint pick distribution the source does not have.

Shapes considered and REFUSED, so the next person stops trying to record
them: outcome claims ("I played it and it lost") need match-level data;
pairing-as-statistic needs a joint distribution; ranking claims ("X is
better than Y here") are checkable from `god_item_scores` but that is a
number the player never sees, and §4.19 says quality rank does not decide
core membership, so where the rank matters it already shows up as
membership; timing claims need a timeline; role and ability-order claims
are about scraped data, not the recommender.

Neither narrative claim re-expresses in these kinds. Build-coherence is a
claim about the METHOD with no god, item or pair named; incomplete-builds is
a claim about how a denominator is read, fixed by `scoring.SLOT_REACH` and
guarded where it belongs, in `test_scoring`. Forcing either would fabricate a
claim the reviewer did not make.
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
REVIEWS_PATH = REPO_ROOT / "data" / "_expert_reviews.yaml"
INDEX_PATH = REPO_ROOT / "viewer" / "public" / "index.json"

#: The matchup situations a build carries a swap row for. Mirrors
#: `assemble._SITUATIONS` — a test pins the two together — and is spelled out
#: here so a claim naming a situation the model does not emit is refused at
#: validation rather than silently never matching a row.
KNOWN_SITUATIONS = ("heavy_cc", "magic_heavy", "physical_heavy", "sustain")


def load_reviews(path=REVIEWS_PATH):
    if not path.exists():
        return []
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return doc.get("reviews") or []


def load_index(path=INDEX_PATH):
    import json
    return json.loads(path.read_text(encoding="utf-8"))


def core_entry_for(index, god, mode="Conquest"):
    """The god's shipped `core` build entry for a mode, or None.

    Deliberately the `core` archetype only. A claim about "the build" is a
    claim about the one the app opens on, not about whichever of the eleven
    flavors happens to contain the item and would let any claim pass."""
    for note in index.get("builds", []):
        if note.get("god") != god or note.get("mode") != mode:
            continue
        for entry in note.get("builds", []):
            if (entry.get("source") == "suggested"
                    and entry.get("archetype") == "core"
                    and not entry.get("fun")):
                return entry
    return None


def core_for(index, god, mode="Conquest"):
    """The god's shipped model core (its `slot_order`) for a mode, or None."""
    entry = core_entry_for(index, god, mode)
    return None if entry is None else list(entry.get("slot_order") or [])


def _support_solo_gods(index):
    return {g["name"] for g in index.get("gods", [])
            if "Support" in str(g.get("role") or "") or "Solo" in str(g.get("role") or "")}


def _subject(review):
    return " · ".join(x for x in (review.get("god"), review.get("mode")) if x) or "whole model"


def _bad(review, message):
    return ValueError(f"{_subject(review)} — {review.get('claim')}: {message}. "
                      "Fix data/_expert_reviews.yaml; a malformed claim must not "
                      "be scored.")


def _gods_in_scope(index, review, detail):
    """Which gods a population claim is counted over.

    `scope: support-solo` is the spelling the 2026-08-09 claim shipped with and
    stays; `scope: role:<Role>` matches the role string as a substring, so
    `role:Carry` takes "Carry" and "Carry Mid" both. No scope means the named
    god, or the whole roster when none is named. Anything else RAISES: a
    misspelled scope that quietly widened to the whole roster would score a
    different claim from the one written down."""
    scope = detail.get("scope")
    if scope is None:
        if review.get("god"):
            return [review["god"]]
        return sorted(g["name"] for g in index.get("gods", []))
    if scope == "support-solo":
        return sorted(_support_solo_gods(index))
    if isinstance(scope, str) and scope.startswith("role:"):
        role = scope[len("role:"):]
        return sorted(g["name"] for g in index.get("gods", [])
                      if role in str(g.get("role") or ""))
    raise _bad(review, f"scope {scope!r} is not 'support-solo' or 'role:<Role>'")


def _population(gods, hits, mode, offence, absence):
    """The shared verdict for a claim counted across a roster.

    "It shows up on everything" is a claim about a population, not about one
    build. None offending is clear; a handful (at most one in eight, and
    always one) is partial; more is holds."""
    if not hits:
        return "clear", absence.format(n=len(gods), mode=mode)
    if len(hits) <= max(1, len(gods) // 8):
        return "partial", f"still {offence} {len(hits)}/{len(gods)} cores: {hits}"
    return "holds", f"{offence} {len(hits)}/{len(gods)} cores: {hits}"


# --- validation ---------------------------------------------------------------
#
# A malformed claim RAISES. Before this existed `detail: {item: [...]}` — the
# key misspelled singular — read as an empty item list, and an empty list of
# absent items is "all present", so a typo cleared a claim. That is the same
# fail-open hole `regressions` closed for `last_verdict`, one field over.

def _names(review, detail, key, at_least=1):
    value = detail.get(key)
    if not isinstance(value, list) or len(value) < at_least or not all(
            isinstance(v, str) and v for v in value):
        raise _bad(review, f"detail.{key} must be a list of at least {at_least} item name(s)")
    return list(value)


def _validate(review, detail):
    claim = review.get("claim")
    if claim in ("missing-item", "item-overweighted"):
        _names(review, detail, "items")
    elif claim == "buy-order":
        _names(review, detail, "order", at_least=2)
    elif claim == "situational-swap":
        vs = detail.get("vs")
        if vs not in KNOWN_SITUATIONS:
            raise _bad(review, f"detail.vs {vs!r} is not one of {list(KNOWN_SITUATIONS)}; "
                       "the model emits a swap row for those four situations and no other")
        _names(review, detail, "items")
    elif claim == "composition":
        if bool(detail.get("stat")) == bool(detail.get("tag")):
            raise _bad(review, "composition needs exactly one of detail.stat / detail.tag")
        if detail.get("min") is None and detail.get("max") is None:
            raise _bad(review, "composition needs detail.min and/or detail.max")
    elif claim == "pairing":
        if not isinstance(detail.get("item"), str) or not detail["item"]:
            raise _bad(review, "detail.item must be one item name")
        _names(review, detail, "with")
    if detail.get("scope") is not None and claim not in ("item-overweighted", "composition"):
        raise _bad(review, f"detail.scope is only meaningful on a population claim, not {claim}")


# --- the kinds ----------------------------------------------------------------

def _check_missing_item(review, detail, index):
    wanted = detail["items"]
    mode = review.get("mode", "Conquest")
    core = core_for(index, review.get("god"), mode)
    if core is None:
        return "unchecked", f"no {mode} core for {review.get('god')}"
    present = [i for i in wanted if i in core]
    absent = [i for i in wanted if i not in core]
    if not absent:
        return "clear", f"all {len(wanted)} present in core"
    if present:
        return "partial", f"present {present} · still absent {absent}"
    return "holds", f"none of {wanted} in core: {core}"


def _check_item_overweighted(review, detail, index):
    """The objection is that these appear where they should not. Scoped claims
    are counted across the roster, because "it shows up on everything" is a
    claim about a population, not about one build."""
    wanted = detail["items"]
    mode = review.get("mode", "Conquest")
    gods = _gods_in_scope(index, review, detail)
    hits = [g for g in gods if any(i in (core_for(index, g, mode) or []) for i in wanted)]
    return _population(gods, hits, mode, offence="in",
                       absence="absent from all {n} {mode} cores in scope")


def _check_buy_order(review, detail, index):
    """detail.order is a list that must appear, in that relative order, in the
    core's `slot_order`. Items between them are fine; items swapped are not.

    FEWER THAN TWO NAMED ITEMS IN THE CORE IS `holds`, NOT `unchecked`. An
    ordering claim whose items vanish has no subject, and `regressions` skips
    `unchecked` rows, so reading it that way would let a resolved claim stop
    being checked without a word. Red, so a human looks."""
    order = detail["order"]
    mode = review.get("mode", "Conquest")
    core = core_for(index, review.get("god"), mode)
    if core is None:
        return "unchecked", f"no {mode} core for {review.get('god')}"
    present = [i for i in order if i in core]
    absent = [i for i in order if i not in core]
    if len(present) < 2:
        return "holds", (f"fewer than two of {order} are in the core, so it shows no "
                         f"such order: {core}")
    positions = [core.index(i) for i in present]
    shown = [i for i in core if i in present]
    if positions != sorted(positions):
        return "holds", f"core buys {shown}, not {present}: {core}"
    if absent:
        return "partial", f"{present} in order · absent {absent}"
    return "clear", f"core buys {present} in that order"


_COVERED = re.compile(r"\(([^()]+)\)\s*$")


def _check_situational_swap(review, detail, index):
    """detail.vs names a situation; detail.items are the swaps that would
    satisfy the reviewer, any one of them. The build's own row for that
    situation is the thing checked, with two ways to be right without a swap:
    the row saying the core already covers it with a named item, or a named
    item simply being in the core — "bring X against heavy CC" is satisfied
    by a build that always brings X."""
    vs, wanted = detail["vs"], detail["items"]
    mode = review.get("mode", "Conquest")
    entry = core_entry_for(index, review.get("god"), mode)
    if entry is None:
        return "unchecked", f"no {mode} core for {review.get('god')}"
    core = list(entry.get("slot_order") or [])
    in_core = [i for i in wanted if i in core]
    if in_core:
        return "clear", f"{in_core[0]} is in the core outright: {core}"
    rows = {r.get("vs_tag"): r for r in entry.get("situational_swaps") or []}
    row = rows.get(vs)
    if row is None:
        return "holds", f"no {vs} row on this build"
    swap = row.get("swap_item")
    if swap is None:
        m = _COVERED.search(str(row.get("swap") or ""))
        swap = m.group(1) if m else None
    if swap in wanted:
        return "clear", f"{vs} row: {row.get('swap')}"
    for other_vs, other in rows.items():
        if other_vs != vs and other.get("swap_item") in wanted:
            return "partial", (f"{other['swap_item']} is the {other_vs} swap, not the "
                               f"{vs} one ({row.get('swap')})")
    return "holds", f"{vs} swap is {row.get('swap')}, not any of {wanted}"


def _carries(item, stat=None, tag=None):
    if tag:
        return tag in (item.get("effect_tags") or [])
    value = (item.get("stats") or {}).get(stat)
    if value is None:
        return False
    try:
        return float(value) != 0
    except (TypeError, ValueError):
        return bool(value)


def _check_composition(review, detail, index):
    """How many core items carry detail.stat (an item stat key, e.g. "Physical
    Protection") or detail.tag (an effect tag, e.g. "sustain"), against
    detail.min and/or detail.max.

    FOR ONE GOD THIS IS TWO-VALUED. A bound is met or it is not; an off-by-one
    gradation would be a number nobody asserted. Over a `scope` it is the
    population verdict `item-overweighted` uses, so one offending god in a
    large roster is partial and several are holds."""
    stat, tag = detail.get("stat"), detail.get("tag")
    lo, hi = detail.get("min"), detail.get("max")
    mode = review.get("mode", "Conquest")
    by_name = {it.get("name"): it for it in index.get("items", [])}
    what = f"tag {tag!r}" if tag else f"stat {stat!r}"

    def carriers(core):
        return [n for n in core if _carries(by_name.get(n, {}), stat=stat, tag=tag)]

    def within(count):
        return (lo is None or count >= lo) and (hi is None or count <= hi)

    bound = " and ".join(s for s in (f"min {lo}" if lo is not None else "",
                                     f"max {hi}" if hi is not None else "") if s)
    if detail.get("scope") is None and review.get("god"):
        core = core_for(index, review["god"], mode)
        if core is None:
            return "unchecked", f"no {mode} core for {review['god']}"
        have = carriers(core)
        why = f"{len(have)} of {len(core)} core items carry {what} ({bound}): {have or core}"
        return ("clear" if within(len(have)) else "holds"), why

    gods = _gods_in_scope(index, review, detail)
    hits = [g for g in gods if not within(len(carriers(core_for(index, g, mode) or [])))]
    return _population(gods, hits, mode, offence=f"outside {bound} on {what} in",
                       absence=f"all {{n}} {{mode}} cores within {bound} on {what}")


def _check_pairing(review, detail, index):
    """detail.item should only be built alongside every item in detail.with.

    A build WITHOUT the item is vacuously clear — the claim says nothing about
    it — and the detail says "vacuous" so that a resolved pairing claim going
    green because the item was dropped is visible for what it is."""
    item, partners = detail["item"], detail["with"]
    mode = review.get("mode", "Conquest")
    core = core_for(index, review.get("god"), mode)
    if core is None:
        return "unchecked", f"no {mode} core for {review.get('god')}"
    if item not in core:
        return "clear", f"vacuous: {item} is not in the core: {core}"
    present = [p for p in partners if p in core]
    absent = [p for p in partners if p not in core]
    if not absent:
        return "clear", f"{item} built with all of {partners}"
    if present:
        return "partial", f"{item} built with {present} · without {absent}"
    return "holds", f"{item} built without any of {partners}: {core}"


_CHECKERS = {
    "missing-item": _check_missing_item,
    "item-overweighted": _check_item_overweighted,
    "buy-order": _check_buy_order,
    "situational-swap": _check_situational_swap,
    "composition": _check_composition,
    "pairing": _check_pairing,
}

#: Claim kinds the checker can actually evaluate. Anything else is recorded and
#: reported but never given a verdict — a checker that silently passes claims it
#: does not understand is worse than one that admits it.
CHECKABLE = tuple(_CHECKERS)


def check(review, index):
    """(verdict, detail) for one recorded claim.

    verdict is "holds" (the objection still stands), "clear" (it no longer
    does), "partial", or "unchecked". A malformed claim raises."""
    claim = review.get("claim")
    if claim not in _CHECKERS:
        return "unchecked", f"claim kind {claim!r} is recorded, not evaluated"
    detail = review.get("detail") or {}
    _validate(review, detail)
    return _CHECKERS[claim](review, detail, index)


MARK = {"clear": "[clear ]", "partial": "[partial]", "holds": "[HOLDS ]",
        "unchecked": "[  --  ]"}


def report(reviews, index, out=sys.stdout):
    rows = []
    for r in reviews:
        verdict, why = check(r, index)
        rows.append((r, verdict, why))
        print(f"{MARK[verdict]} {_subject(r)} — {r.get('claim')}", file=out)
        print(f"          {why}", file=out)
        if r.get("status") and r["status"] != "open":
            print(f"          status: {r['status']} (set by hand)", file=out)
    counts = {}
    for _, v, _ in rows:
        counts[v] = counts.get(v, 0) + 1
    print("", file=out)
    print("  ".join(f"{k}: {v}" for k, v in sorted(counts.items())), file=out)
    print("NOT a score. One reviewer, claims chosen because they looked wrong.",
          file=out)
    return rows


#: How good a verdict is. Only the ORDER matters — a claim moving DOWN this
#: scale is a regression, however far it moves.
VERDICT_RANK = {"holds": 0, "partial": 1, "clear": 2}


def regressions(rows):
    """Claims marked `resolved` whose verdict is worse than it was recorded at.

    This is the only condition worth failing a build on. An `open` claim that
    still holds is the normal state of a to-do item; a resolved one going
    backwards means a fix was undone.

    IT USED TO TEST `verdict == "holds"` ONLY, and that is not what "went
    backwards" means. A resolved claim degrading `clear` -> `partial` sailed
    through, which is not hypothetical: the 2026-08-19 effect-tag pass moved
    Ullr's Conquest core from "all 4 present" to "still absent
    ['Heartseeker']" — Titan's Bane displaced it — and `--check` stayed green
    for the whole change. The one gate in this project that is not made of the
    community's own data could rot one step at a time and never say so.

    The fix is a per-claim BASELINE rather than a global bar, because those are
    different things. `last_verdict` in `_expert_reviews.yaml` records what the
    checker said when a human last looked; anything worse than that fails. A
    claim recorded as `partial` and still `partial` is stable and passes, which
    is what lets the register hold a claim someone has accepted as partly
    answered (`item-overweighted` has been partial at Geb since before this
    check existed) without either lying about it or blocking every build.

    A claim with no `last_verdict` falls back to the old rule, so adding the
    field is opt-in and an unannotated register keeps working.

    AN UNRECOGNISED `last_verdict` RAISES rather than being tolerated. Read
    through `.get(baseline, 0)` a typo landed on rank 0 — the same rank as the
    worst real verdict — so nothing could sit below it and the check silently
    never fired for that claim again. `last_verdict: cleared` plus a current
    verdict of `holds` reported zero regressions; the correctly-spelled
    `clear` reported one.

    That is the same silent-typo hole `data_audit.KNOWN_TAGS` exists to close,
    in the one gate here not made of the community's own data, inside the fix
    written because that gate could rot without saying so. A gate that fails
    OPEN on a spelling mistake is worse than the bug it replaced, because the
    green tick is now evidence of nothing. Loud is the only safe direction."""
    out = []
    for r, verdict, _ in rows:
        if r.get("status") != "resolved" or verdict == "unchecked":
            continue
        baseline = r.get("last_verdict")
        if baseline is None:
            if verdict == "holds":
                out.append(r)
            continue
        if baseline not in VERDICT_RANK:
            raise ValueError(
                f"{_subject(r)} — {r.get('claim')}: last_verdict {baseline!r} is not one of "
                f"{sorted(VERDICT_RANK)}. Fix the spelling in _expert_reviews.yaml; "
                "an unrecognised baseline would silently disable this claim's check.")
        if VERDICT_RANK.get(verdict, 0) < VERDICT_RANK[baseline]:
            out.append(r)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if a resolved claim has regressed")
    args = ap.parse_args(argv)

    reviews = load_reviews()
    if not reviews:
        print("No expert reviews recorded.")
        return 0
    rows = report(reviews, load_index())
    back = regressions(rows)
    if back:
        print("")
        for r in back:
            was = r.get("last_verdict") or "clear"
            print(f"REGRESSED: {_subject(r)} — {r.get('claim')} was marked resolved "
                  f"at '{was}' and is worse now")
    if args.check and back:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
