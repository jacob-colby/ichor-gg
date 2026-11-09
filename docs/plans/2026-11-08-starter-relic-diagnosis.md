# Starter and relic diagnosis — rule vs community, per god (2026-11-08)

Point-in-time, like everything in `docs/plans/`. Measured at main `eef19739` on
SmiteBrain's ob47 window (Obsidian+ ranked Conquest, 3–8 Nov), every god page
fetched ~12:00 on 2026-11-08 and parsed with the decimal-correct rate pattern.

**Decision: most-picked, for both (Jacob, 2026-11-08).** Implemented in
`scoring.pick_starter` / `scoring.pick_relic`; the role table is the fallback
when a god has no community record, and a relic has none.

**Method.** Every tile in each section, not the stored top 3 (truncating to 3
changes the most-picked starter path on Cupid, Discordia and Nemesis).
`n` is `pick_rate × god_matches_played` from the god index, the estimate
`hybrid.community_records` already uses; the page's own count runs ~1% higher
(Ra 417 vs 413) because it was fetched a few hours later. Wins are
`round(win_rate × n)`. **LB** is `tierlist.wilson_lower_bound` (z = 1.96), `—`
under its 30-match floor.

**Starter paths, not items.** Starter sightings sum to 98–103% of each god's
matches (relics 98–101%): each player is counted once, holding EITHER the base
or its upgrade. So a path's share is base + upgrade, and its win rate is the
match-weighted mean of the two. Item-level win rates are survivorship — Nox's
Sands of Time 18% vs Pendulum of the Ages 57%, Artemis's Gilded Arrow 38% vs
Sharpshooter's Arrow 61% — because only a game that went long or well reaches
the upgrade.

**Rules compared.** *Most-picked*: the path (relic) with the largest share.
*Best-evidence*: the largest Wilson LB. *Challenger*: most-picked unless another
candidate's LB exceeds the most-picked's own point win rate.

| | Starters (paths) | Relics |
|---|---|---|
| Gods with a community record | 95 / 95 | 95 / 95 |
| Rule path = most-picked path | 23 / 95 (6 gods: rule path absent from the record) | — no rule |
| Best-evidence ≠ most-picked | 23 | 32 |
| Challenger fires | 6 | 12 |
| Strict challenger (LB > most-picked's UPPER bound) fires | 2 (Kuzenbo, Nox) | 1 (Da Ji) |
| Top-two margin under 5pp | 11 | 24 |

## Starters (paths; base and upgrade sightings summed — they are exclusive)

| God | Role | n | god win | Rule path (its record) | Most-picked path | Best-evidence path (max Wilson LB) | Challenger rule |
|---|---|---|---|---|---|---|---|
| Achilles | Solo Jungle | 131 | 51% | Bumba's Golden Dagger → Bumba's Spear (0.8% pick · 100% win · n=1 · LB —) | **Bumba's Cudgel → Bumba's Hammer** (32% pick · 57% win · n=42 · LB 0.422) | same | most-picked |
| Agni | Mid | 295 | 51% | Conduit Gem → Archmage's Gem (41% pick · 52% win · n=121 · LB 0.432) | **Conduit Gem → Archmage's Gem** (41% pick · 52% win · n=121 · LB 0.432) | same | most-picked |
| Ah Puch | Mid | 108 | 55% | Conduit Gem → Archmage's Gem (5% pick · 40% win · n=5 · LB —) | **Bluestone Pendant → Bluestone Brooch** (70% pick · 54% win · n=76 · LB 0.428) | same | most-picked |
| Aladdin | Jungle | 236 | 62% | Conduit Gem → Archmage's Gem (72% pick · 62% win · n=170 · LB 0.549) | **Conduit Gem → Archmage's Gem** (72% pick · 62% win · n=170 · LB 0.549) | same | most-picked |
| Amaterasu | Solo | 194 | 63% | Warrior's Axe → Sundering Axe (2% pick · 50% win · n=4 · LB —) | **Leather Cowl → Hunter's Cowl** (57% pick · 64% win · n=111 · LB 0.547) | same | most-picked |
| Anhur | Carry | 391 | 51% | Gilded Arrow → Sharpshooter's Arrow (53% pick · 52% win · n=207 · LB 0.454) | **Gilded Arrow → Sharpshooter's Arrow** (53% pick · 52% win · n=207 · LB 0.454) | same | most-picked |
| Anubis | Mid | 104 | 50% | Conduit Gem → Archmage's Gem (74% pick · 52% win · n=77 · LB 0.410) | **Conduit Gem → Archmage's Gem** (74% pick · 52% win · n=77 · LB 0.410) | same | most-picked |
| Aphrodite | Mid Support | 257 | 57% | Conduit Gem → Archmage's Gem (31% pick · 55% win · n=80 · LB 0.441) | **Sands Of Time → Pendulum of the Ages** (53% pick · 59% win · n=136 · LB 0.504) | same | most-picked |
| Apollo | Carry | 336 | 53% | Gilded Arrow → Sharpshooter's Arrow (54% pick · 55% win · n=181 · LB 0.480) | **Gilded Arrow → Sharpshooter's Arrow** (54% pick · 55% win · n=181 · LB 0.480) | same | most-picked |
| Ares | Support | 233 | 54% | Warrior's Axe → Sundering Axe (8% pick · 63% win · n=19 · LB —) | **Selflessness → Heroism** (48% pick · 57% win · n=112 · LB 0.479) | same | most-picked |
| Artemis | Carry | 259 | 56% | Gilded Arrow → Sharpshooter's Arrow (54% pick · 53% win · n=139 · LB 0.443) | **Gilded Arrow → Sharpshooter's Arrow** (54% pick · 53% win · n=139 · LB 0.443) | Leather Cowl → Hunter's Cowl (29% pick · 67% win · n=75 · LB 0.554) | **Leather Cowl → Hunter's Cowl** |
| Artio | Solo Support | 212 | 56% | Warrior's Axe → Sundering Axe (1% pick · 50% win · n=2 · LB —) | **Bumba's Cudgel → Bumba's Hammer** (44% pick · 56% win · n=94 · LB 0.463) | Selflessness → Heroism (15% pick · 66% win · n=32 · LB 0.483) | most-picked |
| Athena | Support | 379 | 57% | Warrior's Axe → Sundering Axe (6% pick · 50% win · n=22 · LB —) | **Bumba's Cudgel → Bumba's Hammer** (46% pick · 58% win · n=175 · LB 0.509) | same | most-picked |
| Atlas | Support | 136 | 46% | Warrior's Axe → Sundering Axe (4% pick · 0% win · n=5 · LB —) | **Bluestone Pendant → Bluestone Brooch** (37% pick · 34% win · n=50 · LB 0.224) | Bumba's Cudgel → Bumba's Hammer (29% pick · 57% win · n=40 · LB 0.422) | **Bumba's Cudgel → Bumba's Hammer** |
| Awilix | Jungle | 166 | 50% | Bumba's Golden Dagger → Bumba's Spear (4% pick · 43% win · n=7 · LB —) | **Leather Cowl → Hunter's Cowl** (63% pick · 50% win · n=105 · LB 0.411) | same | most-picked |
| Bacchus | Support | 529 | 59% | Warrior's Axe → Sundering Axe (3% pick · 56% win · n=16 · LB —) | **Leather Cowl → Hunter's Cowl** (67% pick · 63% win · n=355 · LB 0.577) | same | most-picked |
| Baron Samedi | Mid Support | 187 | 54% | Conduit Gem → Archmage's Gem (28% pick · 62% win · n=52 · LB 0.480) | **Bluestone Pendant → Bluestone Brooch** (32% pick · 55% win · n=60 · LB 0.425) | Conduit Gem → Archmage's Gem (28% pick · 62% win · n=52 · LB 0.480) | most-picked |
| Bastet | Jungle | 318 | 54% | Bumba's Golden Dagger → Bumba's Spear (not in record) | **Bluestone Pendant → Bluestone Brooch** (68% pick · 56% win · n=216 · LB 0.498) | same | most-picked |
| Bellona | Solo | 173 | 55% | Warrior's Axe → Sundering Axe (1% pick · 50% win · n=2 · LB —) | **Death's Toll → Death's Embrace** (52% pick · 57% win · n=90 · LB 0.464) | same | most-picked |
| Cabrakan | Solo Support | 101 | 46% | Warrior's Axe → Sundering Axe (7% pick · 57% win · n=7 · LB —) | **Bumba's Cudgel → Bumba's Hammer** (54% pick · 46% win · n=54 · LB 0.337) | same | most-picked |
| Cerberus | Solo Support | 170 | 55% | Warrior's Axe → Sundering Axe (4% pick · 50% win · n=6 · LB —) | **Conduit Gem → Archmage's Gem** (46% pick · 57% win · n=79 · LB 0.460) | same | most-picked |
| Cernunnos | Carry Jungle | 222 | 55% | Gilded Arrow → Sharpshooter's Arrow (32% pick · 48% win · n=71 · LB 0.367) | **Leather Cowl → Hunter's Cowl** (56% pick · 58% win · n=124 · LB 0.493) | same | most-picked |
| Chaac | Solo | 68 | 50% | Warrior's Axe → Sundering Axe (3% pick · 100% win · n=2 · LB —) | **Bluestone Pendant → Bluestone Brooch** (79% pick · 44% win · n=54 · LB 0.320) | same | most-picked |
| Charon | Support | 99 | 57% | Warrior's Axe → Sundering Axe (2% pick · 100% win · n=2 · LB —) | **Bluestone Pendant → Bluestone Brooch** (71% pick · 58% win · n=71 · LB 0.462) | same | most-picked |
| Chiron | Carry | 284 | 55% | Gilded Arrow → Sharpshooter's Arrow (2% pick · 40% win · n=5 · LB —) | **Bluestone Pendant → Bluestone Brooch** (51% pick · 62% win · n=145 · LB 0.540) | same | most-picked |
| Chronos | Mid Carry | 192 | 52% | Conduit Gem → Archmage's Gem (12% pick · 38% win · n=24 · LB —) | **Sands Of Time → Pendulum of the Ages** (70% pick · 54% win · n=134 · LB 0.453) | same | most-picked |
| Cu Chulainn | Solo | 291 | 51% | Warrior's Axe → Sundering Axe (2% pick · 20% win · n=5 · LB —) | **Bluestone Pendant → Bluestone Brooch** (88% pick · 52% win · n=256 · LB 0.458) | same | most-picked |
| Cupid | Carry | 234 | 56% | Gilded Arrow → Sharpshooter's Arrow (42% pick · 60% win · n=98 · LB 0.503) | **Gilded Arrow → Sharpshooter's Arrow** (42% pick · 60% win · n=98 · LB 0.503) | Leather Cowl → Hunter's Cowl (41% pick · 64% win · n=96 · LB 0.536) | most-picked |
| Da Ji | Jungle | 249 | 55% | Bumba's Golden Dagger → Bumba's Spear (0.4% pick · 100% win · n=1 · LB —) | **Bumba's Cudgel → Bumba's Hammer** (83% pick · 53% win · n=206 · LB 0.466) | same | most-picked |
| Danzaburou | Carry | 153 | 50% | Gilded Arrow → Sharpshooter's Arrow (13% pick · 35% win · n=20 · LB —) | **Conduit Gem → Archmage's Gem** (38% pick · 59% win · n=58 · LB 0.458) | same | most-picked |
| Discordia | Mid | 202 | 55% | Conduit Gem → Archmage's Gem (39% pick · 53% win · n=78 · LB 0.416) | **Sands Of Time → Pendulum of the Ages** (43% pick · 63% win · n=87 · LB 0.527) | same | most-picked |
| Eset | Mid | 134 | 51% | Conduit Gem → Archmage's Gem (53% pick · 49% win · n=71 · LB 0.380) | **Conduit Gem → Archmage's Gem** (53% pick · 49% win · n=71 · LB 0.380) | same | most-picked |
| Fenrir | Jungle | 144 | 51% | Bumba's Golden Dagger → Bumba's Spear (4% pick · 67% win · n=6 · LB —) | **Leather Cowl → Hunter's Cowl** (31% pick · 55% win · n=44 · LB 0.401) | same | most-picked |
| Ganesha | Support | 130 | 50% | Warrior's Axe → Sundering Axe (4% pick · 17% win · n=6 · LB —) | **Selflessness → Heroism** (56% pick · 47% win · n=73 · LB 0.356) | same | most-picked |
| Geb | Support Carry | 270 | 60% | Conduit Gem → Archmage's Gem (3% pick · 43% win · n=7 · LB —) | **Selflessness → Heroism** (75% pick · 62% win · n=202 · LB 0.555) | same | most-picked |
| Gilgamesh | Solo Jungle | 140 | 59% | Bumba's Golden Dagger → Bumba's Spear (0.7% pick · 0% win · n=1 · LB —) | **Leather Cowl → Hunter's Cowl** (45% pick · 59% win · n=63 · LB 0.464) | Bluestone Pendant → Bluestone Brooch (31% pick · 64% win · n=44 · LB 0.489) | most-picked |
| Guan Yu | Solo Support | 96 | 60% | Warrior's Axe → Sundering Axe (9% pick · 67% win · n=9 · LB —) | **Sands Of Time → Pendulum of the Ages** (37% pick · 63% win · n=35 · LB 0.463) | same | most-picked |
| Hachiman | Carry | 484 | 46% | Gilded Arrow → Sharpshooter's Arrow (64% pick · 46% win · n=309 · LB 0.408) | **Gilded Arrow → Sharpshooter's Arrow** (64% pick · 46% win · n=309 · LB 0.408) | same | most-picked |
| Hades | Solo | 102 | 55% | Conduit Gem → Archmage's Gem (82% pick · 55% win · n=84 · LB 0.441) | **Conduit Gem → Archmage's Gem** (82% pick · 55% win · n=84 · LB 0.441) | same | most-picked |
| Hecate | Mid | 119 | 48% | Conduit Gem → Archmage's Gem (71% pick · 44% win · n=85 · LB 0.335) | **Conduit Gem → Archmage's Gem** (71% pick · 44% win · n=85 · LB 0.335) | same | most-picked |
| Hel | Mid Support | 345 | 51% | Conduit Gem → Archmage's Gem (27% pick · 58% win · n=93 · LB 0.479) | **Sands Of Time → Pendulum of the Ages** (63% pick · 51% win · n=218 · LB 0.448) | Conduit Gem → Archmage's Gem (27% pick · 58% win · n=93 · LB 0.479) | most-picked |
| Hercules | Solo | 88 | 45% | Warrior's Axe → Sundering Axe (4% pick · 25% win · n=4 · LB —) | **Bumba's Cudgel → Bumba's Hammer** (80% pick · 46% win · n=70 · LB 0.346) | same | most-picked |
| Horus | Support Solo | 263 | 52% | Warrior's Axe → Sundering Axe (15% pick · 51% win · n=39 · LB 0.362) | **Selflessness → Heroism** (50% pick · 56% win · n=131 · LB 0.472) | same | most-picked |
| Hou Yi | Carry | 457 | 53% | Gilded Arrow → Sharpshooter's Arrow (79% pick · 53% win · n=361 · LB 0.483) | **Gilded Arrow → Sharpshooter's Arrow** (79% pick · 53% win · n=361 · LB 0.483) | same | most-picked |
| Hua Mulan | Solo | 97 | 47% | Warrior's Axe → Sundering Axe (22% pick · 41% win · n=22 · LB —) | **Bluestone Pendant → Bluestone Brooch** (67% pick · 49% win · n=65 · LB 0.375) | same | most-picked |
| Hun Batz | Jungle | 148 | 51% | Bumba's Golden Dagger → Bumba's Spear (5% pick · 57% win · n=7 · LB —) | **Bumba's Cudgel → Bumba's Hammer** (87% pick · 50% win · n=129 · LB 0.411) | same | most-picked |
| Ishtar | Carry | 248 | 59% | Gilded Arrow → Sharpshooter's Arrow (58% pick · 57% win · n=144 · LB 0.488) | **Gilded Arrow → Sharpshooter's Arrow** (58% pick · 57% win · n=144 · LB 0.488) | Leather Cowl → Hunter's Cowl (25% pick · 63% win · n=62 · LB 0.505) | most-picked |
| Ix Chel | Mid Support | 112 | 56% | Conduit Gem → Archmage's Gem (20% pick · 61% win · n=23 · LB —) | **Sands Of Time → Pendulum of the Ages** (60% pick · 60% win · n=67 · LB 0.477) | same | most-picked |
| Izanami | Carry | 743 | 64% | Gilded Arrow → Sharpshooter's Arrow (13% pick · 63% win · n=97 · LB 0.530) | **Conduit Gem → Archmage's Gem** (39% pick · 66% win · n=290 · LB 0.602) | same | most-picked |
| Janus | Mid | 489 | 54% | Conduit Gem → Archmage's Gem (84% pick · 55% win · n=411 · LB 0.497) | **Conduit Gem → Archmage's Gem** (84% pick · 55% win · n=411 · LB 0.497) | same | most-picked |
| Jing Wei | Carry | 126 | 45% | Gilded Arrow → Sharpshooter's Arrow (94% pick · 44% win · n=118 · LB 0.354) | **Gilded Arrow → Sharpshooter's Arrow** (94% pick · 44% win · n=118 · LB 0.354) | same | most-picked |
| Jormungandr | Solo Support | 86 | 51% | Warrior's Axe → Sundering Axe (12% pick · 27% win · n=11 · LB —) | **Bluestone Pendant → Bluestone Brooch** (72% pick · 52% win · n=62 · LB 0.394) | same | most-picked |
| Kali | Jungle | 119 | 50% | Bumba's Golden Dagger → Bumba's Spear (3% pick · 33% win · n=3 · LB —) | **Leather Cowl → Hunter's Cowl** (40% pick · 55% win · n=47 · LB 0.412) | same | most-picked |
| Khepri | Support | 109 | 65% | Warrior's Axe → Sundering Axe (not in record) | **Selflessness → Heroism** (53% pick · 61% win · n=57 · LB 0.484) | same | most-picked |
| Kukulkan | Mid | 312 | 54% | Conduit Gem → Archmage's Gem (78% pick · 54% win · n=243 · LB 0.476) | **Conduit Gem → Archmage's Gem** (78% pick · 54% win · n=243 · LB 0.476) | same | most-picked |
| Kuzenbo | Support | 335 | 50% | Warrior's Axe → Sundering Axe (18% pick · 68% win · n=60 · LB 0.558) | **Bluestone Pendant → Bluestone Brooch** (39% pick · 40% win · n=131 · LB 0.324) | Warrior's Axe → Sundering Axe (18% pick · 68% win · n=60 · LB 0.558) | **Warrior's Axe → Sundering Axe** |
| Loki | Jungle | 481 | 54% | Bumba's Golden Dagger → Bumba's Spear (0.8% pick · 75% win · n=4 · LB —) | **Bumba's Cudgel → Bumba's Hammer** (72% pick · 52% win · n=346 · LB 0.471) | same | most-picked |
| Medusa | Carry | 199 | 54% | Gilded Arrow → Sharpshooter's Arrow (37% pick · 55% win · n=74 · LB 0.441) | **Leather Cowl → Hunter's Cowl** (44% pick · 51% win · n=88 · LB 0.409) | Gilded Arrow → Sharpshooter's Arrow (37% pick · 55% win · n=74 · LB 0.441) | most-picked |
| Mercury | Jungle | 170 | 48% | Bumba's Golden Dagger → Bumba's Spear (11% pick · 63% win · n=19 · LB —) | **Leather Cowl → Hunter's Cowl** (52% pick · 48% win · n=88 · LB 0.376) | same | most-picked |
| Merlin | Mid | 331 | 55% | Conduit Gem → Archmage's Gem (15% pick · 53% win · n=49 · LB 0.394) | **Sands Of Time → Pendulum of the Ages** (58% pick · 56% win · n=192 · LB 0.492) | same | most-picked |
| Mordred | Solo Jungle | 199 | 62% | Bumba's Golden Dagger → Bumba's Spear (0.5% pick · 100% win · n=1 · LB —) | **Bluestone Pendant → Bluestone Brooch** (51% pick · 65% win · n=102 · LB 0.551) | same | most-picked |
| Morgan Le Fay | Mid | 176 | 51% | Conduit Gem → Archmage's Gem (25% pick · 52% win · n=44 · LB 0.379) | **Bluestone Pendant → Bluestone Brooch** (56% pick · 47% win · n=99 · LB 0.379) | Conduit Gem → Archmage's Gem (25% pick · 52% win · n=44 · LB 0.379) | most-picked |
| Ne Zha | Jungle | 336 | 51% | Bumba's Golden Dagger → Bumba's Spear (1% pick · 50% win · n=4 · LB —) | **Leather Cowl → Hunter's Cowl** (40% pick · 49% win · n=134 · LB 0.409) | Bumba's Cudgel → Bumba's Hammer (21% pick · 59% win · n=71 · LB 0.475) | most-picked |
| Neith | Carry Mid | 172 | 53% | Gilded Arrow → Sharpshooter's Arrow (11% pick · 42% win · n=19 · LB —) | **Conduit Gem → Archmage's Gem** (45% pick · 53% win · n=78 · LB 0.416) | same | most-picked |
| Nemesis | Jungle | 136 | 48% | Bumba's Golden Dagger → Bumba's Spear (4% pick · 40% win · n=5 · LB —) | **Bumba's Cudgel → Bumba's Hammer** (36% pick · 45% win · n=49 · LB 0.319) | Leather Cowl → Hunter's Cowl (36% pick · 53% win · n=49 · LB 0.394) | most-picked |
| Nike | Solo | 351 | 52% | Warrior's Axe → Sundering Axe (4% pick · 40% win · n=15 · LB —) | **Bluestone Pendant → Bluestone Brooch** (46% pick · 51% win · n=162 · LB 0.436) | Conduit Gem → Archmage's Gem (41% pick · 56% win · n=144 · LB 0.481) | most-picked |
| Nox | Mid Support | 723 | 43% | Conduit Gem → Archmage's Gem (30% pick · 41% win · n=217 · LB 0.347) | **Sands Of Time → Pendulum of the Ages** (34% pick · 39% win · n=246 · LB 0.328) | Selflessness → Heroism (16% pick · 54% win · n=116 · LB 0.453) | **Selflessness → Heroism** |
| Nu Wa | Mid | 128 | 52% | Conduit Gem → Archmage's Gem (64% pick · 51% win · n=82 · LB 0.406) | **Conduit Gem → Archmage's Gem** (64% pick · 51% win · n=82 · LB 0.406) | same | most-picked |
| Nut | Carry Mid | 334 | 52% | Conduit Gem → Archmage's Gem (18% pick · 48% win · n=60 · LB 0.362) | **Death's Toll → Death's Embrace** (72% pick · 53% win · n=241 · LB 0.468) | same | most-picked |
| Odin | Solo Jungle | 115 | 55% | Bumba's Golden Dagger → Bumba's Spear (not in record) | **Bumba's Cudgel → Bumba's Hammer** (56% pick · 60% win · n=65 · LB 0.479) | same | most-picked |
| Osiris | Solo | 82 | 44% | Warrior's Axe → Sundering Axe (25% pick · 25% win · n=20 · LB —) | **Death's Toll → Death's Embrace** (53% pick · 49% win · n=43 · LB 0.346) | same | most-picked |
| Pele | Jungle | 185 | 53% | Bumba's Golden Dagger → Bumba's Spear (3% pick · 43% win · n=7 · LB —) | **Leather Cowl → Hunter's Cowl** (65% pick · 54% win · n=120 · LB 0.453) | same | most-picked |
| Poseidon | Mid | 276 | 53% | Conduit Gem → Archmage's Gem (30% pick · 55% win · n=83 · LB 0.447) | **Sands Of Time → Pendulum of the Ages** (43% pick · 53% win · n=119 · LB 0.440) | Conduit Gem → Archmage's Gem (30% pick · 55% win · n=83 · LB 0.447) | most-picked |
| Princess Bari | Carry Mid | 83 | 40% | Conduit Gem → Archmage's Gem (67% pick · 40% win · n=55 · LB 0.281) | **Conduit Gem → Archmage's Gem** (67% pick · 40% win · n=55 · LB 0.281) | same | most-picked |
| Ra | Mid | 413 | 50% | Conduit Gem → Archmage's Gem (39% pick · 48% win · n=161 · LB 0.403) | **Sands Of Time → Pendulum of the Ages** (58% pick · 51% win · n=239 · LB 0.447) | same | most-picked |
| Rama | Carry | 233 | 54% | Gilded Arrow → Sharpshooter's Arrow (70% pick · 58% win · n=163 · LB 0.506) | **Gilded Arrow → Sharpshooter's Arrow** (70% pick · 58% win · n=163 · LB 0.506) | same | most-picked |
| Ratatoskr | Jungle | 491 | 60% | Bumba's Golden Dagger → Bumba's Spear (0.4% pick · 50% win · n=2 · LB —) | **Bluestone Pendant → Bluestone Brooch** (44% pick · 62% win · n=216 · LB 0.559) | same | most-picked |
| Ravana | Jungle | 268 | 51% | Bumba's Golden Dagger → Bumba's Spear (3% pick · 71% win · n=7 · LB —) | **Leather Cowl → Hunter's Cowl** (39% pick · 51% win · n=104 · LB 0.415) | Bumba's Cudgel → Bumba's Hammer (37% pick · 56% win · n=99 · LB 0.457) | most-picked |
| Scylla | Mid | 344 | 53% | Conduit Gem → Archmage's Gem (91% pick · 53% win · n=313 · LB 0.472) | **Conduit Gem → Archmage's Gem** (91% pick · 53% win · n=313 · LB 0.472) | same | most-picked |
| Sobek | Support | 266 | 54% | Warrior's Axe → Sundering Axe (6% pick · 62% win · n=16 · LB —) | **Bluestone Pendant → Bluestone Brooch** (61% pick · 53% win · n=162 · LB 0.454) | same | most-picked |
| Sol | Mid Carry | 204 | 59% | Conduit Gem → Archmage's Gem (38% pick · 56% win · n=78 · LB 0.454) | **Conduit Gem → Archmage's Gem** (38% pick · 56% win · n=78 · LB 0.454) | Leather Cowl → Hunter's Cowl (18% pick · 67% win · n=36 · LB 0.503) | most-picked |
| Sun Wukong | Solo | 231 | 55% | Warrior's Axe → Sundering Axe (4% pick · 40% win · n=10 · LB —) | **Bluestone Pendant → Bluestone Brooch** (74% pick · 57% win · n=171 · LB 0.492) | same | most-picked |
| Susano | Jungle | 311 | 56% | Bumba's Golden Dagger → Bumba's Spear (not in record) | **Bumba's Cudgel → Bumba's Hammer** (77% pick · 57% win · n=240 · LB 0.503) | same | most-picked |
| Sylvanus | Support | 246 | 57% | Warrior's Axe → Sundering Axe (0.8% pick · 100% win · n=2 · LB —) | **Selflessness → Heroism** (37% pick · 57% win · n=91 · LB 0.469) | War Flag → War Banner (26% pick · 59% win · n=64 · LB 0.471) | most-picked |
| Thanatos | Jungle | 327 | 57% | Bumba's Golden Dagger → Bumba's Spear (3% pick · 91% win · n=11 · LB —) | **Bumba's Cudgel → Bumba's Hammer** (61% pick · 58% win · n=199 · LB 0.508) | same | most-picked |
| The Morrigan | Mid | 181 | 55% | Conduit Gem → Archmage's Gem (63% pick · 53% win · n=114 · LB 0.435) | **Conduit Gem → Archmage's Gem** (63% pick · 53% win · n=114 · LB 0.435) | Sands Of Time → Pendulum of the Ages (21% pick · 76% win · n=38 · LB 0.608) | **Sands Of Time → Pendulum of the Ages** |
| Thor | Jungle Solo | 549 | 55% | Bumba's Golden Dagger → Bumba's Spear (0.4% pick · 50% win · n=2 · LB —) | **Bumba's Cudgel → Bumba's Hammer** (52% pick · 56% win · n=285 · LB 0.503) | same | most-picked |
| Tsukuyomi | Jungle | 371 | 53% | Bumba's Golden Dagger → Bumba's Spear (not in record) | **Bumba's Cudgel → Bumba's Hammer** (78% pick · 54% win · n=289 · LB 0.482) | same | most-picked |
| Ullr | Carry | 349 | 58% | Gilded Arrow → Sharpshooter's Arrow (0.8% pick · 33% win · n=3 · LB —) | **Bumba's Cudgel → Bumba's Hammer** (86% pick · 59% win · n=300 · LB 0.537) | same | most-picked |
| Vulcan | Mid | 359 | 53% | Conduit Gem → Archmage's Gem (44% pick · 57% win · n=158 · LB 0.492) | **Sands Of Time → Pendulum of the Ages** (52% pick · 50% win · n=186 · LB 0.429) | Conduit Gem → Archmage's Gem (44% pick · 57% win · n=158 · LB 0.492) | most-picked |
| Xbalanque | Carry | 250 | 58% | Gilded Arrow → Sharpshooter's Arrow (8% pick · 35% win · n=20 · LB —) | **Death's Toll → Death's Embrace** (78% pick · 60% win · n=195 · LB 0.530) | same | most-picked |
| Xing Tian | Support Solo | 300 | 54% | Warrior's Axe → Sundering Axe (3% pick · 44% win · n=9 · LB —) | **Bluestone Pendant → Bluestone Brooch** (70% pick · 56% win · n=210 · LB 0.494) | same | most-picked |
| Yemoja | Support | 88 | 52% | Warrior's Axe → Sundering Axe (not in record) | **Bluestone Pendant → Bluestone Brooch** (63% pick · 54% win · n=56 · LB 0.407) | same | most-picked |
| Ymir | Support | 467 | 56% | Warrior's Axe → Sundering Axe (4% pick · 56% win · n=18 · LB —) | **Leather Cowl → Hunter's Cowl** (57% pick · 56% win · n=266 · LB 0.504) | War Flag → War Banner (20% pick · 62% win · n=94 · LB 0.516) | most-picked |
| Zeus | Mid | 210 | 58% | Conduit Gem → Archmage's Gem (26% pick · 45% win · n=55 · LB 0.330) | **Conduit Gem → Archmage's Gem** (26% pick · 45% win · n=55 · LB 0.330) | Sands Of Time → Pendulum of the Ages (20% pick · 69% win · n=42 · LB 0.540) | **Sands Of Time → Pendulum of the Ages** |

## Relics (base relics only — upgrades are bought into the six)

| God | n | Most-picked | #2 | #3 | Best-evidence | Challenger rule |
|---|---|---|---|---|---|---|
| Achilles | 131 | **Phantom Shell (27%/33%, n=35, LB 0.208)** | Purification Beads (20%/67%, n=26, LB —) | Sundering Arc (18%/46%, n=24, LB —) | same | most-picked |
| Agni | 295 | **Purification Beads (65%/46%, n=192, LB 0.389)** | Aegis of Acceleration (35%/60%, n=103, LB 0.505) |  | Aegis of Acceleration | **Aegis of Acceleration** |
| Ah Puch | 108 | **Aegis of Acceleration (46%/37%, n=50, LB 0.241)** | Purification Beads (42%/62%, n=45, LB 0.476) | Phantom Shell (11%/92%, n=12, LB —) | Purification Beads | **Purification Beads** |
| Aladdin | 236 | **Purification Beads (69%/65%, n=163, LB 0.574)** | Aegis of Acceleration (27%/55%, n=64, LB 0.426) | Blink Rune (3%/57%, n=7, LB —) | same | most-picked |
| Amaterasu | 194 | **Agility Relic (53%/60%, n=103, LB 0.505)** | Phantom Shell (15%/63%, n=29, LB —) | Purification Beads (15%/63%, n=29, LB —) | same | most-picked |
| Anhur | 391 | **Purification Beads (63%/50%, n=246, LB 0.438)** | Aegis of Acceleration (35%/50%, n=137, LB 0.414) | Agility Relic (2%/83%, n=8, LB —) | same | most-picked |
| Anubis | 104 | **Aegis of Acceleration (47%/38%, n=49, LB 0.264)** | Purification Beads (27%/66%, n=28, LB —) | Blink Rune (24%/54%, n=25, LB —) | same | most-picked |
| Aphrodite | 257 | **Aegis of Acceleration (44%/61%, n=113, LB 0.518)** | Purification Beads (39%/49%, n=100, LB 0.394) | Phantom Shell (12%/63%, n=31, LB 0.469) | same | most-picked |
| Apollo | 336 | **Purification Beads (57%/52%, n=192, LB 0.450)** | Aegis of Acceleration (35%/56%, n=118, LB 0.469) | Agility Relic (3%/50%, n=10, LB —) | Aegis of Acceleration | most-picked |
| Ares | 233 | **Blink Rune (53%/59%, n=123, LB 0.505)** | Phantom Shell (31%/53%, n=72, LB 0.414) | Sundering Arc (11%/44%, n=26, LB —) | same | most-picked |
| Artemis | 259 | **Purification Beads (62%/55%, n=161, LB 0.476)** | Aegis of Acceleration (33%/57%, n=85, LB 0.459) | Agility Relic (3%/75%, n=8, LB —) | same | most-picked |
| Artio | 212 | **Phantom Shell (35%/53%, n=74, LB 0.415)** | Purification Beads (31%/64%, n=66, LB 0.516) | Aegis of Acceleration (14%/67%, n=30, LB 0.488) | Purification Beads | most-picked |
| Athena | 379 | **Phantom Shell (35%/55%, n=133, LB 0.464)** | Blink Rune (24%/58%, n=91, LB 0.480) | Purification Beads (21%/63%, n=80, LB 0.515) | Purification Beads | most-picked |
| Atlas | 136 | **Phantom Shell (41%/54%, n=56, LB 0.407)** | Purification Beads (20%/37%, n=27, LB —) | Sundering Arc (16%/32%, n=22, LB —) | same | most-picked |
| Awilix | 166 | **Purification Beads (46%/51%, n=76, LB 0.403)** | Blink Rune (33%/42%, n=55, LB 0.297) | Aegis of Acceleration (17%/59%, n=28, LB —) | same | most-picked |
| Bacchus | 529 | **Agility Relic (51%/64%, n=270, LB 0.582)** | Phantom Shell (14%/52%, n=74, LB 0.402) | Purification Beads (14%/53%, n=74, LB 0.415) | same | most-picked |
| Baron Samedi | 187 | **Purification Beads (35%/60%, n=65, LB 0.479)** | Aegis of Acceleration (31%/55%, n=58, LB 0.425) | Phantom Shell (27%/45%, n=50, LB 0.312) | same | most-picked |
| Bastet | 318 | **Purification Beads (63%/57%, n=200, LB 0.501)** | Aegis of Acceleration (23%/49%, n=73, LB 0.382) | Blink Rune (5%/50%, n=16, LB —) | same | most-picked |
| Bellona | 173 | **Agility Relic (51%/57%, n=88, LB 0.464)** | Phantom Shell (17%/55%, n=29, LB —) | Purification Beads (12%/43%, n=21, LB —) | same | most-picked |
| Cabrakan | 101 | **Sundering Arc (30%/57%, n=30, LB 0.392)** | Phantom Shell (28%/43%, n=28, LB —) | Purification Beads (21%/33%, n=21, LB —) | same | most-picked |
| Cerberus | 170 | **Blink Rune (47%/53%, n=80, LB 0.417)** | Phantom Shell (30%/54%, n=51, LB 0.414) | Sundering Arc (12%/52%, n=20, LB —) | same | most-picked |
| Cernunnos | 222 | **Purification Beads (66%/53%, n=147, LB 0.450)** | Aegis of Acceleration (19%/57%, n=42, LB 0.422) | Agility Relic (7%/69%, n=16, LB —) | same | most-picked |
| Chaac | 68 | **Blink Rune (25%/53%, n=17, LB —)** | Sundering Arc (23%/50%, n=16, LB —) | Purification Beads (22%/47%, n=15, LB —) | — | most-picked |
| Charon | 99 | **Phantom Shell (45%/64%, n=45, LB 0.498)** | Aegis of Acceleration (21%/48%, n=21, LB —) | Sundering Arc (16%/44%, n=16, LB —) | same | most-picked |
| Chiron | 284 | **Purification Beads (52%/52%, n=148, LB 0.440)** | Aegis of Acceleration (48%/58%, n=136, LB 0.497) | Phantom Shell (0.3%/100%, n=1, LB —) | Aegis of Acceleration | most-picked |
| Chronos | 192 | **Purification Beads (57%/52%, n=109, LB 0.430)** | Aegis of Acceleration (36%/47%, n=69, LB 0.351) | Phantom Shell (4%/71%, n=8, LB —) | same | most-picked |
| Cu Chulainn | 291 | **Phantom Shell (25%/53%, n=73, LB 0.421)** | Blink Rune (24%/49%, n=70, LB 0.372) | Sundering Arc (19%/53%, n=55, LB 0.398) | same | most-picked |
| Cupid | 234 | **Purification Beads (73%/57%, n=171, LB 0.492)** | Aegis of Acceleration (26%/54%, n=61, LB 0.417) | Phantom Shell (0.8%/50%, n=2, LB —) | same | most-picked |
| Da Ji | 249 | **Purification Beads (61%/47%, n=152, LB 0.390)** | Aegis of Acceleration (30%/68%, n=75, LB 0.568) | Blink Rune (7%/53%, n=17, LB —) | Aegis of Acceleration | **Aegis of Acceleration** |
| Danzaburou | 153 | **Purification Beads (50%/45%, n=76, LB 0.341)** | Aegis of Acceleration (45%/56%, n=69, LB 0.448) | Blink Rune (3%/50%, n=5, LB —) | Aegis of Acceleration | most-picked |
| Discordia | 202 | **Aegis of Acceleration (49%/48%, n=99, LB 0.389)** | Purification Beads (49%/62%, n=99, LB 0.518) | Agility Relic (0.5%/100%, n=1, LB —) | Purification Beads | **Purification Beads** |
| Eset | 134 | **Aegis of Acceleration (48%/55%, n=64, LB 0.426)** | Purification Beads (44%/47%, n=59, LB 0.353) | Phantom Shell (6%/63%, n=8, LB —) | same | most-picked |
| Fenrir | 144 | **Purification Beads (49%/52%, n=71, LB 0.407)** | Sundering Arc (26%/47%, n=37, LB 0.310) | Aegis of Acceleration (12%/61%, n=17, LB —) | same | most-picked |
| Ganesha | 130 | **Phantom Shell (58%/49%, n=75, LB 0.383)** | Blink Rune (12%/67%, n=16, LB —) | Purification Beads (12%/33%, n=16, LB —) | same | most-picked |
| Geb | 270 | **Phantom Shell (47%/57%, n=127, LB 0.480)** | Blink Rune (42%/67%, n=113, LB 0.582) | Purification Beads (6%/56%, n=16, LB —) | Blink Rune | **Blink Rune** |
| Gilgamesh | 140 | **Purification Beads (31%/56%, n=43, LB 0.411)** | Blink Rune (29%/56%, n=41, LB 0.410) | Aegis of Acceleration (15%/62%, n=21, LB —) | same | most-picked |
| Guan Yu | 96 | **Sundering Arc (38%/64%, n=36, LB 0.476)** | Phantom Shell (35%/56%, n=34, LB 0.395) | Aegis of Acceleration (13%/50%, n=12, LB —) | same | most-picked |
| Hachiman | 484 | **Purification Beads (55%/47%, n=266, LB 0.411)** | Aegis of Acceleration (43%/48%, n=208, LB 0.414) | Agility Relic (1%/20%, n=5, LB —) | Aegis of Acceleration | most-picked |
| Hades | 102 | **Purification Beads (33%/59%, n=34, LB 0.422)** | Aegis of Acceleration (25%/65%, n=26, LB —) | Phantom Shell (17%/33%, n=17, LB —) | same | most-picked |
| Hecate | 119 | **Purification Beads (52%/56%, n=62, LB 0.441)** | Aegis of Acceleration (48%/40%, n=57, LB 0.286) |  | same | most-picked |
| Hel | 345 | **Aegis of Acceleration (48%/56%, n=166, LB 0.484)** | Purification Beads (31%/44%, n=107, LB 0.349) | Phantom Shell (20%/49%, n=69, LB 0.378) | same | most-picked |
| Hercules | 88 | **Phantom Shell (24%/67%, n=21, LB —)** | Blink Rune (18%/38%, n=16, LB —) | Sundering Arc (18%/31%, n=16, LB —) | — | most-picked |
| Horus | 263 | **Phantom Shell (43%/49%, n=113, LB 0.397)** | Blink Rune (27%/63%, n=71, LB 0.518) | Purification Beads (12%/52%, n=32, LB 0.364) | Blink Rune | **Blink Rune** |
| Hou Yi | 457 | **Purification Beads (69%/54%, n=315, LB 0.484)** | Aegis of Acceleration (30%/49%, n=137, LB 0.407) | Agility Relic (0.9%/75%, n=4, LB —) | same | most-picked |
| Hua Mulan | 97 | **Sundering Arc (37%/50%, n=36, LB 0.345)** | Phantom Shell (33%/47%, n=32, LB 0.309) | Aegis of Acceleration (14%/29%, n=14, LB —) | same | most-picked |
| Hun Batz | 148 | **Purification Beads (46%/50%, n=68, LB 0.384)** | Blink Rune (40%/52%, n=59, LB 0.400) | Aegis of Acceleration (12%/50%, n=18, LB —) | Blink Rune | most-picked |
| Ishtar | 248 | **Purification Beads (50%/54%, n=124, LB 0.453)** | Aegis of Acceleration (41%/63%, n=102, LB 0.531) | Agility Relic (8%/63%, n=20, LB —) | Aegis of Acceleration | most-picked |
| Ix Chel | 112 | **Aegis of Acceleration (45%/57%, n=50, LB 0.423)** | Purification Beads (41%/61%, n=46, LB 0.465) | Phantom Shell (13%/40%, n=15, LB —) | Purification Beads | most-picked |
| Izanami | 743 | **Purification Beads (65%/64%, n=483, LB 0.596)** | Aegis of Acceleration (34%/61%, n=253, LB 0.547) | Agility Relic (0.3%/50%, n=2, LB —) | same | most-picked |
| Janus | 489 | **Purification Beads (57%/55%, n=279, LB 0.490)** | Aegis of Acceleration (41%/53%, n=200, LB 0.461) | Blink Rune (2%/27%, n=10, LB —) | same | most-picked |
| Jing Wei | 126 | **Purification Beads (50%/52%, n=63, LB 0.403)** | Aegis of Acceleration (48%/37%, n=60, LB 0.256) | Agility Relic (2%/33%, n=3, LB —) | same | most-picked |
| Jormungandr | 86 | **Aegis of Acceleration (36%/45%, n=31, LB 0.292)** | Phantom Shell (32%/64%, n=28, LB —) | Sundering Arc (23%/45%, n=20, LB —) | same | most-picked |
| Kali | 119 | **Blink Rune (40%/44%, n=48, LB 0.307)** | Purification Beads (36%/57%, n=43, LB 0.433) | Agility Relic (12%/53%, n=14, LB —) | Purification Beads | most-picked |
| Khepri | 109 | **Phantom Shell (56%/53%, n=61, LB 0.402)** | Purification Beads (20%/77%, n=22, LB —) | Aegis of Acceleration (13%/93%, n=14, LB —) | same | most-picked |
| Kukulkan | 312 | **Purification Beads (51%/54%, n=159, LB 0.463)** | Aegis of Acceleration (47%/54%, n=147, LB 0.457) | Blink Rune (0.9%/33%, n=3, LB —) | same | most-picked |
| Kuzenbo | 335 | **Phantom Shell (38%/43%, n=127, LB 0.350)** | Sundering Arc (29%/59%, n=97, LB 0.488) | Blink Rune (12%/50%, n=40, LB 0.352) | Sundering Arc | **Sundering Arc** |
| Loki | 481 | **Purification Beads (57%/53%, n=274, LB 0.470)** | Aegis of Acceleration (23%/58%, n=111, LB 0.484) | Sundering Arc (10%/58%, n=48, LB 0.443) | Aegis of Acceleration | most-picked |
| Medusa | 199 | **Aegis of Acceleration (53%/61%, n=105, LB 0.514)** | Purification Beads (45%/49%, n=90, LB 0.388) | Agility Relic (1%/0%, n=2, LB —) | same | most-picked |
| Mercury | 170 | **Purification Beads (62%/47%, n=105, LB 0.374)** | Aegis of Acceleration (30%/47%, n=51, LB 0.341) | Agility Relic (4%/71%, n=7, LB —) | same | most-picked |
| Merlin | 331 | **Purification Beads (60%/52%, n=199, LB 0.448)** | Aegis of Acceleration (40%/59%, n=132, LB 0.506) | Phantom Shell (0.3%/0%, n=1, LB —) | Aegis of Acceleration | most-picked |
| Mordred | 199 | **Purification Beads (38%/66%, n=76, LB 0.546)** | Phantom Shell (21%/57%, n=42, LB 0.422) | Sundering Arc (15%/74%, n=30, LB 0.556) | Sundering Arc | most-picked |
| Morgan Le Fay | 176 | **Aegis of Acceleration (32%/49%, n=56, LB 0.357)** | Purification Beads (32%/50%, n=56, LB 0.373) | Blink Rune (16%/61%, n=28, LB —) | Purification Beads | most-picked |
| Ne Zha | 336 | **Purification Beads (43%/48%, n=144, LB 0.399)** | Aegis of Acceleration (26%/58%, n=87, LB 0.470) | Blink Rune (12%/45%, n=40, LB 0.307) | Phantom Shell | **Phantom Shell** |
| Neith | 172 | **Purification Beads (57%/55%, n=98, LB 0.452)** | Aegis of Acceleration (42%/52%, n=72, LB 0.401) | Phantom Shell (0.6%/0%, n=1, LB —) | same | most-picked |
| Nemesis | 136 | **Purification Beads (47%/46%, n=64, LB 0.337)** | Blink Rune (17%/48%, n=23, LB —) | Sundering Arc (14%/47%, n=19, LB —) | same | most-picked |
| Nike | 351 | **Purification Beads (34%/50%, n=119, LB 0.416)** | Aegis of Acceleration (28%/57%, n=98, LB 0.473) | Blink Rune (14%/59%, n=49, LB 0.452) | Aegis of Acceleration | most-picked |
| Nox | 723 | **Aegis of Acceleration (33%/45%, n=239, LB 0.390)** | Purification Beads (33%/44%, n=239, LB 0.378) | Phantom Shell (26%/40%, n=188, LB 0.332) | same | most-picked |
| Nu Wa | 128 | **Aegis of Acceleration (59%/54%, n=76, LB 0.428)** | Purification Beads (38%/49%, n=49, LB 0.356) | Agility Relic (2%/50%, n=3, LB —) | same | most-picked |
| Nut | 334 | **Purification Beads (54%/45%, n=180, LB 0.379)** | Aegis of Acceleration (46%/60%, n=154, LB 0.518) | Phantom Shell (0.3%/0%, n=1, LB —) | Aegis of Acceleration | **Aegis of Acceleration** |
| Odin | 115 | **Blink Rune (36%/60%, n=41, LB 0.457)** | Purification Beads (28%/58%, n=32, LB 0.423) | Phantom Shell (17%/60%, n=20, LB —) | same | most-picked |
| Osiris | 82 | **Phantom Shell (31%/31%, n=25, LB —)** | Purification Beads (20%/35%, n=16, LB —) | Sundering Arc (20%/47%, n=16, LB —) | — | most-picked |
| Pele | 185 | **Purification Beads (42%/62%, n=78, LB 0.504)** | Blink Rune (22%/46%, n=41, LB 0.321) | Aegis of Acceleration (21%/44%, n=39, LB 0.293) | same | most-picked |
| Poseidon | 276 | **Purification Beads (58%/48%, n=160, LB 0.405)** | Aegis of Acceleration (42%/59%, n=116, LB 0.495) | Agility Relic (0.4%/0%, n=1, LB —) | Aegis of Acceleration | **Aegis of Acceleration** |
| Princess Bari | 83 | **Purification Beads (53%/40%, n=44, LB 0.277)** | Aegis of Acceleration (47%/40%, n=39, LB 0.271) |  | same | most-picked |
| Ra | 413 | **Purification Beads (52%/46%, n=215, LB 0.395)** | Aegis of Acceleration (46%/54%, n=190, LB 0.471) | Phantom Shell (2%/88%, n=8, LB —) | Aegis of Acceleration | **Aegis of Acceleration** |
| Rama | 233 | **Purification Beads (69%/57%, n=161, LB 0.494)** | Aegis of Acceleration (29%/45%, n=68, LB 0.343) | Agility Relic (1%/67%, n=2, LB —) | same | most-picked |
| Ratatoskr | 491 | **Purification Beads (51%/62%, n=250, LB 0.558)** | Aegis of Acceleration (19%/59%, n=93, LB 0.490) | Sundering Arc (16%/59%, n=79, LB 0.485) | same | most-picked |
| Ravana | 268 | **Blink Rune (31%/51%, n=83, LB 0.401)** | Purification Beads (19%/48%, n=51, LB 0.341) | Aegis of Acceleration (15%/67%, n=40, LB 0.520) | Aegis of Acceleration | **Aegis of Acceleration** |
| Scylla | 344 | **Purification Beads (46%/53%, n=158, LB 0.454)** | Aegis of Acceleration (41%/54%, n=141, LB 0.457) | Sundering Arc (8%/52%, n=28, LB —) | Aegis of Acceleration | most-picked |
| Sobek | 266 | **Phantom Shell (39%/58%, n=104, LB 0.481)** | Blink Rune (33%/55%, n=88, LB 0.442) | Sundering Arc (14%/54%, n=37, LB 0.384) | same | most-picked |
| Sol | 204 | **Aegis of Acceleration (62%/63%, n=126, LB 0.540)** | Purification Beads (34%/53%, n=69, LB 0.420) | Agility Relic (2%/50%, n=4, LB —) | same | most-picked |
| Sun Wukong | 231 | **Sundering Arc (31%/60%, n=72, LB 0.482)** | Aegis of Acceleration (19%/57%, n=44, LB 0.422) | Phantom Shell (19%/44%, n=44, LB 0.297) | same | most-picked |
| Susano | 311 | **Purification Beads (54%/58%, n=168, LB 0.502)** | Blink Rune (26%/55%, n=81, LB 0.447) | Aegis of Acceleration (10%/58%, n=31, LB 0.408) | same | most-picked |
| Sylvanus | 246 | **Phantom Shell (44%/52%, n=108, LB 0.425)** | Blink Rune (25%/53%, n=62, LB 0.410) | Aegis of Acceleration (16%/61%, n=39, LB 0.459) | Aegis of Acceleration | most-picked |
| Thanatos | 327 | **Purification Beads (45%/58%, n=147, LB 0.497)** | Blink Rune (34%/54%, n=111, LB 0.448) | Aegis of Acceleration (15%/59%, n=49, LB 0.452) | same | most-picked |
| The Morrigan | 181 | **Purification Beads (57%/58%, n=103, LB 0.486)** | Aegis of Acceleration (27%/54%, n=49, LB 0.394) | Blink Rune (12%/48%, n=22, LB —) | same | most-picked |
| Thor | 549 | **Purification Beads (54%/58%, n=296, LB 0.524)** | Aegis of Acceleration (27%/50%, n=148, LB 0.420) | Sundering Arc (10%/48%, n=55, LB 0.347) | same | most-picked |
| Tsukuyomi | 371 | **Purification Beads (66%/53%, n=245, LB 0.468)** | Aegis of Acceleration (31%/52%, n=115, LB 0.431) | Phantom Shell (2%/67%, n=7, LB —) | same | most-picked |
| Ullr | 349 | **Purification Beads (70%/55%, n=244, LB 0.486)** | Aegis of Acceleration (29%/63%, n=101, LB 0.536) | Blink Rune (0.6%/50%, n=2, LB —) | Aegis of Acceleration | most-picked |
| Vulcan | 359 | **Purification Beads (57%/53%, n=205, LB 0.463)** | Aegis of Acceleration (41%/53%, n=147, LB 0.450) | Phantom Shell (2%/57%, n=7, LB —) | same | most-picked |
| Xbalanque | 250 | **Purification Beads (61%/58%, n=152, LB 0.499)** | Aegis of Acceleration (30%/59%, n=75, LB 0.474) | Agility Relic (9%/45%, n=22, LB —) | same | most-picked |
| Xing Tian | 300 | **Phantom Shell (43%/52%, n=129, LB 0.434)** | Blink Rune (29%/60%, n=87, LB 0.493) | Sundering Arc (17%/54%, n=51, LB 0.414) | Blink Rune | most-picked |
| Yemoja | 88 | **Phantom Shell (40%/58%, n=35, LB 0.409)** | Aegis of Acceleration (27%/50%, n=24, LB —) | Purification Beads (22%/50%, n=19, LB —) | same | most-picked |
| Ymir | 467 | **Agility Relic (55%/56%, n=257, LB 0.499)** | Phantom Shell (18%/61%, n=84, LB 0.500) | Blink Rune (15%/61%, n=70, LB 0.497) | Phantom Shell | most-picked |
| Zeus | 210 | **Aegis of Acceleration (50%/63%, n=105, LB 0.533)** | Purification Beads (47%/52%, n=99, LB 0.418) | Agility Relic (2%/50%, n=4, LB —) | same | most-picked |
