# SMITE 2 viewer: in-app build editor + community starters

Status: approved, ready for implementation plan
Date: 2026-07-18

## Problem

Two related asks:
1. **Save your own builds** — the viewer is read-only; there's no way to create a
   personal (`mine`) build from the app. Make the viewer read-write so a build can
   be composed and saved into the vault.
2. **Starters on community builds** — the recommender stamps a role-based starter
   on suggested builds; community builds should show it too.

This is Part 2 of the two-part request (Part 1, starters, shipped). v1 scope for
the editor **excludes situational-swap editing** (decided during brainstorming).

## Design

### A. Community starters (small)

- `recommend --all` stamps the god's `pick_starter` result onto the **community**
  entry of each Conquest Build note (same value it stamps on suggested). Done via
  a read-modify-write of the note's community entry after the suggested write
  (or folded into the same write).
- Viewer: the STARTER block's `!community` guard is dropped — it renders whenever
  the active entry has a `starter`. `CommunityBuildEntry` type gains
  `starter?: {base, upgrade}`.

### B. `mine` build data model

A `mine` entry: `{source: "mine", name: string, slot_order: string[],
starter?: {base, upgrade}, notes?: string}`. `CuratedBuildEntry` gains an optional
`name`. `tabLabel` returns the `name` for a mine entry (falling back to "mine"),
the archetype for suggested, the source otherwise. Multiple named mine builds per
god/mode are allowed.

### C. Python `save_build` (write logic)

- `notes.upsert_mine_entry(path, god, mode, entry)` — add or replace (matched by
  `name`) a single `mine` entry, preserving community/suggested/other mine entries
  verbatim. Creates the note if missing. Mirrors `merge_suggested_entries`.
- `notes.delete_mine_entry(path, name)` — remove the mine entry with that name.
- `tools/smite/save_build.py` CLI: reads a **JSON object from stdin**
  `{action: "save"|"delete", god, mode, name, slot_order, starter?, notes?}` and
  dispatches. **Safety**: validates `god` against the real gods (Gods/ notes) and
  `mode` against `["Conquest", "Joust"]` before deriving the `<god>-<mode>.md`
  path — no path traversal. `slot_order`/`starter` items validated against the
  tracked item pool; unknown names rejected. Data flows via stdin JSON, never
  shell-interpolated.

### D. `build_index` exports the starter roster

`build_index` adds a top-level `starters` to `index.json` — the `weights.starters`
list (`{base, upgrade}` pairs) — so the editor's starter dropdown has the options
without duplicating the config in JS.

### E. Local write endpoint (Vite middleware)

`vite.config.ts` gains a small plugin with `configureServer`: middleware on
`POST /api/build` reads the JSON body, spawns `python -m smite.save_build`
(cwd = `../tools`, body piped to stdin, **fixed argv — no shell**), and on success
runs `python -m smite.build_index` to refresh `index.json`, returning `{ok}` or
`{ok:false, error}`. Localhost-only (dev server). Not present in a production
build — acceptable, the app is only used via the local dev server.

### F. Editor UI

- A **"＋ New build"** button (in the DetailPanel header) opens a `BuildEditor`
  panel scoped to the current god + mode.
- Fields: **name** (text), **item picker** (search the `items` list; click to add;
  the chosen list shows in order with remove + up/down reorder; max 6), **starter**
  (dropdown from `index.starters`, default = the god's current recommended
  starter), **notes** (textarea, optional).
- **Save** → `POST /api/build` `{action:"save", …}` → on `{ok}` call the existing
  `reload()` (re-fetches `index.json`) → close editor → the new named `mine` tab
  appears and is selectable.
- Existing `mine` tabs get **Edit** (opens the editor pre-filled) and **Delete**
  (`POST /api/build` `{action:"delete"}` → reload). Save with an existing name
  overwrites (upsert).
- Errors from the endpoint surface inline in the editor (e.g. "Save failed: …").

### Data flow

Editor form → `POST /api/build` → Vite middleware → `python -m smite.save_build`
(writes/updates the `mine` entry in `<god>-<mode>.md`) → `python -m smite.build_index`
(rebuilds `index.json`) → endpoint returns ok → viewer `reload()` → new tab shows.

## Testing

- **Python**: `upsert_mine_entry` adds a named mine entry and preserves
  community/suggested; a second upsert with the same name replaces (not
  duplicates); `delete_mine_entry` removes only that entry. `save_build` CLI
  parses stdin JSON, rejects an unknown god/mode (no file written), and dispatches
  save/delete. `build_index` output carries `starters`.
- **Viewer (vitest/RTL)**: `tabLabel` returns a mine entry's `name`; the community
  STARTER line renders when the community entry has a starter; the `BuildEditor`
  adds/removes items and calls the endpoint with the right payload (mocked
  `fetch`); Save success triggers `reload`.
- **Manual/integration**: run the app via the dev server, create a build, confirm
  it writes the note + appears as a tab after reload; edit and delete it; confirm
  community builds show the starter.

## Limitations / non-goals

- **Saving requires the local dev server** (run.bat) — the write endpoint is
  dev-only. This matches how the app is used; a static production build is
  read-only.
- **No situational-swap editing** in v1 (mine builds have no swap column). Suggested
  builds still show swaps.
- The endpoint is unauthenticated but localhost-only and validates inputs — fine
  for a personal local tool; not for network exposure.
- Reordering UI is simple up/down buttons in v1 (no drag-and-drop).

## Open questions — resolved

- Save mechanism → in-app editor with a local Vite write endpoint shelling a
  Python `save_build` CLI (JSON via stdin; validated; no shell interpolation).
- Swap editing → excluded from v1.
- Starter in the editor → dropdown from an `index.starters` roster, default =
  the god's recommended starter; community builds also display the starter.
