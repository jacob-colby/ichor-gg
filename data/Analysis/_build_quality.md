# Build quality — `combat.py` pointed at whole builds

_Input fingerprint: `9f722a7ad5c8` — items, gods, tags, community builds, weights. Regenerate with `python -m smite.build_quality`; a different fingerprint means different inputs._

> **READ THIS BEFORE ANY NUMBER BELOW.** Of the 138 buildable items, 137 carry passive text and the shipped pricing flags read 13 of them — so **90% of the pool carries passive value this arithmetic cannot see**, and **75% of the community's item slots do** (407 of 543; 89% of ours, 479 of 540). `combat.py` reads exactly one passive — Deathbringer's +35% crit damage. The bias is not even: by the gold model's own residual the community pays **+79g more per slot above its stat line than we do** (mean residual -11g against -90g) and buys fewer stat columns per item (2.75 against 3.41) — that premium IS the passive. **A verdict in our favour is the one to distrust.** The most-bought blind community items are Freya's Tears (27), Genji's Guard (26), Obsidian Shard (26), Shell of Rebuke (20), Shifter's Shield (19).

This is the only instrument in the repo that can say a build is BETTER rather than more conventional: `validate.compute` is circular (STATE.md §1) and the leakage-free gate is coverage of the community's items, and both go down when a build is genuinely better and unconventional. `combat.py` is calibrated to 0.0% against in-game readings and has never seen a community build. It also cannot see a passive, which is the paragraph above.

Assumptions, all of them on every figure:

- **full ability uptime** — every ability cast the moment it is off cooldown, at its last rank, with no cast time charged (none exists in the scrape; register §4.12), so a god casts everything AND swings at full rate in the same second
- **no relic, single target, no lifesteal sustain, no crowd control, no wave clear**
- targets at exactly 70 and 170 protection of the god's own damage type, no Plating or Dampening
- level 20, six items, the community's slot picks against our meta-free `model` core (the first community entry, aspect or not — the one `validate` scores against)
- printed stat lines only, with penetration kept as two goods and capped (40% / 50); Deathbringer at the measured 1.85x
- a chain god's basic attack at the chain's mean multiplier; an ability without a scraped cooldown dropped, never imputed; a DoT counted as its listed damage once
- dual-role labels (`Solo Jungle`) collapse to their first word in the role tables
- a burst is one cast of every counted ability, summed; it charges no basic attacks, because a burst window in seconds does not exist in this repo (register §4.12)

**What none of this measures, at any level of slicing:** CC chain duration, peel, aura coverage, wave clear, objective damage, map tempo. Much of what a Support contributes is on that list, which is why Support's objective excludes damage rather than weighting it small — scoring a quantity badly is worse than declining to score it, and on 3 of 14 Supports the damage column is identical on both sides because neither build buys any.

Nothing here feeds `scoring`, `assemble` or a weight. It is a report a human reads.

## 1. The worked example

### Medusa (Carry)

**community** — 13,550g: Tyrfing · Odysseus' Bow · Riptalon · Silverbranch Bow · The Executioner · Hunter's Bow
  stat line: Attack Damage 70 · Attack Speed % 140 · Lifesteal % 7.5 · Penetration % 20 · Strength 25
  abilities counted: Acid Spray, Lacerate, Petrify

**ours** — 15,500g: Lernaean Bow · Jotunn's Revenge · Nimble Ring · Death Metal · Rod of Tahuti · Soul Gem
  stat line: Attack Speed % 50 · Cooldown Rate 35 · Critical Chance % 20 · Intelligence 215 · Lifesteal % 15 · Mana Regen 2 · Max Mana 500 · Penetration 10 · Penetration % 5 · Strength 110
  abilities counted: Acid Spray, Lacerate, Petrify

| | basic DPS | ability DPS | TOTAL | EHP physical | EHP magical |
|---|---|---|---|---|---|
| COMMUNITY vs squishy (70) | 343.9 | 35.9 | **379.8** | 3,788 | 3,353 |
| COMMUNITY vs tank (170) | 227.3 | 23.7 | **251.0** | 3,788 | 3,353 |
| OURS vs squishy (70) | 313.1 | 76.5 | **389.5** | 3,788 | 3,353 |
| OURS vs tank (170) | 194.8 | 47.6 | **242.4** | 3,788 | 3,353 |

| per 1000g | DPS vs 70 | DPS vs 170 | EHP physical | EHP magical |
|---|---|---|---|---|
| COMMUNITY | 28.0 | 18.5 | 280 | 247 |
| OURS | 25.1 | 15.6 | 244 | 216 |

## 2. The roster — our `model` core, printed stat lines

90 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 90 | **70** | **17** | 3 | -51.8% | +3.7% | **+24.2%** | +46.8% | +191.9% |
| total DPS vs 170 prot | 90 | **68** | **19** | 3 | -55.8% | +3.3% | **+24.6%** | +39.3% | +188.7% |
| effective health, physical | 90 | **36** | **9** | 45 | -22.3% | +0.0% | **+0.0%** | +14.0% | +144.7% |
| effective health, magical | 90 | **36** | **9** | 45 | -24.0% | +0.0% | **+0.0%** | +19.9% | +136.6% |
| total DPS vs 70 prot per 1000g | 90 | **63** | **27** | 0 | -44.1% | -4.9% | **+17.7%** | +31.9% | +169.8% |
| total DPS vs 170 prot per 1000g | 90 | **63** | **26** | 1 | -48.5% | -6.6% | **+13.8%** | +27.4% | +166.8% |
| effective health, physical per 1000g | 90 | **28** | **62** | 0 | -41.1% | -11.4% | **-6.6%** | +8.9% | +147.4% |
| effective health, magical per 1000g | 90 | **33** | **57** | 0 | -42.0% | -11.9% | **-5.6%** | +10.1% | +164.9% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 14 / 3 / +46.0% | 13 / 5 / +35.5% | 5 / 0 / +0.0% | 5 / 0 / +0.0% |
| Jungle | 18 | 13 / 5 / +23.4% | 12 / 6 / +22.1% | 2 / 2 / +0.0% | 2 / 2 / +0.0% |
| Mid | 22 | 19 / 3 / +28.0% | 19 / 2 / +28.5% | 3 / 1 / +0.0% | 3 / 1 / +0.0% |
| Solo | 18 | 17 / 1 / +43.5% | 17 / 1 / +40.7% | 12 / 6 / +6.2% | 12 / 6 / +6.6% |
| Support | 14 | 7 / 5 / +1.6% | 7 / 5 / +1.6% | 14 / 0 / +30.5% | 14 / 0 / +36.1% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 12 / 6 / +29.0% | 12 / 6 / +19.0% | 2 / 16 / -9.1% | 2 / 16 / -9.1% |
| Jungle | 18 | 12 / 6 / +20.0% | 12 / 6 / +15.8% | 3 / 15 / -8.0% | 3 / 15 / -8.0% |
| Mid | 22 | 18 / 4 / +12.5% | 18 / 3 / +12.0% | 3 / 19 / -10.2% | 3 / 19 / -10.2% |
| Solo | 18 | 16 / 2 / +46.7% | 16 / 2 / +45.1% | 9 / 9 / -0.0% | 11 / 7 / +6.8% |
| Support | 14 | 5 / 9 / -10.8% | 5 / 9 / -10.8% | 11 / 3 / +17.5% | 14 / 0 / +18.6% |

## 3. Judged by role, on each role's own objective

Most roles clear a THRESHOLD and then maximise something else, and one pooled metric cannot represent five roles that do not share an objective. Each row below names both quantities. **The passive blind spot at the top of this report applies to every row here exactly as it applies to the pooled figures** — slicing by role does not escape it, and the bias still runs in our favour.

**An objective containing effective health is scored on BOTH damage channels and read as the interval between them.** A build has one damage output and two effective healths; which one its survival is read on is a property of the ATTACKER, and there is no attacker in this comparison. Against a stream that is a share `f` physical, effective health is `1 / (f/EHP_p + (1-f)/EHP_m)` — a weighted harmonic mean, because what averages over a mixed stream is the damage-taken multiplier and not its reciprocal — and the ours-over-theirs ratio is monotone in `f`, so **every possible damage mix lands between the two channels and the pair is the whole range**. `ahead` below therefore means ahead at every mix, `behind` means behind at every mix, and `mix-dependent` means the answer is a fact about the enemy team that this comparison does not contain. Averaging the two channels would assert equal exposure, which is a constant no source here supplies — and would not even be the answer to its own question, since the correct collapse at 50/50 is harmonic and not arithmetic. Until 2026-08-23 both roles read `ehp_physical` alone, i.e. the two roles whose job is durability were scored on half the damage in the game.

| Role | n | Threshold | Binds? | Maximised | ahead | behind | level | mix-dependent | median |
|---|---|---|---|---|---|---|---|---|---|
| Carry | 18 | survive one enemy burst rotation | **no** — 0 of 36 builds fail it | sustained DPS per 1000g | **12** | **6** | 0 | – (no EHP term) | **+29.0%** |
| Jungle | 18 | rotation burst >= a reference squishy's EHP | **no** — all 80 builds fail it | rotation burst per 1000g | **11** | **7** | 0 | – (no EHP term) | **+5.6%** |
| Mid | 22 | rotation burst >= a reference squishy's EHP | **no** — all 80 builds fail it | sustained DPS per 1000g | **18** | **4** | 0 | – (no EHP term) | **+12.5%** |
| Solo | 18 | **none** | – | duel score, EHP x DPS | **16** | **1** | 0 | **1** | **+49.5% … +51.2%** |
| Support | 14 | **none** | – | effective health per 1000g | **11** | **0** | 0 | **3** | **+17.5% … +18.6%** |

Builds whose verdict the damage mix decides — the interval spans both answers, so neither is available here:

- **Amaterasu** (Solo) — vs a physical opponent -0.6% · vs a magical opponent +20.5%
- **Ares** (Support) — vs a physical opponent -8.1% · vs a magical opponent +1.2%
- **Athena** (Support) — vs a physical opponent -7.6% · vs a magical opponent +21.4%
- **Horus** (Support) — vs a physical opponent -6.7% · vs a magical opponent +9.1%

Why each objective is what it is:

- **Carry** — a Carry needs enough effective health to live through one burst — a floor, not a maximand. Buying more than the floor is gold not spent on damage, which is what the pooled metric scored as a win.
- **Jungle** — same kill threshold as Mid, and past it a gank is priced on burst rather than on sustained damage — a Jungler is not standing in the fight for the seconds a DPS figure assumes.
- **Mid** — a Mid's rotation either kills the squishy or it does not; past that the question is how often it comes back.
- **Solo** — not a threshold at all — a RATIO. Their time-to-kill on you over yours on them is (EHP / ref DPS) / (ref EHP / DPS), so the reference opponent CANCELS in ours-over-theirs and what is left is EHP x DPS. A build that doubles effective health and halves damage scores exactly 1.00 — neutral, which is the case neither scalar describes, and it is a property of the algebra rather than of a constant anyone chose. The EHP factor is effective health against THAT reference opponent, so it is scored on both channels and read as the interval between them — a duel against a physical opponent and a duel against a magical one, with every mixed opponent in between.
- **Support** — damage is EXCLUDED, not down-weighted. Most of what a Support is for is in `UNMEASURABLE`, and its damage column is provably empty on 3 of 14 gods. Effective health is scored on BOTH channels and read as the interval between them: a Support that survives physical damage and one that survives magical damage are different builds, and which matters is a property of the enemy team, which is not in this comparison.

### Neither threshold binds, and that is a statement about this arithmetic

Both thresholds were defined, measured and left in the table with their measurement, rather than dropped quietly. Re-measured on every run by `threshold_probe`:

| Threshold | population | reference | separates | nearest build |
|---|---|---|---|---|
| Carry: survive one enemy burst rotation | 36 builds | largest burst in the roster at 0 protection — Scylla, ours, 2,952, magical damage, so effective health is read on that channel | **0 of 36** | 1.14x the threshold |
| Mid / Jungle: rotation burst >= a reference squishy's EHP | 80 builds | median effective health of the community's own Carry and Mid builds, on the channel each attacker's own damage type reads — physical 3,788 / magical 3,399 | **80 of 80** | 0.72x the threshold |

A threshold that separates none of the population and a threshold that separates all of it are equally useless, and one of each is what these are. **Read this as "we cannot currently evaluate a threshold", not as "thresholds do not matter in SMITE"** — the cause is on our side of the arithmetic. A burst here is one cast of every ability with no basic attacks, no item passive, no follow-up and one target, while effective health is full level-20 health plus every protection the six items carry; the two are about an order of magnitude apart. Two things would change the answer and neither is a tuning choice: **a clock** (register §4.12 — a burst window in seconds would let basic attacks into the burst, and it is refused because no source supplies one), or **priced passives** (register §4.5 — ~90% of the pool carries value neither side of this comparison can see). Until one of those exists, Carry, Mid and Jungle are judged on their maximand alone.

### Where the Carry surplus comes from — measured, and currently closed

This section describes a defect that is **not currently present**: our Carry cores buy no more Physical Protection than the community's. It re-measures on every run rather than asserting that, so a refresh or a weight change that brings the surplus back restores the diagnosis in the same paragraph. `offmap_efficiency` is the flag that closed it — see docs/STATE.md §4.15.

Mean defensive stats bought at level 20, community (C) against our `model` core (O):

| Role | n | Physical Protection C / O | Magical Protection C / O | Max Health C / O |
|---|---|---|---|---|
| Carry | 18 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 55.6 |
| Jungle | 18 | 3.3 / 8.9 | 6.4 / 11.1 | 83.3 / 183.3 |
| Mid | 22 | 5.5 / 10.9 | 7.1 / 19.1 | 29.5 / 81.8 |
| Solo | 18 | 110.1 / 104.4 | 112.0 / 107.2 | 691.9 / 894.4 |
| Support | 14 | 90.6 / 137.1 | 113.1 / 166.1 | 461.8 / 953.6 |

The community buys 0.0 Physical Protection across all 18 Carries and we buy 0.0, a surplus of +0.0. The defensive items still reaching a Carry core, with how many of ours hold each against how many of the community's — an EMPTY list here is the measurement, not a missing section:

- **Golden Blade** — ours 5 of 18, community 0 of 18 (Max Health 200)

Two things worth keeping now that the surplus is gone. Effective health is the quantity to read it on, and it is +0.0% physical and +0.0% magical against the community's — LEVEL is the honest target here, not zero, because §4.13 means no threshold in this report can charge us for buying too LITTLE defence, so a figure BELOW the community's would not be visible as a cost. And `defense_affinity` and `draft.archetype_scaled_stats` are **excluded as causes**: both are read only by the viewer's draft overlay (`viewer/src/lib/threats.ts`), which is applied on top of a finished core and never reaches the builds measured here, and `defense_affinity` is 0.0 for Carry in any case because it is derived from the same role map that names no protection for the role. See docs/STATE.md §4.

### Where the off-map charge lands — measured on every run

`offmap_efficiency` ships at **0.55** and charges an item for the gold it spent on stats the god's fit map does not name (STATE.md §3, §4.15). This is what that bill is made of in our own cores, at full strength — the charge is linear in the strength, so the shipped value scales every row equally. **Nothing here changes a build**; it is here because every attempt on this charge so far has had to rebuild the composition by hand against a dataset that had moved under the previous one.

| Role | n | off-map gold in our cores | largest lines |
|---|---|---|---|
| Carry | 18 | 1,371g | Max Health 100.0% |
| Jungle | 18 | 9,391g | Echo 46.0%, Lifesteal 22.2%, Max Health 17.5%, Attack Speed 5.6%, Plating 4.4% |
| Mid | 22 | 4,967g | Lifesteal 87.6%, Plating 12.4% |
| Solo | 18 | 3,964g | Plating 93.1%, Lifesteal 6.9% |
| Support | 14 | 2,871g | Plating 100.0% |

And what the two mechanical tests of §4.16 say about each stat being billed. A stat named by SOME role map has a CONTRAST, so another role's silence about it is a positive statement by the same table and charging it is legitimate; a stat named NOWHERE has no contrast to read. The second column is test (ii) — if `combat.py` can see the stat then charging it is a hypothesis this report can check, which is why it may not simply be exempted.

| Stat | named by `role_stats` | `combat.py` | on `offmap_exempt` |
|---|---|---|---|
| Plating | 0 of 21 — **nowhere** | flat_reduction_multiplier — **on the target only** | no |
| Lifesteal | 3 of 21 (Carry, Hunter, Sharpshooter) | LIFESTEAL_MINION_SCALE | no |
| Echo | 0 of 21 — **nowhere** | echo_multiplier | no |
| Max Health | 6 of 21 (Brawler, Guardian, Solo, Support, Tank, Warrior) | effective_health | no |
| Attack Speed | 5 of 21 (Carry, Constant, Hunter, Pressure, Sharpshooter) | attack_dps | no |
| Tenacity | 0 of 21 — **nowhere** | TENACITY_CAP | no |
| Pathfinding | 0 of 21 — **nowhere** | PATHFINDING_COMBAT_SCALE | no |

**No verdict is drawn here**, and that is deliberate: deciding whether a line in the first table is a defect needs the community's own record and the leakage-free coverage gate as well, and both live outside this module. The verdicts reached so far are register §4.15 (the defect stats — charge them), §4.16 (mana and the regens — exempt them), §4.18 (Echo — charge it, and why the role that pays most for it is not being wronged) and §4.19 (Plating and Dampening — charge them, because the check cannot be run and sparing either changes nothing in the mode that has a gate).

A row reading **on the target only** is the one case this report cannot adjudicate at all: `combat.py` prices the stat on an OPPONENT and nothing reads it off the build being judged, so a charge on it is neither confirmed nor refuted by anything above. See `TARGET_SIDE_ONLY`.

## 4. The same, for the blended `core` (what the Balanced tab ships)

`core` carries `win` and `pick`, so it is part community build already; the gap between this block and §2 is what the meta signal buys in this arithmetic.

90 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 90 | **67** | **21** | 2 | -40.9% | +0.5% | **+21.6%** | +38.6% | +136.2% |
| total DPS vs 170 prot | 90 | **67** | **21** | 2 | -39.4% | +0.2% | **+19.4%** | +38.7% | +133.6% |
| effective health, physical | 90 | **38** | **9** | 43 | -25.3% | +0.0% | **+0.0%** | +18.6% | +144.7% |
| effective health, magical | 90 | **31** | **14** | 45 | -26.4% | +0.0% | **+0.0%** | +9.0% | +136.6% |
| total DPS vs 70 prot per 1000g | 90 | **60** | **30** | 0 | -41.3% | -9.6% | **+10.8%** | +25.1% | +111.7% |
| total DPS vs 170 prot per 1000g | 90 | **60** | **30** | 0 | -42.5% | -9.6% | **+8.9%** | +25.9% | +109.4% |
| effective health, physical per 1000g | 90 | **29** | **58** | 3 | -39.2% | -11.8% | **-5.9%** | +8.8% | +134.4% |
| effective health, magical per 1000g | 90 | **24** | **62** | 4 | -40.2% | -12.2% | **-7.8%** | +3.7% | +109.7% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 14 / 4 / +32.7% | 14 / 4 / +31.5% | 5 / 0 / +0.0% | 5 / 0 / +0.0% |
| Jungle | 18 | 12 / 5 / +15.7% | 12 / 6 / +11.0% | 2 / 3 / +0.0% | 2 / 3 / +0.0% |
| Mid | 22 | 18 / 4 / +18.2% | 18 / 3 / +20.3% | 4 / 1 / +0.0% | 4 / 1 / +0.0% |
| Solo | 18 | 15 / 3 / +34.6% | 15 / 3 / +34.7% | 13 / 5 / +7.4% | 8 / 9 / -0.3% |
| Support | 14 | 8 / 5 / +1.3% | 8 / 5 / +1.3% | 14 / 0 / +35.0% | 12 / 1 / +38.5% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 14 / 4 / +20.2% | 14 / 4 / +16.9% | 1 / 16 / -9.5% | 1 / 16 / -9.5% |
| Jungle | 18 | 11 / 7 / +8.1% | 10 / 8 / +3.5% | 2 / 14 / -8.4% | 2 / 14 / -8.4% |
| Mid | 22 | 17 / 5 / +7.7% | 18 / 4 / +6.5% | 3 / 19 / -8.9% | 3 / 19 / -8.9% |
| Solo | 18 | 14 / 4 / +30.6% | 14 / 4 / +30.2% | 10 / 8 / +3.2% | 7 / 11 / -6.1% |
| Support | 14 | 4 / 10 / -9.9% | 4 / 10 / -9.9% | 13 / 1 / +21.8% | 11 / 2 / +20.2% |

## 5. Sensitivity — the passives the gold model CAN price

Same as §2 with the shipped pricing flags applied to every stat line: the Adaptive Stat grants (`price_adaptive`) and the mana conversions (`price_conversions`). This is the one slice of the blind spot that can be put on the table; the other 124 items stay invisible here too.

90 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 90 | **69** | **18** | 3 | -54.5% | +3.7% | **+23.1%** | +42.5% | +191.9% |
| total DPS vs 170 prot | 90 | **69** | **18** | 3 | -55.8% | +2.1% | **+21.6%** | +39.2% | +188.7% |
| effective health, physical | 90 | **36** | **9** | 45 | -22.3% | +0.0% | **+0.0%** | +14.0% | +144.7% |
| effective health, magical | 90 | **36** | **9** | 45 | -24.0% | +0.0% | **+0.0%** | +19.9% | +136.6% |
| total DPS vs 70 prot per 1000g | 90 | **63** | **27** | 0 | -54.4% | -5.3% | **+13.5%** | +27.9% | +169.8% |
| total DPS vs 170 prot per 1000g | 90 | **61** | **28** | 1 | -53.8% | -7.1% | **+10.4%** | +28.3% | +166.8% |
| effective health, physical per 1000g | 90 | **28** | **62** | 0 | -41.1% | -11.4% | **-6.6%** | +8.9% | +147.4% |
| effective health, magical per 1000g | 90 | **33** | **57** | 0 | -42.0% | -11.9% | **-5.6%** | +10.1% | +164.9% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 15 / 2 / +27.5% | 16 / 2 / +19.4% | 5 / 0 / +0.0% | 5 / 0 / +0.0% |
| Jungle | 18 | 13 / 5 / +18.5% | 12 / 5 / +18.3% | 2 / 2 / +0.0% | 2 / 2 / +0.0% |
| Mid | 22 | 19 / 3 / +24.9% | 19 / 3 / +25.2% | 3 / 1 / +0.0% | 3 / 1 / +0.0% |
| Solo | 18 | 15 / 3 / +35.3% | 15 / 3 / +32.3% | 12 / 6 / +6.2% | 12 / 6 / +6.6% |
| Support | 14 | 7 / 5 / +1.6% | 7 / 5 / +1.6% | 14 / 0 / +30.5% | 14 / 0 / +36.1% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 13 / 5 / +19.4% | 12 / 5 / +9.5% | 2 / 16 / -9.1% | 2 / 16 / -9.1% |
| Jungle | 18 | 13 / 5 / +13.3% | 12 / 6 / +10.4% | 3 / 15 / -8.0% | 3 / 15 / -8.0% |
| Mid | 22 | 18 / 4 / +12.3% | 18 / 4 / +11.5% | 3 / 19 / -10.2% | 3 / 19 / -10.2% |
| Solo | 18 | 14 / 4 / +42.6% | 14 / 4 / +39.4% | 9 / 9 / -0.0% | 11 / 7 / +6.8% |
| Support | 14 | 5 / 9 / -10.8% | 5 / 9 / -10.8% | 11 / 3 / +17.5% | 14 / 0 / +18.6% |

Verdict on DPS vs 70 flips for 4 god(s) between §2 and §5: Achilles (+35.1 → -18.7), Aphrodite (-1.4 → +18.4), Hades (+31.9 → -16.4), Poseidon (+24.1 → -29.7).

## 6. The blind spot, measured

| | buildable pool | community slots | our `model` slots |
|---|---|---|---|
| items / slots | 138 | 543 | 540 |
| carrying unpriced passive text | 124 (89.9%) | 407 (75.0%) | 479 (88.7%) |
| mean gold residual per slot (cost − stat-line prediction) | – | -11g | -90g |
| mean stat columns per item | – | 2.75 | 3.41 |

Passives the shipped flags price (13): Book of Thoth, Brawler’s Beat Stick, Daybreak Gavel, Deathbringer, Eye of Erebus, Mercury's Talaria, Nimble Ring, Omen Drum, Rod of Tahuti, Sun Beam Bow, The Executioner, Transcendence, Vital Amplifier.

Most-bought blind items — community: Freya's Tears (27), Genji's Guard (26), Obsidian Shard (26), Shell of Rebuke (20), Shifter's Shield (19). Ours: Jotunn's Revenge (53), Kinetic Cuirass (37), Amanita Charm (36), Freya's Tears (31), Spear of Desolation (29).

## 7. Every god — `model` core, printed stat lines

C = community, O = ours. DPS vs 70 is shown as total (basic + ability).

| God | Role | Gold C / O | DPS vs 70 — C (basic+ability) | O (basic+ability) | Δ | DPS vs 170 — C | O | Δ | EHP phys — C | O | Δ | EHP mag — C | O | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Achilles | Solo Jungle | 14,400 / 14,600 | 178.7 (135.0+43.7) | 213.8 (166.1+47.7) | +19.6% | 121.6 | 133.1 | +9.5% | 6,742 | 9,039 | +34.1% | 7,559 | 9,283 | +22.8% |
| Agni | Mid | 15,400 / 16,600 | 217.1 (146.8+70.3) | 267.0 (183.2+83.7) | +23.0% | 142.3 | 173.4 | +21.9% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Ah Puch | Mid | 14,900 / 16,600 | 162.7 (120.8+41.8) | 225.1 (169.1+56.0) | +38.4% | 109.1 | 146.2 | +34.1% | 4,799 | 4,347 | -9.4% | 4,263 | 3,862 | -9.4% |
| Aladdin | Jungle | 13,550 / 15,900 | 109.2 (102.5+6.7) | 168.7 (160.4+8.3) | +54.5% | 71.6 | 106.2 | +48.5% | 4,233 | 4,233 | +0.0% | 3,846 | 3,846 | +0.0% |
| Amaterasu | Solo | 13,600 / 14,500 | 111.1 (92.6+18.5) | 132.0 (105.4+26.6) | +18.8% | 70.0 | 82.2 | +17.5% | 9,913 | 8,296 | -16.3% | 9,345 | 9,476 | +1.4% |
| Anhur | Carry | 13,550 / 15,150 | 398.9 (363.1+35.8) | 586.2 (524.2+61.9) | +46.9% | 263.7 | 364.5 | +38.2% | 4,148 | 4,493 | +8.3% | 3,644 | 3,947 | +8.3% |
| Anubis | Mid | 14,600 / 16,600 | 140.8 (119.6+21.2) | 195.5 (166.5+29.0) | +38.8% | 94.4 | 127.0 | +34.5% | 4,202 | 4,202 | +0.0% | 3,912 | 3,912 | +0.0% |
| Aphrodite | Mid Support | 13,050 / 15,350 | 131.5 (78.3+53.2) | 130.1 (82.4+47.7) | -1.1% | 80.9 | 81.0 | +0.0% | 5,615 | 7,029 | +25.2% | 5,450 | 8,258 | +51.5% |
| Apollo | Carry | 13,750 / 15,150 | 391.3 (357.9+33.4) | 569.9 (512.0+57.8) | +45.6% | 258.7 | 354.4 | +37.0% | 4,076 | 4,421 | +8.5% | 3,580 | 3,883 | +8.5% |
| Ares | Support | 13,350 / 14,750 | 60.3 (60.3+0.0) | 87.9 (87.9+0.0) | +45.8% | 37.9 | 54.7 | +44.2% | 10,036 | 10,187 | +1.5% | 10,178 | 11,383 | +11.8% |
| Artemis | Carry | 13,750 / 15,850 | 401.0 (378.5+22.5) | 659.5 (616.4+43.1) | +64.5% | 265.1 | 390.3 | +47.2% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Artio | Solo Support | 13,500 / 14,800 | 101.8 (58.3+43.5) | 171.5 (115.3+56.2) | +68.5% | 64.1 | 106.8 | +66.6% | 11,614 | 10,438 | -10.1% | 8,285 | 9,864 | +19.1% |
| Athena | Support | 12,900 / 14,750 | 117.6 (84.4+33.2) | 159.3 (122.6+36.6) | +35.4% | 74.0 | 99.2 | +33.9% | 9,640 | 10,187 | +5.7% | 8,198 | 11,383 | +38.8% |
| Atlas | Support | 13,200 / 14,750 | 100.9 (83.7+17.2) | 91.2 (72.9+18.2) | -9.6% | 63.5 | 57.4 | -9.6% | 8,842 | 11,736 | +32.7% | 9,126 | 11,503 | +26.0% |
| Awilix | Jungle | 16,250 / 16,650 | 401.2 (323.7+77.6) | 485.4 (350.9+134.5) | +21.0% | 266.8 | 320.9 | +20.2% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Bacchus | Support | 13,100 / 14,750 | 88.9 (60.3+28.7) | 124.7 (87.9+36.8) | +40.2% | 56.0 | 77.6 | +38.7% | 8,273 | 10,040 | +21.4% | 9,530 | 11,460 | +20.3% |
| Baron Samedi | Mid Support | 13,800 / 15,350 | 195.5 (82.4+113.1) | 176.1 (82.4+93.7) | -9.9% | 121.7 | 109.6 | -9.9% | 5,419 | 7,029 | +29.7% | 5,655 | 8,258 | +46.0% |
| Bastet | Jungle | 14,800 / 16,650 | 339.0 (281.7+57.2) | 417.2 (343.9+73.3) | +23.1% | 222.7 | 275.8 | +23.9% | 4,117 | 4,117 | +0.0% | 3,702 | 3,702 | +0.0% |
| Bellona | Solo | 15,200 / 14,800 | 342.2 (313.3+28.8) | 186.1 (142.6+43.5) | -45.6% | 220.4 | 115.9 | -47.4% | 8,410 | 10,251 | +21.9% | 7,466 | 9,475 | +26.9% |
| Cabrakan | Solo Support | 15,050 / 14,800 | 126.2 (63.3+62.9) | 187.2 (121.6+65.7) | +48.4% | 79.4 | 116.6 | +46.7% | 10,805 | 10,438 | -3.4% | 9,471 | 9,864 | +4.2% |
| Cerberus | Solo Support | 13,600 / 14,750 | 82.0 (52.2+29.8) | 86.4 (52.2+34.2) | +5.4% | 51.6 | 54.4 | +5.4% | 9,499 | 11,614 | +22.3% | 10,797 | 11,460 | +6.1% |
| Cernunnos | Carry Jungle | 13,700 / 15,650 | 447.0 (427.7+19.3) | 286.6 (250.3+36.4) | -35.9% | 295.5 | 173.9 | -41.2% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Chaac | Solo | 13,500 / 15,100 | 172.8 (92.5+80.4) | 199.5 (106.1+93.5) | +15.4% | 107.5 | 125.6 | +16.8% | 6,958 | 7,839 | +12.7% | 6,540 | 9,082 | +38.9% |
| Charon | Support | 15,450 / 14,750 | 142.6 (76.0+66.6) | 102.0 (55.4+46.5) | -28.5% | 90.8 | 64.2 | -29.3% | 6,418 | 11,614 | +81.0% | 6,116 | 11,383 | +86.1% |
| Chiron | Carry | 17,050 / 15,600 | 527.5 (444.8+82.7) | 627.1 (553.2+73.9) | +18.9% | 366.8 | 389.3 | +6.1% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Chronos | Mid Carry | 14,700 / 16,400 | 251.7 (153.6+98.1) | 339.9 (224.3+115.6) | +35.0% | 164.9 | 229.7 | +39.3% | 4,016 | 4,016 | +0.0% | 3,630 | 3,630 | +0.0% |
| Cu Chulainn | Solo | 15,300 / 14,550 | 132.6 (36.2+96.4) | 242.4 (130.3+112.1) | +82.8% | 83.5 | 150.9 | +80.8% | 11,911 | 10,282 | -13.7% | 10,396 | 7,901 | -24.0% |
| Cupid | Carry | 13,750 / 15,650 | 393.9 (376.5+17.4) | 293.6 (254.2+39.4) | -25.5% | 260.4 | 178.1 | -31.6% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Da Ji | Jungle | 14,450 / 16,100 | 338.8 (279.2+59.6) | 371.4 (303.0+68.4) | +9.6% | 228.0 | 258.3 | +13.3% | 3,865 | 3,865 | +0.0% | 3,452 | 3,452 | +0.0% |
| Danzaburou | Carry | 14,300 / 15,500 | 288.9 (186.0+102.9) | 431.9 (327.1+104.9) | +49.5% | 197.5 | 268.8 | +36.1% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Discordia | Mid | 15,350 / 16,600 | 221.2 (145.0+76.2) | 263.5 (172.8+90.7) | +19.1% | 143.1 | 171.2 | +19.6% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Eset | Mid | 14,700 / 16,600 | 236.7 (161.4+75.3) | 303.3 (206.2+97.2) | +28.1% | 153.2 | 197.0 | +28.7% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Fenrir | Jungle | 12,500 / 16,650 | 239.6 (195.0+44.6) | 434.3 (356.7+77.6) | +81.3% | 149.0 | 287.1 | +92.7% | 5,824 | 4,571 | -21.5% | 5,244 | 4,052 | -22.7% |
| Ganesha | Support | 13,150 / 14,750 | 99.2 (59.5+39.7) | 105.1 (59.5+45.6) | +5.9% | 62.5 | 66.2 | +5.9% | 8,708 | 11,613 | +33.4% | 8,968 | 11,383 | +26.9% |
| Geb | Support | 11,300 / 14,700 | 113.1 (58.3+54.8) | 103.7 (58.3+45.4) | -8.4% | 71.2 | 65.3 | -8.4% | 7,164 | 14,002 | +95.5% | 8,359 | 12,929 | +54.7% |
| Gilgamesh | Solo Jungle | 15,750 / 14,550 | 164.1 (132.8+31.2) | 244.9 (209.8+35.1) | +49.3% | 105.7 | 152.5 | +44.3% | 8,755 | 10,373 | +18.5% | 8,122 | 7,901 | -2.7% |
| Guan Yu | Solo Support | 14,900 / 14,500 | 120.9 (87.8+33.1) | 167.7 (135.9+31.9) | +38.7% | 76.1 | 104.4 | +37.2% | 8,131 | 9,611 | +18.2% | 7,994 | 9,611 | +20.2% |
| Hades | Solo | 15,200 / 15,950 | 175.2 (111.6+63.6) | 207.1 (118.4+88.7) | +18.2% | 114.8 | 135.7 | +18.2% | 6,184 | 6,732 | +8.9% | 5,577 | 6,298 | +12.9% |
| Hecate | Mid | 13,650 / 16,600 | 282.9 (134.9+148.0) | 364.7 (166.5+198.2) | +28.9% | 180.6 | 236.9 | +31.1% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Hercules | Solo | 15,050 / 14,800 | 130.1 (70.0+60.2) | 198.9 (136.6+62.4) | +52.8% | 81.9 | 123.9 | +51.1% | 8,548 | 9,783 | +14.4% | 8,386 | 9,254 | +10.4% |
| Horus | Support | 13,300 / 14,750 | 64.8 (61.2+3.6) | 94.0 (89.4+4.6) | +45.1% | 40.8 | 58.5 | +43.5% | 9,325 | 9,645 | +3.4% | 8,934 | 10,814 | +21.0% |
| Hou Yi | Carry | 13,800 / 15,400 | 416.0 (379.6+36.4) | 453.5 (386.8+66.7) | +9.0% | 275.0 | 285.5 | +3.8% | 4,076 | 4,076 | +0.0% | 3,580 | 3,580 | +0.0% |
| Hua Mulan | Solo | 13,400 / 14,550 | 108.1 (65.3+42.8) | 202.3 (152.5+49.7) | +87.2% | 68.0 | 125.9 | +85.1% | 10,263 | 10,432 | +1.6% | 9,333 | 8,380 | -10.2% |
| Hun Batz | Jungle | 16,350 / 16,650 | 389.5 (274.7+114.8) | 483.9 (346.4+137.5) | +24.3% | 255.8 | 319.9 | +25.0% | 4,233 | 4,233 | +0.0% | 3,752 | 3,752 | +0.0% |
| Ishtar | Carry | 13,650 / 15,600 | 421.6 (412.1+9.5) | 616.8 (604.5+12.3) | +46.3% | 278.7 | 388.4 | +39.3% | 3,861 | 4,203 | +8.9% | 3,416 | 3,719 | +8.9% |
| Ix Chel | Mid Support | 13,600 / 15,350 | 324.8 (132.5+192.3) | 223.1 (77.5+145.6) | -31.3% | 214.0 | 138.8 | -35.1% | 3,866 | 7,164 | +85.3% | 3,595 | 8,508 | +136.6% |
| Izanami | Carry | 13,500 / 15,500 | 376.3 (358.2+18.1) | 378.1 (324.6+53.4) | +0.5% | 242.5 | 235.3 | -3.0% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Janus | Mid | 14,700 / 16,600 | 245.6 (130.0+115.5) | 313.8 (166.5+147.3) | +27.8% | 158.9 | 203.8 | +28.3% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Jing Wei | Carry | 15,900 / 15,600 | 430.7 (408.5+22.2) | 641.6 (616.6+25.0) | +49.0% | 277.5 | 404.0 | +45.6% | 3,788 | 4,130 | +9.0% | 3,353 | 3,656 | +9.0% |
| Jormungandr | Solo Support | 15,650 / 14,550 | 145.2 (74.2+71.0) | 178.9 (108.0+70.9) | +23.2% | 91.4 | 111.4 | +21.8% | 8,783 | 10,772 | +22.6% | 8,261 | 8,849 | +7.1% |
| Kali | Jungle | 15,500 / 15,600 | 287.1 (260.6+26.5) | 355.1 (304.4+50.8) | +23.7% | 189.8 | 218.3 | +15.0% | 4,233 | 4,233 | +0.0% | 3,752 | 3,752 | +0.0% |
| Khepri | Support | 14,800 / 14,750 | 159.5 (99.8+59.6) | 99.8 (58.3+41.4) | -37.4% | 99.2 | 62.8 | -36.7% | 4,796 | 11,736 | +144.7% | 5,676 | 11,503 | +102.7% |
| Kukulkan | Mid | 15,150 / 16,600 | 207.9 (129.7+78.2) | 276.0 (166.5+109.5) | +32.8% | 136.2 | 179.3 | +31.7% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Loki | Jungle | 14,700 / 16,300 | 230.6 (213.2+17.4) | 323.7 (303.1+20.6) | +40.4% | 155.2 | 206.9 | +33.3% | 4,117 | 4,117 | +0.0% | 3,702 | 3,702 | +0.0% |
| Medusa | Carry | 13,550 / 15,500 | 379.8 (343.9+35.9) | 389.5 (313.1+76.5) | +2.6% | 251.0 | 242.4 | -3.4% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Mercury | Jungle | 15,850 / 16,050 | 569.3 (560.3+9.0) | 388.4 (372.3+16.1) | -31.8% | 358.5 | 255.1 | -28.8% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Merlin | Mid | 15,100 / 16,600 | 293.4 (127.0+166.5) | 360.8 (166.5+194.3) | +23.0% | 194.5 | 234.4 | +20.5% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Mordred | Solo Jungle | 15,050 / 15,150 | 104.1 (62.8+41.3) | 192.6 (137.4+55.1) | +85.0% | 65.5 | 121.2 | +85.0% | 10,866 | 8,443 | -22.3% | 9,797 | 7,919 | -19.2% |
| Morgan Le Fay | Mid | 15,350 / 16,600 | 222.0 (147.5+74.5) | 264.4 (175.6+88.8) | +19.1% | 143.7 | 171.7 | +19.6% | 4,015 | 4,015 | +0.0% | 3,630 | 3,630 | +0.0% |
| Ne Zha | Jungle | 15,100 / 16,100 | 478.6 (450.7+27.9) | 434.3 (397.8+36.5) | -9.3% | 322.0 | 302.0 | -6.2% | 4,233 | 4,233 | +0.0% | 3,752 | 3,752 | +0.0% |
| Neith | Carry Mid | 13,650 / 15,650 | 286.3 (167.4+118.9) | 385.2 (243.0+142.2) | +34.6% | 182.8 | 233.7 | +27.8% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Nemesis | Jungle | 15,950 / 15,800 | 339.0 (286.2+52.7) | 500.1 (457.8+42.3) | +47.5% | 222.7 | 314.8 | +41.4% | 5,075 | 4,233 | -16.6% | 4,594 | 3,752 | -18.3% |
| Nu Wa | Mid | 14,850 / 16,600 | 213.9 (146.5+67.4) | 282.3 (187.0+95.2) | +31.9% | 138.4 | 183.3 | +32.5% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Nut | Carry Mid | 13,800 / 16,300 | 314.3 (301.0+13.2) | 262.3 (233.6+28.7) | -16.5% | 207.7 | 175.1 | -15.7% | 4,045 | 4,045 | +0.0% | 3,580 | 3,580 | +0.0% |
| Odin | Solo Jungle | 13,250 / 14,500 | 135.0 (97.7+37.3) | 167.5 (131.6+35.9) | +24.1% | 84.1 | 104.3 | +24.1% | 8,161 | 8,443 | +3.5% | 7,964 | 9,595 | +20.5% |
| Osiris | Solo | 15,350 / 14,550 | 145.8 (76.7+69.1) | 299.5 (224.8+74.6) | +105.4% | 91.8 | 186.5 | +103.1% | 10,806 | 10,167 | -5.9% | 9,259 | 7,735 | -16.5% |
| Pele | Jungle | 15,600 / 16,100 | 337.8 (332.3+5.5) | 291.9 (284.6+7.3) | -13.6% | 212.7 | 203.0 | -4.6% | 4,307 | 4,307 | +0.0% | 3,817 | 3,817 | +0.0% |
| Poseidon | Mid | 14,900 / 16,600 | 240.0 (179.1+60.8) | 264.1 (182.2+81.8) | +10.0% | 153.2 | 171.5 | +11.9% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Princess Bari | Carry Mid | 15,000 / 15,650 | 189.8 (135.9+53.9) | 372.8 (321.9+50.9) | +96.4% | 122.8 | 234.7 | +91.1% | 4,046 | 4,046 | +0.0% | 3,745 | 3,745 | +0.0% |
| Ra | Mid | 15,200 / 16,300 | 281.6 (147.8+133.8) | 316.1 (150.9+165.1) | +12.2% | 177.3 | 211.0 | +19.0% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Rama | Carry | 13,750 / 16,100 | 380.7 (376.5+4.2) | 560.7 (553.1+7.6) | +47.3% | 251.7 | 339.4 | +34.8% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Ratatoskr | Jungle | 14,700 / 14,300 | 347.7 (291.3+56.4) | 350.7 (279.0+71.8) | +0.9% | 231.2 | 223.8 | -3.2% | 6,419 | 6,419 | +0.0% | 5,689 | 5,689 | +0.0% |
| Ravana | Jungle | 17,300 / 14,700 | 440.9 (308.8+132.1) | 212.5 (128.0+84.5) | -51.8% | 299.4 | 132.3 | -55.8% | 4,559 | 9,584 | +110.2% | 3,986 | 8,974 | +125.1% |
| Scylla | Mid | 14,450 / 16,600 | 241.0 (126.3+114.7) | 332.4 (166.5+165.9) | +37.9% | 157.9 | 216.0 | +36.7% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Sobek | Support | 12,850 / 14,750 | 111.1 (60.3+50.8) | 114.6 (60.3+54.3) | +3.2% | 69.9 | 72.1 | +3.2% | 8,177 | 11,475 | +40.3% | 8,129 | 11,247 | +38.4% |
| Sol | Mid Carry | 14,450 / 16,400 | 230.6 (204.8+25.9) | 277.1 (244.6+32.5) | +20.1% | 155.9 | 187.2 | +20.1% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Sun Wukong | Solo | 13,400 / 14,500 | 61.6 (56.9+4.7) | 179.8 (174.6+5.2) | +191.9% | 38.8 | 112.0 | +188.7% | 9,952 | 10,159 | +2.1% | 9,147 | 7,857 | -14.1% |
| Susano | Jungle | 14,150 / 16,650 | 273.5 (248.0+25.5) | 431.6 (382.9+48.6) | +57.8% | 172.2 | 285.3 | +65.6% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Sylvanus | Support | 12,950 / 14,750 | 71.2 (47.6+23.6) | 71.2 (47.6+23.6) | +0.0% | 44.8 | 44.8 | +0.0% | 9,425 | 11,736 | +24.5% | 8,301 | 11,503 | +38.6% |
| Thanatos | Jungle | 14,050 / 16,650 | 326.8 (244.6+82.2) | 494.6 (372.5+122.0) | +51.3% | 203.2 | 326.9 | +60.9% | 4,655 | 4,655 | +0.0% | 4,126 | 4,126 | +0.0% |
| The Morrigan | Mid | 14,900 / 16,600 | 180.6 (142.2+38.5) | 245.7 (185.1+60.6) | +36.0% | 118.3 | 159.6 | +34.9% | 3,894 | 3,894 | +0.0% | 3,452 | 3,452 | +0.0% |
| Thor | Jungle Solo | 14,300 / 14,600 | 266.8 (227.7+39.1) | 199.4 (172.4+27.0) | -25.3% | 179.5 | 124.2 | -30.8% | 4,559 | 9,019 | +97.8% | 5,392 | 9,486 | +75.9% |
| Tsukuyomi | Jungle | 14,250 / 15,800 | 262.3 (234.8+27.5) | 487.9 (453.8+34.1) | +86.0% | 178.5 | 307.2 | +72.1% | 4,307 | 4,307 | +0.0% | 3,766 | 3,766 | +0.0% |
| Ullr | Carry | 14,350 / 15,300 | 353.7 (255.5+98.2) | 584.3 (496.1+88.2) | +65.2% | 238.0 | 353.7 | +48.6% | 4,148 | 4,148 | +0.0% | 3,644 | 3,644 | +0.0% |
| Vulcan | Mid | 13,500 / 16,600 | 267.2 (122.0+145.2) | 355.9 (186.0+169.8) | +33.2% | 172.9 | 234.4 | +35.6% | 4,015 | 4,015 | +0.0% | 3,630 | 3,630 | +0.0% |
| Xbalanque | Carry | 13,700 / 15,600 | 392.9 (377.6+15.3) | 641.4 (621.2+20.2) | +63.2% | 253.1 | 403.8 | +59.5% | 3,788 | 4,130 | +9.0% | 3,353 | 3,656 | +9.0% |
| Xing Tian | Support Solo | 13,350 / 14,750 | 20.8 (0.0+20.8) | 23.9 (0.0+23.9) | +14.8% | 13.1 | 15.0 | +14.8% | 1,754 | 2,250 | +28.3% | 1,962 | 2,385 | +21.5% |
| Yemoja | Support | 13,950 / 14,750 | 92.1 (87.4+4.8) | 61.8 (57.7+4.0) | -33.0% | 57.3 | 38.9 | -32.2% | 7,697 | 11,912 | +54.8% | 6,681 | 11,675 | +74.7% |
| Ymir | Support | 13,050 / 14,750 | 118.6 (63.3+55.3) | 118.6 (63.3+55.3) | +0.0% | 74.7 | 74.7 | +0.0% | 9,741 | 12,300 | +26.3% | 10,017 | 13,401 | +33.8% |
| Zeus | Mid | 15,300 / 16,600 | 247.4 (147.4+100.0) | 325.7 (208.0+117.7) | +31.7% | 158.0 | 214.6 | +35.8% | 3,894 | 3,894 | +0.0% | 3,452 | 3,452 | +0.0% |
