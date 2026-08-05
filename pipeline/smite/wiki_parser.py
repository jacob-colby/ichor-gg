# tools/smite/wiki_parser.py
"""Parsers for wiki.smite2.com god and item pages (MediaWiki-style HTML,
confirmed by fetching the live site with Playwright during planning)."""
import re

from bs4 import BeautifulSoup

STAT_LABELS = {
    "Health": "health",
    "Mana": "mana",
    "Attack Speed": "attack_speed",
    "Physical Pro.": "physical_prot",
    "Magical Pro.": "magical_prot",
    "Move Speed": "move_speed",
    # Basic-attack damage. Every god page carries it and the allowlist dropped
    # it, which left no way to compute what an auto-attack actually hits for —
    # the floor any damage model has to start from.
    "Attack Power": "attack_power",
    "Health Regen": "health_regen",
    "Mana Regen": "mana_regen",
}


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _parse_stat(value_text: str):
    m = re.match(r"([\d.]+)\s*\(([+-][\d.]+)%?\)", _clean(value_text))
    if not m:
        return None
    return {"base": float(m.group(1)), "per_level": float(m.group(2))}


def _parse_number_list(text: str) -> list:
    text = text.replace("seconds", "").replace("mana", "")
    return [float(n) for n in re.findall(r"[\d.]+", text)]


def _parse_stats(td) -> dict:
    """The infobox Stats cell is a flat run of `<b>value</b> StatName <br>`
    pairs (e.g. `<b>45</b> Strength <br><b>20%</b> Critical Chance`) — not a
    table, so there's no row/column structure to key off. For each <b> take
    its own text as the value, then walk forward through its next siblings
    (stopping at the following <br>, which marks the end of that pair) to
    collect the stat-name text that follows it. Values are kept as strings
    (not coerced to a single numeric type) since some are flat numbers and
    some are percentages."""
    stats = {}
    for b in td.find_all("b"):
        value = _clean(b.get_text())
        name_parts = []
        for sibling in b.next_siblings:
            if getattr(sibling, "name", None) == "br":
                break
            name_parts.append(sibling if isinstance(sibling, str) else sibling.get_text())
        name = _clean("".join(name_parts))
        if name:
            stats[name] = value
    return stats


def _extract_image_url(infobox):
    """The infobox's first centered <td colspan="2"> row (right after the
    title row) holds the portrait/icon image on both god and item pages —
    confirmed identical structure on both page types during planning."""
    for row in infobox.find_all("tr"):
        td = row.find("td", attrs={"colspan": "2"})
        if td is None:
            continue
        style = td.get("style", "")
        if "text-align: center" not in style:
            continue
        img = td.find("img")
        if img is not None and img.get("src"):
            return img["src"]
    return None


def parse_god_page(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    infobox = soup.find("table", class_="infobox")
    if infobox is None:
        raise ValueError("no infobox found on god page")

    result = {"base_stats": {}}
    for row in infobox.find_all("tr"):
        th, td = row.find("th"), row.find("td")
        if th is None or td is None:
            continue
        label = _clean(th.get_text()).rstrip(":")
        if label == "Pantheon":
            result["pantheon"] = _clean(td.get_text())
        elif label == "Roles":
            result["role"] = _clean(td.get_text())
        elif label == "Specializations":
            result["specializations"] = [_clean(a.get_text()) for a in td.find_all("a")]
        elif label == "Attack Type":
            result["damage_type"] = "magical" if "magical" in _clean(td.get_text()).lower() else "physical"
        elif label == "Release date":
            result["release_date"] = _clean(td.get_text())
        elif label in STAT_LABELS:
            stat = _parse_stat(td.get_text())
            if stat:
                result["base_stats"][STAT_LABELS[label]] = stat

    result["image_url"] = _extract_image_url(infobox)
    result["abilities"] = _parse_abilities(soup)
    result["aspects"] = _parse_aspects(soup)
    return result


def _section_tables(soup, heading_id: str) -> list:
    """wikitable elements between an <h2 id=heading_id> and the next <h2>."""
    heading = soup.find(id=heading_id)
    if heading is None:
        return []
    tables = []
    for sibling in heading.parent.find_next_siblings():
        if sibling.find("h2") is not None:
            break
        if sibling.name == "table" and "wikitable" in (sibling.get("class") or []):
            tables.append(sibling)
    return tables


# Control text the wiki renders inside the ability table itself. It is UI, not
# content, and shipped as body copy on every one of the 513 abilities.
_ABILITY_CHROME = ("Expand Ability Video", "Expand Ability video", "Ability Video")


# The wiki colour-codes every detail line by what it does, and `get_text()`
# threw that away — leaving "Damage: 95 | 165 | 235" with no way to tell whether
# it lands as physical or magical, which is the first thing a damage model has
# to know. Recovered from the cached HTML, no refetch.
#
# The damage pair was checked against every god whose damage type we already
# store: #ff5f5f appears on 290 damage lines and every one belongs to a
# physical god, #2ca8fd on 271 and every one to a magical god. No overlap in
# either direction, across the whole 247-page cache.
_DETAIL_KINDS = {
    "#ff5f5f": "physical",   # damage, physical
    "#2ca8fd": "magical",    # damage, magical
    "#fcc26a": "mechanic",   # range, radius, cone angle, cooldown, cost
    "#c2a377": "buff",       # self/ally buffs — move speed, cooldown reduction
    "#e156c0": "debuff",     # silence, protection reduction
    "#b556ff": "slow",
    "#ff61d8": "stun",
    "#4fc253": "heal",
    "#32cdd9": "shield",
}

_HEX = re.compile(r"#[0-9a-fA-F]{6}")


def _detail_kind(li):
    """What the wiki's colouring says this detail line is, or None when it is
    uncoloured or uses one of the long tail of god-specific colours we don't
    claim to recognise. Unknown is left unknown rather than guessed."""
    span = li.find("span", style=_HEX)
    if span is None:
        return None
    m = _HEX.search(span.get("style") or "")
    return _DETAIL_KINDS.get(m.group(0).lower()) if m else None


def clean_ability_description(description: str, details, slot: str = "", name: str = "") -> str:
    """Strip the wiki's UI chrome, the duplicated detail lines, and the leading
    tagline from an ability's prose.

    Shared by the parser and by the one-off migration over already-scraped
    notes (`scripts/clean_ability_text.py`), so both do exactly the same thing.
    """
    prose = _normalize_colons(_clean(description or ""))
    for chunk in [slot, name, *(details or [])]:
        if chunk:
            prose = prose.replace(_normalize_colons(_clean(chunk)), " ")
    for junk in _ABILITY_CHROME:
        prose = prose.replace(junk, " ")
    prose = _clean(prose)
    marker = prose.find("Notes:")
    if 0 <= marker <= 60:
        prose = prose[marker + len("Notes:"):]
    return re.sub(r"^[\s\-|•]+", "", _clean(prose))


def _normalize_colons(text: str) -> str:
    """"Damage : 95" -> "Damage: 95" so inline prose and list items compare."""
    return re.sub(r"\s*:\s*", ": ", text)


def _parse_abilities(soup) -> list:
    abilities = []
    for table in _section_tables(soup, "Abilities"):
        header_th = table.find("th")
        if header_th is None:
            continue
        spans = header_th.find_all("span")
        if len(spans) < 2:
            continue
        ability = {"slot": _clean(spans[0].get_text()), "name": _clean(spans[1].get_text())}

        details, kinds, dmg_types = [], [], []
        for li in table.find_all("li"):
            text = _clean(li.get_text())
            if not text:
                continue
            details.append(text)
            kind = _detail_kind(li)
            kinds.append(kind)
            if kind in ("physical", "magical") and text.lower().startswith("damage"):
                dmg_types.append(kind)
            low = text.lower()
            if low.startswith("cooldown:"):
                ability["cooldown"] = _parse_number_list(text.split(":", 1)[1])
            elif low.startswith("cost:"):
                ability["cost"] = _parse_number_list(text.split(":", 1)[1])
        if details:
            ability["details"] = details
            # Parallel to `details`, same length, None where the wiki used a
            # colour we don't claim to recognise. Kept beside the raw lines
            # rather than folded into them so nothing reading `details` today
            # has to change.
            if any(kinds):
                ability["detail_kinds"] = kinds
        # One damage type per ability where its damage lines agree. Recorded
        # only on agreement — an ability that genuinely deals both should not
        # be flattened to whichever colour came first.
        if dmg_types and len(set(dmg_types)) == 1:
            ability["damage_type"] = dmg_types[0]

        # Description = the table's prose minus the header (slot+name), the
        # detail lines, and the wiki's own UI chrome. Subtracting the detail
        # lines used to miss almost all of them: the wiki spaces colons
        # differently inline ("Damage : 95") than in the list items
        # ("Damage: 95"), so every ability shipped its stat block twice.
        description = clean_ability_description(
            table.get_text(" "), details, ability["slot"], ability["name"])
        if description:
            ability["description"] = description

        abilities.append(ability)
    return abilities


def _parse_aspects(soup) -> list:
    tables = _section_tables(soup, "God_Aspect")
    if not tables:
        return []
    dds = tables[0].find_all("dd")
    if len(dds) < 2:
        return []
    return [{"name": _clean(dds[0].get_text()), "kit_changes": _clean(dds[1].get_text())}]


def parse_item_page(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    infobox = soup.find("table", class_="infobox")
    if infobox is None:
        raise ValueError("no infobox found on item page")

    result = {}
    passive_text = ""
    active_text = ""
    base_cost = None
    total_cost = None
    for row in infobox.find_all("tr"):
        th, td = row.find("th"), row.find("td")
        if th is None or td is None:
            continue
        label = _clean(th.get_text()).rstrip(":")
        if label == "Item Type":
            m = re.search(r"Tier (\d)", td.get_text())
            result["tier"] = int(m.group(1)) if m else (_clean(td.get_text()) or None)
        elif label == "Cost":
            digits = re.sub(r"\D", "", td.get_text())
            base_cost = int(digits) if digits else None
        elif label == "Total Cost":
            digits = re.sub(r"\D", "", td.get_text())
            total_cost = int(digits) if digits else None
        elif label == "Passive Effect":
            passive_text = _clean(td.get_text())
        elif label == "Active Effect":
            active_text = _clean(td.get_text())
        elif label == "Stats":
            stats = _parse_stats(td)
            if stats:
                result["stats"] = stats

    # Starter/base items (e.g. Bluestone Pendant, Vampiric Shroud) don't build
    # up from components, so they populate "Cost" and leave "Total Cost"
    # blank. Regular items have both, with "Cost" as the smaller
    # component-only figure — "Total Cost" must win whenever it's present.
    result["cost"] = total_cost if total_cost is not None else base_cost

    # Many items (e.g. Bloodforge) carry their whole effect under "Active
    # Effect" with an empty "Passive Effect" row — capture both. Stat-only
    # items (Titan's Bane, Obsidian Shard) leave both empty, so `passive`
    # stays unset. When both exist, join them into the single passive field
    # the recommender tags on and the viewer displays.
    effect_parts = [t for t in (passive_text, active_text) if t]
    if effect_parts:
        result["passive"] = " ".join(effect_parts)

    result["image_url"] = _extract_image_url(infobox)
    owner = god_specific_owner(result["image_url"])
    if owner:
        result["god"] = owner

    recipe = soup.find("table", class_="recipe-table")
    result["builds_from"] = _direct_recipe_children(recipe) if recipe else []
    return result


# A god-specific item's icon is generated as
# `GodSpecific_<God_Name>_<Item_Name>.png`, e.g.
# `GodSpecific_Aladdin_Genie%27s_Lamp.png`. Nothing else on the page names the
# owner — the infobox says only "God Specific" — and the owner is what decides
# whether the item may take one of a god's six slots. Ratatoskr's acorns and
# Aladdin's lamp are real build slots (the lamp is in 77% of his community
# builds), so they must be buildable for their god and invisible to everyone
# else.
_GOD_SPECIFIC_ICON_RE = re.compile(r"GodSpecific_([A-Za-z0-9_%'-]+?)_[A-Za-z0-9_%'-]+\.png")


def god_specific_owner(image_url):
    """The god a `God Specific` item belongs to, or None."""
    if not image_url:
        return None
    m = _GOD_SPECIFIC_ICON_RE.search(image_url)
    if not m:
        return None
    return m.group(1).replace("_", " ").replace("%27", "'").strip() or None


def derive_headshot_url(portrait_url):
    """From a god portrait URL, derive the square scoreboard-icon asset URL
    (the wiki serves it as the same asset name with _Default_Icon.png). Returns
    the full-res (non-thumb) /images path, or None if the portrait URL doesn't
    match the expected _Default.png asset shape."""
    if not portrait_url:
        return None
    m = re.search(r"([^/]+)_Default\.png", portrait_url)
    if not m:
        return None
    return f"/images/{m.group(1)}_Default_Icon.png"


def _direct_recipe_children(root_table) -> list:
    """The recipe tree is nested tables; a *direct* component is a
    table.recipe-table that is an immediate child of one of the root
    table's own <td> cells — not a table nested any deeper (that would be
    a component's own sub-component, not this item's direct build_from)."""
    root_tbody = root_table.find("tbody", recursive=False) or root_table
    children = []
    for row in root_tbody.find_all("tr", recursive=False):
        for cell in row.find_all("td", recursive=False):
            nested = cell.find("table", class_="recipe-table", recursive=False)
            if nested is None:
                continue
            name_cell = nested.find("td", attrs={"data-name": True})
            if name_cell is not None:
                children.append(name_cell["data-name"])
    return children
