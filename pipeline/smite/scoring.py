"""Four-signal weighted item scoring for a given god: efficiency (hard math)
+ win rate + pick rate + archetype god-fit. Transparent, tunable weights in
_weights.yaml; effect-tags in _tags.yaml. See the design spec."""
import copy
import math

import yaml

from smite import damage_value, kit
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


# A god's `damage_type` is ONE label, but SMITE 2 kits are not one thing.
# Neith is labelled physical and takes 55% of her ability damage off
# Intelligence; Danzaburou 53%; Cabrakan is labelled magical and takes 59% off
# Strength. The label was a hard gate, so the recommender could not offer these
# gods a single item the stat their kit mostly scales on — while the community
# builds them that way and nothing else. Neith's whole community build was
# Intelligence, which scored her a structural 0% with zero items even visible.
#
# Nothing new is scraped for this: `kit.scaling_profile` already measures the
# split from the per-ability coefficients. The label decides which stats are
# ON-type; the measurement decides whether the OFF-type ones are also allowed.
#
# Defaults live in _weights.yaml under `hybrid_scaling`. The confidence floor
# is the one `kit.kit_stat_overlay` already uses — under 3 abilities with
# parsed scaling the share is an artifact of a sparse scrape (Artio and Ullr
# scrape 2 abilities each), so those gods keep the strict label.
HYBRID_MIN_OFF_SHARE = 0.30
HYBRID_MIN_ABILITIES = 3


def off_type_share(god, weights=None):
    """How much of this god's ability damage scales on the stat their
    `damage_type` label says is useless. 0.0 when the kit scrape is too thin
    to trust."""
    cfg = ((weights or {}).get("hybrid_scaling") or {})
    min_abilities = cfg.get("min_abilities", HYBRID_MIN_ABILITIES)
    profile = kit.scaling_profile(god)
    if profile["n_scaling_abilities"] < min_abilities:
        return 0.0
    return (profile["int_share"] if god.get("damage_type") == "physical"
            else profile["str_share"])


def is_hybrid_scaler(god, weights=None):
    cfg = ((weights or {}).get("hybrid_scaling") or {})
    if not cfg.get("enabled", True):
        return False
    threshold = cfg.get("min_off_share", HYBRID_MIN_OFF_SHARE)
    return off_type_share(god, weights) >= threshold


def passes_damage_filter(item, god, weights=None):
    dt = item_damage_type(item)
    if dt == "neutral" or dt == god.get("damage_type"):
        return True
    return is_hybrid_scaler(god, weights)


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
    vocabulary just gets an empty map, handled gracefully downstream.

    A measured hybrid scaler keeps its off-type POWER stat, because
    `passes_damage_filter` now lets those items through and a stat the fit map
    scores at zero would be admitted and then never picked. Only the power stat
    is restored — Critical Chance stays dropped for magical gods, since its
    exclusion was never about damage type (see `_OPPOSITE_OFFENSE`)."""
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
    dropped = set(_OPPOSITE_OFFENSE.get(god.get("damage_type"), ()))
    if is_hybrid_scaler(god, weights):
        dropped.discard("Intelligence" if god.get("damage_type") == "physical"
                        else "Strength")
    for stat in dropped:
        merged.pop(stat, None)
    return merged


def stat_reference(items):
    """`{stat: reference magnitude}` for the magnitude-aware fit — the median
    of the non-zero values each stat takes across buildable items.

    Median rather than max: one outlier item would otherwise set the scale for
    every other, and a stat carried by a single 200-point item would make every
    ordinary roll of it look negligible."""
    import statistics
    seen = {}
    for item in items:
        if not is_buildable(item):
            continue
        for stat, raw in (item.get("stats") or {}).items():
            value = parse_stat_value(raw)
            if value:
                seen.setdefault(stat, []).append(value)
    return {stat: statistics.median(vals) for stat, vals in seen.items()}


def god_fit_score(item, god, weights, item_tags, stat_overlay=None, tag_bonus=None,
                  base_map=None, stat_reference=None):
    """Archetype fit in [0,1]: weighted presence of role-relevant stats, plus a
    small bonus for archetype-relevant tags. An optional stat_overlay (flavor
    weights, which win over the god's role map) and tag_bonus (per-tag deltas,
    may be negative) skew the fit. base_map, when given, replaces the role-map
    lookup (score_god_items passes the kit-blended map); flavor stat_overlay
    still wins on shared keys.

    `stat_reference` {stat: typical magnitude} makes the stat term MAGNITUDE
    aware (B4). Without it this counts presence — an item with 5 Strength and
    one with 80 score identically, which was the single largest imprecision in
    the per-god score. With it, each stat contributes its own share of a
    reference magnitude, so a token amount is credited as a token amount.
    Saturating at 1.0 keeps a freakishly large roll from dominating a weight
    that is meant to say "this god wants this stat", not "more is always
    better without limit"."""
    stats = item.get("stats") or {}
    role_map = dict(base_map) if base_map is not None else _role_stat_map(god, weights)
    if stat_overlay:
        role_map = {**role_map, **stat_overlay}
    denom = sum(role_map.values()) or 1.0
    stat_fit = 0.0
    for stat, w in role_map.items():
        value = parse_stat_value(stats.get(stat))
        if value is None:
            continue
        if stat_reference:
            # Fraction of a reference magnitude, so 5 Strength is not 80.
            ref = stat_reference.get(stat)
            share = min(value / ref, 1.0) if ref else 1.0
        else:
            share = 1.0
        stat_fit += w * share
    stat_fit = min(stat_fit / denom, 1.0)

    offense_tags = {"burst", "execute", "protection-shred"}
    bonus = 0.1 if any(t in offense_tags for t in (item_tags or [])) else 0.0
    if tag_bonus:
        for t in (item_tags or []):
            bonus += tag_bonus.get(t, 0.0)
    return max(0.0, min(stat_fit + bonus, 1.0))


def lookup_rates(god_build, item_name):
    """(pick_rate, win_rate) for item_name from the god's community build entry,
    or (0.0, None) if this god's players never buy it.

    A slot pick is authoritative. Failing that, the item's best sighting among
    the slots' `alternates` — which is what `build_index.popular_items` shows
    the reader, so the two agree on any item the build row can call unbought.

    They used to disagree, and the product printed both numbers on one screen.
    Ratatoskr's page rendered "Thistlethorn Acorn · pick 0.00 · meta doesn't
    buy this" in the buy order while the popular-items panel directly below it
    said "27% pick · 48% win" for the same item. Reading slot picks only, an
    item that is the community's SECOND choice in three separate slots looked
    like an item nobody had ever bought. It affected 406 item/god pairs: the
    win signal saw 519 of them and should have seen 925.

    This costs headline coverage, 53.8% -> 49.6%, and that is the leaked term
    moving rather than quality. Coverage counts only the community's SLOT
    picks, so preferring a 55%-win alternate over a 46%-win slot pick is scored
    as a miss — exactly the judgement the tool exists to make. The within-god
    rank correlation, which this does not distort, is unchanged at 0.564. See
    the leakage probe in calibrate.py."""
    best_alternate = None
    for entry in god_build.get("builds", []):
        if entry.get("source") != "community":
            continue
        for slot in entry.get("slot_order", []):
            if not isinstance(slot, dict):
                continue
            if slot.get("name") == item_name:
                # An item the community actually slots is authoritative here,
                # and returning early matters: the same item can also appear as
                # a higher-pick alternate in another slot, and preferring that
                # sighting detaches the item from the rate it is graded against
                # (measured: rank correlation 0.564 -> 0.453).
                return slot.get("pick_rate", 0.0), slot.get("win_rate")
            for alt in slot.get("alternates") or []:
                if alt.get("name") != item_name:
                    continue
                rate = alt.get("pick_rate") or 0.0
                if best_alternate is None or rate > best_alternate[0]:
                    best_alternate = (rate, alt.get("win_rate"))
    return best_alternate or (0.0, None)


# What an item scores on the `win` signal when the community has never built
# it. NOT a neutral value, despite reading like one — and the distinction runs
# the recommender.
#
# SmiteBrain reports a win rate for a MEDIAN OF 5 items per god against a
# candidate pool of 95. So for 95.2% of everything ranked, this constant IS the
# win signal — and `win` carries the largest weight in the blend at 0.45. Its
# job is not to rank the unknown items against each other (it cannot; they all
# get the same number). Its job is a THRESHOLD: it decides where the ~5
# measured items sit relative to the ~90 unmeasured ones.
#
# 0.5 is not the middle of anything real. Observed item win rates average
# 0.556, and 66% of them are above 0.5, so this setting quietly favours the
# unmeasured item over the average measured one. That is what produces the
# remaining 0%-coverage gods: Anubis's community items measure 0.27-0.47 and
# Danzaburou's 0.36-0.44, so every one of them ranks below an item with no data
# at all, and their cores fill with unmeasured items.
#
# LEFT AT 0.5 DELIBERATELY. The obvious repair — impute the god's own mean
# instead of a constant — is unmeasurable here, because the only metric that
# responds is `validate.compute`, whose coverage term rewards any change that
# favours community items and punishes any change that does not (see the
# leakage probe in calibrate.py). Measured anyway, for the record: god-mean
# imputation moves coverage 53.3% -> 38.3% and leaves the within-god rank
# correlation at 0.569, i.e. the ONLY thing that moved was the circular term.
# Reading `alternates` as well (which would give 925 items real data instead of
# 519) behaves identically: coverage 53.3% -> 49.2%, rank correlation unchanged
# at 0.569.
#
# Changing this needs a metric that is not made of the community's own build.
UNKNOWN_WIN_RATE = 0.5


def unknown_win_rate(weights):
    return (weights or {}).get("unknown_win_rate", UNKNOWN_WIN_RATE)


def signal_score(item, god, god_build, eff_score, weights, item_tags,
                 stat_overlay=None, tag_bonus=None, base_map=None,
                 stat_reference=None):
    w = weights["signals"]
    pick, win = lookup_rates(god_build, item["name"])
    win_norm = win if win is not None else unknown_win_rate(weights)
    fit = god_fit_score(item, god, weights, item_tags, stat_overlay, tag_bonus,
                        base_map=base_map, stat_reference=stat_reference)
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


def is_buildable(item, god=None):
    """A final item that can occupy one of the SIX core slots: tier 3, plus a
    `God Specific` item when `god` is the god it belongs to.

    Excludes tier 1/2 components (purchase-path steps, not final slots) and
    relics, which the game gives their own slots — a relic has never competed
    for the space it wins here.

    God-specific items DO take one of the six, but only for their owner:
    Aladdin's Genie's Lamp is in 77% of his community builds and Ratatoskr's
    acorns in 32-43% of his, while being unbuyable for all 85 other gods.
    Passing no `god` answers the god-agnostic question ("can this ever take a
    core slot?") and excludes them, which is what the gold model and the item
    page want.

    Also excludes an item with NO STATS AT ALL, which every signal here is
    blind to. Efficiency is `cost - predicted_cost` and prediction is a sum
    over stats, so a statless item's residual is just its cost against the
    intercept; fit is a weighted read of its stats, so it scores zero. Neither
    number means anything, and both were being compared against items where
    they do.

    Found via Blink Rune: cost 0, `stats: {}`, tier "Relic". A free item is
    maximally *undervalued* by that arithmetic — it read as the best bargain in
    the game and had reached 262 shipped build slots. Blinking Abyss is the
    mirror case at 2600 gold and no stats, which reads as maximally premium.
    Measured then, and the largest single gain in the recommender's history:
    coverage 48.4% -> 51.0%, win-weighted 50.6% -> 53.3%.

    THE STATLESS RULE WAS NOT ENOUGH, and the reason is worth recording. It
    excluded every relic only because every relic then known happened to be
    statless — a coincidence in the data standing in for a rule about the game.
    Scraping the eight T3/relic items the item list had never discovered
    (2026-08-05) broke the coincidence: Time-lock Aegis, Shell of Rebuke,
    Talisman of Purification and Agility Greaves all carry stats, and all four
    immediately started winning core slots at 2500 gold apiece. Excluding
    relics by TIER, which is what the game actually says, restores it:
    coverage 51.0% -> 52.6%, win-weighted 53.1% -> 54.8%.

    Note the asymmetry with `efficiency.efficiency_pool`, which deliberately
    keeps relics IN the gold fit. Removing them from both drops coverage to
    47.5% — the same lesson components taught: a narrower fit pool identifies
    stat prices worse, and the fit's job is to rank, not to predict cost."""
    if not (item.get("stats") or {}):
        return False
    owner = item.get("god")
    if owner:
        return bool(god) and owner == god.get("name")
    tier = item.get("tier")
    # A non-numeric tier is the wiki's label for a relic/glyph/active.
    return isinstance(tier, int) and not isinstance(tier, bool) and tier >= 3


def resolve_profile(weights, mode="Conquest", flavor=None, aspect_overlay=None):
    """Compose a mode profile ⊕ aspect ⊕ flavor into an effective scoring overlay.
    Mode sets signal overrides + tag bonuses; the aspect overlay and flavor each
    add stat weights + tag bonuses (flavor wins on a shared key) + a lifesteal cap
    (flavor's explicit cap wins, else the aspect's, else 1). suppress_underrated is
    true when the mode zeroes the pick signal (underrated needs pick data).
    Fun flavors (`fun: true`) zero the win/pick meta signals and may declare
    `bypass` entries ("damage_filter", "archetype_fit") to escape class guards.
    A mode may also declare `excluded_items` — items that do not exist in it."""
    mode_prof = (weights.get("modes") or {}).get(mode.lower(), {}) or {}
    fl = ((weights.get("flavors") or {}).get(flavor) or {}) if flavor else {}
    asp = aspect_overlay or {}
    bypass = set(fl.get("bypass") or [])
    fun = bool(fl.get("fun"))
    signals = {**weights["signals"], **(mode_prof.get("signals") or {})}
    if fun:
        # Off-class items have no meta data; a neutral 0.5 win rate would only
        # add noise, so fun builds are scored on efficiency + flavor fit alone.
        signals = {**signals, "win": 0.0, "pick": 0.0}
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
        # Items the mode does not offer at all. A flavor cannot bypass this the
        # way it bypasses the damage filter: an item that isn't in the shop is
        # not a daring pick, it's a build the player cannot actually assemble.
        "excluded_items": frozenset(mode_prof.get("excluded_items") or ()),
        "label": mode_prof.get("label"),
        "flavor": flavor,
        "bypass_damage_filter": "damage_filter" in bypass,
        "archetype_bypass": "archetype_fit" in bypass,
        "fun": fun,
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
        hybrid = is_hybrid_scaler(god, eff_weights)
        for stat, w in kit.kit_stat_overlay(kit.scaling_profile(god), god,
                                            include_off_type=hybrid).items():
            base_map[stat] = (1 - blend) * base_map.get(stat, 0.0) + blend * w
        # B4: move the offensive weights toward what this god's own scaling
        # coefficients say. Defensive stats keep their role weight — nothing
        # here can price a stat that adds no damage.
        dmg_blend = eff_weights.get("damage_fit_blend", 0.0)
        if dmg_blend:
            base_map = damage_value.blend_stat_values(god, base_map, dmg_blend)

    # Magnitude reference for the fit term, computed once over the whole pool.
    reference = stat_reference(items) if eff_weights.get("magnitude_fit", False) else None

    # Filtering here, at the single point every archetype's rows come from,
    # keeps an excluded item out of the core, the flex slots, the situational
    # swaps and the underrated list at once — none of those can reintroduce a
    # name that never entered `rows`.
    excluded = profile.get("excluded_items") or frozenset()

    rows = []
    for item in items:
        if item["name"] in excluded:
            continue
        if not is_buildable(item, god):
            continue
        if (not profile.get("bypass_damage_filter")
                and not passes_damage_filter(item, god, eff_weights)):
            continue
        eff = efficiency_scores_map.get(item["name"], {}).get("score", 0.5)
        row = signal_score(item, god, god_build, eff, eff_weights,
                           tags_map.get(item["name"], []), stat_overlay, tag_bonus,
                           base_map=base_map, stat_reference=reference)
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
    type, whose match_any (or null=any) intersects the god's token set, and
    whose `requires_scaling` thresholds the god's own kit actually meets.

    `requires_scaling` {stat: min_weight} is what keeps the off-type builds
    honest. A Strength build on a magical god is a real option for Sol, whose
    abilities scale 1.00 on Strength, and nonsense for Scylla, who scales 0.28.
    Gating on the god's measured coefficients rather than on a role label means
    the tab appears exactly where the kit supports it — and it is why Chiron
    gets no Intelligence build despite Chiron Mid being a thing people try: his
    kit scales 0.05 on Intelligence, so the model would be lying to offer it.
    """
    out = []
    for name, f in (weights.get("flavors") or {}).items():
        dts = f.get("damage_types")
        if dts and god.get("damage_type") not in dts:
            continue
        match_any = f.get("match_any")
        if match_any and not (_god_tokens(god) & set(match_any)):
            continue
        needs = f.get("requires_scaling")
        if needs:
            measured = damage_value.stat_weights(god)
            if not measured or any(measured.get(stat, 0.0) < floor
                                   for stat, floor in needs.items()):
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
