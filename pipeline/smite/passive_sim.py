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
                               "'5% of their healing echoed to you' is"),
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


def _clip(text, limit=110):
    """The item's own text, cut at a word boundary with an ellipsis."""
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(" .,:;") + "…"
