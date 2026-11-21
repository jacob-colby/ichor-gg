# Done criterion 3 — the 10-god spot check (2026-11-14)

A packet for Jacob's sitting: ten Conquest gods, two per role, each with the
side-by-side verdict and the numbers behind it. **Diagnosis only.** Nothing here
changes a model, a weight, a verdict, `COVERAGE_MIN` or `COVERAGE_GAP`.

This is a dated, point-in-time file. It goes stale on the next
`chore(data): daily community refresh`; the live verdicts are on each god's page.

## Inputs and the commands every number came from

Run from `pipeline/` on `e58fe531` (main after the 2026-11-14 refresh), Windows:

| Command | What it gave |
|---|---|
| `python -m smite.calibrate --control` | input fingerprint **`0875fb0ffa62`**, random-core baseline 5.7%, eff 0.70 : fit 0.30 → 43.0% (7.6× chance), eff 0.45 : fit 0.55 → 39.5% (7.0×). Same fingerprint as `docs/CURRENT.md`. (`_calibration.md` is stamped `047109f54fd7`, a different dataset — not used.) |
| `python -m smite.side_by_side --out <scratch>/sbs.md --json <scratch>/sbs` | every verdict, damage/EHP figure, breakpoint, coverage share, diff, model reason and best-swap below; and the role counts. Written to scratch, not to `viewer/public/`. |
| `PYTHONPATH=. PYTHONIOENCODING=utf-8 python ../docs/audits/2026-11-spot-check_extract.py <scratch>/sbs` | the selection (rule below) and the tables in this file. It adds the god's own record from `data/builds/<God>-Conquest.md` (`god_matches_played`, `god_matches_won`, `god_win_rate`) and `tierlist.wilson_lower_bound` (z 1.96, `MIN_MATCHES` 30). |

**The scratch run against the committed viewer files:** 92 of 96 per-god JSON
files are byte-identical to `viewer/public/side_by_side/`; the four that differ
(Jormungandr, Kuzenbo, Mercury, Nike — the known Windows-vs-CI `.xx5` tie
noise) have the same verdict, the same Ichor six and the same damage axis. None
of the four is in this packet. So the god pages on the preview show the numbers
below.

## How to read the numbers

- **Axes** are Ichor ÷ community. *Damage* is the geometric mean of four
  ratios (burst and 10s sustained, each vs the median squishy and the median
  tank); *survival* is the geometric mean of effective health vs physical and vs
  magical. Band ±5%.
- **The verdict is judged on the 2/4/6-item weighted axes** (equal weights), not
  the six-item ones. Both are printed; the "six items only" verdict is the old rule.
- **Readable** = not "not enough simulated" (either build under 50% of its gold
  fully simulated, or a gap over 14%) and not "aspect not simulated".
- **Community record per item:** `Pick` and the item's win rate are the god's
  community-build sighting (rounded to 2 places at source).
  `Est. matches = round(pick × god matches)`; wins = `round(win × est)`; the
  Wilson lower bound is on those. Compare the item's win rate with **the god's
  own win rate**, not with 50%. Under 30 estimated matches there is no bound.
  An Ichor item with no community row was never seen in this god's builds.
- **Ichor's reason** is the `model` archetype's own score for that god
  (`side_by_side.ARCHETYPE = "model"`): rank, quality = blend of efficiency
  (gold value of the stats) and fit (role/kit weight), and the score of the
  weakest item Ichor kept. **Best swap**: the damage / survival axes if that
  community item replaced the named Ichor item.

## The selection rule (fixed before reading any god's numbers)

1. Readable gods only, Conquest, base kit.
2. In each role, sort readable gods by community matches, most first.
3. **Slot A ("Ichor reads better"):** the most-played god with verdict
   "Ichor better". If the role has none, the readable god with the highest
   damage × survival product of the six-item axes, and say so.
4. **Slot B ("community better or trade-off"):** Nemesis if it is readable;
   otherwise the most-played god with verdict "community better" or "trade-off".
5. "Level", "early-game" and "late-game" gods are not drawn.

Most-played is the rule because a bigger community record is the one Jacob can
check the item rows against — it is not chosen to favour either side.

**Readable counts this run: 57 of 95** — Carry 10, Jungle 11, Mid 20, Solo 11,
Support 5 (same totals as the 2026-11-14 brief). Every role has at least two, so
no role stops.

**Two rule hits worth stating up front:**

- **Nemesis is not readable.** It is "not enough simulated": Ichor 82.6% of
  gold simulated vs community 100%, a 17.4% gap over the 14% maximum (Tekko-Kagi's
  pathfinding is the unsimulated item). Without the rule it would read "level";
  six-item-only "community better". It is not in the packet.
- **Support has no "Ichor better" god** (role counts: community better 3,
  trade-off 2, withheld 8). Slot A falls back to rule 3's second half: Sobek,
  a trade-off.

## The ten

| Role | God | Slot | Matches | Verdict | Weighted damage / survival | Six-item damage / survival |
|---|---|---|---:|---|---|---|
| Carry | Xbalanque | A | 636 | Ichor better | 1.056 / 1.075 | 1.212 / 1.045 |
| Carry | Hou Yi | B | 994 | community better | 0.970 / 0.885 | 0.945 / 0.861 |
| Jungle | Loki | A | 1,079 | Ichor better | 1.040 / 1.127 | 1.092 / 1.196 |
| Jungle | Thor | B | 1,361 | trade-off | 0.504 / 1.730 | 0.312 / 2.496 |
| Mid | Vulcan | A | 794 | Ichor better | 1.051 / 1.042 | 1.092 / 1.132 |
| Mid | Nox | B | 1,348 | trade-off | 0.824 / 1.548 | 0.819 / 1.748 |
| Solo | Odin | A | 286 | Ichor better | 1.184 / 1.067 | 1.180 / 1.181 |
| Solo | Cu Chulainn | B | 643 | trade-off | 1.120 / 0.811 | 1.202 / 0.786 |
| Support | Sobek | A (fallback) | 659 | trade-off | 1.245 / 0.880 | 1.171 / 0.888 |
| Support | Ymir | B | 1,166 | community better | 0.860 / 1.032 | 0.799 / 1.031 |

Tally: Ichor better 4, community better 2, trade-off 4. The pages are linked
from the pull request.

### What stands out across the ten (for the sitting, not a finding)

- **Three of the four trade-offs are Ichor building tank items onto a god the
  community builds for damage** (Thor, Nox; Sobek in Support). Thor is the
  extreme: 27–37% of the community's damage for 2.4–2.6× its effective health.
  The verdict rule has no exchange rate between the axes, so it calls that a
  trade-off and not a loss. Whether that is defensible is exactly Jacob's call.
- **Two "Ichor better" verdicts sit on the band edge.** Vulcan's weighted damage
  is 1.051 against a 1.05 threshold, with survival 1.042 inside the band; Loki's
  damage is 1.040 (inside) and the verdict is carried by survival 1.127.
- **Ichor's Sobek and Ymir sixes are the same six items** (Genji's Guard,
  Kinetic Cuirass, Freya's Tears, Draconic Scale, Amanita Charm, Erosion).
- **Hou Yi's Ichor six is an Intelligence build on a physical hunter** —
  Rod of Tahuti (fit 0.11), Bragi's Harp, Nimble Ring, Death Metal — and none of
  those four appears in Hou Yi's 994-match community record.

# Per god

## Xbalanque — Carry

Picked by: most-played 'Ichor better'. God record: 370/636 won (58.2%). Kit: base.

**Verdict: Ichor better.** Damage axis 1.212, survival axis 1.045 (Ichor ÷ community, 6 items; weighted over 2/4/6: 1.056 / 1.075). Without the coverage rule: Ichor better; six items only: Ichor better. Simulated share Ichor 100%, community 100% (gap 0.0%).

- Ichor: Golden Blade, Tyrfing, Lernaean Bow, Dominance, Qin's Blade, Demon Blade (15,300 g)
- Community: Tyrfing, Odysseus' Bow, Dominance, Silverbranch Bow, The Executioner, Devourer's Gauntlet (15,200 g)
- Shared: Tyrfing, Dominance
- Community slot 6: Hunter's Bow (unfinished) → Devourer's Gauntlet

| At 6 items | Ichor | Community | Ichor ÷ community |
|---|---:|---:|---:|
| Burst vs squishy | 752 | 448 | 1.676 |
| Burst vs tank | 472 | 282 | 1.674 |
| 10s sustained vs squishy | 9,782 | 11,069 | 0.884 |
| 10s sustained vs tank | 6,592 | 7,573 | 0.870 |
| Effective health vs physical | 4,130 | 3,972 | 1.040 |
| Effective health vs magical | 3,656 | 3,482 | 1.050 |

| Power at | damage axis | survival axis | Ichor sustained vs squishy | community |
|---|---:|---:|---:|---:|
| 2 items | 0.909 | 1.090 | 2,782 | 3,769 |
| 4 items | 1.068 | 1.090 | 5,403 | 7,414 |
| 6 items | 1.212 | 1.045 | 9,782 | 11,069 |

| Differing item | Side | Pick | Est. matches | Item win vs god | Wilson LB | Ichor's reason (model) | Best swap |
|---|---|---:|---:|---|---:|---|---|
| Odysseus' Bow | community | 26% | 165 | 56% vs 58% (-2.2 pt) | 0.481 | model rank #23, quality 0.394 (efficiency 0.38, fit 0.43); the weakest item Ichor kept scores 0.492, 0.098 short | for Golden Blade: 1.078 / 0.917 |
| Silverbranch Bow | community | 21% | 134 | 62% vs 58% (+3.8 pt) | 0.535 | model rank #14, quality 0.437 (efficiency 0.40, fit 0.52); the weakest item Ichor kept scores 0.492, 0.056 short | for Golden Blade: 1.122 / 0.917 |
| The Executioner | community | 15% | 95 | 69% vs 58% (+10.8 pt) | 0.596 | model rank #34, quality 0.342 (efficiency 0.30, fit 0.43); the weakest item Ichor kept scores 0.492, 0.151 short | for Golden Blade: 1.050 / 0.917 |
| Devourer's Gauntlet | community | 26% | 165 | 60% vs 58% (+1.8 pt) | 0.524 | model rank #30, quality 0.378 (efficiency 0.40, fit 0.33); the weakest item Ichor kept scores 0.492, 0.115 short | for Golden Blade: 1.080 / 1.016 |
| Golden Blade | ichor | — | — | not in community record | — | model rank #2, quality 0.534 (efficiency 0.45, fit 0.73); the weakest item Ichor kept scores 0.492 | — |
| Lernaean Bow | ichor | — | — | not in community record | — | model rank #3, quality 0.524 (efficiency 0.47, fit 0.64); the weakest item Ichor kept scores 0.492 | — |
| Qin's Blade | ichor | — | — | not in community record | — | model rank #6, quality 0.492 (efficiency 0.39, fit 0.72); the weakest item Ichor kept scores 0.492 | — |
| Demon Blade | ichor | — | — | not in community record | — | model rank #5, quality 0.516 (efficiency 0.36, fit 0.87); the weakest item Ichor kept scores 0.492 | — |

**What would make this indefensible:** Ichor's damage lead is all burst (+67%) while it trails 10s sustained by 12–13% and is behind on damage at 2 items (0.909); if one rotation should not weigh the same as ten seconds of attacks for a hunter, this is not "Ichor better". Also: none of Ichor's four own items is in the 636-match record, and The Executioner, which Ichor ranks #34, has a lower bound (0.596) above the god's own 58.2%.

## Hou Yi — Carry

Picked by: most-played 'community better' or 'trade-off'. God record: 512/994 won (51.5%). Kit: base.

**Verdict: community better.** Damage axis 0.945, survival axis 0.861 (Ichor ÷ community, 6 items; weighted over 2/4/6: 0.970 / 0.885). Without the coverage rule: community better; six items only: community better. Simulated share Ichor 100%, community 100% (gap 0.0%).

- Ichor: Jotunn's Revenge, Tyrfing, Death Metal, Nimble Ring, Bragi's Harp, Rod of Tahuti (15,350 g)
- Community: Devourer's Gauntlet, Dagger of Frenzy, Dominance, Riptalon, Deathbringer, The Executioner (15,750 g)
- Community slot 6: Hunter's Bow (unfinished) → The Executioner

| At 6 items | Ichor | Community | Ichor ÷ community |
|---|---:|---:|---:|
| Burst vs squishy | 1,008 | 931 | 1.083 |
| Burst vs tank | 602 | 578 | 1.042 |
| 10s sustained vs squishy | 8,345 | 9,236 | 0.904 |
| 10s sustained vs tank | 5,031 | 6,438 | 0.781 |
| Effective health vs physical | 4,377 | 5,183 | 0.844 |
| Effective health vs magical | 3,840 | 4,377 | 0.877 |

| Power at | damage axis | survival axis | Ichor sustained vs squishy | community |
|---|---:|---:|---:|---:|
| 2 items | 1.068 | 0.937 | 2,675 | 2,252 |
| 4 items | 0.905 | 0.861 | 4,818 | 5,511 |
| 6 items | 0.945 | 0.861 | 8,345 | 9,236 |

| Differing item | Side | Pick | Est. matches | Item win vs god | Wilson LB | Ichor's reason (model) | Best swap |
|---|---|---:|---:|---|---:|---|---|
| Devourer's Gauntlet | community | 81% | 805 | 53% vs 52% (+1.5 pt) | 0.496 | model rank #57, quality 0.365 (efficiency 0.40, fit 0.29); the weakest item Ichor kept scores 0.517, 0.152 short | for Jotunn's Revenge: 1.052 / 1.120 |
| Dagger of Frenzy | community | 74% | 736 | 53% vs 52% (+1.5 pt) | 0.494 | model rank #34, quality 0.416 (efficiency 0.42, fit 0.40); the weakest item Ichor kept scores 0.517, 0.101 short | for Jotunn's Revenge: 1.116 / 1.000 |
| Dominance | community | 34% | 338 | 53% vs 52% (+1.5 pt) | 0.476 | model rank #10, quality 0.501 (efficiency 0.47, fit 0.56); the weakest item Ichor kept scores 0.517, 0.016 short | for Jotunn's Revenge: 1.079 / 1.000 |
| Riptalon | community | 20% | 199 | 54% vs 52% (+2.5 pt) | 0.468 | model rank #14, quality 0.479 (efficiency 0.45, fit 0.56); the weakest item Ichor kept scores 0.517, 0.038 short | for Jotunn's Revenge: 1.089 / 1.117 |
| Deathbringer | community | 19% | 189 | 60% vs 52% (+8.5 pt) | 0.527 | model rank #24, quality 0.450 (efficiency 0.44, fit 0.46); the weakest item Ichor kept scores 0.517, 0.067 short | for Jotunn's Revenge: 1.100 / 1.000 |
| The Executioner | community | 24% | 239 | 49% vs 52% (-2.5 pt) | 0.427 | model rank #69, quality 0.326 (efficiency 0.30, fit 0.38); the weakest item Ichor kept scores 0.517, 0.190 short | for Jotunn's Revenge: 1.131 / 1.000 |
| Jotunn's Revenge | ichor | — | — | not in community record | — | model rank #4, quality 0.539 (efficiency 0.65, fit 0.27); the weakest item Ichor kept scores 0.517 | — |
| Tyrfing | ichor | 11% | 109 | 47% vs 52% (-4.5 pt) | 0.377 | model rank #3, quality 0.578 (efficiency 0.53, fit 0.68); the weakest item Ichor kept scores 0.517 | — |
| Death Metal | ichor | — | — | not in community record | — | model rank #2, quality 0.594 (efficiency 0.63, fit 0.52); the weakest item Ichor kept scores 0.517 | — |
| Nimble Ring | ichor | — | — | not in community record | — | model rank #5, quality 0.529 (efficiency 0.57, fit 0.45); the weakest item Ichor kept scores 0.517 | — |
| Bragi's Harp | ichor | — | — | not in community record | — | model rank #6, quality 0.517 (efficiency 0.47, fit 0.62); the weakest item Ichor kept scores 0.517 | — |
| Rod of Tahuti | ichor | — | — | not in community record | — | model rank #1, quality 0.603 (efficiency 0.82, fit 0.11); the weakest item Ichor kept scores 0.517 | — |

**What would make this indefensible:** The community's survival lead (806 more EHP vs physical with no protection item in its six) is lifesteal — Devourer's Gauntlet's passive is worth +374 EHP and Riptalon's +215 in `sbs.md` — so if the multi-fight lifesteal chain overstates it, survival 0.885 moves toward the band and the verdict rests on damage 0.970 alone, which is inside it.

## Loki — Jungle

Picked by: most-played 'Ichor better'. God record: 579/1079 won (53.7%). Kit: base.

**Verdict: Ichor better.** Damage axis 1.092, survival axis 1.196 (Ichor ÷ community, 6 items; weighted over 2/4/6: 1.040 / 1.127). Without the coverage rule: Ichor better; six items only: Ichor better. Simulated share Ichor 100%, community 100% (gap 0.0%).

- Ichor: Jotunn's Revenge, Transcendence, The Reaper, Heartseeker, The Crusher, Titan's Bane (16,000 g)
- Community: Jotunn's Revenge, Hydra's Lament, Barbed Carver, Heartseeker, Titan's Bane, The Crusher (15,950 g)
- Shared: Jotunn's Revenge, Heartseeker, The Crusher, Titan's Bane

| At 6 items | Ichor | Community | Ichor ÷ community |
|---|---:|---:|---:|
| Burst vs squishy | 1,794 | 1,568 | 1.144 |
| Burst vs tank | 1,194 | 1,094 | 1.092 |
| 10s sustained vs squishy | 5,474 | 5,159 | 1.061 |
| 10s sustained vs tank | 3,480 | 3,241 | 1.074 |
| Effective health vs physical | 5,285 | 4,428 | 1.194 |
| Effective health vs magical | 4,750 | 3,966 | 1.198 |

| Power at | damage axis | survival axis | Ichor sustained vs squishy | community |
|---|---:|---:|---:|---:|
| 2 items | 0.963 | 1.000 | 1,318 | 1,354 |
| 4 items | 1.068 | 1.196 | 2,969 | 2,796 |
| 6 items | 1.092 | 1.196 | 5,474 | 5,159 |

| Differing item | Side | Pick | Est. matches | Item win vs god | Wilson LB | Ichor's reason (model) | Best swap |
|---|---|---:|---:|---|---:|---|---|
| Hydra's Lament | community | 34% | 367 | 57% vs 54% (+3.3 pt) | 0.518 | model rank #7, quality 0.597 (efficiency 0.55, fit 0.71); the weakest item Ichor kept scores 0.504 | for The Reaper: 1.030 / 0.779 |
| Barbed Carver | community | 18% | 194 | 55% vs 54% (+1.3 pt) | 0.481 | model rank #24, quality 0.436 (efficiency 0.36, fit 0.62); the weakest item Ichor kept scores 0.504, 0.067 short | for The Reaper: 1.003 / 0.836 |
| Transcendence | ichor | — | — | not in community record | — | model rank #12, quality 0.504 (efficiency 0.50, fit 0.52); the weakest item Ichor kept scores 0.504 | — |
| The Reaper | ichor | — | — | not in community record | — | model rank #3, quality 0.635 (efficiency 0.52, fit 0.91); the weakest item Ichor kept scores 0.504 | — |

**What would make this indefensible:** The verdict is carried by survival (weighted 1.127; damage 1.040 is inside the band), and that survival lead appears only from 4 items (1.000 → 1.196) when Transcendence and The Reaper come in; if their stacks fill slower in game than on the stack clock, Loki is "level". Note also that Hydra's Lament scores 0.597 for Loki, above the 0.504 of the weakest item Ichor kept, and is still not in the six — something other than score (a cap) excluded it.

## Thor — Jungle

Picked by: most-played 'community better' or 'trade-off'. God record: 749/1361 won (55.0%). Kit: base.

**Verdict: trade-off.** Damage axis 0.312, survival axis 2.496 (Ichor ÷ community, 6 items; weighted over 2/4/6: 0.504 / 1.730). Without the coverage rule: trade-off; six items only: trade-off. Simulated share Ichor 100%, community 100% (gap 0.0%).

- Ichor: Genji's Guard, Jotunn's Revenge, Berserker's Shield, Kinetic Cuirass, Shield Splitter, Amanita Charm (14,300 g)
- Community: Jotunn's Revenge, Hydra's Lament, The Crusher, Heartseeker, Titan's Bane, Avatar's Parashu (17,150 g)
- Shared: Jotunn's Revenge
- Community slot 6: Skeggox (unfinished) → Avatar's Parashu

| At 6 items | Ichor | Community | Ichor ÷ community |
|---|---:|---:|---:|
| Burst vs squishy | 829 | 2,818 | 0.294 |
| Burst vs tank | 547 | 2,023 | 0.271 |
| 10s sustained vs squishy | 3,316 | 8,972 | 0.370 |
| 10s sustained vs tank | 1,994 | 6,211 | 0.321 |
| Effective health vs physical | 10,867 | 4,559 | 2.384 |
| Effective health vs magical | 10,420 | 3,986 | 2.614 |

| Power at | damage axis | survival axis | Ichor sustained vs squishy | community |
|---|---:|---:|---:|---:|
| 2 items | 0.823 | 1.163 | 1,676 | 2,103 |
| 4 items | 0.499 | 1.785 | 2,685 | 4,387 |
| 6 items | 0.312 | 2.496 | 3,316 | 8,972 |

| Differing item | Side | Pick | Est. matches | Item win vs god | Wilson LB | Ichor's reason (model) | Best swap |
|---|---|---:|---:|---|---:|---|---|
| Hydra's Lament | community | 24% | 327 | 55% vs 55% (-0.0 pt) | 0.496 | model rank #12, quality 0.506 (efficiency 0.55, fit 0.40); the weakest item Ichor kept scores 0.544, 0.038 short | for Amanita Charm: 1.184 / 0.757 |
| The Crusher | community | 11% | 150 | 55% vs 55% (-0.0 pt) | 0.467 | model rank #9, quality 0.520 (efficiency 0.51, fit 0.55); the weakest item Ichor kept scores 0.544, 0.025 short | for Amanita Charm: 1.327 / 0.757 |
| Heartseeker | community | 31% | 422 | 52% vs 55% (-3.0 pt) | 0.471 | model rank #10, quality 0.511 (efficiency 0.45, fit 0.65); the weakest item Ichor kept scores 0.544, 0.033 short | for Amanita Charm: 1.325 / 0.757 |
| Titan's Bane | community | 11% | 150 | 57% vs 55% (+2.0 pt) | 0.487 | model rank #13, quality 0.498 (efficiency 0.48, fit 0.55); the weakest item Ichor kept scores 0.544, 0.046 short | for Amanita Charm: 1.254 / 0.757 |
| Avatar's Parashu | community | 6% | 82 | 64% vs 55% (+9.0 pt) | 0.526 | model rank #30, quality 0.455 (efficiency 0.46, fit 0.45); the weakest item Ichor kept scores 0.544, 0.089 short | for Amanita Charm: 1.436 / 0.757 |
| Genji's Guard | ichor | — | — | not in community record | — | model rank #6, quality 0.546 (efficiency 0.71, fit 0.16); the weakest item Ichor kept scores 0.544 | — |
| Berserker's Shield | ichor | — | — | not in community record | — | model rank #7, quality 0.544 (efficiency 0.66, fit 0.28); the weakest item Ichor kept scores 0.544 | — |
| Kinetic Cuirass | ichor | — | — | not in community record | — | model rank #3, quality 0.574 (efficiency 0.61, fit 0.49); the weakest item Ichor kept scores 0.544 | — |
| Shield Splitter | ichor | — | — | not in community record | — | model rank #5, quality 0.553 (efficiency 0.58, fit 0.49); the weakest item Ichor kept scores 0.544 | — |
| Amanita Charm | ichor | — | — | not in community record | — | model rank #2, quality 0.595 (efficiency 0.68, fit 0.39); the weakest item Ichor kept scores 0.544 | — |

**What would make this indefensible:** Ichor builds a full tank six on a Jungle assassin: 27–37% of the community's damage for 2.4–2.6× its EHP, and none of Ichor's five own items is in Thor's 1,361-match record. If a jungler is judged on damage at all, "trade-off" is the rule having no exchange rate between axes, not a defence of the build.

## Vulcan — Mid

Picked by: most-played 'Ichor better'. God record: 409/794 won (51.5%). Kit: base.

**Verdict: Ichor better.** Damage axis 1.092, survival axis 1.132 (Ichor ÷ community, 6 items; weighted over 2/4/6: 1.051 / 1.042). Without the coverage rule: Ichor better; six items only: Ichor better. Simulated share Ichor 100%, community 100% (gap 0.0%).

- Ichor: Spear of Desolation, Doom Orb, Spear of the Magus, Rod of Tahuti, Obsidian Shard, Soul Gem (16,450 g)
- Community: Book of Thoth, Spear of Desolation, Rod of Tahuti, Obsidian Shard, The World Stone, Chronos' Pendant (16,050 g)
- Shared: Spear of Desolation, Rod of Tahuti, Obsidian Shard
- Community slot 5: Evil Eye (unfinished) → The World Stone
- Community slot 6: Shrapnel Mod (unscoreable) → Chronos' Pendant
- Community slot 7: Surplus Mod (unscoreable) → None
- Community slot 8: Thermal Mod (unscoreable) → None
- Community slot 9: Seismic Mod (unscoreable) → None

| At 6 items | Ichor | Community | Ichor ÷ community |
|---|---:|---:|---:|
| Burst vs squishy | 3,401 | 3,064 | 1.110 |
| Burst vs tank | 2,095 | 1,810 | 1.158 |
| 10s sustained vs squishy | 8,323 | 8,050 | 1.034 |
| 10s sustained vs tank | 5,082 | 4,750 | 1.070 |
| Effective health vs physical | 4,558 | 4,015 | 1.135 |
| Effective health vs magical | 4,095 | 3,630 | 1.128 |

| Power at | damage axis | survival axis | Ichor sustained vs squishy | community |
|---|---:|---:|---:|---:|
| 2 items | 1.097 | 1.000 | 3,387 | 2,970 |
| 4 items | 0.969 | 1.000 | 5,650 | 5,497 |
| 6 items | 1.092 | 1.132 | 8,323 | 8,050 |

| Differing item | Side | Pick | Est. matches | Item win vs god | Wilson LB | Ichor's reason (model) | Best swap |
|---|---|---:|---:|---|---:|---|---|
| Book of Thoth | community | 45% | 357 | 50% vs 52% (-1.5 pt) | 0.447 | model rank #21, quality 0.439 (efficiency 0.48, fit 0.35); the weakest item Ichor kept scores 0.556, 0.116 short | for Doom Orb: 1.010 / 1.000 |
| The World Stone | community | 13% | 103 | 51% vs 52% (-0.5 pt) | 0.419 | model rank #10, quality 0.544 (efficiency 0.49, fit 0.66); the weakest item Ichor kept scores 0.556, 0.011 short | for Doom Orb: 0.988 / 1.000 |
| Chronos' Pendant | community | 13% | 103 | 45% vs 52% (-6.5 pt) | 0.354 | model rank #9, quality 0.552 (efficiency 0.56, fit 0.52); the weakest item Ichor kept scores 0.556, 0.004 short | for Doom Orb: 0.958 / 1.000 |
| Doom Orb | ichor | — | — | not in community record | — | model rank #8, quality 0.556 (efficiency 0.51, fit 0.66); the weakest item Ichor kept scores 0.556 | — |
| Spear of the Magus | ichor | — | — | not in community record | — | model rank #5, quality 0.589 (efficiency 0.56, fit 0.66); the weakest item Ichor kept scores 0.556 | — |
| Soul Gem | ichor | 7% | 56 | 51% vs 52% (-0.5 pt) | 0.390 | model rank #3, quality 0.652 (efficiency 0.53, fit 0.93); the weakest item Ichor kept scores 0.556 | — |

**What would make this indefensible:** Weighted damage is 1.051 against a 1.05 threshold and survival 1.042 is inside the band; anything that moves Ichor's weighted damage by 0.1% turns this into "level", and Ichor is behind at 4 items (0.969).

## Nox — Mid

Picked by: most-played 'community better' or 'trade-off'. God record: 599/1348 won (44.4%). Kit: base.

**Verdict: trade-off.** Damage axis 0.819, survival axis 1.748 (Ichor ÷ community, 6 items; weighted over 2/4/6: 0.824 / 1.548). Without the coverage rule: trade-off; six items only: trade-off. Simulated share Ichor 100%, community 100% (gap 0.0%).

- Ichor: Genji's Guard, Kinetic Cuirass, Spear of Desolation, Freya's Tears, Rod of Tahuti, Amanita Charm (15,350 g)
- Community: Spear of Desolation, Chronos' Pendant, Rod of Tahuti, Freya's Tears, Obsidian Shard, Gauntlet of Thebes (15,750 g)
- Shared: Spear of Desolation, Freya's Tears, Rod of Tahuti
- Community slot 6: Evil Eye (unfinished) → Gauntlet of Thebes

| At 6 items | Ichor | Community | Ichor ÷ community |
|---|---:|---:|---:|
| Burst vs squishy | 1,146 | 1,514 | 0.757 |
| Burst vs tank | 653 | 926 | 0.705 |
| 10s sustained vs squishy | 3,546 | 3,743 | 0.947 |
| 10s sustained vs tank | 2,067 | 2,328 | 0.888 |
| Effective health vs physical | 8,239 | 5,308 | 1.552 |
| Effective health vs magical | 9,611 | 4,882 | 1.969 |

| Power at | damage axis | survival axis | Ichor sustained vs squishy | community |
|---|---:|---:|---:|---:|
| 2 items | 0.829 | 1.499 | 2,143 | 2,458 |
| 4 items | 0.825 | 1.416 | 2,869 | 3,148 |
| 6 items | 0.819 | 1.748 | 3,546 | 3,743 |

| Differing item | Side | Pick | Est. matches | Item win vs god | Wilson LB | Ichor's reason (model) | Best swap |
|---|---|---:|---:|---|---:|---|---|
| Chronos' Pendant | community | 11% | 148 | 53% vs 44% (+8.6 pt) | 0.447 | model rank #23, quality 0.482 (efficiency 0.56, fit 0.29); the weakest item Ichor kept scores 0.553, 0.071 short | for Amanita Charm: 1.145 / 0.743 |
| Obsidian Shard | community | 10% | 135 | 44% vs 44% (-0.4 pt) | 0.356 | model rank #16, quality 0.506 (efficiency 0.53, fit 0.44); the weakest item Ichor kept scores 0.553, 0.047 short | for Amanita Charm: 1.246 / 0.743 |
| Gauntlet of Thebes | community | 19% | 256 | 42% vs 44% (-2.4 pt) | 0.363 | model rank #86, quality 0.254 (efficiency 0.30, fit 0.15); the weakest item Ichor kept scores 0.553, 0.298 short | for Amanita Charm: 0.997 / 0.802 |
| Genji's Guard | ichor | 10% | 135 | 47% vs 44% (+2.6 pt) | 0.385 | model rank #6, quality 0.577 (efficiency 0.71, fit 0.26); the weakest item Ichor kept scores 0.553 | — |
| Kinetic Cuirass | ichor | — | — | not in community record | — | model rank #4, quality 0.599 (efficiency 0.61, fit 0.58); the weakest item Ichor kept scores 0.553 | — |
| Amanita Charm | ichor | — | — | not in community record | — | model rank #2, quality 0.620 (efficiency 0.68, fit 0.48); the weakest item Ichor kept scores 0.553 | — |

**What would make this indefensible:** Two tank items and Amanita Charm on a Mid cost 18% of the damage for 55–97% more EHP; if a Mid's survival does not trade one-for-one with damage, this is "community better". The community's Gauntlet of Thebes (19%, est. 256) Ichor ranks #86 — the one place Ichor's dismissal is backed by the record (42% vs the god's 44%).

## Odin — Solo

Picked by: most-played 'Ichor better'. God record: 172/286 won (60.1%). Kit: base.

**Verdict: Ichor better.** Damage axis 1.180, survival axis 1.181 (Ichor ÷ community, 6 items; weighted over 2/4/6: 1.184 / 1.067). Without the coverage rule: Ichor better; six items only: Ichor better. Simulated share Ichor 100%, community 100% (gap 0.0%).

- Ichor: Jotunn's Revenge, Genji's Guard, Kinetic Cuirass, Shield Splitter, Freya's Tears, Amanita Charm (14,500 g)
- Community: Jotunn's Revenge, Breastplate of Valor, Genji's Guard, Freya's Tears, Hide of the Nemean Lion, Brawler’s Beat Stick (14,800 g)
- Shared: Jotunn's Revenge, Genji's Guard, Freya's Tears
- Community slot 5: Sundering Echo (unscoreable) → Brawler’s Beat Stick

| At 6 items | Ichor | Community | Ichor ÷ community |
|---|---:|---:|---:|
| Burst vs squishy | 883 | 727 | 1.215 |
| Burst vs tank | 579 | 430 | 1.348 |
| 10s sustained vs squishy | 3,172 | 2,968 | 1.069 |
| 10s sustained vs tank | 1,963 | 1,772 | 1.108 |
| Effective health vs physical | 9,775 | 9,577 | 1.021 |
| Effective health vs magical | 11,092 | 8,117 | 1.366 |

| Power at | damage axis | survival axis | Ichor sustained vs squishy | community |
|---|---:|---:|---:|---:|
| 2 items | 1.001 | 1.038 | 1,848 | 1,844 |
| 4 items | 1.406 | 0.990 | 3,104 | 2,207 |
| 6 items | 1.180 | 1.181 | 3,172 | 2,968 |

| Differing item | Side | Pick | Est. matches | Item win vs god | Wilson LB | Ichor's reason (model) | Best swap |
|---|---|---:|---:|---|---:|---|---|
| Breastplate of Valor | community | 30% | 86 | 61% vs 60% (+0.9 pt) | 0.499 | model rank #8, quality 0.524 (efficiency 0.63, fit 0.27); the weakest item Ichor kept scores 0.557, 0.034 short | for Amanita Charm: 1.046 / 0.817 |
| Hide of the Nemean Lion | community | 7% | 20 | 83% vs 60% (+22.9 pt) | — (n<30) | model rank #26, quality 0.470 (efficiency 0.54, fit 0.31); the weakest item Ichor kept scores 0.557, 0.087 short | for Amanita Charm: 1.048 / 0.906 |
| Brawler’s Beat Stick | community | 5% | 14 | 38% vs 60% (-22.1 pt) | — (n<30) | model rank #45, quality 0.422 (efficiency 0.45, fit 0.35); the weakest item Ichor kept scores 0.557, 0.136 short | for Amanita Charm: 1.089 / 0.833 |
| Kinetic Cuirass | ichor | 6% | 17 | 75% vs 60% (+14.9 pt) | — (n<30) | model rank #2, quality 0.603 (efficiency 0.61, fit 0.59); the weakest item Ichor kept scores 0.557 | — |
| Shield Splitter | ichor | — | — | not in community record | — | model rank #5, quality 0.566 (efficiency 0.58, fit 0.54); the weakest item Ichor kept scores 0.557 | — |
| Amanita Charm | ichor | — | — | not in community record | — | model rank #1, quality 0.623 (efficiency 0.68, fit 0.49); the weakest item Ichor kept scores 0.557 | — |

**What would make this indefensible:** The community record is the thinnest in the packet: 286 matches, and three of the six differing items have under 30 estimated matches (no bound). "Ichor better" here is the simulator's word with almost nothing on the community side to check it against.

## Cu Chulainn — Solo

Picked by: most-played 'community better' or 'trade-off'. God record: 336/643 won (52.3%). Kit: base.

**Verdict: trade-off.** Damage axis 1.202, survival axis 0.786 (Ichor ÷ community, 6 items; weighted over 2/4/6: 1.120 / 0.811). Without the coverage rule: trade-off; six items only: trade-off. Simulated share Ichor 100%, community 100% (gap 0.0%).

- Ichor: Genji's Guard, Berserker's Shield, Jotunn's Revenge, Kinetic Cuirass, Tyrfing, Amanita Charm (14,300 g)
- Community: Shifter's Shield, Mystical Mail, Freya's Tears, Kinetic Cuirass, Hide of the Nemean Lion, Devourer's Gauntlet (15,350 g)
- Shared: Kinetic Cuirass
- Community slot 6: Medal of Defense (unfinished) → Devourer's Gauntlet

| At 6 items | Ichor | Community | Ichor ÷ community |
|---|---:|---:|---:|
| Burst vs squishy | 1,591 | 1,538 | 1.035 |
| Burst vs tank | 940 | 920 | 1.022 |
| 10s sustained vs squishy | 4,814 | 3,406 | 1.414 |
| 10s sustained vs tank | 2,879 | 2,065 | 1.394 |
| Effective health vs physical | 10,084 | 14,805 | 0.681 |
| Effective health vs magical | 9,645 | 10,642 | 0.906 |

| Power at | damage axis | survival axis | Ichor sustained vs squishy | community |
|---|---:|---:|---:|---:|
| 2 items | 1.003 | 0.899 | 2,219 | 2,079 |
| 4 items | 1.166 | 0.757 | 3,703 | 2,797 |
| 6 items | 1.202 | 0.786 | 4,814 | 3,406 |

| Differing item | Side | Pick | Est. matches | Item win vs god | Wilson LB | Ichor's reason (model) | Best swap |
|---|---|---:|---:|---|---:|---|---|
| Shifter's Shield | community | 52% | 334 | 53% vs 52% (+0.7 pt) | 0.476 | model rank #29, quality 0.441 (efficiency 0.50, fit 0.31); the weakest item Ichor kept scores 0.530, 0.088 short | for Amanita Charm: 1.073 / 0.927 |
| Mystical Mail | community | 14% | 90 | 53% vs 52% (+0.7 pt) | 0.431 | model rank #67, quality 0.371 (efficiency 0.44, fit 0.22); the weakest item Ichor kept scores 0.530, 0.158 short | for Amanita Charm: 1.038 / 0.886 |
| Freya's Tears | community | 23% | 148 | 54% vs 52% (+1.7 pt) | 0.460 | model rank #11, quality 0.488 (efficiency 0.61, fit 0.21); the weakest item Ichor kept scores 0.530, 0.041 short | for Amanita Charm: 1.025 / 0.894 |
| Hide of the Nemean Lion | community | 10% | 64 | 54% vs 52% (+1.7 pt) | 0.426 | model rank #30, quality 0.440 (efficiency 0.54, fit 0.22); the weakest item Ichor kept scores 0.530, 0.089 short | for Amanita Charm: 1.046 / 0.892 |
| Devourer's Gauntlet | community | 17% | 109 | 53% vs 52% (+0.7 pt) | 0.439 | model rank #69, quality 0.367 (efficiency 0.40, fit 0.30); the weakest item Ichor kept scores 0.530, 0.163 short | for Berserker's Shield: 1.163 / 1.006 |
| Genji's Guard | ichor | — | — | not in community record | — | model rank #5, quality 0.535 (efficiency 0.71, fit 0.12); the weakest item Ichor kept scores 0.530 | — |
| Berserker's Shield | ichor | — | — | not in community record | — | model rank #1, quality 0.623 (efficiency 0.72, fit 0.39); the weakest item Ichor kept scores 0.530 | — |
| Jotunn's Revenge | ichor | — | — | not in community record | — | model rank #4, quality 0.541 (efficiency 0.65, fit 0.28); the weakest item Ichor kept scores 0.530 | — |
| Tyrfing | ichor | — | — | not in community record | — | model rank #6, quality 0.530 (efficiency 0.53, fit 0.52); the weakest item Ichor kept scores 0.530 | — |
| Amanita Charm | ichor | — | — | not in community record | — | model rank #2, quality 0.568 (efficiency 0.68, fit 0.31); the weakest item Ichor kept scores 0.530 | — |

**What would make this indefensible:** The community stacks protection (Shifter's Shield at 52%, est. 334, plus Mystical Mail and Hide of the Nemean Lion) and Ichor ranks its top pick #29; if a Solo is judged on survival first, two-thirds of the community's physical EHP (0.681) for +41% sustained damage is a loss, not a trade-off.

## Sobek — Support

Picked by: no 'Ichor better' god; highest damage x survival axis product. God record: 351/659 won (53.3%). Kit: base.

**Verdict: trade-off.** Damage axis 1.171, survival axis 0.888 (Ichor ÷ community, 6 items; weighted over 2/4/6: 1.245 / 0.880). Without the coverage rule: trade-off; six items only: trade-off. Simulated share Ichor 84%, community 83% (gap 0.4%).

- Ichor: Kinetic Cuirass, Genji's Guard, Freya's Tears, Draconic Scale, Amanita Charm, Erosion (14,800 g)
- Community: Gauntlet of Thebes, Stampede, Freya's Tears, Shell of Rebuke, Genji's Guard, Prophetic Cloak (14,450 g)
- Shared: Genji's Guard, Freya's Tears
- Community slot 6: Medal of Defense (unfinished) → Prophetic Cloak

| At 6 items | Ichor | Community | Ichor ÷ community |
|---|---:|---:|---:|
| Burst vs squishy | 1,022 | 1,022 | 1.000 |
| Burst vs tank | 591 | 591 | 1.000 |
| 10s sustained vs squishy | 2,857 | 2,090 | 1.367 |
| 10s sustained vs tank | 1,694 | 1,231 | 1.376 |
| Effective health vs physical | 15,282 | 17,124 | 0.892 |
| Effective health vs magical | 15,511 | 17,565 | 0.883 |

| Power at | damage axis | survival axis | Ichor sustained vs squishy | community |
|---|---:|---:|---:|---:|
| 2 items | 1.265 | 1.047 | 2,535 | 1,572 |
| 4 items | 1.304 | 0.733 | 2,758 | 1,620 |
| 6 items | 1.171 | 0.888 | 2,857 | 2,090 |

| Differing item | Side | Pick | Est. matches | Item win vs god | Wilson LB | Ichor's reason (model) | Best swap |
|---|---|---:|---:|---|---:|---|---|
| Gauntlet of Thebes | community | 51% | 336 | 51% vs 53% (-2.3 pt) | 0.456 | model rank #87, quality 0.265 (efficiency 0.30, fit 0.18); the weakest item Ichor kept scores 0.550, 0.285 short | for Draconic Scale: 1.017 / 1.052 |
| Stampede | community | 25% | 165 | 51% vs 53% (-2.3 pt) | 0.433 | model rank #31, quality 0.479 (efficiency 0.51, fit 0.41); the weakest item Ichor kept scores 0.550, 0.071 short | for Erosion: 1.000 / 0.968 |
| Shell of Rebuke | community | 17% | 112 | 56% vs 53% (+2.7 pt) | 0.470 | model rank #52, quality 0.420 (efficiency 0.41, fit 0.45); the weakest item Ichor kept scores 0.550, 0.130 short | for Erosion: 0.996 / 1.401 |
| Prophetic Cloak | community | 10% | 66 | 59% vs 53% (+5.7 pt) | 0.470 | model rank #27, quality 0.486 (efficiency 0.45, fit 0.57); the weakest item Ichor kept scores 0.550, 0.064 short | for Erosion: 0.993 / 0.938 |
| Kinetic Cuirass | ichor | — | — | not in community record | — | model rank #2, quality 0.647 (efficiency 0.61, fit 0.74); the weakest item Ichor kept scores 0.550 | — |
| Draconic Scale | ichor | — | — | not in community record | — | model rank #6, quality 0.563 (efficiency 0.53, fit 0.64); the weakest item Ichor kept scores 0.550 | — |
| Amanita Charm | ichor | — | — | not in community record | — | model rank #1, quality 0.668 (efficiency 0.68, fit 0.64); the weakest item Ichor kept scores 0.550 | — |
| Erosion | ichor | — | — | not in community record | — | model rank #9, quality 0.550 (efficiency 0.51, fit 0.64); the weakest item Ichor kept scores 0.550 | — |

**What would make this indefensible:** All of Ichor's damage lead is sustained (+37%; burst is identical at 1,022 — neither six adds burst) and all of its deficit is survival (0.880); if a Support is judged on survival, this is "community better". 16–17% of each build's gold is not fully simulated (gap 0.4%, so it passes).

## Ymir — Support

Picked by: most-played 'community better' or 'trade-off'. God record: 656/1166 won (56.3%). Kit: base.

**Verdict: community better.** Damage axis 0.799, survival axis 1.031 (Ichor ÷ community, 6 items; weighted over 2/4/6: 0.860 / 1.032). Without the coverage rule: community better; six items only: community better. Simulated share Ichor 84%, community 78% (gap 6.2%).

- Ichor: Genji's Guard, Kinetic Cuirass, Freya's Tears, Draconic Scale, Amanita Charm, Erosion (14,800 g)
- Community: Devourer's Gauntlet, Berserker's Shield, Kinetic Cuirass, Freya's Tears, Hussar's Wings, Gauntlet of Thebes (15,600 g)
- Shared: Kinetic Cuirass, Freya's Tears
- Community slot 6: Medal of Defense (unfinished) → Gauntlet of Thebes

| At 6 items | Ichor | Community | Ichor ÷ community |
|---|---:|---:|---:|
| Burst vs squishy | 404 | 491 | 0.823 |
| Burst vs tank | 234 | 280 | 0.835 |
| 10s sustained vs squishy | 2,380 | 3,121 | 0.763 |
| 10s sustained vs tank | 1,419 | 1,828 | 0.776 |
| Effective health vs physical | 15,447 | 17,324 | 0.892 |
| Effective health vs magical | 15,541 | 13,033 | 1.192 |

| Power at | damage axis | survival axis | Ichor sustained vs squishy | community |
|---|---:|---:|---:|---:|
| 2 items | 0.998 | 1.080 | 2,208 | 1,986 |
| 4 items | 0.798 | 0.987 | 2,281 | 2,993 |
| 6 items | 0.799 | 1.031 | 2,380 | 3,121 |

| Differing item | Side | Pick | Est. matches | Item win vs god | Wilson LB | Ichor's reason (model) | Best swap |
|---|---|---:|---:|---|---:|---|---|
| Devourer's Gauntlet | community | 26% | 303 | 54% vs 56% (-2.3 pt) | 0.485 | not in the model's pool for this god (fails the damage-type filter or cannot take a core slot) | for Draconic Scale: 1.252 / 1.040 |
| Berserker's Shield | community | 31% | 361 | 56% vs 56% (-0.3 pt) | 0.508 | not in the model's pool for this god (fails the damage-type filter or cannot take a core slot) | for Erosion: 1.032 / 0.992 |
| Hussar's Wings | community | 7% | 82 | 64% vs 56% (+7.7 pt) | 0.526 | model rank #34, quality 0.467 (efficiency 0.39, fit 0.64); the weakest item Ichor kept scores 0.552, 0.085 short | for Erosion: 1.009 / 1.093 |
| Gauntlet of Thebes | community | 17% | 198 | 61% vs 56% (+4.7 pt) | 0.542 | model rank #87, quality 0.266 (efficiency 0.30, fit 0.18); the weakest item Ichor kept scores 0.552, 0.286 short | for Draconic Scale: 1.020 / 1.048 |
| Genji's Guard | ichor | — | — | not in community record | — | model rank #3, quality 0.602 (efficiency 0.71, fit 0.34); the weakest item Ichor kept scores 0.552 | — |
| Draconic Scale | ichor | — | — | not in community record | — | model rank #5, quality 0.565 (efficiency 0.53, fit 0.64); the weakest item Ichor kept scores 0.552 | — |
| Amanita Charm | ichor | — | — | not in community record | — | model rank #1, quality 0.669 (efficiency 0.68, fit 0.64); the weakest item Ichor kept scores 0.552 | — |
| Erosion | ichor | — | — | not in community record | — | model rank #8, quality 0.552 (efficiency 0.51, fit 0.64); the weakest item Ichor kept scores 0.552 | — |

**What would make this indefensible:** The loss is all damage (0.860) with survival level (1.032), so if a Support is not judged on damage this is "level". And two of the community's four differing items — Devourer's Gauntlet (26%) and Berserker's Shield (31%), ~664 estimated matches between them — are not in the model's pool for Ymir at all; Ichor's "reason" for them is a filter, not a score.
