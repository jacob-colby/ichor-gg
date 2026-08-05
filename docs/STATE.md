# State of the project

_Last verified 2026-08-05, against `main` at the merge of PR #22._

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

Chance is ~6.0%. Shipped is ~29%, i.e. **~4.9× chance**. That is the number to
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

Reading 1–5 through §1: each made `efficiency` more informative but less like
the community's data, which the gate punishes by construction. That is a
hypothesis, not a proof — but re-running them against the *old* metric will
just reproduce the old answer.

---

## 5. What is actually left

Roughly in the order I would do them.

### Two thirds of the shipped builds rest on nothing measurable
174 of 261 build groups are Joust and Arena. Those modes have no community data
at all, so the recommender falls back to efficiency + fit alone — the
combination measured at 4.9× chance for *finding* items and ≈0 for *ranking*
them. The tier list now admits this; the builds do not, and the builds are the
product. Either find a source with per-mode outcomes, or disclose it on those
builds the way the tier list does.

### There is no feedback loop
Everything validates against community data, which §1 shows cannot adjudicate
the model's central claims. The project can currently tell you whether it is
*honest*; it cannot tell you whether it is *good*. The cheapest fix is capturing
real games — a way to record "I played this build, here's what happened" turns
opinion into a second, non-circular gate. **This is the highest-value thing
left and it is not a modelling task.**

### The win signal is a constant for ~95% of the pool
SmiteBrain reports a win rate for a median of **5 items per god** against a
candidate pool of ~95, yet `win` carries the largest weight (0.45). For most
items the signal is a flat offset, and `unknown_win_rate` is a threshold
deciding where the ~5 measured items sit relative to the ~90 unmeasured ones.
It is also what produces the remaining 0%-coverage gods, whose set is
*unstable* — it moved 6 → 4 → 5 across one session's changes. Fixing this needs
a metric that isn't made of the community's build.

### Smaller, well-defined
- **Penetration caps (40% / 50)** — the only unverified combat constant. Needs
  a leveled practice target; `calibrate_combat --plan` will generate the setup.
- **Aspect-conditional stats don't parse.** Briskberry Acorn's stats live in
  prose (`Non-Aspect: 45 Strength … Aspect: 400 Max Health`), so it ships
  statless and unbuildable. Affects god-specific items today; will affect more
  if the wiki adopts the pattern.
- **Cu Chulainn and Ix Chel** have empty wiki pages — nothing to scrape. They
  are in the roster and get picked up automatically if that changes.
- **Threat detection reads wiki ability tags.** A god who is situationally a
  healer without the `Healing` label is not counted.

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
```

Scraping needs Playwright (`python -m playwright install chromium`).

`data_audit` exits non-zero whenever it has findings, and it currently has
three standing ones — Blink Rune (`cost: 0`, genuinely free) and Mote of Chaos
/ Survivor's Sash (tier-2 items the wiki lists with no stats). All three are
real properties of the source data, not defects, and none reaches a build.
Treat "3 findings, all of them these" as green; treat a fourth as news.

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

Tests: `cd pipeline && python -m pytest smite/tests -q` (489) ·
`cd viewer && npm test -- --run` (559).

---

## 7. Current numbers

| | |
|---|---|
| Gods tracked | 87 of 89 on the roster |
| Items | 220 |
| Build groups | 261 (87 gods × 3 modes) |
| Build flavors | core, model, hybrid, burst, bruiser, anti-tank, attack-speed, cooldown, crit, strength, intelligence, str-int |
| Conquest gods placed | 87 / 87 |
| Joust / Arena gods placed | 0 / 87 — no outcome data exists |
| Items placed | 191 / 220 |
| Community sample | 4,952 Obsidian+ Conquest matches, 28 Jul – 1 Aug |
| Headline gate | coverage 48.6%, win-weighted 50.8%, ρ 0.557 |
| **Leakage-free** | **29.2% vs 6.0% chance = 4.89×** |
| Combat model | 0.0% worst case over 12 observations |
| Gods at 0% coverage | 5 — Anubis, Chronos, Danzaburou, Jing Wei, Neith |
| Tests | 489 pipeline · 559 viewer |

Regenerate the first two blocks with `validate.compute` and `smite.calibrate`;
do not hand-edit them.
