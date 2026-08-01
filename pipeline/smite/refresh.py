"""CLI: refresh SMITE god/item/build notes from wiki.smite2.com and
smitebrain.com. Run as: python -m smite.refresh --refresh Chiron --kind god
"""
import argparse
import re
import sys
import json
from datetime import date
from pathlib import Path

import requests

from smite import notes, smitebrain_parser, wiki_parser
from smite.browser_fetch import BrowserFetcher
from smite.cache import CachedFetcher

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = REPO_ROOT / "data"
BUILDS_ROOT = REPO_ROOT / "data" / "builds"

WIKI_BASE = "https://wiki.smite2.com/w/"
SMITEBRAIN_BASE = "https://smitebrain.com/gods/"

# Matches link text like "SMITE 2 Open Beta 39" on the wiki's Patch_notes
# index. Deliberately loose on whitespace/case — the wiki is hand-authored,
# not generated.
_PATCH_VERSION_RE = re.compile(r"SMITE\s*2\s*Open\s*Beta\s*(\d+)", re.IGNORECASE)


def _download_icon(image_url: str, slug: str) -> None:
    """Download a god/item portrait/icon from wiki.smite2.com. The HTML
    pages are Cloudflare-gated (hence Playwright elsewhere in this module)
    but the static image files are not — confirmed with a plain requests
    fetch during planning — so this uses requests directly, no browser
    needed. Skips if already downloaded (>1000 bytes), same convention as
    the vault's other Gaming asset-download scripts."""
    if not image_url:
        return
    icons_dir = DATA_ROOT / "_assets" / "icons"
    out_path = icons_dir / f"{slug}.png"
    if out_path.exists() and out_path.stat().st_size > 1000:
        return

    full_url = "https://wiki.smite2.com" + image_url
    try:
        response = requests.get(full_url, timeout=20)
        response.raise_for_status()
    except Exception as exc:
        # A broken/expired icon URL is cosmetic, not a data failure — the
        # god/item note itself was already written by the caller before
        # this runs. Never let an icon miss look like a refresh failure.
        print(f"  [icon skip] {slug}: {exc}")
        return

    icons_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(response.content)


def refresh_patch_version(wiki_fetcher, force: bool = False):
    """Scrape the wiki's Patch_notes index for the current SMITE 2 patch
    (e.g. "Open Beta 39") and persist it to data/_patch.json, so the viewer
    can show which patch the shipped data reflects instead of just a vague
    "Updated yesterday".

    The page lists every patch link ("SMITE 2 Open Beta 39", "...Beta 38",
    ...), newest first in practice — but this parses every match and takes
    the highest N rather than trusting document order, since that ordering
    is just editorial convention on a wiki page, not a guarantee.

    Never raises: any fetch/parse failure (Cloudflare hiccup, wiki layout
    change, no matches at all) returns None and leaves an existing
    data/_patch.json untouched, exactly like a cosmetic icon-download miss
    elsewhere in this module — a failed patch-version scrape must not look
    like (or cause) a failed refresh."""
    import json

    try:
        html = wiki_fetcher.fetch(WIKI_BASE + "Patch_notes", force=force)
        numbers = [int(m.group(1)) for m in _PATCH_VERSION_RE.finditer(html)]
        if not numbers:
            return None
        patch = {"patch": f"Open Beta {max(numbers)}", "captured": date.today().isoformat()}
    except Exception as exc:
        print(f"  [patch skip] {exc}")
        return None

    patch_path = DATA_ROOT / "_patch.json"
    patch_path.parent.mkdir(parents=True, exist_ok=True)
    patch_path.write_text(json.dumps(patch, indent=2), encoding="utf-8")
    return patch


def refresh_god(name: str, wiki_fetcher, force: bool = False) -> None:
    url = WIKI_BASE + name.replace(" ", "_")
    parsed = wiki_parser.parse_god_page(wiki_fetcher.fetch(url, force=force))

    frontmatter = {
        "type": "smite-god",
        "name": name,
        "pantheon": parsed.get("pantheon"),
        "role": parsed.get("role"),
        "specializations": parsed.get("specializations", []),
        "damage_type": parsed.get("damage_type"),
        "release_date": parsed.get("release_date"),
        "base_stats": parsed["base_stats"],
        "abilities": parsed["abilities"],
        "aspects": parsed["aspects"],
        "source_url": url,
        "last_verified": date.today().isoformat(),
    }
    wiki_block = "\n".join(f"- {a['name']}" for a in parsed["abilities"])
    notes.merge_god_note(DATA_ROOT / "Gods" / f"{name}.md", frontmatter, wiki_block,
                          log_dir=DATA_ROOT / "_logs")
    slug = name.lower().replace(" ", "-").replace("'", "")
    _download_icon(parsed.get("image_url"), slug)
    _download_icon(wiki_parser.derive_headshot_url(parsed.get("image_url")), slug + "-head")


def refresh_item(name: str, wiki_fetcher, force: bool = False) -> None:
    url = WIKI_BASE + name.replace(" ", "_")
    parsed = wiki_parser.parse_item_page(wiki_fetcher.fetch(url, force=force))

    frontmatter = {
        "type": "smite-item",
        "name": name,
        "tier": parsed.get("tier"),
        "cost": parsed.get("cost"),
        "stats": parsed.get("stats", {}),
        "passive": parsed.get("passive"),
        "builds_from": parsed.get("builds_from", []),
        "builds_into": [],
        "source_url": url,
        "last_verified": date.today().isoformat(),
    }
    notes.merge_item_note(DATA_ROOT / "Items" / f"{name}.md", frontmatter,
                           parsed.get("passive", ""), log_dir=DATA_ROOT / "_logs")
    _download_icon(parsed.get("image_url"), name.lower().replace(" ", "-").replace("'", ""))


def refresh_builds_into() -> None:
    """Derive builds_into for every item by inverting builds_from across the
    whole Items/ set — the wiki never shows this relationship directly."""
    items_dir = DATA_ROOT / "Items"
    all_items = {}
    for path in items_dir.glob("*.md"):
        frontmatter, body = notes.read_note(path)
        if frontmatter.get("name"):
            all_items[frontmatter["name"]] = (path, frontmatter, body)

    builds_into = {name: [] for name in all_items}
    for name, (_, frontmatter, _) in all_items.items():
        for component in frontmatter.get("builds_from", []):
            if component in builds_into:
                builds_into[component].append(name)

    for name, (path, frontmatter, body) in all_items.items():
        frontmatter["builds_into"] = builds_into[name]
        notes.write_note(path, frontmatter, body)


# SmiteBrain publishes ONE page per god with no mode dimension, so its numbers
# are Conquest. Scraping it for other modes stored Conquest pick/win rates under
# a Joust label, which the tier list then presented as Joust community data.
# Only scrape community stats for modes the source actually covers.
COMMUNITY_MODES = {"conquest"}


# The god index: one request covering every god, with wins, losses and the
# exact match window. `division` is the rank band the numbers describe —
# Obsidian+ is the broadest of the three the source offers, so it carries the
# largest sample; the narrower Master+/Deity bands trade sample size for skill.
# Whatever is chosen has to be stated in the viewer, because "the community"
# means something different in each.
GOD_INDEX_URL = "https://smitebrain.com/gods/__data.json"
GOD_INDEX_DIVISION = "obsidian"


def refresh_god_index(community_fetcher, force: bool = False) -> dict:
    """Pull every god's win/loss record from the index, keyed by god name.

    One request for all of them, rather than a page each: the index is also
    the only place the source publishes a denominator, and the only place it
    covers gods that have no aspect at all — 18 of which the per-god scrape
    was silently skipping.

    Conquest only, like the rest of the community signal (see COMMUNITY_MODES).
    """
    url = f"{GOD_INDEX_URL}?division={GOD_INDEX_DIVISION}"
    payload = json.loads(community_fetcher.fetch(url, force=force))
    rows = smitebrain_parser.parse_god_index(payload)
    # Aspect-split rows would collide on god name; the default response is
    # already god-level, but guard rather than trust the query string.
    return {r["god"]: r for r in rows if r.get("aspect") in (None, "None")}


def god_index_entry(row: dict) -> dict:
    """The community-entry fields carried by one index row.

    Namespaced `god_*` so they never read as the aspect's numbers, which sit
    in the same entry and mean something narrower. Provenance travels with
    the figures — a win rate without its rank band and date window is not a
    fact anyone can check.
    """
    return {
        "god_win_rate": row.get("win_rate"),
        "god_matches_won": row.get("matches_won"),
        "god_matches_played": row.get("matches_played"),
        "god_division": GOD_INDEX_DIVISION,
        "god_window_start": (row.get("start_time") or "")[:10] or None,
        "god_window_end": (row.get("end_time") or "")[:10] or None,
        "god_matches_analyzed": row.get("matches_analyzed"),
    }


ITEM_INDEX_URL = "https://smitebrain.com/items/__data.json"
# Sits beside _roster.json / _patch.json: a small, versioned table the index
# build reads. Items have no per-item build note the way gods do, so their
# community record needs a home of its own rather than being derived at index
# time from whatever happened to appear in a god's slot list.
COMMUNITY_ITEMS_FILE = "_community_items.json"


def refresh_item_index(community_fetcher, data_root: Path, force: bool = False) -> int:
    """Pull every item's win rate and match count, and store the table.

    The previous item signal was the *mean of per-god win rates* over the gods
    whose community build happened to list the item — unweighted, so an item in
    two builds counted as loudly as one in forty, and derived from the same
    aspect figures the god path just moved away from. This is the item's own
    record against a real denominator.
    """
    url = f"{ITEM_INDEX_URL}?division={GOD_INDEX_DIVISION}"
    payload = json.loads(community_fetcher.fetch(url, force=force))
    rows = smitebrain_parser.parse_item_index(payload)
    table = {
        r["display_name"]: {
            "win_rate": r["win_rate"],
            "matches_won": r["matches_won"],
            "matches_played": r["matches_played"],
            "use_rate": r.get("use_rate"),
        }
        for r in rows
    }
    out = {
        "division": GOD_INDEX_DIVISION,
        "window_start": (rows[0].get("start_time") or "")[:10] if rows else None,
        "window_end": (rows[0].get("end_time") or "")[:10] if rows else None,
        "matches_analyzed": rows[0].get("matches_analyzed") if rows else None,
        "items": table,
    }
    (data_root / COMMUNITY_ITEMS_FILE).write_text(
        json.dumps(out, indent=2, sort_keys=True), encoding="utf-8")
    return len(table)


def refresh_god_builds(god: str, mode: str, community_fetcher, force: bool = False,
                       index_row: dict | None = None) -> None:
    """`index_row` is this god's row from `refresh_god_index`, when the caller
    has already pulled it. Absent, the note keeps only the aspect figures and
    the tier list falls back to scoring by those — degraded, not broken."""
    if mode.lower() not in COMMUNITY_MODES:
        return
    slug = god.lower().replace(" ", "-").replace("'", "")
    url = f"{SMITEBRAIN_BASE}{slug}/"
    parsed = smitebrain_parser.parse_build_page(community_fetcher.fetch(url, force=force))

    aspect = parsed["aspects"][0] if parsed["aspects"] else None
    community_entry = {
        "aspect": aspect["name"] if aspect else None,
        "aspect_pick_rate": aspect["pick_rate"] if aspect else None,
        "aspect_win_rate": aspect["win_rate"] if aspect else None,
        "slot_order": parsed["items"],
        "source_url": url,
        "last_verified": date.today().isoformat(),
    }
    if index_row:
        community_entry.update(god_index_entry(index_row))
    notes.merge_build_note(BUILDS_ROOT / f"{god}-{mode}.md", god, mode, community_entry)


def refresh_all(force: bool = False) -> None:
    """Re-pull every god/item already known (i.e. already has a note under
    Gods/ or Items/) plus the community build for every Build note's god.
    Discovering brand-new gods/items that don't have a note yet is still a
    manual first `--refresh <name> --kind ...` — this only refreshes what's
    already tracked, matching a deliberate on-demand/weekly full pass rather
    than continuous roster discovery.

    A failure on one god/item/build (changed wiki layout, malformed note,
    wrong SmiteBrain slug, ...) is isolated and logged rather than aborting
    the whole run — an unattended weekly pass should get through everything
    it can and report what it couldn't, not silently stop partway."""
    wiki_fetcher = BrowserFetcher(DATA_ROOT / "_cache" / "wiki")
    community_fetcher = CachedFetcher(DATA_ROOT / "_cache" / "smitebrain")
    failures = []

    refresh_patch_version(wiki_fetcher, force=force)

    god_names = [notes.read_note(p)[0].get("name") for p in (DATA_ROOT / "Gods").glob("*.md")]
    for name in filter(None, god_names):
        try:
            refresh_god(name, wiki_fetcher, force=force)
        except Exception as exc:
            print(f"  [FAILED] god '{name}': {exc}")
            failures.append(f"god '{name}': {exc}")

    item_names = [notes.read_note(p)[0].get("name") for p in (DATA_ROOT / "Items").glob("*.md")]
    for name in filter(None, item_names):
        try:
            refresh_item(name, wiki_fetcher, force=force)
        except Exception as exc:
            print(f"  [FAILED] item '{name}': {exc}")
            failures.append(f"item '{name}': {exc}")
    if item_names:
        refresh_builds_into()

    # One request for every god's win/loss record, before the per-god loop —
    # a failure here degrades the run to aspect-only figures rather than
    # aborting it, which is the same isolation the loop below uses.
    god_index = {}
    try:
        god_index = refresh_god_index(community_fetcher, force=force)
        print(f"  god index: {len(god_index)} gods with win/loss records")
    except Exception as exc:
        print(f"  [FAILED] god index: {exc} — falling back to aspect figures")
        failures.append(f"god index: {exc}")

    # Items get the same treatment, and must be pulled in the same run: their
    # table is a stored artifact, so skipping it leaves item stats frozen at
    # whenever it was last written while every other figure moves on.
    try:
        n_items = refresh_item_index(community_fetcher, DATA_ROOT, force=force)
        print(f"  item index: {n_items} items with win/loss records")
    except Exception as exc:
        print(f"  [FAILED] item index: {exc} — item stats keep their last values")
        failures.append(f"item index: {exc}")

    build_paths = list(BUILDS_ROOT.glob("*.md"))
    for build_path in build_paths:
        build_frontmatter, _ = notes.read_note(build_path)
        god, mode = build_frontmatter.get("god"), build_frontmatter.get("mode")
        if god and mode:
            try:
                refresh_god_builds(god, mode, community_fetcher, force=force,
                                   index_row=god_index.get(god))
            except Exception as exc:
                print(f"  [FAILED] build '{god}-{mode}': {exc}")
                failures.append(f"build '{god}-{mode}': {exc}")

    total = len(god_names) + len(item_names) + len(build_paths)
    print(f"Refresh complete: {total - len(failures)}/{total} succeeded")
    if failures:
        print(f"{len(failures)} failed:")
        for f in failures:
            print(f"  - {f}")


# Pantheon/section labels that appear alongside gods in the wiki's Gods grid.
_ROSTER_NON_GODS = {
    "Arthurian", "Babylonian", "Celtic", "Chinese", "Egyptian", "Greek", "Hindu",
    "Japanese", "Korean", "Maya", "Norse", "Polynesian", "Roman", "Voodoo",
    "Yoruba", "Tales of Arabia", "Gems",
}


def refresh_roster(wiki_fetcher, force: bool = False) -> list:
    """Scrape the full SMITE 2 god roster (names) from the wiki's Gods page so the
    dev add-god modal can list every god, tracked or not. Thumbnails on that page
    are JS-loaded placeholders, so the roster is names-only; the modal shows local
    head icons for tracked gods and initials for the rest."""
    import json
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(wiki_fetcher.fetch(WIKI_BASE + "Gods", force=force), "html.parser")
    names = []
    for a in soup.select('span[typeof="mw:File"] a[href^="/w/"][title]'):
        t = a.get("title")
        if t and t not in _ROSTER_NON_GODS and t not in names:
            names.append(t)
    roster = [{"name": n, "thumb": ""} for n in sorted(names)]
    (DATA_ROOT / "_roster.json").write_text(
        json.dumps(roster, indent=2, ensure_ascii=False), encoding="utf-8")
    return roster


def refresh_roster_add_all(force: bool = False) -> dict:
    """Scrape every roster god not yet tracked so the pool can grow toward
    the full roster in one run. A single god's scrape failure (Cloudflare,
    parse error, wrong slug, ...) is caught and recorded rather than
    aborting the batch — an unattended bulk-add should get through
    everything it can and report what it couldn't. Does NOT reindex; that's
    a separate step after the operator reviews the failures."""
    import json

    roster_path = DATA_ROOT / "_roster.json"
    if not roster_path.exists():
        return {"added": [], "failed": [], "skipped": 0,
                "note": f"{roster_path} not found; run --roster first"}

    roster = json.loads(roster_path.read_text(encoding="utf-8"))
    roster_names = [g["name"] for g in roster]
    tracked = {p.stem for p in (DATA_ROOT / "Gods").glob("*.md")}
    untracked = [name for name in roster_names if name not in tracked]

    wiki = BrowserFetcher(DATA_ROOT / "_cache" / "wiki")
    community = CachedFetcher(DATA_ROOT / "_cache" / "smitebrain")

    added = []
    failed = []
    for name in untracked:
        try:
            refresh_god(name, wiki, force=force)
            refresh_god_builds(name, "Conquest", community, force=force)
            added.append(name)
        except Exception as exc:
            failed.append((name, str(exc)))

    return {"added": added, "failed": failed, "skipped": len(roster_names) - len(untracked)}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Refresh SMITE 2 reference data")
    parser.add_argument("--refresh", metavar="NAME", help="re-pull one god or item by name")
    parser.add_argument("--kind", choices=["god", "item"], help="required with --refresh")
    parser.add_argument("--refresh-builds", metavar="GOD", help="re-pull SmiteBrain build stats for one god")
    parser.add_argument("--mode", default="Conquest", help="game mode for --refresh-builds")
    parser.add_argument("--all", action="store_true", help="re-pull everything already tracked")
    parser.add_argument("--roster", action="store_true", help="refresh the full god roster (_roster.json)")
    parser.add_argument("--roster-add-all", action="store_true",
                         help="scrape every roster god not yet tracked (no reindex)")
    parser.add_argument("--patch", action="store_true",
                         help="refresh the current SMITE 2 patch version (data/_patch.json)")
    parser.add_argument("--force", action="store_true", help="bypass the local cache")
    args = parser.parse_args(argv)

    if args.patch:
        result = refresh_patch_version(BrowserFetcher(DATA_ROOT / "_cache" / "wiki"), force=args.force)
        if result:
            print(f"Refreshed patch version: {result['patch']}")
        else:
            print("Could not determine the current patch version (fetch/parse failed)")
        return 0

    if args.roster:
        roster = refresh_roster(BrowserFetcher(DATA_ROOT / "_cache" / "wiki"), force=args.force)
        print(f"Refreshed roster: {len(roster)} gods")
        return 0

    if args.roster_add_all:
        summary = refresh_roster_add_all(force=args.force)
        if summary.get("note"):
            print(summary["note"])
        print(f"Added {len(summary['added'])}, failed {len(summary['failed'])}, "
              f"skipped {summary['skipped']} (already tracked)")
        for name, err in summary["failed"]:
            print(f"  FAILED {name}: {err}")
        return 0

    if args.all:
        refresh_all(force=args.force)
        print("Refreshed all tracked gods, items, and builds")
        return 0

    if args.refresh:
        if args.kind not in ("god", "item"):
            print("--refresh requires --kind god|item", file=sys.stderr)
            return 1
        wiki_fetcher = BrowserFetcher(DATA_ROOT / "_cache" / "wiki")
        if args.kind == "god":
            refresh_god(args.refresh, wiki_fetcher, force=args.force)
        else:
            refresh_item(args.refresh, wiki_fetcher, force=args.force)
            refresh_builds_into()
        print(f"Refreshed {args.kind} '{args.refresh}'")
        return 0

    if args.refresh_builds:
        community_fetcher = CachedFetcher(DATA_ROOT / "_cache" / "smitebrain")
        refresh_god_builds(args.refresh_builds, args.mode, community_fetcher, force=args.force)
        print(f"Refreshed community build for '{args.refresh_builds}' ({args.mode})")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
