"""Scrape the tier-1/2 components our items reference but we never tracked.

Every item note lists what it `builds_from`, and 41 of the 57 distinct
components named that way were absent from `data/Items`. That is not only a
broken link on the item page — it distorts the gold model.

The regression identifies a per-stat price by seeing the same stat priced in
different bundles. Tier-3 items bundle three or four stats together, so several
stats are collinear across the whole tier-3 set and their individual prices
cannot be separated. Cheap components are the items that break those ties:
they carry one or two stats each. With only 16 of 57 present, refitting without
them drives Lifesteal, Health Regen and Dampening to exactly zero — NNLS
hitting its non-negativity floor because nothing in the data can identify them.

So the fix is to have the components, not to drop the ones we do have.

Additive and resumable: an item already on disk is skipped, so a killed run
costs nothing and re-running finishes the job.

Usage:  python scripts/fetch_missing_components.py [--dry-run] [--limit N]
"""
import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "pipeline"))

from smite import notes, refresh  # noqa: E402
from smite.browser_fetch import BrowserFetcher  # noqa: E402

ITEMS_DIR = REPO_ROOT / "data" / "Items"


def survey():
    """`(have, missing)` — component names referenced by an item we track."""
    have, referenced = set(), set()
    for path in ITEMS_DIR.glob("*.md"):
        frontmatter, _ = notes.read_note(path)
        if not frontmatter.get("name"):
            continue
        have.add(frontmatter["name"])
        referenced |= set(frontmatter.get("builds_from") or [])
    return have, sorted(referenced - have)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="list them, fetch nothing")
    ap.add_argument("--limit", type=int, help="stop after N (for a quick check)")
    args = ap.parse_args(argv)

    have, missing = survey()
    if args.limit:
        missing = missing[:args.limit]
    print(f"{len(have)} items tracked, {len(missing)} referenced components missing")
    if args.dry_run or not missing:
        for name in missing:
            print(f"  {name}")
        return 0

    fetcher = BrowserFetcher(REPO_ROOT / "data" / "_cache" / "wiki")
    ok, failed = 0, []
    for i, name in enumerate(missing, 1):
        if (ITEMS_DIR / f"{name}.md").exists():
            continue                      # resumable: a prior run got it
        try:
            refresh.refresh_item(name, fetcher)
            ok += 1
            print(f"  [{i}/{len(missing)}] {name}")
        except Exception as exc:          # noqa: BLE001 - one bad page must not end the run
            failed.append((name, str(exc)[:90]))
            print(f"  [{i}/{len(missing)}] {name} — FAILED: {str(exc)[:90]}")

    print(f"\nfetched {ok}, failed {len(failed)}")
    for name, err in failed:
        print(f"  {name}: {err}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
