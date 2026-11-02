"""Record the wiki pages the new-entity path reads, from a runner.

The sandbox sessions cannot reach wiki.smite2.com; a GitHub-hosted runner can
(honest UA, robots-allowed `/w/<Page>` URLs only — see `stats_refresh`). This
fetches the roster grid, the Items index, every untracked god on the roster
and every untracked item the Items index links, and writes each response to
`smite/tests/fixtures/recorded/new_entities/` so the add path can be tested
offline against what the wiki actually serves. Prints one line per page.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, ".")
from smite import refresh, stats_refresh, wiki_parser  # noqa: E402

OUT = Path("smite/tests/fixtures/recorded/new_entities")
CAP = 20


def slug(page):
    return re.sub(r"[^a-z0-9]+", "_", page.lower()).strip("_")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    f = stats_refresh.WikiPageFetcher()
    # Start from what is already recorded. "Untracked" is decided against the
    # live data/, so an entity added since the last recording is not fetched
    # again, and replacing the index outright dropped it from the fixture —
    # which is how Nike, Hachiman, Kuzenbo and Hel left it (f454b88). A
    # re-record adds and refreshes entries; it never forgets one.
    index_path = OUT / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else {}

    def get(page, parse=None):
        try:
            html = f.fetch(page)
        except Exception as exc:
            print(f"[probe] FAIL {page}: {exc}")
            index[page] = {"error": str(exc)}
            return None
        name = f"page_{slug(page)}.html"
        (OUT / name).write_text(html, encoding="utf-8")
        verdict = ""
        if parse:
            try:
                p = parse(html)
                verdict = (f" abilities={len(p.get('abilities') or [])} aspects={len(p.get('aspects') or [])}"
                           f" base_stats={len(p.get('base_stats') or {})} role={p.get('role')}"
                           if parse is wiki_parser.parse_god_page else
                           f" tier={p.get('tier')} cost={p.get('cost')} stats={p.get('stats')}"
                           f" passive={(p.get('passive') or '')[:80]!r}")
            except Exception as exc:
                verdict = f" does not parse: {exc}"
        print(f"[probe] {len(html):>7d}B {page}{verdict}")
        index[page] = {"file": name}
        return html

    gods_html = get("Gods")
    roster = refresh.parse_roster_names(gods_html) if gods_html else []
    tracked_gods = {p.stem for p in (refresh.DATA_ROOT / "Gods").glob("*.md")}
    new_gods = [n for n in roster if n not in tracked_gods]
    print(f"[probe] roster {len(roster)}, untracked {new_gods}")
    for n in new_gods[:CAP]:
        get(n, wiki_parser.parse_god_page)

    items_html = get("Items")
    tracked = {refresh._icon_key(p.stem) for p in (refresh.DATA_ROOT / "Items").glob("*.md")}
    cands = {}
    if items_html:
        for tier, raw in refresh._ITEM_ICON_RE.findall(items_html):
            nm = raw.replace("_", " ").replace("%27", "'").strip()
            k = refresh._icon_key(nm)
            if k in tracked or refresh._ICON_VARIANT_SUFFIX_RE.sub("", k) in tracked:
                continue
            cands.setdefault(nm, tier)
        links = re.findall(r'<a href="/w/([^"#?]+)" title="([^"]+)"', items_html)
        print(f"[probe] Items page: {len(links)} links, untracked icon names {sorted(cands)}")
    for nm in sorted(cands)[:CAP]:
        get(nm, wiki_parser.parse_item_page)
    index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
