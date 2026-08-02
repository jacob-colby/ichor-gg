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
             lineage. Treat as a working assumption, not a fact; these are the
             constants an in-game check should target first.

The `PENETRATION` block is entirely INFERRED and it is the load-bearing part
of `effective_protection`. Nothing downstream should be shipped to the site
until it has been checked against real numbers — see `calibrate_report`.
"""

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
# DOCUMENTED, and corroborated MEASURED. The wiki's Deathbringer page states
# "Critical Strikes deal 1.65 times the damage. With Deathbringer this is
# increased to 2 times the damage." Our own scrape of that item independently
# reads "+35% Critical Strike Damage", and 1.65 + 0.35 = 2.00 exactly, which
# is the arithmetic the item was clearly designed around.
#
# The wiki's own Stats page instead says crits "increase your damage by 150%".
# That contradicts the pair above and cannot be reconciled with the +35% item,
# so it is treated as stale wording rather than a competing value. Worth an
# in-game check anyway — it is one screenshot.
CRIT_MULTIPLIER = 1.65

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

# MEASURED. Basic attacks scale off Strength, Intelligence and Attack Damage
# together, and the ratios are per-god: 84 of 89 parsed basic attacks read
# "100% Strength + 20% Intelligence + 100% Attack Damage", and the rest differ
# (one is 60% Strength + 100% Intelligence). These defaults exist only for a
# god whose line failed to parse — prefer the god's own scraped ratios.
DEFAULT_ATTACK_SCALING = {"Strength": 1.00, "Intelligence": 0.20, "Attack Damage": 1.00}


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


def attack_damage(attack_power, scaling, stats):
    """One basic attack before mitigation.

    `scaling` is the god's own ratios (see DEFAULT_ATTACK_SCALING) and `stats`
    the god's current totals. Attack Power is the god's level-scaled base and
    is added flat — it is not itself multiplied by a ratio."""
    return attack_power + sum(ratio * stats.get(stat, 0.0)
                              for stat, ratio in (scaling or {}).items())


def ability_damage(base, scaling, stats):
    """One ability hit before mitigation: its rank value plus each scaling
    ratio applied to the matching stat."""
    return base + sum(ratio * stats.get(stat, 0.0)
                      for stat, ratio in (scaling or {}).items())


def damage_dealt(raw, protection, *, flat_pen=0.0, pct_pen=0.0,
                 flat_reduction=0.0, pct_reduction=0.0,
                 plating=0.0, dampening=0.0, crit=False,
                 crit_multiplier=CRIT_MULTIPLIER):
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
    """
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


# ── Calibration ───────────────────────────────────────────────────────────

def calibrate_report(observations):
    """Compare this model against real in-game numbers.

    `observations` are dicts of `{label, expected, **damage_dealt kwargs}`
    where `expected` is what the game actually showed. Returns per-case error
    and the worst absolute relative error, which is the figure the gate should
    be set on.

    This exists because the penetration block is INFERRED and load-bearing.
    Until someone runs real numbers through it, `combat.py` is a well-sourced
    hypothesis, and nothing that consumes it should reach the site.
    """
    rows = []
    for obs in observations:
        obs = dict(obs)
        label = obs.pop("label", "")
        expected = obs.pop("expected")
        actual = damage_dealt(**obs)
        error = (actual - expected) / expected if expected else float("inf")
        rows.append({"label": label, "expected": expected,
                     "actual": actual, "rel_error": error})
    worst = max((abs(r["rel_error"]) for r in rows), default=0.0)
    return {"cases": rows, "worst_rel_error": worst, "n": len(rows)}
