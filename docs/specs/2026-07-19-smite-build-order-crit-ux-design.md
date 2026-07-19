# SMITE 2 viewer/recommender: buy-order, flex swaps, crit-core, editor UX

Status: approved, ready for implementation plan
Date: 2026-07-19

## Problem

Six pieces of feedback on the shipped recommender + editor. This spec covers five
of them (Batch 1); **god aspects** (the sixth) get their own spec/cycle.

1. After saving a new build, the app should keep the user on the god's page and
   show the build they just made (it currently drops back to the first tab).
2. The build editor's item picker and chosen-slot list should show item icons.
3. The Conquest/Joust toggle should move to the left, above the build-type tabs
   (it's currently top-right in the header).
4. Item order isn't a real buy path — core items are score-sorted. Add a
   recommended **purchase order**, and make situational swaps target a marked
   **flex slot** instead of the last (lowest-scored) item.
5. Crit builds only have 0–2 crit items. A crit build should **guarantee a crit
   core** (a hard minimum of crit items).

## Design

### A. Editor UX (feedback 1, 2)

- **Icons (2):** `BuildEditor` renders each item's icon (via `iconSlug`) in both
  the search-results dropdown and the chosen-slots list, matching the DetailPanel
  slot rows (small rounded icon + name, with the same onError retry/hide).
- **Stay + select saved build (1):** After a successful save, the app keeps the
  current god selected (already true) **and** selects the newly-saved build's
  tab. Mechanism: `BuildEditor.onSaved` passes the saved `name` up; `DetailPanel`
  records it as a `pendingSelect` name; the god/note reset effect, instead of
  always resetting to tab 0, selects the entry whose `name === pendingSelect`
  when one is pending (then clears it), falling back to 0. This survives the
  async `reload()` producing a fresh note object.

### B. Mode toggle placement (feedback 3)

Move the Conquest/Joust segmented toggle out of the header's top-right and place
it left-aligned in its own row directly above the build-type tab row. The header
(headshot + god name + pantheon/role) stays; the toggle no longer floats right.

### C. Purchase order (feedback 4a)

The recommender computes a **buy order** for the core and emits `slot_order` in
that order (for `suggested` builds only — community builds keep SmiteBrain's own
order; `mine` builds keep the user's order).

- A tunable `build_order` block in `_weights.yaml`:
  ```yaml
  build_order:
    # Lower stage = bought earlier. stage = default + sum(tag_stage for the
    # item's effect_tags) + cost * cost_weight. Ties broken by cost, then name.
    default_stage: 0
    cost_weight: 0.0004        # ~ +1 stage per 2500g, so pricier trends later
    tag_stage:
      anti-heal: -1            # cheap, high-impact spikes go early
      protection-shred: -1
      wave-clear: -1
      sustain: 0
      aura: 1                  # team auras / luxury go late
      mobility: 0
  ```
- `scoring.build_order(core, items_by_name, tags_map, weights)` returns the core
  names sorted ascending by stage. This is an explicit heuristic (we have no real
  build-path data); it's labeled as "recommended order" in the viewer, and fully
  tunable. The core *membership* (which 6 items) is unchanged — only their order.
- The viewer shows the slots numbered 1→6 as the buy order (the SLOT ORDER header
  becomes "BUILD ORDER" for suggested builds).

### D. Flex-slot swaps (feedback 4b)

Situational swaps must not evict the final power spike. The recommender marks the
1–2 most replaceable core items as **flex**, and the viewer swaps *into* a flex
slot.

- `assemble`/`recommend` compute `flex_slots`: the *lowest-scored* core items
  (least essential by total score — independent of buy order), count tunable via
  `build_order.flex_count` (default 2). Stored as `flex_slots: [name, ...]` on
  each `suggested` entry.
- Viewer `applySwap(slotOrder, swapItem, flexSlots)`: the removed slot is the
  first `flexSlots` entry present in `slotOrder` (not the literal last). If no
  flex slot is known (community/mine, or empty), fall back to current behavior
  (remove last). The removed slot renders struck-through and the swap-in item is
  appended/highlighted as today. Flex slots get a subtle "flex" marker in the
  build list so the user can see which slots situational items replace.
- `CuratedBuildEntry` gains `flex_slots?: string[]`.

### E. Crit-core guarantee (feedback 5)

A crit-flavor build guarantees a minimum number of crit items.

- The crit flavor in `_weights.yaml` gains a `require` constraint:
  ```yaml
  crit:
    damage_types: [physical]
    match_any: [Carry, Sharpshooter]
    stats: {Critical Chance: 1.5, Attack Speed: 1.2, Strength: 0.8}
    max_lifesteal: 1
    require: {stat: "Critical Chance", min: 3}   # NEW
  ```
- `assemble_core` accepts an optional `require` arg `{stat, min}`. It first seeds
  the core with the top-`min` highest-scored buildable items carrying that stat
  (respecting the existing boots/lifesteal/dup rules), then fills remaining slots
  by score as today. If the pool has fewer than `min` qualifying items, it seeds
  as many as exist (no crash) — the buildable crit pool is 6, so min=3 is safe.
- `recommend.build_suggested_entries` passes the active flavor's `require` (if
  any) into `assemble_core`. Only flavors that declare `require` are constrained;
  core/burst/bruiser/anti-tank are unaffected.

## Data flow

`_weights.yaml` (build_order + crit.require) → `recommend --all`:
`assemble_core(..., require=...)` builds the constrained core → `build_order(...)`
sorts it → `flex_slots` computed from score → each `suggested` entry carries
`slot_order` (buy order) + `flex_slots` → `build_index` passes them through →
viewer renders buy order, flex markers, flex-targeted swaps.

## Testing

- **Python**: `build_order` sorts a core by stage (cheap anti-heal before a
  pricey aura item); `assemble_core` with `require={stat: "Critical Chance",
  min: 3}` yields ≥3 crit items and still fills 6 slots; a crit-flavor entry from
  `build_suggested_entries` has ≥3 crit items and a non-empty `flex_slots` that is
  a subset of `slot_order`.
- **Viewer (vitest/RTL)**: `applySwap` removes the flex slot (not the last) when
  `flexSlots` is supplied, and falls back to last when it isn't; `BuildEditor`
  shows item icons in results and chosen slots; after a save the just-saved tab
  is selected (pendingSelect); the mode toggle renders above the tab row.
- **Manual/integration**: regen; confirm suggested builds show a sensible buy
  order, crit builds are crit-heavy, situational chips swap a flex slot, the
  editor shows icons, saving lands on the new build, and the toggle is top-left.

## Limitations / non-goals

- Buy order is a transparent heuristic (cost + tag stage), not real build-path
  data — labeled as "recommended order," fully tunable in `_weights.yaml`.
- Flex marking is score-based (least-essential core), not matchup-specific.
- **Aspects are out of scope here** — separate spec/cycle.
- Community/mine builds keep their own item order and last-slot swap fallback
  (only `suggested` builds get buy order + flex slots).

## Open questions — resolved during design

- Build order → add a recommended buy order (heuristic, tunable).
- Swap target → target a marked flex slot (1–2 least-essential core items).
- Crit → guarantee a crit core (hard min via a flavor `require` constraint).
- Aspects → overlays + toggle + kit text, as its own later cycle.
