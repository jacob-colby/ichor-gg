"""The god page's "Recent builds": what players bought, newest first.

    python -m smite.recent_builds        # writes viewer/public/recent/<slug>.json

DATA, not model. It reads the per-match store `aspect_matches` keeps and ships
the newest `KEEP` matches per god in a form the viewer can filter without a
server. Nothing here reaches a score.

WHAT IT CAN AND CANNOT SHOW (measured 2026-11-09 on the 36,947-match store):
  * It is an ASPECT feed. 36,137 of the matches carry an aspect; the 810 that
    do not are a ten-per-god contrast sample, not a census. A god with no
    aspect has no file at all. The page says so rather than passing the sample
    off as "recent base-kit builds".
  * `rank` is SmiteBrain's finishing rank within Obsidian+. The only cut the
    source documents is Master+ (rank >= `MASTER_RANK`), so that is the only
    rank filter offered; inventing finer bands would be a claim nobody measured.
  * `placement == 1` is the team's WIN (`aspect_matches` shows the three
    checks). Items are INVENTORY slots, not a buy order, so the list is shown
    as a set of items and never as an order.
  * A match is not a player. The store holds no identifier by design.

SIZE. 13 MB of store becomes about 15-25 KB per god, fetched only when the
Community view is opened, the same way `side_by_side/<slug>.json` is.
"""
import argparse
import json
from pathlib import Path

from smite import aspect_matches as am

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "viewer" / "public" / "recent"

#: Newest matches kept per god. Enough for every filter to still leave a page
#: of results on a busy god, small enough to stay a lazy fetch.
KEEP = 80
#: Master+ cut, from `aspect_matches.DIVISION`'s own note.
MASTER_RANK = 4400


_SMALL = {"of", "the", "and"}


def _title(slug: str) -> str:
    """A slug nobody has a note for (relics: `aegis-of-acceleration`)."""
    return " ".join(w if i and w in _SMALL else w.capitalize() for i, w in enumerate(slug.split("-")))


def _names(slug, names):
    return None if slug is None else names.get(slug) or _title(slug)


def god_file(god_slug: str, meta: dict, names: dict, root: Path = am.STORE_ROOT):
    """One god's payload, or None when the store has nothing for them."""
    flat = [r for recs in am.load_god(root, god_slug).values() for r in recs]
    if not flat:
        return None
    flat = sorted(flat, key=lambda r: r["t"], reverse=True)[:KEEP]
    aspect_names = {a["value"]: a["name"] for a in meta.get("aspects", {}).get(god_slug, [])}
    builds = []
    for r in flat:
        items = [_names(s, names) for s in r["items"] if s]
        builds.append({
            "t": r["t"],
            "win": r["placement"] == 1,
            "role": r["role"],
            "master": (r["rank"] or 0) >= MASTER_RANK,
            "aspect": aspect_names.get(r["aspect"], r["aspect"]) if r["aspect"] else None,
            "patch": am.window_of(r["t"], meta),
            "items": items,
            "starter": _names(r["starter"], names),
            "relic": _names(r["relic"], names),
        })
    return {
        "god": god_slug,
        "kept": len(builds),
        "aspects": sorted(aspect_names.values()),
        "patches": sorted({b["patch"] for b in builds if b["patch"]}, reverse=True),
        "roles": sorted({b["role"] for b in builds}),
        "builds": builds,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", type=Path, default=OUT_DIR)
    args = ap.parse_args(argv)
    meta = am.load_meta()
    names = am.item_name_lookup()
    args.out.mkdir(parents=True, exist_ok=True)
    wrote = 0
    for slug in sorted(meta.get("aspects", {})):
        payload = god_file(slug, meta, names)
        if payload is None:
            continue
        path = args.out / f"{slug}.json"
        text = json.dumps(payload, separators=(",", ":")) + "\n"
        if not path.exists() or path.read_text() != text:
            path.write_text(text)
        wrote += 1
    print(f"recent builds: {wrote} gods -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
