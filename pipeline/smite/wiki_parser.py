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

        for li in table.find_all("li"):
            text = _clean(li.get_text())
            if text.lower().startswith("cooldown:"):
                ability["cooldown"] = _parse_number_list(text.split(":", 1)[1])
            elif text.lower().startswith("cost:"):
                ability["cost"] = _parse_number_list(text.split(":", 1)[1])
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
            text = _clean(td.get_text())
            if text:
                result["passive"] = text

    recipe = soup.find("table", class_="recipe-table")
    result["builds_from"] = _direct_recipe_children(recipe) if recipe else []
    return result


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
