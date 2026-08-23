# Build quality — `combat.py` pointed at whole builds

_Input fingerprint: `c454186bff12` — items, gods, tags, community builds, weights. Regenerate with `python -m smite.build_quality`; a different fingerprint means different inputs._

> **READ THIS BEFORE ANY NUMBER BELOW.** Of the 138 buildable items, 137 carry passive text and the shipped pricing flags read 13 of them — so **90% of the pool carries passive value this arithmetic cannot see**, and **75% of the community's item slots do** (405 of 537; 89% of ours, 473 of 534). `combat.py` reads exactly one passive — Deathbringer's +35% crit damage. The bias is not even: by the gold model's own residual the community pays **+82g more per slot above its stat line than we do** (mean residual -7g against -89g) and buys fewer stat columns per item (2.80 against 3.41) — that premium IS the passive. **A verdict in our favour is the one to distrust.** The most-bought blind community items are Genji's Guard (29), Shifter's Shield (28), Obsidian Shard (26), Spear of Desolation (23), Shell of Rebuke (21).

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

**community** — 13,950g: Tyrfing · Odysseus' Bow · Silverbranch Bow · The Executioner · Deathbringer · Manchu Bow
  stat line: Attack Damage 60 · Attack Speed % 113 · Critical Chance % 20 · Penetration % 10 · Strength 70
  abilities counted: Acid Spray, Lacerate, Petrify

**ours** — 15,500g: Lernaean Bow · Jotunn's Revenge · Nimble Ring · Death Metal · Rod of Tahuti · Soul Gem
  stat line: Attack Speed % 50 · Cooldown Rate 35 · Critical Chance % 20 · Intelligence 215 · Lifesteal % 15 · Mana Regen 2 · Max Mana 500 · Penetration 10 · Penetration % 5 · Strength 110
  abilities counted: Acid Spray, Lacerate, Petrify

| | basic DPS | ability DPS | TOTAL | EHP physical | EHP magical |
|---|---|---|---|---|---|
| COMMUNITY vs squishy (70) | 409.5 | 37.6 | **447.1** | 3,788 | 3,353 |
| COMMUNITY vs tank (170) | 263.8 | 24.2 | **288.0** | 3,788 | 3,353 |
| OURS vs squishy (70) | 313.1 | 76.5 | **389.5** | 3,788 | 3,353 |
| OURS vs tank (170) | 194.8 | 47.6 | **242.4** | 3,788 | 3,353 |

| per 1000g | DPS vs 70 | DPS vs 170 | EHP physical | EHP magical |
|---|---|---|---|---|
| COMMUNITY | 32.0 | 20.6 | 272 | 240 |
| OURS | 25.1 | 15.6 | 244 | 216 |

## 2. The roster — our `model` core, printed stat lines

89 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 89 | **72** | **13** | 4 | -49.0% | +8.0% | **+27.7%** | +45.6% | +132.1% |
| total DPS vs 170 prot | 89 | **72** | **14** | 3 | -48.3% | +6.8% | **+27.7%** | +42.3% | +128.4% |
| effective health, physical | 89 | **32** | **17** | 40 | -36.7% | +0.0% | **+0.0%** | +9.0% | +226.1% |
| effective health, magical | 89 | **33** | **17** | 39 | -38.5% | +0.0% | **+0.0%** | +9.0% | +224.5% |
| total DPS vs 70 prot per 1000g | 89 | **62** | **26** | 1 | -47.4% | -2.4% | **+19.3%** | +31.6% | +128.1% |
| total DPS vs 170 prot per 1000g | 89 | **64** | **25** | 0 | -46.8% | -2.6% | **+15.5%** | +30.5% | +114.8% |
| effective health, physical per 1000g | 89 | **24** | **64** | 1 | -38.6% | -11.6% | **-7.6%** | +1.1% | +194.0% |
| effective health, magical per 1000g | 89 | **26** | **61** | 2 | -40.3% | -11.4% | **-6.7%** | +4.6% | +192.6% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 14 / 4 / +38.2% | 13 / 5 / +33.3% | 5 / 1 / +0.0% | 5 / 1 / +0.0% |
| Jungle | 17 | 14 / 2 / +24.3% | 15 / 2 / +22.0% | 2 / 4 / +0.0% | 2 / 4 / +0.0% |
| Mid | 22 | 19 / 2 / +24.0% | 19 / 2 / +25.4% | 3 / 2 / +0.0% | 3 / 3 / +0.0% |
| Solo | 18 | 18 / 0 / +58.3% | 18 / 0 / +56.6% | 9 / 9 / -0.3% | 9 / 9 / +1.4% |
| Support | 14 | 7 / 5 / +3.0% | 7 / 5 / +3.0% | 13 / 1 / +39.1% | 14 / 0 / +33.0% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 12 / 5 / +25.2% | 12 / 6 / +21.6% | 2 / 15 / -7.5% | 2 / 15 / -7.5% |
| Jungle | 17 | 13 / 4 / +20.7% | 14 / 3 / +15.2% | 2 / 15 / -9.6% | 2 / 15 / -9.6% |
| Mid | 22 | 17 / 5 / +9.8% | 19 / 3 / +12.4% | 3 / 19 / -8.7% | 3 / 19 / -8.7% |
| Solo | 18 | 16 / 2 / +48.1% | 15 / 3 / +46.5% | 6 / 12 / -4.8% | 6 / 11 / -2.5% |
| Support | 14 | 4 / 10 / -8.8% | 4 / 10 / -8.8% | 11 / 3 / +22.8% | 13 / 1 / +16.6% |

## 3. Judged by role, on each role's own objective

Most roles clear a THRESHOLD and then maximise something else, and one pooled metric cannot represent five roles that do not share an objective. Each row below names both quantities. **The passive blind spot at the top of this report applies to every row here exactly as it applies to the pooled figures** — slicing by role does not escape it, and the bias still runs in our favour.

| Role | n | Threshold | Binds? | Maximised | ahead | behind | tie | median |
|---|---|---|---|---|---|---|---|---|
| Carry | 18 | survive one enemy burst rotation | **no** — 0 of 36 builds fail it | sustained DPS per 1000g | **12** | **5** | 1 | **+25.2%** |
| Jungle | 17 | rotation burst >= a reference squishy's EHP | **no** — all 78 builds fail it | rotation burst per 1000g | **12** | **5** | 0 | **+10.3%** |
| Mid | 22 | rotation burst >= a reference squishy's EHP | **no** — all 78 builds fail it | sustained DPS per 1000g | **17** | **5** | 0 | **+9.8%** |
| Solo | 18 | **none** | – | duel score, EHP x DPS | **17** | **1** | 0 | **+53.4%** |
| Support | 14 | **none** | – | effective health per 1000g | **11** | **3** | 0 | **+22.8%** |

Why each objective is what it is:

- **Carry** — a Carry needs enough effective health to live through one burst — a floor, not a maximand. Buying more than the floor is gold not spent on damage, which is what the pooled metric scored as a win.
- **Jungle** — same kill threshold as Mid, and past it a gank is priced on burst rather than on sustained damage — a Jungler is not standing in the fight for the seconds a DPS figure assumes.
- **Mid** — a Mid's rotation either kills the squishy or it does not; past that the question is how often it comes back.
- **Solo** — not a threshold at all — a RATIO. Their time-to-kill on you over yours on them is (EHP / ref DPS) / (ref EHP / DPS), so the reference opponent CANCELS in ours-over-theirs and what is left is EHP x DPS. A build that doubles effective health and halves damage scores exactly 1.00 — neutral, which is the case neither scalar describes, and it is a property of the algebra rather than of a constant anyone chose.
- **Support** — damage is EXCLUDED, not down-weighted. Most of what a Support is for is in `UNMEASURABLE`, and its damage column is provably empty on 3 of 14 gods.

### Neither threshold binds, and that is a statement about this arithmetic

Both thresholds were defined, measured and left in the table with their measurement, rather than dropped quietly. Re-measured on every run by `threshold_probe`:

| Threshold | population | reference | separates | nearest build |
|---|---|---|---|---|
| Carry: survive one enemy burst rotation | 36 builds | largest burst in the roster at 0 protection — Scylla, ours, 2,952 | **0 of 36** | 1.14x the threshold |
| Mid / Jungle: rotation burst >= a reference squishy's EHP | 78 builds | median effective health of the community's own Carry and Mid builds, magical — 3,399 | **78 of 78** | 0.72x the threshold |

A threshold that separates none of the population and a threshold that separates all of it are equally useless, and one of each is what these are. **Read this as "we cannot currently evaluate a threshold", not as "thresholds do not matter in SMITE"** — the cause is on our side of the arithmetic. A burst here is one cast of every ability with no basic attacks, no item passive, no follow-up and one target, while effective health is full level-20 health plus every protection the six items carry; the two are about an order of magnitude apart. Two things would change the answer and neither is a tuning choice: **a clock** (register §4.12 — a burst window in seconds would let basic attacks into the burst, and it is refused because no source supplies one), or **priced passives** (register §4.5 — ~90% of the pool carries value neither side of this comparison can see). Until one of those exists, Carry, Mid and Jungle are judged on their maximand alone.

### Where the Carry surplus comes from — measured, and currently closed

This section describes a defect that is **not currently present**: our Carry cores buy no more Physical Protection than the community's. It re-measures on every run rather than asserting that, so a refresh or a weight change that brings the surplus back restores the diagnosis in the same paragraph. `offmap_efficiency` is the flag that closed it — see docs/STATE.md §4.15.

Mean defensive stats bought at level 20, community (C) against our `model` core (O):

| Role | n | Physical Protection C / O | Magical Protection C / O | Max Health C / O |
|---|---|---|---|---|
| Carry | 18 | 0.0 / 0.0 | 0.0 / 0.0 | 27.8 / 55.6 |
| Jungle | 17 | 8.5 / 3.8 | 8.5 / 5.9 | 117.6 / 138.2 |
| Mid | 22 | 7.0 / 10.9 | 13.0 / 19.1 | 24.5 / 81.8 |
| Solo | 18 | 118.6 / 104.4 | 115.4 / 107.2 | 798.1 / 894.4 |
| Support | 14 | 88.9 / 137.1 | 111.8 / 166.1 | 437.5 / 953.6 |

The community buys 0.0 Physical Protection across all 18 Carries and we buy 0.0, a surplus of +0.0. The defensive items still reaching a Carry core, with how many of ours hold each against how many of the community's — an EMPTY list here is the measurement, not a missing section:

- **Golden Blade** — ours 5 of 18, community 0 of 18 (Max Health 200)

Two things worth keeping now that the surplus is gone. Effective health is the quantity to read it on, and it is +0.0% physical and +0.0% magical against the community's — LEVEL is the honest target here, not zero, because §4.13 means no threshold in this report can charge us for buying too LITTLE defence, so a figure BELOW the community's would not be visible as a cost. And `defense_affinity` and `draft.archetype_scaled_stats` are **excluded as causes**: both are read only by the viewer's draft overlay (`viewer/src/lib/threats.ts`), which is applied on top of a finished core and never reaches the builds measured here, and `defense_affinity` is 0.0 for Carry in any case because it is derived from the same role map that names no protection for the role. See docs/STATE.md §4.

## 4. The same, for the blended `core` (what the Balanced tab ships)

`core` carries `win` and `pick`, so it is part community build already; the gap between this block and §2 is what the meta signal buys in this arithmetic.

89 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 89 | **70** | **16** | 3 | -41.9% | +5.0% | **+19.1%** | +41.9% | +148.6% |
| total DPS vs 170 prot | 89 | **72** | **14** | 3 | -43.3% | +3.9% | **+20.5%** | +39.9% | +145.8% |
| effective health, physical | 89 | **32** | **17** | 40 | -36.7% | +0.0% | **+0.0%** | +12.3% | +334.8% |
| effective health, magical | 89 | **29** | **20** | 40 | -38.5% | +0.0% | **+0.0%** | +8.9% | +350.7% |
| total DPS vs 70 prot per 1000g | 89 | **61** | **27** | 1 | -44.4% | -7.1% | **+11.6%** | +30.2% | +121.8% |
| total DPS vs 170 prot per 1000g | 89 | **63** | **26** | 0 | -45.8% | -3.9% | **+10.9%** | +28.9% | +119.4% |
| effective health, physical per 1000g | 89 | **28** | **59** | 2 | -36.3% | -12.5% | **-7.3%** | +6.2% | +288.1% |
| effective health, magical per 1000g | 89 | **25** | **62** | 2 | -38.1% | -13.5% | **-7.4%** | +2.2% | +302.3% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 14 / 3 / +24.1% | 14 / 3 / +22.5% | 5 / 1 / +0.0% | 5 / 1 / +0.0% |
| Jungle | 17 | 14 / 3 / +14.5% | 14 / 3 / +12.2% | 2 / 4 / +0.0% | 2 / 4 / +0.0% |
| Mid | 22 | 19 / 3 / +16.8% | 21 / 1 / +20.1% | 3 / 2 / +0.0% | 3 / 3 / +0.0% |
| Solo | 18 | 18 / 0 / +59.3% | 18 / 0 / +57.5% | 9 / 9 / -1.5% | 6 / 11 / -5.8% |
| Support | 14 | 5 / 7 / -2.1% | 5 / 7 / -2.1% | 13 / 1 / +43.9% | 13 / 1 / +46.1% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 13 / 5 / +25.6% | 13 / 5 / +18.7% | 3 / 15 / -8.6% | 3 / 15 / -8.6% |
| Jungle | 17 | 13 / 4 / +11.1% | 13 / 4 / +5.6% | 2 / 14 / -8.8% | 2 / 14 / -8.8% |
| Mid | 22 | 15 / 6 / +3.0% | 17 / 5 / +7.9% | 3 / 18 / -9.0% | 3 / 18 / -9.0% |
| Solo | 18 | 16 / 2 / +46.6% | 16 / 2 / +45.0% | 7 / 11 / -7.6% | 6 / 12 / -13.1% |
| Support | 14 | 4 / 10 / -14.7% | 4 / 10 / -14.7% | 13 / 1 / +26.8% | 11 / 3 / +27.5% |

## 5. Sensitivity — the passives the gold model CAN price

Same as §2 with the shipped pricing flags applied to every stat line: the Adaptive Stat grants (`price_adaptive`) and the mana conversions (`price_conversions`). This is the one slice of the blind spot that can be put on the table; the other 124 items stay invisible here too.

89 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 89 | **72** | **14** | 3 | -61.7% | +6.5% | **+22.8%** | +44.9% | +132.1% |
| total DPS vs 170 prot | 89 | **72** | **14** | 3 | -61.3% | +6.8% | **+21.5%** | +42.9% | +128.4% |
| effective health, physical | 89 | **32** | **17** | 40 | -36.7% | +0.0% | **+0.0%** | +9.0% | +226.1% |
| effective health, magical | 89 | **33** | **17** | 39 | -38.5% | +0.0% | **+0.0%** | +9.0% | +224.5% |
| total DPS vs 70 prot per 1000g | 89 | **64** | **25** | 0 | -60.6% | -2.8% | **+14.6%** | +27.6% | +128.1% |
| total DPS vs 170 prot per 1000g | 89 | **64** | **24** | 1 | -60.1% | -2.4% | **+13.8%** | +25.1% | +114.8% |
| effective health, physical per 1000g | 89 | **24** | **64** | 1 | -38.6% | -11.6% | **-7.6%** | +1.1% | +194.0% |
| effective health, magical per 1000g | 89 | **26** | **61** | 2 | -40.3% | -11.4% | **-6.7%** | +4.6% | +192.6% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 14 / 4 / +27.0% | 14 / 4 / +18.6% | 5 / 1 / +0.0% | 5 / 1 / +0.0% |
| Jungle | 17 | 15 / 2 / +20.7% | 15 / 2 / +21.5% | 2 / 4 / +0.0% | 2 / 4 / +0.0% |
| Mid | 22 | 18 / 3 / +20.6% | 18 / 3 / +21.6% | 3 / 2 / +0.0% | 3 / 3 / +0.0% |
| Solo | 18 | 18 / 0 / +58.3% | 18 / 0 / +56.6% | 9 / 9 / -0.3% | 9 / 9 / +1.4% |
| Support | 14 | 7 / 5 / +3.0% | 7 / 5 / +3.0% | 13 / 1 / +39.1% | 14 / 0 / +33.0% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 13 / 5 / +17.9% | 12 / 5 / +10.9% | 2 / 15 / -7.5% | 2 / 15 / -7.5% |
| Jungle | 17 | 14 / 3 / +16.2% | 14 / 3 / +14.8% | 2 / 15 / -9.6% | 2 / 15 / -9.6% |
| Mid | 22 | 18 / 4 / +9.0% | 18 / 4 / +10.8% | 3 / 19 / -8.7% | 3 / 19 / -8.7% |
| Solo | 18 | 15 / 3 / +48.1% | 16 / 2 / +46.5% | 6 / 12 / -4.8% | 6 / 11 / -2.5% |
| Support | 14 | 4 / 10 / -8.8% | 4 / 10 / -8.8% | 11 / 3 / +22.8% | 13 / 1 / +16.6% |

Verdict on DPS vs 70 flips for 2 god(s) between §2 and §5: Pele (-0.8 → +12.8), Poseidon (+20.9 → -33.5).

## 6. The blind spot, measured

| | buildable pool | community slots | our `model` slots |
|---|---|---|---|
| items / slots | 138 | 537 | 534 |
| carrying unpriced passive text | 124 (89.9%) | 405 (75.4%) | 473 (88.6%) |
| mean gold residual per slot (cost − stat-line prediction) | – | -7g | -89g |
| mean stat columns per item | – | 2.80 | 3.41 |

Passives the shipped flags price (13): Book of Thoth, Brawler’s Beat Stick, Daybreak Gavel, Deathbringer, Eye of Erebus, Mercury's Talaria, Nimble Ring, Omen Drum, Rod of Tahuti, Sun Beam Bow, The Executioner, Transcendence, Vital Amplifier.

Most-bought blind items — community: Genji's Guard (29), Shifter's Shield (28), Obsidian Shard (26), Spear of Desolation (23), Shell of Rebuke (21). Ours: Jotunn's Revenge (52), Kinetic Cuirass (36), Amanita Charm (35), Freya's Tears (30), Spear of Desolation (29).

## 7. Every god — `model` core, printed stat lines

C = community, O = ours. DPS vs 70 is shown as total (basic + ability).

| God | Role | Gold C / O | DPS vs 70 — C (basic+ability) | O (basic+ability) | Δ | DPS vs 170 — C | O | Δ | EHP phys — C | O | Δ | EHP mag — C | O | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Achilles | Solo Jungle | 13,250 / 14,600 | 92.6 (57.6+35.0) | 213.8 (166.1+47.7) | +131.0% | 58.3 | 133.1 | +128.4% | 11,400 | 9,039 | -20.7% | 9,792 | 9,283 | -5.2% |
| Agni | Mid | 15,650 / 16,600 | 229.8 (161.8+68.0) | 267.0 (183.2+83.7) | +16.2% | 146.7 | 173.4 | +18.2% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Ah Puch | Mid | 15,650 / 16,600 | 180.8 (132.7+48.1) | 225.1 (169.1+56.0) | +24.5% | 118.4 | 146.2 | +23.4% | 4,347 | 4,347 | +0.0% | 3,862 | 3,862 | +0.0% |
| Aladdin | Jungle | 13,550 / 15,900 | 109.2 (102.5+6.7) | 168.7 (160.4+8.3) | +54.5% | 71.6 | 106.2 | +48.5% | 4,233 | 4,233 | +0.0% | 3,846 | 3,846 | +0.0% |
| Amaterasu | Solo | 12,750 / 14,500 | 122.3 (108.1+14.2) | 132.0 (105.4+26.6) | +8.0% | 77.0 | 82.2 | +6.8% | 11,704 | 8,296 | -29.1% | 7,976 | 9,476 | +18.8% |
| Anhur | Carry | 13,750 / 15,150 | 407.2 (371.4+35.8) | 586.2 (524.2+61.9) | +43.9% | 269.2 | 364.5 | +35.4% | 4,148 | 4,493 | +8.3% | 3,644 | 3,947 | +8.3% |
| Anubis | Mid | 15,000 / 16,600 | 148.9 (125.4+23.5) | 195.5 (166.5+29.0) | +31.3% | 97.6 | 127.0 | +30.2% | 4,202 | 4,202 | +0.0% | 3,912 | 3,912 | +0.0% |
| Aphrodite | Mid Support | 12,300 / 15,350 | 137.7 (84.0+53.7) | 130.1 (82.4+47.7) | -5.5% | 87.6 | 81.0 | -7.6% | 4,755 | 7,029 | +47.8% | 4,615 | 8,258 | +78.9% |
| Apollo | Carry | 13,750 / 15,150 | 391.3 (357.9+33.4) | 569.9 (512.0+57.8) | +45.6% | 258.7 | 354.4 | +37.0% | 4,076 | 4,421 | +8.5% | 3,580 | 3,883 | +8.5% |
| Ares | Support | 12,800 / 14,750 | 60.3 (60.3+0.0) | 87.9 (87.9+0.0) | +45.8% | 37.9 | 54.7 | +44.2% | 9,868 | 10,187 | +3.2% | 8,565 | 11,383 | +32.9% |
| Artemis | Carry | 13,700 / 15,850 | 401.1 (379.6+21.6) | 659.5 (616.4+43.1) | +64.4% | 258.4 | 390.3 | +51.0% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Artio | Solo Support | 13,350 / 14,800 | 100.3 (58.3+42.0) | 171.5 (115.3+56.2) | +71.1% | 63.1 | 106.8 | +69.2% | 10,100 | 10,438 | +3.3% | 9,166 | 9,864 | +7.6% |
| Athena | Support | 13,350 / 14,750 | 117.6 (84.4+33.2) | 159.3 (122.6+36.6) | +35.4% | 74.0 | 99.2 | +33.9% | 10,758 | 10,187 | -5.3% | 9,271 | 11,383 | +22.8% |
| Atlas | Support | 13,350 / 14,750 | 100.9 (83.7+17.2) | 91.2 (72.9+18.2) | -9.6% | 63.5 | 57.4 | -9.6% | 8,661 | 11,736 | +35.5% | 9,955 | 11,503 | +15.5% |
| Awilix | Jungle | 15,550 / 16,650 | 318.4 (252.7+65.8) | 485.4 (350.9+134.5) | +52.4% | 200.5 | 320.9 | +60.0% | 4,959 | 4,117 | -17.0% | 4,594 | 3,752 | -18.3% |
| Bacchus | Support | 13,300 / 14,750 | 88.9 (60.3+28.7) | 124.7 (87.9+36.8) | +40.2% | 56.0 | 77.6 | +38.7% | 9,339 | 10,040 | +7.5% | 10,637 | 11,460 | +7.7% |
| Baron Samedi | Mid Support | 13,700 / 15,350 | 176.1 (82.4+93.7) | 176.1 (82.4+93.7) | +0.0% | 109.6 | 109.6 | +0.0% | 5,762 | 7,029 | +22.0% | 5,607 | 8,258 | +47.3% |
| Bastet | Jungle | 15,050 / 16,650 | 344.1 (286.4+57.8) | 417.2 (343.9+73.3) | +21.2% | 226.0 | 275.8 | +22.0% | 4,117 | 4,117 | +0.0% | 3,702 | 3,702 | +0.0% |
| Bellona | Solo | 13,700 / 14,800 | 142.6 (117.1+25.4) | 186.1 (142.6+43.5) | +30.5% | 89.8 | 115.9 | +29.1% | 10,730 | 10,251 | -4.5% | 9,758 | 9,475 | -2.9% |
| Cabrakan | Solo Support | 13,250 / 14,800 | 118.1 (63.3+54.8) | 187.2 (121.6+65.7) | +58.6% | 74.3 | 116.6 | +56.8% | 10,164 | 10,438 | +2.7% | 8,670 | 9,864 | +13.8% |
| Cerberus | Solo Support | 13,600 / 14,750 | 82.0 (52.2+29.8) | 86.4 (52.2+34.2) | +5.4% | 51.6 | 54.4 | +5.4% | 9,499 | 11,614 | +22.3% | 10,797 | 11,460 | +6.1% |
| Cernunnos | Carry Jungle | 13,900 / 15,650 | 359.9 (340.1+19.8) | 286.6 (250.3+36.4) | -20.3% | 237.9 | 173.9 | -26.9% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Chaac | Solo | 13,800 / 15,100 | 180.8 (100.4+80.4) | 199.5 (106.1+93.5) | +10.3% | 116.5 | 125.6 | +7.8% | 7,260 | 7,839 | +8.0% | 8,381 | 9,082 | +8.4% |
| Charon | Support | 14,800 / 14,750 | 158.4 (93.4+64.9) | 102.0 (55.4+46.5) | -35.6% | 101.0 | 64.2 | -36.4% | 6,000 | 11,614 | +93.6% | 5,374 | 11,383 | +111.8% |
| Chiron | Carry | 13,100 / 15,600 | 308.8 (254.5+54.3) | 627.1 (553.2+73.9) | +103.1% | 196.7 | 389.3 | +97.9% | 4,644 | 3,788 | -18.4% | 4,110 | 3,353 | -18.4% |
| Chronos | Mid Carry | 14,700 / 16,400 | 251.7 (153.6+98.1) | 339.9 (224.3+115.6) | +35.0% | 164.9 | 229.7 | +39.3% | 4,016 | 4,016 | +0.0% | 3,630 | 3,630 | +0.0% |
| Cu Chulainn | Solo | 13,500 / 14,550 | 136.3 (36.2+100.1) | 242.4 (130.3+112.1) | +77.9% | 85.8 | 150.9 | +75.9% | 10,898 | 10,282 | -5.6% | 9,616 | 7,901 | -17.8% |
| Cupid | Carry | 13,550 / 15,650 | 385.1 (367.8+17.4) | 293.6 (254.2+39.4) | -23.8% | 254.6 | 178.1 | -30.0% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Da Ji | Jungle | 14,450 / 16,100 | 338.8 (279.2+59.6) | 371.4 (303.0+68.4) | +9.6% | 228.0 | 258.3 | +13.3% | 3,865 | 3,865 | +0.0% | 3,452 | 3,452 | +0.0% |
| Danzaburou | Carry | 14,550 / 15,500 | 329.9 (233.8+96.2) | 431.9 (327.1+104.9) | +30.9% | 207.7 | 268.8 | +29.4% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Discordia | Mid | 15,100 / 16,600 | 234.0 (153.4+80.6) | 263.5 (172.8+90.7) | +12.6% | 147.4 | 171.2 | +16.2% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Eset | Mid | 14,750 / 16,600 | 202.9 (137.2+65.8) | 303.3 (206.2+97.2) | +49.5% | 132.9 | 197.0 | +48.2% | 4,202 | 3,760 | -10.5% | 5,058 | 3,399 | -32.8% |
| Fenrir | Jungle | 16,150 / 16,650 | 291.0 (239.4+51.6) | 434.3 (356.7+77.6) | +49.3% | 191.1 | 287.1 | +50.2% | 7,226 | 4,571 | -36.7% | 6,587 | 4,052 | -38.5% |
| Ganesha | Support | 12,850 / 14,750 | 99.2 (59.5+39.7) | 105.1 (59.5+45.6) | +5.9% | 62.5 | 66.2 | +5.9% | 8,291 | 11,613 | +40.1% | 8,547 | 11,383 | +33.2% |
| Geb | Support | 12,950 / 14,700 | 109.4 (58.3+51.1) | 103.7 (58.3+45.4) | -5.2% | 68.9 | 65.3 | -5.2% | 7,428 | 14,002 | +88.5% | 8,516 | 12,929 | +51.8% |
| Gilgamesh | Solo Jungle | 15,750 / 14,550 | 201.8 (169.6+32.2) | 244.9 (209.8+35.1) | +21.4% | 127.1 | 152.5 | +20.0% | 9,520 | 10,373 | +9.0% | 7,406 | 7,901 | +6.7% |
| Guan Yu | Solo Support | 15,200 / 14,500 | 105.5 (77.7+27.8) | 167.7 (135.9+31.9) | +59.0% | 66.4 | 104.4 | +57.3% | 9,933 | 9,611 | -3.2% | 9,781 | 9,611 | -1.7% |
| Hades | Solo | 14,750 / 15,950 | 151.4 (90.7+60.7) | 207.1 (118.4+88.7) | +36.8% | 94.2 | 135.7 | +44.0% | 7,086 | 6,732 | -5.0% | 6,629 | 6,298 | -5.0% |
| Hecate | Mid | 14,700 / 16,600 | 285.6 (130.0+155.6) | 364.7 (166.5+198.2) | +27.7% | 184.8 | 236.9 | +28.2% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Hercules | Solo | 15,050 / 14,800 | 125.8 (70.0+55.8) | 198.9 (136.6+62.4) | +58.1% | 79.2 | 123.9 | +56.3% | 10,112 | 9,783 | -3.3% | 8,860 | 9,254 | +4.5% |
| Horus | Support | 13,300 / 14,750 | 65.3 (61.2+4.1) | 94.0 (89.4+4.6) | +43.9% | 41.1 | 58.5 | +42.3% | 8,603 | 9,645 | +12.1% | 8,326 | 10,814 | +29.9% |
| Hou Yi | Carry | 13,750 / 15,400 | 404.5 (368.1+36.4) | 453.5 (386.8+66.7) | +12.1% | 267.4 | 285.5 | +6.8% | 4,076 | 4,076 | +0.0% | 3,580 | 3,580 | +0.0% |
| Hua Mulan | Solo | 13,550 / 14,550 | 105.7 (65.3+40.4) | 202.3 (152.5+49.7) | +91.3% | 66.6 | 125.9 | +89.2% | 9,991 | 10,432 | +4.4% | 9,714 | 8,380 | -13.7% |
| Hun Batz | Jungle | 16,150 / 16,650 | 381.4 (274.7+106.8) | 483.9 (346.4+137.5) | +26.9% | 250.6 | 319.9 | +27.7% | 4,233 | 4,233 | +0.0% | 3,752 | 3,752 | +0.0% |
| Ishtar | Carry | 15,400 / 15,600 | 440.4 (430.8+9.5) | 616.8 (604.5+12.3) | +40.1% | 291.1 | 388.4 | +33.4% | 3,861 | 4,203 | +8.9% | 3,416 | 3,719 | +8.9% |
| Ix Chel | Mid Support | 15,200 / 15,350 | 367.4 (141.9+225.5) | 223.1 (77.5+145.6) | -39.3% | 231.3 | 138.8 | -40.0% | 3,866 | 7,164 | +85.3% | 3,595 | 8,508 | +136.6% |
| Izanami | Carry | 13,550 / 15,500 | 375.5 (356.6+18.9) | 378.1 (324.6+53.4) | +0.7% | 248.2 | 235.3 | -5.2% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Janus | Mid | 14,700 / 16,600 | 245.6 (130.0+115.5) | 313.8 (166.5+147.3) | +27.8% | 158.9 | 203.8 | +28.3% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Jing Wei | Carry | 14,250 / 15,600 | 470.5 (448.3+22.2) | 641.6 (616.6+25.0) | +36.4% | 303.1 | 404.0 | +33.3% | 3,788 | 4,130 | +9.0% | 3,353 | 3,656 | +9.0% |
| Jormungandr | Solo Support | 13,750 / 14,550 | 134.1 (70.8+63.3) | 178.9 (108.0+70.9) | +33.5% | 84.4 | 111.4 | +32.0% | 8,445 | 10,772 | +27.6% | 8,394 | 8,849 | +5.4% |
| Kali | Jungle | 15,150 / 15,600 | 285.6 (260.3+25.4) | 355.1 (304.4+50.8) | +24.3% | 184.0 | 218.3 | +18.6% | 4,233 | 4,233 | +0.0% | 3,752 | 3,752 | +0.0% |
| Khepri | Support | 15,200 / 14,750 | 195.4 (139.7+55.7) | 99.8 (58.3+41.4) | -49.0% | 121.6 | 62.8 | -48.3% | 4,796 | 11,736 | +144.7% | 4,227 | 11,503 | +172.1% |
| Kukulkan | Mid | 16,250 / 16,600 | 205.7 (125.7+79.9) | 276.0 (166.5+109.5) | +34.2% | 131.3 | 179.3 | +36.5% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Loki | Jungle | 14,450 / 16,300 | 227.0 (209.7+17.2) | 323.7 (303.1+20.6) | +42.6% | 152.7 | 206.9 | +35.5% | 4,117 | 4,117 | +0.0% | 3,702 | 3,702 | +0.0% |
| Medusa | Carry | 13,950 / 15,500 | 447.1 (409.5+37.6) | 389.5 (313.1+76.5) | -12.9% | 288.0 | 242.4 | -15.8% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Mercury | Jungle | 14,700 / 16,050 | 489.6 (480.9+8.8) | 388.4 (372.3+16.1) | -20.7% | 333.1 | 255.1 | -23.4% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Merlin | Mid | 15,350 / 16,600 | 328.1 (138.6+189.5) | 360.8 (166.5+194.3) | +10.0% | 209.5 | 234.4 | +11.9% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Mordred | Solo Jungle | 14,800 / 15,150 | 101.2 (62.8+38.5) | 192.6 (137.4+55.1) | +90.2% | 63.7 | 121.2 | +90.2% | 12,501 | 8,443 | -32.5% | 10,124 | 7,919 | -21.8% |
| Morgan Le Fay | Mid | 15,050 / 16,600 | 205.7 (126.4+79.4) | 264.4 (175.6+88.8) | +28.5% | 134.8 | 171.7 | +27.4% | 4,015 | 4,015 | +0.0% | 4,929 | 3,630 | -26.4% |
| Ne Zha | Jungle | 14,850 / 16,100 | 377.4 (351.2+26.2) | 434.3 (397.8+36.5) | +15.1% | 254.0 | 302.0 | +18.9% | 5,708 | 4,233 | -25.8% | 5,167 | 3,752 | -27.4% |
| Neith | Carry Mid | 14,800 / 15,650 | 296.1 (184.3+111.8) | 385.2 (243.0+142.2) | +30.1% | 189.1 | 233.7 | +23.6% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Nemesis | Jungle | 16,200 / 15,800 | 271.8 (226.1+45.7) | 500.1 (457.8+42.3) | +84.0% | 182.9 | 314.8 | +72.1% | 5,437 | 4,233 | -22.1% | 4,896 | 3,752 | -23.4% |
| Nu Wa | Mid | 15,200 / 16,600 | 251.3 (166.9+84.4) | 282.3 (187.0+95.2) | +12.3% | 158.2 | 183.3 | +15.9% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Nut | Carry Mid | 16,200 / 16,300 | 352.1 (336.1+16.0) | 262.3 (233.6+28.7) | -25.5% | 243.4 | 175.1 | -28.1% | 4,045 | 4,045 | +0.0% | 3,580 | 3,580 | +0.0% |
| Odin | Solo Jungle | 13,400 / 14,500 | 135.0 (97.7+37.3) | 167.5 (131.6+35.9) | +24.1% | 84.1 | 104.3 | +24.1% | 7,749 | 8,443 | +9.0% | 7,552 | 9,595 | +27.1% |
| Osiris | Solo | 13,300 / 14,550 | 130.3 (81.0+49.3) | 299.5 (224.8+74.6) | +129.7% | 82.1 | 186.5 | +127.2% | 12,363 | 10,167 | -17.8% | 8,577 | 7,735 | -9.8% |
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
| Ymir | Support | 13,400 / 14,750 | 110.4 (63.3+47.1) | 118.6 (63.3+55.3) | +7.4% | 69.5 | 74.7 | +7.4% | 10,632 | 12,300 | +15.7% | 10,754 | 13,401 | +24.6% |
| Zeus | Mid | 15,050 / 16,600 | 243.8 (140.1+103.7) | 325.7 (208.0+117.7) | +33.6% | 157.8 | 214.6 | +36.0% | 5,050 | 3,894 | -22.9% | 4,548 | 3,452 | -24.1% |
