"""Done criterion 2: Ichor's build beside the community's, passives simulated.

    python -m smite.side_by_side                 # every god -> data/Analysis/_side_by_side.md
                                                 #   and viewer/public/side_by_side.json
    python -m smite.side_by_side --god Medusa    # one god, to stdout

`compare(god)` runs Ichor's `model` core (efficiency + fit, meta off — the
build the model picks having never seen a win rate) and the community's
CLEANED six (`community_six`) through `combat.py`, with every item passive
`passive_sim` can model run inside a clock rather than priced. It returns
every quantity the criterion names:

  * burst combo, and 10 seconds sustained, against a squishy and a tanky target
  * effective cooldowns and the crit expected value
  * effective health against physical and against magical damage
  * the same power figures at 2, 4 and 6 items
  * for every item only one side buys: the community's pick and win rate, what
    its passive does in numbers, and why Ichor does not buy it, in the model's
    own terms
  * a verdict under the rule in `verdict`, written down below

IT IS A DIAGNOSTIC AND FEEDS NOTHING, for the reason `build_quality` gives
(register §4.4): a damage measure that becomes a fit signal is a different
experiment. Nothing in `scoring`, `assemble`, `recommend` or `build_index`
imports this module.

THE CLOCK (`simulate`). Everything is cast at t=0 in rotation order, then
recast the moment its effective cooldown ends; basic attacks start at t=0 and
the next swing is `1 / attacks_per_second` later, re-read after every hit so a
stacking attack-speed buff speeds the clock. An ability and a swing due at the
same instant resolve ability first, which is the combo order an "empower the
next attack" item is written for. There are NO cast times — the assumption
`build_quality` prints and register §4.12 names: a god casts and swings in the
same second. That flatters ability-heavy kits that also auto-attack. It
flatters both sides of one god identically, which is why a ratio between the
two builds is the reading and the absolute figure is not.

THE BURST COMBO is every ability once plus one basic attack after them, on the
same clock with t frozen at 0. It is a declaration — the shortest sequence
that exercises both ability procs and "next attack" procs — not a measured
combo; `build_quality` refused a burst WINDOW in seconds for the same reason.

THE TARGETS ARE DATA, NOT CONSTANTS (`reference_targets`). The squishy is the
median Mid at level 20 wearing the community's own six; the tank is the median
Support the same way. Each field — base health, item health, both protections,
Plating, Dampening — is a separate median over that role. Percent-health
passives (Soul Reaver, Qin's Blade, Heartseeker) need a real health split
between base and items, which a bare "70 protection" target does not have.

THE VERDICT RULE (`judge`). The original rule (`verdict`, 2026-11-02, written
before the run): two axes, each a geometric mean of Ichor-over-community ratios:
  damage D   = sustained 10s and burst, each vs squishy and vs tank (4 ratios)
  survival S = effective health vs physical and vs magical (2 ratios)
With band b = `BAND` (5%):
  Ichor better      one axis above 1+b, the other not below 1-b
  community better  one axis below 1-b, the other not above 1+b
  trade-off         one axis above 1+b and the other below 1-b
  level             both inside the band
THE FAIRNESS PASS (2026-11-02, after a review found the six-item reading
unfair in two ways). `judge` applies, in order:
  1. kit — an aspect the community mostly plays and `combat.py` cannot play
     gives ASPECT_NOT_SIMULATED (below);
  2. coverage — under `COVERAGE_MIN` of either build's gold fully simulated,
     or a gap over `COVERAGE_GAP`, gives NOT_ENOUGH_SIMULATED (the evidence for
     both numbers is beside them);
  3. phase — ahead at 2+4 items and behind at six on the composite
     sqrt(D x S), each outside the band, is EARLY_GAME (the reverse LATE_GAME);
  4. otherwise `verdict` on D and S as the `BREAKPOINT_WEIGHTS`-weighted
     geometric mean of the 2-, 4- and 6-item axes.
`judge_six_only` is the old rule, kept so the page prints old against new.
Stacks follow the game clock (the FIGHT block: `MINUTES_PER_ITEM`,
`STACK_MINUTES_TO_FULL`); the report prints the old none/full ends and the
clock at two other times-to-full beside it.

THE FIGHT (2026-11-02). Kills, assists, an enemy on our god and "On Use"
presses are events in the clock, each under a written assumption in the
FIGHT block below; effective health is the raw damage that enemy deals before
our bar is gone (equal to the static integral when nothing in the build
reacts — tested).
THE KIT IS MATCHED FIRST (2026-11-02, Jacob). The community six is what
players built on the kit they played. Where more than `ASPECT_MAJORITY` of
this god's community games are on an aspect, that aspect is the fair kit for
the comparison. `combat.py` simulates no aspect kit change (`SIMULATED_ASPECTS`
is empty, and saying so is the point), so those gods get the verdict
`ASPECT_NOT_SIMULATED`: their base-kit numbers are still shown, labelled, but
they get no verdict and are left out of every count. A base-kit comparison is
never presented as fair against an aspect build. Every comparison carries
`kit`: which kit was used and the aspect's pick rate.
Gold is not an axis: both are finished builds, and the per-gold reading is
`build_quality`'s. `verdict_counts` re-runs the rule at 2% and 10% so a reader
can see how much of the split the band chose.

WHAT IS NOT IN IT, and the page prints it: crowd control, peel, mobility,
health-regen sustain, allies, waves, objectives, and every passive
`passive_sim` marks `not simulated` — listed per build, per item, with the
reason.
"""
import argparse
import json
import math
import re
import statistics
import sys
from dataclasses import dataclass, field
from pathlib import Path

from smite import (build_quality as bq, combat, community_target, damage_value, efficiency,
                   passive_sim, recommend, scoring)

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = REPO_ROOT / "data" / "Analysis" / "_side_by_side.md"
JSON_DIR = REPO_ROOT / "viewer" / "public" / "side_by_side"

LEVEL = 20
WINDOW = 10.0
BREAKPOINTS = (2, 4, 6)
BAND = 0.05
SENSITIVITY_BANDS = (0.02, 0.05, 0.10)
ARCHETYPE = "model"

#: An aspect played in more than this share of the god's community games is
#: the kit the community build was made for. "Mostly plays" — a majority.
ASPECT_MAJORITY = 0.5
#: Aspects whose kit change `combat.py` simulates. None today: the scrape
#: carries aspect TEXT, and turning it into arithmetic is per-aspect work.
SIMULATED_ASPECTS = frozenset()
ASPECT_NOT_SIMULATED = "aspect not simulated"
SQUISHY_ROLE, TANK_ROLE = "Mid", "Support"

#: SIMULATION COVERAGE (2026-11-02). A passive the clock cannot run is worth
#: ZERO here, so the build holding more of them looks worse for a reason that
#: is not the build. `simulated_share` is the share of a build's gold in items
#: whose passive is fully simulated or that have none; PARTIAL and NOT
#: SIMULATED items count as missing. Whole-item gold is an upper bound on
#: what is missing (an item's STATS always run), and it is used because no
#: tighter split is measurable here: fitting stat prices on the items with no
#: passive and reading a passive's price as cost minus its stats gives a
#: NEGATIVE passive price on 7 of 10 tier-3 items (tier 3 carries more stat
#: per gold than components), and the shipped residual fit absorbs the passive
#: into the stats (Jotunn's Revenge's passive prices at 0g). Both were tried.
#:
#: The gap is DERIVED, not chosen: the median simulated passive in a compared
#: build moves the damage axis by 5.8% (506 passives, 2026-11-02), more than
#: the whole verdict band, so one item of coverage gap (~1/6 of a build's
#: gold) can flip a verdict on its own. COVERAGE_GAP = BAND / (6 x 5.8%) is the
#: gap at which the median stand-in moves the axis by exactly the band.
#: COVERAGE_MIN is "most of each build's gold is simulated": below half, the
#: verdict is more assumption than computation. Either test failing withholds
#: the verdict as NOT_ENOUGH_SIMULATED; the numbers and the verdict the rule
#: WOULD give (`verdict_unwithheld`) are still shown.
COVERAGE_MIN = 0.50
COVERAGE_GAP = 0.14
NOT_ENOUGH_SIMULATED = "not enough simulated"

#: EARLY GAME (2026-11-02). The verdict weighs the 2-, 4- and 6-item points
#: equally: each axis is the weighted geometric mean of the per-point axes.
#: Equal thirds because each power spike is held for roughly a third of a
#: Conquest game, and the record argues AGAINST weighting the finished six
#: up — the community's slot 6 is a half-built component on 61 of 90 gods,
#: i.e. most games end before six items exist. Stacking passives are on the
#: game clock at every point (`stack_state`, the FIGHT block).
BREAKPOINT_WEIGHTS = {2: 1 / 3, 4: 1 / 3, 6: 1 / 3}
#: A god whose early points (2 and 4 items, equal weight) and finished six
#: point opposite ways on the composite sqrt(damage x survival), each outside
#: the band, gets a PHASE verdict instead of win/lose. Named from Ichor's side:
#: "early-game build" = Ichor's build is ahead early and behind at six.
EARLY_GAME = "early-game build"
LATE_GAME = "late-game build"

# ── THE FIGHT BLOCK (2026-11-02) ──────────────────────────────────────────
# Until this block the duel held no kill, no enemy hitting our god and no
# "On Use" press, so every item gated on one read zero and was NOT SIMULATED
# — 378 unsimulated item slots on Ichor's side against the community's 244,
# which withheld 75 of 87 verdicts. Each assumption below is chosen ONCE, is
# the same for both builds of a god, and is printed on the page. None was
# tuned against a verdict; the report's sensitivity lines re-run the counts
# with each one moved.
#
# KILL_RULE. The target dies when our damage in the fight reaches its max
# health: ONE kill per fight of WINDOW seconds (an effective-health run that
# lasts longer is a run of consecutive fights, each with a fresh target and
# at most one kill). Damage past the kill still counts toward the sustained
# figure, as it always has (the window measures output, the sponge keeps its
# debuffs), so no build without a takedown item moves. A first draft counted
# a kill at EVERY multiple of max health and gave a carry ~5 kills in 10s —
# a sponge, not a fight — and was dropped before any verdict was read. A
# burst has no kills (a combo declared at t=0, nothing after it to refund).
#
#: ASSISTS. One assist every ASSIST_INTERVAL seconds of the sustained window
#: and of the effective-health run, the first at ASSIST_FIRST. A 10s window
#: that is a fight with teammates in it holds at least one teammate takedown
#: our god is part of; one per window is the least non-zero reading, and the
#: middle of the window is the mean arrival of one uniform event. It does not
#: depend on either build — both get the same assists at the same instants —
#: so it cannot be tuned toward a side. `--no-assists` style sensitivity is in
#: the report ("assists off").
ASSIST_INTERVAL = 10.0
ASSIST_FIRST = 5.0
#
#: THE ENEMY. Someone hits our god: physical as basic attacks, magical as
#: ability hits. Its raw DPS per damage type is the reference SQUISHY's
#: effective health against that type over WINDOW — an enemy exactly as
#: lethal as the comparison asks our god to be (kill the median Mid in 10s).
#: The cadence is data too: attacks at the median community Carry's attack
#: speed, ability hits at the median community Mid's casts per second
#: (`attacker_profile`). In the sustained window the enemy deals each type at
#: ENEMY_SHARE of that DPS (no record of the enemy team says otherwise; an
#: even split favours neither Genji's Guard's magical trigger nor Kinetic
#: Cuirass's physical one). In an effective-health run it deals ONE type at
#: full DPS until our bar is gone. Static items read exactly what they read
#: before: the DPS sets WHEN things happen, never how much raw damage a
#: static bar absorbs (`test_fight_ehp_equals_static_when_nothing_moves`).
#: Our god's damage does not stop if it dies inside the window — survival is
#: the other axis, and the two are not multiplied here. Health regen,
#: Plating and Dampening on our side are not in it (they were not in
#: effective health before either). Lifesteal and heals are, since the
#: HEALING block below.
ENEMY_SHARE = 0.5
#
# ── THE HEALING BLOCK (2026-11-03) ────────────────────────────────────────
# Until this block nothing in the clock healed except three item hooks, and
# the target never healed at all, so lifesteal, heal-on-hit items and every
# anti-heal item read zero: sustain and its counter, the two things the
# Joust and Arena profiles move most, were invisible to the comparison.
# Each side now has a healing-received channel:
#
#   OUR GOD heals off its Lifesteal on EVERY damage instance it deals to the
#   target (attack, ability, item proc, aura, active): `combat.
#   lifesteal_healing` at the vs-god rate. "Lifesteal" with no qualifier is
#   read as all damage dealt — the literal reading; no SMITE 2 source here
#   states an ability or proc discount, and inventing one would be a
#   constant. Heal-on-hit items (Shield of the Phoenix, Soul Gem, The Reaper,
#   Amanita Charm, Gluttonous Grimoire's stored damage, Bloodforge and
#   Blood-Bound Book's shield-lifesteal) land through the same `heal`. Every
#   heal is cut by the enemy TEAM's expected healing reduction, `attacker.
#   anti_heal` (`team_anti_heal`): 40% times the chance at least one of five
#   enemies, one per role, holds an anti-heal item in its community six. A
#   team because the reduction does not stack, so who applies it does not
#   matter. On 2026-11-03 data only 3 of 94 community sixes hold one (2 Solo,
#   1 Jungle), so the cut is ~6%. Overheal is wasted, so a heal at full
#   health books nothing.
#
#   THE TARGET heals off ITS lifesteal on the damage the enemy deals our god
#   — the target is the enemy hitting back, one opponent, not two — through
#   OUR anti-heal (`passive_sim.ANTI_HEAL`: live for 5s after the trigger,
#   the strongest one only). Its lifesteal is the MEAN over the reference
#   role's community sixes, not the median every other target field uses: a
#   median of a field most Mids leave at zero is zero, which would hide an
#   effect a third of them carry, and expected healing is linear in the
#   stat. A heal cannot exceed what our damage has taken off it this fight.
#
# What it moves: the SUSTAINED figure is now NET damage (dealt minus the
# target's healing), and the kill rule counts net damage too, so anti-heal
# reads on the damage axis; our healing lands in the fight's health bar, so
# lifesteal reads on the survival axis (`fight_ehp`). A burst has no enemy,
# so nothing heals in it. Health REGEN is still out: a per-second trickle
# over a 10s window is small, and both builds' bases carry the same regen.
HEALING = True
#: Heals land only before this many seconds of a run. Unbounded in the
#: verdict; the report re-runs the counts at one WINDOW (healing inside the
#: first fight only), because an effective-health run is a chain of
#: consecutive 10s fights and lifesteal compounds over the chain.
HEAL_UNTIL = math.inf
#: An effective-health run stops here if our god is still alive (it never is
#: at these DPS; the remainder of the bar is then added statically).
EHP_RUN_CAP = 600.0
#
#: ACTIVES. Every "On Use" item in a compared build is pressed the first
#: moment its condition holds and again the moment its cooldown ends; the
#: condition is written beside each in `passive_sim`. A press refused (Death
#: Metal on a magical god; Pendulum Blade with nothing on cooldown) is
#: retried after ACTIVE_RETRY seconds — a quarter second, finer than any
#: cooldown and any attack interval in the roster. An active that is only
#: crowd control, movement or an ally link stays NOT SIMULATED, named.
ACTIVE_RETRY = 0.25
#: Sanguine Lash's active tick, "every 0.33s" off its text.
SANGUINE_FAST = 0.33
#
#: THE GAME CLOCK FOR STACKS (2026-11-02). PR #77 held persistent stacks at
#: ZERO at 2 and 4 items and FULL at six, the two ends. Now each finished item
#: is bought MINUTES_PER_ITEM after the last, so the k-th completes at minute
#: k x MINUTES_PER_ITEM, and each breakpoint is read the moment it is reached.
#: 5 minutes because six items land near minute 30: the last measured SMITE
#: Conquest average was 29 minutes (SMITE 1 community stats, 2022); SMITE 2
#: guides give 25-45; and the community's slot 6 is a half-built component on
#: 61 of 90 gods, i.e. games end about when the sixth would complete. Even
#: pacing ignores that early gold is slower; the six-item point is unaffected
#: by that and the early points err toward MORE stacks, which favours the
#: community (it front-loads stacking items).
MINUTES_PER_ITEM = 5.0
#: A stacking item is full this many minutes after it is bought (Devourer's,
#: Thebes, Book of Thoth, Transcendence, Rage — each fills off minions, damage
#: to minions or god takedowns). NOT MEASURED: no farm or takedown rate is in
#: this repo. 10 is the order of a laner's farm: 75 Devourer's stacks at ~8
#: last hits a minute; 50 Thoth stacks of 900 damage each (45,000) to minions;
#: Rage's 5 takedowns at ~1 per 2 minutes, the rate of ~15 takedowns in a
#: 30-minute game. The report brackets it at STACK_MINUTES_BRACKET.
STACK_MINUTES_TO_FULL = 10.0
STACK_MINUTES_BRACKET = (5.0, 20.0)


def stack_state(names, k, minutes_to_full=STACK_MINUTES_TO_FULL):
    """`{item: fraction of full}` at the k-item breakpoint for every stacking
    item among the first k: bought at minute j x MINUTES_PER_ITEM (slot j,
    1-based), read at minute k x MINUTES_PER_ITEM, linear to full."""
    out = {}
    for j, n in enumerate(names[:k], start=1):
        held = (k - j) * MINUTES_PER_ITEM
        out[n] = min(1.0, held / minutes_to_full) if minutes_to_full > 0 else 1.0
    return out


# "Range: 8.8 meters" on the Basic Attack. The roster splits into 1.92/2.56
# (44 gods) and 5.6/6.4/8.8 (46), so any threshold in the gap gives the same
# split; 4.0 is the gap's middle and changes nothing if moved within it.
_RANGE = re.compile(r"Range:\s*([\d.]+)")
MELEE_RANGE = 4.0


def is_melee(god):
    """True / False from the basic attack's scraped range, None if unparsed."""
    for a in god.get("abilities") or []:
        if "Basic Attack" not in (a.get("slot") or ""):
            continue
        for line in a.get("details") or []:
            m = _RANGE.search(line)
            if m:
                return float(m.group(1)) < MELEE_RANGE
    return None


# ── Stats ─────────────────────────────────────────────────────────────────

def printed_totals(names, items_by_name):
    """`(totals, gold)` off the printed stat lines, with every pricing flag
    OFF — a priced passive here would be counted twice, once as a stat and
    once by its simulator."""
    before = efficiency.apply_pricing_flags({})
    try:
        return bq.build_totals(names, items_by_name)
    finally:
        efficiency.restore_pricing_flags(before)


def simulated_share(names, items_by_name):
    """Share of the build's gold in items the clock models fully (see
    `COVERAGE_MIN`)."""
    total = ok = 0.0
    for n in names:
        gold = float(items_by_name[n].get("cost") or 0.0)
        total += gold
        if passive_sim.lookup(items_by_name[n]).status in (passive_sim.SIMULATED, passive_sim.NO_PASSIVE):
            ok += gold
    return ok / total if total else 1.0


def passives_for(names, items_by_name, disabled=()):
    return [(n, passive_sim.lookup(items_by_name[n])) for n in names if n not in disabled]


def build_stats(names, items_by_name, level=LEVEL, stacks="full", disabled=()):
    """Printed totals, then every passive's `grants`, then every `converts`,
    in build order. Returns `(stats, item_totals, gold)`."""
    items, gold = printed_totals(names, items_by_name)
    stats = dict(items)
    plist = passives_for(names, items_by_name, disabled)
    for phase in ("grants", "converts"):
        for name, p in plist:
            hook = getattr(p, phase)
            if hook is None:
                continue
            ctx = passive_sim.StatContext(items=items, stats=dict(stats), level=level,
                                          stacks=stacks, names=tuple(names))
            for k, v in (hook(ctx) or {}).items():
                stats[k] = stats.get(k, 0.0) + v
    return stats, items, gold


# ── The clock ─────────────────────────────────────────────────────────────

@dataclass
class Event:
    t: float
    kind: str                # "attack" | "ability"
    name: str
    raw: float
    is_ultimate: bool = False
    attack_index: int = -1
    multiplier: float = 1.0
    uncapped_pct_pen: float = 0.0
    procs: list = field(default_factory=list)


class Sim:
    """One build on one god against one target over one window.

    `enemy` turns on the FIGHT block's attacker: "both" (the sustained
    window: each damage type at `ENEMY_SHARE` of its DPS), "physical" or
    "magical" (an effective-health run, at full DPS). It needs the target to
    carry an `attacker` profile (`reference_targets`); toy targets without one
    get no enemy. `takedowns` turns on kills and assists (off in a burst)."""

    def __init__(self, god, names, items_by_name, target, *, window=WINDOW, level=LEVEL,
                 stacks="full", disabled=(), enemy=None, takedowns=None):
        self.god, self.names, self.level, self.target = god, list(names), level, target
        self.window = window
        self.stacks = stacks
        self.damage_type = (god.get("damage_type") or "physical").lower()
        self.melee = is_melee(god)
        self.base_stats, self.item_totals, self.gold = build_stats(
            names, items_by_name, level, stacks, disabled)
        self.passives = passives_for(names, items_by_name, disabled)
        self.active = {n for n, _ in self.passives}
        self.dynamic, self.state, self.shreds = {}, {}, {}
        self.t = 0.0
        self._current_item = None
        self._after = []
        self.by_channel = {"attack": 0.0, "ability": 0.0, "proc": 0.0}
        self.by_item = {}
        self.attack_power = combat.god_attack_power(god, level)
        chain = combat.attack_chain_multipliers(god)
        self.mean_swing = sum(chain) / len(chain) if chain else 1.0
        self.attack_scaling = damage_value._basic_attack_scaling(god)
        self.base_aps = bq.base_attack_speed(god, level)
        self.crit_mult = combat.CRIT_MULTIPLIER + (
            combat.DEATHBRINGER_CRIT_BONUS if "Deathbringer" in self.active else 0.0)
        ult_mod = 1.0
        for _, p in self.passives:
            if p.cooldown:
                ult_mod *= p.cooldown(None).get("ultimate", 1.0)
        rotation, self.dropped = bq.ability_rotation(god)
        cdr = self.base_stats.get("Cooldown Rate", 0.0)
        self.rotation = [dict(a, effective_cooldown=a["cooldown"] * (ult_mod if a["is_ultimate"] else 1.0)
                              * combat.cooldown_multiplier(cdr)) for a in rotation]
        self.nxt = {}
        # stat hooks, read on every stat lookup
        self._bonus = [(set(p.bonus_keys), p.stat_bonus) for _, p in self.passives if p.stat_bonus]
        self._bonus_keys = set().union(*(k for k, _ in self._bonus)) if self._bonus else set()
        # the fight layer
        self.enemy = enemy if target.get("attacker") else None
        self.takedowns = (window is not None) if takedowns is None else takedowns
        self.dealt, self.kills, self.assists = 0.0, 0, 0
        self._fight, self._fight_start, self._fight_killed = 0, 0.0, False
        self.casts, self.kill_times = [], []   # (t, ability) and t, for tests and the page
        base = god.get("base_stats") or {}
        self.max_health = bq.level_value(base.get("health"), level) + self.base_stats.get("Max Health", 0.0)
        self.hp = self.max_health
        self.own_prot = {
            "physical": bq.level_value(base.get("physical_prot"), level)
            + self.base_stats.get("Physical Protection", 0.0),
            "magical": bq.level_value(base.get("magical_prot"), level)
            + self.base_stats.get("Magical Protection", 0.0)}
        self.health_lost, self.absorbed = 0.0, 0.0
        self.shields = {}
        # HEALING block: both sides' healing-received channels.
        self.healed, self.heal_by_item = 0.0, {}
        self.heal_cut = (target["attacker"].get("anti_heal", 0.0)
                         if self.enemy and HEALING else 0.0)
        self.target_lifesteal = target.get("lifesteal", 0.0) if HEALING else 0.0
        self.target_healed, self._fight_heal_start = 0.0, 0.0
        self.anti_heal = [(n, *passive_sim.ANTI_HEAL[n]) for n in self.active
                          if n in passive_sim.ANTI_HEAL] if HEALING else []
        self.anti_heal_until, self.anti_heal_live = -1.0, 0.0
        self.gluttonous = "Gluttonous Grimoire" in self.active
        self._segments, cuts = [], {0.0, 1.0}
        for _, p in self.passives:
            if p.ehp_segments and not p.prot_bonus:
                lost, spans = 0.0, []
                for share, ep, em in p.ehp_segments(None):
                    spans.append((lost, lost + share, ep, em))
                    lost += share
                    cuts.add(round(lost, 9))
                self._segments.append(spans)
        self._cuts_hp = sorted({self.max_health * (1.0 - c) for c in cuts}, reverse=True)
        self.actives = [(n, p) for n, p in self.passives if p.active]
        self.active_ready = {n: 0.0 for n, _ in self.actives}

    # stats at the current instant
    def _stat_raw(self, key):
        v = self.base_stats.get(key, 0.0) + self.dynamic.get(key, 0.0)
        if "Brawler’s Beat Stick" in self.active and key in ("Strength", "Intelligence"):
            # "While in Combat: +2% Strength, +2% Intelligence ... every 1.5s.
            # Stacks up to 5 times." Combat starts at t=0, first stack at 1.5s.
            v *= 1.0 + 0.02 * min(5, int(self.t // 1.5))
        if key in self._bonus_keys:
            for keys, fn in self._bonus:
                if key in keys:
                    v = fn(self, key, v)
        return v

    def _death_metal_on(self):
        st = self.state.get("Death Metal")
        return bool(st) and self.t < st["until"]

    def stat(self, key):
        if self._death_metal_on() and key in ("Intelligence", "Strength", "Critical Chance %"):
            # Death Metal's active: "Lose all Intelligence. Gain 66% of it as
            # Strength. +25% Crit Chance"
            if key == "Intelligence":
                return 0.0
            if key == "Strength":
                return self._stat_raw("Strength") + 0.66 * self._stat_raw("Intelligence")
            return self._stat_raw(key) + 25.0
        return self._stat_raw(key)

    @property
    def stats(self):
        keys = set(self.base_stats) | set(self.dynamic) | self._bonus_keys
        if "Death Metal" in self.active:
            keys |= {"Strength", "Critical Chance %"}
        return {k: self.stat(k) for k in keys}

    def attacks_per_second(self):
        return combat.attacks_per_second(self.base_aps, self.stat("Attack Speed %"))

    def crit_chance(self):
        return min(self.stat("Critical Chance %"), 100.0) / 100.0

    def crit_ev(self):
        return 1.0 + self.crit_chance() * (self.crit_mult - 1.0)

    def swing_raw(self):
        return combat.attack_damage(self.attack_power, self.attack_scaling, self.stats, self.mean_swing)

    def item_state(self, item, **defaults):
        return self.state.setdefault(item, dict(defaults))

    def add_shred(self, item, pct, max_stacks, duration, t):
        """A protection-reduction stack. Call it through `after`, so it lands
        after the hit that applies it.
        Each application refreshes the whole stack's duration — the usual
        behaviour of a stacking debuff; the texts say only "for 4s" and
        "stacks up to N", and a per-stack expiry would drop a stack on an
        exactly-4s cadence for no stated reason."""
        stacks, _, until, _ = self.shreds.get(item, (0, 0.0, -1.0, pct))
        stacks = stacks + 1 if t <= until else 1
        self.shreds[item] = (min(stacks, max_stacks), t, t + duration, pct)

    def shred_at(self, t):
        return sum(stacks * pct for stacks, start, until, pct in self.shreds.values()
                   if start <= t <= until)

    def after(self, fn):
        """Run `fn` once the current hit and its procs have been dealt."""
        self._after.append(fn)

    def proc(self, amount, dtype, ev, item=None):
        ev.procs.append((amount, dtype, item or self._current_item))

    def amplification(self, t):
        st = self.state.get("Spear of the Magus")
        return 1.05 if st and "from" in st and st["from"] <= t <= st["until"] else 1.0

    # the arithmetic, delegated to combat wherever combat already has it
    def mitigated(self, raw, dtype, t, *, kind, uncapped=0.0):
        if dtype == "true":
            return raw * self.amplification(t)
        prot = self.target["physical_prot" if dtype == "physical" else "magical_prot"]
        flat = min(self.stat("Penetration"), combat.FLAT_PEN_CAP)
        pct = min(min(self.stat("Penetration %") / 100.0, combat.PCT_PEN_CAP) + uncapped, 1.0)
        eff = max(0.0, prot * (1.0 - self.shred_at(t)) * (1.0 - pct) - flat)
        out = raw * combat.mitigation(eff) * self.amplification(t)
        if kind == "attack":
            out *= combat.flat_reduction_multiplier(self.target.get("plating", 0.0), combat.PLATING_CAP)
        elif kind == "ability":
            out *= combat.flat_reduction_multiplier(self.target.get("dampening", 0.0), combat.DAMPENING_CAP)
        return out

    # ── damage dealt, and the kills it makes ──
    def _deal(self, amount, channel, item=None):
        fight = int(self.t // WINDOW)
        if fight != self._fight:   # a new fight: fresh target, no kill yet
            self._fight, self._fight_start, self._fight_killed = fight, self.dealt, False
            self._fight_heal_start = self.target_healed
        self.by_channel[channel] += amount
        if item is not None:
            self.by_item[item] = self.by_item.get(item, 0.0) + amount
        self.dealt += amount
        if not HEALING or amount <= 0:
            return
        # Anti-heal lands on the target with the damage (HEALING block).
        for _, cut, seconds, trigger in self.anti_heal:
            if trigger == "any" or channel == "attack":
                if self.t > self.anti_heal_until:
                    self.anti_heal_live = 0.0
                self.anti_heal_live = max(self.anti_heal_live, cut)
                self.anti_heal_until = self.t + seconds
        # Lifesteal: a share of EVERY damage instance to a god (`combat.
        # lifesteal_healing`, the vs-god rate), read off the stat right now —
        # but only on damage to a LIVE target. Past this fight's kill the
        # damage still counts toward output (the sponge, KILL_RULE), yet
        # there is no god left to steal from; without this a 10s fight's
        # lifesteal ran on a corpse and a 30% lifesteal build out-healed the
        # enemy forever (Ishtar's community six read 8x its static EHP).
        ls = self.stat("Lifesteal %")
        alive = self.target["max_health"] - (
            (self.dealt - amount - self._fight_start) - (self.target_healed - self._fight_heal_start))
        if ls > 0 and alive > 0:
            nominal = combat.lifesteal_healing(min(amount, alive), ls)
            if self.gluttonous:
                passive_sim._gluttonous_store(self, nominal)
            self.heal(nominal, item="Lifesteal")

    def _check_kills(self):
        """At most one kill per fight of WINDOW seconds: when our damage
        since that fight began reaches the target's max health (FIGHT block,
        KILL_RULE)."""
        if not self.takedowns:
            return
        net = (self.dealt - self._fight_start) - (self.target_healed - self._fight_heal_start)
        if not self._fight_killed and net >= self.target["max_health"]:
            self._fight_killed = True
            self.kills += 1
            self.kill_times.append(self.t)
            self._takedown("kill")

    def _takedown(self, kind):
        for name, p in self.passives:
            if p.on_takedown:
                self._current_item = name
                p.on_takedown(self, kind)

    def active_damage(self, amount, dtype, item=None):
        """Damage from an active (or a reflect): mitigated as a proc, booked
        to its item, counted toward kills."""
        name = item or self._current_item
        self._deal(self.mitigated(amount, dtype, self.t, kind="proc"), "proc", name)
        self._check_kills()

    # ── cooldowns ──
    def refund(self, non_ult, ult):
        """Take seconds off every ability still on cooldown, never past now."""
        for i, a in enumerate(self.rotation):
            if i in self.nxt and self.nxt[i] > self.t:
                self.nxt[i] = max(self.t, self.nxt[i] - (ult if a["is_ultimate"] else non_ult))

    def any_on_cooldown(self):
        return any(v > self.t for v in self.nxt.values())

    def ready_active(self, name):
        if name in self.active_ready:
            self.active_ready[name] = min(self.active_ready[name], self.t)

    def shorten_active(self, name, seconds):
        if name in self.active_ready:
            self.active_ready[name] = max(self.t, self.active_ready[name] - seconds)

    def _press(self, trigger):
        for name, p in self.actives:
            if p.active_trigger != trigger or self.t < self.active_ready[name]:
                continue
            self._current_item = name
            if p.active(self):
                self.active_ready[name] = self.t + p.active_cooldown

    def _next_active(self, trigger):
        times = [self.active_ready[n] for n, p in self.actives if p.active_trigger == trigger]
        return min(times) if times else math.inf

    # ── our god's health ──
    def heal(self, amount, item=None):
        """Heal our god: the enemy's expected healing reduction first
        (`heal_cut`), then capped at max health. Books what LANDED."""
        if self.t >= HEAL_UNTIL:
            return
        amount = combat.healing_received(amount, (self.heal_cut,))
        landed = max(0.0, min(self.max_health - self.hp, amount))
        self.hp += landed
        self.healed += landed
        name = item or self._current_item or "?"
        self.heal_by_item[name] = self.heal_by_item.get(name, 0.0) + landed

    def target_cut(self):
        """The healing reduction live on the TARGET now (ours)."""
        return self.anti_heal_live if self.t <= self.anti_heal_until else 0.0

    def _target_heal(self, damage_to_us):
        """The target lifesteals off the damage it deals our god (it IS the
        enemy hitting us), through our anti-heal, capped at what our damage
        this fight has taken off it."""
        if self.target_lifesteal <= 0 or damage_to_us <= 0:
            return
        heal = combat.healing_received(combat.lifesteal_healing(damage_to_us, self.target_lifesteal),
                                       (self.target_cut(),))
        missing = ((self.dealt - self._fight_start)
                   - (self.target_healed - self._fight_heal_start))
        heal = min(heal, max(0.0, missing))
        self.target_healed += heal
        if heal > 0 and "Stygian Anchor" in self.active and self.target_cut() > 0:
            # "5% of their Healing Echoed to you"
            self.heal(0.05 * heal, item="Stygian Anchor")

    def add_shield(self, name, amount, until):
        self.shields[name] = (amount, until)

    def shield_up(self, name):
        s = self.shields.get(name)
        return bool(s) and s[0] > 0 and self.t < s[1]

    def prot_now(self, dtype, hp=None):
        """Our protection against `dtype` at health `hp` (default: now). Read
        it at a slice's MIDPOINT, as the static integral does."""
        hp = self.hp if hp is None else hp
        lost = 1.0 - hp / self.max_health if self.max_health else 1.0
        extra = 0.0
        for spans in self._segments:
            for lo, hi, ep, em in spans:
                if lo <= lost < hi:
                    extra += ep if dtype == "physical" else em
                    break
        for _, p in self.passives:
            if p.prot_bonus:
                extra += p.prot_bonus(self, dtype)
        return self.own_prot[dtype] + extra

    def mitigation_now(self, dtype):
        return combat.mitigation(self.prot_now(dtype))

    def take_hit(self, raw, dtype, kind):
        """One enemy hit of `raw` pre-mitigation damage. Shields take it
        first, then health, slice by slice at the protection each slice
        carries — exactly the static integral when nothing moves. Adds to
        `absorbed` (raw damage taken) and `health_lost`."""
        hit = {"raw": raw, "dtype": dtype, "kind": kind}
        for name, p in self.actives:
            if p.active_trigger == "hit_taken" and self.t >= self.active_ready[name]:
                self._current_item = name
                if p.active(self):
                    self.active_ready[name] = self.t + p.active_cooldown
        mult = 1.0
        for _, p in self.passives:
            if p.reduce_hit:
                mult *= p.reduce_hit(self, hit)
        left = raw * mult
        self.absorbed += raw - left
        lost_before = self.health_lost
        shield_before = sum(a for a, _ in self.shields.values())
        while left > 1e-9 and self.hp > 1e-9:
            floor = next((c for c in self._cuts_hp if c < self.hp - 1e-9), 0.0)
            m = 1.0 + self.prot_now(dtype, (self.hp + floor) / 2) / 100.0
            live = [(n, s) for n, s in self.shields.items() if s[0] > 1e-9 and self.t < s[1]]
            if live:
                n, (amt, until) = live[0]
                take = min(amt, left / m)
                self.shields[n] = (amt - take, until)
                left -= take * m
                self.absorbed += take * m
                continue
            drop = self.hp - floor
            if left >= drop * m:
                self.hp, left = floor, left - drop * m
                self.absorbed += drop * m
                self.health_lost += drop
            else:
                d = left / m
                self.hp -= d
                self.absorbed += left
                self.health_lost += d
                left = 0.0
        if HEALING:
            taken = (self.health_lost - lost_before) + max(
                0.0, shield_before - sum(a for a, _ in self.shields.values()))
            self._target_heal(taken)
        for name, p in self.passives:
            if p.on_hit_taken:
                self._current_item = name
                p.on_hit_taken(self, hit)

    def remaining_ehp(self, dtype):
        """Raw damage the rest of the bar (and any live shield) would take,
        statically, at the protection each slice carries now."""
        out, hp = 0.0, self.hp
        for amt, until in self.shields.values():
            if self.t < until:
                out += amt * (1.0 + self.prot_now(dtype) / 100.0)
        for floor in [c for c in self._cuts_hp if c < hp - 1e-9] + [0.0]:
            if hp > floor:
                out += (hp - floor) * (1.0 + self.prot_now(dtype, (hp + floor) / 2) / 100.0)
                hp = floor
        return out

    def _resolve(self, ev):
        hooks = [(n, p.on_attack if ev.kind == "attack" else p.on_ability)
                 for n, p in self.passives]
        for name, hook in hooks:
            if hook:
                self._current_item = name
                hook(self, ev)
        if ev.kind == "attack":
            p = self.crit_chance()
            hit = self.mitigated(ev.raw * ev.multiplier, self.damage_type, ev.t, kind="attack",
                                 uncapped=ev.uncapped_pct_pen)
            hit *= 1.0 + p * (self.crit_mult - 1.0)
        else:
            hit = self.mitigated(ev.raw * ev.multiplier, self.damage_type, ev.t, kind="ability",
                                 uncapped=ev.uncapped_pct_pen)
            hit *= combat.echo_multiplier(self.stat("Echo"), ev.is_ultimate)
        self._deal(hit, ev.kind)
        for amount, dtype, item in ev.procs:
            self._deal(self.mitigated(amount, dtype, ev.t, kind="proc"), "proc", item)
        pending, self._after = self._after, []
        for fn in pending:
            fn()
        self._check_kills()

    def _attack(self, t, index):
        self.t = t
        raw = combat.attack_damage(self.attack_power, self.attack_scaling, self.stats, self.mean_swing)
        self._resolve(Event(t, "attack", "Basic Attack", raw, attack_index=index))

    def _ability(self, t, a):
        self.t = t
        self.casts.append((t, a["name"]))
        raw = combat.ability_damage(a["base"], a["scaling"], self.stats)
        self._resolve(Event(t, "ability", a["name"], raw, is_ultimate=a["is_ultimate"]))

    def _aura(self, t):
        if "Sanguine Lash" in self.active:
            self.t = t
            d = self.mitigated(passive_sim._sanguine(self, t), "physical", t, kind="proc")
            self._deal(d, "proc", "Sanguine Lash")
            self._check_kills()

    def _enemy_schedule(self):
        """`[(next_t, interval, raw_per_hit, dtype, kind)]` for the enemy."""
        if not self.enemy:
            return []
        prof = self.target["attacker"]
        out = []
        for dtype, kind in (("physical", "attack"), ("magical", "ability")):
            if self.enemy not in ("both", dtype):
                continue
            share = ENEMY_SHARE if self.enemy == "both" else 1.0
            step = prof["interval"][kind]
            out.append([0.0, step, prof["raw_dps"][dtype] * share * step, dtype, kind])
        return out

    def run_window(self, until_dead=False):
        """Event order at one instant: "start" actives, abilities (rotation
        order), "after_casts" actives, the swing, the aura, an assist, then
        the enemy's hits. Aura ticks at whole seconds up to and including the
        window's end. With `until_dead`, runs until the enemy has taken our
        god's whole bar (or the window ends) and returns raw damage taken."""
        self.nxt = {i: 0.0 for i in range(len(self.rotation))}
        next_attack, index = 0.0, 0
        aura = 1.0 if "Sanguine Lash" in self.active else math.inf
        assist = ASSIST_FIRST if self.takedowns else math.inf
        foes = self._enemy_schedule()
        while True:
            if until_dead and self.hp <= 1e-9:
                break
            options = []
            ts = self._next_active("start")
            if ts < self.window:
                options.append((ts, -1, "start", None))
            if self.nxt:
                i = min(self.nxt, key=lambda k: (self.nxt[k], k))
                if self.nxt[i] < self.window:
                    options.append((self.nxt[i], 0, "ability", i))
            ta = self._next_active("after_casts")
            if ta < self.window:
                options.append((ta, 0.5, "after_casts", None))
            if next_attack < self.window:
                options.append((next_attack, 1, "attack", None))
            if aura <= self.window:
                options.append((aura, 2, "aura", None))
            if assist < self.window:
                options.append((assist, 3, "assist", None))
            for j, f in enumerate(foes):
                if f[0] < self.window:
                    options.append((f[0], 4 + j, "enemy", j))
            if not options:
                break
            t, _, kind, i = min(options)
            if kind == "ability":
                self._ability(t, self.rotation[i])
                self.nxt[i] = t + self.rotation[i]["effective_cooldown"]
            elif kind == "attack":
                self._attack(t, index)
                index += 1
                aps = self.attacks_per_second()
                next_attack = t + (1.0 / aps if aps > 0 else math.inf)
            elif kind == "aura":
                self._aura(t)
                # Sanguine Lash's active: "Now damages every 0.33s for 4s";
                # otherwise the aura ticks on whole seconds.
                st = self.state.get("Sanguine Lash")
                if st and t + SANGUINE_FAST <= st.get("until", -1.0):
                    aura = t + SANGUINE_FAST
                else:
                    aura = float(math.floor(t + 1e-9) + 1)
            elif kind in ("start", "after_casts"):
                self.t = t
                before = dict(self.active_ready)
                self._press(kind)
                for n, p in self.actives:  # a press refused now is retried later
                    if p.active_trigger == kind and self.active_ready[n] == before[n] <= t:
                        self.active_ready[n] = t + ACTIVE_RETRY
                st = self.state.get("Sanguine Lash")
                if st and st.get("until", -1.0) > t:
                    aura = min(aura, t + SANGUINE_FAST)
            elif kind == "assist":
                self.t = t
                self.assists += 1
                self._takedown("assist")
                assist = t + ASSIST_INTERVAL
            else:
                self.t = t
                f = foes[i]
                self.take_hit(f[2], f[3], f[4])
                f[0] = t + f[1]
        if until_dead:
            return self.absorbed + (self.remaining_ehp(self.enemy) if self.hp > 1e-9 else 0.0)
        return self.total() - self.target_healed

    def run_burst(self):
        self._press("start")
        for a in self.rotation:
            self._ability(0.0, a)
        self._attack(0.0, 0)
        return self.total()

    def total(self):
        return sum(self.by_channel.values())


# ── Effective health ──────────────────────────────────────────────────────

def effective_health(god, names, items_by_name, level=LEVEL, stacks="full", disabled=()):
    """`(ehp_physical, ehp_magical, health)`. Health-gated protection is
    integrated over the bar (`passive_sim`'s `ehp_segments`): a slice of
    the bar carrying P protection absorbs `slice x (1 + P/100)`. Brawler's
    in-combat stacks are read at zero (entering the fight)."""
    stats, _, _ = build_stats(names, items_by_name, level, stacks, disabled)
    base = god.get("base_stats") or {}
    health = bq.level_value(base.get("health"), level) + stats.get("Max Health", 0.0)
    phys = bq.level_value(base.get("physical_prot"), level) + stats.get("Physical Protection", 0.0)
    mag = bq.level_value(base.get("magical_prot"), level) + stats.get("Magical Protection", 0.0)
    cuts = {0.0, 1.0}
    pieces = []
    for _, p in passives_for(names, items_by_name, disabled):
        if not p.ehp_segments:
            continue
        lost, spans = 0.0, []
        for share, ep, em in p.ehp_segments(None):
            spans.append((lost, lost + share, ep, em))
            lost += share
            cuts.add(round(lost, 9))
        pieces.append(spans)
    cuts = sorted(cuts)
    out_p = out_m = 0.0
    for lo, hi in zip(cuts, cuts[1:]):
        mid = (lo + hi) / 2
        ep = sum(s[2] for spans in pieces for s in spans if s[0] <= mid < s[1])
        em = sum(s[3] for spans in pieces for s in spans if s[0] <= mid < s[1])
        out_p += (hi - lo) * combat.effective_health(health, phys + ep)
        out_m += (hi - lo) * combat.effective_health(health, mag + em)
    return out_p, out_m, health


# ── One build ─────────────────────────────────────────────────────────────

FIGHT_HOOKS = ("on_takedown", "on_hit_taken", "reduce_hit", "prot_bonus", "active")


def moves_in_a_fight(names, items_by_name, disabled=()):
    """True if any item in the build reacts to the FIGHT block's events, or
    heals our god in one (HEALING block: lifesteal on the stat line counts)."""
    plist = passives_for(names, items_by_name, disabled)
    if any(getattr(p, h) for _, p in plist for h in FIGHT_HOOKS):
        return True
    if not HEALING:
        return False
    if any(p.heals for _, p in plist):
        return True
    stats, _, _ = build_stats(names, items_by_name, disabled=disabled)
    return stats.get("Lifesteal %", 0.0) > 0


def fight_ehp(god, names, items_by_name, targets, stacks="full", disabled=()):
    """`(ehp_physical, ehp_magical, health)` under the FIGHT block's enemy:
    one damage type at full DPS until our bar is gone, our god fighting the
    squishy (so its kills and the assists happen). Raw damage taken is the
    effective health. A build with nothing that reacts to a fight gets the
    static integral, which the run equals in that case."""
    static = effective_health(god, names, items_by_name, stacks=stacks, disabled=disabled)
    sq = targets.get("squishy") or {}
    if not sq.get("attacker") or not moves_in_a_fight(names, items_by_name, disabled):
        return static
    out = []
    for dtype in ("physical", "magical"):
        s = Sim(god, names, items_by_name, sq, window=EHP_RUN_CAP, stacks=stacks,
                disabled=disabled, enemy=dtype, takedowns=True)
        out.append(s.run_window(until_dead=True))
    return out[0], out[1], static[2]


def power(god, names, items_by_name, targets, stacks="clock", disabled=()):
    """The four damage figures and the two effective healths. `stacks` is
    "full", "none", a `stack_state` dict, or "clock" — the game clock at
    `len(names)` items."""
    if stacks == "clock":
        stacks = stack_state(names, len(names))
    out = {}
    for tname, target in targets.items():
        s = Sim(god, names, items_by_name, target, stacks=stacks, disabled=disabled, enemy="both")
        out[f"sustained_{tname}"] = s.run_window()
        out[f"channels_{tname}"] = dict(s.by_channel)
        out[f"procs_{tname}"] = dict(s.by_item)
        out[f"takedowns_{tname}"] = {"kills": s.kills, "assists": s.assists}
        out[f"healing_{tname}"] = {"healed": s.healed, "target_healed": s.target_healed,
                                   "by_item": dict(s.heal_by_item)}
        b = Sim(god, names, items_by_name, target, window=None, stacks=stacks, disabled=disabled)
        out[f"burst_{tname}"] = b.run_burst()
    out["ehp_physical"], out["ehp_magical"], out["health"] = fight_ehp(
        god, names, items_by_name, targets, stacks=stacks, disabled=disabled)
    return out


def profile(god, names, items_by_name, targets):
    names = list(names)
    full = power(god, names, items_by_name, targets)
    s = Sim(god, names, items_by_name, targets["squishy"], stacks=stack_state(names, len(names)))
    cds = [{"name": a["name"], "base": a["cooldown"], "effective": a["effective_cooldown"],
            "ultimate": a["is_ultimate"]} for a in s.rotation]
    p = s.crit_chance()
    passives = []
    for n in names:
        pv = passive_sim.lookup(items_by_name[n])
        passives.append({"item": n, "status": pv.status, "summary": pv.summary,
                         "assumptions": list(pv.assumptions)})
    keep = lambda pw: {m: pw[m] for m in DAMAGE_KEYS + SURVIVAL_KEYS}
    stacking = any(passive_sim.lookup(items_by_name[n]).stacking for n in names)
    breakpoints, full_stacks, old_stacks = {}, {}, {}
    brackets = {m: {} for m in STACK_MINUTES_BRACKET}
    for k in BREAKPOINTS:
        pw = full if k == 6 else power(god, names[:k], items_by_name, targets)
        breakpoints[k] = keep(pw)
        if not stacking:
            full_stacks[k] = old_stacks[k] = breakpoints[k]
            for m in STACK_MINUTES_BRACKET:
                brackets[m][k] = breakpoints[k]
            continue
        # The two ends PR #77 used, kept for the before/after table: stacks
        # FULL everywhere (the bracket), and NONE at 2 and 4 / FULL at six
        # (the rule before the game clock).
        pf = keep(power(god, names[:k], items_by_name, targets, stacks="full"))
        full_stacks[k] = pf
        old_stacks[k] = pf if k == 6 else keep(
            power(god, names[:k], items_by_name, targets, stacks="none"))
        for m in STACK_MINUTES_BRACKET:
            brackets[m][k] = keep(power(god, names[:k], items_by_name, targets,
                                        stacks=stack_state(names, k, m)))
    return {
        "items": names, "gold": s.gold, **full,
        "cooldowns": cds,
        "cooldown_rate": s.base_stats.get("Cooldown Rate", 0.0),
        "mean_cooldown": _mean([c["effective"] for c in cds if not c["ultimate"]]),
        "ultimate_cooldown": _mean([c["effective"] for c in cds if c["ultimate"]]),
        "crit_chance": p, "crit_multiplier": s.crit_mult,
        "crit_ev": 1.0 + p * (s.crit_mult - 1.0),
        "attacks_per_second": s.attacks_per_second(),
        "breakpoints": breakpoints, "breakpoints_full_stacks": full_stacks,
        "breakpoints_old_stacks": old_stacks,
        **{f"breakpoints_stacks_{m:g}min": brackets[m] for m in STACK_MINUTES_BRACKET},
        "passives": passives,
        "simulated_share": simulated_share(names, items_by_name),
        "dropped_abilities": s.dropped,
    }


def passive_contribution(god, names, items_by_name, targets, item):
    """What one item's PASSIVE is worth in this build, in numbers: the build
    with that passive switched off (its printed stats kept)."""
    on = power(god, names, items_by_name, targets)
    off = power(god, names, items_by_name, targets, disabled={item})
    return {m: on[m] - off[m] for m in DAMAGE_KEYS + SURVIVAL_KEYS}


def _mean(xs):
    return sum(xs) / len(xs) if xs else None


DAMAGE_KEYS = ["sustained_squishy", "sustained_tank", "burst_squishy", "burst_tank"]
SURVIVAL_KEYS = ["ehp_physical", "ehp_magical"]


# ── Which builds ──────────────────────────────────────────────────────────

def community_six(god, build_note, items_by_name):
    """The community's six, CLEANED by the one rule `community_target` owns:
    its `scored` slots in bought order, then the community's next finished
    picks appended to reach six (`community_target.comparison_six`, whose
    docstring says why drop-then-fill and not swap-in-place). Returns
    `(names, substitutions)`; fewer than six means the record cannot make a
    build and the god is skipped, named.

    80 of 90 raw community slot lists contain a tier-2 component (Evil Eye,
    Skeggox, Sage's Ring...), a statless relic (Blinking Abyss) or a
    duplicate, because SmiteBrain's slot is "what was in that slot", including
    a component sold later. Comparing a build with a 1000g component in it to
    six finished items would be a comparison of gold, not of choices."""
    entry = next((b for b in build_note.get("builds") or [] if b.get("source") == "community"), None)
    if not entry:
        return [], []
    return community_target.comparison_six(entry.get("slot_order"), items_by_name, god)


def community_rates(build_note, name):
    """`{pick_rate, win_rate, where}` as printed by SmiteBrain — the raw slot
    figure if the item is a slot pick, else its best alternate sighting."""
    entry = next((b for b in build_note.get("builds") or [] if b.get("source") == "community"), None)
    best = None
    for i, slot in enumerate((entry or {}).get("slot_order") or [], start=1):
        if not isinstance(slot, dict):
            continue
        if slot.get("name") == name:
            return {"pick_rate": slot.get("pick_rate"), "win_rate": slot.get("win_rate"),
                    "where": f"slot {i}"}
        for a in slot.get("alternates") or []:
            if a.get("name") == name and (best is None or (a.get("pick_rate") or 0) > best["pick_rate"]):
                best = {"pick_rate": a.get("pick_rate") or 0.0, "win_rate": a.get("win_rate"),
                        "where": f"slot {i} alternate"}
    return best or {"pick_rate": 0.0, "win_rate": None, "where": "not in the record"}


# ── Targets ───────────────────────────────────────────────────────────────

def target_from(god, names, items_by_name, level=LEVEL):
    items, _ = printed_totals(names, items_by_name)
    base = god.get("base_stats") or {}
    bh = bq.level_value(base.get("health"), level)
    return {"base_health": bh, "item_health": items.get("Max Health", 0.0),
            "physical_prot": bq.level_value(base.get("physical_prot"), level)
            + items.get("Physical Protection", 0.0),
            "magical_prot": bq.level_value(base.get("magical_prot"), level)
            + items.get("Magical Protection", 0.0),
            "plating": items.get("Plating", 0.0), "dampening": items.get("Dampening", 0.0),
            "lifesteal": items.get("Lifesteal %", 0.0),
            "anti_heal": max((passive_sim.ANTI_HEAL[n][0] for n in names if n in passive_sim.ANTI_HEAL),
                             default=0.0)}


#: Fields of a reference target read as a MEAN, not a median (HEALING block).
MEAN_FIELDS = ("lifesteal", "anti_heal")


def reference_targets(gods, builds_by_god, items_by_name):
    """Median Mid (squishy) and median Support (tank) at level 20 in the
    community's cleaned six — every field its own median."""
    out = {}
    for label, role in (("squishy", SQUISHY_ROLE), ("tank", TANK_ROLE)):
        rows = []
        for g in gods:
            if bq.primary_role(g) != role:
                continue
            six, _ = community_six(g, builds_by_god.get(g["name"]) or {}, items_by_name)
            if len(six) == 6:
                rows.append(target_from(g, six, items_by_name))
        t = {k: (statistics.fmean if k in MEAN_FIELDS else statistics.median)(r[k] for r in rows)
             for k in rows[0]}
        t["max_health"] = t["base_health"] + t["item_health"]
        t["role"], t["n"] = role, len(rows)
        out[label] = t
    prof = attacker_profile(gods, builds_by_god, items_by_name, out["squishy"])
    for t in out.values():
        t["attacker"] = prof
    return out


def attacker_profile(gods, builds_by_god, items_by_name, squishy):
    """The FIGHT block's enemy. Raw DPS per type kills the reference squishy
    in WINDOW; attacks come at the median community Carry's attack speed and
    ability hits at the median community Mid's casts per second, each on its
    finished six at level 20 (game-clock stacks)."""
    raw_dps = {"physical": combat.effective_health(squishy["max_health"], squishy["physical_prot"]) / WINDOW,
               "magical": combat.effective_health(squishy["max_health"], squishy["magical_prot"]) / WINDOW}
    aps, casts = [], []
    cuts = {}   # role -> [healing reduction of each community six]
    for g in gods:
        role = bq.primary_role(g)
        six, _ = community_six(g, builds_by_god.get(g["name"]) or {}, items_by_name)
        if len(six) != 6:
            continue
        cuts.setdefault(role, []).append(target_from(g, six, items_by_name)["anti_heal"])
        if role not in ("Carry", SQUISHY_ROLE):
            continue
        s = Sim(g, six, items_by_name, squishy, stacks=stack_state(six, 6))
        if role == "Carry":
            aps.append(s.attacks_per_second())
        else:
            rate = sum(1.0 / a["effective_cooldown"] for a in s.rotation if a["effective_cooldown"] > 0)
            if rate > 0:
                casts.append(rate)
    return {"raw_dps": raw_dps,
            "interval": {"attack": 1.0 / statistics.median(aps),
                         "ability": 1.0 / statistics.median(casts)},
            "n": {"attack": len(aps), "ability": len(casts)},
            # HEALING block: the expected healing reduction on our heals.
            "anti_heal": team_anti_heal(cuts)}


def team_anti_heal(cuts_by_role):
    """The expected healing reduction on our god from a whole enemy TEAM, one
    god per role: `cut x P(at least one role holds anti-heal)`, each role's
    share read off its community sixes. A team, not one attacker, because
    "Healing Reduction does not stack with other similar effects": whoever
    applies it, our heal is cut once. `cut` is the strongest reduction any
    holder carries (40% for every item in the pool)."""
    miss, cut = 1.0, 0.0
    for xs in cuts_by_role.values():
        if not xs:
            continue
        held = [x for x in xs if x > 0]
        miss *= 1.0 - len(held) / len(xs)
        cut = max([cut] + held)
    return cut * (1.0 - miss)


# ── The model's reasons ───────────────────────────────────────────────────

class ModelView:
    """The shipped scoring for the meta-free `model` archetype: each item's
    efficiency, fit and quality on this god, with the pricing flags ON as
    `recommend.main` runs them."""

    def __init__(self, items, weights, tags_map):
        self.items, self.weights, self.tags_map = items, weights, tags_map
        before = efficiency.apply_pricing_flags(weights)
        try:
            self.eff, _ = efficiency.efficiency_scores(items)
        finally:
            efficiency.restore_pricing_flags(before)

    def rows(self, god, build_note):
        before = efficiency.apply_pricing_flags(self.weights)
        try:
            profile_ = scoring.resolve_profile(self.weights, "Conquest", None)
            rows = scoring.score_god_items(god, self.items, build_note, self.eff,
                                           self.weights, self.tags_map, profile_)
        finally:
            efficiency.restore_pricing_flags(before)
        ranked = sorted(rows, key=lambda r: (-r["quality"], r["item"]))
        return {r["item"]: dict(r, rank=i + 1) for i, r in enumerate(ranked)}


def model_reason(rows, name, ours):
    """Why Ichor does or does not buy `name`, in the model's own terms."""
    r = rows.get(name)
    cut = min((rows[n]["quality"] for n in ours if n in rows), default=None)
    if r is None:
        return {"scored": False,
                "text": "not in the model's pool for this god (fails the damage-type filter "
                        "or cannot take a core slot)"}
    out = {"scored": True, "rank": r["rank"], "quality": r["quality"],
           "efficiency": r["efficiency"], "fit": r["fit"], "cut": cut}
    gap = (cut - r["quality"]) if cut is not None else 0.0
    out["text"] = (f"model rank #{r['rank']}, quality {r['quality']:.3f} "
                   f"(efficiency {r['efficiency']:.2f}, fit {r['fit']:.2f})"
                   + (f"; the weakest item Ichor kept scores {cut:.3f}" if cut is not None else ""))
    if r["rank"] <= 6 and name not in ours:
        out["text"] += "; ranked inside the six but the assembler's caps/coherence left it out"
    elif gap > 0:
        out["text"] += f", {gap:.3f} short"
    return out


# ── Compare ───────────────────────────────────────────────────────────────

def ratio(a, b):
    return a / b if b else (1.0 if not a else math.inf)


def geomean(xs):
    xs = [x for x in xs if x and x > 0 and math.isfinite(x)]
    return math.exp(sum(math.log(x) for x in xs) / len(xs)) if xs else 1.0


def axes(ours, theirs):
    return (geomean([ratio(ours[k], theirs[k]) for k in DAMAGE_KEYS]),
            geomean([ratio(ours[k], theirs[k]) for k in SURVIVAL_KEYS]))


def verdict(d, s, band=BAND):
    """The rule in the module docstring. Returns one of
    "Ichor better" / "community better" / "trade-off" / "level"."""
    up = lambda x: x > 1 + band
    down = lambda x: x < 1 - band
    if (up(d) and down(s)) or (up(s) and down(d)):
        return "trade-off"
    if up(d) or up(s):
        return "Ichor better"
    if down(d) or down(s):
        return "community better"
    return "level"


def breakpoint_axes(ours, theirs, key="breakpoints"):
    """`{k: (damage, survival)}` at each breakpoint."""
    return {k: axes(ours[key][k], theirs[key][k]) for k in BREAKPOINTS}


def weighted_axes(bp, weights=None):
    """The weighted geometric mean of the per-point axes."""
    weights = weights or BREAKPOINT_WEIGHTS
    w = sum(weights.values())
    return tuple(math.exp(sum(weights[k] * math.log(bp[k][i]) for k in weights) / w)
                 for i in (0, 1))


def phase(bp, band=BAND):
    """EARLY_GAME / LATE_GAME / None from the composite at 2+4 vs at 6."""
    comp = lambda d, s: math.sqrt(d * s)
    early = math.sqrt(comp(*bp[2]) * comp(*bp[4]))
    late = comp(*bp[6])
    if early > 1 + band and late < 1 - band:
        return EARLY_GAME
    if early < 1 - band and late > 1 + band:
        return LATE_GAME
    return None


def coverage_check(ours_share, theirs_share):
    """`(ok, reason)` under COVERAGE_MIN and COVERAGE_GAP."""
    low = min(ours_share, theirs_share)
    gap = abs(ours_share - theirs_share)
    if low < COVERAGE_MIN:
        return False, f"{low:.0%} of one build's gold is simulated (minimum {COVERAGE_MIN:.0%})"
    if gap > COVERAGE_GAP:
        return False, f"coverage differs by {gap:.0%} (maximum {COVERAGE_GAP:.0%})"
    return True, None


def judge(r, band=BAND, withhold=True, key="breakpoint_axes"):
    """The full rule on one comparison row: kit, then coverage, then the
    phase label, then the weighted 2/4/6 verdict. `key` picks the stack
    assumption at 2 and 4 items (the bracket reads the full-stack end)."""
    if not r["kit"]["simulated"]:
        return ASPECT_NOT_SIMULATED
    if withhold and not r["coverage"]["ok"]:
        return NOT_ENOUGH_SIMULATED
    bp = {int(k): v for k, v in r[key].items()}
    return phase(bp, band) or verdict(*weighted_axes(bp), band)


def judge_six_only(r, band=BAND):
    """The 2026-11-02 rule before this session: the finished six alone."""
    if not r["kit"]["simulated"]:
        return ASPECT_NOT_SIMULATED
    return verdict(r["damage_axis"], r["survival_axis"], band)


def kit_for(build_note):
    """Which kit the comparison is on, from the community entry's own aspect
    pick rate: `{kit, aspect, pick_rate, win_rate, simulated}`. `kit` is
    "base" or the aspect's name; `simulated` is False only when the aspect is
    the fair kit and `combat.py` cannot play it."""
    entry = next((b for b in build_note.get("builds") or [] if b.get("source") == "community"), {})
    aspect, rate = entry.get("aspect"), entry.get("aspect_pick_rate")
    on_aspect = bool(aspect) and rate is not None and rate > ASPECT_MAJORITY
    return {"kit": aspect if on_aspect else "base", "aspect": aspect,
            "pick_rate": rate, "win_rate": entry.get("aspect_win_rate"),
            "simulated": (not on_aspect) or aspect in SIMULATED_ASPECTS}


def compare(god, build_note, items_by_name, targets, model_rows=None):
    """Everything criterion 2 names for one god, or None (with a reason)."""
    community, subs = community_six(god, build_note, items_by_name)
    ours = bq.suggested_core(build_note, ARCHETYPE)
    if len(community) < 6:
        return None, f"community record makes {len(community)} of 6"
    if len(ours) < 6 or any(n not in items_by_name for n in ours):
        return None, "no full model build"
    ours = ours[:6]
    kit = kit_for(build_note)
    p_ours = profile(god, ours, items_by_name, targets)
    p_theirs = profile(god, community, items_by_name, targets)
    d, s = axes(p_ours, p_theirs)
    bp = breakpoint_axes(p_ours, p_theirs)
    ok, why = coverage_check(p_ours["simulated_share"], p_theirs["simulated_share"])
    rows = model_rows or {}

    diffs = []
    ours_only = [n for n in ours if n not in community]
    for side, mine, other, build in (("community", community, ours, p_theirs),
                                     ("ichor", ours, community, p_ours)):
        for name in mine:
            if name in other:
                continue
            pv = passive_sim.lookup(items_by_name[name])
            entry = {"item": name, "side": side,
                     "gold": float(items_by_name[name].get("cost") or 0.0),
                     "community": community_rates(build_note, name),
                     "passive": {"status": pv.status, "summary": pv.summary,
                                 "assumptions": list(pv.assumptions)},
                     "model": model_reason(rows, name, ours)}
            if pv.status in (passive_sim.SIMULATED, passive_sim.PARTIAL):
                entry["passive"]["worth"] = passive_contribution(
                    god, mine, items_by_name, targets, name)
            if side == "community" and ours_only:
                entry["best_swap"] = best_swap(god, ours, name, ours_only, items_by_name, targets,
                                               p_ours)
            diffs.append(entry)
    out = {
        "god": god["name"], "role": bq.primary_role(god), "damage_type": god.get("damage_type"),
        "melee": is_melee(god), "level": LEVEL, "window": WINDOW,
        "ichor": p_ours, "community": p_theirs, "community_substitutions": subs,
        "shared": [n for n in ours if n in community],
        "damage_axis": d, "survival_axis": s, "kit": kit,
        "breakpoint_axes": bp, "weighted_axes": weighted_axes(bp),
        "breakpoint_axes_full_stacks": breakpoint_axes(p_ours, p_theirs, "breakpoints_full_stacks"),
        "breakpoint_axes_old_stacks": breakpoint_axes(p_ours, p_theirs, "breakpoints_old_stacks"),
        **{f"breakpoint_axes_stacks_{m:g}min": breakpoint_axes(p_ours, p_theirs, f"breakpoints_stacks_{m:g}min")
           for m in STACK_MINUTES_BRACKET},
        "coverage": {"ichor": p_ours["simulated_share"], "community": p_theirs["simulated_share"],
                     "gap": abs(p_ours["simulated_share"] - p_theirs["simulated_share"]),
                     "ok": ok, "reason": why},
        "diffs": diffs,
    }
    out["verdict"] = judge(out)
    out["verdict_unwithheld"] = judge(out, withhold=False)
    out["verdict_six_only"] = judge_six_only(out)
    return out, None


def best_swap(god, ours, incoming, candidates, items_by_name, targets, base):
    """Put a community-only item into Ichor's build in place of each
    Ichor-only item; report the swap that moves the damage axis most, with
    both axes. This is what "the community wins with passives simulated"
    has to survive: the item on its own, in our build."""
    best = None
    for out in candidates:
        trial = [incoming if n == out else n for n in ours]
        pw = power(god, trial, items_by_name, targets)
        d, s = axes(pw, base)
        if best is None or d > best["damage_axis"]:
            best = {"replaces": out, "damage_axis": d, "survival_axis": s}
    return best


# ── The roster ────────────────────────────────────────────────────────────

def run(gods, items, builds_by_god, weights, tags_map, only=None):
    items_by_name = {it["name"]: it for it in items}
    targets = reference_targets(gods, builds_by_god, items_by_name)
    view = ModelView(items, weights, tags_map)
    rows, skipped = [], []
    for g in sorted(gods, key=lambda g: g["name"]):
        if only and g["name"] != only:
            continue
        note = builds_by_god.get(g["name"]) or {}
        row, why = compare(g, note, items_by_name, targets, view.rows(g, note))
        if row:
            rows.append(row)
        else:
            skipped.append({"god": g["name"], "reason": why})
    return rows, skipped, targets


def judged(rows):
    """Rows that carry a verdict — every row except `ASPECT_NOT_SIMULATED`."""
    return [r for r in rows if r["verdict"] != ASPECT_NOT_SIMULATED]


def aspect_excluded(rows):
    """Gods left out of every count because the community plays an aspect
    the combat model cannot, most-played first — the follow-up list."""
    return sorted((r for r in rows if r["verdict"] == ASPECT_NOT_SIMULATED),
                  key=lambda r: -(r["kit"]["pick_rate"] or 0))


VERDICT_ORDER = ("Ichor better", "community better", "trade-off", "level",
                 EARLY_GAME, LATE_GAME, NOT_ENOUGH_SIMULATED)


def verdict_counts(rows, band=BAND, rule=None):
    """Per role, over `judged` rows only, under `rule` (default `judge`)."""
    rule = rule or judge
    out = {}
    for r in judged(rows):
        v = rule(r, band)
        out.setdefault(r["role"], {}).setdefault(v, 0)
        out[r["role"]][v] += 1
    return out


def not_simulated(rows):
    """Every item in a compared build whose passive is not (fully) simulated,
    with the number of builds it sits in."""
    out = {}
    for r in rows:
        for side in ("ichor", "community"):
            for p in r[side]["passives"]:
                if p["status"] in (passive_sim.NOT_SIMULATED, passive_sim.PARTIAL):
                    e = out.setdefault(p["item"], {"status": p["status"], "builds": 0,
                                                   "why": "; ".join(p["assumptions"]) or p["summary"]})
                    e["builds"] += 1
    return dict(sorted(out.items(), key=lambda kv: -kv[1]["builds"]))


def _pct(x):
    return f"{(x - 1) * 100:+.1f}%"


def kit_line(k):
    if not k.get("aspect") or k.get("pick_rate") is None:
        return "base (no aspect record)"
    played = f"{k['aspect']} played in {k['pick_rate']:.0%} of games"
    if k["kit"] == "base":
        return f"base ({played})"
    if not k["simulated"]:
        return (f"{k['aspect']} ({k['pick_rate']:.0%} of games) — NOT SIMULATED: the numbers "
                "below are on the base kit and carry no verdict")
    return f"{k['aspect']} ({played})"


def god_lines(r):
    i, c = r["ichor"], r["community"]
    L = [f"## {r['god']} ({r['role']}, {r['damage_type']}, {'melee' if r['melee'] else 'ranged'})",
         "",
         f"**Verdict: {r['verdict']}**"
         + (f" (the rule would say {r['verdict_unwithheld']}: {r['coverage']['reason']})"
            if r["verdict"] == NOT_ENOUGH_SIMULATED else "")
         + f" — weighted 2/4/6: damage {_pct(r['weighted_axes'][0])}, survival {_pct(r['weighted_axes'][1])}; "
         f"six items: damage {_pct(r['damage_axis'])}, survival {_pct(r['survival_axis'])} "
         f"(six-item rule: {r['verdict_six_only']})",
         "",
         f"Simulated: {r['coverage']['ichor']:.0%} of Ichor's gold, {r['coverage']['community']:.0%} "
         "of the community's",
         "",
         f"Kit: {kit_line(r['kit'])}",
         "",
         f"- Ichor ({i['gold']:.0f}g): {' · '.join(i['items'])}",
         f"- Community ({c['gold']:.0f}g): {' · '.join(c['items'])}",
         ]
    for s in r["community_substitutions"]:
        L.append(f"  - cleaned: slot {s['slot']} {s['dropped']} ({s['class']}) dropped"
                 + (f"; filled at position {s['position']} with {s['used']} ({s['note']})"
                    if s["used"] else ""))
    L += ["", "| | Ichor | Community | Δ |", "|---|---|---|---|",
          f"| gold | {i['gold']:.0f} | {c['gold']:.0f} | {i['gold'] - c['gold']:+.0f} |"]
    for key, label in (("burst_squishy", "burst vs squishy"), ("burst_tank", "burst vs tank"),
                       ("sustained_squishy", "10s sustained vs squishy"),
                       ("sustained_tank", "10s sustained vs tank"),
                       ("ehp_physical", "EHP vs physical"), ("ehp_magical", "EHP vs magical")):
        L.append(f"| {label} | {i[key]:.0f} | {c[key]:.0f} | {_pct(ratio(i[key], c[key]))} |")
    fmt = lambda v: "—" if v is None else f"{v:.1f}s"
    L.append(f"| mean ability cooldown | {fmt(i['mean_cooldown'])} | {fmt(c['mean_cooldown'])} | |")
    L.append(f"| ultimate cooldown | {fmt(i['ultimate_cooldown'])} | {fmt(c['ultimate_cooldown'])} | |")
    L.append(f"| crit EV (chance × mult) | {i['crit_ev']:.3f} ({i['crit_chance']:.0%} × {i['crit_multiplier']:.2f}) "
             f"| {c['crit_ev']:.3f} ({c['crit_chance']:.0%} × {c['crit_multiplier']:.2f}) | |")
    for k in BREAKPOINTS:
        a, b = i["breakpoints"][k], c["breakpoints"][k]
        L.append(f"| {k} items: 10s vs squishy / EHP phys | {a['sustained_squishy']:.0f} / {a['ehp_physical']:.0f} "
                 f"| {b['sustained_squishy']:.0f} / {b['ehp_physical']:.0f} "
                 f"| {_pct(ratio(a['sustained_squishy'], b['sustained_squishy']))} / "
                 f"{_pct(ratio(a['ehp_physical'], b['ehp_physical']))} |")
    for k in BREAKPOINTS:
        dk, sk = r["breakpoint_axes"][k]
        L.append(f"| {k} items: damage / survival axis | | | {_pct(dk)} / {_pct(sk)} |")
    L.append("")
    for d in r["diffs"]:
        cr = d["community"]
        rates = (f"pick {cr['pick_rate']:.0%}, win {cr['win_rate']:.0%} ({cr['where']})"
                 if cr.get("win_rate") is not None else cr["where"])
        worth = d["passive"].get("worth")
        w = (f"; passive worth {worth['sustained_squishy']:+.0f} sustained / "
             f"{worth['burst_squishy']:+.0f} burst / {worth['ehp_physical']:+.0f} EHP"
             if worth else "")
        who = "Community only" if d["side"] == "community" else "Ichor only"
        L.append(f"- **{d['item']}** ({who}, {d['gold']:.0f}g) — {rates}. "
                 f"Passive [{d['passive']['status']}]: {d['passive']['summary']}{w}. "
                 f"Model: {d['model']['text']}.")
        if d.get("best_swap"):
            bs = d["best_swap"]
            L.append(f"  - in Ichor's build for {bs['replaces']}: damage {_pct(bs['damage_axis'])}, "
                     f"survival {_pct(bs['survival_axis'])}")
    gaps = [p for side in ("ichor", "community") for p in r[side]["passives"]
            if p["status"] in (passive_sim.NOT_SIMULATED, passive_sim.PARTIAL)]
    if gaps:
        L.append("")
        L.append("Not (fully) simulated: " + "; ".join(
            sorted({f"{p['item']} ({p['status']}: {'; '.join(p['assumptions']) or p['summary']})"
                    for p in gaps})))
    L.append("")
    return L


def totals(counts):
    out = {}
    for per_role in counts.values():
        for v, n in per_role.items():
            out[v] = out.get(v, 0) + n
    return out


def count_table(counts):
    L = ["| role | " + " | ".join(VERDICT_ORDER) + " |", "|---" * (len(VERDICT_ORDER) + 1) + "|"]
    tot = totals(counts)
    for role in sorted(counts):
        L.append(f"| {role} | " + " | ".join(str(counts[role].get(v, 0)) for v in VERDICT_ORDER) + " |")
    L.append("| **all** | " + " | ".join(f"**{tot.get(v, 0)}**" for v in VERDICT_ORDER) + " |")
    return L


def community_wins(rows, withheld=False):
    """Community-better gods, worst for Ichor first (weighted axes). With
    `withheld`, the ones the coverage rule withholds instead."""
    pick = [r for r in judged(rows)
            if (r["verdict"] == NOT_ENOUGH_SIMULATED and r["verdict_unwithheld"] == "community better")
            == withheld and (withheld or r["verdict"] == "community better")]
    return sorted(pick, key=lambda r: r["weighted_axes"][0] * r["weighted_axes"][1])


def top_swap(r):
    """The community-only item that, swapped into Ichor's six, lifts Ichor's
    damage axis most: `{item, replaces, damage_axis, survival_axis}`."""
    best = None
    for d in r["diffs"]:
        bs = d.get("best_swap")
        if bs and (best is None or bs["damage_axis"] > best["damage_axis"]):
            best = dict(bs, item=d["item"])
    return best


def report_lines(rows, skipped, targets, data_patch, no_assists=None, sensitivity=()):
    L = ["# Ichor vs community, passives simulated", "",
         f"Data: {data_patch}. Level {LEVEL}, {WINDOW:.0f}s window. Ichor = the `model` build "
         "(meta off); community = the cleaned six. Generated by `python -m smite.side_by_side`; "
         "the rules are in that module's docstring.", "",
         "## Targets (medians of the community's own builds)", "",
         "| | role | n | base HP | item HP | phys prot | mag prot | plating | dampening | lifesteal (mean) |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for k, t in targets.items():
        L.append(f"| {k} | {t['role']} | {t['n']} | {t['base_health']:.0f} | {t['item_health']:.0f} "
                 f"| {t['physical_prot']:.0f} | {t['magical_prot']:.0f} | {t['plating']:.0f} | {t['dampening']:.0f} "
                 f"| {t.get('lifesteal', 0.0):.1f}% |")
    att = targets["squishy"].get("attacker")
    if att:
        L += ["", "## The fight (module FIGHT block)", "",
              f"- Kill: when our damage in a {WINDOW:.0f}s fight reaches the target's max health; at most "
              "one per fight. None in a burst.",
              f"- Assist: one every {ASSIST_INTERVAL:g}s, first at {ASSIST_FIRST:g}s — the same instants "
              "for both builds.",
              f"- Enemy on our god: raw {att['raw_dps']['physical']:.0f} physical / "
              f"{att['raw_dps']['magical']:.0f} magical DPS (kills the squishy in {WINDOW:.0f}s); attacks every "
              f"{att['interval']['attack']:.2f}s (median of {att['n']['attack']} community Carries), ability hits "
              f"every {att['interval']['ability']:.2f}s (median of {att['n']['ability']} community Mids). "
              f"Sustained window: each type at {ENEMY_SHARE:.0%}. Effective health: one type at full DPS "
              "until the bar is gone.",
              "- Actives: pressed the first moment their condition holds, again on cooldown "
              "(conditions in `passive_sim`).",
              "- Healing (module HEALING block): our god lifesteals off every damage instance to a live "
              "target and takes item heals, cut by the enemy team's expected healing reduction "
              f"({att.get('anti_heal', 0.0):.1%}); the target lifesteals off the damage it deals us, cut by "
              "our anti-heal while it is live. Sustained damage is NET of the target's healing."]
    L += ["", "## Verdicts by role", "",
          f"Rule (module docstring): band ±{BAND:.0%}; the 2-, 4- and 6-item points weighted "
          + " / ".join(f"{w:.2f}" for w in BREAKPOINT_WEIGHTS.values())
          + "; a god ahead early and behind at six (or the reverse) is a phase verdict; withheld as "
          f"\"{NOT_ENOUGH_SIMULATED}\" when either build has under {COVERAGE_MIN:.0%} of its gold "
          f"simulated or the two differ by more than {COVERAGE_GAP:.0%}.", ""]
    L += count_table(verdict_counts(rows))
    L += ["", f"Old rule against new, all roles ({len(judged(rows))} gods with a kit match). "
          "The bracket column re-runs the 2/4/6 rule with stacking passives FULL at 2 and 4 items "
          "instead of on the game clock — the top end of the stack assumption:", "",
          "| verdict | six items only (old) | 2/4/6 weighted, not withheld | same, full stacks early (bracket) "
          "| 2/4/6 weighted + coverage (new) |",
          "|---|---|---|---|---|"]
    old = totals(verdict_counts(rows, rule=judge_six_only))
    mid = totals(verdict_counts(rows, rule=lambda r, b: judge(r, b, withhold=False)))
    brk = totals(verdict_counts(rows, rule=lambda r, b: judge(r, b, withhold=False,
                                                              key="breakpoint_axes_full_stacks")))
    new = totals(verdict_counts(rows))
    for v in VERDICT_ORDER:
        L.append(f"| {v} | {old.get(v, 0)} | {mid.get(v, 0)} | {brk.get(v, 0)} | {new.get(v, 0)} |")
    moved = [r for r in judged(rows) if r["verdict"] != r["verdict_six_only"]]
    L.append(f"\n{len(moved)} verdicts differ from the six-item rule; "
             f"{sum(1 for r in judged(rows) if r['verdict'] == NOT_ENOUGH_SIMULATED)} are withheld for coverage.")
    L += ["", "### Stack timing: before and after the game clock", "",
          f"Each finished item lands {MINUTES_PER_ITEM:g} minutes after the last; a stacking item is full "
          f"{STACK_MINUTES_TO_FULL:g} minutes after it is bought (`STACK_MINUTES_TO_FULL`, not measured — "
          "bracketed). \"Before\" is PR #77's rule: no stacks at 2 and 4 items, full at six.", "",
          "| verdict | before: none early, full at six | game clock "
          + " | ".join(f"(full in {m:g} min)" for m in STACK_MINUTES_BRACKET)
          + f" | **game clock ({STACK_MINUTES_TO_FULL:g} min)** |",
          "|---" * (3 + len(STACK_MINUTES_BRACKET)) + "|"]
    stack_rules = [lambda r, b, k=k: judge(r, b, key=k) for k in
                   ["breakpoint_axes_old_stacks"]
                   + [f"breakpoint_axes_stacks_{m:g}min" for m in STACK_MINUTES_BRACKET]
                   + ["breakpoint_axes"]]
    stack_counts = [totals(verdict_counts(rows, rule=rule)) for rule in stack_rules]
    for v in VERDICT_ORDER:
        L.append(f"| {v} | " + " | ".join(str(c.get(v, 0)) for c in stack_counts) + " |")
    if no_assists is not None:
        c = totals(verdict_counts(no_assists))
        L += ["", "Assists off (`ASSIST_FIRST` = never; kills unchanged), new rule: "
              + ", ".join(f"{v} {c.get(v, 0)}" for v in VERDICT_ORDER) + "."]
    for label, alt in sensitivity:
        c = totals(verdict_counts(alt))
        L += ["", f"{label}, new rule: " + ", ".join(f"{v} {c.get(v, 0)}" for v in VERDICT_ORDER) + "."]
    L += ["", "Band sensitivity (all roles, new rule):", ""]
    for b in SENSITIVITY_BANDS:
        c = totals(verdict_counts(rows, b))
        L.append(f"- ±{b:.0%}: " + ", ".join(f"{v} {c.get(v, 0)}" for v in VERDICT_ORDER))
    phased = [r for r in judged(rows) if r["verdict_unwithheld"] in (EARLY_GAME, LATE_GAME)]
    if phased:
        L += ["", "## Early- and late-game builds", "",
              "Ichor's build ahead at 2 and 4 items and behind at six is an early-game build; the "
              "reverse is a late-game build (composite √(damage × survival), Ichor over community):", ""]
        for r in sorted(phased, key=lambda r: r["god"]):
            bp = r["breakpoint_axes"]
            L.append(f"- {r['god']} ({r['role']}): **{r['verdict_unwithheld']}**"
                     + (" (withheld for coverage)" if r["verdict"] == NOT_ENOUGH_SIMULATED else "")
                     + " — " + ", ".join(f"{k} items {_pct(math.sqrt(bp[k][0] * bp[k][1]))}"
                                         for k in BREAKPOINTS))
    excluded = aspect_excluded(rows)
    L += ["", f"## Aspect not simulated ({len(excluded)} gods, no verdict, not counted)", "",
          f"The community plays an aspect in more than {ASPECT_MAJORITY:.0%} of these gods' games "
          "and `combat.py` cannot play an aspect kit, so a base-kit comparison would not be fair. "
          "Most-played first — this is the list to simulate next:", ""]
    for r in excluded:
        k = r["kit"]
        L.append(f"- {r['god']} ({r['role']}): {k['aspect']}, {k['pick_rate']:.0%} of games"
                 + (f", {k['win_rate']:.0%} win" if k.get("win_rate") is not None else ""))
    L += ["", "## Where the community wins", ""]
    for r in community_wins(rows):
        d, sv = r["weighted_axes"]
        swap = top_swap(r)
        L.append(f"- {r['god']} ({r['role']}): weighted damage {_pct(d)}, survival {_pct(sv)}"
                 + (f"; most recovered by {swap['item']} for {swap['replaces']} "
                    f"(damage {_pct(swap['damage_axis'])})" if swap else ""))
    withheld = community_wins(rows, withheld=True)
    if withheld:
        L += ["", "Would be community better, withheld for coverage:", ""]
        for r in withheld:
            d, sv = r["weighted_axes"]
            c = r["coverage"]
            swap = top_swap(r)
            L.append(f"- {r['god']} ({r['role']}): weighted damage {_pct(d)}, survival {_pct(sv)}; "
                     f"simulated {c['ichor']:.0%} Ichor / {c['community']:.0%} community"
                     + (f"; most recovered by {swap['item']} for {swap['replaces']} "
                        f"(damage {_pct(swap['damage_axis'])})" if swap else ""))
    L += ["", "## Not simulated (items in compared builds)", "",
          "| item | status | builds | why |", "|---|---|---|---|"]
    for name, e in not_simulated(rows).items():
        L.append(f"| {name} | {e['status']} | {e['builds']} | {e['why']} |")
    if skipped:
        L += ["", "## Skipped", ""] + [f"- {s['god']}: {s['reason']}" for s in skipped]
    L += ["", "# Per god", ""]
    for r in rows:
        L += god_lines(r)
    return L


def with_overrides(gods, items, builds_by_god, weights, tags_map, **overrides):
    """The roster re-run with module constants overridden, for a sensitivity
    line (`HEALING=False`, `HEAL_UNTIL=WINDOW`)."""
    g = globals()
    saved = {k: g[k] for k in overrides}
    g.update(overrides)
    try:
        return run(gods, items, builds_by_god, weights, tags_map)[0]
    finally:
        g.update(saved)


#: The healing sensitivity lines the report prints.
HEALING_SENSITIVITY = (
    ("Healing off (HEALING = False: no lifesteal, no heals, target never heals)", {"HEALING": False}),
    (f"Heals in the first {WINDOW:.0f}s fight only (HEAL_UNTIL = WINDOW)", {"HEAL_UNTIL": WINDOW}),
)


def without_assists(gods, items, builds_by_god, weights, tags_map):
    """The roster re-run with no assists, for the report's sensitivity line."""
    global ASSIST_FIRST
    saved, ASSIST_FIRST = ASSIST_FIRST, math.inf
    try:
        return run(gods, items, builds_by_god, weights, tags_map)[0]
    finally:
        ASSIST_FIRST = saved


def _jsonable(x):
    if isinstance(x, dict):
        return {str(k): _jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_jsonable(v) for v in x]
    if isinstance(x, float):
        return round(x, 4) if math.isfinite(x) else None
    return x


def slug(name):
    """File name for a god — the viewer's `iconSlug` exactly (spaces to
    hyphens, apostrophes dropped), so the page can derive it from the name."""
    return name.lower().replace(" ", "-").replace("'", "")


def viewer_god(r):
    """One god's comparison, trimmed to what the page draws."""
    def side(p):
        keep = DAMAGE_KEYS + SURVIVAL_KEYS + [
            "items", "gold", "mean_cooldown", "ultimate_cooldown", "cooldown_rate",
            "crit_chance", "crit_multiplier", "crit_ev", "attacks_per_second", "passives"]
        out = {k: p[k] for k in keep}
        out["breakpoints"] = p["breakpoints"]
        return out
    return {"god": r["god"], "role": r["role"], "melee": r["melee"], "kit": r["kit"],
            "damage_axis": r["damage_axis"], "survival_axis": r["survival_axis"],
            "verdict": r["verdict"], "verdict_unwithheld": r["verdict_unwithheld"],
            "verdict_six_only": r["verdict_six_only"], "coverage": r["coverage"],
            "weighted_axes": r["weighted_axes"], "breakpoint_axes": r["breakpoint_axes"],
            "shared": r["shared"],
            "substitutions": r["community_substitutions"],
            "ichor": side(r["ichor"]), "community": side(r["community"]),
            "diffs": r["diffs"]}


def write_viewer_files(out_dir, rows, skipped, targets, patch):
    """`<dir>/<god>.json` per god plus `_meta.json` (targets, rule, counts).
    Per god so the page fetches ~10 KB on demand instead of the roster."""
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.json"):
        old.unlink()
    dump = lambda obj: json.dumps(_jsonable(obj), ensure_ascii=False, separators=(",", ":"))
    for r in rows:
        (out_dir / f"{slug(r['god'])}.json").write_text(dump(viewer_god(r)), encoding="utf-8")
    (out_dir / "_meta.json").write_text(dump({
        "data": patch, "level": LEVEL, "window": WINDOW, "band": BAND,
        "breakpoint_weights": BREAKPOINT_WEIGHTS, "coverage_min": COVERAGE_MIN,
        "coverage_gap": COVERAGE_GAP,
        "verdict_counts_six_only": verdict_counts(rows, rule=judge_six_only),
        "targets": targets, "skipped": skipped, "verdict_counts": verdict_counts(rows),
        "aspect_majority": ASPECT_MAJORITY,
        "aspect_not_simulated": [r["god"] for r in aspect_excluded(rows)],
    }), encoding="utf-8")


def load_inputs():
    items = recommend.load_items()
    gods = recommend.load_gods()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags_map = scoring.load_tags(recommend.TAGS_PATH)
    builds = {g["name"]: recommend.load_build_note(g["name"]) for g in gods}
    return items, gods, weights, tags_map, builds


def data_patch():
    try:
        p = json.loads((REPO_ROOT / "data" / "_patch.json").read_text(encoding="utf-8"))
        return f"items/gods {p.get('data_patch')}, community window {p.get('patch')}"
    except (OSError, ValueError):
        return "unknown patch"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--god")
    ap.add_argument("--out", type=Path, default=REPORT_PATH)
    ap.add_argument("--json", type=Path, nargs="?", const=JSON_DIR, default=None,
                    help=f"also write the viewer's per-god files (default dir {JSON_DIR})")
    args = ap.parse_args(argv)
    items, gods, weights, tags_map, builds = load_inputs()
    rows, skipped, targets = run(gods, items, builds, weights, tags_map, only=args.god)
    if args.god:
        if not rows:
            print(f"{args.god}: {skipped[0]['reason'] if skipped else 'unknown god'}", file=sys.stderr)
            return 1
        print("\n".join(god_lines(rows[0])))
        return 0
    patch = data_patch()
    sens = [(label, with_overrides(gods, items, builds, weights, tags_map, **o))
            for label, o in HEALING_SENSITIVITY]
    args.out.write_text("\n".join(report_lines(rows, skipped, targets, patch, without_assists(
        gods, items, builds, weights, tags_map), sensitivity=sens)) + "\n", encoding="utf-8")
    if args.json:
        write_viewer_files(args.json, rows, skipped, targets, patch)
    counts = verdict_counts(rows)
    print(f"{len(rows)} gods compared, {len(judged(rows))} judged, "
          f"{len(aspect_excluded(rows))} aspect not simulated, {len(skipped)} skipped; wrote {args.out}"
          + (f" and {args.json}" if args.json else ""))
    for role in sorted(counts):
        print(f"  {role:<8} " + ", ".join(f"{k} {v}" for k, v in sorted(counts[role].items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
