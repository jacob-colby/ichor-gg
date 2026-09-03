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

Reading 1–5 through §1: each made `efficiency` more informative but less like
the community's data, which the gate punishes by construction. That is a
hypothesis, not a proof — but re-running them against the *old* metric will
just reproduce the old answer.

---

## 5. What is actually left

Roughly in the order I would do them.

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

### Why four items that reach no core move forty cores
§4.21's open question, deliberately handed on rather than answered there.
`price_stat_multipliers` gives four relics ~535 gold of priced stat line each;
none of the four enters a core with the flag on, and 40 of 90 Conquest cores,
29 Joust and 50 Arena change anyway, with the intercept moving 934 → 854 and
Strength 21.81 → 22.87 g/pt. `price_adaptive` recorded a gain with the same
shape — "the gain is not the eight items, it is the intercept" — and this is
the same shape with the opposite sign. Whether that is the fit's identifiability
(four relics with a 20-column stat line each), the pool-mean reference vector
spreading a relic's premium across every column, or something else, is not
decided here. Whoever takes it should re-run the sweep with the flag's grant
restricted to the columns the relic already carries (the `conversion_grants`
"amplify only" precedent) as the first arm.

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
python -m smite.order_agreement          # does our buy ORDER contradict the community's? (~40s)
python -m smite.order_agreement --sweep  # community_weight 0.00 -> 1.00, with the held-out split
python -m smite.order_agreement --god Medusa   # one god, heuristic order beside the shipped one
```

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

`data_audit` exits non-zero whenever it has findings, and it currently has
four standing ones — Blink Rune (`cost: 0`, genuinely free), Genie's Lamp
(`cost: None`; the wiki says `-1`, a sentinel meaning Aladdin is given it
rather than buying it) and Mote of Chaos / Survivor's Sash (tier-2 items the
wiki lists with no stats). All four are real properties of the source data,
not defects, and none reaches a build. Treat "4 findings, all of them these"
as green; treat a fifth as news.

A god's ABILITY MODS are exempt by shape (`God Specific`, cost exactly 0, no
stats) — Vulcan's five are a kit upgrade the game grants, and without the
exemption every future god with the system would add five permanent findings
to a gate whose value is that a new finding means something.
`scoring.is_buildable` already refuses them for being statless. The test is
`cost == 0`, not merely falsy, which is what keeps Genie's Lamp visible: a Mod
has no price because it is not bought, the Lamp has no price we could read,
and only the second is a fact about our parsing.

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
findings. So the scrape stays a human's decision and the detection is
automated: `smite.wiki_watch` runs daily, reads two pages, writes nothing, and
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

Tests: `cd pipeline && python -m pytest smite/tests -q` (904) ·
`cd viewer && npm test -- --run` (765).

Scheduled: `.github/workflows/refresh-data.yml` (09:15 UTC, SmiteBrain +
snapshot + reindex, commits) and `watch-wiki.yml` (09:45 UTC, `smite.wiki_watch`,
`contents: read`, commits nothing). The wiki scrape itself is
`smite.refresh_and_deploy`, by hand, on `main`.

---

## 7. Current numbers

| | |
|---|---|
| Gods tracked | 90 of 92 on the roster — Ravana added 2026-08-29, four days after his 25 Aug release, by the manual path `smite.wiki_watch` now points at. The other two the wiki lists, Hachiman and Hel, are roster entries with no page behind them ("There is currently no text in this page"), so the grid leads the wiki's own content and this row will read N of N+2 until it catches up. That is why the watcher triggers on NAMES and a page probe, never on a count |
| Items | 226 |
| Build groups | 270 (90 gods × 3 modes) |
| Build flavors | core, model, hybrid, burst, bruiser, anti-tank, attack-speed, cooldown, crit, strength, intelligence, str-int, mana-stack |
| Conquest gods placed | 90 / 90 |
| Joust / Arena gods placed | 0 / 90 — no outcome data exists |
| Items placed | 208 / 226 — the community window kept rebuilding (see Community sample): 888 → 2,301 → 3,498 → 8,200 matches, and 13 more items crossed into enough sightings to earn a tier band. Still below the 226 the pre-reset thirteen-day window placed. Tracks the DATA, not the model |
| Community sample | 8,200 Obsidian+ Conquest matches, 25 Aug – 1 Sep — the upstream window is still the one that RESET on 25 Aug (§7's previous entries), now seven days deep against a peak of 18,716 on thirteen. Three more `chore(data): daily community refresh` commits (af04139, e910b75, ea3b5e7) landed since the 3,498/three-day reading; `git diff --name-only d957319 HEAD` (the commit that reading was taken at) touches only `data/builds/`, `data/_community_items.json` and `viewer/public/index.json` — no weights, no pipeline or viewer code — so every figure below this row that moved, moved on data alone. No patch boundary — `data/_patch.json` is unmoved at Open Beta 40 |
| Headline gate | coverage 53.0%, win-weighted 54.9% — up +3.4pp/+1.9pp off the 49.6%/53.0% this row carried at fingerprint `052cab0a44cc`, on the data move above and nothing else. Read this as more evidence arriving, not as a verdict — both targets are model inputs (§1) |
| **Leakage-free** | **40.9% probe · 37.6% at eff 0.45, vs 5.7% chance = 6.6–7.2×** — **this level is not fully leakage-free and §4.23 says by how much**: a shipped pricing flag reads a constant measured off the community record, worth about −2.6pp of the first figure and −0.6pp of the second, so the multiple is nearer 6.7× at the left-hand corner. It moves the level, not any verdict. — **re-measure with `python -m smite.calibrate --control` (~7s) before comparing anything to this row; if it prints a different input fingerprint, this row describes different inputs — including because someone edited `_weights.yaml`, which the fingerprint also covers.** Re-measured 2026-09-02 at input fingerprint `9f722a7ad5c8` — moved from `208b8d329f8e` by `build_order.community_weight` landing in `_weights.yaml`, which the hash covers; the two splits read **40.9% / 37.6% at both**, to the digit, with 337 of 810 Conquest builds reordered, because order cannot move a membership measure (§4.24). Previously measured 2026-09-01 at `208b8d329f8e`: the 41.5 · 38.4 vs 5.7 this row carried was fingerprint `052cab0a44cc` and describes the 3,498-match reading, so the −0.6pp/−0.8pp is the three `chore(data): daily community refresh` commits named above and NOT a model change — same diff, same "touches only data" check. The random-core baseline is unchanged at the digit: `exact_random_core_baseline` is **5.7391%** at both fingerprints, off a byte-identical pool of 90 gods and 226 items, so the 5.7%/5.7% printed is real agreement and not the ±0.15pp wobble §1 warns about needing to check for. Coverage and the leakage-free probe moved in OPPOSITE directions on the same data move (headline gate up, this row down), which is exactly what §1 says a metric with the community's own build as a target will do and not a reason to prefer either reading |
| Adaptive pricing | 8 buildable items repriced, 4 of 8 stop reading `premium`, and **83 of 89 Conquest cores change** — none of them by gaining one of the eight. See `price_adaptive` |
| Cap overflow | 47 -> 0, and back -> 0 of 2433 builds over the penetration cap. `cap_overflow` took the original 47 to 29; `price_adaptive` reshaped enough cores to clear the rest — measured, not designed — and `offmap_efficiency` at 0.55 put three back (§7's 2026-08-29 reading, 3 of 2390). The community window rebuilding (see Community sample) moved both numbers again: suggested-build count went 2,479 (post-reset) → 2,433 (Conquest 810, Joust 811, Arena 812) and the three over-cap builds are gone with it. That the count fell further while the community sample GREW is not the direction the Items-placed and Headline-gate rows moved in, and this file does not have a mechanism for it on record — reported as a fact, not explained away. Neither number is a model change: no weights, pipeline or viewer code moved in the commits behind it (see Community sample). See `cap_overflow` |
| Combat model | 0.0% worst case over 12 observations |
| Gods at 0% coverage | 1 — Khepri. The community window rebuilding (see Community sample) took Ares and Yemoja off it, to 20% and 60% coverage; Khepri is the one god that crossed into it fresh, at 0.0% coverage and 0.0% win-weighted (`n=5` pairs, none matching). CHECKED THAT THIS IS REAL: all 90 gods (Ravana now included) are still in `validate.compute`'s per-god denominator, so nobody left by dropping out of the measure, which is the failure mode this row would otherwise hide. This row tracks the DATA more than the model |
| Expert claims | 4 recorded · 3 resolved · 1 open (1 open by decision) |
| Item effect-tag coverage | 130 of 138 buildable tagged · 8 reviewed, no tag warranted · 0 unreviewed |
| Tests | 904 pipeline · 765 viewer |

Regenerate the first two blocks with `validate.compute` and `smite.calibrate`;
do not hand-edit them.
