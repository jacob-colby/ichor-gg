"""Point `combat` at a whole build: ours against the community's, per god.

THE ONLY INSTRUMENT HERE THAT CAN SAY "BETTER" RATHER THAN "MORE CONVENTIONAL".
Every other gate in this repo measures agreement with the community —
`validate.compute` is circular (docs/STATE.md §1) and the leakage-free
coverage in `calibrate` asks how many of the community's items we found. Both
go DOWN when a build is genuinely better and unconventional, so neither can
answer "is our build good". `combat.py` can: it is calibrated to 0.0%
worst-case against in-game readings (`calibrate_combat`) and it has never seen
a community build. This module is the first thing to point it at six items at
once.

IT IS A DIAGNOSTIC, NOT A SCORING INPUT. Nothing here is imported by
`scoring`, `assemble`, `recommend` or `build_index`, and nothing here reads a
weight to decide anything. Register §4.4 (docs/STATE.md) is what happens when a
damage measure becomes a fit signal; the output of this module is a report a
human reads, and a test pins the import boundary.

WHAT IT COMPUTES, per god, for the community Conquest core and our meta-free
`model` core — six items, level 20:

  * sustained basic-attack DPS against 70 and 170 protection
  * ability DPS with every ability cast off cooldown, against the same two
  * the same rotation charged ONCE each — the burst — against 0, 70 and 170
  * effective health, physical and magical (`combat.effective_health`)
  * total gold, and each figure per 1000 gold

AND IT JUDGES EACH ROLE ON THAT ROLE'S OWN OBJECTIVE, because one pooled
metric applied to 89 gods hides a defect. Measured 2026-08-21: our `model`
core is tankier than the community's on 18 of 18 Carries while winning damage
on only 12 — the weakest damage record of any role. The identical behaviour is
CORRECT for Support (EHP ahead on 14 of 14, DPS a coin flip with 3 exact
ties), so a single scalar that scores "more EHP is better" cannot tell the two
apart, and the pooled "71 of 89 ahead" is partly an artifact of averaging
roles that do not share a job. `ROLE_OBJECTIVES` names, per role, the quantity
MAXIMISED and the quantity treated as a THRESHOLD, so a reader can disagree
with the choice rather than only with the number.

THE THRESHOLDS DO NOT BIND, AND THAT IS ABOUT US, NOT ABOUT SMITE. A Carry
survival floor and a Mid/Jungle kill threshold were both defined, measured and
kept in the table with their measurement (`threshold_probe`, re-run on every
report): the first separates 0 of 36 builds even against the roster's single
largest burst read at zero protection, the second separates 78 of 78. A burst
here is one cast of every ability with no basic attacks, no item passive, no
follow-up and one target, while effective health is full level-20 health plus
every protection six items carry — an order of magnitude apart. Read it as
"we cannot currently evaluate a threshold". What would change the answer is
named and is not a tuning knob: the register §4.12 clock, or priced passives.

"Ours" is the `model` archetype — efficiency + fit with `win` and `pick`
switched off — because that is the build the model would pick if it had never
seen the community's data, which is the honest counterpart to the community's
own. The blended `core` (the viewer's Balanced tab) is reported alongside it
because it is what ships; in Joust and Arena the two are byte-identical.

THE WORKED EXAMPLE IT REPRODUCES. Medusa, computed by hand on 2026-08-21 and
reproduced here to 0.1 on every figure (`test_build_quality`):

    community 13,750g   Tyrfing · Odysseus' Bow · Silverbranch Bow · Riptalon ·
                        The Executioner · Manchu Bow
    ours      15,400g   Berserker's Shield · Jotunn's Revenge · Nimble Ring ·
                        Death Metal · Rod of Tahuti · Soul Gem

                              basic DPS   ability DPS     TOTAL
      COMMUNITY vs 70 prot       352.8    +    35.9  =   388.6
                vs 170 prot      233.2    +    23.7  =   256.9
      OURS      vs 70 prot       242.4    +    72.4  =   314.8
                vs 170 prot      150.8    +    45.1  =   195.9

Viper Shot contributes nothing to either line, and not by special case: its
scaling line reads `Damage Scaling Per Tick:` and
`damage_value.ability_damage_components` accepts `Damage Scaling:` only, so
the ability has a rank list and no scaling and is skipped — the same rule the
damage model applies everywhere. The hand computation excluded it too.

FOUR PLACES THE ARITHMETIC IS EASY TO GET WRONG, each pinned by a test:

  * attack speed per level is a PERCENT: Medusa's 1.0 base at 1.4/level is
    1.266 at level 20, not 27.6 (`base_attack_speed`)
  * `ATTACK_POWER_SCALE` (0.81) applies to the base only, never to per-level
    growth — `combat.god_attack_power` already does this and is used as is
  * flat and percent penetration are different goods and are never summed;
    `efficiency.item_stat_values` keeps them apart and `damage_dealt` takes
    them as separate kwargs, capped by `effective_protection`
  * a chain god's basic attack is taken at the chain's MEAN multiplier, for
    the reason `damage_value.marginal_damage_per_stat` takes it there: the
    multipliers apply to swing time as well as damage

THE CAVEAT THAT BELONGS ON THE FACE OF THE REPORT, not in a footnote, and the
report prints it before any number. Measured 2026-08-21 (`passive_blind_spot`
re-measures it on every run): of 138 buildable items, 137 carry passive text
and the shipped pricing flags read 13 of them, so ~90% of the pool carries
passive value this arithmetic cannot see, and ~76% of the community's item
slots do. `combat.py` itself reads exactly ONE passive — Deathbringer's +35%
crit damage, measured in game. The bias is not even: by the gold model's own
residual the community pays ~135g more per slot above its stat line than we
do — that premium IS the passive — so a verdict in OUR favour is the one to
distrust. The report says so at the top, and so does every other way out of
this module: `emit` is its only print and its only file write, it puts the
caveat before the body, and `main` measures the blind spot before it can
branch. That is structural because it has to be — the `--god` path, the one
STATE.md §6 recommends, once returned before the blind spot was measured and
printed a DPS table with no caveat at all (2026-08-21). Two tests hold it:
one refuses a print or write anywhere but `emit`, the other drives every
flag the parser knows and refuses a figure before the caveat on any of them.

THE OTHER ASSUMPTIONS, also printed on the report: full ability uptime with no
cast times (register §4.12 — nothing in the scrape has one, so a god casts
everything off cooldown AND swings at full rate in the same second), no relic,
single target, no lifesteal sustain, no crowd control, no wave clear, both
targets at exactly 70 / 170 of the god's own damage type with no Plating or
Dampening, and an ability without a scraped cooldown dropped rather than
imputed (the rule `damage_value._base_cooldown` already applies).

    python -m smite.build_quality                 # write data/Analysis/_build_quality.md
    python -m smite.build_quality --god Medusa    # one god's profile, to stdout
    python -m smite.build_quality --role Carry    # one role's verdict, to stdout
"""
import argparse
import re
import sys
import types
from collections import Counter
from pathlib import Path

import numpy as np

from smite import calibrate, combat, damage_value, efficiency, recommend, scoring

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = REPO_ROOT / "data" / "Analysis" / "_build_quality.md"

#: Level the comparison is taken at — six items is a finished build, and a
#: finished build is a level-20 question.
LEVEL = 20

#: Target protections. 70 is a late-game squishy, 170 a tank; both are of the
#: god's own damage type, with no Plating or Dampening.
TARGETS = (70, 170)

#: Protections the BURST is taken against. 0 is not a target anyone meets — it
#: is there so `threshold_probe` can read a burst at its arithmetic maximum,
#: which is what makes "the threshold does not bind" a statement about the
#: whole range rather than about one choice of target.
BURST_TARGETS = (0,) + TARGETS

#: Our build's archetype. `model` is efficiency + fit with the meta off; `core`
#: is the blended build that ships as the viewer's Balanced tab.
DEFAULT_ARCHETYPE = "model"

# "Cooldown: 12 | 11.5 | 11 | 10.5 | 10 seconds" — the fallback when a god
# note carries the line but not the parsed `cooldown` list.
_COOLDOWN = re.compile(r"^Cooldown:\s*([\d.]+(?:\s*\|\s*[\d.]+)*)\s*seconds?\s*$")

#: The metrics the distribution is reported on, as `(key, label)`. Each has a
#: per-1000-gold twin.
METRICS = (
    ("dps_70", "total DPS vs 70 prot"),
    ("dps_170", "total DPS vs 170 prot"),
    ("ehp_physical", "effective health, physical"),
    ("ehp_magical", "effective health, magical"),
)

#: Role order for every by-role table, then anything unrecognised, sorted.
ROLE_ORDER = ("Carry", "Jungle", "Mid", "Solo", "Support")

#: WHAT EACH ROLE'S BUILD IS FOR. One pooled metric cannot judge five roles
#: that do not share an objective — measured 2026-08-21, our `model` core is
#: tankier than the community's on 18 of 18 Carries while winning damage on 12,
#: which is the same behaviour that is CORRECT for Support (EHP ahead 14 of 14,
#: DPS a coin flip with 3 exact ties). Scoring EHP as "more is better" for a
#: Carry cannot tell those apart, so the pooled "71 of 89 ahead" is partly an
#: artifact of averaging roles with different jobs.
#:
#: Each entry names the quantity that was MAXIMISED and the quantity that was
#: treated as a THRESHOLD, so a reader can disagree with the choice rather than
#: only with the number. `threshold` is None on every role, and that is a
#: measurement rather than a design preference — see `threshold_probe`, which
#: re-runs it on every report.
#:
#: `Support` scores no damage at all. Down-weighting it would still be scoring
#: it, and on 3 of 14 Supports (Ymir, Sylvanus, Xing Tian) the DPS column is
#: identical on both sides to 0.00% because neither build buys damage — the
#: column carries literally zero information there. A wave-clear threshold
#: would need a minion health pool and a clear-time window, neither of which
#: exists in this repo; excluding damage is the honest form of "we cannot
#: price what Support is for". See `UNMEASURABLE`.
ROLE_OBJECTIVES = {
    "Carry": {
        "maximise": ("dps_70/1000g", "sustained DPS per 1000g"),
        "threshold": ("survive one enemy burst rotation", "carry_survival"),
        "because": "a Carry needs enough effective health to live through one "
                   "burst — a floor, not a maximand. Buying more than the floor "
                   "is gold not spent on damage, which is what the pooled metric "
                   "scored as a win.",
    },
    "Mid": {
        "maximise": ("dps_70/1000g", "sustained DPS per 1000g"),
        "threshold": ("rotation burst >= a reference squishy's EHP", "kill_threshold"),
        "because": "a Mid's rotation either kills the squishy or it does not; "
                   "past that the question is how often it comes back.",
    },
    "Jungle": {
        "maximise": ("burst_70/1000g", "rotation burst per 1000g"),
        "threshold": ("rotation burst >= a reference squishy's EHP", "kill_threshold"),
        "because": "same kill threshold as Mid, and past it a gank is priced on "
                   "burst rather than on sustained damage — a Jungler is not "
                   "standing in the fight for the seconds a DPS figure assumes.",
    },
    "Solo": {
        "maximise": ("duel_70", "duel score, EHP x DPS"),
        "threshold": None,
        "because": "not a threshold at all — a RATIO. Their time-to-kill on you "
                   "over yours on them is (EHP / ref DPS) / (ref EHP / DPS), so "
                   "the reference opponent CANCELS in ours-over-theirs and what "
                   "is left is EHP x DPS. A build that doubles effective health "
                   "and halves damage scores exactly 1.00 — neutral, which is "
                   "the case neither scalar describes, and it is a property of "
                   "the algebra rather than of a constant anyone chose.",
    },
    "Support": {
        "maximise": ("ehp_physical/1000g", "effective health per 1000g"),
        "threshold": None,
        "because": "damage is EXCLUDED, not down-weighted. Most of what a "
                   "Support is for is in `UNMEASURABLE`, and its damage column "
                   "is provably empty on 3 of 14 gods.",
    },
}

#: What no arithmetic here reaches, named so a per-role verdict cannot read as
#: though slicing the roster escaped it. Support's real contribution is mostly
#: on this list, which is why its objective excludes damage rather than
#: weighting it small.
UNMEASURABLE = (
    "CC chain duration", "peel", "aura coverage", "wave clear",
    "objective damage", "map tempo",
)


# ── The god at level 20 ───────────────────────────────────────────────────

def level_value(block, level=LEVEL):
    """`base + per_level x (level - 1)` for a scraped base-stat block."""
    block = block or {}
    return float(block.get("base") or 0.0) + float(block.get("per_level") or 0.0) * max(0, level - 1)


def base_attack_speed(god, level=LEVEL):
    """Attacks per second before items.

    `per_level` is a PERCENT of base — 1.4 reads as +1.4% per level, so a 1.0
    base is 1.266 at level 20. The roster carries 1.4 on 49 gods, which as a
    flat rate would be 27 swings a second; `damage_value._base_attack_speed`
    declined to apply it for the draft and said why. Here the level is the
    whole point of the comparison, so it is applied, as a percent.
    """
    block = (god.get("base_stats") or {}).get("attack_speed") or {}
    base = float(block.get("base") or 1.0)
    per_level = float(block.get("per_level") or 0.0)
    return base * (1.0 + per_level * max(0, level - 1) / 100.0)


def _cooldown_at_max(god, component):
    """The last-rank cooldown of the ability a component came from, or None.

    Reads the parsed `cooldown` list first and falls back to the
    `Cooldown: a | b | c seconds` detail line. None means the ability is
    dropped from the rotation, never imputed — the rule
    `damage_value._base_cooldown` already applies.
    """
    for ability in god.get("abilities") or []:
        if ability.get("name") != component["name"]:
            continue
        cooldowns = ability.get("cooldown") or []
        if cooldowns:
            return float(cooldowns[-1]) or None
        for line in ability.get("details") or []:
            m = _COOLDOWN.match(line.strip())
            if m:
                values = [float(x) for x in m.group(1).split("|")]
                return values[-1] or None
        return None
    return None


def ability_rotation(god):
    """`(counted, dropped)`: every ability with a damage component and a
    cooldown, at its LAST rank, and the names of those with no cooldown."""
    counted, dropped = [], []
    for component in damage_value.ability_damage_components(god):
        cooldown = _cooldown_at_max(god, component)
        if not cooldown:
            dropped.append(component["name"])
            continue
        counted.append({
            "name": component["name"],
            "base": component["ranks"][-1],
            "scaling": component["scaling"],
            "cooldown": cooldown,
            "is_ultimate": component["is_ultimate"],
        })
    return counted, dropped


# ── The build ─────────────────────────────────────────────────────────────

def build_totals(names, items_by_name):
    """`(stat totals, gold)` for a list of item names, through
    `efficiency.item_stat_values` so flat and percent columns stay apart.

    Raises KeyError on an item the pool does not know: a silently-skipped item
    would read as a cheaper, weaker build and nobody would see why."""
    totals, cost = {}, 0.0
    for name in names:
        item = items_by_name[name]
        cost += float(item.get("cost") or 0.0)
        for key, value in efficiency.item_stat_values(item).items():
            totals[key] = totals.get(key, 0.0) + value
    return totals, cost


def crit_multiplier_for(names):
    """The one passive `combat` reads: Deathbringer's +35% ADDS to 1.5x,
    measured in game (`combat.DEATHBRINGER_CRIT_BONUS`)."""
    bonus = combat.DEATHBRINGER_CRIT_BONUS if "Deathbringer" in names else 0.0
    return combat.CRIT_MULTIPLIER + bonus


def profile(god, names, items_by_name, level=LEVEL, targets=TARGETS):
    """Everything the report says about one build on one god.

    `basic_dps`, `ability_dps` and `total_dps` are keyed by target protection.
    `per_1000g` carries the same figures divided by the build's gold in
    thousands, which is the only way a 13,750g build and a 15,400g one can be
    put on the same line.

    `burst` is the same rotation charged ONCE each instead of off cooldown —
    every ability in `ability_rotation` at its last rank, summed, keyed by
    target protection over `BURST_TARGETS`. It is the Jungle objective's
    maximand and the quantity both proposed thresholds are made of, and it
    counts NO basic attacks: adding them needs a burst-window duration in
    seconds, which nothing in the scrape supplies and which register §4.12
    already refused to invent for `damage_per_second`. That omission is why
    `threshold_probe` reads the way it does, and naming it here is the point.
    """
    stats, cost = build_totals(names, items_by_name)
    base = god.get("base_stats") or {}

    attack_power = combat.god_attack_power(god, level)
    chain = combat.attack_chain_multipliers(god)
    mean_swing = sum(chain) / len(chain) if chain else 1.0
    raw_basic = combat.attack_damage(attack_power, damage_value._basic_attack_scaling(god),
                                     stats, mean_swing)
    swing_rate = base_attack_speed(god, level)
    crit = min(stats.get("Critical Chance %", 0.0), 100.0) / 100.0
    flat_pen = stats.get("Penetration", 0.0)
    pct_pen = stats.get("Penetration %", 0.0) / 100.0
    cooldown_rate = stats.get("Cooldown Rate", 0.0)
    echo = stats.get("Echo", 0.0)

    rotation, dropped = ability_rotation(god)
    basic_dps, ability_dps, total_dps = {}, {}, {}
    for prot in targets:
        basic_dps[prot] = combat.attack_dps(
            raw_basic, prot, swing_rate, stats.get("Attack Speed %", 0.0),
            crit_chance=crit, crit_multiplier=crit_multiplier_for(names),
            flat_pen=flat_pen, pct_pen=pct_pen)
        per_second = 0.0
        for ability in rotation:
            raw = combat.ability_damage(ability["base"], ability["scaling"], stats)
            hit = combat.expected_ability_damage(raw, prot, echo, ability["is_ultimate"],
                                                 flat_pen=flat_pen, pct_pen=pct_pen)
            per_second += hit * combat.casts_per_second(ability["cooldown"], cooldown_rate)
        ability_dps[prot] = per_second
        total_dps[prot] = basic_dps[prot] + per_second

    burst = {}
    for prot in BURST_TARGETS:
        burst[prot] = sum(
            combat.expected_ability_damage(
                combat.ability_damage(a["base"], a["scaling"], stats),
                prot, echo, a["is_ultimate"], flat_pen=flat_pen, pct_pen=pct_pen)
            for a in rotation)

    health = level_value(base.get("health"), level) + stats.get("Max Health", 0.0)
    phys = level_value(base.get("physical_prot"), level) + stats.get("Physical Protection", 0.0)
    mag = level_value(base.get("magical_prot"), level) + stats.get("Magical Protection", 0.0)
    out = {
        "items": list(names), "cost": cost, "stats": stats,
        "attack_power": attack_power, "attack_speed": swing_rate,
        "raw_basic": raw_basic, "mean_swing": mean_swing,
        "basic_dps": basic_dps, "ability_dps": ability_dps, "total_dps": total_dps,
        "burst": burst,
        "health": health, "physical_prot": phys, "magical_prot": mag,
        "ehp_physical": combat.effective_health(health, phys),
        "ehp_magical": combat.effective_health(health, mag),
        "abilities": [a["name"] for a in rotation], "dropped": dropped,
    }
    thousands = cost / 1000.0 if cost else float("nan")
    out["per_1000g"] = {
        "total_dps": {p: v / thousands for p, v in total_dps.items()},
        "burst": {p: v / thousands for p, v in burst.items()},
        "ehp_physical": out["ehp_physical"] / thousands,
        "ehp_magical": out["ehp_magical"] / thousands,
    }
    # The Solo objective. EHP x DPS is what "their TTK on you over yours on
    # them" reduces to once the reference opponent cancels, so it is stored
    # raw and has no per-1000g twin: dividing a product of two per-gold
    # figures would charge the build's gold twice.
    out["duel"] = {p: out["ehp_physical"] * total_dps[p] for p in targets}
    return out


#: `metric` key prefix -> the profile field it reads, for the three that are
#: keyed by target protection. `duel` is absent deliberately: it has no
#: per-1000g twin, so it cannot go through the same branch.
_KEYED_BY_TARGET = {"dps_": "total_dps", "burst_": "burst"}


def metric(prof, key):
    """One of `METRICS` or a role objective's maximand off a profile.

    `key` may carry a `/1000g` suffix, except `duel_*` — asking for a duel
    score per 1000 gold raises, because the product already contains the
    build's gold twice and dividing it again is not a quantity.
    """
    per_gold = key.endswith("/1000g")
    base = key[:-len("/1000g")] if per_gold else key
    if base.startswith("duel_"):
        if per_gold:
            raise KeyError(f"{key}: a duel score has no per-1000g twin — it is a "
                           "product of two figures that each already carry the gold")
        return prof["duel"][int(base[len("duel_"):])]
    for prefix, field in _KEYED_BY_TARGET.items():
        if base.startswith(prefix):
            prot = int(base[len(prefix):])
            return (prof["per_1000g"][field] if per_gold else prof[field])[prot]
    return prof["per_1000g"][base] if per_gold else prof[base]


# ── Which builds ──────────────────────────────────────────────────────────

def community_core(build_note):
    """The community's slot items — the FIRST community entry, aspect or not,
    which is the one `validate._community_slots` scores against."""
    for b in build_note.get("builds") or []:
        if b.get("source") == "community":
            return [s.get("name") if isinstance(s, dict) else s
                    for s in b.get("slot_order") or []]
    return []


def suggested_core(build_note, archetype=DEFAULT_ARCHETYPE):
    """Our build of one archetype for the BASE kit — the first matching entry
    with no aspect, so an aspect overlay never stands in for the god."""
    for b in build_note.get("builds") or []:
        if (b.get("source") == "suggested" and b.get("archetype") == archetype
                and not b.get("aspect")):
            return [s.get("name") if isinstance(s, dict) else s
                    for s in b.get("slot_order") or []]
    return []


def primary_role(god):
    """`Solo Jungle` -> `Solo`: the roster's dual labels collapse to their
    first word for the role breakdown, and the report says so."""
    return str(god.get("role") or "").split()[0] if god.get("role") else "?"


def compare(god, build_note, items_by_name, archetype=DEFAULT_ARCHETYPE,
            level=LEVEL, targets=TARGETS):
    """`{god, role, primary_role, community, ours}` or None when either build
    is not a full six or names an item the pool lacks — skipped and named,
    never padded."""
    community = community_core(build_note)
    ours = suggested_core(build_note, archetype)
    if len(community) < 6 or len(ours) < 6:
        return None
    if any(n not in items_by_name for n in community + ours):
        return None
    return {
        "god": god["name"], "role": god.get("role"), "primary_role": primary_role(god),
        "community": profile(god, community[:6], items_by_name, level, targets),
        "ours": profile(god, ours[:6], items_by_name, level, targets),
    }


# ── Distribution ──────────────────────────────────────────────────────────

def distribution(rows, key):
    """Where we stand on one metric across the roster: counts ahead / behind /
    level, and quantiles of our figure over the community's, as a percentage
    delta. A ratio, so a 400-DPS Carry and a 150-DPS Support weigh the same."""
    deltas = []
    for row in rows:
        theirs = metric(row["community"], key)
        mine = metric(row["ours"], key)
        deltas.append((mine / theirs - 1.0) * 100.0 if theirs else float("nan"))
    arr = np.array([d for d in deltas if not np.isnan(d)], dtype=float)
    if not arr.size:
        return {"n": 0, "ahead": 0, "behind": 0, "level": 0, "quantiles": {}}
    return {
        "n": int(arr.size),
        "ahead": int((arr > 0.5).sum()),
        "behind": int((arr < -0.5).sum()),
        "level": int((np.abs(arr) <= 0.5).sum()),
        "quantiles": {q: float(np.percentile(arr, q)) for q in (0, 25, 50, 75, 100)},
        "deltas": deltas,
    }


def group_by_role(rows):
    """`{primary role: rows}` in `ROLE_ORDER`, then anything else, sorted."""
    groups = {}
    for row in rows:
        groups.setdefault(row["primary_role"], []).append(row)
    keys = ([r for r in ROLE_ORDER if r in groups]
            + sorted(k for k in groups if k not in ROLE_ORDER))
    return {role: groups[role] for role in keys}


def by_role(rows, key):
    """`{primary role: distribution}` in a fixed role order, then any other."""
    return {role: distribution(group, key) for role, group in group_by_role(rows).items()}


# ── Can either threshold bind? ────────────────────────────────────────────

def threshold_probe(rows):
    """Whether the two proposed thresholds can separate any build from any
    other, re-measured on every run rather than asserted once.

    `ROLE_OBJECTIVES` names a threshold for Carry, Mid and Jungle and then
    carries None for all three. This is why, and it is a fact about what this
    module can compute rather than about SMITE:

      * the CARRY floor is "survive one enemy burst rotation". Taken at its
        most generous — the single largest burst anywhere in the roster, read
        at ZERO protection, against each Carry's own effective health — and
        it still separates nobody.
      * the MID/JUNGLE kill threshold is "rotation burst >= a reference
        squishy's EHP", the reference being the median EHP of the community's
        own Carry and Mid builds. Every Mid and Jungle build in the roster
        fails it, on both sides.

    Both come out one-sided for one shared reason, and it is a hole in the
    damage model rather than a verdict on thresholds: a burst here is one cast
    of every ability with NO basic attacks (register §4.12 — there is no cast
    time in the scrape, so there is no window to swing in), no item passive
    (~90% of the pool, see `passive_blind_spot`), no follow-up and one target,
    while EHP is full level-20 health plus every protection the six items
    carry. The two are roughly an order of magnitude apart in scale and the
    constant that would close the gap is a burst-window duration in seconds,
    which no source here supplies.

    Returns the counts and the HEADROOM — how far the tightest build sits from
    the threshold, as a ratio — so a future run on different data, or with a
    clock or priced passives in the model, prints a threshold that binds
    instead of this.
    """
    groups = group_by_role(rows)
    sides = ("community", "ours")

    bursts = [(metric(row[side], "burst_0"), row["god"], side)
              for row in rows for side in sides]
    reference_burst, burst_god, burst_side = max(bursts)

    squishy = [row[side]["ehp_magical"]
               for role in ("Carry", "Mid") for row in groups.get(role, []) for side in ("community",)]
    reference_ehp = float(np.median(squishy)) if squishy else float("nan")

    def probe(name, population, value, passes, reference):
        """`passes(value_of_build, reference)` is the threshold as a reader
        would state it; `failed` counts the builds it separates out.

        `nearest` is the margin of the build that came CLOSEST to the
        threshold, as `value / reference` — the ratio nearest 1.0, whichever
        side it falls. A threshold that separates nobody and a threshold that
        separates everybody are both useless, and this is the one number that
        says how far either is from doing something.
        """
        out = {"name": name, "reference": reference, "n": 0, "failed": 0,
               "nearest": float("nan")}
        margins = []
        for row in population:
            for side in sides:
                v = value(row[side])
                out["n"] += 1
                out["failed"] += 0 if passes(v, reference) else 1
                margins.append(v / reference if reference else float("nan"))
        if margins:
            out["nearest"] = float(min(margins, key=lambda m: abs(m - 1.0)))
        return out

    carry = probe(
        "Carry: survive one enemy burst rotation",
        groups.get("Carry", []), lambda p: p["ehp_magical"],
        lambda v, ref: v >= ref, reference_burst)
    carry["detail"] = (f"largest burst in the roster at 0 protection — {burst_god}, "
                       f"{burst_side}, {reference_burst:,.0f}")

    kill = probe(
        "Mid / Jungle: rotation burst >= a reference squishy's EHP",
        groups.get("Mid", []) + groups.get("Jungle", []),
        lambda p: metric(p, "burst_70"), lambda v, ref: v >= ref, reference_ehp)
    kill["detail"] = ("median effective health of the community's own Carry and Mid "
                      f"builds, magical — {reference_ehp:,.0f}")

    return {"carry_survival": carry, "kill_threshold": kill,
            "reference_burst": reference_burst, "reference_squishy_ehp": reference_ehp}


# ── The blind spot ────────────────────────────────────────────────────────

def _stat_lines(items, weights):
    """Each item's stat line twice: as printed, and under the shipped pricing
    flags. An item whose two lines differ has a passive the gold model prices."""
    before = efficiency.apply_pricing_flags({})
    try:
        printed = {it["name"]: efficiency.item_stat_values(it) for it in items}
        efficiency.apply_pricing_flags(weights)
        priced = {it["name"]: efficiency.item_stat_values(it) for it in items}
    finally:
        efficiency.restore_pricing_flags(before)
    return printed, priced


def passive_blind_spot(items, gods, builds_by_god, weights, archetype=DEFAULT_ARCHETYPE):
    """How much of what the builds buy this arithmetic cannot see.

    An item is BLIND when it carries passive text and the shipped pricing flags
    leave its stat line unchanged — the gold model reads nothing from it, and
    `combat` reads nothing from any passive but Deathbringer's. Measured over
    the god-agnostic buildable pool (`scoring.is_buildable`), over the
    community's slot picks and over ours; slots of any tier count, because the
    question for a slot is whether there is value in it the model cannot see,
    and a tier-2 component with a passive is exactly that.

    The premium is the gold model's residual (`cost - predicted_cost`): what a
    slot pays above what its stat line predicts is, by construction, what it
    pays for the passive. Mean per slot, community against ours.
    """
    by_name = {it["name"]: it for it in items}
    printed, priced = _stat_lines(items, weights)
    priced_names = {n for n in printed if printed[n] != priced[n]}

    def blind(name):
        item = by_name.get(name)
        return bool(item) and bool((item.get("passive") or "").strip()) and name not in priced_names

    before = efficiency.apply_pricing_flags({})
    try:
        residuals = {n: s["residual"] for n, s in efficiency.efficiency_scores(items)[0].items()}
    finally:
        efficiency.restore_pricing_flags(before)

    pool = [it for it in items if scoring.is_buildable(it)]
    pool_passive = [it for it in pool if (it.get("passive") or "").strip()]
    pool_blind = [it for it in pool_passive if blind(it["name"])]

    def slots(names):
        n = len(names)
        res = [residuals[x] for x in names if x in residuals]
        cols = [len(printed[x]) for x in names if x in printed]
        return {
            "slots": n,
            "blind": sum(1 for x in names if blind(x)),
            "share": (sum(1 for x in names if blind(x)) / n) if n else float("nan"),
            "mean_residual": (sum(res) / len(res)) if res else float("nan"),
            "mean_stats": (sum(cols) / len(cols)) if cols else float("nan"),
            "top_blind": [(name, count) for name, count in Counter(names).most_common()
                          if blind(name)][:5],
        }

    community_names, our_names = [], []
    for god in gods:
        note = builds_by_god.get(god["name"]) or {}
        community_names += community_core(note)
        our_names += suggested_core(note, archetype)
    return {
        "buildable": len(pool),
        "with_passive": len(pool_passive),
        "priced": sorted(n for n in priced_names if n in {it["name"] for it in pool}),
        "blind": len(pool_blind),
        "blind_share": len(pool_blind) / len(pool) if pool else float("nan"),
        "community": slots(community_names),
        "ours": slots(our_names),
    }


# ── Two stat lines ────────────────────────────────────────────────────────

def run(gods, items, builds_by_god, weights, archetype=DEFAULT_ARCHETYPE,
        priced=False, level=LEVEL, targets=TARGETS):
    """`(rows, skipped)` over the roster.

    `priced` False reads every item's PRINTED stat line, which is the
    headline. True applies the shipped pricing flags — the Adaptive Stat
    grants and the mana conversions the gold model prices — with
    `PRICE_CRIT_MULTIPLIERS` forced off, because `combat` applies
    Deathbringer's bonus as the 1.85x it measured rather than as a crit-chance
    equivalent. The difference between the two runs is the one slice of the
    blind spot this arithmetic can put a number on.
    """
    items_by_name = {it["name"]: it for it in items}
    before = efficiency.apply_pricing_flags(weights if priced else {})
    try:
        if priced:
            efficiency.PRICE_CRIT_MULTIPLIERS = False
        rows, skipped = [], []
        for god in sorted(gods, key=lambda g: g["name"]):
            row = compare(god, builds_by_god.get(god["name"]) or {}, items_by_name,
                          archetype, level, targets)
            (rows if row else skipped).append(row or god["name"])
    finally:
        efficiency.restore_pricing_flags(before)
    return rows, skipped


# ── The report ────────────────────────────────────────────────────────────

def _pct(x):
    return f"{x:+.1f}%"


def _dist_table(rows, keys, title_key=lambda k: k):
    lines = ["| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for key in keys:
        d = distribution(rows, key)
        q = d["quantiles"]
        if not q:
            lines.append(f"| {title_key(key)} | 0 | – | – | – | – | – | – | – | – |")
            continue
        lines.append(f"| {title_key(key)} | {d['n']} | **{d['ahead']}** | **{d['behind']}** | "
                     f"{d['level']} | {_pct(q[0])} | {_pct(q[25])} | **{_pct(q[50])}** | "
                     f"{_pct(q[75])} | {_pct(q[100])} |")
    return lines


def _role_table(rows, keys, labels):
    roles = list(by_role(rows, keys[0]).keys())
    header = "| Role | n | " + " | ".join(f"{labels[k]} ahead / behind / median" for k in keys) + " |"
    lines = [header, "|---|---|" + "---|" * len(keys)]
    for role in roles:
        cells = []
        n = None
        for key in keys:
            d = by_role(rows, key)[role]
            n = d["n"]
            med = d["quantiles"].get(50, float("nan"))
            cells.append(f"{d['ahead']} / {d['behind']} / {_pct(med)}")
        lines.append(f"| {role} | {n} | " + " | ".join(cells) + " |")
    return lines


#: The stat keys a "defence" claim is made of, in report order.
DEFENSIVE_STATS = ("Physical Protection", "Magical Protection", "Max Health")


def defence_by_role(rows):
    """Mean defensive stats bought, per role, community against ours.

    The role split's headline finding is that our Carries are tankier than the
    community's on 18 of 18 while losing damage on 6, and this is where that
    comes from as a stat line rather than as a verdict.
    """
    out = {}
    for role, group in group_by_role(rows).items():
        out[role] = {"n": len(group)}
        for side in ("community", "ours"):
            out[role][side] = {
                stat: sum(row[side]["stats"].get(stat, 0.0) for row in group) / len(group)
                for stat in DEFENSIVE_STATS}
    return out


def defence_drivers(rows, role, items_by_name, top=3):
    """The items carrying the role's defensive surplus: most common in OUR
    cores for that role, carrying a defensive stat, ranked by how much of the
    gap they account for. `(name, ours_count, community_count, stats)`."""
    group = group_by_role(rows).get(role, [])
    ours, theirs = Counter(), Counter()
    for row in group:
        ours.update(row["ours"]["items"])
        theirs.update(row["community"]["items"])
    scored = []
    for name, count in ours.items():
        item = items_by_name.get(name)
        if item is None:
            continue
        stats = {k: v for k, v in efficiency.item_stat_values(item).items()
                 if k in DEFENSIVE_STATS}
        if stats:
            scored.append((count, name, theirs.get(name, 0), stats))
    scored.sort(key=lambda s: (-s[0], s[1]))
    return [(name, count, seen, stats) for count, name, seen, stats in scored[:top]]


def carry_mechanism_lines(rows, items_by_name):
    """WHERE THE CARRY SURPLUS COMES FROM — recorded, not acted on.

    This is a diagnosis handed to a later session on purpose: the session that
    found it should not also be the one that fixes it. Nothing here changes a
    weight, a build or an item, and the numbers re-measure on every run so a
    refresh that moves them says so instead of leaving this paragraph stale.

    One hypothesis is already excluded, mechanically rather than statistically,
    and is recorded in docs/STATE.md §4 so it is not re-derived: neither
    `defense_affinity` (`build_index`) nor `draft.archetype_scaled_stats` can
    reach these builds — both are read only by `viewer/src/lib/threats.ts`, the
    draft overlay, which is applied on top of a finished core — and
    `defense_affinity` is 0.0 for Carry anyway, because it is derived from
    `scoring._role_stat_map` and the Carry map names no protection.
    """
    defence = defence_by_role(rows)
    carry = defence.get("Carry")
    if not carry:
        return []
    lines = [
        "### Where the Carry surplus comes from — recorded, not acted on", "",
        "The row above is the finding this section was built for, so its mechanism is written "
        "down. **Nothing here has been changed in response to it**; the diagnosis is deliberately "
        "left to a session other than the one that found it.", "",
        "Mean defensive stats bought at level 20, community (C) against our `model` core (O):", "",
        "| Role | n | " + " | ".join(f"{s} C / O" for s in DEFENSIVE_STATS) + " |",
        "|---|---|" + "---|" * len(DEFENSIVE_STATS),
    ]
    for role, d in defence.items():
        cells = " | ".join(f"{d['community'][s]:,.1f} / {d['ours'][s]:,.1f}" for s in DEFENSIVE_STATS)
        lines.append(f"| {role} | {d['n']} | {cells} |")
    drivers = defence_drivers(rows, "Carry", items_by_name)
    lines += [
        "",
        f"The community buys **exactly {carry['community']['Physical Protection']:,.1f} Physical "
        f"Protection** across all {carry['n']} Carries; we buy "
        f"{carry['ours']['Physical Protection']:,.1f}. It is not spread across the pool — the "
        "items carrying it, with how many of our Carry cores hold each against how many of the "
        "community's:", "",
    ]
    for name, mine, seen, stats in drivers:
        line = " · ".join(f"{k} {v:g}" for k, v in sorted(stats.items()))
        lines.append(f"- **{name}** — ours {mine} of {carry['n']}, community {seen} of "
                     f"{carry['n']} ({line})")
    phys = by_role(rows, "ehp_physical")["Carry"]["quantiles"].get(50, float("nan"))
    mag = by_role(rows, "ehp_magical")["Carry"]["quantiles"].get(50, float("nan"))
    lines += [
        "",
        "Two things a later session should not have to rediscover. The protection is **physical "
        "only**, so against the magical burst a Carry most often dies to it buys health and "
        f"nothing else — which is why the same builds read {_pct(phys)} on effective health "
        f"physical and {_pct(mag)} magical. And `defense_affinity` and "
        "`draft.archetype_scaled_stats` are "
        "**excluded as causes**: both are read only by the viewer's draft overlay "
        "(`viewer/src/lib/threats.ts`), which is applied on top of a finished core and never "
        "reaches the builds measured here, and `defense_affinity` is 0.0 for Carry in any case "
        "because it is derived from the same role map that names no protection for the role. "
        "See docs/STATE.md §4.",
    ]
    return lines


def role_verdict(rows, role, objective):
    """One role's verdict on its OWN objective: `{role, n, maximise, threshold,
    ahead, behind, level, median}`. Never on the pooled metric — a Carry and a
    Support do not share one."""
    group = group_by_role(rows).get(role, [])
    key, label = objective["maximise"]
    d = distribution(group, key)
    return {
        "role": role, "n": d["n"], "key": key, "maximise": label,
        "threshold": objective["threshold"], "because": objective["because"],
        "ahead": d["ahead"], "behind": d["behind"], "level": d["level"],
        "median": d["quantiles"].get(50, float("nan")),
    }


def role_verdicts(rows, objectives=None):
    """Every role in `ROLE_ORDER` that has rows, judged on its own objective.
    A role with no entry in `ROLE_OBJECTIVES` is returned with `maximise` None
    rather than silently dropped or silently given someone else's metric."""
    objectives = ROLE_OBJECTIVES if objectives is None else objectives
    out = []
    for role in group_by_role(rows):
        objective = objectives.get(role)
        if objective is None:
            out.append({"role": role, "n": len(group_by_role(rows)[role]), "key": None,
                        "maximise": None, "threshold": None,
                        "because": "no objective is recorded for this role label",
                        "ahead": 0, "behind": 0, "level": 0, "median": float("nan")})
            continue
        out.append(role_verdict(rows, role, objective))
    return out


def _verdict_table(verdicts, probe):
    lines = ["| Role | n | Threshold | Binds? | Maximised | ahead | behind | tie | median |",
             "|---|---|---|---|---|---|---|---|---|"]
    for v in verdicts:
        if v["threshold"] is None:
            threshold, binds = "**none**", "–"
        else:
            name, probe_key = v["threshold"]
            p = probe[probe_key]
            threshold = name
            if p["failed"] == 0:
                binds = f"**no** — 0 of {p['n']} builds fail it"
            elif p["failed"] == p["n"]:
                binds = f"**no** — all {p['n']} builds fail it"
            else:
                binds = f"yes — {p['failed']} of {p['n']} fail"
        maximise = v["maximise"] or "_no objective recorded_"
        median = "–" if v["median"] != v["median"] else f"**{_pct(v['median'])}**"
        lines.append(f"| {v['role']} | {v['n']} | {threshold} | {binds} | {maximise} | "
                     f"**{v['ahead']}** | **{v['behind']}** | {v['level']} | {median} |")
    return lines


def role_verdict_lines(rows, probe, verdicts=None, items_by_name=None):
    """The per-role section: what each role's build is FOR, whether its
    threshold binds, and where we stand on its own maximand.

    Every verdict states which quantity was a threshold and which was
    maximised, so a reader can disagree with the choice rather than only with
    the number — that is the point of the section and a test holds it.
    """
    verdicts = role_verdicts(rows) if verdicts is None else verdicts
    lines = [
        "Most roles clear a THRESHOLD and then maximise something else, and one pooled metric "
        "cannot represent five roles that do not share an objective. Each row below names both "
        "quantities. **The passive blind spot at the top of this report applies to every row "
        "here exactly as it applies to the pooled figures** — slicing by role does not escape "
        "it, and the bias still runs in our favour.",
        "",
    ]
    lines += _verdict_table(verdicts, probe)
    lines += ["", "Why each objective is what it is:", ""]
    for v in verdicts:
        lines.append(f"- **{v['role']}** — {v['because']}")
    lines += ["", "### Neither threshold binds, and that is a statement about this arithmetic", ""]
    lines += [
        "Both thresholds were defined, measured and left in the table with their measurement, "
        "rather than dropped quietly. Re-measured on every run by `threshold_probe`:",
        "",
        "| Threshold | population | reference | separates | nearest build |",
        "|---|---|---|---|---|",
    ]
    for key in ("carry_survival", "kill_threshold"):
        p = probe[key]
        lines.append(f"| {p['name']} | {p['n']} builds | {p['detail']} | "
                     f"**{p['failed']} of {p['n']}** | {p['nearest']:.2f}x the threshold |")
    lines += [
        "",
        "A threshold that separates none of the population and a threshold that separates all of "
        "it are equally useless, and one of each is what these are. **Read this as \"we cannot "
        "currently evaluate a threshold\", not as \"thresholds do not matter in SMITE\"** — the "
        "cause is on our side of the arithmetic. A burst here is one cast of every ability with "
        "no basic attacks, no item passive, no follow-up and one target, while effective health "
        "is full level-20 health plus every protection the six items carry; the two are about an "
        "order of magnitude apart. Two things would change the answer and neither is a tuning "
        "choice: **a clock** (register §4.12 — a burst window in seconds would let basic attacks "
        "into the burst, and it is refused because no source supplies one), or **priced passives** "
        "(register §4.5 — ~90% of the pool carries value neither side of this comparison can see). "
        "Until one of those exists, Carry, Mid and Jungle are judged on their maximand alone.",
    ]
    if items_by_name is not None:
        lines += [""] + carry_mechanism_lines(rows, items_by_name)
    return lines


def _god_table(rows):
    lines = ["| God | Role | Gold C / O | DPS vs 70 — C (basic+ability) | O (basic+ability) | Δ | "
             "DPS vs 170 — C | O | Δ | EHP phys — C | O | Δ | EHP mag — C | O | Δ |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        c, o = r["community"], r["ours"]

        def d(key):
            return _pct((metric(o, key) / metric(c, key) - 1.0) * 100.0)

        lines.append(
            f"| {r['god']} | {r['role']} | {c['cost']:,.0f} / {o['cost']:,.0f} | "
            f"{c['total_dps'][70]:.1f} ({c['basic_dps'][70]:.1f}+{c['ability_dps'][70]:.1f}) | "
            f"{o['total_dps'][70]:.1f} ({o['basic_dps'][70]:.1f}+{o['ability_dps'][70]:.1f}) | {d('dps_70')} | "
            f"{c['total_dps'][170]:.1f} | {o['total_dps'][170]:.1f} | {d('dps_170')} | "
            f"{c['ehp_physical']:,.0f} | {o['ehp_physical']:,.0f} | {d('ehp_physical')} | "
            f"{c['ehp_magical']:,.0f} | {o['ehp_magical']:,.0f} | {d('ehp_magical')} |")
    return lines


def _profile_lines(label, p):
    lines = [f"**{label}** — {p['cost']:,.0f}g: " + " · ".join(p["items"])]
    stat_line = " · ".join(f"{k} {v:g}" for k, v in sorted(p["stats"].items()))
    lines.append(f"  stat line: {stat_line}")
    lines.append(f"  abilities counted: {', '.join(p['abilities']) or 'none'}"
                 + (f" · dropped for no cooldown: {', '.join(p['dropped'])}" if p["dropped"] else ""))
    return lines


def worked_example(row):
    """The Medusa block, in the brief's own table shape."""
    c, o = row["community"], row["ours"]
    lines = [f"### {row['god']} ({row['role']})", ""]
    lines += _profile_lines("community", c) + [""] + _profile_lines("ours", o) + [""]
    lines += ["| | basic DPS | ability DPS | TOTAL | EHP physical | EHP magical |",
              "|---|---|---|---|---|---|"]
    for label, p in (("COMMUNITY", c), ("OURS", o)):
        for prot in TARGETS:
            tag = "squishy (70)" if prot == 70 else f"tank ({prot})" if prot == 170 else str(prot)
            lines.append(f"| {label} vs {tag} | {p['basic_dps'][prot]:.1f} | "
                         f"{p['ability_dps'][prot]:.1f} | **{p['total_dps'][prot]:.1f}** | "
                         f"{p['ehp_physical']:,.0f} | {p['ehp_magical']:,.0f} |")
    lines += ["", "| per 1000g | DPS vs 70 | DPS vs 170 | EHP physical | EHP magical |",
              "|---|---|---|---|---|"]
    for label, p in (("COMMUNITY", c), ("OURS", o)):
        g = p["per_1000g"]
        lines.append(f"| {label} | {g['total_dps'][70]:.1f} | {g['total_dps'][170]:.1f} | "
                     f"{g['ehp_physical']:,.0f} | {g['ehp_magical']:,.0f} |")
    return lines


def caveat_lines(blind):
    """The paragraph that has to come before any verdict."""
    c, o = blind["community"], blind["ours"]
    return [
        "> **READ THIS BEFORE ANY NUMBER BELOW.** Of the "
        f"{blind['buildable']} buildable items, {blind['with_passive']} carry passive text and the "
        f"shipped pricing flags read {len(blind['priced'])} of them — so **{blind['blind_share']:.0%} of "
        "the pool carries passive value this arithmetic cannot see**, and "
        f"**{c['share']:.0%} of the community's item slots do** ({c['blind']} of {c['slots']}; "
        f"{o['share']:.0%} of ours, {o['blind']} of {o['slots']}). `combat.py` reads exactly one "
        "passive — Deathbringer's +35% crit damage. The bias is not even: by the gold model's own "
        f"residual the community pays **{c['mean_residual'] - o['mean_residual']:+,.0f}g more per slot "
        "above its stat line than we do** (mean residual "
        f"{c['mean_residual']:+,.0f}g against {o['mean_residual']:+,.0f}g) and buys fewer stat columns "
        f"per item ({c['mean_stats']:.2f} against {o['mean_stats']:.2f}) — that premium IS the passive. "
        "**A verdict in our favour is the one to distrust.** The most-bought blind community items are "
        + ", ".join(f"{n} ({k})" for n, k in c["top_blind"]) + ".",
    ]


def assumption_lines():
    return [
        "Assumptions, all of them on every figure:",
        "",
        "- **full ability uptime** — every ability cast the moment it is off cooldown, at its last "
        "rank, with no cast time charged (none exists in the scrape; register §4.12), so a god casts "
        "everything AND swings at full rate in the same second",
        "- **no relic, single target, no lifesteal sustain, no crowd control, no wave clear**",
        "- targets at exactly 70 and 170 protection of the god's own damage type, no Plating or Dampening",
        "- level 20, six items, the community's slot picks against our meta-free `model` core "
        "(the first community entry, aspect or not — the one `validate` scores against)",
        "- printed stat lines only, with penetration kept as two goods and capped "
        f"({combat.PCT_PEN_CAP:.0%} / {combat.FLAT_PEN_CAP:.0f}); Deathbringer at the measured 1.85x",
        "- a chain god's basic attack at the chain's mean multiplier; an ability without a scraped "
        "cooldown dropped, never imputed; a DoT counted as its listed damage once",
        "- dual-role labels (`Solo Jungle`) collapse to their first word in the role tables",
        "- a burst is one cast of every counted ability, summed; it charges no basic attacks, "
        "because a burst window in seconds does not exist in this repo (register §4.12)",
        "",
        "**What none of this measures, at any level of slicing:** "
        + ", ".join(UNMEASURABLE) + ". Much of what a Support contributes is on that list, which "
        "is why Support's objective excludes damage rather than weighting it small — scoring a "
        "quantity badly is worse than declining to score it, and on 3 of 14 Supports the damage "
        "column is identical on both sides because neither build buys any.",
        "",
        "Nothing here feeds `scoring`, `assemble` or a weight. It is a report a human reads.",
    ]


def _dist_section(rows, skipped, heading, note=None):
    keys = [k for k, _ in METRICS]
    labels = dict(METRICS)

    def title(key):
        if key in labels:
            return labels[key]
        return labels[key[:-len("/1000g")]] + " per 1000g"

    lines = [f"## {heading}", ""]
    if note:
        lines += [note, ""]
    lines.append(f"{len(rows)} gods compared" + (f"; skipped: {', '.join(skipped)}" if skipped else "") + ".")
    lines.append("")
    lines.append("Delta is ours over the community's, per god; a ratio, so every god weighs the same.")
    lines.append("")
    lines += _dist_table(rows, keys + [k + "/1000g" for k in keys], title)
    lines += ["", "By role — ahead / behind / median delta:", ""]
    lines += _role_table(rows, keys, labels)
    lines += ["", "Per 1000 gold, by role:", ""]
    lines += _role_table(rows, [k + "/1000g" for k in keys], {k + "/1000g": v for k, v in labels.items()})
    return lines


def flips(rows_a, rows_b, key="dps_70"):
    """Gods whose verdict on `key` changes sign between two runs."""
    b = {r["god"]: r for r in rows_b}
    out = []
    for r in rows_a:
        if r["god"] not in b:
            continue
        da = metric(r["ours"], key) - metric(r["community"], key)
        db = metric(b[r["god"]]["ours"], key) - metric(b[r["god"]]["community"], key)
        if (da > 0) != (db > 0):
            out.append((r["god"], da, db))
    return out


def write_report(rows, skipped, core_rows, core_skipped, priced_rows, priced_skipped,
                 blind, fingerprint, out_path=REPORT_PATH, example="Medusa",
                 items_by_name=None):
    """Byte-for-byte deterministic, like `_calibration.md`, so its diff is a
    record of what a commit did to the builds rather than of when it ran."""
    head = ["# Build quality — `combat.py` pointed at whole builds", "",
            f"_Input fingerprint: `{fingerprint}` — items, gods, tags, community builds, "
            "weights. Regenerate with `python -m smite.build_quality`; a different fingerprint "
            "means different inputs._", ""]
    lines = []
    lines.append("This is the only instrument in the repo that can say a build is BETTER rather "
                 "than more conventional: `validate.compute` is circular (STATE.md §1) and the "
                 "leakage-free gate is coverage of the community's items, and both go down when a "
                 "build is genuinely better and unconventional. `combat.py` is calibrated to 0.0% "
                 "against in-game readings and has never seen a community build. It also cannot "
                 "see a passive, which is the paragraph above.")
    lines.append("")
    lines += assumption_lines()
    lines.append("")

    lines += ["## 1. The worked example", ""]
    ex = next((r for r in rows if r["god"] == example), None)
    if ex:
        lines += worked_example(ex)
    else:
        lines.append(f"_{example} not compared ({', '.join(skipped) or 'no rows'})._")
    lines.append("")

    lines += _dist_section(rows, skipped, "2. The roster — our `model` core, printed stat lines")
    lines.append("")

    lines += ["## 3. Judged by role, on each role's own objective", ""]
    lines += role_verdict_lines(rows, threshold_probe(rows), items_by_name=items_by_name)
    lines.append("")

    lines += _dist_section(core_rows, core_skipped,
                           "4. The same, for the blended `core` (what the Balanced tab ships)",
                           "`core` carries `win` and `pick`, so it is part community build already; "
                           "the gap between this block and §2 is what the meta signal buys in "
                           "this arithmetic.")
    lines.append("")
    lines += _dist_section(priced_rows, priced_skipped,
                           "5. Sensitivity — the passives the gold model CAN price",
                           "Same as §2 with the shipped pricing flags applied to every stat line: the "
                           "Adaptive Stat grants (`price_adaptive`) and the mana conversions "
                           "(`price_conversions`). This is the one slice of the blind spot that can "
                           "be put on the table; the other "
                           f"{blind['blind']} items stay invisible here too.")
    changed = flips(rows, priced_rows)
    lines.append("")
    if changed:
        lines.append(f"Verdict on DPS vs 70 flips for {len(changed)} god(s) between §2 and §5: "
                     + ", ".join(f"{g} ({a:+.1f} → {b:+.1f})" for g, a, b in changed) + ".")
    else:
        lines.append("No god's verdict on DPS vs 70 flips between §2 and §5.")
    lines.append("")

    c, o = blind["community"], blind["ours"]
    lines += ["## 6. The blind spot, measured", "",
              "| | buildable pool | community slots | our `model` slots |", "|---|---|---|---|",
              f"| items / slots | {blind['buildable']} | {c['slots']} | {o['slots']} |",
              f"| carrying unpriced passive text | {blind['blind']} ({blind['blind_share']:.1%}) | "
              f"{c['blind']} ({c['share']:.1%}) | {o['blind']} ({o['share']:.1%}) |",
              f"| mean gold residual per slot (cost − stat-line prediction) | – | "
              f"{c['mean_residual']:+,.0f}g | {o['mean_residual']:+,.0f}g |",
              f"| mean stat columns per item | – | {c['mean_stats']:.2f} | {o['mean_stats']:.2f} |",
              "",
              "Passives the shipped flags price (" + str(len(blind["priced"])) + "): "
              + ", ".join(blind["priced"]) + ".",
              "",
              "Most-bought blind items — community: "
              + ", ".join(f"{n} ({k})" for n, k in c["top_blind"]) + ". Ours: "
              + ", ".join(f"{n} ({k})" for n, k in o["top_blind"]) + ".",
              ""]

    lines += ["## 7. Every god — `model` core, printed stat lines", "",
              "C = community, O = ours. DPS vs 70 is shown as total (basic + ability).", ""]
    lines += _god_table(rows)
    lines.append("")
    return emit(blind, lines, head=head, out_path=out_path)


def emit(blind, body, head=(), out_path=None):
    """THE ONLY WAY OUT OF THIS MODULE. Every print and every file write is
    here — a test refuses one anywhere else — and what leaves is the caveat
    first, then the body. A path that wants to show a number has no way to
    show it without the blind spot above it, which is the property the
    `--god` path lacked when it returned before `passive_blind_spot` ran
    (2026-08-21).

    `head` is identification, never a figure: the report's title and its
    input fingerprint. The CLI test reads every path's output and refuses a
    figure before the caveat, so a figure in `head` fails there.
    """
    text = "\n".join(list(head) + caveat_lines(blind) + [""] + list(body))
    if out_path is None:
        print(text)
        return None
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    return out_path


# ── CLI ───────────────────────────────────────────────────────────────────

def _fingerprint(items, weights, tags_map, gods, builds_by_god):
    """`calibrate.input_fingerprint` without `_Fixture`, whose constructor
    applies the pricing flags as a side effect — this report sets them itself."""
    fx = types.SimpleNamespace(items=items, weights=weights, tags_map=tags_map,
                               gods=gods, builds_by_god=builds_by_god)
    return calibrate.input_fingerprint(fx)


def build_parser():
    ap = argparse.ArgumentParser(description="combat.py pointed at whole builds, ours vs community")
    ap.add_argument("--god", help="print one god's comparison and stop")
    # Not `choices=ROLE_ORDER`: a role label comes from the scraped roster, so
    # an unknown one is a data question and belongs in the same stderr message
    # as an unknown god rather than in an argparse usage error.
    ap.add_argument("--role", help="print one role's verdict on its own objective and stop")
    ap.add_argument("--archetype", default=DEFAULT_ARCHETYPE,
                    help="our build to compare (default: model)")
    ap.add_argument("--out", type=Path, default=REPORT_PATH)
    return ap


def main(argv=None):
    args = build_parser().parse_args(argv)

    items = recommend.load_items()
    gods = recommend.load_gods()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags_map = scoring.load_tags(recommend.TAGS_PATH)
    builds_by_god = {g["name"]: recommend.load_build_note(g["name"]) for g in gods}
    # Measured before any path can print: the roster-wide blind spot is the
    # caveat on a single god's table as much as on the distribution.
    blind = passive_blind_spot(items, gods, builds_by_god, weights, args.archetype)

    if args.god:
        rows, skipped = run([g for g in gods if g["name"] == args.god], items, builds_by_god,
                            weights, args.archetype)
        if not rows:
            print(f"{args.god}: not compared ({', '.join(skipped) or 'unknown god'})",
                  file=sys.stderr)
            return 1
        emit(blind, worked_example(rows[0]))
        return 0

    if args.role:
        # The whole roster, even for one role: the thresholds are referenced
        # against builds outside the role being judged, so a single-role run
        # would silently change what they are measured against.
        rows, _ = run(gods, items, builds_by_god, weights, args.archetype)
        if args.role not in group_by_role(rows):
            print(f"{args.role}: no gods with that primary role "
                  f"({', '.join(group_by_role(rows))})", file=sys.stderr)
            return 1
        verdicts = [v for v in role_verdicts(rows) if v["role"] == args.role]
        emit(blind, role_verdict_lines(rows, threshold_probe(rows), verdicts,
                                       items_by_name={it["name"]: it for it in items}))
        return 0

    rows, skipped = run(gods, items, builds_by_god, weights, args.archetype)
    core_rows, core_skipped = run(gods, items, builds_by_god, weights, "core")
    priced_rows, priced_skipped = run(gods, items, builds_by_god, weights, args.archetype, priced=True)
    fingerprint = _fingerprint(items, weights, tags_map, gods, builds_by_god)
    path = write_report(rows, skipped, core_rows, core_skipped, priced_rows, priced_skipped,
                        blind, fingerprint, args.out,
                        items_by_name={it["name"]: it for it in items})

    d70, d170 = distribution(rows, "dps_70"), distribution(rows, "dps_170")
    probe = threshold_probe(rows)
    emit(blind, [
        f"{len(rows)} gods compared, {len(skipped)} skipped",
        f"  DPS vs 70:  ahead {d70['ahead']}, behind {d70['behind']}, "
        f"median {_pct(d70['quantiles'][50])}",
        f"  DPS vs 170: ahead {d170['ahead']}, behind {d170['behind']}, "
        f"median {_pct(d170['quantiles'][50])}",
        "  each role on its OWN objective (pooled figures above average roles that do not share one):",
    ] + [
        f"    {v['role']:<8} {v['ahead']:>2} ahead, {v['behind']:>2} behind, "
        f"median {_pct(v['median'])}  — maximised: {v['maximise']}"
        + ("" if v["threshold"] is None else
           f"; threshold ({v['threshold'][0]}) separates "
           f"{probe[v['threshold'][1]]['failed']} of {probe[v['threshold'][1]]['n']}")
        for v in role_verdicts(rows)
    ] + [
        f"  wrote {path}",
    ])
    return 0


if __name__ == "__main__":
    sys.exit(main())
