# Build quality — `combat.py` pointed at whole builds

_Input fingerprint: `052cab0a44cc` — items, gods, tags, community builds, weights. Regenerate with `python -m smite.build_quality`; a different fingerprint means different inputs._

> **READ THIS BEFORE ANY NUMBER BELOW.** Of the 138 buildable items, 137 carry passive text and the shipped pricing flags read 13 of them — so **90% of the pool carries passive value this arithmetic cannot see**, and **74% of the community's item slots do** (395 of 537; 89% of ours, 473 of 534). `combat.py` reads exactly one passive — Deathbringer's +35% crit damage. The bias is not even: by the gold model's own residual the community pays **+78g more per slot above its stat line than we do** (mean residual -11g against -89g) and buys fewer stat columns per item (2.71 against 3.41) — that premium IS the passive. **A verdict in our favour is the one to distrust.** The most-bought blind community items are Genji's Guard (27), Freya's Tears (25), Obsidian Shard (23), Shell of Rebuke (21), Shifter's Shield (20).

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

**community** — 13,750g: Tyrfing · Odysseus' Bow · Silverbranch Bow · The Executioner · Riptalon · Manchu Bow
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
| total DPS vs 70 prot | 89 | **70** | **17** | 2 | -42.7% | +2.9% | **+24.1%** | +45.8% | +194.3% |
| total DPS vs 170 prot | 89 | **69** | **20** | 0 | -44.7% | +2.9% | **+24.1%** | +42.9% | +191.0% |
| effective health, physical | 89 | **37** | **11** | 41 | -28.6% | +0.0% | **+0.0%** | +20.6% | +136.9% |
| effective health, magical | 89 | **36** | **12** | 41 | -32.1% | +0.0% | **+0.0%** | +14.6% | +136.6% |
| total DPS vs 70 prot per 1000g | 89 | **61** | **28** | 0 | -43.8% | -6.8% | **+12.2%** | +32.2% | +142.5% |
| total DPS vs 170 prot per 1000g | 89 | **60** | **29** | 0 | -48.4% | -6.8% | **+12.4%** | +27.9% | +139.8% |
| effective health, physical per 1000g | 89 | **33** | **55** | 1 | -39.3% | -11.9% | **-6.1%** | +7.6% | +123.2% |
| effective health, magical per 1000g | 89 | **33** | **55** | 1 | -40.9% | -12.9% | **-7.5%** | +8.9% | +109.7% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 13 / 3 / +44.5% | 13 / 5 / +35.5% | 5 / 1 / +0.0% | 5 / 1 / +0.0% |
| Jungle | 17 | 13 / 4 / +24.3% | 12 / 5 / +25.0% | 1 / 4 / +0.0% | 1 / 4 / +0.0% |
| Mid | 22 | 19 / 3 / +22.1% | 19 / 3 / +21.2% | 3 / 2 / +0.0% | 3 / 2 / +0.0% |
| Solo | 18 | 16 / 2 / +36.2% | 16 / 2 / +37.0% | 14 / 4 / +17.5% | 13 / 5 / +11.6% |
| Support | 14 | 9 / 5 / +3.2% | 9 / 5 / +3.2% | 14 / 0 / +32.7% | 14 / 0 / +41.8% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 13 / 5 / +29.5% | 12 / 6 / +20.2% | 2 / 16 / -10.8% | 2 / 16 / -10.8% |
| Jungle | 17 | 12 / 5 / +9.2% | 12 / 5 / +9.9% | 3 / 14 / -11.2% | 3 / 14 / -11.2% |
| Mid | 22 | 18 / 4 / +11.7% | 18 / 4 / +11.7% | 5 / 16 / -8.7% | 5 / 16 / -8.7% |
| Solo | 18 | 13 / 5 / +27.5% | 13 / 5 / +26.1% | 11 / 7 / +7.0% | 10 / 8 / +2.7% |
| Support | 14 | 5 / 9 / -8.1% | 5 / 9 / -8.1% | 12 / 2 / +14.1% | 13 / 1 / +17.5% |

## 3. Judged by role, on each role's own objective

Most roles clear a THRESHOLD and then maximise something else, and one pooled metric cannot represent five roles that do not share an objective. Each row below names both quantities. **The passive blind spot at the top of this report applies to every row here exactly as it applies to the pooled figures** — slicing by role does not escape it, and the bias still runs in our favour.

**An objective containing effective health is scored on BOTH damage channels and read as the interval between them.** A build has one damage output and two effective healths; which one its survival is read on is a property of the ATTACKER, and there is no attacker in this comparison. Against a stream that is a share `f` physical, effective health is `1 / (f/EHP_p + (1-f)/EHP_m)` — a weighted harmonic mean, because what averages over a mixed stream is the damage-taken multiplier and not its reciprocal — and the ours-over-theirs ratio is monotone in `f`, so **every possible damage mix lands between the two channels and the pair is the whole range**. `ahead` below therefore means ahead at every mix, `behind` means behind at every mix, and `mix-dependent` means the answer is a fact about the enemy team that this comparison does not contain. Averaging the two channels would assert equal exposure, which is a constant no source here supplies — and would not even be the answer to its own question, since the correct collapse at 50/50 is harmonic and not arithmetic. Until 2026-08-23 both roles read `ehp_physical` alone, i.e. the two roles whose job is durability were scored on half the damage in the game.

| Role | n | Threshold | Binds? | Maximised | ahead | behind | level | mix-dependent | median |
|---|---|---|---|---|---|---|---|---|---|
| Carry | 18 | survive one enemy burst rotation | **no** — 0 of 36 builds fail it | sustained DPS per 1000g | **13** | **5** | 0 | – (no EHP term) | **+29.5%** |
| Jungle | 17 | rotation burst >= a reference squishy's EHP | **no** — all 78 builds fail it | rotation burst per 1000g | **12** | **5** | 0 | – (no EHP term) | **+9.9%** |
| Mid | 22 | rotation burst >= a reference squishy's EHP | **no** — all 78 builds fail it | sustained DPS per 1000g | **18** | **4** | 0 | – (no EHP term) | **+11.7%** |
| Solo | 18 | **none** | – | duel score, EHP x DPS | **16** | **1** | 0 | **1** | **+55.6% … +57.2%** |
| Support | 14 | **none** | – | effective health per 1000g | **12** | **1** | 0 | **1** | **+14.1% … +17.5%** |

Builds whose verdict the damage mix decides — the interval spans both answers, so neither is available here:

- **Amaterasu** (Solo) — vs a physical opponent -21.5% · vs a magical opponent +10.2%
- **Ares** (Support) — vs a physical opponent -4.4% · vs a magical opponent +8.9%

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
| Carry | 18 | 1.9 / 0.0 | 1.9 / 0.0 | 0.0 / 55.6 |
| Jungle | 17 | 8.8 / 3.8 | 12.1 / 5.9 | 88.2 / 138.2 |
| Mid | 22 | 4.1 / 10.9 | 7.6 / 19.1 | 43.2 / 81.8 |
| Solo | 18 | 94.2 / 104.4 | 113.2 / 107.2 | 582.8 / 894.4 |
| Support | 14 | 86.6 / 137.1 | 115.3 / 166.1 | 461.1 / 953.6 |

The community buys 1.9 Physical Protection across all 18 Carries and we buy 0.0, a surplus of -1.9. The defensive items still reaching a Carry core, with how many of ours hold each against how many of the community's — an EMPTY list here is the measurement, not a missing section:

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

89 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 89 | **61** | **25** | 3 | -36.7% | -1.9% | **+16.5%** | +36.3% | +138.4% |
| total DPS vs 170 prot | 89 | **58** | **28** | 3 | -36.2% | -2.2% | **+16.2%** | +35.2% | +135.8% |
| effective health, physical | 89 | **34** | **12** | 43 | -32.9% | +0.0% | **+0.0%** | +22.2% | +131.2% |
| effective health, magical | 89 | **31** | **15** | 43 | -32.9% | +0.0% | **+0.0%** | +12.5% | +136.6% |
| total DPS vs 70 prot per 1000g | 89 | **54** | **32** | 3 | -40.7% | -11.7% | **+6.2%** | +22.4% | +113.4% |
| total DPS vs 170 prot per 1000g | 89 | **52** | **35** | 2 | -42.5% | -15.5% | **+4.8%** | +21.6% | +107.7% |
| effective health, physical per 1000g | 89 | **31** | **55** | 3 | -38.2% | -11.4% | **-6.9%** | +12.3% | +108.0% |
| effective health, magical per 1000g | 89 | **25** | **61** | 3 | -39.6% | -13.3% | **-7.7%** | +2.9% | +109.7% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 14 / 4 / +27.5% | 13 / 5 / +25.0% | 3 / 0 / +0.0% | 3 / 0 / +0.0% |
| Jungle | 17 | 13 / 4 / +14.9% | 13 / 4 / +6.5% | 1 / 5 / +0.0% | 1 / 5 / +0.0% |
| Mid | 22 | 15 / 6 / +16.8% | 14 / 7 / +16.2% | 3 / 2 / +0.0% | 3 / 2 / +0.0% |
| Solo | 18 | 12 / 5 / +26.5% | 11 / 6 / +25.8% | 13 / 5 / +16.9% | 11 / 7 / +6.7% |
| Support | 14 | 7 / 6 / +1.4% | 7 / 6 / +1.4% | 14 / 0 / +40.2% | 13 / 1 / +31.9% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 13 / 5 / +14.8% | 12 / 6 / +7.8% | 2 / 16 / -11.3% | 2 / 16 / -11.3% |
| Jungle | 17 | 12 / 4 / +8.0% | 11 / 6 / +4.6% | 2 / 14 / -10.2% | 2 / 14 / -10.2% |
| Mid | 22 | 13 / 7 / +4.3% | 13 / 7 / +5.1% | 3 / 17 / -7.5% | 3 / 17 / -7.7% |
| Solo | 18 | 11 / 7 / +17.0% | 11 / 7 / +16.3% | 10 / 8 / +7.6% | 7 / 11 / -5.6% |
| Support | 14 | 5 / 9 / -8.7% | 5 / 9 / -8.7% | 14 / 0 / +20.7% | 11 / 3 / +18.2% |

## 5. Sensitivity — the passives the gold model CAN price

Same as §2 with the shipped pricing flags applied to every stat line: the Adaptive Stat grants (`price_adaptive`) and the mana conversions (`price_conversions`). This is the one slice of the blind spot that can be put on the table; the other 124 items stay invisible here too.

89 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 89 | **73** | **16** | 0 | -52.5% | +5.2% | **+24.1%** | +40.8% | +127.9% |
| total DPS vs 170 prot | 89 | **73** | **16** | 0 | -51.9% | +3.6% | **+21.2%** | +38.9% | +125.4% |
| effective health, physical | 89 | **37** | **11** | 41 | -28.6% | +0.0% | **+0.0%** | +20.6% | +136.9% |
| effective health, magical | 89 | **36** | **12** | 41 | -32.1% | +0.0% | **+0.0%** | +14.6% | +136.6% |
| total DPS vs 70 prot per 1000g | 89 | **60** | **27** | 2 | -55.2% | -4.4% | **+12.4%** | +27.2% | +116.7% |
| total DPS vs 170 prot per 1000g | 89 | **59** | **27** | 3 | -54.7% | -6.8% | **+10.1%** | +24.4% | +114.3% |
| effective health, physical per 1000g | 89 | **33** | **55** | 1 | -39.3% | -11.9% | **-6.1%** | +7.6% | +123.2% |
| effective health, magical per 1000g | 89 | **33** | **55** | 1 | -40.9% | -12.9% | **-7.5%** | +8.9% | +109.7% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 16 / 2 / +30.7% | 16 / 2 / +20.2% | 5 / 1 / +0.0% | 5 / 1 / +0.0% |
| Jungle | 17 | 13 / 4 / +23.9% | 13 / 4 / +23.2% | 1 / 4 / +0.0% | 1 / 4 / +0.0% |
| Mid | 22 | 19 / 3 / +22.3% | 19 / 3 / +22.1% | 3 / 2 / +0.0% | 3 / 2 / +0.0% |
| Solo | 18 | 16 / 2 / +33.6% | 16 / 2 / +32.1% | 14 / 4 / +17.5% | 13 / 5 / +11.6% |
| Support | 14 | 9 / 5 / +3.2% | 9 / 5 / +3.2% | 14 / 0 / +32.7% | 14 / 0 / +41.8% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 13 / 5 / +19.4% | 12 / 5 / +11.3% | 2 / 16 / -10.8% | 2 / 16 / -10.8% |
| Jungle | 17 | 13 / 3 / +9.2% | 12 / 4 / +10.0% | 3 / 14 / -11.2% | 3 / 14 / -11.2% |
| Mid | 22 | 17 / 4 / +11.7% | 17 / 4 / +10.3% | 5 / 16 / -8.7% | 5 / 16 / -8.7% |
| Solo | 18 | 12 / 6 / +25.5% | 13 / 5 / +26.1% | 11 / 7 / +7.0% | 10 / 8 / +2.7% |
| Support | 14 | 5 / 9 / -8.1% | 5 / 9 / -8.1% | 12 / 2 / +14.1% | 13 / 1 / +17.5% |

Verdict on DPS vs 70 flips for 1 god(s) between §2 and §5: Nut (-36.3 → +17.5).

## 6. The blind spot, measured

| | buildable pool | community slots | our `model` slots |
|---|---|---|---|
| items / slots | 138 | 537 | 534 |
| carrying unpriced passive text | 124 (89.9%) | 395 (73.6%) | 473 (88.6%) |
| mean gold residual per slot (cost − stat-line prediction) | – | -11g | -89g |
| mean stat columns per item | – | 2.71 | 3.41 |

Passives the shipped flags price (13): Book of Thoth, Brawler’s Beat Stick, Daybreak Gavel, Deathbringer, Eye of Erebus, Mercury's Talaria, Nimble Ring, Omen Drum, Rod of Tahuti, Sun Beam Bow, The Executioner, Transcendence, Vital Amplifier.

Most-bought blind items — community: Genji's Guard (27), Freya's Tears (25), Obsidian Shard (23), Shell of Rebuke (21), Shifter's Shield (20). Ours: Jotunn's Revenge (52), Kinetic Cuirass (36), Amanita Charm (35), Freya's Tears (30), Spear of Desolation (29).

## 7. Every god — `model` core, printed stat lines

C = community, O = ours. DPS vs 70 is shown as total (basic + ability).

| God | Role | Gold C / O | DPS vs 70 — C (basic+ability) | O (basic+ability) | Δ | DPS vs 170 — C | O | Δ | EHP phys — C | O | Δ | EHP mag — C | O | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Achilles | Solo Jungle | 14,450 / 14,600 | 237.9 (194.3+43.7) | 213.8 (166.1+47.7) | -10.1% | 161.9 | 133.1 | -17.8% | 6,355 | 9,039 | +42.2% | 6,838 | 9,283 | +35.8% |
| Agni | Mid | 15,400 / 16,600 | 217.1 (146.8+70.3) | 267.0 (183.2+83.7) | +23.0% | 142.3 | 173.4 | +21.9% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Ah Puch | Mid | 16,550 / 16,600 | 158.4 (117.7+40.8) | 225.1 (169.1+56.0) | +42.1% | 106.2 | 146.2 | +37.7% | 4,799 | 4,347 | -9.4% | 4,263 | 3,862 | -9.4% |
| Aladdin | Jungle | 13,550 / 15,900 | 109.2 (102.5+6.7) | 168.7 (160.4+8.3) | +54.5% | 71.6 | 106.2 | +48.5% | 4,233 | 4,233 | +0.0% | 3,846 | 3,846 | +0.0% |
| Amaterasu | Solo | 13,600 / 14,500 | 125.1 (108.1+17.1) | 132.0 (105.4+26.6) | +5.5% | 78.8 | 82.2 | +4.3% | 11,145 | 8,296 | -25.6% | 9,070 | 9,476 | +4.5% |
| Anhur | Carry | 13,600 / 15,150 | 466.1 (430.3+35.8) | 586.2 (524.2+61.9) | +25.8% | 308.1 | 364.5 | +18.3% | 4,148 | 4,493 | +8.3% | 3,644 | 3,947 | +8.3% |
| Anubis | Mid | 13,950 / 16,600 | 140.3 (121.2+19.1) | 195.5 (166.5+29.0) | +39.3% | 86.3 | 127.0 | +47.2% | 4,202 | 4,202 | +0.0% | 3,912 | 3,912 | +0.0% |
| Aphrodite | Mid Support | 14,150 / 15,350 | 149.1 (93.3+55.8) | 130.1 (82.4+47.7) | -12.7% | 92.8 | 81.0 | -12.7% | 4,439 | 7,029 | +58.3% | 5,450 | 8,258 | +51.5% |
| Apollo | Carry | 13,750 / 15,150 | 391.3 (357.9+33.4) | 569.9 (512.0+57.8) | +45.6% | 258.7 | 354.4 | +37.0% | 4,076 | 4,421 | +8.5% | 3,580 | 3,883 | +8.5% |
| Ares | Support | 13,350 / 14,750 | 60.3 (60.3+0.0) | 87.9 (87.9+0.0) | +45.8% | 37.9 | 54.7 | +44.2% | 9,640 | 10,187 | +5.7% | 9,457 | 11,383 | +20.4% |
| Artemis | Carry | 13,750 / 15,850 | 401.0 (378.5+22.5) | 659.5 (616.4+43.1) | +64.5% | 265.1 | 390.3 | +47.2% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Artio | Solo Support | 11,850 / 14,800 | 108.0 (61.2+46.8) | 171.5 (115.3+56.2) | +58.9% | 68.0 | 106.8 | +57.1% | 7,626 | 10,438 | +36.9% | 8,723 | 9,864 | +13.1% |
| Athena | Support | 13,150 / 14,750 | 117.6 (84.4+33.2) | 159.3 (122.6+36.6) | +35.4% | 74.0 | 99.2 | +33.9% | 8,579 | 10,187 | +18.8% | 7,417 | 11,383 | +53.5% |
| Atlas | Support | 13,350 / 14,750 | 88.8 (72.9+15.9) | 91.2 (72.9+18.2) | +2.6% | 55.9 | 57.4 | +2.6% | 10,001 | 11,736 | +17.3% | 10,289 | 11,503 | +11.8% |
| Awilix | Jungle | 14,800 / 16,650 | 404.8 (296.9+107.9) | 485.4 (350.9+134.5) | +19.9% | 265.9 | 320.9 | +20.7% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Bacchus | Support | 12,350 / 14,750 | 88.9 (60.3+28.7) | 124.7 (87.9+36.8) | +40.2% | 56.0 | 77.6 | +38.7% | 8,169 | 10,040 | +22.9% | 8,310 | 11,460 | +37.9% |
| Baron Samedi | Mid Support | 11,900 / 15,350 | 167.5 (75.3+92.2) | 176.1 (82.4+93.7) | +5.2% | 103.1 | 109.6 | +6.3% | 5,198 | 7,029 | +35.2% | 5,324 | 8,258 | +55.1% |
| Bastet | Jungle | 14,600 / 16,650 | 335.0 (281.7+53.2) | 417.2 (343.9+73.3) | +24.5% | 220.0 | 275.8 | +25.3% | 4,117 | 4,117 | +0.0% | 3,702 | 3,702 | +0.0% |
| Bellona | Solo | 15,100 / 14,800 | 325.0 (297.7+27.3) | 186.1 (142.6+43.5) | -42.7% | 209.4 | 115.9 | -44.7% | 8,410 | 10,251 | +21.9% | 7,466 | 9,475 | +26.9% |
| Cabrakan | Solo Support | 11,650 / 14,800 | 153.6 (96.1+57.5) | 187.2 (121.6+65.7) | +21.9% | 96.7 | 116.6 | +20.5% | 8,607 | 10,438 | +21.3% | 10,001 | 9,864 | -1.4% |
| Cerberus | Solo Support | 11,650 / 14,750 | 84.2 (52.2+32.0) | 86.4 (52.2+34.2) | +2.6% | 53.0 | 54.4 | +2.6% | 7,970 | 11,614 | +45.7% | 8,973 | 11,460 | +27.7% |
| Cernunnos | Carry Jungle | 13,500 / 15,650 | 439.7 (420.4+19.3) | 286.6 (250.3+36.4) | -34.8% | 290.6 | 173.9 | -40.2% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Chaac | Solo | 13,000 / 15,100 | 151.6 (77.8+73.8) | 199.5 (106.1+93.5) | +31.6% | 93.3 | 125.6 | +34.7% | 7,507 | 7,839 | +4.4% | 7,089 | 9,082 | +28.1% |
| Charon | Support | 15,950 / 14,750 | 134.5 (80.8+53.6) | 102.0 (55.4+46.5) | -24.2% | 83.7 | 64.2 | -23.3% | 6,579 | 11,614 | +76.5% | 7,547 | 11,383 | +50.8% |
| Chiron | Carry | 14,000 / 15,600 | 365.1 (291.5+73.7) | 627.1 (553.2+73.9) | +71.7% | 233.0 | 389.3 | +67.1% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Chronos | Mid Carry | 14,350 / 16,400 | 280.5 (196.9+83.6) | 339.9 (224.3+115.6) | +21.2% | 178.9 | 229.7 | +28.4% | 4,016 | 4,016 | +0.0% | 3,630 | 3,630 | +0.0% |
| Cu Chulainn | Solo | 15,150 / 14,550 | 143.7 (36.2+107.5) | 242.4 (130.3+112.1) | +68.7% | 90.5 | 150.9 | +66.8% | 11,201 | 10,282 | -8.2% | 11,637 | 7,901 | -32.1% |
| Cupid | Carry | 13,550 / 15,650 | 385.1 (367.8+17.4) | 293.6 (254.2+39.4) | -23.8% | 254.6 | 178.1 | -30.0% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Da Ji | Jungle | 14,450 / 16,100 | 338.8 (279.2+59.6) | 371.4 (303.0+68.4) | +9.6% | 228.0 | 258.3 | +13.3% | 3,865 | 3,865 | +0.0% | 3,452 | 3,452 | +0.0% |
| Danzaburou | Carry | 14,350 / 15,500 | 289.3 (223.4+65.9) | 431.9 (327.1+104.9) | +49.3% | 200.0 | 268.8 | +34.4% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Discordia | Mid | 15,350 / 16,600 | 221.2 (145.0+76.2) | 263.5 (172.8+90.7) | +19.1% | 143.1 | 171.2 | +19.6% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Eset | Mid | 14,900 / 16,600 | 268.2 (183.0+85.3) | 303.3 (206.2+97.2) | +13.1% | 174.2 | 197.0 | +13.1% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Fenrir | Jungle | 14,150 / 16,650 | 239.6 (195.0+44.6) | 434.3 (356.7+77.6) | +81.3% | 149.0 | 287.1 | +92.7% | 6,403 | 4,571 | -28.6% | 5,824 | 4,052 | -30.4% |
| Ganesha | Support | 11,450 / 14,750 | 102.2 (59.5+42.6) | 105.1 (59.5+45.6) | +2.9% | 64.3 | 66.2 | +2.9% | 8,091 | 11,613 | +43.5% | 8,721 | 11,383 | +30.5% |
| Geb | Support | 11,300 / 14,700 | 113.1 (58.3+54.8) | 103.7 (58.3+45.4) | -8.4% | 71.2 | 65.3 | -8.4% | 7,164 | 14,002 | +95.5% | 8,359 | 12,929 | +54.7% |
| Gilgamesh | Solo Jungle | 14,150 / 14,550 | 215.6 (174.2+41.5) | 244.9 (209.8+35.1) | +13.6% | 137.4 | 152.5 | +11.0% | 7,209 | 10,373 | +43.9% | 6,636 | 7,901 | +19.1% |
| Guan Yu | Solo Support | 13,150 / 14,500 | 119.1 (87.8+31.3) | 167.7 (135.9+31.9) | +40.8% | 75.0 | 104.4 | +39.3% | 6,895 | 9,611 | +39.4% | 7,994 | 9,611 | +20.2% |
| Hades | Solo | 14,750 / 15,950 | 141.3 (90.7+50.6) | 207.1 (118.4+88.7) | +46.6% | 87.9 | 135.7 | +54.3% | 6,184 | 6,732 | +8.9% | 5,577 | 6,298 | +12.9% |
| Hecate | Mid | 15,200 / 16,600 | 324.3 (147.8+176.4) | 364.7 (166.5+198.2) | +12.5% | 204.2 | 236.9 | +16.0% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Hercules | Solo | 15,050 / 14,800 | 130.1 (70.0+60.2) | 198.9 (136.6+62.4) | +52.8% | 81.9 | 123.9 | +51.1% | 8,548 | 9,783 | +14.4% | 8,386 | 9,254 | +10.4% |
| Horus | Support | 13,600 / 14,750 | 64.8 (61.2+3.6) | 94.0 (89.4+4.6) | +45.1% | 40.8 | 58.5 | +43.5% | 9,472 | 9,645 | +1.8% | 10,620 | 10,814 | +1.8% |
| Hou Yi | Carry | 13,350 / 15,400 | 372.0 (337.2+34.8) | 453.5 (386.8+66.7) | +21.9% | 239.7 | 285.5 | +19.1% | 4,076 | 4,076 | +0.0% | 3,580 | 3,580 | +0.0% |
| Hua Mulan | Solo | 12,850 / 14,550 | 108.1 (65.3+42.8) | 202.3 (152.5+49.7) | +87.2% | 68.0 | 125.9 | +85.1% | 8,651 | 10,432 | +20.6% | 8,857 | 8,380 | -5.4% |
| Hun Batz | Jungle | 16,150 / 16,650 | 389.5 (274.7+114.8) | 483.9 (346.4+137.5) | +24.3% | 255.8 | 319.9 | +25.0% | 5,075 | 4,233 | -16.6% | 4,594 | 3,752 | -18.3% |
| Ishtar | Carry | 15,450 / 15,600 | 430.1 (420.5+9.5) | 616.8 (604.5+12.3) | +43.4% | 284.3 | 388.4 | +36.6% | 3,861 | 4,203 | +8.9% | 3,416 | 3,719 | +8.9% |
| Ix Chel | Mid Support | 13,600 / 15,350 | 324.8 (132.5+192.3) | 223.1 (77.5+145.6) | -31.3% | 214.0 | 138.8 | -35.1% | 3,866 | 7,164 | +85.3% | 3,595 | 8,508 | +136.6% |
| Izanami | Carry | 13,500 / 15,500 | 376.3 (358.2+18.1) | 378.1 (324.6+53.4) | +0.5% | 242.5 | 235.3 | -3.0% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Janus | Mid | 17,000 / 16,600 | 288.0 (152.8+135.2) | 313.8 (166.5+147.3) | +8.9% | 192.2 | 203.8 | +6.0% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Jing Wei | Carry | 15,900 / 15,600 | 427.6 (406.1+21.5) | 641.6 (616.6+25.0) | +50.1% | 282.6 | 404.0 | +42.9% | 3,788 | 4,130 | +9.0% | 3,353 | 3,656 | +9.0% |
| Jormungandr | Solo Support | 15,550 / 14,550 | 141.7 (70.8+70.9) | 178.9 (108.0+70.9) | +26.3% | 89.2 | 111.4 | +24.9% | 9,418 | 10,772 | +14.4% | 8,130 | 8,849 | +8.8% |
| Kali | Jungle | 13,850 / 15,600 | 309.3 (282.8+26.5) | 355.1 (304.4+50.8) | +14.8% | 204.5 | 218.3 | +6.7% | 4,233 | 4,233 | +0.0% | 3,752 | 3,752 | +0.0% |
| Khepri | Support | 13,900 / 14,750 | 149.9 (92.9+57.1) | 99.8 (58.3+41.4) | -33.5% | 93.3 | 62.8 | -32.7% | 4,954 | 11,736 | +136.9% | 5,676 | 11,503 | +102.7% |
| Kukulkan | Mid | 14,800 / 16,600 | 184.6 (115.2+69.4) | 276.0 (166.5+109.5) | +49.6% | 120.9 | 179.3 | +48.3% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Loki | Jungle | 14,700 / 16,300 | 230.6 (213.2+17.4) | 323.7 (303.1+20.6) | +40.4% | 155.2 | 206.9 | +33.3% | 4,117 | 4,117 | +0.0% | 3,702 | 3,702 | +0.0% |
| Medusa | Carry | 13,750 / 15,500 | 388.6 (352.8+35.9) | 389.5 (313.1+76.5) | +0.2% | 256.9 | 242.4 | -5.6% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Mercury | Jungle | 14,150 / 16,050 | 471.7 (463.7+8.0) | 388.4 (372.3+16.1) | -17.7% | 311.8 | 255.1 | -18.2% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Merlin | Mid | 15,100 / 16,600 | 293.4 (127.0+166.5) | 360.8 (166.5+194.3) | +23.0% | 194.5 | 234.4 | +20.5% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Mordred | Solo Jungle | 13,300 / 15,150 | 104.1 (62.8+41.3) | 192.6 (137.4+55.1) | +85.0% | 65.5 | 121.2 | +85.0% | 8,978 | 8,443 | -6.0% | 9,062 | 7,919 | -12.6% |
| Morgan Le Fay | Mid | 14,750 / 16,600 | 196.0 (130.3+65.7) | 264.4 (175.6+88.8) | +34.9% | 130.8 | 171.7 | +31.3% | 5,191 | 4,015 | -22.6% | 4,756 | 3,630 | -23.7% |
| Ne Zha | Jungle | 14,850 / 16,100 | 503.7 (474.9+28.8) | 434.3 (397.8+36.5) | -13.8% | 338.9 | 302.0 | -10.9% | 4,233 | 4,233 | +0.0% | 3,752 | 3,752 | +0.0% |
| Neith | Carry Mid | 14,400 / 15,650 | 330.8 (196.0+134.9) | 385.2 (243.0+142.2) | +16.4% | 223.6 | 233.7 | +4.5% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Nemesis | Jungle | 15,450 / 15,800 | 269.2 (224.4+44.8) | 500.1 (457.8+42.3) | +85.8% | 167.4 | 314.8 | +88.1% | 5,075 | 4,233 | -16.6% | 4,594 | 3,752 | -18.3% |
| Nu Wa | Mid | 14,450 / 16,600 | 209.5 (134.0+75.5) | 282.3 (187.0+95.2) | +34.7% | 138.9 | 183.3 | +32.0% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Nut | Carry Mid | 13,950 / 16,300 | 298.5 (284.7+13.9) | 262.3 (233.6+28.7) | -12.1% | 203.1 | 175.1 | -13.8% | 4,045 | 4,045 | +0.0% | 3,580 | 3,580 | +0.0% |
| Odin | Solo Jungle | 13,250 / 14,500 | 135.0 (97.7+37.3) | 167.5 (131.6+35.9) | +24.1% | 84.1 | 104.3 | +24.1% | 8,161 | 8,443 | +3.5% | 7,964 | 9,595 | +20.5% |
| Osiris | Solo | 15,350 / 14,550 | 145.8 (76.7+69.1) | 299.5 (224.8+74.6) | +105.4% | 91.8 | 186.5 | +103.1% | 10,806 | 10,167 | -5.9% | 9,259 | 7,735 | -16.5% |
| Pele | Jungle | 17,000 / 16,100 | 324.1 (318.6+5.4) | 291.9 (284.6+7.3) | -9.9% | 204.0 | 203.0 | -0.5% | 5,163 | 4,307 | -16.6% | 4,674 | 3,817 | -18.3% |
| Poseidon | Mid | 17,500 / 16,600 | 285.3 (212.4+73.0) | 264.1 (182.2+81.8) | -7.5% | 188.0 | 171.5 | -8.8% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Princess Bari | Carry Mid | 14,900 / 15,650 | 199.1 (155.7+43.4) | 372.8 (321.9+50.9) | +87.2% | 134.6 | 234.7 | +74.5% | 4,873 | 4,046 | -17.0% | 4,572 | 3,745 | -18.1% |
| Ra | Mid | 15,200 / 16,300 | 281.6 (147.8+133.8) | 316.1 (150.9+165.1) | +12.2% | 177.3 | 211.0 | +19.0% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Rama | Carry | 13,550 / 16,100 | 372.0 (367.8+4.2) | 560.7 (553.1+7.6) | +50.7% | 245.9 | 339.4 | +38.0% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Ratatoskr | Jungle | 14,700 / 14,300 | 347.7 (291.3+56.4) | 350.7 (279.0+71.8) | +0.9% | 231.2 | 223.8 | -3.2% | 6,419 | 6,419 | +0.0% | 5,689 | 5,689 | +0.0% |
| Scylla | Mid | 14,450 / 16,600 | 241.0 (126.3+114.7) | 332.4 (166.5+165.9) | +37.9% | 157.9 | 216.0 | +36.7% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Sobek | Support | 12,900 / 14,750 | 107.6 (60.3+47.3) | 114.6 (60.3+54.3) | +6.5% | 67.7 | 72.1 | +6.5% | 8,517 | 11,475 | +34.7% | 8,467 | 11,247 | +32.8% |
| Sol | Mid Carry | 16,400 / 16,400 | 246.8 (215.4+31.4) | 277.1 (244.6+32.5) | +12.2% | 159.7 | 187.2 | +17.2% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Sun Wukong | Solo | 11,950 / 14,500 | 61.1 (56.9+4.2) | 179.8 (174.6+5.2) | +194.3% | 38.5 | 112.0 | +191.0% | 7,784 | 10,159 | +30.5% | 7,249 | 7,857 | +8.4% |
| Susano | Jungle | 16,250 / 16,650 | 327.3 (297.7+29.6) | 431.6 (382.9+48.6) | +31.9% | 217.7 | 285.3 | +31.1% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Sylvanus | Support | 13,050 / 14,750 | 72.7 (47.6+25.1) | 71.2 (47.6+23.6) | -2.1% | 45.8 | 44.8 | -2.1% | 9,145 | 11,736 | +28.3% | 7,801 | 11,503 | +47.5% |
| Thanatos | Jungle | 14,050 / 16,650 | 326.8 (244.6+82.2) | 494.6 (372.5+122.0) | +51.3% | 203.2 | 326.9 | +60.9% | 4,655 | 4,655 | +0.0% | 4,126 | 4,126 | +0.0% |
| The Morrigan | Mid | 14,900 / 16,600 | 180.6 (142.2+38.5) | 245.7 (185.1+60.6) | +36.0% | 118.3 | 159.6 | +34.9% | 3,894 | 3,894 | +0.0% | 3,452 | 3,452 | +0.0% |
| Thor | Jungle Solo | 14,300 / 14,600 | 266.8 (227.7+39.1) | 199.4 (172.4+27.0) | -25.3% | 179.5 | 124.2 | -30.8% | 4,559 | 9,019 | +97.8% | 5,392 | 9,486 | +75.9% |
| Tsukuyomi | Jungle | 15,950 / 15,800 | 289.7 (255.2+34.5) | 487.9 (453.8+34.1) | +68.4% | 194.9 | 307.2 | +57.6% | 4,307 | 4,307 | +0.0% | 3,766 | 3,766 | +0.0% |
| Ullr | Carry | 14,600 / 15,300 | 359.0 (259.8+99.2) | 584.3 (496.1+88.2) | +62.8% | 241.6 | 353.7 | +46.4% | 4,148 | 4,148 | +0.0% | 3,644 | 3,644 | +0.0% |
| Vulcan | Mid | 13,500 / 16,600 | 267.2 (122.0+145.2) | 355.9 (186.0+169.8) | +33.2% | 172.9 | 234.4 | +35.6% | 4,015 | 4,015 | +0.0% | 3,630 | 3,630 | +0.0% |
| Xbalanque | Carry | 13,700 / 15,600 | 392.9 (377.6+15.3) | 641.4 (621.2+20.2) | +63.2% | 253.1 | 403.8 | +59.5% | 3,788 | 4,130 | +9.0% | 3,353 | 3,656 | +9.0% |
| Xing Tian | Support Solo | 13,500 / 14,750 | 20.8 (0.0+20.8) | 23.9 (0.0+23.9) | +14.8% | 13.1 | 15.0 | +14.8% | 1,609 | 2,250 | +39.8% | 2,080 | 2,385 | +14.6% |
| Yemoja | Support | 13,900 / 14,750 | 95.9 (91.4+4.5) | 61.8 (57.7+4.0) | -35.6% | 59.7 | 38.9 | -34.8% | 6,932 | 11,912 | +71.8% | 6,436 | 11,675 | +81.4% |
| Ymir | Support | 12,950 / 14,750 | 114.5 (63.3+51.2) | 118.6 (63.3+55.3) | +3.6% | 72.1 | 74.7 | +3.6% | 9,413 | 12,300 | +30.7% | 9,197 | 13,401 | +45.7% |
| Zeus | Mid | 15,300 / 16,600 | 247.4 (147.4+100.0) | 325.7 (208.0+117.7) | +31.7% | 158.0 | 214.6 | +35.8% | 3,894 | 3,894 | +0.0% | 3,452 | 3,452 | +0.0% |
