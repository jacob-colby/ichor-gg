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
Damage" (SMITE 2's name for the swing, not a stat), "dealt 4 times" as four instances of the
stated amount — the reading taken is written next to the code and is the
LITERAL one. Where the effect depends on something this comparison does not
contain (crowd control, an enemy's shield, movement, an ally, wards), the item
is `NOT_SIMULATED` with the reason, and the side-by-side prints that reason
beside the build. A partly modelled item (`PARTIAL`) says which half is
missing. Kills, assists, an enemy hitting our god and "On Use" presses WERE
on that list until 2026-11-02; `side_by_side`'s FIGHT block now puts them in
the clock, each with a written assumption, and the items gated on them read
those events.

WHAT THE CLOCK ASSUMES, so the hooks below can be read without the engine:
  * one target, a god, in range for the whole window (so an aura such as
    Sanguine Lash's 4m ticks every second)
  * our god's OFFENCE at full health unless the hook reads the fight's
    health bar (`sim.hp`: Bancroft's Talon, Berserker's Shield). Other
    health-gated OFFENSIVE branches take the full-health side (Riptalon +10%,
    Shifter's Shield's adaptive power). Health-gated DEFENSIVE branches are
    exact: effective health integrates over the whole health bar, so "below
    60% health: +15 protections" is a piecewise sum (`ehp_segments`), and the
    fight run reads the same slices
  * persistent stacks on the GAME CLOCK (`side_by_side.stack_state`): each
    item bought `MINUTES_PER_ITEM` after the last, full
    `STACK_MINUTES_TO_FULL` after purchase, read the moment each breakpoint is
    reached. "full" and "none" are still accepted, for the bracket.
  * takedowns from the FIGHT block: one kill per 10s fight when our damage
    reaches the target's max health, one assist every 10s from 5s.

HOOKS. Each `Passive` may carry any of:
  grants(ctx)           flat stats from the passive, before conversions
  converts(ctx)         stats computed from the post-grant totals (phase 2)
  on_attack(sim, ev)    extra hits / multipliers on a basic attack
  on_ability(sim, ev)   extra hits on an ability hit
  ehp_segments(ctx)     `[(share_of_health_bar, extra_phys, extra_mag)]`
  cooldown(ctx)         `{"ultimate": multiplier}` on base cooldowns
  on_takedown(sim, k)   a kill or an assist ("kill" | "assist")
  on_hit_taken(sim, h)  after an enemy hit lands on our god
  reduce_hit(sim, h)    a multiplier on an enemy hit before it lands
  prot_bonus(sim, d)    extra protection against damage type d right now
  stat_bonus(sim, k, v) a stat at this instant (`bonus_keys` names which)
  active(sim)           an "On Use" press; True if it fired. Pressed at the
                        fight's start, at the first hit taken, or after the
                        opening casts (`active_trigger`), then on
                        `active_cooldown`
`ctx` is `StatContext` (the build's totals, level, stack state); `sim` is the
live `side_by_side` state. Tests in `test_side_by_side.py` and
`test_fight.py` hand-compute each hook from frozen inputs.
"""
import math
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
    # The fight layer (2026-11-02, `side_by_side`'s FIGHT block): events the
    # duel did not contain before — takedowns, an enemy hitting our god, and
    # "On Use" presses.
    on_takedown: Optional[Callable] = None     # (sim, "kill" | "assist")
    on_hit_taken: Optional[Callable] = None    # (sim, hit) after the hit lands
    reduce_hit: Optional[Callable] = None      # (sim, hit) -> multiplier, before it lands
    prot_bonus: Optional[Callable] = None      # (sim, dtype) -> extra protection now
    stat_bonus: Optional[Callable] = None      # (sim, key, value) -> value
    bonus_keys: tuple = ()
    active: Optional[Callable] = None          # (sim) -> True if it fired
    active_cooldown: float = 0.0
    active_trigger: str = "start"              # "start" | "hit_taken" | "after_casts"
    # Healing (2026-11-03): True if the item heals our god in a fight, so a
    # build holding it gets the fight run rather than the static integral.
    heals: bool = False
    # The coverage pass (2026-11-05, PR #104): three events the clock already
    # had but no hook exposed.
    on_tick: Optional[Callable] = None         # (sim, t) on each whole second
    on_self_heal: Optional[Callable] = None    # (sim, ability name) our ability healed us
    #: A debuff on the target that holds for the whole window, because the
    #: clock's target is in range for the whole window. `{dtype: fraction}`
    #: for a percentage reduction of that protection; `aura_flat_shred` is
    #: the same in flat points. Constant, so it reads the same in the burst.
    aura_shred: dict = field(default_factory=dict)


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


def stack_fraction(stacks, item):
    """How far `item`'s persistent stacks are toward full: 1.0 under "full",
    0.0 under "none", else the game-clock fraction `side_by_side.stack_state`
    computed for that item (`STACK_MINUTES_TO_FULL`)."""
    if stacks == "full":
        return 1.0
    if stacks == "none" or stacks is None:
        return 0.0
    return float(stacks.get(item, 1.0))


def stack_count(ctx, item, cap):
    """Whole stacks held: floor(cap x fraction). The evolutions below are
    reached only at the cap, never by rounding up."""
    return int(cap * stack_fraction(ctx.stacks, item) + 1e-9)


# ── Persistent stacks ─────────────────────────────────────────────────────

def _devourers(ctx):
    # "Each Stack grants: +.4 Strength +0.05% Lifesteal. At 75 Stacks, gain:
    # +10 Strength +3% Lifesteal +5 Penetration. Continue to stack more slowly"
    # Full = 75 stacks: 30 + 10 Strength, 3.75 + 3 Lifesteal, 5 Penetration.
    # Stacks past 75 are not counted: the text gives no rate for "more slowly".
    n = stack_count(ctx, "Devourer's Gauntlet", 75)
    if not n:
        return {}
    out = {"Strength": 0.4 * n, "Lifesteal %": 0.05 * n}
    if n == 75:
        out = {"Strength": out["Strength"] + 10, "Lifesteal %": out["Lifesteal %"] + 3,
               "Penetration": 5.0}
    return out


def _thebes(ctx):
    # "Stacks grant +15 Max Health (max 40 Stacks). At 40 Stacks, Item evolves
    # and gains: +100 Max Health +10 Physical and Magical Protection"
    n = stack_count(ctx, "Gauntlet of Thebes", 40)
    if not n:
        return {}
    if n < 40:
        return {"Max Health": 15.0 * n}
    return {"Max Health": 15 * 40 + 100, "Physical Protection": 10.0,
            "Magical Protection": 10.0}


def _mana_from_items(ctx, item, per_stack_cap=50, per_stack=10, evolved_mana=100):
    """Mana counted by a `...% of Mana from Items` clause: the printed Max
    Mana of the items, plus the item's own stack mana ("Per Mana Infusion
    Stack: +10 Mana", 50 stacks) and evolution mana when full. The stack and
    evolution mana are counted as mana FROM ITEMS because the item grants it;
    the text does not say otherwise."""
    mana = ctx.items.get("Max Mana", 0.0)
    n = stack_count(ctx, item, per_stack_cap)
    mana += n * per_stack + (evolved_mana if n == per_stack_cap else 0)
    return mana


def _thoth_grants(ctx):
    # "+5 Penetration +100 Mana" on evolving; the mana goes in via the converter.
    return {"Penetration": 5.0} if stack_count(ctx, "Book of Thoth", 50) == 50 else {}


def _thoth_converts(ctx):
    # "+Intelligence equal to 5% of Mana from Items" and, evolved, "Additional
    # +Intelligence equal to 2% of Mana from Items".
    pct = 0.07 if stack_count(ctx, "Book of Thoth", 50) == 50 else 0.05
    return {"Intelligence": pct * _mana_from_items(ctx, "Book of Thoth")}


def _transcendence_grants(ctx):
    # Evolved: "+10 Penetration +100 Mana".
    return {"Penetration": 10.0} if stack_count(ctx, "Transcendence", 50) == 50 else {}


def _transcendence_converts(ctx):
    # "+Strength equal to 3% of Mana from Items" — no evolved increase to the 3%.
    return {"Strength": 0.03 * _mana_from_items(ctx, "Transcendence")}


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


#: Chain Lightning hits on THE target per proc. The wiki text says "Hits
#: target and up to 4 nearby enemies ... Can hit the same target more than
#: once"; Jacob's in-game reading (2026-11-02) is that one target takes at most
#: 3 of them — the first hit plus 2 bounces back. The side-by-side is a
#: single-target duel, so ONLY the hits on that target count, and with no other
#: enemy in range every bounce that can return to it does: 3. A teamfight would
#: spread bounces over up to 5 enemies and land fewer on any one; that is not
#: this comparison. The lower bound (the bounces all go elsewhere) is 1.
ODYSSEUS_HITS_ON_TARGET = 3


def odysseus_hit(attack_damage):
    """One Chain Lightning hit: `15 + 60% Attack Damage`, physical."""
    return 15.0 + 0.60 * attack_damage


def _odysseus(sim, ev):
    # "Every fourth Attack Hit: Trigger Chain Lightning. Damage = 15 (+60%
    # Attack Damage) Physical Damage Hits target and up to 4 nearby enemies
    # Bounce Range: 4.8m Can hit the same target more than once".
    # "Attack Damage" is SMITE 2's name for the basic attack's damage — the
    # god's attack power plus its basic-attack scaling (100% Strength, 20%
    # Intelligence, 100% of the Attack Damage stat) — NOT the stat alone. The
    # 2026-11-02 comparison read it as the stat, which made the proc 15 + ~0
    # on almost every build. `ev.raw` is exactly that swing (its place in the
    # god's attack chain included, item multipliers such as Riptalon's not —
    # those apply to the attack, not to what the item reads).
    if ev.attack_index % 4 == 3:
        sim.proc(ODYSSEUS_HITS_ON_TARGET * odysseus_hit(ev.raw), "physical", ev)


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


def _riptalon_bonus(sim, key, v):
    # "While Below 50% Health: ... +7.5% Lifesteal". The DAMAGE branch keeps
    # the module's full-health convention for offence; the lifesteal reads the
    # fight's health bar, which is the only place a heal can land.
    return v + 7.5 if sim.max_health and sim.hp < 0.5 * sim.max_health else v


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
    # "Gain 7% Attack Speed for 5s ... can stack up to 3 times." The 40%
    # healing reduction is applied by `Sim` from `ANTI_HEAL`, like every
    # anti-heal item; the 7% attack-speed DEBUFF on the target is not (the
    # enemy's cadence is a fixed profile).
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
    # dealt over 1s. Subsequent hits on the same target deal 33% bonus Damage,
    # over 3s." Reading taken (2026-11-02; PR #77 left the clause out): a
    # Crusher hit within 3s of the previous one on the target is a SUBSEQUENT
    # hit and deals 1.33x; "over 3s" is that window. One target, so every
    # proc inside 3s of the last qualifies.
    st = sim.item_state("The Crusher", last=-math.inf)
    mult = 1.33 if ev.t - st["last"] <= 3.0 else 1.0
    st["last"] = ev.t
    sim.proc(mult * 0.35 * sim.stat("Strength"), "physical", ev)


def _soul_gem(sim, ev):
    # "Ability Hit: +1 Stack. Three Stacks: Next Ability Hit: Deals Bonus
    # Damage (40% Intelligence) ... Removes the Stacks". The damage type is not
    # stated; it is taken as the god's own.
    # "+20(+6 per Level) Heal you and allies within 3.2m": 140 at level 20,
    # to our god (no allies in the comparison); it lands in the fight's
    # health bar, so it shows in effective health, not damage.
    st = sim.item_state("Soul Gem", stacks=0)
    if st["stacks"] >= 3:
        sim.proc(0.40 * sim.stat("Intelligence"), sim.damage_type, ev)
        sim.heal(20.0 + 6.0 * sim.level)
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



# ── Takedowns (the FIGHT block in `side_by_side`: a kill when our damage
#    reaches the target's max health; an assist on a fixed cadence) ────────

def _jotunn(sim, kind):
    # "God Kill or Assist: -1s Cooldown for Non-Ultimate Abilities -5s
    # Cooldown for Ultimate Abilities". Taken off whatever is left of each
    # cooldown; a cooldown already over banks nothing.
    sim.refund(1.0, 5.0)


def _desolation(sim, kind):
    # "God Kill: -3s Non Ultimate Cooldowns -10s Ultimate Cooldowns God
    # Assist: -1.5s Non Ultimate Cooldowns -5s Ultimate Cooldowns"
    if kind == "kill":
        sim.refund(3.0, 10.0)
    else:
        sim.refund(1.5, 5.0)


def _reaper(sim, kind):
    # "Kill a God: Heal +15% of Slain God's Max Health Assist a God: Heal
    # +7.5% of Slain God's Max Health". The slain god is the reference target
    # in both cases (an assist's victim is not in the comparison; the target
    # is the comparison's only god). The Moonlight Phase clause is a map
    # phase this comparison does not contain, so it is read as off.
    sim.heal((0.15 if kind == "kill" else 0.075) * sim.target["max_health"])


def timed_stacks(state, t, duration):
    """Stacks that "last Ns" and "fall off one at a time": the timer restarts
    on every gain and on every single-stack loss. Returns the stacks held at
    `t` and updates `state` ({"stacks", "expires"}) to that instant."""
    while state["stacks"] and t >= state["expires"]:
        state["stacks"] -= 1
        state["expires"] += duration
    return state["stacks"]


DOOM_ORB_DURATION = 10.0   # "Stacks last 10s"


def _doom_takedown(sim, kind):
    # "Kill or Assist a God: +5 Stacks. Per Stack: +8 Intelligence Max 5
    # Stacks. Stacks last 10s. Stacks fall off one at a time". No minions in
    # the duel, so the minion clause never fires.
    st = sim.item_state("Doom Orb", stacks=0, expires=0.0)
    timed_stacks(st, sim.t, DOOM_ORB_DURATION)
    st["stacks"], st["expires"] = min(5, st["stacks"] + 5), sim.t + DOOM_ORB_DURATION


def _doom_bonus(sim, key, v):
    st = sim.state.get("Doom Orb")
    if not st:
        return v
    return v + 8.0 * timed_stacks(st, sim.t, DOOM_ORB_DURATION)


RAGE_PER_STACK, RAGE_MAX_STACKS, RAGE_BONUS = 4.0, 5, 10.0


def rage_crit(takedowns):
    """"God Kill or Assist: +4% Critical Strike Chance (Max 20%) After 5 God
    Kills or Assists: +10% additional Critical Strike Chance". No duration is
    stated, so the stacks are permanent: earlier fights count
    (`side_by_side.STACK_MINUTES_TO_FULL`), and takedowns in the window add."""
    n = min(takedowns, RAGE_MAX_STACKS)
    return RAGE_PER_STACK * n + (RAGE_BONUS if takedowns >= RAGE_MAX_STACKS else 0.0)


def _rage_takedown(sim, kind):
    st = sim.item_state("Rage", takedowns=_rage_start(sim))
    st["takedowns"] += 1


def _rage_start(sim):
    return int(RAGE_MAX_STACKS * stack_fraction(sim.stacks, "Rage") + 1e-9)


def _rage_bonus(sim, key, v):
    st = sim.item_state("Rage", takedowns=_rage_start(sim))
    return v + rage_crit(st["takedowns"])


# ── Hits taken (the enemy profile in `side_by_side`'s FIGHT block) ────────

def _genji(sim, hit):
    # "Hit by Magical Ability Damage: -3s Cooldowns. Cooldown: 20s". "Cooldowns"
    # with no qualifier is every ability, the ultimate included.
    if hit["kind"] != "ability" or hit["dtype"] != "magical":
        return
    st = sim.item_state("Genji's Guard", ready=0.0)
    if sim.t >= st["ready"]:
        sim.refund(3.0, 3.0)
        st["ready"] = sim.t + 20.0


def kinetic_shockwave(max_health):
    """"dealing 40 (+4% of your Health) Physical Damage" — your MAX health:
    the clock's offence is read at full health (module docstring)."""
    return 40.0 + 0.04 * max_health


def _kinetic_taken(sim, hit):
    # "Damaged by 3 Attacks from gods: Gain Kinetic. Stacks up to 2 times."
    if hit["kind"] != "attack":
        return
    st = sim.item_state("Kinetic Cuirass", hits=0, kinetic=0)
    st["hits"] += 1
    if st["hits"] == 3:
        st["hits"], st["kinetic"] = 0, min(2, st["kinetic"] + 1)


def _kinetic_attack(sim, ev):
    # "Kinetic makes your next Attack unleash a shockwave, even if it misses"
    # — one Kinetic per attack.
    st = sim.item_state("Kinetic Cuirass", hits=0, kinetic=0)
    if st["kinetic"]:
        st["kinetic"] -= 1
        sim.proc(kinetic_shockwave(sim.max_health), "physical", ev)


def breastplate_threshold(level):
    """"On 500 (+25 per Level) Health lost" — 1000 at level 20."""
    return 500.0 + 25.0 * level


def _breastplate(sim, hit):
    # "On 500 (+25 per Level) Health lost: -1s Ability Cooldowns." Health
    # lost is cumulative real health (shields absorb first; a heal does not
    # give it back). Every ability, the ultimate included.
    st = sim.item_state("Breastplate of Valor", paid=0)
    due = int(sim.health_lost // breastplate_threshold(sim.level))
    while st["paid"] < due:
        st["paid"] += 1
        sim.refund(1.0, 1.0)


DRACONIC_DURATION, DRACONIC_MAX, DRACONIC_PER = 1.5, 7, 4.0


def _draconic_taken(sim, hit):
    # "Damaged by a God: Gain 4 Protections against that God's damage type
    # Stacks last 1.5s (max 7) Stacks decay 1 at a time". One pool per damage
    # type; gained AFTER the hit that grants it.
    st = sim.item_state("Draconic Scale:" + hit["dtype"], stacks=0, expires=0.0)
    timed_stacks(st, sim.t, DRACONIC_DURATION)
    st["stacks"], st["expires"] = min(DRACONIC_MAX, st["stacks"] + 1), sim.t + DRACONIC_DURATION


def _draconic_prot(sim, dtype):
    st = sim.state.get("Draconic Scale:" + dtype)
    return DRACONIC_PER * timed_stacks(st, sim.t, DRACONIC_DURATION) if st else 0.0


BERSERK_DURATION = 8.0   # "Become Berserk for 8s"


def _berserk_taken(sim, hit):
    # "When falling below 60% Health: Become Berserk for 8s. While Berserk:
    # +15 Physical Protection +15 Magical Protection +25% Attack Speed". Fires
    # on each crossing from above 60% to below (a heal back over re-arms it);
    # the text states no cooldown.
    st = sim.item_state("Berserker's Shield", armed=True, until=-1.0)
    below = sim.hp < 0.60 * sim.max_health
    if below and st["armed"]:
        st["armed"], st["until"] = False, sim.t + BERSERK_DURATION
    elif not below:
        st["armed"] = True


def _berserk_on(sim):
    st = sim.state.get("Berserker's Shield")
    return bool(st) and sim.t < st["until"]


def _berserk_prot(sim, dtype):
    return 15.0 if _berserk_on(sim) else 0.0


def _berserk_bonus(sim, key, v):
    return v + 25.0 if _berserk_on(sim) else v


# ── "On Use" actives. Each is pressed the first moment its condition holds
#    and again the moment its cooldown ends (`side_by_side`'s FIGHT block);
#    the condition is written beside each one. ────────────────────────────

def _frenzy_active(sim):
    # "+10 (+4 per Level) Attack Damage +20% (+1% per Level) Attack Speed
    # Buff lasts 6 Attacks." Pressed at the fight's start.
    sim.item_state("Dagger of Frenzy", left=0)["left"] = 6
    return True


def _frenzy_bonus(sim, key, v):
    st = sim.state.get("Dagger of Frenzy")
    if not st or not st["left"]:
        return v
    return v + (10.0 + 4.0 * sim.level if key == "Attack Damage" else 20.0 + 1.0 * sim.level)


def _frenzy_attack(sim, ev):
    st = sim.state.get("Dagger of Frenzy")
    if st and st["left"]:
        sim.after(lambda: st.update(left=st["left"] - 1))


def _frenzy_takedown(sim, kind):
    # "Killing a God refreshes Cooldown." A kill only, not an assist.
    if kind == "kill":
        sim.ready_active("Dagger of Frenzy")


def _timed_buff(name, duration):
    def press(sim):
        sim.item_state(name, until=-1.0)["until"] = sim.t + duration
        return True
    return press


def _buff_on(sim, name):
    st = sim.state.get(name)
    return bool(st) and sim.t < st["until"]


def _pct_of(name, pct):
    # "+25% Strength" / "+25% Intelligence": a quarter of the god's total,
    # applied after every flat bonus.
    def bonus(sim, key, v):
        return v * (1.0 + pct) if _buff_on(sim, name) else v
    return bonus


def _death_metal_active(sim):
    # Pressed only by a PHYSICAL god: "Lose all Intelligence. Gain 66% of it
    # as Strength" is a loss for a god whose damage scales on Intelligence.
    if sim.damage_type != "physical":
        return False
    sim.item_state("Death Metal", until=-1.0)["until"] = sim.t + 6.0
    return True


def _lernaean(sim):
    # "Fire 3 arrows that pierce enemies in a 10.5m line. Deals 40% of your
    # Attack Damage as Physical Damage ... Can Critically Strike". Attack
    # Damage is the swing (`_odysseus`); the target is in the line, so all
    # three arrows hit it — the literal upper reading, written down. A crit
    # is its expected value, as for basic attacks.
    swing = sim.swing_raw()
    sim.active_damage(3 * 0.40 * swing * sim.crit_ev(), "physical")
    return True


def _splitter(sim):
    # "+40 (+5 per Level) True Damage". No enemy shields in the comparison, so
    # the shield clauses do nothing. The target is inside 11.2m (the clock's
    # in-range assumption).
    sim.active_damage(40.0 + 5.0 * sim.level, "true")
    return True


def _erebus(sim):
    # "Spawn a Watchful Eye ... Enemy enters range: Fires a seeking projectile:
    # Magical Damage equal to 15% of Enemy Max Health". Read as one projectile
    # per press: the eye is placed where the fight is and the target enters
    # its range once. Moonlight Phase is not in the comparison.
    sim.active_damage(0.15 * sim.target["max_health"], "magical")
    return True


def _pendulum(sim):
    # "-4s Ability Cooldowns." Condition: an ability is on cooldown — so it is
    # pressed straight after the opening casts.
    if not sim.any_on_cooldown():
        return False
    sim.refund(4.0, 4.0)
    return True


def _bbb_active(sim):
    # "+ Health Shield for 6s. Shield = 7.5% Max Health & 75% Intelligence
    # from Items While Shielded: +10% Lifesteal and 10% Penetration". Pressed
    # at the fight's start. The penetration holds while the shield does.
    shield = 0.075 * sim.max_health + 0.75 * sim.item_totals.get("Intelligence", 0.0)
    sim.add_shield("Blood-Bound Book", shield, sim.t + 6.0)
    return True


def _bbb_bonus(sim, key, v):
    return v + 10.0 if sim.shield_up("Blood-Bound Book") else v


def _bbb_takedown(sim, kind):
    # "Kill a God: -25% Cooldown." Read as a quarter of the item's 80s off
    # what remains.
    if kind == "kill":
        sim.shorten_active("Blood-Bound Book", 0.25 * 80.0)


def _amanita(sim):
    # "Create a Healing Mushroom (6.4m radius) for 4.5s. +3% Health Heal every
    # 1.5s +1 Stack of Damage Reduction per Heal 10% Attack and Ability Damage
    # Reduction per Stack ... All Stacks removed after triggering". Pressed
    # at the first hit taken (a heal at full health is wasted); heals at
    # +1.5, +3.0, +4.5s; the next hit after a heal spends every stack.
    st = sim.item_state("Amanita Charm", heals=[], stacks=0)
    st["heals"] = [sim.t + 1.5, sim.t + 3.0, sim.t + 4.5]
    return True


def _amanita_tick(sim):
    st = sim.state.get("Amanita Charm")
    if not st:
        return
    while st["heals"] and st["heals"][0] <= sim.t:
        st["heals"].pop(0)
        sim.heal(0.03 * sim.max_health)
        st["stacks"] += 1


def _amanita_reduce(sim, hit):
    _amanita_tick(sim)
    st = sim.state.get("Amanita Charm")
    if not st or not st["stacks"]:
        return 1.0
    # Ultimates are 5% per stack; the enemy profile has no ultimate.
    mult = max(0.0, 1.0 - 0.10 * st["stacks"])
    st["stacks"] = 0
    return mult


def _hide(sim):
    # "Reflect: 40% of pre-mitigated Attack Damage 20% of pre-mitigated
    # Ability Damage Damage is Reflected as Physical Damage Buff lasts 4s."
    # Pressed at the first hit taken. The attacker is the target (a duel).
    sim.item_state("Hide of the Nemean Lion", until=-1.0)["until"] = sim.t + 4.0
    return True


def _hide_taken(sim, hit):
    if _buff_on(sim, "Hide of the Nemean Lion"):
        share = 0.40 if hit["kind"] == "attack" else 0.20
        sim.active_damage(share * hit["raw"], "physical", item="Hide of the Nemean Lion")


def shell_field_cap(level):
    """"mitigates 25% Damage, up to 300 (+40 Per Level)" — 1100 at 20."""
    return 300.0 + 40.0 * level


def _shell_active(sim):
    # "Create a field of rebuke for allies that mitigates 25% Damage, up to
    # 300 (+40 Per Level). Upon Entering Field: +100 (+10 per Level) Shield for
    # 3s." Pressed at the first hit taken; we stand in it until it is spent.
    sim.item_state("Shell of Rebuke", left=shell_field_cap(sim.level))
    sim.state["Shell of Rebuke"]["left"] = shell_field_cap(sim.level)
    sim.add_shield("Shell of Rebuke", 100.0 + 10.0 * sim.level, sim.t + 3.0)
    return True


def _shell_reduce(sim, hit):
    st = sim.state.get("Shell of Rebuke")
    if not st or st["left"] <= 0:
        return 1.0
    mitigated = hit["raw"] * sim.mitigation_now(hit["dtype"])
    cut = min(0.25 * mitigated, st["left"])
    st["left"] -= cut
    return 1.0 - cut / mitigated if mitigated else 1.0



# ── Items the fight layer made simulable (2026-11-02) ─────────────────────

def _bancroft_bonus(sim, key, v):
    # "Gain bonus Intelligence and Lifesteal scaled from missing Health. Caps
    # at +60 Intelligence and +10% Lifesteal at 40% Health". Linear in missing
    # health from full (0) to 40% health (cap) — the literal "scaled from".
    # Our health is the fight's (an enemy hits back in the sustained window);
    # a burst is at full health, +0. The lifesteal heals in the fight run.
    missing = 1.0 - sim.hp / sim.max_health if sim.max_health else 0.0
    share = min(1.0, missing / 0.60)
    return v + (10.0 if key == "Lifesteal %" else 60.0) * share


def _brawler_prot(sim, dtype):
    # "+2% Protections every 1.5s. Stacks up to 5 times" in combat; combat
    # starts at t=0 (the stat half is in `Sim._stat_raw`). 2% of our god's own
    # protection of that type.
    return sim.own_prot[dtype] * 0.02 * min(5, int(sim.t // 1.5))


CHRONOS_INTERVAL, CHRONOS_FIRST = 10.0, 5.0


def _chronos(sim):
    # "Every 10s: -1s Ability Cooldowns." The 10s timer runs from the game,
    # not the fight, so its phase is unknown: the first tick is at 5s, the
    # mean of a uniform phase (the same reasoning as the FIGHT block's
    # ASSIST_FIRST), then every 10s.
    if sim.t < CHRONOS_FIRST:
        sim.active_ready["Chronos' Pendant"] = CHRONOS_FIRST
        return False
    sim.refund(1.0, 1.0)
    return True


def demon_blade_uptime(crit_chance, attacks_in_window):
    """P(at least one crit among the attacks of the last 3s)."""
    return 1.0 - (1.0 - crit_chance) ** attacks_in_window


def _demon_attack(sim, ev):
    st = sim.item_state("Demon Blade", times=[])
    sim.after(lambda: st["times"].append(ev.t))


def _demon_bonus(sim, key, v):
    # "Critically Strike: +30% Attack Speed for 3s." Crit is an expected
    # value here, so the buff is too: +30% x P(a crit among the attacks made
    # in the last 3s), the probability read off the build's crit chance.
    st = sim.state.get("Demon Blade")
    if not st:
        return v
    n = sum(1 for t in st["times"] if sim.t - 3.0 < t <= sim.t)
    p = min(sim.base_stats.get("Critical Chance %", 0.0), 100.0) / 100.0
    return v + 30.0 * demon_blade_uptime(p, n)


def _sanguine_active(sim):
    # "On Use: Now damages every 0.33s for 4s. Cooldown: 75s". Pressed at the
    # fight's start; the clock ticks the aura every 0.33s while it lasts.
    sim.item_state("Sanguine Lash", until=-1.0)["until"] = sim.t + 4.0
    return True


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
    "Brawler’s Beat Stick": Passive(SIMULATED, "adaptive +35 Str / +50 Int; +2% Str/Int/protections per 1.5s in combat (5)",
                                    ("stacks build from 0 at the start of the window",
                                     "god damage applies 40% healing reduction for 5s",
                                     "static effective health reads 0 stacks; the fight run builds them"),
                                    grants=_brawler_grants, prot_bonus=_brawler_prot),
    "Nimble Ring": Passive(SIMULATED, "per 10 Intelligence: +1 Attack Damage, +1% Attack Speed",
                           ("whole tens of Intelligence",), converts=_nimble),
    "Odysseus' Bow": Passive(SIMULATED, "every 4th attack: chain lightning, 3 hits on the target of 15 + 60% of the basic attack's damage, physical",
                             ("Attack Damage = the basic attack's damage (attack power + Str/Int/Attack Damage scaling), not the stat",
                              "single target: only hits on the target count — the first plus 2 bounces (3)"),
                             on_attack=_odysseus),
    "Polynomicon": Passive(SIMULATED, "after an ability, next attack +80% Int magical (2s cooldown)",
                           on_attack=_polynomicon_attack, on_ability=_polynomicon_ability),
    "Bancroft's Talon": Passive(SIMULATED, "up to +60 Int / +10% LS, linear in missing health to 40% health",
                                ("our health is the fight's; a burst is at full health (+0)",
                                 "the lifesteal heals in the fight's health bar"),
                                stat_bonus=_bancroft_bonus, bonus_keys=("Intelligence", "Lifesteal %"),
                                heals=True),
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
    "Shell of Rebuke": Passive(SIMULATED, "+7.5% of all item stats; active: 25% damage cut up to 1100 and a 300 shield for 3s",
                               ("applied to printed item stats only",
                                "pressed at the first hit taken; we stand in the field until it is spent"),
                               converts=_shell, active=_shell_active, active_cooldown=120.0,
                               active_trigger="hit_taken", reduce_hit=_shell_reduce),
    "Silverbranch Bow": Passive(SIMULATED, "every 3rd attack: one arrow per whole attack/s, 25% of the swing each",
                                on_attack=_silverbranch),
    "Riptalon": Passive(SIMULATED, "attacks +10% damage above 50% health; +7.5% LS below 50%",
                        ("damage: full-health branch (below 50% it is +25%)",
                         "lifesteal: read off the fight's health bar"),
                        on_attack=_riptalon, stat_bonus=_riptalon_bonus,
                        bonus_keys=("Lifesteal %",), heals=True),
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
    "Toxic Blade": Passive(PARTIAL, "+7% attack speed per hit (3 stacks); attacks apply 40% healing reduction for 5s",
                           ("the -7% attack speed debuff on the target is not simulated",),
                           on_attack=_toxic),
    "Hydra's Lament": Passive(SIMULATED, "after an ability, next attack +20% ranged / +30% melee",
                              on_attack=_hydra_attack, on_ability=_hydra_ability),
    "The Crusher": Passive(SIMULATED, "ability hit: +35% Strength physical; x1.33 within 3s of the last",
                           ("'subsequent hits ... over 3s' read as a proc within 3s of the previous one",),
                           on_ability=_crusher),
    "Soul Gem": Passive(SIMULATED, "every 4th ability hit: +40% Int and a 140 heal (level 20)",
                        ("the heal lands in the fight's health bar (effective health)",),
                        on_ability=_soul_gem, heals=True),
    "Divine Ruin": Passive(SIMULATED, "chain lightning 40 + 20% Int every 15s; god damage applies 40% healing reduction for 5s",
                           ("one target: the chain's other four enemies are not in the comparison",),
                           on_ability=_divine_ruin),
    "Spear of the Magus": Passive(SIMULATED, "ability hit marks the target: +5% damage taken for 8s",
                                  on_ability=_spear_magus),
    "Avenging Blade": Passive(SIMULATED, "attacks shred 3.5% protections per stack (3)", on_attack=_avenging),
    "Sanguine Lash": Passive(SIMULATED, "aura: 0.5% (+0.66% per 10% LS) target health per second; active: every 0.33s for 4s (75s)",
                             ("target inside 4m for the whole window", "active pressed at the fight's start"),
                             active=_sanguine_active, active_cooldown=75.0),
    "The World Stone": Passive(SIMULATED, "-25% ultimate cooldown", cooldown=_world_stone),
    "Berserker's Shield": Passive(SIMULATED, "below 60% health: berserk 8s, +15/+15 protections and +25% attack speed",
                                  ("fires on each fall below 60% (no cooldown stated)",
                                   "static effective health integrates the bottom 60% of the bar; the fight clock applies the 8s"),
                                  ehp_segments=_berserker_ehp, on_hit_taken=_berserk_taken,
                                  prot_bonus=_berserk_prot, stat_bonus=_berserk_bonus,
                                  bonus_keys=("Attack Speed %",)),
    "Shifter's Shield": Passive(SIMULATED, "over 75% health +30 Str / +40 Int; under 75% +20/+20 protections",
                                grants=_shifter_grants, ehp_segments=_shifter_ehp),
    "Freya's Tears": Passive(SIMULATED, "per 25% health lost: +15/+15 protections for 5s (2 stacks)",
                             ("the health is lost inside 5s",), ehp_segments=_freya_ehp),
    "Sun Beam Bow": Passive(PARTIAL, "adaptive +20 Str / +40 Int; the toggle active is not simulated",
                            grants=_adaptive(20.0, 40.0)),

    # Takedowns: a kill when our damage reaches the target's max health, an
    # assist on `side_by_side.ASSIST_INTERVAL` (its FIGHT block).
    "Jotunn's Revenge": Passive(SIMULATED, "kill/assist: -1s abilities, -5s ultimate",
                                ("kills and assists from the FIGHT block",),
                                on_takedown=_jotunn),
    "Spear of Desolation": Passive(SIMULATED, "kill: -3s / -10s ult; assist: -1.5s / -5s ult",
                                   ("kills and assists from the FIGHT block",),
                                   on_takedown=_desolation),
    "Rage": Passive(SIMULATED, "+4% crit per god kill/assist (5), +10% more at 5",
                    ("stacks are permanent: earlier fights by the game clock, plus takedowns in the window",),
                    on_takedown=_rage_takedown, stat_bonus=_rage_bonus,
                    bonus_keys=("Critical Chance %",), stacking=True),
    "Doom Orb": Passive(SIMULATED, "kill/assist: +5 stacks of +8 Int (10s, fall off one at a time)",
                        ("no minions in the duel",), on_takedown=_doom_takedown,
                        stat_bonus=_doom_bonus, bonus_keys=("Intelligence",)),
    "The Reaper": Passive(SIMULATED, "heal 15% (kill) / 7.5% (assist) of the slain god's max health",
                          ("the slain god is the reference target", "Moonlight Phase off"),
                          on_takedown=_reaper),
    # Hits taken: the enemy profile in the FIGHT block.
    "Genji's Guard": Passive(SIMULATED, "hit by magical ability damage: -3s cooldowns (20s)",
                             ("every ability, the ultimate included",), on_hit_taken=_genji),
    "Breastplate of Valor": Passive(SIMULATED, "per 1000 health lost (level 20): -1s ability cooldowns",
                                    ("cumulative real health lost; every ability",),
                                    on_hit_taken=_breastplate),
    "Kinetic Cuirass": Passive(SIMULATED, "3 attacks taken: Kinetic (2); next attack +40 + 4% max health physical",
                               ("your Health read as max health",),
                               on_hit_taken=_kinetic_taken, on_attack=_kinetic_attack),
    "Draconic Scale": Passive(SIMULATED, "per hit taken: +4 protection vs that type (7, 1.5s, decay one at a time)",
                              on_hit_taken=_draconic_taken, prot_bonus=_draconic_prot),
    # "On Use" actives, pressed on cooldown once their condition holds.
    "Dagger of Frenzy": Passive(SIMULATED, "active: +90 Attack Damage, +40% attack speed for 6 attacks (15s); a kill refreshes it",
                                ("pressed at the fight's start",),
                                active=_frenzy_active, active_cooldown=15.0, on_attack=_frenzy_attack,
                                stat_bonus=_frenzy_bonus, bonus_keys=("Attack Damage", "Attack Speed %"),
                                on_takedown=_frenzy_takedown),
    "Avatar's Parashu": Passive(SIMULATED, "active: +25% Strength for 10s (120s)",
                                ("pressed at the fight's start", "displacement immunity: no CC in the comparison"),
                                active=_timed_buff("Avatar's Parashu", 10.0), active_cooldown=120.0,
                                stat_bonus=_pct_of("Avatar's Parashu", 0.25), bonus_keys=("Strength",)),
    "Dreamer's Idol": Passive(SIMULATED, "active: +25% Intelligence for 10s (120s)",
                              ("pressed at the fight's start", "displacement immunity: no CC in the comparison"),
                              active=_timed_buff("Dreamer's Idol", 10.0), active_cooldown=120.0,
                              stat_bonus=_pct_of("Dreamer's Idol", 0.25), bonus_keys=("Intelligence",)),
    "Death Metal": Passive(SIMULATED, "active: all Int becomes 66% Strength, +25% crit, 6s (45s)",
                           ("pressed at the fight's start, by a physical god only",),
                           active=_death_metal_active, active_cooldown=45.0),
    "Lernaean Bow": Passive(SIMULATED, "active: 3 arrows of 40% of the swing, physical, can crit (30s)",
                            ("pressed at the fight's start", "all three arrows hit the target (literal upper reading)"),
                            active=_lernaean, active_cooldown=30.0),
    "Shield Splitter": Passive(SIMULATED, "active: 140 true damage at level 20 (15s)",
                               ("pressed at the fight's start", "no enemy shields: the shield clauses do nothing"),
                               active=_splitter, active_cooldown=15.0),
    "Eye of Erebus": Passive(SIMULATED, "adaptive +35 Str / +50 Int; active: 15% of the target's max health, magical (40s)",
                             ("one projectile per press: the target enters the eye's range once",
                              "the slow and Moonlight Phase are not in the comparison"),
                             grants=_adaptive(35.0, 50.0), active=_erebus, active_cooldown=40.0),
    "Pendulum Blade": Passive(SIMULATED, "active: -4s ability cooldowns (40s)",
                              ("pressed as soon as an ability is on cooldown",),
                              active=_pendulum, active_cooldown=40.0, active_trigger="after_casts"),
    "Blood-Bound Book": Passive(SIMULATED, "active: shield 7.5% max health + 75% item Int for 6s; +10% penetration while it holds (80s)",
                                ("pressed at the fight's start", "+10% lifesteal while it holds", "a kill takes 20s (25% of 80s) off"),
                                active=_bbb_active, active_cooldown=80.0, stat_bonus=_bbb_bonus,
                                bonus_keys=("Penetration %", "Lifesteal %"), on_takedown=_bbb_takedown,
                                heals=True),
    "Amanita Charm": Passive(SIMULATED, "active: three heals of 3% max health over 4.5s, each a 10% cut on the next hit (60s)",
                             ("pressed at the first hit taken",),
                             active=_amanita, active_cooldown=60.0, active_trigger="hit_taken",
                             reduce_hit=_amanita_reduce),
    "Hide of the Nemean Lion": Passive(SIMULATED, "active: reflect 40% of attack / 20% of ability damage taken for 4s, physical (60s)",
                                       ("pressed at the first hit taken", "the attacker is the target"),
                                       active=_hide, active_cooldown=60.0, active_trigger="hit_taken",
                                       on_hit_taken=_hide_taken),
    "Chronos' Pendant": Passive(SIMULATED, "every 10s: -1s ability cooldowns",
                                ("timer phase unknown: first tick at 5s, then every 10s",),
                                active=_chronos, active_cooldown=CHRONOS_INTERVAL),
    "Stampede": Passive(NOT_SIMULATED, "active: slow immunity and movement speed",
                        ("the comparison contains no movement",)),
    "Doublet of Binding": Passive(NOT_SIMULATED, "active: link redirects an ally's damage to you",
                                  ("the comparison contains no ally",)),

    # Refused, each for the reason the comparison cannot contain.
    "Erosion": Passive(NOT_SIMULATED, "reduces enemy shields", ("no enemy shield in the comparison",)),
    "Runeforged Hammer": Passive(NOT_SIMULATED, "rune on hard CC", ("no crowd control",)),
    "Tekko-Kagi": Passive(NOT_SIMULATED, "pathfinding on ability use", ("no movement",)),
    "Hastened Fatalis": Passive(NOT_SIMULATED, "movement penalty reduction", ("no movement",)),
    "Musashi's Dual Swords": Passive(NOT_SIMULATED, "movement speed on crit", ("no movement",)),
    "Hussar's Wings": Passive(NOT_SIMULATED, "slow immunity", ("no movement",)),
    "Demon Blade": Passive(SIMULATED, "+30% attack speed for 3s after a crit, as an expected value",
                           ("buff = 30% x P(a crit among the attacks of the last 3s)",),
                           on_attack=_demon_attack, stat_bonus=_demon_bonus,
                           bonus_keys=("Attack Speed %",)),
    "Eye of Providence": Passive(NOT_SIMULATED, "ward economy", ("no wards",)),
}

# ── Healing (2026-11-03) ──────────────────────────────────────────────────
# `Sim` now carries a healing channel on BOTH sides: our god heals (lifesteal
# on every damage instance, plus the items below) at the enemy's expected
# healing reduction, and the target heals off its own lifesteal at ours.
# `combat.healing_received` is the arithmetic; the item texts are below.

#: Every healing-reduction item in the pool: `(fraction, seconds, trigger)`,
#: off its text. "attack" = "Hit a God with an Attack"; "any" = "On God
#: Damage Dealt" / "On God Damaged". `combat.healing_received` takes the
#: strongest live one ("does not stack with other similar effects").
ANTI_HEAL = {
    "Toxic Blade": (0.40, 5.0, "attack"),
    "Divine Ruin": (0.40, 5.0, "any"),
    "Brawler’s Beat Stick": (0.40, 5.0, "any"),
    "Stygian Anchor": (0.40, 5.0, "any"),
}


def _phoenix(sim, ev):
    # "Ability Hit a God: +1.5% Health Heal +2% Mana Restore Triggers once per
    # Ability, per god." Health = our MAX health (the usual reading of
    # "% Health Heal"); one target, so once per cast. Mana is not modelled.
    sim.heal(0.015 * sim.max_health)


GLUTTONOUS_SHARE, GLUTTONOUS_FULL_SHARE = 0.50, 0.65


def gluttonous_cap(max_health, intelligence):
    """"Stored damage is capped to 10% of your Max Health + 50% Intelligence"."""
    return 0.10 * max_health + 0.50 * intelligence


def _gluttonous_store(sim, nominal):
    # "Store 50% of your Lifesteal healing as bonus Magical Damage on your
    # next Attack. If at full Health: Store 65% instead". `nominal` is the
    # lifesteal heal BEFORE overheal and healing reduction — at full health
    # the heal lands on nothing, and the text still stores 65% of it.
    st = sim.item_state("Gluttonous Grimoire", stored=0.0)
    share = GLUTTONOUS_FULL_SHARE if sim.hp >= sim.max_health - 1e-9 else GLUTTONOUS_SHARE
    cap = gluttonous_cap(sim.max_health, sim.stat("Intelligence"))
    st["stored"] = min(cap, st["stored"] + share * nominal)


def _gluttonous_attack(sim, ev):
    st = sim.item_state("Gluttonous Grimoire", stored=0.0)
    if st["stored"] > 0:
        sim.proc(st["stored"], "magical", ev)
        st["stored"] = 0.0


def _bloodforge_active(sim):
    # "+ Health Shield for 6s. Shield = 10% Max Health & 150% Strength from
    # Items While Shielded: +10% Lifesteal". Pressed at the fight's start,
    # like Blood-Bound Book, its twin.
    shield = 0.10 * sim.max_health + 1.50 * sim.item_totals.get("Strength", 0.0)
    sim.add_shield("Bloodforge", shield, sim.t + 6.0)
    return True


def _bloodforge_bonus(sim, key, v):
    return v + 10.0 if sim.shield_up("Bloodforge") else v


def _bloodforge_takedown(sim, kind):
    # "Kill a God: -25% Cooldown." A quarter of the 80s off what remains.
    if kind == "kill":
        sim.shorten_active("Bloodforge", 0.25 * 80.0)


REGISTRY.update({
    "Shield of the Phoenix": Passive(SIMULATED, "ability hit: heal 1.5% of max health",
                                     ("once per cast: one target", "the mana restore is not modelled"),
                                     on_ability=_phoenix, heals=True),
    "Gluttonous Grimoire": Passive(SIMULATED, "50% of lifesteal healing (65% at full health) as magical damage on the next attack, cap 10% max health + 50% Int",
                                   ("stores the nominal heal, before overheal and healing reduction",),
                                   on_attack=_gluttonous_attack, heals=True),
    "Bloodforge": Passive(SIMULATED, "active: shield 10% max health + 150% item Str for 6s; +10% lifesteal while it holds (80s)",
                          ("pressed at the fight's start", "a kill takes 20s (25% of 80s) off"),
                          active=_bloodforge_active, active_cooldown=80.0,
                          stat_bonus=_bloodforge_bonus, bonus_keys=("Lifesteal %",),
                          on_takedown=_bloodforge_takedown, heals=True),
    "Stygian Anchor": Passive(PARTIAL, "god damage applies 40% healing reduction for 5s",
                              ("the -3% attack speed per Sludge stack on the target is not simulated",
                               "its '5% of their healing echoed to you' is simulated"),
                              heals=True),
})
for _n in ("The Reaper", "Amanita Charm"):
    REGISTRY[_n].heals = True


#: Actives: "On Use" items. Until 2026-11-02 every one was refused by this
#: rule ("when it is pressed is a player decision"). Each active in a compared
#: build now has an entry above, pressed on cooldown once its condition holds;
#: an active outside every compared build falls through to this reason.
ACTIVE_REASON = "active item: no simulator written yet (every active in a compared build has one)"


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
        return Passive(NOT_SIMULATED, _clip(text), (ACTIVE_REASON,))
    return Passive(NOT_SIMULATED, _clip(text), ("no simulator written yet",))


# ── THE STATED ZERO (2026-11-11) ──────────────────────────────────────────
#
# A refused passive counts as MISSING gold in `side_by_side`'s coverage test,
# and one item is ~1/6 of a build, so a single refusal on one side withholds
# the verdict. On 2026-11-11 (main 1a9ca2d5, fingerprint 89eb181b72f1) that
# withheld 31 of 95 Conquest gods, 24 of them on a movement passive: Tekko-Kagi
# on Ichor's side (10), Stampede (9) and Hussar's Wings (5) on the community's.
#
# The comparison is a duel in range for the whole window. Its own docstring
# lists what is NOT in it: crowd control, peel, mobility, allies, waves,
# objectives. A passive whose WHOLE effect lies in one of those is not
# "unmeasured" inside this comparison. It is exactly zero, for both builds,
# and saying so is more accurate than withholding: the duel would read the
# same number however well the passive were modelled. STATE.md section 5 left
# this as a rule to decide ("a stated zero, and counting it as covered, or
# leaving those gods withheld"); this is the stated zero.
#
# THE TEST AN ITEM MUST PASS, read off its full text, not off its recorded
# reason: if every clause were computed, would damage dealt to the one enemy
# god or damage survived from it change, with no crowd control landing on
# either side, no movement, no ally and no ward? If no, it is listed here with
# the dimension(s) its effect lives in. If yes, it stays withheld, whatever
# its reason says. Reasons alone are not enough, and these are the cases that
# showed it, each refused for an absent dimension and each LEFT OUT:
#
#   Ragnarok's Wake    "Enemies near where you land take 600 Magical Damage"
#   Radiant Bulwark    "and yourself 20% Damage Mitigation"
#   Chandra's Grace, Heartwood Charm, Rod of Asclepius, Soul Locket
#                      "+10/15% Increased Healing and Shielding" acts on our
#                      own heals, which the HEALING block carries and nothing
#                      here reads; Soul Locket also grants damage reduction
#   Damaru             "Adaptive Stat: +35 Strength or +50 Intelligence" sits
#                      in the passive text and this entry grants nothing
#   Circe's Hexstone   +60 protections with no stated duration
#   Mantle Of Discord, Spectral Armor, Alchemist Coat, Wyrmskin Hide
#                      Dampening or Plating on our god mitigates damage; that
#                      it reads 0 here is the instrument's blind spot (4.19)
#   Ring of Dispel, Pharaoh's Curse, Midgardian Mail
#                      a debuff on the enemy's output
#   Erosion, the Echo items, the Acorns, Typhon's Heart, War Banner,
#   Sharpshooter's Arrow, Xibalban Effigy, Infused Axe, Oracle Staff
#                      the effect is damage, health or a resource in the duel
#
# What the listed items share: a trigger or a payload the duel cannot contain.
# "When Hard Crowd Controlled" never fires because the enemy here lands no
# crowd control; "Hard Crowd Control a God" never fires because ours is not in
# the rotation; an ally-gated item has no ally; pathfinding, slow immunity and
# movement speed move nothing in a fight that is in range throughout.
#
# NOT A VALUE. A stated zero says the passive is worth nothing IN THIS
# COMPARISON. It is not a price, `efficiency` does not read it, and the item
# stays NOT_SIMULATED: the page still names it with its reason beside the
# build. `side_by_side` prints which items a verdict counted this way.
OUT_OF_SCOPE = {
    # movement: pathfinding, movement speed, slows, slow immunity, stealth
    "Tekko-Kagi": ("movement",),
    "Gem of Focus": ("movement",),
    "Gem of Isolation": ("movement",),
    "Hastened Fatalis": ("movement",),
    "Hussar's Wings": ("movement",),
    "Kopesh": ("movement",),
    "Musashi's Dual Swords": ("movement",),
    "Stampede": ("movement",),
    "Helm of Darkness": ("movement",),
    # crowd control: given or taken
    "Ancile": ("crowd control",),
    "Caestus": ("crowd control",),
    "Jade Scepter": ("crowd control",),
    "Magi's Cloak": ("crowd control",),
    "Resolute Mantle": ("crowd control",),
    "Runeforged Hammer": ("crowd control",),
    "Scepter of Dominion": ("crowd control",),
    "Shroud of Vengeance": ("crowd control",),
    "Spirit Robe": ("crowd control",),
    "Stone of Binding": ("crowd control",),
    # an ally
    "Doublet of Binding": ("ally",),
    "Eros' Bow": ("ally",),
    "Lotus Sickle": ("ally",),
    "Umbral Link": ("ally",),
    "Heroism": ("ally", "crowd control"),
    # wards
    "Eye of Providence": ("wards",),
}


def stated_zero(item):
    """The dimensions outside the comparison that this item's whole passive
    lives in, or `()`. Only ever non-empty for a NOT_SIMULATED item."""
    if lookup(item).status != NOT_SIMULATED:
        return ()
    return OUT_OF_SCOPE.get(item.get("name"), ())


def _clip(text, limit=110):
    """The item's own text, cut at a word boundary with an ellipsis."""
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(" .,:;") + "…"


# ── THE COVERAGE PASS (2026-11-05, PR #104's precondition) ─────────────────────────────────
# Everything above was written because `side_by_side`'s 90 comparisons needed
# it. That left 84 of `efficiency_pool`'s 193 scored items carrying a passive
# and absent from this table, reading `NOT_SIMULATED` with "no simulator
# written yet" — a GAP, not a decision. PR #104 measured why that blocks
# pricing passives inside `efficiency`: an absent item is zeroed by absence,
# which LOWERS its predicted cost and makes it look MORE premium, so pricing
# from a 67-of-193 table replaces §4.31's asymmetry with a bigger one.
#
# All 84 are decided below: 33 SIMULATED, 8 PARTIAL, 43 NOT_SIMULATED. The
# split is not a target — it is where the rule at the top of this file lands,
# item by item. Three refusal reasons are new and each is a MEASURED property
# of this clock rather than a shrug:
#
#   * "the enemy's attack speed is not a quantity here" — `attacker_profile`
#     derives the enemy's raw DPS from the reference squishy's effective
#     health over KILL_TIME, and `_enemy_schedule` then sets each hit to
#     `raw_dps x share x step`. Halve `step` and each hit halves. So a debuff
#     on the enemy's ATTACK SPEED, or on its Strength, provably changes no
#     damage in this comparison: the cadence is a schedule, not a source.
#     Midgardian Mail and Pharaoh's Curse are refused on that proof.
#   * "the enemy deals no critical strikes" — `crit_chance` is OUR god's
#     only; nothing on the attacker profile crits. Spectral Armor's whole
#     passive reads that.
#   * "Echo is an expected multiplier here, not an instance" —
#     `combat.echo_multiplier` carries Echo as `1 + chance x share`, linear
#     and deliberately so ("linear is what a build comparison wants"). Five
#     items trigger on "Each time you Echo", which has no countable instance
#     in that design. It is also a two-god mechanic (Ix Chel, Nut) and in
#     neither god's scraped rotation.
#
# And one refusal is a refusal to count HALF of something: Xibalban Effigy
# halves incoming damage for 4s and then deals the mitigated damage back to
# our god. `reduce_hit` would simulate the halving in two lines; the clock
# has no channel for our god damaging itself, so that would book the upside
# alone. An item refused whole is honest; an item credited with its good half
# is the PR #104 failure mode pointing the other way.
#
# WHAT THE CALLER MUST KNOW. Nine of the 33 simulate to a small number
# because their payload needs a SECOND enemy and this comparison has one
# target (the splash items), or needs a distance it does not fix. That is a
# decision with a reason, which absence was not — but it is not a claim about
# the item in a real game, and whoever prices from this table should read
# `assumptions` and not only the number.


def _pct_item_stats(pct):
    """"+X% of all Stats from Items", `_shell`'s clause at another rate.
    Applied to the PRINTED item totals only, so it cannot compound with
    another item's passive grant."""
    def converts(ctx):
        return {k: pct * v for k, v in ctx.items.items() if v}
    return converts


def _every(cooldown, fn, key=None):
    """"Damage a God: ... Cooldown: Ns" — one hook for the attack and ability
    channels together, firing at most once per `cooldown`. The two share one
    timer, because the text gives the item one."""
    def hook(sim, ev):
        st = sim.item_state(key or sim._current_item, ready=0.0)
        if ev.t >= st["ready"]:
            st["ready"] = ev.t + cooldown
            fn(sim, ev)
    return hook


def _adaptive_sum(strength, intelligence):
    """Two adaptive clauses on one item, added before the choice is made:
    the text says "based on highest item stat" for each, and the item totals
    they read are the same, so both clauses always pick the same side."""
    return _adaptive(strength, intelligence)


# ── Ability-hit damage ────────────────────────────────────────────────────

def _ancient_signet(sim, ev):
    # "Ability Hit: +20 (+12 per Level) bonus Magical Damage ... Cooldown: 15s"
    sim.proc(20.0 + 12.0 * sim.level, "magical", ev)


def _archmage(sim, ev):
    # "Ability Hit a God: Deal bonus Magical Damage. Damage = 40% of your
    # Intelligence & 50% of your Strength Cooldown: 20s". "&", so both terms.
    sim.proc(0.40 * sim.stat("Intelligence") + 0.50 * sim.stat("Strength"), "magical", ev)


def _bluestone(sim, ev):
    # "Ability Hit: +100 Physical Damage over 2s Gods take additional damage =
    # 7.5% of their current Health Subsequent hits on the same target: 50%
    # bonus damage for 3s". "Current Health" is the target's health left in
    # this fight (`Sim.target_hp`), not its max. "Subsequent ... for 3s" is
    # read as The Crusher's clause is: a hit within 3s of the previous one.
    st = sim.item_state("Bluestone Brooch", last=-1e18)
    mult = 1.50 if ev.t - st["last"] <= 3.0 else 1.0
    st["last"] = ev.t
    sim.proc(mult * (100.0 + 0.075 * sim.target_hp()), "physical", ev)


def _gladiator(sim, ev):
    # "Abilities deal bonus Physical Damage. Damage = +10 + 40% of your Item
    # Protections Triggers once per Ability Cast, per God" — item protections
    # as `_golden_blade` reads them, and one target, so once per cast.
    prot = sim.stats.get("Physical Protection", 0.0) + sim.stats.get("Magical Protection", 0.0)
    sim.proc(10.0 + 0.40 * prot, "physical", ev)


def _shroud_heal(sim, ev):
    # "Ability Hit: +1% Max Health Heal +1% Max Mana Recovery". Mana is not
    # modelled here (`_phoenix`, and §4.16 on why mana carries no weight).
    sim.heal(0.01 * sim.max_health)


def _oath_sworn(sim, ev):
    # "Ability Hit: Target's Physical Protection is reduced by 5 for 4s. On
    # God Kill or Assist: This effect increases by 1 Physical Protection.
    # This effect caps at 20 total." Flat, so `add_flat_shred`; the growth is
    # the per-takedown counter below, and 20 is the cap on the whole effect.
    st = sim.item_state("Oath-Sworn Spear", points=5.0)
    sim.after(lambda: sim.add_flat_shred("Oath-Sworn Spear", "physical",
                                         st["points"], 1, 4.0, ev.t))


def _oath_sworn_takedown(sim, kind):
    st = sim.item_state("Oath-Sworn Spear", points=5.0)
    st["points"] = min(20.0, st["points"] + 1.0)


# ── Attack-hit effects ────────────────────────────────────────────────────

def _deaths_embrace(sim, ev):
    # "Attack Hit: +1% Max Health Heal +2% Max Mana Restore -0.33s Non
    # Ultimate Cooldowns". Mana is not modelled.
    sim.heal(0.01 * sim.max_health)
    sim.refund(0.33, 0.0)


def _contagion_taken(sim, hit):
    # "Damaged by an Attack or Ability: Apply +1 Stack of Contagion (1 per
    # hit)". The lifesteal clause ("If an enemy Lifesteals 100 Health from
    # you: +5 Stacks") reads the TARGET's lifesteal healing, which the HEALING
    # block does carry (`target_healed`), counted in whole 100s.
    st = sim.item_state("Contagion", stacks=0, seen=0.0)
    st["stacks"] += 1
    steps = int((sim.target_healed - st["seen"]) // 100.0)
    if steps:
        st["stacks"] += 5 * steps
        st["seen"] += 100.0 * steps


def _contagion_attack(sim, ev):
    # "Attack or Hard Crowd Control an afflicted enemy: Deal Magical Damage =
    # 1% Max Health per stack in a 4m radius Remove the Stacks". "Max Health"
    # with no owner reads as OUR max health, as Kinetic Cuirass's does.
    st = sim.item_state("Contagion", stacks=0, seen=0.0)
    if st["stacks"]:
        sim.proc(0.01 * sim.max_health * st["stacks"], "magical", ev)
        st["stacks"] = 0


# ── "Damage a God" procs (attack and ability share one timer) ─────────────

def _sundering_axe_hit(sim, ev):
    # "Damage a God: +150 (+10% of your Item Protections) Bonus True Damage
    # +125 Heal Hits only one God per activation ... Cooldown: 8s"
    prot = sim.stats.get("Physical Protection", 0.0) + sim.stats.get("Magical Protection", 0.0)
    sim.proc(150.0 + 0.10 * prot, "true", ev)
    sim.heal(125.0)


def _prophetic_hit(sim, ev):
    # "Damage a God: +1 Protection Stack against the damage type they deal.
    # Cooldown: 5s." The enemy deals physical as attacks and magical as
    # abilities (the FIGHT block's attacker), so a stack of each.
    st = sim.item_state("Prophetic Cloak", stacks=0.0)
    st["stacks"] = min(15.0, st["stacks"] + 1.0)


def _prophetic_prot(sim, dtype):
    st = sim.state.get("Prophetic Cloak")
    n = st["stacks"] if st else 0.0
    return n + (10.0 if n >= 15.0 else 0.0)


def _prophetic_reduce(sim, hit):
    # "At +15 of each Protection Stack, item evolves: ... +6% Damage
    # Mitigation (or +12% if total Protections > 300)". Read at the moment of
    # the hit, protections as the two pools our god carries now.
    st = sim.state.get("Prophetic Cloak")
    if not st or st["stacks"] < 15.0:
        return 1.0
    total = sim.prot_now("physical") + sim.prot_now("magical")
    return 1.0 - (0.12 if total > 300.0 else 0.06)


def _prophetic_stacks(ctx):
    # The evolution is permanent once reached, so a finished build reads it on
    # the stack clock like any other persistent stack.
    return {}


# ── Auras and per-second effects ──────────────────────────────────────────

def _mystical_mail(sim, t):
    # "Enemies within 4m: 15 (+1 per Level) Magical Damage and lose 25% of
    # Health Shield per 1s. Range Scaling Damage: +50% at Close Range -50% at
    # Maximum Range". The comparison fixes no distance between the gods, so
    # the stated number is taken with neither modifier. No enemy shield, so
    # the shield clause does nothing (`Erosion`'s reason).
    sim.active_damage(15.0 + 1.0 * sim.level, "magical", item="Mystical Mail")


def _yogi(sim, t):
    # "Heal +0.5% of your Max Health per second."
    sim.heal(0.005 * sim.max_health, item="Yogi's Necklace")


def _sphere(sim, t):
    # "Gain +2% Max Health Magical Shield every 3s, up to a maximum of +14%
    # Max Health." The shield is not consumed by time, so it holds until a hit
    # spends it; it is re-granted at the running total every 3s.
    if t <= 0 or int(round(t)) % 3:
        return
    st = sim.item_state("Sphere of Negation", granted=0.0)
    if st["granted"] >= 0.14 - 1e-9:
        return
    st["granted"] = min(0.14, st["granted"] + 0.02)
    held = sim.shields.get("Sphere of Negation", (0.0, -1.0))[0]
    sim.add_shield("Sphere of Negation", held + 0.02 * sim.max_health, 1e18)


def _odigba_takedown(sim, kind):
    # "God Kill or Assist: Heal +5% Max Health over 6s." Paid out by the
    # second, so a takedown late in the window heals only what fits in it.
    sim.item_state("Odigba", until=-1.0)["until"] = sim.t + 6.0


def _odigba_tick(sim, t):
    st = sim.state.get("Odigba")
    if st and t <= st["until"]:
        sim.heal(0.05 * sim.max_health / 6.0, item="Odigba")


def _pridwen_tick(sim, t):
    # "When the Shield expires or breaks: Explode again: Deal Magic Damage
    # (70% of your Protections)." The shield is granted for 5s at the press;
    # the second explosion lands when it ends.
    st = sim.state.get("Glorious Pridwen")
    if st and not st.get("second") and st.get("until", 1e18) <= t:
        st["second"] = True
        sim.active_damage(0.70 * st["prot"], "magical", item="Glorious Pridwen")


# ── Standing stat grants (the self half of a self-and-ally aura) ──────────

def _conch(ctx):
    # "You and allies within 8.8m: +5 (+0.5 per Level) Strength +5 (+1 per
    # Level) Intelligence" — our own half. Separate from the item's printed
    # 25 Strength / 40 Intelligence, which the stat block already carries.
    return {"Strength": 5.0 + 0.5 * ctx.level, "Intelligence": 5.0 + 1.0 * ctx.level}


def _ofuda(ctx):
    # "+20% Attack Speed for you and allies within 8.8m" — our own half,
    # separate from the printed 15%.
    return {"Attack Speed %": 20.0}


def _hunters_cowl(ctx):
    # "Within 8.8m of a God: +30% Attack Speed, +5% Lifesteal, and +15%
    # Movement Speed. Alone: ...". The clock's target is a god in range for
    # the whole window, so the first branch holds. Movement speed is not a
    # quantity here.
    out = _adaptive(55.0, 80.0)(ctx)
    out.update({"Attack Speed %": 30.0, "Lifesteal %": 5.0})
    return out


def _pendulum_ages(ctx):
    # "+3 Strength or +7 Intelligence (based on highest item stat) per 10% of
    # available Mana" — ten steps at full mana, which is where the fight
    # opens and the only mana state this comparison has. Added to the item's
    # own adaptive clause, which picks the same side.
    return _adaptive(45.0 + 30.0, 70.0 + 70.0)(ctx)


def _dwarven(ctx):
    # "+15 Physical Protections +35 Magical Protections" — on top of the
    # printed 35/35. The On Use swap is the half this item does not simulate.
    return {"Physical Protection": 15.0, "Magical Protection": 35.0}


def _oni_reduce(sim, hit):
    # "For each enemy god within 8.8m: +4% Damage Mitigation Max 3 stacks" —
    # one enemy god is in range, so one stack.
    return 1.0 - 0.04


def _adamantine(sim, key, v):
    # "While Below 50% Health: +10 Strength." Read off the fight's health bar,
    # exactly as Bancroft's Talon reads its own.
    return v + 10.0 if sim.hp < 0.50 * sim.max_health else v


# ── Hits taken ────────────────────────────────────────────────────────────

HELM_RADIANCE_PER, HELM_RADIANCE_MAX, HELM_RADIANCE_DURATION = 7.0, 4, 6.0


def _helm_radiance_taken(sim, hit):
    # "Take Physical Damage: +7 Physical Protection for 6s. Stacks up to 4
    # times." Physical only; `Draconic Scale`'s shape with one pool.
    if hit["dtype"] != "physical":
        return
    st = sim.item_state("Helm of Radiance", stacks=0, expires=0.0)
    timed_stacks(st, sim.t, HELM_RADIANCE_DURATION)
    st["stacks"] = min(HELM_RADIANCE_MAX, st["stacks"] + 1)
    st["expires"] = sim.t + HELM_RADIANCE_DURATION


def _helm_radiance_prot(sim, dtype):
    st = sim.state.get("Helm of Radiance")
    if not st or dtype != "physical":
        return 0.0
    return HELM_RADIANCE_PER * timed_stacks(st, sim.t, HELM_RADIANCE_DURATION)


def _leviathan_taken(sim, hit):
    # "Damaged by Enemy God: -0.5s once per Ability Cast or Attack. Cooldown:
    # 10s." The half this item does not simulate is above it: "that God is
    # -10% Strength & Attack Damage", which the enemy's derived DPS cannot
    # read, and "+8 Max Health Permanently", which the text never caps.
    st = sim.item_state("Leviathan's Hide", ready=0.0)
    if sim.t >= st["ready"]:
        st["ready"] = sim.t + 10.0
        sim.refund(0.5, 0.5)


# ── Takedowns ─────────────────────────────────────────────────────────────

def _necronomicon(sim, kind):
    # "God Kill or Assist: +1 Stack of: +30 Intelligence Stacks up to 6
    # times. On Death: Lose 4 Stacks." Our god does not die in the window.
    st = sim.item_state("Necronomicon", stacks=0)
    st["stacks"] = min(6, st["stacks"] + 1)


def _necronomicon_bonus(sim, key, v):
    st = sim.state.get("Necronomicon")
    return v + 30.0 * st["stacks"] if st else v


# ── Our own ability healed us (`ability_heals`) ───────────────────────────

def _daybreak_heal(sim, ability):
    # "Healed yourself with a Healing Ability: +1 Stack (max 3)"
    st = sim.item_state("Daybreak Gavel", stacks=0, buff=0, until=-1.0)
    st["stacks"] = min(3, st["stacks"] + 1)


def _daybreak_ability(sim, ev):
    # "Non-Healing Ability Use: Consume all Stacks, +10 Strength or +15
    # Intelligence (based on highest item stat) for 8s per Stack (max 3)
    # Cooldown: 4s". A cast that heals is not a non-healing ability.
    if ev.name in sim.self_heals:
        return
    st = sim.item_state("Daybreak Gavel", stacks=0, buff=0, until=-1.0, ready=0.0)
    if not st["stacks"] or ev.t < st.get("ready", 0.0):
        return
    st["buff"], st["until"], st["ready"] = st["stacks"], ev.t + 8.0, ev.t + 4.0
    st["stacks"] = 0


def _daybreak_bonus(sim, key, v):
    st = sim.state.get("Daybreak Gavel")
    if not st or not st.get("buff") or sim.t > st["until"]:
        return v
    per = 10.0 if key == "Strength" else 15.0
    return v + per * st["buff"]


def _vital_heal(sim, ability):
    # "Heal yourself with an Ability: +7.5% Attack Speed +5% Attack Damage
    # (Ranged) +10% Attack Damage (Melee) Buff lasts 6s, Stacks up to 3x"
    st = sim.item_state("Vital Amplifier", stacks=0, expires=0.0)
    timed_stacks(st, sim.t, 6.0)
    st["stacks"] = min(3, st["stacks"] + 1)
    st["expires"] = sim.t + 6.0


def _vital_bonus(sim, key, v):
    st = sim.state.get("Vital Amplifier")
    n = timed_stacks(st, sim.t, 6.0) if st else 0
    if not n:
        return v
    if key == "Attack Speed %":
        return v + 7.5 * n
    return v * (1.0 + (0.10 if sim.melee else 0.05) * n)


def _regrowth_heal(sim, ability):
    # "Heal yourself with an Ability: +25% Movement Speed (decays to 0%) for
    # 4s Cooldown: 10s Gain any Movement Speed buff: +5% Health Heal over
    # 10s". The movement speed is not a quantity here, but the SECOND clause
    # fires off the first, so the heal is fully determined: an ability self-
    # heal grants a movement buff, which grants 5% of max health over 10s.
    st = sim.item_state("Regrowth Striders", ready=0.0, until=-1.0)
    if sim.t >= st["ready"]:
        st["ready"], st["until"] = sim.t + 10.0, sim.t + 10.0


def _regrowth_tick(sim, t):
    st = sim.state.get("Regrowth Striders")
    if st and t <= st["until"]:
        sim.heal(0.05 * sim.max_health / 10.0, item="Regrowth Striders")


# ── Actives ───────────────────────────────────────────────────────────────

def _arondight(sim):
    # "Reveal enemy Gods within 17.6m for 6s ... First time you damage a
    # revealed God: +50 (+50% Strength) Physical Damage". The reveal lands on
    # the one target, which is in range. The +25% movement speed is not a
    # quantity here.
    sim.item_state("Arondight", until=-1.0, used=False)
    sim.state["Arondight"].update(until=sim.t + 6.0, used=False)
    return True


def _arondight_hit(sim, ev):
    st = sim.state.get("Arondight")
    if st and not st["used"] and ev.t <= st["until"]:
        st["used"] = True
        sim.proc(50.0 + 0.50 * sim.stat("Strength"), "physical", ev)


def _pridwen(sim):
    # "Explode (4.8m radius): Deal Magical Damage (40% of Protections) Gain a
    # Shield (125% of Protections) for 5s." "Protections" with no qualifier is
    # read as the two pools our god carries, base and items — the reading
    # `_brawler_prot` takes for the same word.
    prot = sim.prot_now("physical") + sim.prot_now("magical")
    sim.item_state("Glorious Pridwen", prot=0.0, until=-1.0, second=False)
    sim.state["Glorious Pridwen"].update(prot=prot, until=sim.t + 5.0, second=False)
    sim.active_damage(0.40 * prot, "magical")
    sim.add_shield("Glorious Pridwen", 1.25 * prot, sim.t + 5.0)
    return True


def _phoenix_feather(sim):
    # "Fire 3 Pulses that Heal you and True Damage enemies within 3.2m. Heal =
    # +75 Health +7.5 Missing Health True Damage = +3% Max Health from Items".
    # The text gives no interval for the pulses and no unit on "+7.5 Missing
    # Health": the LITERAL reading is taken for both — all three pulses at the
    # press, and 7.5 flat health, not 7.5% of what is missing.
    for _ in range(3):
        sim.heal(75.0 + 7.5)
        sim.active_damage(0.03 * sim.item_totals.get("Max Health", 0.0), "true")
    return True


def _myrddin(sim):
    # "Next non-Ultimate Ability used will have no cooldown."
    if not sim.any_on_cooldown():
        return False
    sim._free_cast = True
    return True


def _gargoyle(sim):
    # "Enemies in front of you: Silenced for 1s -10% Protections for 4s". The
    # silence is crowd control and is not in the comparison; the shred is.
    # Moonlight Phase is off (`The Reaper`).
    sim.add_shred("Screeching Gargoyle", 0.10, 1, 4.0, sim.t)
    return True


def _lifebinder(sim):
    # "Fire a projectile that deals 60 (+8 per Level) Magic Damage." The mark,
    # and the heal and shield the first ALLY to damage it receives, are the
    # half this item does not simulate.
    sim.active_damage(60.0 + 8.0 * sim.level, "magical")
    return True


REGISTRY.update({
    # ── Ability and attack procs ──
    "Ancient Signet": Passive(SIMULATED, "ability hit: +20 (+12/level) magical, every 15s",
                              ("no minions in the duel: the -2s minion clause never fires",),
                              on_ability=_every(15.0, _ancient_signet, "Ancient Signet")),
    "Archmage's Gem": Passive(SIMULATED, "adaptive +60 Str / +90 Int; ability hit: 40% Int + 50% Str magical, every 20s",
                              ("\"&\" reads as both terms, not a choice",),
                              grants=_adaptive(60.0, 90.0),
                              on_ability=_every(20.0, _archmage, "Archmage's Gem")),
    "Bluestone Brooch": Passive(SIMULATED, "adaptive +30 Str / +50 Int; ability hit: 100 + 7.5% of the target's current health, x1.5 within 3s",
                                ("\"their current Health\" is the target's health left in this fight",
                                 "\"subsequent ... for 3s\" read as The Crusher's clause is"),
                                grants=_adaptive(30.0, 50.0), on_ability=_bluestone),
    "Blood-soaked Shroud": Passive(SIMULATED, "adaptive +40 Str / +70 Int; ability hit: heal 1% of max health",
                                   ("the mana recovery is not modelled",),
                                   grants=_adaptive(40.0, 70.0), on_ability=_shroud_heal, heals=True),
    "Death's Embrace": Passive(SIMULATED, "adaptive +40 Str / +70 Int; attack hit: heal 1% of max health, -0.33s non-ultimate cooldowns",
                               ("the mana restore is not modelled",),
                               grants=_adaptive(40.0, 70.0), on_attack=_deaths_embrace, heals=True),
    "Gladiator's Shield": Passive(SIMULATED, "ability: +10 + 40% of item protections, physical",
                                  ("one target, so once per cast",), on_ability=_gladiator),
    "Oath-Sworn Spear": Passive(SIMULATED, "ability hit: -5 physical protection for 4s, +1 per takedown to a cap of 20",
                                ("flat protection reduction, not a percentage shred",),
                                on_ability=_oath_sworn, on_takedown=_oath_sworn_takedown),
    "Sundering Axe": Passive(SIMULATED, "adaptive +30 Str / +50 Int; damage a god: 150 + 10% of item protections true, +125 heal, every 8s",
                             ("one timer across the attack and ability channels",),
                             grants=_adaptive(30.0, 50.0),
                             on_attack=_every(8.0, _sundering_axe_hit, "Sundering Axe"),
                             on_ability=_every(8.0, _sundering_axe_hit, "Sundering Axe"), heals=True),

    # ── Standing grants ──
    "Triton's Conch": Passive(SIMULATED, "+15 Strength, +25 Intelligence at level 20 (our own half of the aura)",
                              ("the allies' half is not in the comparison",), grants=_conch),
    "Shogun's Ofuda": Passive(SIMULATED, "+20% attack speed (our own half of the aura)",
                              ("the allies' half is not in the comparison",
                               "separate from the item's printed 15%"), grants=_ofuda),
    "Hunter's Cowl": Passive(SIMULATED, "adaptive +55 Str / +80 Int; near a god: +30% attack speed, +5% lifesteal",
                             ("the target is a god in range for the whole window: the \"Alone\" branch never holds",
                              "the movement speed is not a quantity here"), grants=_hunters_cowl),
    "Pendulum of the Ages": Passive(SIMULATED, "adaptive +75 Str / +140 Int at full mana",
                                    ("the fight opens at full mana, the only mana state the comparison has",
                                     "the +4 mana per second is not modelled"),
                                    grants=_pendulum_ages),
    "Adamantine Sickle": Passive(SIMULATED, "+10 Strength below half health, read off the fight's health bar",
                                 ("exact in the fight run; a burst opens at full health (+0)",),
                                 stat_bonus=_adamantine, bonus_keys=("Strength",)),
    "Oni Hunter's Garb": Passive(SIMULATED, "+4% damage mitigation (one enemy god in range, one stack of three)",
                                 ("one target: the second and third stacks need enemies the comparison lacks",),
                                 reduce_hit=_oni_reduce),
    "Talisman of Purification": Passive(SIMULATED, "+7.5% of all item stats",
                                        ("the cleanse is crowd control and is not in the comparison",),
                                        converts=_pct_item_stats(0.075)),

    # ── Auras and per-second ──
    "Mystical Mail": Passive(SIMULATED, "aura: 15 (+1/level) magical per second",
                             ("target inside 4m for the whole window",
                              "no distance is fixed: the stated damage, neither the +50% nor the -50%",
                              "no enemy shield, so the shield strip does nothing"),
                             on_tick=_mystical_mail),
    "Void Shield": Passive(SIMULATED, "aura: the target's physical protection -10%",
                           ("target in range for the whole window",
                            "no distance is fixed: the stated 10%, neither extreme"),
                           aura_shred={"physical": 0.10}),
    "Void Stone": Passive(SIMULATED, "aura: the target's magical protection -10%",
                          ("target in range for the whole window",
                           "no distance is fixed: the stated 10%, neither extreme"),
                          aura_shred={"magical": 0.10}),
    "Yogi's Necklace": Passive(SIMULATED, "heal 0.5% of max health per second",
                               on_tick=_yogi, heals=True),
    "Sphere of Negation": Passive(SIMULATED, "+2% max health magical shield every 3s, to 14%",
                                  ("the shield has no stated duration: it holds until a hit spends it",),
                                  on_tick=_sphere),

    # ── Hits taken ──
    "Helm of Radiance": Passive(SIMULATED, "physical hit taken: +7 physical protection for 6s (4 stacks)",
                                on_hit_taken=_helm_radiance_taken, prot_bonus=_helm_radiance_prot),
    "Contagion": Passive(SIMULATED, "hits taken stack; an attack spends them for 1% of our max health each, magical",
                         ("\"Max Health\" with no owner reads as ours, as Kinetic Cuirass's does",
                          "the hard-CC trigger is not in the comparison; the attack trigger is",
                          "the enemy's lifesteal clause reads the target's healing, in whole 100s"),
                         on_hit_taken=_contagion_taken, on_attack=_contagion_attack),

    # ── Takedowns ──
    "Necronomicon": Passive(SIMULATED, "kill/assist: +30 Intelligence per stack (6)",
                            ("our god does not die in the window, so no stack is lost",),
                            on_takedown=_necronomicon, stat_bonus=_necronomicon_bonus,
                            bonus_keys=("Intelligence",)),
    "Odigba": Passive(SIMULATED, "kill/assist: heal 5% of max health over 6s",
                      ("paid by the second: a late takedown heals only what fits in the window",),
                      on_takedown=_odigba_takedown, on_tick=_odigba_tick, heals=True),

    # ── Our own ability healed us ──
    "Daybreak Gavel": Passive(SIMULATED, "adaptive +40 Str / +60 Int; a healing ability stacks (3), a non-healing one spends them for +10 Str / +15 Int each, 8s",
                              ("the healing ability is the god's own (`ability_heals`)",),
                              grants=_adaptive(40.0, 60.0), on_self_heal=_daybreak_heal,
                              on_ability=_daybreak_ability, stat_bonus=_daybreak_bonus,
                              bonus_keys=("Strength", "Intelligence")),
    "Vital Amplifier": Passive(SIMULATED, "adaptive +30 Str / +45 Int; a healing ability: +7.5% attack speed and +5%/+10% attack damage, 6s (3 stacks)",
                               ("the healing ability is the god's own (`ability_heals`)",
                                "melee reads the +10% branch, ranged the +5%"),
                               grants=_adaptive(30.0, 45.0), on_self_heal=_vital_heal,
                               stat_bonus=_vital_bonus,
                               bonus_keys=("Attack Speed %", "Attack Damage")),
    "Regrowth Striders": Passive(SIMULATED, "a healing ability grants a movement buff, which heals 5% of max health over 10s (10s)",
                                 ("the movement speed itself is not a quantity here; the heal it triggers is",),
                                 on_self_heal=_regrowth_heal, on_tick=_regrowth_tick, heals=True),

    # ── Damage dealt ──
    "Prophetic Cloak": Passive(SIMULATED, "damage a god (5s): +1 protection stack; at 15, +10/+10 and 6% (12% over 300) damage mitigation",
                               ("the enemy deals both types, so a stack of each accrues",
                                "the evolution is permanent once reached",),
                               on_attack=_every(5.0, _prophetic_hit, "Prophetic Cloak:cd"),
                               on_ability=_every(5.0, _prophetic_hit, "Prophetic Cloak:cd"),
                               prot_bonus=_prophetic_prot, reduce_hit=_prophetic_reduce,
                               stacking=True),

    # ── Actives ──
    "Arondight": Passive(SIMULATED, "active: reveal; the first damage on a revealed god +50 +50% Strength physical (60s)",
                         ("pressed at the fight's start; the one target is in range",
                          "the movement speed is not a quantity here"),
                         active=_arondight, active_cooldown=60.0,
                         on_attack=_arondight_hit, on_ability=_arondight_hit),
    "Glorious Pridwen": Passive(SIMULATED, "active: 40% of protections magical, a shield of 125%, then 70% again when it ends (45s)",
                                ("pressed at the fight's start",
                                 "\"Protections\" read as both pools our god carries, base and items"),
                                active=_pridwen, active_cooldown=45.0, on_tick=_pridwen_tick),
    "Phoenix Feather": Passive(SIMULATED, "active: 3 pulses, each heal 82.5 and 3% of item max health as true damage (120s)",
                               ("pressed at the fight's start",
                                "no interval is given for the pulses: all three at the press",
                                "\"+7.5 Missing Health\" carries no unit: read as 7.5 flat health"),
                               active=_phoenix_feather, active_cooldown=120.0, heals=True),
    "Staff of Myrddin": Passive(SIMULATED, "active: the next non-ultimate ability costs no cooldown (80s)",
                                ("pressed as soon as an ability is on cooldown",),
                                active=_myrddin, active_cooldown=80.0, active_trigger="after_casts"),
    "Screeching Gargoyle": Passive(SIMULATED, "active: the target's protections -10% for 4s (90s)",
                                   ("pressed at the fight's start",
                                    "the silence is crowd control and is not in the comparison",
                                    "Moonlight Phase off"),
                                   active=_gargoyle, active_cooldown=90.0),

    # ── PARTIAL: one half is simulated and the other cannot be ──
    "Agility Greaves": Passive(PARTIAL, "+7.5% of all item stats; the dash and the projectile-speed clauses are movement",
                               ("applied to printed item stats only",),
                               converts=_pct_item_stats(0.075)),
    "Time-lock Aegis": Passive(PARTIAL, "+6% of all item stats; the self-stasis active is not simulated",
                               ("the clock has no channel for our god being unable to act,"
                                " so neither the damage it dodges nor the output it costs can be read",),
                               converts=_pct_item_stats(0.06)),
    "Dwarven Plate": Passive(PARTIAL, "+15 physical / +35 magical protection; the On Use swap is not simulated",
                             ("which protection to raise is a read of the enemy's damage type,"
                              " and the sustained enemy deals both at an even split",),
                             grants=_dwarven),
    "Mercury's Talaria": Passive(PARTIAL, "adaptive +40 Str / +70 Int; the stored-energy clause needs out-of-combat movement",
                                 ("the energy is stored by MOVING while out of combat, and the"
                                  " clock has neither movement nor an out-of-combat phase",),
                                 grants=_adaptive(40.0, 70.0)),
    "Bumba's Spear": Passive(PARTIAL, "adaptive +35 Str / +60 Int; the on-hit damage lands on enemies AROUND the target, not on it",
                             ("one target: the comparison has no second enemy for the cleave",),
                             grants=_adaptive(35.0, 60.0)),
    "Bumba's Hammer": Passive(PARTIAL, "adaptive +35 Str / +60 Int, -0.66s cooldowns and +60 heal on the charged attack; the splash damage is not simulated",
                              ("one target: the +60 true damage lands on enemies around it",),
                              grants=_adaptive(35.0, 60.0),
                              on_ability=lambda sim, ev: sim.item_state("Bumba's Hammer", armed=False)
                              .__setitem__("armed", True),
                              on_attack=lambda sim, ev: _bumba_attack(sim, ev)),
    "Leviathan's Hide": Passive(PARTIAL, "damaged by a god: -0.5s cooldowns, every 10s",
                                ("the -10% Strength on the enemy cannot be read: its DPS is derived"
                                 " from the reference squishy, not built from its stats",
                                 "the +8 max health \"Permanently\" is not counted: the text gives no cap"),
                                on_hit_taken=_leviathan_taken),
    "Lifebinder": Passive(PARTIAL, "active: 60 (+8/level) magical damage; the ally heal and shield are not simulated",
                          ("pressed at the fight's start",),
                          active=_lifebinder, active_cooldown=20.0),

    # ── REFUSED: movement and distance ──
    "Gem of Focus": Passive(NOT_SIMULATED, "pathfinding on ability use", ("no movement",)),
    "Kopesh": Passive(NOT_SIMULATED, "movement speed on a crit", ("no movement",)),
    "Damaru": Passive(NOT_SIMULATED, "movement speed per Rhythm stack, then Harmonized",
                      ("no movement",)),
    "Helm of Darkness": Passive(NOT_SIMULATED, "active: stealth, passing through walls",
                                ("no movement, no stealth", "Moonlight Phase off")),
    "Ragnarok's Wake": Passive(NOT_SIMULATED, "active: fly 30m, then 600 magical and a knock-up",
                               ("the active displaces our god for 4.5s: no movement",
                                "the knock-up is crowd control")),
    "Circe's Hexstone": Passive(NOT_SIMULATED, "active: a dash that knocks up and damages",
                                ("no movement, so whether the dash connects cannot be read",
                                 "the text gives no duration for its +60 protections")),
    "Sharpshooter's Arrow": Passive(NOT_SIMULATED, "attack damage rising with distance, +10% at 6m",
                                    ("the comparison fixes no distance between the gods, and the"
                                     " clause has no value at zero distance to fall back on",
                                     "the +5% gold is economy, not a fight")),
    # ── REFUSED: crowd control ──
    "Ancile": Passive(NOT_SIMULATED, "active: the next ability silences", ("no crowd control",)),
    "Caestus": Passive(NOT_SIMULATED, "protections when hard crowd controlled", ("no crowd control",)),
    "Jade Scepter": Passive(NOT_SIMULATED, "active: knocks gods away", ("no crowd control",)),
    "Resolute Mantle": Passive(NOT_SIMULATED, "health regen and tenacity when hard crowd controlled",
                               ("no crowd control",)),
    "Ring of Dispel": Passive(NOT_SIMULATED, "hard crowd control lowers the target's Strength and Intelligence",
                              ("no crowd control",
                               "and the enemy's Strength is not a quantity here: its DPS is derived")),
    "Scepter of Dominion": Passive(NOT_SIMULATED, "active: a stasis zone", ("no crowd control",)),
    "Shroud of Vengeance": Passive(NOT_SIMULATED, "a shockwave when hard crowd controlled",
                                   ("no crowd control",)),
    "Spirit Robe": Passive(NOT_SIMULATED, "protections and a heal when hit by hard crowd control",
                           ("no crowd control",)),
    "Stone of Binding": Passive(NOT_SIMULATED, "hard crowd control shreds protections",
                                ("no crowd control",)),
    "Mantle Of Discord": Passive(NOT_SIMULATED, "a stun and +15 Dampening when damaged below 40% health",
                                 ("no crowd control",
                                  "and our own Dampening is worth exactly 0 to every number here (§4.19)")),
    # ── REFUSED: no ally ──
    "Chandra's Grace": Passive(NOT_SIMULATED, "regen and cooldowns to the lowest-health ally",
                               ("the comparison contains no ally", "Moonlight Phase off")),
    "Eros' Bow": Passive(NOT_SIMULATED, "a Beloved ally receives Strength and Intelligence",
                         ("the comparison contains no ally",)),
    "Heartwood Charm": Passive(NOT_SIMULATED, "active: stored healing to allies",
                               ("the comparison contains no ally",)),
    "Lotus Sickle": Passive(NOT_SIMULATED, "an ally's attack spends a Lotus stack",
                            ("the comparison contains no ally",)),
    "Radiant Bulwark": Passive(NOT_SIMULATED, "active: a wall that protects allies behind it",
                               ("the comparison contains no ally",)),
    "Rod of Asclepius": Passive(NOT_SIMULATED, "healing an ally raises our healing",
                                ("the comparison contains no ally",)),
    "Soul Locket": Passive(NOT_SIMULATED, "stacks from buffing an ally, spent for damage reduction",
                           ("the comparison contains no ally",)),
    "Umbral Link": Passive(NOT_SIMULATED, "lifesteal healing split with allies",
                           ("the comparison contains no ally",)),
    "Heroism": Passive(NOT_SIMULATED, "a shield to an ally hit by hard crowd control",
                       ("the comparison contains no ally", "no crowd control",
                        "the +1 gold per second is economy, not a fight")),
    # ── REFUSED: mana (§4.16) ──
    "Infused Axe": Passive(NOT_SIMULATED, "mana on a takedown",
                           ("mana is not modelled here, and carries no fit weight (§4.16)",)),
    "Oracle Staff": Passive(NOT_SIMULATED, "mana on a takedown",
                            ("mana is not modelled here, and carries no fit weight (§4.16)",)),
    # ── REFUSED: Echo is an expectation here, not an instance ──
    "Eye of the Storm": Passive(NOT_SIMULATED, "a storm at 10 Echo stacks",
                                ("`combat.echo_multiplier` carries Echo as an expected"
                                 " multiplier, so \"each time you Echo\" has no instance to count",
                                 "and Echo is a two-god mechanic (Ix Chel, Nut), in neither rotation")),
    "Omen Drum": Passive(NOT_SIMULATED, "Echo damage per Dark Resonance stack",
                         ("`combat.echo_multiplier` carries Echo as an expected multiplier,"
                          " so \"each time you Echo\" has no instance to count",)),
    "The Cosmic Horror": Passive(NOT_SIMULATED, "a tentacle every 3 Echoes",
                                 ("`combat.echo_multiplier` carries Echo as an expected"
                                  " multiplier, so \"each time you Echo\" has no instance to count",)),
    "Totem of Death": Passive(NOT_SIMULATED, "8% of missing health on each Echo",
                              ("`combat.echo_multiplier` carries Echo as an expected"
                               " multiplier, so \"each time you Echo\" has no instance to count",)),
    # ── REFUSED: a quantity the enemy profile does not carry ──
    "Midgardian Mail": Passive(NOT_SIMULATED, "the attacker's attack speed -10% per stack (4)",
                               ("the enemy's attack speed is not a quantity here: `attacker_profile`"
                                " derives its raw DPS from the reference squishy and"
                                " `_enemy_schedule` sets each hit to dps x share x step, so halving"
                                " the cadence halves each hit and changes no damage",)),
    "Pharaoh's Curse": Passive(NOT_SIMULATED, "active: -50% shields, -20% movement, -40% attack speed",
                               ("no enemy shield in the comparison", "no movement",
                                "the enemy's attack speed is not a quantity here (Midgardian Mail)")),
    "Spectral Armor": Passive(NOT_SIMULATED, "-30% damage from critical strikes",
                              ("the enemy deals no critical strikes: `crit_chance` is our god's only",
                               "our own Plating is worth exactly 0 to every number here (§4.19)",
                               "the comparison contains no ally")),
    "Wyrmskin Hide": Passive(NOT_SIMULATED, "a Dampening stack per god hit",
                             ("our own Dampening is worth exactly 0 to every number here (§4.19):"
                              " `build_quality.TARGET_SIDE_ONLY`",)),
    # ── REFUSED: no minions, no summons ──
    "Typhon\u2019s Heart": Passive(NOT_SIMULATED, "summons a monster at 30 stacks",
                                   ("the comparison contains no summons, and its stacks come"
                                    " from minion and jungle kills the duel does not have",)),
    "War Banner": Passive(NOT_SIMULATED, "a minion takedown buffs you and nearby allies",
                          ("no minions in the duel", "the comparison contains no ally")),
    "Alchemist Coat": Passive(NOT_SIMULATED, "Dampening on using a consumable, and a free potion",
                              ("the comparison contains no consumables and no inventory economy"
                               " (`Eye of Providence`'s reason)",
                               "and our own Dampening is worth exactly 0 here (§4.19)")),
    # ── REFUSED: the passive rewrites a god's own ability ──
    "Ashwhorl Acorn": Passive(NOT_SIMULATED, "rewrites Ratatoskr's Flurry",
                              ("the clock runs items against a scraped ability rotation and has no"
                               " hook for an item changing an ability's shape",
                               "the stat lines in the text are the item's printed stats, already counted")),
    "Briskberry Acorn": Passive(NOT_SIMULATED, "rewrites Ratatoskr's Dart",
                                ("the clock runs items against a scraped ability rotation and has no"
                                 " hook for an item changing an ability's shape",
                                 "the stat lines in the text are the item's printed stats, already counted")),
    "Thistlethorn Acorn": Passive(NOT_SIMULATED, "rewrites Ratatoskr's Acorn Blast",
                                  ("the clock runs items against a scraped ability rotation and has no"
                                   " hook for an item changing an ability's shape",
                                   "the stat lines in the text are the item's printed stats, already counted")),
    # ── REFUSED: simulating it would count the good half only ──
    "Xibalban Effigy": Passive(NOT_SIMULATED, "active: take 50% damage for 4s, then take the mitigated damage back",
                               ("the clock has no channel for our god damaging itself, and"
                                " `reduce_hit` alone would book the halving without the payback",
                                "Moonlight Phase off")),
})


def _bumba_attack(sim, ev):
    # "Hit this Attack: -0.66s Cooldowns, +60 Heal" — fires on the charged
    # attack landing. The +60 true damage it also deals goes to "enemies
    # within 1.92m of the target", which the comparison does not contain.
    st = sim.item_state("Bumba's Hammer", armed=False)
    if st["armed"]:
        st["armed"] = False
        sim.refund(0.66, 0.66)
        sim.heal(60.0)


REGISTRY["Bumba's Hammer"].heals = True
