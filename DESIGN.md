---
name: ichor
description: A math-driven SMITE 2 build recommender — tactical, data-dense, dark.
colors:
  rail: "#05070a"
  bg0: "#0b0e13"
  bg1: "#0e1116"
  bg2: "#12161d"
  bg3: "#171c24"
  line: "#1e2530"
  line-strong: "#2a3342"
  ink: "#e8edf4"
  ink-soft: "#c3cad6"
  muted: "#8b95a5"
  faint: "#7a8494"
  torchlight-gold: "#e3b23c"
  focus-blue: "#4ea3ff"
  under: "#63c088"
  premium: "#c58b8b"
  role-guardian: "#7f9e97"
  role-warrior: "#b98a6d"
  role-mid: "#9d8bb3"
  role-hunter: "#b6a571"
  role-assassin: "#ab7a8c"
  dmg-physical: "#b98a6d"
  dmg-magical: "#8891b3"
typography:
  display:
    fontFamily: "Rajdhani, sans-serif"
    fontWeight: 600
  body:
    fontFamily: "Inter, sans-serif"
    fontWeight: 400
  label:
    fontFamily: "JetBrains Mono, monospace"
    fontWeight: 500
rounded:
  sm: "6px"
  md: "10px"
  lg: "14px"
spacing:
  sm: "8px"
  md: "16px"
components:
  button-primary:
    backgroundColor: "{colors.torchlight-gold}"
    textColor: "{colors.bg0}"
    rounded: "{rounded.md}"
    padding: "6px 16px"
  chip-active:
    backgroundColor: "{colors.torchlight-gold}"
    textColor: "{colors.bg0}"
    rounded: "9999px"
    padding: "4px 10px"
  chip-inactive:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    rounded: "9999px"
    padding: "4px 10px"
  card-default:
    backgroundColor: "{colors.bg2}"
    rounded: "{rounded.lg}"
  card-selected:
    backgroundColor: "{colors.bg3}"
    rounded: "{rounded.lg}"
---

# Design System: ichor

## Overview

**Creative North Star: "Arena Night"**

ichor reads like a battlefield after dark: a near-black field (`rail` / `bg0`) with one warm accent — torchlight gold — marking whatever matters right now, and role-tinted banners (guardian, warrior, mid, hunter, assassin) identifying the different lanes at a glance. Nothing about the surface competes with the data; the theme exists to make the model's output legible, not to decorate the app.

The philosophy is tactical and data-dense: small, precise labels; a lot of information per element (stats, signals, icons) held together by strict alignment; and a confident, instrumented feel closer to a mission console than a game skin. It deliberately avoids the cutesy rounded gradients and RGB-lightshow look common to "gamer" UI — that is the confirmed visual anti-reference. Gold is rare and load-bearing, not a brand color splashed everywhere.

**Key Characteristics:**
- Near-black surfaces stepped in four tiers (rail → bg0 → bg2 → bg3), each one step "closer" or more elevated.
- One accent (torchlight gold) reserved for selection, primary action, and the model's own signal.
- Role/lane colors are semantic, not decorative — they always mean "this is a Solo/Jungle/Mid/Carry/Support thing."
- Dense, mono-labeled data (font-mono, uppercase, tracked) sits next to display headings and Inter body text without ever feeling cluttered.
- Flat at rest; lift (shadow, glow) appears only when something is selected, active, or floating above the page.

## Colors

Palette is almost entirely a stepped near-black neutral scale, punctuated by one warm accent and a small set of semantic signal colors — there is no decorative secondary/tertiary hue family.

### Primary
- **Torchlight Gold** (`#e3b23c`): the single accent. Marks the selected god/card (`border-gold` + glow), primary buttons, active filter chips, and the model's own heuristic signal (score, "Suggested" tab). If gold appears, it means "this is chosen" or "this is the model talking."

### Secondary
- **Focus Blue** (`#4ea3ff`): reserved for interactive focus and links — a global `:focus-visible` ring (`2px solid`, `2px` offset) on every focusable, `focus-within:border-blue` on the search/input wrappers that opt out of the ring, and hover-underline on inline links. Never used for selection state; that's gold's job.

### Neutral (surface stack)
- **Rail** (`#05070a`): the outermost frame — the darkest layer, used for the thin mobile header bar.
- **Bg0** (`#0b0e13`): the app's base background.
- **Bg1** (`#0e1116`): modal/panel surfaces (e.g. the Legend dialog).
- **Bg2** (`#12161d`): resting card, input, and tooltip surfaces.
- **Bg3** (`#171c24`): selected/elevated card surfaces — one step lighter than Bg2, the visual "lift" for the active state.
- **Line** (`#1e2530`) / **Line Strong** (`#2a3342`): default and emphasized borders/dividers.
- **Ink** (`#e8edf4`) / **Ink Soft** (`#c3cad6`) / **Muted** (`#8b95a5`) / **Faint** (`#7a8494`): a four-step text hierarchy from primary content down to the quietest metadata labels.

### Semantic
- **Under** (`#63c088`): the model values this **above** the market — an item priced below the model's fair value, or a god the model rates above the community's meta.
- **Premium** (`#c58b8b`): the model values this **below** the market — an item priced above fair value, or a god the community's meta rates above the model.

These two are a **direction pair, not a good/bad pair**. They always answer one question — "which way does the model lean against the market?" — whether the market is an item's gold cost or the community's tier list. They are never used for success/failure or for error states; an error is `ink` copy with a primary recovery action, not a red-ish tint.

### Role & Damage Accents
- **Guardian** (`#7f9e97`), **Warrior** (`#b98a6d`), **Mid** (`#9d8bb3`), **Hunter** (`#b6a571`), **Assassin** (`#ab7a8c`): one per lane, used as text/border/dot accents on god cards and lane filters.
- **Physical** (`#b98a6d`, shared with Warrior) / **Magical** (`#8891b3`): damage-type accents on item and build stat displays.

### Named Rules
**The Torchlight Rule.** Gold is load-bearing, not decorative: it appears only on the current selection, the primary action, or the model's own signal. If a design use of gold isn't one of those three, it's wrong.

**The Semantic Color Rule.** Role and damage colors always carry meaning (a specific lane or damage type); never repurpose them as arbitrary decoration elsewhere in the UI.

**The Readable-Floor Rule.** Every text tier, including the quietest, clears WCAG AA (4.5:1) on every surface it can land on. `faint` is the floor at `#7a8494` — 4.52:1 on `bg3`, the lightest surface, and higher everywhere else. It was `#5b6472`, which measured 2.86–3.37:1 and failed AA in all six places it was used. A separator glyph (`·`, `/`) inherits its parent's tier rather than dropping to `line-strong`; a divider that can't be read is a divider that should have been a border.

## Typography

**Display Font:** Rajdhani (sans-serif fallback)
**Body Font:** Inter (sans-serif fallback)
**Measurement Font:** JetBrains Mono (monospace)

**Character:** A tactical, slightly technical pairing — Rajdhani's condensed geometric caps read as "console display" for names and headings, Inter carries all reading-length text cleanly, and JetBrains Mono sets the numbers. The instrument feel comes from figures that line up in a column, not from a typeface applied to everything small.

### The scale

Seven steps, defined once in `index.css` as `--text-*` theme tokens and used by name. **Never an arbitrary size.**

| Step | px | Use |
|---|---|---|
| `text-micro` | 10 | dense mono numerals inside a grid cell — the floor |
| `text-label` | 11 | section eyebrows, tags, secondary chrome |
| `text-small` | 12 | secondary content, chips, captions |
| `text-body` | 13 | default reading size |
| `text-lead` | 15 | intro paragraphs, dialog body |
| `text-title` | 20 | section titles, god/item names in a detail view |
| `text-display` | 32 | the one page claim per surface |

The app previously ran **sixteen** sizes with nine of them inside a 4px band (9 / 9.5 / 10 / 10.5 / 11 / 11.5 / 12 / 12.5 / 13), and 61–84% of every surface's text at or below 10.5px. That is why it read flat: with no ratio between steps there is no hierarchy to read, only small text. The scale is tight at the bottom because this is a dense data tool and open at the top so a page can make a claim.

**10px is a hard floor.** Nothing below it ships — the god sidebar was running 7px.

### Named Rules
**The Measurement Rule.** JetBrains Mono sets **quantities and the codes that align beneath them** — numerals, a unit bound to a numeral (`2500g`, `47% win`), tier letters, `T1`/`T2`/`T3`, score pairs, cumulative gold. Nothing else. The test is: *would it be wrong if these characters didn't line up in a column?* If yes, mono; if no, Inter or Rajdhani.

The one non-numeric exception is the **section eyebrow** — the `text-label` uppercase tracked line that titles a section or a table column. That is the brief's "small mono labels", and it is a *system*: one per section, never a general-purpose style for secondary text.

Everything else sets in the reading faces, including the words *around* a number. `mean +0.03 · 4 below · 5 differ` is a mono run containing three English words; it splits, and only the figures stay mono.

This replaces the Mono-Label Rule, which read "any piece of UI that names a category, state, or count sets in JetBrains Mono". In a data tool that is nearly every string: a lane is a category, `no community data` is a state, and the app followed the rule faithfully into **73% of the items shelf, 65% of the tier list and 51% of Home being set in the label face**. The measure of the failure is that mono had stopped meaning anything — when the body face *is* the mono face, a number no longer stands out from the sentence around it. Named, so it is not re-derived: navigation, actions, verdicts, names, states, effect tags, and prose are **never** mono, however small they are.

**The Linkable-State Rule.** Anything the visitor chose that changes what a surface shows — filters, sort, mode, subject — lives in the hash query string, not in `useState`. "The disputed Mid gods in Joust" and "the undervalued tier-3 anti-heal" are the things this app exists to produce, and for a year none of them could be sent to anyone. Defaults stay out of the query, so a bare `#/tiers` keeps meaning what it always meant; navigating *within* a filtered view carries the query along (`keepQuery`), because clearing the filters that produced the card someone just clicked is never what they asked for. Writes are debounced `replaceState` — a search box bound straight to the address bar trips Safari's 100-writes-per-30s limit in about three seconds of held backspace, and a Back button that walks a query backwards one character at a time is worse than no history at all.

**The Seam Rule.** Every surface names at least one other surface it hands off to, in the visitor's terms rather than as a route label. A destination reachable only from the nav rail is a destination most visitors never form an intent to reach — the draft board sat unlinked for a year. A seam carries state where state exists: "Draft with Chaac" keeps the comp already entered rather than replacing it, because a link that silently discards saved work is worse than no link.

**The One-Claim Rule.** Every surface states its own claim in `text-display`, once, carrying live numbers. The app chrome never repeats it: the header used to print a per-route count that contradicted the surface's own ("159 items" over a shop reading "30 items"). Chrome carries navigation, freshness and actions — nothing the surface is already responsible for saying.

## Layout

Two-pane shell: a fixed god-picker rail (300px on desktop, collapsing to a full-screen modal picker below `md`) beside a flexible detail/build column. Grids default to 4 columns for god cards and `auto-fill, minmax(140–180px)` for item/tier grids, so density adapts to viewport without a manual breakpoint per grid. Sticky, blurred headers (`sticky top-0 backdrop-blur`) keep search/filters visible while the grid below scrolls. Spacing stays tight and consistent with Tailwind's default scale (`gap-1.5–3`, `p-2–5`); nothing airy — density is the point.

## Elevation & Depth

Flat at rest. Depth is used sparingly and only to mark state, not to decorate every surface.

### Shadow Vocabulary
- **Card** (`0 6px 16px rgba(0,0,0,0.35)`): floating surfaces resting just above the page — tooltips, popovers.
- **Raised** (`0 10px 28px rgba(0,0,0,0.45)`): modals and dialogs (Legend, pickers) that sit fully above the page.
- **Glow** (`0 0 0 1px rgba(227,178,60,0.4), 0 4px 14px rgba(227,178,60,0.15)`): the selected-state halo on a god card — the one place shadow doubles as the accent color.

### Named Rules
**The Flat-Until-It-Matters Rule.** Surfaces are flat at rest. Shadow only appears for a floating layer (tooltip, modal) or a selected state (glow) — never as ambient decoration on a resting card.

## Shapes

Corners step with surface size: `sm` (6px) on tight controls like icon buttons and small tags, `md` (10px) on the default control/card radius (inputs, buttons, most cards), `lg` (14px) on modals and the primary god-card frame. Filter chips and status dots go fully round (`rounded-full`) to read as discrete tokens rather than panels. Borders are hairline (`border-line`) by default, stepping up to `border-line-strong` on hover/emphasis, and gold on selection.

## Components

Components should feel **tactile and confident**: presses register physically (a quick 0.97 scale-down on active, 120ms), borders and state changes are unambiguous, and nothing waits on hover alone to communicate state.

### Buttons
- **Shape:** `rounded-md` (10px) for standard buttons; `rounded-full` for filter/chip buttons.
- **Primary:** `bg-torchlight-gold` on `text-bg0`, `px-4 py-1.5`, medium weight — reserved for the one confirming action per view (e.g. Legend's "Got it").
- **Chip/filter (active):** `bg-torchlight-gold text-bg0 font-semibold`; **(inactive):** transparent with `border-line` and muted or role-tinted text.
- **Press:** every tappable button/card carries the shared `.press` class (scale 0.97 on `:active`, 120ms, respects `prefers-reduced-motion`).

### Cards
- **Corner Style:** `rounded-lg` (14px) for the primary god-card grid; `rounded-md` for smaller item/tier cards.
- **Background:** `bg-bg2` at rest; `bg-bg3` (or a `bg3→bg2` gradient when pinned-but-unselected) when elevated/selected.
- **Border:** `border-line` at rest, `border-line-strong` on hover, `border-gold` (+ `shadow-glow`) when selected.
- **Internal Padding:** tight — `p-1.5`–`p-2.5` depending on card size.

### Inputs / Fields
- **Style:** `rounded-md`, `border-line`, `bg-bg2`, muted placeholder text.
- **Focus:** border shifts to `focus-blue` (`focus-within:border-blue` on the wrapper); no glow or shadow on focus, border color alone carries the state. The inner `<input>` is the one element allowed to keep `focus:outline-none`, because its wrapper already shows the state.
- **Everything else** takes the global `:focus-visible` ring — `2px solid focus-blue`, `2px` offset. Never remove it without replacing it with an equally visible state.

### Dialogs
- Real dialogs only: `role="dialog"`, `aria-modal="true"`, `aria-labelledby` pointing at the heading. Focus moves to the heading on open, Tab wraps inside the panel, Escape and a visible ✕ both close, and focus returns to the trigger on unmount.
- **Never open a dialog unprompted.** Reference material (the Legend) is reached from its `?` control; a surface explains itself in its own composition rather than in an interstitial the visitor didn't ask for.

### Search (combobox)
- `role="combobox"` on the input with `aria-expanded`, `aria-controls`, `aria-activedescendant`; `role="listbox"`/`role="option"` on the results.
- Results **overlay** the page (`absolute`) — they never displace content, because a list that pushes layout makes the page lurch on every keystroke.
- Arrow Up/Down wrap, Home/End jump, Escape clears, Enter takes the active option. A polite live region announces the match count, and an explicit "no match" row replaces silence.

### Segmented controls (not tabs)
- Mutually-exclusive choices use `role="group"` with an `aria-label` and `aria-pressed` buttons — **not** `role="tab"`. The app ships no `role="tabpanel"`, and a tablist without one announces a keyboard model that doesn't exist.
- **Never make the model and the community mutually exclusive.** The comparison between them is the product; a control that shows one *instead of* the other is the wrong control. The community is a constant second track, not an option.

### Build ledger (god detail)
- Purchases sit on a **cumulative-gold spine**: a right-aligned mono gold figure per row against a continuous `border-r border-line` hairline. Gold spent, never elapsed time — the index carries item costs and no timings, so a time axis would be invented.
- Each row carries its composite score with a gold bar, its four contributing axes as plain numbers, and what the community does with the same item. None of it is behind a hover; a row expands in place on click, identically at every breakpoint.
- A running total is `null`, not approximate, when any item's cost is unknown — a total with a hole in it misstates the build.
- The four axes are shown as **contributions, never a sum**: the weights that produce the composite aren't published, so nothing in the UI may imply they add up.

### Value receipt (items shop)
- An efficiency verdict is shown **decomposed, never as a bucket alone**: `3000g · fair 2756g · +244g`. The three-value label on its own could say "Premium" but not by how much, which is the number that decides a purchase.
- The detail is a **receipt**: each stat at its fitted gold price, subtotalled, against the actual cost. The pipeline ships `item_gold_values` so this is auditable rather than asserted, and `cost - predicted_cost === residual` holds exactly so the arithmetic on screen always closes.
- Sort on the **continuous residual**, never the bucket — bucketed sorting tied 30 items for first alphabetically and made the most underpriced item unfindable.
- Filter options are **derived from the data**. A hardcoded list shipped a `Glyph` option matching nothing while the one Relic was unreachable.
- Where the model declines to score something, **say why**: tier-1 starters buy an ability rather than stats and sit out the fit on purpose. That is a finding, not a blank — never an em dash.

### Draft diff (draft board)
- A re-rank is shown as a **displacement**, never as a lone arrival: `Divine Ruin · replaces Rod of Tahuti · +0.12 · answers anti-heal`. Keep both builds — the un-adapted one reduced to a membership set is why rows could say "swap in" with nothing to swap in for.
- The magnitude is the model's own bonus, drawn as an `under` bar scaled to the configured clamp. Direction colour is `under` (the model promoting something), never focus-blue.
- **Signals are denominated by the roster, not by how much the visitor has entered.** One known healer of five slots is a 20% signal. Dividing by entries made a 20%-complete draft drive a maximal overlay that then *weakened* as more enemies were added — the model appearing to change its mind.
- Always state how much is still unknown (`3 of 5 enemies known · this build will keep moving`), and render threats that measured zero so absence is distinguishable from not-looked-at.

### Tier bands (tier list)
- Bands are always **the model's** tiers. The community is a **ghost on every card** (`meta B · +0.05`, `meta agrees · S`, or `unranked`), never a second view reached by a toggle — a control that shows one ranking *instead of* the other forces the reader to hold one in memory to compare.
- Tier letters use a neutral ramp (`gold` for S only, then `ink` → `ink-soft` → `muted`). Never borrow `under`/`premium` to mean a tier letter; they mean direction against the market everywhere else.
- Each band states its own agreement tally (`6 disputed · 1 agreed · 2 unranked`), and the page-level summary describes the **whole filtered set**, not the narrowed view — otherwise "only disputed" would make the agreement count read as zero.

### Data bars (divergence)
- A hairline (`3px`) track on `bg-bg3` with a centre tick in `line-strong`; the bar grows outward from centre — `under` to the right, `premium` to the left — scaled to the largest absolute value on the board.
- The bar is the measurement, not decoration: the numeric value always sits beside it, and the row's `aria-label` states both source values and the gap in words.

### Tooltip
- `rounded-md`, `border-line`, `bg-bg2`, `shadow-card`, small (`text-xs`) copy. Flips above/below the trigger and shifts horizontally to avoid clipping; opens on a short hover delay but instantly on keyboard focus (`role="tooltip"`).

### App chrome (rail + header)
- The rail is **labelled**, not icon-only: each destination is an icon above a `text-micro` mono uppercase label, matching the mobile tab bar. Icon-only navigation made a first-timer hover-probe seven unlabelled squares while the mobile bar had carried labels all along.
- Active state is `bg-bg2` + gold glyph, with `aria-current="page"` — never colour alone.
- The header carries the brand anchor, freshness and actions. **No page title and no count** — see the One-Claim Rule.

### Navigation (god sidebar)
- Desktop: fixed 300px column, `border-r border-line`, sticky blurred search/filter header above a scrolling 4-column grid.
- Mobile: collapses to a single header trigger button (`bg-bg2`, current god's icon + name) that opens a full-screen modal picker reusing the same grid/filter body.

### Skeletons (loading state)
- Flat `bg-bg2` bars shaped exactly like the real layout they precede (never a centered spinner or "Loading…" text), animated with a slow `motion-safe:animate-pulse` opacity pulse only — no shadow, no shimmer sweep.
- **Shaped like the route that's actually coming.** Home gets a claim-block-over-lane-board skeleton; build routes get the sidebar/build-rows one. A skeleton shaped like a different page guarantees the jump it exists to prevent.

## Motion

Motion is rationed. A surface gets **one authored moment** — the thing it does in life — not a scattering of hover effects.

- **Eases:** `--ease-standard` (`cubic-bezier(0.2, 0.8, 0.2, 1)`) for state and colour transitions, 120–180ms. `--ease-out-expo` (`cubic-bezier(0.16, 1, 0.3, 1)`) for the authored entrance.
- **Home's moment:** the divergence bars draw outward from the centre line, 440ms, staggered 70ms per lane column (0 → 280ms). Every label, tier, and number is already on screen; only the measurement animates — the page never fades in from blank.
- **The press:** the shared `.press` scale-down (0.97, 120ms) on every tappable element.
- Everything respects `prefers-reduced-motion: reduce`, and reduced motion means *arriving at the final state instantly*, never rendering nothing.

## Do's and Don'ts

### Do:
- **Do** reserve torchlight gold for selection, primary action, or the model's own signal (score/efficiency) — see the Torchlight Rule.
- **Do** set numbers, units bound to a number, and section eyebrows in JetBrains Mono — and nothing else, per the Measurement Rule. A word that happens to sit beside a figure is not a measurement.
- **Do** put chosen state in the URL, and carry it across navigation within the same view, per the Linkable-State Rule.
- **Do** keep loading states as layout-shaped skeletons (pulsing `bg-bg2` bars), never a spinner or centered "Loading…".
- **Do** use the shared `.press` scale-down for every tappable element, and respect `prefers-reduced-motion`.
- **Do** give a surface a real `<h1>` that states its claim, with `<main>`, a skip link, and a heading order that starts at level 1.
- **Do** name what the model and the community each said, in words, wherever a bare score appears — a decimal with no label is a debug print, not a signal.
- **Do** state coverage gaps as content (`18 of 87 gods have no community data yet`), not as an apology or a silent omission.
- **Do** read the per-mode data slice when a mode is selected. `tierlist.gods` mirrors Conquest; showing it in Joust asserts community ratings that don't exist for that mode at all.
- **Do** distinguish an unmeasured signal from a measured zero. A neutral default (`win 0.50`, `pick 0.00`) rendered as a number reads as a finding — say "not measured here" instead.
- **Do** label a running total for what it actually covers. "16,550g core" when the starter isn't on the spine; never "total".

### Don't:
- **Don't** add shadow to a resting surface for decoration — shadow means "floating" (tooltip/modal) or "selected" (glow), per the Flat-Until-It-Matters Rule.
- **Don't** repurpose a role/lane or damage-type color for anything other than that specific lane or damage type.
- **Don't** introduce rounded gradients, neon glows, or angular esports-style slashes — the confirmed anti-reference for this system.
- **Don't** add a second accent hue alongside torchlight gold; secondary interactive state is focus-blue's job, not a new color.
- **Don't** use `under`/`premium` for anything but "which way the model leans against the market" — they are a direction pair, never success/failure and never an error colour.
- **Don't** open a dialog the visitor didn't ask for, and don't let a surface outsource its explanation to one.
- **Don't** let a dropdown, disclosure, or result list sit in normal flow where it displaces the page as it opens.
