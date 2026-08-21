"""What a point of a stat is actually worth to a specific god. (B4/B5)

The precision problem this exists to fix, stated exactly: `god_fit_score` asked
whether an item *has* a stat, threw the magnitude away, and weighted the answer
by a role table. So an item with 5 Strength and one with 80 scored identically,
and every Mid-laner valued Intelligence the same regardless of whether their
abilities scaled 90% off it or 20%.

Both halves are now derived from the god's own scraped coefficients:

  MAGNITUDE  an item contributes its actual numbers
  PER-GOD    weighted by how much damage one more point of that stat adds to
             THIS god's kit, computed from the scaling lines the wiki prints

The arithmetic underneath is `combat`, calibrated against the game to the digit
(`data/_combat_observations.yaml`), so "damage" here means damage rather than a
weighting dressed up as one.

MEASURED RESULT, AND IT IS NEGATIVE. The plan called magnitude-aware fit "the
biggest single precision win". It is not. Every variant was measured against
`validate.compute`, the same gate that arbitrates everything else here, and
every one was worse than the presence-based fit it replaced:

    fit signal                              coverage   win-weighted
    role/kit presence (shipped)                48.4%         50.6%
    + magnitude                                44.9%         46.9%
    + per-god damage weights                   47.1%         49.2%
    + both                                     44.7%         46.9%
    B5 damage gain as the fit signal           23.6%         25.1%

So both halves ship OFF (`magnitude_fit`, `damage_fit_blend`). The code is here
because the measurement is worth keeping and because the same arithmetic is
what the draft needs; it is not here because it improved anything.

READ THAT TABLE THROUGH docs/STATE.md SECTION 1. Every row of it is
`validate.compute`, whose targets are also model inputs. `damage_fit_blend` was
swept against the leakage-free splits for the first time on 2026-08-21 and the
SIGN REVERSES: every setting from 0.05 to 0.75 beats control on both splits
(probe 38.7% -> 39.8% at 0.75), and not one paired CI excludes zero on either.
It stays at 0.0 because nothing clears the noise, not because it is harmful.
Sweep, paired CIs and core churn under `damage_fit_blend` in `_weights.yaml`.

Two explanations, both testable, neither confirmed:

  * MAGNITUDE DOUBLE-COUNTS. Fit is meant to answer "does this god want this
    kind of item". How MUCH of a stat an item carries is already priced by the
    gold model, so making fit proportional to it says the same thing twice and
    crowds out the categorical judgement fit exists to make.
  * DAMAGE GAIN CANNOT PRICE DEFENCE. As a fit signal it collapses because
    every protection and health item scores zero, so guardians and supports get
    incoherent builds. That is structural, not a tuning failure — which is why
    the number is halved rather than nudged.

The honest reading of the last row is that a damage model belongs where a
TARGET is known. `item_damage_gain` reverses the ranking of an item depending
on who you are hitting, and the base score has nobody to hit. The draft does.

WHAT THIS DELIBERATELY DOES NOT DO. It values offence only. Protections, health
and the rest add no damage, and pretending a damage model prices them would be
worse than admitting it doesn't — those keep the role table, which is what a
role table is actually good at. `blend_stat_values` is where the two meet.

KNOWN LIMITS, all inherited and all disclosed on the method page:
  * NEITHER PATH OUT OF THIS MODULE HAS A CLOCK BY DEFAULT.
    `marginal_damage_per_stat` counts one mean swing against a whole ability
    rotation and `item_damage_gain` does the same, so both mixes are
    declarations. `item_damage_gain` can be put on `combat`'s calibrated clock
    with `per_second`; it was measured on 2026-08-21 and ships off, for reasons
    that are structural rather than tunable — see the docstring there and
    register entry 12
  * item passives are prose we extract nothing from, so a passive-heavy item is
    valued at its stat line alone
  * 240 of 513 abilities carry both a rank list and a scaling line; the rest
    contribute nothing here, and a god with fewer than `min_abilities` usable
    ones falls back to the role table entirely
  * damage-over-time tick counts and durations exist only as prose, so a DoT is
    counted as its listed damage once
"""
import re

from smite import combat

# "Damage: 95 | 165 | 235" and its many labelled variants (Initial Damage,
# Explosion Damage, Damage Per Tick, ...). The label is not load-bearing; what
# matters is that the line states a per-rank damage number.
_RANKS = re.compile(r"^[A-Za-z ]*Damage[A-Za-z ]*:\s*([\d.]+(?:\s*\|\s*[\d.]+)*)\s*$")
_SCALING = re.compile(r"([\d.]+)%\s+(Strength|Intelligence|Attack Damage)")

# Stats that add damage and therefore have a defensible per-point value here.
# Anything absent from this set is left to the role table on purpose.
OFFENSIVE = ("Strength", "Intelligence", "Attack Damage")


def ability_damage_components(god):
    """Every ability that states both a per-rank damage number and a scaling
    line, as `{name, ranks, scaling, damage_type, is_ultimate}`.

    An ability missing either is skipped rather than half-counted: a rank list
    with no scaling would look like a flat nuke no stat improves, which would
    drag the god's valuation toward zero for reasons that are an artefact of
    the scrape rather than the kit.
    """
    out = []
    for ability in god.get("abilities") or []:
        slot = ability.get("slot") or ""
        if "Basic Attack" in slot:
            continue
        ranks = scaling = None
        for line in ability.get("details") or []:
            line = line.strip()
            match = _RANKS.match(line)
            if match and ranks is None:
                ranks = [float(x) for x in match.group(1).split("|")]
            elif line.startswith("Damage Scaling:"):
                scaling = {stat: float(pct) / 100
                           for pct, stat in _SCALING.findall(line)}
        if ranks and scaling:
            out.append({"name": ability.get("name"), "ranks": ranks,
                        "scaling": scaling,
                        "damage_type": ability.get("damage_type"),
                        "is_ultimate": "Ultimate" in slot})
    return out


def marginal_damage_per_stat(god, rank=1):
    """`{stat: extra raw damage from one more point}` for this god's kit.

    Pure coefficient arithmetic: one more point of Strength adds its scaling
    ratio to every ability that scales on Strength, plus the basic attack's
    own ratio. No rank values enter — a flat nuke does not change what a point
    of a stat is worth, only what the ability is worth.

    The basic attack counts once at the chain's mean multiplier. Its
    multipliers apply to swing time as well as damage, so the mean is the
    honest per-swing figure rather than the first hit.
    """
    values = {}
    for component in ability_damage_components(god):
        for stat, ratio in component["scaling"].items():
            values[stat] = values.get(stat, 0.0) + ratio

    chain = combat.attack_chain_multipliers(god)
    mean_swing = sum(chain) / len(chain) if chain else 1.0
    basic = _basic_attack_scaling(god)
    for stat, ratio in basic.items():
        values[stat] = values.get(stat, 0.0) + ratio * mean_swing
    return values


def _basic_attack_scaling(god):
    """The god's own basic-attack ratios, or the roster default."""
    for ability in god.get("abilities") or []:
        if "Basic Attack" not in (ability.get("slot") or ""):
            continue
        for line in ability.get("details") or []:
            if line.strip().startswith("Damage Scaling:"):
                found = {stat: float(pct) / 100
                         for pct, stat in _SCALING.findall(line)}
                if found:
                    return found
    return dict(combat.DEFAULT_ATTACK_SCALING)


def usable_ability_count(god):
    return len(ability_damage_components(god))


def stat_weights(god, min_abilities=2):
    """Per-god offensive stat weights in [0,1], normalised to the largest.

    Returns `{}` when the god's kit did not parse well enough to support a
    valuation — 13 of 87 gods, mostly stance gods whose second form scrapes
    as a separate page we never fetch. An empty dict means "use the role
    table", which is an honest fallback rather than a fabricated profile.
    """
    if usable_ability_count(god) < min_abilities:
        return {}
    raw = marginal_damage_per_stat(god)
    offensive = {s: v for s, v in raw.items() if s in OFFENSIVE and v > 0}
    if not offensive:
        return {}
    top = max(offensive.values())
    return {s: v / top for s, v in offensive.items()}


def blend_stat_values(god, role_map, blend=0.5, min_abilities=2):
    """Role table with the god's measured offensive weights blended over it.

    Offensive stats move toward what this god's coefficients actually say;
    everything else — protections, health, cooldown rate — keeps its role
    weight untouched, because no part of this module can price a stat that
    adds no damage.

    `blend` 0 is the old behaviour exactly, 1 ignores the role table for
    offensive stats. It is a weights-file knob because the right value is an
    empirical question, and the answer is whatever `validate.compute` says.
    """
    measured = stat_weights(god, min_abilities)
    if not measured or blend <= 0:
        return dict(role_map)

    out = dict(role_map)
    for stat, weight in measured.items():
        current = role_map.get(stat, 0.0)
        # Scale the measured weight to the role map's own magnitude so the two
        # remain commensurable — this is a re-weighting, not a re-scaling.
        reference = max(role_map.values()) if role_map else 1.0
        out[stat] = (1 - blend) * current + blend * (weight * reference)
    return out


def item_damage_gain(god, item, target_protection, level=1, rank_index=0,
                     per_second=False):
    """B5: extra damage this item buys against a target, over one ability
    rotation plus one basic attack — or per SECOND, with `per_second`.

    The number a build comparison actually wants. Penetration is valued
    correctly against a high-protection target and barely at all against a
    squishy one; raw power is the other way round. A per-stat weighting cannot
    express that at all, because the answer depends on who you are hitting.

    THE BASIC ATTACK IS PART OF THE ROTATION (2026-08-21). It was not, and the
    omission was structural rather than incidental: `ability_damage_components`
    opens by skipping the Basic Attack slot, so every stat that only reaches a
    basic attack contributed exactly zero to the one damage path that reaches a
    recommendation. That is 12 Attack Damage items and 10 Critical Chance items
    scoring 0.0 by construction, on a roster where 84 of 89 basic attacks scale
    100% off Attack Damage. Medusa is the worked case: a Carry whose community
    build is Tyrfing / Odysseus' Bow / Silverbranch Bow / Riptalon /
    The Executioner / Manchu Bow, three of which carry Attack Damage and were
    unpriced here.

    THE UNIT IS A CHOICE AND `per_second` IS IT. One rotation and one swing are
    both natural units and neither converts to the other without a clock, so
    with `per_second` False the ratio below is 1:1 BY DECLARATION and every
    consequence of the ratio — how an attack-speed item compares to a cooldown
    item — is unmodelled. With it True each channel gets its own clock:
    ability damage x `combat.casts_per_second` off the scraped cooldown, basic
    damage x `combat.attacks_per_second` off the scraped base attack speed.
    Attack Speed (34 items) and Cooldown Rate (34 items) buy modelled damage
    for the first time anywhere in this repo, and the mix stops being a
    declaration.

    Per gold was the third candidate and is refused. `efficiency` IS the
    per-gold model, and `build_index._god_item_damage` normalises each column
    against its own best item anyway, so dividing by cost would re-inject the
    gold model into the one signal whose job is to say something gold cannot.

    PER SECOND HAS A KNOWN BIAS AND IT IS NOT A TUNING PROBLEM. It lets a god
    cast every ability off cooldown AND swing at full rate in the same second.
    Nothing here has cast times, so neither channel is charged for the other's,
    and the share of marginal power landing in the basic attack goes (median,
    by role, measured 2026-08-21 on the god's own damage stat):

        role      per rotation   per second
        Carry           34.2%        89.3%
        Jungle          35.1%        92.5%
        Solo            32.6%        90.2%
        Support         19.0%        78.8%
        Mid             11.7%        60.5%

    89% for a Carry is the thing this was built for. **Ymir at 61% basic
    attacks and Agni at 71% are the reductio** — the clock is right and the
    uptime assumption is wrong. Correcting it needs a per-god casting/swinging
    time-share that no source this repo has can supply, and inventing one would
    put an unsourced constant in the module whose whole discipline is that
    constants carry evidence tiers. So the bias is disclosed rather than
    patched, and it is why the switch is a switch. See `damage_per_second` in
    `_weights.yaml` for what it measured.

    The swing is taken at the chain's MEAN multiplier, for the reason
    `marginal_damage_per_stat` takes it there: the multipliers apply to swing
    time as well as damage, so the mean is the honest per-swing figure and the
    sum would hand a three-hit-chain god 3x the basic-attack weight of a
    single-swing god for a chain that also takes 3x as long.

    Critical Chance enters here and only here. It multiplies the whole swing,
    base Attack Power included, so it is the one term whose value depends on
    `level` — which is why `level` finally reaches the arithmetic instead of
    being an accepted-and-ignored argument.

    Returns 0.0 for a god whose kit did not parse — never a fabricated figure.
    The guard is on the ABILITIES still, so exactly the same gods get a figure
    as before; a basic-attack-only valuation for a god whose kit we could not
    read would be a new claim, not a better one.
    """
    components = ability_damage_components(god)
    if not components:
        return 0.0
    if per_second:
        components = [c for c in components if _base_cooldown(god, c, rank_index)]
        if not components:
            return 0.0

    stats = _item_stats(item)
    flat_pen = stats.get("Penetration", 0.0)
    pct_pen = stats.get("Penetration %", 0.0) / 100.0
    cdr = stats.get("Cooldown Rate", 0.0) if per_second else 0.0

    before = after = 0.0
    for component in components:
        rank = component["ranks"][min(rank_index, len(component["ranks"]) - 1)]
        base = combat.ability_damage(rank, component["scaling"], {})
        gained = combat.ability_damage(rank, component["scaling"], stats)
        hit_before = combat.damage_dealt(base, target_protection)
        hit_after = combat.damage_dealt(gained, target_protection,
                                        flat_pen=flat_pen, pct_pen=pct_pen)
        if per_second:
            cooldown = _base_cooldown(god, component, rank_index)
            hit_before *= combat.casts_per_second(cooldown)
            hit_after *= combat.casts_per_second(cooldown, cdr)
        before += hit_before
        after += hit_after

    base_hit, gained_hit = _basic_attack_pair(god, stats, level)
    crit = min(stats.get("Critical Chance %", 0.0), 100.0) / 100.0
    if per_second:
        rate = _base_attack_speed(god)
        before += combat.attack_dps(base_hit, target_protection, rate)
        after += combat.attack_dps(gained_hit, target_protection, rate,
                                   attack_speed_bonus=stats.get("Attack Speed %", 0.0),
                                   crit_chance=crit,
                                   flat_pen=flat_pen, pct_pen=pct_pen)
    else:
        before += combat.expected_attack_damage(base_hit, target_protection)
        after += combat.expected_attack_damage(gained_hit, target_protection,
                                               crit_chance=crit,
                                               flat_pen=flat_pen, pct_pen=pct_pen)
    return after - before


def _base_cooldown(god, component, rank_index=0):
    """The scraped cooldown of the ability a component came from, or None.

    241 of the 253 abilities that already carry a damage component also carry
    a cooldown; the other 12 are dropped from the per-second valuation rather
    than imputed, which is the same rule `ability_damage_components` applies to
    an ability missing its scaling line. Nine gods lose an ability that way and
    none loses all of them. `before` and `after` walk the same filtered list,
    so the delta is never taken across two different kits.
    """
    for ability in god.get("abilities") or []:
        if ability.get("name") != component["name"]:
            continue
        cooldowns = ability.get("cooldown") or []
        if not cooldowns:
            return None
        return float(cooldowns[min(rank_index, len(cooldowns) - 1)]) or None
    return None


def _base_attack_speed(god):
    """The god's scraped base attack speed, WITHOUT per-level growth.

    The roster's `attack_speed.per_level` reads 1.4 for 49 gods, which cannot
    be a flat rate — that would be 27 swings a second at level 20 — so it is
    a percentage. "Cannot be anything else" is an inference and not a source,
    and applying it would scale the basic channel up against the ability
    channel by ~27% at level 20. That channel is the one `item_damage_gain`
    already over-weights (see the uptime note there), so the conservative read
    is the one taken: base only.
    """
    return float((god.get("base_stats") or {}).get("attack_speed", {}).get("base") or 1.0)


def _basic_attack_pair(god, stats, level):
    """One mean-multiplier swing before and after the item, raw."""
    attack_power = combat.god_attack_power(god, level)
    scaling = _basic_attack_scaling(god)
    chain = combat.attack_chain_multipliers(god)
    mean_swing = sum(chain) / len(chain) if chain else 1.0
    return (combat.attack_damage(attack_power, scaling, {}, mean_swing),
            combat.attack_damage(attack_power, scaling, stats, mean_swing))


def _item_stats(item):
    """`{stat: magnitude}` with percent columns kept distinct, matching the
    gold model's own view of an item — flat and percent Penetration are
    different goods and must not be summed."""
    from smite import efficiency
    return efficiency.item_stat_values(item)
