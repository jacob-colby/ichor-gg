"""SMITE 2 damage arithmetic. Pure functions, no I/O.

B3. Every constant here is sourced, and the source is not uniform in quality,
so each one carries its tier. That distinction is the point of the module: a
number we read off our own scrape is not the same kind of fact as a number a
community guide asserts, and a model that mixes them without saying so invites
a wrong answer that looks authoritative.

  MEASURED   Read from data this repo already scrapes. Checkable offline, at
             any time, by re-running the parser. Highest confidence.

  DOCUMENTED The SMITE 2 wiki states it. Good, but the wiki is community-run
             and its stats page carries no formulas — only prose we had to
             turn into arithmetic.

  INFERRED   Community guides assert it and no primary SMITE 2 source we could
             find states it. Much of that material has visible SMITE 1
             lineage. Treat as a working assumption, not a fact.

  OBSERVED   Measured in the game. Outranks all three above, including when it
             contradicts them — which it has.

Calibrated 2026-08-04 (`data/_combat_observations.yaml`). Mitigation and both
penetration terms reproduce reality EXACTLY — the game floors its displayed
damage, so a floored prediction can be compared to the integer on screen with
no tolerance at all, and all four readings match. The penetration block,
previously the load-bearing guess here, is confirmed. The same session
overturned the crit multiplier: two sources agreed on 1.65 and the game says
1.5. That is the reason for the OBSERVED tier and the reason it wins.

Nine readings, every one reproduced exactly: mitigation, both penetration
terms, crit, and basic attacks across melee/ranged and physical/magical.

Still unverified: the penetration CAPS (40% / 50), which need a build stacking
five or six penetration items to exercise, and Deathbringer's crit bonus, which
should reach 2.02x if it multiplies and 1.85x if it adds. And see
`ATTACK_POWER_SCALE` — it is fitted rather than derived, and a level-1 reading
cannot tell a constant ratio from a wrong per-level slope.
"""

import math
import re

# Matches "Attacks in order of 1, 0.75, 1.5x damage and swing time".
_CHAIN = re.compile(r"[Aa]ttacks in order of\s+([\d.,\s]+?)x\s+damage")


# ── Protections ───────────────────────────────────────────────────────────
# DOCUMENTED. The wiki states it as effective health rather than as a damage
# multiplier: "For every 1 Physical Protection, you are able to withstand 1%
# of Physical Damage dealt to you", and EHP = HP x (1 + 0.01 x Protection).
# Those are the same statement — inverting the EHP form gives the multiplier
# below — and they agree with the long-standing SMITE 1 formula, which is why
# this one is treated as solid despite the wiki never printing it.
#
#   mitigation(prot) = 100 / (100 + prot)
#
# 100 protection halves incoming damage. Negative protection amplifies it, and
# the game does not let penetration push a target below zero, so the caller is
# expected to clamp — `effective_protection` does.

# ── Penetration ───────────────────────────────────────────────────────────
# INFERRED, all of it. Applied in a fixed order, reductions before penetration
# and percentage before flat within each:
#
#   effective = (prot * (1 - pct_reduction) - flat_reduction)
#                     * (1 - pct_pen) - flat_pen
#
# Caps: percentage penetration 40%, flat penetration 50. Items can exceed them
# and the excess is said to do nothing. Both caps are reachable with our real
# item pool — six flat-penetration items total 60, and three percentage items
# total 40% — so if the caps are real they bind in ordinary builds, and if
# they are wrong the error lands on exactly the builds that stack penetration.
PCT_PEN_CAP = 0.40
FLAT_PEN_CAP = 50.0

# ── Critical strikes ──────────────────────────────────────────────────────
# OBSERVED. Measured in game on 2026-08-04, and it overturned what the sources
# said. Thanatos's three-hit chain gave 58 / 43 / 87 normal and 87 / 65 / 131
# critical against the same target:
#
#     87/58 = 1.500     65/43 = 1.512     131/87 = 1.506
#
# Three independent ratios on 1.5, with the drift explained by the game
# truncating its displayed numbers — the 0.75x hit is really 43.5 and shows 43,
# so 65/43 reads high while 65/43.5 = 1.494.
#
# This was 1.65 until that measurement. The wiki's Deathbringer page states
# "Critical Strikes deal 1.65 times the damage. With Deathbringer this is
# increased to 2 times", and our scrape of the item reads "+35% Critical Strike
# Damage" — 1.65 + 0.35 = 2.00 exactly, which looked like decisive
# corroboration and was not. The wiki's own Stats page said crits "increase
# your damage by 150%" and that turns out to be the accurate one.
#
# The +35% item still reaches 2x, just multiplicatively: 1.5 x 1.35 = 2.025.
# So the item text and the observed base are consistent and it is the 1.65
# figure that is wrong. Untested, and the cheapest next reading: Rage plus
# Deathbringer crits at 2.02x if the bonus multiplies, 1.85x if it adds.
CRIT_MULTIPLIER = 1.50
DEATHBRINGER_CRIT_BONUS = 0.35

# ── Flat damage-type reductions (SMITE 2 only; no SMITE 1 equivalent) ─────
# DOCUMENTED. Plating reduces damage from Attacks, Dampening from Abilities,
# 1% per point, each capped at 35. These are separate from protections and
# apply on top of them. Our item pool carries Plating on 7 items and Dampening
# on 6, and the gold model has been pricing both with no idea they are capped.
PLATING_CAP = 35.0
DAMPENING_CAP = 35.0

# DOCUMENTED. Tenacity caps at 50% from items; Pathfinding runs at 33%
# effectiveness in combat; lifesteal at 33% against minions. None of these
# feed damage, but they are the reason three of our priced stats are worth
# less than their raw magnitude suggests.
TENACITY_CAP = 0.50
PATHFINDING_COMBAT_SCALE = 0.33
LIFESTEAL_MINION_SCALE = 0.33

# ── Echo ──────────────────────────────────────────────────────────────────
# The shares below are DOCUMENTED: "Echo as a stat gives 30% of your Ability's
# damage as bonus damage on Abilities, and 15% ... on Ultimate Abilities."
#
# That the stat's magnitude is a CHANCE is INFERRED, because the wiki sentence
# alone would make the number meaningless — our items grant Echo 20, 25 and
# 30, and a flat "+30% ability damage" would be identical on all three. Three
# item texts we scrape ourselves say otherwise:
#
#   The Cosmic Horror  "Echo > Cooldown Rate: +20% Echo Damage"  — Echo Damage
#                      is its own damage instance, so something fires again
#   Omen Drum          "...15% of all Ability Damage you dealt is echoed..."
#   Damaru             "Echo: +8% Attack Damage for 5s"  — a trigger, so an
#                      Echo is an event rather than a standing bonus
#
# So Echo is read as a percentage chance for a landed ability to repeat for a
# fraction of its damage. Expected value is therefore linear in the stat,
# which is all a build comparison needs — the variance only matters to a
# single cast. One practice-range observation settles it: repeat an ability
# with an Echo item and see whether the damage is bimodal or uniformly higher.
ECHO_ABILITY_SHARE = 0.30
ECHO_ULTIMATE_SHARE = 0.15

# ── Cooldown rate ─────────────────────────────────────────────────────────
# DOCUMENTED, and quotable: "Cooldown Rate reduces the duration of that
# Cooldown, with every 1 Cooldown Rate allowing you to use abilities 1% more
# often." That is the same shape as protections — 100 / (100 + x) — and it is
# self-limiting, which is why no cap is needed and why the game can promise
# you will never reach zero cooldown. 25 of our items carry the stat and
# nothing in the model could see it before now.
#
# Note this is a RATE, not SMITE 1's flat cooldown reduction: 100 Cooldown
# Rate is twice as many casts, not a 100% reduction.

# MEASURED. Basic attacks scale off Strength, Intelligence and Attack Damage
# together, and the ratios are per-god: 84 of 89 parsed basic attacks read
# "100% Strength + 20% Intelligence + 100% Attack Damage", and the rest differ
# (one is 60% Strength + 100% Intelligence). These defaults exist only for a
# god whose line failed to parse — prefer the god's own scraped ratios.
DEFAULT_ATTACK_SCALING = {"Strength": 1.00, "Intelligence": 0.20, "Attack Damage": 1.00}

# OBSERVED, and unexplained. A basic attack does about 0.81x the Attack Power
# the wiki lists, and the mechanism behind that is not in any source we have.
#
# Measured 2026-08-04 across three gods against a level-1 Kukulkan, which is
# what rules out the obvious explanations — it holds for melee and ranged, and
# for physical and magical:
#
#   god        scraped AP   shown   implied ratio
#   Thanatos        47.76      32   0.8035 - 0.8117
#   Neith           44.40      30   0.7938 - 0.8202
#   Ymir            44.59      28   0.7999 - 0.8284
#
# The intervals are wide because the game floors its display, but they
# intersect at 0.8035 - 0.8117, which excludes a clean 0.80. Requiring all
# eleven readings taken that session — three chain hits with no items, three
# with Rage, three crits, and the two single-swing gods — narrows it to
# 0.8076 - 0.8117. 0.81 is the round value inside that and reproduces every
# one; it is a fitted constant, not a derived one.
#
# Item Strength is NOT scaled: Rage's 30 Strength added 29.6-30.5 raw, so the
# scraped "100% Strength" is exact. Whatever this is, it applies to the base
# alone. Worth revisiting if a source ever explains it, and worth re-measuring
# at a higher level — a constant ratio and a wrong per-level slope look
# identical from level 1.
ATTACK_POWER_SCALE = 0.81


def mitigation(protection):
    """Damage multiplier from a protection value. 0 -> 1.0, 100 -> 0.5.

    Negative protection amplifies damage, which is what the formula says and
    what the game does for protection *debuffs*; penetration is clamped
    separately, in `effective_protection`, because that is where the game
    clamps it."""
    return 100.0 / (100.0 + protection)


def effective_protection(protection, flat_pen=0.0, pct_pen=0.0,
                         flat_reduction=0.0, pct_reduction=0.0):
    """What the target's protection is worth after shred and penetration.

    Order is reductions then penetration, percentage before flat within each.
    Penetration is capped (`PCT_PEN_CAP`, `FLAT_PEN_CAP`) and the result is
    clamped at zero: penetration takes protection to nothing and no further,
    it does not turn into bonus damage.

    Reductions are NOT capped here. They come from abilities and item passives
    rather than from a penetration stat, and no source we have puts a cap on
    them — assuming one would invent a rule.
    """
    after_reduction = protection * (1.0 - pct_reduction) - flat_reduction
    after_pct = after_reduction * (1.0 - min(pct_pen, PCT_PEN_CAP))
    return max(0.0, after_pct - min(flat_pen, FLAT_PEN_CAP))


def flat_reduction_multiplier(points, cap):
    """Plating / Dampening: 1% per point, capped. Returns a damage multiplier."""
    return 1.0 - min(max(points, 0.0), cap) / 100.0


def effective_health(health, protection):
    """The wiki's own form: HP x (1 + 0.01 x protection). Equals
    `health / mitigation(protection)`, which is the invariant worth holding."""
    return health * (1.0 + protection / 100.0)


def attack_chain_multipliers(god):
    """A god's basic-attack chain, as per-swing damage multipliers.

    OBSERVED, then found already scraped. Basic attacks are not one repeated
    swing: Thanatos's detail line reads "Has a 3 hit chain. Attacks in order of
    1, 0.75, 1.5x damage and swing time", and his measured hits were 58 / 43 /
    87 — exactly 1 : 0.75 : 1.5 off a 58 base.

    This matters for any comparison involving attack speed. A chain averaging
    1.083x per swing is not the same as three 1x swings, and the multipliers
    apply to swing TIME as well as damage, so a chain god's real DPS is not
    `hit x rate` with either the first hit or the mean. Returns [1.0] for a god
    with no parsed chain, which is the honest default rather than a guess.
    """
    for a in god.get("abilities") or []:
        if "Basic Attack" not in (a.get("slot") or ""):
            continue
        for line in a.get("details") or []:
            m = _CHAIN.search(line)
            if m:
                return [float(x) for x in re.findall(r"[\d.]+", m.group(1))]
    return [1.0]


def attack_damage(attack_power, scaling, stats, chain_multiplier=1.0):
    """One basic attack before mitigation.

    `attack_power` is the god's SCRAPED value; `ATTACK_POWER_SCALE` is applied
    here, so callers pass what the data holds and do not have to know about the
    correction. `scaling` is the god's own ratios (see DEFAULT_ATTACK_SCALING),
    `stats` its current totals, and `chain_multiplier` the swing's place in the
    god's chain if it has one.

    Item power is added unscaled — measured, not assumed: Rage's 30 Strength
    accounted for 29.6-30.5 raw damage, so the scraped 100% Strength scaling is
    exact and the correction belongs to the base alone.
    """
    base = attack_power * ATTACK_POWER_SCALE
    base += sum(ratio * stats.get(stat, 0.0)
                for stat, ratio in (scaling or {}).items())
    return base * chain_multiplier


def ability_damage(base, scaling, stats):
    """One ability hit before mitigation: its rank value plus each scaling
    ratio applied to the matching stat."""
    return base + sum(ratio * stats.get(stat, 0.0)
                      for stat, ratio in (scaling or {}).items())


def echo_multiplier(echo, ultimate=False):
    """Expected damage multiplier from Echo, for one ability.

    `echo` is the stat's points, read as a percentage chance. A repeat is
    worth `ECHO_ABILITY_SHARE` of the ability (half that on an ultimate), so
    expectation is 1 + chance x share — linear, and linear is what a build
    comparison wants. 30 Echo is about +9% ability damage, +4.5% on ultimates.
    """
    share = ECHO_ULTIMATE_SHARE if ultimate else ECHO_ABILITY_SHARE
    return 1.0 + min(max(echo, 0.0), 100.0) / 100.0 * share


def cooldown_multiplier(cooldown_rate):
    """Cooldown duration multiplier. 100 / (100 + rate) — the same curve as
    mitigation, and self-limiting for the same reason: it approaches zero
    without reaching it."""
    return 100.0 / (100.0 + max(cooldown_rate, -99.0))


def casts_per_second(base_cooldown, cooldown_rate=0.0):
    """How often an ability is actually available. The inverse of its real
    cooldown, so an ability-damage comparison can weigh a long cooldown nuke
    against a short one instead of pretending both land once."""
    cd = base_cooldown * cooldown_multiplier(cooldown_rate)
    return 1.0 / cd if cd > 0 else 0.0


def attacks_per_second(base_attack_speed, pct_bonus=0.0):
    """Basic attacks per second. Gods carry a base near 1.0 and items grant a
    percentage on top.

    No cap is applied. SMITE 1 capped attack speed at 2.5 and it would be easy
    to carry that over, but no SMITE 2 source we found states a cap and
    inventing one would silently flatten every attack-speed build. If a cap
    turns up, it belongs here.
    """
    return max(0.0, base_attack_speed * (1.0 + pct_bonus / 100.0))


def lifesteal_healing(damage_dealt_amount, lifesteal, vs_minion=False):
    """Healing returned from damage. Against minions it is worth a third —
    DOCUMENTED, and the reason lifesteal is worth less in a farming build than
    its raw percentage suggests."""
    scale = LIFESTEAL_MINION_SCALE if vs_minion else 1.0
    return damage_dealt_amount * (lifesteal / 100.0) * scale


def damage_dealt(raw, protection, *, flat_pen=0.0, pct_pen=0.0,
                 flat_reduction=0.0, pct_reduction=0.0,
                 plating=0.0, dampening=0.0, crit=False,
                 crit_multiplier=CRIT_MULTIPLIER, true_damage=False):
    """Raw damage through a target's defences.

    Composition order — protections first, then the flat damage-type
    reductions, then crit — is itself INFERRED. No source we found states
    where Plating and Dampening sit relative to protections, only that they
    exist and what they do. Multiplicative composition is the assumption most
    consistent with how the wiki describes them ("withstand 1% ... per each
    instance of damage"), and it is a thing calibration should confirm.

    `plating` and `dampening` are mutually exclusive in practice: an Attack is
    reduced by Plating, an Ability by Dampening. Passing both is allowed and
    both apply, so a caller modelling a hybrid hit does not have to pick.

    `true_damage` skips protections entirely. Several real effects deal it
    (Sundering Echo's active, among others) and running those through
    mitigation would be plainly wrong. Whether true damage also ignores
    Plating and Dampening is NOT something any source we found addresses, so
    it is modelled as bypassing protections only — the narrower claim. Flagged
    rather than assumed, and worth checking alongside penetration.
    """
    if true_damage:
        out = float(raw)
    else:
        prot = effective_protection(protection, flat_pen, pct_pen,
                                    flat_reduction, pct_reduction)
        out = raw * mitigation(prot)
    out *= flat_reduction_multiplier(plating, PLATING_CAP)
    out *= flat_reduction_multiplier(dampening, DAMPENING_CAP)
    return out * (crit_multiplier if crit else 1.0)


def expected_attack_damage(raw, protection, crit_chance=0.0,
                           crit_multiplier=CRIT_MULTIPLIER, **kwargs):
    """Damage per attack averaged over crit chance — the number that belongs
    in an item comparison, since no build is evaluated on a single swing."""
    p = min(max(crit_chance, 0.0), 1.0)
    normal = damage_dealt(raw, protection, crit=False, **kwargs)
    return normal * (1.0 - p) + normal * crit_multiplier * p


def expected_ability_damage(raw, protection, echo=0.0, ultimate=False, **kwargs):
    """One ability through the target's defences, including Echo's expected
    repeat. The counterpart to `expected_attack_damage` — an ability build and
    an auto-attack build have to be comparable on the same footing."""
    return damage_dealt(raw, protection, **kwargs) * echo_multiplier(echo, ultimate)


def attack_dps(raw, protection, base_attack_speed, attack_speed_bonus=0.0,
               crit_chance=0.0, **kwargs):
    """Sustained basic-attack damage per second.

    This is the term that makes an attack-speed item comparable to a raw-power
    one. Per-hit damage alone cannot do it: a build that swings twice as often
    for two-thirds the damage is stronger, and a model that only sees the hit
    would call it weaker.
    """
    per_hit = expected_attack_damage(raw, protection, crit_chance=crit_chance, **kwargs)
    return per_hit * attacks_per_second(base_attack_speed, attack_speed_bonus)


# ── Calibration ───────────────────────────────────────────────────────────

def displayed(value):
    """What the game prints for a damage value: the floor, not a rounding.

    OBSERVED, 2026-08-04, and it is floor in both directions: a predicted 94.6
    showed as 94 where rounding would have given 95, and Thanatos's 0.75x chain
    hit of 43.5 showed 43. His crit of ~130.5 showing 131 looks like a
    counter-example and is not — interval arithmetic on the chain puts the
    underlying value above 131.

    This makes the gate STRICTER, not looser. Comparing a floored prediction
    against the integer on screen admits no slack, where comparing raw floats
    had to tolerate a percent of display noise and would have accepted a model
    genuinely off by that much.
    """
    return math.floor(value)


def calibrate_report(observations):
    """Compare this model against real in-game numbers.

    `observations` are dicts of `{label, expected, **damage_dealt kwargs}`
    where `expected` is what the game actually showed. Returns per-case error
    and the worst absolute relative error, which is the figure the gate should
    be set on.

    An integer `expected` is taken to be a number read off the screen, so the
    model is floored before comparison — see `displayed`. A non-integer is
    taken to be derived and compared directly.
    """
    rows = []
    for obs in observations:
        obs = dict(obs)
        label = obs.pop("label", "")
        expected = obs.pop("expected")
        actual = damage_dealt(**obs)
        # Compare like with like: an integer reading is what the game printed.
        shown = displayed(actual) if float(expected).is_integer() else actual
        error = (shown - expected) / expected if expected else float("inf")
        rows.append({"label": label, "expected": expected, "actual": actual,
                     "shown": shown, "rel_error": error})
    worst = max((abs(r["rel_error"]) for r in rows), default=0.0)
    return {"cases": rows, "worst_rel_error": worst, "n": len(rows)}
