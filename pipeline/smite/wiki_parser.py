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

        details = []
        for li in table.find_all("li"):
            text = _clean(li.get_text())
            if not text:
                continue
            details.append(text)
            low = text.lower()
            if low.startswith("cooldown:"):
                ability["cooldown"] = _parse_number_list(text.split(":", 1)[1])
            elif low.startswith("cost:"):
                ability["cost"] = _parse_number_list(text.split(":", 1)[1])
        if details:
            ability["details"] = details

        # Description = the table's prose minus the header (slot+name) and the
        # detail lines. Robust to per-ability layout variation.
        prose = _clean(table.get_text(" "))
        for chunk in [ability["slot"], ability["name"], *details]:
            prose = prose.replace(chunk, " ")
        description = re.sub(r"^[\s\-|•]+", "", _clean(prose))  # drop leading cell-separator junk
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
    for row in infobox.find_all("tr"):
        th, td = row.find("th"), row.find("td")
        if th is None or td is None:
            continue
        label = _clean(th.get_text()).rstrip(":")
        if label == "Item Type":
            m = re.search(r"Tier (\d)", td.get_text())
            result["tier"] = int(m.group(1)) if m else None
        elif label == "Total Cost":
            digits = re.sub(r"\D", "", td.get_text())
            result["cost"] = int(digits) if digits else None
        elif label == "Passive Effect":
            passive_text = _clean(td.get_text())
        elif label == "Active Effect":
            active_text = _clean(td.get_text())
        elif label == "Stats":
            stats = _parse_stats(td)
            if stats:
                result["stats"] = stats

    # Many items (e.g. Bloodforge) carry their whole effect under "Active
    # Effect" with an empty "Passive Effect" row — capture both. Stat-only
    # items (Titan's Bane, Obsidian Shard) leave both empty, so `passive`
    # stays unset. When both exist, join them into the single passive field
    # the recommender tags on and the viewer displays.
    effect_parts = [t for t in (passive_text, active_text) if t]
    if effect_parts:
        result["passive"] = " ".join(effect_parts)

    result["image_url"] = _extract_image_url(infobox)

    recipe = soup.find("table", class_="recipe-table")
    result["builds_from"] = _direct_recipe_children(recipe) if recipe else []
    return result


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
