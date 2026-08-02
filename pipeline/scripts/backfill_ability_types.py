"""Backfill the fields the parser used to discard, from the existing cache.

`wiki_parser` dropped three things every god page already carried: Attack
Power (excluded by the STAT_LABELS allowlist), and the wiki's colour coding of
each ability detail line — which is the only place the game states whether an
ability lands as physical or magical damage. `get_text()` flattened the colour
away before anything could read it.

None of that needs refetching: it is sitting in the 247 pages under
`data/_cache/wiki`. This script re-parses those pages and merges only the new
fields into the God notes.

Deliberately narrow, on two counts:

  OFFLINE   The fetcher here reads the cache and raises if a page is missing.
            `refresh --all` would work too, but it shares a code path with the
            network and with SmiteBrain, and a backfill has no business making
            requests.

  ADDITIVE  Only the new keys are written. A full re-merge would also restamp
            `last_verified` and overwrite anything hand-corrected since the
            last scrape, which is not what "recover a dropped field" should
            mean.

Usage:  python -m scripts.backfill_ability_types [--dry-run]
"""
import argparse
import hashlib
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "pipeline"))

from smite import notes, refresh, wiki_parser  # noqa: E402

CACHE_DIR = REPO_ROOT / "data" / "_cache" / "wiki"
GODS_DIR = REPO_ROOT / "data" / "Gods"

# The keys this backfill is allowed to introduce. Anything else the parser now
# produces is left alone — a backfill that quietly rewrote unrelated fields
# would be indistinguishable from a bad scrape.
NEW_STATS = ("attack_power", "health_regen", "mana_regen")
NEW_ABILITY_KEYS = ("damage_type", "detail_kinds")


def cached_html(url: str) -> str | None:
    """The cached page for a URL, or None. Never fetches."""
    path = CACHE_DIR / f"{hashlib.sha256(url.encode('utf-8')).hexdigest()}.html"
    return path.read_text(encoding="utf-8") if path.exists() else None


def merge_god(frontmatter: dict, parsed: dict) -> dict:
    """Counts of what was added: {stats, abilities}. Mutates `frontmatter`."""
    added = {"stats": 0, "abilities": 0}

    base = frontmatter.setdefault("base_stats", {})
    for key in NEW_STATS:
        value = (parsed.get("base_stats") or {}).get(key)
        if value is not None and key not in base:
            base[key] = value
            added["stats"] += 1

    # Match on (slot, name) rather than position: a scrape that picked up a
    # different number of abilities must not shift every field by one.
    by_key = {(a.get("slot"), a.get("name")): a for a in parsed.get("abilities") or []}
    for ability in frontmatter.get("abilities") or []:
        fresh = by_key.get((ability.get("slot"), ability.get("name")))
        if not fresh:
            continue
        touched = False
        for key in NEW_ABILITY_KEYS:
            if key in fresh and key not in ability:
                ability[key] = fresh[key]
                touched = True
        added["abilities"] += bool(touched)

    return added


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="report, write nothing")
    args = ap.parse_args(argv)

    totals = {"gods": 0, "written": 0, "stats": 0, "abilities": 0}
    missing = []

    for path in sorted(GODS_DIR.glob("*.md")):
        frontmatter, body = notes.read_note(path)
        name = (frontmatter or {}).get("name")
        if not name:
            continue
        totals["gods"] += 1

        html = cached_html(refresh.WIKI_BASE + name.replace(" ", "_"))
        if html is None:
            missing.append(name)
            continue

        added = merge_god(frontmatter, wiki_parser.parse_god_page(html))
        totals["stats"] += added["stats"]
        totals["abilities"] += added["abilities"]
        if added["stats"] or added["abilities"]:
            totals["written"] += 1
            if not args.dry_run:
                notes.write_note(path, frontmatter, body)

    verb = "would update" if args.dry_run else "updated"
    print(f"{totals['gods']} gods read, {verb} {totals['written']}: "
          f"{totals['stats']} base stats, {totals['abilities']} abilities")
    if missing:
        print(f"[cache] {len(missing)} gods have no cached page and were skipped: "
              f"{', '.join(sorted(missing))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
