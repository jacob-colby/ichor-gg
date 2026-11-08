# State of the project

_Last verified 2026-08-09, on `feat/community-starters`._

`docs/plans/` and `docs/specs/` are dated, point-in-time documents — they record
what was intended on the day they were written and are never updated. **This
file is the living one.** Read it before changing the model.

The detailed evidence for every decision below lives in the module that
implements it, as a docstring, next to the code it constrains. This file is the
map and the cross-cutting parts; it deliberately does not copy those numbers,
so there is one place for each fact to go stale.

---

## 1. The one thing to understand first

**`validate.compute` — the "coverage" gate — cannot be used to choose model
parameters.** Both of its targets are also model inputs:

| weights | pooled Spearman | coverage |
|---|---|---|
| `win` 1.00 | **1.000** | 60.7% |
| `pick` 1.00 | −0.057 | **86.3%** |
| `efficiency` + `fit` (the actual model) | −0.019 | 29.0% |

`win` *is* the Spearman target, so weighting it alone scores a perfect
correlation. `pick` all but determines community-build membership. Both
degenerate corners contain no modelling at all and beat every honest blend, so
the objective is maximised by **deleting the model**. The guardrails in
`calibrate.weight_grid` are not a prior on top of a sound objective — they are
the only thing standing between the search and that answer.

This explains a long run of "obviously correct change makes the gate worse"
results (§4). A change that makes the model *more* informative but *less* like
the community's own data is punished by construction.

**Use the leakage-free measure instead.** Zero `win` and `pick`, then read
coverage against a random legal 6-item core:

```bash
cd pipeline && python -m smite.calibrate     # prints the probe, the baseline, and the sweep
cd pipeline && python -m smite.calibrate --control   # the same control, ~7s
```

Chance is ~5.7%. Shipped is ~39.7% at the probe split and ~40.3% at eff
0.45, i.e. **~7.0× chance**.

**"Leakage-free" means the SIGNALS are zeroed — it does not mean no
community-derived number reaches the score.** One shipped pricing flag reads a
constant measured off the community record (`conversion_reference`), and
`calibrate` does not neutralise it. Audited and measured 2026-09-03: it is
worth about −2.6pp of level here and −0.6pp at the second split, and changes
no verdict in §4, because every verdict there is a delta with the constant
held fixed on both arms. **§4.20** has the numbers and the blast radius; read
it before quoting an absolute figure dated on or after 2026-08-14.

**IT IS ALSO BLIND TO ANYTHING THE `win` AND `pick` WEIGHTS MULTIPLY BY
ZERO.** Zeroing the two signals is what makes the measure honest, and it is
also why the measure cannot see a decision that lives *inside* one of them.
`scoring.god_unknown_win_rate` — what an item with no community record scores
on `win` — is such a decision, and it currently decides **28% of Conquest core
slots**. Run the control with that placeholder at the god's median, at the
god's floor, at 0.0 and at 1.0: coverage is **40.9074% / 37.6111% in all four**,
identical to four decimals at both splits. **§4.26** has the demonstration and
the size. Read it beside §4.23: that entry found a community-derived constant
this measure cannot *neutralise*, and §4.26 finds a model decision it cannot
*see*. Both are the same sentence — "leakage-free" is a claim about the four
signals and about nothing else — and together they bound what a 0.0pp reading
is allowed to mean.

**Do not quote those figures — re-measure them.** They move with the data, not
just with the model, which is what `--control` exists for: the baseline, the
same two fixed splits, and an input fingerprint, in ~7s instead of ~7 minutes.
It says on its own line when the fingerprint differs from the one stamped in
the committed `_calibration.md`, which is the direct answer to "is this the
same dataset" that a moving baseline was only ever a proxy for. Evidence and
the choice of splits are in `calibrate.py`'s docstring. Headline coverage moving the other way is
expected and is not by itself a reason to revert — that judgement is what
`efficiency.efficiency_pool` and `scoring.lookup_rates` both record.

**The printed baseline wobbles ±0.15pp and it is not a data refresh.** The
usual tell that the committed `_calibration.md` has gone stale is the
random-core baseline moving, because chance cannot depend on a model flag —
and in expectation it does not. But `random_core_baseline` is a 200-draw Monte
Carlo over `score_god_items`, which returns its rows **sorted by score**, so a
model change reshuffles which items a fixed seed samples. Measured across
`price_adaptive` off/Strength/Intelligence (2026-08-21): the printed baseline
read 5.73% / 5.59% / 5.65% while the *exact* value — mean over gods of
`min(6, pool)/pool`, which is what the sampler estimates — was **5.7391% in all
three**, off a byte-identical pool. Compute that closed form before concluding
the data moved.

**Implemented in:** `pipeline/smite/calibrate.py` (leakage probe,
`random_core_baseline`, `model_signal_sweep`, bootstrap CIs).

---

## 2. What the model can and cannot do

Measured, leakage-free, 2026-08-05:

- **It is a working filter.** Efficiency + fit find community-worthy items
  ~4.9× better than chance. Fit does most of that work; efficiency alone
  reaches only ~2× and efficiency-*dominant* blends collapse.
- **It is not a working ranker.** *Within* the community's own item set it has
  no ordering skill — mean within-god rank correlation ≈ −0.02, positive on
  fewer than half the gods.

Both are true at once, and the headline coverage number conflates them. Treat
"these builds contain sensible items" as supported and "these builds are in the
right order" as unproven.

**Neither measure can say a build is BETTER, only more conventional** — both go
down when a build is genuinely better and unconventional. The one instrument
that can is `build_quality.py` (2026-08-21): `combat.py`, which has never seen
a community build and is exact against the game, pointed at our meta-free
`model` core and the community's six items for every god at level 20 —
basic-attack and ability DPS against 70 and 170 protection, effective health,
and each per 1000 gold. Its output is `data/Analysis/_build_quality.md`, the
distribution rather than an average, broken out by role. **Read its caveat
first:** it re-measures on every run that ~90% of the buildable pool and ~76%
of the community's slots carry passive value the arithmetic cannot see, and
that the community pays more per slot above its stat line than we do, so a
verdict in our favour is the one to distrust. It is a diagnostic and feeds
nothing (a test pins the import boundary); it is also the cheap way to re-test
a model change such as `damage_fit_blend` moving off 0.0.

**Its pooled figure is not a verdict either, and since 2026-08-21 it does not
stand alone.** One metric applied to 89 gods averages five roles that do not
share an objective, and that hid a real defect: our Carries are tankier than
the community's on 18 of 18 while winning damage on the fewest of any role,
which is the *same* behaviour that is correct for Support. `ROLE_OBJECTIVES`
judges each role on its own — naming, per role, the quantity maximised and the
quantity treated as a threshold — and §4.13 records that neither threshold can
be evaluated at all under the current damage model. The role split does **not**
escape the passive blind spot; the report says so on the section.

**Since 2026-11-02 there is a second instrument of that kind, and it closes
most of the blind spot rather than printing it.** `side_by_side.py` runs our
`model` core and the community's cleaned six through `combat.py` on a 10-second
event clock with item passives SIMULATED, one item at a time from its own text
(`passive_sim.py` — never one price per passive class, which §4.20 refused and
the 2026-11-02 passives analysis measured at ~0% recovered). It reports burst
and 10s sustained damage against a squishy and a tank taken as the medians of
the community's own Mid and Support builds, effective cooldowns, crit EV,
effective health on both channels (health-gated protection integrated over the
bar), power at 2/4/6 items, and for every item only one side buys: its
community pick and win rate, its passive's worth in numbers, and the model's
own reason for not buying it. Each god gets a verdict under a rule written in
the module docstring before the run. Items it cannot model honestly (kills,
crowd control, actives, an attacker on us, movement) are marked `not
simulated` with the reason, per build. It is a diagnostic and feeds nothing; a
test pins the import boundary. Done criterion 2's status is in §5.

---

## 3. Design decisions worth not re-litigating

Each of these has its evidence in the named module.

| Decision | Where | One-line reason |
|---|---|---|
| Tier list ranks on outcomes, never on our score | `tierlist.py` | Our god score correlated −0.117 with real god strength; the win term alone +0.438 |
| Joust/Arena ship **unranked** rather than model-ranked | `tierlist.py` | No outcome data exists; the score that used to fill the gap is the −0.117 one |
| Gold fit **keeps** components and relics | `efficiency.efficiency_pool` | Narrowing the pool identifies stat prices worse; measured both ways |
| Gold fit **excludes** statless items | `efficiency.efficiency_pool` | No stat information, only intercept drag — and their residual is meaningless |
| A stat needs ≥2 carriers to earn a column | `efficiency.MIN_STAT_CARRIERS` | A single-carrier column is exactly determined, so its residual is a fit artifact |
| **Paid** relics take one of the six; free ones don't | `scoring.is_buildable` | The game's free slot is for the BASE relic. Shell of Rebuke is in 62 community six-item builds; Blink Rune (cost 0) in none |
| God-specific items are buildable for their owner only | `scoring.is_buildable` | Aladdin's lamp is in 77% of his builds and unbuyable for the other 86 gods |
| Hybrid scalers may build off-type items | `scoring.is_hybrid_scaler` | Neith takes 55% of her ability damage off Intelligence; the label is one word, kits are not |
| Community rates read slot picks **and** alternates | `scoring.lookup_rates` | Slot-only made an item bought 27% of the time read as "meta doesn't buy this" |
| `unknown_win_rate` stays at 0.5 | `scoring.UNKNOWN_WIN_RATE` | It is *not* neutral (observed mean 0.556) but the only metric that responds to changing it is the circular one |
| Draft blocks duplicates per **team**, not per board | `useDraftResult.takenFor` | Only ranked Conquest drafts globally-unique picks; Joust and Arena are not draft modes |
| A draft bonus is damped when the core already covers that **tag** | `draftBuild.adaptedCore` | Same judgement `ally_covered` makes about a teammate; tags only, because a stat is a quantity not a job |
| The community scrape reads ONE patch window, chosen per run | `refresh.choose_community_window` | SmiteBrain defaults to the newest patch, whose window opens the hour the patch lands; the 2026-11-04 run read a one-day window and committed it |
| Rolling ranges (`1w`/`2w`/`1m`) are refused as community windows | `smitebrain_parser.patch_windows` | They straddle balance patches, and `validate`'s Spearman floor is calibrated on the window RESETTING at each one |
| A roster-wide loss of complete community records fails the daily job | `refresh._refuse_community_collapse` | 11 of 11 refreshes on record were 100% complete; the enforced gate (`validate --check`) cannot see this and passed on the run that lost 47 |
| Every scored item's passive is DECIDED — simulated, partial or refused | `passive_sim.REGISTRY` | Absence is not a decision: an absent passive is zeroed by accident, which lowers predicted cost and makes the item look more premium. 193 of 193 decided (2026-11-05) |
| A debuff on the enemy's attack speed or Strength is worth exactly 0 here | `side_by_side.attacker_profile` | Its raw DPS is derived from the reference squishy over KILL_TIME and each hit is `dps x share x step`, so the cadence sets WHEN, never how much |
| An item is refused WHOLE rather than credited with its good half | `passive_sim` (Xibalban Effigy) | `reduce_hit` would simulate its 50% cut in two lines and the clock has no channel for the payback, so the item would be booked with its upside alone |
| The comparison page's window label is DERIVED from the data, not the patch | `side_by_side.community_window_label` | Read off `_patch.json` it said "community window Open Beta 47" through a healthy window, a catastrophic one and a restored one alike; the match count is what makes a thin window visible |
| `use_rate`'s denominator is BUILDS, not matches | `side_by_side.community_sample` | 67,532 god-builds against 14,667 matches in the same window, 4.6x apart because the god index records ~4.6 of a match's ten seats; PR #109 labelled the derived figure "matches" |
| Stat conversions are priced against a **typical** build | `passives.conversion_grants` | One pass, no fixed point; prices the deterministic case right and the self-referential one conservatively |
| An **Adaptive Stat** grant is priced, as **Strength** | `passives.adaptive_grants` | Eight buildable items carry their whole power in passive text and all eight read `premium`; the branch is chosen from the item's own text so there is no fixed point, and it is the conservative one on 6 of the 8 |
| That flag's gain is a **pool-wide** reprice, not those eight items | `passives.adaptive_grants` | None of the eight reaches a core either way. 29 items were parking ~1000g each in the intercept, which under-priced every stat for every item: 1111 -> 934, Strength +17% |
| A conversion is priced only into a stat the item **already sells** | `passives.conversion_grants` | Nimble Ring turns Intelligence into a basic-attack channel the god-agnostic fit cannot judge; priced in full it hit 52 cores against 3 community builds |
| Arena and Joust discount **late** items; Conquest does not | `assemble.time_value_multiplier` | Arena's 500 tickets accrue from 0:00 so value is uniform; both Titan modes are back-loaded. Not about affording items — income scales with match length |
| Community pick is **conditional on reaching the slot** | `scoring.SLOT_REACH` | Slot mass decays 0.684 → 0.222 from slot 1 to 6; an item bought sixth was divided by matches that never bought a sixth item |
| Stance gods' abilities live in a **tab wrapper** | `wiki_parser._section_tables` | Ullr, Artio and Merlin reported `n_scaling_abilities: 0` — 28 ability tables the parser walked straight past |
| Eye of Providence carries a **`ward-economy`** penalty | `data/_tags.yaml` | Its stat discount is the ward engine's price tag; 16 Support/Solo cores against 1 community sighting |
| `god_item_scores` ships **one table per mode** | `build_index._god_item_scores` | A mode toggle that changes the label and not the model is worse than none; Eye of Providence sat in Joust cores because the draft was Conquest-scored |
| A threat is the **union** of role label and measured kit | `threats.ts`, `threat_kit.py` | Label alone: `Healing` on 9 of 89 gods. Measurement alone at 1 ability: 42, mostly incidental. Label OR 2+ abilities: 18 |
| A **defensive** draft bonus is scaled by the god's archetype | `defense_affinity`, `threats.threatOverlay` | Flat, it answered "they are magical" with "become tankier" to a Hunter: protections in 40 carry cores went 32 → 70. Scaled, 24 — and penetration 159 → 203 |
| The draft clamp bounds the **stack**, not the strongest channel | `draftBuild.adaptedCore` | Clamping the sum made 2 healers and 4 healers produce the identical build; anti-heal adoption 16/31 → 31/31 with every other comp unchanged |
| A relic answer is called out **on its own line** | `draft.relics` in `_weights.yaml` | It does take one of the six, but the model can't price a `+7.5% of all Stats` multiplier, so it never wins a slot on score and has to be named explicitly |
| Joust/Arena **borrow** Conquest's community record for the Hybrid | `modes.<mode>.borrow_community` | No record of their own meant no Hybrid at all (89/89 gods returned the model core). Borrowed minus `stacking` and `ward-economy`, and disclosed as borrowed |
| The **Balanced** tab is hidden when it equals Model | `builds.dedupeCoreAgainstModel` | Joust and Arena zero `win` and `pick`, so the blend IS the model build — byte-identical on 89/89, with the duplicate claiming a blend that never happened |
| The aspect control is an **orange hexagon on the portrait** | `AspectBadge.tsx` | Where SMITE draws it, so it is self-describing; orange rather than gold keeps the Torchlight Rule intact |
| An aspect with no overlay **falls back** to the base build | `DetailPanel.aspectFamily` | 72 gods have an aspect, 7 have a scoring overlay; filtering strictly blanked the model side for the other 65 |
| An aspect overlay is **derived** from the note, never typed, and ships **only if it moves a build** | `aspect_kit`, `recommend._family_moves` | Abilities from the `kit_changes` text, numbers from the note, overlay = `fit_map` on the aspect kit minus `fit_map` on the base. A family identical to the base tells the toggle's reader their build changes when it does not. 1 of 78 aspects derives today and moves nothing (§4.33) |
| The draft offers **one** archetype, not the god page's eleven | `archetypeParity.test.ts` | The draft's own build already disagrees with the god page's on 73 of 89 gods (16/89 exact, 79.8% item overlap) with NO overlay applied — `adaptedCore` fills greedily in one pass, `assemble_core_converged` re-prices as it fills. Adding flavor tabs on top would ship ten more disagreements; a sweep of 21 overlay settings closes none of it |
| Effect-tags name two things: the **job** and **when the value arrives** | `data/_tags.yaml` | The original 11 were all jobs, and 55 of 138 buildable items went untagged because what they do is conditional, not a role |
| `penetration` is **its own tag**, not folded into `protection-shred` | `data/_tags.yaml` | Shred debuffs the target and helps the whole team; penetration only helps you. Merging them would make the two permanently indistinguishable |
| A tag with no bonus is inert to the **gate** and not to the **builds** | `assemble._is_sustain_item` | 11 of 12 new tags moved coverage 0.0pp; the `sustain` ones still moved 3 cores, because the cap reads the tag |
| `max_lifesteal` is a **sustain** cap and the name is the only thing saying otherwise | `assemble._is_sustain_item` | 13 of 21 buildable `sustain` items carry no Lifesteal stat; narrowing it to the stat would let a core stack three stay-alive items |
| Waste past a stat cap is **priced**, not refused | `assemble.cap_overflow_penalty` | A reject rule fires only when an item's WHOLE line is capped, and no penetration item is pure penetration; charging the overflow keeps the Intelligence and drops the dead penetration |
| An item's offense tags **sum** | `offense_tags` in `_weights.yaml` | Flat, an item answering a tank two ways scored what one answering it once did — which is how `penetration` on Titan's Bane displaced Heartseeker |
| A resolved expert claim is measured against its **own recorded baseline** | `expert_review.regressions` | The old rule only failed on a full reversion, so `clear` → `partial` shipped green |
| `build_quality` is a **diagnostic**, never a scoring input | `build_quality.py` | Register §4.4 is what happens when a damage measure becomes a fit signal; its output is a report a human reads, with the passive blind spot printed above the first number on every path out — `emit` is the module's only print and only file write (the `--god` path once returned before the blind spot was measured, 2026-08-21) |
| Each role is judged on **its own objective**, not on one pooled metric | `build_quality.ROLE_OBJECTIVES` | Ours is tankier than the community on 18 of 18 Carries while winning damage on 12 — the same behaviour that is CORRECT for Support (EHP 14 of 14, DPS a coin flip with 3 exact ties). A scalar scoring "more EHP is better" cannot tell those apart, so the pooled count was partly an artifact of averaging |
| Every role's verdict names **which quantity was a threshold and which was maximised** | `build_quality.role_verdict_lines` | So a reader can disagree with the choice rather than only with the number — and so an inert threshold stays visible next to its measurement instead of being dropped quietly (§4.13) |
| The **duel score** (EHP × DPS) is Solo's objective and **nowhere else's** | `build_quality.ROLE_OBJECTIVES` | Their TTK on you over yours on them, with the reference opponent cancelling exactly, so doubling EHP and halving damage scores 1.00 — no constant chooses it. Applied to Carry it turns 12/6 into 17/1 by paying full price for Berserker's Shield, i.e. it hides the defect the split exists to find |
| An objective with an **effective-health term** is scored on BOTH damage channels | `build_quality.EHP_CHANNELS` | A build has one damage output and TWO effective healths, and which one its survival is read on is a property of the ATTACKER — of which this comparison contains none. Mixed-stream EHP is a weighted HARMONIC mean of the two and the ours-over-theirs ratio is monotone in the mix, so every mix lands between the channels and the pair is the whole range rather than a hedge. Solo and Support read `ehp_physical` alone until 2026-08-23 — the two roles whose job is durability, scored on half the damage in the game (§4.17) |
| A **threshold** reads the one channel its named attacker deals | `build_quality.ehp_against` | The maximands report a pair because no attacker appears in them; a threshold names one — the roster's largest burst, or the Mid/Jungle whose burst is measured — so the channel follows from that attacker's `damage_type` and needs no mix. Both were hard-coded to `ehp_magical`: right by coincidence for the Carry floor, whose reference burster is Scylla, and wrong for the 16 physical Junglers in the kill threshold's population. Neither correction moves either count, which is §4.13 and not a licence |
| Support is scored with damage **excluded**, not down-weighted | `build_quality.ROLE_OBJECTIVES` | Most of what a Support does is in `UNMEASURABLE` (CC chain duration, peel, aura coverage, wave clear, objective damage, map tempo), and on 3 of 14 Supports the DPS column is identical on both sides to 0.00% because neither build buys any. Scoring a quantity badly is worse than declining to score it |
| The fit map gets an **Attack Damage column** from the god's own scaling | `damage_value.attack_damage_fit` | `role_stats` and `kit_stat_overlay` between them never name the stat, so the merged fit map scored it 0.0 on 89 of 89 gods while their basic-attack scaling measures it non-zero on all 78 that parse; probe 38.7% → 39.7%, best 39.6% → 40.3% |
| That column is **credited but not charged** | `scoring.god_fit_score` | `fit` is normalised by the sum of the map, so charging it shrinks every non-carrier's stat term (−12.5% over 10,065 pairs) and promotes the flat tag bonuses added after normalisation — which pulled 43 anti-heal items into Joust and Arena cores, the two modes with no gate to catch it |
| An item is **charged** for the gold it spent on stats the god's map does not name | `efficiency.offmap_adjusted_score` | `efficiency` prices every stat whoever is buying and `god_fit_score` normalises over the map alone, so an off-map stat was credited by one half of `quality` and invisible to the other. Shipped at 0.55 once `offmap_exempt` covered the three stats no map names and no instrument prices; Berserker's Shield leaves 17 of 18 Carry cores and their effective health lands LEVEL with the community's |
| The strength is the **midpoint of a region**, never the argmax | `offmap_efficiency` in `_weights.yaml` | Both leakage-free splits are at or above control across 0.45–0.65; 0.60/0.65 being joint-highest on the probe split is not a reason to pick them (§4.4's plateau). The best split reads 40.0% at five consecutive settings because every core that changes inside the region swaps an item in NEITHER side's community record — checked item by item, not assumed |
| Buy ORDER reads the community's **slot distribution**, not just tags and cost | `assemble.build_order` | `build_order`'s docstring said "we have no real build-path data" and that was FALSE — every community `slot_order` entry is a per-slot distribution and `build_index.popular_items` flattened it to each item's highest rate anywhere. Inside tier 3 costs cluster 2350-3000g, so the order was cheapest-first: 68 of 380 orderable pairs (17.9%) ran backwards against the community on 39 gods, 40 (10.5%) after |
| Ordering agreement is measured as **inversions**, never as displacement alone | `order_agreement.inversions` | Our core and theirs share 3-4 of 6 items, so "our slot 4 vs their slot 2" is two different clocks. A pair of items we BOTH build, whose community centroids differ by a slot, cannot be moved by membership at all |
| Joust and Arena get **no** positional order, borrowed or otherwise | `recommend._build_entry_set` | The Hybrid may borrow Conquest's record for item CHOICE and says `borrowed_from` when it does. A slot centroid is a claim about WHEN a spike lands, and both modes zero `win`/`pick` on the grounds that Conquest describes a different game — Arena's gold spools from 0:00. Timing is more mode-specific than choice, not less (§4.20) |
| `diffCore` reports **order**, not only membership | `draftBuild.diffCore` | Both cores were reduced to `new Set(...)`, so a draft that resequenced the same six produced `added: []`, `removed: []` and a board reading "nothing changed" under a list that had. A test asserted that behaviour as correct |
| The damage model counts the **basic attack**, and its unit is one rotation plus one swing | `damage_value.item_damage_gain` | `ability_damage_components` skips the Basic Attack slot, so Attack Damage — 100% of a basic attack on 84 of 89 gods, and no ability in the roster scales on it — was worth exactly 0.0 in the only damage path that reaches a recommendation. 12 items carried it, 10 more carry Critical Chance. The 1:1 mix is a declaration, not a measurement; the clock that would replace it is register §4.12 |
| An **ally-dependent** item only reaches a god whose kit can buff an ally | `ally_kit.py`, `scoring.score_god_items` | Four items pay out only when YOUR ability buffed, healed or shielded an allied god, and on the other 63 gods the passive is dead text. Lotus Sickle reached 25 gods through the scoring path and sat in shipped `cooldown` and `mana-stack` builds; the gate removed it and Eros' Bow from 125 suggested builds and 4 cores. It rides `excluded_items`, the mode-exclusion seam, so no flavor bypass can reintroduce it |
| The gated set is the passive's **trigger**, not its recipient | `ally_kit.requires_allied_god` | `_passive_classes.yaml`'s `D1 ally-directed` is the recipient question and names 21 items; Triton's Conch and Chandra's Grace land value on allies while the ITEM does the buffing and need nothing of your kit. The trigger phrase names exactly four: Lotus Sickle, Soul Locket, Eros' Bow, Rod of Asclepius. Derived from live text, so a refresh gates a new one unattended |
| An **aspect** is a different kit for that gate | `ally_kit.buffs_allied_god` | 31 gods qualify on the base kit, 5 more only with an aspect selected. Asking the base question for an aspect build withholds a usable item; asking the aspect question for a base build ships an unusable one. Chronos is the live case: his base cores lose Eros' Bow, his Time Field aspect cores keep it |

### The combat model is exact and should stay that way

`combat.py` is calibrated against twelve in-game readings with **0.0% worst-case
error**, gated by:

```bash
cd pipeline && python -m smite.calibrate_combat
```

Constants carry evidence tiers (`MEASURED` / `DOCUMENTED` / `INFERRED` /
`OBSERVED`, where OBSERVED outranks all). Several overturn published sources —
crit is 1.5× not 1.65×, Deathbringer's +35% *adds* to 1.85× not 2.0×, Attack
Power needs a 0.81 correction **on the base only**, and the game floors
displayed damage. Add observations to `data/_combat_observations.yaml`; an
empty file fails the gate deliberately.

`--plan ATTACKER TARGET` generates fully-determined test setups (it skips
abilities with hidden damage terms and items whose passive fires on cast).

---

## 4. Negative results register — do not re-attempt without new evidence

Every one of these looked obviously correct, was implemented, measured, and
shipped **off**. Numbers are in the named module.

1. **Excluding components from the gold fit** — cross-validation said yes, the
   gate said no; the CV was measuring prediction error, which nothing needs.
2. **Stat caps in build assembly** — correct, but changes 0 of 261 cores.

    _Re-measured 2026-08-21, because the first measurement could not have
    fired._ The original ran with three exotic stats in `stat_caps`
    (Tenacity/Plating/Dampening), so "0 cores" was never evidence that caps
    don't matter. The list is now the full SMITE 2 one, surveyed against the
    wiki's Stats page with sources and tiers in `stat_caps` (`_weights.yaml`),
    and penetration is split by unit — `Penetration %` and `Penetration` are
    different goods under one key, which `efficiency.stat_key` already knew
    and the cap machinery did not. **The answer is still 0, now of 2237
    cores** — and the reason has changed. Three of the five caps are genuinely
    unreachable (peak Tenacity 15 of 50, Plating 25 of 35, Dampening 5 of 35),
    as is flat penetration (40 of 50). **Percentage penetration is not: 47 of
    2423 cores overshoot its cap today and 59 more sit exactly on it.** The
    rule cannot act on them because `assemble._capped_out` refuses an item
    only when EVERY stat it carries is capped, and no penetration item in the
    pool is pure penetration. A pure reject rule cannot say "the penetration
    is wasted, the Intelligence is not"; pricing the overflow could.
    **It now does** — `cap_overflow` (2026-08-21) ships at 1.0 and is the one
    thing in this entry that is not a null; see §3. The reject rule stays
    underneath it for the fully-dead-weight case a charge can only make
    expensive. Numbers in `assemble.assemble_core`.

    Two things the survey settled, both in `combat.py`'s penetration block.
    That a penetration cap EXISTS is no longer inferred — it is MEASURED off
    our own scrape, since Titan's Bane, Obsidian Shard and Dominance all carry
    "This effect ignores the Penetration cap". Its VALUE got weaker, not
    stronger: no SMITE 2 source states one, and 40%/50 traces to SMITE 1
    material that SMITE 1 itself superseded in April 2023 (40% → 32%).
    **SMITE 2's cap system is not SMITE 1's** — Cooldown Rate is a haste stat
    with no cap (`CD = base×100/(100+CDR)` diminishes itself, so SMITE 1's 40%
    CDR cap must not be carried across), Attack Speed's SMITE 1 cap was on the
    effect and not on the item stat, and Healing Reduction caps at 25% but
    *does not stack with itself*, which is a non-stacking rule rather than an
    additive budget and cannot live in `stat_caps` at all.
3. **Magnitude-aware fit (B4)** — item stat magnitude as a fit term.
4. **Damage-gain as a fit signal (B5)** — halves the gate; it cannot price
   defence at all.

    _`damage_fit_blend` swept against the leakage-free splits for the first
    time, 2026-08-21._ The two numbers this entry carries are `validate.compute`
    figures, and §1 says what that gate is worth. On the honest measure the
    sign reverses: **every setting from 0.05 to 0.75 beats control on both
    splits** (probe 38.7% → 39.8% at 0.75, best split 39.6% → 40.0%), and **not
    one paired CI excludes zero** on either. It is a real knob — core churn
    rises 3 → 37 of 89 monotonically across the sweep, so unlike `adaptive_fit`
    this one could have varied and did. It stays at 0.0 because nothing clears
    the noise, **not because it makes the model worse**, and the difference
    matters to whoever picks it up next: blends of 0.05–0.30 move exactly one
    god's coverage on the 0.45:0.55 split, so the only strength worth a real
    test is 0.75. Sweep, paired CIs and churn under `damage_fit_blend` in
    `_weights.yaml`. The "halves the gate" claim belongs to the separate
    *damage gain AS the fit signal* row (23.6%), not to this blend.

    _Resolved 2026-08-21, mechanically rather than statistically, and the knob
    turned out to be two knobs._ The aggregate could not settle this and never
    will: the paired statistic is the per-god coverage delta, and at the best
    split it is **exactly zero on 83 of 89 gods** (78 of 89 at the probe
    split), because a core has to actually change AND the changed item has to
    be a community pick before a god contributes anything at all. Resampling a
    vector that is zero on 93% of its entries harder does not make it sharper.
    So the 20 changed cores at 0.75 were read one at a time instead, and the
    knob decomposes:

        arm, at blend 0.75         probe 0.70:0.30      paired 95% CI    cores
        control                          38.7%                     --       --
        all three stats                  39.8%       [-0.22%, +2.58%]    37/89
        Strength + Intelligence only     38.6%       [-1.80%, +1.57%]    29/89
        Attack Damage only               40.4%       [+0.19%, +3.22%]    30/89

    **The Attack Damage column is the whole of it**, and the Strength/
    Intelligence remainder is a null that actively dilutes it — both halves on
    together score 40.0% against 40.6% for the Attack Damage half alone. The
    reason is a hole, not a weighting: `role_stats` never names Attack Damage
    and neither does `kit_stat_overlay`, so the merged fit map scores it at
    **exactly 0.0 on 89 of 89 gods** while `damage_value.stat_weights` measures
    it non-zero on all 78 whose kit parses. That is the fit-side twin of the
    hole §3 closed on the damage side the same week, and neither was visible
    while the two halves were measured as one number.

    **Carved out and shipped ON as `attack_damage_fit` at 1.0** — see §3. It is
    the only thing in this entry whose paired CI excludes zero (probe 38.7% →
    39.7%, [+0.22%, +1.91%], better on 5 gods and worse on none).

    _Swept on Joust and Arena before merging, and that changed the flag._
    Those two modes are 178 of 267 build groups, neither has a community block
    on any of its 89 notes, and both zero `win`/`pick` so the fit map is the
    whole score. The first cut moved 46 of 89 Joust cores and 39 of 89 Arena
    ones — and **43 of those arrivals carried no Attack Damage at all**. They
    were anti-heal items, Divine Ruin and Toxic Blade, and zeroing the mode
    `tag_bonus` removed every one of them. The cause is that `god_fit_score`
    normalises by the sum of the map while the tag bonus is added AFTER, so a
    new column shrinks the stat term (−12.5% over 10,065 god-item pairs) and
    promotes every tag bonus against it. Conquest's only mode bonus is
    negative, so the artifact was invisible in the mode that has the gate and
    decisive in the two that do not. The column now ships excluded from the
    normaliser; Joust churn 46 → 19, Arena 39 → 20, anti-heal arrivals 43 → 19,
    Attack Damage arrivals unchanged, and **about a third of the original
    headline turned out to be the shrink rather than the column** (probe 40.6%
    → 39.7%). A sweep in a mode with no gate found a bug the gated mode was
    rewarding. What is left
    under `damage_fit_blend` is the Strength/Intelligence remainder, re-swept
    as itself: it peaks at 0.30 on the probe split and then falls BELOW control
    (37.7% at full strength, worse on 11 gods against better on 7) while the
    best split sits flat at +0.2pp moving at most two gods. Two splits
    disagreeing about the direction is entry 9's shape and it ships off for
    entry 9's reason. **The register's old summary of this entry was wrong in
    both directions at once** — "halves the gate" was the wrong experiment, and
    "nothing clears the noise" was two experiments averaged into one null.

    Two things found on the way that are worth more than the ship decision:

    * **`blend_stat_values` scales by the wrong reference.** Its docstring says
      defensive stats "keep their role weight untouched", which is true of the
      values and false of the comparison: the measured weights are scaled to
      `max(role_map.values())`, which for a tank or a support is a PROTECTION,
      so offence is promoted toward defence while defence stands still. Mean
      offensive fit mass at 0.75 rises +30% for a damage god and **+71% for a
      tank or support**, and Health/Protection then leaves the moved cores —
      net −1535 points at 0.75, −4125 at 1.00, which is exactly where coverage
      turned back down. Scaling by the largest *offensive* role weight instead
      removes the turn-down (probe 38.9% → 40.0%, best 39.4% → 40.1% at 1.00).
      Measured, not shipped — with Attack Damage carved out there is no gain
      left for it to protect — and recorded so the next attempt starts from
      fixed arithmetic. Jormungandr losing Shifter's Shield, his 46%-pick
      slot-1 item, is this bug and not the damage model.
    * **The gain does NOT concentrate where the damage model measures well.**
      Spearman between a god's coverage delta and its `n_scaling_abilities` is
      +0.05 on the probe split and −0.18 on the best one. Whatever this is, it
      is not "the mechanism working hardest where the kit parsed cleanest", and
      an attempt that assumes it will should check that first.
5. **Pricing item passives** — the extraction is right and the prices are
   visibly more sensible; the recommender still got worse.

    _Scoped 2026-09-02 (§4.20)._ Read this entry as a verdict on `price_passives`'
    CONFIGURATION, not on unconditional grants as a class: beyond the thirteen
    items the shipped carve-outs price, the flag reaches nine tier-2 components,
    Dominance and Shogun's Ofuda, and prices the Adaptive Stat clause as its own
    single-class column (the defect `price_adaptive` records). That is what was
    measured worse. The unconditional grants it never reached — Triton's Conch,
    Dwarven Plate — it never reached because of the parser, and are in §5.
6. **The 2026-08-05 weight sweep's own winner** — rejected as leakage (§1).
7. **Build coherence (2026-08-09)** — the only term that scores a *set* rather
   than an item, discounting an item by how much of its stat line the core
   already holds. Leakage-free coverage 32.1% → 16.6% as strength goes 0 → 1,
   and restricting it to stats with real diminishing returns doesn't rescue it.
   Unlike 1–5 this one probably *is* wrong on its merits rather than punished
   by the gate: real builds are stat-concentrated, so penalising duplication
   pushes away from the shape of every focused build in the game. Numbers under
   `coherence` in `_weights.yaml`; ships off.
8. **Pricing persistent stacks (2026-08-09)** — counting a stacking item at its
   full-stack value when it reaches a cap and keeps it, never for a transient
   stack. Leakage-free coverage 33.1% → 28.8% at the probe split, flat at the
   best split. Keep the numbers in view though: it moves Transcendence from
   rank 25/95 to 6/95 for Ullr and flips its residual +208 → −222, which is the
   exact item an expert reviewer named. **This is the cleanest case on record
   of the two gates disagreeing about a specific item**, and the one most worth
   revisiting if a non-circular measure ever exists. `price_stacks` in
   `_weights.yaml`; ships off.
9. **Conversion-aware fit (2026-08-15)** — the fit half of the conversion fix.
   `price_conversions` taught *efficiency* that Transcendence's 300 mana is
   really Strength; fit still read the item at 0.172 and ranked it 48/95 for
   Ullr in Joust, where there is no win rate to carry it. `conversion_fit` adds
   the source stat to the god's fit map, weighted by what that god's own map
   says about the stat it converts *into* — mana is worth to Ullr exactly what
   Strength is, and worth nothing to a Guardian whose only converter makes
   Intelligence. It works as designed (fit 0.172 → 0.238, rank 48 → 36) and no
   setting from 0.05 to 1.0 beats control on both leakage-free splits; the two
   splits move in *opposite* directions across the sweep. Two things worth
   keeping: the obvious gate ("does the god's pool contain a converter") is
   **vacuous at 87 of 87 gods**, since the damage filter admits Transcendence
   to every physical god and Book of Thoth to every magical one — any future
   attempt must weight by the target, not the converter. And 36/95 is not a
   core slot, so even shipped on this would not produce the build the reviewer
   asked for; the `mana-stack` flavor is the supported route to it. Numbers
   under `conversion_fit` in `_weights.yaml`; ships off.

10. **Adaptive-power fit (2026-08-19)** — the fit half of the adaptive-stat
    problem, and the twin of #5 rather than a repeat of it. Eight buildable
    items carry their whole power stat in passive text and none of it in
    `stats`, so `god_fit_score` reads Omen Drum — 2800 gold — off `{Echo: 30}`
    and returns 0.0000 for Ullr. `adaptive_fit` credits the grant to whichever
    of Strength/Intelligence the god's map weights higher. **It is an exact
    no-op at every strength from 0.15 to 1.0**, and stays an exact no-op even
    with `price_passives` ON. The mechanism is not broken — Omen Drum's fit for
    Ullr goes 0.0000 → 0.1720 — it moves him from rank 90 to 88 of ~90, which
    is not a core slot. These items are bottom-ranked on *efficiency* too, and
    the half that would actually move them is the one that costs −1.4pp on the
    probe split, alone or paired. **Fixing one half of a two-half problem buys
    nothing**, which is worth knowing before anyone tries the other half again.
    Numbers under `adaptive_fit` in `_weights.yaml`; ships off.

    _Re-measured 2026-08-20, because the first sweep could not have varied._
    The strength was applied by injecting the grant into `stats`, and with
    `magnitude_fit` off `share` is 1.0 whatever the value — so every setting
    from 0.15 to 1.0 ran the same code path and "no-op at every strength" had
    measured one behaviour five times. The scale now applies to the stat's
    WEIGHT (`scoring.god_fit_score`), and Omen Drum's fit for Ullr really does
    move with it: 0.0258 at 0.15, 0.086 at 0.5, 0.1720 at 1.0. Coverage is
    still **35.5% / 36.7% at every one of them** — identical to control. The
    conclusion above was right; only its evidence was. The full-strength figure
    it was written from is unchanged, so nothing else in this entry moves.

    _The other half was carved out and shipped ON, 2026-08-21._
    `price_adaptive` is the efficiency half taken alone rather than as part of
    `price_passives`, and it beats control on both leakage-free splits (37.7%
    -> 38.7%, 38.4% -> 39.6%); see §3 and `price_adaptive` in `_weights.yaml`.
    **It does not rescue this entry.** The finding there is that the gain has
    nothing to do with the eight items — they still reach zero model cores with
    the flag on. "Fixing one half of a two-half problem buys nothing" stands;
    what changed is that the efficiency half turned out to be fixing a
    different problem, in the intercept, for the whole pool.

11. **Multi-stat items as an efficiency bias (2026-08-21)** — the one entry
    here that was never implemented, because the diagnosis said there was
    nothing to fix. The symptom is real: across the 89 Conquest cores, items
    carrying 4 stats take 50.4% of the core slots off 19.5% of the buildable
    pool (2.58x) and 1-stat items take **none of 534**. `efficiency` drives
    3-4x more of it than `god_fit_score` does, on both the shipped blend and
    the meta-free `quality` one, and the fit half is already #3.

    The accusation was the regression's fixed intercept (~1111g against a
    tier-3 price that barely moves with stat count). **It is not the
    intercept, and it is not the fit.** Three measurements, in
    `efficiency.INTERCEPT_KEY` with the numbers: stat COUNT adds 0.019 of R2
    over stat MASS and is only a proxy for it; deleting the intercept nearly
    DOUBLES the residual spread it was blamed for (772g → 1398g); and the
    fit-free version — typical rolls per 1000 gold, no regression in it at all
    — is the steepest of the three, at 0.549 / 0.930 / 1.166 / 1.554 by stat
    count. A 4-stat item carries 67% more raw stat magnitude per gold and this
    model credits it 24% more. What it buys with the difference is passive:
    median passive text 259 → 105 characters over the same bands.

    **And the community makes the same trade.** Against the buildable pool the
    recommender actually picks from — the restriction matters, see below —
    Obsidian+ builds lift 4-stat items 2.18x against our 2.58x. The
    over-preference is **+7.7pp of core share, 95% CI [+2.9pp, +12.4pp]**:
    real, and roughly a fifth of what 2.58x reads as against the pool alone.

        stats/item   % pool   % community   lift   % core slots   lift
             1        7.0%         6.4%    0.91x         0.0%    0.00x
             2       34.4%        22.0%    0.64x        10.7%    0.31x
             3       39.1%        28.8%    0.74x        38.8%    0.99x
             4       19.5%        42.6%    2.18x        50.4%    2.58x

    So multi-stat items really are better value in SMITE 2 and the model is
    reading it, slightly loudly. **The over-picking framing points at the wrong
    end of the distribution.** Recall of community items by stat count is
    0.0% (0/29) at one stat, 28.0% at two, 54.2% at three, 58.2% at four —
    **42% of every missed community item is a 1- or 2-stat item**, led by Shell
    of Rebuke (missed 22x, residual +685), The Executioner (14x, +1035) and
    Odysseus' Bow (11x, +431). Those are passive items, which is #5, and three
    of the seven 1-stat tier-3 items carry Adaptive Stat power that is not in
    `stats` at all, which is #10. Anyone returning to this should go after the
    bottom of the table, not the top.

    _That advice was taken, 2026-08-21, and it half worked._ `price_adaptive`
    (§3) prices the Adaptive Stat power those three 1-stat items were missing
    and beats control on both splits — but it does not put them in cores, and
    the recall table above is unchanged in shape. The class they belong to is
    still the bottom of the distribution; what the flag fixed was the intercept
    they were inflating for everyone else.

    One trap on the way in: an unrestricted community set lifts 1-stat items
    1.90x and invites exactly the wrong conclusion. 41 of those 70 sightings
    are tier-1/2 COMPONENTS in unfinished late slots — the other half of the
    `ledger.ts` fact under `SLOT_REACH`. Restricted to items the model can
    actually pick, the 1-stat community lift is 0.91x.

12. **A clock for the damage model (2026-08-21)** — `damage_per_second`. The
    two damage paths both lacked one: `combat` implements `casts_per_second`,
    `cooldown_multiplier`, `attacks_per_second` and `attack_dps`, all
    calibrated and tested, and nothing outside `combat.py` called any of them,
    so Cooldown Rate and Attack Speed bought no modelled damage anywhere in the
    repo. With the flag on, each channel gets its own scraped clock. It is the
    only setting under which 34 Attack Speed items and 34 Cooldown Rate items
    are worth anything.

    **The criterion was set before the measurement and is not moved.** Ships ON
    only if the Carry figure improves, the roster-wide figure does not get
    worse, and `calibrate --control` is unchanged. The measure is where the
    community's own Conquest items land in the B6 damage ordering — and unlike
    §1's gate this one is not circular, because the B6 table takes **no
    community input at all**: scraped kit, item stats, combat constants.

        mean normalised rank, 0 = top      false    true
          Carry   n=108                    0.439   0.351
          Jungle  n=102                    0.264   0.296
          Mid     n=135                    0.286   0.473
          Solo    n=108                    0.720   0.723
          Support n= 78                    0.702   0.714
          ALL     n=531                    0.462   0.500

    Criterion 1 passes and by a wide margin; **criterion 2 fails**. Criterion 3
    holds exactly — 38.7% / 39.6% either way. Items the table scores at all go
    262 → 168 unscored of 531, which biases the metric *toward* per-second, and
    it loses anyway; a second metric with a different denominator agrees
    (Carry 0.650 → 0.469, ALL 0.635 → 0.644).

    **The cause is known, structural, and not a tuning failure.** A per-second
    model lets a god cast everything off cooldown AND swing at full rate in the
    same second. Nothing here has cast times, so neither channel is charged for
    the other's, and the basic attack's share of marginal power goes from a
    median 34.2% to 89.3% for a Carry — plausible — and from 11.7% to 60.5% for
    a Mid, which is not. Medusa is the clean win (Tyrfing 56 → 5, Odysseus' Bow
    and The Executioner scored at all for the first time); Scylla is the clean
    loss (Avatar's Parashu, a Strength item, becomes her top damage item —
    arithmetically correct, since SMITE 2 basic attacks scale 100% Strength for
    everyone, and wrong about a god who does not auto-attack). Fixing it needs
    a per-god casting/swinging time-share no source here can supply, and
    inventing one would put an unsourced constant in the module whose whole
    discipline is that constants carry evidence tiers. Numbers under
    `damage_per_second` in `_weights.yaml`; ships off.

    **What did ship, unconditionally, is the basic attack itself** — see §3.
    That half needed no clock and is a hole rather than a modelling choice.

    **Re-opened 2026-11-05 and still off.** The measure is now committed as
    `smite.scripts.clock_measure`, whose definition reproduces all twelve figures
    above at the commit that recorded them. Under the shipped fit, against `main`
    4130ed90 (flags-off figures, which are what `build_index` runs today, in the
    PR):

        arm                     Carry  Jungle  Mid    Solo  Support  ALL
        rotation (shipped)      0.382  0.299  0.311  0.633  0.764   0.460
        clock, everyone         0.307  0.325  0.467  0.633  0.772   0.490
        Carry only (withdrawn)  0.307  0.299  0.311  0.633  0.764   0.444
        share over 0.50 (rule)  0.370  0.301  0.311  0.632  0.764   0.457

    **No cast-time source was found.** The fight model's `interval` pair looks
    like one and is not: it is the median community Carry's attack rate and the
    median community Mid's cast rate, so two populations, community input, and
    rates rather than durations, and `side_by_side`'s own docstring says "There
    are NO cast times". Both literal readings fail criterion 2, and so does a
    per-god charge from the god's own kit at every value tried.

    **The share does not isolate Carry.** Per second it reads over half on 86 of
    95 gods, 16 of 24 Mids among them, and Jungle (90.4) and Solo (89.9) sit above
    Carry (88.8). It assumes the full uptime it would be judging, so it was
    rejected as circular. Per rotation it runs Carry 30.5, Jungle 33.3, Solo 31.8,
    Support 14.7, Mid 9.4, and mostly restates physical against magical.

    **The rule, chosen from the distribution and committed before it was
    measured (bc51077e): per-rotation share over 0.50**, where "over half" and the
    largest gap in the roster (7.2 points, Loki 45.7 to Guan Yu 52.9) coincide. It
    was not blind, since the role table was already known. It selects Xbalanque,
    Nemesis and Guan Yu and passes all three criteria, criterion 2 not by
    construction, since other roles move. But Carry's gain is one god (Xbalanque
    0.565 -> 0.335), Nemesis gets worse (0.335 -> 0.371), and three gods cannot
    carry a claim. It scores worse for Carry than the role list, so by the decision
    committed with it the clock stays off for everyone.

    **`[Carry]` was withdrawn, not refuted.** It scored better (0.307, held-out
    Carries 0.398 -> 0.310), but it was chosen after seeing the table and its
    criterion 2 passed by construction, so it has no warrant. Nothing here says the
    clock is wrong for Carries; it says this repo cannot yet say who gets it.

    **Two other cut-offs were declared up front, measured once and were ineligible.**
    Per second over 0.50: 85 of the 94 measured gods, ALL 0.475, fails. Rotation
    over 0.226, the largest gap in the body of the distribution: Carry 0.306, ALL
    0.445, passes. It is not a missed winner: it selects 47 physical gods plus Ares
    and leaves out only 2 physical gods, so it is "physical gods" under another
    name, Jungle worsens to 0.313, and of the 16 held-out gods it moves only 6
    improve.

    The clock reaches the draft overlay and nothing else: no core, no residual.

13. **Threshold-and-maximand scoring in `build_quality` (2026-08-21)** — the
    THRESHOLD half only. The maximand half shipped and is in §3; this entry is
    about the two thresholds that came with it and why they carry no verdict.

    Most roles clear a threshold and then maximise something else, so a Carry
    survival floor ("survive one enemy burst rotation") and a Mid/Jungle kill
    threshold ("rotation burst >= a reference squishy's EHP") were defined,
    given references derived from the roster rather than invented, and
    measured. **Neither separates anything.** Taken at its most generous — the
    single largest burst anywhere in the roster, read at ZERO protection — the
    Carry floor is failed by **0 of 36** builds; the kill threshold is failed
    by **78 of 78**. One threshold nobody fails and one everybody fails are
    equally useless.

    **This is a statement about our damage model's completeness, not about
    SMITE.** Read it as *we cannot currently evaluate a threshold*, never as
    *we measured this and thresholds do not matter*. The two quantities are
    not on the same scale and the reason is entirely on our side: a burst here
    is one cast of every ability at its last rank, with **no basic attacks**,
    **no item passive**, no follow-up and one target, while effective health
    is full level-20 health plus every protection six items carry. Median
    burst over own EHP across the 178 builds is 0.12.

    **What would change the answer, both already on this list.** Entry 12's
    clock: a burst window in seconds would let basic attacks into the burst,
    and it is refused for entry 12's reason — no source supplies one, and
    inventing it would make that single unsourced number the whole metric
    (~1,058 damage on a 3-second window for Medusa, more than doubling her
    burst). Or entry 5: ~90% of the pool carries passive value neither side of
    this comparison can see, and burst is where that hurts most, since
    execute, multi-hit and on-hit passives are burst and not sustain.

    So Carry, Mid and Jungle ship judged on their **maximand alone**, with the
    inert threshold left visible in the report next to its measurement rather
    than quietly dropped. `threshold_probe` re-runs it on every report and
    prints a binding threshold the moment one binds; a test drives it on data
    where the burst does reach the health bar, so "separates 0 of n" is a
    measurement that can change and not a constant. Numbers and the probe in
    `build_quality.threshold_probe`.

    **Re-measured 2026-11-05, against `main` 6fc363b2 and #110's builds.** The
    probe itself still prints 0 of 38 and 82 of 82, and it could not have moved:
    `build_quality` does not read `passive_sim` and has no window, so #107 and
    #110 reach it only through the builds. So the same two thresholds were read
    on the fight layer instead (`smite.scripts.threshold_fight`: passives
    simulated, one basic attack in the combo, same `WINDOW`, no new constant):

        threshold, attacker at zero protection        main      #110 builds
        Carry floor, roster's largest burst (4,331)   fails 36/38   fails 31/38
        Carry floor, roster's median burst (~1,800)   fails  0/38   fails  0/38
        Carry floor, any WINDOW-second run            fails 38/38   fails 38/38
        kill threshold on burst, passes               1/83          1/83
        kill threshold on WINDOW, passes              80/83         80/83

    **Still not usable, for a different reason.** The scale problem is gone:
    burst now reaches the health bar. But the floor runs from failing nobody to
    failing nearly everybody depending on which attacker it names, and the only
    attacker it binds against is one god (Scylla, on the community's build). No
    source says which attacker a Carry must survive, and choosing one is the
    unsourced constant this entry refused. It stays out of the verdict.

    **The premise that sent this back here is false: our Carries do not over-buy
    damage.** Ours over community, median of 19 Carries at the reference targets:

        main             burst      sustained vs squishy  vs tank   EHP phys / mag
        ours/community   1.21       0.89                  0.76      0.97 / 0.98
        #110 builds      1.15       0.89                  0.76      1.03 / 1.01

    Ours sustain more against a tank on **1 of 19**, on either tree. That is the
    measured shape of Carry's deficit, and #110 does not close it.

14. **`defense_affinity` / `archetype_scaled_stats` as the cause of Carry
    over-defence (2026-08-21)** — excluded mechanically, so nobody re-derives
    it. The symptom is real and is §3's row: our `model` core is tankier than
    the community's on 18 of 18 Carries while winning damage on only 12, and
    the community buys **exactly 0.0 protections on all 18**. The natural
    suspects are the two draft knobs, and neither can be it.

    **Neither reaches these builds.** `defense_affinity` is written in
    `build_index._enrich_gods` and `draft.archetype_scaled_stats` lives under
    `draft:` in `_weights.yaml`; the only reader of either is
    `viewer/src/lib/threats.ts` (`threatOverlay`). Nothing in `scoring`,
    `assemble`, `recommend` or `efficiency` imports them. The draft overlay is
    applied viewer-side **on top of a finished core**, and `build_quality`
    measures the base `model` core, so the overlay is not in the builds where
    the symptom appears. **And it would be zero anyway**: `defense_affinity`
    is `max(Physical Protection, Magical Protection)` off
    `scoring._role_stat_map`, and the Carry map names no protection — the role
    reads **0.0**, which is the value `test_defense_affinity_follows_the_role_map`
    already pins.

    **What it actually is, recorded and deliberately not acted on**:
    Berserker's Shield (2400g, 40 Physical Protection · 200 Max Health · 20%
    Attack Speed) is in **17 of our 18 Carry cores and 0 of 18 community
    ones**, with Golden Blade (200 Health) in 7 more. It is one item winning a
    slot on efficiency + fit, not a diffuse defensive tilt — and the
    protection is *physical only*, so against a magical burst it buys health
    and nothing else. Diagnosing why it wins is open work (§5) and was left to
    a session other than the one that found it. The stat table and the item
    counts re-measure on every run in `build_quality.carry_mechanism_lines`.

15. **Charging an item for stat mass the god cannot use (2026-08-22)** —
    `offmap_efficiency`. **THIS ENTRY IS NO LONGER A NULL. It ships ON at
    0.55 as of 2026-08-22** — see §3, and read the whole entry as the history
    of how it got there rather than as a reason not to try it. What unblocked
    it was §4.16's exemption growing a third stat, Health Regen; the sweep,
    the region, the alpha choice and the shipped effect are under
    `offmap_efficiency` in `_weights.yaml`, and the short version is that both
    leakage-free splits sit at or above control across 0.45–0.65 (probe
    39.1% → 44.0% at 0.55, best 40.0% → 40.0%), the Carry defect closes, and
    the other four roles give up some margin on `build_quality`'s own
    counts. Everything below was true when the flag shipped off and the
    diagnosis is unchanged. The hole is real and mechanical: `efficiency` is
    god-agnostic and prices every stat an item carries, while
    `scoring.god_fit_score` normalises over the role map alone, so a stat the
    map does not name is in neither its numerator nor its denominator. An
    off-map stat is credited by one half of `quality` and invisible to the
    other. **Verified rather than argued** — grouping all 9,541 (god, item)
    pairs by god and by identical on-map stat SET, the fit stat term is
    constant inside the group in **1174 of 1174** groups, and inside those
    classes mean r(off-map mass share, efficiency) = **+0.441**, positive in
    856 of 1110 groups and in all five roles.

    On the item it was found on it is the whole story. Berserker's Shield
    repriced against the one stat a Carry's map names, at the same 2400g:
    residual **−425g → +849g**, efficiency **0.681 → 0.210**, `quality` rank
    **1–9 → 84–126** of the pool, and it leaves all 18 Carry cores.

    **It shipped off at first because it was worse on both leakage-free splits
    at every strength**, monotonically, with the best split's paired CI
    excluding zero from 0.15 up (probe 39.1% → 34.0%, best 40.0% → 37.0% at full strength;
    churn 22 → 86 of 89 Conquest cores, 36 → 80 Joust, 20 → 86 Arena). Sweep,
    paired CIs and per-mode churn under `offmap_efficiency` in
    `_weights.yaml`.

    **At 0.0 it is an exact no-op and that is checked, not assumed** — §4.10
    is what happens when a strength is applied where nothing reads it.
    `viewer/public/index.json` regenerates BYTE-IDENTICAL with the key present
    and absent. Adding the key does move the `calibrate` input fingerprint
    (`33d6031bd9de` → `c73b6ea6bdde`), because the hash covers `_weights.yaml`
    — the control reads 5.6% / 39.1% / 40.0% at both, to the digit, so a
    fingerprint change here is the file and not the data.

    **The two gates disagree, and this is the cleanest case since entry 8.**
    `build_quality` — non-circular, `combat.py` pointed at whole builds — says
    the Carry defect is real and that this is its lever: Carry on its own
    objective goes 10 ahead / 8 behind / +7.8% to 12 / 5 / +27.3% at 0.25,
    while the effective-health surplus §4.14 recorded collapses from 17/1
    /+26.8% to 2/16/−7.7%. At 0.15 our Carry defensive profile lands level
    with the community's (−0.5%) and we win damage (+12.5%). Weigh it against
    that report's own caveat: a verdict in our favour is the one to distrust,
    and the Carry survival threshold does not bind (§4.13), so a metric that
    cannot charge us for buying **no** defence will always reward buying none.

    **The finding that outlasts the flag: off-map mass is not one thing.**
    The community's own cores carry it in every role, and mostly the same two
    stats — Max Mana and Mana Regen, 62% of the community's Carry off-map mass
    and 78% of their Mid. No role map names either. There the map is
    INCOMPLETE and the charge punishes a real want. Protections on a Carry are the
    actual defect: 55% of our Carry cores' off-map mass is Physical
    Protection, Max Health and Health Regen against **0% of the community's**,
    and Carry is the only role whose map names none of those stats (0 of 18
    gods, against 18 of 18 Solo and 14 of 14 Support). **Nothing available
    here separates the two cases** — naming which stats a role "really" wants
    is the invented constant §4.12 and §4.13 both turned on refusing, and
    reading it off the community's composition is the leakage §1 is about.
    That is why there is no carve-out here of the kind `price_adaptive` was.

    _Amended 2026-08-22 by §4.16, which carved one out anyway — as an
    exemption rather than a weight._ Two claims in this entry were wrong and
    are corrected there rather than here. **The Support/Solo attribution was
    half right:** this entry read "Support loses up to 21.4pp of coverage and
    Solo 9.4pp" as one mechanism, mana. Sparing mana and re-running the
    identical sweep moves Support's −21.4pp to −1.4pp and leaves Solo's
    −9.4pp **exactly where it was** — Solo's is Health Regen and Plating, not
    mana. **And off-map gold share does not predict coverage impact:** mana is
    24% of the gold this charge takes off a Support core and ~93% of Support's
    coverage loss, so the composition table above cannot be reasoned from to
    what a carve-out will do. The sweep itself reproduces here to the digit,
    on both splits and on all three modes' churn, which is what makes the two
    comparable. The entry's conclusion is otherwise unchanged: it still ships
    off, now for a sharper reason — see §4.16.

    Two things ruled out on the way, so nobody re-derives them. It is **not
    §4.11**: off-map share and stat count are near-orthogonal (r = +0.129),
    neither absorbs the other (partial r(share, core | count) −0.210 against a
    simple −0.175; partial r(count, core | share) +0.248 against +0.219), and
    the signs are opposite — count is positively associated with core
    membership, share negatively. It is **not §4.3**: magnitude-aware fit does
    not reorder the class that decides the Carry core, because Berserker's
    Shield's 20% Attack Speed **is** the reference magnitude.

    And the honest case against the whole framing, which the sweep does not
    settle: in that deciding class the two items the community actually buys —
    Odysseus' Bow (10 of 18) and The Executioner (13 of 18) — are the two
    carrying **zero** off-map mass, and they read **+316g and +999g
    overpriced**. That premium is the passive value §4.5 prices at zero. There
    is an unpriced quantity on both sides of this comparison: our item's
    off-map mass is free credit, theirs is a free debit. Charging one without
    pricing the other reaches the right answer for half the right reason.

    _The cost this flag imposes on Jungle was examined 2026-08-23 and is
    §4.18._ Two arms were built to pay it down and both ship off. The short
    version is that the Jungle regression is not what it looks like: across
    the 15 Jungle cores the charge moves, departures carry 42 Jungle community
    slot sightings and arrivals carry 74, and two of the three gods behind the
    14-ahead-to-12 move are swapping The Crusher and The Reaper for Titan's
    Bane.
    **On the community record the charge is already right for Jungle**, which
    is also where five of the probe split's gained gods come from.


16. **Naming Max Mana in the role maps (2026-08-22)** — `offmap_exempt`, and
    the entry is a REFUSAL to write a weight followed by a measurement of the
    thing that did not need one. §4.15's own finding was that the maps are
    incomplete: zero of the 21 `role_stats` entries names Max Mana or Mana
    Regen, while mana is the largest off-map stat by mass in the community's
    cores in every role. The obvious repair is to name it. **There is no
    number to name it with**, and that is the finding.

    **The share that motivates it is the wrong unit, by ~5× on Carry.**
    `god_fit_score` runs with `magnitude_fit` off, so its stat term reads
    PRESENCE; `offmap_efficiency` charges GOLD, off `stat_gold`. Neither
    reads mass. The community's own cores, same off-map definition, three
    units:

        role     off-map MASS mana   as GOLD   core SLOTS carrying any mana
        Carry               67.7%      15.4%     15 of 108 = 13.9%
        Jungle              74.2%      29.7%     42 of 102 = 41.2%
        Mid                 94.1%      65.3%     48 of 132 = 36.4%
        Solo                90.2%      29.6%     24 of 108 = 22.2%
        Support             84.9%      24.2%     24 of  84 = 28.6%

    The median non-zero roll is 250 Max Mana against 35 Strength, and the
    regression prices mana at 1.26 g/pt against Strength's 21.81. Mana is
    voluminous and cheap, so a mass share flatters it and neither unit the
    model actually reads agrees that it dominates anything but Mid.

    **Every leakage-free route to a weight is closed**, and they were tried in
    this order. THE KIT, which is `attack_damage_fit`'s shape and should have
    worked: ability mana costs and base stats are scraped and community-free,
    and over the 78 gods with a full kit and a mana pool they separate the
    five roles by **3pp of rotation-cost-over-pool on a quantity whose roster
    range is 16pp**, with base mana a near-constant (1006–1240, stdev 53) and
    the between-role spread narrower than Solo's own within-role IQR. The kit
    says every role has the same mana economy — an argument for a roster
    constant, against a role column. THE DAMAGE MODEL: **0 of 89 gods** have
    an ability that scales on Max Mana, and `combat.py` contains the string
    "mana" **zero times**, so `build_quality` is blind to mana and cannot
    adjudicate this either. THE ONE GAME-STATED EXCHANGE RATE, Transcendence
    and Book of Thoth, is `conversion_fit`, §4.9, refuted. And the
    intervention already had an informal measurement: the `mana-stack` flavor
    records that Max Mana at 1.2 on a fit overlay selected Genji's Guard and
    Breastplate of Valor, tank items, because mana in this pool lives on tank
    items.

    **So it shipped as an exemption instead, which needs no magnitude.**
    `offmap_exempt` names stats that are off every map and charged to nobody.
    A weight asserts "this role wants this stat, this much"; an exemption
    asserts only "this stat is a roster constant, so its absence from the maps
    is not evidence against it" — which is exactly what the kit measured.

    **Re-swept on §4.15's grid, and the two splits split.** The control column
    reproduces §4.15 to the digit on both splits and on all three modes'
    churn, which is what makes them comparable. Sparing mana, the probe split
    **reverses sign** — 39.1% → 42.3% at 0.25 and 43.1% at 1.00, monotone up,
    with the paired 95% CI EXCLUDING ZERO at 0.25, 0.75 and 1.00 — while the
    best split stays below control at every strength (40.0% → 37.9%) and its
    CI excludes zero at 0.75 and 1.00. **Two splits disagreeing about the
    direction is entry 9's shape**, so `offmap_efficiency` stays at 0.0 and
    `offmap_exempt` ships populated and therefore inert. Its inertness is
    pinned by a test and checked against a regenerated `index.json` rather
    than assumed (§4.10).

    **What the exemption bought, and what is left.** It corrects §4.15's
    Support/Solo attribution — Support's −21.4pp is mana (→ −1.4pp), Solo's
    −9.4pp is not (→ −9.4pp, unmoved) — and it does **not** cost the Carry
    correction anything: Berserker's Shield is in 17 of 18 Carry cores at
    control and **0 of 18 at alpha 0.25 with the exemption on or off**, with
    Medusa's core identical under the two at every strength. What still blocks
    the charge on the best split is Carry (−2.2pp, the role it exists to fix)
    and Solo (−9.4pp), and Solo's is **Health Regen** — 33% of the gold the
    charge removes from a Solo core, 39% from a Support one, 76.40 g/pt and
    named by no role map either. That is the next stat to examine, and this
    entry is the method for it.

    **One trap worth more than the ship decision: off-map GOLD SHARE does not
    predict coverage impact.** Mana is 24% of the gold the charge takes off a
    Support core and ~93% of Support's coverage loss. The composition table in
    §4.15 cannot be reasoned from to what a carve-out will do — measure the
    carve-out. This prediction was made from the gold share before the sweep
    and was wrong about Support.

    Numbers, the full sweep, the per-role table and the kit measurement under
    `offmap_exempt` in `_weights.yaml` and in `efficiency.offmap_gold`.

    _Health Regen joined the list, 2026-08-22, and adding a second stat forced
    the general rule._ This entry argued mana case by case; a list of one
    cannot say what a list is FOR. The rule is two mechanical tests, neither
    of which is a judgement about SMITE: **(i) no `role_stats` entry names the
    stat at all** — not "the role that wants it has no entry", none anywhere,
    because a stat named for some role and not another has a contrast, and the
    silence on the second role is then a positive statement by the same table;
    and **(ii) no instrument in this repo can price it**, since if `combat.py`
    can see it then charging it is a hypothesis `build_quality` can check and
    the honest move is to check it.

    Run over every stat the buildable pool carries, the two tests select
    **exactly three columns** — Max Mana, Mana Regen, Health Regen — and
    reject every defensive stat §4.15 named. Health Regen is named by **0 of
    the 21 `role_stats` entries and 0 of the 89 merged god maps**, against Max
    Health and Physical Protection at 6 of 21 and 36 of 89, so its absence is
    a global silence and theirs is a per-role statement. `combat.py` contains
    the string "regen" **zero times**, and Health Regen is a per-5-seconds
    RATE in a repo that refused to invent a clock (§4.12) — and the clock §4.12
    refused was a COMBAT clock, while regeneration is mostly what happens
    between fights. The scrape adds a supply-side constant: base HP5 at level
    20 spans 5.50–6.22 over 88 gods with 44 of them on exactly 5.50, and as a
    share of the health pool the five role means span 0.020pp inside a roster
    range of 0.069pp.

    **Attack Damage is the instructive row and it is why this is a last
    resort.** It is the one stat named by no role map that got a WEIGHT
    instead (§3, `attack_damage_fit`), because `damage_value.stat_weights`
    supplied a leakage-free exchange rate. So there are three outcomes, not
    two: price it if an instrument can, weight it if an exchange rate exists,
    exempt it only when neither is available.

    **Where Health Regen's case is thinner than mana's, said plainly.** Mana
    had a DEMAND measurement — ability costs are scraped, so `rot/pool` said
    what each role spends. Health regen's demand is incoming damage, which is
    positional and is not a property of any kit; reading it off a role would
    be the invented constant §4.12 and §4.13 turned on refusing. This case
    rests on the two tests and a supply-side constant, with no demand side.

    **Inert at `offmap_efficiency: 0.0`, checked and not assumed (§4.10):**
    `index.json` regenerates BYTE-IDENTICAL with the stat on the list and off
    it (sha256 `c9a2bd6847081cdb` both ways) and no build note moves. The
    `calibrate` fingerprint moves `c68c33d49845` → `e9c995b14743` because the
    hash covers `_weights.yaml`; the control reads 5.6% / 39.1% / 40.0% at
    both, to the digit. Both baselines are REGENERATED ones — the committed
    `index.json` was itself stale against the 22 Aug refresh, and comparing
    bytes against it would have reported that refresh as this key's effect.
    The membership is pinned by a test, including that no defensive stat may
    join.

    **And what it was worth: it unblocked the charge.** Re-running §4.15's own
    sweep with Health Regen spared removes the two-split disagreement that
    kept `offmap_efficiency` at 0.0 — both splits sit at or above control
    across **0.45–0.65**, a region rather than a point, and the flag shipped
    at the midpoint. §4.15 is therefore no longer a null; the sweep, the
    region, the alpha choice and the shipped effect are under
    `offmap_efficiency` in `_weights.yaml`.

    **§4.16's own prediction was right about the mechanism and this is the
    first time that has happened in this pair of entries.** It named Health
    Regen as the next stat and Solo's unmoved −9.4pp as the reason; sparing it
    moves Solo to +2.4pp on the probe split and to zero on the best one. The
    trap it recorded still stands, though — gold share did not predict the
    SIZE of any of it, only the direction.

    _Test (ii) refused its first stat on 2026-08-23, which is §4.18._ Echo
    passes test (i) — named by 0 of 21 entries and 0 of 89 merged maps, the
    same standing as mana — and is the largest single line in the charge on a
    Jungle core at 43.9%. `combat.echo_multiplier` prices it, so the rule
    demanded a check instead of an exemption; the check came back against the
    exemption. Until then the rule had only ever selected, so read §4.16 and
    §4.18 together for what test (ii) is actually for. The membership is now
    enforced against `build_quality.COMBAT_PRICED` by a test rather than by
    this paragraph.

17. **Collapsing `build_quality`'s two effective-health channels into one
    number (2026-08-23)** — a REFUSAL, in §4.16's shape, and the entry exists
    because averaging them is the obvious next "improvement" and is wrong.

    The defect it came from was real and is fixed: `build_quality`'s two
    EHP-bearing objectives — Solo's duel score and Support's effective health
    per 1000 gold — both read `ehp_physical` alone, so **the two roles whose
    job is durability were scored on half the damage in the game**, with
    `ehp_magical` computed on the same line and printed in the same tables.
    A build trading physical protection for magical read as a large loss with
    durability flat.

    **What was refused is the collapse, not the fix.** Three forms were
    considered and all three are a constant this repo cannot source:

      * the MEAN asserts equal exposure to the two damage types. It is also
        not the answer to its own question — against a stream that is a share
        `f` physical, effective health is `1 / (f/EHP_p + (1-f)/EHP_m)`, a
        weighted HARMONIC mean, because what averages over a mixed stream is
        the damage-taken multiplier and not its reciprocal. Amaterasu reads
        -9.7% arithmetic against -6.7% at the 50/50 it claims to describe.
      * the MIN asserts the mix is chosen adversarially per build, which no
        game state produces, and being no kind of mean it is not guaranteed
        to land inside the range at all.
      * a STATED MIX is the only honest scalar and nothing here supplies one.
        The roster is 46 physical gods to 43 magical, but a head count is not
        a damage share; reading the share off what the community buys against
        is the leakage §1 is about. This is §4.16's situation exactly — a
        quantity with no leakage-free exchange rate — and it takes §4.16's
        answer, which is to write no constant.

    **What made "report both" an answer rather than a punt.** The ratio
    ours-over-theirs at mix `f` is a Mobius function of `f` with no pole in
    [0, 1] and is therefore MONOTONE in it, so the interval between the two
    channels is exactly the set of values every possible damage mix can
    produce. The two channels are not two samples — they are the bounds.
    A verdict that holds at both endpoints holds at every mix; one that does
    not is not available at any price payable here. So the report counts
    ahead / behind / level / **mix-dependent**, names every mix-dependent
    build, and prints the median as an interval. Checked in a test rather
    than argued.

    **Measured on the shipped builds, and the direction is not what a reader
    of the old table would guess.** Solo goes 17 ahead / 1 behind to 17 / 0
    with Amaterasu mix-dependent (-23.5% against a physical opponent, +28.3%
    against a magical one); Support 11 / 3 to 11 / 1 with Ares and Athena
    mix-dependent (-10.4% / +15.3% and -14.3% / +11.1%). Bacchus is behind on
    both channels and stays behind. Three of 32 builds, every one of them a
    build the single channel scored as a loss — the artifact ran in exactly
    one direction, because the flag that moved these builds moved them from
    physical protection to magical.

    **How much of 08-22 E was this.** Re-run against E's own pre-change build
    notes, the single-channel column reproduces the shipped commit message to
    the digit (Solo 18/0 +69.0% -> 17/1 +53.4%, Support 14/0 +22.8% ->
    11/3 +22.8%), which is what makes the pair comparable. Per build, E's cost
    to our own maximand is worse than -10% on **10 of 18 Solos on the physical
    channel and 1 of 18 on the magical**, and on **3 of 14 Supports against 0
    of 14**; six of those 32 builds change SIGN between the channels. Solo's
    median cost is -15.6pp read on physical and -4.4pp read on magical, and
    Support's is 0.0pp against +2.0pp. **E's reported cost to Solo and Support
    was measured on the channel it moved away from and not on the channel it
    moved toward**, and every judgement made from that table since is wrong in
    that direction. **It does not reverse E**, and the register should not be
    read as saying so: under the pair, E moves no Solo or Support build from
    ahead-at-every-mix to behind-at-every-mix. Ares goes ahead to
    mix-dependent, Bacchus mix-dependent to behind — and Bacchus was already
    mix-dependent BEFORE E, which the single channel could not show.

    **What would collapse the interval to a point**: a measured damage-type
    share, per match or per role, from a source outside this repo — the
    harmonic form above is then the whole of the change and both endpoints are
    already computed. **What would falsify the bracket**: effective health
    against a mixed stream not being a weighted harmonic mean of the two
    channels, i.e. mitigation ceasing to be linear in protection per damage
    instance, which is `combat.effective_health` and is calibrated to 0.0%.
    Numbers and the derivation in `build_quality.EHP_CHANNELS`.

18. **Charging Jungle for stats its map does not name (2026-08-23)** — the
    hypothesis was "the charge is safe exactly where a role's map covers its
    damage stats". It is **confirmed as a per-god predictor and refuted as a
    mechanism**, and both arms built to act on it ship off. Measured at control
    fingerprint `527eb8f0a586` (baseline 5.8%; the shipped flag reads probe
    43.6% and best 39.4% there, against 38.7% and 39.5% at `offmap_efficiency`
    0.0).

    **Confirmed, at god level rather than role level, which is the test that
    matters.** Predictor: the share of the gold the charge bills in a god's
    control core that sits on a stat `combat.py` prices as damage. Outcome:
    that god's own role maximand measured on OUR core alone, so no community
    build enters — and where §4.17 made that maximand an interval, the scalar
    is the WORST channel, the same reduction `threshold_probe` uses, so no
    interval is averaged into a point. Over the 50 cores the charge moves,
    Spearman **−0.333**; by tercile of damage-share the median delta is
    **+8.6% / −0.5% / −3.6%** and the worse-count is **6 of 16 → 9 of 17 →
    13 of 17**. Restricted to the three roles whose objective §4.17 did not
    touch (Carry, Mid, Jungle, 35 moved cores) it is **−0.396**, with medians
    **+17.5% / +11.8% / −4.8%** and the top tercile worse on **12 of 12**.

    _First measured 2026-08-23 at fingerprint `c454186bff12` and re-measured
    at `527eb8f0a586` after the day's refresh landed; the correlation was
    −0.529 on the earlier data. It is a tendency across 89 gods, not a
    constant, and quoting either figure without its fingerprint is the
    mistake §1 warns about._

    **Refuted on all three cases the hypothesis was built from.**

    * *Mid is not spared by map coverage.* Its off-map bill is **88.3%
      Lifesteal**, which no Mid map names either. Mid is spared because only 2
      of 22 Mid cores move at all — its cores carry the least off-map gold of
      any role, 5,239g over 22 gods against Jungle's 20,906g over 17.
    * *Jungle's bill is not the five stats named.* It is **43.9% Echo** — a
      stat named by 0 of 21 `role_stats` entries and 0 of 89 merged god maps,
      the same standing as mana. Attack Speed is 16.5%, Lifesteal 16.5%, Max
      Health 11.8%, Physical Protection 8.4%; **Critical Chance and Cooldown
      Rate are billed nothing at all.**
    * *Susano's swap is not the off-map stat.* Tekko-Kagi leaves because its
      Attack Speed is billed 418g of 2700g, dropping it 0.488 → 0.409 under
      Pendulum Blade's 0.422. Jungle's maximand is `burst_70/1000g` and a
      burst here counts **no basic attacks** (§4.13), so that Attack Speed was
      worth **exactly 0.0** to the number that reports the loss. What he lost
      is 5 Strength, flat penetration for percentage, and +50g of denominator.

    **And the finding that reverses the premise: on Jungle the charge moves
    cores TOWARD the community record.** Across the 15 Jungle cores it moves,
    departures carry **42** Jungle community slot sightings and arrivals carry
    **74** — The Crusher (2 of 102 Jungle slots) and The Reaper (6) out,
    Titan's Bane (14) and Hydra's Lament (9) in. The `build_quality` drop 14
    ahead/2 behind → 12/5 is **three gods**: Da Ji and Tsukuyomi leave
    `ahead` and Pele goes from level to behind, and **two of the three are
    that exact swap** (8 sightings out, 15 in, each). That is also why the
    probe split rises 38.7% → 43.6%, with five of the gained gods Jungle.

    **Arm 1, `offmap_exempt` gains Echo — refused, and it is the first time
    §4.16's test (ii) has done work.** Echo passes test (i) outright. It fails
    (ii): `combat.echo_multiplier` prices it off a DOCUMENTED share, so the
    rule says check the charge rather than exempt it. Checked:

        arm (alpha 0.55)     probe 0.70   best 0.45   C/J/A churn   Jungle
        control 0.00              38.7%       39.5%     0/ 0/ 0   14a/2b +14.9%
        shipped, Echo billed      43.6%       39.4%    50/48/54   12a/5b +10.3%
        Echo exempt               42.3%       39.2%    50/29/53   14a/2b +15.0%

    It restores Jungle exactly and holds the Carry guard (Berserker's Shield 0
    of 18), and it comes back **against** the exemption for a nameable reason:
    every one of the 7 gods whose coverage moves loses a **community** item to
    an Echo item — The Crusher into six of them, taking Titan's Bane out three
    times, and Damaru into the seventh. The community is not blind to Echo —
    16 of its 537 slots take an Echo item — it buys them for Mid (7) and
    Support (6) and essentially never for Jungle (2 of 102) or Carry (0).
    There **is** information about who wants Echo; it is simply not in
    `role_stats`, and reading it off the
    community's composition is the leakage §1 is about. The methodological
    half is worth as much: Echo's only effect anywhere in the model is the
    multiplier on exactly the ability damage Jungle's maximand sums, so
    sparing its charge **cannot fail** to raise that number. Test (ii) exists
    so the check happens anyway, and the check is worth something only because
    a second, non-circular measure can disagree with it. Here it did.

    **Arm 2, per-role `offmap_efficiency` — the best-performing arm, and
    refused anyway.** Jungle at 0.0 with every other role at 0.55 reads probe
    **42.8%**, best split **39.5%** — the only arm that leaves that split
    exactly at control — Jungle back to 14a/2b +14.9%, Carry untouched at
    12a/5b +28.2%. Three reasons, in order of weight.
    (1) **What it buys is Da Ji and Pele losing Titan's Bane** and getting The
    Crusher and The Reaper back — it is better by an arithmetic that cannot
    count basic attacks and worse by the community's own record. (2) A
    per-role strength is five constants with no source, chosen from the gate
    they improve; §4.12 and §4.13 both turned on refusing exactly that, and it
    costs 0.8pp of the 4.9pp the leakage-free measure gained. (3) **The
    mechanism is not per-role.** Each role's bill is a different stat, and
    inside Jungle the damage share of the bill spans 0.21 to 1.00 across gods;
    one number per role cannot express a per-stat fact.

    **Two things seen in passing and deliberately not acted on.** First, on
    this data the shipped flag reads **39.4% against control's 39.5%** on the
    best split — the "at or above control on both splits" property that chose
    0.55 (§4.15) is now 0.1pp negative there. That is less than one item on
    one god (0.19pp at 89 gods) and it moved with the refresh rather than with
    anything here, so it is reported and not treated as a change; §4.15's
    region is what would have to be re-swept, and that is a different change
    with a different argument. Second, **Plating is the largest untested
    column left** — 39.9% of the bill on a Solo core and 63.2% on a Support
    one, named by no role map and apparently priced by
    `combat.flat_reduction_multiplier`, so it looked eligible for exactly the
    check Echo just failed. _Run 2026-08-23, and it is §4.19: the check cannot
    be run at all — `flat_reduction_multiplier` applies to the TARGET and
    nothing reads Plating off the build being judged — and sparing it moves 0
    of 89 Conquest cores while moving 48 Joust and Arena ones._

    **So nothing shipped, and the composition now re-measures.**
    `build_quality`'s "Where the off-map charge lands" section prints the bill
    per role and per stat with each stat's standing under the two tests beside
    it, because every attempt on this charge so far — §4.15 for the defect
    stats, §4.16 for mana and Health Regen, this one for Echo — has rebuilt
    that table by hand against a dataset that had moved under the last one.
    `scoring.fit_map` is now the single place the merged map is built, so the
    diagnostic asks the same map `score_god_items` scores with rather than
    keeping a second opinion, and `test_no_exempted_stat_may_be_one_combat_can_price`
    enforces test (ii) against `build_quality.COMBAT_PRICED` instead of
    leaving it as a sentence in a comment.

    **The extraction is an exact no-op, checked the way §4.16 says to.**
    `viewer/public/index.json` REGENERATED under the parent commit's code and
    under this one's is byte-identical, sha256 `fed0820b5545`. A diff against
    the *committed* `index.json` is not that check and would have failed:
    the committed file is itself stale against the same day's refresh, which
    is the trap §4.16 recorded and the second time it has been walked into.

    **What this leaves for the next session, and it is a WEIGHT rather than an
    exemption.** `attack_damage_fit` gives 78 of 89 merged maps an Attack
    Damage column, measured from the god's own basic-attack scaling, while
    Attack Speed reaches only 35 of 89 — and the two are the multiplicands of
    the same basic attack. The model therefore credits a god for one half of
    its basic attack and charges it for the other, which is what removed
    Tekko-Kagi from six Jungle cores. An exchange rate for it is available and
    leakage-free the way mana's never was: `combat.attack_dps` states how the
    two combine, and both terms are scraped. That is §4.16's third outcome —
    price it, weight it, or exempt it — and this is the first stat since
    Attack Damage with a real claim on the second.

19. **Exempting Plating and Dampening (2026-08-23)** — §4.18 named Plating as
    the largest untested column; this is that test and its twin, run one after
    the other and kept as one entry because they are one finding with two
    instances. Both are nulls, and this is the first entry where **the check
    test (ii) demands cannot be run at all**. Measured at control fingerprint
    `527eb8f0a586` (baseline 5.8%).

    **Test (i) passes, and it is the strongest fact here.** Plating is named by
    **0 of 21** `role_stats` entries and **0 of 89** merged god maps — the same
    standing as mana and Health Regen, and unlike the defensive stats §4.15
    named. Seven buildable items carry it, 41.02 g/pt, and it is **39.9% of the
    bill on a control Solo core and 63.2% on a Support one**; on the cores the
    charge actually ships it is 93.1% and 100% of what is left.

    **Test (ii) was recorded wrong in §4.16, and the correction is the point.**
    That entry's table reads "Plating / Dampening — priced by
    `plating_multiplier`", which is reading a function signature rather than an
    instrument. `combat.damage_dealt` does take `plating=` and `dampening=` and
    apply them — **to the target**. Nothing in the package ever supplies either
    (an AST walk over every module now pins that), `build_quality`'s own
    assumption line has always said its reference targets carry "no Plating or
    Dampening", and on the buyer's side there is no expression for it at all:
    `effective_health` is `health × (1 + protection/100)` and has no term for a
    flat damage-type reduction. **A build's own Plating is worth exactly 0.0 to
    every number this report prints**, so charging it is not a hypothesis
    `build_quality` can check in either direction. `TARGET_SIDE_ONLY` names the
    pair and two tests hold it.

    **Run indirectly anyway — through the items it moves — and the answer is a
    Conquest no-op.** Sparing Plating at the shipped 0.55 moves **0 of 89**
    Conquest cores. Coverage is identical to the digit on both leakage-free
    splits (43.61% probe, 39.42% best, against the shipped flag's own 43.61%
    and 39.42%), every role's verdict is unchanged including Solo's
    17a/0b/1mix and Support's 11a/1b/1mix, and the Carry guard is untouched
    (Berserker's Shield 0 of 18, Golden Blade 5 of 18).

    **The whole of its effect is in the two modes with no gate.** Joust 17 of
    89 cores and Arena 31 of 89 — and **every arrival is a Plating item**,
    Spectral Armor 13 + 31 and Kinetic Cuirass 4 + 1, with **zero Plating
    departures**. What leaves is Void Stone (28 Arena cores), Stygian Anchor,
    Void Shield and Shifter's Shield. The borrowed Conquest record, which is a
    consistency check and not validation, is unchanged to the item: Joust 153
    of 537 both ways, Arena 129 of 537 both ways. So this is a monotone "buy
    more Plating" push across **178 of 267 build groups**, argued for by
    nothing and refuted by nothing, which is the worst shape a change can have
    here — §5 already says those two modes rest on nothing measurable.

    **And the Conquest zero does not rest on the margin — it rests on the
    assembler**, which is the correction the Dampening pass forced and the most
    reusable thing in this entry. The exemption's push is a constant per item
    (+0.039, +0.078 or +0.117 of `efficiency` for a 5-, 10- or 15-point roll,
    at most **+0.082 of `quality`**), and comparing it against each god's own
    gap — the worst item in the core minus the best Plating item outside it —
    the slack is **NEGATIVE on 8 Support gods** and the cores still do not
    move. Read all the way down on Atlas: the exemption lifts Shield of the
    Phoenix from **rank 11 to rank 6**, above Genji's Guard and Breastplate of
    Valor, both of which ARE in the core, and it still does not enter. The
    guard is `max_lifesteal`: Shield of the Phoenix carries the `sustain` tag,
    Atlas's cap is 1, and Amanita Charm spent it at rank 1 (§3, "`max_lifesteal`
    is a sustain cap and the name is the only thing saying otherwise").

    **So `quality` rank does not decide core membership, and a margin argument
    on it cannot show that a change is safe.** That is worth more than either
    stat's verdict: the obvious way to check "would this move anything" is to
    compare a score delta against a score gap, and on 8 of 89 gods here that
    comparison says yes while the assembler says no. Rebuild the cores. At
    alpha 1.00 seven Conquest cores do move, so the zero is a fact about this
    strength and this pool, not a property of the charge.

    **It corrects §4.16, and by the same mechanism §4.16 itself warned about.**
    That entry attributed Solo's −9.4pp to "Health Regen and Plating", read off
    the gold share. Health Regen was right — sparing it moved Solo to +2.4pp on
    the probe split. Plating is worth **exactly zero** coverage on either
    split. That is the second time off-map gold share has mispredicted a
    carve-out (Support's mana was the first), and §4.16's own line — *the
    composition table cannot be reasoned from to what a carve-out will do,
    measure the carve-out* — is now carrying two confirmations and no
    counter-example.

    **DAMPENING, the twin, run the same way and answered harder.** Test (i)
    passes identically — 0 of 21 `role_stats` entries, 0 of 89 merged maps —
    and test (ii) fails the same way, `DAMPENING_CAP` and
    `flat_reduction_multiplier` applying to the target and to nothing else.
    Six buildable carriers at 35.67 g/pt, and **one community slot in 537**
    (Shogun's Ofuda, on a Solo). What separates it from Plating is that the
    charge on it is already vacuous where it can be measured: **no Dampening
    item reaches a Conquest core on any of the 89 gods, in either archetype,
    at either strength**, so the stat is billed **0 gold** in every Conquest
    core at control and at 0.55 alike. Exempting it moves **0 of 89 Conquest
    cores, 0 of 89 Arena, and 1 of 89 Joust** — Hua Mulan swapping Shield
    Splitter for Shogun's Ofuda, and her overlap with her own borrowed record
    is 0 of 6 either way. Coverage is identical to the digit on both splits,
    every role verdict is unchanged, and borrowed Joust coverage is 153 of 537
    both ways.

    **And its margin is clean where Plating's was not**, which is the contrast
    that makes the pair worth keeping together. The push is +0.0338 or +0.1014
    of `efficiency` (5 or 15 points) against a smallest slack of **+0.0109**
    (Ymir), median +0.1577, and **0 gods of 89 with slack ≤ 0**. Dampening's
    Conquest zero really is a margin fact; Plating's is the assembler's. Two
    stats that look identical on both mechanical tests are held out of the
    cores by two different things, and only one of them would survive a
    reordering of the pool.

    **Where they do reach a build is the two ungated modes**, and the entry
    should not be read as "these stats never matter": Dampening items hold 7
    core slots in Joust and Arena at control, the charge takes Joust to 6, and
    the exemption puts that one back. Plating's exemption moves 48 cores
    there. Everything either exemption would buy is in the 178 of 267 build
    groups with no gate.

    **What would make this answerable, and it is a `EHP_CHANNELS` change.**
    `effective_health` needs a buyer-side flat-reduction term before any
    instrument here can weigh Plating or Dampening. Plating reduces Attacks and
    Dampening reduces Abilities, so that is an attack-vs-ability split of the
    same shape as the physical-vs-magical one §4.17 just made — and composing
    the two makes the durability figure a two-dimensional interval rather than
    a pair. Whoever does it should read §4.17 first: the argument for reporting
    the interval instead of collapsing it is the same argument, and it gets
    harder, not easier, with four corners.

20. **The passive catalogue (2026-09-02)** — a REFUSAL in §4.16's shape,
    applied to nine classes of passive at once, and the entry exists so that
    "price the passives" stops being re-attempted per item. The whole
    argument is `docs/PASSIVES.md`; the data is `data/_passive_classes.yaml`,
    every buildable item's passive classified by the SHAPE of its value and
    held to the pool by `test_passive_catalogue.py`. Measured at fingerprint
    `208b8d329f8e` (baseline 5.7%, probe 40.9%, best 37.6%).

    **The problem it starts from is the one `build_quality` prints on every
    run**: 137 of 138 buildable items carry passive text, the shipped flags
    read 13, `combat.py` reads one, and 75% of the community's slots sit on
    the other 124. §4.5 is the broad attempt and is refuted; three narrow
    carve-outs of the same idea shipped on. Nobody had said what the 124 ARE.

    **Twenty classes in five families**, by three questions a passive has to
    answer yes to before a price can be written without a constant: is the
    value a CURRENCY the model prices (a column, or a `combat.py` quantity
    with a documented exchange rate into one); is its UPTIME one, or stated
    by the text or the build; does any REFERENCE it needs come from item
    data, the kit or combat constants and not from the community. Family A
    is a priced stat in prose (27 items), B a combat quantity with an
    exchange rate (29), C a currency gated by an uptime no source supplies
    (64), D value whose recipient is not the scored god (9), E no currency
    (8). Plus a fourth condition on the PRICE rather than the passive: a
    converted magnitude outside the range a column was fitted on is an
    extrapolation — Yogi's Necklace is exactly Health Regen, and at 60 HP5
    against a column fitted on 2–6 the linear price says 4,600 gold for a
    2,250-gold item.

    **The hypothesis this session was handed — "a carve-out works when the
    passive converts into a stat the model already prices" — is confirmed as
    a filter and refuted as a predictor.** All three shipped flags are A1,
    A2, B1, and family E has never produced a priceable item. But 33 items
    with a priced-currency clause sit in family C: Berserker's Shield
    converts into three priced stats and cannot be priced, because a health
    state gates it. What the three shipped flags share and the hypothesis
    does not name is that the quantity is UNCONDITIONAL and the exchange rate
    was measured, documented or read off the item's own text. Under the
    conjunction, roughly twenty of the 124 are reachable today and about a
    hundred need a primitive this repo has refused (§4.12's clock, a stated
    mix) or lacks (an attacker, allies, a healing model).

    **What is refused, and it is nine classes, each the same refusal as an
    existing entry applied to a class.** C1 health-state (36 community slots)
    needs time-below-threshold, no source; C2 self-trigger is the clock; C3
    enemy-trigger (75 slots — Freya's Tears and Genji's Guard, the two
    most-bought blind items) is the attacker's behaviour, of which a build
    score contains none, which is §4.17's argument; C4 outcome-trigger fires
    on kills, so any rate for it is §1's leakage; C5 cooldown-gated is the
    clock stated plainly and is the LARGEST class in the pool, 32 primary
    and 46 carriers; C6 is §4.8; D1 ally-directed has no allies in a per-god
    score (the draft does, and a tag bonus there is not a price); D2
    enemy-debuff needs the attacker's build or a healing model, and
    `build_quality` has neither, so a charge could not even be checked; E is
    a game-state change with no damage or effective-health expression, and
    the tag axis is already the instrument for it.

    **Three findings worth more than the classification.** (i) `price_passives`
    beyond the thirteen priced items reaches nine tier-2 components,
    Dominance and Shogun's Ofuda, and prices the adaptive clause as its own
    column — §4.5 refutes that configuration, and is barely evidence about
    unconditional grants on buildable items. (ii) The model OVER-BUYS the
    families it cannot price: C-primary items hold 376 of our 540 Conquest
    slots against 229 of the community's 543, because their stat lines are
    discounted for a passive the model then ignores — C1's mean residual is
    −81 and every A/B class is positive. (iii) The three hard cases all have
    a place. Genie's Lamp and Shell of Rebuke are A2, the "% of all Stats"
    multiplier, exact against a POOL-derived five-item reference (557 gold at
    7.5%, most of Shell's +740 residual; the Lamp's problem is then its
    missing price, not its value). The Executioner's shred is B3:
    `effective_protection` already implements the reduction terms, one stack
    is a 214-gold floor against the 70-protection reference, and what defeats
    the additive model is the stack RAMP, an uptime, not the shred.

    **Proposed and not built**: `price_stat_multipliers`, A2's four relics
    and the Lamp, against the pool reference rather than `conversion_reference`
    (which is community-derived, a leak inside a shipped flag that the
    catalogue names and the next carve-out must not repeat). Predictions are
    written before the sweep in `docs/PASSIVES.md` §6.

21. **`price_stat_multipliers` (2026-09-02)** — the carve-out §4.20 proposed,
    built exactly as proposed, default OFF, and it ships OFF: **the falsifier
    written into the commit before the sweep fired.** Numbers, the paired CIs,
    the churn and the role verdicts are under `price_stat_multipliers` in
    `_weights.yaml`; the design is in `passives.multiplier_grants`. Measured
    at control fingerprint `f00ab519045f` (baseline 5.7%, probe 40.9%, best
    37.6%).

    The four residual predictions held to within 50 gold each (Shell of
    Rebuke +740 → +224 against a predicted ~+205). The one prediction that
    mattered was the falsifier: Shell is the only one of the four relics with
    a community record, so coverage could move only through Shell. **Shell
    enters zero cores** — 0 of 90 in every mode with the flag on, as with it
    off — and coverage moved anyway: probe 40.9% → 40.1% (−0.83pp,
    [−3.11, +1.22], 7 better / 8 worse), best 37.6% → 37.5% (−0.19pp,
    [−0.93, +0.48]), with 40 of 90 Conquest model cores, 29 Joust and 50
    Arena changing. Every one of those cores changed without a relic
    entering or leaving it.

    **By the rule the commit set, that is reported and not explained.** What
    is recorded beside it, as measurement only: the regression intercept
    reads 934 with the flag off and 854 on, Strength 21.81 → 22.87 g/pt, and
    the Conquest churn is Genji's Guard, Breastplate of Valor and
    Transcendence arriving against Pendulum Blade, Shield Splitter and
    Shifter's Shield leaving. The Carry guard holds (Berserker's Shield 0 of
    18 either way); `build_quality`'s verdicts are unmoved for Carry, Jungle
    and Mid and give up one god each on Solo and Support. Diagnosing why four
    items that reach no core move forty cores is the next session's work and
    is in §5, deliberately not this entry's.

    Two things the catalogue said that the sweep confirms without touching
    the ship decision: the A2 exchange rate is exact (the residuals landed
    where the pool reference said they would), and a `priced` claim in
    `data/_passive_classes.yaml` is refused by its test until a flag actually
    ships — the four relics stay unpriced there because the flag is off.

22. **`price_on_hit` (2026-09-02)** — the catalogue's second carve-out (class
    B1, flat unconditional on-hit damage priced as Attack Damage on the same
    hit), built as proposed, default OFF, and it ships OFF as a plain null.
    Numbers, paired CIs, churn and verdicts under `price_on_hit` in
    `_weights.yaml`; the design and the survey in `passives.on_hit_grants`.
    Measured at control fingerprint `8da1ada3e67c` (5.7% / 40.9% / 37.6%).

    **The extraction is right and the falsifier did not fire.** Three items
    carry the clause (Tyrfing +15, Bragi's Harp +10, Golden Blade +10; a
    test pins that no fourth item and no component does). The residual
    predictions held to within 75 gold and the refit behaved as written
    beforehand (Attack Damage 21.95 → 20.31 g/pt, intercept unmoved). Unlike
    §4.21, the cores that moved moved BECAUSE of the priced items — 28 of 35
    Conquest model cores by one of the three entering, nothing leaving.

    **And coverage fell on both splits** — probe 40.9% → 39.6% (−1.30pp,
    [−3.28, +0.56], 5 better / 9 worse), best 37.6% → 37.0% (−0.63pp,
    [−1.52, +0.22]) — because the items enter cores on gods whose players do
    not buy them there. Tyrfing enters 17 cores and is in the community
    record on 3 (Cupid, Izanami, Medusa); Golden Blade enters 8, in the
    record on none; Bragi's Harp enters 7, in the record on one (Nut). The
    community holds Tyrfing on 13 gods; with the flag on we hold it on 29.
    That is §4.5's sentence reproduced on a clean three-item subset, with
    the cause now visible: a correct PRICE is god-agnostic, and WHERE the
    cheaper item lands is the fit map's call — `attack_damage_fit` credits
    Attack Damage on 78 of 89 gods whether or not the god auto-attacks, the
    same shape as §4.12's Scylla buying Avatar's Parashu.

    **So the lesson generalises past this flag**: for the attack channel, a
    pricing carve-out cannot ship alone. It needs the fit side to know which
    gods swing — a per-god basic-attack share the kit does not state and
    §4.12 refused to invent — or it will put every on-hit item on every god
    with an Attack Damage column. Golden Blade in Carry cores going 5 → 8
    (Berserker's Shield stays at 0 of 18) is the same mechanism seen from
    §4.14's side.

23. **The community-derived constant inside a shipped pricing flag
    (2026-09-03)** — the seventh entry that is not "we measured this and it is
    false". Nothing was implemented and nothing shipped off: this is an audit
    of a leak that is real, and the answer is that it costs about **−2.6pp of
    LEVEL on the probe split and −0.6pp at eff 0.45, and changes no verdict in
    this register.** Read it before quoting any absolute leakage-free figure
    dated on or after 2026-08-14, and before "fixing" `conversion_reference`.

    **The leak.** `passives.measure_conversion_reference` builds
    `{stat: median total}` by iterating community build entries and skipping
    everything else. That constant is stamped into `_weights.yaml` as
    `conversion_reference`, read by `efficiency.item_stat_values` and
    `assemble.conversion_args`, and feeds `price_conversions`, which SHIPS ON.
    `calibrate` zeroes the `win` and `pick` SIGNALS and does nothing about it,
    so community-derived information reaches `efficiency` inside the
    measurement that exists to be free of it. It has been true since
    `7d025f4` (2026-08-14), where the key and the flag landed together;
    `validate` and `calibrate` have applied pricing flags since `fa22fd0`
    (2026-08-10), so there is no window where the flag was configured but
    unmeasured.

    **The magnitude.** Measured at fingerprint `208b8d329f8e`, exact
    random-core baseline 5.7427%, against three community-free references that
    bracket the community one — the pool mean over the 134 tier-3 buildables
    ×6 (A), the same over carriers only (B), and per-item own + pool mean ×5
    (C). At the shipped `conversion_passes: 3`, with the paired per-god
    bootstrap:

        arm                    probe 0.70:0.30      best 0.45:0.55
        community (shipped)      40.9%                37.6%
        A pool mean ×6           38.4%  −2.59pp       37.0%  −0.63pp
                                 [−4.83, −0.50]       [−1.48, +0.00]
        B carriers ×6            39.2%  −1.76pp       37.0%  −0.63pp
        C per item               38.5%                37.0%
        price_conversions OFF    37.7%                31.6%

    Only the probe interval excludes zero. Item-level the move is much larger
    than the coverage move — Rod of Tahuti's residual −916 → −258, Nimble Ring
    −319 → +25 and out of the `undervalued` band — so this is not a change too
    small to see; it is a change the coverage measure is nearly indifferent to.
    Full tables under `conversion_reference` in `_weights.yaml`.

    **The flag still earns its place, on the same standard.** Against
    `price_conversions` OFF, at the shipped pass count: community +3.24pp
    (CI spans zero) / +6.02pp (excludes zero, 27 gods better 2 worse); pool A
    +0.65pp (spans zero) / +5.39pp (excludes zero, 24/2); pool B +1.48pp /
    +5.39pp. Same verdict on all three — unresolvable at the probe corner,
    clearly positive at the split §1 calls the leakage-free optimum. **The
    community-derived constant is not what is carrying the flag.**

    **Why it is smaller than its shape suggests**, both measured. (1) The
    community value is not a peak: scaling the reference, 1.25× scores 41.2%
    on the probe and 1.50× scores 38.3% on the best split, both above the
    shipped 1.0×. A constant tuned by the target would sit at the maximum.
    (2) It does not track the record — nothing in production calls
    `measure_conversion_reference`, so the number is a hand stamp from
    2026-08-14. The record has drifted 3.1% under it (Intelligence re-derives
    to **335** today against the committed 325) and that drift costs **0.00pp
    on both splits and moves 0 of 90 gods**. And C, the per-item pool
    reference, recovers the community's 500 from item data alone —
    Transcendence 446, Book of Thoth 546. The community median is not carrying
    information the item pool does not already have, which is the mechanism
    under every number above.

    **Blast radius — one caveat, not twelve.** Every leakage-free coverage
    figure measured on or after 2026-08-14 quotes a LEVEL carrying this: §4.2's
    re-measure, §4.9, §4.10's re-measure and its `price_adaptive` carve-out,
    §4.11–§4.19, the `_weights.yaml` evidence blocks dated in that window
    (`price_adaptive`, `attack_damage_fit`, `blend_stat_values`, `cap_overflow`,
    `offmap_efficiency`, `damage_per_second`, `conversion_passes`), §7's
    Leakage-free row, and `_calibration.md`. **None of their verdicts is
    affected**, because each is a delta between two arms with this constant
    held identical on both. What is overstated is the headline multiple: ~7.1×
    chance at the probe corner is ~6.7× with a community-free reference.
    Interaction is not ruled out for the four that touch the same two stats or
    the same four items — **§4.9** (`conversion_fit`, the fit half of this
    exact mechanism, whose verdict rests on two splits moving in opposite
    directions), **§4.16** (whose refusal to price Max Mana cites §4.9),
    **§4.15/§4.18** (`offmap_efficiency` charges stats off a role map, and both
    reference stats are off several), and **`conversion_passes`** itself, whose
    1/2/3/4 table was measured against this constant and which demonstrably
    interacts with it: pool A is the BEST arm on the probe split at one pass
    (41.6%) and the worst at three (38.4%). Those four are the ones to re-run
    first if the constant is ever changed. Listed, not re-run and not amended.

    **Nothing here recommends turning `price_conversions` off**, and nothing
    here changes a value. The value in `_weights.yaml` is deliberately left
    stale: re-stamping 325 → 335 measures identically and would move the input
    fingerprint, invalidating every control quoted against `208b8d329f8e` for
    no gain. The open question — whether `calibrate` should neutralise
    community-derived CONSTANTS the way it zeroes community-derived SIGNALS —
    is answered "it cannot" in `calibrate.py`'s docstring: a signal has a zero
    and a constant does not, emptying this key is the opposite of neutral in
    the assembly half, and the only real neutralisation is substituting a
    different constant, which is a model change and belongs in `_weights.yaml`.
    §5 carries what to do instead.

24. **Borrowing Conquest's slot record to ORDER Joust and Arena builds
    (2026-09-02)** — a REFUSAL, in §4.16's shape, and it is here because it is
    the obvious next move the moment someone reads the report: the positional
    buy order improves Conquest and leaves **180 of 270 build groups exactly
    as they were**, and the machinery to borrow already exists and is already
    used. Measured at control fingerprint `208b8d329f8e` (baseline 5.7%, probe
    40.9%, best 37.6%).

    **The gap it would close is real and is measured.** Scored against
    Conquest's record — which is what a borrower would be asserting — the
    Joust `core` builds run 47 of 201 orderable pairs backwards (23.4%) and
    Arena 36 of 175 (20.6%), against Conquest's own 68 of 380 (17.9%) before
    the change and 40 (10.5%) after. Feeding those modes the borrowed
    positions takes Joust to 34 (16.9%) and Arena to 28 (16.0%). So the
    intervention works in the only sense this repo can check, and it still
    ships off.

    **Why. The precedent that looks like permission is about a different
    question.** `borrow_community` lets the Hybrid take Conquest's record for
    item CHOICE, minus tags that do not transfer, disclosed as borrowed
    (§3). A slot centroid is not a claim about which item — it is a claim
    about WHEN a power spike lands, and both modes deliberately zero `win` and
    `pick` on the grounds that Conquest's rates describe a different game.
    Timing is MORE mode-specific than choice, not less: `modes.arena.economy`
    is 1250 start gold and 15 gold/sec spooling from 0:00 against Conquest's
    back-loaded Titan, which is the same fact `time_value_multiplier` already
    prices — the two modes disagree about when an item is worth buying, in
    this file, with sources. Borrowing the centroid would assert the opposite
    of a constant the repo already carries.

    **And nothing could catch it. Both blindnesses are measured here, not
    argued.** With 337 of 810 Conquest suggested builds reordered,
    `calibrate --control` reads **40.9% / 37.6% against 40.9% / 37.6%**, to the
    digit on both leakage-free splits, and BOTH committed reports REGENERATE
    byte-identical except for their own input-fingerprint line:
    `_build_quality.md` keeps every count, every median and every role verdict,
    and `_calibration.md` — the full ~7-minute run, the whole grid and both
    bootstrap CIs — keeps every number in it. The fingerprint moves because
    it hashes `_weights.yaml` and a key was added there; that is the file, and
    the two reports agreeing to the digit is what says so. §1's gate reads
    membership; `build_quality` scores a finished six-item build at level 20,
    and the same six items at level 20 are the same numbers whatever sequence
    bought them. The only measurement is agreement
    with the community record, and in a borrowed mode that measurement is
    scored against the very record it was ordered by — circular twice over,
    since the record is not even that mode's. This is §4.19's shape exactly:
    "a monotone push across 178 of 267 build groups, argued for by nothing and
    refuted by nothing, which is the worst shape a change can have here."

    **What ships instead is the honest degradation.** `slot_positions` reads
    the note for the mode being built, Joust and Arena notes carry no
    community entry, so `build_order` receives `{}` and returns the heuristic
    — no mode special-case, no flag. The god page's existing disclosure for
    those modes ("no outcome data exists for {mode} … read this as a shortlist
    rather than a buy order") is left TRUE rather than being worked around,
    and `community_ordered` is absent on all 180 groups rather than empty, so
    the page can tell "no evidence" from "not stamped".

    **The measurement's own limits, stated once so they are not rediscovered.**
    `order_agreement` reports agreement with observed play and NOT outcomes,
    and its headline count is scored against the same `slot_order` block
    `build_order` now reads. The one non-circular reading available is the
    held-out split — order on the community's top pick at each slot, score
    against the ALTERNATES that ordering never saw — and it moves 49 of 278
    inversions (17.6%) to 41 (14.7%), monotonically across the sweep, which is
    what put `community_weight` at 1.0 rather than the in-sample table. It is
    a weak check: both halves come from one scrape of one set of matches, so
    they are not independent samples. It is also the only one there is, and
    saying so is the point of the entry.

    **Membership does not move, and that was checked rather than assumed.**
    `build_order` receives an already-assembled core, so per-mode core churn
    is **0 / 0 / 0** over all 2,433 suggested entries with 337 of 810 Conquest
    entries reordered and 0 of 811 Joust and 0 of 812 Arena. Both baselines
    are REGENERATED (§4.16's trap, walked into twice before): the committed
    notes were already stale against the same day's data by 13 rounding-only
    `fit` values, which reproduce under the parent commit's own code.

25. **Why four items that reach no core move forty cores (2026-09-03)** —
    §4.21's open question, answered. **The churn is not the regression refit,
    and it is not assembly. It is that `efficiency_scores` min-max normalises
    the residual pool, so the efficiency signal's SCALE is set by two items,
    and `price_stat_multipliers` reprices one of them.** A DIAGNOSIS: no flag
    moved, no shipped value changed. Re-measured at control fingerprint
    `edaa4af3cdc5` (baseline 5.7%, probe 40.9%, best 37.6%), unchanged at the
    end. Reproduce with `python -m smite.scripts.refit_decomposition`; the
    mechanism is in `efficiency.efficiency_scores`' docstring.

    **It reproduces, and three of §4.21's integers do not.** At 2340ea14, and
    identically at §4.21's own commit `254a7270` and fingerprint
    `f00ab519045f`, the flag moves **39 of 90 Conquest model cores, 32 Joust
    and 52 Arena** (36 / 32 / 52 for `core`), against the recorded 40 / 29 / 50
    (38 `core`). The coverage half of §4.21 reproduces exactly: probe
    40.9074% → 40.0370%, **7 better / 8 worse**; best 37.6111% → 37.4259%,
    **−0.19pp, 1 better / 2 worse** — the recorded god counts and the recorded
    best-split delta, to the digit. The harness is pinned: with the flag off it
    reproduces all **270 shipped build groups** in `data/builds/`, `model` and
    `core`, exactly, and `recommend.build_suggested_entries` itself gives the
    same 39 / 32 / 52. So the phenomenon is real and larger than recorded on
    two modes; the three integers are a counting difference in the original
    sweep that nothing here can recover. **§4.21's verdict is untouched** — the
    falsifier still fires, and this entry is why it fired.

    **The decomposition.** The flag has exactly two inputs downstream: the
    fitted gold table (global) and the five items' own stat lines (local).
    Every residual is `cost - intercept - Σ price·stat`, so an item the flag
    does not price can only move through the table. Run each half alone:

        arm      what is held                     Conquest  Joust  Arena
        ON       both move                              39     32     52
        REFIT    fit ON prices, flag-off stat lines     20      8     15
        LOCAL    flag-on stat lines, fit OFF prices     36     28     54
        NORM     nothing but hi/lo/span/mean/std        32     22     47

    **LOCAL moves no item's residual, no item's price and no item's efficiency
    rank — 0 of 187 rank moves — and still moves 36 / 28 / 54 cores.** Its
    entire effect on those 187 items is `score = 1.2259 * score_off − 0.2259`,
    to a maximum deviation of 4.4e-16. That is machine epsilon: it is not
    approximately a rescale, it is a rescale.

    **A rescale of `score` is a weight change, exactly.** `signal_score` is
    linear in it and an additive constant cannot reorder, so gain `a` moves the
    efficiency:fit ratio from `w_eff` to `a·w_eff`. Verified end to end rather
    than argued: LOCAL and "flag OFF, `signals.efficiency` × 1.2259" produce
    **identical coverage at both splits, 40.4815% and 37.4259%**.

    **Where the scale comes from, and why the top of it is soft.** `hi` is
    Agility Greaves in every arm, and `hi == 2500 − intercept` exactly (1566.47
    off, 1646.13 at the ON intercept). Its one printed stat is `Movement Speed:
    5`, the only carrier in the pool, so `MIN_STAT_CARRIERS` drops the column
    and the fit sees an all-zero row — its residual is its cost against the
    intercept, which `efficiency_pool` already calls "not a measurement of
    anything" when it excludes statless items. Agility Greaves is not statless,
    so it slips that rule and sets the pool maximum. `lo` is Heroism, a real
    stat line, both ways. **So `hi` tracks the intercept**, and any flag that
    moves the intercept reweights this signal for every god.

    **Coverage, by channel.** At the best split the refit contributes exactly
    zero (37.6111%, unmoved to four decimals) and LOCAL, NORM and ON all land
    on the same 37.4259%: the whole move is the rescale. At the probe split
    ON is −0.87pp, NORM −0.39, LOCAL −0.43, REFIT −0.28 — overlapping, not
    additive, and the rescale is the larger half.

    **What it is not.** Not the convergence loop: at `conversion_passes: 1` the
    flag still moves 38 / 30 / 44, so `assemble_core_converged` amplifies by at
    most 1 / 2 / 8 and causes none of it. Not new regression columns: 20 either
    way. Not the relics winning slots: **0 of 270 build groups hold any of the
    five in any arm**, `model` or `core`.

    **The register carries this.** Any flag that moves the intercept or moves
    an extreme residual reweights `efficiency` against `fit` for every god, so
    a carve-out's coverage delta is never purely the items it prices. §4.15,
    §4.16, §4.21 and §4.22 all state deltas measured this way, and so do the
    three flags that SHIPPED ON. §4.22 is the reassuring case and shows what to
    look for — its intercept is unmoved and 28 of its 35 moved cores move by a
    priced item entering — but it is reassuring by inspection, not by
    construction. **Nothing here says any of those verdicts is wrong**; it says
    the attribution sentence in each is weaker than it reads, and that the
    cheap check is the one this entry ran: does the arm move an extreme
    residual or the intercept, and does the churn survive holding the
    normaliser fixed.

    **Not fixed here, and the fix is not obvious.** A scale-free efficiency
    signal (rank, or a robust spread) would re-base every number in §4 at once
    and is its own session with its own control. Whoever takes it should also
    decide whether an item the fit sees as an all-zero row belongs in the
    scored pool at all — that is `efficiency_pool`'s statless rule with one
    carrier instead of none, and it is what puts Agility Greaves at the top of
    the scale.

26. **Discounting an item with no community record (2026-09-03)** —
    `unknown_win_shrink`, shipped **OFF** at 0.0.

    **LEAD WITH THIS, BECAUSE IT STANDS WHATEVER SHIPS: the only non-circular
    gate this project has is structurally blind to a defect that decides 28% of
    Conquest core slots.** `calibrate` evaluates at `win: 0.0` — that is what
    makes it leakage-free — so `scoring.god_unknown_win_rate` is multiplied by
    zero inside it. Demonstrated rather than argued: run `calibrate.control`
    with the placeholder at the god's median, at the god's floor, at **0.0** and
    at **1.0**, and coverage is **40.9074% and 37.6111% in all four arms**,
    identical to four decimal places at both splits. Only the 200-draw baseline
    moves (5.70 / 5.64 / 5.73 / 5.79%), which is CLAUDE.md rule 5's documented
    ±0.15pp reshuffle and not data. **A 0.0pp reading on the splits is not
    evidence of harmlessness here; it is the gate declining to answer.** This is
    the same shape as §4.23 — "leakage-free" is a claim about the four signals
    and about nothing else — arriving from the other side: §4.23 found a
    community-derived number the measure cannot neutralise, this finds a model
    decision the measure cannot see.

    **The defect, at control `edaa4af3cdc5`.** Of the **582** Conquest `core`
    slots, **236 (40.5%)** are held by an item with no measured win rate, and
    **163 of those (69%) — 82 of 97 cores, 75 of 90 gods** — go to an item that
    HAS a record the moment the placeholder can no longer outrank a measurement.
    The stand-in sits a median **0.147** above its god's own worst measured
    rate, worth up to **0.221** of `total` against the 0.0057 margin the Ymir
    case turned on. Joust and Arena zero the `win` weight, so all **1164** of
    their slots are unmeasured and **not one moves at any setting** — this is
    Conquest-only, and the 80% figure over all three modes is not the defect.
    The harness reproduces all **291** shipped `core` build groups exactly with
    the flag off, and reproduces 09-02 C's independent **236 of 582** display
    count; `pick == 0.00` and `win is None` agree on **12,423 of 12,423**
    buildable god/item pairs, so the two absences are one absence.

    **THE PROPOSED FIX CANNOT BE BUILT TO ITS OWN BAR, AND THE REASON IS
    ARITHMETIC.** The bar is that absence must become NEUTRAL, not punished —
    §4.16's rule, that absence from a map is not evidence against a stat, run
    on an item instead of a stat. But `total` is additive and the stand-in is
    ONE number, so it necessarily outranks every measured item below it and
    loses to every one above it. "Cannot outrank a measurement" is satisfied
    only at `p <= min(measured)`, which IS "loses to every measurement". **The
    two rules the bar distinguishes are the same rule for a scalar**, and only
    the first is defensible. A pairwise rule would separate them, and
    `assemble_core` cannot consume one — it needs a total order.

    **The sweep confirms there is nowhere to hide.** Cores changed run **41 /
    62 / 72 / 82 of 97** at shrink 0.25 / 0.50 / 0.75 / 1.00, displacing 57 /
    97 / 129 / 163 slots. Monotone, no plateau, no overlapping CIs to shelter
    in — unlike the efficiency:fit band in §1 there is no "the choice within it
    is not measurable" to fall back on, because every setting is a different
    answer and nothing ranks them. That is §4.16's refusal, measured.

    **`build_quality` CAN see it, and says the builds get worse.** It never
    reads `win`. Head-to-head at shrink 1.0 against the shipped core, on the 76
    gods whose base Conquest core moves, **with no community reference in the
    comparison at all**:

        metric          n   better  worse  level     p25   median     p75
        dps_70         76      32     42      2   -13.1%    -3.9%   +7.5%
        dps_170        76      31     42      3   -15.6%    -5.0%   +8.5%
        burst_70       75      21     44     10    -7.6%    -2.4%   +1.6%
        ehp_physical   76      14     22     40    -4.5%    +0.0%   +0.0%
        ehp_magical    76      20     18     38    +0.0%    +0.0%   +1.5%
        gold                                              +150g median

    Less damage, no effective health bought with it, and 150g more spent. Every
    role's verdict against the community degrades on its own objective — Carry
    median +20.2% → +12.1%, Jungle +7.7% → +2.8%, **Mid 17 ahead / 5 behind →
    12 / 8**, Solo +40.3%/+30.9% → +31.3%/+26.8%, Support +23.3%/+16.5% →
    +13.0%/+10.2%. At **0.25**, the mildest setting that clears the expert gate,
    it is already 14 / 22 on DPS and 8 / 23 on burst.

    **Read that with the module's own bias, which runs the other way.** A
    verdict in OUR favour is the one to distrust (~90% of the pool carries
    passive value the arithmetic cannot see), and §4.13 says it cannot charge us
    for buying too LITTLE defence. Both make this measurement a FLOOR on the
    cost rather than a ceiling. Biased with a known direction is what was
    available, and the direction is against the change.

    **TWO GATES DO MOVE AND BOTH MOVE FOR DISQUALIFYING REASONS.**
    `expert_review` goes **partial → clear** at every setting from 0.25 up:
    Eye of Providence leaves Ymir's core and the checker reads `absent from all
    36 Conquest cores in scope`. That is the claim clearing — and it is the
    coincidence the file's own header warns about, because the rule that removes
    the item removes every unmeasured item's ability to compete, which is the
    163 slots. `validate.compute` reads coverage **53% → 60%** and win-weighted
    **55% → 62%** at shrink 0.25, because demoting unmeasured items promotes
    community-recorded ones and that is precisely what coverage counts. **A
    coverage rise here is evidence against the change, not for it** (§1).

    **What is left standing.** The median is not merely defensible, it is the
    least-committal point available: the maximum-entropy estimate for an item
    drawn from this god's distribution, and the only value that makes "we did
    not measure this" mean neither good nor bad. The docstring's units argument
    was right and this entry does not touch it. **The defect is therefore not
    the placeholder's LOCATION but the weight it is entered at** — 0.45, with no
    uncertainty term, against measurements carrying real evidence. §5 already
    calls that weight "the largest single unexamined number in the model"; this
    entry adds that it cannot be examined either, for the same reason.

    **Not the efficiency rescale of §4.25.** This change never reaches
    `efficiency_scores`; `lo` (−1336.2), `hi` (+1566.5), `span` (2902.7) and all
    187 item scores are bit-identical at every shrink setting (fingerprint
    `61f5025baa3b`). None of the churn is a reweighting of efficiency against
    fit.

    **Reproduce.** `unknown_win_shrink` in `_weights.yaml`; the numbers and the
    argument are in `scoring.god_unknown_win_rate`'s docstring. The flag at 0.0
    is a byte no-op end to end — `recommend --all` and `build_index` reproduce
    every build note, every Analysis report and `index.json` unchanged.

27. **Adjudicating a ward-economy item with combat arithmetic (2026-09-03)** —
    `build_quality --ward-economy`. **The section SHIPS; its answer is a
    refusal, and a verdict it also refuses to hide.**

    §4.26 left candidate 3 of `_expert_reviews.yaml`'s recommendation list as
    the only one standing: point `build_quality` — which never reads `win` and
    has never seen a community build — at the claim "Eye of Providence is
    overvalued because it's assuming you'll get the gold from it". This is that.

    **What it measures.** 56 paired cores (28 Conquest, 28 Joust; 27 Support,
    23 Solo, 6 Mid): the same god's shipped `core`, read from `data/builds/`,
    against the core the model builds with the `ward-economy` tag_bonus
    neutralised. They differ by one item. Eye of Providence is the only carrier
    that ever reaches a core — **Eye of Erebus reads +576g residual, premium,
    and holds zero slots in either arm**, so one of the two tagged items is
    inert and the section says so on every run.

    **The ward core is cheaper on 55 of 56 pairs, median −250g**, and that
    discount is both the thing under objection and the denominator of every
    per-gold figure:

        metric          absolute (ahead/behind, median)   per 1000g
        dps_70                 0 / 30   −1.7%              26 / 28   −0.5%
        burst_70               0 /  8   +0.0% (46 level)   42 /  8   +1.5%
        ehp_physical          41 /  4   +5.7%              52 /  4   +7.6%
        ehp_magical           42 /  4   +6.8%              51 /  2   +8.6%

    Every metric moves toward the ward item once divided by gold. Burst goes
    from 0 ahead to 42.

    **THE VERDICT, RECORDED BECAUSE IT IS THE ANSWER THE INSTRUMENT GAVE.** On
    each role's own objective the ward item is neutral to positive — Support
    **+7.2%**, Solo +0.1% / +0.4%, Mid +1.2%. Priced in gold, a Support core
    would need it to cost a median **+1,063g** (physical) / **+1,060g**
    (magical) MORE before it stopped preferring it. On this arithmetic the
    reviewer's item is not overvalued and **does not need the ward gold to win
    at all**. That is the opposite of what the claim predicts and it is not
    buried.

    **TWO INDEPENDENT REASONS THE VERDICT DOES NOT SETTLE THE CLAIM.**

    *One: nothing here is independent of the printed cost.* `efficiency` is
    `cost − predicted_cost`; every per-1000g figure divides by the core's cost.
    The ward subsidy IS that price — 30/30 protections + 250 health for 2300g
    against a fitted 2550g stat line, which `_tags.yaml` already calls "a 250g
    bargain that is really the ward economy's price tag". So this module
    reading "good stats per gold" **inherits the discount rather than checking
    it**. The claim is about whether a conditional gold stream is collected in
    real games, and that is observed nowhere in this repo. `combat.py` being
    community-blind made it the right instrument to reach for and does not make
    it independent of the price.

    *Two: the objective is won by this shape of item by construction.*
    Support's maximand is `ehp_*/1000g` — no damage term, and §4.13 records both
    of this module's thresholds as inert, so nothing bounds it. A cheap
    protections-and-health brick wins it necessarily, and the **1.7% DPS the
    swap gives away is invisible to the metric scoring it**. The +7.2% is a fact
    about `ROLE_OBJECTIVES` as much as about the item. This is §4.17's warning
    arriving from the other direction: there it was refusing to collapse two
    channels into one number, here it is refusing to read one channel as the
    whole answer.

    So the section prints the absolute reading beside the per-gold one and
    refuses to average or drop either, and a test
    (`test_ward_economy_reports_both_readings_because_they_disagree`) fails if
    a later tidy-up keeps one table.

    **NOT A VERDICT ON THE −0.25, DELIBERATELY OUT OF SCOPE.** The counterfactual
    arm neutralises the tag_bonus because that is the only way to make a core
    holding the item exist; that is the definition of "what does this tag do",
    not a proposal about its size. One consequence is worth stating once and
    not acting on: the penalty was sized against the leakage-free gate, which
    §2 says measures conventionality and never "better", and on the instrument
    that can say better **it costs the 27 Support cores it touches about 7%
    effective health per 1000 gold**. That is a price, not a refutation — the
    penalty may still be right, and nothing here can say.

    **Implementation notes worth not rediscovering.** The shipped arm is READ
    from `data/builds/` with `suggested_core`, the same way `compare` reads it,
    so the build being defended is the one that ships; only the counterfactual
    arm is assembled. What makes them comparable is
    `test_rebuild_core_reproduces_every_shipped_core`, which requires the
    builder to reproduce all 180 Conquest/Joust shipped cores exactly **with
    the pricing flags applied the way `recommend.main --all` applies them** —
    skip that and the harness silently scores a different, unshipped model,
    which is the reproduction trap `_expert_reviews.yaml` already records.
    Swapping the shipped arm from rebuilt to note-read changed no figure, which
    is independent evidence the two agree.

    **Behind a flag, not in the default report**: it builds every core a second
    time (~20s, against ~4s for the whole default run) and answers a question
    about two items rather than about the roster. Arena is excluded because
    `modes.arena.excluded_items` drops both carriers outright, so no pair
    exists there.

28. **The `hybrid` archetype is outside the penetration cap charge
    (2026-09-07)** — a DEFECT, and a measured refusal to close it the obvious
    way. Nothing here shipped; the §7 Cap overflow row is left reading **1**
    with this beside it, because a row that reads 1 with a reason is worth more
    than a row that reads 0 because someone typed it.

    **The offender.** `doc_audit` read `-> 1 of 2479 builds over the
    penetration cap` for the first time. It is Morgan Le Fay, Conquest,
    archetype `hybrid`, aspect overlay *Aspect of the Cursed Crown*:
    `Penetration %` totals **45.0 against a `stat_caps` cap of 40** —
    Gluttonous Grimoire 10, Spear of the Magus 10, Rod of Tahuti 5, Obsidian
    Shard 20.

    **Three candidate causes, and it is the third.** The flag has not stopped
    firing (`cap_overflow: 1.0`, live). The penalty is not too small to
    displace Obsidian Shard's 20 points. **The penalty is never computed for
    this build at all**, because the `hybrid` archetype is assembled somewhere
    the charge was never wired into. `recommend._build_entry_set` passes
    `**assemble.overflow_args(...)` on both of its `assemble_core_converged`
    calls, covering `core`, all eleven flavors and `model` — and it is called
    twice, bare and with the aspect overlay, so **aspect builds consult the cap
    exactly as base builds do**. `hybrid.hybrid_core` does not go through it:
    it calls `assemble.assemble_core` directly with only `n`, `max_lifesteal`,
    `stat_caps` and `coherence_args`. No `cap_overflow`, and no `conversion` or
    `economy` either.

    **The measurement that says "hybrid" and not "aspect".** Adding the charge
    to that one call and rebuilding all 89 gods × 3 modes changes **69 cores,
    every one of them `hybrid`**. Zero cores of any other archetype move. The
    aspect is incidental — it is what makes a swap fire for this god at all,
    since Morgan Le Fay's bare entry set emits no hybrid — and all 73 hybrid
    entries are unguarded, 61 bare and 12 aspect.

    **It has been wrong since the flag shipped, not since this refresh.**
    `cap_overflow` landed 2026-08-21 (`285dbb4`); the `hybrid_core` assembly
    call last moved 2026-08-20 (`114edbb`) and has not changed. The `hybrid`
    archetype has never consulted the cap. The recorded `47 -> 29 -> 0` counts
    were honest counts over all suggested builds; what was never true is the
    implication that the guard covered the set they were counted over.

    **WHY IT SURFACED NOW, AND IT RETIRES THE ROW'S OWN STANDING PUZZLE.** The
    §7 Cap overflow row used to say the suggested-build count fell while the
    community sample grew and that "this file does not have a mechanism for it
    on record". There is one. Non-hybrid suggested entries are **exactly 2,406
    at every commit checked** from 2026-08-29 to today (`d65efdf`, `af04139`,
    `e910b75`, `522456a`, `0e28d47`, `a54a124`, `ea3b5e7`, `2340ea1`,
    `68744e5`, `0e5d8f1`, `f8e4174`, `d5ead22`, HEAD). Every movement in that
    denominator is hybrid emission, because an entry whose swaps do not survive
    is not emitted — 13 / 19 / 23 / 27 / 48 / 27 / 61 / 68 / 73 across the same
    commits. **2,433 -> 2,479 is 27 -> 73 hybrids and nothing else.** The
    unguarded population nearly tripled in six days as the community window
    deepened, and one of them crossed the cap.

    **WHY THE ONE-LINE FIX IS NOT ONE, AND THIS IS THE PART TO READ BEFORE
    TRYING IT.** `coherence` ships at 0.0, so `coherence_args` returns `{}` and
    the `hybrid_core` call satisfies `not coherence and not economy and not
    conversion and not cap_overflow` — it takes `assemble_core`'s **walk
    path**, which consumes rows in the order handed to it. `hybrid_core` builds
    that order deliberately, accepted community picks first, and it is the only
    mechanism that makes a swap stick. Passing `cap_overflow` flips the same
    call to the **re-rank path**, where the constructed order survives only as
    a tie-break and the swap is re-adjudicated on score. Measured over all 89
    gods × 3 modes:

        arm                          entries   hybrid entries   cores changed
        shipped                        2,479         73             —
        + cap charge in hybrid         2,426         20             69

    Over-cap goes 1 -> 0 and **53 of 73 hybrid builds stop existing**. That is
    not a price this session was scoped to pay, and it is not a price the
    penetration cap is worth on its own evidence.

    **A second hazard underneath it.** The re-rank path reads `score_key`,
    default `"total"`, and `hybrid_core` is handed `model_rows` — sorted by
    `quality`. `assemble_core`'s own comment records this exact trap for the
    `model` archetype: turning re-ranking on without settling `score_key` puts
    `win` and `pick` back into a build built to be free of them. Any closure
    has to decide both at once.

    **What a session that closes it must decide** — with its own control, per
    CLAUDE.md rule 5 — is a charge that prices the waste without re-adjudicating
    the swaps (charge the fill but not the accepted picks; or charge the choice
    of DISPLACED item rather than the choice of added one), or an explicit,
    measured acceptance that swaps get re-adjudicated. Not a plumbing change.
    Retuning `cap_overflow`'s strength is a third thing again and is not
    indicated: 1.0 is the principled value (`_weights.yaml`), and the charge is
    not firing here at any strength.

    **Guard.** `test_hybrid.py::test_an_accepted_swap_survives_reassembly_however_low_the_model_rates_it`
    pins the ordering invariant and fails on exactly this trade, so the 73 ->
    20 cannot be made silently.

    **Also unwired, and deliberately out of scope**: `analysis.py`'s
    disagreement report omits the charge too, but it writes
    `Analysis/_disagreements.md` and no build, so no shipped number depends on
    it.

29. **An expert-review baseline that cleared on a refresh, and did not clear
    for the reason it looks like (2026-09-07)** — a record correction, and the
    one kind of finding this register exists to stop being lost.

    The `item-overweighted` claim (Eye of Providence, `support-solo` scope) is
    recorded `resolved` with `last_verdict: partial`. The checker now reads
    `absent from all 36 Conquest cores in scope`, so the baseline was stale and
    `test_the_shipped_register_baselines_match_what_the_checker_says_today`
    was right to fail. It is raised to `clear`.

    **The reason matters more than the verdict, and it is not the one the
    shape suggests.** §4.26's `unknown_win_shrink` would also have cleared this
    claim, at every setting from 0.25 up, by demoting unmeasured items on
    `win`. That is NOT what happened. On Ymir today the placeholder still sits
    above the measured rate it is compared against — Eye of Providence
    unmeasured at Ymir's median 0.575 and scoring 0.5442, Genji's Guard
    measured at 0.52 and scoring 0.5290 — and the gap the `win` term opens is
    now 0.0248 against a 0.0152 margin, where 09-01 recorded 0.018 against
    0.0057. **The mechanism §4.26 names is wider than when it was diagnosed,
    not repaired.** The claim cleared because Kinetic Cuirass entered Ymir's
    core on the 09-04 refresh and Eye of Providence fell off the end — and
    Kinetic Cuirass has no community record for Ymir either. An unmeasured item
    displaced an unmeasured item; nothing carrying evidence took the slot.

    Full evidence, including the third instance of §4.26's mechanism it turned
    up — an item *promoted by losing its record*, worth +0.030 of `total`, and
    measured as NOT sufficient to explain the clear — is in the dated 09-07
    note in `data/_expert_reviews.yaml`, next to the claim it is about.

    **§4.26 IS NOT RE-OPENED.** `unknown_win_shrink` ships OFF at 0.0 and stays
    there. One line of its ledger changes: `expert_review` going partial ->
    clear was one of the two gates that moved for the flag, and that reason is
    now gone outright, because the claim is clear without it. The verdict is
    unaffected — it never rested on that gate — and the two passages in
    `_expert_reviews.yaml` asserting the verdict "stays `partial`" are marked
    false in place rather than edited away, because what they claimed and when
    is the record.

30. **Carry's withheld side-by-side verdicts are a refusal meeting a build,
    not unfinished simulation work (2026-11-04).** The brief was to raise
    simulated-passive coverage so Conquest verdicts stop being withheld,
    Carry first: 3 of 18 readable, target 10. It cannot be done by simulating
    passives, and the reason is structural rather than a matter of effort.

    **Every blocker on every withheld Carry god is an explicitly REFUSED
    passive.** Measured over `viewer/public/side_by_side/*.json`: of the 16
    withheld Carry gods, 15 are blocked by **Tekko-Kagi** and 1 (Jing Wei) by
    **Musashi's Dual Swords**. Refused blockers 16, absent-from-`passive_sim`
    blockers **0**. There is no legitimate simulation work available for the
    role at all.

    **Both are pure movement.** Tekko-Kagi's whole passive text is "Ability
    Used: Gain a stack of Momentum. Momentum grants +7% Pathfinding for 8s.
    Stacks up to 3 times." — no damage, no protection, no stat the comparison
    reads. Its 40 Strength / 20% Attack Speed / 10 Penetration are STATS and
    are already counted; only the passive is unsimulated, and `passive_sim`
    refuses it under `("no movement",)`, which is correct under that module's
    own rule in capitals: NEVER INVENT A VALUE. Simulating it means inventing
    a movement term inside a comparison that has no movement.

    **And the gap, not the floor, is what binds.** `coverage_min` 0.5 is
    nowhere near active: the withheld Carry gods read 82-84% on Ichor's side
    against **100%** on the community's. One unsimulated item in a six-item
    build is a ~17% gap against a `COVERAGE_GAP` of 0.14, which is itself
    DERIVED (`BAND / (6 x 5.8%)`) and not a dial.

    **A one-sided simulation makes things worse, measured.** Simulating
    Tekko-Kagi alone would close 16 Carry gaps and BREAK three Jungle verdicts
    that are currently readable only because both sides are equally ignorant:
    Kali (Ichor 83% / community 82%, gap 0%), Susano (83/84, 1%) and Nemesis
    (83/85, 2%). Lifting one side takes them to 18%, 16% and 15%. Their
    community-side blockers are Hastened Fatalis, Runeforged Hammer and
    Magi's Cloak -- all three also refused, for movement and crowd control.

    **What is actually left is 14 items ABSENT from `passive_sim`**, worth
    Jungle 5, Support 4, Mid 4 and Solo 1 blocker-occurrences and nothing for
    Carry: Ashwhorl / Briskberry / Thistlethorn Acorn, Chandra's Grace, Gem of
    Focus, Leviathan's Hide, Lotus Sickle, Mystical Mail, Omen Drum, Prophetic
    Cloak, Shogun's Ofuda, The Cosmic Horror, Totem of Death, Umbral Link.
    That work is real and does not touch this entry's conclusion.

    **So the decision is a design one and is Jacob's.** Carry is unreadable
    under this comparison as designed, and no amount of passive work changes
    it. The levers are all out of scope here and were all forbidden by the
    brief for good reasons: give the comparison a movement dimension, compare
    the shipped `core` instead of `model`, accept a sample that is not
    role-balanced, or accept Carry verdicts at a wider gap. Nothing was
    shipped; the threshold was not touched.

    One lead this surfaced and did not act on: Tekko-Kagi is in 27 of Ichor's
    builds (15 Carry, 8 Jungle) and the community's Carry builds never hold
    it. An item whose only passive is unpriced looking cheap to the gold model
    is the §4.5 family, and that is a scoring question, not a coverage one.

    **What is left of the movement lever, measured 2026-11-05**
    (`smite.scripts.movement_bound`). #110 does most of what it would have done:

        Tekko-Kagi in Conquest builds     main     #110
        `model`, Carry                   15/19     8/19
        `model`, all roles                  27       11
        `core`, Carry                    11/19     1/19
        `core`, all roles                   17        3
        community, all roles                 0        0

    As an UPPER BOUND on #110's pages, if every movement refusal counted as
    simulated: about 24 coverage gates open and 4 close (approximate: 3 of ~188
    builds read 0.15+ off the page's own share), Carry 9 opened of which 6 read
    (2 Ichor better, 4 trade-off, 3 level). That bound values movement at nothing;
    it only stops the rule withholding, which is a loosening of the measurement
    rather than a movement dimension. A real dimension still needs a value no
    source here supplies. Not built.

31. **Ichor over-buys Tekko-Kagi, and the hypothesis for why was wrong in
    its direction (2026-11-04).** §4.30's closing lead was that an item whose
    only passive is unpriced should look CHEAP to a gold-value model. It does
    not. It looks CORRECT, and every rival looks expensive.

    **The proposed mechanism is dead.** `passive_sim` is imported by exactly
    two modules, `model_audit` and `side_by_side` — both diagnostics.
    `scoring`, `efficiency`, `assemble` and `recommend` never import it, so a
    `NOT_SIMULATED` verdict cannot reach the code that decides what enters a
    core. "Refused" is not being read as "no information" anywhere in scoring,
    because scoring cannot see the refusal at all.

    **The decomposition, on the 10 Carry gods whose Conquest `core` holds it.**
    Tekko-Kagi reads efficiency **0.553** on every one (the signal is
    god-agnostic), fit 0.53-0.64, pick **0.000**, total 0.509-0.550. It wins on
    EFFICIENCY, and it wins it while paying a real pick penalty.

    **CORRECTION 2026-11-05: THE RESIDUALS BELOW ARE FROM THE WRONG FIT.** They
    were read from a bare `efficiency_scores` call with every pricing flag off,
    not the fit that builds the cores. With the flags on, as shipped:

        Tekko-Kagi -25.3 fair        Silverbranch Bow +75.2 fair
        Deathbringer +204.6 fair     Dominance +226.8 premium
        Riptalon +246.1 premium      Dagger of Frenzy +490.2 premium
        The Executioner +566.1 premium    Devourer's Gauntlet +629.9 premium

    The conclusion survives: Tekko-Kagi is fair and what it beats is marked up.
    The scale does not: read about +75 to +630, not "400-1000". The later claim
    that excluding Tekko-Kagi perturbs the scale (Jotunn's -275.8 -> -363.0,
    Deathbringer +527.3 -> +204.6) is **withdrawn**: that difference is flags off
    against flags on, and has nothing to do with the exclusion or with §4.25.
    The held-out measurements in this entry ran with the flags on and stand.

    **Its residual is -4.3 and its tier is `fair`.** 2650 gold buys 2650 gold
    of stats; the weak passive makes it look like nothing in particular. What
    is anomalous is the field it beats, priced against Medusa's community core:

        Tekko-Kagi             -4.3   fair          passive NOT simulated
        Silverbranch Bow      -10.5   fair          passive simulated
        Riptalon              +34.4   fair          passive simulated
        Dominance             +69.2   fair          passive simulated
        Dagger of Frenzy     +404.9   premium       passive simulated
        Devourer's Gauntlet  +513.9   premium       passive simulated
        Deathbringer         +527.3   premium       passive simulated
        The Executioner     +1021.8   premium       passive simulated

    **So the asymmetry runs the other way: the community's items are marked up
    400-1000 gold for passives `efficiency` cannot price, and Tekko-Kagi wins
    by being the one item with nothing to mark up.** That is §4.5 and the
    Berserker's Shield story (§4.15-§4.16) arriving on Carry.

    **And the two instruments have opposite blindnesses.** `efficiency`
    CHOOSES the items and prices stats only. `passive_sim` JUDGES the build and
    simulates all of it — Executioner's 7% shred, Deathbringer's +35% crit
    damage, Devourer's 75 stacks, Dagger of Frenzy's active, Riptalon,
    Silverbranch, Dominance are every one `simulated`, and Tekko-Kagi's is the
    only one that is not. The chooser is blind to exactly what the judge can
    see, which is the whole shape of Carry losing 12 of 18.

    **It is an error, not a disagreement — measured.** Excluding Tekko-Kagi
    from Conquest moves `validate --check` win-weighted 0.51 -> 0.52 and
    `model_audit heldout` **+0.0107 tuning / +0.0082 held-out**, better on the
    leakage-free split it cannot game, and the freed slots fill with
    Jotunn's Revenge, Tyrfing, Silverbranch Bow, Dominance, Riptalon and
    Deathbringer — all passive-simulated, several of them the community's own
    picks. The model is better off without it and moves toward the community.

    **NOTHING WAS SHIPPED, and the obvious fix is refused.** `excluded_items`
    means "the item is not in this mode's shop"; Tekko-Kagi is in Conquest's
    shop, so using that field to drop it would encode a false statement to buy
    a better number. It also treats the symptom: the same markup promotes
    whichever correctly-priced passive-less item is next. Note too that the
    exclusion perturbs the efficiency scale itself (Jotunn's -275.8 -> -363.0,
    Deathbringer +527.3 -> +204.6), which is §4.25.

    **Costed options, all Jacob's call.** (a) Feed `passive_sim`'s per-item
    simulated values into `efficiency` — the principled fix, and NOT what
    §4.20 refuses, since that entry refuses pricing passives by CLASS and this
    is per-item arithmetic the project already computes. Large: it re-bases
    every residual and therefore every §4 delta (§4.25). (b) Give movement a
    value, which makes Tekko-Kagi's 2650 legitimate rather than removing it —
    one of the four Carry levers from §4.30 and still unpicked. (c) Accept the
    disagreement and leave it.

32. **Option (a) built: pricing passives in `efficiency`. ON in PR #110,
    which is held unmerged for review (2026-11-05).**

    §4.31 diagnosed it: `efficiency` chooses on stats alone while `passive_sim`
    judges the finished build, so the chooser is blind to what the judge sees.
    #107 closed coverage (193 of 193 scored items decided), so it is built
    here as `price_passive_sim`. Baseline for every figure: `main` 6c34a58d.
    Re-verified identical after merging `main` 6fc363b2 (#112, labels only).
    Page tables below count all 94 pages; 7 read `aspect not simulated`, so
    `_meta.json` reports the same numerators over 87 judged.

    **THE DESIGN INVENTS NOTHING.** Three columns join the regression:
    Passive Damage (the four DAMAGE_KEYS averaged) and the two effective-health
    channels KEPT APART, because §4.17 refuses to collapse them. NNLS learns
    their gold price the way it learns every stat price: **0.9697 gold per
    point of simulated damage, 0.1597 for physical effective health, 0.0000
    for magical** (driven to zero: no signal). Intercept 932.5 -> 891.0.
    `side_by_side` still FEEDS NOTHING (§4.4): the simulator exports to
    `data/_passive_values.yaml` (`python -m smite.scripts.passive_values
    --write`) and `efficiency` reads the data.

    **THE REFERENCE CONTEXT.** A per-item value is the MEDIAN over up to 30
    builds holding the item (ours and the community's, all modes, sampled
    evenly and deterministically) against the median-Mid and median-Support
    reference targets, and the spread is written beside it. Of 76 valued
    items, 33 sit inside 1.5x, 17 at 1.5-2x, 5 at 2-3x, 4 at 3-5x and 12 above
    5x (Chronos' Pendant 22.5x). Deathbringer is 1.6x over 87 builds, not the
    3.0x it read over 5 shipped cores. Nine measured negative in some build and
    are clamped at zero. 54 items are `refused` (explicit zero, reason kept),
    31 have no passive, 32 are `no-context`.

    **WHAT IT CORRECTS.** Tekko-Kagi -25.3 -> **+205.3**, fair -> premium, and
    it falls from 27 Conquest `model` builds to 11. Devourer's Gauntlet +629.9
    -> +152.7 (premium -> fair), Deathbringer +204.6 -> +56.1. Not a §4.25
    rescale: the decomposition's NORM arm moved 0/3/0 cores.

    **THE DUAL-PRICED ITEMS: THE FLAG WINS, WHICH REVERSES THE FIRST RULE.**
    Eight items are priced by a shipped flag AND simulated. Letting the
    simulated value supersede the flag (the rule first proposed) swapped an
    exact, on-map stat grant for a median that lands in a column no role map
    names, which `offmap_efficiency` then charges back at 55%. It evicted the
    conversion staples from Conquest `model` builds: Rod of Tahuti 35 -> 25,
    Transcendence 13 -> 5, Book of Thoth 6 -> 0, Nimble Ring 7 -> 1. With the
    flag's grant standing they hold (34, 14, 2, 9), and both gates prefer it:

        rule          leakage-free     held-out ww / spearman
        OFF           36.8% / 37.6%          --
        sim wins      39.9% / 38.5%     -0.0014 / +0.0567
        flag wins     41.3% / 38.4%     +0.0167 / +0.0566    <- shipped

    What it gives up is The Executioner: its 7% shred exists only in the
    simulated number, so it stays unpriced and the item reads +739.9. The
    passive columns themselves ARE charged as off-map; they fail the exemption
    rule's test (ii), since `passive_sim` is an instrument that prices them.

    **THE RESULT.** Leakage-free 36.8/37.6 -> **41.3/38.4**. Held-out **+0.0167
    win-weighted / +0.0566 spearman**, a clean PASS and twice §4.31's +0.0082
    benchmark; tuning -0.0036 / +0.0413. Gods at 0% coverage 7 -> 4. Reference
    lines moved: Conquest core 10, Conquest 77, Joust 55, Arena 58.

    **WHAT IT DOES TO THE COMPARISON PAGES** (46 of 282 shown verdicts change:
    Conquest 30, Joust 7, Arena 9):

        readable verdicts    Solo   Support  Mid    Jungle  Carry   total   I / T / C
        Conquest  before    11/19    7/15    6/23    5/18    3/19   32/94    7/17/8
        Conquest  after     10/19    3/15    6/23   12/18    6/19   37/94    8/16/13
        Joust     before     6/19    8/15   12/23    8/18    2/19   36/94   20/13/3
        Joust     after      7/19    8/15   12/23   10/18    2/19   39/94   22/14/3
        Arena     before     3/19    0/15   11/23   12/18    6/19   32/94   22/8/2
        Arena     after      6/19    1/15   13/23   10/18    6/19   36/94   21/12/3

    Conquest Carry goes 3 -> 6 readable, and the six read 0 Ichor better / 1
    trade-off / 5 community better. Support's fall is §4.30's equal-ignorance
    artifact in reverse: Ganesha, Geb, Sylvanus and Yemoja read ours 100% /
    theirs 83-84% with Stampede on the community's side.

    **CORRECTION: THIS ENTRY FIRST CLAIMED "ZERO VERDICTS MOVE".** That was
    never measured. `side_by_side` rewrites the per-god pages only with
    `--json`; without it the run exits 0 and writes nothing, so the readings
    compared `main`'s pages with themselves. The claim, and the conclusion
    built on it that the verdict rule was the binding constraint, are
    withdrawn. A second defect was found the same day: the columns first lived
    in `item_stat_values`, which `build_quality` and `damage_value` read as
    EFFECTIVE STATS, so at ON a build lost The Executioner's real +30 Strength.
    They now live in `efficiency.regression_columns`. Both were invisible at
    OFF, which is why green gates at OFF were not evidence the flag worked.

    **THE COMPARISON-SCOPE QUESTION (`model` or `core`), MEASURED AND LEFT.**
    Judging `core` instead of `model` does not unblock Carry by itself: at
    baseline Carry reads 2/19 against 3/19. With pricing on it reads 12/19
    against 6/19 (total 41 against 37). It is left on `model` because that
    gain is largely `core` being built partly from the community's own win and
    pick signals, so both sides hold the same simulated items and the
    comparison is measuring itself (§1); and because stacking a scope change on
    a re-basing of every residual would make neither attributable.

    **COSTS, STATED.** The penetration-split ratio on the current patch falls
    1.104 -> 1.057, above the 1.0 floor but at the bottom of its old
    leave-one-out range. Support is mostly unjudgeable in Conquest. Readable
    "community better" rises 8 -> 13 in Conquest, because more verdicts are
    readable and the community wins most of the new ones.

33. **An aspect overlay DERIVED from the god's own note (2026-11-05)** —
    shipped ON (`aspect_derive: true`) and INERT: the machinery is live, and
    the one aspect it can derive moves no build. A negative result for the
    build, stated rather than nudged. Code and numbers in `aspect_kit`'s
    docstring; the overlay is `scoring.derived_aspect_overlay`.

    **WHAT WAS DERIVED.** `aspect_kit.apply` reads an aspect's `kit_changes`
    sentence by sentence. WHICH abilities change comes from the text; every
    NUMBER comes from a line already in the note. One rule prices a sentence:
    "<A x> become(s) <B x> instead", where the B term's lines are defined
    exactly once by an ability that grants B. The overlay is `fit_map` on the
    edited kit minus `fit_map` on the base kit, so nothing in it is a chosen
    weight. No god name appears in the code; a test parses the module's AST
    to hold that. Tsukuyomi's Mangetsu derives one sentence of three (Dark
    Moon Shuriken takes Silver Moon Caltrops' `Mangetsu Bonus Damage Scaling:
    30% Strength + 65% Intelligence`). The kit's Intelligence share moves
    0.475 → 0.496, and merged fit moves Intelligence 0.2655 → 0.2694 and
    Strength 0.9745 → 0.9706.

    **WHAT IT MOVED: NOTHING.** No six changes, in any archetype or mode. A
    derived family ships only if it moves a build
    (`recommend._family_moves`), so Tsukuyomi has no aspect family in
    `viewer/public/index.json` and the toggle still falls back to the base
    build. `recommend --all` + `build_index` rewrote no file. Measured
    before → after on fingerprint `4f63ded0872c` (→ `fb0eaf0f2496`; the new
    YAML key is the whole difference):

        held-out win-weighted / Spearman    +0.0000 / +0.0000   PASS
        tuning   win-weighted / Spearman    +0.0000 / +0.0000
        control  0.70:0.30 / 0.45:0.55      41.3% / 38.4% -> 41.3% / 38.4%
        Conquest readable verdicts          54 of 87 -> 54 of 87 (report byte-identical)
        reference builds                    unchanged, 10 gods x 3 modes
        gods other than Tsukuyomi moved     0

    **WHY: two reasons, measured separately.** (1) The derived change is
    SMALL: one 30/65 line joins kit lines that already sum to about
    450% Strength and 410% Intelligence. The brief's passive line
    (15/30) gives 0.2673 and also moves nothing. (2) The channel is NARROW:
    the role table holds 0.7 of every offensive column (`kit_blend` 0.3), and
    the Jungle table names no Intelligence. An upper bound that rewrites his
    whole kit to 1:2 reaches only Intelligence 0.3006. So **the derived mix
    does not look like a magical build, and through this channel no aspect
    text could make a physical Jungler's build magical.**

    **REFUSED, and why.**
      * *Retuning `kit_blend` for aspects.* Its evidence is a 2026-07-22
        sweep against `validate.compute` (`_weights.yaml`), the gate §1 says
        cannot choose parameters. That is a reason to re-measure it
        leakage-free for every god, not to raise it for one aspect. Raising it
        would not help anyway: swept 0.3–1.0 as a diagnostic, the derived
        family moves a build at exactly one setting (0.7, one item in `core`,
        a near-tie) and at none of the seven others.
      * *Applying the overlay unblended* (merging the kit's own Intelligence
        0.898 over the map, as the seven hand overlays merge their typed
        weights). That gives aspect evidence a weight of 1.0 where base-kit
        evidence gets 0.3. It is the eighth hand-tuned overlay by another
        route.
      * *Pricing Piercing Moonlight's "major damage".* The note carries no
        number for the aspect version, so the sentence is `unpriced` and the
        base lines stay.
      * *`SIMULATED_ASPECTS`.* It stays empty. `combat.py` cannot play a kit
        whose ultimate has no aspect numbers. It would also change nothing:
        Mangetsu's 3% pick keeps `side_by_side.kit_for` on the base kit.
      * *Joust team seats.* A derived overlay takes no seat in
        `recommend._team_seats`, so deriving one god's aspect cannot move
        another god's Joust build through the anti-heal share.
      * *Re-adjudicating the seven hand overlays.* Hand overlays still win.
        None of the seven has a sentence that derives, so derivation would
        have nothing to replace them with.

    **THE ROSTER, AND WHAT THE FOLLOW-ONS COST.** 2026-11-05, all 78 aspects:
    235 sentences, **1 derived, 151 unpriced, 83 mechanics only**. The scrape
    carries aspect TEXT and almost never aspect NUMBERS. For the seven gods
    whose aspect is the majority pick, the parser derives nothing:
    Aphrodite's note has `aspects: []`, so there is no text at all; Khepri,
    Nike and Bacchus name a stat with no ratio ("constant Attack Damage",
    "scaling with Strength"); Baron Samedi, Gilgamesh and Cernunnos describe
    mechanics. Each needs a SOURCE for the aspect's numbers (the wiki's
    aspect tooltip, an in-game reading into `_combat_observations.yaml`), not
    more code here. The cheapest second RULE is a removal, "<ability> no
    longer has <Stat> Scaling". The note can price that, and it fires on Pele
    alone today.

    **REVISIT IF** either test in `test_aspect_kit.py` turns red:
    `test_only_tsukuyomi_has_a_derivable_aspect_sentence` (a refresh adds
    aspect numbers, or a new rule lands: more aspects become derivable) or
    `test_the_derived_mangetsu_family_moves_no_build` (the family starts
    moving a build and ships on its own, so confirm it in `index.json`).
    Revisit too if `kit_blend` is re-measured leakage-free at a value other
    than 0.3.

Reading 1–5 through §1: each made `efficiency` more informative but less like
the community's data, which the gate punishes by construction. That is a
hypothesis, not a proof — but re-running them against the *old* metric will
just reproduce the old answer.

---

## 5. What is actually left

Roughly in the order I would do them.

### ~~The shipped index is built with every pricing flag off~~ — fixed 2026-11-05
Found 2026-11-05. `recommend` and `validate` call
`efficiency.apply_pricing_flags`; `build_index` never does, and `load_weights`
does not set them. So `items[*].efficiency`, `efficiency_tier`,
`item_gold_values`, `god_item_scores` and `god_item_damage` come from a different
fit than the one that chooses the builds. Measured at `main` 6fc363b2: all 190
index residuals match the flags-off fit and none match the flags-on one, and the
tier shown differs from the tier used on 42 of 190 items (Rod of Tahuti shows
+267 where the model uses -922). The method page's working is therefore not the
model's working, and #110's repricing will not show on the items page. Not fixed
here: it moves every displayed figure and the draft's scores, so it wants its own
measurement. This is register §4.10's failure mode.

_Fixed the same day._ `build_index.build_index` applies the flags for the whole
build and restores them; re-measured at 4130ed90 first, the gap had widened to
193 of 193 residuals and 59 tiers (Rod of Tahuti +267 shown, -734 used). What
moved, including the draft under 44 enemy comps, is in that docstring: an empty
board cannot change, and a drafted one changes its six on 14-16% of Conquest and
15-23% of Joust `core` boards depending on the comps, `god_item_scores` doing
most of it. (The Joust figure first went out as ~7%, from a harness that
padded Joust boards to five slots and so diluted every threat; re-measured
2026-11-06.) Two
things the fix needed that the defect hid: the receipt could not close on
printed stats once the fit priced passives (87 of 193 items short, up to
1,194g), so each item now ships `efficiency.priced_passive`
(`efficiency.passive_columns`) and the receipt lists it; and the method page's
"what is still unpriced" paragraph named two priced classes while four were on,
so the switches ship as `method.pricing` and the page reads them.
`test_the_index_ships_the_fit_that_chooses_the_builds` pins residuals, tiers,
gold prices, the draft tables' flag state, the restore, and the receipt.

### Done criterion 2 — engine and page built; the per-god follow-through is not

`side_by_side.py` (§2) answers the criterion's numbers for all 94 gods; the
per-god table, item diffs, verdicts by role and the not-simulated list are in
`data/Analysis/_side_by_side.md` (regenerated, not tracked — ~400 KB of daily
churn).

**The fairness pass (2026-11-02, control fingerprint `60bea8b0c5e6`) withholds
75 of the 87 verdicts, and that is the headline.** A review found four ways the
earlier tally (Ichor 16 / community 31 / trade-off 24 / level 16) was unfair;
all four are fixed in `side_by_side.py`, `passive_sim.py` and
`community_target.py`, with the evidence beside the constants:

1. *Coverage.* A passive the clock cannot run is worth zero, and Ichor's
   builds hold far more of them (378 item slots against the community's 244:
   Jotunn's Revenge, Kinetic Cuirass, Genji's Guard, Spear of Desolation,
   Amanita Charm and other actives). Each build now carries the share of its
   gold the clock models fully (`simulated_share`), printed beside the
   verdict. Under `COVERAGE_MIN` 50% or over a `COVERAGE_GAP` of 14% it is
   NOT ENOUGH SIMULATED. The gap is derived: the median simulated passive moves
   the damage axis 5.8%, more than the whole band, so one item of gap can flip
   a verdict alone. Two tighter measures (stat-price residuals) were tried and
   neither can separate a passive's price from its stats — see the constant.
2. *Early game.* The verdict weighs the 2-, 4- and 6-item points equally
   (`BREAKPOINT_WEIGHTS`); a build ahead early and behind at six is an
   EARLY-GAME BUILD (reverse: LATE-GAME), not a loss. Before coverage: Ichor
   better 14→31, community better 31→18. **Most of that swing is the stack
   assumption, not the builds** — the community front-loads stacking items (50
   in its first four slots, Ichor 4) and those read at zero stacks at 2 and 4
   items; with stacks full early the same rule gives 16 / 27. The report prints
   both ends.
3. *Odysseus' Bow* reads "Attack Damage" as the swing (SMITE 2's term), not the
   stat, and lands 3 hits on the lone target (`ODYSSEUS_HITS_ON_TARGET`): its
   passive went from ~3-5% of a build's sustained damage to ~20-23%.
4. *One community cleanup rule.* `community_target.comparison_six` is used
   everywhere: drop components and statless relics/Mods (PR #73's classes),
   then fill to six from the community's next finished picks, APPENDED. No
   comparison six changed membership; six changed order.

What survives: 12 verdicts — Ichor better 3, community better 1 (Nemesis),
trade-off 2, level 5, early-game build 1 (Tsukuyomi). **7 gods get no verdict**
because the kit is matched first: where most of the community plays an aspect
(Aphrodite 79%, Khepri 76%, Nike 67%, Baron Samedi 66%, Gilgamesh 61%,
Bacchus 59%, Cernunnos 53%) the comparison would need an aspect kit
`combat.py` cannot play; their base-kit numbers are shown, labelled, and
counted nowhere (`side_by_side.kit_for`). The god page draws it for Conquest
(`SideBySide.tsx`, one `viewer/public/side_by_side/<god>.json` per god, written
by `--json` in the daily refresh), coverage line included.

**The fight layer (2026-11-03, same fingerprint `60bea8b0c5e6`) cut the
withheld verdicts from 75 to 47 of 87.** `side_by_side`'s FIGHT block puts
four things in the clock, each under one written assumption that both builds
share: a kill (one per 10s fight, when our damage reaches the target's max
health — a first draft that counted every multiple of max health gave a carry
five kills in 10s and was dropped before any verdict was read); an assist
every 10s from 5s; an enemy on our god as lethal as the comparison asks us to
be (the squishy's effective health over 10s, at the median community Carry's
attack speed and Mid's cast rate); and every "On Use" press on cooldown once
its condition holds. Effective health is now the raw damage that enemy deals
before the bar is gone, which equals the static integral when nothing in the
build reacts (tested). Twenty-nine items moved to SIMULATED from their text,
each with a frozen-text test in `test_fight.py`; the readings taken are in
`passive_sim` beside each one. Two results worth keeping: **assists barely
matter** (all off: Ichor better 10 / community better 7, against 11 / 6), and
**PR #77's early-game builds were the stack artifact it suspected** — with
stacks on a game clock (an item every 5 minutes, full 10 minutes after
purchase; neither measured, both bracketed in the report) they go 3 → 0.
Counts now: Ichor better 11, community better 6, trade-off 11, level 12,
early 0, late 0, withheld 47. What still withholds is mostly passives the
comparison cannot contain at all — Tekko-Kagi's pathfinding (22 of the 47),
Stampede, Runeforged Hammer, Eye of Providence, Erosion — and the coverage
rule is doing its job there; loosening it to get verdicts would be tuning.

**Healing (2026-11-03, re-measured on OB47 at fingerprint `2511b1ce28f7` — identical counts).** `side_by_side`'s
HEALING block gives both sides a healing-received channel: our god lifesteals
off every damage instance to a LIVE target plus the heal-on-hit items, cut by
the enemy team's expected anti-heal; the target lifesteals off its hits on
us, cut by ours (strongest reduction only — the item text says it does not
stack), and sustained damage is net of it. Gluttonous Grimoire, Shield of the
Phoenix, Bloodforge and Divine Ruin moved to SIMULATED; Toxic Blade and
Stygian Anchor are PARTIAL (target attack-speed debuff). The healing rows in
`_combat_observations.yaml` are tier DOCUMENTED (the texts' arithmetic), not
in-game readings — that reading is still open. Counts 11 / 6 / 11 / 12 /
withheld 47 → Ichor better 8, community better 10, trade-off 14, level 9,
early 1, withheld 45. Coverage alone moved 2 (both out of withheld); healing
moved 7, all on the SURVIVAL axis and all toward lifesteal-heavy community
sixes (Sun Wukong, Chaac, Mordred, Ishtar, Hua Mulan, Sol, Ymir). **Read it
with the one-fight bound beside it:** an effective-health run is a chain of
10s fights and lifesteal compounds over the chain; with heals only in the
first fight the counts are 11 / 7 / 13 / 10, late 1. Anti-heal moves the
damage axis ~1%: the reference Mid carries 4.8% mean lifesteal, and only 3 of
94 community sixes hold an anti-heal item at all.

**Per mode (2026-11-03).** `python -m smite.side_by_side --mode Joust|Arena|all`
runs Ichor's MODE `model` build against the **borrowed Conquest** six (the
only community record), with Ichor's Conquest build beside it as a second
reference, under each mode's settings (`MODE_SETTINGS`, evidence in the MODES
block): Joust 3 enemies and a 16.7s fight (10s × 5/3 — derived from team
size), Arena 5 enemies and a 15s fight (a judgement, bracketed 10–20s in the
report), stack clock from each mode's `economy`. Arena drops its
`excluded_items` from the borrowed six and refills. Reports
`data/Analysis/_side_by_side_<mode>.md`, viewer files under
`viewer/public/side_by_side/<mode>/`; the god page's comparison now has a mode
switch and says "borrowed" every time. Counts (87 judged): Joust Ichor better
9, community better 4, trade-off 7, level 7, withheld 60; Arena 11 / 1 / 6 /
6, late 1, withheld 62. Withholding is HIGHER than Conquest's 45, and the
Joust not-simulated table says why: Erosion (37 compared builds, no enemy
shield), Toxic Blade (31) and Stygian Anchor (27) — the last two PARTIAL only
for their attack-speed debuff on the target, and both pulled in by the
modes' flat +0.30 anti-heal bonus. Read the mode counts as "most mode builds
cannot be judged yet", not as a win for Ichor. Simulating the target's
attack-speed debuff (the enemy's attack cadence is already a clock) is the
cheapest next step to judge more of them.

**Lifesteal in the fit map (2026-11-03).** The healing verdicts pointed at a
fit-map gap, not a price: `Lifesteal` had a fit weight only in the Carry,
Hunter and Sharpshooter maps, so 0 for 19/19 Solo and 18/18 Jungle gods.
`smite.lifesteal_value` measures a typical item's 7.5% Lifesteal against a
typical 250 Max Health in `fight_ehp`, per role, at both healing bounds, and
`role_stats` now gives Solo 0.52 and Support 0.47 (the geometric mean of the
bounds; Jungle and Mid carry no health weight, so nothing). Coverage 36.6% /
36.7% → 36.6% / 37.2%; 14 `core` cores change in each mode; Conquest verdict
totals do not move. None of the seven motivating gods changes verdict, because
the sustain cap of 1 binds and the community's Solo sixes hold a median of one
sustain item too — the weight changes WHICH sustain item, not how many. The
table and both bounds are in that module's docstring.

**Ability self-heals (2026-11-03).** `smite.ability_heals` reads each
ability's "Heal", "Heal Per Tick" and "Heal Scaling" lines (flat at the last
rank, % max/missing health, % protections, % stat; tick counts from "Heals N
times") for 33 of 94 gods, into the HEALING block's channel, so anti-heal
cuts them. A rotation ability heals on its cast; a heal-only ability (Rain
Dance, Radiance, Cruel Strikes) casts at the first hit taken, then on its
cooldown. **It changes no Conquest verdict at either healing bound**, and none
of the seven lifesteal-leaning gods moves: a god's kit heal is the same for
both of its builds, so it lifts both survival figures together. Community
EHP rises 4–31% on the gods it reaches (Chaac +31%, Mordred +23%). Known
gap: Sun Wukong's cloud heals "every 0.5 seconds" with no stated duration and
is cast once at full health, so it lands nothing.

Left, in order: (1) decide what a movement/CC/ward passive is worth in a
comparison that has no movement, CC or wards — the honest options are a
stated zero (and counting it as covered) or leaving those gods withheld, and
that is a rule for Jacob, not a constant; (2) a measured farm/takedown rate
for `STACK_MINUTES_TO_FULL`, which is reasoned, not measured; (3) a
phone/desktop pass by Jacob; (4) the seven aspect kits, most-played first;
(5) for each surviving "community better" god, a model change or a stated
reason — the report's swap rows name the single item that recovers most.

### Two thirds of the shipped builds rest on nothing measurable
The builds are no longer *identical* to Conquest's, at least:
`modes.<mode>.economy` discounts an item by the share of the scoring window it
is active for, which moves Arena's average purchase −680g and Joust's −133g.
Every input carries its source and tier in `_weights.yaml`; Arena's are
DOCUMENTED (15 g/s spooling from OB28 — the mode page's 11 is pre-OB1 and
stale), Joust's are INFERRED because its wiki page is a stub. Still no outcome
data to check any of it against.

**No source for outcomes exists** (checked 2026-08-10): SmiteBrain is Conquest-only
and ignores every mode query param, smite2.live ships a Joust/Arena selector
with zero rows behind it, SmiteTracker's meta report is Conquest-only. The
builds now disclose it in the reader's own terms — "no outcome data exists for
Joust … read this as a shortlist rather than a buy order".

178 of 267 build groups are Joust and Arena. Those modes have no community data
at all, so the recommender falls back to efficiency + fit alone — the
combination measured at ~6× chance for *finding* items and ≈0 for *ranking*
them. The tier list now admits this; the builds do not, and the builds are the
product. Either find a source with per-mode outcomes, or disclose it on those
builds the way the tier list does.

**Anti-heal and auras are team jobs now (2026-11-03, OB47).** The modes' flat
+0.30 paid every god for one job a team does once ("Healing Reduction does not
stack with other similar effects"). Three parts, evidence beside each:

1. *Static builds* (`team_tags` in `_weights.yaml`). The MODE's bonus for
   `anti-heal` and `aura` is scaled by a share CALIBRATED so a static core
   holds the tag about one time in N (team size): Joust 0.65 / 0.15, Arena
   0.70 / 0.00. A single duplicate value could not do it — at 0.25, 14% of
   Joust cores and 3% of Arena's held anti-heal. Against main, `core`:
   Joust 57/101 change, anti-heal 67 → 35 of 101 (1 in 2.9), team aura
   51 → 34; Arena 67/101 change, anti-heal 30 → 21 (1 in 4.8), team aura
   58 → 19. "Team aura" is an `aura` item that is not also `sustain`: Amanita
   Charm and Soul Gem carry the tag for an incidental ally heal, and 74% of
   cores hold SOME aura-tagged item even with the aura bonus at zero (78 → 76
   and 78 → 75 here), so that column cannot reach 1/N and is not the target.
   Conquest has no team-tag mode bonus and moves 0.
2. *Kit fit* (`pipeline/smite/kit_fit.py`, built once for this and for
   Lotus Sickle's held tag). A kit's capabilities off its ability text
   (`ally_support`: 26 of 94; `melee`), an item's needs off its passive text
   (`ally_support` for "Healed, or Shielded another Allied God" items;
   `near_allies` for "You and allies within 8.8m"), and a tag-free stat fit at
   or above the least-fit item already in the god's core. Agni fails Lotus
   Sickle; Ra passes.
3. *Draft* (`viewer/src/lib/teamTags.ts`). Teammates' builds replace the
   static expectation per tag, and EVERY positive anti-heal/aura bonus — the
   team delta or a healer threat — reaches only kit-fitting items. Your own
   slot no longer counts as a teammate in `threats.deriveThreats` (it damped
   threats your own core answered, a second time). Joust boards holding
   anti-heal, two teammates entered: no enemies 34/94 → 34 (none hold it) or
   13 (both do); three healers 39 or 34. Before the gate, three healers and no
   teammate copy put anti-heal on all 94. Arena, five healers: 56 or 20.

Mode comparison after this (87 judged, against the borrowed six, which did not
move): Joust Ichor better 9 → 13, community better 4 → 4, trade-off 7 → 13,
level 7 → 7, late 0 → 1, withheld 60 → 49; Arena 11 → 19, 1 → 4, 6 → 10,
6 → 7, late 1 → 1, withheld 62 → 46. As before, most of the movement is
COVERAGE — PARTIAL anti-heal items left the builds — not evidence of quality.

### The feedback loop has a first version, and it is tiny
Everything else validates against community data, which §1 shows cannot
adjudicate the model's central claims. `data/_expert_reviews.yaml` +
`smite.expert_review` are the first gate here that isn't made of that data: a
strong player's judgements, written down in a shape a script can replay. Four
claims from one reviewer (2026-08-09) — three resolved, one open.

**It is not a measurement and must never be quoted as one.** One reviewer,
claims chosen because they looked wrong. It answers "did the thing they
objected to change?" and nothing else. The real version of this is still
capturing real games — "I played this build, here's what happened" — and that
remains the highest-value thing left. What exists now is the cheapest possible
stand-in for it, and its value is that judgements stop evaporating when the
conversation ends.

**The vocabulary is six checkable kinds as of 2026-09-03, up from two.** The
original two were both item membership; the four added are an ordering
(`buy-order`), a matchup swap (`situational-swap`), a floor or ceiling on how
many core items carry a stat or tag (`composition`), and a required
co-purchase (`pairing`). Each was admitted on one bar — checkable today from
`index.json`, and able to go `holds` — and the shapes refused for failing it
(outcomes, pairing-as-statistic, score rankings, timing, roles) are listed in
the module docstring so nobody re-derives them. The two `narrative` claims on
file were re-examined and fit none of the six; each says in its `notes` what
it would need. Still four claims: this built the pipe and did not fill it.

### "Leakage-free" is a claim about signals, and constants are not covered
§4.23 found and measured the one place this bites — `conversion_reference`, a
median over community builds, read by a flag that ships ON — and the answer was
−2.6pp / −0.6pp of level and no verdict. What is left is the rule, and it is a
decision rather than a measurement, so it is recorded here and not taken.

**`calibrate` should NOT neutralise community-derived constants, because it
cannot.** Zeroing a signal is well-defined: the weight goes to zero and the
term vanishes. A constant has no zero — emptying `conversion_reference` does
not remove it, it substitutes 0, and in the assembly half that is the
*opposite* of neutral, since `assemble.conversion_score_bonus` then subtracts
no reference and credits a converter with its whole mana. The only available
neutralisation is substituting a different constant, which is a model change; a
`calibrate` that swaps constants behind the config reports the number for a
model nobody ships, which is precisely the defect `efficiency.apply_pricing_flags`
exists to close, arriving from the other side. There is also nothing to
intercept at runtime: `measure_conversion_reference` has no production caller,
so this leak is a one-time human transfer and not a live loop.

Three things that would help, in order of cost:

1. **Declare, don't neutralise.** A registry — a list naming every
   `_weights.yaml` key derived from the community record, and a test that fails
   when a key not on it is produced by a function reading
   `entry["source"] == "community"` — makes the next one declared rather than
   discovered eleven weeks later. That is enforceable; zeroing is not.
2. **Decide whether the MODEL should carry a community-free reference.**
   §4.20 measured three candidates and they cost the same: −2.6pp / −0.6pp of
   level, no verdict changed, `price_conversions` still beating OFF on the same
   standard. It is a small, cheap, honest change and it is the only way to make
   the leakage-free measure actually leakage-free here. It also moves the input
   fingerprint, so it wants its own session and a re-stamped `_calibration.md`.
3. **Sequence it with the passive work.** 09-02 D's `measure_multiplier_reference`
   already builds a pool-derived reference (`slots=5`, because the item being
   priced is the sixth). A conversion reference wants `slots=6` —
   `conversion_grants` includes the item's own contribution, "you own it once
   the item is bought" — so the two are the same measurement at different slot
   counts and a shared helper must keep `slots` a parameter. **Do not unify
   them at 5.** And prefer the per-item shape (the item's own value plus the
   pool mean over the other five slots) over a flat pool mean: the flat mean
   prices Transcendence's source stat at 235 when the item alone carries 300,
   while the per-item form recovers the community's own 500 from item data
   alone (Transcendence 446, Book of Thoth 546). It needs
   `conversion_grants` to take a per-item reference, which nothing does today.

### The win signal is still a constant for ~92% of the pool
SmiteBrain reports a win rate for a median of **11 items per god** against a
pool of 133, and `win` carries the largest weight (0.45). The *flatness* is
addressed — `unknown_win_per_god` imputes the god's own median instead of a
global 0.5, because 77 of 87 gods measure above 0.5 and the constant was
handing every community-built item **+0.0242 on `total`, 186% of Ullr's entire
rank-3-to-10 margin**, purely for appearing in the data.

**The WEIGHT is untouched and unvalidatable.** 0.45 on a signal that is a
constant for 92% of the pool cannot be justified or refuted by anything here:
`calibrate` zeroes `win`, and the headline gate uses it as its own target. It
is the largest single unexamined number in the model.

**AND THE FLATNESS IS NOT AS ADDRESSED AS THIS SECTION USED TO CLAIM — §4.26,
2026-09-03.** Moving the stand-in from a global 0.5 to the god's own median
fixed the units error and nothing else. The median still sits above the bottom
half of the distribution it is drawn from, so **236 of 582 Conquest `core`
slots are held by an item with no measured win rate and 163 of those displace
an item that has one**, across 75 of 90 gods. §4.26 ships the repair
(`unknown_win_shrink`) **OFF** and says why: no scalar can be neutral in an
additive blend — "cannot outrank a measurement" and "loses to every
measurement" are the same rule for one number — and `build_quality`, the one
instrument that can see this at all, says the discounted builds are worse.
**What survives is this section's own point.** The defect is not the
placeholder's location, which is already the least-committal one available; it
is the 0.45 weight it is entered at with no uncertainty term. That is the
number named above, and §4.26 adds that it cannot be examined either.

### ~~Our Carries over-buy defence, and one item is why~~ — fixed 2026-08-22
The role split (§2, §3) found it and deliberately did not fix it: the
community buys **exactly 0.0 protections on all 18 Carries** and we buy 37.8,
which is Berserker's Shield in **17 of our 18 Carry cores against 0 of theirs**
plus Golden Blade in 7. It is one item winning a slot on efficiency + fit, not
a diffuse defensive tilt, and it costs damage — Carry is the weakest damage
record of any role while being 18 of 18 ahead on effective health.

**The two obvious causes are already excluded** and re-deriving them is wasted
work: register §4.14 has the import-path evidence that neither
`defense_affinity` nor `draft.archetype_scaled_stats` can reach these builds,
and that the former is 0.0 for Carry regardless.

_Diagnosed 2026-08-22, and the mechanism is now known (§4.15)._ It is the
**gold model's residual**, not the Attack Speed line and not the health.
`efficiency` prices every stat an item carries whoever is buying, and
`god_fit_score` normalises over the role map alone, so the three stats a Carry
cannot use are credited by one half of `quality` and invisible to the other.
Repriced against the one stat a Carry's map names, Berserker's Shield goes
from −425g to +849g and from rank 1–9 to 84–126, and leaves all 18 cores.

**What is left is the part that has no answer yet.** The obvious correction —
charge the off-map mass — was implemented, swept on all three modes and ships
off: it is worse on both leakage-free splits at every strength, because
off-map mass is two different things and nothing here separates them. Mana and
regen are ride-along the community buys as heavily as we do and no role map
names, so charging them punishes a real want (Support −21.4pp, Solo −9.4pp);
protections on a Carry are the genuine defect. Separating those needs either a
judgement about what a role really wants (the invented constant §4.12 and
§4.13 refuse) or the community's own composition (the leakage §1 is about).

So the open question has moved and narrowed: **the role stat maps are
incomplete in a way that is invisible until something charges against them.**
Anything that reads the map as a complete statement of a god's wants inherits
that. The stat table and the item counts re-measure on every `build_quality`
run; the decomposition is in `efficiency.offmap_adjusted_score`.

_Fixed 2026-08-22, and the incompleteness above is what had to be handled
first._ `offmap_exempt` grew its third stat — Health Regen, on the two
mechanical tests §4.16 records — and with the three ride-along columns spared,
`offmap_efficiency` beats or matches control on both leakage-free splits
across 0.45–0.65 and ships at 0.55. **Berserker's Shield is in 0 of 18 Carry
model cores, from 17**, Golden Blade 7 → 5, Gluttonous Grimoire 2 → 0; mean
Physical Protection in a Carry core 37.8 → 0.0 against the community's 0.0,
and raw effective health lands **LEVEL** (+0.0% median, within ±0.5% on 12 of
18) rather than below. Medusa goes 314.8 → 389.5 total DPS, 87% of the
community's against 70%, with identical effective health on both sides.

**What is left of it, and it is not nothing.** Per 1000 gold our Carry
effective health is now *behind* (−7.5%, 2 ahead / 15 behind) — arithmetic
rather than a finding, since level EHP on a costlier build divides worse — and
the other four roles each give up ground on `build_quality`'s ahead/behind
counts while staying clearly ahead. §4.13 is why that cost is hard to see: no
threshold here can charge us for buying too LITTLE defence, so **level is the
honest target and below it would be invisible.** The role maps are still
incomplete; what changed is that one class of stat now has a rule for being
left alone, and the rest of the incompleteness is untouched.

### The fit map credits half a basic attack and charges the other half
The clearest piece of that remaining incompleteness, found 2026-08-23 while
looking for the Jungle cost (§4.18) and deliberately not acted on in the same
session. `attack_damage_fit` gives **78 of 89** merged god maps an Attack
Damage column, measured from the god's own basic-attack scaling; **Attack
Speed reaches only 35 of 89**, because `role_stats` names it for five labels
and `kit_stat_overlay` emits it only when an ability scales on it. The two are
the multiplicands of the same basic attack, so the model credits a god for one
and bills it for the other — that is what took Tekko-Kagi out of six Jungle
cores, for 418g of a stat those six are credited nothing for and charged in
full.

**It wants a WEIGHT, not an exemption**, and unlike mana the exchange rate
exists and is leakage-free: `combat.attack_dps` states how Attack Damage and
Attack Speed combine, and both terms are scraped. Two things to check first.
The rate is **build-dependent** in a way `damage_value.stat_weights` is not —
it needs a reference build, for which `passives.conversion_grants` is the
precedent (§3, priced against a typical build) — and the column has to ship
`denom_exclude`d for the reason `attack_damage_fit` does, or about a third of
whatever it reads will be the normaliser shrinking every non-carrier (§4.4).

### Nothing here can say a buy ORDER is good
Found and worked around rather than solved, 2026-09-02. `calibrate` measures
membership overlap and is blind to order — reordering the same six items moves
it exactly 0.0pp. `build_quality` points `combat.py` at a finished six-item
build at level 20 and is equally blind, because the same six items at level 20
are the same numbers whatever sequence bought them. So the repo's usual bar,
"beat control on both leakage-free splits", **cannot be met by any ordering
change at all**, and the shipped positional buy order is measured on
agreement with observed play instead (`smite.order_agreement`, and it says so
on every path out).

**What would change it is a clock, and it is §4.12's clock.** An order is a
claim about power over TIME — the value of holding item A at minute 8 rather
than minute 20 — and this repo has no time axis on either side: no cast times,
no match timeline, and `time_value_multiplier` prices a whole build's window
per mode rather than a purchase's. §4.12 refused to invent a combat clock and
that refusal stands; what an order needs is a *gold* clock (when does each
purchase complete, at what income) and `modes.<mode>.economy` already carries
one with sources and tiers. Whether a completion time plus `build_quality`'s
level-20 arithmetic can score a sequence is open and nobody has tried it.

**Until then the honest position is the one shipped:** the community's own
record is evidence about order, it is the only evidence there is, it exists
for one mode of three, and it is labelled everywhere it is used (§4.20).

### `effective_health` has no term for Plating or Dampening
Found the same way, 2026-08-23 (§4.19). `combat.damage_dealt` applies both —
Plating against Attacks, Dampening against Abilities — but only to the TARGET,
and no caller in the package ever supplies a value. On the buyer's side there
is no expression at all: `effective_health` is `health × (1 + protection/100)`.
So **a build's own Plating and Dampening are worth exactly 0.0 to the only
non-circular instrument in the repo**, on 13 items carrying ~38 g/pt, and no
charge or credit on either can be checked in either direction. `TARGET_SIDE_ONLY`
names them and two tests hold the claim.

The fix belongs with `EHP_CHANNELS` and not beside it: attack-vs-ability is the
same shape as the physical-vs-magical split §4.17 made, and composing the two
turns the durability figure into a **two-dimensional interval** rather than a
pair. Read §4.17 before starting — the case for reporting the interval instead
of collapsing it is the same case, and it is harder with four corners than with
two.

### The passive ceiling now has a catalogue, and a proposed next carve-out
Register §4.20 and `docs/PASSIVES.md` (2026-09-02). Every buildable item's
passive is classified by the shape of its value in `data/_passive_classes.yaml`,
held to the pool by a test. Roughly twenty of the 124 unpriced items are
reachable without a new constant; about a hundred are refused, by class, for
the reasons existing entries already give (§4.12's clock, §4.17's attacker,
§4.8's stacks, §1's leakage). The proposed carve-out is `price_stat_multipliers`
— the four "+X% of all Stats from Items" relics and Genie's Lamp, class A2 —
with its predictions written down before any sweep. It is not built. Two things
to hold any carve-out to that the shipped three were not: the reference build
must come from item data (the shipped `conversion_reference` is a community
median), and a converted magnitude must land inside the column's fitted range.

### The leakage-free measure carries a community reference inside a shipped flag
Found by the passive catalogue (§4.20) and verified by the maintainer on
2026-09-02: `conversion_reference` — the reference build `price_conversions`
prices Transcendence, Book of Thoth, Rod of Tahuti and Nimble Ring against — is
`passives.measure_conversion_reference`, a MEDIAN OVER COMMUNITY BUILDS, and
`calibrate` does not neutralise it the way it zeroes `win` and `pick`. So the
two "leakage-free" splits are not fully leakage-free, and every coverage figure
quoted since that flag shipped (2026-08-14) carries it. **This is its own
session.** Do not fix it in passing; the fix is a pool-derived reference of the
kind `multiplier_reference` already is (§4.21, `passives.measure_multiplier_reference`),
re-swept, with the two controls compared — and the size of the leak, which
nobody has measured, is the first number to produce.

### ~~Why four items that reach no core move forty cores~~ — answered 2026-09-03
§4.21's open question, now **§4.25**. It is not the fit's identifiability and
not the reference vector: `efficiency_scores` min-max normalises the residual
pool, `hi` is Agility Greaves (whose only printed stat has one carrier, so the
fit sees an all-zero row and its residual is `2500 − intercept`), and pricing
it rescales every other item's efficiency score by 1.226 with zero change to
any residual or rank. That rescale is exactly an efficiency:fit weight change,
verified to identical coverage on both splits. The suggested first arm there —
restricting the grant to the columns the relic already carries — was not run
and is not the next move; the open question this leaves is whether a scale-free
efficiency signal is worth re-basing all of §4 for.

### The efficiency signal's scale is set by two items, and every §4 delta rides on it
§4.25 (2026-09-03). `score = (hi − residual) / span` over the whole pool, so
any change that moves the most-premium or most-undervalued item — including any
change to the intercept, since `hi == 2500 − intercept` today — reweights
`efficiency` against `fit` for every god. Every carve-out's measured coverage
delta therefore mixes "the items I priced" with "I moved the signal's gain",
and §4.15, §4.16, §4.21, §4.22 and the three flags that shipped ON were all
measured on it. **This is a caveat, not a known error**: §4.25 checked and
changed no verdict. Two things a fix would have to hold: a scale-free signal
re-bases every number in §4 at once and needs its own control on both splits,
and an item the fit sees as an all-zero row (one carrier, dropped by
`MIN_STAT_CARRIERS`) probably does not belong in the scored pool — which is
`efficiency_pool`'s statless rule with one carrier instead of none.

### Two parser precision notes, small and separate
Both inert today and both recorded in `docs/PASSIVES.md` §7 (2026-09-02).
`passives.is_persistent_stacker` reads Kinetic Cuirass ("Stacks up to 2
times", consumed on the next attack) and Oni Hunter's Garb ("Max 3 stacks",
per enemy in range) as persistent — wrong the day `price_stacks` is turned on.
`passives.unconditional_grants` misses two real A1 grants: Triton's Conch's
"+5 (+0.5 per Level)" grammar, and Dwarven Plate's always-on protections
because "On Use" appears later in the text and `is_conditional` reads the
whole passive rather than the clause (`stat_conversions` already splits by
sentence for exactly this reason).

### ~~Four findings from the audit quick-fix session (2026-11-04)~~ — all four closed 2026-11-04

Recorded by PR #97 on fingerprint `a4b1a66d8c0d`; closed by the parse-and-leak
PR the same day. Each fix's evidence is in the docstring next to it.

- ~~**The `Damage Scaling:` label rule drops 70 abilities on 48 gods.**~~
  Fixed: the label rule runs per ability (`damage_value.ability_damage_components`),
  and the strict rule still wins wherever it reads anything. Exactly 70 on 48
  (271 -> 341 of 497 read), counting Aladdin's `Landing Damage:` / `Landing
  Scaling:` grammar; no god is left without stat weights (10 were). Eligibility
  moved on the 8 predicted (Discordia and Hades lose `strength`/`str-int`;
  Aladdin, Anubis, Atlas, Nut, The Morrigan gain both, Cupid gains
  `intelligence`/`str-int`). The Medusa example was re-derived by hand with
  Viper Shot in (`build_quality` docstring): ability DPS 35.9/23.7/72.4/45.1 ->
  37.9/25.1/77.0/47.9, basic unchanged, community still ahead.
- ~~**Most `mana-stack` builds hold neither converter.**~~ A rule gap, not a
  property of the gods: all 111 (on the day's tree) had a converter in their
  scored pool, and only Transcendence and Book of Thoth convert mana.
  `require.any_item` seeds one into the core: 111 -> 0.
- ~~**The held-out check cannot see Joust or Arena.**~~ Confirmed (Joust and
  Arena carry 0 of 94 community entries; `validate` resolves Conquest only) and
  not scorable, so no metric was invented: `heldout` now counts the reference
  lines a change moves per mode against the base's snapshot and says NOT
  SCORED / PARTLY SCORED in words. CLAUDE.md names the reference builds as the
  guard there. It is WIDER than recorded — see below.
- ~~**The Conquest `model` build under-weights the conversion and overflow
  terms by half.**~~ Fixed: `assemble.quality_signals` hands the model path
  efficiency at eff/(eff + fit) (0.70 in Conquest). 28 model builds + 2
  hybrids, Conquest only.

### Five findings from the parse-and-leak session (2026-11-04), not fixed

- **The held-out check cannot see the Conquest `model`, hybrid, flavor or
  aspect builds either.** `validate` assembles ONE build, the blended base-kit
  `core`; its Spearman reads Conquest item scores. So the model-leak fix (28
  model builds, 6 shown verdicts) and the converter fix (146 mana-stack builds)
  both read exactly +0.0000 / +0.0000 — every non-zero held-out delta in that
  PR is the parse fix's. `heldout` now says so (the SCORED bucket is Conquest
  `core` alone), but the instrument still has nothing to score those builds
  with; the side-by-side verdicts are the only evaluation they get.
- ~~**The Joust anti-heal share sits on a cliff.**~~ — fixed 2026-11-04 by
  the fight-survival PR. Not tie-breaks in assembly: in Joust the score has no
  god-specific term, so every god of a role sees the same gap to anti-heal and
  any flat share moves the count a role at a time. The share is now DERIVED
  from its 1-in-N target on every `recommend --all`
  (`recommend.derive_team_share`, `data/_team_shares.json`): 34/101, and
  34-36 under every single ±20% weight nudge where the old fixed 0.60 read
  17-52. Evidence in `recommend.py`.
- **Rank lists with a thousands separator do not parse.** `_RANKS` is
  `[\d.]+`, so Ymir's Shards of Ice (`550 | 750 | 950 | 1,150 | 1,350`) is
  dropped, as are three non-ability lines (Eset, Xbalanque). One damaging
  ability today; its scaling also carries `45% Protections`, which `_SCALING`
  does not read.
- **About ten damaging abilities use a grammar neither rule reads**, none of
  them prefix-shaped: a rank line with no colon (Agni's Path of Flames,
  `Damage 20 | 30 ...`), a scaling line with no rank line (Athena's Reach,
  Cernunnos's Heavy Glaive), per-rank scaling (Janus's Threshold, `25 | 30
  ...% Intelligence`), `% of current health` damage (Nemesis), and prose-only
  scaling (Sun Wukong's Magic Cudgel and Master's Will). Each needs its own
  rule; the per-ability structure makes each a local addition.
- **Viper Shot is in, at one tick per cast.** The DoT limit (`damage_value`
  docstring) now applies to every labelled `Damage Per Tick:` ability the
  per-ability rule reads — 23 of the 70 — so those are counted, and
  undercounted, where before they were absent. A tick-count reading would
  change the Medusa example again.

### Two findings from the ally-kit session (2026-11-04), not fixed

Recorded by the PR that added the ally-dependent gate (`ally_kit.py`).

- **Lotus Sickle and Soul Locket are still tagged on the pre-gate world.**
  Lotus Sickle stays at `[]` — the holding measure from 2026-11-03, whose
  stated precondition ("once ally-dependent items only reach gods whose kit
  can buff/heal/shield an ally") is now met. Giving it the drafted
  `[aura, burst, stacking]` is a BUILD-CHANGING decision for the 31 gods who
  qualify, and this slice deliberately changed nothing but what the gate
  implies, so the tags were left alone. Soul Locket is the mirror risk: it
  carries a full tag list chosen while it could reach all 94 gods. Tagging
  both, measured, is the next slice. Note the gate makes the tag edit SAFER to
  try, not safe — §4.19 warns that `quality` rank does not decide core
  membership, so the cores have to be rebuilt rather than argued from scores.
- **Four items are gated and only two of them were reaching anybody.**
  `Rod of Asclepius` and `Soul Locket` pass the same trigger test as Lotus
  Sickle and Eros' Bow, but appear in zero suggested builds on a
  non-qualifying god today, so the gate is a no-op for them. That is a
  statement about their current scores, not about their safety: both are one
  pricing change away from the defect this gate exists to stop, which is the
  argument for gating the CLASS rather than the two items that happened to
  leak.

### Six findings from the fight-survival session (2026-11-04), not fixed

Recorded by the PR that fixed the survival measure (`side_by_side` SURVIVAL
block) and derived the Joust anti-heal share; fingerprint `9c673795e8c8`.

- **A self-heal scaled on missing health makes survival depend on WHEN it is
  cast, so a Cooldown Rate change can lower fight EHP.** Sol / Conquest, our
  core 2 -> 4 items: Spear of Desolation's 10 Cooldown Rate moves Radiance's
  recast from 10.0s to 7.6s, earlier in the bar's fall, and the heal lands
  smaller (311 -> 255): 4609 -> 4501 physical. The one falling-survival
  comparison left of 282 (96 before), and it is a cooldown, not damage — the
  survival fix holds damage equal and this does not. Baron Samedi's Consign
  Spirits is the same shape. Fixing it is the self-heal model's question
  (cast-when-hurt, or a heal-per-second average), not the kill rule's.
- **`lifesteal_value`'s shipped constants were measured on the old survival
  rule.** `role_stats` Lifesteal for Solo (0.52) and Support (0.47) are the
  geometric mean of its two bounds. Re-run on the new rule (`python -m
  smite.lifesteal_value`): one fight 0.569 / 0.347, chained 2.564 / 2.534,
  geomean **1.208 / 0.938** — about double, because lifesteal no longer stops
  at the kill. Not re-tuned: it is a model weight with its own blast radius
  and needs `calibrate`, and the module's own docstring records that the
  `max_lifesteal` sustain cap, not this weight, bound the gods that motivated it.
- **One path from damage to survival is left, and it is a kill HAPPENING, not
  its timing.** A kill's refunds land at the end of its fight; a build that
  kills in a fight the other does not gets a refund whose recast could, in
  principle, land a missing-health self-heal smaller (the first finding's
  shape). Not seen: 0 violations in 5,076 roster-wide checks (every god, mode,
  both builds, 2/4/6 items, damage x1 / 1.5 / 3 / 10). `test_survival`
  checks the frozen reference builds on every run; the roster check was
  one-off and is not in CI (~6 min).
- **Arena anti-heal and both auras still use swept shares.** Arena's 0.70 reads
  27/101 against a 1-in-5 target of 20; its curve near the target is gentler
  (1-2 cores per 0.01) but has the same role-block structure. Adding
  `arena: [anti-heal]` to `team_tags.derive` would hold it at 20 and move
  about seven Arena cores; out of this PR's scope. Auras cannot be derived
  this way: 74% of cores hold an aura-tagged item at a share of zero.
- **Within a role, some seats tie EXACTLY.** Apollo and Artemis share a Joust
  anti-heal cost (0.589233), as do Bellona and Hercules (0.580322): identical
  role map, kit blend too small to separate them. So the derived count is
  the target plus any seat tied with the target seat (34 today, 35-36 under two
  nudges). Only a god-specific term in Joust's score would separate them.
- **`model_audit sensitivity` now re-derives the share per nudge**, as the
  pipeline would, so `modes.joust.tag_bonus` no longer moves the Joust
  anti-heal COUNT (only which seats hold it). PR #96's 16 Joust flips under that
  nudge were partly the cliff and will read lower on the next run; that is
  the fix, not a loss of coverage.

### The 2026-11-04 refresh deleted 55 comparison pages — cause found and fixed 2026-11-05

**The refresh read a one-day match window and committed it, deleting 55 live
comparison pages.** Not test rot, and not the new god: a source default that
rotates on patch day, with nothing in the pipeline standing in its way.

**The cause.** Open Beta 47 landed 2026-11-03 at 11:33Z. SmiteBrain's per-god
pages and both `__data.json` indexes default to the NEWEST patch, and that
window opens the hour the patch lands, so the 2026-11-04 17:30Z run read a
window **one day old**. Measured 2026-11-05 against the live source:

    window            gods   matches   span
    default (= ob47)    86       529   2026-11-03 .. 11-04   (~6 matches a god)
    ob46                94    67,532   2026-10-20 .. 11-03
    1m (refused)        95   152,375   2026-10-05 .. 11-04

At six matches a god SmiteBrain publishes no Core section at all, so
`parse_build_page` returned `{"items": [], "aspects": [], "starters": []}`,
and `notes.merge_build_note` REPLACES the community entry — so the commit
overwrote the only copy of a complete record. 24 of 94 gods were left with
`slot_order: []`, 24 more with 2-5 slots, and `_community_items.json` fell from
238 items to 166. `side_by_side` skips a god who does not make 6 of 6, so the
run **deleted 55 of the 95 comparison pages** the live site serves.

**The record says this was unprecedented.** Complete 6-of-6 community records
on every refresh commit on file:

    10-22 .. 11-02   91 of 91      (window 2026-10-20 .. , growing daily)
    11-03            95 of 95      (ran 09:15Z, before the patch landed)
    11-04            48 of 96      (the one-day window)

**Nothing in the pipeline could see it, and that is the interesting part.** The
daily job's one ENFORCED gate is `validate --check`, and it passed — its
Spearman floor is window-aware by design (`SPEARMAN_LATE_FROM_DAY`), so it
relaxed to 0.30 for exactly the young window that caused the damage, and
win-weighted stayed above its floor on the 40 gods that survived. `data_audit`
is structurally blind too: its community check looks for items the community
builds that we have no note for, so a scrape returning LESS can only make it
quieter. `_refuse_god_collapse` guards the wiki side per note, at the write;
the community side had no guard at all. What actually noticed was two unit
tests pinning god names — after the commit was pushed and the site rebuilt.

**There was a fourth blind spot, and it is the one a PERSON would have caught
it with (closed 2026-11-05).** `_meta.json`'s `data` string — the line the god
page shows above the comparison — read BOTH halves off `data/_patch.json`,
which records the current GAME patch. So its community half asserted something
nothing had checked, and read `community window Open Beta 47` identically at
`5e960b76` (a healthy Open Beta 46 window), at `6158066f` (the one-day window,
166 items and ~194 matches behind the figures) and at `dc03ded4` (restored,
67,532 matches). Three different states, one string, and wrong even when the
data was right. It is derived from the data now
(`side_by_side.community_window_label`), so a thin window is visible at a
glance: `Open Beta 46, 14,667 matches` against what that day would have shown,
a window one day old. The items/gods half still reads `_patch.json`, because
the wiki IS re-scraped on patch day and that half was never wrong.

**The count took one more fix, and it is a unit error worth remembering
(2026-11-05).** PR #109 derived the figure as `matches_played / use_rate` and
called it "matches". It is exact and unanimous across all 238 items, but
`use_rate` is an item's share of BUILDS, so that denominator is god-builds
observed — **67,532**, against **14,667** matches in the same window, 4.6x
apart because the god index records about 4.6 of a match's ten seats. §7's
"Community sample" row had said 14,667 all along, so the repo contradicted its
own page; a test now cross-checks the two.

The three provenance fields are populated at the source as well
(`refresh.window_provenance`). They had been null and empty since the file was
written for a reason worth recording: the ITEM index response carries none of
`start_time`, `end_time` or `matches_analyzed`, while the GOD index carries all
three, identical on every row. One run picks one window and fetches both
indexes with the same `time=` parameter, so the god index is where the item
table's provenance comes from — cross-source, and written down rather than
assumed. #109's derivation stays as the fallback for the files already on
record, relabelled "builds", which is the unit it can actually support.

**And the suites now run in CI (closed 2026-11-05).** `.github/workflows/`
held the daily refresh, the wiki watcher and four probe jobs, none triggered by
`push` or `pull_request` — so nothing re-ran either suite and every PR's checks
were Vercel deploys. `tests.yml` runs both on push to `main` and on every pull
request (pipeline ~6m56s, viewer ~1m1s, `npm run build` included at 0.5s).
That is why the god-name tests went unnoticed for a day: nothing was running
them.

**The fix, in two parts.** `choose_community_window` probes the newest two
patch windows and takes the one covering more of the roster, **a tie going to
the newer** — so nothing is tuned, nothing goes stale, and the run moves to a
new patch by itself the day its window is ready. One window for the whole run,
because a god read on this patch and a god read on the last one are not
comparable, and comparability is what these records are for. The window now
rides every URL the run touches and is recorded in `_community_items.json`.
Then `_refuse_community_collapse` fails the job rather than committing when
more than one god loses a complete record — read before write, the shape
`refresh_god` already used, with `--allow-shrink` for a genuine roster change.

**Restored.** 94 complete community records (from 47), 238 items in
`_community_items.json` (from 166), and **94 gods compared in every mode** —
285 per-god comparison pages against 230, with 87 judged and 1 skipped. Every
one of the 94 reads the same 14-day window, so `validate --check` is back in
its LATE regime (`spearman 0.27, floor 0.2, late window, day 14`, n=459 against
308) rather than the relaxed early-window one that let the damage through.
Conquest readable verdicts: **11 of 32 judged -> 45 of 87**. The control's
leakage-free splits come back from 26.5% / 24.3% to **36.8% / 37.6%**, against
a 5.8% random core.

**One god legitimately has no page, and it is Nox.** He released in Open Beta
47, so Open Beta 46's window holds no matches for him. What the damaged run
wrote for him was six slots whose win rate was **0.0 on every one** — two
matches dressed as a community record, fed into a model whose `win` term is an
input as well as a target (§1). Losing that is the fix working, and it is the
one god of slack `COMMUNITY_COMPLETE_SLACK` exists for.

### The passive-coverage pass closed the gap and bought no verdicts (2026-11-05)

All 84 scored items that carried a passive and no simulator are decided: **33
simulated, 8 partial, 43 refused**, so 193 of 193 items in `efficiency_pool`
carry a decision and nothing reads "no simulator written yet". Every reading is
in `passive_sim.py`'s COVERAGE PASS section beside the clause it reads, with
the item text frozen in `tests/fixtures/frozen/passive_coverage/`. This is the
precondition PR #104 named for pricing passives inside `efficiency`; it does
not build that.

**It did not buy readable verdicts, and that is the honest headline.** Measured
on the restored 94-god set (the first measurement was taken on the damaged
40-god one and said +1/+1/+3, which was an artefact):

    mode       judged   readable before   after   delta
    Conquest       87                45      44      -1
    Joust          87                43      44      +1
    Arena          87                40      39      -1

Net **-1 of 261** judged god-modes. Nine god-modes moved: four gained
(Ganesha in Conquest and Joust, Ares and Amaterasu in Joust) and five lost
(Cu Chulainn in all three modes, Kuzenbo in Conquest and Joust).

**What it DID buy is the thing worth knowing, and it is measurable: coverage
work on this comparison is finished.** Across all three modes, the number of
blockers still absent from `passive_sim` is **zero**. Every remaining withheld
verdict is blocked by an explicit REFUSAL or a PARTIAL:

    Conquest (43 withheld)   Tekko-Kagi 22 · Runeforged Hammer 5 · Stampede 4 · Erosion 3
    Joust    (43 withheld)   Toxic Blade 20 · Erosion 12 · Runeforged Hammer 5 · Tekko-Kagi 5
    Arena    (48 withheld)   Magi's Cloak 25 · Mantle Of Discord 22 · Toxic Blade 14 · Erosion 13

So §4.30's conclusion — reached there for Carry, on 18 gods — now holds for the
whole comparison, in every mode, as a counted fact rather than an inference.
**No amount of further simulation work can move these verdicts.** The only
levers left are the four §4.30 named (give the comparison a movement
dimension, compare the shipped `core` instead of `model`, accept a sample that
is not role-balanced, or accept a wider gap), and all four are Jacob's.

**Why the sign is negative, exactly.** Ichor's own coverage barely moves — its
builds were already full of simulated items — so the pass almost entirely
lifts the COMMUNITY's side. That helps when it lifts the community toward
Ichor and hurts when it lifts the community PAST Ichor to 100%:

    gained   Ganesha   Support   community 0.6678 -> 0.8339   against Ichor 0.8345   gap 0.1667 -> 0.0006
    lost     Kuzenbo   Support   community 0.8356 -> 1.0      against Ichor 0.8345   gap 0.0011 -> 0.1655
    lost     Cu Chulainn Solo    community 0.8339 -> 1.0      against Ichor 0.8247   gap 0.0091 -> 0.1753

Both losses are one refused item on Ichor's side against a community six with
none: **Cu Chulainn holds `Runeforged Hammer`** (refused, crowd control) and
**Kuzenbo holds `Erosion`** (refused, no enemy shield). Ganesha gains because
BOTH sides end up holding exactly one refusal — his `Erosion` against the
community's `Stampede`. A verdict is now readable precisely when the two sides
hold comparable REFUSED gold, which is a sharper and more honest statement of
what this comparison can read than the old mixture of refusals and absences.

**PR #102's fragile trio is unaffected, and this time that is tested.** Kali,
Susano and Nemesis read identical verdicts and identical coverage gaps before
and after, in all three modes. The earlier claim that they were safe was made
when none of the three was even in the damaged comparison set.

**Two things recorded for whoever builds option (a).**

- **Nine of the 33 simulate to a small number because the comparison has one
  target.** `Bumba's Spear`'s whole on-hit payload lands on enemies AROUND the
  target; `Oni Hunter's Garb` reads one of its three stacks; `Mystical Mail`'s
  and `Void Shield`'s range scaling has no distance to read. Each is a
  DECISION with its reason written beside it, which absence was not — but none
  is a claim about the item in a real game. Pricing a cleave from here will
  under-credit it exactly as the old table over-credited the absent, so read
  `assumptions`, never the number alone.
- **PR #104's supersede rule is recorded and NOT applied, as that PR asked.**
  Eight pool items are priced by a shipped `efficiency` flag *and* simulated
  here (Book of Thoth, Brawler's Beat Stick, Eye of Erebus, Nimble Ring, Rod
  of Tahuti, Sun Beam Bow, Transcendence, The Executioner), and this pass adds
  more of the same shape — every `_adaptive` grant it introduces is an item
  whose adaptive stat `price_adaptive` already carries. There is no double
  count today, because `efficiency` does not read `passive_sim` at all
  (§4.31's Q2: the importers are `model_audit` and `side_by_side`, both
  diagnostics). Option (a) must make a simulated value SUPERSEDE the
  flag-derived grants for that item, or every adaptive item is counted twice.

### Smaller, well-defined
- **Penetration caps (40% / 50)** — the only unverified combat constant. Needs
  a leveled practice target; `calibrate_combat --plan` will generate the setup.
- **Genie's Lamp cannot be modelled at all.** It has no stats on the wiki and
  no price (`Cost: -1`), and its value is `+0.6% per Level of all Stats from
  Items` — a MULTIPLIER on the rest of the build, which nothing here can
  express. It is in 76% of Aladdin's community builds and is structurally
  unbuildable, and that is the honest state: fixing it needs a value model for
  multiplicative items, not a parser change. Briskberry Acorn was the same
  symptom with a different cause and is fixed (`wiki_parser._stats_from_prose`).
  _Catalogued 2026-09-02 (§4.20, `docs/PASSIVES.md`): the multiplier is class A2,
  exact against a pool-derived reference (891 gold at level 20); what is left is
  that the Lamp has no PRICE, and writing one is a constant._
- ~~**Cu Chulainn and Ix Chel** have empty wiki pages~~ — fixed 2026-08-19.
  Both pages filled in and both scraped clean, so the pool is now 89 of 89.
  Cu Chulainn is a **stance god** (Human / Berserk) and landed all 10 abilities
  across both forms, 8 of them with parsed scaling — the `_section_tables`
  fix earning its keep on a god it was never tested against.
- **Transcendence and the other stacking items don't price.** Their listed
  stats are deliberately below curve because the stacking is the value, so the
  gold model reads them as poor value — Transcendence ranks 25th of 40 for
  Ullr while being his community build's first item. The mirror of the
  `ward-economy` case and the one open expert claim with a clear cause.
- ~~**Threat detection reads wiki ability tags.**~~ — fixed 2026-08-19.
  `threat_kit.py` classifies the scraped ability text instead, and the draft
  now grades a comp on the union of label and measurement: healers 9 → 18 gods,
  lockdown 40 → 48, and **player-made walls** exist as a threat class at all
  (Cabrakan, Odin, Thor, Ymir — no wiki label describes it). The counts say a
  kit *contains* an effect, not how often it lands or how long it lasts; that
  is the honest ceiling on text classification.

---

## 6. Operating it

```bash
cd pipeline
python -m smite.refresh --all            # re-scrape gods, items, community builds
python -m smite.refresh --discover-items # items the cache references but Items/ lacks
python -m smite.recommend --all          # recompute suggested builds
python -m smite.build_index              # rewrite viewer/public/index.json
python -m smite.data_audit               # integrity gate, non-zero exit on findings
python -m smite.validate --check         # regression floor (NOT a tuning target — see §1)
python -m smite.calibrate                # the leakage-free measure (~7 min)
python -m smite.calibrate --control      # just the control (~7s) - run before comparing
python -m smite.calibrate_combat         # the combat gate
python -m smite.expert_review            # replay recorded expert judgements
python -m smite.expert_review --check    # non-zero exit if a resolved claim regressed
python -m smite.doc_audit                # §7's numbers, doc value beside computed
python -m smite.doc_audit --check        # non-zero exit if a §7 figure has drifted
python -m smite.build_quality            # combat.py pointed at whole builds, ours vs community (~4s)
python -m smite.build_quality --god Medusa   # one god, to stdout
python -m smite.build_quality --role Carry    # one role's verdict on its own objective
python -m smite.build_quality --ward-economy  # the `ward-economy` carriers against a core built without them (~20s)
python -m smite.side_by_side             # criterion 2: ours vs community, passives SIMULATED (~40s)
python -m smite.side_by_side --god Medusa    # one god's side-by-side, item diffs and verdict
python -m smite.order_agreement          # does our buy ORDER contradict the community's? (~40s)
python -m smite.order_agreement --sweep  # community_weight 0.00 -> 1.00, with the held-out split
python -m smite.order_agreement --god Medusa   # one god, heuristic order beside the shipped one
python -m smite.model_audit reference    # 10 frozen reference gods: builds + verdicts, exit 1 on change (~15s)
python -m smite.model_audit reference --write  # accept a reference change ON PURPOSE; explain it in the PR
python -m smite.model_audit heldout      # validate metrics on tuning vs held-out gods, delta vs origin/main (~20s)
python -m smite.model_audit passives     # recommended items whose simulated passive never fires (~45s)
python -m smite.model_audit coverage     # what the model simulates -> viewer/public/model_coverage.json
python -m smite.model_audit sensitivity  # SLOW (~15 min): each major weight x0.8 / x1.2, fragile verdicts
```

**The model audit (2026-11-03, `smite.model_audit`).** Checks the model as a
whole system rather than one god at a time; the method and what each part does
NOT claim are in the module docstring. It writes reports and changes nothing.

  * **Every model PR reports the held-out delta, and may lower it by at most
    1 point if it says why** (Jacob, 2026-11-03). Run `python -m
    smite.model_audit heldout` and paste its table into the PR: win-weighted
    coverage and pooled Spearman on the tuning and held-out gods, and the delta
    of each against `origin/main` run on THIS tree's data, so the delta is the
    code and config alone. A held-out drop of up to 1 point (0.01) on either
    metric merges if the PR description explains it; a bigger drop on either
    blocks the merge. The command prints `PASS`, `PASS IF EXPLAINED` or `FAIL`,
    and `--check` exits 1 on `FAIL` only (`model_audit.HELDOUT_TOLERANCE`).
    The first version said "must not lower" at all, which sat against §1 — a
    change can rightly lower a metric whose target is a model input. The split is a hash of the god's name
    (30% held out) and is never re-drawn. **It scores Conquest's base-kit
    `core` only** (coverage) and Conquest item scores (Spearman): Joust and
    Arena have no community record, and `validate` assembles no other build.
    So `heldout` also prints how many frozen reference lines the change moves
    in that scored bucket and outside it, and says NOT SCORED / PARTLY SCORED
    when it moves what the delta cannot see; there the reference builds are
    the guard (2026-11-04). **Read deltas only, never the
    held-out LEVEL against the tuning level:** on 2026-11-03 the held-out
    25 sit at the 2nd percentile of random 25-god draws on win-weighted (0.40
    vs 0.54) and the 94th on Spearman (0.40 vs 0.22), so the halves differ by
    draw, not by tuning. Both metrics still have a model input as their target
    (§1), so this guards against fitting a change to the gods it was looked at
    on; it does not replace `calibrate`, and §1's point — a model change can
    rightly lower the headline — now needs the held-out half to agree.
  * **Ten reference gods are frozen** (two per role,
    `tests/fixtures/frozen/reference/`): every suggested build and the
    side-by-side verdict, all three modes, recomputed on frozen Open Beta 47
    inputs with the live code and `_weights.yaml`. `test_model_audit.py` fails
    when any of them changes; the PR that changes one runs `reference --write`
    and explains each line of the diff. The inputs are frozen so a data refresh
    never moves it (the test gate above would otherwise reject every patch).
    `reference --refreeze` re-captures them and is a deliberate act.
  * The sanity invariants are tests on the same frozen inputs: an item never
    lowers a stat it grants; power rises 2 -> 4 -> 6 (each figure, against a
    reviewed list of ten known drops (twelve until 2026-11-04), and the composite with none); nothing
    NaN, and a zero score only where fit is zero; with the `modes` block
    removed all three modes give identical builds.

`doc_audit` gates the derivable figures in §7 below, and the few `PRODUCT.md`
and `CLAUDE.md` repeat. It **only reads.** The prose in those rows is worth
more than the numbers in them, and deciding whether a number moving is
expected is a human's job, so it prints the row, the doc's value and the
computed value, and stops. Rows it deliberately leaves alone —
counterfactuals, judgements, history — are in its `UNGATED` map with a reason
each, and a §7 row that no check claims is itself a finding, so a new row
cannot arrive unchecked. `--skip-model` drops the three rows needing a model
run, taking it from ~23s to ~4s, and names them as unchecked rather than
passing quietly. The Tests row counts tests, so a commit that adds tests must
move that row in the same commit.

Scraping needs Playwright (`python -m playwright install chromium`).

`data_audit` exits non-zero on any OPEN finding, and as of 2026-11-02 it exits
0. The three standing ones — Blink Rune (`cost: 0`, genuinely free), Genie's
Lamp (`cost: None`; the wiki's `-1` sentinel, Aladdin is given it) and Mote of
Chaos (its whole effect is a `% of all Stats` multiplier) — are recorded with
their reasons in `data/_audit_reviewed.yaml`, matched on item, issue AND
detail, so a changed value is news again and an entry whose finding goes away
reports as `stale-review`. The fourth, Survivor's Sash, was a parser gap and
not a property of the item: its whole stat line is an Adaptive Stat clause in
the Passive cell. `wiki_parser.adaptive_stat` now records that clause as its
own `adaptive_stat` field on all 30 carriers, kept OUT of `stats` so the grant
is still priced exactly once (`passives.adaptive_grants`) and no statless item
— the Sash, Sundering Echo — silently enters the gold fit or the buildable
pool. Doing either is a model change for `calibrate`, not a parser fix.

A god's ABILITY MODS are exempt by shape (`God Specific`, cost exactly 0, no
stats) — Vulcan's five are a kit upgrade the game grants, and without the
exemption every future god with the system would add five permanent findings
to a gate whose value is that a new finding means something.
`scoring.is_buildable` already refuses them for being statless. The test is
`cost == 0`, not merely falsy, which is what keeps Genie's Lamp visible: a Mod
has no price because it is not bought, the Lamp has no price we could read,
and only the second is a fact about our parsing.

**Community slots that are not a target** (2026-11-02, `smite.community_target`).
A community "six" is what players held at the final whistle. Tier-1/2
components (Evil Eye, Sage's Ring, Medal of Defense, Skeggox) fill 72 community
slot-5/6 sightings, and statless relics and god Mods (Blinking Abyss, Sundering
Echo, Vulcan's Mods, Genie's Lamp) are purchases Ichor cannot read. Every
comparison with community builds now drops the first class and counts the
second as its own labelled class: `validate`'s report (its `in score` filter
already excluded both, so its floors are unchanged by construction),
`build_quality` (labelled; combat still runs on the six as bought, because a
five-item comparison is the comparison pages' rework), and the viewer ledger's
"what the community buys instead". `expert_review` compares against expert
claims, not community builds, and is untouched. Nothing the site recommends
reads it — a test pins the import boundary. On 2026-11-02 data: Ichor `core`
shared 207 of 543 community slots (38.1%) before, 207 of 448 scored slots
(46.2%) after; 95 of the 336 old "disagreements" (28%) were never a model
error. `calibrate`'s leakage-free coverage still scores the raw community set
and is deliberately not re-based here — every §4 number is measured on it.

**Two sources, two spellings.** The community source and our item notes
disagree on apostrophes and casing, and a failed join reads as "this god's
players never buy it" rather than as a spelling problem — 22 of 1,566 community
sightings were being dropped that way. `notes.canonicalise_community_items`
folds them at INGEST so exactly one place knows, and everything downstream
joins on one spelling. It only rewrites on an exact folded match, so a
genuinely new item still reaches the untracked detector.

**Adding a new item is manual by design.** `refresh_all` only re-pulls what
already has a note, so nothing can learn an item exists. Two detectors close
that loop and both should stay green: `--discover-items` scans the wiki cache,
and `data_audit` flags any item a community build names. Twelve items were
missing before those existed, including the pool's first anti-heal item.

**Item and god STATS of what is tracked refresh themselves** (2026-11-02,
`smite.stats_refresh`, on the daily job after `patch_feed`). Due when the game
patch (Steam feed) or the wiki's Patch_notes index is newer than `data_patch`,
or weekly; otherwise one request. The wiki signal exists because the Steam
feed's first live run found no patch title newer than Open Beta 26 — recent
posts do not carry the label, so `patch_feed` alone would miss OB47.
First live run, 2026-11-02 on a runner: OB40 -> OB46, 45 gods and 66 items
changed, 317 requests, ~14 min, every gate green. It exposed one parser bug,
fixed in `wiki_parser._stats_from_prose`: an `Adaptive Stat:` clause on a page
with an empty `Stats:` cell was recovered as BOTH stats (Survivor's Sash,
Sundering Echo). That run's data was NOT merged: on it, 14 tests that pin
Open Beta 40 evidence fail (`test_passives` adaptive values and counts,
`test_passive_catalogue` — Blinking Abyss newly buildable and uncatalogued,
Damaru newly repriced — `test_build_quality`'s hand-computed Medusa,
`test_scoring`'s relic set, `test_efficiency`'s penetration columns). They are
evidence, not data checks, and re-deriving them is its own job; the first
scheduled run on `main` after this lands will make the same OB46 change and
turn them red there. The daily job does not run pytest, so nothing stops it.
**Superseded 2026-11-02, same day — see "The test gate" below.** Two
measurements made it possible and they reverse half of the paragraph below.
From a GitHub runner, the wiki challenges a spoofed-Chrome User-Agent (403
`cf-mitigated`) and serves an honest bot UA (200) — so no browser is needed;
and robots.txt disallows `/*api.php`, so it reads article pages only. It is
all-or-nothing: every tracked page is fetched and parsed into memory, one
fetch failure, parse exception or `ParseCollapse` writes nothing, aggregate
coverage and null/numeric checks run against the data being replaced, and
the notes are swapped in by directory rename before `data_from` is set. The
Ullr/Artio/Merlin kit blanking below is a refusal on this path, not a silent
write — it is a test. Roster growth stays manual for the first reason below.
Evidence and rules are in the module docstring.

**Adding a new GOD is manual for a second reason, and it is stronger.** The
same `refresh_all` limitation applies — it would never have found Ravana — but
scheduling the wiki scrape would also be unsafe, and that is measured rather
than assumed. `wiki_parser.parse_god_page` raises on exactly one thing, a
missing infobox; every other shape change degrades to empty, and
`notes.merge_god_note` REPLACES the note's frontmatter, so a silent parse miss
does not fail to update — it overwrites the only copy. Blanking the kits of
Ullr, Artio and Merlin (the three this happened to, see `_section_tables`
above) and recomputing their cores moves win-weighted coverage 0.5530 ->
0.5552, UPWARD, PASSes `validate --check`, and produces zero `data_audit`
findings. So the scrape of TRACKED notes stays guarded and the detection is
automated (new entities are now added unattended, whole or not at all — see
§6, "New gods and items"): `smite.wiki_watch` runs daily, reads two pages, writes nothing, and
opens one reusable issue. Be wrong toward missing data, never toward wrong
data — a missing god is self-announcing and costs one command, a silently
emptied kit is invisible and moves every core it touches.

**A scrape that shrinks a note is refused, not written.** `refresh.ParseCollapse`
fires when a god's ability count drops (zero always, including for a god nobody
has scraped before — no god page has an empty kit) or when an item loses every
stat or a readable cost, and it prints both sides: `Ullr: 4 abilities -> 0`. The
override is `--allow-shrink`, deliberately NOT `--force`: `--force` means
"ignore the HTTP cache" and a patch-day operator passes it every run, so folding
the two would disable the guard exactly when it matters. `data_audit.audit_gods`
carries the same rule as `no-abilities` / `no-scaling-abilities`, for a note
that got in before the guard existed.

**The snapshot store is a change log, not a calendar.** `patch_notes` is a diff
between two item-stat snapshots, and it was `[]` from the day the page shipped
because `write_snapshot` had one caller — `refresh_and_deploy`, a manual
command. The daily job now runs `smite.snapshots` before `build_index` (the
index READS the store; banked after, a note ships one refresh late). It writes
only when item stats moved: `build_patch_report` keeps 5 consecutive pairs, and
since item stats are wiki data while the daily job pulls SmiteBrain only, an
unconditional write would bank an identical file every morning and bury any
real change under five empty periods within a week.

**A period is a patch only if the ITEM DATA moved patch.** Each `patch_notes`
period carries `patch_from`/`patch_to`, `crosses_patch`, automatic
`highlights` and, for crossing periods only, an `official_url`.
`data/_patch_history.json` keeps two dates per label: `first_seen` (the game
moved; written unattended by `smite.patch_feed` from Steam's announcement feed
on the daily job) and `data_from` (wiki item data first scraped under it;
written only by `refresh_patch_version`). Periods are attributed by
`data_from`, so a game patch with no wiki refresh behind it does not relabel a
period — August's dataset expansion stays "within Open Beta 40". `data_from`
is now written unattended by `smite.stats_refresh`, only after its write lands.
`data/_patch.json` is derived from the history: `patch` is the game label the
viewer prints, `data_patch` is what `wiki_watch` compares the wiki against.
Links come from the Steam post (`official_url` on the row) and
`data/_patch_links.yaml` overrides them. **Not yet verified live** — the
session that wrote `patch_feed` could not reach Steam; its fixture is
constructed. Gods are still not snapshotted. The rules and reasons are in the
`snapshots.py` and `patch_feed.py` docstrings.

**The passive catalogue lives in `data/_passive_classes.yaml`** — one entry per
buildable item with passive text, classes per clause, `priced` per clause;
`test_passive_catalogue.py` fails if the pool and the file disagree or if a
`priced` claim does not match what the shipped flags reprice. A carve-out that
ships must update it. `docs/PASSIVES.md` is the argument.

**Tuning lives in `data/_weights.yaml`** — signals, role stat maps, kit blend,
hybrid scaling, flavors, aspects, per-mode overrides, lifesteal/stat caps,
cap overflow, passive pricing, draft overlay, build order, starters. Every
off-by-default experiment (`magnitude_fit`, `damage_fit_blend`,
`price_passives`) is a §4 entry with its numbers in the file, and every
default-ON one (`price_crit_multipliers`, `price_conversions`,
`price_adaptive`) carries the sweep that put it there.

**Use `npm run build`, not `tsc --noEmit`** — the latter misses errors that the
project reference build catches.

Tests: `cd pipeline && python -m pytest smite/tests -q` (1466) ·
`cd viewer && npm test -- --run` (980).

**A test that reads the live community window never pins a value the window moves daily** (2026-11-07): counts, `window_end`, ratios and verdicts are asserted as invariants, and only what moves at a patch boundary (`window`, `window_start`) is pinned, so moving one declares a new window established — the rule, the evidence and the declaration checklist are in `pipeline/smite/tests/live_window.py`.

Scheduled: `.github/workflows/refresh-data.yml` (09:15 UTC, SmiteBrain +
patch feed + wiki stats when due + snapshot + reindex, then one open data PR
a day that auto-merges once the suite passes) and
`watch-wiki.yml` (09:45 UTC, `smite.wiki_watch`, `contents: read`, commits
nothing). `probe-stat-sources.yml` is dispatch-only and re-checks which stat
sources a runner can reach. New gods and items are added by the daily job too
(`smite.new_entities`, below); `--refresh` by hand is now only for a page the
unattended path refused.

**New gods and items (2026-11-02).** `smite.new_entities` runs on the daily
job after the stats gate. It adds any god on the roster grid, or item on the
Items index, that `data/` does not track: whole or not at all (a page missing
infobox fields, abilities, a scaling ability, or real base stats is left out
and logged; Nox's pre-release page, every base stat 0.0, is the live example),
an unclassified passive as `uncatalogued` in `_passive_classes.yaml` (stat-only
by construction, flagged in the viewer), and behind the suite plus `validate
--check` and `calibrate_combat`, with an entity that turns a check red bisected
out and the rest kept. Log: `data/_new_entities.json`. This answers the
wiki_watch argument above — the danger was overwriting a good note with an
empty one; a NEW entity has no note to lose, so a bad parse can only be
refused. The evidence is in the module docstring. A test that pins a roster
or pool COUNT would keep every new entity out, so none may (the one that did,
`test_damage_value`'s `== 79`, is now the invariant it stood for).

**The test gate (2026-11-02).** A wiki stats refresh is kept only if the
whole pytest suite still passes on it. `smite.stats_gate save` sets the
owned files aside before `stats_refresh`. `check` then recomputes on the new
stats and runs the suite. A test that fails on the new stats and passes on
the old restores the old ones (the history and refresh state included, so
the next run is due again). Each such test is printed as `::error::`, the
community data still commits, and the run fails at its last step. It fails
closed: a crash, a missing report or a timeout is a rejection. The argument
is in the module docstring. That only works if the tests don't pin a patch,
so the fourteen above were reworked rather than re-pinned. Arithmetic now
reads Open Beta 40 inputs frozen in `tests/fixtures/frozen/` (see
`tests/frozen.py`), each next to an invariant over the live data. The passive
catalogue classifies a reshaped passive by `variants:` with a `match:` on
the live text, so it is right on two patches at once. Expert-review
baselines carry `verdict_patch`, and the job prints `expert_review --check`
as an advisory step. On the OB46 data PR #66's run produced, the suite is
green with two warnings that a human should read:

  * Eye of Providence is back in 4 of 36 support cores (Atlas, Charon, Sobek,
    Ymir). **Diagnosed 2026-11-02: real, re-baselined to `partial` for Open
    Beta 46.** Two game changes did it, both on its neighbours: Shifter's
    Shield was nerfed (+100g, −100 Max Health), and six items gained Mana
    Regen, which repriced the mana columns and cost Breastplate of Valor 62g
    of value. Reverting those two groups alone takes it back to 0/36. The
    counterfactual table is in the claim's note in `_expert_reviews.yaml`.
  * The penetration columns converged from 1.9x to 1.39x (49.9 vs 35.9
    gold/point). **Diagnosed 2026-11-02: real, and it changes no build.**
    That warning reads the fit with every pricing flag OFF. The shipped fit
    went 1.26x → 1.10x (54.9/43.6 → 51.3/46.5). The percentage side fell
    because Titan's Bane (−250g) and Obsidian Shard (−150g) got cheaper with
    the same stats. Most of the flat side's rise is The Crusher losing 25 Echo
    for −50g. The fit can't see Crusher's passive, so the price it has left
    over lands on its thinnest column. That is the standing passives-at-zero
    property (§4.5), not a new artefact. No single item anchors either column
    on OB46: the leave-one-out range is [43.0, 48.8] flat and [48.8, 55.1]
    percent. Raw OB40's own 1.9x had a leave-one-out range of [1.48, 2.34],
    so it was never a stable reference. Pinning both columns back to OB40
    prices on OB46 data changes **0 of 90** Conquest cores. No code was
    changed for either shift. **Fixed 2026-11-02: the check now reads the
    shipped fit.** `efficiency.penetration_split` applies `_weights.yaml`'s
    pricing flags and warns only when the shipped `Penetration %`/`Penetration`
    ratio is at or below `PENETRATION_SPLIT_FLOOR = 1.0`. Shipped: OB40 1.26x
    (leave-one-out [1.18, 1.38]), OB46 1.10x ([1.05, 1.20]); both frozen in
    `tests/fixtures/frozen/`. 1.0 is not fitted between them. It is the point
    where a percent point is priced no dearer than a flat one, which is wrong
    against any target above 100 protections, and it sits under OB46's whole
    leave-one-out range. Above it the ratio is a property of the item set, and
    1.10 → 1.26 moved no core. The raw ratio stays in the message as
    information only and never warns. The derivation is next to the constant.

Two of the fourteen were not test pinning. **Blinking Abyss was never newly
buildable.** `_stats_from_prose` read `Deal 25 (+10% Strength &
Intelligence)`, a damage ratio, as `Strength: 10%`, and that one phantom stat
is all that made it pass `is_buildable`. Scaling parentheticals are now cut,
so it is statless again, as on every earlier scrape. **Damaru** is a real
rework: it became an Adaptive Stat item, which the flags now price. Six more
catalogued passives changed shape on OB46 without failing anything, and they
were reclassified along with it.

**Steam's feed, measured (2026-11-02).** `probe-steam-feed.yml` recorded a
real GetNewsForApp response from a runner (`tests/fixtures/recorded/steam/`).
Since January 2026, titles carry no patch label. The label is in the body,
as a `smite2.com/news/open-beta-NN-update-notes/` link (OB22–33), a heading
(OB37) or prose (OB26, OB44). `patch_feed` now reads title, then link, then
body, and finds 14 labels in that response, every one in game order and on
the same day as the hand-recorded history where they overlap. Steam is
still the weak source. Its newest post is 2026-10-06, and its newest
LABELLED post is OB44, while the game is on OB46. Hi-Rez no longer announces
every patch there. The wiki's Patch_notes index stays the primary due
signal, and `stats_refresh` logs a `[patch sources]` cross-check against
`data/_patch_feed.json` every day.

---

## 7. Current numbers

| | |
|---|---|
| Gods tracked | 95 of 98 on the roster (2026-11-03; 99 on 2026-11-02 — the roster count fell by one upstream). Ravana was added by hand 2026-08-29; Nike, Hachiman, Kuzenbo and Hel were the first added unattended, by `smite.new_entities` on a runner. The other five are on the grid without a usable page: Kumbhakarna, Heimdallr and Maman Brigitte 404, and Nox's pre-release page reads every base stat as 0.0, so it is refused until it fills in. The grid leads the wiki's own content, so this row reads N of N+k by design. `data/_new_entities.json` says which are waiting and why |
| Items | 228 |
| Build groups | 285 (95 gods × 3 modes) |
| Build flavors | core, model, hybrid, burst, bruiser, anti-tank, attack-speed, cooldown, crit, strength, intelligence, str-int, mana-stack |
| Conquest gods placed | <!--now-->95 / 95<!--/now--> (2026-11-06, the #117 refresh to the OB47 window, which changed no code, weights or tags). Was 94 / 95: Nox had no community matches in the OB46 window and has 406 in this one, enough for a band (C). Tracks the DATA |
| Joust / Arena gods placed | 0 / 95 — no outcome data exists |
| Items placed | <!--now-->189 / 228<!--/now--> (2026-11-06, the #117 refresh alone — it changed no code, weights or tags). The window reset at the Open Beta 47 boundary and is three days deep, 2,859 matches against the 14,667 the OB46 window closed on (see Community sample), and 39 items carry no tier band where 12 did. Was 216 / 228 (2026-11-03). Earlier, 210 / 226 — the community window kept rebuilding (see Community sample): 888 → 2,301 → 3,498 → 8,200 → 16,223 matches, and 2 more items crossed into enough sightings to earn a tier band since the 8,200 reading. Still below the 226 the pre-reset thirteen-day window placed, and now only 16 short of it on roughly the same depth of sample. Tracks the DATA, not the model |
| Community sample | 2,859 Obsidian+ Conquest matches, 3 Nov – 6 Nov (2026-11-06, OB47). The window RESET at the Open Beta 47 boundary; the OB46 window it replaced closed at 14,667 matches over 20 Oct – 3 Nov, so this one is running at a comparable rate (about 950 a day against about 1,050) and is simply three days deep. The rest of this row is the 25 Aug – 7 Sep window's history (16,223 matches then) — the upstream window is still the one that RESET on 25 Aug (§7's previous entries), now fourteen days deep against a peak of 18,716 on thirteen, so it has very nearly rebuilt. Four more `chore(data): daily community refresh` commits (68744e5, 0e5d8f1, f8e4174, d5ead22) landed since the 8,200/seven-day reading, alongside the 09-03 E and F merges. **THE ATTRIBUTION IS NOT THE USUAL `touches only data/` CHECK THIS TIME, BECAUSE THIS TIME IT WOULD BE FALSE** — E and F moved `scoring.py`, `_weights.yaml`, `doc_audit.py` and `build_quality.py`. It was done directly instead: rebuilding every suggested entry at HEAD from `data/` reproduces **all 2,479 of them, byte-identical to `viewer/public/index.json`**, so no figure below this row moved on a model change. The single live weights key E added, `unknown_win_shrink: 0.0`, is short-circuited inside `scoring.god_unknown_win_rate` before it reads anything; it still moves the input fingerprint, which hashes the parsed weights, so a fingerprint change across this window is not by itself evidence the data moved. No patch boundary — `data/_patch.json` is unmoved at Open Beta 40 |
| Headline gate | coverage 47.6%, win-weighted 51.6% (2026-11-06, the #117 refresh to the OB47 window and nothing else — #117 changed no code, weights or tags; coverage −1.4pp and win-weighted +1.2pp, opposite directions on one data move; NOT a tuning target, §1). Before that, 49.0% / 50.4% (2026-11-04, OB47, after the parse-and-leak PR — all of it the per-ability damage parse, since `validate` scores only the blended Conquest `core`; NOT a tuning target, §1). Before that, 49.1% / 50.2% (2026-11-03, after #82–#91). Before that, 51.9% / 53.4% — down −1.1pp/−1.5pp off the 53.0%/54.9% this row carried at fingerprint `047109f54fd7`, on the data move above and nothing else (the rebuild check in Community sample is what says "and nothing else"). It moved the other way on the previous refresh and the same sentence applied then: both targets are model inputs (§1), so neither direction is a verdict on the model |
| **Leakage-free** | **39.2% probe · 36.4% at eff 0.45, vs 5.8% chance = 6.3–6.7×** (2026-11-06, input fingerprint `564aa7a9d6a9` — moved by the #117 refresh to the OB47 window alone, which changed no code, weights or tags: −2.1pp at the probe and −2.0pp at eff 0.45, the two splits moving the same way this time. The 5.8% now holds at the digit in closed form too: `exact_random_core_baseline` reads **5.7565%** off a pool of 95 gods and 228 items. Re-measured 2026-11-07 at `713cb427c4da` after #119, which added `draft.answer_keep` to `_weights.yaml` — a key the fingerprint covers and this probe never reads — and every figure in this row, the split below included, is identical to the digit.) **OB47 FIRST LOOK — a label for provenance, not a claim of quality:** these figures, and the split that follows, are the first measurement of the shipped model on the OB47 window, taken 2026-11-06 before any decision was judged on it. Split by `model_audit.split_of`, the probe reads 44.1% on 69 gods (vs 5.7% chance, 7.7×) and 26.4% on the other 26 (vs 6.1%, 4.4×); the chance figures are the 200-draw sampler's. **The two halves are a hash split by name, not a generalisation test.** `split_of` arrived on 2026-11-04 (`d0c1d590`), and the efficiency and fit constants that set this probe's score were judged on every god in the pool before then, so neither half was held out from them and the gap cannot be overfitting. (This row first called the halves "tuning" and "held-out", which invites that reading.) Nor is the gap noise. Shuffling the labels 20,000 times at fixed group sizes puts 17.7pp at 2.97 sd from zero (two-sided p 0.003), and it held on OB46's closed window, five times deeper, at 13.3pp (44.8% vs 31.5%; 25 gods because Nox had no matches; p 0.028). Danzaburou, Medusa and Sun Wukong sit at 0% probe coverage in both windows. What the gap records is WHERE the community-free model's six persistently disagrees with the community's, not which side is right there: no data here has build-level outcomes to settle that. The shipped blend shows 7.8pp (p 0.15) on OB47 and 9.2pp (p 0.11) on OB46, because win and pick lift agreement evenly across gods. `model_audit heldout` is unaffected: it compares each half against `origin/main` on the same split, so which gods the hash drew cancels. A figure taken on this window after a decision has been judged on it is a different measurement, to quote beside this one and never in its place. Before that, 41.3% / 38.4% vs 5.8% = 6.6–7.1× (2026-11-04, OB47, fingerprint `949b3b576a90` — moved from `a4b1a66d8c0d` by `_weights.yaml` edits alone, the data is the same; +0.4pp on both splits, all of it the per-ability damage parse, as the model-leak, converter and Joust-share changes read 0.0 here; before that 36.6% / 37.2% vs 5.8%; 41.3% / 37.1% on the 25 Aug – 7 Sep window) — **this level is not fully leakage-free and §4.23 says by how much**: a shipped pricing flag reads a constant measured off the community record, worth about −2.6pp of the first figure and −0.6pp of the second as measured on the 2026-11-04 inputs, which put the multiple nearer 6.7× at the left-hand corner then (41.3%); not re-taken on the OB47 window. It moves the level, not any verdict. — **re-measure with `python -m smite.calibrate --control` (~7s) before comparing anything to this row; if it prints a different input fingerprint, this row describes different inputs — including because someone edited `_weights.yaml`, which the fingerprint also covers.** Re-measured 2026-09-07 at input fingerprint `339839d1a880`, moved from `047109f54fd7` by four `chore(data): daily community refresh` commits AND by `unknown_win_shrink: 0.0` landing in `_weights.yaml` — the fingerprint cannot tell those apart, and the second is a no-op the flag short-circuits (§4.26), so the −2.6pp read here would have been misattributed by a fingerprint change alone. The two splits moved in OPPOSITE directions on the same data, 40.9% → 41.3% at the probe and 37.6% → 37.1% at eff 0.45, which is why this row states both and not their average. Previously measured 2026-09-02 at `9f722a7ad5c8`, reading 40.9% / 37.6%. The random-core baseline is unchanged at the digit: `exact_random_core_baseline` is **5.7391%**, off a pool of 90 gods and 226 items, so the 5.7% printed is real agreement and not the ±0.15pp wobble §1 warns about needing to check for. Re-checked 2026-11-04 at input fingerprint `db3f6bb49ee5` with the ally gate in (both splits still 37.0% / 37.6%), where the SAMPLER printed 5.8% and the exact form reads **5.7498%** — so 5.7% still stands. The exact figure did move, from **5.6744%** with the gate off, and for once that is not the wobble: the gate SHRINKS each non-qualifying god's candidate pool by up to four items, and chance is pool-ratio, so a smaller pool really is likelier to hit a community item. It is the one kind of change that legitimately moves this number, which is why the closed form and not the sampler was used to decide the digit did not change. Coverage and this probe again moved in opposite directions on the same data move (headline gate down, this row's probe up), which is what §1 says a metric with the community's own build as a target will do and is not a reason to prefer either reading |
| Adaptive pricing | 8 buildable items repriced, 4 of 8 stop reading `premium`, and **83 of 89 Conquest cores change** — none of them by gaining one of the eight. See `price_adaptive` |
| Cap overflow | 47 -> 0 of 2564 builds over the penetration cap (2026-11-06, the #117 refresh to the OB47 window alone, which changed no code, weights or tags). **0 DOES NOT MEAN §4.28's DEFECT IS FIXED**: `hybrid.hybrid_core` still re-assembles without `overflow_args`, and none of the 11 hybrid builds this window produces happens to cross the cap. The denominator fell by exactly the hybrid count, 48 to 11, on a window a fifth as deep; the 2,553 non-hybrid entries are the same at both commits. **A CORRECTION TO THIS ROW AS IT STOOD: its figure, 2 of 2601, was right and its prose was stale.** The two builds over at `fd10141c` were Anubis / Conquest / `hybrid` and Anubis / Joust / `hybrid`, bare kit, 45% percentage penetration each against the cap of 40 — both hybrids, so both §4.28's defect — and Morgan Le Fay had no hybrid build at that commit. The "THE 1" and Morgan Le Fay sentences below describe an earlier reading of 1 that the row's figure had already moved past. Before that, 2 of 2601 (2026-11-04, OB47; 2553 -> 2577 is the per-ability damage parse moving flavor eligibility, +8 tabs net per mode, none of them over; 2550 -> 2553 is Ares gaining the `strength` flavor in three modes when his kit first parsed; the 3 new ones were not investigated in this pass — §4.28's defect accounted for the 1 below). **At that earlier reading: THE 1 IS A DEFECT AND IT IS LEFT READING 1 ON PURPOSE — §4.28 has it.** History first: `cap_overflow` took the original 47 to 29; `price_adaptive` reshaped enough cores to clear the rest — measured, not designed — `offmap_efficiency` at 0.55 put three back (3 of 2390, 2026-08-29), and the post-reset window took it to 0 of 2433. The one build over at that reading was Morgan Le Fay / Conquest / `hybrid` / Aspect of the Cursed Crown, at 45% percentage penetration against a cap of 40. It is over because **the `hybrid` archetype is the one build the charge has never been wired into**: `recommend._build_entry_set` passes `overflow_args` for `core`, all eleven flavors and `model`, and does so for the bare and the aspect entry set alike, but `hybrid.hybrid_core` re-assembles through `assemble.assemble_core` with `stat_caps` and coherence only. Aspect builds DO consult the cap; this archetype does not, and has not since the flag shipped (2026-08-21) one day after that call last moved. **This also retires the standing puzzle this row used to carry** — "the count fell while the sample grew, and this file has no mechanism for it". There is one: non-hybrid suggested entries were exactly 2,406 at every commit checked from 2026-08-29 to the day this sentence was written (2,553 at both `fd10141c` and `d1c6f091`), so the whole denominator is 2,406 plus however many hybrid swaps fire, and that tracks how deep the community window is. 2,433 -> 2,479 is 27 -> 73 hybrids and nothing else. See `cap_overflow` and §4.28 |
| Combat model | 0.0% worst case over 12 observations |
| Gods at 0% coverage | 6 — Ah Puch, Athena, Atlas, Cernunnos, Gilgamesh, Mordred. (2026-11-06, the #117 refresh to the OB47 window alone, which changed no code, weights or tags; recorded, not investigated.) Each of the six has 5 or 6 community pairs and matches none, so one item either way moves a god on or off this row. Cernunnos is the only one carried over: Cupid, Guan Yu and Mercury now read 20%, 60% and 20%, on 5 pairs each. CHECKED THAT THIS IS REAL: all 95 gods are in `validate.compute`'s per-god denominator. Before that, 4 — Cernunnos, Cupid, Guan Yu, Mercury (2026-11-03, OB47; not investigated in that pass). On the 25 Aug – 7 Sep window it was 1, Mercury: The community window rebuilding (see Community sample) took Khepri off it, to 20% coverage; Mercury is the one god that crossed into it fresh, at 0.0% coverage and 0.0% win-weighted (`n=5` pairs, none matching). That is the third consecutive refresh window in which the single occupant of this row has been a different god — Ares/Yemoja, then Khepri, now Mercury — which is the strongest available sign that this row tracks the DATA and not the model. CHECKED THAT THIS IS REAL: all 90 gods are still in `validate.compute`'s per-god denominator, so nobody left by dropping out of the measure, which is the failure mode this row would otherwise hide |
| Expert claims | 4 recorded · 3 resolved · 1 open (1 open by decision) |
| Item effect-tag coverage | 132 of 140 buildable tagged · 8 reviewed, no tag warranted · 0 unreviewed |
| Tests | 1466 pipeline · 980 viewer |

Regenerate the first two blocks with `validate.compute` and `smite.calibrate`;
do not hand-edit them.
