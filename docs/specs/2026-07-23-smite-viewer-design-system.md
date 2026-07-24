# SMITE 2 Viewer — Design System implementation spec

Source: Claude Design handoff "SMITE 2 Design System.dc.html". Direction:
Discord-refined dark + Clash Royale card depth + Notion spacing/restraint.
Whole-app redesign. Tokens live in `viewer/src/index.css` `@theme` (Tailwind v4)
→ use utility classes (`bg-bg2`, `text-muted`, `border-line`, `rounded-md`,
`shadow-card`, `ease-standard`, `text-role-mid`, etc.). Add `.press` class to
every tappable card/pill/tab for the 0.97 press feedback.

## Tokens (all live as Tailwind utilities now)
Surfaces: `rail #05070a` (icon rail/frame) · `bg0 #0b0e13` · `bg1 #0e1116` ·
`bg2 #12161d` (cards/fields) · `bg3 #171c24` · `line #1e2530` · `line-strong #2a3342`.
Text: `ink #e8edf4` · `ink-soft #c3cad6` · `muted #8b95a5` · `faint #5b6472`.
Accent: `gold #e3b23c` (primary) · `blue #4ea3ff` · `under #63c088` (undervalued) ·
`premium #c58b8b` (overpriced).
Role: `role-guardian #7f9e97` · `role-warrior #b98a6d` · `role-mid #9d8bb3` ·
`role-hunter #b6a571` · `role-assassin #ab7a8c` · `dmg-physical #b98a6d` ·
`dmg-magical #8891b3`. Map a god's role token by its primary role word; damage by
`damage_type`. Helper: derive a role→token map in `lib`.
Radii: `sm 6px` (chips/small) · `md 10px` (fields/cards) · `lg 14px` (portraits).
Shadows: `shadow-card` (rest) · `shadow-raised` (hover, sparingly) · `shadow-glow`
(selected/pinned gold glow). Motion: 120ms press / 180ms hover+tab / 280ms modal+pin,
`ease-standard`. Fonts: `font-display` Rajdhani (headers/names), `font-sans` Inter
(body), `font-mono` JetBrains (stats/%/cost).

## Shell (App.tsx)
- Desktop: **64px left icon rail**, bg `rail`, right border `line`. Top: `S2`
  logo tile (gold bg, bg0 text, rounded-lg). Then icon buttons Builds / Gods /
  Items (24→~16px stroke icons). Active = gold stroke + `border border-gold`
  tile; inactive = muted stroke on `bg2` tile. Below rail top-align; a help/`?`
  can sit at rail bottom.
- Content header (per view): title (Rajdhani 16px bold) + count (`faint`) + the
  view's search box (right) + freshness `Data from <date>` (mono, faint) + `?`.
- Mobile (<~720px): hide the rail; render a **bottom tab bar** (Builds/Gods/Items),
  active tab gold text + `border-t-2 border-gold`. Header collapses (title + date + ?).
- Scraping banner + dev controls: quiet tier (see Dev).

## Gods tab (GodsIndex) — flagship
- Filter bar: search field (bg2, `line` border, `ti`/svg search glyph, muted
  placeholder; focus → `border-blue`) + role filter **pills**: "All" (active =
  gold bg / bg0 text) then one pill per role in that role's color (inactive =
  transparent + `line` border + role-colored text). Right: "<n> gods" count.
  Sticky under the header on scroll.
- **Pinned shelf**: if any pins, a `PINNED` mono/gold label + a grid of pinned
  GodCards above the main grid.
- Main grid: `grid` `repeat(auto-fill, minmax(150px, 1fr))` gap-2.5 (→ 4–6 cols
  by width; 3 cols on mobile).
- **GodCard**: rounded-xl (`12px`), `bg2` + `border-line`. Column: portrait
  (`rounded-md`, 52px desktop / 44px mobile, object-cover) + name (Rajdhani 600
  ~12.5px) + role word (role color, ~9.5px). Pin button top-right.
  States: hover → `border-line-strong` 180ms (desktop only, no lift); pinned →
  gradient `bg2`→`bg3` + `border-gold/40` + `shadow-glow` + gold filled pin +
  floats into the Pinned shelf; press → `.press`; empty (0 results) → centered
  muted text + "Clear filters" link; loading → skeleton bg2 cards.
- **PinButton**: icon-only toggle top-right, hit target ≥32px. Unpinned = faint
  stroke pin, opacity .6; hover → opacity 1, stroke `ink-soft`; pinned = gold
  fill/stroke. Persist pinned god names in localStorage (`smite.pinnedGods`).
  **Replaces the old remove-X.** Pinned gods sort to the top of the list.
- Pin toggle motion: crossfade icon to gold 180ms; card FLIP-animates into the
  shelf over 280ms (no abrupt reflow) — acceptable to keep simple (reorder +
  transition) if a full FLIP is heavy.

## Build detail (DetailPanel) — priority mobile surface
- God header: head icon (52px rounded-lg, `shadow-card`) + name (Rajdhani 700
  24px) + `pantheon · <role in role color> · <damage in dmg color>`. Right:
  mode toggle (segmented Conquest/Joust, active gold) + Aspect toggle.
- Variant tabs (Core / flavor(s) / Community): segmented pills, active gold.
- Desktop two-column: left = `STARTER` (base→upgrade icons+names) + `BUILD ORDER`
  slot rows; right = `WHY THIS ITEM` card (name + `cost·T#` mono + score bars
  value/win/pick/fit: `bg-line` track, gold fill, mono value) + `SITUATIONAL`
  swap chips (active/relevant = gold bg/bg0; others = bg2 / faint).
- Mobile: single column; slot rows min-height 44px with a chevron; **tap a row
  expands an inline why-this-item disclosure** (score bars) below it — no
  fixed-position popover. Keep the existing live swap-preview diff (added = blue
  text + blue/10 bg; removed = muted + line-through + 30% icon opacity).
- SlotRow: icon 32px + name + optional `flex`/off-meta tag + (community) pick/win%.

## Items shop (ItemsShop) + ItemPickerModal
- Filter bar: search + tier/ratings/tags/stat/sort selects (bg2 fields, `line`
  border). Grid `repeat(auto-fill, minmax(~180px))` (5-ish desktop, 2 mobile).
- **ItemCard**: `bg2` + `border-line` rounded-md. Row: icon 32px + name (ellipsis)
  + `cost·T#` mono (faint). Footer: efficiency badge — undervalued = `under` text
  on `under/13%` chip; premium = `premium` on `premium/13%` chip; fair = muted on
  `bg-line` — plus effect tag (`blue`, right). Hover → `border-line-strong`.

## Dev / owner-only tier
Add/remove god + scraping banner are a deliberately quiet tier: `faint` text, NO
accent color, **dashed `line-strong` border**, small uppercase `DEV` tag
(mono, faint, boxed). Scraping banner: flat 120ms fade-in, no pulse/glow/loop.
Must read as subordinate to every user-facing control. Keep dev-only (import.meta
DEV) gating as today.

## Motion summary
Card hover: border line→line-strong 180ms, no translate (except pinned/rail glow,
instant). Press: scale .97 120ms (all tappables → `.press`). Pin: gold crossfade
180ms + FLIP 280ms. Tab/mode switch: 150–180ms color/bg crossfade, no slide.
Tooltip/why: desktop hover 150ms; mobile tap → inline disclosure. Dev/scraping:
flat fade, no attention motion.

## Constraints
Preserve ALL functionality + tests' public behavior. Tailwind v4 utilities only.
Dark-only. Responsive ~360→desktop. `npm run build` (tsc -b) MUST pass — it type-
checks .test.tsx too. Keep hash routing, localStorage "my builds", dev gating.
