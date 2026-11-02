"""Record Steam's real GetNewsForApp responses for app 2437170 as fixtures.

Read-only. Writes pipeline/smite/tests/fixtures/recorded/steam/*.json and
prints every post's date, feed, tags and title so the log alone is enough to
see what titles the patch feed has to match.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

URL = "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/"
OUT = Path(__file__).resolve().parents[1] / "smite" / "tests" / "fixtures" / "recorded" / "steam"
UA = "ichor-gg/1.0 (+https://github.com/jacob-colby/ichor-gg)"

VARIANTS = {
    # Exactly what smite.patch_feed.fetch_news sends.
    "announcements": {"appid": 2437170, "count": 50, "maxlength": 0,
                      "feeds": "steam_community_announcements", "format": "json"},
    # No feed filter, short bodies: shows which feeds exist at all.
    "all_feeds": {"appid": 2437170, "count": 100, "maxlength": 300, "format": "json"},
}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, params in VARIANTS.items():
        r = requests.get(URL, params=params, timeout=30, headers={"User-Agent": UA})
        print(f"== {name}: HTTP {r.status_code}, {len(r.content)} bytes, {r.headers.get('content-type')}")
        if r.status_code != 200:
            print(r.text[:500])
            continue
        payload = r.json()
        (OUT / f"{name}.json").write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n",
                                          encoding="utf-8")
        for it in payload.get("appnews", {}).get("newsitems", []):
            day = datetime.fromtimestamp(int(it["date"]), tz=timezone.utc).date()
            print(f"{day} | {it.get('feedname')} | {it.get('tags')} | {it.get('title')!r} | {it.get('url')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
