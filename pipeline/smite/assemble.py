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


def assemble_core(rows, items_by_name, n=6, max_lifesteal=1, require=None):
    """Highest-total items filling n slots: at most one boots, at most
    `max_lifesteal` lifesteal/sustain items, no duplicates. rows must be
    pre-sorted by -total (score_god_items already does). When `require`
    {stat, min} is given, the core is seeded with the top-scored items carrying
    that stat (up to `min`, honoring the same rules) before filling by score."""
    core, used = [], set()
    have_boots = [False]
    lifesteal_count = [0]
    _row_tags = {r["item"]: r.get("tags") for r in rows}

    def _try_add(name):
        if name in used or len(core) >= n:
            return False
        item = items_by_name.get(name, {})
        if _is_boots(item):
            if have_boots[0]:
                return False
            have_boots[0] = True
        is_ls = _is_lifesteal(item, _row_tags.get(name))
        if is_ls and lifesteal_count[0] >= max_lifesteal:
            return False
        if is_ls:
            lifesteal_count[0] += 1
        core.append(name)
        used.add(name)
        return True

    if require:
        stat, need = require.get("stat"), require.get("min", 0)
        seeded = 0
        for r in rows:
            if seeded >= need:
                break
            item = items_by_name.get(r["item"], {})
            if stat in (item.get("stats") or {}) and _try_add(r["item"]):
                seeded += 1

    for r in rows:
        if len(core) >= n:
            break
        _try_add(r["item"])
    return core


def build_order(core, items_by_name, tags_map, weights):
    """Recommended purchase order for a core (heuristic — we have no real
    build-path data). stage = default + sum(tag_stage for the item's tags) +
    cost*cost_weight; sorted ascending (ties: cost, then name)."""
    cfg = (weights or {}).get("build_order") or {}
    default_stage = cfg.get("default_stage", 0)
    cost_weight = cfg.get("cost_weight", 0)
    tag_stage = cfg.get("tag_stage") or {}

    def stage(name):
        item = items_by_name.get(name, {})
        tags = tags_map.get(name) or []
        s = default_stage + sum(tag_stage.get(t, 0) for t in tags)
        cost = item.get("cost") or 0
        return (s + cost * cost_weight, cost, name)

    return sorted(core, key=stage)


def flex_slots(core, rows, count=2):
    """The `count` least-essential core items — the lowest-scored ones (rows are
    score-descending, so the core's score order is its order in `rows`). Returns
    a subset of `core`."""
    order = [r["item"] for r in rows if r["item"] in set(core)]
    n = min(count, len(order))
    return order[-n:] if n else []


# (vs_tag, needed_tag, protection_stat, human label). protection_stat is used
# instead of a tag for the burst situations (protections are a stat, not a
# passive effect).
_SITUATIONS = [
    ("heavy_cc", "cc-immunity", None, "CC-immunity / cleanse"),
    ("magic_heavy", None, "Magical Protection", "magical protection"),
    ("physical_heavy", None, "Physical Protection", "physical protection"),
    ("sustain", "anti-heal", None, "anti-heal"),
]


def _item_qualifies(name, items_by_name, tags_map, needed_tag, prot_stat, row_tags=None):
    item = items_by_name.get(name, {})
    item_tags = tags_map.get(name) or row_tags or []
    if needed_tag and needed_tag in item_tags:
        return True
    if prot_stat and parse_stat_value((item.get("stats") or {}).get(prot_stat)) is not None:
        return True
    return False


def situational_swaps(rows, items_by_name, tags_map, core=None):
    """For each matchup situation, the best item to bring IN that isn't already
    in the core (and isn't already claimed by an earlier situation, so the four
    rows don't all collapse to the same item). A swap you already build isn't a
    swap — if the core already contains a qualifying item, the row says so
    instead of telling you to add what you have; if the pool has none at all,
    the row says that. vs_tag values match the viewer's archetype taxonomy."""
    core = list(core or [])
    core_set = set(core)
    chosen = set()
    table = []
    for vs_tag, needed_tag, prot_stat, label in _SITUATIONS:
        pick = None
        for r in rows:
            name = r["item"]
            if name in core_set or name in chosen:
                continue
            if _item_qualifies(name, items_by_name, tags_map, needed_tag, prot_stat, r.get("tags")):
                pick = name
                break
        if pick:
            chosen.add(pick)
            table.append({"vs_tag": vs_tag, "swap": f"{pick} — {label}", "swap_item": pick})
            continue
        covered = next((n for n in core
                        if _item_qualifies(n, items_by_name, tags_map, needed_tag, prot_stat)), None)
        if covered:
            table.append({"vs_tag": vs_tag, "swap": f"core already covers {label} ({covered})", "swap_item": None})
        else:
            table.append({"vs_tag": vs_tag, "swap": f"(no {label} available in pool)", "swap_item": None})
    return table
