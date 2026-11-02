"""Can a GitHub-hosted runner reach the wiki's stats pages?

One line per request: HTTP status, bytes, Cloudflare's mitigation header, and
whether the existing parser reads the page. Prints, never writes, never fails.
Run by `.github/workflows/probe-stat-sources.yml` (dispatch only).

Only robots-allowed URLs: robots.txt itself and `/w/<Page>` article pages.
`api.php` is `Disallow`ed for every agent and is deliberately not probed.

First run, 2026-11-02: spoofed Chrome UA -> 403 cf-mitigated=challenge; the
honest UA `stats_refresh` sends -> 200, and parse output identical to the
rendered page on six pages including Ullr and Merlin.
"""
import sys

import requests

sys.path.insert(0, ".")
from smite import stats_refresh, wiki_parser  # noqa: E402

CHROME_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
             "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
PAGES = [("Patch_notes", None), ("Bancroft's_Talon", wiki_parser.parse_item_page),
         ("Ullr", wiki_parser.parse_god_page)]


def probe(url, ua, parse=None):
    try:
        r = requests.get(url, headers={"User-Agent": ua}, timeout=25)
    except Exception as exc:
        print(f"[probe] ERR {type(exc).__name__}: {exc}  {url}")
        return
    verdict = ""
    if parse and r.ok:
        try:
            parsed = parse(r.text)
            verdict = f" parses: abilities={len(parsed.get('abilities') or [])} stats={parsed.get('stats')}"
        except Exception as exc:
            verdict = f" does not parse: {exc}"
    print(f"[probe] {r.status_code} {len(r.content):>7d}B cf-mitigated={r.headers.get('cf-mitigated', '-')} "
          f"ua={'chrome' if ua == CHROME_UA else 'ichor'} {url}{verdict}")


def main():
    base = "https://wiki.smite2.com"
    probe(base + "/robots.txt", stats_refresh.USER_AGENT)
    for page, parse in PAGES:
        probe(f"{base}/w/{page}", stats_refresh.USER_AGENT, parse)
    probe(f"{base}/w/{PAGES[1][0]}", CHROME_UA)
    return 0


if __name__ == "__main__":
    sys.exit(main())
