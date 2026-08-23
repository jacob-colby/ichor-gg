# Build quality — `combat.py` pointed at whole builds

_Input fingerprint: `527eb8f0a586` — items, gods, tags, community builds, weights. Regenerate with `python -m smite.build_quality`; a different fingerprint means different inputs._

> **READ THIS BEFORE ANY NUMBER BELOW.** Of the 138 buildable items, 137 carry passive text and the shipped pricing flags read 13 of them — so **90% of the pool carries passive value this arithmetic cannot see**, and **77% of the community's item slots do** (412 of 537; 89% of ours, 473 of 534). `combat.py` reads exactly one passive — Deathbringer's +35% crit damage. The bias is not even: by the gold model's own residual the community pays **+93g more per slot above its stat line than we do** (mean residual +3g against -89g) and buys fewer stat columns per item (2.79 against 3.41) — that premium IS the passive. **A verdict in our favour is the one to distrust.** The most-bought blind community items are Genji's Guard (30), Shifter's Shield (27), Obsidian Shard (26), Shell of Rebuke (25), Spear of Desolation (23).

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

**community** — 13,750g: Tyrfing · Odysseus' Bow · Riptalon · Silverbranch Bow · The Executioner · Manchu Bow
  stat line: Attack Damage 80 · Attack Speed % 133 · Lifesteal % 7.5 · Penetration % 20 · Strength 25
  abilities counted: Acid Spray, Lacerate, Petrify

**ours** — 15,500g: Lernaean Bow · Jotunn's Revenge · Nimble Ring · Death Metal · Rod of Tahuti · Soul Gem
  stat line: Attack Speed % 50 · Cooldown Rate 35 · Critical Chance % 20 · Intelligence 215 · Lifesteal % 15 · Mana Regen 2 · Max Mana 500 · Penetration 10 · Penetration % 5 · Strength 110
  abilities counted: Acid Spray, Lacerate, Petrify

| | basic DPS | ability DPS | TOTAL | EHP physical | EHP magical |
|---|---|---|---|---|---|
| COMMUNITY vs squishy (70) | 352.8 | 35.9 | **388.6** | 3,788 | 3,353 |
| COMMUNITY vs tank (170) | 233.2 | 23.7 | **256.9** | 3,788 | 3,353 |
| OURS vs squishy (70) | 313.1 | 76.5 | **389.5** | 3,788 | 3,353 |
| OURS vs tank (170) | 194.8 | 47.6 | **242.4** | 3,788 | 3,353 |

| per 1000g | DPS vs 70 | DPS vs 170 | EHP physical | EHP magical |
|---|---|---|---|---|
| COMMUNITY | 28.3 | 18.7 | 275 | 244 |
| OURS | 25.1 | 15.6 | 244 | 216 |

## 2. The roster — our `model` core, printed stat lines

89 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 89 | **71** | **13** | 5 | -49.0% | +7.4% | **+27.8%** | +45.8% | +132.1% |
| total DPS vs 170 prot | 89 | **71** | **15** | 3 | -48.3% | +6.8% | **+27.7%** | +44.2% | +128.4% |
| effective health, physical | 89 | **30** | **17** | 42 | -31.7% | +0.0% | **+0.0%** | +9.0% | +226.1% |
| effective health, magical | 89 | **33** | **17** | 39 | -35.3% | +0.0% | **+0.0%** | +9.0% | +224.5% |
| total DPS vs 70 prot per 1000g | 89 | **62** | **26** | 1 | -47.4% | -5.0% | **+20.1%** | +32.8% | +135.7% |
| total DPS vs 170 prot per 1000g | 89 | **64** | **25** | 0 | -46.8% | -2.8% | **+17.3%** | +30.5% | +133.1% |
| effective health, physical per 1000g | 89 | **26** | **61** | 2 | -32.9% | -11.4% | **-7.6%** | +1.6% | +194.0% |
| effective health, magical per 1000g | 89 | **29** | **58** | 2 | -40.3% | -11.3% | **-6.7%** | +5.4% | +192.6% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 14 / 3 / +40.3% | 13 / 5 / +34.1% | 5 / 1 / +0.0% | 5 / 1 / +0.0% |
| Jungle | 17 | 13 / 3 / +26.9% | 14 / 3 / +25.0% | 2 / 4 / +0.0% | 2 / 4 / +0.0% |
| Mid | 22 | 19 / 2 / +24.0% | 19 / 2 / +25.4% | 3 / 2 / +0.0% | 3 / 3 / +0.0% |
| Solo | 18 | 18 / 0 / +58.3% | 18 / 0 / +56.6% | 6 / 10 / -3.2% | 9 / 9 / +1.4% |
| Support | 14 | 7 / 5 / +3.0% | 7 / 5 / +3.0% | 14 / 0 / +39.1% | 14 / 0 / +36.5% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 12 / 5 / +28.2% | 12 / 6 / +22.3% | 2 / 15 / -8.9% | 2 / 15 / -8.9% |
| Jungle | 17 | 13 / 4 / +23.1% | 13 / 4 / +20.2% | 3 / 14 / -8.4% | 3 / 14 / -8.4% |
| Mid | 22 | 17 / 5 / +9.8% | 19 / 3 / +12.4% | 3 / 19 / -9.2% | 3 / 19 / -9.3% |
| Solo | 18 | 16 / 2 / +47.3% | 16 / 2 / +45.6% | 7 / 11 / -3.9% | 8 / 9 / -1.2% |
| Support | 14 | 4 / 10 / -8.8% | 4 / 10 / -8.8% | 11 / 2 / +22.8% | 13 / 1 / +19.9% |

## 3. Judged by role, on each role's own objective

Most roles clear a THRESHOLD and then maximise something else, and one pooled metric cannot represent five roles that do not share an objective. Each row below names both quantities. **The passive blind spot at the top of this report applies to every row here exactly as it applies to the pooled figures** — slicing by role does not escape it, and the bias still runs in our favour.

**An objective containing effective health is scored on BOTH damage channels and read as the interval between them.** A build has one damage output and two effective healths; which one its survival is read on is a property of the ATTACKER, and there is no attacker in this comparison. Against a stream that is a share `f` physical, effective health is `1 / (f/EHP_p + (1-f)/EHP_m)` — a weighted harmonic mean, because what averages over a mixed stream is the damage-taken multiplier and not its reciprocal — and the ours-over-theirs ratio is monotone in `f`, so **every possible damage mix lands between the two channels and the pair is the whole range**. `ahead` below therefore means ahead at every mix, `behind` means behind at every mix, and `mix-dependent` means the answer is a fact about the enemy team that this comparison does not contain. Averaging the two channels would assert equal exposure, which is a constant no source here supplies — and would not even be the answer to its own question, since the correct collapse at 50/50 is harmonic and not arithmetic. Until 2026-08-23 both roles read `ehp_physical` alone, i.e. the two roles whose job is durability were scored on half the damage in the game.

| Role | n | Threshold | Binds? | Maximised | ahead | behind | level | mix-dependent | median |
|---|---|---|---|---|---|---|---|---|---|
| Carry | 18 | survive one enemy burst rotation | **no** — 0 of 36 builds fail it | sustained DPS per 1000g | **12** | **5** | 1 | – (no EHP term) | **+28.2%** |
| Jungle | 17 | rotation burst >= a reference squishy's EHP | **no** — all 78 builds fail it | rotation burst per 1000g | **12** | **5** | 0 | – (no EHP term) | **+10.3%** |
| Mid | 22 | rotation burst >= a reference squishy's EHP | **no** — all 78 builds fail it | sustained DPS per 1000g | **17** | **5** | 0 | – (no EHP term) | **+9.8%** |
| Solo | 18 | **none** | – | duel score, EHP x DPS | **17** | **0** | 0 | **1** | **+54.6% … +55.0%** |
| Support | 14 | **none** | – | effective health per 1000g | **11** | **1** | 1 | **1** | **+19.9% … +22.8%** |

Builds whose verdict the damage mix decides — the interval spans both answers, so neither is available here:

- **Amaterasu** (Solo) — vs a physical opponent -11.5% · vs a magical opponent +28.5%
- **Ares** (Support) — vs a physical opponent -10.4% · vs a magical opponent +15.3%

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
| Mid / Jungle: rotation burst >= a reference squishy's EHP | 78 builds | median effective health of the community's own Carry and Mid builds, on the channel each attacker's own damage type reads — physical 3,788 / magical 3,399 | **78 of 78** | 0.72x the threshold |

A threshold that separates none of the population and a threshold that separates all of it are equally useless, and one of each is what these are. **Read this as "we cannot currently evaluate a threshold", not as "thresholds do not matter in SMITE"** — the cause is on our side of the arithmetic. A burst here is one cast of every ability with no basic attacks, no item passive, no follow-up and one target, while effective health is full level-20 health plus every protection the six items carry; the two are about an order of magnitude apart. Two things would change the answer and neither is a tuning choice: **a clock** (register §4.12 — a burst window in seconds would let basic attacks into the burst, and it is refused because no source supplies one), or **priced passives** (register §4.5 — ~90% of the pool carries value neither side of this comparison can see). Until one of those exists, Carry, Mid and Jungle are judged on their maximand alone.

### Where the Carry surplus comes from — measured, and currently closed

This section describes a defect that is **not currently present**: our Carry cores buy no more Physical Protection than the community's. It re-measures on every run rather than asserting that, so a refresh or a weight change that brings the surplus back restores the diagnosis in the same paragraph. `offmap_efficiency` is the flag that closed it — see docs/STATE.md §4.15.

Mean defensive stats bought at level 20, community (C) against our `model` core (O):

| Role | n | Physical Protection C / O | Magical Protection C / O | Max Health C / O |
|---|---|---|---|---|
| Carry | 18 | 0.0 / 0.0 | 0.0 / 0.0 | 27.8 / 55.6 |
| Jungle | 17 | 8.8 / 3.8 | 9.1 / 5.9 | 100.0 / 138.2 |
| Mid | 22 | 7.0 / 10.9 | 13.0 / 19.1 | 24.5 / 81.8 |
| Solo | 18 | 124.3 / 104.4 | 118.9 / 107.2 | 731.9 / 894.4 |
| Support | 14 | 86.1 / 137.1 | 115.4 / 166.1 | 405.4 / 953.6 |

The community buys 0.0 Physical Protection across all 18 Carries and we buy 0.0, a surplus of +0.0. The defensive items still reaching a Carry core, with how many of ours hold each against how many of the community's — an EMPTY list here is the measurement, not a missing section:

- **Golden Blade** — ours 5 of 18, community 0 of 18 (Max Health 200)

Two things worth keeping now that the surplus is gone. Effective health is the quantity to read it on, and it is +0.0% physical and +0.0% magical against the community's — LEVEL is the honest target here, not zero, because §4.13 means no threshold in this report can charge us for buying too LITTLE defence, so a figure BELOW the community's would not be visible as a cost. And `defense_affinity` and `draft.archetype_scaled_stats` are **excluded as causes**: both are read only by the viewer's draft overlay (`viewer/src/lib/threats.ts`), which is applied on top of a finished core and never reaches the builds measured here, and `defense_affinity` is 0.0 for Carry in any case because it is derived from the same role map that names no protection for the role. See docs/STATE.md §4.

### Where the off-map charge lands — measured on every run

`offmap_efficiency` ships at **0.55** and charges an item for the gold it spent on stats the god's fit map does not name (STATE.md §3, §4.15). This is what that bill is made of in our own cores, at full strength — the charge is linear in the strength, so the shipped value scales every row equally. **Nothing here changes a build**; it is here because every attempt on this charge so far has had to rebuild the composition by hand against a dataset that had moved under the previous one.

| Role | n | off-map gold in our cores | largest lines |
|---|---|---|---|
| Carry | 18 | 1,371g | Max Health 100.0% |
| Jungle | 17 | 9,185g | Echo 47.0%, Lifesteal 22.7%, Max Health 17.9%, Attack Speed 5.7%, Tenacity 3.9% |
| Mid | 22 | 4,967g | Lifesteal 87.6%, Plating 12.4% |
| Solo | 18 | 3,964g | Plating 93.1%, Lifesteal 6.9% |
| Support | 14 | 2,871g | Plating 100.0% |

And what the two mechanical tests of §4.16 say about each stat being billed. A stat named by SOME role map has a CONTRAST, so another role's silence about it is a positive statement by the same table and charging it is legitimate; a stat named NOWHERE has no contrast to read. The second column is test (ii) — if `combat.py` can see the stat then charging it is a hypothesis this report can check, which is why it may not simply be exempted.

| Stat | named by `role_stats` | `combat.py` | on `offmap_exempt` |
|---|---|---|---|
| Plating | 0 of 21 — **nowhere** | flat_reduction_multiplier | no |
| Lifesteal | 3 of 21 (Carry, Hunter, Sharpshooter) | LIFESTEAL_MINION_SCALE | no |
| Echo | 0 of 21 — **nowhere** | echo_multiplier | no |
| Max Health | 6 of 21 (Brawler, Guardian, Solo, Support, Tank, Warrior) | effective_health | no |
| Attack Speed | 5 of 21 (Carry, Constant, Hunter, Pressure, Sharpshooter) | attack_dps | no |
| Tenacity | 0 of 21 — **nowhere** | TENACITY_CAP | no |
| Pathfinding | 0 of 21 — **nowhere** | PATHFINDING_COMBAT_SCALE | no |

**No verdict is drawn here**, and that is deliberate: deciding whether a line in the first table is a defect needs the community's own record and the leakage-free coverage gate as well, and both live outside this module. The verdicts reached so far are register §4.15 (the defect stats — charge them), §4.16 (mana and the regens — exempt them) and §4.18 (Echo — charge it, and why the role that pays most for it is not being wronged).

## 4. The same, for the blended `core` (what the Balanced tab ships)

`core` carries `win` and `pick`, so it is part community build already; the gap between this block and §2 is what the meta signal buys in this arithmetic.

89 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 89 | **70** | **17** | 2 | -41.9% | +4.4% | **+20.7%** | +41.5% | +95.8% |
| total DPS vs 170 prot | 89 | **71** | **16** | 2 | -43.3% | +3.9% | **+21.0%** | +39.9% | +92.2% |
| effective health, physical | 89 | **33** | **16** | 40 | -47.1% | +0.0% | **+0.0%** | +12.3% | +291.7% |
| effective health, magical | 89 | **31** | **18** | 40 | -35.3% | +0.0% | **+0.0%** | +12.3% | +345.9% |
| total DPS vs 70 prot per 1000g | 89 | **61** | **27** | 1 | -44.4% | -7.1% | **+11.3%** | +29.4% | +108.4% |
| total DPS vs 170 prot per 1000g | 89 | **63** | **26** | 0 | -45.8% | -3.2% | **+10.8%** | +28.9% | +101.2% |
| effective health, physical per 1000g | 89 | **29** | **57** | 3 | -53.1% | -11.5% | **-6.3%** | +4.2% | +253.2% |
| effective health, magical per 1000g | 89 | **30** | **58** | 1 | -37.8% | -12.4% | **-6.8%** | +3.9% | +302.1% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 16 / 2 / +37.8% | 15 / 3 / +32.7% | 5 / 1 / +0.0% | 5 / 1 / +0.0% |
| Jungle | 17 | 13 / 4 / +14.2% | 13 / 4 / +10.0% | 2 / 4 / +0.0% | 2 / 4 / +0.0% |
| Mid | 22 | 18 / 4 / +16.8% | 20 / 2 / +19.1% | 3 / 2 / +0.0% | 3 / 3 / +0.0% |
| Solo | 18 | 18 / 0 / +49.7% | 18 / 0 / +48.8% | 9 / 9 / +0.5% | 8 / 9 / -3.8% |
| Support | 14 | 5 / 7 / -2.1% | 5 / 7 / -2.1% | 14 / 0 / +45.4% | 13 / 1 / +41.7% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 15 / 3 / +20.1% | 15 / 3 / +15.6% | 3 / 15 / -9.7% | 3 / 15 / -9.7% |
| Jungle | 17 | 12 / 5 / +11.3% | 12 / 5 / +5.7% | 4 / 12 / -7.7% | 4 / 12 / -7.7% |
| Mid | 22 | 14 / 7 / +2.3% | 16 / 6 / +5.5% | 3 / 19 / -9.0% | 3 / 19 / -9.0% |
| Solo | 18 | 16 / 2 / +45.2% | 16 / 2 / +47.0% | 6 / 11 / -4.3% | 8 / 10 / -5.4% |
| Support | 14 | 4 / 10 / -14.7% | 4 / 10 / -14.7% | 13 / 0 / +26.8% | 12 / 2 / +23.6% |

## 5. Sensitivity — the passives the gold model CAN price

Same as §2 with the shipped pricing flags applied to every stat line: the Adaptive Stat grants (`price_adaptive`) and the mana conversions (`price_conversions`). This is the one slice of the blind spot that can be put on the table; the other 124 items stay invisible here too.

89 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 89 | **71** | **15** | 3 | -61.7% | +7.4% | **+24.0%** | +45.1% | +132.1% |
| total DPS vs 170 prot | 89 | **72** | **14** | 3 | -61.3% | +6.5% | **+22.6%** | +44.2% | +128.4% |
| effective health, physical | 89 | **30** | **17** | 42 | -31.7% | +0.0% | **+0.0%** | +9.0% | +226.1% |
| effective health, magical | 89 | **33** | **17** | 39 | -35.3% | +0.0% | **+0.0%** | +9.0% | +224.5% |
| total DPS vs 70 prot per 1000g | 89 | **63** | **26** | 0 | -60.6% | -2.8% | **+15.2%** | +29.0% | +135.7% |
| total DPS vs 170 prot per 1000g | 89 | **64** | **23** | 2 | -60.1% | -2.8% | **+14.2%** | +28.3% | +133.1% |
| effective health, physical per 1000g | 89 | **26** | **61** | 2 | -32.9% | -11.4% | **-7.6%** | +1.6% | +194.0% |
| effective health, magical per 1000g | 89 | **29** | **58** | 2 | -40.3% | -11.3% | **-6.7%** | +5.4% | +192.6% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 15 / 3 / +27.0% | 15 / 3 / +18.6% | 5 / 1 / +0.0% | 5 / 1 / +0.0% |
| Jungle | 17 | 14 / 3 / +21.2% | 15 / 2 / +21.5% | 2 / 4 / +0.0% | 2 / 4 / +0.0% |
| Mid | 22 | 18 / 3 / +22.7% | 18 / 3 / +22.9% | 3 / 2 / +0.0% | 3 / 3 / +0.0% |
| Solo | 18 | 17 / 1 / +58.3% | 17 / 1 / +56.6% | 6 / 10 / -3.2% | 9 / 9 / +1.4% |
| Support | 14 | 7 / 5 / +3.0% | 7 / 5 / +3.0% | 14 / 0 / +39.1% | 14 / 0 / +36.5% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 13 / 5 / +17.9% | 12 / 5 / +10.9% | 2 / 15 / -8.9% | 2 / 15 / -8.9% |
| Jungle | 17 | 13 / 4 / +16.4% | 15 / 2 / +14.8% | 3 / 14 / -8.4% | 3 / 14 / -8.4% |
| Mid | 22 | 18 / 4 / +9.0% | 18 / 4 / +10.8% | 3 / 19 / -9.2% | 3 / 19 / -9.3% |
| Solo | 18 | 15 / 3 / +47.3% | 15 / 2 / +45.6% | 7 / 11 / -3.9% | 8 / 9 / -1.2% |
| Support | 14 | 4 / 10 / -8.8% | 4 / 10 / -8.8% | 11 / 2 / +22.8% | 13 / 1 / +19.9% |

Verdict on DPS vs 70 flips for 3 god(s) between §2 and §5: Hades (+23.6 → -23.1), Pele (-0.8 → +12.8), Poseidon (+20.9 → -33.5).

## 6. The blind spot, measured

| | buildable pool | community slots | our `model` slots |
|---|---|---|---|
| items / slots | 138 | 537 | 534 |
| carrying unpriced passive text | 124 (89.9%) | 412 (76.7%) | 473 (88.6%) |
| mean gold residual per slot (cost − stat-line prediction) | – | +3g | -89g |
| mean stat columns per item | – | 2.79 | 3.41 |

Passives the shipped flags price (13): Book of Thoth, Brawler’s Beat Stick, Daybreak Gavel, Deathbringer, Eye of Erebus, Mercury's Talaria, Nimble Ring, Omen Drum, Rod of Tahuti, Sun Beam Bow, The Executioner, Transcendence, Vital Amplifier.

Most-bought blind items — community: Genji's Guard (30), Shifter's Shield (27), Obsidian Shard (26), Shell of Rebuke (25), Spear of Desolation (23). Ours: Jotunn's Revenge (52), Kinetic Cuirass (36), Amanita Charm (35), Freya's Tears (30), Spear of Desolation (29).

## 7. Every god — `model` core, printed stat lines

C = community, O = ours. DPS vs 70 is shown as total (basic + ability).

| God | Role | Gold C / O | DPS vs 70 — C (basic+ability) | O (basic+ability) | Δ | DPS vs 170 — C | O | Δ | EHP phys — C | O | Δ | EHP mag — C | O | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Achilles | Solo Jungle | 14,900 / 14,600 | 92.6 (57.6+35.0) | 213.8 (166.1+47.7) | +131.0% | 58.3 | 133.1 | +128.4% | 11,377 | 9,039 | -20.6% | 10,182 | 9,283 | -8.8% |
| Agni | Mid | 15,650 / 16,600 | 229.8 (161.8+68.0) | 267.0 (183.2+83.7) | +16.2% | 146.7 | 173.4 | +18.2% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Ah Puch | Mid | 15,650 / 16,600 | 180.8 (132.7+48.1) | 225.1 (169.1+56.0) | +24.5% | 118.4 | 146.2 | +23.4% | 4,347 | 4,347 | +0.0% | 3,862 | 3,862 | +0.0% |
| Aladdin | Jungle | 13,550 / 15,900 | 109.2 (102.5+6.7) | 168.7 (160.4+8.3) | +54.5% | 71.6 | 106.2 | +48.5% | 4,233 | 4,233 | +0.0% | 3,846 | 3,846 | +0.0% |
| Amaterasu | Solo | 12,700 / 14,500 | 122.3 (108.1+14.2) | 132.0 (105.4+26.6) | +8.0% | 77.0 | 82.2 | +6.8% | 10,118 | 8,296 | -18.0% | 7,960 | 9,476 | +19.1% |
| Anhur | Carry | 13,750 / 15,150 | 407.2 (371.4+35.8) | 586.2 (524.2+61.9) | +43.9% | 269.2 | 364.5 | +35.4% | 4,148 | 4,493 | +8.3% | 3,644 | 3,947 | +8.3% |
| Anubis | Mid | 15,000 / 16,600 | 148.9 (125.4+23.5) | 195.5 (166.5+29.0) | +31.3% | 97.6 | 127.0 | +30.2% | 4,202 | 4,202 | +0.0% | 3,912 | 3,912 | +0.0% |
| Aphrodite | Mid Support | 14,150 / 15,350 | 159.1 (97.1+62.0) | 130.1 (82.4+47.7) | -18.2% | 99.0 | 81.0 | -18.2% | 4,755 | 7,029 | +47.8% | 4,615 | 8,258 | +78.9% |
| Apollo | Carry | 13,750 / 15,150 | 391.3 (357.9+33.4) | 569.9 (512.0+57.8) | +45.6% | 258.7 | 354.4 | +37.0% | 4,076 | 4,421 | +8.5% | 3,580 | 3,883 | +8.5% |
| Ares | Support | 12,800 / 14,750 | 60.3 (60.3+0.0) | 87.9 (87.9+0.0) | +45.8% | 37.9 | 54.7 | +44.2% | 9,868 | 10,187 | +3.2% | 8,565 | 11,383 | +32.9% |
| Artemis | Carry | 13,700 / 15,850 | 401.1 (379.6+21.6) | 659.5 (616.4+43.1) | +64.4% | 258.4 | 390.3 | +51.0% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Artio | Solo Support | 13,200 / 14,800 | 100.3 (58.3+42.0) | 171.5 (115.3+56.2) | +71.1% | 63.1 | 106.8 | +69.2% | 10,420 | 10,438 | +0.2% | 8,349 | 9,864 | +18.1% |
| Athena | Support | 13,300 / 14,750 | 117.6 (84.4+33.2) | 159.3 (122.6+36.6) | +35.4% | 74.0 | 99.2 | +33.9% | 9,164 | 10,187 | +11.2% | 8,851 | 11,383 | +28.6% |
| Atlas | Support | 13,350 / 14,750 | 100.9 (83.7+17.2) | 91.2 (72.9+18.2) | -9.6% | 63.5 | 57.4 | -9.6% | 8,661 | 11,736 | +35.5% | 9,955 | 11,503 | +15.5% |
| Awilix | Jungle | 15,550 / 16,650 | 318.4 (252.7+65.8) | 485.4 (350.9+134.5) | +52.4% | 200.5 | 320.9 | +60.0% | 4,959 | 4,117 | -17.0% | 4,594 | 3,752 | -18.3% |
| Bacchus | Support | 13,300 / 14,750 | 88.9 (60.3+28.7) | 124.7 (87.9+36.8) | +40.2% | 56.0 | 77.6 | +38.7% | 9,339 | 10,040 | +7.5% | 10,637 | 11,460 | +7.7% |
| Baron Samedi | Mid Support | 13,700 / 15,350 | 176.1 (82.4+93.7) | 176.1 (82.4+93.7) | +0.0% | 109.6 | 109.6 | +0.0% | 5,762 | 7,029 | +22.0% | 5,607 | 8,258 | +47.3% |
| Bastet | Jungle | 15,050 / 16,650 | 344.1 (286.4+57.8) | 417.2 (343.9+73.3) | +21.2% | 226.0 | 275.8 | +22.0% | 4,117 | 4,117 | +0.0% | 3,702 | 3,702 | +0.0% |
| Bellona | Solo | 13,700 / 14,800 | 142.6 (117.1+25.4) | 186.1 (142.6+43.5) | +30.5% | 89.8 | 115.9 | +29.1% | 10,730 | 10,251 | -4.5% | 9,758 | 9,475 | -2.9% |
| Cabrakan | Solo Support | 13,250 / 14,800 | 118.1 (63.3+54.8) | 187.2 (121.6+65.7) | +58.6% | 74.3 | 116.6 | +56.8% | 10,164 | 10,438 | +2.7% | 8,670 | 9,864 | +13.8% |
| Cerberus | Solo Support | 13,600 / 14,750 | 82.0 (52.2+29.8) | 86.4 (52.2+34.2) | +5.4% | 51.6 | 54.4 | +5.4% | 9,499 | 11,614 | +22.3% | 10,797 | 11,460 | +6.1% |
| Cernunnos | Carry Jungle | 13,900 / 15,650 | 359.9 (340.1+19.8) | 286.6 (250.3+36.4) | -20.3% | 237.9 | 173.9 | -26.9% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Chaac | Solo | 13,250 / 15,100 | 142.8 (62.8+80.1) | 199.5 (106.1+93.5) | +39.7% | 89.9 | 125.6 | +39.7% | 9,203 | 7,839 | -14.8% | 8,342 | 9,082 | +8.9% |
| Charon | Support | 14,500 / 14,750 | 139.5 (79.3+60.2) | 102.0 (55.4+46.5) | -26.9% | 91.0 | 64.2 | -29.5% | 6,000 | 11,614 | +93.6% | 6,968 | 11,383 | +63.4% |
| Chiron | Carry | 13,800 / 15,600 | 320.6 (264.6+56.0) | 627.1 (553.2+73.9) | +95.6% | 204.3 | 389.3 | +90.6% | 4,644 | 3,788 | -18.4% | 4,110 | 3,353 | -18.4% |
| Chronos | Mid Carry | 14,700 / 16,400 | 251.7 (153.6+98.1) | 339.9 (224.3+115.6) | +35.0% | 164.9 | 229.7 | +39.3% | 4,016 | 4,016 | +0.0% | 3,630 | 3,630 | +0.0% |
| Cu Chulainn | Solo | 15,200 / 14,550 | 136.3 (36.2+100.1) | 242.4 (130.3+112.1) | +77.9% | 85.8 | 150.9 | +75.9% | 11,237 | 10,282 | -8.5% | 9,956 | 7,901 | -20.6% |
| Cupid | Carry | 13,550 / 15,650 | 385.1 (367.8+17.4) | 293.6 (254.2+39.4) | -23.8% | 254.6 | 178.1 | -30.0% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Da Ji | Jungle | 16,250 / 16,100 | 401.5 (329.3+72.2) | 371.4 (303.0+68.4) | -7.5% | 263.7 | 258.3 | -2.1% | 3,865 | 3,865 | +0.0% | 3,452 | 3,452 | +0.0% |
| Danzaburou | Carry | 14,100 / 15,500 | 290.9 (195.5+95.5) | 431.9 (327.1+104.9) | +48.5% | 178.8 | 268.8 | +50.3% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Discordia | Mid | 15,100 / 16,600 | 234.0 (153.4+80.6) | 263.5 (172.8+90.7) | +12.6% | 147.4 | 171.2 | +16.2% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Eset | Mid | 14,750 / 16,600 | 202.9 (137.2+65.8) | 303.3 (206.2+97.2) | +49.5% | 132.9 | 197.0 | +48.2% | 4,202 | 3,760 | -10.5% | 5,058 | 3,399 | -32.8% |
| Fenrir | Jungle | 16,350 / 16,650 | 299.2 (239.4+59.8) | 434.3 (356.7+77.6) | +45.1% | 196.6 | 287.1 | +46.1% | 6,693 | 4,571 | -31.7% | 6,258 | 4,052 | -35.3% |
| Ganesha | Support | 12,850 / 14,750 | 99.2 (59.5+39.7) | 105.1 (59.5+45.6) | +5.9% | 62.5 | 66.2 | +5.9% | 8,291 | 11,613 | +40.1% | 8,547 | 11,383 | +33.2% |
| Geb | Support | 12,950 / 14,700 | 109.4 (58.3+51.1) | 103.7 (58.3+45.4) | -5.2% | 68.9 | 65.3 | -5.2% | 7,428 | 14,002 | +88.5% | 8,516 | 12,929 | +51.8% |
| Gilgamesh | Solo Jungle | 15,750 / 14,550 | 201.8 (169.6+32.2) | 244.9 (209.8+35.1) | +21.4% | 127.1 | 152.5 | +20.0% | 9,520 | 10,373 | +9.0% | 7,406 | 7,901 | +6.7% |
| Guan Yu | Solo Support | 15,200 / 14,500 | 105.5 (77.7+27.8) | 167.7 (135.9+31.9) | +59.0% | 66.4 | 104.4 | +57.3% | 9,933 | 9,611 | -3.2% | 9,781 | 9,611 | -1.7% |
| Hades | Solo | 17,050 / 15,950 | 183.6 (108.8+74.8) | 207.1 (118.4+88.7) | +12.8% | 117.0 | 135.7 | +16.0% | 7,086 | 6,732 | -5.0% | 6,629 | 6,298 | -5.0% |
| Hecate | Mid | 14,700 / 16,600 | 285.6 (130.0+155.6) | 364.7 (166.5+198.2) | +27.7% | 184.8 | 236.9 | +28.2% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Hercules | Solo | 15,050 / 14,800 | 125.8 (70.0+55.8) | 198.9 (136.6+62.4) | +58.1% | 79.2 | 123.9 | +56.3% | 10,112 | 9,783 | -3.3% | 8,860 | 9,254 | +4.5% |
| Horus | Support | 13,300 / 14,750 | 65.3 (61.2+4.1) | 94.0 (89.4+4.6) | +43.9% | 41.1 | 58.5 | +42.3% | 8,603 | 9,645 | +12.1% | 8,326 | 10,814 | +29.9% |
| Hou Yi | Carry | 13,750 / 15,400 | 404.5 (368.1+36.4) | 453.5 (386.8+66.7) | +12.1% | 267.4 | 285.5 | +6.8% | 4,076 | 4,076 | +0.0% | 3,580 | 3,580 | +0.0% |
| Hua Mulan | Solo | 15,500 / 14,550 | 105.7 (65.3+40.4) | 202.3 (152.5+49.7) | +91.3% | 66.6 | 125.9 | +89.2% | 10,432 | 10,432 | +0.0% | 10,490 | 8,380 | -20.1% |
| Hun Batz | Jungle | 16,150 / 16,650 | 381.4 (274.7+106.8) | 483.9 (346.4+137.5) | +26.9% | 250.6 | 319.9 | +27.7% | 4,233 | 4,233 | +0.0% | 3,752 | 3,752 | +0.0% |
| Ishtar | Carry | 15,400 / 15,600 | 440.4 (430.8+9.5) | 616.8 (604.5+12.3) | +40.1% | 291.1 | 388.4 | +33.4% | 3,861 | 4,203 | +8.9% | 3,416 | 3,719 | +8.9% |
| Ix Chel | Mid Support | 15,200 / 15,350 | 367.4 (141.9+225.5) | 223.1 (77.5+145.6) | -39.3% | 231.3 | 138.8 | -40.0% | 3,866 | 7,164 | +85.3% | 3,595 | 8,508 | +136.6% |
| Izanami | Carry | 13,550 / 15,500 | 375.5 (356.6+18.9) | 378.1 (324.6+53.4) | +0.7% | 248.2 | 235.3 | -5.2% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Janus | Mid | 14,700 / 16,600 | 245.6 (130.0+115.5) | 313.8 (166.5+147.3) | +27.8% | 158.9 | 203.8 | +28.3% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Jing Wei | Carry | 14,250 / 15,600 | 470.5 (448.3+22.2) | 641.6 (616.6+25.0) | +36.4% | 303.1 | 404.0 | +33.3% | 3,788 | 4,130 | +9.0% | 3,353 | 3,656 | +9.0% |
| Jormungandr | Solo Support | 13,750 / 14,550 | 134.1 (70.8+63.3) | 178.9 (108.0+70.9) | +33.5% | 84.4 | 111.4 | +32.0% | 8,445 | 10,772 | +27.6% | 8,394 | 8,849 | +5.4% |
| Kali | Jungle | 15,300 / 15,600 | 271.1 (243.3+27.7) | 355.1 (304.4+50.8) | +31.0% | 174.6 | 218.3 | +25.0% | 4,233 | 4,233 | +0.0% | 3,752 | 3,752 | +0.0% |
| Khepri | Support | 15,200 / 14,750 | 195.4 (139.7+55.7) | 99.8 (58.3+41.4) | -49.0% | 121.6 | 62.8 | -48.3% | 4,796 | 11,736 | +144.7% | 4,227 | 11,503 | +172.1% |
| Kukulkan | Mid | 14,800 / 16,600 | 184.6 (115.2+69.4) | 276.0 (166.5+109.5) | +49.6% | 120.9 | 179.3 | +48.3% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Loki | Jungle | 14,700 / 16,300 | 230.6 (213.2+17.4) | 323.7 (303.1+20.6) | +40.4% | 155.2 | 206.9 | +33.3% | 4,117 | 4,117 | +0.0% | 3,702 | 3,702 | +0.0% |
| Medusa | Carry | 13,750 / 15,500 | 388.6 (352.8+35.9) | 389.5 (313.1+76.5) | +0.2% | 256.9 | 242.4 | -5.6% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Mercury | Jungle | 14,700 / 16,050 | 489.6 (480.9+8.8) | 388.4 (372.3+16.1) | -20.7% | 333.1 | 255.1 | -23.4% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Merlin | Mid | 15,350 / 16,600 | 328.1 (138.6+189.5) | 360.8 (166.5+194.3) | +10.0% | 209.5 | 234.4 | +11.9% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Mordred | Solo Jungle | 13,250 / 15,150 | 106.9 (62.8+44.2) | 192.6 (137.4+55.1) | +80.1% | 67.3 | 121.2 | +80.1% | 9,741 | 8,443 | -13.3% | 9,037 | 7,919 | -12.4% |
| Morgan Le Fay | Mid | 15,050 / 16,600 | 205.7 (126.4+79.4) | 264.4 (175.6+88.8) | +28.5% | 134.8 | 171.7 | +27.4% | 4,015 | 4,015 | +0.0% | 4,929 | 3,630 | -26.4% |
| Ne Zha | Jungle | 14,850 / 16,100 | 377.4 (351.2+26.2) | 434.3 (397.8+36.5) | +15.1% | 254.0 | 302.0 | +18.9% | 5,708 | 4,233 | -25.8% | 5,167 | 3,752 | -27.4% |
| Neith | Carry Mid | 15,000 / 15,650 | 299.0 (187.2+111.8) | 385.2 (243.0+142.2) | +28.8% | 190.9 | 233.7 | +22.4% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Nemesis | Jungle | 16,200 / 15,800 | 271.8 (226.1+45.7) | 500.1 (457.8+42.3) | +84.0% | 182.9 | 314.8 | +72.1% | 5,437 | 4,233 | -22.1% | 4,896 | 3,752 | -23.4% |
| Nu Wa | Mid | 15,200 / 16,600 | 251.3 (166.9+84.4) | 282.3 (187.0+95.2) | +12.3% | 158.2 | 183.3 | +15.9% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Nut | Carry Mid | 15,750 / 16,300 | 366.8 (353.0+13.9) | 262.3 (233.6+28.7) | -28.5% | 249.6 | 175.1 | -29.9% | 4,045 | 4,045 | +0.0% | 3,580 | 3,580 | +0.0% |
| Odin | Solo Jungle | 13,550 / 14,500 | 135.0 (97.7+37.3) | 167.5 (131.6+35.9) | +24.1% | 84.1 | 104.3 | +24.1% | 8,169 | 8,443 | +3.3% | 6,990 | 9,595 | +37.3% |
| Osiris | Solo | 15,100 / 14,550 | 140.2 (81.0+59.2) | 299.5 (224.8+74.6) | +113.6% | 88.3 | 186.5 | +111.2% | 12,647 | 10,167 | -19.6% | 9,279 | 7,735 | -16.6% |
| Pele | Jungle | 14,850 / 16,100 | 292.7 (286.4+6.4) | 291.9 (284.6+7.3) | -0.3% | 192.3 | 203.0 | +5.6% | 4,307 | 4,307 | +0.0% | 3,817 | 3,817 | +0.0% |
| Poseidon | Mid | 15,200 / 16,600 | 243.2 (181.5+61.7) | 264.1 (182.2+81.8) | +8.6% | 155.3 | 171.5 | +10.5% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Princess Bari | Carry Mid | 17,500 / 15,650 | 265.2 (187.7+77.5) | 372.8 (321.9+50.9) | +40.6% | 172.3 | 234.7 | +36.3% | 4,046 | 4,046 | +0.0% | 3,745 | 3,745 | +0.0% |
| Ra | Mid | 15,200 / 16,300 | 281.6 (147.8+133.8) | 316.1 (150.9+165.1) | +12.2% | 177.3 | 211.0 | +19.0% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Rama | Carry | 13,750 / 16,100 | 380.7 (376.5+4.2) | 560.7 (553.1+7.6) | +47.3% | 251.7 | 339.4 | +34.8% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Ratatoskr | Jungle | 13,750 / 14,300 | 282.7 (220.0+62.7) | 350.7 (279.0+71.8) | +24.0% | 190.3 | 223.8 | +17.6% | 5,715 | 6,419 | +12.3% | 5,065 | 5,689 | +12.3% |
| Scylla | Mid | 14,450 / 16,600 | 241.0 (126.3+114.7) | 332.4 (166.5+165.9) | +37.9% | 157.9 | 216.0 | +36.7% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Sobek | Support | 13,150 / 14,750 | 107.6 (60.3+47.3) | 114.6 (60.3+54.3) | +6.5% | 67.7 | 72.1 | +6.5% | 8,313 | 11,475 | +38.0% | 9,486 | 11,247 | +18.6% |
| Sol | Mid Carry | 14,600 / 16,400 | 224.2 (197.4+26.8) | 277.1 (244.6+32.5) | +23.6% | 146.9 | 187.2 | +27.5% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Sun Wukong | Solo | 14,250 / 14,500 | 77.5 (72.7+4.8) | 179.8 (174.6+5.2) | +132.1% | 51.2 | 112.0 | +118.6% | 7,595 | 10,159 | +33.8% | 8,548 | 7,857 | -8.1% |
| Susano | Jungle | 14,550 / 16,650 | 357.5 (319.0+38.5) | 431.6 (382.9+48.6) | +20.7% | 234.8 | 285.3 | +21.5% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Sylvanus | Support | 12,850 / 14,750 | 71.2 (47.6+23.6) | 71.2 (47.6+23.6) | +0.0% | 44.8 | 44.8 | +0.0% | 8,136 | 11,736 | +44.2% | 7,949 | 11,503 | +44.7% |
| Thanatos | Jungle | 16,150 / 16,650 | 389.8 (295.2+94.7) | 494.6 (372.5+122.0) | +26.9% | 256.1 | 326.9 | +27.7% | 4,655 | 4,655 | +0.0% | 4,126 | 4,126 | +0.0% |
| The Morrigan | Mid | 15,250 / 16,600 | 209.9 (161.6+48.3) | 245.7 (185.1+60.6) | +17.0% | 134.0 | 159.6 | +19.1% | 3,894 | 3,894 | +0.0% | 3,452 | 3,452 | +0.0% |
| Thor | Jungle Solo | 14,450 / 14,600 | 299.4 (262.2+37.3) | 199.4 (172.4+27.0) | -33.4% | 201.5 | 124.2 | -38.4% | 4,559 | 9,019 | +97.8% | 3,986 | 9,486 | +138.0% |
| Tsukuyomi | Jungle | 14,600 / 15,800 | 308.5 (272.7+35.7) | 487.9 (453.8+34.1) | +58.2% | 207.6 | 307.2 | +48.0% | 4,307 | 4,307 | +0.0% | 3,766 | 3,766 | +0.0% |
| Ullr | Carry | 14,600 / 15,300 | 359.0 (259.8+99.2) | 584.3 (496.1+88.2) | +62.8% | 241.6 | 353.7 | +46.4% | 4,148 | 4,148 | +0.0% | 3,644 | 3,644 | +0.0% |
| Vulcan | Mid | 12,700 / 16,600 | 274.5 (131.2+143.3) | 355.9 (186.0+169.8) | +29.6% | 175.3 | 234.4 | +33.7% | 4,015 | 4,015 | +0.0% | 3,630 | 3,630 | +0.0% |
| Xbalanque | Carry | 13,050 / 15,600 | 369.3 (354.0+15.3) | 641.4 (621.2+20.2) | +73.7% | 238.0 | 403.8 | +69.7% | 3,788 | 4,130 | +9.0% | 3,353 | 3,656 | +9.0% |
| Xing Tian | Support Solo | 13,300 / 14,750 | 23.9 (0.0+23.9) | 23.9 (0.0+23.9) | +0.0% | 15.0 | 15.0 | +0.0% | 690 | 2,250 | +226.1% | 735 | 2,385 | +224.5% |
| Yemoja | Support | 14,150 / 14,750 | 105.1 (99.6+5.5) | 61.8 (57.7+4.0) | -41.2% | 67.9 | 38.9 | -42.7% | 6,639 | 11,912 | +79.4% | 6,327 | 11,675 | +84.5% |
| Ymir | Support | 12,950 / 14,750 | 110.4 (63.3+47.1) | 118.6 (63.3+55.3) | +7.4% | 69.5 | 74.7 | +7.4% | 9,466 | 12,300 | +29.9% | 9,584 | 13,401 | +39.8% |
| Zeus | Mid | 15,050 / 16,600 | 243.8 (140.1+103.7) | 325.7 (208.0+117.7) | +33.6% | 157.8 | 214.6 | +36.0% | 5,050 | 3,894 | -22.9% | 4,548 | 3,452 | -24.1% |
