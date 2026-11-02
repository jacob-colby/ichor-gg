"""Detect a new SMITE 2 patch from Steam's announcement feed, unattended.

    python -m smite.patch_feed            # record any new patch; always exits 0
    python -m smite.patch_feed --dry-run  # print what it would record

WHY STEAM. The daily job runs on a GitHub-hosted runner, and the label has to
come from somewhere that runner can reach without a browser. The wiki is
Cloudflare-gated (see `refresh-data.yml`). smite2.com is a rendered site with
no documented feed, and its URL scheme is something we would be guessing at.
SmiteBrain's god index carries no patch field. Steam's `GetNewsForApp` is a
public, keyless JSON API, and filtered to `steam_community_announcements` it
is the developer's own posts for app 2437170 — nobody else can write there.
Patch-notes posts carry the label in the title ("OB46 - King Kappa Update").

NOT VERIFIED LIVE. The sandbox this was written in could not reach
api.steampowered.com, smite2.com or the wiki. `tests/fixtures/steam_news.json`
is constructed to GetNewsForApp v2's documented shape, not recorded. The first
scheduled run after this lands is the first live test; if the title format
differs, the symptom is "[patch feed] no patch posts in N announcements" in
the job log and NO change to the data — never a wrong label.

WHAT A POST MUST LOOK LIKE TO COUNT. Announcement feed only; a label in the
title (`OB46`, `Open Beta 46`); none of `PREVIEW_WORDS` in the title. The last
rule matters: Hi-Rez posts previews and PTS notes for a patch before it ships,
and recording one would flip the label early. A hotfix post for a label
already recorded is a no-op by construction.

WHAT IT RECORDS. Only labels NEWER (by number) than the newest recorded, each
as `{patch, first_seen, source: "steam", official_url?}`, oldest first, so a
run that missed several patches backfills all of them. `first_seen` is the
post date (UTC), floored at the previous row's date so the history stays in
game order. It never sets `data_from`: Steam saying OB47 is out says nothing
about whether Ichor's item stats are OB47's (see `snapshots`).

The link is a smite2.com/hirezstudios.com notes URL quoted in the post body
when there is one for this label, else the post's own Steam URL. Never built
from a pattern. `data/_patch_links.yaml` overrides either.

FAILURE NEVER FAILS THE REFRESH. Any fetch or parse error is logged and
returns no change; `main` returns 0 on every path, including a bug. A run that
finds nothing new writes nothing, so a same-day re-run is a no-op and the
commit step sees no diff.
"""
import argparse
import json
import re
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

from smite import snapshots

DATA_ROOT = snapshots.DATA_ROOT
STEAM_NEWS_URL = "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/"
ANNOUNCEMENTS_FEED = "steam_community_announcements"
FETCH_COUNT = 50

_LABEL_RE = re.compile(r"\b(?:OB|Open\s*Beta)\s*-?\s*(\d{1,3})\b", re.IGNORECASE)
PREVIEW_WORDS = re.compile(r"\b(preview|pts|public\s+test|sneak|teaser|coming\s+soon|trailer|livestream)\b",
                           re.IGNORECASE)
_URL_RE = re.compile(r"https://[^\s\"'<>\[\]]+")


def fetch_news(session=None, timeout: float = 20.0) -> dict:
    """GetNewsForApp, announcements only, full bodies (maxlength=0)."""
    import requests
    get = (session or requests).get
    resp = get(STEAM_NEWS_URL, timeout=timeout, params={
        "appid": snapshots.STEAM_APP_ID, "count": FETCH_COUNT,
        "maxlength": 0, "feeds": ANNOUNCEMENTS_FEED, "format": "json"})
    resp.raise_for_status()
    return resp.json()


def _official_link(item: dict, n: int):
    body = item.get("contents") or ""
    for url in _URL_RE.findall(body):
        url = url.rstrip(".,);")
        host_ok = snapshots.is_official_url(url) and "steam" not in url
        if host_ok and re.search(rf"(?:open-beta-|ob-?){n}(?!\d)", url, re.IGNORECASE):
            return url
    url = item.get("url")
    return url if snapshots.is_official_url(url) else None


def patch_posts(payload: dict) -> list:
    """[{patch, first_seen, official_url?}] one per label, earliest post wins.
    Raises on a payload that is not GetNewsForApp's shape — the caller logs."""
    items = payload["appnews"]["newsitems"]
    found = {}
    for item in items:
        if item.get("feedname") != ANNOUNCEMENTS_FEED:
            continue
        title = item.get("title") or ""
        m = _LABEL_RE.search(title)
        if not m or PREVIEW_WORDS.search(title):
            continue
        n = int(m.group(1))
        day = datetime.fromtimestamp(int(item["date"]), tz=timezone.utc).date().isoformat()
        row = {"patch": f"Open Beta {n}", "first_seen": day, "source": "steam"}
        link = _official_link(item, n)
        if link:
            row["official_url"] = link
        prior = found.get(n)
        if prior is None or day < prior["first_seen"]:
            if prior and "official_url" in prior and "official_url" not in row:
                row["official_url"] = prior["official_url"]
            found[n] = row
        elif "official_url" not in prior and link:
            prior["official_url"] = link
    return [found[n] for n in sorted(found)]


def new_rows(history: list, posts: list) -> list:
    """The posts newer than everything recorded, with dates floored so the
    history stays in order."""
    known = [snapshots.patch_number(r["patch"]) for r in history]
    newest = max((n for n in known if n is not None), default=-1)
    floor = max((str(r["first_seen"]) for r in history), default="")
    out = []
    for row in posts:
        if snapshots.patch_number(row["patch"]) <= newest:
            continue
        row = dict(row, first_seen=max(row["first_seen"], floor))
        floor = row["first_seen"]
        out.append(row)
    return out


def update(data_root: Path = DATA_ROOT, fetch=fetch_news, dry_run: bool = False) -> list:
    """Fetch, detect, record. Returns the rows recorded ([] on no change or
    on any failure). Never raises."""
    data_root = Path(data_root)
    history_path = data_root / "_patch_history.json"
    try:
        payload = fetch()
    except Exception as exc:
        print(f"[patch feed] fetch failed, keeping the current label: {exc}")
        return []
    try:
        posts = patch_posts(payload)
    except Exception as exc:
        print(f"[patch feed] unreadable response, keeping the current label: {exc!r}")
        return []
    if not posts:
        n = len(((payload or {}).get("appnews") or {}).get("newsitems") or [])
        print(f"[patch feed] no patch posts in {n} announcements — nothing recorded")
        return []

    history = snapshots.load_patch_history(history_path)
    rows = new_rows(history, posts)
    if not rows:
        print(f"[patch feed] newest post is {posts[-1]['patch']}, already recorded — no change")
        return []
    for r in rows:
        print(f"[patch feed] new patch {r['patch']} from {r['first_seen']}"
              + (f" — {r['official_url']}" if r.get("official_url") else " — no official link"))
    if dry_run:
        return rows
    merged = history + rows
    snapshots._save_history(merged, history_path)
    snapshots.write_current_patch(merged, data_root / "_patch.json")
    return rows


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Record new SMITE 2 patches from Steam")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        update(dry_run=args.dry_run)
    except Exception:
        # A bug here must not fail the data refresh; the log is the alarm.
        print("[patch feed] unexpected error, nothing recorded:")
        traceback.print_exc(file=sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
