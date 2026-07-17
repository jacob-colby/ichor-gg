# SMITE 2 build recommender: signal-weighted item scoring + build assembly

Status: approved, ready for implementation plan
Date: 2026-07-16

## Problem

The reference pipeline (see [2026-07-16-smite-reference-system-design.md](2026-07-16-smite-reference-system-design.md))
now stores structured god/item/build data for a 10-god pool. Jacob wants a
layer on top that does actual computation over that data to answer two
questions:

1. **Which items are underrated or genuinely strong for a given god** — not by
   vibes, but by math where math is possible.
2. **What to build** — a few final suggested builds per god across build-types
   and matchup situations, combining four signals: gold-efficiency math,
   performance (win rate), popularity (pick rate), and god stats/archetype.

The hard constraint that shapes the whole design: **we do not have ability
damage-scaling coefficients.** The wiki infobox we parse gives ability names,
cooldowns, and costs — not "this ability deals 80% of Strength + 15% of missing
health." So true per-god damage simulation is out of scope. The system must be
rigorous where numbers exist and openly qualitative where they don't, and never
fake a coefficient it doesn't have.

## Guiding principle

**Trust comes from transparency, not from false precision.** Every suggestion
carries its reasoning. The system surfaces and explains candidates for Jacob to
test in-game; it is not an oracle. A recommender that is rigorous on
gold-efficiency and honestly labels the tag/fit layers as judgment will earn
more trust than one that emits confident decimals for things it's guessing at.

## Existing data this builds on

Pipeline-owned, already populated under `04. System/Data/SMITE/`:

- **Items** (`Items/<name>.md` frontmatter): `cost` (int, total gold),
  `stats` (dict of stat-name → string value, e.g. `Strength: '45'`,
  `Critical Chance: 20%`, `Intelligence: '75'`, `Penetration: '10'`),
  `passive` (free text), `builds_from`, `builds_into`, `tier`.
- **Gods** (`Gods/<name>.md` frontmatter): `base_stats`, `role`,
  `specializations` (e.g. `Sharpshooter`, `Nuker`), `damage_type`
  (`physical`/`magical`), `abilities` (names + cooldown/cost only), `aspects`.
- **Builds** (`03. Workspaces/Gaming/SMITE 2/Builds/<god>-<mode>.md`): a
  `builds[]` array; the `source: community` entry holds SmiteBrain per-slot
  `pick_rate` and `win_rate`.

Data-shape notes that matter for implementation:
- Stat values are **strings**, some `%`-suffixed (`20%`, `'10'`). Parsing must
  strip `%`/whitespace and coerce to float; non-numeric values are dropped.
- SMITE 2 offensive power is `Strength` (physical) and `Intelligence`
  (magical). This is the basis of the damage-type filter.
- `cost` is the item's **total** build cost — correct for a value regression.

## Architecture

A new set of modules under `tools/smite/`, orchestrated by a `recommend.py`
CLI that runs **after** `refresh.py` (it consumes scraped data) and feeds
`build_index.py` (so the viewer picks up suggested builds). Pure functions with
data in / data out, mirroring the existing pipeline's testable style.

```
tools/smite/
  efficiency.py   → empirical gold-value regression + per-item efficiency tiers
  scoring.py      → four-signal weighted score per (god, item)
  assemble.py     → ranked items → named builds + situational-swap table
  recommend.py    → CLI orchestrator: load data → score → assemble → write
```

Two new **user-owned config files** under `04. System/Data/SMITE/` — the entire
tuning surface:

```
_weights.yaml   → signal weights + role→stat-weighting map
_tags.yaml      → item name → effect-tags (LLM-seeded once, hand-correctable)
```

Both are sidecars, deliberately separate from scraped notes so that
`refresh.py` (which rewrites item/god frontmatter wholesale) never clobbers
human judgment or tuning.

### Layer 1 — Efficiency (hard math)

Derive the gold value of each stat **empirically from the item set itself**,
rather than hand-authoring a "gold per point" table from community lore.

1. Build a matrix: rows = items, columns = every distinct numeric stat, plus
   an intercept. Values = parsed stat amounts (0 where absent).
2. Non-negative least squares regression of `cost` on that matrix →
   `gold_value[stat]`, the marginal gold the game assigns each stat.
   (Non-negative: a stat can't have negative gold value; NNLS avoids
   nonsensical negative coefficients from collinear stats.)
3. For each item:
   ```
   predicted_cost = intercept + Σ (stat_amount × gold_value[stat])
   residual       = actual_cost − predicted_cost
   ```

Interpretation — this *is* the "underrated" detector:
- **residual < 0** (cheaper than its raw stats imply) → an **undervalued
  stat-stick**.
- **residual ≫ 0** → you're paying a premium for a passive/active. Whether that
  premium is worth it is **not** decided here — Layer 2 explains it. The math
  correctly declines to guess.

Small-N honesty: with ~33 items the fit is noisy. Layer 1 therefore exposes a
**tier** (`undervalued` / `fair` / `premium`), computed from the residual's
z-score across the item set, as the primary output — not a false-precision
gold figure. The raw residual is retained for the report but the tier drives
scoring. Tiers sharpen automatically as the item pool grows.

Config knobs (none required; all have defaults): stat-exclusion list (e.g.
ignore pure-utility stats that distort the fit if needed).

### Layer 2 — Effect-tags (calibrated judgment)

Passives and actives carry value the stat regression can't see. A fixed tag
vocabulary categorizes each item's `passive` text:

```
burst · execute · anti-heal · protection-shred · peel · wave-clear ·
mobility · sustain · cc-immunity · aura · anti-crit
```

- **Seeding:** a one-time LLM pass reads each item's `passive` and proposes
  tags into `_tags.yaml`. Output is reviewed/corrected by hand — this is
  explicitly a human-in-the-loop artifact, not scraped truth.
- **Storage:** `_tags.yaml` maps `item name → [tags]`. Sidecar, so item refresh
  never touches it. New items refreshed later show up as untagged and are
  reported as "needs tagging" by `recommend.py` rather than silently scored as
  effect-less.
- **Role in scoring:** tags do two things — (a) *explain* a positive efficiency
  residual (premium justified vs. overpriced), and (b) drive
  situational-swap logic in Layer 3/assembly (e.g. `anti-heal` is force-slotted
  vs. high-sustain comps).

The vocabulary is fixed and small on purpose; an open-ended tag set becomes
unmatchable noise.

### Layer 3 — God-fit (structural, archetype-based)

With no scaling coefficients, fit is **archetype matching, not damage
simulation.** Three deterministic components:

1. **Damage-type filter (hard rule):** physical gods only consider
   `Strength`-primary items, magical gods only `Intelligence`-primary. Neutral
   items (protections, boots, CDR/utility) pass for everyone. This is a filter,
   not a weight — mismatched items are excluded entirely.
2. **Role/spec stat-weighting:** a `role → {stat: weight}` map in `_weights.yaml`
   (e.g. `Sharpshooter` up-weights `Attack Speed`/`Critical Chance`; `Nuker`
   up-weights `Strength`/`Intelligence`/`Penetration`). Applied to the item's
   stats to produce a god-fit sub-score.
3. **Tag-relevance:** tags matching the god's archetype (from role/spec) add a
   small fit bonus (e.g. `execute` for an assassin). Conservative weights —
   this is the softest signal.

Fit is explicitly labeled in the report as archetype-derived so its ceiling is
never oversold.

### Signal aggregation

Per `(god, item)`, a transparent weighted sum in [0, 1]-normalized space:

```
score = w_eff  · efficiency_tier_value
      + w_win  · win_rate            (from community build entry; neutral if absent)
      + w_pick · pick_rate           (popularity)
      + w_fit  · god_fit
```

Weights live in `_weights.yaml` with sane defaults (starting point:
`w_eff 0.35, w_win 0.30, w_pick 0.15, w_fit 0.20`) and are fully user-tunable.
Every term is retained per item for the report, so any ranking is auditable.

**Underrated flag:** `score` high **and** `pick_rate` low (both past
configurable thresholds) → the divergence between "good" and "popular." A
first-class output, surfaced by name.

### Build assembly

Greedy-with-rules (not optimization — transparent and debuggable). Per god:

**Named builds (2–3):**
- **Core:** highest-scoring items filling slots under hard constraints —
  exactly one boots, damage-type-appropriate only, at most one
  lifesteal/sustain item (unless the role reads bruiser), no duplicates.
- **Build-type variant(s):** emitted only when the role supports a real fork
  (hunter → *crit/auto* vs *ability/burst*; mage → *burst/pen* vs
  *poke/sustain*). Single-path roles get one build, not a padded second.
  Variant membership is decided by which stat-cluster an item emphasizes.

**Situational-swap table:** for each situation
(`vs heavy CC`, `vs physical burst`, `vs magical burst`, `vs high-sustain`),
which item swaps into a flex slot and the **tag-based reason**. Here a tag
overrides efficiency by design: vs. sustain comps an `anti-heal` item is
force-slotted regardless of residual. If the god has **no** item carrying the
needed tag, the row says so explicitly ("no anti-heal available in pool") —
silence is a bug, not an answer.

**Underrated highlights:** the flagged divergence items, by name, with tier +
tags.

### Outputs

Both, per the design decision:

1. **Suggested build entries** appended to the god's Build note `builds[]`
   array as `source: suggested`, structured like existing entries
   (`slot_order`, `situational_swaps`, plus an `archetype` label and a
   one-line `rationale`). `merge_build_note` already only ever rewrites the
   `community` entry, so `suggested` entries survive refresh — but that
   function must be extended so `recommend.py` can regenerate the `suggested`
   entry in place (replace-if-present, like `community`) without disturbing
   `mine`. Shows in the viewer, visually distinct from `mine`/`community`.
2. **Analysis report** at `04. System/Data/SMITE/Analysis/<god>.md` — a
   generated, machine-owned "show your work" table: per item, the efficiency
   tier + raw residual, tags, god-fit, win/pick rate, total score, and
   underrated flag. Regenerated each run; not hand-edited.

`build_index.py` is extended to carry `source: suggested` entries into
`index.json` so the viewer renders them. The viewer's existing discriminated
union on `source` gets a `suggested` arm (badge/label only — no new layout).

## CLI

```
python -m smite.recommend --god "Chiron"     # one god
python -m smite.recommend --all              # every god with a build note
python -m smite.recommend --all --report-only  # skip writing build entries
```

Runs after refresh. Reports untagged items encountered. Never network-touches —
pure computation over local notes + config.

## Phasing

The implementation plan sequences so each phase is independently working and
testable, matching Jacob's "gold efficiency first" instinct:

- **Phase A — Efficiency engine.** `efficiency.py` + a `--report-only` path
  that emits just the efficiency tier/residual table per item (god-agnostic).
  Ships and is verifiable alone: does the regression flag known stat-sticks as
  undervalued and known passive-items as premium?
- **Phase B — Judgment layers + scoring.** `_tags.yaml` seeding, god-fit,
  `scoring.py`, the four-signal score and underrated flag. Report now per-god.
- **Phase C — Assembly + write + viewer.** `assemble.py`, suggested build
  entries, `merge_build_note`/`build_index.py`/viewer integration.

## Testing approach

- **Efficiency:** synthetic item sets with known linear structure → regression
  recovers the planted gold values; a deliberately-underpriced item lands in
  the `undervalued` tier; a stat-light passive-heavy item lands `premium`.
- **Scoring:** fixed weights + fixture items → exact expected ranking; the
  underrated flag fires only when score-high/pick-low both cross thresholds.
- **Assembly:** fixture god + scored items → constraints hold (one boots, no
  dupes, damage-type filter, single lifesteal); situational table emits the
  "no anti-heal available" row when the pool lacks the tag.
- **Merge/write:** a `suggested` entry regenerates in place without disturbing
  `mine`/`community`; refresh still preserves `mine`.
- All offline (no live marker) — computation over local fixtures.

## Limitations (stated, not hidden)

- **No damage simulation.** God-fit is archetype-based; it cannot capture
  item-ability combos. A future phase could add scaling coefficients *if* they
  prove scrapable — out of scope here.
- **Effect-tags are opinion.** Calibrated against meta, validated by spot-check,
  not derived. Wrong tags → wrong situational advice; that's why they're
  hand-correctable.
- **Small-N regression noise.** Mitigated by tiering, improves with pool size.
- **Situational logic is rule-based, not opponent-modeled.** It says "bring
  anti-heal vs. sustain," not "how much."
- **Win/pick rate is SmiteBrain high-elo, not pro-scene.** Accepted as the
  performance proxy per the design decision; no separate pro source.

## Open questions — resolved during design

- *"Pro data" source* → use SmiteBrain `win_rate` (already scraped) as the
  performance signal; no new scraping.
- *Scoring model* → transparent tunable weighted sum, not learned/regression
  weights (avoids overfitting thin beta data).
- *Output* → both suggested build entries (viewer) and per-god analysis report.
- *Efficiency baseline* → empirical NNLS regression over the item set, not a
  hand-authored table.
- *Tag/weight storage* → sidecar YAML files, refresh-safe.
