"""Four-signal weighted item scoring for a given god: efficiency (hard math)
+ win rate + pick rate + archetype god-fit. Transparent, tunable weights in
_weights.yaml; effect-tags in _tags.yaml. See the design spec."""
import copy
import math

import yaml

from smite import kit
from smite.efficiency import parse_stat_value

DEFAULT_WEIGHTS = {
    "signals": {"efficiency": 0.35, "win": 0.30, "pick": 0.15, "fit": 0.20},
    # role/spec label → {stat: weight}. Labels match exactly first, then by
    # whitespace token ("Carry Jungle" → Carry + Jungle), so the scraped
    # vocabulary (Mid, Solo, Support, Slayer, "Burst Damage", …) always lands.
    # Stat keys must be real item stat keys ("Max Health", not "Health").
    "role_stats": {
        "Sharpshooter": {"Attack Speed": 1.0, "Critical Chance": 1.0, "Strength": 0.6, "Lifesteal": 0.5},
        "Nuker": {"Intelligence": 1.0, "Strength": 0.6, "Penetration": 1.0, "Cooldown Rate": 0.5},
        "Mage": {"Intelligence": 1.0, "Penetration": 0.8, "Cooldown Rate": 0.5},
        "Hunter": {"Strength": 1.0, "Attack Speed": 0.8, "Critical Chance": 0.6, "Lifesteal": 0.5},
        "Carry": {"Strength": 0.8, "Attack Speed": 0.6, "Critical Chance": 0.6, "Lifesteal": 0.5},
        "Assassin": {"Strength": 1.0, "Penetration": 0.8},
        "Warrior": {"Strength": 0.8, "Physical Protection": 0.5, "Max Health": 0.5},
        "Guardian": {"Physical Protection": 1.0, "Magical Protection": 1.0, "Max Health": 0.8},
        "Tank": {"Physical Protection": 1.0, "Magical Protection": 1.0, "Max Health": 0.8},
        "Support": {"Physical Protection": 0.9, "Magical Protection": 0.9, "Max Health": 0.8},
        "Brawler": {"Max Health": 0.8, "Physical Protection": 0.5, "Magical Protection": 0.5, "Strength": 0.4},
        "Solo": {"Max Health": 0.7, "Physical Protection": 0.5, "Magical Protection": 0.5, "Strength": 0.4},
        "Jungle": {"Strength": 1.0, "Penetration": 0.8},
        "Slayer": {"Strength": 1.0, "Penetration": 0.8},
        "Mid": {"Intelligence": 1.0, "Penetration": 0.8, "Cooldown Rate": 0.5},
        "Sniper": {"Intelligence": 1.0, "Penetration": 0.8},
        "Burst": {"Penetration": 0.8, "Cooldown Rate": 0.5},
        "Healing": {"Cooldown Rate": 0.8, "Intelligence": 0.4},
        "Buffs": {"Cooldown Rate": 0.6},
        "Constant": {"Attack Speed": 0.6},
        "Pressure": {"Attack Speed": 0.5},
    },
    # "Underrated" = intrinsically good for this god (high quality = efficiency
    # + fit, independent of the meta) yet rarely picked. It deliberately does
    # NOT gate on the blended `total`: an unpicked item carries a neutral win
    # rate (0.5) and zero pick, which drag `total` down precisely for the items
    # we most want to surface. `top_quality_frac` auto-calibrates per god (flag
    # only the top fraction by quality), so no fragile absolute score cutoff.
    "underrated": {"max_pick": 0.15, "top_quality_frac": 0.30},
    # How much the kit-scaling overlay skews god-fit (0 = role map only).
    "kit_blend": 0.5,
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


# Offensive stats that are dead weight for the opposite damage type: an
# Intelligence entry on a physical god (Cernunnos's "Nuker" spec) would skew
# fit toward items the damage filter already forbids — drop them up front.
# Attack Speed stays for magical gods (hybrid Int+AS items are real). Magical
# drops Critical Chance too: a crit-carrying item without Intelligence is
# classified physical by item_damage_type and never reaches a magical god's
# pool anyway, so the entry only removes dead denominator weight, not real
# fit credit — the one exception would be a hybrid Int+Crit item, which
# would lose fit credit here, an accepted trade since none exist in the pool.
_OPPOSITE_OFFENSE = {
    "physical": ("Intelligence",),
    "magical": ("Strength", "Critical Chance"),
}


def _role_stat_map(god, weights):
    """Merged {stat: weight} fit map for a god's role + specializations. Each
    label matches `role_stats` exactly first, then falls back to whitespace
    tokens ("Carry Jungle" → Carry + Jungle), so the scraped multi-word
    vocabulary always lands. Overlapping stats keep the max weight. Offensive
    stats of the opposite damage type are dropped (the damage filter already
    forbids those items, so they'd only skew fit). Unknown labels (no exact
    or token match in role_stats) contribute nothing — a god with unseen
    vocabulary just gets an empty map, handled gracefully downstream."""
    role_stats = weights["role_stats"]
    labels = [str(s) for s in (god.get("specializations") or [])]
    if god.get("role"):
        labels.append(str(god["role"]))
    merged = {}
    for label in labels:
        keys = [label] if label in role_stats else [t for t in label.split() if t in role_stats]
        for key in keys:
            for stat, w in role_stats[key].items():
                merged[stat] = max(merged.get(stat, 0.0), w)
    for stat in _OPPOSITE_OFFENSE.get(god.get("damage_type"), ()):
        merged.pop(stat, None)
    return merged


def god_fit_score(item, god, weights, item_tags, stat_overlay=None, tag_bonus=None,
                  base_map=None):
    """Archetype fit in [0,1]: weighted presence of role-relevant stats, plus a
    small bonus for archetype-relevant tags. An optional stat_overlay (flavor
    weights, which win over the god's role map) and tag_bonus (per-tag deltas,
    may be negative) skew the fit. base_map, when given, replaces the role-map
    lookup (score_god_items passes the kit-blended map); flavor stat_overlay
    still wins on shared keys. NOT damage simulation — see spec."""
    stats = item.get("stats") or {}
    role_map = dict(base_map) if base_map is not None else _role_stat_map(god, weights)
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
                 stat_overlay=None, tag_bonus=None, base_map=None):
    w = weights["signals"]
    pick, win = lookup_rates(god_build, item["name"])
    win_norm = win if win is not None else 0.5   # neutral when unknown
    fit = god_fit_score(item, god, weights, item_tags, stat_overlay, tag_bonus,
                        base_map=base_map)
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
        max_ls, ls_explicit = fl["max_lifesteal"], True
    elif "max_lifesteal" in asp:
        max_ls, ls_explicit = asp["max_lifesteal"], True
    else:
        max_ls, ls_explicit = 1, False
    return {
        "signals": signals,
        "stat_overlay": stat_overlay,
        "tag_bonus": tag_bonus,
        "max_lifesteal": max_ls,
        "max_lifesteal_explicit": ls_explicit,
        "suppress_underrated": signals.get("pick", 1) == 0,
        "label": mode_prof.get("label"),
        "flavor": flavor,
    }


def god_max_lifesteal(god, weights, profile):
    """Effective lifesteal cap for assembling this god's core. An explicit
    flavor/aspect cap always wins; otherwise the first matching `lifesteal_caps`
    rule (starter-style damage_types/match_any gating) may raise the default.
    Exists because the community meta double-stacks sustain on basic-attack
    carries (Devourer's + Riptalon on Cernunnos) — see _disagreements.md."""
    if profile.get("max_lifesteal_explicit"):
        return profile["max_lifesteal"]
    tokens = _god_tokens(god)
    dt = god.get("damage_type")
    for rule in (weights.get("lifesteal_caps") or []):
        dts = rule.get("damage_types")
        if dts and dt not in dts:
            continue
        match_any = rule.get("match_any")
        if match_any and not (tokens & set(match_any)):
            continue
        return rule.get("max_lifesteal", profile["max_lifesteal"])
    return profile["max_lifesteal"]


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

    # Fun flavors set archetype_bypass to ignore the god's archetype entirely.
    if profile.get("archetype_bypass"):
        base_map = {}
    else:
        base_map = _role_stat_map(god, weights)
        blend = eff_weights.get("kit_blend", 0.5)
        for stat, w in kit.kit_stat_overlay(kit.scaling_profile(god), god).items():
            base_map[stat] = (1 - blend) * base_map.get(stat, 0.0) + blend * w

    rows = []
    for item in items:
        if not is_buildable(item):
            continue
        if not passes_damage_filter(item, god):
            continue
        eff = efficiency_scores_map.get(item["name"], {}).get("score", 0.5)
        row = signal_score(item, god, god_build, eff, eff_weights,
                           tags_map.get(item["name"], []), stat_overlay, tag_bonus,
                           base_map=base_map)
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
