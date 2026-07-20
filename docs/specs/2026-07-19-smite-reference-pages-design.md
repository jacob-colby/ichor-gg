# SMITE 2 viewer: reference pages (items shop, god info, legend, routing)

Status: approved, ready for implementation plan
Date: 2026-07-19

## Problem

The viewer only shows builds. The user wants it to also be a **reference**:
- A filterable **items shop/index** for all 159 items showing each item's
  efficiency rating (Underrated / Fair / Overrated), stats, passive, tags.
- Each god's page gains an **Info** view: abilities + base stats + aspect. The
  scraped abilities are currently just names + slots, so ability data is
  **re-scraped richer** (descriptions + detail rows).
- A **first-run legend** explaining the app (builds, sources, flavors, aspects,
  buy-order/flex, that scores are heuristics).
- Items and gods get **shareable URLs** (hash routing) so friends can link to a
  specific item or god.

## Design

### Part A — Richer ability scraping (Python)

`wiki_parser._parse_abilities` currently captures `{slot, name, cooldown?, cost?}`.
Extend it to also capture:
- `description`: the ability's main descriptive text (the non-`<li>` text of the
  ability table, cleaned).
- `details`: a list of the labeled detail lines (every `<li>` in the table —
  Cooldown, Cost, Damage, Range, Radius, etc.) as `["Cooldown: 12/11/…", …]`
  strings. Robust to per-ability variation (no scaling-coefficient math).

`refresh --all` re-scrapes the 10 gods (Cloudflare-gated Playwright), `build_index`
passes the enriched abilities through (they already ride along in god data), and
the `Ability` type gains `description?: string; details?: string[]`. Conservative
scope: capture what's on the page; don't synthesize scaling numbers.

### Part B — Hash routing + top nav (viewer foundation)

A tiny dependency-free `useHashRoute` hook parses `location.hash` into a route and
re-parses on `hashchange`; navigation sets `location.hash`. Routes:

| Hash | View |
|---|---|
| `#/` | Builds, no god selected |
| `#/god/<Name>` | Builds for that god (Builds tab) |
| `#/god/<Name>/info` | That god's Info tab |
| `#/items` | Items shop |
| `#/items/<Name>` | Items shop with that item's detail open |

A top nav bar holds **Builds** / **Items** tabs and a **?** help button (opens the
legend). Works on static hosts (hash only — no server rewrites). The current
`selectedGod`/`mode` component state is derived from the route in `App`.

### Part C — Items shop page

A filterable, sortable grid of item cards (`ItemsShop.tsx`):
- **Card**: icon, name, cost, tier badge, top stats, effect-tag chips, and an
  **efficiency badge** — `undervalued`→**Underrated** (green), `fair`→**Fair**
  (muted), `premium`→**Overrated** (amber/red), `null`→**—** (untiered).
- **Filters** (a bar/sidebar): text search (name), tier (1/2/3), efficiency
  (Underrated/Fair/Overrated/Untiered), effect tag (multi-select from the 10
  tags), and a "has stat" select (from the ~19 stat keys). Sort: name, cost ↑/↓,
  efficiency.
- **Item detail** (route `#/items/<Name>`): a panel/modal with full stats,
  passive, cost/tier, tags, efficiency, and `builds_from`/`builds_into` shown as
  clickable links to those items. Reuses the existing tooltip body, expanded.
- All client-side over `index.json` items; pure filter/sort helpers are unit-tested.

### Part D — God Info tab

On a god's page, a **Builds | Info** toggle (in the header row). Info renders:
- **Identity**: pantheon · role · damage type · release date.
- **Base stats table**: from `god.base_stats` (`{stat: {base, per_level}}`) —
  formatted rows (Health, Mana, Protections, Speed, …) with base + per-level.
- **Abilities**: one block per ability — slot, name, `description`, and `details`
  lines (from Part A).
- **Aspect**: name + `kit_changes` (if the god has one).
Deep-linked at `#/god/<Name>/info`.

### Part E — First-run legend

A dismissible overlay shown on first visit (localStorage `smite:legend-seen`),
reopenable via the **?** nav button. Explains: the god rail + builds; **suggested**
(heuristic, our scoring) vs **community** (SmiteBrain meta) vs **mine** (your
saved builds); **flavors** (crit/burst/…); **aspect** toggle; **mode** toggle;
**BUILD ORDER** + **flex** slots; the **Items** shop + efficiency ratings; and a
one-line honesty note (heuristics, fan project). Concise, skimmable.

## Data flow

Wiki → `wiki_parser` (richer abilities) → god notes → `build_index` → `index.json`
(gods carry enriched abilities; items already carry efficiency_tier + tags) →
viewer routes: Builds (rail + DetailPanel), god Info (base stats + abilities +
aspect), Items shop (filter/sort + item detail). Mine builds stay in localStorage.

## Testing

- **Python**: `_parse_abilities` extracts `description` + `details` from a fixture
  ability table (plus the existing slot/name/cooldown/cost); a stat-only table
  still yields name/slot with empty details.
- **Viewer (vitest/RTL)**: `useHashRoute` parses each route shape and updates on
  hashchange; the item filter/sort helpers filter by tier/efficiency/tag/stat and
  sort by cost/name/efficiency; `ItemsShop` renders cards and narrows on a filter;
  the efficiency badge maps tiers to Underrated/Fair/Overrated; the god Info tab
  renders base stats + abilities; the legend shows on first run and hides after
  dismissal (localStorage), reopens via the ? button.
- **Manual/integration**: re-scrape + regen; browse the items shop with filters;
  open an item's deep link; open a god's Info tab (abilities + stats); confirm the
  legend on first load and the ? reopen; `npm run build` (deploy build) passes;
  static preview: routing + legend + shop work with no backend.

## Limitations / non-goals

- Ability data is scraped as description + detail lines — **no** scaling-coefficient
  modeling (the recommender's god-fit stays archetype-based).
- No separate Gods index page (the rail is the god picker); god info is a tab on
  the god page.
- Hash routing only (no history API / server routes) — fine for static hosting.
- Items shop is client-side over `index.json`; no server search.

## Open questions — resolved during design

- Gods browsing → Info tab on the god page (no separate Gods index).
- Ability depth → re-scrape richer ability data (description + detail lines).
- Deep links → hash routing (`#/items/<name>`, `#/god/<name>/info`).
- Efficiency labels → undervalued=Underrated, fair=Fair, premium=Overrated,
  null=Untiered.
