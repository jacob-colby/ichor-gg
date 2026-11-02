"""Round 2: robots.txt in full, and do the existing parsers read api.php output
the same as the rendered page? Records raw responses as fixtures under
smite/tests/fixtures/recorded/ for the stats-refresh tests."""
import json, pathlib, sys, time
import requests
sys.path.insert(0, ".")
from smite import wiki_parser, refresh

UA = "ichor-gg/1.0 (+https://github.com/jacob-colby/ichor-gg; patch-day stats refresh)"
OUT = pathlib.Path("smite/tests/fixtures/recorded")
OUT.mkdir(parents=True, exist_ok=True)
S = requests.Session(); S.headers["User-Agent"] = UA

def get(url, **kw):
    time.sleep(1.5)
    r = S.get(url, timeout=30, **kw)
    print(f"[probe2] {r.status_code} {len(r.content):>7d}B cf={r.headers.get('cf-mitigated','-')} {url[:110]}")
    return r

r = get("https://wiki.smite2.com/robots.txt")
print("[probe2] ---- robots.txt ----"); print(r.text); print("[probe2] ---- end robots ----")
(OUT / "wiki_robots.txt").write_text(r.text)

API = "https://wiki.smite2.com/api.php"
for page, kind in [("Bancroft's Talon", "item"), ("Deathbringer", "item"), ("Mote of Chaos", "item"),
                   ("Chiron", "god"), ("Ullr", "god"), ("Merlin", "god"), ("Patch notes", "patch")]:
    r = get(API, params={"action": "parse", "page": page, "prop": "text|revid",
                         "format": "json", "formatversion": "2", "redirects": "1"})
    slug = page.lower().replace(" ", "_").replace("'", "")
    (OUT / f"api_parse_{slug}.json").write_text(r.text)
    html = r.json()["parse"]["text"]
    full = get("https://wiki.smite2.com/w/" + page.replace(" ", "_")).text
    (OUT / f"page_{slug}.html").write_text(full)
    if kind == "patch":
        import re
        nums = [int(m.group(1)) for m in refresh._PATCH_VERSION_RE.finditer(html)]
        print(f"[probe2] patch notes via api: max={max(nums) if nums else None}")
        continue
    fn = wiki_parser.parse_god_page if kind == "god" else wiki_parser.parse_item_page
    try:
        a, b = fn(html), fn(full)
        a.pop("image_url", None); b.pop("image_url", None)
        same = a == b
        print(f"[probe2] {page}: api parse == page parse: {same}"
              + (f" abilities={len(a.get('abilities', []))}" if kind == 'god' else f" stats={a.get('stats')} cost={a.get('cost')}"))
        if not same:
            for k in set(a) | set(b):
                if a.get(k) != b.get(k):
                    print(f"[probe2]   differs on {k}: api={str(a.get(k))[:120]} page={str(b.get(k))[:120]}")
    except Exception as exc:
        print(f"[probe2] {page}: parser error {exc!r}")

# Batch: can one request return many pages' revisions? (cheap staleness check)
r = get(API, params={"action": "query", "prop": "revisions", "rvprop": "timestamp|ids",
                     "titles": "Bancroft's Talon|Chiron|Ullr", "format": "json", "formatversion": "2"})
(OUT / "api_query_revisions.json").write_text(r.text)
print("[probe2]", r.text[:600])
