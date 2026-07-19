"""Four-signal weighted item scoring for a given god: efficiency (hard math)
+ win rate + pick rate + archetype god-fit. Transparent, tunable weights in
_weights.yaml; effect-tags in _tags.yaml. See the design spec."""
import copy
import math

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
    # "Underrated" = intrinsically good for this god (high quality = efficiency
    # + fit, independent of the meta) yet rarely picked. It deliberately does
    # NOT gate on the blended `total`: an unpicked item carries a neutral win
    # rate (0.5) and zero pick, which drag `total` down precisely for the items
    # we most want to surface. `top_quality_frac` auto-calibrates per god (flag
    # only the top fraction by quality), so no fragile absolute score cutoff.
    "underrated": {"max_pick": 0.15, "top_quality_frac": 0.30},
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


# Basic-attack stats mark an item as physical even without a literal Strength
# stat — a mage never builds attack speed / crit / raw Attack Damage, so these
# belong to the physical class, not the "neutral, everyone" class. Without this,
# an attack-speed item (e.g. Dagger of Frenzy) reads as neutral and can leak
# into a mage's suggested build. Intelligence still wins if present (hybrid
# converters like Nimble Ring carry Intelligence and are legitimately magical).
_PHYSICAL_SIGNAL_STATS = ("Strength", "Attack Damage", "Attack Speed", "Critical Chance")


def item_damage_type(item):
    stats = item.get("stats") or {}
    # Intelligence wins outright: it is useless to physical gods, so any item
    # carrying it is a mage item — including hybrids that also grant attack
    # speed (e.g. Nimble Ring). Only when there's no Intelligence do basic-attack
    # signals mark the item physical; everything else is neutral (buildable by
    # anyone — protections, cooldown, mana, movement).
    if "Intelligence" in stats:
        return "magical"
    if any(s in stats for s in _PHYSICAL_SIGNAL_STATS):
        return "physical"
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


def god_fit_score(item, god, weights, item_tags, stat_overlay=None, tag_bonus=None):
    """Archetype fit in [0,1]: weighted presence of role-relevant stats, plus a
    small bonus for archetype-relevant tags. An optional stat_overlay (flavor
    weights, which win over the god's role map) and tag_bonus (per-tag deltas,
    may be negative) skew the fit. NOT damage simulation — see spec."""
    stats = item.get("stats") or {}
    role_map = _role_stat_map(god, weights)
    if stat_overlay:
        role_map = {**role_map, **stat_overlay}
    denom = sum(role_map.values()) or 1.0
    stat_fit = 0.0
    for stat, w in role_map.items():
        if parse_stat_value(stats.get(stat)) is not None:
            stat_fit += w
    stat_fit = min(stat_fit / denom, 1.0)

    offense_tags = {"burst", "execute", "protection-shred"}
    bonus = 0.1 if any(t in offense_tags for t in (item_tags or [])) else 0.0
    if tag_bonus:
        for t in (item_tags or []):
            bonus += tag_bonus.get(t, 0.0)
    return max(0.0, min(stat_fit + bonus, 1.0))


def lookup_rates(god_build, item_name):
    """(pick_rate, win_rate) for item_name from the god's community build entry,
    or (0.0, None) if the item isn't in that build."""
    for entry in god_build.get("builds", []):
        if entry.get("source") == "community":
            for slot in entry.get("slot_order", []):
                if isinstance(slot, dict) and slot.get("name") == item_name:
                    return slot.get("pick_rate", 0.0), slot.get("win_rate")
    return 0.0, None


def signal_score(item, god, god_build, eff_score, weights, item_tags,
                 stat_overlay=None, tag_bonus=None):
    w = weights["signals"]
    pick, win = lookup_rates(god_build, item["name"])
    win_norm = win if win is not None else 0.5   # neutral when unknown
    fit = god_fit_score(item, god, weights, item_tags, stat_overlay, tag_bonus)
    total = (w["efficiency"] * eff_score + w["win"] * win_norm
             + w["pick"] * pick + w["fit"] * fit)
    # Intrinsic merit for this god — efficiency + fit only, renormalized so it
    # sits in the same [0,1] range as its inputs. Meta signals (win/pick) are
    # deliberately excluded: quality answers "is this good for the god?", not
    # "is this already popular?", which is what the underrated check needs.
    quality = (w["efficiency"] * eff_score + w["fit"] * fit) / ((w["efficiency"] + w["fit"]) or 1.0)
    return {"item": item["name"], "efficiency": eff_score, "win": win_norm,
            "pick": pick, "fit": fit, "quality": quality, "total": total,
            "tags": list(item_tags or [])}


def mark_underrated(rows, weights):
    """Set each row's `underrated` flag: intrinsically high-quality for this god
    (top `top_quality_frac` by quality) yet with pick rate at or below
    `max_pick`. Operates on the whole row set at once because the quality cutoff
    is relative to this god's own item distribution — a deliberately
    self-calibrating replacement for a fixed absolute score threshold, which
    never fired against real data (unpicked items can't reach a high blended
    total). Mutates rows in place and returns them."""
    u = weights["underrated"]
    if not rows:
        return rows
    frac = u.get("top_quality_frac", 0.30)
    cutoff_count = max(1, math.ceil(frac * len(rows)))
    quality_threshold = sorted((r["quality"] for r in rows), reverse=True)[cutoff_count - 1]
    for r in rows:
        r["underrated"] = r["pick"] <= u["max_pick"] and r["quality"] >= quality_threshold
    return rows


def is_buildable(item):
    """A final item you'd actually build: tier 3, or a tier-None active/relic.
    Excludes tier 1/2 component items (they're purchase-path steps, not final
    build slots)."""
    tier = item.get("tier")
    return tier is None or tier >= 3


def resolve_profile(weights, mode="Conquest", flavor=None, aspect_overlay=None):
    """Compose a mode profile ⊕ aspect ⊕ flavor into an effective scoring overlay.
    Mode sets signal overrides + tag bonuses; the aspect overlay and flavor each
    add stat weights + tag bonuses (flavor wins on a shared key) + a lifesteal cap
    (flavor's explicit cap wins, else the aspect's, else 1). suppress_underrated is
    true when the mode zeroes the pick signal (underrated needs pick data)."""
    mode_prof = (weights.get("modes") or {}).get(mode.lower(), {}) or {}
    fl = ((weights.get("flavors") or {}).get(flavor) or {}) if flavor else {}
    asp = aspect_overlay or {}
    signals = {**weights["signals"], **(mode_prof.get("signals") or {})}
    tag_bonus = {**(mode_prof.get("tag_bonus") or {}),
                 **(asp.get("tag_bonus") or {}),
                 **(fl.get("tag_bonus") or {})}
    stat_overlay = {**(asp.get("stats") or {}), **(fl.get("stats") or {})}
    if "max_lifesteal" in fl:
        max_ls = fl["max_lifesteal"]
    elif "max_lifesteal" in asp:
        max_ls = asp["max_lifesteal"]
    else:
        max_ls = 1
    return {
        "signals": signals,
        "stat_overlay": stat_overlay,
        "tag_bonus": tag_bonus,
        "max_lifesteal": max_ls,
        "suppress_underrated": signals.get("pick", 1) == 0,
        "label": mode_prof.get("label"),
        "flavor": flavor,
    }


def score_god_items(god, items, god_build, efficiency_scores_map, weights, tags_map, profile=None):
    """Score every buildable, damage-filter-passing item for one god, ranked by
    total descending. An optional profile (from resolve_profile) applies mode
    signal overrides + stat/tag overlays and can suppress the underrated flag."""
    profile = profile or {}
    eff_weights = weights
    if profile.get("signals"):
        eff_weights = _deep_merge(weights, {"signals": profile["signals"]})
    stat_overlay = profile.get("stat_overlay")
    tag_bonus = profile.get("tag_bonus")

    rows = []
    for item in items:
        if not is_buildable(item):
            continue
        if not passes_damage_filter(item, god):
            continue
        eff = efficiency_scores_map.get(item["name"], {}).get("score", 0.5)
        row = signal_score(item, god, god_build, eff, eff_weights,
                           tags_map.get(item["name"], []), stat_overlay, tag_bonus)
        row["tier"] = efficiency_scores_map.get(item["name"], {}).get("tier", "fair")
        rows.append(row)

    if profile.get("suppress_underrated"):
        for r in rows:
            r["underrated"] = False
    else:
        mark_underrated(rows, weights)
    return sorted(rows, key=lambda r: -r["total"])


def _god_tokens(god):
    """Every whitespace-separated token across the god's role + specializations,
    for matching flavor eligibility against the real lane/spec vocabulary."""
    toks = set()
    for spec in (god.get("specializations") or []):
        toks.update(str(spec).split())
    toks.update(str(god.get("role") or "").split())
    return toks


def eligible_flavors(god, weights):
    """Flavor names whose damage_types (or null=any) include the god's damage
    type, and whose match_any (or null=any) intersects the god's token set."""
    out = []
    for name, f in (weights.get("flavors") or {}).items():
        dts = f.get("damage_types")
        if dts and god.get("damage_type") not in dts:
            continue
        match_any = f.get("match_any")
        if match_any and not (_god_tokens(god) & set(match_any)):
            continue
        out.append(name)
    return out


def pick_starter(god, weights):
    """The role-appropriate starter for a god: highest-priority entry in the
    `starters` config whose damage_types (or null=any) include the god's damage
    type and whose match_any (or null=any) intersects the god's tokens. Returns
    {base, upgrade} or None if no starters are configured."""
    tokens = _god_tokens(god)
    dt = god.get("damage_type")
    best = None
    for s in (weights.get("starters") or []):
        dts = s.get("damage_types")
        if dts and dt not in dts:
            continue
        match_any = s.get("match_any")
        if match_any and not (tokens & set(match_any)):
            continue
        if best is None or s.get("priority", 0) > best.get("priority", 0):
            best = s
    if best is None:
        return None
    return {"base": best["base"], "upgrade": best["upgrade"]}
