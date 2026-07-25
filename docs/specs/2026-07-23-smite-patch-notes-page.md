# SMITE 2 viewer — Patch-notes page (Phase 5)

Status: design + implementation spec
Date: 2026-07-23

## Problem
Show what changed between patches: which items were buffed/nerfed, with
before/after stats — the last of the six done-state criteria.

## Source of truth: the snapshot store (shipped Phase 3.2)
`tools/smite/snapshots.py` writes `<data>/Analysis/snapshots/<YYYY-MM-DD>.json`
on every `refresh_and_deploy` run: `{itemName: {cost, tier, stats}}`. It already
exposes `load_snapshot(path)` and
`diff_snapshots(old, new) -> {added:[names], removed:[names], changed:[{name, cost:[old,new]?, stats:{stat:[old,new]}}]}`.

**Bootstrapping reality:** the page needs ≥2 snapshots to diff. Until the weekly
cron has run twice, it must render a friendly empty state ("No patch history yet
— changes appear after the next data refresh"), NOT an error or a fake diff.

## Design
### `build_patch_report(snapshot_paths, limit=5) -> list[dict]` (in `snapshots.py`)
- Take the snapshot files sorted by date; diff each consecutive pair
  (old → new); newest first; keep at most `limit` periods.
- Each period: `{from, to, added:[names], removed:[names], changed:[entry]}` where
  entry = `{name, cost: [old,new]|None, stats: {stat: [old,new]}, verdict}`.
- **verdict classification** (`buff` | `nerf` | `mixed` | `adjusted`), computed per
  item from the direction of its deltas:
  - Parse each stat value's leading number (reuse `data_audit.STAT_VALUE_RE`
    semantics). A stat going **up** is a buff signal, **down** a nerf signal —
  - EXCEPT `cost`, where **up = nerf**, **down = buff** (paying more is worse).
  - All signals same direction → `buff` / `nerf`; both present → `mixed`;
    none parseable (e.g. only a tier/type change) → `adjusted`.
- Deterministic ordering (by name within a period).
- Emitted into `index.json` as `patch_notes: [...]` by `build_index` (empty list
  when <2 snapshots — never omit the key).

### Viewer (`PatchNotes.tsx`, route `#/patch`)
- Nav gains a **Patch** entry (icon rail + mobile bottom bar).
- Newest period expanded by default; older periods collapsed (`<details>`-style
  disclosure, reusing the design tokens; no external lib).
- Per period: header `from → to` (mono dates) + counts (`n changed · n added · n removed`).
- Per changed item: item icon + name + a **verdict chip** — buff = `text-under` on
  `bg-under/10`, nerf = `text-premium` on `bg-premium/10`, mixed = gold, adjusted =
  muted — then the deltas as rows: `stat  old → new` with the new value colored by
  that stat's direction (up green / down rose; inverted for cost). Mono numbers.
- Added items listed with a small "new" chip; removed with a muted strike style.
- Empty state as described above.
- Mobile: single column, rows wrap; same tokens.

## Testing
- **Python**: verdict classification (pure buff, pure nerf, mixed, cost-only
  inverted, unparseable → adjusted); `build_patch_report` pairs consecutive
  snapshots newest-first and respects `limit`; <2 snapshots → `[]`; added/removed
  surface correctly; `build_index` emits `patch_notes` (empty list when no history).
- **Viewer**: renders periods; newest expanded; verdict chips by class; before→after
  values shown; empty state when `patch_notes` is empty/absent; nav routes `#/patch`.
- **Manual**: with only 1 real snapshot today, verify the empty state renders; then
  synthesize a second snapshot locally (test fixture, NOT committed) to eyeball a
  populated diff before shipping.

## Limitations
- History starts now — no retroactive patch data (nothing was recorded before
  Phase 3.2). Real content appears after the cron's 2nd run.
- Snapshots are refresh-dated, not patch-versioned: a "period" is
  "between two data refreshes", which approximates a patch if the cron is weekly.
  Labeled with dates, not patch numbers, to stay honest.
- Only item cost/tier/stats are tracked (not passives/ability text) — a passive-only
  rework shows as `adjusted` with no numeric deltas.
