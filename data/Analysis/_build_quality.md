# Build quality — `combat.py` pointed at whole builds

_Input fingerprint: `ea30ca4c0735` — items, gods, tags, community builds, weights. Regenerate with `python -m smite.build_quality`; a different fingerprint means different inputs._

> **READ THIS BEFORE ANY NUMBER BELOW.** Of the 138 buildable items, 137 carry passive text and the shipped pricing flags read 13 of them — so **90% of the pool carries passive value this arithmetic cannot see**, and **76% of the community's item slots do** (408 of 537; 91% of ours, 484 of 534). `combat.py` reads exactly one passive — Deathbringer's +35% crit damage. The bias is not even: by the gold model's own residual the community pays **+135g more per slot above its stat line than we do** (mean residual -1g against -136g) and buys fewer stat columns per item (2.81 against 3.49) — that premium IS the passive. **A verdict in our favour is the one to distrust.** The most-bought blind community items are Genji's Guard (29), Shifter's Shield (28), Obsidian Shard (25), Spear of Desolation (24), Shell of Rebuke (22).

This is the only instrument in the repo that can say a build is BETTER rather than more conventional: `validate.compute` is circular (STATE.md §1) and the leakage-free gate is coverage of the community's items, and both go down when a build is genuinely better and unconventional. `combat.py` is calibrated to 0.0% against in-game readings and has never seen a community build. It also cannot see a passive, which is the paragraph above.

Assumptions, all of them on every figure:

- **full ability uptime** — every ability cast the moment it is off cooldown, at its last rank, with no cast time charged (none exists in the scrape; register §4.12), so a god casts everything AND swings at full rate in the same second
- **no relic, single target, no lifesteal sustain, no crowd control, no wave clear**
- targets at exactly 70 and 170 protection of the god's own damage type, no Plating or Dampening
- level 20, six items, the community's slot picks against our meta-free `model` core (the first community entry, aspect or not — the one `validate` scores against)
- printed stat lines only, with penetration kept as two goods and capped (40% / 50); Deathbringer at the measured 1.85x
- a chain god's basic attack at the chain's mean multiplier; an ability without a scraped cooldown dropped, never imputed; a DoT counted as its listed damage once
- dual-role labels (`Solo Jungle`) collapse to their first word in the role tables

Nothing here feeds `scoring`, `assemble` or a weight. It is a report a human reads.

## 1. The worked example

### Medusa (Carry)

**community** — 13,750g: Tyrfing · Odysseus' Bow · Silverbranch Bow · Riptalon · The Executioner · Manchu Bow
  stat line: Attack Damage 80 · Attack Speed % 133 · Lifesteal % 7.5 · Penetration % 20 · Strength 25
  abilities counted: Acid Spray, Lacerate, Petrify

**ours** — 15,400g: Berserker's Shield · Jotunn's Revenge · Nimble Ring · Death Metal · Rod of Tahuti · Soul Gem
  stat line: Attack Speed % 40 · Cooldown Rate 35 · Critical Chance % 20 · Health Regen 4 · Intelligence 215 · Lifesteal % 15 · Mana Regen 2 · Max Health 200 · Max Mana 500 · Penetration 10 · Penetration % 5 · Physical Protection 40 · Strength 70
  abilities counted: Acid Spray, Lacerate, Petrify

| | basic DPS | ability DPS | TOTAL | EHP physical | EHP magical |
|---|---|---|---|---|---|
| COMMUNITY vs squishy (70) | 352.8 | 35.9 | **388.6** | 3,788 | 3,353 |
| COMMUNITY vs tank (170) | 233.2 | 23.7 | **256.9** | 3,788 | 3,353 |
| OURS vs squishy (70) | 242.4 | 72.4 | **314.8** | 5,095 | 3,656 |
| OURS vs tank (170) | 150.8 | 45.1 | **195.9** | 5,095 | 3,656 |

| per 1000g | DPS vs 70 | DPS vs 170 | EHP physical | EHP magical |
|---|---|---|---|---|
| COMMUNITY | 28.3 | 18.7 | 275 | 244 |
| OURS | 20.4 | 12.7 | 331 | 237 |

## 2. The roster — our `model` core, printed stat lines

89 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 89 | **71** | **15** | 3 | -49.0% | +4.9% | **+23.6%** | +50.5% | +165.6% |
| total DPS vs 170 prot | 89 | **67** | **17** | 5 | -48.3% | +2.6% | **+18.3%** | +48.2% | +156.4% |
| effective health, physical | 89 | **46** | **17** | 26 | -36.7% | +0.0% | **+5.3%** | +34.5% | +144.7% |
| effective health, magical | 89 | **41** | **23** | 25 | -38.5% | -1.5% | **+0.0%** | +15.5% | +172.1% |
| total DPS vs 70 prot per 1000g | 89 | **65** | **23** | 1 | -47.4% | -0.6% | **+12.3%** | +41.7% | +157.4% |
| total DPS vs 170 prot per 1000g | 89 | **64** | **24** | 1 | -46.8% | -4.1% | **+10.3%** | +36.8% | +142.4% |
| effective health, physical per 1000g | 89 | **46** | **43** | 0 | -38.5% | -9.8% | **+1.4%** | +22.9% | +152.2% |
| effective health, magical per 1000g | 89 | **34** | **54** | 1 | -40.3% | -11.4% | **-4.1%** | +5.3% | +180.4% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 12 / 6 / +11.9% | 9 / 7 / +5.0% | 18 / 0 / +34.5% | 17 / 1 / +9.0% |
| Jungle | 17 | 15 / 2 / +40.4% | 14 / 3 / +33.3% | 4 / 4 / +0.0% | 4 / 4 / +0.0% |
| Mid | 22 | 20 / 2 / +20.3% | 20 / 2 / +23.2% | 3 / 2 / +0.0% | 3 / 3 / +0.0% |
| Solo | 18 | 18 / 0 / +79.5% | 18 / 0 / +74.8% | 7 / 11 / -2.0% | 4 / 14 / -6.4% |
| Support | 14 | 6 / 5 / +0.0% | 6 / 5 / +0.0% | 14 / 0 / +36.9% | 13 / 1 / +33.5% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 11 / 7 / +7.8% | 10 / 8 / +2.2% | 18 / 0 / +27.5% | 11 / 7 / +4.9% |
| Jungle | 17 | 14 / 2 / +26.6% | 13 / 4 / +20.2% | 4 / 13 / -9.7% | 4 / 13 / -9.7% |
| Mid | 22 | 18 / 4 / +8.5% | 19 / 2 / +10.9% | 2 / 20 / -9.2% | 3 / 19 / -9.3% |
| Solo | 18 | 17 / 1 / +69.5% | 17 / 1 / +67.6% | 8 / 10 / -4.0% | 4 / 13 / -9.9% |
| Support | 14 | 5 / 9 / -8.8% | 5 / 9 / -8.8% | 14 / 0 / +22.8% | 12 / 2 / +18.3% |

## 3. The same, for the blended `core` (what the Balanced tab ships)

`core` carries `win` and `pick`, so it is part community build already; the gap between this block and §2 is what the meta signal buys in this arithmetic.

89 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 89 | **69** | **15** | 5 | -35.6% | +2.7% | **+18.9%** | +39.8% | +182.3% |
| total DPS vs 170 prot | 89 | **68** | **17** | 4 | -36.4% | +1.4% | **+17.9%** | +35.5% | +172.6% |
| effective health, physical | 89 | **43** | **13** | 33 | -27.7% | +0.0% | **+0.0%** | +40.1% | +111.5% |
| effective health, magical | 89 | **38** | **18** | 33 | -35.7% | +0.0% | **+0.0%** | +16.3% | +126.1% |
| total DPS vs 70 prot per 1000g | 89 | **61** | **27** | 1 | -36.4% | -6.8% | **+9.5%** | +30.2% | +149.4% |
| total DPS vs 170 prot per 1000g | 89 | **58** | **30** | 1 | -36.2% | -5.4% | **+6.6%** | +26.2% | +140.8% |
| effective health, physical per 1000g | 89 | **42** | **46** | 1 | -32.5% | -10.3% | **-0.9%** | +25.2% | +100.3% |
| effective health, magical per 1000g | 89 | **31** | **57** | 1 | -40.0% | -11.2% | **-5.3%** | +6.6% | +118.9% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 15 / 2 / +16.1% | 15 / 3 / +12.6% | 12 / 0 / +34.1% | 11 / 1 / +8.8% |
| Jungle | 17 | 15 / 2 / +19.1% | 12 / 5 / +15.9% | 5 / 3 / +0.0% | 4 / 4 / +0.0% |
| Mid | 22 | 18 / 4 / +15.2% | 20 / 2 / +17.6% | 3 / 2 / +0.0% | 4 / 2 / +0.0% |
| Solo | 18 | 17 / 1 / +51.8% | 17 / 1 / +50.1% | 9 / 8 / +1.6% | 6 / 10 / -8.2% |
| Support | 14 | 4 / 6 / +0.0% | 4 / 6 / +0.0% | 14 / 0 / +45.4% | 13 / 1 / +42.5% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 12 / 5 / +5.5% | 11 / 6 / +3.7% | 13 / 4 / +19.6% | 10 / 7 / +2.5% |
| Jungle | 17 | 14 / 3 / +15.4% | 12 / 5 / +9.6% | 5 / 12 / -7.0% | 4 / 13 / -7.0% |
| Mid | 22 | 14 / 8 / +2.7% | 14 / 8 / +5.5% | 2 / 20 / -9.1% | 2 / 20 / -9.0% |
| Solo | 18 | 17 / 1 / +40.1% | 17 / 1 / +38.5% | 8 / 10 / -3.9% | 3 / 15 / -10.5% |
| Support | 14 | 4 / 10 / -12.4% | 4 / 10 / -12.4% | 14 / 0 / +26.8% | 12 / 2 / +27.6% |

## 4. Sensitivity — the passives the gold model CAN price

Same as §2 with the shipped pricing flags applied to every stat line: the Adaptive Stat grants (`price_adaptive`) and the mana conversions (`price_conversions`). This is the one slice of the blind spot that can be put on the table; the other 124 items stay invisible here too.

89 gods compared.

Delta is ours over the community's, per god; a ratio, so every god weighs the same.

| Metric | n | ahead | behind | level (±0.5%) | worst | p25 | median | p75 | best |
|---|---|---|---|---|---|---|---|---|---|
| total DPS vs 70 prot | 89 | **66** | **20** | 3 | -61.7% | +0.0% | **+22.7%** | +50.5% | +165.6% |
| total DPS vs 170 prot | 89 | **63** | **21** | 5 | -61.3% | +0.0% | **+18.6%** | +43.4% | +156.4% |
| effective health, physical | 89 | **46** | **17** | 26 | -36.7% | +0.0% | **+5.3%** | +34.5% | +144.7% |
| effective health, magical | 89 | **41** | **23** | 25 | -38.5% | -1.5% | **+0.0%** | +15.5% | +172.1% |
| total DPS vs 70 prot per 1000g | 89 | **56** | **32** | 1 | -60.6% | -7.7% | **+9.4%** | +37.5% | +157.4% |
| total DPS vs 170 prot per 1000g | 89 | **56** | **32** | 1 | -60.1% | -8.7% | **+9.0%** | +33.1% | +142.4% |
| effective health, physical per 1000g | 89 | **46** | **43** | 0 | -38.5% | -9.8% | **+1.4%** | +22.9% | +152.2% |
| effective health, magical per 1000g | 89 | **34** | **54** | 1 | -40.3% | -11.4% | **-4.1%** | +5.3% | +180.4% |

By role — ahead / behind / median delta:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 11 / 7 / +4.2% | 7 / 9 / -1.6% | 18 / 0 / +34.5% | 17 / 1 / +9.0% |
| Jungle | 17 | 14 / 3 / +40.1% | 14 / 3 / +32.1% | 4 / 4 / +0.0% | 4 / 4 / +0.0% |
| Mid | 22 | 18 / 4 / +18.7% | 19 / 3 / +20.7% | 3 / 2 / +0.0% | 3 / 3 / +0.0% |
| Solo | 18 | 17 / 1 / +79.5% | 17 / 1 / +74.8% | 7 / 11 / -2.0% | 4 / 14 / -6.4% |
| Support | 14 | 6 / 5 / +0.0% | 6 / 5 / +0.0% | 14 / 0 / +36.9% | 13 / 1 / +33.5% |

Per 1000 gold, by role:

| Role | n | total DPS vs 70 prot ahead / behind / median | total DPS vs 170 prot ahead / behind / median | effective health, physical ahead / behind / median | effective health, magical ahead / behind / median |
|---|---|---|---|---|---|
| Carry | 18 | 5 / 13 / -3.1% | 5 / 13 / -8.8% | 18 / 0 / +27.5% | 11 / 7 / +4.9% |
| Jungle | 17 | 14 / 3 / +26.0% | 13 / 4 / +16.1% | 4 / 13 / -9.7% | 4 / 13 / -9.7% |
| Mid | 22 | 16 / 5 / +7.6% | 17 / 5 / +9.0% | 2 / 20 / -9.2% | 3 / 19 / -9.3% |
| Solo | 18 | 16 / 2 / +69.5% | 16 / 1 / +67.6% | 8 / 10 / -4.0% | 4 / 13 / -9.9% |
| Support | 14 | 5 / 9 / -8.8% | 5 / 9 / -8.8% | 14 / 0 / +22.8% | 12 / 2 / +18.3% |

Verdict on DPS vs 70 flips for 7 god(s) between §2 and §4: Hades (+23.6 → -23.1), Hou Yi (-30.8 → +9.2), Ishtar (+3.8 → -58.7), Kali (+13.9 → -33.3), Poseidon (+20.9 → -33.5), Ra (+36.7 → -11.5), Xbalanque (+6.0 → -56.3).

## 5. The blind spot, measured

| | buildable pool | community slots | our `model` slots |
|---|---|---|---|
| items / slots | 138 | 537 | 534 |
| carrying unpriced passive text | 124 (89.9%) | 408 (76.0%) | 484 (90.6%) |
| mean gold residual per slot (cost − stat-line prediction) | – | -1g | -136g |
| mean stat columns per item | – | 2.81 | 3.49 |

Passives the shipped flags price (13): Book of Thoth, Brawler’s Beat Stick, Daybreak Gavel, Deathbringer, Eye of Erebus, Mercury's Talaria, Nimble Ring, Omen Drum, Rod of Tahuti, Sun Beam Bow, The Executioner, Transcendence, Vital Amplifier.

Most-bought blind items — community: Genji's Guard (29), Shifter's Shield (28), Obsidian Shard (25), Spear of Desolation (24), Shell of Rebuke (22). Ours: Jotunn's Revenge (55), Berserker's Shield (40), Kinetic Cuirass (36), Amanita Charm (34), Freya's Tears (30).

## 6. Every god — `model` core, printed stat lines

C = community, O = ours. DPS vs 70 is shown as total (basic + ability).

| God | Role | Gold C / O | DPS vs 70 — C (basic+ability) | O (basic+ability) | Δ | DPS vs 170 — C | O | Δ | EHP phys — C | O | Δ | EHP mag — C | O | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Achilles | Solo Jungle | 13,250 / 14,900 | 92.6 (57.6+35.0) | 245.9 (193.4+52.5) | +165.6% | 58.3 | 149.5 | +156.4% | 11,400 | 9,938 | -12.8% | 9,792 | 7,485 | -23.6% |
| Agni | Mid | 15,650 / 16,600 | 229.8 (161.8+68.0) | 267.0 (183.2+83.7) | +16.2% | 146.7 | 173.4 | +18.2% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Ah Puch | Mid | 15,350 / 16,600 | 196.2 (140.9+55.3) | 225.1 (169.1+56.0) | +14.7% | 125.3 | 146.2 | +16.7% | 4,347 | 4,347 | +0.0% | 3,862 | 3,862 | +0.0% |
| Aladdin | Jungle | 13,550 / 16,350 | 109.2 (102.5+6.7) | 178.4 (168.5+9.9) | +63.4% | 71.6 | 107.7 | +50.6% | 4,233 | 4,233 | +0.0% | 3,846 | 3,846 | +0.0% |
| Amaterasu | Solo | 13,000 / 14,550 | 122.3 (108.1+14.2) | 150.6 (126.5+24.1) | +23.2% | 77.0 | 93.8 | +21.8% | 10,646 | 10,140 | -4.8% | 8,488 | 8,312 | -2.1% |
| Anhur | Carry | 13,750 / 14,850 | 407.2 (371.4+35.8) | 489.1 (435.0+54.2) | +20.1% | 269.2 | 311.6 | +15.8% | 4,148 | 5,960 | +43.7% | 3,644 | 4,250 | +16.6% |
| Anubis | Mid | 15,000 / 16,600 | 148.9 (125.4+23.5) | 195.5 (166.5+29.0) | +31.3% | 97.6 | 127.0 | +30.2% | 4,202 | 4,202 | +0.0% | 3,912 | 3,912 | +0.0% |
| Aphrodite | Mid Support | 12,300 / 15,350 | 137.7 (84.0+53.7) | 130.1 (82.4+47.7) | -5.5% | 87.6 | 81.0 | -7.6% | 4,755 | 7,029 | +47.8% | 4,615 | 8,258 | +78.9% |
| Apollo | Carry | 13,750 / 14,850 | 391.3 (357.9+33.4) | 474.1 (423.5+50.6) | +21.1% | 258.7 | 302.0 | +16.8% | 4,076 | 5,871 | +44.0% | 3,580 | 4,186 | +16.9% |
| Ares | Support | 12,800 / 14,800 | 60.3 (60.3+0.0) | 105.4 (105.4+0.0) | +75.0% | 37.9 | 65.6 | +73.0% | 9,868 | 12,249 | +24.1% | 8,565 | 10,001 | +16.8% |
| Artemis | Carry | 13,700 / 14,950 | 401.1 (379.6+21.6) | 485.6 (446.7+38.9) | +21.1% | 258.4 | 295.2 | +14.2% | 3,788 | 5,518 | +45.7% | 3,353 | 3,959 | +18.1% |
| Artio | Solo Support | 13,350 / 14,550 | 100.3 (58.3+42.0) | 194.6 (138.4+56.2) | +94.1% | 63.1 | 121.2 | +91.9% | 10,100 | 10,639 | +5.3% | 9,166 | 8,740 | -4.6% |
| Athena | Support | 13,350 / 14,800 | 117.6 (84.4+33.2) | 180.4 (147.2+33.2) | +53.4% | 74.0 | 112.3 | +51.7% | 10,758 | 12,249 | +13.9% | 9,271 | 10,001 | +7.9% |
| Atlas | Support | 13,350 / 14,750 | 100.9 (83.7+17.2) | 91.2 (72.9+18.2) | -9.6% | 63.5 | 57.4 | -9.6% | 8,661 | 11,736 | +35.5% | 9,955 | 11,503 | +15.5% |
| Awilix | Jungle | 15,550 / 16,600 | 318.4 (252.7+65.8) | 567.6 (438.8+128.8) | +78.3% | 200.5 | 351.7 | +75.4% | 4,959 | 4,117 | -17.0% | 4,594 | 3,752 | -18.3% |
| Bacchus | Support | 13,300 / 14,800 | 88.9 (60.3+28.7) | 138.8 (105.4+33.4) | +56.1% | 56.0 | 86.4 | +54.4% | 9,339 | 12,093 | +29.5% | 10,637 | 10,082 | -5.2% |
| Baron Samedi | Mid Support | 13,200 / 15,600 | 176.1 (82.4+93.7) | 202.4 (95.2+107.2) | +14.9% | 109.6 | 129.0 | +17.7% | 5,331 | 5,989 | +12.3% | 5,058 | 7,152 | +41.4% |
| Bastet | Jungle | 14,650 / 16,600 | 307.0 (257.9+49.1) | 500.3 (430.0+70.3) | +63.0% | 206.6 | 310.0 | +50.1% | 4,117 | 4,117 | +0.0% | 3,702 | 3,702 | +0.0% |
| Bellona | Solo | 13,700 / 14,550 | 142.6 (117.1+25.4) | 214.6 (171.1+43.5) | +50.5% | 89.8 | 133.6 | +48.9% | 10,730 | 10,432 | -2.8% | 9,758 | 8,380 | -14.1% |
| Cabrakan | Solo Support | 13,250 / 14,550 | 118.1 (63.3+54.8) | 211.5 (145.9+65.7) | +79.2% | 74.3 | 131.7 | +77.2% | 10,164 | 10,639 | +4.7% | 8,670 | 8,740 | +0.8% |
| Cerberus | Solo Support | 13,600 / 14,750 | 84.2 (52.2+32.0) | 86.4 (52.2+34.2) | +2.6% | 53.0 | 54.4 | +2.6% | 9,179 | 11,614 | +26.5% | 10,861 | 11,460 | +5.5% |
| Cernunnos | Carry Jungle | 13,900 / 15,400 | 359.9 (340.1+19.8) | 285.6 (254.7+31.0) | -20.6% | 237.9 | 177.7 | -25.3% | 3,788 | 5,095 | +34.5% | 3,353 | 3,656 | +9.0% |
| Chaac | Solo | 14,150 / 15,150 | 187.6 (113.6+74.0) | 212.0 (127.3+84.7) | +13.0% | 120.9 | 133.5 | +10.4% | 7,349 | 9,653 | +31.3% | 7,373 | 7,893 | +7.1% |
| Charon | Support | 14,800 / 14,750 | 158.4 (93.4+64.9) | 102.0 (55.4+46.5) | -35.6% | 101.0 | 64.2 | -36.4% | 6,000 | 11,614 | +93.6% | 5,374 | 11,383 | +111.8% |
| Chiron | Carry | 14,200 / 15,500 | 300.3 (236.8+63.5) | 529.8 (454.6+75.3) | +76.4% | 196.3 | 320.7 | +63.4% | 4,644 | 5,095 | +9.7% | 4,110 | 3,656 | -11.1% |
| Chronos | Mid Carry | 14,700 / 16,400 | 251.7 (153.6+98.1) | 339.9 (224.3+115.6) | +35.0% | 164.9 | 229.7 | +39.3% | 4,016 | 4,016 | +0.0% | 3,630 | 3,630 | +0.0% |
| Cu Chulainn | Solo | 15,000 / 14,550 | 121.5 (36.2+85.2) | 242.4 (130.3+112.1) | +99.6% | 76.5 | 150.9 | +97.4% | 12,045 | 10,282 | -14.6% | 10,465 | 7,901 | -24.5% |
| Cupid | Carry | 13,550 / 15,400 | 385.1 (367.8+17.4) | 290.4 (258.4+32.1) | -24.6% | 254.6 | 180.7 | -29.0% | 3,788 | 5,095 | +34.5% | 3,353 | 3,656 | +9.0% |
| Da Ji | Jungle | 14,450 / 16,000 | 338.8 (279.2+59.6) | 410.5 (331.9+78.7) | +21.2% | 228.0 | 254.9 | +11.8% | 3,865 | 3,865 | +0.0% | 3,452 | 3,452 | +0.0% |
| Danzaburou | Carry | 14,050 / 15,500 | 280.9 (180.8+100.1) | 348.1 (256.6+91.5) | +23.9% | 176.9 | 224.6 | +27.0% | 3,788 | 5,412 | +42.9% | 3,353 | 3,883 | +15.8% |
| Discordia | Mid | 15,100 / 16,600 | 234.0 (153.4+80.6) | 263.5 (172.8+90.7) | +12.6% | 147.4 | 171.2 | +16.2% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Eset | Mid | 14,750 / 16,600 | 202.9 (137.2+65.8) | 303.3 (206.2+97.2) | +49.5% | 132.9 | 197.0 | +48.2% | 4,202 | 3,760 | -10.5% | 5,058 | 3,399 | -32.8% |
| Fenrir | Jungle | 16,150 / 16,600 | 291.0 (239.4+51.6) | 520.4 (446.1+74.3) | +78.8% | 191.1 | 322.4 | +68.7% | 7,226 | 4,571 | -36.7% | 6,587 | 4,052 | -38.5% |
| Ganesha | Support | 12,850 / 14,750 | 99.2 (59.5+39.7) | 105.1 (59.5+45.6) | +5.9% | 62.5 | 66.2 | +5.9% | 8,291 | 11,613 | +40.1% | 8,547 | 11,383 | +33.2% |
| Geb | Support | 12,950 / 14,700 | 109.4 (58.3+51.1) | 103.7 (58.3+45.4) | -5.2% | 68.9 | 65.3 | -5.2% | 7,428 | 14,002 | +88.5% | 8,516 | 12,929 | +51.8% |
| Gilgamesh | Solo Jungle | 15,500 / 14,800 | 144.1 (118.1+26.0) | 263.4 (223.3+40.1) | +82.8% | 92.8 | 160.1 | +72.5% | 11,805 | 9,417 | -20.2% | 8,204 | 7,173 | -12.6% |
| Guan Yu | Solo Support | 15,200 / 14,500 | 105.5 (77.7+27.8) | 167.7 (135.9+31.9) | +59.0% | 66.4 | 104.4 | +57.3% | 9,933 | 9,611 | -3.2% | 9,781 | 9,611 | -1.7% |
| Hades | Solo | 17,050 / 15,950 | 183.6 (108.8+74.8) | 207.1 (118.4+88.7) | +12.8% | 117.0 | 135.7 | +16.0% | 7,086 | 6,732 | -5.0% | 6,629 | 6,298 | -5.0% |
| Hecate | Mid | 14,700 / 16,600 | 285.6 (130.0+155.6) | 364.7 (166.5+198.2) | +27.7% | 184.8 | 236.9 | +28.2% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Hercules | Solo | 15,050 / 14,550 | 125.8 (70.0+55.8) | 226.2 (163.9+62.4) | +79.8% | 79.2 | 140.9 | +77.8% | 10,112 | 9,968 | -1.4% | 8,860 | 8,173 | -7.8% |
| Horus | Support | 13,300 / 14,500 | 65.3 (61.2+4.1) | 111.9 (107.3+4.6) | +71.3% | 41.1 | 69.7 | +69.4% | 8,603 | 9,844 | +14.4% | 8,326 | 9,679 | +16.3% |
| Hou Yi | Carry | 13,750 / 15,300 | 404.5 (368.1+36.4) | 373.7 (311.1+62.7) | -7.6% | 267.4 | 235.3 | -12.0% | 4,076 | 5,446 | +33.6% | 3,580 | 3,883 | +8.5% |
| Hua Mulan | Solo | 13,450 / 14,550 | 108.1 (65.3+42.8) | 202.3 (152.5+49.7) | +87.2% | 68.0 | 125.9 | +85.1% | 10,652 | 10,432 | -2.1% | 9,345 | 8,380 | -10.3% |
| Hun Batz | Jungle | 16,150 / 16,600 | 381.4 (274.7+106.8) | 564.8 (433.2+131.7) | +48.1% | 250.6 | 349.9 | +39.7% | 4,233 | 4,233 | +0.0% | 3,752 | 3,752 | +0.0% |
| Ishtar | Carry | 15,400 / 14,850 | 440.4 (430.8+9.5) | 444.2 (429.9+14.3) | +0.9% | 291.1 | 283.0 | -2.8% | 3,861 | 5,608 | +45.2% | 3,416 | 4,022 | +17.7% |
| Ix Chel | Mid Support | 15,200 / 15,350 | 367.4 (141.9+225.5) | 223.1 (77.5+145.6) | -39.3% | 231.3 | 138.8 | -40.0% | 3,866 | 7,164 | +85.3% | 3,595 | 8,508 | +136.6% |
| Izanami | Carry | 13,550 / 15,400 | 375.5 (356.6+18.9) | 298.9 (251.3+47.6) | -20.4% | 248.2 | 186.0 | -25.1% | 3,788 | 5,095 | +34.5% | 3,353 | 3,656 | +9.0% |
| Janus | Mid | 14,700 / 16,600 | 245.6 (130.0+115.5) | 313.8 (166.5+147.3) | +27.8% | 158.9 | 203.8 | +28.3% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Jing Wei | Carry | 14,250 / 14,900 | 470.5 (448.3+22.2) | 487.7 (458.5+29.2) | +3.7% | 303.1 | 303.7 | +0.2% | 3,788 | 5,518 | +45.7% | 3,353 | 3,959 | +18.1% |
| Jormungandr | Solo Support | 15,450 / 14,550 | 134.1 (70.8+63.3) | 178.9 (108.0+70.9) | +33.5% | 84.4 | 111.4 | +32.0% | 9,896 | 10,772 | +8.8% | 8,980 | 8,849 | -1.5% |
| Kali | Jungle | 15,150 / 15,900 | 285.6 (260.3+25.4) | 299.5 (243.0+56.6) | +4.9% | 184.0 | 179.2 | -2.6% | 4,233 | 5,627 | +32.9% | 3,752 | 4,064 | +8.3% |
| Khepri | Support | 15,200 / 14,750 | 195.4 (139.7+55.7) | 99.8 (58.3+41.4) | -49.0% | 121.6 | 62.8 | -48.3% | 4,796 | 11,736 | +144.7% | 4,227 | 11,503 | +172.1% |
| Kukulkan | Mid | 14,850 / 16,600 | 219.2 (134.0+85.2) | 276.0 (166.5+109.5) | +25.9% | 140.0 | 179.3 | +28.1% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Loki | Jungle | 14,700 / 16,300 | 230.6 (213.2+17.4) | 323.7 (303.1+20.6) | +40.4% | 155.2 | 206.9 | +33.3% | 4,117 | 4,117 | +0.0% | 3,702 | 3,702 | +0.0% |
| Medusa | Carry | 13,750 / 15,400 | 388.6 (352.8+35.9) | 314.8 (242.4+72.4) | -19.0% | 256.9 | 195.9 | -23.7% | 3,788 | 5,095 | +34.5% | 3,353 | 3,656 | +9.0% |
| Mercury | Jungle | 14,700 / 15,650 | 489.6 (480.9+8.8) | 332.1 (315.2+16.8) | -32.2% | 333.1 | 201.0 | -39.7% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Merlin | Mid | 15,350 / 16,600 | 328.1 (138.6+189.5) | 360.8 (166.5+194.3) | +10.0% | 209.5 | 234.4 | +11.9% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Mordred | Solo Jungle | 13,050 / 14,550 | 101.2 (62.8+38.5) | 194.5 (146.7+47.9) | +92.1% | 63.7 | 121.1 | +90.0% | 10,488 | 10,296 | -1.8% | 9,545 | 8,439 | -11.6% |
| Morgan Le Fay | Mid | 15,050 / 16,600 | 205.7 (126.4+79.4) | 264.4 (175.6+88.8) | +28.5% | 134.8 | 171.7 | +27.4% | 4,015 | 4,015 | +0.0% | 4,929 | 3,630 | -26.4% |
| Ne Zha | Jungle | 14,850 / 16,000 | 377.4 (351.2+26.2) | 478.1 (435.9+42.2) | +26.7% | 254.0 | 296.8 | +16.9% | 5,708 | 4,233 | -25.8% | 5,167 | 3,752 | -27.4% |
| Neith | Carry Mid | 14,800 / 15,400 | 296.1 (184.3+111.8) | 358.1 (246.4+111.7) | +20.9% | 189.1 | 222.8 | +17.8% | 3,788 | 5,095 | +34.5% | 3,353 | 3,656 | +9.0% |
| Nemesis | Jungle | 16,200 / 15,650 | 271.8 (226.1+45.7) | 424.2 (379.0+45.2) | +56.1% | 182.9 | 260.7 | +42.5% | 5,437 | 4,585 | -15.7% | 4,896 | 4,064 | -17.0% |
| Nu Wa | Mid | 15,200 / 16,600 | 251.3 (166.9+84.4) | 282.3 (187.0+95.2) | +12.3% | 158.2 | 183.3 | +15.9% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Nut | Carry Mid | 16,200 / 15,650 | 352.1 (336.1+16.0) | 252.4 (228.7+23.7) | -28.3% | 243.4 | 158.9 | -34.7% | 4,045 | 5,413 | +33.8% | 3,580 | 3,883 | +8.5% |
| Odin | Solo Jungle | 13,400 / 14,550 | 135.0 (97.7+37.3) | 190.4 (157.9+32.6) | +41.1% | 84.1 | 118.6 | +41.1% | 7,749 | 10,296 | +32.9% | 7,552 | 8,439 | +11.8% |
| Osiris | Solo | 13,300 / 14,550 | 130.3 (81.0+49.3) | 299.5 (224.8+74.6) | +129.7% | 82.1 | 186.5 | +127.2% | 11,936 | 10,167 | -14.8% | 8,390 | 7,735 | -7.8% |
| Pele | Jungle | 14,850 / 16,000 | 292.7 (286.4+6.4) | 319.9 (311.9+8.0) | +9.3% | 192.3 | 198.6 | +3.3% | 4,307 | 4,307 | +0.0% | 3,817 | 3,817 | +0.0% |
| Poseidon | Mid | 15,200 / 16,600 | 243.2 (181.5+61.7) | 264.1 (182.2+81.8) | +8.6% | 155.3 | 171.5 | +10.5% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Princess Bari | Carry Mid | 17,500 / 15,450 | 265.2 (187.7+77.5) | 407.8 (368.2+39.7) | +53.8% | 172.3 | 263.1 | +52.7% | 4,046 | 4,389 | +8.5% | 3,745 | 4,062 | +8.5% |
| Ra | Mid | 15,200 / 16,300 | 279.4 (165.2+114.2) | 316.1 (150.9+165.1) | +13.1% | 178.4 | 211.0 | +18.3% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Rama | Carry | 13,750 / 15,400 | 380.7 (376.5+4.2) | 481.4 (473.7+7.7) | +26.4% | 251.7 | 276.5 | +9.9% | 3,788 | 5,095 | +34.5% | 3,353 | 3,656 | +9.0% |
| Ratatoskr | Jungle | 13,400 / 14,300 | 280.0 (216.5+63.5) | 350.7 (279.0+71.8) | +25.2% | 194.7 | 223.8 | +14.9% | 5,715 | 6,419 | +12.3% | 5,065 | 5,689 | +12.3% |
| Scylla | Mid | 14,750 / 16,600 | 244.4 (128.0+116.4) | 332.4 (166.5+165.9) | +36.0% | 160.1 | 216.0 | +34.9% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Sobek | Support | 13,150 / 14,750 | 107.6 (60.3+47.3) | 114.6 (60.3+54.3) | +6.5% | 67.7 | 72.1 | +6.5% | 8,313 | 11,475 | +38.0% | 9,486 | 11,247 | +18.6% |
| Sol | Mid Carry | 14,600 / 16,400 | 224.2 (197.4+26.8) | 277.1 (244.6+32.5) | +23.6% | 146.9 | 187.2 | +27.5% | 3,760 | 3,760 | +0.0% | 3,399 | 3,399 | +0.0% |
| Sun Wukong | Solo | 14,250 / 14,550 | 77.5 (72.7+4.8) | 203.7 (198.6+5.0) | +162.8% | 51.2 | 126.8 | +147.5% | 7,595 | 10,167 | +33.9% | 8,548 | 7,735 | -9.5% |
| Susano | Jungle | 14,550 / 16,600 | 357.5 (319.0+38.5) | 525.5 (478.8+46.7) | +47.0% | 234.8 | 325.6 | +38.7% | 4,117 | 4,117 | +0.0% | 3,752 | 3,752 | +0.0% |
| Sylvanus | Support | 12,850 / 14,750 | 71.2 (47.6+23.6) | 71.2 (47.6+23.6) | +0.0% | 44.8 | 44.8 | +0.0% | 8,136 | 11,736 | +44.2% | 7,949 | 11,503 | +44.7% |
| Thanatos | Jungle | 16,150 / 16,600 | 389.8 (295.2+94.7) | 582.7 (465.9+116.9) | +49.5% | 256.1 | 361.0 | +41.0% | 4,655 | 4,655 | +0.0% | 4,126 | 4,126 | +0.0% |
| The Morrigan | Mid | 15,250 / 16,600 | 209.9 (161.6+48.3) | 245.7 (185.1+60.6) | +17.0% | 134.0 | 159.6 | +19.1% | 3,894 | 3,894 | +0.0% | 3,452 | 3,452 | +0.0% |
| Thor | Jungle Solo | 14,450 / 14,900 | 299.4 (262.2+37.3) | 230.8 (201.0+29.8) | -22.9% | 201.5 | 140.3 | -30.4% | 4,559 | 9,945 | +118.2% | 3,986 | 7,633 | +91.5% |
| Tsukuyomi | Jungle | 14,600 / 15,600 | 308.5 (272.7+35.7) | 369.4 (333.8+35.6) | +19.7% | 207.6 | 227.0 | +9.4% | 4,307 | 5,718 | +32.8% | 3,766 | 4,074 | +8.2% |
| Ullr | Carry | 14,600 / 15,500 | 359.0 (259.8+99.2) | 528.0 (438.3+89.7) | +47.1% | 241.6 | 319.6 | +32.3% | 4,148 | 5,535 | +33.4% | 3,644 | 3,947 | +8.3% |
| Vulcan | Mid | 12,700 / 16,600 | 274.5 (131.2+143.3) | 365.7 (166.5+199.2) | +33.2% | 175.3 | 237.5 | +35.5% | 4,015 | 4,015 | +0.0% | 3,630 | 3,630 | +0.0% |
| Xbalanque | Carry | 15,350 / 14,850 | 460.8 (445.5+15.3) | 466.7 (443.1+23.6) | +1.3% | 296.9 | 297.3 | +0.2% | 3,788 | 5,518 | +45.7% | 3,353 | 3,959 | +18.1% |
| Xing Tian | Support Solo | 15,050 / 14,750 | 23.9 (0.0+23.9) | 23.9 (0.0+23.9) | +0.0% | 15.0 | 15.0 | +0.0% | 1,657 | 2,250 | +35.7% | 1,528 | 2,385 | +56.1% |
| Yemoja | Support | 15,300 / 14,750 | 95.3 (89.5+5.8) | 61.8 (57.7+4.0) | -35.2% | 57.2 | 38.9 | -32.0% | 7,445 | 11,912 | +60.0% | 7,268 | 11,675 | +60.6% |
| Ymir | Support | 13,300 / 14,750 | 118.6 (63.3+55.3) | 118.6 (63.3+55.3) | +0.0% | 74.7 | 74.7 | +0.0% | 9,741 | 12,300 | +26.3% | 10,017 | 13,401 | +33.8% |
| Zeus | Mid | 15,050 / 16,600 | 243.8 (140.1+103.7) | 325.7 (208.0+117.7) | +33.6% | 157.8 | 214.6 | +36.0% | 5,050 | 3,894 | -22.9% | 4,548 | 3,452 | -24.1% |
