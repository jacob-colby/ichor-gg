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
    """wikitable elements between an <h2 id=heading_id> and the next <h2>,
    including ones NESTED inside a sibling rather than being one.

    The nesting is not a curiosity — it is how the wiki renders every
    STANCE god, and reading only top-level siblings lost their entire kit.
    Ullr, Artio and Merlin put their real abilities inside a
    `div.img-tab-wrapper`, one `div.img-tab-panel` per stance, so a walk that
    only accepted `sibling.name == "table"` collected exactly two tables for
    each of them — Basic Attack and Passive — and none of the abilities.

    Measured on the cached HTML: 28 ability tables were invisible this way,
    8 for Ullr (Bow + Axe), 8 for Artio, 12 for Merlin (Arcane + Fire + Ice).
    Downstream that is not a cosmetic gap. `kit.scaling_profile` counts
    abilities carrying a scaling line, so all three gods reported
    `n_scaling_abilities: 0`; `kit_stat_overlay` returns {} below 3, so their
    god-fit fell back to the role label alone with no measurement in it at
    all, and `scoring.is_hybrid_scaler` could never fire for them. Ullr is the
    god a Masters player picked out as the recommender's worst output."""
    heading = soup.find(id=heading_id)
    if heading is None:
        return []
    tables = []
    for sibling in heading.parent.find_next_siblings():
        if sibling.find("h2") is not None:
            break
        if sibling.name == "table" and "wikitable" in (sibling.get("class") or []):
            tables.append(sibling)
        else:
            # `find_all` is document order, so a wrapper's panels arrive in the
            # order the page presents them (first stance first).
            tables.extend(sibling.find_all("table", class_="wikitable"))
    return tables


def _stance_of(table) -> str | None:
    """Which stance tab this ability table sits under, or None for a god with
    no stances.

    The panel carries no label of its own — the readable name lives on the
    matching nav trigger's `data-target` ("Bow", "Axe", "Arcane", …) — so the
    two are paired by position within the wrapper, which is what makes the tab
    UI work in the first place."""
    panel = table.find_parent("div", class_="img-tab-panel")
    if panel is None:
        return None
    wrapper = panel.find_parent("div", class_="img-tab-wrapper")
    if wrapper is None:
        return None
    panels = wrapper.find_all("div", class_="img-tab-panel")
    triggers = wrapper.find_all("span", class_="img-trigger")
    try:
        index = panels.index(panel)
    except ValueError:
        return None
    if index >= len(triggers):
        return None
    return triggers[index].get("data-target") or None


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
    #: (slot, name, details) already emitted. A stance god's shared ability is
    #: repeated once per tab, and the repeat is only sometimes a duplicate:
    #: Merlin's Elemental Mastery is byte-identical in all three stances, while
    #: his Flicker is a DIFFERENT ability in each (Arcane heals, Fire applies
    #: Radiate's burn, Ice cuts cooldowns). Keying on the details rather than
    #: on the name keeps all three Flickers and collapses the one that really
    #: is the same ability listed three times — which matters because
    #: `kit.scaling_profile` averages over abilities, so a triple-counted one
    #: would weight the kit toward itself.
    seen = set()
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

        key = (ability["slot"], ability["name"], tuple(details))
        if key in seen:
            continue
        seen.add(key)

        # Recorded only where it exists, so the 84 gods without stances carry
        # no empty field and nothing downstream has to learn a new shape.
        stance = _stance_of(table)
        if stance:
            ability["stance"] = stance

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


def _parse_cost(text: str):
    """A gold cost from an infobox cell, or None when there isn't one.

    Stripping non-digits and calling `int` is what this used to do, and it
    turned the wiki's `-1` sentinel into a one-gold item. Genie's Lamp reads
    `Cost: -1` with `Total Cost:` blank — it is not purchasable, Aladdin simply
    has it — and it shipped priced at 1 gold. That is the Blink Rune failure
    exactly (`scoring.is_buildable`): a near-free item is maximally
    "undervalued" by `cost - predicted_cost`, so the arithmetic reads the
    cheapest thing in the game as the best bargain in it.

    A negative cost is a sentinel, never a price, so it returns None and the
    item is treated as unpriced rather than as free."""
    m = re.search(r"-?\d+", text or "")
    if not m:
        return None
    value = int(m.group())
    return value if value >= 0 else None


# Every stat name the corpus uses. A closed vocabulary is what makes
# `_stats_from_prose` safe: it matches "45 Strength" and refuses "5 projectiles",
# so recovering stats from prose can't invent a stat out of ability text.
# Longest-first so "Max Health" wins over a hypothetical "Health".
ITEM_STAT_NAMES = (
    "Physical Protection", "Magical Protection", "Critical Chance",
    "Cooldown Rate", "Movement Speed", "Attack Damage", "Attack Speed",
    "Health Regen", "Intelligence", "Mana Regen", "Max Health", "Max Mana",
    "Penetration", "Pathfinding", "Dampening", "Lifesteal", "Strength",
    "Tenacity", "Plating", "Echo",
)
_PROSE_STAT_RE = re.compile(
    r"(?<![\w.])(\d+(?:\.\d+)?%?)\s+(" + "|".join(ITEM_STAT_NAMES) + r")\b")


def _stats_from_prose(text: str) -> dict:
    """Stats an editor typed into the Passive Effect cell instead of Stats.

    A wiki data-entry quirk, not a parsing failure on our side: Briskberry
    Acorn's infobox has `Stats:` EMPTY and `Passive Effect: Non-Aspect: 45
    Strength 8 Pathfinding Aspect: 400 Max Health 4 Health Regen 2 Mana Regen
    <then the real ability prose>`. Its two sibling acorns have the identical
    stat shape (Strength 45 + Max Health 400 + two extras) filled in properly,
    so this is one page formatted differently, not a different kind of item.

    The cost of not recovering them is total. `scoring.is_buildable` excludes a
    statless item outright — correctly, since efficiency and fit are both
    functions of `stats` and would otherwise be reading an empty dict — so
    Briskberry Acorn was structurally unbuildable while being the community's
    single most-picked opening item for Ratatoskr at 30%. Not a ranking the
    model got wrong; a pick it was forbidden to make.

    BOTH aspect branches are taken, as a union. It reads like double-counting
    and isn't: the sibling acorns' own `Stats:` cells list stats from both
    branches too (Ashwhorl carries Attack Speed and Tenacity, Thistlethorn
    Lifesteal and Cooldown Rate, both alongside the shared Strength and Max
    Health), so the union is what the wiki means by an acorn's stat line — the
    Non-Aspect/Aspect labels here are formatting on the ability changes that
    follow, which the editor let run backwards over the stats.

    Only ever called when `Stats:` came back empty, so it can never override a
    properly-filled cell."""
    return {name: value for value, name in _PROSE_STAT_RE.findall(text or "")}


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
            base_cost = _parse_cost(td.get_text())
        elif label == "Total Cost":
            total_cost = _parse_cost(td.get_text())
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

    # Last resort only — see `_stats_from_prose`. An empty `Stats:` cell beside
    # a passive that names stats is an editing slip on the wiki, and the
    # alternative to reading it is shipping the item unbuildable.
    if not result.get("stats"):
        recovered = _stats_from_prose(passive_text)
        if recovered:
            result["stats"] = recovered

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
