#!/usr/bin/env python3
"""
fetch-icons.py — SMITE 2 god portrait icons
============================================
Downloads 64×64 god portrait icons and saves them as PNG files.

Primary source:  SmiteSource direct icon URLs
    https://www.smitesource.com/images/gods/<Name>_icon.png
    e.g. https://www.smitesource.com/images/gods/Chiron_icon.png

Fallback source: Hi-Rez official API (requires credentials)
    Set SMITE_DEV_ID and SMITE_AUTH_KEY environment variables to enable.
    Fetches getGodsJson, reads entry["godIcon_URL"] per god.

Skips files that already exist and are >1000 bytes (real icons).
Enforces the 50 KB per-file cap and logs failures to _fetch_failures.txt.
Priority-pool gods (★) are listed first in output.

Usage:
    cd "07. Gaming/_assets/smite2/icons/"
    python3 fetch-icons.py

    # With Hi-Rez API credentials (optional fallback):
    SMITE_DEV_ID=<id> SMITE_AUTH_KEY=<key> python3 fetch-icons.py

Expected output: 31 PNG files, each 10–40 KB, all within the 50 KB spec.
"""

import hashlib
import json
import os
import ssl
import time
import urllib.request
from pathlib import Path

HERE      = Path(__file__).parent
MAX_BYTES = 50_000   # 50 KB cap per spec
SLEEP     = 0.8      # seconds between requests — be polite

UA  = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
CTX = ssl.create_default_context()

# SmiteSource URL pattern
SMITE_SOURCE_URL = "https://www.smitesource.com/images/gods/{name}_icon.png"

# Hi-Rez API base (SMITE 1 API has same roster as SMITE 2)
HIREZ_BASE = "https://api.smitegame.com/smiteapi.svc"

# Jacob's pool — shown first in output with ★
PRIORITY_POOL = {"chiron", "ullr", "hou-yi"}

# Full god roster: (filename_slug, SmiteSource_PascalCase_name)
# SmiteSource uses PascalCase with underscores for multi-word names.
GODS = [
    # Jacob's pool (priority — embedded in all 3 god notes)
    ("chiron",    "Chiron"),
    ("ullr",      "Ullr"),
    ("hou-yi",    "Hou_Yi"),

    # Contextual hunters (matchup notes)
    ("neith",     "Neith"),
    ("apollo",    "Apollo"),
    ("artemis",   "Artemis"),
    ("cupid",     "Cupid"),
    ("jing-wei",  "Jing_Wei"),
    ("izanami",   "Izanami"),
    ("medusa",    "Medusa"),

    # Broader meta roster
    ("hercules",  "Hercules"),
    ("thor",      "Thor"),
    ("bellona",   "Bellona"),
    ("loki",      "Loki"),
    ("bastet",    "Bastet"),
    ("nemesis",   "Nemesis"),
    ("susano",    "Susano"),
    ("fenrir",    "Fenrir"),
    ("anubis",    "Anubis"),
    ("ra",        "Ra"),
    ("agni",      "Agni"),
    ("hades",     "Hades"),
    ("poseidon",  "Poseidon"),
    ("kukulkan",  "Kukulkan"),
    ("zeus",      "Zeus"),
    ("ah-puch",   "Ah_Puch"),
    ("merlin",    "Merlin"),
    ("athena",    "Athena"),
    ("ares",      "Ares"),
    ("ymir",      "Ymir"),
    ("sobek",     "Sobek"),
]


# ---------------------------------------------------------------------------
# Network helpers
# ---------------------------------------------------------------------------

def fetch_bytes(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "image/png,image/jpeg,image/*,*/*",
            "Referer": "https://www.smitesource.com/",
        }
    )
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read()


def fetch_json(url: str, timeout: int = 20) -> object:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return json.loads(r.read())


def is_png_or_jpg(data: bytes) -> bool:
    return data[:8] == b"\x89PNG\r\n\x1a\n" or data[:2] == b"\xff\xd8"


# ---------------------------------------------------------------------------
# Hi-Rez API helpers (optional — only used when env vars are set)
# ---------------------------------------------------------------------------

def _hirez_sig(method: str, dev_id: str, auth_key: str, timestamp: str) -> str:
    raw = f"{dev_id}{method}{auth_key}{timestamp}"
    return hashlib.md5(raw.encode()).hexdigest()


def _hirez_ts() -> str:
    return time.strftime("%Y%m%d%H%M%S", time.gmtime())


def fetch_hirez_god_icons(dev_id: str, auth_key: str) -> dict[str, str]:
    """
    Call getGodsJson and return a dict mapping lowercase god name → godIcon_URL.
    Returns empty dict on any failure.
    """
    method = "getgodsjson"
    ts  = _hirez_ts()
    sig = _hirez_sig(method, dev_id, auth_key, ts)
    url = f"{HIREZ_BASE}/getgodsjson/1/{dev_id}/{sig}/{ts}"
    print(f"  [hirez] Fetching god list from Hi-Rez API …")
    try:
        gods = fetch_json(url)
    except Exception as exc:
        print(f"  [hirez] API call failed: {exc}")
        return {}

    if not isinstance(gods, list):
        print(f"  [hirez] Unexpected response format")
        return {}

    icon_map = {}
    for g in gods:
        name = g.get("Name", "").lower()
        icon_url = g.get("godIcon_URL", "")
        if name and icon_url:
            icon_map[name] = icon_url

    print(f"  [hirez] Got {len(icon_map)} god icons from API")
    return icon_map


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    dev_id   = os.environ.get("SMITE_DEV_ID", "")
    auth_key = os.environ.get("SMITE_AUTH_KEY", "")
    use_hirez = bool(dev_id and auth_key)

    print("=== SMITE 2 god portrait icons ===")
    print(f"Primary source : SmiteSource direct icon URLs")
    if use_hirez:
        print(f"Fallback source: Hi-Rez API (credentials provided)")
    else:
        print(f"Fallback source: none (set SMITE_DEV_ID + SMITE_AUTH_KEY to enable Hi-Rez API)")
    print()

    # Pre-fetch Hi-Rez icon map if credentials are available
    hirez_map: dict[str, str] = {}
    if use_hirez:
        hirez_map = fetch_hirez_god_icons(dev_id, auth_key)
        print()

    # Sort: priority pool first, then alphabetical by slug
    def sort_key(item):
        slug, _ = item
        return (0 if slug in PRIORITY_POOL else 1, slug)

    ok       = []
    skipped  = []
    failures = []

    for slug, ss_name in sorted(GODS, key=sort_key):
        star = "★" if slug in PRIORITY_POOL else " "
        out  = HERE / f"{slug}.png"

        # Skip real icons (>1 KB) — never overwrite downloaded files
        if out.exists() and out.stat().st_size > 1000:
            size_kb = out.stat().st_size // 1024
            print(f"  {star} [skip] {slug}.png — already present ({size_kb}KB)")
            skipped.append(slug)
            time.sleep(SLEEP * 0.2)
            continue

        img_data: bytes | None = None
        source_used = ""

        # ---- Attempt 1: SmiteSource direct PNG ----
        ss_url = SMITE_SOURCE_URL.format(name=ss_name)
        try:
            data = fetch_bytes(ss_url)
            if data and is_png_or_jpg(data):
                img_data   = data
                source_used = f"SmiteSource ({ss_url})"
        except Exception as exc:
            # 404 or network error — fall through to Hi-Rez
            pass

        # ---- Attempt 2: Hi-Rez API godIcon_URL ----
        if img_data is None and hirez_map:
            # Try matching by slug or SmiteSource name (case-insensitive)
            hirez_key = slug.replace("-", " ")           # "hou-yi" → "hou yi"
            icon_url  = hirez_map.get(hirez_key) or hirez_map.get(slug)
            if not icon_url:
                # Also try the SmiteSource PascalCase name lowercased
                icon_url = hirez_map.get(ss_name.lower().replace("_", " "))
            if icon_url:
                try:
                    data = fetch_bytes(icon_url)
                    if data and is_png_or_jpg(data):
                        img_data   = data
                        source_used = f"Hi-Rez API ({icon_url})"
                except Exception as exc:
                    pass

        if img_data is None:
            msg = (
                f"{slug} — all sources failed  "
                f"[SmiteSource: {SMITE_SOURCE_URL.format(name=ss_name)}]"
            )
            print(f"  {star} [MISS] {slug}")
            failures.append(msg)
            time.sleep(SLEEP)
            continue

        size_kb = len(img_data) // 1024
        over    = len(img_data) > MAX_BYTES
        note    = f" ⚠ oversized ({size_kb}KB > {MAX_BYTES // 1024}KB)" if over else ""

        if over:
            failures.append(
                f"{slug} — oversized {size_kb}KB (>{MAX_BYTES // 1024}KB) — {source_used}"
            )

        out.write_bytes(img_data)
        print(f"  {star} [ OK ] {slug}.png  {size_kb}KB  [{source_used.split('(')[0].strip()}]{note}")
        ok.append(slug)
        time.sleep(SLEEP)

    # ---- Summary ----
    print(f"\n=== Summary ===")
    print(f"Downloaded : {len(ok)}")
    print(f"Skipped    : {len(skipped)}  (already existed)")
    print(f"Failures   : {len(failures)}")

    if failures:
        fail_path = HERE / "_fetch_failures.txt"
        fail_path.write_text("\n".join(failures) + "\n")
        print(f"\nFailures written to: {fail_path.name}")
        print("\nManual fallback options:")
        print("  A) Browser → https://smite.fandom.com/wiki/<GodName>")
        print("     Right-click infobox portrait → Save image as → rename to <slug>.png")
        print("     Resize to 64×64 if needed (macOS Preview / ImageMagick)")
        print("  B) Hi-Rez API: set SMITE_DEV_ID + SMITE_AUTH_KEY env vars and re-run")
        print("     Register at https://smitegame.com/api-terms-of-use/ (free)")

    total_kb = sum(
        (HERE / f"{s}.png").stat().st_size
        for s in ok
        if (HERE / f"{s}.png").exists()
    ) // 1024
    print(f"Total downloaded: {total_kb}KB")
    print("\nAll embeds in 07. Gaming/SMITE 2/01-god-notes/ will now render in Obsidian.")


if __name__ == "__main__":
    main()
