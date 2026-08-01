"""What moved between two refreshes.

The snapshot system banks item *cost and stats*, so patch notes can say an item
got cheaper — but nothing recorded where anything was RANKED, which is the one
thing this site is about. A god going A to S is invisible in the patch notes.

Nothing new has to be stored to fix that: `viewer/public/index.json` is
committed on every refresh, so git already holds the ranking history. This
reads two revisions of it and reports the movement.

    python -m smite.rank_diff                    # last refresh vs the one before
    python -m smite.rank_diff HEAD~5 HEAD        # any two revisions
    python -m smite.rank_diff --items            # items instead of gods

A caveat the output states for itself: a diff spanning a change to the scoring
method reports the method change, not the patch. The `--since` line names both
revisions so that is visible rather than assumed.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = "viewer/public/index.json"

# Best to worst, so a positive move is upward.
TIER_ORDER = {"S": 0, "A": 1, "B": 2, "C": 3}


def _index_at(rev: str) -> dict:
    """The committed index.json at `rev`, or None when it isn't there."""
    try:
        blob = subprocess.run(
            ["git", "show", f"{rev}:{INDEX_PATH}"],
            cwd=REPO_ROOT, capture_output=True, text=True, encoding="utf-8", check=True,
        ).stdout
        return json.loads(blob)
    except (subprocess.CalledProcessError, ValueError):
        return None


def _revisions_touching_index(limit: int = 2) -> list:
    """The most recent commits that actually changed the index, newest first.

    Commits that left it alone are skipped: comparing against one would report
    no movement and read as "nothing changed this patch".
    """
    out = subprocess.run(
        ["git", "log", f"-{limit}", "--format=%H", "--", INDEX_PATH],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    ).stdout.split()
    return out


def _placements(index: dict, subject: str) -> dict:
    """name -> (our tier, community tier) for everything both sides placed."""
    entries = ((index or {}).get("tierlist") or {}).get(subject) or []
    return {
        e["name"]: (e.get("tier_ours"), e.get("tier_community"))
        for e in entries if e.get("name")
    }


def _move(old, new):
    """Signed rungs moved, positive = up. None when either side is unplaced —
    an arrival or a departure is not a movement and must not be scored as one."""
    if old not in TIER_ORDER or new not in TIER_ORDER:
        return None
    return TIER_ORDER[old] - TIER_ORDER[new]


def diff(old_index: dict, new_index: dict, subject: str = "gods") -> dict:
    """Movement between two indexes, split by what actually happened."""
    old, new = _placements(old_index, subject), _placements(new_index, subject)

    moved_ours, moved_community, arrived, departed = [], [], [], []
    for name in sorted(set(old) | set(new)):
        o_ours, o_comm = old.get(name, (None, None))
        n_ours, n_comm = new.get(name, (None, None))

        if name not in old:
            arrived.append(name)
            continue
        if name not in new:
            departed.append(name)
            continue

        step = _move(o_ours, n_ours)
        if step:
            moved_ours.append((name, o_ours, n_ours, step))
        step_c = _move(o_comm, n_comm)
        if step_c:
            moved_community.append((name, o_comm, n_comm, step_c))

    # Biggest movement first, then name, so runs are stable.
    moved_ours.sort(key=lambda r: (-abs(r[3]), r[0]))
    moved_community.sort(key=lambda r: (-abs(r[3]), r[0]))
    return {
        "ours": moved_ours,
        "community": moved_community,
        "arrived": arrived,
        "departed": departed,
    }


def _render(rows, heading):
    if not rows:
        return [f"{heading}: nothing moved"]
    out = [f"{heading}: {len(rows)}"]
    for name, before, after, step in rows:
        arrow = "up" if step > 0 else "down"
        out.append(f"  {name:<18} {before} -> {after}  ({arrow} {abs(step)})")
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description="Rank movement between two refreshes")
    parser.add_argument("revs", nargs="*", help="two git revisions (default: the last two that changed the index)")
    parser.add_argument("--items", action="store_true", help="items instead of gods")
    args = parser.parse_args(argv)

    if len(args.revs) == 2:
        new_rev, old_rev = args.revs[1], args.revs[0]
    else:
        revs = _revisions_touching_index(2)
        if len(revs) < 2:
            print("Need two committed revisions of index.json to compare.")
            return 1
        new_rev, old_rev = revs[0], revs[1]

    old_index, new_index = _index_at(old_rev), _index_at(new_rev)
    if old_index is None or new_index is None:
        print("Could not read index.json at one of those revisions.")
        return 1

    subject = "items" if args.items else "gods"
    result = diff(old_index, new_index, subject)

    print(f"--since {old_rev[:9]}  --until {new_rev[:9]}   ({subject})")
    # Named so a methodology change is not mistaken for a patch effect.
    print("(a span crossing a scoring change reports the scoring change)\n")
    print("\n".join(_render(result["ours"], "We moved")))
    print()
    print("\n".join(_render(result["community"], "The community moved")))
    if result["arrived"]:
        print(f"\nNewly ranked: {', '.join(result['arrived'])}")
    if result["departed"]:
        print(f"No longer ranked: {', '.join(result['departed'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
