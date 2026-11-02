# Build quality — `combat.py` pointed at whole builds

_Input fingerprint: `ecd7b1249f43` — items, gods, tags, community builds, weights. Regenerate with `python -m smite.build_quality`; a different fingerprint means different inputs._

> **READ THIS BEFORE ANY NUMBER BELOW.** Of the 138 buildable items, 137 carry passive text and the shipped pricing flags read 14 of them — so **89% of the pool carries passive value this arithmetic cannot see**, and **73% of the community's item slots do** (397 of 543; 89% of ours, 483 of 540). `combat.py` reads exactly one passive — Deathbringer's +35% crit damage. The bias is not even: by the gold model's own residual the community pays **+134g more per slot above its stat line than we do** (mean residual +26g against -108g) and buys fewer stat columns per item (2.68 against 3.37) — that premium IS the passive. **A verdict in our favour is the one to distrust.** The most-bought blind community items are Freya's Tears (34), Obsidian Shard (24), Spear of Desolation (21), Devourer's Gauntlet (20), Shell of Rebuke (17).

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

**community** — 13,950g: Devourer's Gauntlet · Dagger of Frenzy · Dominance · Riptalon · Silverbranch Bow · Manchu Bow
  stat line: Attack Damage 75 · Attack Speed % 98 · Lifesteal % 12.5 · Mana Regen 4 · Max Mana 150 · Penetration % 20 · Strength 75
  abilities counted: Acid Spray, Lacerate, Petrify

**ours** — 15,550g: Jotunn's Revenge · Death Metal · Nimble Ring · Tekko-Kagi · Rod of Tahuti · Soul Gem
  stat line: Attack Speed % 40 · Cooldown Rate 35 · Critical Chance % 20 · Intelligence 220 · Lifesteal % 15 · Mana Regen 2 · Max Mana 500 · Penetration 20 · Penetration % 5 · Strength 110
  abilities counted: Acid Spray, Lacerate, Petrify

| | basic DPS | ability DPS | TOTAL | EHP physical | EHP magical |
|---|---|---|---|---|---|
| COMMUNITY vs squishy (70) | 372.1 | 39.6 | **411.7** | 3,788 | 3,353 |
| COMMUNITY vs tank (170) | 246.0 | 26.2 | **272.1** | 3,788 | 3,353 |
| OURS vs squishy (70) | 313.5 | 82.2 | **395.7** | 3,788 | 3,353 |
| OURS vs tank (170) | 190.2 | 49.8 | **240.0** | 3,788 | 3,353 |

| per 1000g | DPS vs 70 | DPS vs 170 | EHP physical | EHP magical |
|---|---|---|---|---|
| COMMUNITY | 29.5 | 19.5 | 272 | 240 |
| OURS | 25.4 | 15.4 | 244 | 216 |

## 2. The roster — our `model` core, printed stat lines

90 gods compared.

Community six, labelled (`community_target`): on 68 gods it holds an **unfinished** component (72 slots — the match ended before the build did), and on 20 an **unscoreable** statless relic or god Mod (20 slots). Combat still runs on the six as bought, so on those gods "ahead" is partly ahead of a half-built item and is not a disagreement about what to finish on.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 90 | **75** | **13** | 2 | -39.1% | +6.8% | **+30.1%** | +53.3% | +174.0% |
| total DPS vs 170 prot | 90 | **74** | **14** | 2 | -39.8% | +5.8% | **+25.9%** | +49.2% | +172.6% |
| effective health, physical | 90 | **34** | **14** | 42 | -47.4% | +0.0% | **+0.0%** | +11.2% | +87.0% |
| effective health, magical | 90 | **39** | **8** | 43 | -45.4% | +0.0% | **+0.0%** | +20.8% | +141.9% |
| total DPS vs 70 prot per 1000g | 90 | **65** | **23** | 2 | -40.3% | -1.0% | **+20.8%** | +40.4% | +151.2% |
| total DPS vs 170 prot per 1000g | 90 | **63** | **24** | 3 | -41.0% | -1.8% | **+17.2%** | +36.5% | +150.0% |
| effective health, physical per 1000g | 90 | **34** | **53** | 3 | -51.7% | -11.8% | **-5.1%** | +9.0% | +98.7% |
| effective health, magical per 1000g | 90 | **39** | **49** | 2 | -48.2% | -10.9% | **-3.2%** | +15.4% | +128.2% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 13 / 4 / +32.4% | 12 / 5 / +21.2% | 5 / 0 / +0.0% | 5 / 0 / +0.0% |
| Jungle | 18 | 16 / 1 / +40.2% | 15 / 2 / +36.4% | 3 / 3 / +0.0% | 3 / 3 / +0.0% |
| Mid | 22 | 19 / 3 / +28.5% | 19 / 3 / +29.4% | 3 / 2 / +0.0% | 2 / 3 / +0.0% |
| Solo | 18 | 17 / 1 / +40.8% | 18 / 0 / +40.1% | 12 / 6 / +12.6% | 15 / 2 / +15.3% |
| Support | 14 | 10 / 4 / +6.5% | 10 / 4 / +6.5% | 11 / 3 / +22.4% | 14 / 0 / +40.9% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 12 / 6 / +21.4% | 12 / 6 / +15.0% | 5 / 12 / -4.1% | 5 / 12 / -4.1% |
| Jungle | 18 | 15 / 3 / +30.6% | 15 / 3 / +29.0% | 4 / 14 / -10.1% | 4 / 14 / -10.1% |
| Mid | 22 | 18 / 4 / +11.5% | 16 / 5 / +10.1% | 3 / 18 / -8.5% | 3 / 18 / -8.5% |
| Solo | 18 | 16 / 1 / +35.3% | 16 / 1 / +33.8% | 13 / 5 / +8.6% | 13 / 5 / +15.1% |
| Support | 14 | 4 / 9 / -3.0% | 4 / 9 / -2.6% | 9 / 4 / +10.9% | 14 / 0 / +25.8% |

## 3. Judged by role, on each role's own objective

Most roles clear a THRESHOLD and then maximise something else, and one pooled metric cannot represent five roles that do not share an objective. Each row below names both quantities. **The passive blind spot at the top of this report applies to every row here exactly as it applies to the pooled figures** — slicing by role does not escape it, and the bias still runs in our favour.

**An objective containing effective health is scored on BOTH damage channels and read as the interval between them.** A build has one damage output and two effective healths; which one its survival is read on is a property of the ATTACKER, and there is no attacker in this comparison. Against a stream that is a share `f` physical, effective health is `1 / (f/EHP_p + (1-f)/EHP_m)` — a weighted harmonic mean, because what averages over a mixed stream is the damage-taken multiplier and not its reciprocal — and the ours-over-theirs ratio is monotone in `f`, so **every possible damage mix lands between the two channels and the pair is the whole range**. `ahead` below therefore means ahead at every mix, `behind` means behind at every mix, and `mix-dependent` means the answer is a fact about the enemy team that this comparison does not contain. Averaging the two channels would assert equal exposure, which is a constant no source here supplies — and would not even be the answer to its own question, since the correct collapse at 50/50 is harmonic and not arithmetic. Until 2026-08-23 both roles read `ehp_physical` alone, i.e. the two roles whose job is durability were scored on half the damage in the game.

| Role | n | Threshold | Binds? | Maximised | ahead | behind | level | mix-dependent | median |
|---|---|---|---|---|---|---|---|---|---|
| Carry | 18 | survive one enemy burst rotation | **no** — 0 of 36 builds fail it | sustained DPS per 1000g | **12** | **6** | 0 | – (no EHP term) | **+21.4%** |
| Jungle | 18 | rotation burst >= a reference squishy's EHP | **no** — all 80 builds fail it | rotation burst per 1000g | **13** | **5** | 0 | – (no EHP term) | **+11.9%** |
| Mid | 22 | rotation burst >= a reference squishy's EHP | **no** — all 80 builds fail it | sustained DPS per 1000g | **18** | **4** | 0 | – (no EHP term) | **+11.5%** |
| Solo | 18 | **none** | – | duel score, EHP x DPS | **18** | **0** | 0 | **0** | **+59.0% … +68.0%** |
| Support | 14 | **none** | – | effective health per 1000g | **9** | **0** | 1 | **4** | **+10.9% … +25.8%** |

Builds whose verdict the damage mix decides — the interval spans both answers, so neither is available here:

- **Bacchus** (Support) — vs a physical opponent -14.1% · vs a magical opponent +25.3%
- **Horus** (Support) — vs a physical opponent -4.6% · vs a magical opponent +4.2%
- **Sylvanus** (Support) — vs a physical opponent -17.2% · vs a magical opponent +11.7%
- **Ymir** (Support) — vs a physical opponent -11.3% · vs a magical opponent +26.2%

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
| Jungle | 18 | 16.1 / 10.0 | 11.1 / 7.5 | 111.1 / 161.1 |
| Mid | 22 | 6.4 / 10.9 | 10.5 / 18.4 | 60.2 / 81.8 |
| Solo | 18 | 97.8 / 107.2 | 83.8 / 96.4 | 603.3 / 863.9 |
| Support | 14 | 106.4 / 140.4 | 82.6 / 159.3 | 667.1 / 889.3 |

The community buys 0.0 Physical Protection across all 18 Carries and we buy 0.0, a surplus of +0.0. The defensive items still reaching a Carry core, with how many of ours hold each against how many of the community's — an EMPTY list here is the measurement, not a missing section:

- **Golden Blade** — ours 5 of 18, community 0 of 18 (Max Health 200)

Two things worth keeping now that the surplus is gone. Effective health is the quantity to read it on, and it is +0.0% physical and +0.0% magical against the community's — LEVEL is the honest target here, not zero, because §4.13 means no threshold in this report can charge us for buying too LITTLE defence, so a figure BELOW the community's would not be visible as a cost. And `defense_affinity` and `draft.archetype_scaled_stats` are **excluded as causes**: both are read only by the viewer's draft overlay (`viewer/src/lib/threats.ts`), which is applied on top of a finished core and never reaches the builds measured here, and `defense_affinity` is 0.0 for Carry in any case because it is derived from the same role map that names no protection for the role. See docs/STATE.md §4.

### Where the off-map charge lands — measured on every run

`offmap_efficiency` ships at **0.55** and charges an item for the gold it spent on stats the god's fit map does not name (STATE.md §3, §4.15). This is what that bill is made of in our own cores, at full strength — the charge is linear in the strength, so the shipped value scales every row equally. **Nothing here changes a build**; it is here because every attempt on this charge so far has had to rebuild the composition by hand against a dataset that had moved under the previous one.

| Role | n | off-map gold in our cores | largest lines |
|---|---|---|---|
| Carry | 18 | 1,290g | Max Health 100.0% |
| Jungle | 18 | 7,943g | Attack Speed 46.4%, Lifesteal 28.6%, Max Health 19.5%, Tenacity 4.9%, Pathfinding 0.6% |
| Mid | 22 | 4,803g | Lifesteal 87.5%, Plating 12.5% |
| Solo | 18 | 6,861g | Attack Speed 52.3%, Plating 43.9%, Lifesteal 3.8% |
| Support | 14 | 4,404g | Plating 63.8%, Attack Speed 36.2% |

And what the two mechanical tests of §4.16 say about each stat being billed. A stat named by SOME role map has a CONTRAST, so another role's silence about it is a positive statement by the same table and charging it is legitimate; a stat named NOWHERE has no contrast to read. The second column is test (ii) — if `combat.py` can see the stat then charging it is a hypothesis this report can check, which is why it may not simply be exempted.

| Stat | named by `role_stats` | `combat.py` | on `offmap_exempt` |
|---|---|---|---|
| Attack Speed | 5 of 21 (Carry, Constant, Hunter, Pressure, Sharpshooter) | attack_dps | no |
| Lifesteal | 3 of 21 (Carry, Hunter, Sharpshooter) | LIFESTEAL_MINION_SCALE | no |
| Plating | 0 of 21 — **nowhere** | flat_reduction_multiplier — **on the target only** | no |
| Max Health | 6 of 21 (Brawler, Guardian, Solo, Support, Tank, Warrior) | effective_health | no |
| Tenacity | 0 of 21 — **nowhere** | TENACITY_CAP | no |
| Pathfinding | 0 of 21 — **nowhere** | PATHFINDING_COMBAT_SCALE | no |

**No verdict is drawn here**, and that is deliberate: deciding whether a line in the first table is a defect needs the community's own record and the leakage-free coverage gate as well, and both live outside this module. The verdicts reached so far are register §4.15 (the defect stats — charge them), §4.16 (mana and the regens — exempt them), §4.18 (Echo — charge it, and why the role that pays most for it is not being wronged) and §4.19 (Plating and Dampening — charge them, because the check cannot be run and sparing either changes nothing in the mode that has a gate).

A row reading **on the target only** is the one case this report cannot adjudicate at all: `combat.py` prices the stat on an OPPONENT and nothing reads it off the build being judged, so a charge on it is neither confirmed nor refuted by anything above. See `TARGET_SIDE_ONLY`.

## 4. The same, for the blended `core` (what the Balanced tab ships)

`core` carries `win` and `pick`, so it is part community build already; the gap between this block and §2 is what the meta signal buys in this arithmetic.

90 gods compared.

Community six, labelled (`community_target`): on 68 gods it holds an **unfinished** component (72 slots — the match ended before the build did), and on 20 an **unscoreable** statless relic or god Mod (20 slots). Combat still runs on the six as bought, so on those gods "ahead" is partly ahead of a half-built item and is not a disagreement about what to finish on.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 90 | **78** | **12** | 0 | -38.4% | +7.5% | **+23.3%** | +44.7% | +150.1% |
| total DPS vs 170 prot | 90 | **75** | **12** | 3 | -37.9% | +6.7% | **+20.7%** | +42.5% | +147.3% |
| effective health, physical | 90 | **32** | **14** | 44 | -47.4% | +0.0% | **+0.0%** | +14.0% | +92.0% |
| effective health, magical | 90 | **34** | **12** | 44 | -45.4% | +0.0% | **+0.0%** | +16.7% | +136.1% |
| total DPS vs 70 prot per 1000g | 90 | **64** | **24** | 2 | -39.1% | -1.8% | **+11.9%** | +34.1% | +128.4% |
| total DPS vs 170 prot per 1000g | 90 | **61** | **24** | 5 | -42.0% | -1.9% | **+8.0%** | +31.1% | +125.9% |
| effective health, physical per 1000g | 90 | **29** | **58** | 3 | -51.0% | -13.1% | **-6.4%** | +6.1% | +110.9% |
| effective health, magical per 1000g | 90 | **32** | **56** | 2 | -47.1% | -12.5% | **-6.4%** | +12.0% | +110.3% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 16 / 2 / +25.0% | 15 / 2 / +22.7% | 3 / 0 / +0.0% | 3 / 0 / +0.0% |
| Jungle | 18 | 17 / 1 / +28.4% | 16 / 1 / +26.9% | 2 / 4 / +0.0% | 2 / 4 / +0.0% |
| Mid | 22 | 18 / 4 / +18.9% | 17 / 4 / +17.4% | 2 / 3 / +0.0% | 2 / 3 / +0.0% |
| Solo | 18 | 17 / 1 / +35.9% | 17 / 1 / +35.1% | 14 / 4 / +17.0% | 13 / 5 / +7.3% |
| Support | 14 | 10 / 4 / +6.5% | 10 / 4 / +6.5% | 11 / 3 / +20.9% | 14 / 0 / +43.0% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 15 / 3 / +14.6% | 14 / 3 / +11.2% | 2 / 15 / -8.4% | 2 / 15 / -8.4% |
| Jungle | 18 | 14 / 4 / +15.6% | 15 / 3 / +15.9% | 3 / 15 / -12.4% | 3 / 15 / -12.4% |
| Mid | 22 | 14 / 7 / +1.4% | 12 / 8 / +2.4% | 3 / 18 / -8.6% | 3 / 18 / -8.6% |
| Solo | 18 | 16 / 2 / +32.4% | 15 / 2 / +29.4% | 11 / 7 / +10.4% | 11 / 7 / +7.2% |
| Support | 14 | 5 / 8 / -3.9% | 5 / 8 / -3.9% | 10 / 3 / +8.0% | 13 / 1 / +25.6% |

## 5. Sensitivity — the passives the gold model CAN price

Same as §2 with the shipped pricing flags applied to every stat line: the Adaptive Stat grants (`price_adaptive`) and the mana conversions (`price_conversions`). This is the one slice of the blind spot that can be put on the table; the other 123 items stay invisible here too.

90 gods compared.

Community six, labelled (`community_target`): on 68 gods it holds an **unfinished** component (72 slots — the match ended before the build did), and on 20 an **unscoreable** statless relic or god Mod (20 slots). Combat still runs on the six as bought, so on those gods "ahead" is partly ahead of a half-built item and is not a disagreement about what to finish on.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 90 | **75** | **14** | 1 | -37.4% | +10.2% | **+24.1%** | +46.8% | +135.4% |
| total DPS vs 170 prot | 90 | **74** | **15** | 1 | -38.1% | +8.9% | **+23.4%** | +44.6% | +132.8% |
| effective health, physical | 90 | **34** | **14** | 42 | -47.4% | +0.0% | **+0.0%** | +11.2% | +87.0% |
| effective health, magical | 90 | **39** | **8** | 43 | -45.4% | +0.0% | **+0.0%** | +20.8% | +141.9% |
| total DPS vs 70 prot per 1000g | 90 | **66** | **21** | 3 | -37.2% | +0.3% | **+16.2%** | +37.9% | +117.3% |
| total DPS vs 170 prot per 1000g | 90 | **65** | **21** | 4 | -37.9% | +0.1% | **+13.7%** | +32.6% | +114.9% |
| effective health, physical per 1000g | 90 | **34** | **53** | 3 | -51.7% | -11.8% | **-5.1%** | +9.0% | +98.7% |
| effective health, magical per 1000g | 90 | **39** | **49** | 2 | -48.2% | -10.9% | **-3.2%** | +15.4% | +128.2% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 16 / 2 / +34.9% | 16 / 2 / +25.6% | 5 / 0 / +0.0% | 5 / 0 / +0.0% |
| Jungle | 18 | 16 / 1 / +36.8% | 15 / 2 / +30.8% | 3 / 3 / +0.0% | 3 / 3 / +0.0% |
| Mid | 22 | 17 / 5 / +23.1% | 17 / 5 / +22.5% | 3 / 2 / +0.0% | 2 / 3 / +0.0% |
| Solo | 18 | 17 / 1 / +30.8% | 17 / 1 / +29.2% | 12 / 6 / +12.6% | 15 / 2 / +15.3% |
| Support | 14 | 9 / 5 / +5.6% | 9 / 5 / +5.6% | 11 / 3 / +22.4% | 14 / 0 / +40.9% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 15 / 3 / +22.8% | 14 / 4 / +15.0% | 5 / 12 / -4.1% | 5 / 12 / -4.1% |
| Jungle | 18 | 15 / 2 / +26.0% | 15 / 2 / +20.8% | 4 / 14 / -10.1% | 4 / 14 / -10.1% |
| Mid | 22 | 15 / 7 / +7.7% | 15 / 6 / +5.3% | 3 / 18 / -8.5% | 3 / 18 / -8.5% |
| Solo | 18 | 16 / 1 / +25.4% | 16 / 1 / +23.3% | 13 / 5 / +8.6% | 13 / 5 / +15.1% |
| Support | 14 | 5 / 8 / -4.6% | 5 / 8 / -4.6% | 9 / 4 / +10.9% | 14 / 0 / +25.8% |

Verdict on DPS vs 70 flips for 6 god(s) between §2 and §5: Cernunnos (-44.2 → +59.1), Khepri (+6.5 → -29.3), Medusa (-16.1 → +91.3), Nut (-0.6 → +60.6), Poseidon (+19.3 → -35.4), Ra (+51.6 → -22.1).

## 6. The blind spot, measured

| | buildable pool | community slots | our `model` slots |
|---|---|---|---|
| items / slots | 138 | 543 | 540 |
| carrying unpriced passive text | 123 (89.1%) | 397 (73.1%) | 483 (89.4%) |
| mean gold residual per slot (cost − stat-line prediction) | – | +26g | -108g |
| mean stat columns per item | – | 2.68 | 3.37 |

Passives the shipped flags price (14): Book of Thoth, Brawler’s Beat Stick, Damaru, Daybreak Gavel, Deathbringer, Eye of Erebus, Mercury's Talaria, Nimble Ring, Omen Drum, Rod of Tahuti, Sun Beam Bow, The Executioner, Transcendence, Vital Amplifier.

Most-bought blind items — community: Freya's Tears (34), Obsidian Shard (24), Spear of Desolation (21), Devourer's Gauntlet (20), Shell of Rebuke (17). Ours: Jotunn's Revenge (50), Amanita Charm (36), Kinetic Cuirass (32), Genji's Guard (30), Spear of Desolation (26).

## 7. Every god — `model` core, printed stat lines

C = community, O = ours. DPS vs 70 is shown as total (basic + ability).

| God | Role | Gold C / O | DPS vs 70 — C (basic+ability) | O (basic+ability) | Δ | DPS vs 170 — C | O | Δ | EHP phys — C | O | Δ | EHP mag — C | O | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Achilles | Solo Jungle | 15,650 / 14,500 | 138.5 (100.5+38.1) | 227.7 (181.7+46.1) | +64.4% | 87.2 | 141.8 | +62.6% | 9,312 | 10,837 | +16.4% | 7,292 | 8,024 | +10.0% |
| Agni | Mid | 15,500 / 16,450 | 228.6 (162.7+65.8) | 263.8 (183.2+80.6) | +15.4% | 145.9 | 171.4 | +17.4% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Ah Puch | Mid | 15,600 / 16,450 | 130.4 (92.1+38.3) | 227.3 (169.1+58.3) | +74.3% | 81.2 | 147.7 | +81.9% | 7,078 | 4,347 | -38.6% | 7,072 | 3,862 | -45.4% |
| Aladdin | Jungle | 13,300 / 15,850 | 110.1 (103.4+6.7) | 172.6 (162.6+10.0) | +56.8% | 72.1 | 110.2 | +52.8% | 4,233 | 4,233 | +0.0% | 3,846 | 3,846 | +0.0% |
| Amaterasu | Solo | 13,200 / 14,300 | 136.7 (119.7+17.1) | 153.9 (130.3+23.5) | +12.6% | 86.1 | 95.8 | +11.3% | 10,148 | 9,490 | -6.5% | 8,715 | 8,962 | +2.8% |
| Anhur | Carry | 13,750 / 15,000 | 425.3 (385.0+40.3) | 597.9 (528.7+69.2) | +40.6% | 281.1 | 353.9 | +25.9% | 4,148 | 4,493 | +8.3% | 3,644 | 3,947 | +8.3% |
| Anubis | Mid | 16,150 / 16,450 | 143.2 (123.6+19.6) | 195.5 (166.5+29.0) | +36.5% | 92.4 | 127.0 | +37.5% | 4,202 | 4,202 | +0.0% | 3,912 | 3,912 | +0.0% |
| Aphrodite | Mid Support | 14,650 / 15,350 | 154.6 (116.1+38.5) | 121.0 (83.2+37.8) | -21.7% | 101.3 | 75.3 | -25.7% | 3,760 | 7,029 | +87.0% | 3,399 | 8,117 | +138.8% |
| Apollo | Carry | 13,950 / 15,000 | 414.1 (376.5+37.6) | 582.2 (517.5+64.7) | +40.6% | 273.7 | 344.6 | +25.9% | 4,076 | 4,421 | +8.5% | 3,580 | 3,883 | +8.5% |
| Ares | Support | 13,200 / 14,500 | 60.3 (60.3+0.0) | 110.9 (110.9+0.0) | +84.1% | 37.9 | 69.8 | +84.1% | 9,918 | 11,255 | +13.5% | 8,452 | 10,548 | +24.8% |
| Artemis | Carry | 13,600 / 15,150 | 375.5 (351.7+23.8) | 525.9 (482.5+43.4) | +40.1% | 241.9 | 311.2 | +28.7% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Artio | Solo Support | 13,500 / 14,300 | 101.8 (58.3+43.5) | 197.7 (142.8+54.9) | +94.2% | 64.1 | 123.1 | +92.0% | 11,091 | 9,968 | -10.1% | 7,748 | 9,411 | +21.5% |
| Athena | Support | 12,850 / 14,500 | 113.3 (84.4+28.9) | 185.0 (154.7+30.3) | +63.3% | 71.3 | 116.5 | +63.3% | 8,419 | 11,255 | +33.7% | 8,395 | 10,548 | +25.6% |
| Atlas | Support | 11,500 / 14,400 | 90.0 (72.9+17.1) | 88.8 (72.9+15.9) | -1.3% | 56.7 | 55.9 | -1.3% | 8,187 | 12,026 | +46.9% | 8,350 | 12,901 | +54.5% |
| Awilix | Jungle | 14,400 / 16,250 | 338.8 (270.1+68.7) | 581.6 (458.8+122.8) | +71.7% | 230.5 | 360.3 | +56.3% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Bacchus | Support | 13,300 / 14,500 | 129.1 (102.3+26.8) | 141.5 (110.9+30.6) | +9.6% | 81.3 | 89.1 | +9.6% | 11,863 | 11,112 | -6.3% | 7,776 | 10,623 | +36.6% |
| Baron Samedi | Mid Support | 13,050 / 15,350 | 126.2 (53.7+72.5) | 177.7 (83.2+94.5) | +40.8% | 79.5 | 110.6 | +39.1% | 6,889 | 7,029 | +2.0% | 8,455 | 8,117 | -4.0% |
| Bastet | Jungle | 14,500 / 16,250 | 316.7 (262.0+54.7) | 516.7 (449.6+67.1) | +63.1% | 220.3 | 320.1 | +45.3% | 4,117 | 4,117 | +0.0% | 3,702 | 3,702 | +0.0% |
| Bellona | Solo | 14,300 / 14,300 | 178.8 (150.4+28.4) | 218.9 (176.5+42.4) | +22.4% | 112.6 | 136.3 | +21.0% | 10,940 | 9,783 | -10.6% | 8,861 | 9,029 | +1.9% |
| Cabrakan | Solo Support | 13,100 / 14,300 | 163.2 (96.1+67.1) | 211.3 (150.4+60.9) | +29.5% | 102.7 | 131.6 | +28.0% | 9,042 | 9,968 | +10.2% | 9,055 | 9,411 | +3.9% |
| Cerberus | Solo Support | 13,250 / 14,500 | 76.7 (52.2+24.5) | 83.8 (52.2+31.6) | +9.3% | 48.3 | 52.8 | +9.3% | 10,489 | 11,620 | +10.8% | 8,427 | 10,952 | +30.0% |
| Cernunnos | Carry Jungle | 13,750 / 15,550 | 406.7 (385.0+21.7) | 362.5 (326.6+35.9) | -10.9% | 268.8 | 219.9 | -18.2% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Chaac | Solo | 15,100 / 14,950 | 169.3 (83.6+85.7) | 251.2 (170.5+80.7) | +48.4% | 106.6 | 158.2 | +48.4% | 6,663 | 9,490 | +42.4% | 6,438 | 7,243 | +12.5% |
| Charon | Support | 15,600 / 14,400 | 135.4 (81.0+54.4) | 96.0 (55.4+40.5) | -29.1% | 86.2 | 60.4 | -29.9% | 6,492 | 11,909 | +83.4% | 7,427 | 12,774 | +72.0% |
| Chiron | Carry | 14,400 / 15,400 | 376.2 (294.4+81.8) | 604.8 (521.1+83.7) | +60.8% | 247.1 | 375.5 | +51.9% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Chronos | Mid Carry | 16,100 / 16,250 | 253.5 (154.7+98.8) | 339.9 (224.3+115.6) | +34.1% | 166.1 | 229.7 | +38.3% | 4,016 | 4,016 | +0.0% | 3,630 | 3,630 | +0.0% |
| Cu Chulainn | Solo | 13,700 / 14,550 | 125.2 (36.2+89.0) | 280.8 (160.8+120.0) | +124.4% | 78.8 | 174.9 | +121.9% | 12,871 | 9,470 | -26.4% | 8,861 | 6,927 | -21.8% |
| Cupid | Carry | 15,550 / 15,550 | 420.2 (400.9+19.3) | 294.9 (255.4+39.5) | -29.8% | 277.7 | 178.9 | -35.6% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Da Ji | Jungle | 14,450 / 15,850 | 380.3 (314.7+65.6) | 401.9 (334.2+67.8) | +5.7% | 249.8 | 264.0 | +5.7% | 3,865 | 3,865 | +0.0% | 3,452 | 3,452 | +0.0% |
| Danzaburou | Carry | 16,150 / 15,550 | 382.4 (315.8+66.5) | 440.3 (327.4+112.8) | +15.2% | 264.3 | 267.1 | +1.1% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Discordia | Mid | 13,150 / 16,450 | 209.6 (137.3+72.3) | 263.5 (172.8+90.7) | +25.7% | 139.9 | 171.2 | +22.3% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Eset | Mid | 12,950 / 16,450 | 216.3 (151.6+64.6) | 303.3 (206.2+97.2) | +40.3% | 141.7 | 197.0 | +39.1% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Fenrir | Jungle | 14,900 / 16,250 | 196.2 (161.5+34.7) | 537.5 (466.4+71.1) | +174.0% | 122.1 | 333.0 | +172.6% | 8,687 | 4,571 | -47.4% | 5,382 | 4,052 | -24.7% |
| Ganesha | Support | 12,850 / 14,500 | 100.8 (59.5+41.3) | 107.0 (59.5+47.5) | +6.1% | 63.5 | 67.4 | +6.1% | 8,291 | 11,620 | +40.2% | 8,395 | 10,876 | +29.6% |
| Geb | Support Carry | 13,050 / 14,500 | 103.7 (58.3+45.4) | 116.9 (58.3+58.6) | +12.8% | 65.3 | 73.6 | +12.8% | 10,546 | 11,744 | +11.4% | 7,572 | 10,992 | +45.2% |
| Gilgamesh | Solo Jungle | 13,950 / 14,800 | 259.9 (209.0+50.9) | 346.4 (306.5+40.0) | +33.3% | 161.6 | 210.6 | +30.3% | 5,741 | 9,029 | +57.3% | 4,837 | 6,402 | +32.3% |
| Guan Yu | Solo Support | 13,150 / 14,300 | 103.7 (77.7+26.0) | 217.6 (187.1+30.4) | +109.8% | 65.3 | 135.5 | +107.5% | 7,544 | 9,449 | +25.2% | 8,929 | 8,962 | +0.4% |
| Hades | Solo | 14,850 / 15,900 | 217.7 (132.8+84.9) | 207.6 (120.9+86.7) | -4.6% | 139.0 | 140.3 | +0.9% | 4,348 | 5,876 | +35.1% | 3,862 | 6,869 | +77.8% |
| Hecate | Mid | 15,150 / 16,450 | 277.3 (132.2+145.1) | 364.7 (166.5+198.2) | +31.5% | 177.1 | 236.9 | +33.8% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Hercules | Solo | 13,100 / 14,300 | 173.9 (102.2+71.8) | 229.8 (169.0+60.8) | +32.1% | 108.3 | 143.1 | +32.1% | 8,155 | 9,327 | +14.4% | 6,888 | 8,814 | +28.0% |
| Horus | Support Solo | 13,200 / 14,300 | 64.7 (61.2+3.4) | 152.2 (147.9+4.3) | +135.4% | 40.7 | 94.8 | +132.8% | 9,372 | 9,681 | +3.3% | 7,996 | 9,030 | +12.9% |
| Hou Yi | Carry | 13,950 / 15,450 | 439.2 (396.7+42.4) | 459.4 (387.9+71.5) | +4.6% | 282.9 | 282.4 | -0.2% | 4,076 | 4,076 | +0.0% | 3,580 | 3,580 | +0.0% |
| Hua Mulan | Solo | 13,200 / 14,300 | 134.6 (92.4+42.2) | 205.7 (157.3+48.4) | +52.8% | 84.8 | 128.1 | +51.1% | 7,791 | 9,783 | +25.6% | 8,274 | 9,029 | +9.1% |
| Hun Batz | Jungle | 14,200 / 16,250 | 330.6 (236.1+94.4) | 577.9 (452.7+125.2) | +74.8% | 205.6 | 358.1 | +74.2% | 4,233 | 4,233 | +0.0% | 3,752 | 3,752 | +0.0% |
| Ishtar | Carry | 13,800 / 15,600 | 320.3 (310.1+10.2) | 616.8 (604.5+12.3) | +92.6% | 206.4 | 388.4 | +88.2% | 3,861 | 4,203 | +8.9% | 3,416 | 3,719 | +8.9% |
| Ix Chel | Mid Support | 15,050 / 15,350 | 369.9 (142.8+227.1) | 225.4 (78.3+147.1) | -39.1% | 232.9 | 140.3 | -39.8% | 3,866 | 7,164 | +85.3% | 3,595 | 8,367 | +132.7% |
| Izanami | Carry | 15,850 / 15,550 | 459.8 (434.9+24.9) | 382.5 (325.0+57.5) | -16.8% | 304.0 | 232.0 | -23.7% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Janus | Mid | 15,550 / 16,450 | 263.3 (145.4+118.0) | 313.8 (166.5+147.3) | +19.2% | 178.0 | 203.8 | +14.5% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Jing Wei | Carry | 15,800 / 15,600 | 537.9 (513.8+24.1) | 641.6 (616.6+25.0) | +19.3% | 346.6 | 404.0 | +16.6% | 3,788 | 4,130 | +9.0% | 3,353 | 3,656 | +9.0% |
| Jormungandr | Solo Support | 16,000 / 14,300 | 148.0 (74.2+73.8) | 178.5 (109.8+68.7) | +20.6% | 93.2 | 111.1 | +19.3% | 10,195 | 10,092 | -1.0% | 8,075 | 9,529 | +18.0% |
| Kali | Jungle | 15,350 / 15,800 | 250.5 (225.1+25.4) | 334.4 (277.8+56.6) | +33.5% | 161.4 | 216.4 | +34.1% | 4,233 | 4,233 | +0.0% | 3,752 | 3,752 | +0.0% |
| Khepri | Support | 13,300 / 14,500 | 93.3 (58.3+35.0) | 99.8 (58.3+41.4) | +6.9% | 58.7 | 62.8 | +6.9% | 8,712 | 11,744 | +34.8% | 6,997 | 10,992 | +57.1% |
| Kukulkan | Mid | 14,650 / 16,450 | 185.9 (116.1+69.9) | 276.0 (166.5+109.5) | +48.4% | 121.8 | 179.3 | +47.2% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Loki | Jungle | 17,150 / 16,000 | 331.5 (308.1+23.3) | 331.5 (311.9+19.5) | +0.0% | 225.1 | 211.9 | -5.9% | 4,117 | 4,117 | +0.0% | 3,702 | 3,702 | +0.0% |
| Medusa | Carry | 13,950 / 15,550 | 411.7 (372.1+39.6) | 395.7 (313.5+82.2) | -3.9% | 272.1 | 240.0 | -11.8% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Mercury | Jungle | 15,150 / 16,100 | 503.0 (493.8+9.3) | 451.6 (433.5+18.1) | -10.2% | 332.5 | 288.6 | -13.2% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Merlin | Mid | 13,150 / 16,450 | 290.3 (132.3+158.0) | 366.2 (166.5+199.8) | +26.2% | 193.8 | 237.9 | +22.8% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Mordred | Solo Jungle | 13,900 / 14,300 | 141.7 (103.9+37.8) | 197.8 (151.3+46.6) | +39.6% | 89.2 | 123.2 | +38.1% | 8,807 | 9,646 | +9.5% | 7,646 | 9,088 | +18.9% |
| Morgan Le Fay | Mid | 14,800 / 16,450 | 220.2 (150.5+69.7) | 264.4 (175.6+88.8) | +20.1% | 145.1 | 171.7 | +18.4% | 4,440 | 4,015 | -9.6% | 4,014 | 3,630 | -9.6% |
| Ne Zha | Jungle | 16,000 / 15,850 | 447.4 (414.6+32.7) | 477.6 (439.1+38.6) | +6.8% | 301.0 | 313.7 | +4.2% | 5,075 | 4,233 | -16.6% | 4,594 | 3,752 | -18.3% |
| Neith | Carry Mid | 14,850 / 15,550 | 350.9 (257.6+93.3) | 444.1 (318.7+125.4) | +26.6% | 237.1 | 269.4 | +13.6% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Nemesis | Jungle | 15,600 / 15,800 | 278.6 (233.1+45.5) | 466.8 (419.0+47.9) | +67.6% | 173.3 | 302.1 | +74.3% | 5,075 | 4,233 | -16.6% | 4,594 | 3,752 | -18.3% |
| Nu Wa | Mid | 15,050 / 16,450 | 252.8 (167.9+85.0) | 282.3 (187.0+95.2) | +11.6% | 159.2 | 183.3 | +15.2% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Nut | Carry Mid | 13,450 / 16,100 | 337.9 (326.6+11.2) | 337.3 (310.1+27.2) | -0.2% | 217.7 | 212.4 | -2.5% | 4,045 | 4,045 | +0.0% | 3,580 | 3,580 | +0.0% |
| Odin | Solo Jungle | 13,050 / 14,300 | 137.1 (97.7+39.4) | 194.7 (162.9+31.7) | +42.0% | 85.4 | 121.2 | +42.0% | 6,658 | 9,646 | +44.9% | 6,653 | 9,088 | +36.6% |
| Osiris | Solo | 13,200 / 14,550 | 198.1 (132.2+65.9) | 354.6 (274.7+79.9) | +79.0% | 124.7 | 220.8 | +77.0% | 11,082 | 9,355 | -15.6% | 7,705 | 6,772 | -12.1% |
| Pele | Jungle | 14,450 / 15,850 | 276.5 (271.6+4.9) | 321.2 (314.1+7.1) | +16.2% | 183.9 | 211.0 | +14.7% | 4,307 | 4,307 | +0.0% | 3,817 | 3,817 | +0.0% |
| Poseidon | Mid | 15,050 / 16,450 | 244.8 (182.6+62.1) | 264.1 (182.2+81.8) | +7.9% | 156.3 | 171.5 | +9.7% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Princess Bari | Carry Mid | 17,150 / 15,650 | 228.0 (160.7+67.3) | 430.8 (378.4+52.4) | +88.9% | 152.2 | 267.7 | +75.9% | 4,046 | 4,046 | +0.0% | 3,745 | 3,745 | +0.0% |
| Ra | Mid | 16,450 / 16,150 | 264.5 (156.4+108.1) | 316.1 (150.9+165.1) | +19.5% | 168.9 | 211.0 | +24.9% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Rama | Carry | 13,750 / 15,600 | 395.8 (391.4+4.5) | 547.5 (539.6+8.0) | +38.3% | 261.6 | 339.9 | +29.9% | 3,788 | 3,788 | +0.0% | 3,353 | 3,353 | +0.0% |
| Ratatoskr | Jungle | 15,000 / 14,000 | 335.2 (262.8+72.5) | 356.1 (287.2+68.9) | +6.2% | 220.2 | 227.2 | +3.2% | 5,715 | 6,419 | +12.3% | 5,065 | 5,689 | +12.3% |
| Ravana | Jungle | 15,700 / 14,450 | 188.4 (120.1+68.4) | 239.9 (157.4+82.5) | +27.3% | 121.4 | 149.3 | +23.0% | 8,603 | 9,140 | +6.2% | 7,725 | 8,548 | +10.6% |
| Scylla | Mid | 14,350 / 16,450 | 216.6 (114.0+102.6) | 332.4 (166.5+165.9) | +53.5% | 146.4 | 216.0 | +47.5% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Sobek | Support | 13,250 / 14,400 | 102.3 (60.3+42.1) | 107.6 (60.3+47.3) | +5.1% | 64.4 | 67.7 | +5.1% | 10,363 | 11,773 | +13.6% | 8,249 | 12,629 | +53.1% |
| Sol | Mid Carry | 16,300 / 16,250 | 449.7 (433.2+16.6) | 277.1 (244.6+32.5) | -38.4% | 301.5 | 187.2 | -37.9% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Sun Wukong | Solo | 13,750 / 14,500 | 115.9 (111.4+4.6) | 184.2 (179.0+5.3) | +58.9% | 74.7 | 114.7 | +53.6% | 5,640 | 10,514 | +86.4% | 5,774 | 7,857 | +36.1% |
| Susano | Jungle | 13,950 / 16,250 | 261.2 (231.5+29.7) | 545.3 (500.5+44.8) | +108.8% | 166.4 | 337.8 | +103.0% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Sylvanus | Support | 12,900 / 15,100 | 76.9 (57.1+19.8) | 87.6 (59.1+28.5) | +13.8% | 48.4 | 55.7 | +15.1% | 10,249 | 9,931 | -3.1% | 7,307 | 9,556 | +30.8% |
| Thanatos | Jungle | 14,300 / 16,250 | 407.2 (310.2+97.0) | 598.5 (487.1+111.4) | +47.0% | 267.5 | 370.8 | +38.6% | 4,655 | 4,655 | +0.0% | 4,126 | 4,126 | +0.0% |
| The Morrigan | Mid | 14,650 / 16,450 | 181.8 (143.1+38.7) | 245.7 (185.1+60.6) | +35.1% | 119.1 | 159.6 | +34.0% | 3,894 | 3,894 | +0.0% | 3,452 | 3,452 | +0.0% |
| Thor | Jungle Solo | 14,300 / 14,950 | 268.1 (227.7+40.4) | 276.2 (245.8+30.4) | +3.0% | 180.4 | 180.6 | +0.1% | 5,325 | 9,140 | +71.6% | 4,753 | 6,675 | +40.4% |
| Tsukuyomi | Jungle | 14,300 / 15,800 | 288.1 (260.8+27.3) | 453.9 (415.0+38.8) | +57.5% | 191.6 | 293.7 | +53.3% | 4,307 | 4,307 | +0.0% | 3,766 | 3,766 | +0.0% |
| Ullr | Carry | 14,100 / 15,400 | 353.7 (255.5+98.2) | 604.4 (502.4+102.0) | +70.9% | 238.0 | 375.2 | +57.6% | 4,148 | 4,148 | +0.0% | 3,644 | 3,644 | +0.0% |
| Vulcan | Mid | 12,050 / 16,450 | 242.6 (116.1+126.5) | 365.7 (166.5+199.2) | +50.8% | 158.9 | 237.5 | +49.5% | 4,015 | 4,015 | +0.0% | 3,630 | 3,630 | +0.0% |
| Xbalanque | Carry | 13,800 / 15,600 | 452.6 (435.3+17.4) | 641.4 (621.2+20.2) | +41.7% | 299.2 | 403.8 | +35.0% | 3,788 | 4,130 | +9.0% | 3,353 | 3,656 | +9.0% |
| Xing Tian | Support Solo | 13,050 / 14,400 | 20.0 (0.0+20.0) | 20.8 (0.0+20.8) | +3.8% | 12.6 | 13.1 | +3.8% | 1,720 | 2,640 | +53.5% | 1,296 | 3,135 | +141.9% |
| Yemoja | Support | 13,850 / 15,100 | 97.0 (92.0+5.0) | 76.2 (71.7+4.6) | -21.4% | 62.7 | 48.5 | -22.5% | 7,697 | 10,094 | +31.1% | 6,534 | 9,712 | +48.6% |
| Ymir | Support | 13,950 / 14,400 | 125.1 (76.0+49.2) | 118.6 (63.3+55.3) | -5.2% | 78.8 | 74.7 | -5.2% | 13,463 | 12,332 | -8.4% | 10,154 | 13,228 | +30.3% |
| Zeus | Mid | 15,150 / 16,450 | 249.0 (148.4+100.7) | 325.7 (208.0+117.7) | +30.8% | 159.0 | 214.6 | +34.9% | 3,894 | 3,894 | +0.0% | 3,452 | 3,452 | +0.0% |
