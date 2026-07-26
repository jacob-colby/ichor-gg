# Site polish, god sidebar, and draft page — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax.

**Goal:** Turn the viewer from a local tool into a site: a god sidebar that replaces the Gods tab, a standalone draft page with mode-aware team sizes and shareable URLs, richer build/swap/ability/community sections, and the polish (home page, meta tags, skeletons) that makes shared links look real.

**Spec:** `docs/specs/2026-07-25-site-polish-and-draft-page-design.md` — read it first; it holds the decisions and the rationale.

**Tech:** Python (pytest) for `abilities.py` + `popular_items`; Vite + React + TS + Tailwind v4 (vitest/RTL) for everything else.

**House rules:** TDD — failing test first. `npm run build` (`tsc -b`) is the real type gate and checks test files too. Commit only your own paths, never `git add -A`. Match the existing dark design system (`bg-bg2 border-line text-muted text-faint`, `.press`, `font-display`, `font-mono`).

---

## Ordering and parallelism

```
Wave 1 (independent):  P1 abilities.py     P2 popular_items
Wave 2 (independent):  V1 routing shell    V2 proportional threats
Wave 3 (needs V1):     V3 sidebar          V6 home page       V7 meta/OG
Wave 4 (needs V1+V2):  V4 draft page
Wave 5 (needs P1+P2):  V5 god-page sections
Wave 6:                V8 skeletons + freshness, then V9 verification
```

---

## Task P1 — Ability upgrade order

**Files:** Create `pipeline/smite/abilities.py`, `pipeline/smite/tests/test_abilities.py`. Modify `pipeline/smite/build_index.py`, `data/_weights.yaml`.

- [ ] **Step 1: Add config** to `data/_weights.yaml`:

```yaml
# Ability upgrade order is DERIVED (no source scrapes it) — see abilities.py.
abilities:
  ult_levels: [5, 9, 13, 17]   # SMITE 2: ult unlocks at 5, then every 4
  early_points: 1              # one point in each non-ult ability first
  max_levels: 20
```

- [ ] **Step 2: Failing tests** in `test_abilities.py`. `ability_order(god, scaling)` returns a list of 20 ability slots. Assert: ult appears at exactly the configured levels; each non-ult ability gets its early point before any is maxed; remaining points go to the highest-scaling ability first; the list is length 20 and contains only real ability slots; a god with no parsed scaling still returns a valid 20-level order (falls back to slot order).
- [ ] **Step 3: Run, confirm failure.** `cd pipeline && python -m pytest smite/tests/test_abilities.py -q`
- [ ] **Step 4: Implement.** Read `kit.py` for how ability scaling is parsed and reuse it — do NOT write a second parser. Also expose `summary(order)` → `{"max_order": ["2","1","3"], "ult_levels": [5,9,13,17]}` for the compact UI line.
- [ ] **Step 5: Emit.** In `build_index.build_index`, add `ability_order` to each god dict (order list + summary). Extend `test_build_index.py` to assert every god carries it.
- [ ] **Step 6: Full suite green.** `cd pipeline && python -m pytest smite/tests -q -m "not live"`
- [ ] **Step 7: Regenerate + commit.** `python -m smite.build_index`, then commit `abilities.py`, its test, `build_index.py`, `test_build_index.py`, `data/_weights.yaml`, `viewer/public/index.json`.

## Task P2 — Most-picked community items

**Files:** Modify `pipeline/smite/build_index.py` (+ a helper module if cleaner), `pipeline/smite/tests/test_build_index.py`.

- [ ] **Step 1: Failing test.** `popular_items` for a god: aggregates every community slot entry into `{name, pick_rate, win_rate}`, **dedupes across slots keeping the highest pick_rate**, sorts by pick_rate descending, and returns `[]` for a god with no community data.
- [ ] **Step 2: Confirm failure.**
- [ ] **Step 3: Implement**, attached per-god/per-mode to the community build entry in the index (`popular_items`). Remember community slots carry `alternates` — include those too, they're real picks.
- [ ] **Step 4: Full suite green.**
- [ ] **Step 5: Regenerate + commit.** Sanity-check a known god (Agni) has a sensible ordered list.

## Task V1 — Routing shell

**Files:** `viewer/src/lib/useHashRoute.ts` (+ test), `viewer/src/App.tsx` (+ test).

- [ ] **Step 1: Failing tests.** `Route.view` gains `"home"` and `"draft"` and loses `"gods"`; `#/` and an empty hash parse to `home`; `#/draft` parses; **`#/gods` redirects to home**; `toHash.home()` / `toHash.draft()` exist.
- [ ] **Step 2: Confirm failure.**
- [ ] **Step 3: Implement.** Update the `NAV` array to **Home · Builds · Draft · Items · Tiers · Patch** (pick fitting stroke icons in the existing style). Home is the default view. Leave the render branches for Home/Draft as `null` placeholders — V6/V4 fill them — but do NOT break the build.
- [ ] **Step 4: Tests + `npm run build` green. Commit.**

## Task V2 — Proportional threat scaling

**Files:** `viewer/src/lib/threats.ts` (+ test), `viewer/src/types.ts`, `data/_weights.yaml`.

- [ ] **Step 1: Failing tests.** `deriveThreats` records `enemyCount`; `threatOverlay` scales by `count / enemyCount` so **2 healers of 3 produces a larger bonus than 2 of 5**; an empty comp produces no bonuses and never divides by zero.
- [ ] **Step 2: Confirm failure.**
- [ ] **Step 3: Implement.** Rename `draft.per_enemy` → `draft.per_share` in `_weights.yaml` and rescale (`per_share ≈ per_enemy × 5`) so a full 5-god Conquest comp lands where it does today. Verify against the current behaviour: 2 healers of 5 must still promote Divine Ruin for Agni.
- [ ] **Step 4: Tests green. Commit** (include the `_weights.yaml` change + regenerated index if the value is emitted).

## Task V3 — God sidebar (retire `GodsIndex`)

**Files:** Create `viewer/src/components/GodSidebar.tsx` (+ test). Delete `GodsIndex.tsx` + its test. Modify `App.tsx`, `GodRail.tsx` (removed or absorbed).

- [ ] **Step 1: Failing tests.** Renders a 4-col grid of gods; search narrows; a lane pill filters; pinned gods render in a `PINNED` group above the rest; clicking a god selects it; the selected god is marked; empty result shows a Clear-filters affordance; the mobile picker opens and closes.
- [ ] **Step 2: Confirm failure.**
- [ ] **Step 3: Implement.** Lift the filter/pin logic out of `GodsIndex` (don't rewrite it — `filterGods`, `sortGods`, `usePins`, `roleAccent` all exist). Sticky search + lane pills; extra filters behind a "Filters" disclosure. Mobile: full-screen picker opened from a header button showing the current god.
- [ ] **Step 4: Delete `GodsIndex.tsx` + test; remove its imports.** Tests + `npm run build` green. **Commit.**

## Task V4 — Draft page

**Files:** Create `viewer/src/components/DraftPage.tsx` (+ test). Modify `viewer/src/lib/draft.ts` (+ test), `App.tsx`. Delete `DraftBar.tsx` + test (absorbed).

- [ ] **Step 1: Failing tests.** Mode toggle switches Conquest(5v5)↔Joust(3v3) and **truncates rather than clears**; ally slot 1 is labeled as yours; **with slot 1 empty the page shows the teaching empty state and no build**; filling it renders the adapted core; threat chips show shares (`2/3 healers`); URL round-trip — `#/draft?m=joust&me=Agni&e=Loki` parses, and entering a draft updates the hash; a URL draft beats localStorage; unknown god names are ignored.
- [ ] **Step 2: Confirm failure.**
- [ ] **Step 3: Implement.** `useDraft` gains mode + a `me` slot and URL encode/decode (`replaceState`, not push). Add a **Copy link** button. Reuse `deriveThreats`/`threatOverlay`/`adaptedCore` unchanged apart from V2's signature. Remove `DraftBar` from `DetailPanel`.
- [ ] **Step 4: Tests + build green. Commit.**

## Task V5 — God page: swaps, hover fix, abilities, popular items

**Files:** `viewer/src/components/DetailPanel.tsx` (+ test), `viewer/src/components/GodInfo.tsx` (+ test), `viewer/src/types.ts`.

- [ ] **Step 1: Failing tests.**
  - Swap entries show the swap item, `in for <replaced item>`, and an order-shift note **only** when the cost band differs (assert absence in the equal-cost case).
  - Hovering a build-order row shows item identity (name, `cost · tier`, stats/passive) **and** the four score bars — one hover, one panel.
  - The starter row no longer has its own separate tooltip.
  - `GodInfo` renders the ability order grid with ult levels marked and the heuristic disclaimer.
  - A popular-items section renders items with pick %, marks ones already in the core, and renders nothing when the god has no community data.
- [ ] **Step 2: Confirm failure.**
- [ ] **Step 3: Implement.** Fold item identity into the WHY card (this is the regression fix — remove the competing tooltip). Order-shift threshold reads from `_weights.yaml` via the index. Types for `ability_order` and `popular_items`.
- [ ] **Step 4: Tests + build green. Commit.**

## Task V6 — Home page

**Files:** Create `viewer/src/components/Home.tsx` (+ test). Modify `App.tsx`.

- [ ] **Step 1: Failing tests.** Renders a search that navigates to a god on submit; renders pinned gods, or a prompt when there are none; renders an S-tier slice from `tierlist`; renders the latest patch period when `patch_notes` is non-empty and omits the section when empty; shows the freshness stamp.
- [ ] **Step 2: Confirm failure.** **Step 3: Implement.** **Step 4: Tests + build green. Commit.**

## Task V7 — Meta tags, OG image, per-route titles

**Files:** `viewer/index.html`, `viewer/public/og.png`, `viewer/src/lib/useHashRoute.ts` or a small `useDocumentTitle` hook (+ test).

- [ ] **Step 1: Failing test** for the title helper: `documentTitle(route, god?)` → `Agni — ichor`, `Tier list — ichor`, `ichor — SMITE 2 build recommender` for home.
- [ ] **Step 2: Confirm failure. Step 3: Implement** the helper + wire it so the title updates on navigation.
- [ ] **Step 4: `index.html`** — real `<title>`, description, `og:title`/`og:description`/`og:image`/`og:url`, `twitter:card=summary_large_image`, `theme-color=#0b0e13`, favicon + apple-touch-icon.
- [ ] **Step 5: Create `viewer/public/og.png`** at 1200×630 — dark `#0b0e13` background, "ichor" in Rajdhani gold `#e3b23c`, the tagline "SMITE 2 build recommender", and a few god head icons as texture. Generate it with Pillow from `data/_assets/icons` so it's reproducible; commit both the tiny generator script and the PNG.
- [ ] **Step 6: Tests + build green. Commit.**

## Task V8 — Skeletons + relative freshness

**Files:** Create `viewer/src/components/Skeleton.tsx`. Modify `App.tsx`, `viewer/src/lib/` (a `relativeDate` helper + test).

- [ ] **Step 1: Failing test** for `relativeDate("2026-07-23", now)` → `2 days ago`; today → `today`; and it keeps the absolute date available for a `title`.
- [ ] **Step 2: Confirm failure. Step 3: Implement**, replace the bare `Loading…` with layout-matched skeletons, and swap the freshness stamp to relative-with-absolute-on-hover.
- [ ] **Step 4: Tests + build green. Commit.**

## Task V9 — Full verification

- [ ] `cd pipeline && python -m pytest smite/tests -q -m "not live"` — green.
- [ ] `cd pipeline && python -m smite.data_audit` — exit 0.
- [ ] `cd viewer && npx vitest run` — green. `npm run build` — clean.
- [ ] Browser: every surface at desktop **and** 390px — home, sidebar (incl. mobile picker), god page (swaps/hover/abilities/popular items), draft (both modes, you-slot gating, copy link), items, tiers, patch.
- [ ] Paste a draft URL into a fresh browser profile; confirm it reproduces.
- [ ] Confirm `#/gods` redirects and no dead nav entry remains.
- [ ] Report: test counts, index size delta, anything deferred.

---

## Self-review
- **Spec coverage:** A→V3 · B→V2+V4 · C→V5 · D→P1+V5 · E→V5 · F→P2+V5 · R1→V6 · R2→V4 · R3→V7 · R4/R5→V8 · R6→V4. All covered.
- **Deletions are explicit** (`GodsIndex`, `DraftBar`, the starter tooltip) so nothing is left orphaned.
- **Risk:** V5 is the largest task — if it stalls, split it into swaps+hover / abilities+popular-items.
