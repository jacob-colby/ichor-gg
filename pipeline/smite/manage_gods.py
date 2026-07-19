"""Add or remove a god from the tracked pool. Invoked by the viewer's dev-only
/api/gods endpoint (owner operation — add scrapes the wiki via Playwright).

Usage: python -m smite.manage_gods add "<God Name>"
       python -m smite.manage_gods remove "<God Name>"
"""
import json
import shutil
import sys

from smite import recommend, build_index
from smite.refresh import DATA_ROOT, refresh_god, refresh_god_builds
from smite.browser_fetch import BrowserFetcher
from smite.cache import CachedFetcher

GODS_ROOT = DATA_ROOT / "Gods"
BUILDS_ROOT = recommend.BUILDS_ROOT


def _reindex():
    recommend.main(["--all"])
    build_index.write_index(
        recommend.VAULT_ROOT,
        recommend.VAULT_ROOT / "viewer" / "public" / "index.json",
    )


def _fail(msg):
    print(json.dumps({"ok": False, "error": msg}))
    return 1


def add(name):
    name = (name or "").strip()
    if not name:
        return _fail("name required")
    try:
        wiki = BrowserFetcher(DATA_ROOT / "_cache" / "wiki")
        refresh_god(name, wiki)
        community = CachedFetcher(DATA_ROOT / "_cache" / "smitebrain")
        refresh_god_builds(name, "Conquest", community)
    except Exception as exc:  # scrape failure -> no partial pool entry
        return _fail(f"scrape failed for {name!r}: {exc}")
    _reindex()
    print(json.dumps({"ok": True}))
    return 0


def remove(name):
    name = (name or "").strip()
    god_note = GODS_ROOT / f"{name}.md"
    if not god_note.exists():
        return _fail(f"not a tracked god: {name!r}")
    (GODS_ROOT / "_removed").mkdir(exist_ok=True)
    shutil.move(str(god_note), str(GODS_ROOT / "_removed" / f"{name}.md"))
    removed_builds = BUILDS_ROOT / "_removed"
    removed_builds.mkdir(exist_ok=True)
    for p in BUILDS_ROOT.glob(f"{name}-*.md"):
        shutil.move(str(p), str(removed_builds / p.name))
    _reindex()
    print(json.dumps({"ok": True}))
    return 0


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) < 2 or argv[0] not in ("add", "remove"):
        return _fail("usage: manage_gods add|remove <name>")
    return add(argv[1]) if argv[0] == "add" else remove(argv[1])


if __name__ == "__main__":
    sys.exit(main())
