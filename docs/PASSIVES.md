# The passive catalogue

_Written 2026-09-02 at commit d4ce174, input fingerprint `208b8d329f8e`
(control re-measured first: random-core baseline 5.7%, probe 40.9%, best 37.6%;
8,200 Obsidian+ Conquest matches, 25 Aug – 1 Sep, the window that reset on
25 Aug). This file is the argument. The data is `data/_passive_classes.yaml`,
one entry per buildable item with passive text, and
`test_passive_catalogue.py` holds that file to the pool so it cannot go stale
without failing. Read STATE.md §1, §4.5, §4.8, §4.12, §4.16 and §4.19 first —
every verdict below leans on one of them._

## 0. What this is for

`combat.py` reads exactly one passive. The shipped pricing flags read thirteen
items. Of the 138 god-agnostic buildable items, 137 carry passive text, so
**124 items carry value nothing in the model can see**, and by
`build_quality`'s own count 75% of the community's slots sit on them. Every
quality claim the project makes is biased by that, in our favour, and the
report says so on every run.

Three sessions attacked it. The broad attempt — price every unconditional
grant — is register §4.5 and ships off. Three narrow carve-outs of the same
idea shipped on: `price_crit_multipliers`, `price_conversions`,
`price_adaptive`. Nobody had catalogued what the other 124 passives ARE, so
each carve-out was chosen by inspection. This file does the catalogue, so the
next choice is made from a list rather than from a hunch, and so that "this
class cannot be priced" can be written down once with its reason instead of
being rediscovered per item.

**How to read it.** Classes are by the SHAPE of the value — what kind of
quantity the passive is — never by item, role or how often the community buys
it. An item lists every shape its text carries, primary first; "priced" is
per clause, so The Executioner's Adaptive Stat is priced and its shred is not.
Community slot counts appear in exactly one table (§3) and are descriptive:
they say where the ceiling is, and they are not an input to any verdict.

## 1. The three questions, and the range guard

Whether a passive can be priced without inventing a constant comes down to
three questions, and the shipped carve-outs are the three cases where every
answer was yes.

1. **CURRENCY.** Is the value a quantity the gold model prices — a regression
   column — or a `combat.py` quantity that maps onto one by a DOCUMENTED or
   OBSERVED formula? Crit damage maps onto Critical Chance because the crit
   multiplier was measured in game. A silence maps onto nothing.
2. **UPTIME.** Is the quantity always on, or is its rate fixed by the item's
   own text ("every fourth Attack Hit") or by the build's own stat line? A
   grant that exists "below 60% Health" or "for 8s after a crit" is worth its
   number times a fraction of fight time, and no source here supplies that
   fraction. §4.12 refused to invent the clock that would.
3. **REFERENCE.** If the value depends on something outside the item — the
   rest of the build, the target's health, your own protections — can the
   reference come from item data, the scraped kit or combat constants? A
   reference read off what the community buys is §1's circularity.

A fourth condition is not about the passive but about the price. **The
regression's gold per point is fitted over the range the pool actually
carries**, and a converted passive that lands far outside that range is priced
by extrapolation, not by evidence. Yogi's Necklace is the instance: "Heal +0.5%
of your Max Health per second" is exactly Health Regen, and at the roster-median
2,405 health at level 20 it is 60 HP5 — against a column fitted on 2 to 6. The
linear price (76.40 g/pt) says 4,600 gold for a 2,250-gold item. That is not a
finding about the item; it is the fit being asked a question it never saw.

    column fitted range, shipped flags (gold per point, carriers, min / median / max)
      Health Regen        76.40   15    2.00 /   4.00 /   6.00
      Penetration %       54.89   12    5.00 /  10.00 /  20.00
      Penetration         43.62   10    5.00 /  10.00 /  10.00
      Cooldown Rate       27.21   32   10.00 /  10.00 /  25.00
      Critical Chance %   26.02    9   10.00 /  20.00 /  34.00
      Attack Damage       21.95   11   10.00 /  25.00 /  60.00
      Strength            21.81   61   10.00 /  35.00 /  90.00
      Attack Speed %      20.89   30    8.00 /  20.00 /  52.50
      Intelligence        14.77   47   20.00 /  55.00 / 161.25
      Max Health           1.37   68  100.00 / 250.00 / 550.00

The families follow from the questions. **A** and **B** answer all three yes
(A: the passive IS a priced stat written in prose; B: it is a combat quantity
with an exchange rate into one). **C** fails uptime. **D** has a currency but
the recipient is not the god being scored. **E** has no currency at all.

## 2. The classes

| code | name | what it is | exchange rate | what it needs | verdict |
|---|---|---|---|---|---|
| A1 | grant-in-prose | an unconditional priced stat written in the passive | none — it is the stat | a level, if the text says "per Level" | **tractable** (`price_adaptive`'s shape) |
| A2 | build-conversion | a grant computed from a total over the rest of the build | none — it is the stat | a reference build from ITEM DATA | **tractable** (`price_conversions`' shape) |
| A3 | build-branch | which stat you get is fixed by the build's own stat line | none | a reference build to pick the branch | **tractable** (`price_adaptive` chose a branch from text) |
| A4 | cooldown-return | a cooldown refund that is a rate or a standing fraction | `cooldown_multiplier` — DOCUMENTED | the ability share, for a one-ability refund | **tractable** for the unconditional members |
| A5 | self-sustain | a heal or shield on yourself | a rate → Health Regen; a standing shield → Max Health | a health reference; a channel for a shield | tractable in currency, **refused on range** (see §1) |
| B1 | attack-channel-damage | bonus damage per basic-attack hit, or a crit multiplier | per hit ≡ Attack Damage per hit; crit via `CRIT_MULTIPLIER` (OBSERVED) | a level; your own stats for a scaled proc | **tractable** (`price_crit_multipliers` is a member) |
| B2 | cast-channel-damage | bonus damage per ability hit | per cast ≡ Strength / Intelligence through the roster-median ability scaling (scraped) | a target health reference for %-health members | **tractable per cast**; the target reference is the open design question |
| B3 | target-shred | reduces the target's protections | `effective_protection`'s reduction terms ≡ penetration at a reference target | a reference target (70 / 170, already used) | **tractable as a floor**; the stack ramp is uptime |
| B4 | self-mitigation | a % damage reduction on yourself | `mitigation` ≡ protection-equivalent at a reference protection | your own protections; the trigger for all but one member | tractable in currency, gated by C for every member |
| B5 | per-second-damage | a standing aura dealing damage per second | `attacks_per_second` at the roster-median base | enemies inside the radius | gated by C3 |
| C1 | health-state | exists only above / below / in proportion to a health fraction | — | time spent at that health | **refused**: no source, and the floor is the only priceable part |
| C2 | self-trigger | a timed buff on your own cast, hit or crit | trigger rate is kit-derivable | the duration against the fight clock | **refused**: §4.12's clock |
| C3 | enemy-trigger | fires on what the enemy does to you | — | the attacker's behaviour | **refused**: §4.17's argument — no attacker appears in a build score |
| C4 | outcome-trigger | fires on a kill or an assist | — | a kill rate | **refused**: the trigger IS the outcome `win` measures; any rate for it is §1's leakage |
| C5 | cooldown-gated | an active, or a proc with its own cooldown | — | fight length over cooldown | **refused**: §4.12's clock, exactly |
| C6 | persistent-stack | value that accrues over the match and is kept | — | the fraction of the cap a match reaches | **refused**: §4.8, measured off; `stack_fraction` swept, null |
| D1 | ally-directed | an aura, heal, shield or buff to allies | — | the allies | **refused for a per-god score**; the draft knows the team and is the home for it |
| D2 | enemy-debuff | reduces the enemy's damage, attack speed or healing | — | the attacker's build; a healing model | **refused**: `build_quality` has no attacker and no lifesteal sustain |
| E1 | control-utility | CC, immunity, mobility, stealth, vision, wards, gold, a consumable | none exists | — | **refused**: no currency; tags are the instrument |
| E2 | summon | a unit with its own health and damage | none | — | **refused** |

### Counts, and where the community's slots sit

Primary class only, so each item is counted once; "any" counts an item under
every class its text carries. Slots are the 543 community and 540 model
Conquest core slots `build_quality` compares. Mean residual is the shipped gold
model's, positive meaning the item costs more than its stat line predicts —
which is, by construction, what it pays for the passive.

    class  items(primary)  unpriced  any-clause  community slots  our slots  mean residual
    A1          12             4         14             16            3         +247
    A2           8             4          8             67           56         +396
    A3           1             1          4              1            0          +36
    A4           3             3          8             19            1         +206
    A5           3             3         11              1            0          +78
    B1          10             9         13             57           35         +176
    B2          10            10         23             55           63         +146
    B3           5             5          7              0            0         +221
    B4           2             2          8              0            0           -2
    B5           2             2          2              0            0         +368
    C1           5             5          9             36           30          -81
    C2           8             8         28              1           32         +227
    C3          11            11         21             75          105          +76
    C4           5             5          8             44           93          +36
    C5          32            32         46             65          116         +180
    C6           3             3          8              8            0         +570
    D1           3             3         21              0            0         +264
    D2           6             6         11              0            2         +146
    E1           7             7         25              7            1         +239
    E2           1             1          1              0            0         +213

    family   items   community slots   our slots
      A        27         104              60
      B        29         112              98
      C        64         229             376
      D         9           0               2
      E         8           7               1

Two things the table says that a reader would not guess. **C5 is the largest
class by a wide margin** — 32 of the 137 items are actives or cooldown-gated
procs, 46 carry such a clause, and every one of them prices at "fight length
over cooldown", the single constant §4.12 refused. And **the model already
over-buys the two families it cannot price**: C-primary items take 376 of our
540 slots against 229 of the community's 543, because their stat lines are the
part the model reads and the passive is where the gold went. That is the
blind spot's direction stated from the other side — we are not just missing
value, we are systematically paying for stat lines that were discounted for a
passive we then ignore.

### The classes, one at a time

**A1 — grant in prose.** Four unpriced items. Dominance (+20% penetration on
basic attacks, cap-ignoring, one channel), Shogun's Ofuda (+20% Attack Speed
for you — the ally half is D1), Triton's Conch (+5 (+0.5/level) Strength,
+5 (+1/level) Intelligence: +15 / +25 at level 20), Dwarven Plate (+15 and
+35 protections, always; the active only swaps which type gets which). The
broad parser reaches exactly two of them, and that is a finding about §4.5
worth more than the class: `price_passives` prices the Adaptive Stat clause as
its own column (the defect `price_adaptive` records), nine tier-2 components,
Dominance and Shogun's Ofuda — **and nothing else**. Its refutation is a
verdict on the column choice and on the components, not on unconditional
grants as a class. Triton's Conch defeats the grammar ("+5 (+0.5 per Level)
Strength") and Dwarven Plate is refused because "On Use" appears elsewhere in
the text, which `is_conditional` reads over the whole passive. Two of the four
have a wrinkle: Dominance is channel-specific and cap-ignoring, so it lands in
the `Penetration %` column at 1,098 gold for an item whose residual is +270 —
the Nimble Ring shape (`conversion_grants`' "amplify only" rule exists because
of it), and `cap_overflow` would charge it for a cap it ignores; Triton's needs
a level, and the only level the repo states is `build_quality`'s 20, in a
diagnostic, not in the scorer.

**A2 — build conversion.** The four priced converters and the four relics
carrying "+7.5% (6%) of all Stats from Items" — Agility Greaves, Shell of
Rebuke, Talisman of Purification, Time-lock Aegis — plus Genie's Lamp, which is
"+0.6% per Level", 12% at 20, and god-specific. It is the conversion shape with
source = every stat, and it is exact against a reference build: the median
tier-3 buildable item carries 1,485 gold of priced stats under the shipped
flags, a five-item reference is 7,427, and 7.5% of it is **557 gold** (446 at
6%, 891 at the Lamp's 12%). Set beside the residuals — Shell +740, Talisman
+1,022, Time-lock +946, Agility Greaves +1,566 — the multiplier is most of
Shell's premium and the remainder on each is the price of its active (C5).
One thing the precedent got wrong and this class must not repeat:
`conversion_reference` is the median over COMMUNITY builds, which is a
community-derived reference inside a shipped flag. The leakage-free reference
is the pool's own: the mean stat vector of a tier-3 buildable item, times
five, from item data alone.

**A3 — build branch.** The Cosmic Horror: "Echo > Cooldown Rate: +20% Echo
Damage / Echo < Cooldown Rate: +35 Intelligence". No uptime — the build
decides, deterministically. Under the pool reference Cooldown Rate exceeds
Echo (32 carriers against 6), so the branch is +35 Intelligence, a priced stat.
Shifter's Shield's "whichever is higher" and Dwarven Plate's switch are the
same shape as secondary clauses. `price_adaptive` is the precedent: it chose a
branch from the item's own text rather than from the fitted prices, precisely
so there is no fixed point.

**A4 — cooldown return.** Chronos' Pendant is the clean member: "-1s Ability
Cooldowns every 10s" is a 10% cooldown reduction on everything, and by the
documented `100/(100+x)` curve that is **11.1 Cooldown Rate**, unconditional,
no clock (the 10s is the item's own period, not a fight length). The World
Stone (-30% on the ultimate: 42.9 Cooldown Rate on one ability) needs the
ultimate's share of the rotation, which the kit supplies per god but a
god-agnostic price does not have. Heartwood Charm (-20% on healing abilities)
is the same with "healer" for "ultimate". The other five carriers of a
cooldown-return clause are triggered — by damage taken (Breastplate, Genji's,
Leviathan's), by kills (Jotunn's, Desolation) or by an active (Pendulum,
Myrddin) — and belong to C.

**A5 — self sustain.** Three primaries and eleven carriers. A RATE converts
exactly to Health Regen and a STANDING shield to Max Health — Sphere of
Negation's 14% max-health magical shield is 337 health at the roster median,
462 gold, in range, on one damage channel only (§4.17's pair; a shield that
stops magical damage is Max Health against magical and nothing against
physical). Yogi's Necklace is §1's range case and is refused on it. Shield of
the Phoenix heals per ability hit per god, and a per-cast heal has no column
and no rotation clock to become one.

**B1 — attack-channel damage.** The largest tractable class by community
slots (57), and the one §4.15 named: Odysseus' Bow and The Executioner "read
+316g and +999g overpriced — that premium is the passive value §4.5 prices at
zero." A flat bonus per attack hit is Attack Damage per hit at a symmetric
reference target, with no clock, because the Attack Damage column is itself
per hit. Tyrfing's base "+15 bonus Physical Damage" on every attack is
unconditional (its ramp is C2). Bragi's Harp is +70 magical per hit at level
20 — above the column's fitted maximum of 60 and on the wrong damage type for
a physical attacker, which is a wash only at a symmetric target. Odysseus' Bow
and Silverbranch Bow state their rate (every fourth, every third hit) and scale
off your OWN Attack Damage and swing — the self-referential conversion case,
which `conversion_grants` prices conservatively against a reference and
"amplify only" where the item does not itself carry the stat. Golden Blade and
Gladiator's Shield scale off your own item protections. Qin's Blade scales off
the TARGET's health: 2% of base health is scraped (roster median 2,405 →
48 per hit) and 5% of item health needs a target reference build. Hydra's
Lament and Polynomicon boost one swing per cast, which is per-rotation
accounting with no clock but does need the god's basic-attack damage.

**B2 — cast-channel damage.** Ten primaries. The Crusher's "+35% of your
Strength per ability hit" is a per-cast Strength conversion; for a god whose
abilities scale a median 0.65 Strength (scraped, 257 abilities parse) it is
worth +54% of what Strength is worth per cast. That exchange rate is the shape
`attack_damage_fit` used and it is leakage-free; it is also god-dependent, so
the god-agnostic price would use the roster median and the god side would go
to fit — where §4.10 measured that fit-side corrections alone do not move
cores. Heartseeker and Soul Reaver scale off the target's health (Qin's
reference question again); Gladiator's off your protections; Spear of the
Magus is a +5% multiplier on your own damage (and everyone else's — D1). The
other four B2 primaries are gated: Ancient Signet and Divine Ruin by a 15s
cooldown (C5), Barbed Carver by 5s stacks (C2), Totem of Death by the target's
MISSING health, which is the target's C1.

**B3 — target shred.** The Executioner's clause, and the class the backlog
called "defeating an additive gold model". It does not, quite:
`effective_protection` already takes `flat_reduction` and `pct_reduction`,
applied before penetration (INFERRED order, uncapped). Against the 70-protection
reference, one Executioner stack (-7%) removes 4.9 protection and four remove
19.6 — a flat-penetration equivalent of 214 to 855 gold at 43.62 g/pt. What is
not additive is the STACK RAMP: four hits to reach it, four seconds to lose
it, and whether a Carry keeps it up is a fight-clock question. Under the
model's own one-swing unit, one stack is the floor, which is
`crit_damage_as_chance`'s "IT IS A FLOOR" move exactly. Oath-Sworn Spear
(-20 flat at level 20, per ability hit, 4s) and Void Shield / Void Stone
(-10% on enemies within 8.8m, a standing aura) are the other members; the
team's share of every shred is D1 and stays unpriced, which is correct — it
is also why `_tags.yaml` keeps `protection-shred` and `penetration` apart.

**B4 — self mitigation.** The exchange rate is exact and worth writing down
even though no member can use it today: a standing mitigation `m` at your own
protection `P` is worth `(100+P)/(1-m) - 100 - P` protection points, so 4% at
the roster-median 76 is +7.3 and 12% is +24. Oni Hunter's Garb needs enemies
in range (one is the floor in any fight), Prophetic Cloak's lands at the evolve
cap (C6), Spectral Armor's is worth the attacker's crit share (C3), and the
rest are actives. Wyrmskin Hide and Alchemist Coat grant buyer-side Dampening,
for which `effective_health` has no term at all — §4.19.

**B5 — per-second damage.** Mystical Mail and Sanguine Lash: a standing aura
inside 4m. Per-second converts to per-hit through `attacks_per_second` at the
scraped base, with no new constant, but the radius is melee range and the
uptime against a ranged attacker is zero — C3.

**C1 – C6 — gated by uptime.** Sixty-four items, 229 community slots, and
this is where Freya's Tears (27), Genji's Guard (26), Shifter's Shield (19),
Spear of Desolation (19), Riptalon (14) and Jotunn's Revenge (14) live — six
of the ten most-bought blind items. Every one of them has a CURRENCY:
Berserker's Shield's "+15 Physical Protection +15 Magical Protection +25%
Attack Speed" is three priced stats. What none of them has is a source for
the fraction of a fight the condition holds. The classes differ in what would
supply it, and that is why they are kept apart: C2's trigger rate is
kit-derivable (a cast every 4s keeps an 8s buff at 100%) but its duration is
against the clock; C3's trigger is the attacker's behaviour, of which a build
score contains none; C4's trigger is the outcome itself; C5 is the clock
stated plainly; C6 is §4.8, already measured. Two things are priceable inside
C without a constant and are worth keeping in view: a FLOOR common to both
states (Riptalon's +10% Attack Damage is granted above 50% health and below
it — the interval is [+10%, +25%] and its lower end is unconditional), and
the CEILING at full uptime, which bounds what any future uptime model could
add. §4.17's argument applies: the pair is the whole range, and a single
number inside it is a stated mix nothing here supplies.

**D1 / D2 — recipient is not the scored god.** Nine primaries and 32
carriers. The value is real and the score cannot hold it: `score_god_items`
scores one god, and an aura's worth is a function of who stands in it. The
draft is the one surface that knows the team — `draftBuild.adaptedCore`
reads threats and tags — so ally-directed value has a home there as a tag
bonus, not in `efficiency`. D2 additionally needs the attacker's build
(a -10% Strength debuff is worth the attacker's Strength) or a healing model
(`build_quality` runs with "no lifesteal sustain"); neither instrument has
either.

**E1 / E2 — no currency.** Eight primaries and 26 carriers. A silence, a
stasis, a slow, an immunity, a stealth, a reveal, a ward, a potion, a summon.
`build_quality`'s UNMEASURABLE list names the same things. Nothing converts a
change of game state into damage or effective health without a model of the
fight, and the tag axis (`peel`, `cc-immunity`, `mobility`, `ward-economy`)
is the instrument this repo already chose for value it can identify and not
quantify.

## 3. The hypothesis, tested

The hypothesis offered with this session: all three shipped carve-outs
convert a passive into a quantity of a stat the gold model already prices, and
that is the tractability criterion. Tested against the catalogue rather than
assumed:

**As a filter it is right and it is the strongest fact in the table.** The
three shipped carve-outs are A1, A2 and B1 — every one converts into a priced
column — and family E, which has no currency, contains no item any instrument
here could ever price. Nothing that shipped came from C, D or E.

**As a predictor it is wrong, and the way it is wrong is the useful part.**
Currency alone marks 43 of the 124 as reachable by primary class and 76 by
any clause. But 33 items with a priced-currency clause sit in C: Berserker's
Shield converts into three priced stats and cannot be priced, because the
conversion is gated by a health state nobody can measure. The three shipped
flags share a SECOND property the hypothesis does not name — **the quantity
is unconditional**: Deathbringer's +35% is always on, the Adaptive Stat is
always on, and a conversion is always on once a reference fixes the source.
And a THIRD: the exchange rate came from a measured or documented formula or
the item's own text, never from a chosen constant. So the criterion is the
conjunction in §1 — currency ∧ uptime ∧ sourced reference — with the range
guard on top, and under it roughly twenty of the 124 are reachable today
(A1 4, A2 4, A3 1, A4 1, A5 1, B1 5–6, B2 3–4, B3 2–4, B4 0–1) while about a
hundred need a primitive the repo has refused (a clock, an uptime, a damage
mix) or lacks (an attacker, allies, a healing model). The refined criterion
also predicts the two refused-on-their-own-terms cases: `price_stacks` (C6)
satisfied currency and failed uptime, and `conversion_fit` (§4.9) satisfied
currency and reached for a reference from the community's composition.

## 4. The three known-hard cases

**Genie's Lamp** is A2 for its value and a DATA problem for its price. "+0.6%
per Level of all Stats from Items" is the "% of all stats" multiplier at 12%
at level 20 — 891 gold at the pool reference, computed the same way as Shell's
557 — and it is not the multiplier that keeps the Lamp out of the model. It
has no stats and no cost (`Cost: -1`, Aladdin is given it), so
`scoring.is_buildable` refuses it as statless and `efficiency` has no
residual for an item with no price. A2 would give it a stat line; nothing
here can give it a price without writing one, and a written price is a
constant (§4.12's rule). The wishes are C5 and E1. Honest state: buildable
for Aladdin under A2, and priced at "free" — which is the Blink Rune failure
mode (`is_buildable`'s docstring) and would need its own rule.

**Shell of Rebuke** is A2 + C5 + D1 + B4, and the catalogue puts a number on
the split: the multiplier is ~557 of its +740 residual and the mitigation
field for allies on a 120s cooldown is the rest. It is the most-missed
community item in the register (§4.11: 22×, residual +685 then, +740 now;
20 community slots against 0 of ours). The multiplier is exactly the shape
`price_conversions` shipped; the active is exactly the shape §4.12 refused.

**The Executioner's shred** is B3, and B3 has an exchange rate: the reduction
terms `effective_protection` already implements, against the 70-protection
reference `build_quality` already uses. What defeats the additive model is not
the shred but its RAMP — one to four stacks over four attacks, four seconds
to drop — which is an uptime. One stack is the floor, and it is a priceable
number (214 gold); the ceiling (855) is the number the community is
evidently paying for. `calibrate_combat --plan` could measure whether the 7%
is of total or of base protections, which the text does not say; that is the
only combat constant in this file that is not already pinned.

## 5. What is tractable, what is not

**Tractable now, no new constant** — the classes a carve-out can be cut from:

- **A2 build conversion**, the "% of all stats" relics: exact against a
  pool-derived reference; four buildable items and the Lamp.
- **A1 grant in prose**: Dwarven Plate and Triton's Conch cleanly (the
  latter at a stated level); Shogun's Ofuda's self half; Dominance with the
  channel and cap-overflow caveats.
- **A3 build branch**: The Cosmic Horror, under the pool reference.
- **A4 cooldown return**: Chronos' Pendant, exactly.
- **A5 standing shield**: Sphere of Negation, as magical-channel Max Health.
- **B1 flat on-hit**: Tyrfing's base +15 and Golden Blade's flat +10 with no
  question at all; Bragi's Harp with a level and a range caveat; the stated-
  rate procs (Odysseus', Silverbranch) as conservative self-referential
  conversions.
- **B2 per-cast scaled off your own stat**: The Crusher, through the
  roster-median scaling; Gladiator's Shield through a protection reference.
- **B3 shred, the floor**: one Executioner stack, one Oath-Sworn hit, and the
  standing Void Shield / Void Stone auras.

**Tractable in currency, refused on a second question** — where the refusal
is a fact worth a register line:

- **A5 rate sustain (Yogi's Necklace)**: the conversion is exact and the
  price is an extrapolation ten times past the fitted range. The general
  form: a converted magnitude outside a column's fitted range has no evidence
  behind its price, and the guard belongs in any future carve-out.
- **B1 / B2 members scaled off the TARGET** (Qin's, Heartseeker, Soul Reaver,
  Ethereal Staff): base health is scraped; the target's item health is a
  reference build for the OPPONENT, which is a mix question of §4.17's kind.
- **B4 / B5 as a class**: the exchange rates are exact and every member is
  gated by an enemy in range or an attacker's behaviour.
- **Buyer-side Plating and Dampening grants** (Wyrmskin, Alchemist Coat,
  Mantle): §4.19 — worth 0.0 to the only non-circular instrument until
  `effective_health` grows the term.

**Not priceable, and precisely why** — the refusals, each of which is the
same refusal as an existing register entry applied to a class:

- **C1 health-state** (5 primary, 9 carriers, 36 community slots): needs
  the fraction of fight time spent below a threshold. No source. The floor
  common to both states is the only unconditional part, and for most members
  it is zero.
- **C2 self-trigger** (8 / 28 / 1): the trigger rate is kit-derivable, the
  duration needs the fight clock. §4.12.
- **C3 enemy-trigger** (11 / 21 / 75): the attacker's behaviour, of which a
  build score contains none. §4.17's reasoning, and this class holds the two
  most-bought blind items in the game.
- **C4 outcome-trigger** (5 / 8 / 44): the trigger is the outcome `win`
  measures. A kill rate from anywhere is §1's leakage in a new coat, and from
  the kit it would be an invented constant.
- **C5 cooldown-gated** (32 / 46 / 65): fight length over cooldown. §4.12,
  and the largest class in the pool.
- **C6 persistent stacks** (3 / 8 / 8): §4.8. Not re-run.
- **D1 ally-directed** (3 / 21 / 0): a per-god score has no allies. The draft
  does; a tag bonus there is the honest route and is not a price.
- **D2 enemy-debuff** (6 / 11 / 0): needs the attacker's build or a healing
  model; `build_quality` has neither, so the charge could not be checked.
- **E1 / E2** (8 / 26 / 7): no currency. The tag axis is the instrument.

## 6. What I propose, and why

**`price_stat_multipliers`** — class A2's unpriced members: the four relics
and Genie's Lamp, "+X% of all Stats from Items" priced as X% of a
POOL-DERIVED five-item reference stat vector (mean `item_stat_values` over
tier-3 buildable items × 5, from item data alone — not `conversion_reference`,
which is community-derived), added to the item's own stat line under the
shipped flags. Default OFF. Swept on both leakage-free splits with the paired
per-god bootstrap, per-mode churn beside coverage, control re-measured first
and last, and the Carry guard (Berserker's Shield 0 of 18) and
`build_quality`'s role verdicts reported.

Why this one first, in order of weight:

1. **Every answer in §1 is yes with nothing chosen.** Unconditional; the
   exchange rate is the item's own percentage; the reference is item data;
   557 gold on a 2,500-gold item is inside every column's range because it is
   spread across all of them.
2. **It is the register's own top miss.** Shell of Rebuke is §4.11's
   most-missed community item and the fourth most-bought blind item; the
   other three relics have zero community slots, so the coverage effect is
   legible — it can only come through Shell — and the churn should be small
   and readable item by item, which is the condition under which §4.15's
   region was trusted.
3. **It is the only class that houses two of the three hard cases**, and it
   turns "Genie's Lamp cannot be modelled at all" into "Genie's Lamp has a
   stat line and no price", which is a narrower and more honest sentence.
4. **The prediction is written before the sweep**, per §4.16's trap: Shell's
   residual +740 → ~+183, Talisman +1,022 → ~+465, Time-lock +946 → ~+500,
   Agility Greaves +1,566 → ~+1,009. If the sweep moves coverage by more than
   Shell's 20 slots can account for, something else moved.

The two next in line, if this one ships or nulls:

- **`price_on_hit`** (B1, flat unconditional members first: Tyrfing +15,
  Golden Blade +10, Bragi's Harp): the largest reachable class by community
  slots (57) and the one §4.15 pointed at. Two design questions before code —
  the level convention for "per Level" text, and whether a magical bonus on a
  physical hit is priced at the symmetric reference or refused (a §4.17 mix).
- **`price_cooldown_returns`** (A4, Chronos' Pendant alone): exact, tiny,
  and a clean test of whether a one-item conversion into an existing column
  moves anything at all.

## 7. Found on the way, recorded and not acted on

- **`is_persistent_stacker` has two false positives**: Kinetic Cuirass
  ("Stacks up to 2 times", consumed on the next attack) and Oni Hunter's Garb
  ("Max 3 stacks", per enemy in range) carry no decay keyword and read as
  persistent. Inert while `price_stacks` is off; wrong the day it is not.
- **`unconditional_grants` misses two real A1 grants**: Triton's Conch's
  "+5 (+0.5 per Level)" grammar, and Dwarven Plate's always-on protections
  refused because "On Use" appears later in the text and `is_conditional`
  reads the whole passive rather than the clause. `stat_conversions` already
  splits by sentence for the same reason; the broad parser does not.
- **§4.5's scope is narrower than its sentence.** Beyond the thirteen items
  the shipped carve-outs price, `price_passives` reaches nine tier-2
  components, Dominance and Shogun's Ofuda, and prices the adaptive clause as
  its own column. "Pricing passives in general is refuted" is true of that
  configuration; it is not evidence about A1 grants on buildable items,
  because it has barely any.
- **The model over-buys the unpriceable families.** C-primary items hold 376
  of our 540 slots against 229 of the community's 543. Their stat lines are
  discounted for a passive the model then ignores — the residual table's
  negative column is the same fact from the other side (C1 mean residual -81,
  every A/B class positive).
- **The range guard** (§1) is a general condition on every conversion, not a
  Yogi's Necklace footnote, and none of the three shipped flags checks it.
  All three happen to land in range; the next one should assert it.

## 8. The items

Generated from `data/_passive_classes.yaml`; the note is the sidecar's.
Primary class first. A priced clause is marked.

| item | classes | note |
|---|---|---|
| Book of Thoth | **A2** (priced) · C6 | 5% of item mana as Intelligence (priced against the reference build); evolve stacks are §4.8 |
| Brawler’s Beat Stick | **A1** (priced) · D2 · C2 | Adaptive Stat priced; anti-heal and the in-combat +2%/stack ramp are not |
| Daybreak Gavel | **A1** (priced) · C2 · D1 | Adaptive Stat priced; the heal-stack burst needs the god to heal (heal-scaling) and a cast to spend it |
| Deathbringer | **B1** (priced) | +35% crit damage converted to Critical Chance off the OBSERVED 1.5x — the floor uses the item's own 20% |
| Eye of Erebus | **A1** (priced) · C5 · B2 · E1 | Adaptive Stat priced; the Watchful Eye is an active on 40s with % max-health damage and a reveal |
| Mercury's Talaria | **A1** (priced) · C2 | Adaptive Stat priced; stored-energy bonus needs time out of combat |
| Nimble Ring | **A2** (priced) | per-10-Intelligence conversion into Attack Damage and Attack Speed, priced amplify-only (the Attack Speed half) against the reference |
| Omen Drum | **A1** (priced) · C5 · B2 | Adaptive Stat priced; the mark-and-echo is an active on 90s |
| Rod of Tahuti | **A2** (priced) | 25% of item Intelligence as Intelligence, the deterministic conversion case |
| Sun Beam Bow | **A1** (priced) · C5 · B1 | Adaptive Stat priced; the toggle is an active with a mana cost per second |
| The Executioner | **A1** (priced) · B3 · C2 | Adaptive Stat priced. The shred — 7% protections per attack, 4 stacks, 4s — is B3 with a stack ramp; 1 stack is the floor under the model's one-swing unit |
| Transcendence | **A2** (priced) · C6 | 3% of item mana as Strength, the self-referential conversion case, priced conservatively; evolve stacks are §4.8 |
| Vital Amplifier | **A1** (priced) · C2 · D1 | Adaptive Stat priced; the attack-speed buff needs the god to heal |
| Agility Greaves | A2 · E1 · C5 | +7.5% of all item stats — A2 with source = every stat; projectile speed, movement-penalty relief and the dash are E1 |
| Alchemist Coat | E1 · C2 | a free Multi Potion per 60s is economy; +10 Dampening on consumable use is a timed buff on a buyer-side stat no instrument reads (§4.19) |
| Amanita Charm | C5 · D1 · B4 | active on 60s; the mushroom heals allies and stacks % mitigation for the duration |
| Ancient Signet | B2 · C5 | +20 (+12/level) magical damage per ability hit, but on a 15s internal cooldown — per-cast currency gated by the clock |
| Ancile | C5 · E1 | active silence on 70s |
| Arondight | C5 · E1 · B2 | active reveal on 60s, with movement speed and one bonus hit |
| Avatar's Parashu | C5 · E1 | +25% Strength for 10s on a 120s active — the grant is a priced stat, the uptime is 8% at best |
| Avenging Blade | B3 · C2 | -3.5% protections per attack hit, 3 stacks, 4s; doubled in the jungle or on a healing target |
| Bancroft's Talon | C1 | Intelligence and Lifesteal ramp off MISSING health, capping at 40% health — the tags file's "caps at" case |
| Barbed Carver | B2 · C2 | +8% (+1% per 10% Lifesteal) damage per stack per ability hit, 3 stacks lasting 5s |
| Berserker's Shield | C1 | below 60% health for 8s +15/+15 protections +25% Attack Speed — every grant is a priced stat, the state has no uptime source |
| Blood-Bound Book | C5 · A5 · C4 | active shield (7.5% max health + 75% Intelligence) on 80s, refreshed by kills |
| Bloodforge | C5 · A5 · C4 | active shield (10% max health + 150% Strength) on 80s, refreshed by kills |
| Bracer of The Abyss | C2 | +8 Attack Damage per god hit, 8 stacks, 10s — priced currency, uptime needs the clock |
| Bragi's Harp | B1 | +10 (+3/level) magical damage on every attack hit, no cooldown, no condition — +70 per hit at level 20, above the Attack Damage column's fitted range (max 60) |
| Breastplate of Valor | C3 · A4 | -1s cooldowns per 500 (+25/level) health lost — a cooldown return whose trigger is damage taken |
| Chandra's Grace | D1 · C5 | every 30s the lowest-health ally gets regen and cooldown ticks |
| Chronos' Pendant | A4 | -1s on all cooldowns every 10s — a 10% cooldown reduction, which is 11.1 Cooldown Rate by the documented formula, unconditional |
| Circe's Hexstone | C5 · E1 · B2 | active dash with CC immunity, protections and a knock-up on 120s |
| Contagion | C3 · D2 · B2 | stacks build from being hit; the burst is 1% max health per stack and needs the attacker's hit rate |
| Dagger of Frenzy | C5 · C4 | active +Attack Damage +Attack Speed for 6 attacks on 15s, refreshed by kills |
| Damaru | C2 | crit -> +8% ability damage 5s; echo -> +8% Attack Damage 5s — trigger rates derivable from crit chance and Echo, durations need the clock |
| Death Metal | C5 · A3 | active swaps Intelligence for 66% Strength and +25% crit for 6s on 45s |
| Demon Blade | C2 | crit -> +30% Attack Speed for 3s |
| Devourer's Gauntlet | C6 | 75 minion stacks to +40 Strength +6.75% Lifesteal, kept — §4.8 |
| Divine Ruin | D2 · B2 · C5 | 25% anti-heal on god damage; chain lightning 40 + 20% Intelligence on a 15s cooldown |
| Dominance | A1 | +20% penetration on basic attacks, unconditional, cap-ignoring, channel-specific — the one unconditional grant the broad parser reaches that no carve-out took |
| Doom Orb | C2 | +8 Intelligence per stack from minion kills, 5 stacks, 10s decay |
| Doublet of Binding | C5 · D1 | active redirects 20% of an ally's damage to you |
| Draconic Scale | C3 | +4 protections per hit taken, 7 stacks lasting 1.5s |
| Dreamer's Idol | C5 · E1 | +25% Intelligence and displacement immunity for 10s on a 120s active |
| Dwarven Plate | A1 · A3 | +15 and +35 protections, always on — the active only swaps which type gets which; the parser refuses it because "On Use" appears in the text |
| Eros' Bow | D1 · C5 | heals a marked ally per attack hit |
| Erosion | D2 · C3 | -30% shields on enemies in range; +10% protections when that fires |
| Ethereal Staff | B2 · C2 | steal 6% of the target's max health and mana per ability hit, stacks lasting 60s — needs a target health reference |
| Eye of Providence | E1 | wards and gold — ward-economy, the tag that already carries a penalty |
| Eye of the Storm | C5 · E1 | toggled vortex that costs your own health |
| Freya's Tears | C3 · C1 | +15/+15 protections for 5s each time 25% of health is lost, 2 stacks — trigger is damage taken |
| Gauntlet of Thebes | C6 | +15 max health per minion assist to 40, then evolves — §4.8 |
| Gem of Focus | C2 | +7% Pathfinding per ability used, 3 stacks, 8s — the one C2 whose uptime the kit could supply (cast rate vs 8s), but Pathfinding runs at 33% in combat |
| Gem of Isolation | E1 | 15% slow on ability hit |
| Genji's Guard | C3 · A4 | -3s cooldowns when hit by magical ability damage, once per 20s — a cooldown return whose trigger is the enemy's cast |
| Gladiator's Shield | B2 | +10 + 40% of item protections per ability cast per god — needs a reference for your own protections |
| Glorious Pridwen | C5 · A5 · B2 | active shield and explosion scaling off protections on 45s |
| Gluttonous Grimoire | B1 · C1 | stores 25% (40% at full health) of lifesteal healing as next-attack damage — needs a lifesteal-healing reference and a health state |
| Golden Blade | B1 | +10 + 20% of item protections per attack, in a 2.5m area — needs a reference for your own protections |
| Hastened Fatalis | E1 · C2 | attack-movement penalty relief on god hits |
| Heartseeker | B2 | 2% of your Strength as a % of the target's max health per ability hit — needs a target health reference; the base-health half is scraped |
| Heartwood Charm | A4 · D1 · C5 | -20% cooldowns on healing abilities (a standing fraction, healers only); stored healing released by an active |
| Helm of Darkness | C5 · E1 | active stealth and wall passthrough on 90s |
| Helm of Radiance | C3 | +7 physical protection per physical hit taken, 4 stacks, 6s |
| Hide of the Nemean Lion | C5 · C3 | active reflect on 60s — value is the attacker's damage |
| Hussar's Wings | E1 | slow immunity, unconditional and with no currency |
| Hydra's Lament | B1 · C2 | the next attack after an ability deals +30% (melee) or +20% (ranged) — one boosted swing per cast, needs a reference basic-attack damage |
| Jade Scepter | C5 · E1 | active knock-away on 60s |
| Jotunn's Revenge | C4 · A4 | cooldown returns on god kill or assist |
| Kinetic Cuirass | C3 · B1 | shockwave after being hit by 3 attacks — `is_persistent_stacker` reads its "Stacks up to 2 times" as persistent, which is wrong and inert while price_stacks is off |
| Lernaean Bow | C5 · B1 · D2 | active piercing volley on 30s with -50% shield; "Can Critically Strike" is permission |
| Leviathan's Hide | D2 · C6 · C3 | -10% Strength on your attacker; +8 max health per attack on a god, permanent and UNCAPPED; -0.5s cooldown when damaged |
| Lifebinder | C5 · D1 · B2 | active projectile that marks; the first ally to hit is healed and shielded |
| Magi's Cloak | E1 · C5 | a hard-CC-immunity bubble every 90s |
| Mantle Of Discord | C1 · C3 · E1 | below 40% health when damaged, stun and CC immunity, 110s |
| Midgardian Mail | D2 · C3 | -8% attack speed on whoever hits you, 4 stacks |
| Musashi's Dual Swords | E1 · C2 | crit -> +15% movement speed 5s |
| Mystical Mail | B5 · C3 | 15 (+1/level) magical damage per second to enemies within 4m — per-second, and melee-range |
| Necronomicon | C4 | +30 Intelligence per god kill or assist, 6 stacks, lose 4 on death |
| Oath-Sworn Spear | B3 · C2 | -1 physical protection per level (-20 at 20) for 4s per ability hit — flat shred, a flat-penetration equivalent; one hit is the floor |
| Obsidian Shard | C5 · A1 | +20% cap-ignoring penetration on the first ability cast, once per 10s — the stat is priced, the "first cast" needs a rotation length |
| Odysseus' Bow | B1 | every fourth attack hit chains 15 + 60% Attack Damage — a stated 1-in-4 rate, and the 60% is a self-referential conversion off your own Attack Damage |
| Oni Hunter's Garb | B4 · C3 | +4% mitigation per enemy god within 8.8m, to 3 — one enemy is the floor in any fight; `is_persistent_stacker` also misreads its "Max 3 stacks" |
| Pendulum Blade | C5 · A4 | -4s on all cooldowns per 40s active — 10% if used on cooldown, which is a use-rate assumption |
| Pharaoh's Curse | C5 · D2 | active -50% shields -20% movement -40% attack speed in 5.6m on 45s |
| Phoenix Feather | C5 · A5 · B2 | active heal and true-damage pulses on 120s |
| Polynomicon | B1 · C2 | next attack after an ability deals 80% of Intelligence, 2s cooldown — one boosted swing per cast |
| Prophetic Cloak | C6 · B4 · C3 | protection stacks per god damaged, evolving into +10/+10 and 6-12% mitigation — §4.8, and the mitigation lands only at the cap |
| Qin's Blade | B1 | +2% target base health +5% target item health per attack hit — base health is scraped (roster median 2405 at level 20), item health needs a target reference |
| Radiant Bulwark | C5 · D1 · B4 | active wall sharing your protections with allies behind it, 100s |
| Rage | C4 | +4% crit chance per god kill or assist to 20%, +10% after five |
| Ragnarok's Wake | C5 · E1 · B2 | active 600-damage meteor with a knock-up on 140s |
| Regrowth Striders | C2 · A5 · E1 | movement speed when you heal, and a 5% heal when you gain movement speed |
| Resolute Mantle | C3 · C6 | regen and tenacity when hard-CC'd, with a permanent 0.5 regen / 1 tenacity per stack to 20 |
| Riptalon | C1 | +10% Attack Damage above 50% health, +25% and +7.5% Lifesteal below — the +10% is common to both states and is a FLOOR |
| Rod of Asclepius | C5 · D1 | active team heal on 90s |
| Runeforged Hammer | C3 · B2 | hard-CC a god, then an attack forges the rune for +50 + 65% of item protections — your own CC rate is kit-derivable, the rest needs a target |
| Sanguine Lash | B5 · C3 · C5 | -0.75% health per second to enemies within 4m (+1% per 10% Lifesteal), with an active that triples the tick rate |
| Scepter of Dominion | C5 · E1 | active stasis zone on 90s |
| Screeching Gargoyle | C5 · B3 · E1 | active silence and -10% protections in a cone on 90s |
| Shell of Rebuke | A2 · C5 · D1 · B4 | +7.5% of all item stats (A2, ~557g at a five-item reference) plus an active mitigation field for allies on 120s — the +740 residual is roughly the sum |
| Shield Splitter | C5 · D2 · B2 | active true-damage projectile with -70% shield on 15s |
| Shield of the Phoenix | A5 · C2 | +1.5% health +2% mana per ability hit per god — a per-cast heal, which no column and no rotation clock can turn into Health Regen |
| Shifter's Shield | C1 · A3 | above 75% health +30 Strength or +40 Intelligence (whichever is higher — the adaptive branch); below, +20/+20 protections |
| Shogun's Ofuda | A1 · D1 | +20% Attack Speed for you (A1, the other unconditional grant the broad parser reaches) and for allies within 8.8m (D1) |
| Shroud of Vengeance | C3 · B2 | shockwave of 50 + 40% of protections (to 650) when hard-CC'd |
| Silverbranch Bow | B1 | every third attack hit fires arrows worth 25% of basic-attack damage, one per point of Attack Speed — a stated 1-in-3 rate scaled off your own swing |
| Soul Gem | B2 · A5 · D1 | every third ability hit adds 40% Intelligence damage and heals you and nearby allies |
| Soul Reaver | B2 | +1.2% target base health +3% target item health per ability hit, over 2s — the same target reference as Qin's Blade |
| Spear of Desolation | C4 | cooldown returns on god kill or assist |
| Spear of the Magus | B2 · D1 · C2 | marked gods take +5% damage from all sources for 8s — a multiplier on your own damage (B2) and everyone else's (D1) |
| Spectral Armor | B4 · C3 · D1 | -30% damage from critical strikes, -15% for allies — worth the attacker's crit share, a property of the attacker |
| Sphere of Negation | A5 | a standing magical shield of up to 14% max health, refilling 2% per 3s — Max Health on the magical channel only (§4.17's pair) |
| Spirit Robe | C3 | +40/+40 protections and a 4% heal for 6s when hit by hard CC |
| Staff of Myrddin | C5 · A4 | active that makes the next non-ultimate free, 80s |
| Stampede | C5 · D1 · E1 | active team movement speed and slow immunity on 90s |
| Stone of Binding | B3 · C2 | -7/-7 protections for 6s per hard CC you land, 3 stacks — your CC count is kit-derivable, the rate needs the clock |
| Stygian Anchor | D2 · A5 · C2 | 25% anti-heal, attack-speed slow and healing echoed to you, per stack |
| Talisman of Purification | A2 · C5 · D1 · E1 | +7.5% of all item stats (A2) plus a team cleanse on 140s |
| Tekko-Kagi | C2 | +7% Pathfinding per ability used, 3 stacks, 8s — the same clause as Gem of Focus |
| The Cosmic Horror | A3 | Echo > Cooldown Rate gives +20% echo damage, Echo < Cooldown Rate gives +35 Intelligence — decided by the build's own stat line, no uptime; a reference build says which branch |
| The Crusher | B2 | 35% of your Strength per ability hit over 1s, +33% on repeat hits — a per-cast Strength conversion, needing the roster-median ability scaling as the exchange rate |
| The Reaper | C4 · A5 | heal 15% of the slain god's max health on kill, 7.5% on assist |
| The World Stone | A4 | -30% cooldown on the ultimate only — 42.9 Cooldown Rate on one ability, so it needs the ultimate's share of the rotation, which is kit-derivable per god |
| Time-lock Aegis | A2 · C5 · E1 | +6% of all item stats (A2, ~446g at the reference) plus an active immunity on 140s |
| Titan's Bane | C5 · A1 | the same "first ability cast +20% cap-ignoring penetration, 10s" clause as Obsidian Shard |
| Totem of Death | B2 · C1 | 10% of the target's MISSING health per echo, once per second — the target's health state, of which a build score has none |
| Toxic Blade | D2 · C2 | 25% anti-heal and -7% attack speed on the target per attack hit; +7% attack speed to you, 3 stacks, 5s |
| Triton's Conch | A1 · D1 | +5 (+0.5/level) Strength +5 (+1/level) Intelligence to you (A1: +15 / +25 at level 20) and to allies in 8.8m (D1); the parser misses the per-level grammar |
| Typhon’s Heart | E2 · C6 | 30 stacks summon a monster scaling off Lifesteal and Intelligence |
| Tyrfing | B1 · C2 | +15 flat damage on every attack, unconditional (B1); +15 more per stack on god hits, up to 6 stacks by level, 4s (C2) |
| Umbral Link | D1 · C1 | above 50% health your lifesteal healing is split with allies, who each grant you +10 protections |
| Void Shield | B3 · D1 | -10% physical protection on enemies within 8.8m, ±50% by range — the self-share is a standing % shred, the team share is D1 |
| Void Stone | B3 · D1 | -10% magical protection on enemies within 8.8m — the magical twin of Void Shield |
| Wyrmskin Hide | C2 · B4 | Dampening per level against a god you hit, once per 8s — a buyer-side Dampening, which `effective_health` has no term for (§4.19) |
| Xibalban Effigy | C5 · B4 | active 50% mitigation for 4s that is paid back afterwards, 90s |
| Yogi's Necklace | A5 | heal 0.5% of max health per second — exactly Health Regen (60 HP5 at the roster-median 2405 health), and TEN TIMES the largest value the column was fitted on (6); the linear price does not reach it |
