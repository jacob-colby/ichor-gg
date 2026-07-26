# ichor — site polish, god sidebar, draft page

Status: approved, ready for implementation plan
Date: 2026-07-25

## Problem
The viewer still reads like a local tool: it opens on "Select a god from the
rail", links share as a grey box titled `viewer`, drafts can't be sent to a
friend, and the god picker is a narrow icon strip. This spec covers six
requested features plus six polish items that close the tool→site gap.

## Decisions taken up front
1. **The sidebar replaces the Gods tab.** A 4-column sidebar with search,
   filters and pins does exactly what `#/gods` does, so `#/gods` is retired
   rather than kept as a near-duplicate.
2. **Threats scale by share of team, not raw count.** 2 healers out of 3 in
   Joust is a bigger threat than 2 out of 5 in Conquest; proportion captures
   that with no per-mode retuning.
3. **Ability order is derived from kit scaling**, not scraped or hand-entered,
   and is labeled a heuristic wherever it appears.

---

## A. God sidebar (replaces `GodRail` and `#/gods`)

`GodsIndex.tsx` is retired; its capabilities move into the sidebar.

- **Layout**: fixed-width left column, scrollable, **4-column** grid of god
  cards (head icon + name + lane accent). Selected god carries `shadow-glow` +
  gold border; hover brightens per the design system.
- **Top of sidebar** (sticky): search field, then a compact filter row — lane
  pills (Solo/Jungle/Mid/Carry/Support in their role colors) plus pantheon and
  damage-type selects behind a "Filters" disclosure so the default view stays
  clean.
- **Pinned gods** float into a `PINNED` group above the main grid, reusing the
  existing `usePins` localStorage hook and pin-button interaction.
- **Empty result**: muted "No gods match" + Clear filters.
- **Mobile**: the sidebar becomes a full-screen god picker opened from a header
  button showing the current god; picking one closes it. The bottom tab bar is
  unchanged.
- **Routing**: `#/gods` is removed from `Route.view`, its nav entry drops, and
  any incoming `#/gods` redirects to home. Nav becomes
  **Home · Builds · Draft · Items · Tiers · Patch**.

## B. Draft page (`#/draft`)

Moves off the god page into its own surface; the `DraftBar` on `DetailPanel`
is removed in favor of it.

- **Mode toggle** (top, segmented): **Conquest → 5v5**, **Joust → 3v3**. Mode
  drives team sizes *and* feeds the existing mode profile into scoring.
- **Teams**: an ally row and an enemy row of god slots. Conquest = 5 allies
  (including you) + 5 enemies; Joust = 3 + 3. Switching mode truncates extra
  slots rather than clearing the draft.
- **Slot 1 of allies is you** — visually distinct (gold ring, "You" label).
  **Until it is filled the page shows a teaching empty state**, because there
  is no god to build for. Once filled, suggestions render immediately and
  update as further slots are entered.
- **Threat read-out**: chip row of derived threats, now expressed as shares
  (`3/5 magical`, `2/3 healers`).
- **Output**: the adapted core (section C) plus the reasons already produced by
  `draftBuild`.
- **Shareable URL** (see R2).

### Threat model change — proportional scaling
`deriveThreats` gains the enemy-team size; `threatOverlay` multiplies by
`count / team_size` instead of `count`. `_weights.yaml` `draft.per_enemy` is
rescaled to a `per_share` value so magnitudes land where they do today for a
5-god comp (i.e. `per_share ≈ per_enemy × 5`). Ally coverage logic is
unchanged. The existing clamp (`max_bonus`) still bounds total influence.

## C. Core build + situational swaps

Replaces the current flat situational-chip row, on both the god page and the
draft page.

- **Core 6** rendered as today (icon, name, cost, flex marker).
- **Below it, a swap list.** Each entry shows the swap item and, in small muted
  text beneath: **what it comes in for** (`in for Spear of the Magus`) and,
  when the purchase position changes, **how the order shifts**
  (`buy 3rd instead of 5th`).
  - The replaced item is whatever `applySwap` already targets (lowest-scored
    eligible slot) — surface that rather than inventing a second rule.
  - **Order shift** is derived from cost banding: compare the swap item's cost
    to the item it replaces; if it is materially cheaper it moves earlier, if
    dearer it moves later, otherwise the order note is omitted. Threshold in
    `_weights.yaml`. Where nothing shifts, print nothing — no filler text.
- Clicking a swap still previews it against the core using the existing diff
  styling (added blue / removed struck-through).

## D. Ability upgrade order (god page)

- **New pipeline module** `abilities.py`: `ability_order(god, kit_profile)` →
  a 20-level list plus a compact summary (`max 2 → 1 → 3`, `ult at 5/9/13/17`).
- **Heuristic**, in this priority: put one early point in each non-ult ability
  for utility; take the ult at every level it unlocks; otherwise spend points
  maxing abilities ranked by the damage scaling `kit.py` already parses,
  tie-broken by slot order. All knobs (early-points count, ult levels) live in
  `_weights.yaml` under `abilities:`.
- **Emitted** into `index.json` as `gods[].ability_order`.
- **Viewer**: on the god Info tab, a compact level grid (1–20, ult levels
  highlighted gold) plus the summary line, with an explicit
  *"derived from ability scaling — a heuristic, not community data"* note.

## E. Fix: item info on hover in the build order

**Regression.** Build-order slot rows lost their `<Tooltip>` when the draft
feature introduced the hover-driven WHY card; only the starter row still has
one. Two hover mechanisms competing is the underlying problem.

**Fix**: fold item identity into the WHY card so one hover gives everything —
name, `cost · tier`, stats, passive, efficiency badge, effect tags, **and** the
four score bars. Slot rows keep `onMouseEnter`/`onFocus`. On mobile the inline
disclosure gains the same content. The starter row's separate tooltip is
removed so there is exactly one pattern.

## F. Most-picked community items (god page)

A section distinct from the community *build*: what this god's playerbase
actually buys, as items rather than an ordered build.

- **Pipeline**: aggregate the god's community build slots into a per-item
  `{name, pick_rate, win_rate}` list, sorted by pick rate, deduped across
  slots (keep the highest pick). Emit as `builds[].builds[].popular_items` on
  the community entry, or alongside it — implementation's choice, but it must
  be per-god and per-mode.
- **Viewer**: a grid of item cards showing icon, name, **pick %**, win %.
  Items already in the suggested core are marked so the overlap is legible.
- Gods with no community data show nothing (not an empty shell).

---

## Polish (the six recommendations)

**R1 — Home page (`#/`).** Replaces "Select a god from the rail" as the
landing view. Contains: a prominent search that jumps straight to a god; your
**pinned gods** (or, with none, a short "pin gods to keep them here" prompt);
the **top of the tier list** (S-tier gods, both sources); the **latest patch
changes** if any exist; and the freshness stamp. Nav gains a Home entry, which
becomes the default route.

**R2 — Shareable draft URLs.** Encode the draft in the hash:
`#/draft?m=conquest&me=Agni&a=Ymir,Ra&e=Loki,Thor,Hel`. On load, a URL draft
wins over localStorage; entering a draft updates the URL (replaceState, so it
doesn't spam history). A **Copy link** button on the draft page. Unknown or
untracked god names are ignored gracefully, as they already are.

**R3 — Meta tags.** `<title>` is currently `viewer`. Set a real title
(`ichor — SMITE 2 build recommender`), description, `og:title` /
`og:description` / `og:image` / `og:url`, `twitter:card=summary_large_image`,
`theme-color` (`#0b0e13`), and a proper favicon + apple-touch-icon. Ship a
committed 1200×630 `og.png`. **Per-route document titles** too
(`Agni — ichor`, `Tier list — ichor`), since these get pasted into Discord.

**R4 — Skeletons.** Replace the bare `Loading…` with skeleton cards matching
each surface's real layout (sidebar grid, build rows, item grid). No spinners.

**R5 — Relative freshness.** Render `Updated 2 days ago` with the absolute
date on hover; recompute from `data_updated`.

**R6 — Draft empty state.** The draft page is empty until you pick your god, so
that state must teach: one line on what the page does, and a visible cue that
the first ally slot is you. Never an error, never a blank panel.

---

## Data flow
`refresh` → `recommend` (+ new `abilities.py`) → `build_index` emits
`gods[].ability_order` and per-god `popular_items` alongside the existing
`god_item_scores` / `tierlist` / `patch_notes` → viewer renders Home, the god
sidebar, god page (build + swaps + abilities + popular items), and the Draft
page.

## Testing
- **Python**: `ability_order` respects ult levels, spends early points, maxes by
  scaling, and totals 20 levels; `popular_items` sorts by pick rate, dedupes
  across slots, and is empty when the god has no community data;
  `build_index` emits both keys and stays hermetic to the vault root passed in.
- **Viewer (pure)**: proportional threat scaling (2/3 > 2/5 for the same tag);
  mode switch truncates rather than clears; swap "in for" target matches
  `applySwap`; order-shift note appears only when the cost band changes; draft
  URL encode/decode round-trips and survives unknown names.
- **Viewer (component)**: sidebar filters/pins/selection and its mobile picker;
  `#/gods` redirects; draft page gates output on the user's slot; hover shows
  item info *and* score bars; popular-items section renders pick %; home page
  renders pinned gods, tier slice and patch slice; skeletons appear while
  loading.
- **Manual**: desktop + 390px on every surface; a shared draft URL opened in a
  fresh browser reproduces the draft; a link unfurls correctly (validate OG
  tags with a checker).

## Limitations to state in the UI
- Ability order is a **heuristic derived from ability scaling**, not community
  or pro data.
- Popular items reflect SmiteBrain's covered gods only; 18 gods have no
  community signal and simply won't show the section.
- Draft suggestions still use the last data refresh's scores; no live re-scoring.

## Non-goals
- No payload splitting — `index.json` is 3.9 MB raw but ~300 KB gzipped.
- No accounts, no server, no analytics. The site stays static.
- No new scraping sources.
