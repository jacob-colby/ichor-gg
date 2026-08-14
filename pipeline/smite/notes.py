"""Read/write vault notes with YAML frontmatter, preserving hand-written
content across pipeline refreshes.

Two ownership models, matching the design spec:
- God/Item notes: frontmatter is entirely pipeline-owned; the body has a
  WIKI:START/END marker block for pulled prose (same pattern as the vault's
  existing Daily Hub NOW:START/END block) — everything outside it is the
  user's and untouched.
- Build notes: frontmatter holds a `builds` array with one entry per
  source (community/pro/mine). Refresh only ever replaces the
  `source: community` entry; other entries are preserved verbatim.
"""
import re
from datetime import date
from pathlib import Path

import yaml

FRONTMATTER_RE = re.compile(r"^---\n(.*?\n)---\n?", re.DOTALL)
# Markers must be the entirety of their own line. This deliberately excludes a
# marker mentioned inline as part of hand-written prose (e.g. a note *about*
# this pipeline that quotes "<!-- WIKI:START -->" mid-sentence) — only a real,
# intentionally-placed marker line matches.
#
# Known, accepted limitation: this can't distinguish a real marker line from
# one that's inside a fenced code block (e.g. hand-written docs demonstrating
# the marker syntax inside triple-backticks) — a fenced example still reads as
# a marker line and will trip the ValueError below. That's intentional: failing
# loudly on anything ambiguous is safer than trying to parse markdown fencing
# to guess intent. See test_merge_god_note_raises_on_marker_inside_code_fence.
#
# Conversely, if the *only* marker-shaped content in a not-yet-pipeline-touched
# file happens to form one well-formed pair (e.g. a fenced documentation
# example on its own, with no real block anywhere else in the file), it is
# indistinguishable from a real block and will be silently treated as one —
# accepted because this scanner never parses markdown fencing, and God/Item
# notes are always created by the pipeline's own first write before any
# hand-editing occurs, so this never arises in practice.
MARKER_LINE_RE = re.compile(r"^<!-- WIKI:(START|END) -->$", re.MULTILINE)


def _find_wiki_block_span(body: str):
    """Returns (start_match, end_match) for the single START/END marker-line
    pair, or None if there are no markers at all. Raises ValueError for
    anything else (missing END, extra markers, wrong order, nesting) —
    refusing to guess is safer than silently picking a spanning match.

    Counting *matched pairs* after the fact (the previous approach) can never
    catch an unpaired marker, because a regex only sees complete pairs — a
    stray unpaired START followed later by a real block still forms exactly
    one "pair" match, silently spanning (and swallowing) everything in
    between. Scanning the raw marker lines themselves closes that hole.
    """
    markers = list(MARKER_LINE_RE.finditer(body))
    if not markers:
        return None
    if len(markers) != 2 or markers[0].group(1) != "START" or markers[1].group(1) != "END":
        raise ValueError(
            "malformed or ambiguous WIKI markers — expected exactly one "
            "START/END pair, each alone on its own line"
        )
    return markers[0], markers[1]


def read_note(path: Path) -> tuple:
    if not path.exists():
        return {}, ""
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    frontmatter = yaml.safe_load(m.group(1)) or {}
    return frontmatter, text[m.end():]


def write_note(path: Path, frontmatter: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    yaml_text = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True)
    path.write_text(f"---\n{yaml_text}---\n{body}", encoding="utf-8")


def merge_god_note(path: Path, scraped_frontmatter: dict, wiki_block_content: str,
                    log_dir: Path = None) -> None:
    existing_frontmatter, existing_body = read_note(path)

    if log_dir is not None:
        log_refresh_diff(log_dir, scraped_frontmatter.get("name", path.stem),
                          existing_frontmatter, scraped_frontmatter)

    new_block = f"<!-- WIKI:START -->\n{wiki_block_content}\n<!-- WIKI:END -->"
    span = _find_wiki_block_span(existing_body)
    if span is None:
        new_body = f"{new_block}\n\n{existing_body}" if existing_body.strip() else f"{new_block}\n"
    else:
        # Exact string-position splice, not re.sub — so nothing in
        # wiki_block_content (backslashes included) is ever interpreted as a
        # regex replacement pattern.
        start_match, end_match = span
        new_body = existing_body[:start_match.start()] + new_block + existing_body[end_match.end():]

    write_note(path, scraped_frontmatter, new_body)


# Item notes follow the exact same ownership rule as god notes.
merge_item_note = merge_god_note


#: Spellings that differ between the community source and our item notes but
#: mean the same item. All three shipped silently for weeks.
#:
#:     community                our note                 difference
#:     Brawler's Beat Stick     Brawler’s Beat Stick     straight vs curly apostrophe
#:     Mantle of Discord        Mantle Of Discord        capital O
#:     Spear Of The Magus       Spear of the Magus       of/the casing
#:
#: A mismatch is not a cosmetic problem. `scoring.lookup_rates` finds an item's
#: community record by comparing our name to the slot's, so a failed join reads
#: as "this god's players never buy it" - pick 0, win None - which is a
#: statement about the meta rather than about our spelling. The items also lose
#: their icon and their link in the viewer, which joins the same way.
#:
#: Normalised rather than aliased, because the next drift will be a fourth
#: spelling and a table of three renames would not catch it.
def _fold_item_name(name: str) -> str:
    """A join key that ignores the ways these two sources disagree."""
    import unicodedata
    folded = unicodedata.normalize("NFKC", str(name or ""))
    # Curly apostrophe, prime, and backtick all stand in for an apostrophe.
    for ch in ("’", "ʼ", "′", "`"):
        folded = folded.replace(ch, "'")
    return " ".join(folded.split()).casefold()


def canonical_item_name(name, known_names):
    """`name` rewritten to the spelling our item notes use, or unchanged.

    Only ever rewrites when the folded forms match EXACTLY. A near-miss is left
    alone so `data_audit`'s untracked-item detector still reports a genuinely
    new item rather than silently merging it into whichever existing name
    happened to look closest.
    """
    if not name:
        return name
    lookup = {_fold_item_name(k): k for k in known_names or ()}
    return lookup.get(_fold_item_name(name), name)


def canonicalise_community_items(community_entry: dict, known_names) -> int:
    """Rewrite every item name in a community entry to our spelling, in place.

    Returns how many names changed, so a caller can log a drift that would
    otherwise be invisible.
    """
    if not community_entry or not known_names:
        return 0
    lookup = {_fold_item_name(k): k for k in known_names}
    changed = 0

    def fix(entry):
        nonlocal changed
        name = entry.get("name")
        if not name:
            return
        canon = lookup.get(_fold_item_name(name))
        if canon and canon != name:
            entry["name"] = canon
            changed += 1

    for slot in community_entry.get("slot_order") or []:
        if not isinstance(slot, dict):
            continue
        fix(slot)
        for alt in slot.get("alternates") or []:
            fix(alt)
    for key in ("community_starters", "popular_items"):
        for entry in community_entry.get(key) or []:
            if isinstance(entry, dict):
                fix(entry)
    return changed


def merge_build_note(path: Path, god: str, mode: str, community_entry: dict) -> None:
    frontmatter, body = read_note(path)
    if not frontmatter:
        frontmatter = {"type": "smite-build", "god": god, "mode": mode, "builds": []}

    builds = [b for b in frontmatter.get("builds", []) if b.get("source") != "community"]
    builds.insert(0, {"source": "community", **community_entry})
    frontmatter["builds"] = builds

    write_note(path, frontmatter, body)


def log_refresh_diff(log_dir: Path, name: str, old_frontmatter: dict, new_frontmatter: dict) -> None:
    changes = []
    for key in sorted(set(old_frontmatter) | set(new_frontmatter)):
        if key in ("source_url", "last_verified"):
            continue
        if old_frontmatter.get(key) != new_frontmatter.get(key):
            changes.append(f"- **{key}**: `{old_frontmatter.get(key)}` -> `{new_frontmatter.get(key)}`")
    if not changes:
        return
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"refresh-{date.today().isoformat()}.md"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"## {name}\n" + "\n".join(changes) + "\n\n")


def merge_suggested_entries(path: Path, god: str, mode: str, suggested_entries: list) -> None:
    """Replace all `source: suggested` entries in a Build note with the supplied
    list, preserving community/mine/pro entries verbatim. Mirrors
    merge_build_note's community replacement — only the recommender's own
    entries are regenerated, everything hand-owned survives."""
    frontmatter, body = read_note(path)
    if not frontmatter:
        frontmatter = {"type": "smite-build", "god": god, "mode": mode, "builds": []}
    kept = [b for b in frontmatter.get("builds", []) if b.get("source") != "suggested"]
    frontmatter["builds"] = kept + list(suggested_entries)
    write_note(path, frontmatter, body)


def upsert_mine_entry(path: Path, god: str, mode: str, entry: dict) -> None:
    """Add or replace (matched by name) a single source:mine build entry,
    preserving community/suggested/other-mine entries. Creates the note if
    missing."""
    frontmatter, body = read_note(path)
    if not frontmatter:
        frontmatter = {"type": "smite-build", "god": god, "mode": mode, "builds": []}
    name = entry.get("name")
    kept = [b for b in frontmatter.get("builds", [])
            if not (b.get("source") == "mine" and b.get("name") == name)]
    frontmatter["builds"] = kept + [{**entry, "source": "mine"}]
    write_note(path, frontmatter, body)


def delete_mine_entry(path: Path, name: str) -> None:
    """Remove the source:mine entry with the given name; leave all else intact."""
    frontmatter, body = read_note(path)
    if not frontmatter:
        return
    frontmatter["builds"] = [b for b in frontmatter.get("builds", [])
                             if not (b.get("source") == "mine" and b.get("name") == name)]
    write_note(path, frontmatter, body)
