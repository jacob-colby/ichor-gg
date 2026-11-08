"""CLI: refresh SMITE god/item/build notes from wiki.smite2.com and
smitebrain.com. Run as: python -m smite.refresh --refresh Chiron --kind god
"""
import argparse
import re
import sys
import json
from datetime import date
from pathlib import Path

import requests
import yaml

from smite import notes, smitebrain_parser, wiki_parser
from smite.browser_fetch import BrowserFetcher
from smite.cache import CachedFetcher

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = REPO_ROOT / "data"
BUILDS_ROOT = REPO_ROOT / "data" / "builds"

WIKI_BASE = "https://wiki.smite2.com/w/"
SMITEBRAIN_BASE = "https://smitebrain.com/gods/"

# Matches link text like "SMITE 2 Open Beta 39" on the wiki's Patch_notes
# index. Deliberately loose on whitespace/case — the wiki is hand-authored,
# not generated.
_PATCH_VERSION_RE = re.compile(r"SMITE\s*2\s*Open\s*Beta\s*(\d+)", re.IGNORECASE)


def _download_icon(image_url: str, slug: str) -> None:
    """Download a god/item portrait/icon from wiki.smite2.com. The HTML
    pages are Cloudflare-gated (hence Playwright elsewhere in this module)
    but the static image files are not — confirmed with a plain requests
    fetch during planning — so this uses requests directly, no browser
    needed. Skips if already downloaded (>1000 bytes), same convention as
    the vault's other Gaming asset-download scripts."""
    if not image_url:
        return
    icons_dir = DATA_ROOT / "_assets" / "icons"
    out_path = icons_dir / f"{slug}.png"
    if out_path.exists() and out_path.stat().st_size > 1000:
        return

    # An override may supply an absolute URL from another CDN; the wiki's own
    # `image_url` is always a site-relative /images path.
    full_url = (image_url if image_url.startswith("http")
                else "https://wiki.smite2.com" + image_url)
    try:
        response = requests.get(full_url, timeout=20)
        response.raise_for_status()
    except Exception as exc:
        # A broken/expired icon URL is cosmetic, not a data failure — the
        # god/item note itself was already written by the caller before
        # this runs. Never let an icon miss look like a refresh failure.
        print(f"  [icon skip] {slug}: {exc}")
        return

    icons_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(response.content)


def scrape_patch_version(wiki_fetcher, force: bool = False):
    """The current SMITE 2 patch string from the wiki's Patch_notes index, or
    None. Reads only — `refresh_patch_version` is the half that persists it,
    and `wiki_watch` needs to compare without writing anything."""
    try:
        html = wiki_fetcher.fetch(WIKI_BASE + "Patch_notes", force=force)
    except Exception as exc:
        print(f"  [patch skip] {exc}")
        return None
    numbers = [int(m.group(1)) for m in _PATCH_VERSION_RE.finditer(html)]
    return f"Open Beta {max(numbers)}" if numbers else None


def refresh_patch_version(wiki_fetcher, force: bool = False):
    """Scrape the wiki's Patch_notes index for the current SMITE 2 patch
    (e.g. "Open Beta 39") and persist it to data/_patch.json, so the viewer
    can show which patch the shipped data reflects instead of just a vague
    "Updated yesterday".

    The page lists every patch link ("SMITE 2 Open Beta 39", "...Beta 38",
    ...), newest first in practice — but this parses every match and takes
    the highest N rather than trusting document order, since that ordering
    is just editorial convention on a wiki page, not a guarantee.

    Never raises: any fetch/parse failure (Cloudflare hiccup, wiki layout
    change, no matches at all) returns None and leaves an existing
    data/_patch.json untouched, exactly like a cosmetic icon-download miss
    elsewhere in this module — a failed patch-version scrape must not look
    like (or cause) a failed refresh."""
    import json

    try:
        version = scrape_patch_version(wiki_fetcher, force=force)
        if version is None:
            return None
        patch = {"patch": version, "captured": date.today().isoformat()}
    except Exception as exc:
        print(f"  [patch skip] {exc}")
        return None

    # The history is the record; _patch.json is derived from it, so the wiki
    # (which lags) can never walk back a newer label the Steam feed recorded
    # — it only marks the label the item data was scraped under.
    from smite import snapshots
    history_path = DATA_ROOT / "_patch_history.json"
    patch_path = DATA_ROOT / "_patch.json"
    try:
        snapshots.record_patch(patch["patch"], patch["captured"], history_path)
        history = snapshots.load_patch_history(history_path, fallback=False)
    except Exception as exc:
        print(f"  [patch history skip] {exc}")
        history = [{"patch": patch["patch"], "first_seen": patch["captured"]}]
    patch_path.parent.mkdir(parents=True, exist_ok=True)
    snapshots.write_current_patch(history, patch_path)
    return patch


def _head_icon_overrides():
    """`{slug: url}` from _icon_sources.yaml — head icons the wiki frames as
    portraits rather than faces. Read on every refresh so the override cannot
    be silently undone by a re-scrape; see that file for why it exists."""
    path = DATA_ROOT / "_icon_sources.yaml"
    if not path.exists():
        return {}
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return doc.get("head_icons") or {}


class ParseCollapse(Exception):
    """A scrape that would replace real data with less of it.

    `wiki_parser.parse_god_page` raises on exactly one thing — a missing
    infobox. Every other shape change degrades silently to empty: no `Roles`
    row and `role` is absent, no `Abilities` heading and `abilities` is `[]`.
    That is not a read-only failure, because `notes.merge_god_note` ends in
    `write_note(path, scraped_frontmatter, ...)` — the scrape REPLACES the
    frontmatter, and the note is the only copy. A silent miss does not fail to
    update, it overwrites.

    It has happened. Ullr, Artio and Merlin put their abilities inside a
    `div.img-tab-wrapper` the walk did not enter, and all three reported
    `n_scaling_abilities: 0` (STATE.md §7, `wiki_parser._section_tables`).
    Nothing downstream saw it: blanking those three kits and recomputing moves
    win-weighted coverage from 0.5530 to 0.5552 — UP — leaves `validate
    --check` PASSing and `data_audit`'s god audit at zero findings, because
    `kit_stat_overlay` returns {} below 3 abilities and god-fit quietly falls
    back to the role label. Measured 2026-08-29, in memory, on this data.

    So the refusal lives here, at the write, where the old value is still in
    hand. `--allow-shrink` is the override for a genuine rework."""


def _refuse_god_collapse(name: str, existing: dict, parsed: dict) -> None:
    """Raise unless `parsed` is at least as complete as what the note holds.

    Two rules, and the first is not a special case of the second: a god page
    with zero abilities does not exist on the wiki, so zero is a parse failure
    on its own, including for a god nobody has scraped before. That is the
    "half-parses a new god" case."""
    old_n = len(existing.get("abilities") or [])
    new_n = len(parsed.get("abilities") or [])
    if new_n == 0:
        raise ParseCollapse(
            f"{name}: {old_n} abilities -> 0. No god page has zero abilities, "
            f"so this is a parse failure, not a rework. Note left unchanged.")
    if new_n < old_n:
        raise ParseCollapse(
            f"{name}: {old_n} abilities -> {new_n}. Note left unchanged. If the "
            f"patch really removed {old_n - new_n}, re-run with --allow-shrink.")


def god_note_content(name: str, parsed: dict, url: str, today: str = None) -> tuple:
    """(frontmatter, wiki block) for a parsed god page. Shared by the manual
    `refresh_god` and the unattended `stats_refresh`, so the two cannot write
    different notes from the same page."""
    frontmatter = {
        "type": "smite-god",
        "name": name,
        "pantheon": parsed.get("pantheon"),
        "role": parsed.get("role"),
        "specializations": parsed.get("specializations", []),
        "damage_type": parsed.get("damage_type"),
        "release_date": parsed.get("release_date"),
        "base_stats": parsed["base_stats"],
        "abilities": parsed["abilities"],
        "aspects": parsed["aspects"],
        "source_url": url,
        "last_verified": today or date.today().isoformat(),
    }
    return frontmatter, "\n".join(f"- {a['name']}" for a in parsed["abilities"])


def item_note_content(name: str, parsed: dict, url: str, today: str = None) -> dict:
    """Frontmatter for a parsed item page. `builds_into` is left empty — it is
    derived across the whole set by `builds_into_map`."""
    frontmatter = {
        "type": "smite-item",
        "name": name,
        "tier": parsed.get("tier"),
        "cost": parsed.get("cost"),
        # `or {}`, not a default: a statless page (a free relic) parses to
        # None, and the record on disk has always said `{}` (Blink Rune).
        "stats": parsed.get("stats") or {},
        "passive": parsed.get("passive"),
        "builds_from": parsed.get("builds_from", []),
        "builds_into": [],
        "source_url": url,
        "last_verified": today or date.today().isoformat(),
    }
    # Only `God Specific` items carry an owner (wiki_parser.god_specific_owner).
    # Set conditionally rather than always: writing `god: null` onto the other
    # 215 notes would be a 215-file diff on the next full refresh, for a key
    # every reader already treats as absent.
    if parsed.get("god"):
        frontmatter["god"] = parsed["god"]
    # Conditional for the same reason: 30 of 226 items carry an Adaptive Stat clause.
    if parsed.get("adaptive_stat"):
        frontmatter["adaptive_stat"] = parsed["adaptive_stat"]
    return frontmatter


def builds_into_map(builds_from: dict) -> dict:
    """{name: [items it builds into]} from {name: builds_from}, in the order
    the names arrive. The wiki never shows this relationship directly."""
    out = {name: [] for name in builds_from}
    for name, components in builds_from.items():
        for component in components or []:
            if component in out:
                out[component].append(name)
    return out


def refresh_god(name: str, wiki_fetcher, force: bool = False,
                allow_shrink: bool = False) -> None:
    url = WIKI_BASE + name.replace(" ", "_")
    parsed = wiki_parser.parse_god_page(wiki_fetcher.fetch(url, force=force))

    # Read before write, so the refusal can quote both sides. `read_note` on a
    # path that does not exist returns empty, which is the new-god case.
    god_path = DATA_ROOT / "Gods" / f"{name}.md"
    if not allow_shrink:
        _refuse_god_collapse(name, notes.read_note(god_path)[0] or {}, parsed)

    frontmatter, wiki_block = god_note_content(name, parsed, url)
    notes.merge_god_note(god_path, frontmatter, wiki_block,
                          log_dir=DATA_ROOT / "_logs")
    slug = name.lower().replace(" ", "-").replace("'", "")
    _download_icon(parsed.get("image_url"), slug)
    # The wiki's derived icon is a head crop for most gods and a half- or
    # full-body portrait for a few; those few are pinned to a better source.
    head_url = (_head_icon_overrides().get(slug)
                or wiki_parser.derive_headshot_url(parsed.get("image_url")))
    _download_icon(head_url, slug + "-head")


def _refuse_item_collapse(name: str, existing: dict, parsed: dict) -> None:
    """The item-side twin of `_refuse_god_collapse`, and deliberately narrower.

    Zero stats is NOT a parse failure for an item the way zero abilities is for
    a god: Mote of Chaos is a genuinely statless tier-2 (a reviewed
    `data_audit` fact), and Survivor's Sash keeps `stats: {}` beside its
    recorded `adaptive_stat`. So this refuses only on a
    LOSS — stats that were there and are not, or a cost that was readable and
    is not. A statless item that stays statless writes as normal."""
    old_stats = existing.get("stats") or {}
    new_stats = parsed.get("stats") or {}
    if old_stats and not new_stats:
        raise ParseCollapse(
            f"{name}: {len(old_stats)} stats -> 0. Note left unchanged. If the "
            f"patch really stripped it, re-run with --allow-shrink.")
    if existing.get("cost") is not None and parsed.get("cost") is None:
        raise ParseCollapse(
            f"{name}: cost {existing['cost']} -> unreadable. Note left "
            f"unchanged. Re-run with --allow-shrink to accept it.")


def refresh_item(name: str, wiki_fetcher, force: bool = False,
                 allow_shrink: bool = False) -> None:
    url = WIKI_BASE + name.replace(" ", "_")
    parsed = wiki_parser.parse_item_page(wiki_fetcher.fetch(url, force=force))

    item_path = DATA_ROOT / "Items" / f"{name}.md"
    if not allow_shrink:
        _refuse_item_collapse(name, notes.read_note(item_path)[0] or {}, parsed)

    frontmatter = item_note_content(name, parsed, url)
    notes.merge_item_note(item_path, frontmatter,
                           parsed.get("passive", ""), log_dir=DATA_ROOT / "_logs")
    _download_icon(parsed.get("image_url"), name.lower().replace(" ", "-").replace("'", ""))


# Wiki item icons are served as `T<tier>_<Item_Name>.png`. That filename is the
# most reliable item marker in the cached HTML: it is generated, carries the
# tier, and appears on every page that so much as links the item — including
# the build-path boxes on its components' pages, which is how an item nobody
# has scraped still leaves a trace.
_ITEM_ICON_RE = re.compile(r"/T(\d)_([A-Za-z0-9_%'()-]+)\.png")
# Icon art for an item's upgraded or damage-typed variant, which is the same
# tracked item (`Book_of_Thoth_Evolved`, `Draconic_Scale_Magical`).
_ICON_VARIANT_SUFFIX_RE = re.compile(r"(evolved|magical|physical|ob\d+)$")


def _icon_key(name: str) -> str:
    """Item names for comparison only. Icon filenames drop the spaces the note
    keeps (`AlchemistCoat` for "Alchemist Coat") and percent-encode
    apostrophes, so a raw comparison reports ~38 false gaps against 8 real
    ones."""
    return re.sub(r"[^a-z0-9]", "", name.lower())


def discover_untracked_items(data_root: Path = None) -> dict:
    """Items the cached wiki references that have no note under Items/.

    `refresh_all` re-pulls only what is already tracked, by design — but that
    leaves no way to learn an item exists. This reads the cache we already
    have, so it costs no requests and can run on every pass.

    Returns `{name: [tiers]}`. Names come from icon filenames, so they are
    wiki page titles and can be handed straight to `--refresh ... --kind item`.
    """
    data_root = data_root or DATA_ROOT
    tracked = set()
    for path in (data_root / "Items").glob("*.md"):
        name = notes.read_note(path)[0].get("name")
        if name:
            tracked.add(_icon_key(name))

    found = {}
    for path in (data_root / "_cache" / "wiki").glob("*.html"):
        html = path.read_text(encoding="utf-8", errors="ignore")
        for tier, raw in _ITEM_ICON_RE.findall(html):
            name = raw.replace("_", " ").replace("%27", "'").strip()
            key = _icon_key(name)
            if key in tracked or _ICON_VARIANT_SUFFIX_RE.sub("", key) in tracked:
                continue
            found.setdefault(name, set()).add(int(tier))
    return {name: sorted(tiers) for name, tiers in sorted(found.items())}


def refresh_builds_into() -> None:
    """Derive builds_into for every item by inverting builds_from across the
    whole Items/ set — the wiki never shows this relationship directly."""
    items_dir = DATA_ROOT / "Items"
    all_items = {}
    for path in items_dir.glob("*.md"):
        frontmatter, body = notes.read_note(path)
        if frontmatter.get("name"):
            all_items[frontmatter["name"]] = (path, frontmatter, body)

    builds_into = builds_into_map(
        {name: fm.get("builds_from", []) for name, (_, fm, _) in all_items.items()})

    for name, (path, frontmatter, body) in all_items.items():
        frontmatter["builds_into"] = builds_into[name]
        notes.write_note(path, frontmatter, body)


# SmiteBrain publishes ONE page per god with no mode dimension, so its numbers
# are Conquest. Scraping it for other modes stored Conquest pick/win rates under
# a Joust label, which the tier list then presented as Joust community data.
# Only scrape community stats for modes the source actually covers.
COMMUNITY_MODES = {"conquest"}


# The god index: one request covering every god, with wins, losses and the
# exact match window. `division` is the rank band the numbers describe —
# Obsidian+ is the broadest of the three the source offers, so it carries the
# largest sample; the narrower Master+/Deity bands trade sample size for skill.
# Whatever is chosen has to be stated in the viewer, because "the community"
# means something different in each.
GOD_INDEX_URL = "https://smitebrain.com/gods/__data.json"
GOD_INDEX_DIVISION = "obsidian"


#: SmiteBrain's match window, as a query parameter on the per-god pages and
#: on both `__data.json` indexes (`?time=ob46`). Measured 2026-11-05: `time`
#: is the only name that works — `range`, `patch`, `window`, `timeRange`,
#: `version`, `t` and `tr` are all ignored and return the default.
COMMUNITY_WINDOW_PARAM = "time"

#: How many patch windows to probe before picking one. Two: the collapse this
#: exists to stop happens in the hours and days after a patch lands, and by
#: then the PREVIOUS patch's window is closed and complete. If both of the
#: newest two are thin, that is not a window problem and
#: `_refuse_community_collapse` is the backstop.
WINDOW_CANDIDATES = 2


def _god_index_rows(community_fetcher, window=None, force: bool = False) -> list:
    """The god index's god-level rows for one window (`None` = site default).
    Aspect-split rows would collide on god name; the default response is
    already god-level, but guard rather than trust the query string."""
    url = f"{GOD_INDEX_URL}?division={GOD_INDEX_DIVISION}"
    if window:
        url += f"&{COMMUNITY_WINDOW_PARAM}={window}"
    payload = json.loads(community_fetcher.fetch(url, force=force))
    return [r for r in smitebrain_parser.parse_god_index(payload)
            if r.get("aspect") in (None, "None")]


def choose_community_window(community_fetcher, probe_god: str, force: bool = False):
    """Which match window this run should read. `(window id, gods covered)`.

    WHY THIS EXISTS, and it is the whole reason (2026-11-05). SmiteBrain's
    per-god pages and both indexes default to the NEWEST patch, and that
    window opens the hour the patch lands. Open Beta 47 landed 2026-11-03
    11:33Z; the 2026-11-04 17:30Z refresh therefore read a window **one day
    old** — 529 matches across 86 gods, about six matches each — where Open
    Beta 46's closed window holds 67,532 across 94. At six matches a god,
    SmiteBrain publishes no Core section at all, so `parse_build_page` read
    nothing and the day's commit wrote `slot_order: []` for 24 gods and a
    short list for 24 more. `side_by_side` then skipped every god that no
    longer makes 6 of 6 and DELETED 55 live comparison pages. Every one of the
    eleven refreshes on record before it had a 100% complete record
    (91/91 then 95/95); that day read 48 of 96.

    THE RULE, and it deliberately carries no threshold: probe the newest
    `WINDOW_CANDIDATES` patch windows and take the one covering the most gods,
    a tie going to the NEWER. Nothing is tuned and nothing goes stale — the
    moment a new patch's window covers as much as the one before it, it wins
    on the tie and the run moves on by itself. The alternative, a rolling
    `1m` range, is refused in `smitebrain_parser.patch_windows`.

    One window for the WHOLE run, because a god read on this patch and a god
    read on the last one are not comparable, and the comparison target is
    exactly what these records are for.
    """
    try:
        windows = smitebrain_parser.patch_windows(
            community_fetcher.fetch(community_url(probe_god), force=force))
    except Exception as exc:
        print(f"  [window] could not read the range selector: {exc} — site default")
        return None, None
    if not windows:
        print("  [window] no patch windows offered — site default")
        return None, None

    best, best_n = None, -1
    for window in windows[:WINDOW_CANDIDATES]:        # newest first
        try:
            n = len(_god_index_rows(community_fetcher, window, force=force))
        except Exception as exc:
            print(f"  [window] {window}: {exc}")
            continue
        print(f"  window {window}: {n} gods with a record")
        if n > best_n:              # strict, so a tie keeps the NEWER window
            best, best_n = window, n
    if best is None:
        print("  [window] every candidate failed — site default")
        return None, None
    print(f"  window chosen: {best} ({best_n} gods)"
          + ("" if best == windows[0] else f" — {windows[0]} is too young to carry the roster"))
    return best, best_n


#: A community record is COMPLETE when SmiteBrain gives the god all six
#: slots. Everything downstream reads six: `community_target.comparison_six`
#: fills to six, `side_by_side` skips a god who does not make 6 of 6, and the
#: viewer's comparison page is written per god that does.
COMMUNITY_COMPLETE_SLOTS = 6

#: How many complete records a run may LOSE before it is a collapse rather
#: than churn. One, and that is generous: on the eleven refreshes on record
#: before 2026-11-04 every god with a record had a complete one — 91 of 91
#: from 10-22 to 11-02, then 95 of 95 on 11-03 — and the count only ever grew,
#: by gods being added. The slack covers a god genuinely disabled or reworked
#: out of the meta overnight. The run that this guard exists for lost 47.
COMMUNITY_COMPLETE_SLACK = 1


def complete_community_records(builds_root=None) -> dict:
    """`{god: slots}` for every Conquest build note carrying a community
    record, counting only gods whose record is COMPLETE. Read off the notes on
    disk, so it reads the same before a run and after it."""
    out = {}
    for path in sorted((builds_root or BUILDS_ROOT).glob("*-Conquest.md")):
        frontmatter, _ = notes.read_note(path)
        god = (frontmatter or {}).get("god")
        if not god:
            continue
        entry = next((b for b in frontmatter.get("builds") or []
                      if b.get("source") == "community"), None)
        if entry is None:
            continue
        slots = len(entry.get("slot_order") or [])
        if slots >= COMMUNITY_COMPLETE_SLOTS:
            out[god] = slots
    return out


def _refuse_community_collapse(before: dict, after: dict) -> None:
    """Raise unless the run kept the complete records it started with.

    `_refuse_god_collapse` does this per god note for the WIKI side, at the
    write, where the old value is still in hand. The community side had no
    such guard, which is how 2026-11-04 committed a one-day match window: the
    one enforced gate on the daily job is `validate --check`, and it PASSED —
    its Spearman floor is window-aware by design (`SPEARMAN_LATE_FROM_DAY`)
    and so relaxes to 0.30 for exactly the young window that caused the
    damage. The thing that actually noticed was two unit tests pinning god
    names, after the commit was already pushed and the site rebuilt.

    This is a ROSTER-wide rule, not a per-god one, because a thin window hits
    every god at once and no single god's note looks alarming on its own.
    """
    lost = sorted(set(before) - set(after))
    if len(lost) <= COMMUNITY_COMPLETE_SLACK:
        return
    raise ParseCollapse(
        f"community records: {len(before)} complete -> {len(after)}. "
        f"{len(lost)} god(s) lost a complete {COMMUNITY_COMPLETE_SLOTS}-slot record "
        f"({', '.join(lost[:8])}{', ...' if len(lost) > 8 else ''}). "
        f"A whole roster thinning at once is a WINDOW or a source problem, not a "
        f"meta shift — check `choose_community_window`'s log above for which match "
        f"window this run read. Nothing has been recomputed or committed. If the "
        f"loss is real, re-run with --allow-shrink.")


def refresh_god_index(community_fetcher, force: bool = False, window=None) -> dict:
    """Pull every god's win/loss record from the index, keyed by god name.

    One request for all of them, rather than a page each: the index is also
    the only place the source publishes a denominator, and the only place it
    covers gods that have no aspect at all — 18 of which the per-god scrape
    was silently skipping.

    Conquest only, like the rest of the community signal (see COMMUNITY_MODES).
    """
    return {r["god"]: r for r in _god_index_rows(community_fetcher, window, force=force)}


def god_index_entry(row: dict) -> dict:
    """The community-entry fields carried by one index row.

    Namespaced `god_*` so they never read as the aspect's numbers, which sit
    in the same entry and mean something narrower. Provenance travels with
    the figures — a win rate without its rank band and date window is not a
    fact anyone can check.
    """
    return {
        "god_win_rate": row.get("win_rate"),
        "god_matches_won": row.get("matches_won"),
        "god_matches_played": row.get("matches_played"),
        "god_division": GOD_INDEX_DIVISION,
        "god_window_start": (row.get("start_time") or "")[:10] or None,
        "god_window_end": (row.get("end_time") or "")[:10] or None,
        "god_matches_analyzed": row.get("matches_analyzed"),
    }


ITEM_INDEX_URL = "https://smitebrain.com/items/__data.json"
# Sits beside _roster.json / _patch.json: a small, versioned table the index
# build reads. Items have no per-item build note the way gods do, so their
# community record needs a home of its own rather than being derived at index
# time from whatever happened to appear in a god's slot list.
COMMUNITY_ITEMS_FILE = "_community_items.json"


#: The three provenance fields SmiteBrain publishes about a window, and where.
#: Measured 2026-11-05 against both cached `__data.json` payloads: the GOD
#: index carries all three, identical on every row (`start_time`, `end_time`,
#: `matches_analyzed`); the ITEM index carries NONE of them — its rows are
#: `display_name`, `win_rate`, `matches_played`, `use_rate` and presentation
#: fields only. So `_community_items.json`'s three fields of those names could
#: never be filled from the response that builds it, which is why they had been
#: null and empty since the file was written.
#:
#: They are filled from the god index instead. That is the same window: one run
#: picks one window (`choose_community_window`) and both indexes are fetched
#: with the same `time=` parameter and the same division, so the two describe
#: the same match set. Cross-source, and written down rather than assumed.
WINDOW_PROVENANCE = ("start_time", "end_time", "matches_analyzed")


def window_provenance(rows) -> dict:
    """`{window_start, window_end, matches_analyzed}` off index rows that
    carry them, or `{}`. Read from the FIRST row and only the first: the
    fields describe the window, not the god, and are identical on all 94."""
    row = next(iter(rows or []), None)
    if not row or not any(row.get(f) for f in WINDOW_PROVENANCE):
        return {}
    return {"window_start": (row.get("start_time") or "")[:10],
            "window_end": (row.get("end_time") or "")[:10],
            "matches_analyzed": row.get("matches_analyzed")}


def refresh_item_index(community_fetcher, data_root: Path, force: bool = False,
                       window=None, provenance=None) -> int:
    """Pull every item's win rate and match count, and store the table.

    The previous item signal was the *mean of per-god win rates* over the gods
    whose community build happened to list the item — unweighted, so an item in
    two builds counted as loudly as one in forty, and derived from the same
    aspect figures the god path just moved away from. This is the item's own
    record against a real denominator.
    """
    url = f"{ITEM_INDEX_URL}?division={GOD_INDEX_DIVISION}"
    if window:
        url += f"&{COMMUNITY_WINDOW_PARAM}={window}"
    payload = json.loads(community_fetcher.fetch(url, force=force))
    rows = smitebrain_parser.parse_item_index(payload)
    # Stripped: the source names one item "Aegis of Acceleration " with a
    # trailing space (2026-11-08), which no record can join on. The god page's
    # tile alt text carries the same space and `_tile_entry` strips it there.
    table = {
        r["display_name"].strip(): {
            "win_rate": r["win_rate"],
            "matches_won": r["matches_won"],
            "matches_played": r["matches_played"],
            "use_rate": r.get("use_rate"),
        }
        for r in rows
    }
    out = {
        "division": GOD_INDEX_DIVISION,
        # Which window produced this table, so a reader can tell a thin patch
        # window from a thin meta without re-scraping.
        "window": window,
        # The window's own provenance, from the god index (`window_provenance`):
        # the item rows carry none of it. `matches_analyzed` is the MATCH count
        # — not the number of builds observed, which is the denominator
        # `use_rate` is a share of and is ~4.6x larger (67,532 builds against
        # 14,667 matches on the 2026-11-05 table).
        **{"window_start": None, "window_end": None, "matches_analyzed": None},
        **(provenance or {}),
        "items": table,
    }
    (data_root / COMMUNITY_ITEMS_FILE).write_text(
        json.dumps(out, indent=2, sort_keys=True), encoding="utf-8")
    return len(table)


def _known_item_names():
    """Every item name our notes use. Cached — `refresh_community` calls this
    once per god and the directory does not change mid-run."""
    global _KNOWN_ITEM_NAMES
    if _KNOWN_ITEM_NAMES is None:
        _KNOWN_ITEM_NAMES = [p.stem for p in (DATA_ROOT / "Items").glob("*.md")]
    return _KNOWN_ITEM_NAMES


_KNOWN_ITEM_NAMES = None


def community_build_entry(god: str, html: str, index_row: dict | None = None) -> dict:
    """The `source: community` entry for one god's SmiteBrain build page.
    Split from `refresh_god_builds` so `new_entities` can build it before the
    god's note exists and write it only if the god passes the gate."""
    url = community_url(god)
    parsed = smitebrain_parser.parse_build_page(html)

    aspect = parsed["aspects"][0] if parsed["aspects"] else None
    community_entry = {
        "aspect": aspect["name"] if aspect else None,
        "aspect_pick_rate": aspect["pick_rate"] if aspect else None,
        "aspect_win_rate": aspect["win_rate"] if aspect else None,
        "slot_order": parsed["items"],
        # What this god's players actually open with, top 3 by pick rate. The
        # app previously showed a starter chosen by a role rule in
        # _weights.yaml, so every Carry got the same opener no matter what
        # Carry players bought.
        "community_starters": [dict(s) for s in parsed["starters"]],
        # Which BASE relic they take into the free relic slot, top 3 by pick
        # rate, same shape as `community_starters`. Filled below, once the
        # names are canonical (`free_relic_sightings`).
        "community_relics": [],
        # Every tile of each section, which is what the starter and relic
        # recommendation reads (`scoring.pick_starter`, `scoring.pick_relic`);
        # the two lists above are their top 3, for display. Copies, never the
        # same dicts: YAML would write a shared object as an anchor and alias.
        "starter_sightings": [dict(s) for s in parsed["starter_sightings"]],
        "relic_sightings": [dict(s) for s in parsed["relics"]],
        "source_url": url,
        "last_verified": date.today().isoformat(),
    }
    if index_row:
        community_entry.update(god_index_entry(index_row))
    # Canonicalise at INGEST, so exactly one place knows the two sources spell
    # some items differently and everything downstream - scoring, the index,
    # the viewer's icons and links, the audit - joins on one spelling. See
    # `notes.canonicalise_community_items` for what shipped broken.
    drift = notes.canonicalise_community_items(community_entry, _known_item_names())
    if drift:
        print(f"  {god}: renamed {drift} community item(s) to our spelling")
    relics = free_relic_sightings(community_entry["relic_sightings"])
    community_entry["relic_sightings"] = relics
    community_entry["community_relics"] = [dict(r) for r in relics[:smitebrain_parser.RELICS_SHOWN]]
    return community_entry


def free_relic_sightings(sightings: list) -> list:
    """The Relics section's tiles, minus every one our item records say is NOT
    a free base relic, in the section's own order (pick rate descending). The
    entry's `community_relics` is the first `RELICS_SHOWN` of these.

    SmiteBrain's Relics section carries a junk tail under half a percent —
    Gauntlet of Thebes, Yogi's Necklace, Devourer's Gauntlet, even the paid
    UPGRADE Time-lock Aegis, which is bought into the six and never sits in the
    free slot (`scoring.is_buildable`). None reached a top 3 on 2026-11-08, but
    a god with two real relics in play would show one as his third. A name with
    NO record is kept, not dropped: that is a new relic the wiki has and we do
    not, and it should surface as unresolved rather than vanish."""
    known, free = set(_known_item_names()), _free_relic_names()
    return [s for s in sightings or [] if s.get("name") not in known or s.get("name") in free]


def _free_relic_names() -> set:
    """Items whose record is a relic at cost 0 — the game's free slot. Cached
    like `_known_item_names`: `refresh_community` asks once per god."""
    global _FREE_RELIC_NAMES
    if _FREE_RELIC_NAMES is None:
        out = set()
        for p in (DATA_ROOT / "Items").glob("*.md"):
            fm, _ = notes.read_note(p)
            if fm.get("tier") == "Relic" and fm.get("cost") == 0:
                out.add(fm.get("name") or p.stem)
        _FREE_RELIC_NAMES = out
    return _FREE_RELIC_NAMES


_FREE_RELIC_NAMES = None


def community_url(god: str, window=None) -> str:
    url = f"{SMITEBRAIN_BASE}{god.lower().replace(' ', '-').replace(chr(39), '')}/"
    return f"{url}?{COMMUNITY_WINDOW_PARAM}={window}" if window else url


def refresh_god_builds(god: str, mode: str, community_fetcher, force: bool = False,
                       index_row: dict | None = None, window=None) -> None:
    """`index_row` is this god's row from `refresh_god_index`, when the caller
    has already pulled it. Absent, the note keeps only the aspect figures and
    the tier list falls back to scoring by those — degraded, not broken.

    `window` is the match window `choose_community_window` picked for the run;
    it MUST be the same for every god, or the records are not comparable."""
    if mode.lower() not in COMMUNITY_MODES:
        return
    html = community_fetcher.fetch(community_url(god, window), force=force)
    notes.merge_build_note(BUILDS_ROOT / f"{god}-{mode}.md", god, mode,
                           community_build_entry(god, html, index_row))


def _not_published_yet(exc: Exception, build_frontmatter: dict) -> bool:
    """A SmiteBrain 404 for a god whose note has NEVER had community data: a
    god added from the wiki (`new_entities`) before SmiteBrain has a page for
    him. Not a failure — the model's builds do not need it, and it fills in on
    the first run after SmiteBrain publishes. A 404 for a god that HAS had
    community data is still a failure: that is a slug change or an outage."""
    status = getattr(getattr(exc, "response", None), "status_code", None)
    had = any(b.get("source") == "community" for b in build_frontmatter.get("builds") or [])
    return status == 404 and not had


def refresh_community(force: bool = True, allow_shrink: bool = False) -> int:
    """Re-pull everything that changes daily, and nothing that doesn't.

    This is the half of `refresh_all` that can run unattended anywhere. The
    split is not about speed, it is about what each source needs to be reached:

        smitebrain.com   plain HTTP, no bot protection, and the numbers move
                         every day — win rates, pick rates, builds, starters.
        wiki.smite2.com  Cloudflare-gated, so it needs a real browser
                         (BrowserFetcher/Playwright), and it only changes on
                         patch days — god kits, item stats, icons.

    A daily job that tried to do both would be a daily Playwright run against
    Cloudflare from a datacentre IP, which is the part most likely to start
    failing and the part least likely to have anything new in it. So the
    scheduled job runs this, and the wiki side stays a deliberate `--all` when
    a patch lands.

    Returns the number of failures, so a caller can exit non-zero without
    having to parse the log. Every failure is isolated: an unattended pass
    should get through what it can and report the rest.
    """
    community_fetcher = CachedFetcher(DATA_ROOT / "_cache" / "smitebrain")
    failures = []

    # Read BEFORE anything is written, so the collapse refusal at the end can
    # quote both sides — the same read-before-write shape `refresh_god` uses.
    before = complete_community_records()

    build_paths = list(BUILDS_ROOT.glob("*.md"))
    probe_god = next((fm.get("god") for fm in
                      (notes.read_note(p)[0] or {} for p in sorted(build_paths))
                      if fm.get("god")), None)
    window, _ = (choose_community_window(community_fetcher, probe_god, force=force)
                 if probe_god else (None, None))

    god_index = {}
    try:
        god_index = refresh_god_index(community_fetcher, force=force, window=window)
        print(f"  god index: {len(god_index)} gods with win/loss records")
    except Exception as exc:
        print(f"  [FAILED] god index: {exc} — falling back to aspect figures")
        failures.append(f"god index: {exc}")

    try:
        n_items = refresh_item_index(community_fetcher, DATA_ROOT, force=force, window=window,
                                     provenance=window_provenance(god_index.values()))
        print(f"  item index: {n_items} items with win/loss records")
    except Exception as exc:
        print(f"  [FAILED] item index: {exc} — item stats keep their last values")
        failures.append(f"item index: {exc}")

    for build_path in build_paths:
        frontmatter, _ = notes.read_note(build_path)
        god, mode = frontmatter.get("god"), frontmatter.get("mode")
        if not (god and mode):
            continue
        try:
            refresh_god_builds(god, mode, community_fetcher, force=force,
                               index_row=god_index.get(god), window=window)
        except Exception as exc:
            if _not_published_yet(exc, frontmatter):
                print(f"  [not yet on SmiteBrain] {god}: no community page; model builds only")
                continue
            print(f"  [FAILED] build '{god}-{mode}': {exc}")
            failures.append(f"build '{god}-{mode}': {exc}")

    print(f"Community refresh: {len(build_paths) - len(failures)}/{len(build_paths)} "
          f"build notes updated, {len(failures)} failure(s)")
    for f in failures:
        print(f"  - {f}")

    after = complete_community_records()
    print(f"  complete community records: {len(before)} -> {len(after)}")
    if not allow_shrink:
        _refuse_community_collapse(before, after)
    return len(failures)


def refresh_all(force: bool = False, allow_shrink: bool = False) -> int:
    """Re-pull every god/item already known (i.e. already has a note under
    Gods/ or Items/) plus the community build for every Build note's god.
    Discovering brand-new gods/items that don't have a note yet is still a
    manual first `--refresh <name> --kind ...` — this only refreshes what's
    already tracked, matching a deliberate on-demand/weekly full pass rather
    than continuous roster discovery.

    A failure on one god/item/build (changed wiki layout, malformed note,
    wrong SmiteBrain slug, ...) is isolated and logged rather than aborting
    the whole run — an unattended weekly pass should get through everything
    it can and report what it couldn't, not silently stop partway.

    Returns the failure count. It used to return None while `main` returned 0
    regardless, so a run that printed twelve `[FAILED]` lines still exited
    clean — which made every "gate it on the exit code" plan for this command
    a no-op. `refresh_community` had it right; this is the same contract."""
    wiki_fetcher = BrowserFetcher(DATA_ROOT / "_cache" / "wiki")
    community_fetcher = CachedFetcher(DATA_ROOT / "_cache" / "smitebrain")
    failures = []

    refresh_patch_version(wiki_fetcher, force=force)

    god_names = [notes.read_note(p)[0].get("name") for p in (DATA_ROOT / "Gods").glob("*.md")]
    for name in filter(None, god_names):
        try:
            refresh_god(name, wiki_fetcher, force=force, allow_shrink=allow_shrink)
        except Exception as exc:
            print(f"  [FAILED] god '{name}': {exc}")
            failures.append(f"god '{name}': {exc}")

    item_names = [notes.read_note(p)[0].get("name") for p in (DATA_ROOT / "Items").glob("*.md")]
    for name in filter(None, item_names):
        try:
            refresh_item(name, wiki_fetcher, force=force, allow_shrink=allow_shrink)
        except Exception as exc:
            print(f"  [FAILED] item '{name}': {exc}")
            failures.append(f"item '{name}': {exc}")
    if item_names:
        refresh_builds_into()

    # One request for every god's win/loss record, before the per-god loop —
    # a failure here degrades the run to aspect-only figures rather than
    # aborting it, which is the same isolation the loop below uses.
    god_index = {}
    try:
        god_index = refresh_god_index(community_fetcher, force=force)
        print(f"  god index: {len(god_index)} gods with win/loss records")
    except Exception as exc:
        print(f"  [FAILED] god index: {exc} — falling back to aspect figures")
        failures.append(f"god index: {exc}")

    # Items get the same treatment, and must be pulled in the same run: their
    # table is a stored artifact, so skipping it leaves item stats frozen at
    # whenever it was last written while every other figure moves on.
    try:
        n_items = refresh_item_index(community_fetcher, DATA_ROOT, force=force)
        print(f"  item index: {n_items} items with win/loss records")
    except Exception as exc:
        print(f"  [FAILED] item index: {exc} — item stats keep their last values")
        failures.append(f"item index: {exc}")

    build_paths = list(BUILDS_ROOT.glob("*.md"))
    for build_path in build_paths:
        build_frontmatter, _ = notes.read_note(build_path)
        god, mode = build_frontmatter.get("god"), build_frontmatter.get("mode")
        if god and mode:
            try:
                refresh_god_builds(god, mode, community_fetcher, force=force,
                                   index_row=god_index.get(god))
            except Exception as exc:
                print(f"  [FAILED] build '{god}-{mode}': {exc}")
                failures.append(f"build '{god}-{mode}': {exc}")

    total = len(god_names) + len(item_names) + len(build_paths)
    print(f"Refresh complete: {total - len(failures)}/{total} succeeded")
    if failures:
        print(f"{len(failures)} failed:")
        for f in failures:
            print(f"  - {f}")
    return len(failures)


# Pantheon/section labels that appear alongside gods in the wiki's Gods grid.
_ROSTER_NON_GODS = {
    "Arthurian", "Babylonian", "Celtic", "Chinese", "Egyptian", "Greek", "Hindu",
    "Japanese", "Korean", "Maya", "Norse", "Polynesian", "Roman", "Voodoo",
    "Yoruba", "Tales of Arabia", "Gems",
}


def parse_roster_names(html: str) -> list:
    """God names from the wiki's Gods grid, in document order.

    Split out of `refresh_roster` so `wiki_watch` can ask what the roster says
    without writing `_roster.json` — a detector that mutates the thing it is
    watching has nothing left to compare against next time."""
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    names = []
    for a in soup.select('span[typeof="mw:File"] a[href^="/w/"][title]'):
        t = a.get("title")
        if t and t not in _ROSTER_NON_GODS and t not in names:
            names.append(t)
    return names


def refresh_roster(wiki_fetcher, force: bool = False) -> list:
    """Scrape the full SMITE 2 god roster (names) from the wiki's Gods page so the
    dev add-god modal can list every god, tracked or not. Thumbnails on that page
    are JS-loaded placeholders, so the roster is names-only; the modal shows local
    head icons for tracked gods and initials for the rest."""
    import json

    names = parse_roster_names(wiki_fetcher.fetch(WIKI_BASE + "Gods", force=force))
    roster = [{"name": n, "thumb": ""} for n in sorted(names)]
    (DATA_ROOT / "_roster.json").write_text(
        json.dumps(roster, indent=2, ensure_ascii=False), encoding="utf-8")
    return roster


def refresh_roster_add_all(force: bool = False, allow_shrink: bool = False) -> dict:
    """Scrape every roster god not yet tracked so the pool can grow toward
    the full roster in one run. A single god's scrape failure (Cloudflare,
    parse error, wrong slug, ...) is caught and recorded rather than
    aborting the batch — an unattended bulk-add should get through
    everything it can and report what it couldn't. Does NOT reindex; that's
    a separate step after the operator reviews the failures."""
    import json

    roster_path = DATA_ROOT / "_roster.json"
    if not roster_path.exists():
        return {"added": [], "failed": [], "skipped": 0,
                "note": f"{roster_path} not found; run --roster first"}

    roster = json.loads(roster_path.read_text(encoding="utf-8"))
    roster_names = [g["name"] for g in roster]
    tracked = {p.stem for p in (DATA_ROOT / "Gods").glob("*.md")}
    untracked = [name for name in roster_names if name not in tracked]

    wiki = BrowserFetcher(DATA_ROOT / "_cache" / "wiki")
    community = CachedFetcher(DATA_ROOT / "_cache" / "smitebrain")

    added = []
    failed = []
    for name in untracked:
        try:
            refresh_god(name, wiki, force=force, allow_shrink=allow_shrink)
            refresh_god_builds(name, "Conquest", community, force=force)
            added.append(name)
        except Exception as exc:
            failed.append((name, str(exc)))

    return {"added": added, "failed": failed, "skipped": len(roster_names) - len(untracked)}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Refresh SMITE 2 reference data")
    parser.add_argument("--refresh", metavar="NAME", help="re-pull one god or item by name")
    parser.add_argument("--kind", choices=["god", "item"], help="required with --refresh")
    parser.add_argument("--refresh-builds", metavar="GOD", help="re-pull SmiteBrain build stats for one god")
    parser.add_argument("--mode", default="Conquest", help="game mode for --refresh-builds")
    parser.add_argument("--all", action="store_true", help="re-pull everything already tracked")
    parser.add_argument("--community", action="store_true",
                         help="re-pull only smitebrain (daily-changing: win/pick rates, builds, "
                              "starters). No browser needed, so this is the one safe to schedule.")
    parser.add_argument("--roster", action="store_true", help="refresh the full god roster (_roster.json)")
    parser.add_argument("--roster-add-all", action="store_true",
                         help="scrape every roster god not yet tracked (no reindex)")
    parser.add_argument("--patch", action="store_true",
                         help="refresh the current SMITE 2 patch version (data/_patch.json)")
    parser.add_argument("--discover-items", action="store_true",
                         help="list items the cached wiki references but Items/ doesn't track")
    parser.add_argument("--force", action="store_true", help="bypass the local cache")
    # NOT folded into --force. --force means "ignore the HTTP cache" and a
    # patch-day operator passes it on every run; overloading it would turn
    # the collapse guard off exactly when it matters most.
    parser.add_argument("--allow-shrink", action="store_true",
                         help="accept a scrape that REMOVES abilities or stats "
                              "(a genuine rework). Off by default: the same shape "
                              "change reads as a silent parse miss, and the note "
                              "is overwritten, not merged.")
    args = parser.parse_args(argv)

    if args.patch:
        result = refresh_patch_version(BrowserFetcher(DATA_ROOT / "_cache" / "wiki"), force=args.force)
        if result:
            print(f"Refreshed patch version: {result['patch']}")
        else:
            print("Could not determine the current patch version (fetch/parse failed)")
        return 0

    if args.discover_items:
        untracked = discover_untracked_items()
        if not untracked:
            print("No untracked items referenced in the wiki cache.")
            return 0
        print(f"{len(untracked)} untracked item(s) referenced in the wiki cache:")
        for name, tiers in untracked.items():
            print(f"  T{'/'.join(str(t) for t in tiers)}  {name}")
        print("\nAdd one with:  python -m smite.refresh --refresh '<name>' --kind item")
        return 0

    if args.roster:
        roster = refresh_roster(BrowserFetcher(DATA_ROOT / "_cache" / "wiki"), force=args.force)
        print(f"Refreshed roster: {len(roster)} gods")
        return 0

    if args.roster_add_all:
        summary = refresh_roster_add_all(force=args.force, allow_shrink=args.allow_shrink)
        if summary.get("note"):
            print(summary["note"])
        print(f"Added {len(summary['added'])}, failed {len(summary['failed'])}, "
              f"skipped {summary['skipped']} (already tracked)")
        for name, err in summary["failed"]:
            print(f"  FAILED {name}: {err}")
        return 0

    if args.community:
        # Non-zero on any failure so a scheduled run fails loudly rather than
        # committing a half-refreshed dataset. A ParseCollapse is the same
        # contract, louder: the roster's community records thinned, so the
        # step fails HERE and the job never reaches its recompute or its
        # commit (`_refuse_community_collapse`).
        try:
            return 1 if refresh_community(force=True,
                                          allow_shrink=args.allow_shrink) else 0
        except ParseCollapse as exc:
            print(f"::error::{exc}")
            return 1

    if args.all:
        # Non-zero on any failure, same contract as --community. This used to
        # return 0 unconditionally, so a run printing twelve [FAILED] lines
        # still exited clean.
        n_failed = refresh_all(force=args.force, allow_shrink=args.allow_shrink)
        print("Refreshed all tracked gods, items, and builds")
        return 1 if n_failed else 0

    if args.refresh:
        if args.kind not in ("god", "item"):
            print("--refresh requires --kind god|item", file=sys.stderr)
            return 1
        wiki_fetcher = BrowserFetcher(DATA_ROOT / "_cache" / "wiki")
        if args.kind == "god":
            refresh_god(args.refresh, wiki_fetcher, force=args.force,
                        allow_shrink=args.allow_shrink)
        else:
            refresh_item(args.refresh, wiki_fetcher, force=args.force,
                         allow_shrink=args.allow_shrink)
            refresh_builds_into()
        print(f"Refreshed {args.kind} '{args.refresh}'")
        return 0

    if args.refresh_builds:
        community_fetcher = CachedFetcher(DATA_ROOT / "_cache" / "smitebrain")
        refresh_god_builds(args.refresh_builds, args.mode, community_fetcher, force=args.force)
        print(f"Refreshed community build for '{args.refresh_builds}' ({args.mode})")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
