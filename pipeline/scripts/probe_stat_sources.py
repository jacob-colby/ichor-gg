"""Can a GitHub-hosted runner reach a source of item and god STATS?

Logs one line per URL: HTTP status, byte count, the Cloudflare mitigation
header if any, and a short verdict. Prints, never writes, never fails — the
job log is the result. Run by `.github/workflows/probe-stat-sources.yml`.

    python scripts/probe_stat_sources.py
"""
import json
import sys

import requests

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
BOT_UA = "ichor-gg-probe/1.0 (+https://github.com/jacob-colby/ichor-gg)"

ITEM = "Bancroft's_Talon"
GOD = "Chiron"

PLAIN = [
    ("wiki html item", f"https://wiki.smite2.com/w/{ITEM}"),
    ("wiki robots", "https://wiki.smite2.com/robots.txt"),
    ("wiki api siteinfo /api.php", "https://wiki.smite2.com/api.php?action=query&meta=siteinfo&format=json"),
    ("wiki api siteinfo /w/api.php", "https://wiki.smite2.com/w/api.php?action=query&meta=siteinfo&format=json"),
    ("wiki api parse item", f"https://wiki.smite2.com/api.php?action=parse&page={ITEM}&prop=text&format=json&formatversion=2"),
    ("wiki api parse god", f"https://wiki.smite2.com/api.php?action=parse&page={GOD}&prop=text&format=json&formatversion=2"),
    ("wiki api parse patch notes", "https://wiki.smite2.com/api.php?action=parse&page=Patch_notes&prop=text&format=json&formatversion=2"),
    ("wiki raw wikitext", f"https://wiki.smite2.com/w/index.php?title={ITEM}&action=raw"),
    ("smitebrain items index", "https://smitebrain.com/items/__data.json?division=obsidian"),
    ("smitebrain item page", "https://smitebrain.com/items/bancrofts-talon/__data.json"),
    ("smitebrain robots", "https://smitebrain.com/robots.txt"),
    ("smite2.com", "https://www.smite2.com/"),
    ("smitesource", "https://www.smitesource.com/"),
    ("smitesource robots", "https://www.smitesource.com/robots.txt"),
    ("steam news", "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=2437170&count=3&feeds=steam_community_announcements"),
]


def probe(label, url, ua):
    try:
        r = requests.get(url, headers={"User-Agent": ua}, timeout=25)
        body = r.content
        cf = r.headers.get("cf-mitigated", "")
        ctype = r.headers.get("content-type", "").split(";")[0]
        head = body[:160].decode("utf-8", "replace").replace("\n", " ")
        print(f"[probe] {label:32s} {r.status_code} {len(body):>8d}B {ctype:24s} "
              f"cf-mitigated={cf or '-'} | {head}")
        return r
    except Exception as exc:
        print(f"[probe] {label:32s} ERR {type(exc).__name__}: {exc}")
        return None


def describe_smitebrain_items(r):
    """What does a SmiteBrain item row carry? Stats, or only rates?"""
    try:
        payload = r.json()
        text = json.dumps(payload)
        for key in ("Intelligence", "Strength", "Physical Protection", "stats", "cost", "price"):
            print(f"[probe]   smitebrain items payload mentions {key!r}: {key in text}")
    except Exception as exc:
        print(f"[probe]   smitebrain items payload unreadable: {exc!r}")


def describe_wiki_parse(r):
    try:
        html = r.json()["parse"]["text"]
        sys.path.insert(0, ".")
        from smite import wiki_parser
        parsed = wiki_parser.parse_item_page(html)
        print(f"[probe]   wiki api parse -> parse_item_page: tier={parsed.get('tier')} "
              f"cost={parsed.get('cost')} stats={parsed.get('stats')}")
    except Exception as exc:
        print(f"[probe]   wiki api parse not usable: {exc!r}")


def browser_probe():
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        print(f"[probe] playwright unavailable: {exc}")
        return
    for url in (f"https://wiki.smite2.com/w/{ITEM}",
                f"https://wiki.smite2.com/api.php?action=parse&page={ITEM}&prop=text&format=json&formatversion=2"):
        try:
            with sync_playwright() as p:
                b = p.chromium.launch()
                page = b.new_page(user_agent=UA)
                resp = page.goto(url, wait_until="networkidle", timeout=45000)
                html = page.content()
                title = page.title()
                b.close()
            print(f"[probe] playwright {url[:70]:70s} {resp.status if resp else '?'} "
                  f"{len(html)}B title={title!r} infobox={'infobox' in html}")
        except Exception as exc:
            print(f"[probe] playwright {url[:70]} ERR {type(exc).__name__}: {exc}")


def main():
    for label, url in PLAIN:
        r = probe(label, url, UA)
        if label == "wiki api parse item" and r is not None and r.ok:
            describe_wiki_parse(r)
        if label == "smitebrain items index" and r is not None and r.ok:
            describe_smitebrain_items(r)
    print("[probe] --- same wiki URLs with an honest bot User-Agent ---")
    for label, url in PLAIN[:6]:
        probe(label + " (bot UA)", url, BOT_UA)
    print("[probe] --- headless Chromium ---")
    browser_probe()
    return 0


if __name__ == "__main__":
    sys.exit(main())
