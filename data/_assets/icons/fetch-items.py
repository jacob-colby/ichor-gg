#!/usr/bin/env python3
"""
fetch-items.py — SMITE 2 item icons

Same working pattern as fetch-gods.py: SmiteSource direct icon URLs, which
are not Cloudflare-gated (unlike wiki.smite2.com itself).
    https://www.smitesource.com/images/items/<Name>_icon.png
    e.g. https://www.smitesource.com/images/items/Deathbringer_icon.png

Reads the item name list from every Items/*.md note's `name` frontmatter
field (via smite.notes) rather than a hardcoded list, so it scales as items
get added by the refresh pipeline.

Skips files that already exist and are >1000 bytes. Enforces a 50KB cap and
logs failures to _fetch_failures.txt, same as fetch-gods.py.
"""
import ssl
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "tools"))
from smite import notes  # noqa: E402

HERE = Path(__file__).parent
# file is at 04. System/Data/SMITE/_assets/icons/fetch-items.py; Items/ is a
# sibling of _assets/ under SMITE/, i.e. two levels up from this file.
ITEMS_DIR = Path(__file__).resolve().parents[2] / "Items"
MAX_BYTES = 50_000
SLEEP = 0.8
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
CTX = ssl.create_default_context()
SMITE_SOURCE_URL = "https://www.smitesource.com/images/items/{name}_icon.png"


def fetch_bytes(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept": "image/png,image/jpeg,image/*,*/*",
        "Referer": "https://www.smitesource.com/",
    })
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read()


def is_png_or_jpg(data: bytes) -> bool:
    return data[:8] == b"\x89PNG\r\n\x1a\n" or data[:2] == b"\xff\xd8"


def item_names() -> list:
    names = []
    for path in sorted(ITEMS_DIR.glob("*.md")):
        frontmatter, _ = notes.read_note(path)
        if frontmatter.get("name"):
            names.append(frontmatter["name"])
    return names


def main():
    names = item_names()
    if not names:
        print(f"No item notes found in {ITEMS_DIR} — run refresh.py first.")
        return

    ok, skipped, failures = [], [], []
    for name in names:
        slug = name.lower().replace(" ", "-").replace("'", "")
        out = HERE / f"{slug}.png"
        if out.exists() and out.stat().st_size > 1000:
            print(f"  [skip] {slug}.png — already present")
            skipped.append(slug)
            continue

        ss_name = name.replace(" ", "_").replace("'", "")
        url = SMITE_SOURCE_URL.format(name=ss_name)
        try:
            data = fetch_bytes(url)
        except Exception as exc:
            failures.append(f"{slug} — {exc} — {url}")
            print(f"  [MISS] {slug} — {exc}")
            time.sleep(SLEEP)
            continue

        if not data or not is_png_or_jpg(data):
            failures.append(f"{slug} — not a valid image — {url}")
            print(f"  [MISS] {slug} — not a valid image")
            time.sleep(SLEEP)
            continue

        if len(data) > MAX_BYTES:
            failures.append(f"{slug} — oversized {len(data)//1024}KB (>{MAX_BYTES // 1024}KB) — {url}")

        out.write_bytes(data)
        print(f"  [ OK ] {slug}.png ({len(data)//1024}KB)" + (" ⚠ oversized" if len(data) > MAX_BYTES else ""))
        ok.append(slug)
        time.sleep(SLEEP)

    print(f"\nDownloaded: {len(ok)}, Skipped: {len(skipped)}, Failed: {len(failures)}")
    if failures:
        (HERE / "_fetch_failures.txt").write_text("\n".join(failures) + "\n")
        print(f"Failures written to {HERE / '_fetch_failures.txt'}")


if __name__ == "__main__":
    main()
