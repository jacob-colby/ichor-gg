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
  * effective health, physical and magical (`combat.effective_health`)
  * total gold, and each figure per 1000 gold

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
distrust. The report says so at the top, and a test refuses a report that
states a distribution without it.

THE OTHER ASSUMPTIONS, also printed on the report: full ability uptime with no
cast times (register §4.12 — nothing in the scrape has one, so a god casts
everything off cooldown AND swings at full rate in the same second), no relic,
single target, no lifesteal sustain, no crowd control, no wave clear, both
targets at exactly 70 / 170 of the god's own damage type with no Plating or
Dampening, and an ability without a scraped cooldown dropped rather than
imputed (the rule `damage_value._base_cooldown` already applies).

    python -m smite.build_quality                 # write data/Analysis/_build_quality.md
    python -m smite.build_quality --god Medusa    # one god's profile, to stdout
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

    health = level_value(base.get("health"), level) + stats.get("Max Health", 0.0)
    phys = level_value(base.get("physical_prot"), level) + stats.get("Physical Protection", 0.0)
    mag = level_value(base.get("magical_prot"), level) + stats.get("Magical Protection", 0.0)
    out = {
        "items": list(names), "cost": cost, "stats": stats,
        "attack_power": attack_power, "attack_speed": swing_rate,
        "raw_basic": raw_basic, "mean_swing": mean_swing,
        "basic_dps": basic_dps, "ability_dps": ability_dps, "total_dps": total_dps,
        "health": health, "physical_prot": phys, "magical_prot": mag,
        "ehp_physical": combat.effective_health(health, phys),
        "ehp_magical": combat.effective_health(health, mag),
        "abilities": [a["name"] for a in rotation], "dropped": dropped,
    }
    thousands = cost / 1000.0 if cost else float("nan")
    out["per_1000g"] = {
        "total_dps": {p: v / thousands for p, v in total_dps.items()},
        "ehp_physical": out["ehp_physical"] / thousands,
        "ehp_magical": out["ehp_magical"] / thousands,
    }
    return out


def metric(prof, key):
    """One of `METRICS` off a profile; `key` may carry a `/1000g` suffix."""
    per_gold = key.endswith("/1000g")
    base = key[:-len("/1000g")] if per_gold else key
    if base.startswith("dps_"):
        prot = int(base[len("dps_"):])
        return (prof["per_1000g"]["total_dps"] if per_gold else prof["total_dps"])[prot]
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


def by_role(rows, key):
    """`{primary role: distribution}` in a fixed role order, then any other."""
    order = ["Carry", "Jungle", "Mid", "Solo", "Support"]
    groups = {}
    for row in rows:
        groups.setdefault(row["primary_role"], []).append(row)
    keys = [r for r in order if r in groups] + sorted(k for k in groups if k not in order)
    return {role: distribution(groups[role], key) for role in keys}


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
                 blind, fingerprint, out_path=REPORT_PATH, example="Medusa"):
    """Byte-for-byte deterministic, like `_calibration.md`, so its diff is a
    record of what a commit did to the builds rather than of when it ran."""
    lines = ["# Build quality — `combat.py` pointed at whole builds", ""]
    lines.append(f"_Input fingerprint: `{fingerprint}` — items, gods, tags, community builds, "
                 "weights. Regenerate with `python -m smite.build_quality`; a different fingerprint "
                 "means different inputs._")
    lines.append("")
    lines += caveat_lines(blind)
    lines.append("")
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
    lines += _dist_section(core_rows, core_skipped,
                           "3. The same, for the blended `core` (what the Balanced tab ships)",
                           "`core` carries `win` and `pick`, so it is part community build already; "
                           "the gap between this block and §2 is what the meta signal buys in "
                           "this arithmetic.")
    lines.append("")
    lines += _dist_section(priced_rows, priced_skipped,
                           "4. Sensitivity — the passives the gold model CAN price",
                           "Same as §2 with the shipped pricing flags applied to every stat line: the "
                           "Adaptive Stat grants (`price_adaptive`) and the mana conversions "
                           "(`price_conversions`). This is the one slice of the blind spot that can "
                           "be put on the table; the other "
                           f"{blind['blind']} items stay invisible here too.")
    changed = flips(rows, priced_rows)
    lines.append("")
    if changed:
        lines.append(f"Verdict on DPS vs 70 flips for {len(changed)} god(s) between §2 and §4: "
                     + ", ".join(f"{g} ({a:+.1f} → {b:+.1f})" for g, a, b in changed) + ".")
    else:
        lines.append("No god's verdict on DPS vs 70 flips between §2 and §4.")
    lines.append("")

    c, o = blind["community"], blind["ours"]
    lines += ["## 5. The blind spot, measured", "",
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

    lines += ["## 6. Every god — `model` core, printed stat lines", "",
              "C = community, O = ours. DPS vs 70 is shown as total (basic + ability).", ""]
    lines += _god_table(rows)
    lines.append("")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


# ── CLI ───────────────────────────────────────────────────────────────────

def _fingerprint(items, weights, tags_map, gods, builds_by_god):
    """`calibrate.input_fingerprint` without `_Fixture`, whose constructor
    applies the pricing flags as a side effect — this report sets them itself."""
    fx = types.SimpleNamespace(items=items, weights=weights, tags_map=tags_map,
                               gods=gods, builds_by_god=builds_by_god)
    return calibrate.input_fingerprint(fx)


def print_god(row):
    print("\n".join(worked_example(row)))


def main(argv=None):
    ap = argparse.ArgumentParser(description="combat.py pointed at whole builds, ours vs community")
    ap.add_argument("--god", help="print one god's comparison and stop")
    ap.add_argument("--archetype", default=DEFAULT_ARCHETYPE,
                    help="our build to compare (default: model)")
    ap.add_argument("--out", type=Path, default=REPORT_PATH)
    args = ap.parse_args(argv)

    items = recommend.load_items()
    gods = recommend.load_gods()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags_map = scoring.load_tags(recommend.TAGS_PATH)
    builds_by_god = {g["name"]: recommend.load_build_note(g["name"]) for g in gods}

    if args.god:
        rows, skipped = run([g for g in gods if g["name"] == args.god], items, builds_by_god,
                            weights, args.archetype)
        if not rows:
            print(f"{args.god}: not compared ({', '.join(skipped) or 'unknown god'})")
            return 1
        print_god(rows[0])
        return 0

    rows, skipped = run(gods, items, builds_by_god, weights, args.archetype)
    core_rows, core_skipped = run(gods, items, builds_by_god, weights, "core")
    priced_rows, priced_skipped = run(gods, items, builds_by_god, weights, args.archetype, priced=True)
    blind = passive_blind_spot(items, gods, builds_by_god, weights, args.archetype)
    fingerprint = _fingerprint(items, weights, tags_map, gods, builds_by_god)
    path = write_report(rows, skipped, core_rows, core_skipped, priced_rows, priced_skipped,
                        blind, fingerprint, args.out)

    d70, d170 = distribution(rows, "dps_70"), distribution(rows, "dps_170")
    print(f"{len(rows)} gods compared, {len(skipped)} skipped")
    print(f"  DPS vs 70:  ahead {d70['ahead']}, behind {d70['behind']}, "
          f"median {_pct(d70['quantiles'][50])}")
    print(f"  DPS vs 170: ahead {d170['ahead']}, behind {d170['behind']}, "
          f"median {_pct(d170['quantiles'][50])}")
    print(f"  blind: {blind['blind_share']:.0%} of the pool, "
          f"{blind['community']['share']:.0%} of community slots — read the caveat")
    print(f"  wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
