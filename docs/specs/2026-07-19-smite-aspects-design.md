# SMITE 2 recommender/viewer: god aspects

Status: approved, ready for implementation plan
Date: 2026-07-19

## Problem

God **aspects** change a god's kit — sometimes drastically (Cernunnos's basics
become melee auto-attacks; Ra becomes a healer; Hercules an ally-heal tank). The
recommender ignores them, and the viewer never shows what an aspect does. Feedback
item 6 (of the six-item batch): factor aspects into suggestions, add an Aspect
toggle per god page, and show what the aspect actually does.

Decided during design: the toggle **swaps** the suggested builds to aspect-tuned
versions (not extra tabs), and **all 7 gods with a wiki aspect** get the toggle
(Agni, Cernunnos, Chiron, Chronos, Hercules, Morgan Le Fay, Ra). Bari, Susano,
Ullr have no aspect on the wiki → no toggle.

## Design

### Data already present

`God.aspects[0]` (in god data / index.json) carries the aspect `name` +
`kit_changes` text for the 7 gods — so the viewer can display "what the aspect
does" with no new scraping.

### A. Aspect overlays in `_weights.yaml`

A tunable `aspects:` block keyed by **god name**, each a scoring overlay in the
same shape as flavors — `stats` (god-fit stat weights), optional `tag_bonus`,
optional `max_lifesteal`. Hand-authored per god from its kit text; light for
aspects that barely change the build (Agni, Chiron), meaningful for the rest:

```yaml
aspects:
  Cernunnos:   # Strife — basics become melee cleave autos
    stats: {Strength: 1.0, Attack Speed: 0.8, Lifesteal: 0.8, Max Health: 0.6}
    tag_bonus: {sustain: 0.2}
    max_lifesteal: 2
  Hercules:    # Preservation — ally-heal bruiser/tank
    stats: {Max Health: 1.2, Physical Protection: 0.9, Magical Protection: 0.9}
    tag_bonus: {aura: 0.3, sustain: 0.2}
    max_lifesteal: 2
  Ra:          # Thermotherapy — heals allies, abilities lose scaling → support
    stats: {Cooldown Rate: 0.8, Magical Protection: 0.5, Max Health: 0.6, Intelligence: 0.4}
    tag_bonus: {aura: 0.3, sustain: 0.2}
  Chronos:     # Relativity — team time-field, loses Time Lord Int → support mage
    stats: {Cooldown Rate: 0.8, Intelligence: 0.6, Magical Protection: 0.4, Max Health: 0.4}
    tag_bonus: {aura: 0.3}
  Morgan Le Fay:  # Cursed Crown — melee, %max-HP damage
    stats: {Max Health: 1.0, Intelligence: 0.8, Magical Protection: 0.4}
    tag_bonus: {sustain: 0.2}
    max_lifesteal: 2
  Agni:        # Combustion — ignite via basics; still a burst mage
    stats: {Attack Speed: 0.4}
  Chiron:      # Heroic Tutor — damage copy + ally buffs; still a carry
    stats: {Attack Speed: 0.3}
    tag_bonus: {aura: 0.1}
```

Stat keys match real item stat names (verified against the pool: `Strength`,
`Intelligence`, `Attack Speed`, `Max Health`, `Physical/Magical Protection`,
`Cooldown Rate`, `Lifesteal`, `Penetration`, …). The exact weights are tunable;
they're a starting calibration.

### B. `resolve_profile` composes mode ⊕ aspect ⊕ flavor

`scoring.resolve_profile(weights, mode, flavor, aspect_overlay=None)` gains an
aspect overlay:
- `stat_overlay = {**aspect.stats, **flavor.stats}` (flavor wins on a shared stat).
- `tag_bonus = {**mode.tag_bonus, **aspect.tag_bonus, **flavor.tag_bonus}`.
- `max_lifesteal` = flavor's if the flavor sets one, else the aspect's if set,
  else 1.

Base builds (aspect_overlay=None) are unchanged — existing behavior is preserved.

### C. `recommend` emits a parallel aspect set

`build_suggested_entries` emits the base suggested entries (as today), then — if
the god has a wiki aspect **and** an `aspects[<god>]` overlay — emits a second set
(core + the same eligible flavors) computed with the aspect overlay. Each aspect
entry carries `aspect: <aspect_name>` (from god data); base entries have no
`aspect` field. Buy-order, flex_slots, crit-core `require`, and the starter all
apply to aspect entries exactly as to base ones.

Result per Conquest note: community + base suggested (core+flavors) + aspect
suggested (core+flavors) [+ any mine]. `merge_suggested_entries` already replaces
all `suggested` entries wholesale, so both sets are written together.

### D. Data model

`CuratedBuildEntry` gains `aspect?: string`. No change to community/mine entries.
The aspect's display text comes from `godData.aspects[0]` (name + kit_changes),
not duplicated onto entries.

### E. Viewer — Aspect toggle + kit banner

- DetailPanel detects `hasAspect = suggested entries include any with an
  `aspect`. When true, render an **Aspect** toggle (a segmented On/Off, next to
  the mode toggle row). Default **off**.
- Shown entries: community + mine always; suggested filtered to `!aspect` when
  off, `aspect === <the god's aspect>` when on. Tabs render the filtered set;
  toggling resets the active tab to 0.
- When on, a **kit banner** above the tabs shows the aspect name + `kit_changes`
  text (from `godData.aspects[0]`), so the user sees what the aspect does.
- The toggle is per-god (resets when the god or mode changes); no cross-god
  persistence (unlike the mode toggle) — an aspect is a per-god concept.

## Data flow

`_weights.yaml` `aspects` → `recommend --all`: base entries + aspect entries
(tagged `aspect`) via `resolve_profile(..., aspect_overlay=...)` →
`merge_suggested_entries` writes both sets → `build_index` passes them through →
viewer Aspect toggle filters base vs aspect suggested + shows the kit banner.

## Testing

- **Python**: `resolve_profile` with an aspect overlay merges stats/tags and
  respects the max_lifesteal precedence; base (no aspect) is unchanged.
  `build_suggested_entries` for an aspect god (e.g. Hercules) emits both a
  no-`aspect` core and an `aspect`-tagged core, the aspect core carries the
  aspect's name, and buy-order/flex/require still hold; a non-aspect god
  (Susano) emits only base entries.
- **Viewer (vitest/RTL)**: a god with aspect entries shows the Aspect toggle;
  toggling it filters the suggested tabs to the aspect set and reveals the kit
  banner; a god with no aspect entries shows no toggle; community/mine remain
  visible in both states.
- **Manual/integration**: regen; on Hercules/Ra/Cernunnos confirm the aspect
  build differs (tankier / support / auto-attack) and the kit banner shows the
  real text; on Susano confirm no toggle; base builds unchanged with the toggle
  off.

## Limitations / non-goals

- Aspect overlays are hand-tuned heuristics from kit text (freeform, not
  structured), fully tunable in `_weights.yaml` — same honest ceiling as flavors.
- No aspect-specific damage-type flip or ability-scaling simulation; overlays are
  stat/tag skews only. (An optional `damage_type` override field is allowed in
  the config shape but unused in v1.)
- Aspect uses the same eligible flavors as the base build (the overlay reweights;
  it doesn't change which flavors are offered).
- Gods without a wiki aspect (Bari, Susano, Ullr) get no toggle.

## Open questions — resolved during design

- Toggle behavior → swap the suggested builds to aspect-tuned versions (+ kit
  banner), not extra tabs.
- Which gods → all 7 with a wiki aspect (even minor ones like Agni/Chiron).
- Where aspect text comes from → existing `God.aspects[0].kit_changes`.
