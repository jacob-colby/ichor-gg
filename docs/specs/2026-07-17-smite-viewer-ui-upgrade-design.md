# SMITE 2 viewer UI upgrade: Arena Night polish + tooltips + live swaps + one-click launch

Status: approved, ready for implementation plan
Date: 2026-07-17

## Problem

The second-monitor build viewer (`viewer/`, Vite + React 19 + TS + Tailwind v4)
works but is visually plain and has gaps that hurt at-a-glance use mid-game.
This upgrade covers five things Jacob asked for, plus a launcher:

1. **God images** — use the square scoreboard **headshot**, not the tall full-body art.
2. **Hover tooltips** — in-game-style detail on items and gods.
3. **Visual polish** — cohesive color scheme, font pairing, animations.
4. **Situational swaps update the build preview** — clicking a matchup reflows the build.
5. **Bug** — community builds show duplicate items.
6. **One-click launch** — a button/file to open the app without a terminal.

## Decisions (locked during brainstorming)

- **Visual direction: "Arena Night"** — deep slate + gold primary + electric-blue
  secondary, Rajdhani condensed headers, Inter body, mono for numbers.
- **Swap model: replace-with-live-diff**, replacing the **lowest-scored core slot**
  (the natural flex slot; same-category replacement rejected because cores are
  almost all offense, so there's rarely a like-for-like defensive slot).
- **Headshots are a real, available asset**: the wiki serves
  `T_<God>(S2)_Default_Icon.png` (square god-select icon) distinct from the tall
  `T_<God>(S2)_Default.png` portrait we currently scrape.
- **Duplicate bug is in the data**: SmiteBrain's Core takes the top pick per
  numbered slot; the same item can win two slots (e.g. Chiron → Titan's Bane
  twice). Fix in the parser by substituting the next-best alternative.

## Architecture

Two layers: small **pipeline enablers** (Python) that put the right data/assets
in place, then the **viewer redesign** (React/TS) that consumes them. Plus a
**launcher**. Each pipeline change is independently shippable and testable; the
viewer work is one coherent redesign of the existing components.

### Pipeline enablers

**P1 — Headshot assets** (`tools/smite/`)
- `wiki_parser.parse_god_page` already extracts the portrait `image_url`. Add
  extraction of the headshot URL (the `_Default_Icon` variant). If it isn't
  directly on the page, derive it from the portrait URL's asset name
  (`..._Default.png` → `..._Default_Icon.png`) and confirm with a HEAD/GET.
- `refresh.refresh_god` downloads it via the existing `_download_icon` helper to
  `_assets/icons/<slug>-head.png`. Keep the portrait too (used in the detail header).
- `build_index._copy_icons` already copies all `*.png`, so `-head.png` flows to
  `viewer/public/icons/` automatically.
- Slug convention unchanged: `name.lower().replace(" ","-").replace("'","")`,
  suffix `-head`.

**P2 — Community-build dedup** (`tools/smite/smitebrain_parser.py`)
- `_parse_core_recommended_build` currently takes the top pick per Core slot with
  no cross-slot dedup. Change: track chosen item names; when a slot's top pick is
  already chosen, walk that slot's ranked alternatives to the first unused one.
  If every alternative in a slot is already used, drop the slot (build shrinks
  rather than duplicates — a correct, rare fallback). Result: `slot_order` has no
  duplicate item names.
- Re-run `refresh --refresh-builds <god>` for all 10 gods + `build_index`.

**P3 — Structured swaps + richer item payload**
- `recommend.build_suggested_entries`: each `situational_swaps` entry gains
  `swap_item` — the clean item name (e.g. `"Magi's Cloak"`) for a real swap, or
  `null` for the "core already covers…" / "no … available" rows. The existing
  prose `swap` string stays (drives the non-swap display text). The viewer needs
  a clean name to drive the diff; parsing it out of prose is unreliable.
- `build_index.build_index`: fold two god-agnostic fields into each item in the
  index — `effect_tags` (from `_tags.yaml`) and `efficiency_tier`
  (`undervalued`/`fair`/`premium`, from `efficiency.efficiency_scores`). This is
  what lets item tooltips show *why* an item is good without the viewer
  recomputing anything.

### Viewer redesign (`viewer/src/`)

**V1 — Arena Night design tokens** (`src/index.css` + a small theme layer)
Define the palette, fonts, radii, and motion durations as CSS variables in one
place so the look is tunable centrally:
```
--bg-0:#0b0e13; --bg-1:#0e1116; --bg-2:#12161d; --line:#1e2530;
--gold:#e3b23c; --blue:#4ea3ff; --text:#e8edf4; --muted:#8b95a5;
--tier-under:#63c088; --tier-premium:#c58b8b;   /* efficiency tiers */
--dur:140ms;
```
Fonts: Rajdhani (headers) + Inter (body) + a mono for numbers, self-hosted or via
a single Google Fonts link. Motion: 120–160ms ease transitions on hover, tab
change, selection, and the swap diff. No gradients-as-crutch; flat surfaces with
one accent. Applies across all components below.

**V2 — GodRail with headshots + tooltips** (`src/components/GodRail.tsx`)
- Swap the icon `src` to `/icons/<slug>-head.png` (square). Wider rail (~72px) so
  headshots read clearly; keep the selected-ring treatment in gold.
- Hover/focus → god tooltip (see V5): pantheon · role · damage type · ability names.

**V3 — DetailPanel header + slot styling** (`src/components/DetailPanel.tsx`)
- New header: headshot + god name (Rajdhani) + role/pantheon subline + mode badge.
- Source tabs restyled (gold active). Slot rows: item icon, name, and for
  community entries the pick/win in mono; hovering an item → item tooltip (V5).
- Keep the existing hard-won correctness (index-based `activeIndex`, `[god, note]`
  reset dep, `${name}-${i}` slot keys, `onError` icon hide) — restyle only.

**V4 — Live swap preview** (`src/components/DetailPanel.tsx` + `src/lib/builds.ts`)
- Matchup chips reflect the 4 real `vs_tag`s emitted by the recommender
  (`heavy_cc`, `magic_heavy`, `physical_heavy`, `sustain`) — drop the stale
  `poke` chip. A chip whose swap has `swap_item === null` renders as an
  informative, non-clickable state ("covered" / "none").
- Clicking an active chip sets a selected-matchup state. The rendered
  `slot_order` becomes a derived "effective build": replace the **last** entry
  (lowest-scored core slot) with `swap_item`. The removed item shows struck
  through/dimmed; the incoming item highlighted in gold/blue with a "swap in"
  marker. Click again (or the chip) to clear. Pure derivation in `builds.ts`
  (`applySwap(slotOrder, swap)`), unit-testable.
- Only applies to entries that have structured swaps (suggested builds). Community
  entries have no swaps; `mine` entries keep prose swaps (no diff) — unchanged.

**V5 — Tooltip component** (`src/components/Tooltip.tsx`, new)
- A small reusable hover/focus tooltip: ~150ms open delay, positioned to avoid
  clipping at viewport edges (flip/shift), dismiss on blur/mouse-leave/Esc,
  `role="tooltip"` + `aria-describedby` for keyboard/screen-reader access.
- **Item content**: name · tier · cost · stat lines (name: value) · passive text ·
  a footer row with efficiency tier + effect-tags as small pills.
- **God content**: name · pantheon · role · damage type · ability names list.
- Content is presentational; data already in the index after P3.

### Launcher (Windows, one click)

- **`run.bat`** at the vault root: `cd` into `viewer`, `npm install` only if
  `node_modules` is missing, then `npm run dev -- --open` (Vite opens the default
  browser when the server is ready). Double-click from Explorer works standalone.
- **`03. Workspaces/Gaming/SMITE 2/Open Build Viewer.md`** — an Obsidian note with
  a one-click `file:///…/run.bat` link and a one-line "first launch installs deps,
  then the browser opens automatically" note, so it's launchable from inside the
  vault.
- **Fix `.claude/launch.json`** — its `smite-viewer-dev` config points at the
  removed worktree path `.claude/worktrees/smite-viewer/viewer`; repoint to
  `viewer` so any launch tooling works.

## Data flow

```
wiki.smite2.com → refresh (P1 headshots) → _assets/icons/<slug>-head.png
smitebrain.com  → refresh --refresh-builds (P2 dedup) → Builds/*.md (distinct items)
recommend --all (P3 swap_item) ────────────────────────→ Builds/*.md suggested entries
build_index (P3 effect_tags/efficiency_tier + copy icons) → viewer/public/index.json + /icons
viewer (V1–V5) ← reads index.json
run.bat / Obsidian note → npm run dev --open
```

## Testing approach

- **Python**: `smitebrain_parser` dedup — a fixture Core where one item is the top
  pick in two slots yields distinct `slot_order` via next-best substitution; a
  slot whose every alternative is used is dropped. `build_index` — items carry
  `effect_tags` + `efficiency_tier`; `recommend` swap entries carry `swap_item`
  (name or null). Headshot URL derivation — `..._Default.png` → `..._Default_Icon.png`.
- **Viewer (vitest + RTL)**: `applySwap` pure-function tests (replaces last slot,
  no-op when `swap_item` null); Tooltip shows item stats/passive/tier; GodRail
  uses `-head` src; clicking a matchup chip renders the struck/added diff; a
  `null`-swap chip is non-interactive.
- **Manual**: run the app, verify headshots load, tooltips position correctly at
  edges, swap diff reflows, Arena Night theme in the browser.

## Limitations / non-goals

- Not touching the recommender's scoring math or the god-fit ceiling (out of scope).
- Headshot fetch depends on the wiki's `_Default_Icon` asset existing per god; if a
  god lacks one, fall back to the portrait (the `onError` hide already prevents a
  broken image, and the portrait remains a valid icon).
- Launcher is Windows-only (Jacob's machine); no cross-platform script.
- No dark/light theme toggle — the app is dark-only by design (second-monitor game use).

## Open questions — resolved during design

- Visual direction → Arena Night.
- Swap interaction → replace-with-diff, lowest-scored slot, viewer-derived.
- Which images → dedicated square headshot asset, portrait retained for the header.
- Dedup location → SmiteBrain parser (data is wrong at the source).
- Tooltip data → fold effect-tags + efficiency tier into the item payload (worth the
  small `build_index` change; makes tooltips explain *why*).
- Launch → `run.bat` + Obsidian launcher note + fix stale `launch.json`.
