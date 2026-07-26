---
target: Items shop
total_score: 21
max_score: 40
na_heuristics: 
p0_count: 2
p1_count: 2
timestamp: 2026-07-26T18-43-51Z
slug: viewer-src-components-itemsshop-tsx
---
Method: dual-agent (A: a01d26e810e1647b3 · B: ac1af9d89bc0cb7aa)

## Design Health Score

Surface mode: **Operate**. All ten heuristics apply.

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 2 | Clicking a card mid-grid inserts the detail panel **4342px above the viewport** — measured. The surface's only interaction produces no visible feedback. No live region; `App.tsx:120` serves the sidebar-shaped skeleton to this route. |
| 2 | Match System / Real World | 3 | `g`, `T3`, icons and passive text are native SMITE vocabulary. Undercut by a `Glyph` filter option for a tier the data doesn't contain, and by `—` meaning nothing. |
| 3 | User Control and Freedom | 2 | The detail panel has **zero close controls** — browser Back is the only exit. No "clear filters". Filter state isn't in the URL, so a filtered view is unshareable and lost on reload. |
| 4 | Consistency and Standards | 1 | **Zero headings of any level in the entire document.** Filter bar is `position: static` where DESIGN.md mandates sticky. `text-blue` used as a content colour on effect tags (`ItemsShop.tsx:59`) — a second accent by the back door. The signal is called `Efficient` here and `under` everywhere else. |
| 5 | Error Prevention | 2 | The `Glyph` option (`ItemsShop.tsx:150`) matches **zero** items — a guaranteed dead end. `Relic` exists in the data but is absent from the filter, so one item is unreachable. Seven items have duplicated `builds_from`, producing a React duplicate-key warning when their detail opens. |
| 6 | Recognition Rather Than Recall | 3 | The card is genuinely scannable. But the only definition of Efficient/Premium is one 11px line that scrolls away, as does the filter bar. |
| 7 | Flexibility and Efficiency | 2 | Sort-by-Rating orders by **bucket** (`itemFilters.ts:40-41`), so 30 items tie for first and the most-underpriced item in the game isn't findable. Search matches `name` only — typing `anti-heal` returns nothing while a tag filter for it sits two controls away. |
| 8 | Aesthetic and Minimalist Design | 3 | The card is a well-packed object and contrast is clean throughout. But **74.7% of all text on the page is 10px**, and the largest text anywhere in `main` is 14px. |
| 9 | Error Recovery | 1 | **No empty state, no no-results state, no bad-link state.** A no-match search collapses the grid to `height: 0` and leaves 614px of blank pane. `#/items/Not An Item` renders the plain shop while setting `document.title` to the bogus name — a silent 404. |
| 10 | Help and Documentation | 2 | One sentence. It never explains the regression, the 12 nulls, or the 106-item community gap. |
| **Total** | | **21/40** | **Acceptable** |

Session calibration: Home 18, god detail 19, draft 15, items shop **21**. This is the **best-scoring** surface of the five and the first to clear the "Poor" band — the craft is sound; the failures are that it won't show its own numbers.

## Design Specificity Verdict

**This surface invented the app's central idea and then forgot it.**

`pipeline/smite/efficiency.py:94-104` fits a non-negative least-squares regression of item cost onto item stats and produces four numbers per item — `residual` (actual cost minus the cost its stats predict), `z`, a normalized `score`, and a `tier` label. Its own docstring says the continuous score is what the aggregator consumes and `tier` is "the report label".

Then `pipeline/smite/build_index.py:72`:

```python
it["efficiency_tier"] = eff.get(it["name"], {}).get("tier")
```

**Three of the four numbers are discarded at the pipeline boundary.** So the one surface whose entire job is *"is this item worth its gold"* renders a 10px chip reading `Fair` — 80 of 159 items get that identical chip — and never tells you what fair price the model computed, or by how much the item misses it. Rod of Tahuti costs 3000g and is stamped `Premium`; the shop can't say whether that means 3050g-predicted (noise) or 2100g-predicted (a 900g passive tax). Those are completely different purchases.

PRODUCT.md principle 1 is "show the math, not just the answer." The math exists, is computed on every pipeline run, and is deleted one line later.

**Meanwhile the same item argues properly one route away.** `tierlist.items` carries `ours`, `community`, `tier_ours`, `tier_community` for all 159 items — and `App.tsx:228` passes the shop only `items` and `openItem`. Glorious Pridwen is a two-tier disagreement on `#/tiers` and a grey shrug on `#/items`.

And the direction pair got renamed in transit: `under`/`premium` reads as **Efficient/Premium** here (`itemFilters.ts:51,53`) — a quality word paired with a price word, which isn't a direction pair and doesn't read as the same system as the four redesigned siblings.

**Deterministic scan:** 0 findings, exit 0 on `ItemsShop.tsx`, `ItemPickerModal.tsx`, `Tooltip.tsx`. Verified non-vacuous — the same binary returns exit 2 (`overused-font`) on `index.css`, and no config suppression exists. Assessment B correctly flags that `.tsx` inputs run in regex mode, so this is "no regex-detectable anti-pattern", not a clean bill of health.

**Fifth surface running where a clean detector sat on a 15–21/40 design.** Token discipline here is genuinely good: 2 font families, all radii on-scale (6px and 10px only), zero hardcoded hex, zero stale greys.

What the browser caught instead:
- **Zero headings, document-wide.** The page title "Items" is a `<span>`; the item detail name is a `<div>`.
- **Zero contrast failures on text** — lowest pair 4.80:1. But **non-text contrast fails**: the card border is `#1e2530` on `#0b0e13` = **1.25:1**, card fill vs page **1.07:1**, hover border **1.52:1** (needs 3:1). Those are the only visual identification of 159 card buttons and 5 selects.
- **Six interactive elements with no accessible name** — the search input (placeholder only) and **all five selects**. A screen reader announces five unnamed comboboxes in a row.
- **All 159 cards render at once**; 1785 DOM nodes inside `main` (94.6% of the document), 159 concurrent icon requests on first paint, and `ItemCard` isn't memoized, so every keystroke re-renders every match.
- **The active filter is pixel-identical to the four inactive ones** — measured identical border, background, colour, and weight.
- **The header says "159 items" while the shop says "30 items"** — two contradictory counts on screen simultaneously.
- No horizontal overflow at any width; only 26px unused width at 1440. Density is real here.

## Overall Impression

This is the best-built of the five surfaces and the most frustrating, because the gap is a single deleted field. The card is a genuinely good dense object — icon, name, gold cost, tier, efficiency chip, community win rate, sample size, and tags in 78px — and it's *shared* with `ItemPickerModal`, so the shop and the build editor speak one card language. That reuse is the right instinct.

Then a player asks the one question the surface exists to answer, and gets an adjective.

**The biggest opportunity reaches into Python.** Shipping `predicted_cost` and `residual` alongside the existing label turns `Premium` into `3000g · fair price 2140g · +860g premium`, and the detail can show the stat-by-stat gold attribution the regression already computes — `predicted_cost` is literally a sum of `stat × marginal gold`. That table *is* the math, and it exists today.

## What's Working

1. **The card is a well-packed object and it's shared.** `ItemsShop.tsx:42-64` fits eight facts into 78px without feeling stuffed, and `ItemPickerModal.tsx:70` reuses it. One card language across two surfaces is the right instinct and should survive any redesign.
2. **Contrast and token discipline hold under measurement without anyone re-touching the file.** Lowest text pair 4.80:1; 2 font families; radii only 6px and 10px, both on-scale; zero hardcoded hex. The Readable-Floor Rule survived here for free.
3. **The component graph is real and already wired.** `builds_from`/`builds_into` render as chips that navigate, and `#/items/:name` works correctly on cold load. That's the skeleton of a much better surface.

## Priority Issues

### [P0] The efficiency model is a label with the math amputated
**What:** `build_index.py:72` keeps only `tier`, discarding the `residual`, `z`, and `score` computed at `efficiency.py:113-118`. `App.tsx:228` additionally withholds `tierlist`, so the shop can't show the community's letter either.
**Why it matters:** this surface originated `under`/`premium` and is now the only one that won't show its own numbers. Three buckets for 159 items, where 80 share one label, is not a decision aid.
**Fix:** ship `predicted_cost` and `residual` per item; decompose the verdict on the card (`3000g · fair 2140g · +860g`) and show the stat-by-stat gold attribution in the detail. Pass `tierlist` through so the community's letter shows as a ghost, as on the tier list. **This reaches into the Python pipeline.**
**Suggested command:** `/impeccable bolder`

### [P0] Clicking an item does nothing visible
**What:** `ItemsShop.tsx:126-128` renders the detail as the first child of the scrolling column. Measured: scroll to the end of the grid, click the last card → the hash and title update and the panel materialises at `top: -4342px`. Nothing changes on screen, focus stays on `<body>`, nothing is announced. The panel also has **zero close controls**.
**Why it matters:** this is the surface's only interaction, and it silently does nothing for anyone who didn't arrive by deep link.
**Fix:** make it a real dialog per the pattern `Legend.tsx` already ships — Escape, a visible ✕, focus move and return — rather than a disclosure that displaces the grid.
**Suggested command:** `/impeccable harden`

### [P1] Three coverage gaps, all silent
**What:** **106 of 159 items have no community data** and `MetaBadge` (`ItemsShop.tsx:36-39`) simply returns `null`. **12 items** have `efficiency_tier: null` and render as `—`. **127 of 159** reference `builds_from` components absent from the item set, so items render a dangling `Builds from:` with nothing after it.
**Why it matters:** PRODUCT.md principle 5 is "be honest about coverage gaps rather than papering over them." The 12 nulls are null for a *principled* reason — `efficiency.py:61-68` excludes tier-1 starters because their gold buys an ability, not stats — and that sentence would be the most interesting thing on the page. It's written nowhere.
**Fix:** `no community data` and `not scored · starter` as explicit content; state the dropped components as a count; add a page-level `53 of 159 items have community data`.
**Suggested command:** `/impeccable clarify`

### [P1] No empty state, no no-results state, no bad-link state — and a filter that guarantees the first
**What:** `Glyph` (`ItemsShop.tsx:150`) matches zero items — the tier values are `[3, 2, "Relic", 1]`. Selecting it yields a grid of measured height **0px**. A no-match search does the same, leaving 614px of blank pane. `#/items/Not An Item` renders the shop while setting the tab title to the bogus name.
**Fix:** add a no-results block naming the active filters with a clear control; delete `Glyph`, add `Relic`; extend search to `effect_tags`, stat names and `passive`; add a not-found notice.
**Suggested command:** `/impeccable harden`

### [P2] It doesn't read as part of the redesigned system
**What:** zero headings; filter bar not sticky; five native selects where siblings use `role="group"`+`aria-pressed`; `text-blue` as a content colour; `Efficient` where the system says `under`; sort-by-Rating ties 30 items; 74.7% of text at 10px.
**Fix:** an `<h1>` stating the claim from live numbers (*"30 of 159 items are priced below what their stats are worth"*); `sticky top-0 backdrop-blur` on the filter row; segmented controls for Tier and Rating (4 values each); sort by the continuous score once it ships; rename the label so one signal has one name.
**Suggested command:** `/impeccable typeset`

## Persona Red Flags

**Alex (power user)** — wants the most underpriced item in the game and cannot get it: sort-by-Rating ties 30 items alphabetically. Wants to compare two items — impossible, the URL holds one and the panel replaces itself. Wants to share a filtered view — filter state isn't in the URL. Wants the residual — computed and deleted at the pipeline boundary. Every question he has, the data can answer and the UI cannot.

**Sam (keyboard + screen reader)** — catastrophic. Zero headings, so no structural navigation at all. Five selects and a search input with **no accessible name** — five unnamed comboboxes in a row. No live region, so filtering 159 → 0 is announced as nothing, into a container that then contains nothing. Activating a card changes the URL and title but moves no focus and announces no change. 166 sequential tab stops with no bypass.

**Kira (Masters, "is this worth its gold?")** — asks one question and gets an adjective. `Premium` on Rod of Tahuti says the model thinks she's overpaying but not by how much — so she can't weigh it against the passive, which is exactly the judgement the help text tells her to make while withholding the number she'd need. Blinking Abyss is stamped `Premium` on `stats: {}` — the regression saw an empty stat line and priced it as pure tax, an artifact presented identically to a real finding. And she can't ask "worth it *for whom*": `god_item_scores` holds 40 ranked items per god and the shop never touches it.

## Minor Observations

- Seven items have duplicated `builds_from` (Rod of Tahuti is `["Evil Eye","Evil Eye"]`), producing a React duplicate-key warning when those details open — which is why one assessment saw it and the other didn't.
- The efficiency chip is Inter 10px, not JetBrains Mono, while the `159 items` count beside it *is* mono. The Mono-Label Rule broken inconsistently within one bar.
- Card names use `.truncate` with no `title`: 25 truncate at 1440, **57 at 375**. "Hide of the Nemean Lion" is unreadable and unrecoverable.
- At 768 the grid yields only **3 columns at 215px** where 4 would fit at ~170px — density left on the table exactly where it's scarcest.
- At 375 the filter bar is **112px, 17.7% of the visible pane**, before a single item appears.
- Card heights are ragged — 78px for 135 cards, 89px for the 24 with tags — so rows containing a tagged item are 11px taller.
- Stat rows in the detail are raw key/value with no damage-type accent, despite DESIGN.md defining `dmg-physical`/`dmg-magical` "on item and build stat displays".
- `EFFICIENCY[3]` is a selectable filter option labelled `—`. A filter named after a punctuation mark.
- `source_url` and `last_verified` exist on every item and neither is shown.

## Questions to Consider

1. If `residual` is computed for all 159 items and discarded one line later, what is the shop *for*? The tier list already shows a better efficiency read of the same items.
2. The most interesting sentence in this codebase is `efficiency.py:61-68` — tier-1 starters are excluded because their gold buys an ability, not stats. That's the model naming its own blind spot. It renders as `—`.
3. Blinking Abyss has `stats: {}` and gets `Premium`. Should an item whose entire value is invisible to the regression carry the regression's verdict at all, or say *"not priceable — value is in the passive"*?
4. `god_item_scores` holds 40 ranked items per god and no surface uses it. What is this shop if it has a god selector — "underpriced *for Ra*" instead of underpriced in the abstract? Isn't per-god underpricing the actual positioning claim?
5. Every sibling refused a source toggle because the comparison is the product. This surface has no toggle — but also no comparison. Is that better or worse?
