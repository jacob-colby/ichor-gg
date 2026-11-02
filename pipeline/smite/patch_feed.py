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

WHERE THE LABEL ACTUALLY IS — RECORDED, NOT ASSUMED. The first version read the
label from the TITLE only ("OB46 - King Kappa Update"), from a fixture built to
the API's documentation. Its first live run (2026-11-02) found nothing newer
than Open Beta 26. A real response, recorded from a GitHub runner the same day
(`.github/workflows/probe-steam-feed.yml`, saved as
`tests/fixtures/recorded/steam/`), shows why: since January 2026 Hi-Rez titles
patch posts by their headline god or event ("Unleash HEL!", "TO VICTORY with
NIKE!"), and the label moved into the BODY, in one of three forms:

    title        "Horus Ascends! Take Flight in Update 36"         1 post
    notes link   smite2.com/news/open-beta-NN-update-notes/        OB22-OB33
    body text    "[h1]OB 37- Goddess Of Cats Update[/h1]",
                 "tested in live ... during OB44"                  OB26, 37, 44

So a post is read title first, then the official notes link, then the body;
`label_source` on each row says which. Checked against the recorded history:
every label it reads is dated on or after that patch's recorded `first_seen`
and before the next one's (`test_patch_feed.py`).

STEAM IS NOW THE WEAK SOURCE, and this is a measurement too. The recorded
response's newest post is 2026-10-06 and carries no label; the newest
LABELLED post is Open Beta 44 (2026-09-22), while the game and the wiki are on
Open Beta 46. Hi-Rez stopped announcing every patch on Steam, and of the
recent ones it did announce, most name no patch anywhere. The wiki's
Patch_notes index (`stats_refresh`) is the primary due signal; this feed is
the cross-check, and `cross_check` logs every day the two disagree.

WHAT A POST MUST LOOK LIKE TO COUNT. Announcement feed only; none of
`PREVIEW_WORDS` in the title; a label from one of the three forms above. A
body mention is dropped when the text just before it reads as a preview
("coming", "next", "upcoming", "PTS"): Hi-Rez previews a patch before it ships,
and recording one would flip the label early. The highest label left in a body
is the post's — a launch post looks BACK at the last patch ("In OB36, the
attenuation radius was...") but never past its own. A hotfix post for a label
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
# "Take Flight in Update 36" — titles only; in a body "update 2" is too loose.
_TITLE_UPDATE_RE = re.compile(r"\bUpdate\s+(\d{2,3})\b", re.IGNORECASE)
_NOTES_LINK_RE = re.compile(r"smite2\.com/news/open-beta-(\d{1,3})-update-notes", re.IGNORECASE)
# Left context that turns a body mention into a preview of a patch not out yet.
_PREVIEW_CONTEXT = re.compile(r"\b(coming|next|upcoming|preview|pts|public\s+test|later\s+in|"
                              r"arriv\w*\s+in|planned\s+for|until)\b[^.\]]*$", re.IGNORECASE)
STATE_FILE = "_patch_feed.json"
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


def post_label(item: dict):
    """(n, how) for one announcement, or None. `how` is 'title', 'notes-link'
    or 'body', tried in that order."""
    title = item.get("title") or ""
    if PREVIEW_WORDS.search(title):
        return None
    for rx in (_LABEL_RE, _TITLE_UPDATE_RE):
        m = rx.search(title)
        if m:
            return int(m.group(1)), "title"
    body = item.get("contents") or ""
    links = [int(m.group(1)) for m in _NOTES_LINK_RE.finditer(body)]
    if links:
        return max(links), "notes-link"
    mentions = [int(m.group(1)) for m in _LABEL_RE.finditer(body)
                if not _PREVIEW_CONTEXT.search(body[max(0, m.start() - 80):m.start()])]
    if mentions:
        return max(mentions), "body"
    return None


def patch_posts(payload: dict) -> list:
    """[{patch, first_seen, official_url?}] one per label, earliest post wins.
    Raises on a payload that is not GetNewsForApp's shape — the caller logs."""
    items = payload["appnews"]["newsitems"]
    found = {}
    for item in items:
        if item.get("feedname") != ANNOUNCEMENTS_FEED:
            continue
        label = post_label(item)
        if label is None:
            continue
        n, how = label
        day = datetime.fromtimestamp(int(item["date"]), tz=timezone.utc).date().isoformat()
        row = {"patch": f"Open Beta {n}", "first_seen": day, "source": "steam", "label_source": how}
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

    newest = posts[-1]
    print(f"[patch feed] newest labelled post: {newest['patch']} ({newest['first_seen']}, "
          f"read from the {newest['label_source']})")
    if not dry_run:
        _write_state(data_root, newest)

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


def _write_state(data_root: Path, newest: dict) -> None:
    """What Steam last said, for `cross_check`. No run date in it, so the file
    only changes when Steam does and a quiet day commits nothing."""
    body = {k: newest[k] for k in ("patch", "first_seen", "label_source")}
    path = Path(data_root) / STATE_FILE
    try:
        if json.loads(path.read_text(encoding="utf-8")) == body:
            return
    except (OSError, ValueError):
        pass
    path.write_text(json.dumps(body, indent=2) + "\n", encoding="utf-8")


def load_state(data_root: Path = DATA_ROOT) -> dict:
    try:
        return json.loads((Path(data_root) / STATE_FILE).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def cross_check(steam: dict, wiki_patch) -> str:
    """One log line comparing Steam's newest labelled post with the wiki's
    Patch_notes index. Steam BEHIND the wiki is the normal state since Hi-Rez
    stopped labelling (a ::notice::); Steam AHEAD means the wiki is lagging and
    a stats refresh will wait for it (a ::warning::). Neither changes data."""
    s = snapshots.patch_number((steam or {}).get("patch"))
    w = snapshots.patch_number(wiki_patch)
    if s is None or w is None:
        return (f"::notice::[patch sources] cannot compare: Steam says {(steam or {}).get('patch')}, "
                f"the wiki says {wiki_patch}")
    if s == w:
        return f"[patch sources] agree: Steam and the wiki both say Open Beta {w}"
    if s < w:
        return (f"::notice::[patch sources] disagree: Steam's newest labelled post is Open Beta {s} "
                f"({steam.get('first_seen')}, from the {steam.get('label_source')}), the wiki says "
                f"Open Beta {w} — Steam is behind; the wiki drives the refresh")
    return (f"::warning::[patch sources] disagree: Steam says Open Beta {s} "
            f"({steam.get('first_seen')}), the wiki still says Open Beta {w} — the wiki is behind; "
            "a stats refresh waits for it")


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
