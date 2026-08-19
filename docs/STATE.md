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
```

Chance is ~5.9%. Shipped is ~36%, i.e. **~6.1× chance**. That is the number to
quote and the number to move. Headline coverage moving the other way is
expected and is not by itself a reason to revert — that judgement is what
`efficiency.efficiency_pool` and `scoring.lookup_rates` both record.

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
| Relics can't take one of the six core slots | `scoring.is_buildable` | The game gives them their own slot |
| God-specific items are buildable for their owner only | `scoring.is_buildable` | Aladdin's lamp is in 77% of his builds and unbuyable for the other 86 gods |
| Hybrid scalers may build off-type items | `scoring.is_hybrid_scaler` | Neith takes 55% of her ability damage off Intelligence; the label is one word, kits are not |
| Community rates read slot picks **and** alternates | `scoring.lookup_rates` | Slot-only made an item bought 27% of the time read as "meta doesn't buy this" |
| `unknown_win_rate` stays at 0.5 | `scoring.UNKNOWN_WIN_RATE` | It is *not* neutral (observed mean 0.556) but the only metric that responds to changing it is the circular one |
| Draft blocks duplicates per **team**, not per board | `useDraftResult.takenFor` | Only ranked Conquest drafts globally-unique picks; Joust and Arena are not draft modes |
| A draft bonus is damped when the core already covers that **tag** | `draftBuild.adaptedCore` | Same judgement `ally_covered` makes about a teammate; tags only, because a stat is a quantity not a job |
| Stat conversions are priced against a **typical** build | `passives.conversion_grants` | One pass, no fixed point; prices the deterministic case right and the self-referential one conservatively |
| A conversion is priced only into a stat the item **already sells** | `passives.conversion_grants` | Nimble Ring turns Intelligence into a basic-attack channel the god-agnostic fit cannot judge; priced in full it hit 52 cores against 3 community builds |
| Arena and Joust discount **late** items; Conquest does not | `assemble.time_value_multiplier` | Arena's 500 tickets accrue from 0:00 so value is uniform; both Titan modes are back-loaded. Not about affording items — income scales with match length |
| Community pick is **conditional on reaching the slot** | `scoring.SLOT_REACH` | Slot mass decays 0.684 → 0.222 from slot 1 to 6; an item bought sixth was divided by matches that never bought a sixth item |
| Stance gods' abilities live in a **tab wrapper** | `wiki_parser._section_tables` | Ullr, Artio and Merlin reported `n_scaling_abilities: 0` — 28 ability tables the parser walked straight past |
| Eye of Providence carries a **`ward-economy`** penalty | `data/_tags.yaml` | Its stat discount is the ward engine's price tag; 16 Support/Solo cores against 1 community sighting |
| `god_item_scores` ships **one table per mode** | `build_index._god_item_scores` | A mode toggle that changes the label and not the model is worse than none; Eye of Providence sat in Joust cores because the draft was Conquest-scored |
| A threat is the **union** of role label and measured kit | `threats.ts`, `threat_kit.py` | Label alone: `Healing` on 9 of 89 gods. Measurement alone at 1 ability: 42, mostly incidental. Label OR 2+ abilities: 18 |
| Relics are recommended on **their own line**, never in the core | `draft.relics` in `_weights.yaml` | `is_buildable` excludes relics from the six because the game gives them their own slot — a tag bonus aimed at one could never fire |
| The aspect control is an **orange hexagon on the portrait** | `AspectBadge.tsx` | Where SMITE draws it, so it is self-describing; orange rather than gold keeps the Torchlight Rule intact |
| An aspect with no overlay **falls back** to the base build | `DetailPanel.aspectFamily` | 72 gods have an aspect, 7 have a scoring overlay; filtering strictly blanked the model side for the other 65 |

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
3. **Magnitude-aware fit (B4)** — item stat magnitude as a fit term.
4. **Damage-gain as a fit signal (B5)** — halves the gate; it cannot price
   defence at all.
5. **Pricing item passives** — the extraction is right and the prices are
   visibly more sensible; the recommender still got worse.
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

174 of 261 build groups are Joust and Arena. Those modes have no community data
at all, so the recommender falls back to efficiency + fit alone — the
combination measured at 4.9× chance for *finding* items and ≈0 for *ranking*
them. The tier list now admits this; the builds do not, and the builds are the
product. Either find a source with per-mode outcomes, or disclose it on those
builds the way the tier list does.

### The feedback loop has a first version, and it is tiny
Everything else validates against community data, which §1 shows cannot
adjudicate the model's central claims. `data/_expert_reviews.yaml` +
`smite.expert_review` are the first gate here that isn't made of that data: a
strong player's judgements, written down in a shape a script can replay. Four
claims from one reviewer (2026-08-09) — two now resolved, two open.

**It is not a measurement and must never be quoted as one.** One reviewer,
claims chosen because they looked wrong. It answers "did the thing they
objected to change?" and nothing else. The real version of this is still
capturing real games — "I played this build, here's what happened" — and that
remains the highest-value thing left. What exists now is the cheapest possible
stand-in for it, and its value is that judgements stop evaporating when the
conversation ends.

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
python -m smite.calibrate                # the leakage-free measure
python -m smite.calibrate_combat         # the combat gate
python -m smite.expert_review            # replay recorded expert judgements
python -m smite.expert_review --check    # non-zero exit if a resolved claim regressed
```

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

**Tuning lives in `data/_weights.yaml`** — signals, role stat maps, kit blend,
hybrid scaling, flavors, aspects, per-mode overrides, lifesteal/stat caps,
draft overlay, build order, starters. Every off-by-default experiment
(`magnitude_fit`, `damage_fit_blend`, `price_passives`) is a §4 entry with its
numbers in the file.

**Use `npm run build`, not `tsc --noEmit`** — the latter misses errors that the
project reference build catches.

Tests: `cd pipeline && python -m pytest smite/tests -q` (596) ·
`cd viewer && npm test -- --run` (614).

---

## 7. Current numbers

| | |
|---|---|
| Gods tracked | 89 of 89 on the roster |
| Items | 226 |
| Build groups | 267 (89 gods × 3 modes) |
| Build flavors | core, model, hybrid, burst, bruiser, anti-tank, attack-speed, cooldown, crit, strength, intelligence, str-int, mana-stack |
| Conquest gods placed | 89 / 89 |
| Joust / Arena gods placed | 0 / 89 — no outcome data exists |
| Items placed | 220 / 220 |
| Community sample | 17,490 Obsidian+ Conquest matches, 28 Jul – 10 Aug |
| Headline gate | coverage 48%, win-weighted 49% — see `unknown_win_per_god`; the drop IS the removed community-agreement prior |
| **Leakage-free** | **37.5% vs 5.8% chance = 6.47×** |
| Combat model | 0.0% worst case over 12 observations |
| Gods at 0% coverage | 3 — Achilles, Chaac, Danzaburou |
| Expert claims | 4 recorded · 2 resolved · 2 open (1 open by decision) |
| Tests | 610 pipeline · 636 viewer |

Regenerate the first two blocks with `validate.compute` and `smite.calibrate`;
do not hand-edit them.
