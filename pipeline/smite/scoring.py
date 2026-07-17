"""Four-signal weighted item scoring for a given god: efficiency (hard math)
+ win rate + pick rate + archetype god-fit. Transparent, tunable weights in
_weights.yaml; effect-tags in _tags.yaml. See the design spec."""
import copy

import yaml

from smite.efficiency import parse_stat_value

DEFAULT_WEIGHTS = {
    "signals": {"efficiency": 0.35, "win": 0.30, "pick": 0.15, "fit": 0.20},
    # role/specialization → {stat: weight}. Extend as new roles enter the pool;
    # unknown roles simply contribute nothing to fit (graceful).
    "role_stats": {
        "Sharpshooter": {"Attack Speed": 1.0, "Critical Chance": 1.0, "Strength": 0.6},
        "Nuker": {"Intelligence": 1.0, "Penetration": 1.0, "Cooldown Rate": 0.5},
        "Mage": {"Intelligence": 1.0, "Penetration": 0.8, "Cooldown Rate": 0.5},
        "Hunter": {"Strength": 1.0, "Attack Speed": 0.8, "Critical Chance": 0.6},
        "Carry": {"Strength": 0.8, "Attack Speed": 0.6, "Critical Chance": 0.6},
        "Assassin": {"Strength": 1.0, "Penetration": 0.8},
        "Warrior": {"Strength": 0.8, "Physical Protection": 0.5, "Health": 0.5},
        "Guardian": {"Physical Protection": 1.0, "Magical Protection": 1.0, "Health": 0.8},
    },
    "underrated": {"min_score": 0.6, "max_pick": 0.15},
}


def _deep_merge(base, override):
    out = copy.deepcopy(base)
    for k, v in (override or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def load_weights(path):
    if not path.exists():
        return copy.deepcopy(DEFAULT_WEIGHTS)
    override = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return _deep_merge(DEFAULT_WEIGHTS, override)


def load_tags(path):
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_weights_default():
    return copy.deepcopy(DEFAULT_WEIGHTS)


def item_damage_type(item):
    stats = item.get("stats") or {}
    has_str = "Strength" in stats
    has_int = "Intelligence" in stats
    if has_str and not has_int:
        return "physical"
    if has_int and not has_str:
        return "magical"
    return "neutral"


def passes_damage_filter(item, god):
    dt = item_damage_type(item)
    return dt == "neutral" or dt == god.get("damage_type")


def _role_stat_map(god, weights):
    merged = {}
    roles = list(god.get("specializations") or [])
    if god.get("role"):
        roles.append(god["role"])
    for role in roles:
        for stat, w in weights["role_stats"].get(role, {}).items():
            merged[stat] = max(merged.get(stat, 0.0), w)
    return merged


def god_fit_score(item, god, weights, item_tags):
    """Archetype fit in [0,1]: weighted presence of role-relevant stats, plus a
    small bonus for archetype-relevant tags. NOT damage simulation — see spec."""
    stats = item.get("stats") or {}
    role_map = _role_stat_map(god, weights)
    denom = sum(role_map.values()) or 1.0
    stat_fit = 0.0
    for stat, w in role_map.items():
        if parse_stat_value(stats.get(stat)) is not None:
            stat_fit += w
    stat_fit = min(stat_fit / denom, 1.0)

    # Small tag bonus for offense-oriented tags on damage roles. Conservative.
    offense_tags = {"burst", "execute", "protection-shred"}
    tag_bonus = 0.1 if any(t in offense_tags for t in (item_tags or [])) else 0.0
    return min(stat_fit + tag_bonus, 1.0)


def lookup_rates(god_build, item_name):
    """(pick_rate, win_rate) for item_name from the god's community build entry,
    or (0.0, None) if the item isn't in that build."""
    for entry in god_build.get("builds", []):
        if entry.get("source") == "community":
            for slot in entry.get("slot_order", []):
                if isinstance(slot, dict) and slot.get("name") == item_name:
                    return slot.get("pick_rate", 0.0), slot.get("win_rate")
    return 0.0, None


def signal_score(item, god, god_build, eff_score, weights, item_tags):
    w = weights["signals"]
    pick, win = lookup_rates(god_build, item["name"])
    win_norm = win if win is not None else 0.5   # neutral when unknown
    fit = god_fit_score(item, god, weights, item_tags)
    total = (w["efficiency"] * eff_score + w["win"] * win_norm
             + w["pick"] * pick + w["fit"] * fit)
    return {"item": item["name"], "efficiency": eff_score, "win": win_norm,
            "pick": pick, "fit": fit, "total": total, "tags": list(item_tags or [])}


def is_underrated(row, weights):
    u = weights["underrated"]
    return row["total"] >= u["min_score"] and row["pick"] <= u["max_pick"]


def is_buildable(item):
    """A final item you'd actually build: tier 3, or a tier-None active/relic.
    Excludes tier 1/2 component items (they're purchase-path steps, not final
    build slots)."""
    tier = item.get("tier")
    return tier is None or tier >= 3


def score_god_items(god, items, god_build, efficiency_scores_map, weights, tags_map):
    """Score every buildable, damage-filter-passing item for one god, ranked by
    total descending."""
    rows = []
    for item in items:
        if not is_buildable(item):
            continue
        if not passes_damage_filter(item, god):
            continue
        eff = efficiency_scores_map.get(item["name"], {}).get("score", 0.5)
        row = signal_score(item, god, god_build, eff, weights, tags_map.get(item["name"], []))
        row["underrated"] = is_underrated(row, weights)
        row["tier"] = efficiency_scores_map.get(item["name"], {}).get("tier", "fair")
        rows.append(row)
    return sorted(rows, key=lambda r: -r["total"])
