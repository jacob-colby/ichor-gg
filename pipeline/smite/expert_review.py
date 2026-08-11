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
"""
import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
REVIEWS_PATH = REPO_ROOT / "data" / "_expert_reviews.yaml"
INDEX_PATH = REPO_ROOT / "viewer" / "public" / "index.json"

#: Claim kinds the checker can actually evaluate. Anything else is recorded and
#: reported but never given a verdict — a checker that silently passes claims it
#: does not understand is worse than one that admits it.
CHECKABLE = ("missing-item", "item-overweighted")


def load_reviews(path=REVIEWS_PATH):
    if not path.exists():
        return []
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return doc.get("reviews") or []


def load_index(path=INDEX_PATH):
    import json
    return json.loads(path.read_text(encoding="utf-8"))


def core_for(index, god, mode="Conquest"):
    """The god's shipped model core for a mode, or None.

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
                return list(entry.get("slot_order") or [])
    return None


def _support_solo_gods(index):
    return {g["name"] for g in index.get("gods", [])
            if "Support" in str(g.get("role") or "") or "Solo" in str(g.get("role") or "")}


def check(review, index):
    """(verdict, detail) for one recorded claim.

    verdict is "holds" (the objection still stands), "clear" (it no longer
    does), "partial", or "unchecked"."""
    claim = review.get("claim")
    detail = review.get("detail") or {}
    if claim not in CHECKABLE:
        return "unchecked", f"claim kind {claim!r} is recorded, not evaluated"

    wanted = list(detail.get("items") or [])
    mode = review.get("mode", "Conquest")

    if claim == "missing-item":
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

    # item-overweighted: the objection is that these appear where they should
    # not. Scoped claims are counted across the roster, because "it shows up on
    # everything" is a claim about a population, not about one build.
    scope = detail.get("scope")
    if scope == "support-solo":
        gods = sorted(_support_solo_gods(index))
    elif review.get("god"):
        gods = [review["god"]]
    else:
        gods = sorted(g["name"] for g in index.get("gods", []))
    hits = []
    for god in gods:
        core = core_for(index, god, mode) or []
        if any(i in core for i in wanted):
            hits.append(god)
    if not hits:
        return "clear", f"absent from all {len(gods)} {mode} cores in scope"
    if len(hits) <= max(1, len(gods) // 8):
        return "partial", f"still in {len(hits)}/{len(gods)} cores: {hits}"
    return "holds", f"in {len(hits)}/{len(gods)} cores: {hits}"


MARK = {"clear": "[clear ]", "partial": "[partial]", "holds": "[HOLDS ]",
        "unchecked": "[  --  ]"}


def report(reviews, index, out=sys.stdout):
    rows = []
    for r in reviews:
        verdict, why = check(r, index)
        rows.append((r, verdict, why))
        subject = " · ".join(x for x in (r.get("god"), r.get("mode")) if x) or "whole model"
        print(f"{MARK[verdict]} {subject} — {r.get('claim')}", file=out)
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


def regressions(rows):
    """Claims a human marked `resolved` that the checker now says still hold.

    This is the only condition worth failing a build on. An `open` claim that
    still holds is the normal state of a to-do item; a resolved one coming back
    means a fix was undone."""
    return [r for r, verdict, _ in rows
            if r.get("status") == "resolved" and verdict == "holds"]


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
            subject = " · ".join(x for x in (r.get("god"), r.get("mode")) if x) or "whole model"
            print(f"REGRESSED: {subject} — {r.get('claim')} was marked resolved")
    if args.check and back:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
