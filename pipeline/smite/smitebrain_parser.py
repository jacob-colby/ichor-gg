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

    # Scan forward from the Core heading, but stop at the next <h2> (if any).
    # The real page may have further sections after Core (matchups, counters,
    # etc.); without this boundary, any unrelated "font-semibold" div with
    # digit text further down the page could be mistaken for a slot label.
    slots = {}
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
        first_tile = tile_list.find("div", class_="flex")
        if first_tile is None:
            continue
        entry = _tile_entry(first_tile)
        if entry is not None:
            slots[int(text)] = entry

    return [slots[n] for n in sorted(slots)]


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
