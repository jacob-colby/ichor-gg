# SMITE recommender — scoring intelligence, fun builds, and explanation UI

**Date:** 2026-07-22 · **Status:** approved (scope/calibration/fun-build forks decided by Jacob via Q&A)
**Baseline to beat:** coverage 60% · win-weighted 62% · pooled Spearman 0.26 (n=54, 11 gods incl. Ymir)

## Problem

The fit signal (20% of every item score) is broken for most of the pool:

1. `_role_stat_map` does exact-string lookups into `role_stats`, but the scraped
   role/spec vocabulary rarely matches. **5 of 11 gods have an empty fit map**
   (Chronos, Hercules, Ra, Susano, Ymir → fit ≈ 0 for every item). Ymir (Support
   tank) gets mage damage items in his suggested core; his coverage is 25%.
2. **Cernunnos is worse than empty**: his `Nuker` spec injects the mage stat map
   (Penetration 1.0, CDR 0.5) into a physical hunter, pulling him toward
   Jotunn's/Hydra's while the community runs lifesteal + attack speed
   (Devourer's Gauntlet 63% pick). Coverage 25–32%.
3. `god_fit` is archetype-only — it ignores how the god's kit actually scales,
   even though every scraped ability carries `Damage Scaling: X% Strength + Y%
   Intelligence` lines (verified parseable for all 11 gods).
4. The four signal weights (0.35/0.30/0.15/0.20) are hand-guessed, never
   calibrated against the validation metric.
5. No tooling exists to surface *where* we disagree with the community meta, so
   blind spots (like the lifesteal cap fighting Cernunnos's double-sustain
   community build) stay invisible.
6. No off-class "fun" builds: the damage filter and archetype fit actively (and
   correctly, for serious builds) forbid e.g. crit Ymir.

## Goals

- Raise the honest headline metrics (coverage / win-weighted / Spearman) with
  changes proven by the validation harness — no confident-looking noise.
- Encode kit-awareness (ability scaling) into fit.
- Build a disagreement report that turns meta-vs-us gaps into hypotheses.
- Ship clearly-labeled fun off-class builds (crit Ymir et al.).
- Surface the new intelligence in the viewer (why-this-item, fun badges,
  meta-divergence), visually verified via Chrome MCP.

Non-goals: combat simulation; diminishing-returns/breakpoint-aware assembly
(noted as future work); Joust meta data (doesn't exist); new gods.

## Phase 1 — scoring (gated on validation metrics at every step)

Order matters: fix inputs first, calibrate last. After each step run
`python -m smite.validate` and record the three headline numbers in the plan;
a step that doesn't help (or hurts) gets investigated or reverted, not stacked.

### 1a. Effect-tag fixes (quick win)

Apply the `possible-missing` rows from `_tag_audit.md` after reading each
item's actual passive text (audit says review, don't auto-apply): `sustain`
for Barbed Carver / Gluttonous Grimoire / Hunter's Cowl / Sanguine Lash /
Typhon's Heart (+ Contagion if its text supports it), `aura` for Soul Gem /
Umbral Link / War Banner / War Flag. Keep `_tags.yaml` comments accurate.

### 1b. Role-vocabulary fix (`scoring.py`)

`_role_stat_map` matches each role/spec string **exactly first, then by
whitespace tokens** (so `Carry Jungle` hits `Carry` + `Jungle`). Extend
`role_stats` (defaults + `_weights.yaml`) to cover the real vocabulary:

- `Tank`, `Guardian`, `Support`: Physical/Magical Protection 1.0, Health 0.8
- `Brawler`, `Solo`: Health 0.8, protections 0.6, Strength 0.4
- `Jungle`, `Slayer`, `Assassin`: Strength 1.0, Penetration 0.8
- `Mid`, `Sniper`, `Burst Damage`: Intelligence 1.0, Penetration 0.8, Cooldown Rate 0.5
- `Healing`, `Buffs`: Cooldown Rate 0.8, aura-tag bonus handled via tags
- `Constant Damage`, `Pressure`: Attack Speed 0.6 (+ damage-type stat via kit)
- Lifesteal 0.5 added to `Carry`/`Sharpshooter`/`Hunter` (community carries
  build sustain; we currently give it zero fit credit)

Multi-word keys stay legal (exact match wins over token match on conflicts).
Damage-type guard: offensive stat entries only contribute when they pass the
god's damage type (Intelligence entries are inert for physical gods and vice
versa — prevents a repeat of the Cernunnos Nuker pollution). Defensive/neutral
stats always apply.

### 1c. Kit-scaling profile (`kit.py`, new module)

`scaling_profile(god)` parses each ability's `details` for
`Damage Scaling: … N% <Stat>` and returns:

- `str_share` / `int_share`: normalized Strength vs Intelligence scaling totals
  across abilities (basic attack excluded from ability totals)
- `basic_attack_share`: fraction of scaling references that flow through basic
  attacks / `Basic Attack Damage` (e.g. Ymir's Frostbite 175% BAD)
- `ability_count_with_scaling` (confidence; Ullr has 1 → low confidence)

`kit_stat_overlay(profile, god)` converts that to stat weights: the god's
dominant scaling stat gets weight ∝ its share; `basic_attack_share` boosts
Attack Speed (and, for physical gods, Critical Chance); high ability
orientation boosts Cooldown Rate and Penetration. Low-confidence profiles
(< 3 scaling abilities) fall back to the role map alone.

Blend in `god_fit_score`: `role_map ⊕ kit_overlay` where kit wins on
*offensive* stats and the role map wins on defensive stats — a tanky-role god
(Ymir: 305% Int in kit) still fits tank items first; the kit decides which
*damage* stats deserve credit. Exact blend factor is a tunable in
`_weights.yaml` (`kit_blend`, default 0.5), so validation can decide.

### 1d. Disagreement report (`analysis.py`, new module + CLI)

`python -m smite.analysis` → `Analysis/_disagreements.md`:

- **Missed meta:** per god, community items (pick ≥ 0.10) ranked outside our
  top 10 — with our score breakdown (eff/win/pick/fit), tags, and passive text.
- **Off-meta picks:** items in our suggested core with community pick < 0.05 —
  same breakdown, so "is this genuinely better or are we blind?" is answerable.
- **Constraint conflicts:** cases where assembly rules (lifesteal cap, boots,
  crit floor) excluded a high-community item that scoring ranked highly
  (Cernunnos double-lifesteal is the known instance).
- Cross-god rollup: items that repeatedly appear in either list.

This is a read-only report; run it, form hypotheses, encode fixes (tags,
role_stats, kit blend, or an assembly-rule change like per-flavor
`max_lifesteal: 2` for sustain-meta carries), re-validate. Findings worth
keeping get one-line notes in the report header.

### 1e. Weight calibration with guardrails (`calibrate.py`, new module + CLI)

Grid search (step 0.05) over the four signal weights, constraints:
sum = 1, `efficiency + fit ≥ 0.50`, `pick ≤ 0.15`. Objective: mean of
(pooled Spearman, mean coverage) — both normalized. Leave-one-god-out: report
per-fold winners and the spread; a winner that flips across folds is
overfitting and disqualified. Writes `Analysis/_calibration.md` (frontier
table + chosen recommendation + LOGO stability). The winning weights are then
applied to `_weights.yaml` by hand in the same branch with the report cited —
the weights file stays the human-legible opinion surface.

## Phase 2 — fun off-class builds

Engine support, not special cases:

- Flavor schema gains `fun: true` and `bypass: [damage_filter, archetype_fit]`.
- `score_god_items` skips `passes_damage_filter` when bypassed; with
  `archetype_fit` bypassed, fit uses **only** the flavor's `stats` overlay
  (the god's role map is ignored — the whole point is fighting the class).
- Fun profiles zero `win`/`pick` (off-class items have no meta data; neutral
  0.5 win would just add noise) → underrated flag auto-suppressed.
- Eligibility: fun flavors use the same `damage_types`/`match_any` gates
  (null = any god). Ship one to start: **`fun-crit`** (crit/attack-speed stack
  for anyone — crit Ymir realized; `require: {stat: Critical Chance, min: 3}`,
  boots + crit-floor rules still apply so it's a coherent silly build, not a
  random one).
- `recommend.py` emits fun entries after serious ones with `fun: true` stamped
  on the entry; rationale text is honest: "For fun — deliberately fights this
  god's kit. Not scored against the meta."
- `build_index.py` passes the flag through; validation **excludes** fun builds
  (they'd poison coverage by design).

## Phase 3 — viewer (each item verified with Chrome MCP screenshots)

1. **Why-this-item:** `build_index.py` embeds each suggested build's per-item
   score breakdown (total, eff, win, pick, fit + top contributing stats/tags).
   DetailPanel item chips get a click/hover popover showing it. Keeps
   index.json growth modest (only suggested-build items, rounded values).
2. **Fun badges:** fun builds render with a distinct badge ("For fun — off-class
   on purpose") and sit last in the suggested list; styling must make them
   impossible to mistake for optimal recommendations.
3. **Meta-divergence markers:** in a suggested build, items absent from the
   community build get a subtle "off-meta" dot; tooltip shows community pick%
   for the item (data already flows via per-item `meta`). Community-tab items
   we *don't* suggest get no marker (the report covers that side).
4. **Polish pass:** screenshot-driven sweep (desktop + mobile widths, light +
   dark) fixing rough edges found along the way.

Type-gate: `cd viewer && npm run build` (never `npx tsc --noEmit`).

## Testing

- pytest (existing `tools/tests` conventions): kit parser (fixtures from real
  god notes incl. Ullr sparse case), token role matching (Cernunnos no longer
  inherits Intelligence, Ymir gets protections), bypass flags, fun-flavor
  profile (win/pick zeroed), calibration objective + constraints, disagreement
  report sections. TDD per superpowers workflow.
- Viewer: type-safe build + existing vitest patterns for the popover/badge
  components if the repo already tests components; otherwise build-gate +
  screenshot verification.
- End-to-end: `recommend --all` regenerates cleanly; validation report written;
  EOL-only diffs checked out per repo convention.

## Workflow & hygiene

Isolated git worktree branch (e.g. `smite-scoring-intelligence`); frequent
commits scoped to own paths only (never `git add -A`); `git fetch` + integrate
before push (30-min calendar cron on main); finish via
finishing-a-development-branch. Scrapes: none needed — all work runs offline
over existing notes.

## Success criteria

- Headline metrics improve over 60% / 62% / 0.26 — target directionally
  meaningful gains (Ymir and Cernunnos coverage are the obvious movers), with
  the calibration report documenting the frontier honestly.
- Disagreement report exists and at least two encoded findings from it are
  validated by the metric.
- `fun-crit` builds render for all gods incl. Ymir, clearly badged.
- Screenshot evidence for every Phase-3 change.

## Future work (explicitly out of scope)

- Diminishing-returns / breakpoint-aware assembly (attack-speed cap, pen cap).
- Per-ability item-passive synergy (e.g. Polynomicon with high-cooldown kits).
- Joust-specific validation data if a source ever appears.
