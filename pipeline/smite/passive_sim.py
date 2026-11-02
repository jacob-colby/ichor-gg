"""Item passives SIMULATED, one item at a time, from the item's own text.

WHY THIS EXISTS. Done criterion 2 (2026-11-02) asks for Ichor's build and the
community's to be run "through Ichor's combat model with item passives
simulated, not priced". The passives analysis of the same day is the reason
for the word: pricing passives in the gold model recovers ~0% of the
community's choices by passive TYPE and 7% learned per item and role, and the
values hang together per ITEM. So a passive here is never one price per class
(register §4.20's classes are a refusal, not a pricing table); it is a few
lines of arithmetic that do what that one item says, inside the clock
`side_by_side.simulate` runs.

THE RULE: NEVER INVENT A VALUE. Every number below is read off the item text
quoted beside it (the wiki scrape in `data/Items`, Open Beta 46 as of
2026-11-02). Where the text needs a reading it does not settle — "Attack
Damage" as the stat or as the swing, "dealt 4 times" as four instances of the
stated amount — the reading taken is written next to the code and is the
LITERAL one. Where the effect depends on something this comparison does not
contain (a kill, crowd control, an enemy's shield, movement, an active's
timing, the enemy's hit rate on you), the item is `NOT_SIMULATED` with the
reason, and the side-by-side prints that reason beside the build. A partly
modelled item (`PARTIAL`) says which half is missing.

WHAT THE CLOCK ASSUMES, so the hooks below can be read without the engine:
  * one target, a god, in range for the whole window (so an aura such as
    Sanguine Lash's 4m ticks every second)
  * our god at FULL health. Health-gated OFFENSIVE branches take the full-
    health side (Riptalon +10%, Shifter's Shield's adaptive power, Bancroft's
    Talon +0). Health-gated DEFENSIVE branches are not a guess at all: effective
    health integrates over the whole health bar, so "below 60% health: +15
    protections" is exact as a piecewise sum (`ehp_segments`)
  * persistent stacks (Devourer's, Thebes, Book of Thoth, Transcendence) at
    ZERO on the 2- and 4-item breakpoints and FULL on the finished six — the
    two ends, not an invented time-to-full. `side_by_side.BREAKPOINTS` says so
    on the page.
  * kill- and assist-gated effects at zero kills: Rage's crit, Jotunn's and
    Spear of Desolation's cooldown refunds, Doom Orb's stacks. A ten-second
    window with one target contains no kill that would not end it.

HOOKS. Each `Passive` may carry any of:
  grants(ctx)           flat stats from the passive, before conversions
  converts(ctx)         stats computed from the post-grant totals (phase 2)
  on_attack(sim, ev)    extra hits / multipliers on a basic attack
  on_ability(sim, ev)   extra hits on an ability hit
  ehp_segments(ctx)     `[(share_of_health_bar, extra_phys, extra_mag)]`
  cooldown(ctx)         `{"ultimate": multiplier}` on base cooldowns
`ctx` is `StatContext` (the build's totals, level, stack state); `sim` is the
live `side_by_side` state. Tests in `test_passive_sim.py` hand-compute each
hook from frozen inputs.
"""
from dataclasses import dataclass, field
from typing import Callable, Optional

SIMULATED = "simulated"
PARTIAL = "partial"
NOT_SIMULATED = "not simulated"
NO_PASSIVE = "no passive"


@dataclass
class Passive:
    status: str
    summary: str
    assumptions: tuple = ()
    grants: Optional[Callable] = None
    converts: Optional[Callable] = None
    on_attack: Optional[Callable] = None
    on_ability: Optional[Callable] = None
    ehp_segments: Optional[Callable] = None
    cooldown: Optional[Callable] = None
    stacking: bool = False


@dataclass
class StatContext:
    """What a stat hook may read. `items` is the printed stat total of the
    six (or two, or four) items, `stats` the running total including earlier
    grants, `stacks` is "full" or "none"."""
    items: dict
    stats: dict
    level: int
    stacks: str = "full"
    names: tuple = ()
    extra: dict = field(default_factory=dict)


def _adaptive(strength, intelligence):
    """`Adaptive Stat: +S Strength or +I Intelligence (based on highest item
    stat)`. "Highest item stat" is read off the PRINTED item totals, the
    literal text; a tie goes to Strength (no item text addresses a tie)."""
    def grants(ctx):
        if ctx.items.get("Intelligence", 0.0) > ctx.items.get("Strength", 0.0):
            return {"Intelligence": intelligence}
        return {"Strength": strength}
    return grants


def _full(ctx):
    return ctx.stacks == "full"


# ── Persistent stacks ─────────────────────────────────────────────────────

def _devourers(ctx):
    # "Each Stack grants: +.4 Strength +0.05% Lifesteal. At 75 Stacks, gain:
    # +10 Strength +3% Lifesteal +5 Penetration. Continue to stack more slowly"
    # Full = 75 stacks: 30 + 10 Strength, 3.75 + 3 Lifesteal, 5 Penetration.
    # Stacks past 75 are not counted: the text gives no rate for "more slowly".
    if not _full(ctx):
        return {}
    return {"Strength": 0.4 * 75 + 10, "Lifesteal %": 0.05 * 75 + 3, "Penetration": 5.0}


def _thebes(ctx):
    # "Stacks grant +15 Max Health (max 40 Stacks). At 40 Stacks, Item evolves
    # and gains: +100 Max Health +10 Physical and Magical Protection"
    if not _full(ctx):
        return {}
    return {"Max Health": 15 * 40 + 100, "Physical Protection": 10.0,
            "Magical Protection": 10.0}


def _mana_from_items(ctx, per_stack_cap=50, per_stack=10, evolved_mana=100):
    """Mana counted by a `...% of Mana from Items` clause: the printed Max
    Mana of the items, plus the item's own stack mana ("Per Mana Infusion
    Stack: +10 Mana", 50 stacks) and evolution mana when full. The stack and
    evolution mana are counted as mana FROM ITEMS because the item grants it;
    the text does not say otherwise."""
    mana = ctx.items.get("Max Mana", 0.0)
    if _full(ctx):
        mana += per_stack_cap * per_stack + evolved_mana
    return mana


def _thoth_grants(ctx):
    # "+5 Penetration +100 Mana" on evolving; the mana goes in via the converter.
    return {"Penetration": 5.0} if _full(ctx) else {}


def _thoth_converts(ctx):
    # "+Intelligence equal to 5% of Mana from Items" and, evolved, "Additional
    # +Intelligence equal to 2% of Mana from Items".
    pct = 0.07 if _full(ctx) else 0.05
    return {"Intelligence": pct * _mana_from_items(ctx)}


def _transcendence_grants(ctx):
    # Evolved: "+10 Penetration +100 Mana".
    return {"Penetration": 10.0} if _full(ctx) else {}


def _transcendence_converts(ctx):
    # "+Strength equal to 3% of Mana from Items" — no evolved increase to the 3%.
    return {"Strength": 0.03 * _mana_from_items(ctx)}


# ── Conversions ───────────────────────────────────────────────────────────

def _tahuti(ctx):
    # "+Intelligence equal to 25% of your Intelligence from items."
    # "From items" = printed item Intelligence plus item-passive grants already
    # applied (adaptive, conversions earlier in the phase), all of which come
    # from items.
    return {"Intelligence": 0.25 * ctx.stats.get("Intelligence", 0.0)}


def _nimble(ctx):
    # "For every 10 Intelligence: +1 Attack Damage +1% Attack Speed". "For
    # every 10" is read as whole tens (floor) — the literal reading.
    tens = int(ctx.stats.get("Intelligence", 0.0) // 10)
    return {"Attack Damage": float(tens), "Attack Speed %": float(tens)}


def _shell(ctx):
    # "+7.5% of all Stats from Items." Applied to the PRINTED item totals only,
    # so it cannot compound with another item's passive grant.
    return {k: 0.075 * v for k, v in ctx.items.items() if v}


# ── Basic-attack procs ────────────────────────────────────────────────────

def _flat_on_attack(amount, dtype="physical"):
    def hook(sim, ev):
        sim.proc(amount, dtype, ev)
    return hook


def _tyrfing(sim, ev):
    # "Attacks deal +15 bonus Physical Damage. On God hit: Increase bonus
    # Damage by +15 for 4s Stacks once, +1 Stack per 4 Levels (Max 6 Stacks)"
    # Cap at level L = min(6, 1 + L // 4): 6 at level 20. The stack lands
    # AFTER the hit that applies it.
    st = sim.item_state("Tyrfing", stacks=0, until=-1.0)
    stacks = st["stacks"] if ev.t <= st["until"] else 0
    sim.proc(15.0 + 15.0 * stacks, "physical", ev)
    st["stacks"] = min(stacks + 1, min(6, 1 + sim.level // 4))
    st["until"] = ev.t + 4.0


def _qins(sim, ev):
    # "Bonus Damage = +2% Target Base Health +5% Target Item Health" (physical)
    sim.proc(0.02 * sim.target["base_health"] + 0.05 * sim.target["item_health"],
             "physical", ev)


def _golden_blade(sim, ev):
    # "Damage = +10 + 20% of your Item Protections" — item protections read as
    # physical plus magical protection carried on items, passive grants included.
    prot = sim.stats.get("Physical Protection", 0.0) + sim.stats.get("Magical Protection", 0.0)
    sim.proc(10.0 + 0.20 * prot, "physical", ev)


def _bragi(sim, ev):
    # "Attack Hit: +10 (+3 per Level) bonus Magical Damage"
    sim.proc(10.0 + 3.0 * sim.level, "magical", ev)


def _odysseus(sim, ev):
    # "Every fourth Attack Hit: Trigger Chain Lightning. Damage = 15 (+60%
    # Attack Damage) Physical Damage Hits target and up to 4 nearby enemies".
    # LITERAL READING: "Attack Damage" is the stat of that name (Silverbranch's
    # text says "Basic Attack Damage" when it means the swing, so the two texts
    # are read as meaning different things). One target, so one hit — "can hit
    # the same target more than once" needs another enemy to bounce through.
    if ev.attack_index % 4 == 3:
        sim.proc(15.0 + 0.60 * sim.stats.get("Attack Damage", 0.0), "physical", ev)


def _silverbranch(sim, ev):
    # "Every third Attack Hit: Fire a homing Silver Arrow at your target.
    # Damage = 25% of you Basic Attack Damage as Physical Damage. Fire 1 arrow
    # for every 1 Attack Speed you have" — whole attacks per second, at least 1.
    if ev.attack_index % 3 == 2:
        arrows = max(1, int(sim.attacks_per_second()))
        sim.proc(arrows * 0.25 * ev.raw, "physical", ev)


def _riptalon(sim, ev):
    # "While Above 50% Health: Attacks gain +10% Damage" — full-health branch.
    ev.multiplier *= 1.10


def _dominance(sim, ev):
    # "Basic Attacks gain an additional +20% Penetration This effect ignores
    # the Penetration cap"
    ev.uncapped_pct_pen += 0.20


def _executioner(sim, ev):
    # "Attack a God or Boss: Apply 1 Stack of Piercing. Piercing reduces 7%
    # Protections for 4s. Stacks up to 4 times." Applied AFTER the hit; each
    # application refreshes the stack (`Sim.add_shred`).
    sim.after(lambda: sim.add_shred("The Executioner", 0.07, 4, 4.0, ev.t))


def _avenging(sim, ev):
    # "-3.5% Protections ... Debuff lasts 4s, Stacks up to 3 times." The
    # doubling ("in Jungle OR heals 5%") is not met by a single duel target.
    sim.after(lambda: sim.add_shred("Avenging Blade", 0.035, 3, 4.0, ev.t))


def _bracer(sim, ev):
    # "Hit enemy Gods: +8 Attack Damage for 10s. Stacks up to 8 times." AFTER
    # the hit.
    st = sim.item_state("Bracer of The Abyss", stacks=0, until=-1.0)
    stacks = st["stacks"] if ev.t <= st["until"] else 0
    st["stacks"], st["until"] = min(stacks + 1, 8), ev.t + 10.0
    sim.dynamic["Attack Damage"] = 8.0 * st["stacks"]


def _toxic(sim, ev):
    # "Gain 7% Attack Speed for 5s ... can stack up to 3 times." Self-buff only;
    # the 40% healing reduction has nothing to reduce in a duel with no heals.
    st = sim.item_state("Toxic Blade", stacks=0, until=-1.0)
    stacks = st["stacks"] if ev.t <= st["until"] else 0
    st["stacks"], st["until"] = min(stacks + 1, 3), ev.t + 5.0
    sim.dynamic["Attack Speed %"] = 7.0 * st["stacks"]


def _polynomicon_attack(sim, ev):
    # "Ability Used: Your next Attack deals bonus Magical Damage. Damage = 80%
    # of your Intelligence. Cooldown: 2s"
    st = sim.item_state("Polynomicon", primed=False, ready=0.0)
    if st["primed"]:
        sim.proc(0.80 * sim.stat("Intelligence"), "magical", ev)
        st["primed"], st["ready"] = False, ev.t + 2.0


def _polynomicon_ability(sim, ev):
    st = sim.item_state("Polynomicon", primed=False, ready=0.0)
    if ev.t >= st["ready"]:
        st["primed"] = True


def _hydra_attack(sim, ev):
    # "Ability Used: Bonus Damage on your next successful Attack. +30% for
    # Melee or +20% for Ranged. Buff lasts 8s." Melee/ranged from the god's own
    # basic-attack range (`side_by_side.is_melee`).
    st = sim.item_state("Hydra's Lament", until=-1.0)
    if ev.t <= st["until"]:
        ev.multiplier *= 1.30 if sim.melee else 1.20
        st["until"] = -1.0


def _hydra_ability(sim, ev):
    sim.item_state("Hydra's Lament", until=-1.0)["until"] = ev.t + 8.0


# ── Ability-hit procs ─────────────────────────────────────────────────────

def _soul_reaver(sim, ev):
    # "Ability Hit: +Bonus Magical Damage. Bonus Damage = +1.2% Target Base
    # Health & +3% Target Item Health, dealt 4 times over 2s. Triggers once per
    # Ability, per god." LITERAL READING: four instances of the stated amount,
    # at 0.5s spacing; ticks past the window's end are not counted.
    per_tick = 0.012 * sim.target["base_health"] + 0.03 * sim.target["item_health"]
    st = sim.item_state("Soul Reaver", fired=set())
    if ev.name in st["fired"]:
        return
    st["fired"].add(ev.name)
    ticks = sum(1 for k in range(1, 5) if sim.window is None or ev.t + 0.5 * k < sim.window)
    sim.proc(per_tick * ticks, "magical", ev)


def _heartseeker(sim, ev):
    # "Damage = 2% of your Strength, as a % of the target's Max Health." So
    # 200 Strength is 4% of max health, physical, per ability hit.
    pct = 0.02 * sim.stat("Strength") / 100.0
    sim.proc(pct * sim.target["max_health"], "physical", ev)


def _crusher(sim, ev):
    # "Ability Hit: +Physical Damage. Damage = 35% of your Strength. Damage is
    # dealt over 1s." The "+33% on subsequent hits, over 3s" clause has no
    # stated base window and is not counted (`PARTIAL`).
    sim.proc(0.35 * sim.stat("Strength"), "physical", ev)


def _soul_gem(sim, ev):
    # "Ability Hit: +1 Stack. Three Stacks: Next Ability Hit: Deals Bonus
    # Damage (40% Intelligence) ... Removes the Stacks". The damage type is not
    # stated; it is taken as the god's own.
    st = sim.item_state("Soul Gem", stacks=0)
    if st["stacks"] >= 3:
        sim.proc(0.40 * sim.stat("Intelligence"), sim.damage_type, ev)
        st["stacks"] = 0
    else:
        st["stacks"] += 1


def _divine_ruin(sim, ev):
    # "trigger Chain Lightning when off cooldown: Magical Damage = 40 + 20%
    # Intelligence ... Cooldown: 15s" — on god damaged, so the first hit of a
    # fight. One target, one hit.
    st = sim.item_state("Divine Ruin", ready=0.0)
    if ev.t >= st["ready"]:
        sim.proc(40.0 + 0.20 * sim.stat("Intelligence"), "magical", ev)
        st["ready"] = ev.t + 15.0


def _shattering(name):
    # "First Ability Cast: Gains +20% Penetration This effect ignores the
    # Penetration cap Shattering does not Stack with itself. Cooldown: 10s"
    def hook(sim, ev):
        st = sim.item_state("Shattering", ready=0.0)  # shared: does not stack
        if ev.t >= st["ready"]:
            ev.uncapped_pct_pen += 0.20
            st["ready"] = ev.t + 10.0
    return hook


def _barbed_carver_ability(sim, ev):
    # "Ability Hit: Target gains +1 Stack of Jagged Wounds for 5s (max 3)
    # Triggers once per Ability, per target. Each Stack: +8% (+1% per 10%
    # Lifesteal) Attack and Ability Damage as Physical Damage."
    # Read as: each attack/ability hit on the wounded target deals that share
    # of the hit's pre-mitigation damage again, as physical. The stack lands
    # AFTER the hit that applies it.
    _barbed_bonus(sim, ev)
    st = sim.item_state("Barbed Carver", expiries=[], seen=set())
    if ev.name in st["seen"]:
        return
    st["seen"].add(ev.name)
    live = sorted(t for t in st["expiries"] if t > ev.t)
    st["expiries"] = (live + [ev.t + 5.0])[-3:]


def _barbed_bonus(sim, ev):
    st = sim.item_state("Barbed Carver", expiries=[], seen=set())
    stacks = sum(1 for t in st["expiries"] if t > ev.t)
    if stacks:
        share = 0.08 + 0.01 * int(sim.stat("Lifesteal %") // 10)
        sim.proc(stacks * share * ev.raw, "physical", ev)


def _spear_magus(sim, ev):
    # "Ability Hit a God: That God is marked for 8s. Marked Gods take 5%
    # increased damage from all sources." Marked from the hit AFTER.
    st = sim.item_state("Spear of the Magus", until=-1.0)
    sim.after(lambda: st.update({"from": ev.t, "until": ev.t + 8.0}))


# ── Aura ──────────────────────────────────────────────────────────────────

def _sanguine(sim, t):
    # "Enemy gods Within 4m: -0.5% Health (max 200) as Physical Damage per 1s.
    # +0.66% for every 10% Lifesteal". Health read as the target's MAX health;
    # "max 200" as a cap on each tick. Whole tens of lifesteal.
    pct = 0.5 + 0.66 * int(sim.stat("Lifesteal %") // 10)
    return min(200.0, pct / 100.0 * sim.target["max_health"])


# ── Effective health ──────────────────────────────────────────────────────

def _berserker_ehp(ctx):
    # "When falling below 60% Health: ... +15 Physical Protection +15 Magical
    # Protection" — the bottom 60% of the bar carries the extra protection.
    return [(0.40, 0.0, 0.0), (0.60, 15.0, 15.0)]


def _shifter_ehp(ctx):
    # "Under 75% Health: +20 Physical and Magical Protection."
    return [(0.25, 0.0, 0.0), (0.75, 20.0, 20.0)]


def _shifter_grants(ctx):
    # "Over 75% Health: +30 Strength or +40 Intelligence (whichever is
    # higher)" — full-health branch, for damage only (the EHP split above).
    return _adaptive(30.0, 40.0)(ctx)


def _freya_ehp(ctx):
    # "On 25% of your Health Lost: +15 Physical and Magical Protections for 5s
    # Can stack up to 2 times." Exact on a fight that drains the bar inside 5s
    # (a burst); the first quarter carries none, the second 15, the rest 30.
    return [(0.25, 0.0, 0.0), (0.25, 15.0, 15.0), (0.50, 30.0, 30.0)]


def _world_stone(ctx):
    # "-25% Cooldown for your Ultimate Ability." Applied to the base cooldown.
    return {"ultimate": 0.75}


def _brawler_grants(ctx):
    return _adaptive(35.0, 50.0)(ctx)


# Every item whose effect is simulated or explicitly refused. An item absent
# from this table and carrying passive text reads `NOT_SIMULATED` with the
# reason "no simulator written yet", which is a gap and says so.
REGISTRY = {
    # The fifteen undervalued items from the 2026-11-02 passives analysis.
    "Devourer's Gauntlet": Passive(SIMULATED, "75 stacks: +40 Strength, +6.75% Lifesteal, +5 Penetration",
                                   ("full stacks on the finished build, none at 2 and 4 items",
                                    "stacks past 75 not counted (no rate given)"),
                                   grants=_devourers, stacking=True),
    "Gauntlet of Thebes": Passive(SIMULATED, "40 stacks + evolve: +700 Max Health, +10/+10 protections",
                                  ("full stacks on the finished build, none at 2 and 4 items",),
                                  grants=_thebes, stacking=True),
    "The Executioner": Passive(SIMULATED, "adaptive +30 Str / +55 Int; attacks shred 7% protections per stack (4)",
                               ("stack applies after the hit", "shreds sum with other shreds"),
                               grants=_adaptive(30.0, 55.0), on_attack=_executioner),
    "Barbed Carver": Passive(SIMULATED, "ability hits stack Jagged Wounds (3): each stack repeats 8% (+1% per 10% LS) of every hit as physical",
                             ("bonus is a share of the hit's pre-mitigation damage",),
                             on_attack=_barbed_bonus, on_ability=_barbed_carver_ability),
    "Book of Thoth": Passive(SIMULATED, "Int = 5% of item mana (7% evolved); 50 stacks +500 mana, evolve +100 mana +5 pen",
                             ("full stacks on the finished build, none at 2 and 4 items",),
                             grants=_thoth_grants, converts=_thoth_converts, stacking=True),
    "Magi's Cloak": Passive(NOT_SIMULATED, "CC-immunity bubble every 90s",
                            ("the comparison contains no crowd control",)),
    "Soul Reaver": Passive(SIMULATED, "each ability: 4 ticks of 1.2% base + 3% item health, magical",
                           ("literal reading: four instances of the stated amount",
                            "once per ability per god"),
                           on_ability=_soul_reaver),
    "Brawler’s Beat Stick": Passive(PARTIAL, "adaptive +35 Str / +50 Int; +2% Str/Int/protections per 1.5s in combat (5)",
                                    ("stacks build from 0 at the start of the window",
                                     "40% healing reduction not simulated (no healing in a duel)",
                                     "effective health read at 0 stacks (entering the fight)"),
                                    grants=_brawler_grants),
    "Nimble Ring": Passive(SIMULATED, "per 10 Intelligence: +1 Attack Damage, +1% Attack Speed",
                           ("whole tens of Intelligence",), converts=_nimble),
    "Odysseus' Bow": Passive(SIMULATED, "every 4th attack: 15 + 60% Attack Damage (stat), physical",
                             ("literal reading: the Attack Damage STAT, not the swing",
                              "one target, so one chain hit"),
                             on_attack=_odysseus),
    "Polynomicon": Passive(SIMULATED, "after an ability, next attack +80% Int magical (2s cooldown)",
                           on_attack=_polynomicon_attack, on_ability=_polynomicon_ability),
    "Bancroft's Talon": Passive(PARTIAL, "up to +60 Int / +10% LS from missing health (cap at 40% health)",
                                ("simulated at full health: +0. The ceiling is +60 Intelligence",)),
    "Ethereal Staff": Passive(PARTIAL, "each ability hit steals 5% max health (60s)",
                              ("health steal changes both sides' max health mid-fight; damage unaffected,"
                               " effective health read before the fight",)),
    "Transcendence": Passive(SIMULATED, "Str = 3% of item mana; 50 stacks +500 mana, evolve +100 mana +10 pen",
                             ("full stacks on the finished build, none at 2 and 4 items",),
                             grants=_transcendence_grants, converts=_transcendence_converts,
                             stacking=True),
    "Gem of Isolation": Passive(NOT_SIMULATED, "15% slow on ability hit",
                                ("the comparison contains no movement",)),

    # Near-misses and the items both sides buy most.
    "Shell of Rebuke": Passive(PARTIAL, "+7.5% of all item stats; the rebuke field active is not simulated",
                               ("applied to printed item stats only",), converts=_shell),
    "Silverbranch Bow": Passive(SIMULATED, "every 3rd attack: one arrow per whole attack/s, 25% of the swing each",
                                on_attack=_silverbranch),
    "Riptalon": Passive(SIMULATED, "attacks +10% damage above 50% health",
                        ("full-health branch; below 50% it is +25% and +7.5% LS",), on_attack=_riptalon),
    "Heartseeker": Passive(SIMULATED, "ability hit: (2% of Strength)% of target max health, physical",
                           on_ability=_heartseeker),
    "Deathbringer": Passive(SIMULATED, "+35% crit damage, ADDS to 1.5x (measured in game)"),
    "Rod of Tahuti": Passive(SIMULATED, "+25% of item Intelligence", converts=_tahuti),
    "Obsidian Shard": Passive(SIMULATED, "first ability each 10s: +20% penetration past the cap",
                              on_ability=_shattering("Obsidian Shard")),
    "Titan's Bane": Passive(SIMULATED, "first ability each 10s: +20% penetration past the cap",
                            on_ability=_shattering("Titan's Bane")),
    "Dominance": Passive(SIMULATED, "basic attacks +20% penetration past the cap", on_attack=_dominance),
    "Tyrfing": Passive(SIMULATED, "attacks +15 physical, +15 per stack on god hit (6 at level 20)",
                       on_attack=_tyrfing),
    "Manchu Bow": Passive(SIMULATED, "attacks +10 physical", on_attack=_flat_on_attack(10.0)),
    "Qin's Blade": Passive(SIMULATED, "attacks +2% base +5% item health, physical", on_attack=_qins),
    "Golden Blade": Passive(SIMULATED, "attacks +10 + 20% item protections, physical", on_attack=_golden_blade),
    "Bragi's Harp": Passive(SIMULATED, "attacks +10 +3/level magical", on_attack=_bragi),
    "Bracer of The Abyss": Passive(SIMULATED, "+8 Attack Damage per god hit (8 stacks, 10s)", on_attack=_bracer),
    "Toxic Blade": Passive(PARTIAL, "+7% attack speed per hit (3 stacks); healing reduction not simulated",
                           on_attack=_toxic),
    "Hydra's Lament": Passive(SIMULATED, "after an ability, next attack +20% ranged / +30% melee",
                              on_attack=_hydra_attack, on_ability=_hydra_ability),
    "The Crusher": Passive(PARTIAL, "ability hit: +35% Strength physical; the +33% follow-up is not counted",
                           on_ability=_crusher),
    "Soul Gem": Passive(PARTIAL, "every 4th ability hit: +40% Int; the heal is not simulated",
                        on_ability=_soul_gem),
    "Divine Ruin": Passive(PARTIAL, "chain lightning 40 + 20% Int every 15s; healing reduction not simulated",
                           on_ability=_divine_ruin),
    "Spear of the Magus": Passive(SIMULATED, "ability hit marks the target: +5% damage taken for 8s",
                                  on_ability=_spear_magus),
    "Avenging Blade": Passive(SIMULATED, "attacks shred 3.5% protections per stack (3)", on_attack=_avenging),
    "Sanguine Lash": Passive(PARTIAL, "aura: 0.5% (+0.66% per 10% LS) target health per second; active not simulated",
                             ("target inside 4m for the whole window",)),
    "The World Stone": Passive(SIMULATED, "-25% ultimate cooldown", cooldown=_world_stone),
    "Berserker's Shield": Passive(PARTIAL, "below 60% health: +15/+15 protections (in EHP); +25% attack speed not in damage",
                                  ("damage read at full health",), ehp_segments=_berserker_ehp),
    "Shifter's Shield": Passive(SIMULATED, "over 75% health +30 Str / +40 Int; under 75% +20/+20 protections",
                                grants=_shifter_grants, ehp_segments=_shifter_ehp),
    "Freya's Tears": Passive(SIMULATED, "per 25% health lost: +15/+15 protections for 5s (2 stacks)",
                             ("the health is lost inside 5s",), ehp_segments=_freya_ehp),
    "Sun Beam Bow": Passive(PARTIAL, "adaptive +20 Str / +40 Int; the toggle active is not simulated",
                            grants=_adaptive(20.0, 40.0)),

    # Refused, each for the reason the comparison cannot contain.
    "Jotunn's Revenge": Passive(NOT_SIMULATED, "cooldown refund on kill/assist", ("no kill in a 10s duel",)),
    "Spear of Desolation": Passive(NOT_SIMULATED, "cooldown refund on kill/assist", ("no kill in a 10s duel",)),
    "Rage": Passive(NOT_SIMULATED, "+crit chance on kill/assist", ("read at 0 kills: printed 20% only",)),
    "Doom Orb": Passive(NOT_SIMULATED, "+8 Int per stack from kills/assists (10s)", ("no kill in a 10s duel",)),
    "The Reaper": Passive(NOT_SIMULATED, "heal on kill/assist", ("no kill in a 10s duel",)),
    "Genji's Guard": Passive(NOT_SIMULATED, "cooldowns refund when hit by magical abilities", ("no attacker on our god",)),
    "Breastplate of Valor": Passive(NOT_SIMULATED, "cooldowns refund on health lost", ("no attacker on our god",)),
    "Kinetic Cuirass": Passive(NOT_SIMULATED, "shockwave after taking 3 attacks", ("no attacker on our god",)),
    "Draconic Scale": Passive(NOT_SIMULATED, "+4 protections per hit taken (1.5s)", ("needs the attacker's hit rate",)),
    "Erosion": Passive(NOT_SIMULATED, "reduces enemy shields", ("no enemy shield in the comparison",)),
    "Runeforged Hammer": Passive(NOT_SIMULATED, "rune on hard CC", ("no crowd control",)),
    "Gluttonous Grimoire": Passive(NOT_SIMULATED, "stores lifesteal healing as damage", ("no healing modelled",)),
    "Tekko-Kagi": Passive(NOT_SIMULATED, "pathfinding on ability use", ("no movement",)),
    "Hastened Fatalis": Passive(NOT_SIMULATED, "movement penalty reduction", ("no movement",)),
    "Musashi's Dual Swords": Passive(NOT_SIMULATED, "movement speed on crit", ("no movement",)),
    "Hussar's Wings": Passive(NOT_SIMULATED, "slow immunity", ("no movement",)),
    "Demon Blade": Passive(NOT_SIMULATED, "+30% attack speed for 3s after a crit",
                           ("crit is an expected value here, not a sequence",)),
    "Shield of the Phoenix": Passive(NOT_SIMULATED, "heal on ability hit", ("no healing modelled",)),
    "Eye of Providence": Passive(NOT_SIMULATED, "ward economy", ("no wards",)),
}

#: Actives: "On Use" items. Their timing is a player decision with a
#: cooldown measured in tens of seconds; the window would have to choose when
#: to press it. Refused by a rule rather than one by one.
ACTIVE_REASON = "active item: when it is pressed is a player decision"


def lookup(item):
    """The `Passive` for an item dict — registry first, then the two
    structural refusals (no passive text; an active), then "not written"."""
    name = item.get("name")
    if name in REGISTRY:
        return REGISTRY[name]
    text = (item.get("passive") or "").strip()
    if not text:
        return Passive(NO_PASSIVE, "")
    if "On Use" in text:
        return Passive(NOT_SIMULATED, text[:90], (ACTIVE_REASON,))
    return Passive(NOT_SIMULATED, text[:90], ("no simulator written yet",))
