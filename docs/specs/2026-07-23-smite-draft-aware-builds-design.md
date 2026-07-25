# SMITE 2 — Draft-aware builds (ally + enemy comp)

Status: approved, ready for implementation plan
Date: 2026-07-23

## Problem
After play-testing, the highest-value missing feature: adapt a god's build to the
actual match — the 4 allies and 5 enemies. Today the viewer exposes 4 fixed
situational swaps (`heavy_cc`, `magic_heavy`, `physical_heavy`, `sustain`) and
leaves the player to decide which apply. This makes that automatic and graded.

## Constraint that shapes everything
The viewer is a **static site**; scoring runs in Python at build time. A live
"enter 10 gods → re-rank" therefore has to happen **client-side**. The design
ships the inputs the browser needs and mirrors the Python scoring/assembly rules
in TypeScript.

## Threat model (derived from data already in the index)
No new scraping. Enemy signals, graded by count rather than binary:
- **Damage split** — `damage_type` across the 5 enemies → magical/physical
  protection value scales with the count (5/5 magical ≫ 3/5).
- **Lockdown / Crowd Control / Area Control** specs → `cc-immunity`, Tenacity.
- **Healing / Sustain** specs → `anti-heal`, scaled by number of healers.
- **Carry / Sharpshooter** specs → `anti-crit`.
- **Tank** specs → `protection-shred`, Penetration.

Ally signals — **team-responsibility assignment** (all three behaviors approved):
- **Avoid duplication** — a job already covered by an ally (anti-heal, an aura,
  front-line) is deprioritized for you (auras don't stack; anti-heal is one
  person's job). Coverage is inferred from each ally god's **own suggested core**
  (its items' `effect_tags`) plus its `specializations`.
- **Fill gaps** — a job **nobody** covers is raised for you. Same mechanism,
  opposite sign.
- **Damage mix** — an all-physical ally comp means enemies stack physical
  protection → raise Penetration / `protection-shred` for you.

## Mechanism — a draft is just another scoring overlay
`scoring.resolve_profile` already composes mode ⊕ aspect ⊕ flavor into
`{signals, tag_bonus, stat_overlay, max_lifesteal}`. A draft is one more
contributor of `tag_bonus` + `stat_overlay`, evaluated in the browser:

```
adjusted(item) = base_total(god, item)
               + Σ tag_bonus[t]           for t in item.effect_tags
               + Σ stat_bonus[s]          for s in item.stats
```
Then the client re-assembles a 6-item core with the **same constraints as
`assemble.assemble_core`**: at most one boots (`"Movement Speed" in stats`), at
most `max_lifesteal` lifesteal/sustain items (`"sustain" in tags` or a
`Lifesteal` stat), no duplicates, fill by adjusted score. Starter is unchanged
(it is chosen by role, not by matchup).

**Bounded influence** (approved): total threat bonus per item is clamped so a
scary comp shifts roughly 1–3 slots, never converting a damage build into full
defense. All existing constraints hold. Every magnitude lives in `_weights.yaml`
under a new `draft:` block — the house pattern of tunable sidecars.

## Data to ship (new)
`index.json` gains `god_item_scores: { "<god>": { "<item>": <base_total> } }`,
capped at the **top N items per god** (default 40, tunable) — a god's #60 item is
not going to be promoted by a bounded bonus. Estimated a few hundred KB on a
3.4 MB index; items already carry `effect_tags` and `stats` globally, so nothing
else is duplicated.

## UI
- **Draft bar** on the god page (collapsible, above the build tabs): two rows —
  Allies (4 slots) and Enemies (5 slots) — each slot opening the existing
  god-picker modal, filtered to the 87 gods with data. Clear button.
- **Threat read-out**: chip row summarizing what was derived —
  `4 magical · 2 healers · heavy CC · no ally anti-heal`.
- **Draft tab** beside Core / flavors / Community. Renders the adapted 6 with
  changed slots marked and a per-slot reason (`↑ anti-heal — 2 enemy healers,
  no ally covers it`), reusing the existing swap-diff styling (added = blue,
  removed = muted/strikethrough).
- **Persistence**: the draft is stored in `localStorage` (`smite:draft`) so a
  mid-match reload doesn't lose it.
- **Stacking**: the draft overlay applies **on top of** the active mode + flavor,
  never replacing them.

## Testing
- **Python**: `god_item_scores` emitted, respects the top-N cap, contains only
  buildable/damage-filter-passing items, and `build_index` stays hermetic to the
  vault root passed in.
- **Viewer (pure fns, heavily unit-tested)**: threat derivation from comps
  (each signal, graded by count, empty comp → no threats); ally coverage
  inference (covered job deprioritized, uncovered job raised); the adjusted
  ranking; assembly constraints mirrored (one boots, lifesteal cap, no dupes,
  exactly 6); bounded influence (a maximal threat comp changes ≤ 3 slots);
  reasons attached to changed slots.
- **Viewer (component)**: draft bar adds/removes gods, threat chips render, the
  Draft tab shows the adapted build with diffs, Clear resets, persistence
  round-trips through localStorage.
- **Manual**: a real draft on a known god, desktop + 390px.

## Limitations (stated, not hidden)
- Enemy/ally picks are limited to the **87 gods with data** — Cu Chulainn and
  Ix Chel have empty wiki pages, so no damage type or specs exist to derive from.
- Ally coverage **assumes teammates build roughly their suggested core** — a
  reasonable prior, not a promise.
- Threat derivation uses `specializations`, which are coarse wiki labels; it will
  not catch a god who is situationally a healer without the tag.
- Client-side re-rank uses the **shipped base score**, so it inherits whatever
  the last data refresh produced (no live re-scoring against fresh meta).
