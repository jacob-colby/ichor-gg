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
  * Retention is a ROLLING 45 days. Two readings, six hours apart: no record
    predated 2026-09-24 17:09Z at the first probe, and none predated
    2026-09-24 23:09Z at 23:24Z after the backfill (a busy feed walked to a
    short page). Each is 45.0 days before its reading, and both sit two days
    INTO OB44's window, so the floor is not a patch boundary. Anything not in
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
in the store whole. A window that starts before it is either absent from the
registry or carries `partial_from` equal to it — the source's retention cut
its start — and the note entry names it, so no window is silently short.
`_aggregate.json` holds the split index's aspect / no-aspect rows per window.
Records are assigned to the newest window whose start is not after them, and
none later than the newest window's end is stored (next section).

A PATCH BOUNDARY (`known_extent`, `misfiled`; 2026-11-09). The feed is the
newest matches whatever patch they were played on; the window a record is
FILED in comes from the range selector's windows (`window_of`), and the store
is append-only. So a match played after a new patch opens, fetched on a run
whose selector does not list that patch yet, would be filed in the old window,
and from the day the selector lists the new one `window_of` names it —
`test_aspect_store`'s committed-store test red on every run after, with
nothing to move the record, and "Pipeline suite" blocking every daily data PR
(#139 reported it; `test_aspect_matches` replays it: 14 matches stranded in
ob47 by day N+1 on the old rule). The selector does lag a patch, measured on
the community record, which read the newest LISTED window before 11-05, fresh
on each scheduled run (`data/_cache` is not kept between runs): the 11-03 run
(started 16:59Z, 61754eb0) still read ob46, at least 5.5 hours after ob47's
first match (11:30:13Z), and the 09-22 run (started 14:01Z, 900bf284) still
read the 09-08 window, at least 2h27m after ob44's first (11:33:41Z).

  * HOLD BACK, don't refuse. A run files nothing later than the newest
    window's `end` — SmiteBrain's newest match in it: on 11-09 ob47's end,
    18:17:55.767Z, was exactly the newest stored record — and holds the rest
    for the next run. Nothing is lost: a held match is newer than every stored
    one, and each walk runs down to the newest stored match, so the next run
    fetches it again (inside retention; the walk's 800-page cap is ~76 days of
    the busiest feed). That now holds for the no-aspect feed too, which is
    walked the same way since the census. A newest window with no
    `end` vouches for nothing after its start. Refusing the run instead would
    lose the whole day to one match the index had not counted yet, and every
    day of a lag; the store would gain nothing by it.
  * WHY `end` IS A SAFE EXTENT. All 38,433 stored records (11-09) sit inside
    `[start, end]` of their own window; the three boundaries on record leave
    gaps (ob44 -> ob45 1h31m, ob45 -> ob46 51m, ob46 -> ob47 2m11s), never an
    overlap; and during the 11-03 lag ob46's end read 11-02, BEHIND the
    boundary, not past it. One lag observed at day precision is not proof
    that SmiteBrain never extends an old window into the new patch, so:
  * THE GUARD FOR THE DAY IT IS NOT. If a refreshed window's start ever lands
    under a match already stored, `refresh` refuses the run (`misfiled`,
    FeedCollapse, before any feed is walked, nothing written). The store
    keeps agreeing with its committed meta, so CI stays green, and the refusal
    takes the workflow's `rejected` path: the day's other data lands, the run
    is red. It refuses every run until someone moves those records, which an
    append-only store has no step for — a human's call, not this module's.
    0.4 s over the 11-09 store.

THE BACKFILL (2026-11-08) walked all 86 aspect feeds to the end of retention,
in two passes: OB46 and OB47 first (1,636 requests), then OB45 and the
retained part of OB44 (2,130 more; 3,766 in all, no retries). Every feed
ended on a short page. The retention floor was measured AFTER the last feed
was walked, and the floor only moves forward, so every feed walked earlier
saw at least that far back. `complete_from` is that floor, 2026-09-24
23:09:08Z; the 69 older records that the earliest feeds still reached were
dropped, so every feed is cut at the same instant. OB44 therefore carries
`partial_from`: its first 2.5 days are gone at the source and cannot be
fetched again. 36,947 matches: OB44 9,336 (71% of the aggregate's aspect
matches, the 2.5 missing days), OB45 11,912 (85%), OB46 10,711 (85%), OB47
4,178 plus the 810-match no-aspect sample (85%).

THE NO-ASPECT CENSUS (2026-11-11; `NONE_CENSUS`, `meta["census_from"]`).
Through 2026-11-10 the no-aspect feed was stored as a SAMPLE, the ten newest
matches per god per run, so 94% of the store was aspect players (38,204 of
40,616 matches) and a god with no aspect (14 of 95) had no file at all. The
builds this repo ships are base-kit builds, and the one question the store
can answer that nothing else here can (does a match holding more of a build
win more, `build_outcomes`) could only be asked of the wrong kit. So the
no-aspect feed is now walked whole, exactly as an aspect feed is.
  * `census_from[slug]` is the instant from which that god's no-aspect
    matches are ALL stored. It matters because a sampled store has gaps below
    its newest no-aspect match: until a god has it, the walk ignores what is
    stored and starts over at the newest window's start; after, it stops at
    the newest stored no-aspect match like any other feed.
  * THE BACKFILL was OB47 only: 2026-11-11, 3,031 requests, 27,168 matches
    added, no retry. OB47 then held 28,676 no-aspect matches against the
    aggregate's 33,514 (86%, the feed's usual share). Every god's
    `census_from` is OB47's start, 2026-11-03T11:30:13.083Z. OB44-OB46 keep
    their samples and are NOT a census: the page that crosses a window's
    start also files a few older matches (515 landed in OB46), and
    `census_from` is what says they are stragglers. The 45-day retention
    would still have reached back to late September on that day; it was not
    walked, because those matches are other patches' items.
  * WHAT IT COSTS, and it is a standing cost. About 3,300 no-aspect matches a
    day at OB47's rate: roughly 330 more requests and 15 minutes on the daily
    job, and about 1.1 MB a day in git (the store went 13 MB -> 23 MB on the
    backfill). A retention policy for the store is undecided and is Jacob's
    call; `NONE_CENSUS = False` restores the sample.
  * Nothing in the notes changes for it: `community_aspects` reads aspect
    records and the aggregate, never a no-aspect record.

WHAT ONE RUN FETCHES (`refresh`), about 550 requests at 2.5 s (~24 min) at
2026-11-11's volumes, on top of the ~100 the community refresh already sends
(217 and ~9 min before the census):
  * the newest two windows' split index (start/end + aspect aggregates);
  * every god's `aspect=none` feed: its `availableAspects` off the first
    page, and the no-aspect matches walked back to the newest one stored
    (THE NO-ASPECT CENSUS above);
  * every aspect feed walked back to the newest match already stored, or, for
    a feed with nothing stored, to the start of the newest window. A missed
    day costs nothing: the next run walks further back. So does a held-back
    match (A PATCH BOUNDARY above).

ALL OR NOTHING (`FeedCollapse`). Every page is validated before anything is
written — the feed's shape, every record's hard fields, that the `godSlug` and
`aspect` filters took effect, that the cursor moved. One failure refuses the
whole run and the store is left exactly as it was, the contract
`refresh.ParseCollapse` gives the community records. The store is append-only
(a refresh never deletes a match), so a refused run loses a day at most, and
the next run's walk recovers it.

THE BUILD-NOTE ENTRY (`community_aspects:` in each Conquest note), per aspect:
  * WINDOW RULE (`choose_windows`, reach-back agreed 2026-11-09): the newest
    patch window, unless it holds fewer than `MIN_MATCHES` of this aspect's
    matches; then the last CLOSED one; then the newest windows POOLED — the
    newest and the last closed together, then one more closed window at a
    time — until the pool holds `MIN_MATCHES`; if every stored window together
    is still short the entry says so and claims nothing. The entry names the
    windows it reads (`windows`, oldest first, and `patches`, "OB45–OB47"),
    and which branch chose them. The first two branches are #129's rule
    unchanged, so the 65 entries it showed read the same windows, matches and
    shares now (checked entry by entry on 2026-11-09); only the 21 it left
    below the minimum can move.
  * WHY POOL, AND WHY THIS WAY — measured 2026-11-09 on the store as #129 left
    it (36,947 matches, 86 aspects, 21 below the minimum):

        rule                                   shown  of the 21
        #129 (newest, else last closed)          65        0
        walk back, pooled, flag changed items    78       13   <- shipped
        walk back, STOP at a changed item        69-70    4-5
        the newest single window holding 30      74        9
        every stored window pooled               78       13, but rewrites all 65

    The 13: Amaterasu 36, Atlas 64, Cupid 45, Mordred 74, Nu Wa 75 and
    Tsukuyomi 57 (OB45–OB47); Apollo 43, Cerberus 34, Chronos 35, Ix Chel 34
    and Jormungandr 34 (OB46–OB47); Da Ji 38 and Horus 36 (OB44–OB47). Still
    below: Geb (28 with everything pooled), Rama 23, Hercules 17 and The
    Morrigan's five copied aspects. Pooling from the newest rather than
    reading the deepest single window keeps the entry as recent as the floor
    allows: Jormungandr reads 34 matches from OB46–OB47, not OB45's 104.
  * ITEM CHANGES ARE FLAGGED, NEVER A STOP (`item_changes`, `_change_flag`).
    A pooled match may have bought an item since changed, so every listed
    item, starter and relic whose cost, tier or stats moved at a patch AFTER
    the oldest window read carries `changed`: the patch, and how many of the
    pooled matches that bought it are older. It applies to every shown entry,
    not only pooled ones: #129's last-closed reads already showed Cabrakan's
    and Osiris' OB46 builds holding Ancient Signet, which OB47 changed (9 of 9
    and 11 of 11 buys older), unflagged. A STOP rule was measured and
    refused: visibility then hinges on the quality of the change data (see
    the next point; Tsukuyomi is shown or hidden on one unplaceable +5
    Intelligence), and one peripheral item hides real evidence (Chronos' 35
    matches over the 7 that bought War Flag).
  * THE CHANGE SOURCE IS THE SNAPSHOT STORE, and it has two measured blind
    spots. (1) Item data was scraped under OB40 (2026-08-01, 08-29), OB46
    (11-02) and OB47 (11-03) and never in between, so OB46 -> OB47 is exact
    (Ancient Signet, Selflessness, War Flag) and everything else is ONE
    OB40 -> OB46 diff of 35 items with no patch attached. Such an item is
    flagged with the whole span ("OB41–OB46", `exact: false`, "up to N
    older"). (2) A snapshot holds cost, tier and stats, not passives, so a
    passive change is never flagged. The wiki's OB41–OB47 patch-notes pages
    were read once to size both (2026-11-09, 7 requests, not committed and
    not read by this code): they name OB45 Heartwood Charm, Lotus Sickle,
    Dominance, Gluttonous Grimoire; OB46 Devourer's Gauntlet, Sanguine Lash,
    Eye of the Storm, Eros' Bow, Midgardian Mail, Alchemist Coat, Riptalon,
    Xibalban Effigy; OB47 Ancient Signet, Lifebinder, Soul Locket,
    Selflessness, War Flag. They date Obsidian Shard and Polynomicon to OB44,
    which no pool crosses, so the span over-flags those two; and they name
    five of the 35 stat diffs NOWHERE — Rod of Tahuti (Intelligence 80 -> 85),
    Berserker's Shield, Death Metal, Musashi's Dual Swords, Rage — so neither
    source can date every change. The passive-only changes the snapshots miss
    are the price of reading a source the daily job keeps — the largest is
    Devourer's Gauntlet, changed in OB46 and among the six most-bought items
    of 5 shown builds that read OB45 or older. A hand transcription of the
    notes would be exact today and stale from OB48. From OB47 on, each
    patch's snapshot is exact for stats. The daily job re-derives the entries
    after the snapshot step, so a patch day's flags are that day's.
  * NOT GUARDED: a GOD's or an aspect's own balance changes. Nothing in the
    repo records them per patch. By the same wiki pages, 5 of the 78 entries
    read a window older than a patch that changed the god: Hou Yi and Nut
    (last closed OB46, changed in OB47, both #129 reads), and Cupid, Horus
    and Jormungandr (pooled).
  * THE RULE DEPENDS ON WHAT THE STORE RETAINS. The walk has no depth limit
    of its own: it reaches as far back as the store holds, so a retention
    policy (undecided, Jacob's call) is also its reach-back limit. Dropping
    OB44 today hides Da Ji and Horus; dropping OB45 too hides 8 of the 13,
    Tsukuyomi among them. Kept forever, a thin aspect pools as many patches
    as it needs (Geb would need about five).
  * `MIN_MATCHES` IS `tierlist.MIN_MATCHES` (30), imported, not restated — the
    repo's existing floor below which "the interval is so wide the god is
    better described as unmeasured". The entry's claims are binomial shares
    with the same interval, so the same floor applies. It was NOT chosen
    against Tsukuyomi, and it is not lowered for him: pooling is what reaches
    him, and nothing measured here says 30 is wrong.
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

TSUKUYOMI, the acceptance case (Obsidian+). 2026-11-08: Mangetsu held 6
matches in OB47 and 21 in OB46, so #129's rule, which falls back one window
only, left him `below minimum` (OB44 17, OB45 30, OB46 21, OB47 6). At about
1.6 matches a day he cannot count on 30 inside one 14-day patch. 2026-11-09,
under the reach-back rule: the two-window read is 27, so the walk adds OB45
and stops at 57 matches, "OB45–OB47". 56% Mid, 26% Jungle, 11% Carry — a role
shift off Jungle (the Wilson upper bound of the Jungle share is 0.39). He
buys Rod of Tahuti 86%, Book of Thoth 79%, Chronos' Pendant 72%, Obsidian
Shard 63%, Polynomicon 33%, Spear of Desolation 23%; starter Bluestone Brooch
42%; relic Purification Beads 60%. Four listed items carry the OB41–OB46 span
(Rod of Tahuti, Obsidian Shard, Polynomicon, Spear of the Magus — blind spot
(1) above); nothing OB47 changed is in his build. Pinned on a frozen copy of
his store in `tests/fixtures/aspect_store_tsukuyomi`. This is the community's
build, not Ichor's: his model build still cannot change role (STATE.md §5).

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
#: No-aspect pages per god per run when the census is off — the contrast
#: sample #129 stored, deliberately capped.
NONE_PAGES = 1
#: Walk every god's no-aspect feed whole, like an aspect feed (THE NO-ASPECT
#: CENSUS in the module docstring). `meta["census_from"][slug]` is the instant
#: from which that god's no-aspect matches are all in the store.
NONE_CENSUS = True
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
#: Every starter seen, not a top 3: a starter is a PATH (base, then its one
#: upgrade), each match holds one end, and a path's share is the two ends
#: summed — a path whose ends sit 3rd and 4th is invisible in a top 3. The
#: viewer's main starter tile learned this first (`lib/starters.ts`).
STARTERS_SHOWN = None
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


def walk_feed(fetch, slug, god_name, aspect, floor, first=None):
    """Every record of one feed newer than `floor` (plus the page that crosses
    it — the merge dedupes). `aspect` is the `{name, value}` the feed is
    filtered on, or None for the no-aspect feed. Stops at a short page: the
    end of the source's retention. `first` is page one as `(records,
    raw_oldest_timestamp)` when the caller has already fetched it."""
    value = aspect["value"] if aspect else "none"
    out, cursor = [], None
    for page in range(MAX_PAGES_PER_FEED):
        if page == 0 and first is not None:
            records, oldest_raw = first
        else:
            records, _, oldest_raw = parse_page(fetch(feed_url(slug, value, cursor)),
                                                god_name, aspect, cursor)
        out.extend(records)
        if len(records) < PAGE_SIZE or (floor and records[-1]["t"] <= floor):
            return out
        cursor = oldest_raw
    raise FeedCollapse(f"{god_name} {value}: {MAX_PAGES_PER_FEED} pages without "
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


def known_extent(meta: dict):
    """The latest instant a run may file a match at: the newest window's `end`
    (SmiteBrain's newest match in it), or its start when the index gave no
    end; None with no windows. Anything later is held back (module docstring,
    A PATCH BOUNDARY)."""
    windows = ordered_windows(meta)
    if not windows:
        return None
    span = meta["windows"][windows[0]]
    return span.get("end") or span["start"]


def misfiled(root: Path, meta: dict) -> list:
    """`(window dir, god slug, t, window_of)` for every stored match that
    `meta` would file in another window — what `test_aspect_store`'s
    committed-store test would fail on."""
    out = []
    for path in sorted(root.glob("*/*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                t = json.loads(line)["t"]
                w = window_of(t, meta)
                if w != path.parent.name:
                    out.append((path.parent.name, path.stem, t, w))
    return out


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


def refresh(fetch, gods: list, root: Path = STORE_ROOT, window_ids=None, log=print,
            census=None) -> dict:
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
        meta["windows"][w] = {**meta["windows"].get(w, {}),
                              "start": split["start"], "end": split["end"]}
        aggregate[w] = {"start": split["start"], "end": split["end"], "rows": split["rows"]}
    wrong = misfiled(root, meta)
    if wrong:
        w, slug, t, now = wrong[0]
        raise FeedCollapse(f"these windows would refile {len(wrong)} stored matches (first: "
                           f"{slug} {t} sits in {w}, would be {now}) — SmiteBrain redrew a "
                           "boundary under data already stored; the store cannot move them")
    newest_start = meta["windows"][ordered_windows(meta)[0]]["start"]
    extent = known_extent(meta)

    census = NONE_CENSUS if census is None else census
    census_from = dict(meta.get("census_from") or {})
    pending, empty_none_pages, summary, held = {}, 0, {}, 0
    for god in gods:
        slug = god_slug(god)
        records, available, oldest_raw = parse_page(fetch(feed_url(slug, "none")), god)
        if not records:
            empty_none_pages += 1
        meta["aspects"][slug] = available
        if not available and not census:
            continue
        stored = [r for recs in load_god(root, slug).values() for r in recs]
        if census:
            # Whole from `census_from` on, so the newest stored no-aspect match
            # is a safe floor; before a god's first census run the store holds
            # only samples with gaps between them, and the walk starts over at
            # the newest window's start.
            mine = [r["t"] for r in stored if r["aspect"] is None]
            floor = max(mine) if slug in census_from and mine else newest_start
            got = walk_feed(fetch, slug, god, None, floor, first=(records, oldest_raw))
            census_from.setdefault(slug, newest_start)
            summary[f"{slug}/none"] = len(got)
        else:
            got = list(records[: NONE_PAGES * PAGE_SIZE])
        for aspect in available:
            mine = [r["t"] for r in stored if r["aspect"] == aspect["value"]]
            floor = max(mine) if mine else newest_start
            fresh = walk_feed(fetch, slug, god, aspect, floor)
            got.extend(fresh)
            summary[f"{slug}/{aspect['value']}"] = len(fresh)
        kept = [r for r in got if r["t"] <= extent]
        held += len(got) - len(kept)
        pending[slug] = kept
    if gods and empty_none_pages > len(gods) / 2:
        raise FeedCollapse(f"{empty_none_pages} of {len(gods)} gods returned no matches at all")

    added = {}
    for slug, records in pending.items():
        for w, n in store_records(root, slug, records, meta).items():
            added[w] = added.get(w, 0) + n
    if census:
        meta["census_from"] = census_from
    save_json(root / META_FILE, meta)
    save_json(root / AGGREGATE_FILE, aggregate)
    log(f"  aspect matches: {sum(added.values())} new across {len(pending)} gods "
        f"({', '.join(f'{w} +{n}' for w, n in sorted(added.items()))})"
        + (f"; {held} later than {ordered_windows(meta)[0]}'s end ({extent}) held for "
           "the next run" if held else ""))
    return {"added": added, "feeds": summary, "held": held}


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


def _share_list(counter: Counter, n: int, names: dict, limit: int, flag=None) -> list:
    """The `limit` most-bought, as shares of matches. `flag(slug)` adds a
    `changed` key to an item whose stats moved after the oldest pooled window."""
    ranked = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:limit]
    out = []
    for slug, c in ranked:
        row = {"name": names.get(slug, slug), "share": round(c / n, 2)}
        changed = flag(slug) if flag else None
        if changed:
            row["changed"] = changed
        out.append(row)
    return out


def choose_windows(counts: dict, windows: list):
    """`(pool, rule)`: the windows an entry reads, NEWEST FIRST, and which
    branch of the rule chose them. `windows` is the store's, newest first.

      newest       the newest window alone, when it holds MIN_MATCHES;
      last closed  else the last closed window alone, when it does;
      pooled back  else the newest windows together — the newest and the last
                   closed, then one more closed window at a time — until the
                   pool holds MIN_MATCHES;
      below minimum when every stored window together is still short.

    The first two branches are the rule as #129 shipped it, unchanged, so an
    entry that showed before reads the same windows now. The walk has no depth
    limit: it reaches as far back as the store holds, so a retention policy is
    also this rule's reach-back limit (module docstring)."""
    if windows and counts.get(windows[0], 0) >= MIN_MATCHES:
        return [windows[0]], "newest"
    if len(windows) > 1 and counts.get(windows[1], 0) >= MIN_MATCHES:
        return [windows[1]], "last closed"
    total = 0
    for i, w in enumerate(windows):
        total += counts.get(w, 0)
        if i and total >= MIN_MATCHES:
            return list(windows[: i + 1]), "pooled back"
    return [], "below minimum"


def window_patch(window: str):
    """47 from "ob47": SmiteBrain names its patch windows after the patch."""
    m = re.fullmatch(r"ob(\d+)", str(window or ""))
    return int(m.group(1)) if m else None


def patch_label(windows: list) -> str:
    """"OB47", or "OB45–OB47" for a pool. `windows` oldest first."""
    first, last = windows[0].upper(), windows[-1].upper()
    return first if first == last else f"{first}–{last}"


# -- which items changed since a window ----------------------------------------

def item_changes(snapshots_dir: Path = None, history_path: Path = None) -> list:
    """Every item whose cost, tier or stats moved between two consecutive
    item-stat snapshots: `[{slug, name, after, through}]`, where the change
    happened at a patch in `(after, through]` — or DURING `through` when the
    two are equal (a wiki correction or a hotfix inside one patch). Patches
    are attributed the way the patch-notes page attributes them, by when ITEM
    DATA was scraped under each label (`snapshots.data_history`), and `after`
    is None when the older snapshot predates every label.

    This is the only per-patch record of item changes the repo keeps, and it
    has two blind spots, both measured 2026-11-09 (module docstring): it holds
    no item data between OB40 and OB46, so a change in that span carries the
    whole span; and a snapshot holds cost, tier and stats only, so a PASSIVE
    change is never seen. Imported here: `snapshots` pulls in the scoring
    stack, and the daily refresh step needs none of it."""
    from smite import snapshots
    history = snapshots.data_history(snapshots.load_patch_history(
        history_path or snapshots.PATCH_HISTORY_PATH))
    paths = sorted(Path(snapshots_dir or snapshots.SNAPSHOTS_DIR).glob("*.json"),
                   key=lambda p: p.stem)
    out = []
    for old, new in zip(paths, paths[1:]):
        diff = snapshots.diff_snapshots(snapshots.load_snapshot(old), snapshots.load_snapshot(new))
        after = snapshots.patch_number(snapshots.patch_at(history, old.stem))
        through = snapshots.patch_number(snapshots.patch_at(history, new.stem))
        if through is None:
            continue
        for entry in diff["changed"]:
            out.append({"slug": god_slug(_fold(entry["name"])), "name": entry["name"],
                        "after": after, "through": through})
    return out


def _change_flag(slug: str, recs_by_w: dict, pool: list, changes: list, bought):
    """The flag for one listed item, or None: its LATEST change at a patch
    after the oldest pooled window, and how many of the pooled matches that
    bought it are older than that patch. `pool` newest first; `bought(record)`
    says whether a record bought the item."""
    oldest = window_patch(pool[-1])
    hits = [c for c in changes if c["slug"] == slug and c["through"] > oldest]
    if not hits:
        return None
    c = max(hits, key=lambda c: (c["through"], c["after"] or -1))
    exact = c["after"] is not None and c["after"] + 1 == c["through"]
    mine = [w for w in pool for r in recs_by_w[w] if bought(r)]
    # Matches in a window before `through` predate the change if it came at
    # `through`, the latest patch it can have come at; so for a range this is
    # an upper bound, and for a change during one patch a lower one.
    older = sum(window_patch(w) < c["through"] for w in mine)
    of = f"{older} of the {len(mine)} matches that bought it are older"
    through = f"OB{c['through']}"
    if exact:
        patch, says = through, f"changed in {through}; {of}"
    elif c["after"] == c["through"]:
        patch, says = through, f"its stats moved during {through}; at least {of}"
    elif c["after"] is None:
        patch = f"{through} or earlier"
        says = f"its stats moved at {through} or earlier, at a patch not recorded; up to {of}"
    else:
        patch = f"OB{c['after'] + 1}–{through}"
        says = (f"its stats moved between Ichor's OB{c['after']} and {through} item data, "
                f"at a patch not recorded; up to {of}")
    return {"patch": patch, "exact": exact, "older_matches": older,
            "matches": len(mine), "says": says}


def _aggregate_row(aggregate: dict, window: str, god: str, aspect_name):
    for r in (aggregate.get(window) or {}).get("rows") or []:
        if _fold(r["god"]) == _fold(god) and _fold(r["aspect"] or "") == _fold(aspect_name or ""):
            return r
    return None


def _pooled_aggregate(aggregate: dict, pool: list, god: str, aspect_name):
    """`(matches, win_rate)` summed over the pooled windows' split index rows,
    or `(None, None)` when any pooled window has no row: a sum over part of the
    pool would describe different windows from the record beside it."""
    rows = [_aggregate_row(aggregate, w, god, aspect_name) for w in pool]
    if not rows or any(r is None for r in rows):
        return None, None
    played = sum(r["matches_played"] or 0 for r in rows)
    won = sum(r["matches_won"] or 0 for r in rows)
    return played, (round(won / played, 3) if played else None)


def aspect_entry(god: str, base_role: str, aspect: dict, by_window: dict,
                 meta: dict, aggregate: dict, names: dict, changes=()) -> dict:
    windows = ordered_windows(meta)
    recs_by_w = {w: [r for r in by_window.get(w, []) if r["aspect"] == aspect["value"]]
                 for w in windows}
    counts = {w: len(v) for w, v in recs_by_w.items() if v}
    pool, rule = choose_windows(counts, windows)
    entry = {"aspect": aspect["name"], "status": "shown" if pool else "below minimum"}
    if not pool:
        entry["matches_by_window"] = counts
        return entry
    recs = [r for w in pool for r in recs_by_w[w]]
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

    def flag(field):
        test = ((lambda slug: lambda r: slug in r["items"]) if field == "items"
                else (lambda slug: lambda r: r[field] == slug))
        return lambda slug: _change_flag(slug, recs_by_w, pool, changes, test(slug))

    agg_n, agg_rate = _pooled_aggregate(aggregate, pool, god, aspect["name"])
    none_n, none_rate = _pooled_aggregate(aggregate, pool, god, None)
    oldest_first = pool[::-1]
    entry.update({
        "windows": oldest_first,
        "patches": patch_label(oldest_first),
        "window_rule": rule,
        "window_start": meta["windows"][pool[-1]]["start"][:10],
        "window_end": (meta["windows"][pool[0]].get("end") or "")[:10] or None,
        "matches": n,
        "wins": wins,
        "win_share": round(wins / len(decided), 2) if decided else None,
        "aggregate": {
            "aspect_matches": agg_n,
            "aspect_win_rate": agg_rate,
            "no_aspect_matches": none_n,
            "no_aspect_win_rate": none_rate,
        },
        "roles": [{"role": r, "matches": c, "share": round(c / n, 2)}
                  for r, c in sorted(roles.items(), key=lambda kv: (-kv[1], kv[0]))],
        "base_role": base_role,
        "base_role_share": round(base_share, 2),
        "role_shift": shift,
        "items": _share_list(items, n, names, ITEMS_SHOWN, flag("items")),
        "starters": _share_list(starters, n, names, STARTERS_SHOWN, flag("starter")),
        "relics": _share_list(relics, n, names, RELICS_SHOWN, flag("relic")),
        "matches_by_window": counts,
    })
    unmapped = sorted({s for c in (items, starters, relics) for s in c if s not in names})
    if unmapped:
        entry["unmapped_slugs"] = unmapped
    return entry


def note_block(god: str, base_role: str, root: Path, meta: dict, aggregate: dict, names: dict,
               changes=()):
    """The `community_aspects` value for one god's Conquest note, or None.
    `changes` is `item_changes()`: what flags a listed item."""
    aspects = meta.get("aspects", {}).get(god_slug(god)) or []
    if not aspects:
        return None
    by_window = load_god(root, god_slug(god))
    partial = {w: span["partial_from"][:10] for w, span in (meta.get("windows") or {}).items()
               if span.get("partial_from")}
    return {
        "source": f"SmiteBrain per-match feed, {meta.get('division', DIVISION)}+ "
                  f"(data/Analysis/aspect_matches)",
        **({"complete_from": meta["complete_from"][:10]} if meta.get("complete_from") else {}),
        **({"partial_windows": dict(sorted(partial.items()))} if partial else {}),
        "minimum_matches": MIN_MATCHES,
        "window_rule": "the newest patch window; else the last closed one; else the newest "
                       "windows pooled, reaching back one closed window at a time, until "
                       "they hold minimum_matches of the aspect's matches",
        "item_changes": "an item is flagged when its cost, tier or stats moved at a patch "
                        "after the oldest window read (data/Analysis/snapshots); a passive "
                        "change is not recorded there and is never flagged",
        "aspects": [aspect_entry(god, base_role, a, by_window, meta, aggregate, names, changes)
                    for a in aspects],
    }


def base_role_of(god: str, gods_root: Path = GODS_ROOT):
    fm, _ = notes.read_note(gods_root / f"{god}.md")
    return fm.get("role")


def write_notes(root: Path = STORE_ROOT, builds_root: Path = BUILDS_ROOT,
                gods_root: Path = GODS_ROOT, items_root: Path = ITEMS_ROOT) -> int:
    """Rewrite `community_aspects` in every Conquest note. Returns notes changed."""
    meta, aggregate, names = load_meta(root), load_aggregate(root), item_name_lookup(items_root)
    changes = item_changes()
    changed = 0
    for path in sorted(builds_root.glob("*-Conquest.md")):
        fm, body = notes.read_note(path)
        god = fm.get("god")
        if not god:
            continue
        block = note_block(god, base_role_of(god, gods_root), root, meta, aggregate, names,
                           changes)
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
            pool, rule = choose_windows(counts, windows)
            rows.append({"god": slug, "aspect": a["name"], "counts": counts,
                         "windows": pool[::-1], "rule": rule,
                         "matches": sum(counts.get(w, 0) for w in pool)})
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
              + (f"  {patch_label(r['windows'])} {r['matches']} ({r['rule']})" if r["windows"]
                 else f"  - ({r['rule']})"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
