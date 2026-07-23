# SMITE 2 viewer: modals, Gods tab, freshness UI, second community source

Status: approved, ready for implementation plan
Date: 2026-07-22

## Problem

A batch of viewer/data improvements after the scoring-intelligence session:
1. **pick% reads 0** — the "WHY THIS ITEM" popover's `pick` bar shows 0 for the
   ~54% of suggested items not in a god's community build (the pick *signal* is
   genuinely 0). Confusing; looks broken.
2. **Add-god** is a text box — want an **icon picker modal**.
3. **Adding an item** to a build is a search box — want an **item modal with filters**.
4. No **Gods tab** — want a filterable gods index like the Items shop.
5. Only **one community build** per god is shown — want more, from a **second source**.
6. No **data-freshness** signal — want "data from <date>" everywhere + a live
   "scraping…" state in dev.

Also fold in the three review-chip findings from the last session (off-meta
tooltip pick%, a cosmetic type cast, a dead `kit_blend` fallback literal).

This is large; the plan sequences the independent viewer work first and gates the
second-source phase (Part F) on a live feasibility check.

## Design

### Part A — pick% popover fix + chip cleanups (small)

In `DetailPanel`'s WHY-THIS-ITEM popover, the `pick` bar shows the raw signal.
Change it so an item with `pick === 0` (or absent) renders **"off-meta — not in
community build"** instead of a 0 bar, and where the item *does* have a community
pick% (it's in this god's community build), show that %. Same for the community
pick badge already shown. Also apply the chip fixes: off-meta marker tooltip
shows the community pick% when known; remove the dead `kit_blend` fallback literal
in the Python; fix the cosmetic type cast. (Note the em-dash mojibake in fun
rationales if it renders as `�` in the browser — re-encode as UTF-8.)

### Part B — freshness UI

`build_index` adds a top-level **`data_updated`** = the most recent `last_verified`
across gods + community builds (real scrape recency, not build time — avoids
spurious diffs). Viewer shows **"Data from <date>"** in the top nav/footer,
everywhere (works in the hosted build). In **dev only**, a global **"scraping…"**
indicator appears while an add-god/refresh request is in flight (the ManageGods
add already has a per-request busy state; lift it to a small app-level banner so
it's visible during the ~30–90s scrape). `Item`/`God` types unchanged; `IndexData`
gains `data_updated?: string`.

### Part C — Gods tab

A filterable **Gods index** (`GodsIndex.tsx`) mirroring the Items shop, at route
`#/gods`. Cards: headshot, name, pantheon · role · damage type; filters for
pantheon / role / damage type + text search. Click → the existing god page
(`#/god/<name>`). Top nav gains a **Gods** button between Builds and Items. Pure
filter helpers (`godFilters.ts`) unit-tested, mirroring `itemFilters.ts`.

### Part D — Add-god icon modal + god roster

To pick a god by icon we need the **full SMITE 2 roster** (names + head icons),
including gods not yet tracked. `refresh` gains a roster step: fetch the wiki's
list-of-gods page → `04. System/Data/SMITE/_roster.json` = `[{name, icon_slug}]`
for every god, and download each head icon into `_assets/icons/` (so the modal has
images). `build_index` exposes `roster` in `index.json` (and copies the icons as
usual). The dev **Add-god button opens a modal**: a searchable grid of every
roster god, already-tracked ones dimmed/marked, untracked ones clickable →
`POST /api/gods {action:"add"}` (the existing endpoint) with the busy/scraping
state from Part B. Remove still works from the rail. Hosted build: no modal (dev
only). If the roster page is impractical to parse, fall back to a hand-maintained
roster list committed as `_roster.json` (still drives the modal).

### Part E — Item-selection modal with filters

The `BuildEditor` item search box is replaced by an **"Add item" button → modal**:
a filterable item grid reusing `filterItems`/`sortItems` + the shop's card layout
(tier / rating / tag / stat filters + search), click an item → adds it to the
build (max 6, existing rule), close. Keeps the current reorder/remove/starter/
notes flow. `ItemPickerModal.tsx`, tested.

### Part F — Second community source (feasibility-gated)

**Goal:** show more than one community build per god by adding a second stats site.
**Reality:** candidate sites (SmiteSource, ProSmiteBuilds, SmiteTracker) are
bot-protected + JS-rendered (SmiteSource 403s a plain fetch), reachable only via
the existing Playwright `BrowserFetcher`. So the source + parser is a **spike**:

1. **Spike (gate):** using `BrowserFetcher`, fetch one god page from the top
   candidate(s) and confirm it exposes **multiple distinct builds** per god with
   item lists (win/pick if available). Pick the most reliable. **If none do,
   fall back** to *per-slot alternatives* from SmiteBrain (keep the 2nd/3rd
   most-picked tile per slot — data the current parser already sees but discards)
   and stop here; the data-model + viewer below still apply.
2. **Data model:** a build note's `community` becomes **one-or-more** entries,
   each tagged `source` (`smitebrain` / `<second>`) and a short `label`
   (e.g. "SmiteBrain Core", "SmiteSource #1"). `build_index`/`notes` handle a list;
   per-item `meta` aggregates across all community sources.
2b. New parser module (e.g. `tools/smite/<source>_parser.py`) + a `refresh`
    hook to fetch + write the extra community entries; `validate` still uses
    SmiteBrain as the ground-truth for the metric (one source stays canonical).
3. **Viewer:** the DetailPanel community area shows a **build selector** (sub-tabs
   or a dropdown) when >1 community build exists; each renders its own slot_order
   with that build's pick/win. One community build → unchanged UI.

Part F ships only if the spike succeeds; otherwise the fallback (per-slot
alternatives) delivers "more than one option" without a fragile new scraper.

## Data flow

`refresh` (+roster, +second source if F) → notes → `build_index` (`data_updated`,
`roster`, list-valued community, per-item meta across sources) → `index.json` →
viewer: Gods tab, freshness stamp, add-god icon modal (dev), item picker modal,
multi community-build selector, fixed pick% popover.

## Testing

- **Python:** `build_index` emits `data_updated` (max last_verified) + `roster`;
  multi-community handling keeps N community entries and aggregates meta across
  them; second-source parser (if built) parses a saved fixture into build entries.
- **Viewer (vitest/RTL):** `godFilters` filter/sort; GodsIndex renders + narrows;
  the pick popover shows "off-meta" for pick=0 and a % otherwise; the add-god modal
  lists roster gods and marks tracked ones; the item-picker modal filters + adds;
  the community selector appears only when >1 build; the freshness stamp renders.
- **Manual/integration (Chrome MCP screenshots):** Gods tab + filters; add-god
  modal picks an untracked god and scrapes it; item modal adds an item to a build;
  freshness stamp + dev scraping banner; multi community builds (or the per-slot
  fallback). `npm run build` passes; static preview has no dev-only controls.

## Limitations / non-goals

- Second source is spike-gated; if no site reliably exposes multiple builds, we
  ship per-slot alternatives instead (stated up front, not a silent cut).
- The roster/icon modal needs a full god list; if the wiki list page is
  impractical, a committed `_roster.json` backs it.
- Freshness "scraping…" is dev-only (friends can't scrape); the timestamp is
  universal.
- No scoring-model changes here (that's the separate calibration/kit-scaling work).

## Open questions — resolved during design

- More community builds → add a second source (spike-gated; per-slot-alternatives
  fallback).
- Freshness UI → universal "data from <date>" + dev-only live scraping indicator.
- Proceed → one spec for the batch; plan sequences viewer-first, source last.
