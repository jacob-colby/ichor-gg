"""Parser for smitebrain.com god build pages — the single recommended
Core build order (top pick per numbered slot) and per-aspect pick/win
rate, from ranked-match data. No bot protection on this site (confirmed
with a plain curl fetch during planning) — use cache.py, not
browser_fetch.py, to reach it.

The real page has four sections in order: Aspects, Relics, Starters,
Core. Only Core represents an actual build order — it groups items by
numbered slot (1-6), each slot showing several alternative picks sorted
by pick_rate descending. The recommended build is the top (first) tile
in each slot. Relics and Starters are alternatives, not a build order,
and are intentionally excluded from `items` — they come back under their
own keys (`relics`, `starters`), parsed by `_flat_section`. (This module
previously scanned the whole document for every stat-tile it could find,
silently mixing Relics, Starters, and every Core-slot alternative into one
list — confirmed via a live fetch to be real, garbage data: ~170 entries
on Chiron's page alone. This rewrite scopes extraction to just the Core
section's top-pick-per-slot.)

RATES UNDER 1% CARRY A DECIMAL, AND WERE READ TEN TIMES TOO HIGH UNTIL
2026-11-08. The page prints "0.7% pick" for a thin tile, and the old
pattern `(\\d+)%` cannot match "0.7%" at the "0", so the search slid one
character and matched "7%". Measured over all 95 gods at the ob47 window:
the top-3 `community_starters` had the wrong third entry on 10 gods (Cu
Chulainn's "Sundering Axe 7%" is 0.7%), top-3 relics would have had it on
12, and the first aspect's pick rate was 10x on 3 (Da Ji, Horus, The
Morrigan). The Core section is unaffected on all 95 — no kept Core tile
(top pick or its two alternates) is under 1% — so no core moves.
"""
import re

from bs4 import BeautifulSoup

PICK_WIN_RE = re.compile(r"(\d+(?:\.\d+)?)%\s*pick.*?(\d+(?:\.\d+)?)%\s*win", re.DOTALL)


def _rates(m) -> tuple:
    """(pick_rate, win_rate) as fractions from a PICK_WIN_RE match. Rounded
    to 4dp so "0.7%" stores as 0.007 rather than 0.006999999999999999, and
    so an integer rate stores exactly as it always has (41% -> 0.41)."""
    return round(float(m.group(1)) / 100, 4), round(float(m.group(2)) / 100, 4)


def parse_build_page(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    starter_sightings = _flat_section(soup, "Starters")
    return {
        "items": _parse_core_recommended_build(soup),
        "aspects": _parse_aspects(soup),
        "starters": starter_sightings[:STARTERS_SHOWN],
        # Every tile, for `scoring.starter_paths`: a path whose two ends sit
        # 3rd and 4th is invisible in a top 3.
        "starter_sightings": starter_sightings,
        "relics": _parse_relics(soup),
    }


#: How many starters are worth showing. The tail is long and thin — past the
#: third the rates are usually low single digits, which is noise dressed as a
#: choice.
STARTERS_SHOWN = 3
#: The same cap for relics, applied by the caller AFTER it drops the
#: section's non-relic junk tail (`refresh.community_relics`).
RELICS_SHOWN = 3


def _parse_starters(soup) -> list:
    """The Starters section: what this god's players actually open with.

    Scraped now, having been deliberately skipped since the first version of
    this parser — "Relics and Starters are alternatives, not a build order, and
    are intentionally excluded". True of the build ORDER, but it meant the app
    had no community starter at all: the one it showed came from a role rule in
    _weights.yaml, so every Carry got the same opener regardless of what Carry
    players actually bought.

    Unlike Core these are not slotted, so there is no numbered-slot structure to
    walk — the section is a flat list of tiles already sorted by pick rate
    (`_flat_section`).

    Like relics, the rates sum to 98-103% on every god (2026-11-08, ob47): each
    player is counted ONCE, holding either the base or its upgrade, so the two
    ends of one purchase path are exclusive sightings and the path's share is
    their SUM. Ra: Pendulum of the Ages 41% + Sands of Time 17% is a 58% path.
    """
    return _flat_section(soup, "Starters")[:STARTERS_SHOWN]


def _parse_relics(soup) -> list:
    """The Relics section: which BASE relic this god's players take into the
    game's free relic slot, every tile, ranked by pick rate. Uncapped here,
    unlike starters: the section carries a junk tail of non-relic items at
    under half a percent (Gauntlet of Thebes on 6 of 95 gods, Yogi's Necklace
    on 3, one-offs like Time-lock Aegis — an UPGRADE, which is bought into the
    six), and only the caller has the item records to drop it before taking a
    top 3 (`refresh.community_build_entry`).

    The rates are shares of the god's matches and sum to 98-101% on every god
    (measured 2026-11-08, ob47): one relic per player, so each tile is an
    exclusive choice, not an overlapping one. Ra: Purification Beads 52%,
    Aegis of Acceleration 46%, Phantom Shell 2%, Blink Rune 0.2%."""
    return _flat_section(soup, "Relics")


def _flat_section(soup, title: str) -> list:
    """Every tile in one unslotted section (Starters, Relics), deduped by
    name, ranked by pick rate descending then name.

    Scoped to the heading's own section container, NOT a forward walk.
    `find_all_next()` from the heading runs into the Core section and happily
    reports Tyrfing and Jotunn's Revenge as starters — the `break` on the next
    `h2` never fires, because Core's heading sits inside a different wrapper
    than this one's rather than downstream of it.

    Deduped because the markup nests a tile inside its own wrapper and a naive
    walk sees each one twice; the higher rate wins, which is the same rule
    `build_index.popular_items` uses."""
    heading = soup.find("h2", string=re.compile(r"^\s*" + title + r"?\s*$"))
    if heading is None:
        return []
    best = {}
    for el in heading.parent.find_all("div", class_="flex"):
        entry = _tile_entry(el)
        if entry is None:
            continue
        seen = best.get(entry["name"])
        if seen is None or entry["pick_rate"] > seen["pick_rate"]:
            best[entry["name"]] = entry
    return sorted(best.values(), key=lambda e: (-e["pick_rate"], e["name"]))


def _tile_entry(container) -> dict:
    """Extract {name, pick_rate, win_rate} from one tile container (a div
    holding an img[alt] plus a descendant text-xs stat div), or None."""
    img = container.find("img", alt=True)
    if img is None:
        return None
    name = img["alt"].strip()
    if not name:
        return None
    stat_div = container.find("div", class_="text-xs")
    if stat_div is None:
        return None
    m = PICK_WIN_RE.search(stat_div.get_text())
    if not m:
        return None
    pick, win = _rates(m)
    return {"name": name, "pick_rate": pick, "win_rate": win}


def _parse_core_recommended_build(soup) -> list:
    heading = soup.find("h2", string=re.compile(r"^\s*Core\s*$"))
    if heading is None:
        return []

    # First pass: collect each numbered slot's alternatives in rank order.
    slot_alternatives = {}
    for el in heading.find_all_next():
        if el.name == "h2":
            break
        if el.name != "div":
            continue
        if "font-semibold" not in (el.get("class") or []):
            continue
        text = el.get_text(strip=True)
        if not text.isdigit():
            continue
        tile_list = el.find_next_sibling("div")
        if tile_list is None:
            continue
        entries = []
        for tile in tile_list.find_all("div", class_="flex"):
            entry = _tile_entry(tile)
            if entry is not None:
                entries.append(entry)
        if entries:
            slot_alternatives[int(text)] = entries

    # Second pass: per slot in order, take the first item not already chosen.
    # If every alternative in a slot is already used, drop the slot (a rare,
    # correct fallback — a real build never lists the same item twice).
    chosen, used = [], set()
    for n in sorted(slot_alternatives):
        alts = slot_alternatives[n]
        picked = next((e for e in alts if e["name"] not in used), None)
        if picked is None:
            continue
        used.add(picked["name"])
        others = [e for e in alts if e["name"] != picked["name"]][:2]
        chosen.append({**picked, "alternates": others} if others else picked)
    return chosen


#: The range selector on every god page: `1w`, `2w`, `1m`, then one id per
#: patch, newest first (`ob47`, `ob46`, ...). It is page chrome, present even
#: on a god whose window holds no build at all, which is what makes it safe to
#: read off any god.
PATCH_WINDOW_RE = re.compile(r"^ob(\d+)$")


def patch_windows(html: str) -> list:
    """Every PATCH window id the page offers, newest first.

    Read rather than hardcoded, so a patch landing adds its own id without a
    code change. The rolling ranges (`1w`, `2w`, `1m`) are deliberately left
    out: they straddle patches, and `validate`'s Spearman floor is calibrated
    on the window RESETTING every patch (`SPEARMAN_LATE_FROM_DAY`), so mixing
    two balance patches into one community record would quietly break the one
    constant that depends on the window's shape.
    """
    soup = BeautifulSoup(html, "html.parser")
    ids = []
    for sel in soup.find_all("select"):
        for option in sel.find_all("option"):
            value = (option.get("value") or "").strip()
            if PATCH_WINDOW_RE.match(value) and value not in ids:
                ids.append(value)
    return sorted(ids, key=lambda v: int(PATCH_WINDOW_RE.match(v).group(1)), reverse=True)


def _parse_aspects(soup) -> list:
    """Aspects are identified by name prefix ("Aspect of"), same as before
    this fix — this part of the page was already correct. Anchored off the
    stat div and searching downward for the image (rather than walking up
    from the image), matching the module's pre-fix approach: the stat div's
    class ("text-xs text-gray-400") is specific enough that it never has its
    own wrapper problem, and it is always a direct descendant of the tile
    container. Walking up from the <img> instead would be unsafe — a
    Tailwind icon-centering wrapper around the <img> (e.g.
    <div class="flex items-center justify-center ...">) also matches
    class_="flex", so find_parent from the image could land on that inner
    wrapper instead of the true tile container, silently dropping the tile."""
    aspects = []
    for stat_div in soup.find_all("div", class_="text-xs"):
        container = stat_div.find_parent("div", class_="flex")
        if container is None:
            continue
        img = container.find("img", alt=True)
        if img is None:
            continue
        name = img["alt"].strip()
        if not name.startswith("Aspect of"):
            continue
        m = PICK_WIN_RE.search(stat_div.get_text())
        if not m:
            continue
        pick, win = _rates(m)
        aspects.append({"name": name, "pick_rate": pick, "win_rate": win})
    return aspects


# ── The god index (`/gods/__data.json`) ─────────────────────────────────────
#
# The per-god pages give one aspect's win rate and nothing else. The index
# gives, for every god: wins, losses, the exact match window, and the site's
# own confidence width — so a rate can be weighed by how much play is behind
# it instead of taken at face value. It also covers gods with no aspect at
# all, which the per-god scrape silently skipped.
#
# The payload is SvelteKit's `devalue` encoding: one flat array where every
# value inside an object or array is an INDEX into that array, not the value
# itself. Negative indices are sentinels (-1 undefined, -2 a hole, -3 NaN,
# and so on) — all of which we surface as None rather than pretending to a
# number. Decoding by pattern-matching on key names happens to work today and
# breaks the moment a real integer collides with a valid index, so this
# dereferences properly.

# Fields we require before trusting a row. `matches_played` is the point of
# the exercise: without a denominator a win rate cannot be weighed.
_GOD_INDEX_REQUIRED = ("god", "win_rate", "matches_played")
# Items name themselves `display_name` and report no `matches_won`, so wins
# are derived from the rate — see `parse_item_index`.
_ITEM_INDEX_REQUIRED = ("display_name", "win_rate", "matches_played")


def _devalue(flat, index, _seen=None):
    """Resolve one devalue index into a plain Python value."""
    if not isinstance(index, int) or index < 0 or index >= len(flat):
        return None
    # Cycles are legal in devalue; ours has none, but a malformed payload
    # must not hang the refresh.
    _seen = _seen or set()
    if index in _seen:
        return None
    _seen = _seen | {index}

    value = flat[index]
    if isinstance(value, list):
        # Type-tagged scalars arrive as ["Date", "2026-07-14T…"].
        if len(value) == 2 and value[0] in ("Date", "BigInt") and isinstance(value[1], str):
            return value[1]
        return [_devalue(flat, i, _seen) for i in value]
    if isinstance(value, dict):
        return {k: _devalue(flat, i, _seen) for k, i in value.items()}
    return value


def _parse_stat_index(payload: dict, required: tuple) -> list:
    """Rows from any `__data.json` stats response carrying `required` fields.

    Rows missing any required field are dropped rather than half-trusted.
    Order is the source's own (win rate, descending) — callers needing
    determinism should sort.
    """
    nodes = [n for n in (payload.get("nodes") or []) if isinstance(n, dict)]
    flat = next((n["data"] for n in nodes if isinstance(n.get("data"), list)), None)
    if not flat:
        return []

    rows = []
    for slot, value in enumerate(flat):
        if not isinstance(value, dict) or "win_rate" not in value:
            continue
        row = _devalue(flat, slot)
        if not isinstance(row, dict):
            continue
        if any(row.get(k) is None for k in required):
            continue
        rows.append(row)
    return rows


def parse_god_index(payload: dict) -> list:
    """Every god row in a `/gods/__data.json` response."""
    return _parse_stat_index(payload, _GOD_INDEX_REQUIRED)


def parse_item_index(payload: dict) -> list:
    """Every item row in an `/items/__data.json` response.

    Items report `win_rate` and `matches_played` but no `matches_won`, so the
    win count is derived by rounding — a half-match either way is noise beside
    denominators in the hundreds, and the alternative is discarding the only
    sample size the source gives us for items.
    """
    rows = _parse_stat_index(payload, _ITEM_INDEX_REQUIRED)
    for row in rows:
        row["matches_won"] = round(row["win_rate"] * row["matches_played"])
    return rows
