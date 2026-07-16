"""CLI: refresh SMITE god/item/build notes from wiki.smite2.com and
smitebrain.com. Run as: python -m smite.refresh --refresh Chiron --kind god
"""
import argparse
import sys
from pathlib import Path

from smite import notes, smitebrain_parser, wiki_parser
from smite.browser_fetch import BrowserFetcher
from smite.cache import CachedFetcher

VAULT_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = VAULT_ROOT / "04. System" / "Data" / "SMITE"
BUILDS_ROOT = VAULT_ROOT / "03. Workspaces" / "Gaming" / "SMITE 2" / "Builds"

WIKI_BASE = "https://wiki.smite2.com/w/"
SMITEBRAIN_BASE = "https://smitebrain.com/gods/"


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
    }
    wiki_block = "\n".join(f"- {a['name']}" for a in parsed["abilities"])
    notes.merge_god_note(DATA_ROOT / "Gods" / f"{name}.md", frontmatter, wiki_block,
                          log_dir=DATA_ROOT / "_logs")


def refresh_item(name: str, wiki_fetcher, force: bool = False) -> None:
    url = WIKI_BASE + name.replace(" ", "_")
    parsed = wiki_parser.parse_item_page(wiki_fetcher.fetch(url, force=force))

    frontmatter = {
        "type": "smite-item",
        "name": name,
        "tier": parsed.get("tier"),
        "cost": parsed.get("cost"),
        "passive": parsed.get("passive"),
        "builds_from": parsed.get("builds_from", []),
        "builds_into": [],
        "source_url": url,
    }
    notes.merge_item_note(DATA_ROOT / "Items" / f"{name}.md", frontmatter,
                           parsed.get("passive", ""), log_dir=DATA_ROOT / "_logs")


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


def refresh_god_builds(god: str, mode: str, community_fetcher, force: bool = False) -> None:
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
    }
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

    build_paths = list(BUILDS_ROOT.glob("*.md"))
    for build_path in build_paths:
        build_frontmatter, _ = notes.read_note(build_path)
        god, mode = build_frontmatter.get("god"), build_frontmatter.get("mode")
        if god and mode:
            try:
                refresh_god_builds(god, mode, community_fetcher, force=force)
            except Exception as exc:
                print(f"  [FAILED] build '{god}-{mode}': {exc}")
                failures.append(f"build '{god}-{mode}': {exc}")

    total = len(god_names) + len(item_names) + len(build_paths)
    print(f"Refresh complete: {total - len(failures)}/{total} succeeded")
    if failures:
        print(f"{len(failures)} failed:")
        for f in failures:
            print(f"  - {f}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Refresh SMITE 2 reference data")
    parser.add_argument("--refresh", metavar="NAME", help="re-pull one god or item by name")
    parser.add_argument("--kind", choices=["god", "item"], help="required with --refresh")
    parser.add_argument("--refresh-builds", metavar="GOD", help="re-pull SmiteBrain build stats for one god")
    parser.add_argument("--mode", default="Conquest", help="game mode for --refresh-builds")
    parser.add_argument("--all", action="store_true", help="re-pull everything already tracked")
    parser.add_argument("--force", action="store_true", help="bypass the local cache")
    args = parser.parse_args(argv)

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
