"""What aspect PLAYERS buy: a per-aspect community record, from SmiteBrain's
per-match build feed. DATA, not model — nothing here reaches a score.

WHY THIS EXISTS (2026-11-08). Ichor ships an aspect build for seven gods, all
hand-typed stat overlays (`_weights.yaml` `aspects:`), and STATE.md §4.33
showed the wiki cannot do better: it carries aspect TEXT, almost never aspect
NUMBERS. This reads a different source — what the players who pick an aspect
actually buy, and which ROLE they take it into — which needs no numbers at all.
Tsukuyomi is the case that motivated it: his Aspect of Mangetsu is a magical
Mid build on a physical Jungler, and no stat overlay can say that.

THE SOURCE, every claim measured 2026-11-08 by hand before this was written:

  * `GET /api/trpc/builds.getBuilds?input={godSlug, role, division, aspect,
    lastEvaluatedBuildDate}` — the call behind the builds page's "More Builds"
    button (read out of the site's JS bundle). Plain tRPC, no transformer. A
    page is the 10 newest matches before the cursor, newest first; the cursor
    is the last record's `hz_match_start_timestamp` and is EXCLUSIVE (319
    distinct Tsukuyomi matches walked with no duplicate at a page edge). The
    `__data.json` page only ever shows the first 10 — `page=` and `offset=` are
    ignored — which is why this was first thought to be a 10-match feed.
  * `player_placement` is the TEAM OUTCOME and 1 is the WIN. Three ways:
      - mirror: six Tsukuyomi matches looked up in their enemies' feeds; 14 of
        14 records found carry the opposite placement and list Tsukuyomi as an
        enemy, and within a team all five agree (two matches mirrored 5 of 5);
      - the site paints `player_placement===1` green and anything else red;
      - against the aggregate's `matches_won` (OB47, Obsidian+), the feed's
        placement-1 share tracks win rate on both sides of 50%: Jing Wei
        .461 vs .446, Atlas .491 vs .456, Aladdin .618 vs .620, Mordred .644
        vs .626. Read as 1 = loss, those would run the wrong way.
  * The feed is a SUBSET of the aggregate: 81-96% of its matches (Tsukuyomi
    319 of 377 in OB47). A win share off the feed is close to the aggregate's
    and not equal to it, so the aspect-vs-no-aspect WIN RATES are taken from
    the aggregate (`splitByAspect=true`, one request for every god), and the
    feed is used for what only it has: items, starter, relic, role.
  * Retention is about 45 days: no record anywhere predates 2026-09-24
    17:09Z, 45.0 days before the probe and two days INTO OB44's window, so it
    is not a patch boundary. One reading; if it is rolling, anything not in
    this store is gone after 45 days, which is why the store is in git.
  * `division` is nested (`obsidian` ⊇ `master` ⊇ `deity`: master's 72
    Mangetsu matches are all among obsidian's 73). `role=` is a strict subset
    of `role=all` and multiplies nothing. `aspect=none` and `aspect=<slug>`
    both take effect; the god page's aggregate IGNORES `aspect=`.
  * tRPC OMITS a null key (`aspect` is absent on a no-aspect record) where
    `__data.json` sends `null`. Item names drift in case and spacing ("Spear
    Of The Magus", "Aegis of Acceleration "), so items are keyed on the slug
    in `detail_href`, never on the name. 27% of records hold an "Empty" slot.
    Slot numbers are inventory slots, NOT a confirmed buy order.

WHAT IS STORED, and what is not. `data/Analysis/aspect_matches/<window>/
<god-slug>.jsonl`, one match per line, oldest first, deduplicated per god on
`m`. Each line: `m` (first 16 hex of SHA-256 of the match GUID), `t`, `aspect`
(slug or null), `role`, `rank`, `placement`, `items` (one slug per inventory
slot, null for an empty one — six slots, except Vulcan's Aspect of
Fortification, which returns 7 or 8), `starter`, `relic`, `enemies` (god
slugs). NOT stored: the player's name, and the raw GUID — it is a link to a
public tracker.gg page that names all ten players, and the hash still dedupes
and still joins the same game across gods' files. `_meta.json` holds the
window registry (SmiteBrain's own start/end per patch window), each god's
aspect list, and `complete_from`: the instant from which EVERY aspect feed is
in the store whole. Nothing older was fetched, so a window starting before it
is not in the registry at all, rather than present and silently short.
`_aggregate.json` holds the split index's aspect / no-aspect rows per window.
Records are assigned to the newest window whose start is not after them.

THE BACKFILL (2026-11-08) went back to OB46's start for all 86 aspect feeds,
not to the end of retention. The full 45 days measured at ~4,770 requests,
about 3.9 h at the 2.5 s floor plus latency; the session's limit was 2.5 h, so
the cutoff is OB46 and `complete_from` says so. From mid-OB44 the source's
older matches age out a day at a time and cannot be fetched again.

WHAT ONE RUN FETCHES (`refresh`), about 217 requests at 2.5 s (~9 min) for
2026-11-08's volumes, on top of the ~100 the community refresh already sends:
  * the newest two windows' split index (start/end + aspect aggregates);
  * one `aspect=none` page per god: its `availableAspects`, and the 10 newest
    no-aspect matches as a SAMPLE — a contrast, not a census (it is the 10
    newest at the time of the run, so it leans to that time of day);
  * every aspect feed walked back to the newest match already stored, or, for
    a feed with nothing stored, to the start of the newest window. A missed
    day costs nothing: the next run walks further back.

ALL OR NOTHING (`FeedCollapse`). Every page is validated before anything is
written — the feed's shape, every record's hard fields, that the `godSlug` and
`aspect` filters took effect, that the cursor moved. One failure refuses the
whole run and the store is left exactly as it was, the contract
`refresh.ParseCollapse` gives the community records. The store is append-only
(a refresh never deletes a match), so a refused run loses a day at most, and
the next run's walk recovers it.

THE BUILD-NOTE ENTRY (`community_aspects:` in each Conquest note), per aspect:
  * WINDOW RULE: the newest patch window, unless it holds fewer than
    `MIN_MATCHES` of this aspect's matches, in which case the last CLOSED one;
    if that is thin too the entry says so and claims nothing. The entry names
    the window it describes and which branch of the rule chose it.
  * `MIN_MATCHES` IS `tierlist.MIN_MATCHES` (30), imported, not restated — the
    repo's existing floor below which "the interval is so wide the god is
    better described as unmeasured". The entry's claims are binomial shares
    with the same interval, so the same floor applies. It was NOT chosen
    against Tsukuyomi, and it leaves him without an entry (below).
  * ROLE SHIFT: said when the god's base role (his god note's `role`) is not
    what most of the aspect's players play — the 95% Wilson UPPER bound of the
    base role's share is under 0.5 — and the most-played role is another. A
    bound, not a point share, because a thin aspect's role split is noisy.
  * Matches, not players: a thin aspect can be a few one-tricks. Measured
    once, from the raw feed before names were dropped: Mangetsu's 73
    Obsidian+ matches (09-24 to 11-08) are 28 players, ONE of whom played 22
    (30%), and the top three 49%; his 41 Mid matches are 16 players, one of
    them 15. The store cannot count players without keeping an identifier,
    which it does not, so the entry's `matches` is all it can claim, and a
    reader of a thin aspect's item shares should assume a few people.

TSUKUYOMI, the acceptance case (2026-11-08, Obsidian+): Mangetsu holds 5
matches in OB47 and 21 in OB46, both under 30, so his entry is a stated
`below minimum` with the per-window counts (OB44 17, OB45 30, OB46 21, OB47
5). Pooled over the 45 retained days it is 73 matches, 56% Mid and 27% Jungle,
buying Rod of Tahuti 81%, Book of Thoth 74%, Chronos' Pendant 58%. At about
1.1 matches a day he cannot reach 30 inside one 14-day patch, so whether to
pool closed windows is the next session's decision, and the store keeps them
apart so it can be made.

    python -m smite.aspect_matches refresh    # the daily job's step
    python -m smite.aspect_matches derive     # rewrite the notes from the store
    python -m smite.aspect_matches depth      # gods x windows, aspect matches
"""
import argparse
import hashlib
import json
import math
import re
import sys
import time
import urllib.parse
from collections import Counter
from datetime import datetime
from pathlib import Path

from smite import notes, smitebrain_parser, tierlist

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = REPO_ROOT / "data"
BUILDS_ROOT = DATA_ROOT / "builds"
GODS_ROOT = DATA_ROOT / "Gods"
ITEMS_ROOT = DATA_ROOT / "Items"
STORE_ROOT = DATA_ROOT / "Analysis" / "aspect_matches"
META_FILE = "_meta.json"
AGGREGATE_FILE = "_aggregate.json"

FEED_URL = "https://smitebrain.com/api/trpc/builds.getBuilds"
INDEX_URL = "https://smitebrain.com/gods/__data.json"
GOD_PAGE_URL = "https://smitebrain.com/gods/{slug}/"
#: Obsidian+, the same band as `refresh.GOD_INDEX_DIVISION`, so the aspect
#: record and the god's community record describe the same players. The
#: narrower bands are recoverable from `rank` (Master+ is rank >= 4400).
DIVISION = "obsidian"
PAGE_SIZE = 10
#: No-aspect pages per god per run — the contrast sample, deliberately capped.
NONE_PAGES = 1
#: The newest two windows get their split index refreshed each run: the
#: current one is still growing, and the one before is what the fallback reads.
WINDOWS_REFRESHED = 2
#: A walk this long means the cursor stopped moving or the stop never came. The
#: largest aspect on record (Izanami's Sickle, ~105 matches/day) is ~470 pages
#: across the whole 45-day retention.
MAX_PAGES_PER_FEED = 800
MIN_INTERVAL = 2.5

MIN_MATCHES = tierlist.MIN_MATCHES
WILSON_Z = tierlist.WILSON_Z
ITEMS_SHOWN = 8
STARTERS_SHOWN = 3
RELICS_SHOWN = 3
MATCH_KEY_LEN = 16

ROLES = ("Solo", "Jungle", "Mid", "Carry", "Support", "Unknown")
RECORD_KEYS = ("m", "t", "aspect", "role", "rank", "placement", "items",
               "starter", "relic", "enemies")
_GUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)
_TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$")
MIN_SLOTS = 6


class FeedCollapse(Exception):
    """The feed came back in a shape this module does not trust. Nothing is
    written; the store keeps yesterday's data."""


# -- source --------------------------------------------------------------------

def god_slug(name: str) -> str:
    """SmiteBrain's god slug — the same rule as `refresh.community_url`, which
    reaches all 95 gods every day (a test holds the two together)."""
    return name.lower().replace(" ", "-").replace("'", "")


def feed_url(slug: str, aspect=None, cursor=None, division=DIVISION) -> str:
    inp = {"godSlug": slug, "role": "all", "division": division}
    if aspect:
        inp["aspect"] = aspect
    if cursor:
        inp["lastEvaluatedBuildDate"] = cursor
    return f"{FEED_URL}?input=" + urllib.parse.quote(json.dumps(inp, separators=(",", ":")))


def index_url(window=None) -> str:
    url = f"{INDEX_URL}?division={DIVISION}&splitByAspect=true"
    return f"{url}&time={window}" if window else url


class PoliteFetcher:
    """Uncached GET at `MIN_INTERVAL`. Uncached on purpose: every cursor page
    is a new URL, so a disk cache would only accumulate files, and a cached
    FIRST page would hide a day's matches until the TTL ran out."""

    def __init__(self, min_interval: float = MIN_INTERVAL):
        import requests
        from smite.cache import USER_AGENT
        self._session = requests.Session()
        self._session.headers["User-Agent"] = USER_AGENT
        self.min_interval = min_interval
        self._last = 0.0
        self.requests = 0

    def __call__(self, url: str) -> str:
        wait = self.min_interval - (time.time() - self._last)
        if wait > 0:
            time.sleep(wait)
        try:
            response = self._session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        finally:
            self._last = time.time()
            self.requests += 1


def match_key(guid: str) -> str:
    return hashlib.sha256(guid.strip().lower().encode("utf-8")).hexdigest()[:MATCH_KEY_LEN]


def _norm_ts(ts) -> str:
    """One spelling per instant, so string order is time order."""
    m = _TS_RE.match(ts) if isinstance(ts, str) else None
    if not m:
        raise FeedCollapse(f"timestamp {ts!r} is not ISO-8601 UTC")
    try:
        whole = datetime.strptime(ts[:19], "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        raise FeedCollapse(f"timestamp {ts!r} is not a real instant")
    millis = int(((m.group(1) or ".0")[1:] + "000")[:3])
    return whole.strftime("%Y-%m-%dT%H:%M:%S.") + f"{millis:03d}Z"


def _item_slug(entry, where: str):
    """The slug off `detail_href`, or None for an empty slot / no item.

    A few items carry no link at all — Brawler's Ruin, on 108 of the first
    1,893 backfilled records (2026-11-08). Those are slugged from the name by
    the rule every link follows (`chronos-pendant` for "Chronos' Pendant"),
    rather than refused: an unlinked item is a real purchase, not a malformed
    scrape. A link that is present and not an item link IS refused."""
    if entry is None:
        return None
    if not isinstance(entry, dict) or not isinstance(entry.get("item_name"), str):
        raise FeedCollapse(f"{where}: item is {entry!r}")
    name = entry["item_name"].strip()
    if name == "Empty":
        return None
    href = entry.get("detail_href")
    if not href:
        if not name:
            raise FeedCollapse(f"{where}: item with neither a name nor a link")
        return god_slug(_fold(name))
    if not href.startswith("/items/") or len(href) <= len("/items/"):
        raise FeedCollapse(f"{where}: {name!r} links to {href!r}, not an item")
    return href[len("/items/"):].strip("/")


def _fold(text) -> str:
    return notes._fold_item_name(text)


def _slot_keys(items):
    """`["1", ..., "k"]` for an inventory of k >= 6 numbered slots, else None.

    Six on every record but one aspect's: Vulcan's Aspect of Fortification
    comes back with 7 or 8 (2026-11-08 backfill), so a fixed six would refuse
    a real inventory. All k are stored; nothing downstream assumes six."""
    if not isinstance(items, dict) or not items:
        return None
    if not all(isinstance(k, str) and k.isdigit() for k in items):
        return None
    keys = sorted(items, key=int)
    if keys != [str(i) for i in range(1, len(keys) + 1)] or len(keys) < MIN_SLOTS:
        return None
    return keys


def parse_record(raw: dict, god_name: str, aspect=None) -> dict:
    """One feed record -> one stored record. `aspect` is the `{name, value}`
    the feed was filtered on, or None for the no-aspect feed. Raises
    FeedCollapse on anything a stored record could not be trusted with."""
    if not isinstance(raw, dict):
        raise FeedCollapse(f"record is {type(raw).__name__}, not an object")
    guid = raw.get("hz_match_guid")
    if not isinstance(guid, str) or not _GUID_RE.match(guid):
        raise FeedCollapse(f"record has no match GUID ({guid!r})")
    where = f"{god_name} {guid[:8]}"
    if _fold(raw.get("character_choice")) != _fold(god_name):
        raise FeedCollapse(f"{where}: record is for {raw.get('character_choice')!r} — "
                           "the godSlug filter did not take effect")
    got = (raw.get("aspect") or {}).get("item_name")
    if aspect is None and got:
        raise FeedCollapse(f"{where}: no-aspect feed returned {got!r} — aspect=none was ignored")
    if aspect is not None and _fold(got) != _fold(aspect["name"]):
        raise FeedCollapse(f"{where}: {aspect['value']} feed returned {got!r} — the aspect "
                           "filter was ignored")
    items = raw.get("items")
    slots = _slot_keys(items)
    if slots is None:
        raise FeedCollapse(f"{where}: items are not slots 1..k, k >= 6 "
                           f"({sorted(items) if isinstance(items, dict) else items!r})")
    placement = raw.get("player_placement")
    if placement not in (1, 2, None):
        raise FeedCollapse(f"{where}: placement {placement!r}")
    role = raw.get("played_role")
    if role not in ROLES:
        raise FeedCollapse(f"{where}: role {role!r}")
    rank = raw.get("player_finishing_rank")
    if rank is not None and not isinstance(rank, (int, float)):
        raise FeedCollapse(f"{where}: rank {rank!r}")
    enemies = []
    for e in raw.get("enemy_gods") or []:
        if e and isinstance(e, dict) and e.get("slug"):
            enemies.append(e["slug"])
    return {
        "m": match_key(guid),
        "t": _norm_ts(raw.get("hz_match_start_timestamp")),
        "aspect": aspect["value"] if aspect else None,
        "role": role,
        "rank": int(rank) if rank is not None else None,
        "placement": placement,
        "items": [_item_slug(items[s], f"{where} slot {s}") for s in slots],
        "starter": _item_slug(raw.get("starter"), f"{where} starter"),
        "relic": _item_slug(raw.get("relic"), f"{where} relic"),
        "enemies": enemies,
    }


def parse_page(text: str, god_name: str, aspect=None, cursor=None):
    """`(records, available_aspects, raw_oldest_timestamp)` for one page."""
    try:
        data = json.loads(text)["result"]["data"]
        builds = data["builds"]
    except (ValueError, KeyError, TypeError) as exc:
        raise FeedCollapse(f"{god_name}: response is not a getBuilds result ({exc!r})")
    if not isinstance(builds, list) or len(builds) > PAGE_SIZE:
        raise FeedCollapse(f"{god_name}: builds is not a page of at most {PAGE_SIZE}")
    available = data.get("availableAspects")
    if not isinstance(available, list) or not all(
            isinstance(a, dict) and a.get("name") and a.get("value") for a in available):
        raise FeedCollapse(f"{god_name}: availableAspects is {available!r}")
    records = [parse_record(b, god_name, aspect) for b in builds]
    times = [r["t"] for r in records]
    if times != sorted(times, reverse=True):
        raise FeedCollapse(f"{god_name}: page is not newest-first")
    if cursor and times and times[0] >= _norm_ts(cursor):
        raise FeedCollapse(f"{god_name}: the cursor did not move ({cursor} -> {times[0]})")
    oldest_raw = builds[-1].get("hz_match_start_timestamp") if builds else None
    return records, [{"name": a["name"].strip(), "value": a["value"]} for a in available], oldest_raw


def walk_feed(fetch, slug, god_name, aspect, floor):
    """Every record of one aspect feed newer than `floor` (plus the page that
    crosses it — the merge dedupes). Stops at a short page: the end of the
    source's retention."""
    out, cursor = [], None
    for _ in range(MAX_PAGES_PER_FEED):
        records, _, oldest_raw = parse_page(fetch(feed_url(slug, aspect["value"], cursor)),
                                            god_name, aspect, cursor)
        out.extend(records)
        if len(records) < PAGE_SIZE or (floor and records[-1]["t"] <= floor):
            return out
        cursor = oldest_raw
    raise FeedCollapse(f"{god_name} {aspect['value']}: {MAX_PAGES_PER_FEED} pages without "
                       "reaching the stored data or the end of the feed")


# -- windows and the aggregate -------------------------------------------------

def parse_split_index(text: str) -> dict:
    """`{window, start, end, rows}` off a `splitByAspect=true` god index."""
    payload = json.loads(text)
    rows = smitebrain_parser.parse_god_index(payload)
    if not rows:
        raise FeedCollapse("split index has no rows")
    first = rows[0]
    start, end = first.get("start_time"), first.get("end_time")
    if not start:
        raise FeedCollapse("split index carries no window start")
    window = None
    for node in payload.get("nodes") or []:
        flat = (node or {}).get("data")
        if isinstance(flat, list) and flat and isinstance(flat[0], dict) \
                and "selectedTime" in flat[0]:
            window = smitebrain_parser._devalue(flat, flat[0]["selectedTime"])
    return {"window": window, "start": _norm_ts(start), "end": _norm_ts(end) if end else None,
            "rows": [{"god": r["god"], "aspect": None if r.get("aspect") in (None, "None") else r["aspect"],
                      "matches_played": r.get("matches_played"), "matches_won": r.get("matches_won")}
                     for r in rows]}


def ordered_windows(meta: dict) -> list:
    """Window ids, newest first, by SmiteBrain's own start time."""
    wins = meta.get("windows") or {}
    return sorted(wins, key=lambda w: wins[w]["start"], reverse=True)


def window_of(ts: str, meta: dict):
    wins = meta.get("windows") or {}
    for w in ordered_windows(meta):
        if wins[w]["start"] <= ts:
            return w
    return None


# -- store ---------------------------------------------------------------------

def _read_json(path: Path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def load_meta(root: Path = STORE_ROOT) -> dict:
    return _read_json(root / META_FILE, {"division": DIVISION, "windows": {}, "aspects": {}})


def load_aggregate(root: Path = STORE_ROOT) -> dict:
    return _read_json(root / AGGREGATE_FILE, {})


def load_god(root: Path, slug: str) -> dict:
    """`{window: [records]}` for one god."""
    out = {}
    for path in sorted(root.glob(f"*/{slug}.jsonl")):
        out[path.parent.name] = [json.loads(line) for line in
                                 path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return out


def merge(existing: list, new: list) -> list:
    """Union on `m`, the stored copy winning; oldest first."""
    by_key = {r["m"]: r for r in new}
    by_key.update({r["m"]: r for r in existing})
    return sorted(by_key.values(), key=lambda r: (r["t"], r["m"]))


def _record_line(r: dict) -> str:
    return json.dumps({k: r[k] for k in RECORD_KEYS}, separators=(",", ":"), ensure_ascii=False)


def _write_text(path: Path, text: str) -> bool:
    """LF on every platform, so a store written on Windows is byte-identical
    to one the Linux runner writes."""
    data = text.encode("utf-8")
    if path.exists() and path.read_bytes() == data:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    tmp.replace(path)
    return True


def store_records(root: Path, slug: str, records: list, meta: dict) -> dict:
    """Merge `records` into one god's files. Returns `{window: added}`."""
    by_window = {}
    for r in records:
        w = window_of(r["t"], meta)
        if w is None:
            raise FeedCollapse(f"{slug}: match at {r['t']} predates every known window")
        by_window.setdefault(w, []).append(r)
    stored = load_god(root, slug)
    added = {}
    for w, recs in by_window.items():
        before = stored.get(w, [])
        merged = merge(before, recs)
        added[w] = len(merged) - len(before)
        _write_text(root / w / f"{slug}.jsonl", "".join(_record_line(r) + "\n" for r in merged))
    return added


def save_json(path: Path, obj) -> bool:
    return _write_text(path, json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False) + "\n")


# -- the daily refresh ---------------------------------------------------------

def conquest_gods(builds_root: Path = BUILDS_ROOT) -> list:
    out = []
    for path in sorted(builds_root.glob("*-Conquest.md")):
        fm, _ = notes.read_note(path)
        if fm.get("god"):
            out.append(fm["god"])
    return out


def refresh(fetch, gods: list, root: Path = STORE_ROOT, window_ids=None, log=print) -> dict:
    """Fetch, validate, and only then write. See the module docstring."""
    meta, aggregate = load_meta(root), load_aggregate(root)
    if window_ids is None:
        window_ids = smitebrain_parser.patch_windows(
            fetch(GOD_PAGE_URL.format(slug=god_slug(gods[0]))))[:WINDOWS_REFRESHED]
    if not window_ids:
        raise FeedCollapse("the range selector offered no patch windows")
    for w in window_ids:
        split = parse_split_index(fetch(index_url(w)))
        if split["window"] not in (None, w):
            raise FeedCollapse(f"asked for window {w}, the index answered {split['window']}")
        meta["windows"][w] = {"start": split["start"], "end": split["end"]}
        aggregate[w] = {"start": split["start"], "end": split["end"], "rows": split["rows"]}
    newest_start = meta["windows"][ordered_windows(meta)[0]]["start"]

    pending, empty_none_pages, summary = {}, 0, {}
    for god in gods:
        slug = god_slug(god)
        records, available, _ = parse_page(fetch(feed_url(slug, "none")), god)
        if not records:
            empty_none_pages += 1
        meta["aspects"][slug] = available
        if not available:
            continue
        stored = [r for recs in load_god(root, slug).values() for r in recs]
        got = list(records[: NONE_PAGES * PAGE_SIZE])
        for aspect in available:
            mine = [r["t"] for r in stored if r["aspect"] == aspect["value"]]
            floor = max(mine) if mine else newest_start
            fresh = walk_feed(fetch, slug, god, aspect, floor)
            got.extend(fresh)
            summary[f"{slug}/{aspect['value']}"] = len(fresh)
        pending[slug] = got
    if gods and empty_none_pages > len(gods) / 2:
        raise FeedCollapse(f"{empty_none_pages} of {len(gods)} gods returned no matches at all")

    added = {}
    for slug, records in pending.items():
        for w, n in store_records(root, slug, records, meta).items():
            added[w] = added.get(w, 0) + n
    save_json(root / META_FILE, meta)
    save_json(root / AGGREGATE_FILE, aggregate)
    log(f"  aspect matches: {sum(added.values())} new across {len(pending)} gods "
        f"({', '.join(f'{w} +{n}' for w, n in sorted(added.items()))})")
    return {"added": added, "feeds": summary}


# -- the build-note entry ------------------------------------------------------

def _wilson(k: int, n: int, z: float = WILSON_Z):
    if n <= 0:
        return None, None
    p = k / n
    denom = 1 + z * z / n
    centre = p + z * z / (2 * n)
    margin = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centre - margin) / denom, (centre + margin) / denom


def item_name_lookup(items_root: Path = ITEMS_ROOT) -> dict:
    """slug -> our item-note spelling. Folded the way `notes.canonical_item_name`
    folds, then slugged the way SmiteBrain slugs."""
    out = {}
    for path in sorted(items_root.glob("*.md")):
        name = (notes.read_note(path)[0] or {}).get("name") or path.stem
        out[god_slug(_fold(name))] = name
    return out


def _share_list(counter: Counter, n: int, names: dict, limit: int) -> list:
    ranked = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:limit]
    return [{"name": names.get(slug, slug), "share": round(c / n, 2)} for slug, c in ranked]


def choose_window(counts: dict, windows: list):
    """`(window, rule)`. Newest, else the last closed, else none."""
    if windows and counts.get(windows[0], 0) >= MIN_MATCHES:
        return windows[0], "newest"
    if len(windows) > 1 and counts.get(windows[1], 0) >= MIN_MATCHES:
        return windows[1], "last closed"
    return None, "below minimum"


def _aggregate_row(aggregate: dict, window: str, god: str, aspect_name):
    for r in (aggregate.get(window) or {}).get("rows") or []:
        if _fold(r["god"]) == _fold(god) and _fold(r["aspect"] or "") == _fold(aspect_name or ""):
            return r
    return None


def aspect_entry(god: str, base_role: str, aspect: dict, by_window: dict,
                 meta: dict, aggregate: dict, names: dict) -> dict:
    windows = ordered_windows(meta)
    recs_by_w = {w: [r for r in by_window.get(w, []) if r["aspect"] == aspect["value"]]
                 for w in windows}
    counts = {w: len(v) for w, v in recs_by_w.items() if v}
    window, rule = choose_window(counts, windows)
    entry = {"aspect": aspect["name"], "status": "shown" if window else "below minimum"}
    if window is None:
        entry["matches_by_window"] = counts
        return entry
    recs = recs_by_w[window]
    n = len(recs)
    decided = [r for r in recs if r["placement"] in (1, 2)]
    wins = sum(r["placement"] == 1 for r in decided)
    roles = Counter(r["role"] for r in recs)
    # A note's role can name two ("Solo Jungle"); `scoring.fit_map` reads
    # each token as a role, so the base is the SET and its share is summed.
    base_roles = str(base_role or "").split()
    in_base = sum(roles.get(r, 0) for r in base_roles)
    base_share = in_base / n
    _, base_hi = _wilson(in_base, n)
    top_role, top_n = sorted(roles.items(), key=lambda kv: (-kv[1], kv[0]))[0]
    shift = None
    if base_roles and top_role not in base_roles and base_hi < 0.5:
        named = "/".join(base_roles)
        shift = {"role": top_role, "share": round(top_n / n, 2),
                 "says": f"most {aspect['name']} players do not play {named}: "
                         f"{top_role} {top_n / n:.0%}, {named} {base_share:.0%}"}
    items = Counter(s for r in recs for s in set(r["items"]) if s)
    starters = Counter(r["starter"] for r in recs if r["starter"])
    relics = Counter(r["relic"] for r in recs if r["relic"])
    agg = _aggregate_row(aggregate, window, god, aspect["name"])
    agg_none = _aggregate_row(aggregate, window, god, None)
    win = meta["windows"][window]
    entry.update({
        "window": window,
        "window_rule": rule,
        "window_start": win["start"][:10],
        "window_end": (win.get("end") or "")[:10] or None,
        "matches": n,
        "wins": wins,
        "win_share": round(wins / len(decided), 2) if decided else None,
        "aggregate": {
            "aspect_matches": agg and agg["matches_played"],
            "aspect_win_rate": (round(agg["matches_won"] / agg["matches_played"], 3)
                                if agg and agg["matches_played"] else None),
            "no_aspect_matches": agg_none and agg_none["matches_played"],
            "no_aspect_win_rate": (round(agg_none["matches_won"] / agg_none["matches_played"], 3)
                                   if agg_none and agg_none["matches_played"] else None),
        },
        "roles": [{"role": r, "matches": c, "share": round(c / n, 2)}
                  for r, c in sorted(roles.items(), key=lambda kv: (-kv[1], kv[0]))],
        "base_role": base_role,
        "base_role_share": round(base_share, 2),
        "role_shift": shift,
        "items": _share_list(items, n, names, ITEMS_SHOWN),
        "starters": _share_list(starters, n, names, STARTERS_SHOWN),
        "relics": _share_list(relics, n, names, RELICS_SHOWN),
        "matches_by_window": counts,
    })
    unmapped = sorted({s for c in (items, starters, relics) for s in c if s not in names})
    if unmapped:
        entry["unmapped_slugs"] = unmapped
    return entry


def note_block(god: str, base_role: str, root: Path, meta: dict, aggregate: dict, names: dict):
    """The `community_aspects` value for one god's Conquest note, or None."""
    aspects = meta.get("aspects", {}).get(god_slug(god)) or []
    if not aspects:
        return None
    by_window = load_god(root, god_slug(god))
    return {
        "source": f"SmiteBrain per-match feed, {meta.get('division', DIVISION)}+ "
                  f"(data/Analysis/aspect_matches)",
        "minimum_matches": MIN_MATCHES,
        "window_rule": "the newest patch window, or the last closed one when the newest "
                       "holds fewer than minimum_matches of the aspect's matches",
        "aspects": [aspect_entry(god, base_role, a, by_window, meta, aggregate, names)
                    for a in aspects],
    }


def base_role_of(god: str, gods_root: Path = GODS_ROOT):
    fm, _ = notes.read_note(gods_root / f"{god}.md")
    return fm.get("role")


def write_notes(root: Path = STORE_ROOT, builds_root: Path = BUILDS_ROOT,
                gods_root: Path = GODS_ROOT, items_root: Path = ITEMS_ROOT) -> int:
    """Rewrite `community_aspects` in every Conquest note. Returns notes changed."""
    meta, aggregate, names = load_meta(root), load_aggregate(root), item_name_lookup(items_root)
    changed = 0
    for path in sorted(builds_root.glob("*-Conquest.md")):
        fm, body = notes.read_note(path)
        god = fm.get("god")
        if not god:
            continue
        block = note_block(god, base_role_of(god, gods_root), root, meta, aggregate, names)
        if fm.get("community_aspects") == block:
            continue
        if block is None:
            fm.pop("community_aspects", None)
        else:
            fm["community_aspects"] = block
        notes.write_note(path, fm, body)
        changed += 1
    return changed


# -- depth report --------------------------------------------------------------

def depth_rows(root: Path = STORE_ROOT) -> list:
    meta = load_meta(root)
    windows = ordered_windows(meta)
    rows = []
    for slug, aspects in sorted(meta.get("aspects", {}).items()):
        stored = load_god(root, slug)
        for a in aspects:
            counts = {w: sum(r["aspect"] == a["value"] for r in stored.get(w, [])) for w in windows}
            window, rule = choose_window(counts, windows)
            rows.append({"god": slug, "aspect": a["name"], "counts": counts,
                         "window": window, "rule": rule})
    return rows


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="python -m smite.aspect_matches")
    ap.add_argument("command", choices=("refresh", "derive", "depth"))
    args = ap.parse_args(argv)
    if args.command == "refresh":
        fetch = PoliteFetcher()
        try:
            refresh(fetch, conquest_gods())
        except FeedCollapse as exc:
            print(f"::error::aspect feed refused, store unchanged: {exc}")
            return 1
        finally:
            print(f"  aspect feed: {fetch.requests} requests")
        print(f"  aspect entries: {write_notes()} Conquest notes changed")
        return 0
    if args.command == "derive":
        print(f"aspect entries: {write_notes()} Conquest notes changed")
        return 0
    rows = depth_rows()
    windows = ordered_windows(load_meta())
    print(f"{'god':16} {'aspect':34} " + " ".join(f"{w:>5}" for w in windows) + "  entry")
    for r in sorted(rows, key=lambda r: -sum(r["counts"].values())):
        print(f"{r['god']:16} {r['aspect'][:34]:34} "
              + " ".join(f"{r['counts'].get(w, 0):5}" for w in windows)
              + f"  {r['window'] or '-'} ({r['rule']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
