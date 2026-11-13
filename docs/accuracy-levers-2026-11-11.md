# Accuracy levers for done criterion 2 (2026-11-11)

Read-only scoping. Nothing in the model, the scoring or the residual fit was
changed, and no data file was rewritten. This is a dated point-in-time file
(like `docs/plans/`): it will not be updated.

**Baseline.** `main` at `1a9ca2d5` (PR #150). Control re-measured before
anything else: input fingerprint `89eb181b72f1`, random-core baseline 5.7%,
leakage-free 41.5% (eff 0.70) and 38.1% (eff 0.45). All four match
`docs/CURRENT.md`. Community window `ob47`, 8,406 matches. Run on Windows; the
side-by-side verdicts it produced are identical to the 95 committed per-god
pages (0 differences), so the Windows tie caveat does not reach this report.

**Labels.** Every figure is tagged **[M]** measured in this session on that
baseline, **[M-prior]** measured earlier and quoted from `docs/STATE.md`
without re-running (the brief's "already measured" list and the register), or
**[R]** reasoned, not run.

## 1. Two corrections to the brief before anything else

1. **The readable count is 57 of 95, not 37 of 94. [M]** The 37 is §4.32's
   table, taken on PR #110's branch before it merged. On `main` the committed
   pages have read 54 or more since #110 merged on 11-05:

   | commit | date | gods | readable | Carry readable |
   |---|---|---|---|---|
   | #112 `6fc363b2` | 11-04 | 94 | 44 | 3 of 19 |
   | #110 `3c0c751f` | 11-05 | 94 | 54 | 9 of 19 |
   | #117 `d1c6f091` | 11-06 | 95 | 54 | 10 of 19 |
   | #124 `eef19739` | 11-08 | 95 | 55 | 10 of 19 |
   | #141 `eb76069a` | 11-09 | 95 | 55 | 10 of 19 |
   | #149 `5e6604d3` | 11-10 | 95 | 55 | 10 of 19 |
   | #150 `1a9ca2d5` | 11-11 | 95 | 57 | 10 of 19 |

   So there are **38 unreadable gods today, not 57**, and section 3 breaks down
   those 38. The number 57 is now the readable count.

2. **Carry reads 10 of 19, not 6 of 19. [M]** §4.30 set the Carry target at
   10. If the 10-god spot check (criterion 3) is blocked only on that number,
   it has been unblocked since 11-06. Whether 10 readable Carries is enough is
   your call; the count itself is no longer the obstacle.

One more fact that changes how to read every lever below: **the readable set
is not stable. [M]** Between consecutive page rewrites, 9, 6, 4 and 2 gods
crossed the readable line (11-06 to 11-08, to 11-09, to 11-10, to 11-11). The
last two steps are data refreshes only, with no model change. A god is
readable when both builds hold comparable refused gold, and the community six
moves daily.

## 2. "Readable verdict", exactly as the code defines it

`pipeline/smite/side_by_side.py`, `compare` then `judge`. For one god in
Conquest, Ichor's base-kit `model` core (efficiency and fit, no win or pick)
is run against the community's cleaned six (`community_target.comparison_six`).
The god gets a row unless one of two skip conditions holds, and the row's
verdict is decided in this order:

| step | condition | result |
|---|---|---|
| skip | the community record makes fewer than 6 finished items | no row |
| skip | Ichor has no full `model` six | no row |
| 1. kit | the community entry's `aspect_pick_rate` is above `ASPECT_MAJORITY` 0.5 and the aspect is not in `SIMULATED_ASPECTS` (which is empty) | `aspect not simulated` |
| 2. coverage | either build's `simulated_share` is under `COVERAGE_MIN` 0.50, or the two shares differ by more than `COVERAGE_GAP` 0.14 | `not enough simulated` |
| 3. phase | ahead at 2 and 4 items and behind at 6 (or the reverse), each outside `BAND` 0.05 | `early-game build` / `late-game build` |
| 4. verdict | weighted 2/4/6-item damage and survival axes against the 5% band | `Ichor better` / `community better` / `trade-off` / `level` |

`simulated_share` is the share of a build's gold in items whose passive is
fully simulated or that have no passive. PARTIAL and NOT SIMULATED items count
as missing at their whole cost.

**A readable verdict is a row that reaches step 3 or 4.** `level` is readable:
a tie is an answer, not a withheld one. Today [M]: 95 rows, 0 skipped, 7 stop
at step 1, 31 stop at step 2, 57 readable (trade-off 18, community better 17,
level 11, Ichor better 8, early-game 2, late-game 1).

| role | gods | readable | coverage-withheld | aspect |
|---|---|---|---|---|
| Solo | 19 | 8 | 9 | 2 |
| Support | 15 | 6 | 7 | 2 |
| Mid | 24 | 20 | 2 | 2 |
| Jungle | 18 | 13 | 5 | 0 |
| Carry | 19 | 10 | 8 | 1 |

## 3. Why each of the 38 unreadable gods is unreadable [M]

Against the brief's categories:

| category | gods | note |
|---|---|---|
| no data | 0 | every god has a full community six and a full `model` six; 0 skipped |
| too little data | 0 | the thinnest god has 110 matches in the window; no rule in `judge` reads sample size |
| ties | 0 | a tie is `level`, which is readable (11 gods) |
| missing role | 0 | no rule in `judge` reads role |
| aspect gap | 7 | the community mostly plays an aspect `combat.py` cannot play |
| other: coverage gap | 31 | one side holds a refused or partial passive the other side does not |

All 31 coverage cases fail the **gap**, none fails the floor (the lowest share
on any withheld build is 57%). All 31 are blocked by an explicit refusal or a
PARTIAL in `passive_sim`; none is an item with no decision. That matches
§4.30 and the 11-05 coverage pass, now with different names on it: Tekko-Kagi
blocks 10 (was 22 at the 11-05 count [M-prior]) and the community's Stampede
is now the second-largest blocker (9).

By what the blocking passive needs that the comparison lacks (a god can count
in two classes): movement 24, crowd control 6, health steal (PARTIAL) 2, ally
1, enemy crit 1, enemy shield 1, a kit-changing item 1. By side: the
community's build 19, Ichor's build 10, both 2.

"Coverage" is Ichor share / community share. "If judged" is
`verdict_unwithheld`: what the rule would say with the coverage test off. It
is shown so the cost of withholding is visible, not as a verdict.

| God | Role | Why unreadable | Blocking item (side) | Coverage | If judged |
|---|---|---|---|---|---|
| Anhur | Carry | coverage gap 17%, movement | Tekko-Kagi (Ichor) | 83% / 100% | Ichor better |
| Apollo | Carry | coverage gap 17%, movement | Tekko-Kagi (Ichor) | 83% / 100% | level |
| Artemis | Carry | coverage gap 17%, movement | Tekko-Kagi (Ichor) | 83% / 100% | level |
| Chiron | Carry | coverage gap 18%, movement | Tekko-Kagi (Ichor) | 82% / 100% | trade-off |
| Danzaburou | Carry | coverage gap 18%, movement | Tekko-Kagi (Ichor) | 82% / 100% | Ichor better |
| Hachiman | Carry | coverage gap 17%, movement | Tekko-Kagi (Ichor) | 83% / 100% | Ichor better |
| Rama | Carry | coverage gap 17%, movement | Tekko-Kagi (Ichor) | 83% / 100% | trade-off |
| Ullr | Carry | coverage gap 18%, movement | Tekko-Kagi (Ichor) | 82% / 100% | trade-off |
| Izanami | Carry | aspect gap: Aspect of the Sickle, 83% of games; would also fail the gap | Omen Drum (community) | 100% / 83% | n/a |
| Nemesis | Jungle | coverage gap 17%, movement | Tekko-Kagi (Ichor) | 83% / 100% | level |
| Tsukuyomi | Jungle | coverage gap 17%, movement | Tekko-Kagi (Ichor) | 83% / 100% | Ichor better |
| Ne Zha | Jungle | coverage gap 15%, crowd control | Magi's Cloak (community) | 100% / 85% | trade-off |
| Pele | Jungle | coverage gap just over 14%, crowd control | Magi's Cloak (community) | 100% / 86% | community better |
| Ratatoskr | Jungle | coverage gap 16%, kit-changing items on both sides | Ashwhorl, Briskberry, Thistlethorn Acorn (Ichor); Briskberry, Thistlethorn Acorn (community) | 57% / 73% | trade-off |
| Ah Puch | Mid | coverage gap 16%, movement | Gem of Isolation (community) | 100% / 84% | trade-off |
| Hel | Mid | coverage gap 15%, ally | Chandra's Grace (community) | 100% / 85% | trade-off |
| Aphrodite | Mid | aspect gap: Aspect of Heartbreak, 74%; would also fail the gap | Helm of Darkness (community) | 100% / 83% | n/a |
| Baron Samedi | Mid | aspect gap: Aspect of Hysteria, 71%; would also fail the gap | Alchemist Coat (community) | 100% / 85% | n/a |
| Amaterasu | Solo | coverage gap 22%, movement | Hussar's Wings (community) | 100% / 78% | community better |
| Bellona | Solo | coverage gap 22%, movement | Hussar's Wings (community) | 100% / 78% | community better |
| Hercules | Solo | coverage gap 22%, movement | Hussar's Wings (community) | 100% / 78% | trade-off |
| Osiris | Solo | coverage gap 22%, movement | Hussar's Wings (community) | 100% / 78% | level |
| Cerberus | Solo | coverage gap 17%, movement | Stampede (community) | 100% / 83% | trade-off |
| Chaac | Solo | coverage gap 17%, movement | Gem of Focus (community) | 100% / 83% | trade-off |
| Cabrakan | Solo | coverage gap 17%, crowd control | Runeforged Hammer (community) | 100% / 83% | Ichor better |
| Artio | Solo | coverage gap 16%, enemy crit | Spectral Armor (community) | 100% / 84% | late-game build |
| Jormungandr | Solo | coverage gap 16%, PARTIAL health steal | Ethereal Staff (community) | 100% / 84% | community better |
| Gilgamesh | Solo | aspect gap: Aspect of Shamash, 60%; coverage passes | none | 100% / 100% | n/a |
| Nike | Solo | aspect gap: Aspect of Victorious Conquest, 63%; coverage passes | none | 100% / 100% | n/a |
| Ares | Support | coverage gap 16%, movement | Stampede (community) | 100% / 84% | trade-off |
| Geb | Support | coverage gap 16%, movement | Stampede (community) | 100% / 84% | trade-off |
| Athena | Support | coverage gap 34%, movement and crowd control | Stampede, Spirit Robe (community) | 100% / 66% | trade-off |
| Ganesha | Support | coverage gap 34%, movement and crowd control | Stampede, Spirit Robe (community) | 100% / 66% | trade-off |
| Horus | Support | coverage gap 34%, movement and crowd control | Stampede, Stone of Binding (community) | 100% / 66% | trade-off |
| Sylvanus | Support | coverage gap 35%, movement | Stampede, Circe's Hexstone (community) | 100% / 65% | trade-off |
| Atlas | Support | coverage gap 18%, both sides | Erosion (Ichor); Stampede, Ethereal Staff (community) | 84% / 66% | Ichor better |
| Bacchus | Support | aspect gap: Aspect of Revelry, 80%; would also fail the gap | Hussar's Wings (community) | 100% / 78% | n/a |
| Khepri | Support | aspect gap: Aspect of Laceration, 67%; would also fail the gap | Stampede (community) | 100% / 84% | n/a |

Two notes on the table. Five of the seven aspect gods would stay unreadable
even with their aspect kit simulated, because they also fail the gap; only
Gilgamesh and Nike are one step from a verdict. And ten readable gods are
readable only because both sides hold one refusal each (Kali, Charon, Sobek,
Xing Tian, Ymir, Eset, Hecate, Janus, Nu Wa, Ra hold a refusal on one or both
sides inside the gap); 47 of the 57 are 100% simulated on both sides.

### The two gods at 0% coverage are a different problem [M]

Coverage (the `validate` figure in `docs/CURRENT.md`) and readability are
separate instruments. Neither 0% god is thin on data.

| | Jormungandr | Mercury |
|---|---|---|
| matches in window | 180 | 298 |
| community target | Eye of Erebus, Shifter's Shield, Ethereal Staff, Freya's Tears, Soul Reaver | Rage, Dagger of Frenzy, Deathbringer, Silverbranch Bow, Riptalon |
| shipped `core` | Shell of Rebuke, Berserker's Shield, Amanita Charm, Kinetic Cuirass, Genji's Guard, Shield Splitter | Jotunn's Revenge, Avatar's Parashu, Titan's Bane, Tyrfing, The Crusher, Heartseeker |
| rank of the target items in Ichor's pool | 9, 42, 58, 70, 120 of 136 | 16, 17, 21, 33, 36 of 97 |
| what the record shows | the community builds an Intelligence bruiser; Ichor builds a pure tank. Eye of Erebus has fit 0.058 | the community builds basic attacks (attack speed and crit); Ichor builds abilities |

Both are the model reading the god's kit differently from how the god is
played, not missing data. Jormungandr is one of the three gods §4.34 names
where the fit side and the simulator disagree most on Intelligence share
(0.630 against 0.471 [M-prior]). I am recording the mechanism, not diagnosing
it: that is a model question for its own session.

With `win` and `pick` zeroed the list of 0% gods is 10, not 2 [M]: Cernunnos,
Cupid, Danzaburou, Fenrir, Hachiman, Hou Yi, Medusa, Mercury, Ravana,
Tsukuyomi. All ten are physical; six are Carries and four are Junglers. The "2" in
the tracker is the shipped blend, which reads the community's own win and
pick.

## 4. What I measured that the levers rest on

**4a. Sample size is not what limits accuracy today. [M]** Per-god matches in
the `ob47` window: minimum 110, median 373, maximum 1,121; none under 100, 16
under 200. Rank correlation between a god's match count and its coverage is
0.10 (leakage-free) and 0.14 (shipped blend). By thirds of gods ordered by
match count, leakage-free coverage is 38.7% / 40.1% / 45.5% and the shipped
blend 45.8% / 51.6% / 55.6%. There is a slope, and it is small beside the
spread within each third.

**4b. The target is noisy even when no god is thin. [M]** A god's match count
is not the sample behind a slot. Slot matches are `pick_rate x
god_matches_played`: of 573 community slot picks, 135 (24%) rest on fewer than
30 matches, and the median slot rests on 62. Of the 1,718 win-rate readings in
the notes (slots and alternates), 578 (34%) rest on fewer than 30 matches and
49 on fewer than 10. Extreme readings (win rate at or above 0.70, or at or
below 0.30) number 124 among the thin third and 75 among the other two
thirds. Jormungandr's note carries a 1.00 win rate on an alternate with about
7 matches behind it.

**4c. The target moves under a fixed model. [M]** Same code, same weights,
today's items, scored against the community record as committed on earlier
days:

| target as of | window, matches | gods whose target set equals today's | mean Jaccard vs today | leakage-free | shipped blend |
|---|---|---|---|---|---|
| 11-11 | ob47, 8,406 | 95 of 95 | 1.000 | 41.5% | 51.1% |
| 11-10 | ob47, 7,420 | 62 of 95 | 0.894 | 41.3% | 50.0% |
| 11-09 | ob47, 6,470 | 53 of 95 | 0.862 | 42.2% | 50.2% |
| 11-06 | ob47, 2,859 | 25 of 95 | 0.708 | 39.2% | 47.6% |
| 11-05 | ob46 closed, 14,667 | 25 of 95 | 0.703 | 41.3% | 49.0% |

One day and about 1,000 more matches changes the target for 33 of 95 gods. The
leakage-free figure spans 39.2% to 42.2% with no model change at all, which
is wider than most deltas in the register. (The shipped-blend column reads win
and pick from each day's record, so it is that day's model on that day's
target.)

**4d. OB48 will make 4b and 4c worse within two days of landing. [M-prior,
R]** `refresh.choose_community_window` has no minimum depth. Its own docstring
(measured 11-09) shows that at four of the last seven patch boundaries it
moved to a window one day old, with 23 to 39 tracked gods under 30 matches of
their own and a per-god minimum of 2 to 5. Reasoned from that: about 11-18 the
target for most gods will rest on a few dozen matches, and coverage, the
readable set and the shipped `core` builds will all move for reasons that are
not the patch.

**4e. Outcome data exists that nothing reads, and it can already say
something. [M]** `data/Analysis/aspect_matches/` holds 40,616 matches (OB44 to
OB47) with the six items held and the team outcome. No instrument reads the
outcome against a build. A first probe, restricted to matches holding six
finished tier-3 items so game length is held roughly equal (9,486 matches, 66
gods with 30 or more), regressing win on the number of items shared with a
reference six, within god:

| reference six | win-rate change per shared item | 95% CI (bootstrap over gods) |
|---|---|---|
| Ichor `model` (never sees win or pick) | +1.38pp | +0.14 to +2.64 |
| Ichor shipped `core` | +1.50pp | +0.41 to +2.57 |
| the community's own six | +0.77pp | -0.18 to +1.64 |

Read this as "the instrument has power", not as a result. Four limits, all
measured: 94% of the store is aspect players (38,204 of 40,616), because the
no-aspect feed is stored only as a 10-newest sample per run (2,412 matches,
at most 30 per god); the builds compared are base-kit builds; survivors are
overrepresented (finished-six matches win 62%); and `core` reads aggregate
win rates, so only the `model` row is free of leakage. Restricting to the
god's primary role leaves 3,311 matches and every interval spans zero.

The store also deepens the win signal modestly: a median of 14 items per god
with 30 or more matches pooled over four windows, against the 11 per god the
note carries; within OB47 alone the median is 2.

**4f. Aspect builds have a target now, and the shipped builds miss it. [M]**
79 aspects carry a "what aspect players buy" record at the 30-match floor.
The shipped base `core` shares 18.6% of the aspect players' six most-held
items, against 47.9% of the same gods' pooled community target. For the 38
aspects played in a different role it is 10.5%; for the others 26.0%. 36 gods
share zero items. For the six gods with a shipped hand overlay and a record,
the overlay build shares 0 or 1 of 6 items with what aspect players hold
(Agni 0, Chiron 0, Morgan Le Fay 0, Ra 0, Cernunnos 1, Chronos 1); Agni's
Combustion players hold Devourer's Gauntlet, Dominance and Odysseus' Bow while
both Ichor builds are mage builds. Caveat: "six most held" is a share of
games, not a slot record, so it is not the same statistic as coverage.

## 5. The levers, ranked

Ranked by expected effect on what criterion 2 is about (whether the builds
are right), then on readable count, per unit of cost and risk. A lever that
only makes the number look better ranks low on purpose.

| # | Lever | Moves | Expected effect | Cost | Risk | OB48 |
|---|---|---|---|---|---|---|
| 1 | **Store the no-aspect match feed as a census and build a build-level outcome diagnostic on it** | accuracy (gives it a measure) | The probe in 4e already separates `model` from zero at +1.38pp per shared item [M]. A base-kit census would be roughly 4x the current store per window [R: 8,406 matches x about 4.6 recorded seats is about 38,700 god-builds in OB47, against 8,655 stored] and would remove the aspect skew. It is the only instrument here that could say a build is better, not more conventional | Medium. One feed per god added to the daily job; a backfill of the 45-day retention is on the order of 15,000 requests [R]. A diagnostic module that feeds nothing, like `side_by_side` | Load on SmiteBrain; survivor and role confounds need a stated design; a tempting next step is feeding it back into the score, which is §4.4's "different experiment" | **More urgent.** Retention is a rolling 45 days, so base-kit OB47 matches not stored by late December are gone, and the pre-patch half of an OB47/OB48 comparison can only be captured now |
| 2 | **Decide the stated-zero rule for movement, crowd-control and ally passives** (the first item on STATE §5's own "left" list) | readable count | Movement only: 57 to 75 readable, Carry 10 to 18, Solo 8 to 14; three Supports close (Sobek, Xing Tian, Ymir). Movement and CC: 81. Every refusal: 83 [M]. Newly readable verdicts are mostly trade-off and level | Small. A rule and its tests; no model change | It values movement at nothing and says so. It is a loosening of the measurement, which STATE calls "a rule for Jacob, not a constant" | Neutral |
| 3 | **Pool the community target across windows with a per-god floor** (the rule `aspect_matches` already uses), or at least hold the window switch until the new window has depth | accuracy of the target, churn | Removes the day-1 thin window described in 4d [R]. Expected to cut the daily target churn in 4c, size not measured: a pooled slot record cannot be built from the notes in git, it needs a second window fetched per god | Medium. About 95 more requests a day; merge slot rates weighted by matches; flag items changed at the boundary | It is a change to model inputs: the fingerprint, every control and the shipped `core` builds move. Pooling across a balance patch mixes two games | **More urgent, and in tension with the plan.** Changing the window rule before OB48 spoils the criterion 1 observation. Run it after the boundary has been watched once |
| 4 | **Shrink thin win rates toward the god's own rate** | accuracy of `core`, churn | Reach measured: with a prior worth 30 matches, 40 of 95 shipped cores change (45 of 570 slots); 10 matches, 22 cores; 100 matches, 57 cores [M]. 87 of 570 shipped core slots sit on fewer than 30 matches and 235 on no record at all [M]. Effect on accuracy: not measurable today, because the leakage-free measure zeroes `win` and the held-out metrics use it as their target | Small to write; medium to gate, since neither gate can see it | Churn with no instrument to say it helped (the same position as §4.26, which shipped OFF). Lever 1 is what would make this one measurable | More urgent by the same argument as lever 3: the day-1 window is where raw rates are worst |
| 5 | **Give aspect builds a role and score them against the per-aspect record** | accuracy for aspect players | The gap is large and measured (4f): 18.6% against 47.9%, and 0 or 1 of 6 for the hand overlays. A role-shift seam (the variant-god proposal in the 11-08 plan) addresses the 38 role-shift aspects [R] | Large. A model change through a seam that does not exist; the only gate is the frozen reference builds, since `heldout` cannot see an aspect build | An eighth hand overlay by another route (§4.33). Records rest on 30 to about 100 matches each and pool across patches | Neutral to more urgent: the per-aspect record resets toward its floor each patch, though its reach-back rule softens that |
| 6 | **Fix the two kit-reading misses behind the 0% gods** (Jormungandr, Mercury) and look at the ten physical Carries and Junglers at 0% leakage-free | accuracy | Up to 2 of 95 gods off 0% in the headline; that all ten leakage-free zeros are physical Carries or Junglers suggests a shared mechanism [R]. Not diagnosed here | Medium. A model session with a held-out delta | §4.34 already refuses the obvious closures; a per-god fix is a hand table | Moot only if OB48 changes those kits |
| 7 | **Simulate the majority-pick aspect kits** | readable count | At most 2 gods (Gilgamesh, Nike). The other 5 also fail the coverage gap [M] | Large. Needs a source for aspect numbers the scrape does not carry (§4.33) | In-game readings per aspect; goes stale each balance patch | Could be made moot or reshuffled: the majority set already changed once between 11-06 and 11-09 [M-prior] |
| 8 | **Close the scorer and simulator gap** (§4.34) | accuracy; readable count not at all | Readable count: none, since no withheld verdict is withheld for it [M]. Accuracy: 72 of 95 gods have scaling the fit side reads and the simulator does not, and 4 hybrid gates would flip [M-prior]; direction unknown | Large. Every closure is a model change on 61 to 72 gods | Needs per-ability constants the notes do not carry | Neutral |
| 9 | **Loosen `COVERAGE_GAP`** | readable count only | 0.15: 59. 0.16: 63. 0.17: 69. 0.18: 80. 0.23: 84. No limit: 88 [M]. The whole Tekko-Kagi block opens between 0.17 and 0.18 | Trivial | The constant is derived (`BAND / (6 x 5.8%)`), not a dial. Moving it to get verdicts is tuning the instrument; lever 2 is the honest form of the same wish | Neutral |
| 10 | **Compare `core` instead of `model`** | readable count | Carry 6 to 12 at the time it was measured [M-prior]. Already rejected as circular; listed so it is not re-proposed | Trivial | It partly measures itself | Neutral |
| 11 | **Other sources, Joust and Arena outcomes** | accuracy for 2 of 3 modes | Unknown. No source existed on 2026-08-10 [M-prior]; that check is three months old, and SmiteBrain's `/gods/<slug>/matchups` route has never been probed. A re-check costs an hour [R] | Small to re-check; large if a source appears | None in checking | Neutral |
| 12 | **More simulation of item passives** | readable count | None. Zero blockers are absent from `passive_sim`; all 31 are refusals or partials [M], as on 11-05 [M-prior] | n/a | n/a | n/a |

Three things the brief asked about that are not levers on today's data:

- **Priors or shrinkage for thin gods.** There are no thin gods in the current
  window (4a). The thin thing is the slot, not the god (4b), and that is lever
  4. Thin gods will exist for a few days after each patch (4d), and that is
  lever 3.
- **Pooling across modes.** Joust and Arena have no community record to pool;
  they already borrow Conquest's.
- **Aspect overlays as a readable-count lever.** The comparison runs the base
  kit and the base `model` build, so no overlay can change a verdict
  [M-prior, §4.33]. Their accuracy case is lever 5.

## 6. The one I would run first

**Lever 1: store the no-aspect match feed whole, and build the outcome
diagnostic on it.**

Three reasons. First, it is the only lever that changes what "accuracy" can
mean here. Every other accuracy lever on the list (3, 4, 5, 6, 8) ends in the
same sentence: the change moves builds and no gate can say whether it helped.
Coverage measures agreement, the leakage-free figure moves three points with
the target alone (4c), and the side-by-side reads 57 gods on a comparison that
contains no movement. The probe in 4e shows that match outcomes can separate a
build from zero on the data already in the repository, with a model that has
never seen a win rate, and its biggest weakness (94% aspect players) is a
storage choice, not a limit of the source.

Second, the data is perishable and nothing else on the list is. The feed keeps
45 days. Each day the no-aspect feed is sampled instead of stored is a day of
base-kit outcomes that cannot be recovered, and OB48 on about 11-17 starts the
clock on OB47's.

Third, it does not conflict with the plan to let OB48 land before changing
criterion 2. It changes no score, no build and no fingerprint. It is a data
store and a diagnostic that feeds nothing.

What it does not do: it will not raise the readable count. If the readable
count is the number you need to move, lever 2 does that in an afternoon, and
it is a decision, not work.

## Appendix: how each measured figure was produced

All on `1a9ca2d5`, fingerprint `89eb181b72f1`. The scripts were session-local
and are not committed.

- **Verdicts, blockers, coverage shares (sections 1 to 3).**
  `side_by_side.load_inputs()` then `side_by_side.run(...)` in Conquest; each
  row's `verdict`, `verdict_unwithheld`, `coverage`, `kit` and the
  NOT SIMULATED and PARTIAL entries of both sides' `passives`. Checked against
  `viewer/public/side_by_side/*.json`: 0 differences.
- **History table (section 1).** The same per-god pages read with `git show`
  at each first-parent commit that touched `viewer/public/side_by_side`.
- **Threshold sweep (lever 9).** Re-applied `coverage_check` at each gap to the
  stored shares and read `verdict_unwithheld`.
- **Stated-zero rule (lever 2).** Recomputed each build's share from item cost,
  counting a NOT SIMULATED item as covered when its recorded reason names
  movement (then crowd control, then an ally, then any reason). PARTIAL items
  stay uncovered.
- **Per-god coverage, zero-coverage gods, sample sizes (3, 4a, 4b).**
  `calibrate._Fixture().evaluate` at signals 0.70/0/0/0.30 and at the shipped
  signals; `god_matches_played` and slot `pick_rate` from each note's
  community entry.
- **Target stability (4c).** Community entries of `data/builds/*-Conquest.md`
  read with `git show` at `5e6604d3`, `eb76069a`, `d1c6f091` and `3c0c751f`,
  substituted into the fixture with today's items, gods and weights.
- **Outcome probe (4e).** Every line of `data/Analysis/aspect_matches/ob*/`,
  keeping matches whose six slots are all tier-3 items in the item set
  (`brawlers-ruin` mapped to Brawler's Beat Stick). Per god with 30 or more
  such matches: overlap with the reference six against `placement == 1`,
  pooled within-god slope, 2,000 bootstrap resamples over gods.
- **Aspect record (4f).** `community_aspects.aspects[*].items[:6]` with status
  `shown`, against the base `core`, the aspect `core` where one ships, and the
  `community_target` scored set.
- **Shrinkage reach (lever 4).** Each win rate in a copy of the note replaced
  by `(win x m + prior x k) / (m + k)`, `m = pick_rate x god_matches_played`,
  prior the god's own win rate; shipped-blend cores rebuilt with
  `assemble.assemble_core_converged` and compared with the unshrunk cores.

## Addendum, same day: the levers worked through, and one correction

Written after the report, when the levers were run. Everything above stands as
written at the time except the correction below.

**Correction to 4e and to the case for lever 1. [M]** The +1.38pp for the
`model` build came from the store as it then was: 94% aspect players, four
patches. With the no-aspect feed stored whole for OB47 (28,676 base-kit
matches), the same statistic on base-kit finished sixes in the god's primary
role (5,360 matches, 59 gods) reads `model` +0.44pp (-1.37 to +2.23), `core`
+2.53pp (+0.83 to +4.32), the community's six +2.82pp (+1.73 to +4.06), a
random legal six +0.19pp (sd 1.87). The `model` build does not separate from
zero on outcomes; the community's six does. Lever 1 was still the right first
lever, and for a stronger reason than the one given: it produced a result the
agreement instruments could not, and it was not the result the probe
suggested.

| # | Lever | What was done | Where |
|---|---|---|---|
| 1 | No-aspect census and outcome diagnostic | Built; OB47 backfilled (3,031 requests, 27,168 matches). Standing cost about 15 minutes a day and 1.1 MB a day in git [M] | #158, draft |
| 2 | Stated-zero rule | Built, 25 items vetted against their full text, 13 left out. Conquest readable 57 to 78, Carry 10 to 18; Joust 46 to 43; Arena 44 to 46 [M]. Fewer than the 81 estimated in section 5, because four ally items also carry a healing clause | #152, draft |
| 3 | Community window | Built as a depth floor, not pooling. Holds the old window one or two runs after a patch on every boundary on record [M] | #153, draft, held until OB48 has been watched |
| 4 | Shrink thin win rates | Built as a switch that ships off. Judged on post-dated outcomes (cores from the 11-06 record, 3,909 later matches): a null at every setting [M] | #157, draft |
| 5 | Aspect builds | The instrument only: the toggle's build holds 19% of what aspect players hold [M]. The role-seam model change is not built | #156 |
| 6 | Zero-coverage gods | Traced to the hybrid gate: 0.30 opened the magical pool to ten physical Carries and Junglers. Threshold moved to 0.54: held-out +0.0312 / +0.0162, leakage-free mixed against chance (7.21x to 6.79x, and 6.61x to 6.92x) [M]. One test is red for a real reason (Tsukuyomi's derived aspect overlay) | #155, draft |
| 7 | Majority aspect kits | Blocked. The aspect text for Gilgamesh and Nike carries no numbers; it needs in-game readings | none |
| 8 | Scorer and simulator gap | Nothing run. The register's refusal stands; lever 6 is one instance of that gap | none |
| 9, 10, 12 | Gap threshold, `core` scope, more simulation | Nothing to run, as ranked | none |
| 11 | Other sources | Re-checked. Still no per-god Joust or Arena source; smite2.live now has global Arena item win rates | #154 |
