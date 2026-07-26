---
target: God detail (Builds + Info)
total_score: 19
max_score: 40
na_heuristics: 
p0_count: 3
p1_count: 2
timestamp: 2026-07-26T15-59-42Z
slug: viewer-src-components-detailpanel-tsx
---
Method: dual-agent (A: a27d8b4e833eacb85 · B: a292fd69ef324ec51)

## Design Health Score

Surface mode: **Operate**. All ten heuristics apply.

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 2 | Switching to Joust silently deletes the Community tab *and* the entire Popular Items block with no notice. The WHY panel has no programmatic or visual association with the row that summoned it. |
| 2 | Match System / Real World | 3 | Genuinely good SMITE vocabulary — "buy earlier / buy later", "off-meta", "in for X". Undercut by `value 0.41 / fit 1.00`: unitless decimals on an unexplained scale, and `efficiency_tier` printed as a raw lowercase enum (`fair`). |
| 3 | User Control and Freedom | 2 | "+ New build" (`DetailPanel.tsx:228`) replaces the whole panel with no route change, so Back doesn't cancel it and the god header vanishes. Mode isn't in the URL — a shared `#/god/Ra` always reopens Conquest. |
| 4 | Consistency and Standards | 1 | `role="tablist"`/`role="tab"` (`:322`) with no `aria-controls`, no `id`, no roving tabindex, no arrow keys — and **zero `role="tabpanel"` exist anywhere in the app**. `ItemPickerModal.tsx:29` violates every clause of the Dialogs rule added to DESIGN.md this session. 87 nested-interactive violations in the sidebar. The same win rate renders `60%` in one column and `0.60` in another. |
| 5 | Error Prevention | 2 | The aspect toggle can strand you (below). Swaps with no `swap_item` render as unexplained disabled buttons (`:518`). |
| 6 | Recognition Rather Than Recall | 1 | The four score axes — `value / win / pick / fit` — are explained **nowhere in the application**, Legend included. The 0–1 scale has no stated meaning. Flavor names, `flex`, and the aspect concept live only in the Legend, which DESIGN.md now explicitly forbids ("don't let a surface outsource its explanation to one"). |
| 7 | Flexibility and Efficiency | 2 | No way to compare two builds, no deep link to a tab or mode, no keyboard path to the evidence panel. |
| 8 | Aesthetic and Minimalist Design | 2 | The Builds column has **no `max-width`**, so slot rows measure 1034px at 1440. 204 of 258 text-bearing elements render at ≤10.5px; 87 buttons are 7px type in a 14.6×14.5px box. The page ends in 451 characters of 12px italic grey. |
| 9 | Error Recovery | 2 | This surface's empty state is one line: `No build data yet for {god}.` (`:175`) — no heading, no cause, no next step. |
| 10 | Help and Documentation | 2 | The Legend is well-built and reachable, but it carries explanation this surface should own and still doesn't cover the score axes. |
| **Total** | | **19/40** | **Poor** |

For calibration: Home scored 18/40 before its redesign. This is the same level — the whole app sits here, and Home is now the outlier in the other direction.

## Design Specificity Verdict

**LLM assessment:** This is a generic detail pane with SMITE data in it, and the tell is the default state.

**Every god opens on the community build.** `DetailPanel.tsx:141` is `useState(0)`, and `entries[0]` is the community entry — I verified this holds for Ra, Cupid, Horus, Awilix, and Merlin. An application whose homepage now says *"We disagree with the meta on 53 of 69 ranked gods"* opens its deepest surface on the meta's answer. The model's own build is tab two.

The math is present in the data and discarded in the view. `slot_scores` carries `{total, efficiency, win, pick, fit}` — I read `Spear of Desolation: {total: 0.59, efficiency: 0.41, win: 0.6, pick: 0.51, fit: 1}` straight out of `index.json`. `WhyScoreBlock` (`:41-60`) renders four of those five and **silently drops `total`** — the composite the model actually ranks by. Four components, no weights, no sum, no composite: you can look at it, you cannot check it. And it's reachable only by hovering a row on desktop (`:425`), with no affordance saying so, on a tab you have to switch to first. Three gates in front of PRODUCT.md's first principle.

Meanwhile the index hands this surface everything Home used and it uses none of it. I confirmed `DetailPanel.tsx` contains **zero references to `tierlist`**, and `App.tsx:251` doesn't pass it. So `ours`, `community`, `tier_ours`, `tier_community` — all four, per god — never reach the page. Neither does `god_item_scores.Ra`, a ranked 40-item map whose values match `slot_scores.total` exactly. Not one score, one tier letter, one delta bar, or one `under`/`premium` mark appears on the surface where a player looks at six specific items for one specific god.

Own-world adherence is weaker than Home's too. All four section eyebrows (`:374, :406, :501, :546`) are `font-display tracking-widest`, not mono uppercase — the Mono-Label Rule broken four times on one screen, and again throughout `GodInfo`. Focus-blue is used as a decorative category tint on `effect_tags` (`:104`) and as the semantic "added" state on swap rows (`:435`), which is both the "no second accent hue" don't and a wasted opportunity: "the model swapped this in" is exactly what `under` exists to say.

**Deterministic scan:** `detect.mjs` returned **0 findings, exit 0** on `DetailPanel.tsx` + `GodInfo.tsx`, and **0 findings, exit 0** on `BuildEditor`/`ItemPickerModal`/`Tooltip`/`GodSidebar`. Verified as genuine, not a false negative: a widened run across all components returned 2 findings (`broken-image` ×2, both in `DetailPanel.test.tsx` — test fixtures, not shipping code), proving the toolchain fires, and `.impeccable/config.json` does not exist, so nothing is suppressed.

**Same lesson as Home, and worth stating plainly: token compliance is not design quality.** The detector is clean, there are zero hardcoded hex values in any component file, and the palette is disciplined. The defects below are all compositional and semantic — exactly the class no scanner sees.

What the browser caught that the detector cannot:
- **Contrast: zero failures on both tabs.** The `faint` change to `#7a8494` landed and holds — 4.52:1 on `bg3`, 4.80 on `bg2`, 5.11 on `bg0`. Worth noting the worst case clears by 0.02, so any surface lighter than `#171c24` breaks it.
- **No `<h1>` on `#/god/Ra`** — the only heading is `<h2>Ra`. **`#/god/Ra/info` has zero headings of any level**; `BASE STATS`, `ABILITIES`, `ABILITY ORDER`, `ASPECT` are styled `div`s. Zero `<section>` elements on either tab.
- **87 nested-interactive violations** — each sidebar row is a `div[role="button"]` containing two focusable buttons (`GodSidebar.tsx:66-86`). ARIA prohibits this.
- **299 focusables; 87 remove buttons measure 14.6×14.5px** with 7px type, failing the 24×24 WCAG 2.2 AA minimum. Template tabs are 24px tall — exactly at the floor.
- **A 414px layout jump** when hovering a build row: SITUATIONAL moves from `y=333` to `y=747`, because the WHY panel is inserted in normal flow above it (`:494`). DESIGN.md now forbids this in words.
- **The Builds column has `max-width: none`; the Info column has `max-width: 672px`.** Adjacent tabs on the same route differ by 362px of measure at 1440.
- **Scroll height is identical (919px) at 1280 and 1440** — 160px more viewport buys zero additional content, only wider rows.
- **25.7% of the Info tab is duplicated text.** Every ability renders twice: a raw blob and the same fields as parsed chips. 39 of 52 chips (75%) are verbatim duplicates of blob content, 540px of 2100px scroll height. **All six blobs contain the literal string `"Expand Ability Video"`** — source-site UI chrome shipped as body copy — and are prefixed `"Ra Notes:"`. Merlin's passive renders `"provides 1 stack of ."` and `"Firing a Attack consumes 1 stack of and deals Magical Damage"` — dropped template tokens, rendered verbatim.
- **Off-scale radii:** ~181 elements at 4px (bare `rounded`, 12 source usages) and 7 at 11px (`rounded-[11px]`, `App.tsx:170`), against the documented `6/10/14` scale.
- **Console: zero errors, zero warnings** across all eight route visits.

**Visual overlays:** Not available. The pane is not composited, so screenshots fail and injection was skipped. Every finding above is DOM/CSSOM/geometry-derived. Purely visual defects — z-order collisions, unintended overlap that doesn't change box geometry, animation stutter — were not measurable and are unreported.

**One correction where the two assessments appeared to conflict, because it's actually a finding.** I told both agents Awilix had no community data; A took it, B reported it didn't reproduce. Both are right about different fields. Awilix's `tierlist` entry is `{ours: 0.537, community: null, tier_ours: "S", tier_community: null}` — no community *rating* — while its build note carries a full community *build* with 10 popular items. So Home correctly lists Awilix among the 18 unranked, and god detail correctly shows its community build, and **nothing anywhere tells the player these are different things**. A god can be simultaneously "unranked" and "here's what the community builds."

## Overall Impression

The surface has real craft in its parts and no argument in its whole. The situational-swap mechanic is genuinely well-engineered, the SMITE vocabulary is native, and the mobile inline disclosure is a better interaction than its desktop counterpart. Then the page opens on the meta's build, hides the model's reasoning behind a hover, drops the composite score from the breakdown it does show, and never once states what the model thinks of this god.

**The biggest opportunity:** the Home→detail handoff is currently a reversal. A player clicks Cupid out of Home's Carry column having just read `0.45 · 0.68`, tier C against tier S — a two-tier argument they came to have — and the god page shows no score, no tier, no delta, and opens on the community build. Every number needed is one object lookup away in data the component isn't even passed. Making the header carry Home's exact row vocabulary would fix the seam, give the route an `<h1>`, and cost roughly 60px of the ~654px of width currently going unused.

## What's Working

1. **The situational-swap mechanic is the best-engineered thing on the surface.** Selecting a swap live-previews the resulting build (`applySwap`, `builds.ts:43`), strikes the removed slot, marks the added one inline, and states what it replaces plus a cost-derived "buy earlier / buy later" note gated behind a deliberate 15% no-op band (`:118`). "Where nothing shifts, print nothing" is the right instinct, and reusing `applySwap` to derive the replaced name rather than inventing a second targeting rule is disciplined.

2. **The mobile disclosure is the better interaction, and it's the one nobody sees.** Tapping a row expands the full item card inline — identity, stats, passive, tags, and the WHY bars — anchored to the row that owns them (`:481`). No layout-jump problem, no hover dependency, a clear affordance. Desktop got the worse version of the same idea.

3. **Contrast and token discipline are now genuinely clean.** Zero contrast failures across both tabs, zero hardcoded hex in any component file, three font families, three weights. The `faint` fix from the Home pass holds across this surface without further work.

## Priority Issues

### [P0] Every god opens on the community build
**What:** `DetailPanel.tsx:141` — `useState(0)`, and `entries[0]` is the community entry for every god I checked (Ra, Cupid, Horus, Awilix, Merlin).
**Why it matters:** the single most self-contradictory decision in the app. It also means the `off-meta` badges, `slot_scores`, the situational column, `flex` markers, and the rationale — everything the model produces — are all hidden on first paint.
**Fix:** default to the suggested `core` archetype (already computed at `:223` as `suggestedCore`), reorder the tablist so suggested flavors come first and community reads as the comparison, and relabel it: "Community" alone doesn't say "SmiteBrain high-elo", which is currently stranded in the Legend.
**Suggested command:** `/impeccable shape`

### [P0] The surface never states the model's verdict on this god
**What:** `:266-313` renders name, pantheon, role, damage type and stops. Verified: `DetailPanel.tsx` contains zero references to `tierlist`, and `App.tsx:251` doesn't pass it.
**Why it matters:** breaks the Home→detail handoff at its only seam, contradicts PRODUCT.md principles 1 and 3, leaves the route with no `<h1>`, and makes Awilix's unranked status invisible where Home states 18 unranked as content.
**Fix:** promote the header into an `<h1>`-level claim block reusing Home's row vocabulary — `model 0.53 · community 0.59`, the tier pair, the centred `under`/`premium` bar, the delta. For an unranked god print `community — · unranked` and one sentence, never a blank.
**Suggested command:** `/impeccable bolder`

### [P0] The score decomposition is hover-only, drops the composite, and shoves the page 414px
**What:** `whyIndex` is set on `onMouseEnter`/`onFocus` only (`:425`); the panel renders in normal flow above SITUATIONAL (`:494`). Measured: hovering row 0 moves SITUATIONAL from `y=333` to `y=747`. `WhyScoreBlock` (`:41`) renders `efficiency/win/pick/fit` and never `score.total` — confirmed present in the data as `0.59`. `ScoreBar` (`:32`) clamps the bar at 1 but prints the unclamped value, so a value >1 shows a full bar beside a number that disagrees with it.
**Why it matters:** the product's first principle is "show the math." The math is behind an invisible desktop-only gesture, is incomplete, and punishes you with a 414px yo-yo for looking.
**Fix:** reserve the right column's height unconditionally so SITUATIONAL never moves; default `whyIndex` to 0 so the panel is populated on arrival; render `total` as the headline with the four axes beneath it as contributions; give each row a persistent inline total so the row itself carries signal. And name the scale somewhere — `value/win/pick/fit` are explained nowhere in the app.
**Suggested command:** `/impeccable harden`

### [P1] Broken ARIA on both tab layers, plus an unguarded modal
**What:** `:322` — tablist/tab with `aria-selected` but no `id`, no `aria-controls`, no roving tabindex, no arrow keys; **zero `role="tabpanel"` exist anywhere in the app**. `App.tsx:245` — Builds/Info are plain buttons with no `aria-current`. `ItemPickerModal.tsx:29` — no `role="dialog"`, no `aria-modal`, no Escape, no focus trap, no focus return. `:421` — rows announce `aria-expanded` for a panel that is `md:hidden`. Plus 87 nested-interactive violations in `GodSidebar.tsx:66`.
**Why it matters:** a screen-reader user hears "tab, 1 of 6, selected", presses Right Arrow, nothing happens; presses Enter on a row, hears "expanded", nothing appears. `Legend.tsx` — rebuilt correctly this session — proves the pattern is understood; `ItemPickerModal` just never got it.
**Fix:** either implement the full tab pattern or drop to `<button aria-pressed>` in a `role="group"`. Port `Legend.tsx`'s focus-trap effect into `ItemPickerModal`. Suppress `aria-expanded` above `md`, or make the inline disclosure the single cross-breakpoint mechanism. Move the pin/remove buttons out of the row's `role="button"`.
**Suggested command:** `/impeccable audit`

### [P1] The Info tab is an unedited scrape with no headings
**What:** zero headings of any level on `#/god/Ra/info` and `#/god/Merlin/info`. Every ability renders twice — a raw blob plus the same fields as parsed chips — with 39 of 52 chips (75%) verbatim duplicates, accounting for 540px of the tab's 2100px scroll height. All six blobs contain `"Expand Ability Video"`; all are prefixed `"Ra Notes:"`. Merlin renders `"provides 1 stack of ."` and `"Firing a Attack consumes 1 stack of…"` — dropped template tokens. Merlin's missing `ability_order` and truncated ability list are silent omissions with no empty state.
**Why it matters:** Info is half this surface and currently reads as raw scraper output. The missing headings are an outright a11y defect on a page that is mostly prose.
**Fix:** give it an `<h1>` and real `<h2>` section headings; render `description` **or** `details`, never both; strip `"<God> Notes:"` and `"Expand Ability Video"` in the pipeline; state missing ability order as content.
**Suggested command:** `/impeccable clarify`

### [P2] The model's strongest evidence is rendered as an unreadable prose dump
**What:** `:579` — a 451-character `rationale` at 12px italic muted across a 1034px measure (~150ch), ending in 23 comma-separated item names ("Underrated for this god: Gluttonous Grimoire, The Cosmic Horror, …"). Meanwhile `god_item_scores.Ra` holds a ranked 40-item map, and `tierlist.items` carries per-item model-vs-community scores. Neither is passed to the component.
**Why it matters:** "underrated for this god" is the product's entire pitch, rendered as grey italic below the fold.
**Fix:** replace it with a ranked "Underpriced for {god}" strip built from `god_item_scores`, each item showing its model score against community with the same `under`/`premium` bar Home uses. Keep the leading clause as a short mono caption wrapped to ~68ch. This fills the width that's currently empty.
**Suggested command:** `/impeccable bolder`

## Persona Red Flags

**Alex (power user)** — Wants to compare the model's core against the community build. He can't: they're mutually exclusive tabs, and switching wipes the score panel. Hovers a row for numbers and the swaps he was about to click jump 414px away. Sees the same win rate as `60%` in one tab and `0.60` in another with no way to know they're the same number. Shares `#/god/Ra` after switching to Joust; his friend opens Conquest. Clicks "+ New build", the god context vanishes, and Back doesn't undo it.

**Sam (keyboard + screen reader)** — The skip link lands on `<main>`, which begins with the 87-god sidebar: **288 focusable elements before the build content**. No `<h1>` on Builds, **no headings at all** on Info, so heading navigation is useless. The tablist announces tab semantics arrow keys don't honor. Rows announce `aria-expanded` for a panel that's `md:hidden`. The WHY panel has no programmatic relationship to its row and no live region. The item picker is an untrapped overlay with no Escape. The 87 remove buttons are 14.6×14.5px.

**Kira (Masters, here to interrogate the model)** — Arrived from Home because Cupid showed `0.45 · 0.68`, C against S. The god page never mentions it and opens on the community build. She finds `core`, hovers, and gets four gold bars — `value 0.41, win 0.60, pick 0.51, fit 1.00` — with no total, no weights, no baseline, and no explanation of the scale anywhere in the app including the Legend. She sees `fit 1.00` on several items and can't tell whether that's a real ceiling or a clamp (it's a clamp on the bar; the number is unclamped). She sees "off-meta" badges but never a count or magnitude — never "the model's core shares 3 of 6 items with what people actually buy", a fact the page has both halves of and never computes. She can't argue with this. She can only look at it.

## Minor Observations

- `AppSkeleton` uses `w-64` (256px) for a sidebar that renders at `md:w-[300px]` — a **44px horizontal jump** on first paint, on a surface whose own stated rule is "shaped like the route that's actually coming." It also omits the tab row, mode toggle, STARTER, right column, and Popular Items.
- `text-muted/70` on alternate-item labels (`:461`) computes to 3.71:1 at 10px — the one Readable-Floor violation left, and its full content lives only in a `title` attribute, unreachable on touch.
- `"in core"` on popular-item tiles is **9px** (`:571`) while carrying a real signal.
- Cupid's template rail reads `Crit` where Ra/Horus/Awilix read `Fun-Crit 🎲` — two vocabularies for the same rail.
- The aspect toggle can strand you: `hasAspect` (`:179`) tests all builds including community, but the filter (`:183`) keeps only *suggested* entries with an aspect. Cupid + "Aspect: Love" collapses the tablist to a single `community` tab with the toggle still lit gold and no explanation.
- Header `count` shows `god.pantheon` ("Egyptian") on this route where every other route shows a count (`App.tsx:151`).
- `mineEntries` never re-reads on cross-tab `storage` events (`:157`).
- Off-scale radii: ~181 elements at 4px, 7 at `rounded-[11px]` (`App.tsx:170`).

## Questions to Consider

1. If the model's build and the community's build were shown **side by side in one view** — same six rows, two columns, disagreements marked — would you need the tablist at all? Six tabs may be a workaround for a comparison you never built.
2. `slot_scores.total` exists and is discarded. What weighted formula turns `0.41 / 0.60 / 0.51 / 1.00` into `0.59`? If it can't be printed, the four bars are decoration rather than evidence — and Kira will know in ten seconds.
3. Home's memorable moment is a systematic pattern made visible. What is god detail's? The strongest unused candidate is sitting in `god_item_scores`: 40 items ranked for this god, with the community's actual picks marked in that ranking.
4. Why is `under`/`premium` — the direction pair just widened from items to gods — absent from the one surface where a player studies six specific items for one specific god?
5. A god can be "unranked" on Home and simultaneously show a full community build here. Which is true, and where does the page say so?
