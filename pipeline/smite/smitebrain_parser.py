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
and are intentionally excluded from `items` — the design spec's Build
schema has no field for them. (This module previously scanned the whole
document for every stat-tile it could find, silently mixing Relics,
Starters, and every Core-slot alternative into one list — confirmed via
a live fetch to be real, garbage data: ~170 entries on Chiron's page
alone. This rewrite scopes extraction to just the Core section's
top-pick-per-slot.)
"""
import re

from bs4 import BeautifulSoup

PICK_WIN_RE = re.compile(r"(\d+)%\s*pick.*?(\d+)%\s*win", re.DOTALL)


def parse_build_page(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    return {
        "items": _parse_core_recommended_build(soup),
        "aspects": _parse_aspects(soup),
    }


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
    return {"name": name, "pick_rate": int(m.group(1)) / 100, "win_rate": int(m.group(2)) / 100}


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
        aspects.append({"name": name, "pick_rate": int(m.group(1)) / 100, "win_rate": int(m.group(2)) / 100})
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
_INDEX_REQUIRED = ("god", "win_rate", "matches_played")


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


def parse_god_index(payload: dict) -> list:
    """Every god row in a `/gods/__data.json` response.

    Returns dicts carrying at least god/win_rate/matches_played; rows missing
    any of those are dropped rather than half-trusted. Order is the source's
    own (win rate, descending) — callers that need determinism should sort.
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
        if any(row.get(k) is None for k in _INDEX_REQUIRED):
            continue
        rows.append(row)
    return rows
