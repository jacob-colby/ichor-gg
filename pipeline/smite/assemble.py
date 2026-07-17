"""Turn scored item rows into a suggested build: a constrained core plus a
situational-swap table. Greedy-with-rules, not optimization — transparent and
debuggable. vs_tag values match the viewer's archetype taxonomy so the existing
chip-highlighting works unchanged."""
from smite.efficiency import parse_stat_value


def _is_boots(item):
    return "Movement Speed" in (item.get("stats") or {})


def _is_lifesteal(item, tags):
    stats = item.get("stats") or {}
    return "sustain" in (tags or []) or any("Lifesteal" in s for s in stats)


def assemble_core(rows, items_by_name, n=6, bruiser=False):
    """Highest-total items filling n slots: exactly one boots, at most one
    lifesteal (unless bruiser), no duplicates. rows must be pre-sorted by
    -total (score_god_items already does)."""
    core, used = [], set()
    have_boots = have_lifesteal = False
    for r in rows:
        if len(core) >= n:
            break
        name = r["item"]
        if name in used:
            continue
        item = items_by_name.get(name, {})
        if _is_boots(item):
            if have_boots:
                continue
            have_boots = True
        if _is_lifesteal(item, r.get("tags")) and have_lifesteal and not bruiser:
            continue
        if _is_lifesteal(item, r.get("tags")):
            have_lifesteal = True
        core.append(name)
        used.add(name)
    return core


# (vs_tag, needed_tag, protection_stat, human label). protection_stat is used
# instead of a tag for the burst situations (protections are a stat, not a
# passive effect).
_SITUATIONS = [
    ("heavy_cc", "cc-immunity", None, "CC-immunity / cleanse"),
    ("magic_heavy", None, "Magical Protection", "magical protection"),
    ("physical_heavy", None, "Physical Protection", "physical protection"),
    ("sustain", "anti-heal", None, "anti-heal"),
]


def situational_swaps(rows, items_by_name, tags_map):
    table = []
    for vs_tag, needed_tag, prot_stat, label in _SITUATIONS:
        pick = None
        for r in rows:
            item = items_by_name.get(r["item"], {})
            item_tags = tags_map.get(r["item"], r.get("tags") or [])
            if needed_tag and needed_tag in item_tags:
                pick = r["item"]
                break
            if prot_stat and parse_stat_value((item.get("stats") or {}).get(prot_stat)) is not None:
                pick = r["item"]
                break
        if pick:
            table.append({"vs_tag": vs_tag, "swap": f"{pick} — {label}"})
        else:
            table.append({"vs_tag": vs_tag, "swap": f"(no {label} available in pool)"})
    return table
