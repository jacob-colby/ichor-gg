---
target: Home page
total_score: 18
max_score: 40
na_heuristics: 
p0_count: 2
p1_count: 2
timestamp: 2026-07-26T15-07-12Z
slug: viewer-src-components-home-tsx
---
Method: dual-agent (A: a491eaf64d1c8a6af · B: a3d3b107480b4ac1c)

## Design Health Score

Surface mode: **Operate** (app home for a data tool). All ten heuristics apply.

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 2 | `Freshness` (`Home.tsx:220`) is honest and well-built but 11px `text-faint` at the page bottom. `AppSkeleton` (`App.tsx:90`) renders a sidebar+build-rows shape on *every* route including Home — the skeleton guarantees the jump it exists to prevent. No mode (Conquest/Joust) context on the tier slice. |
| 2 | Match System / Real World | 2 | "Top of the tier list" never says S-tier. `0.53 · 0.59` uses no player vocabulary. The words *underpriced*, *efficiency*, *kit fit*, *model* — the product's actual language per PRODUCT.md — appear nowhere on Home. |
| 3 | User Control and Freedom | 2 | Legend closes on backdrop click (`Legend.tsx:7`) but has no Escape handler, no visible ✕, no focus trap, no focus move on open. Pinned gods can't be unpinned from Home — `PinnedSection` (`Home.tsx:115`) renders bare `GodTile`s with no pin control. |
| 4 | Consistency and Standards | 2 | Two drifting god-chip variants: `GodTile` (`Home.tsx:96`, 44px icon / 11.5px name / flex-wrap) vs the inline tier tile (`Home.tsx:157`, 40px / 11px / CSS grid). Same object, different specs, non-aligned grids, only one has `aria-label`. Radii `rounded-xl` (12px) and `rounded` (4px) sit outside the declared `sm:6 / md:10 / lg:14` scale (`index.css:36`). Search is `max-w-xl` inside a `max-w-4xl` column — left edges align to nothing. |
| 5 | Error Prevention | 2 | No empty-search state — `HomeSearch` (`Home.tsx:75`) renders the `<ul>` only when `results.length > 0`, so a typo shows nothing at all. App-level error (`App.tsx:83`) has no guardrail path. |
| 6 | Recognition Rather Than Recall | 1 | The lowest score, and it is the product's core. `0.53 · 0.59` (`Home.tsx:165`) has no column header, no legend entry, no `title`, no tooltip, no `aria-label`. Awilix's lone `0.54` is unresolvable — model or community? The Legend that might explain it was dismissed on load and never explains this notation anyway. |
| 7 | Flexibility and Efficiency | 2 | Enter-to-first-match (`Home.tsx:52`) is a genuine accelerator. But `HomeSearch` has no `onKeyDown` at all: no arrow traversal, no `/` or Cmd-K focus hotkey, no recents, no unpin, no reorder. |
| 8 | Aesthetic and Minimalist Design | 2 | Not minimal — underfilled. Measured **231px dead space at 1280×800 (32%)**, **455px at 768×1024 (48%)**; the page does not scroll on desktop. The tier grid is `md:grid-cols-6` with 9 items → a full row plus an orphan row of 3 beside 3 empty cells. |
| 9 | Error Recovery | 1 | `App.tsx:86` surfaces `Failed to load index.json (HTTP 404)` verbatim as user-facing copy, on a bare `bg-bg0` with no chrome — and styles it `text-premium`, which DESIGN.md defines as "efficiency above fair price", not "error". No empty-search state. Sections vanish silently (`LatestPatch` returns `null`, `Home.tsx:182`). |
| 10 | Help and Documentation | 2 | The Legend is well-written but fires unprompted at first load, is dismissed forever (`smite:legend-seen`), and its first bullet says "Pick a god from the **left rail**" — Home has no left rail. |
| **Total** | | **18/40** | **Poor** |

18/40 is a harsh number and it deserves a caveat: the app *works*. Nothing here is broken. The score is dragged down by two clusters — the accessibility/semantics layer (heuristics 1, 3, 9) and the unlabeled-signal problem (heuristics 2, 6) — and those two clusters have the same root: **the page renders the model's output without rendering the model's meaning.**

## Design Specificity Verdict

**LLM assessment:** This is a generic dashboard shell wearing a good design system's clothes, and Home is where the disguise comes off. Swap the god portraits for avatars and "Top of the tier list" for "Top performers" and you have the home page of any SaaS analytics tool: centered search, empty-state paragraph, grid of tiles, timestamp. Nothing in the composition knows it is fronting a *deliberately contrarian mathematical model*.

The one place the thesis surfaces is `Home.tsx:165–168`:

```tsx
{scoreText(g.ours)}
{g.community != null && <> · {scoreText(g.community)}</>}
```

The model's verdict and the community's verdict side by side — the single most distinctive data structure in the entire product — rendered at **9.5px in `text-faint`, measured 3.03:1 contrast**, unlabeled, at the bottom of the tile hierarchy. Ra shows `0.53 · 0.59`: the model *dissenting from the meta*, which is literally the reason this product exists. Awilix shows `0.54` alone: one of the 18 gods with no community data, which PRODUCT.md is proud to surface honestly. The page explains neither. That is not density — it is an unlabeled debug print.

Arena Night as a *system* is authored and specific. The Home *composition* is not. It is the default arrangement a competent engineer reaches for when the brief is "make a home page." The user's own read — "a working script with a UI" — is exactly correct.

**Deterministic scan:** `detect.mjs` returned **0 findings, exit 0** on `Home.tsx`, and **0 findings, exit 0** across `App.tsx`, `GodSidebar.tsx`, `Footer.tsx`, `Legend.tsx`, `Skeleton.tsx`. Assessment B did not take that on faith — it verified the toolchain fires by planting a control file with deliberate anti-patterns, which returned 5 findings (`bounce-easing`, `design-system-color` ×2, `design-system-radius`, `design-system-font`), then deleted it. It also confirmed no `.impeccable/config.json` suppression exists and re-ran with `--no-config`.

**This is the most important finding in the report.** The clean scan is genuine. Token discipline is real: 3 font families (exactly the DESIGN.md set), 9 text colors (all tokens except plain white), 4 weights, zero horizontal overflow at 375/768/1280. **The problem is not drift. There is nothing to clean up.** The problem is that a page can be perfectly compliant with its design system and still have no composition, no hierarchy, and no argument. The detector cannot see the absence of a thesis.

What the detector missed and the browser caught:

- **6 contrast failures, all one root cause** — `--color-faint: #5b6472` cannot reach 4.5:1 on any of the four surface tiers. Measured: tier scores **3.03:1**, freshness **3.23:1**, footer **3.23:1**, header count **3.23:1**, dev chip **3.23:1**.
- **No `<h1>`, no `<main>`, no skip link, no `<footer>`** — landmarks are exactly `NAV, HEADER, NAV`. Document starts at heading level 2.
- **No author focus ring anywhere** — `outline-style: none` on 30 of 30 focusables; grep confirms zero `:focus-visible` rules and zero `outline` declarations in `index.css`. DESIGN.md reserves focus-blue for focus; it is implemented in exactly one place.
- **14 sub-44px tap targets at desktop widths** — six 36×36 rail icons, 12px-tall footer links, a 16px-tall "See full tier list →".
- **Type range is 14px → 9.5px.** Both `<h2>`s render at 14px. Nothing on the page is large. This is the mechanical cause of "flat, minimal hierarchy" — a page whose type scale spans 4.5px has no ratio to build hierarchy from.
- **296px layout shift per keystroke** — the search results `<ul>` (`Home.tsx:76`) is in normal flow with `mt-2`, so typing one character shoves `home-pinned` from y=169 to y=465.

**Visual overlays:** Not available. The browser pane is not composited in this session (`visibilityState: "hidden"`, `document.hasFocus() === false`), so `computer{action:"screenshot"}` fails and script-injection presentation was skipped. No user-visible overlay exists. All visual findings above are DOM/CSSOM measurements taken via `javascript_tool` at forced viewport sizes, not screenshots. Assessment B also flagged that real keyboard-Tab focus could not be delivered, so "no author focus ring" is confirmed from source rather than observed.

## Overall Impression

The craft floor here is higher than the score suggests, and that is what makes the gap frustrating. Someone thought carefully about degraded data — `Freshness`, `LatestPatch`, and `TierSlice` all return `null` rather than render an empty shell, and `Skeleton.tsx` carries a doc comment stating its own philosophy ("A centered 'Loading…' is the clearest tell that something is a script with a UI rather than a site"). That is the instinct of someone building a product.

Then the page built on those parts says nothing. A first-time visitor gets a blocking modal, a search box, a grey apology, nine tiles of unexplained decimals, an 11px timestamp, and 231 pixels of black. They never learn what ichor is. The word *model* never appears. The word *underpriced* never appears.

**The single biggest opportunity:** you have a product whose entire thesis is *"the model disagrees with the meta, and we'll show you where"* — and that disagreement is already computed and already on the page, nine times, rendered as illegible grey. Promoting the model↔meta delta from footnote to headline would simultaneously fix the specificity problem, the hierarchy problem, the empty-space problem, and the recognition problem. One move, four fixes. That is where the landing moment lives, and it costs no density because it occupies space that is currently measured as dead.

## What's Working

1. **The degraded-data discipline is real product character, correctly authored.** `Freshness` (`Home.tsx:220`) puts the relative date in the visible string and the absolute ISO in `title=`, appends the patch label only when present, and returns `null` entirely on an older index. Same rigor in `LatestPatch` (`Home.tsx:182`) and `TierSlice` (`Home.tsx:145`). It works because it never fabricates a state it can't back with data — a direct expression of PRODUCT.md principle 5. This is the pattern the rest of the page should be built on.

2. **Enter-to-first-match is the right accelerator for the right user.** `Home.tsx:52–55`. A returning player types three letters, presses Enter, and is on a build page. That is a genuine read of the repeat-visit loop, and the 44px-tall result rows are comfortably tappable. The keyboard model *around* it is incomplete, but the core instinct is correct — it's the only part of Home designed for a specific person.

3. **Token discipline is genuinely excellent and independently verified.** 3 font families, 9 colors, 4 weights, zero overflow at three breakpoints, and a clean detector run validated against a control. Whatever gets built next inherits a system that is actually being followed — which means the fixes below are compositional, not a cleanup.

## Priority Issues

### [P0] The model's own numbers are unlabeled, illegible, and stripped of the disagreement that is the product

**What:** `Home.tsx:165–168` renders the model score and community score in `font-mono text-[9.5px] text-faint` — measured 9.5px at **3.03:1**, failing WCAG AA by a wide margin. No header, no legend, no `title`, no `aria-label`. A single number (Awilix `0.54`) is indistinguishable from a missing one. `TierSlice` filters on `tier_ours === "S"` (`Home.tsx:146`) and then discards the most interesting fact in the comparison — which gods the model and the meta disagree about.

**Why it matters:** this is simultaneously the WCAG blocker and the positioning failure. PRODUCT.md principle 1 is "show the math, not just the answer"; principle 3 is "say when the model and the community disagree instead of smoothing it over." Home *does* show the disagreement and then renders it as grey noise. Every competitive player who lands here sees two decimals and no reason to care.

**Fix:** promote the score pair to primary tile content — ≥12px, model score in `text-ink-soft` or, per the Torchlight Rule's third clause, **in gold** (the model's own signal is one of gold's three legitimate uses, and gold currently appears on Home exactly twice: the logo and the active rail icon). Add a persistent mono micro-label decoding the notation once, in place (`MODEL · COMMUNITY`, 10px uppercase tracked). Render missing community data as an explicit `unranked` token, not an absent one. Give each tile a real `aria-label`. And when the two diverge past a threshold, mark it — a small `↑ meta` / `↓ meta` delta turns nine inert tiles into nine arguments, which is the product.

**Suggested command:** `/impeccable bolder`

### [P0] The first thing every visitor experiences is a blocking modal that describes a different page

**What:** `App.tsx:57` opens `Legend` on first load regardless of route. `Legend.tsx:7` builds it from a `div` with no `role="dialog"`, no `aria-modal`, no `aria-labelledby`, no focus trap, no focus move on open, no Escape handler, and no visible ✕ (backdrop click does close it — that part works). Verified live: `document.activeElement` stays `BODY`; a dispatched Escape leaves it open; the accessibility tree lists all 22 background controls ahead of the "Got it" button. Its first bullet reads "Pick a god from the **left rail**" — Home has no left rail.

**Why it matters:** WCAG 2.4.3 (focus order) and 4.1.2 (name/role/value), plus this *is* the product's first impression. 673 characters of grey body copy is the worst possible substitute for a landing moment, and it documents a screen the user is not on.

**Fix:** stop auto-opening it on Home. The arrival moment belongs to the page, not a modal — put the one-sentence thesis *in* the composition, next to the thing it explains. Keep the Legend as on-demand reference behind `?`, and when it opens make it a real dialog: `role="dialog" aria-modal="true" aria-labelledby`, focus the heading, trap Tab, close on Escape and a visible ✕, restore focus to the trigger. Make bullet one route-neutral.

**Suggested command:** `/impeccable onboard`

### [P1] No `<h1>`, no `<main>`, no focus ring, and a 14px→9.5px type range

**What:** measured live — zero `<h1>`, zero `<main>`, no skip link, `Footer.tsx` uses a `div`. Largest text on the page is the two `<h2>`s at 14px (`SectionHeader`, `Home.tsx:26`, `text-sm`). `outline-style: none` on 30 of 30 focusables, and `index.css` contains no `:focus-visible` rule and no `outline` declaration at all. Six `text-faint` uses fail 4.5:1.

**Why it matters:** the 4.5px type range is the mechanical cause of "flat grids, minimal hierarchy" — there is no ratio to build hierarchy from. For a screen-reader user, every route change dumps them at the top of a 7-button icon rail with no page identity and no way to jump to content. For a keyboard user, focus is invisible in a design system that explicitly reserves a color for it.

**Fix:** add a real `<h1>` carrying the product's claim in Rajdhani at 28–36px — this *is* the arrival moment being asked for, and it costs zero density because it lands in space currently measured as dead. Wrap routed content in `<main id="main">`, add a visually-hidden skip link, convert `Footer` to `<footer>`. Add one global `:focus-visible` ring in focus-blue. Re-pitch section headers as mono eyebrows *under* the h1 — that restores a three-step hierarchy (h1 → eyebrow → data) in place of the current one-step. Either raise `faint` to ~#6f7a8a or stop using it under 12px.

**Suggested command:** `/impeccable typeset`

### [P1] The page is 32–48% empty and does not scroll — density is claimed but not delivered

**What:** with zero pins, content spans y=91→537 in a 717px pane at 1280×800; `scrollHeight === clientHeight`; **231px dead**. At 768×1024: **455px dead (48%)**. With 7 pins at 768: still 370px dead. The tier grid (`Home.tsx:155`) is `md:grid-cols-6` with 9 items → an orphan row of 3 beside 3 empty cells at both tablet and desktop. `LatestPatch` returns `null` on live data, silently removing a third of the intended page — and per PRODUCT.md that is the *shipping* case, not an edge case.

**Why it matters:** the complaint isn't that the page is too tight, it's that it's unfinished — and the measurement backs it. A tool that leaves half the viewport black while claiming "density is the point" reads as a stub, not a stance.

**Fix:** author Home for the empty-patch-notes case, since that is the real one. Fill the frame with things only ichor has: the top model↔meta *disagreements* (already computed), the most underpriced items from the efficiency model, coverage stated proudly as content rather than caveat (87 of 89 gods; 18 unranked). Make the tier grid `grid-cols-3` at md for a clean 3×3, or take 8/12 so no orphan row exists.

**Suggested command:** `/impeccable layout`

### [P2] Search shifts 296px per keystroke with zero combobox semantics

**What:** `Home.tsx:75–91` renders results in normal flow. Measured: one character moves `home-pinned` 296px down the page. The input has no `role="combobox"`, `aria-expanded`, `aria-controls`, `aria-activedescendant`, or `aria-autocomplete`; the `<ul>` has no `role="listbox"` and the `<li>`s no `role="option"`; there is no `aria-live` region; `HomeSearch` has no `onKeyDown` at all, so Arrow Down does nothing and Enter-to-first-match is completely invisible.

**Why it matters:** the shift is the most visible "not shipped" tell on the page — the layout lurches under the cursor as you type. For a screen-reader user, typing produces total silence: no announcement that six results appeared, no way to walk them, no signal that Enter will fire.

**Fix:** make the dropdown `absolute` inside a `relative` wrapper so it overlays instead of displacing. Add the full combobox pattern plus Arrow Up/Down, Home/End, Escape-to-clear, a visible `bg-bg3` active-option highlight, and a polite live region announcing the result count. Add an explicit no-results state.

**Suggested command:** `/impeccable harden`

## Persona Red Flags

**Alex (impatient power user)** — Gets a blocking 673-character modal before touching anything; will click "Got it" without reading, permanently dismissing the only explanation of `0.53 · 0.59` in the app (`smite:legend-seen` never expires, `App.tsx:58`). No `/` or Cmd-K to focus search. Arrow keys do nothing in the result list, so he must reach for the mouse mid-flow or gamble that Enter lands right. The page lurches 296px as he types. After pinning seven gods he still can't unpin from Home or reorder them — pin order is raw insertion order (`pins.ts:27`). 231px of black under the fold, and the desktop rail is seven unlabeled 36×36 icons he has to hover-probe.

**Sam (keyboard + screen reader)** — Hard blocker on load: the Legend is not a dialog, focus never enters it, Escape doesn't close it, and reaching "Got it" requires tabbing past all 22 controls it visually covers. No `<h1>`, no `<main>`, no skip link. The nine tier tiles have no `aria-label` — their computed name is `"Ra0.53 · 0.59"`, a name followed by two undefined decimals, nine times. Search announces nothing. Every mono/metadata string fails AA (3.03–3.23:1). Card borders are `#1e2530` on `#12161d` — **1.18:1** — so tile boundaries are invisible under reduced contrast sensitivity, which contributes to the "flat grid" read for *everyone*. No author focus ring on 30 focusables.

**Kira (Masters-ranked mid, wants to interrogate the model)** — derived from PRODUCT.md's competitive-player audience. She lands and sees Loki, Bastet, Fenrir, Da Ji ranked S — a list she may violently disagree with — with no stated basis anywhere on the page. No "model score", no "gold efficiency", no "kit fit", no methodology link, no sample size, no mode. `0.53 · 0.59` on Ra is *literally the disagreement she came for*, and the page doesn't mark it, color it, sort by it, or name it. She can't tell Awilix's lone `0.54` means "no community data" — the design silently converts an honesty feature into an ambiguity. No Conquest/Joust context despite `App.tsx:45` holding mode state. Nothing links to *why*: PRODUCT.md principle 2, "never hide the reasoning behind it", has no expression on this surface at all. She has one move: leave.

## Minor Observations

- `App.tsx:90` renders the sidebar+build-rows `AppSkeleton` while loading **Home**, whose real layout is a centered 576px search over an 848px grid. `Skeleton.tsx` states its own goal as "mirror the real layout so the page doesn't jump" — on Home it guarantees the jump. A `HomeSkeleton` is ~15 lines.
- `App.tsx:83` error state has no chrome, no logo, no heading, and surfaces `Failed to load index.json (HTTP 404)` verbatim in `text-premium` — which breaks the Semantic Color Rule, since DESIGN.md defines `premium` as an efficiency signal, not an error color.
- `rounded-xl` (12px, `Home.tsx:58/76/194`) and `rounded` (4px, `Home.tsx:84`) fall outside the declared `sm:6 / md:10 / lg:14` scale in `index.css:36`. Tailwind overrides `sm/md/lg` from the theme but leaves `xl` at its default — a silent drift the detector's radius rule doesn't catch.
- `max-w-[84px]` truncation is applied to both chip types (`Home.tsx:106`, `:164`) but they measure 62px and 101px wide — dead code on one, wrong threshold on the other. "Baron Samedi" truncates in the pinned row and not in the tier row.
- `godIcon` (`Home.tsx:14`) sets `visibility: hidden` on second failure, leaving a 40–44px hole rather than an initial-letter fallback. 87 gods × two icon variants is a lot of surface for a silent hole.
- `SectionHeader`'s link (`Home.tsx:28`) is a `<button>` styled as a link that performs navigation. It should be an `<a href>` so it's middle-clickable, Cmd-clickable, and copyable — these URLs get pasted into Discord.
- Motion inventory on Home, measured: **exactly one** transition (a 180ms color set). Zero animations, zero transforms outside `.press:active`. Nothing enters, nothing staggers, nothing acknowledges arrival.
- `Section` (`Home.tsx:36`) adds only `w-full` and never varies — dead abstraction.
- The mobile bottom tab bar renders 6 labeled items; the desktop rail renders the same 6 as unlabeled 36×36 icons. The mobile treatment is strictly more usable than the desktop one.
- 13 `<svg>` elements carry no `aria-hidden="true"`. All sit inside labeled buttons so nothing is unnamed to AT — tidiness, not a barrier.

## Questions to Consider

1. If a player screenshots this page into a Discord with "this thing says Loki is S-tier" — what in the image tells anyone *why* they should care, or what ichor is? Right now: a timestamp and a Hi-Rez disclaimer.
2. You built a model that deliberately disagrees with the meta — rank correlation 0.36, a number PRODUCT.md is *proud* of — and rendered the disagreement at 9.5px in the lowest-contrast grey in the system. What would this page look like if the disagreement were the headline instead of the footnote?
3. The Legend explains the app better than the app explains itself, and you show it once, blocking, before the user has seen anything. Why does the explanation live in a modal instead of in the composition?
4. "Density is the point" — but Home is measurably 32–48% empty and doesn't scroll. Is density the actual value, or a post-hoc justification for small type?
5. Trace a fresh clone on day one: `TierSlice` → `null`, `LatestPatch` → `null`, `Freshness` → `null`, `PinnedSection` → one grey sentence. The entire page is a search box and an apology. Is that the state you designed, or the state you fell into?
6. Gold appears exactly twice on Home: the logo mark and the active rail icon. The Torchlight Rule reserves gold for selection, primary action, **or the model's own signal** — and the model's signal is all over this page, in grey. Why is the accent absent from the one thing it was reserved for?
