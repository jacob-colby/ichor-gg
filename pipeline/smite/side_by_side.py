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

THE VERDICT RULE (`verdict`), written before the run and not tuned after it.
Two axes, each a geometric mean of Ichor-over-community ratios:
  damage D   = sustained 10s and burst, each vs squishy and vs tank (4 ratios)
  survival S = effective health vs physical and vs magical (2 ratios)
With band b = `BAND` (5%):
  Ichor better      one axis above 1+b, the other not below 1-b
  community better  one axis below 1-b, the other not above 1+b
  trade-off         one axis above 1+b and the other below 1-b
  level             both inside the band
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
lifesteal sustain, healing, waves, objectives, and every passive
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

from smite import (build_quality as bq, combat, damage_value, efficiency,
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
    """One build on one god against one target over one window."""

    def __init__(self, god, names, items_by_name, target, *, window=WINDOW, level=LEVEL,
                 stacks="full", disabled=()):
        self.god, self.names, self.level, self.target = god, list(names), level, target
        self.window = window
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

    # stats at the current instant
    def stat(self, key):
        v = self.base_stats.get(key, 0.0) + self.dynamic.get(key, 0.0)
        if "Brawler’s Beat Stick" in self.active and key in ("Strength", "Intelligence"):
            # "While in Combat: +2% Strength, +2% Intelligence ... every 1.5s.
            # Stacks up to 5 times." Combat starts at t=0, first stack at 1.5s.
            v *= 1.0 + 0.02 * min(5, int(self.t // 1.5))
        return v

    @property
    def stats(self):
        keys = set(self.base_stats) | set(self.dynamic)
        return {k: self.stat(k) for k in keys}

    def attacks_per_second(self):
        return combat.attacks_per_second(self.base_aps, self.stat("Attack Speed %"))

    def crit_chance(self):
        return min(self.stat("Critical Chance %"), 100.0) / 100.0

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
        self.by_channel[ev.kind] += hit
        for amount, dtype, item in ev.procs:
            d = self.mitigated(amount, dtype, ev.t, kind="proc")
            self.by_channel["proc"] += d
            self.by_item[item] = self.by_item.get(item, 0.0) + d
        pending, self._after = self._after, []
        for fn in pending:
            fn()

    def _attack(self, t, index):
        self.t = t
        raw = combat.attack_damage(self.attack_power, self.attack_scaling, self.stats, self.mean_swing)
        self._resolve(Event(t, "attack", "Basic Attack", raw, attack_index=index))

    def _ability(self, t, a):
        self.t = t
        raw = combat.ability_damage(a["base"], a["scaling"], self.stats)
        self._resolve(Event(t, "ability", a["name"], raw, is_ultimate=a["is_ultimate"]))

    def _aura(self, t):
        if "Sanguine Lash" in self.active:
            self.t = t
            d = self.mitigated(passive_sim._sanguine(self, t), "physical", t, kind="proc")
            self.by_channel["proc"] += d
            self.by_item["Sanguine Lash"] = self.by_item.get("Sanguine Lash", 0.0) + d

    def run_window(self):
        """Abilities (rotation order) before a swing at the same instant;
        aura ticks at whole seconds up to and including the window's end."""
        nxt = {i: 0.0 for i in range(len(self.rotation))}
        next_attack, index = 0.0, 0
        auras = [float(k) for k in range(1, int(self.window) + 1)]
        while True:
            options = []
            if nxt:
                i = min(nxt, key=lambda k: (nxt[k], k))
                if nxt[i] < self.window:
                    options.append((nxt[i], 0, "ability", i))
            if next_attack < self.window:
                options.append((next_attack, 1, "attack", None))
            if auras:
                options.append((auras[0], 2, "aura", None))
            if not options:
                break
            t, _, kind, i = min(options)
            if kind == "ability":
                self._ability(t, self.rotation[i])
                nxt[i] = t + self.rotation[i]["effective_cooldown"]
            elif kind == "attack":
                self._attack(t, index)
                index += 1
                aps = self.attacks_per_second()
                next_attack = t + (1.0 / aps if aps > 0 else math.inf)
            else:
                self._aura(auras.pop(0))
        return self.total()

    def run_burst(self):
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

def power(god, names, items_by_name, targets, stacks="full", disabled=()):
    """The four damage figures and the two effective healths."""
    out = {}
    for tname, target in targets.items():
        s = Sim(god, names, items_by_name, target, stacks=stacks, disabled=disabled)
        out[f"sustained_{tname}"] = s.run_window()
        out[f"channels_{tname}"] = dict(s.by_channel)
        out[f"procs_{tname}"] = dict(s.by_item)
        b = Sim(god, names, items_by_name, target, window=None, stacks=stacks, disabled=disabled)
        out[f"burst_{tname}"] = b.run_burst()
    out["ehp_physical"], out["ehp_magical"], out["health"] = effective_health(
        god, names, items_by_name, stacks=stacks, disabled=disabled)
    return out


def profile(god, names, items_by_name, targets):
    names = list(names)
    full = power(god, names, items_by_name, targets)
    s = Sim(god, names, items_by_name, targets["squishy"])
    cds = [{"name": a["name"], "base": a["cooldown"], "effective": a["effective_cooldown"],
            "ultimate": a["is_ultimate"]} for a in s.rotation]
    p = s.crit_chance()
    passives = []
    for n in names:
        pv = passive_sim.lookup(items_by_name[n])
        passives.append({"item": n, "status": pv.status, "summary": pv.summary,
                         "assumptions": list(pv.assumptions)})
    breakpoints = {}
    for k in BREAKPOINTS:
        stacks = "full" if k == 6 else "none"
        pw = full if k == 6 else power(god, names[:k], items_by_name, targets, stacks=stacks)
        breakpoints[k] = {m: pw[m] for m in DAMAGE_KEYS + SURVIVAL_KEYS}
    return {
        "items": names, "gold": s.gold, **full,
        "cooldowns": cds,
        "cooldown_rate": s.base_stats.get("Cooldown Rate", 0.0),
        "mean_cooldown": _mean([c["effective"] for c in cds if not c["ultimate"]]),
        "ultimate_cooldown": _mean([c["effective"] for c in cds if c["ultimate"]]),
        "crit_chance": p, "crit_multiplier": s.crit_mult,
        "crit_ev": 1.0 + p * (s.crit_mult - 1.0),
        "attacks_per_second": s.attacks_per_second(),
        "breakpoints": breakpoints, "passives": passives,
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
    """The community's six, CLEANED: each slot's item if it can take a core
    slot for this god (`scoring.is_buildable` — a tier 3, a paid relic with
    stats, or the god's own item), else that slot's first alternate that can
    and is not already taken. Returns `(names, substitutions)`; fewer than six
    means the record cannot make a build and the god is skipped, named.

    80 of 90 raw community slot lists contain a tier-2 component (Evil Eye,
    Skeggox, Sage's Ring...), a statless relic (Blinking Abyss) or a
    duplicate, because SmiteBrain's slot is "what was in that slot", including
    a component sold later. Comparing a build with a 1000g component in it to
    six finished items would be a comparison of gold, not of choices."""
    entry = next((b for b in build_note.get("builds") or [] if b.get("source") == "community"), None)
    if not entry:
        return [], []
    ok = lambda n: n in items_by_name and scoring.is_buildable(items_by_name[n], god)
    names, subs = [], []
    for slot in entry.get("slot_order") or []:
        name = slot.get("name") if isinstance(slot, dict) else slot
        if ok(name) and name not in names:
            names.append(name)
            continue
        alt = next((a["name"] for a in (slot.get("alternates") or [])
                    if ok(a.get("name")) and a["name"] not in names), None) if isinstance(slot, dict) else None
        if alt:
            names.append(alt)
            subs.append({"slot": len(names), "dropped": name, "used": alt})
        else:
            subs.append({"slot": None, "dropped": name, "used": None})
    # A slot with no usable alternate (Medusa's sixth: Manchu Bow, whose
    # alternates are Silverbranch Bow, already taken, and Hunter's Bow, a
    # component) is filled with the most-picked usable alternate anywhere in
    # the record — the community's own next choice, never ours.
    pool = sorted(((a.get("pick_rate") or 0.0, a.get("name"))
                   for slot in entry.get("slot_order") or [] if isinstance(slot, dict)
                   for a in slot.get("alternates") or []), key=lambda x: -x[0])
    for _, alt in pool:
        if len(names) >= 6:
            break
        if ok(alt) and alt not in names:
            names.append(alt)
            gap = next((s for s in subs if s["used"] is None), None)
            if gap:
                gap.update(slot=len(names), used=alt, note="most-picked alternate in the record")
    return names[:6], subs


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
            "plating": items.get("Plating", 0.0), "dampening": items.get("Dampening", 0.0)}


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
        t = {k: statistics.median(r[k] for r in rows) for k in rows[0]}
        t["max_health"] = t["base_health"] + t["item_health"]
        t["role"], t["n"] = role, len(rows)
        out[label] = t
    return out


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
    return {
        "god": god["name"], "role": bq.primary_role(god), "damage_type": god.get("damage_type"),
        "melee": is_melee(god), "level": LEVEL, "window": WINDOW,
        "ichor": p_ours, "community": p_theirs, "community_substitutions": subs,
        "shared": [n for n in ours if n in community],
        "damage_axis": d, "survival_axis": s, "kit": kit,
        "verdict": verdict(d, s) if kit["simulated"] else ASPECT_NOT_SIMULATED,
        "diffs": diffs,
    }, None


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


def verdict_counts(rows, band=BAND):
    """Per role, over `judged` rows only."""
    out = {}
    for r in judged(rows):
        v = verdict(r["damage_axis"], r["survival_axis"], band)
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
         f"**Verdict: {r['verdict']}** — damage {_pct(r['damage_axis'])}, survival {_pct(r['survival_axis'])}",
         "",
         f"Kit: {kit_line(r['kit'])}",
         "",
         f"- Ichor ({i['gold']:.0f}g): {' · '.join(i['items'])}",
         f"- Community ({c['gold']:.0f}g): {' · '.join(c['items'])}",
         ]
    for s in r["community_substitutions"]:
        L.append(f"  - cleaned: slot item {s['dropped']} → "
                 + (f"{s['used']} ({s.get('note', 'that slot’s alternate')})" if s["used"]
                    else "no usable alternate"))
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


def report_lines(rows, skipped, targets, data_patch):
    L = ["# Ichor vs community, passives simulated", "",
         f"Data: {data_patch}. Level {LEVEL}, {WINDOW:.0f}s window. Ichor = the `model` build "
         "(meta off); community = the cleaned six. Generated by `python -m smite.side_by_side`; "
         "the rules are in that module's docstring.", "",
         "## Targets (medians of the community's own builds)", "",
         "| | role | n | base HP | item HP | phys prot | mag prot | plating | dampening |",
         "|---|---|---|---|---|---|---|---|---|"]
    for k, t in targets.items():
        L.append(f"| {k} | {t['role']} | {t['n']} | {t['base_health']:.0f} | {t['item_health']:.0f} "
                 f"| {t['physical_prot']:.0f} | {t['magical_prot']:.0f} | {t['plating']:.0f} | {t['dampening']:.0f} |")
    L += ["", "## Verdicts by role", "",
          f"Rule: band ±{BAND:.0%} on damage and survival axes (see the module docstring).", "",
          "| role | Ichor better | community better | trade-off | level |", "|---|---|---|---|---|"]
    counts = verdict_counts(rows)
    order = ("Ichor better", "community better", "trade-off", "level")
    tot = {v: 0 for v in order}
    for role in sorted(counts):
        L.append(f"| {role} | " + " | ".join(str(counts[role].get(v, 0)) for v in order) + " |")
        for v in order:
            tot[v] += counts[role].get(v, 0)
    L.append("| **all** | " + " | ".join(f"**{tot[v]}**" for v in order) + " |")
    L += ["", "Band sensitivity (all roles):", ""]
    for b in SENSITIVITY_BANDS:
        c = {}
        for r in judged(rows):
            v = verdict(r["damage_axis"], r["survival_axis"], b)
            c[v] = c.get(v, 0) + 1
        L.append(f"- ±{b:.0%}: " + ", ".join(f"{v} {c.get(v, 0)}" for v in order))
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
    losses = sorted((r for r in rows if r["verdict"] == "community better"),
                    key=lambda r: r["damage_axis"] * r["survival_axis"])
    for r in losses:
        L.append(f"- {r['god']} ({r['role']}): damage {_pct(r['damage_axis'])}, survival {_pct(r['survival_axis'])}")
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
            "verdict": r["verdict"], "shared": r["shared"],
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
    args.out.write_text("\n".join(report_lines(rows, skipped, targets, patch)) + "\n", encoding="utf-8")
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
