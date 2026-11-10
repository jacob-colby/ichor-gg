---
name: ichor
description: A SMITE 2 build recommender that shows its working — the phone beside the monitor, mid-draft.
colors:
  ground: "#101114"
  surface: "#16171b"
  surface-2: "#1f2026"
  surface-3: "#292a31"
  line: "#33353c"
  line-strong: "#464851"
  ink: "#ebebee"
  ink-soft: "#cfd0d6"
  muted: "#a6a9b2"
  quiet: "#8b8e97"
  thermal-violet: "#a998ff"
  violet-ink: "#14121f"
  positive: "#6fcf9f"
  negative: "#f09a9a"
  aspect-ember: "#ef8034"
  link-blue: "#8fc2ff"
  role-guardian: "#7f9e97"
  role-warrior: "#b98a6d"
  role-mid: "#8fa3c8"
  role-hunter: "#b6a571"
  role-assassin: "#b9879a"
  dmg-physical: "#b98a6d"
  dmg-magical: "#8fa3c8"
typography:
  hero:
    fontFamily: "Sofia Sans Extra Condensed, Sofia Sans, sans-serif"
    fontSize: "64px"
    fontWeight: 800
    lineHeight: 0.88
  god:
    fontFamily: "Sofia Sans Extra Condensed, Sofia Sans, sans-serif"
    fontSize: "46px"
    fontWeight: 800
    lineHeight: 0.9
  head:
    fontFamily: "Sofia Sans Extra Condensed, Sofia Sans, sans-serif"
    fontSize: "30px"
    fontWeight: 800
    lineHeight: 1
  row:
    fontFamily: "Sofia Sans Extra Condensed, Sofia Sans, sans-serif"
    fontSize: "22px"
    fontWeight: 700
    lineHeight: 1
  say:
    fontFamily: "Sofia Sans, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.38
  copy:
    fontFamily: "Sofia Sans, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.5
  note:
    fontFamily: "Sofia Sans, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.4
  cap:
    fontFamily: "Sofia Sans, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.4
rounded:
  sm: "6px"
  md: "10px"
  control: "12px"
  lg: "14px"
  xl: "18px"
spacing:
  gutter-phone: "16px"
  gutter-desktop: "24px"
  row-gap: "6px"
  tap: "44px"
components:
  button-primary:
    backgroundColor: "{colors.thermal-violet}"
    textColor: "{colors.violet-ink}"
    rounded: "{rounded.md}"
    height: "44px"
    padding: "0 20px"
  item-row:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    height: "64px"
    padding: "8px 14px 8px 10px"
  item-row-swapped:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
  command-field-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    height: "44px"
  command-field-page:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    height: "56px"
  chip-you:
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    height: "44px"
  chip-enemy:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    height: "44px"
  segment-active:
    backgroundColor: "{colors.thermal-violet}"
    textColor: "{colors.violet-ink}"
    rounded: "9px"
    height: "44px"
  segment-inactive:
    textColor: "{colors.muted}"
    rounded: "9px"
    height: "44px"
  tab-bar:
    backgroundColor: "{colors.ground}"
    textColor: "{colors.quiet}"
    height: "64px"
---

# Design System: ichor

> **2026-11-03:** the 2026-11 redesign replaced the "Arena Night" world (torchlight gold, Rajdhani / Inter / JetBrains Mono, the god-picker rail, lens tabs, the floating draft dock) with **Thermal Ink** — direction A, "Second Screen", plus direction C's typed query. Everything below describes what is built. The product-truth rules that outlived the old world are kept in their own section and still bind.

## Overview

**Creative North Star: "The Second Screen"**

ichor is the phone propped beside the monitor in a draft lobby. A player has a few seconds between picks, one thumb free, and a single question: what do I buy? So every screen gives one answer — who you are playing, the six items in buy order with the gold spent by each, and one sentence comparing that six to what the god's own players buy — and the reasoning sits one tap below it, never in front of it. On a desktop the same answer grows a real second column instead of stretching.

The look is a broadcast lower-third printed on ink: a flat near-black ground, condensed uppercase names (Sofia Sans Extra Condensed) set like a caster's caption over a humane reading face (Sofia Sans), and exactly one hue that means anything — violet, the model's own voice and the selected state. (The aspect's orange hexagon is the game's own mark, not a second voice: see Aspect Ember.) The enemy side never gets a colour; it is drawn in an ink outline and says "Enemy" in words. The gold a player spends is the only number on the main path; percentages appear only as "N% of Ra players buy this".

What it refuses: the dashboard. No debug decimals (`fit 0.69`), no eyebrow-over-heading stacks, no pill soup, no identical card grids, no second accent. Arena Night's "tactical console" feel is the anti-reference now — this world is a broadcast, not an instrument.

**Key Characteristics:**
- One answer per screen; detail is a disclosure away, never a scroll past.
- Dark only, flat ground, two lifted surfaces and a hairline.
- Violet is selection, the primary action and the model talking — nothing else.
- Condensed uppercase for names, gold and controls; Sofia Sans for anything read as a sentence.
- One authored motion: the lock-in when an enemy pick changes a row.
- A bottom tab bar on a phone; a top bar with the command field and a second column from 1024px.

## Colors

A stepped near-black neutral stack, one violet, and a direction pair. No decorative hue family.

### Primary
- **Thermal Violet** (`#a998ff`): the model's voice and the chosen state. The active segment of the mode switch, the selected god's ring, "you" in the command field, a draft-swapped item row's ring and its reason line, primary buttons ("Go", "Try again", "Choose a god"), the focus ring, the active tab's top rule. 7.8:1 on `ground`.
- **Violet Ink** (`#14121f`): text set on violet (7.6:1). Never white on violet.

### Neutral
- **Ground** (`#101114`): the page. Flat — Thermal Ink is printed, not lit; there is no radial falloff.
- **Surface** (`#16171b`) / **Surface 2** (`#1f2026`) / **Surface 3** (`#292a31`): item rows and fields at rest; hover, the active option, a swapped row; the switch track and fallback art.
- **Line** (`#33353c`) / **Line Strong** (`#464851`): hairlines and dashed empty slots; scrollbars.
- **Ink** (`#ebebee`, 15.9:1) / **Ink Soft** (`#cfd0d6`) / **Muted** (`#a6a9b2`, 8.0:1) / **Quiet** (`#8b8e97`, 5.8:1 on ground, 5.0:1 on surface-2): the text stack. Quiet is the floor.

### Semantic
- **Positive** (`#6fcf9f`) / **Negative** (`#f09a9a`): the direction of a comparison and nothing else — which way the model leans against the market (an item's price, a god's tier). Never success/failure, never an error colour; an error is ink copy with a recovery action.
- **Aspect Ember** (`#ef8034`): the game's own marker for an aspect, and since 2026-11-09 (Jacob) the aspect switch's colour on the new surfaces. It is drawn only as the aspect hexagon (`AspectHex`), always ember: the outline when the aspect is off, filled with its notch when on, at rest and on hover, never grey. It appears on the switch (god page, draft board), the command field's aspect chip, a recent god opened with its aspect on, and the kept routes' portrait badge. The switch's on-state frame is the only other ember: a 45% border over a 12% wash. As a graphical object (WCAG 1.4.11, 3:1) it is 7.0:1 on ground, 6.7:1 on surface, 6.0:1 on surface-2 and 6.0:1 on the on-state wash. The ground-coloured notch is 7.0:1 on the fill. The 45% border is 2.3:1 and is decoration, because the fill is what says "on". Never text, and never anything but the aspect.
- **Link Blue** (`#8fc2ff`): links that leave the app (the item's wiki page, official patch notes) and inline links inside the kept route bodies.

### Role & Damage Accents
- **Guardian** `#7f9e97`, **Warrior** `#b98a6d`, **Mid** `#8fa3c8`, **Hunter** `#b6a571`, **Assassin** `#b9879a`; **Physical** `#b98a6d`, **Magical** `#8fa3c8`. Text tints only (the lane under a god card's name, the role in the god header). Every one clears 5.3:1 on ground. Mid moved off lavender to steel blue so a Mid god can never read as "selected" next to violet.

### Named Rules
**The One Hue Rule.** Violet appears only on the current selection, the primary action, or the model's own voice. If a use of violet is none of those three, it is wrong. The aspect switch is the one selection not drawn in violet. The aspect is the player's own choice and the game marks it in orange, so its on state is Aspect Ember (see Semantic). Violet there would read as the model talking. A measured gap in the verdict sentence is emphasised by **weight**, not violet — the gap is often the community's advantage, and violet would read as the model claiming the win.

**The Ink-Outline Enemy Rule.** The enemy team has no hue. Enemy portraits carry a 1.5px ink ring and the word "Enemy"; they are never red. Red-for-enemy would collide with `negative`, which means "the model rates this below the market".

**The Semantic Color Rule.** Role and damage tints always mean that lane or that damage type; never repurpose them as decoration.

**The Readable-Floor Rule.** Every text tier clears WCAG AA (4.5:1) on every surface it can land on, and **nothing is set below 12px** (`text-cap`). Quiet on surface-2 is the tightest pairing at 5.0:1. A separator glyph (`·`) inherits its parent's tier. Kept route bodies may still use the 11px `text-micro` for a numeral inside a dense grid cell; no new surface may.

## Typography

**Display Font:** Sofia Sans Extra Condensed 700/800 (`font-cond`, always uppercase, +0.005em)
**Body Font:** Sofia Sans 400/500/600 (`font-sans`)
**Numbers:** the same faces with tabular figures (`.num`) wherever figures read down a column.

**Character:** a broadcast caption over a reading face from the same superfamily — the condensed caps carry names at a size a glance can catch, and Sofia Sans keeps every sentence humane. There is no mono face; the old `font-mono` / `font-display` names point at Sofia Sans so the kept route bodies stopped loading Rajdhani, Inter and JetBrains Mono.

### Hierarchy
- **Hero** (cond 800, 64px desktop / 52px phone, 0.88–0.9): "Who are you playing?" only.
- **God** (cond 800, 46px phone / 68px desktop, 0.9): the god's name, the god page's `h1`.
- **Head** (cond 800, 30px, 1): sheet titles, section names, error headings.
- **Row** (cond 700, 22px, 1): item names in the six; 19–21px in suggestions, chips and option rows.
- **Say** (Sofia Sans 400, 17px / 21px desktop, 1.38, ≤46ch / 40ch): the one verdict sentence.
- **Copy** (400, 15px, 1.5): reading text, ≤60ch.
- **Note** (400, 13px, 1.4): an item's reason, secondary lines.
- **Cap** (400–600, 12px, 1.4): captions, provenance, counts, the "Aspect" label. The floor.

### Named Rules
**The Caption Rule.** Condensed caps are for **names and controls** — gods, items, modes, tabs, gold figures, buttons. A sentence is never set in condensed caps; a name is never set in the reading face at row size.

**The No-Eyebrow Rule.** No kicker above a heading. A list is introduced by one quiet cond label that names it (`ICHOR'S SIX · BUY ORDER`), on the same line as its column label (`Gold spent`) — not stacked over a title.

**The Plain-Number Rule.** On the main path a number is gold or a share of a god's players, written with its unit in words: `13,400`, "55% of Ra players buy it first", "Tier B on 1,286 Conquest games". Model scores and decimals live in the disclosures, the Method page and the kept route bodies (the god's own kit, item ranking and ranking pages), always with a label that says what they measure ("weight 0.35 of the score", "18.91g a point"). A gold figure set in the caption face keeps its `g` lower case (`2,500g`, not `2,500G`).

## Layout

**Phone first (390px).** Single column, 16px gutters, content padded clear of a fixed **bottom tab bar** (64px + the home indicator: `pb-tabbar`). The god page reads header (with the mode switch) → verdict sentence → the **focus strip** (aspect switch + focus chips, one sideways-scrolling row) and the line naming what it changed → the starter and relic tiles → the six → disclosures (Most picked first), with the **enemy strip** sticky just above the tab bar the whole way down. God select reads hero → command field → the **recent gods** (one sideways-scrolling row, the god you were last on first) → the 3-up card grid, with the **role filter** fixed above the tab bar in thumb reach.

**Desktop (≥1024px, `useWide`).** A sticky 56px **top bar** inside a 1240px container: wordmark · Gods (reading “Gods · Ra” on a god page) · Draft · **the command field** (flex, 220–440px) · Tiers · Items · Patch notes · Method · freshness stamp · Help. The field, the four reading links and the stamp are the bar's **middle**, one size container: the open field widens to exactly that middle and everything else in it steps aside, so a control is either fully there or fully gone — never half under the field (a fixed 640px open width ended part-way across the links until 2026-11-07). The **freshness stamp** is compact — "OB47 · 1d", the patch and the data's age — whenever the middle has room for it (from 1024px, unless a long "Gods · Morgan Le Fay" leaves none), with the whole sentence ("Updated yesterday · Open Beta 47") as its screen-reader text and tooltip, and in Help, so it is never hover-only. The god page becomes a real **second column**: `minmax(0,1fr) 380px`, gap 48px — the build column capped at 680px, and an aside holding the enemy-team panel, the **Most picked** panel and "Why this build". The aside is not sticky since 2026-11-08: with Most picked in it the column is taller than a laptop screen, and a sticky column that tall hides its own bottom until the page ends. God select puts the role filter beside the hero and grows the grid to 7-up. One layout is rendered, not two hidden by CSS, so each control has one copy in the accessibility tree.

Spacing is airy by intent: about five item rows per phone screen, 6px between rows, 44px minimum for every tap target. Overlays — the suggestion list, sheets — sit above the page and never push layout.

## Elevation & Depth

Flat, tonal, and printed. Depth comes from the surface step (ground → surface → surface-2) and a hairline, not from light. Shadow is reserved for things that genuinely float.

### Shadow Vocabulary
- **Raised** (`inset 0 1px 0 rgba(255,255,255,0.05), 0 10px 28px rgba(0,0,0,0.5)`): the command field's suggestion list, the phone's enemy strip riding over the page.
- **Sheet** (`0 -18px 48px rgba(0,0,0,0.55)`): bottom sheets (More, the enemy picker).
- **Card** (`inset 0 1px 0 rgba(255,255,255,0.04), 0 6px 16px rgba(0,0,0,0.35)`): tooltips and popovers in the kept route bodies.
- **Glow** (`0 0 0 1px rgba(169,152,255,0.45), 0 4px 14px rgba(169,152,255,0.12)`): the selected state where a ring alone is not enough.

### Named Rules
**The Flat-Until-It-Floats Rule.** A resting row, card or field has no shadow. Shadow means "this is above the page" — a list, a sheet, the strip.

## Shapes

Soft, consistent corners stepped by size: 6px on tags and badges, 9–10px on chips, segments and buttons, **12px on controls and item rows** (the default), 14px on panels (the enemy panel, the Most picked panel), 18px on sheet tops. Fully round only for the position badge and switch knobs. Borders are 1px `line` hairlines; an empty enemy slot is a 1.5px dashed `quiet` square; selection is a 2px (or 1.5px on a chip) violet ring, never a coloured left border.

## Components

Components feel **tactile and quiet**: every tappable thing carries `.press` (scale 0.97, 120ms), state changes are unambiguous, and nothing communicates on hover alone.

### Buttons
- **Primary:** violet on violet-ink, 44px high, 10px radius, cond 18px bold uppercase. One per view ("Go", "Try again", "Choose a god").
- **Inline action:** cond 18px violet text with a drawn glyph (never a unicode arrow), sized to a 44px hit area inside the sentence. The god page's "⇄ Show theirs" was one until 2026-11-09; it is now the whose-build switch.
- **Quiet:** 1px line border, muted text, 44px ("Clear enemy team", "Help").

### Segmented control (ModeSwitch, WhoseSwitch, RoleFilter)
- `role="group"` + `aria-pressed` buttons, never `role="tab"`. A surface-filled track (12px radius, 4px inset); the active segment is violet with violet-ink text; inactive is muted, ink on hover. Cond 16–18px uppercase.

### Whose build (WhoseSwitch)
- **Ichor's | Community**, two equal 44px segments in the segmented grammar (`role="group"` "Whose build"), between the verdict and the focus strip: you choose whose six first, and what adjusts it sits under it (Jacob, 2026-11-09). It is offered for every god with a Conquest community record, in every mode, and it is in the link (`whose=community`). Switching mode keeps it; a bare god link opens on Ichor's, as it opens on Conquest.
- **Ichor's** is the page as it was: the focus strip, the line, the six.
- **Community** is the six the head-to-head measured: the Conquest record cleaned of components, statless relics and duplicates (`communityBuild.ts`), with no stand-in when a god has no comparison file. It has nothing to adjust, so the focus chips go and only the aspect switch stays. Under it, one `note` line per fact: what the six is ("What Ra's Conquest players buy most in each slot.") and what the cleaning refilled ("Blinking Abyss → The Crusher"). That six is every player on any aspect, so it is never shown as an aspect's: with the aspect on, one slot (`community-aspect-slot`) owns the whole build area, starter, relic and six, for the per-aspect community build to fill, and until it exists it says so ("There's no community build for Thermotherapy yet."). Its rows carry no adjusted or swapped marks, since the enemy team never moves a record. Off Conquest it is Conquest's six, headed "Conquest's community six", with the most-picked list's asterisks on its rows and the reasons printed under it.
- The starter tile reads the build's own stamp on Ichor's side and the community record's on the community's. The relic is the community's most-taken on both, because no build carries one.

### Focus strip (FocusStrip) — one six, adjusted
- The page shows **one** six — Ichor's six, the `model` build the head-to-head measures — and every other build as an **adjustment** of it. One `role="group"` ("Adjust the build") holds the aspect switch, then the focus chips (cooldown, attack speed, anti-tank, bruiser, burst, mana-stack, then the god's own crit / strength / intelligence / str + int), then, after a hairline, the two other *answers*: **Balanced** (the blend with players' win and pick rates) and **Hybrid** (the model corrected where a player record is strong). An answer chip shows only when it gives a different six — Balanced equals Ichor's six in Joust and Arena by construction. A focus chip always shows; when it changes nothing the line says so ("Same as Ichor's six for Ah Puch", "Same as Balanced for Ra").
- Chips: 44px, 10px radius, cond 17px uppercase, `aria-pressed`; selected is violet with violet-ink text (selection), the rest surface with a hairline ring. Phone: one row that scrolls sideways, bled to the screen edge with a 28px fade on the right, the chosen chip scrolled into view; from 1024px it wraps.
- Choosing one changes the six **in place**. The line under the strip names the change: the chip's name in cond, then "Swaps 2 of 6:" over one swap per line ("Spear of the Magus → Chronos' Pendant"; a screen reader hears "replaced by"), then a `cap` note on where it came from. It reads the same at one swap and at six. With no focus chosen, switching the aspect on gets the same treatment ("Built for Thermotherapy. Swaps 2 of 6:").
- **Phone: one line.** Below 1024px the lead is the summary of a native disclosure ("COOLDOWN Swaps 3 of 6 ›", 44px), and the list and note sit behind it, because the six's own rows already carry every swap ("In for Soul Gem"). Open, the list pushed all six rows under the enemy bar. A lead with nothing behind it ("Same as Ichor's six for Ah Puch.") stays plain text, not a control. From 1024px the list stays open.
- Order in the column: verdict → whose switch → strip → line → the buy order, so the line sits directly over the slots it marks. The verdict still speaks only for Ichor's main six and says so when a focus is chosen. On the community's side it reads the main six's sentence whatever focus Ichor's side was left on, because that measurement is the two of them.

### Aspect switch (AspectToggle)
- `role="switch"` first in the focus strip (and on the draft board): the **aspect hexagon** (`AspectHex`, 24px, pointy-top) and a two-part label — "Aspect" in 12px quiet over the aspect's short name in cond 16px uppercase ("Thermotherapy", "Passionate Storm": "Aspect of" and a leading "the" dropped). The name **wraps at its spaces to two lines, never truncates**. 52px minimum height, 12px radius. Its accessible name is the full aspect name plus "(doesn't change the build)" when that is true, and when switched on the line under the strip says whether the build moved.
- **Off:** the hexagon is an ember outline on a hairline (`line`) frame; on hover the frame goes `quiet` and the name ink, while the hexagon stays ember. **On:** the hexagon fills, keeping a ground-coloured notch in the middle so "on" is a shape and not only more orange. The frame takes a 45% ember border over a 12% ember wash, and the name goes ink. The outline is drawn in both states, so the mark doesn't change size. The fill fades in over 150ms on `--ease-standard`, with no transition under reduced motion.
- **Why orange, not violet** (Jacob, 2026-11-09: "The Aspect icon should always be bright orange, ideally with a hexagon shape … a toggle design that fills in when enabled"): violet is the model's voice, and the aspect is the player's choice and the game's own marker. Until then it was a 32×20 pill track that turned violet when on.

### ItemRow (the six)
- 64px minimum, 12px radius, surface (surface-2 on hover); a 48px item icon with its position in a small round badge; the name in cond 22px; the reason in 13px muted below; gold spent in cond 21px tabular figures at the right. The whole row links to the item.
- **Swapped** (the enemy draft moved it in): surface-2 with a 2px violet ring, the reason in violet semibold ("Swapped in for Spear of the Magus — brings anti-heal"), and the lock-in motion.
- **Adjusted** (the reader's focus or aspect moved it in): surface-2 with a 2px `line-strong` ring and the reason led by what it replaced, in ink-soft semibold ("In for Book of Thoth · 26% of Ra players build it"). Neutral, not violet: it is the reader's own choice playing out, not the model's voice. When both apply the draft's mark wins.
- **Flagged** (a borrowed Conquest six off Conquest): an asterisk after the name, its reason read to a screen reader in place, and printed under the six by the most-picked list's rule.

### Starter and relic tiles (KitTile)
- The starter and the relic open the buy order with the six's own treatment, **the same size as an item row and no bigger**: 64px minimum, surface, a 48px icon, the name in cond 22px, one reason line ("25% of Ra players open this way"; "In Conquest, …" off Conquest). "Start" / "Relic" is a small round badge where a row prints its position, so the buy order reads Start, Relic, 1 … 6 and the name has the whole line. The starter keeps its pairing: the base's icon carries the upgrade's as a 28px inset, and the name reads "Conduit Gem → Archmage's Gem". No gold: the column is the six's running total.
- What else the god's players take, by share ("Others · Pendulum of the Ages 41%"), is one tap away. The whole tile is the summary of a native disclosure, and its right edge, where a row prints gold, reads "+2 ›". A tile whose record has no other picks is plain, not a control. Until 2026-11-09 the list sat open under each tile, which made each tile about twice a row: on a 375×812 phone the two took 268px.
- Side by side from 640px when both exist. They stack on a phone, and also at 1024–1279px, where the aside narrows the column and a half-width starter tile wrapped its name to four lines. The relic tile renders only when the index carries `community_relics`; nothing stands in for it.

### Aspect players' build (AspectCommunity)
- On the **Community** side of the whose-build switch with the aspect on, it owns the whole build area (`community-aspect-slot`): what the aspect's own Conquest players finish games holding, from the per-aspect record. **Community, not Ichor's model**, and the first line says so in those words. Neutral throughout — no violet, because this is not the model talking. On Ichor's side with the aspect on, the line under the strip says "What its players buy is on the Community side."
- The build area's own label names it, with the count where Ichor's side prints `Gold spent`: `THE COMMUNITY'S MANGETSU BUILD` · `57 games · OB45–OB47`. A pooled entry names every patch it reads, and the first line says why it pooled ("pooled: no recent patch alone has 30 games").
- When most of the aspect's players take the god into another role, one ink-soft line says so with the shares, and that Ichor's six above is built for the base role because the model can't move a role for an aspect yet.
- The starter and relic as KitTiles, the starter as a path with its two ends summed ("53% of these games open this way"), then six 64px rows ranked by share of games ("In 86% of these games") with **no position badge and no gold column**: it is not a buy order, and the caption says so.
- An item whose stats moved after the oldest patch read carries "changed OB47*" on its line; the notes under the list give the sentence the record carries ("…20 of the 34 matches that bought it are older") and say that passive changes are not recorded.
- Below the minimum it states the count ("Too few games to show: 28 Conquest games across OB44–OB47, and this needs 30"). Joust and Arena have no per-aspect record, and say that instead of showing Conquest's. Whenever there is no aspect build to show, one more line points at the any-aspect six ("Switch the aspect off to see what all Geb players buy, on any aspect").

### Most picked (MostPicked)
- What the god's own players buy most, from the Conquest record, ranked by each item's share **at its commonest slot** (never summed across slots — the record can't say whether those players overlap): up to ten 44px rows on hairlines — 32px icon, name in cond 19px, "38% buy it fourth" in `cap`, and a tick (with "In this build" for a screen reader) on the items in the six on screen. A `cap` key under it: "✓ In the build on screen · 3 of 9".
- **Every mode.** Joust and Arena show Conquest's list and say so in its first line. An item whose Conquest record doesn't describe it there carries an asterisk, and the notes under the list name the items and give the reason from `_weights.yaml` (`community_transfer` in the index): Joust — rotation items; Arena — stacking items ("Conquest's record is for a finished stack…"), rotation items, and the ward items its shop doesn't sell.
- Desktop: a 14px-radius hairline panel in the aside, under the enemy panel. Phone: a "Most picked" disclosure whose summary already says "3 of Ra's top 9 are in this build".
- A running total shows `—` rather than an approximation when any cost is unknown.

### VerdictLine
- The comparison as one sentence directly under the header, at `say`: the claim in ink with the measured gap in semibold, then the honesty tail in muted ("…Lotus Sickle isn't simulated yet, so the damage gap is partly unmeasured."). While measuring it says so, in quiet, with `aria-busy`. Off Conquest on the community's side it says whose record the borrowed six is ("Arena has no community record of its own, so this is the six Ra's Conquest players buy.").

### EnemyStrip / EnemySheet
- **Strip (phone):** a raised, blurred bar sticky above the tab bar: "ENEMY" + "3 of 5" (and "2 swaps" in violet) beside five 48px slots (three in Joust). Filled slots are portraits with a 1.5px ink ring; empty ones dashed squares with a plus. Every slot opens the sheet on itself.
- **Panel (desktop):** the same slots in the second column's surface panel with names under them, "N of 5 known", a status line, and "Clear enemy team".
- **Sheet:** a real dialog ("Enemy 1 of 5") with the slot row, a search field that takes focus, and a 5-up portrait grid. Picking auto-advances to the next empty slot. Picks write the shared draft (you in ally slot 1) and the page URL's `vs=`.

### GodGrid ("Who are you playing?")
- 2:3 card art in a 3-up (phone) to 7-up (desktop) grid, name in cond 21px over a bottom scrim, lane tint under it. With text in the field, the first card — Enter's target, ranked exactly as the parser ranks a word — carries a violet ring and an "Enter" tag. The empty result says what was searched: "No god matches "zz" in Mid."
- **Recent** (this browser only, `command/recents.ts`): while the field is empty and no role is chosen, a row above the grid of the last 8 gods whose build page was opened, by any route (a card, the field, a pasted link, the draft board), newest first and once each. Each keeps the **mode and aspect state it was last viewed in**, so a switch flipped on the page counts and a newer visit replaces both; the enemies are not kept. A card is the head portrait (40px) and the name in cond 19px on a 56px surface tile with a hairline, no ring, and under the name, in `cap` muted, what a tap gives when it isn't the default: the mode word ("Joust"), and the filled 14px aspect hexagon when it opens with the aspect on ("Aspect" to a screen reader); never "Conquest" or "No aspect". It reopens that god's page in that mode with that aspect state, by the god-page hash helper, so `whose` and `build` stay at their defaults. The first card is the god you were last on, so there is no separate "Back to" card. A quiet Clear sits on the heading's line. Phone: one row that scrolls sideways, bled to the screen edge; from 1024px it wraps, since a mouse has no sideways swipe. It was a row of recent *queries* (your god, three enemy heads, "vs …" and the mode) plus a "Back to Ra" card until 2026-11-09, when Jacob asked for a list of gods that keeps the mode and aspect and drops the enemies.

### CommandField (the typed query)
- **What it reads:** `ra vs hecate ymir joust aspect`. The first god is you; `vs` (or a second god) starts the enemy side; a mode word sets the mode; `aspect` turns yours on and `no aspect` or `aspect off` turns it off. **The last keyword of a kind wins**: a later mode word replaces an earlier one in the text, and so does a later aspect word, so there is one mode chip and one aspect chip at most (`keepLastKeyword`). The aspect words carry their value since 2026-11-09 (Jacob); until then `aspect` toggled, and "Aspect" could stand beside "No aspect". `no aspect` is read as one keyword before any god name, so its "no" is never Nox; "no" alone, or before anything else, still is. A typed `no aspect` is a chip (an outlined hexagon) as a typed `conquest` is, and off stays out of the link as the default. Parsing is pure and total (`command/query.ts`): anything it can't place stays visible as a struck-through chip whose accessible name is the reason ("zz isn't a god or a mode"; "Only 3 enemies fit in Joust").
- **Where it lives:** the desktop top bar on every route (44px, the global search, a `/` hint at rest; open, it widens over the bar's whole middle — see Layout), and the phone's god-select screen (56px, replacing the search box). **Not** on the phone god page — the enemy strip is the enemy UI there; one screen, one control.
- **Chips:** finished words become chips — you with a violet ring on a 15% violet wash, enemies on surface-2 with an ink-ringed portrait, mode/aspect as hairline chips, each with a remove ✕ (CloseGlyph). The aspect chip leads with a 16px aspect hexagon: filled for "Aspect", the outline for "No aspect". Backspace on an empty input pulls the last chip back into text to be fixed.
- **Suggestions:** an ARIA combobox listbox that **overlays** the page (raised shadow, 16px radius) and never pushes layout. God rows show the portrait, role and which side it would land on ("You" in violet, "Enemy" in muted). The aspect row leads with the aspect hexagon, filled when choosing it turns the aspect on ("Aspect of Thermotherapy", inserting `aspect`) and the outline when it turns it off ("Aspect off", inserting `no aspect`, which replaces the "Aspect" chip rather than standing beside it). The next step offers whichever state isn't on; a typed "asp" is the on row; and while the word is only "no", the list offers Nox first, as the parser reads it, then "Aspect off". On the phone grid the first word gets no list — the grid below is the list — and the list appears once a god is committed. Items appear when the text's first word is no god ("rage" → Rage, opens `#/items/Rage`). With the field empty the top bar's list offers the recent gods — the same entries as god select's Recent row, so the site has one meaning of "recent" — each row a portrait, the name over its role and any non-default mode ("Solo · Arena") with the filled hexagon when the aspect is on, and "Recent"; choosing one opens the god there.
- **Submit:** Enter (or Go) takes the top suggestion for the unfinished word and goes: a god alone → `#/god/Ra` (the stored draft is left alone); a god vs a team → `#/god/Ra?vs=Hecate,Ymir&mode=joust`, with the team written into the shared draft first; a team with no god → the draft board. The top bar's field empties after a submit.
- **Keyboard:** `/` (outside a text field) or Ctrl/⌘K focuses it; arrows move the active option; Tab completes; Escape closes and restores.
- **Phone keyboard:** the field scrolls itself to the top of the screen when opened, and the list's height is measured against `visualViewport`, so it ends above the keys rather than under them.

### Navigation
- **Tab bar (phone):** Gods · Draft · More, 64px, drawn glyphs (one 1.75 stroke set) over cond 15px labels; the active tab is ink with a 2px violet rule on top, the rest quiet. **Gods is one tab for picking a god and reading its build**, current on the roster and on every god page. It lands on the roster, whose Recent row starts with the god you were last on: the one-tap return to the last build. It was two tabs, Build and Gods, until 2026-11-03: Jacob read them as the same thing twice, and they were. "More" opens a sheet with Tiers, Items, Patch notes, Method, Help, the freshness stamp and the fan-project line.
- **Top bar (desktop):** the same destinations flat, the command field between them and the reading routes, the active one ink with a 2px violet underline.

### Sheets and dialogs
- Real dialogs only: `role="dialog"`, `aria-modal`, labelled by their heading, focus moved in and returned on close, Escape and a visible close button. Bottom sheets on a phone (grab handle, 18px top radius, sheet shadow), centred panels from 1024px. Never opened unprompted.

### Reading routes (Tiers, Items, Patch notes, Method, Draft)
All five share one header grammar (`PageParts.tsx`): an `h1` that **names** the page in the caption face (god-size, 46px phone / 68px desktop) — never a sentence in caps — then **the claim** at `say`, the page's one answer with its live numbers in semibold ink ("**94 of 94 gods** placed on **67,204** Conquest god-games" — the numbers are live), then a quieter `note`/`copy` line of how-to-read-it, a `cap` provenance line where the data supplies one, and a **seam** (cond 18px muted + chevron, 44px) to the surface it hands off to — on Tiers, Items and Draft that is Method, each asking its own question. Lists are **rows on hairlines**, not cards: a 40px icon or portrait, the name in cond 20px, one `cap` line under it, figures right-aligned in cond tabular. **Text tabs** (cond 19px, ink + a 2px violet rule under the chosen one, `aria-pressed`) choose *what* is shown; the mode keeps its segmented switch.

- **Tiers.** ModeSwitch → subject tabs (Gods · Aspects · Items, each offered only when the slice has rows) → RoleFilter → a "Most played first inside each band" check. Each band is headed by its **letter** at 56px (80px desktop, sticky in a 96px left column) in neutral ink — the letter is the verdict — with its count and sample in `cap`; rows show win % over games, never a score, 3-up from `xl`. Unmeasured entries get their own "Not measured" group with the reason in words. **Joust and Arena render no letters at all**: the claim says the mode has no win data, and the roster follows A to Z, unranked, each linking to its build in that mode.
- **Items.** A ledger. Phone row: name, the verdict word (the pipeline's bucket) in semibold ink, then the arithmetic decomposed in `cap` — `2,400g · worth 2,957g · −557g` — and the community win % over games on the right. Desktop: a column grid (Item · Verdict · Costs · Worth · Gap · Wins) under a `cap` column header, with the filters in a 232px left column. On a phone the filters (Verdict and Tier as check rows with counts, Effect, Stat, Order as 44px selects — every option derived from the data) live in a **Filters** sheet whose footer button says how many items it will show. Opening a row opens the **receipt** in a Sheet (bottom sheet on a phone): the verdict sentence, then base price + each stat (`85 × 13.58g a point`) rounded by largest remainder so the column sums to the worth exactly, a 2px rule, Worth, Costs, the gap; unpriced stats are named, a tier-1 starter says why it is not priced, and a missing community record says "not measured".
- **Patch notes.** One reading column (760px). Each period: its patches as an `h2` (cond 30px), the dates from the ISO parts in `cap`, the hand-checked official link if any, the biggest changes as rows (kind as a `cap` word in ink: Buff, Nerf, Mixed, Added, Removed — never green/red), and "All N changes" in a Disclosure listing every cost and stat old → new. Empty says it is empty and why; a refresh inside one patch says its items "entered Ichor's data" and are not counted as changes.
- **Method.** A reading page: Sofia Sans 17px / 1.6 at 68ch, cond 30px section heads, no eyebrows; the blend as four rows with a 4px neutral proportion bar and "weight 0.35 of the score"; the fitted gold-a-point table with "thin" marked in words; the limits as a hairline-ruled list. From 1024px a sticky section list sits in the right column (buttons that scroll, not `#id` links — the hash is the router's).
- **Draft board.** The claim ("This team moved **1 of 6** items in Ra's six"), then each swap as a sentence on a hairline row with the arriving item's icon ringed violet: "**Divine Ruin** replaces Spear of the Magus · answers healing" (the reason in violet: the model's voice). Then the full-width ModeSwitch and two **team rows** of equal slots (five in one row at 390): *Your team* — you first with a 2px violet ring and your name in violet, four allies in a hairline ring — and *Enemy* in the 1.5px ink ring, each with "N of 5" beside the row name, every slot opening the same picker Sheet the god page uses (`EnemySheet`, `side="ally"` for your team). Under them: "3 still unknown, so this six will keep moving", Copy link and Clear as quiet buttons, the aspect switch, the starter, and the adapted six as ItemRows. The threat table ("Against this team", the desktop's sticky right column) lists every threat as "2 of 5" over the roster, with who and how it is answered ("Answered by Divine Ruin", "Weighed — nothing with crowd-control immunity or peel outscored the six", "No item answers this — Shell of Rebuke does, as a relic"); it prints measured zeros only once an enemy is in.

### Skeletons
- Layout-shaped `surface` bars under the real wordmark, shaped like the route that is coming (the god page or god select), pulsing opacity only.

## Motion

One authored moment, everything else still.

- **The lock-in.** When an enemy pick changes the six, the swapped row slides up 10px out of a clipped edge (`clip-path: inset(0 0 100% 0)` → `inset(0)`) and settles, 320ms `--ease-out-expo` (`cubic-bezier(0.16, 1, 0.3, 1)`); its reason line follows 160ms later, 260ms. Keyed by item name, so it plays when the item *changes*, not on re-render. Like a broadcast lower-third landing.
- **Supporting:** sheets rise 24px over 220ms; `.press` scales to 0.97 over 120ms; colour and border transitions run 150ms on `--ease-standard` (`cubic-bezier(0.2, 0.8, 0.2, 1)`), and so does the aspect hexagon filling in.
- **Reduced motion** means arriving at the final state instantly: the swapped row is simply there, still ringed and still carrying its reason; the aspect hexagon is simply filled.

## Product-truth rules (kept from the previous world)

These bind every surface regardless of look.

**The Linkable-State Rule.** Anything the visitor chose that changes what a surface shows lives in the hash query: the god page's `mode`, `aspect`, `build`, `whose` and `vs`; god select's `q` and `role`; the shop's filters. Defaults stay out of the query, so a bare `#/god/Ra` keeps meaning what it meant (and leaves the stored draft alone). A typed query lands on a URL that reproduces it; picker edits write `vs=` back. Writes are debounced `replaceState`, and a queued write is flushed before the app navigates so it can never land on the next page.

**The Seam Rule.** Every surface names another it hands off to, in the visitor's terms: the god page links to the god's kit, every item ranked and its ranking; the roster's Recent row returns to your last build, and to any god you opened lately, in one tap. A seam carries state where state exists — the shared draft is one draft across the god page, the Draft tab and the command field.

**The Honest-Verdict Rule.** The comparison states a verdict a player can act on, near the build, and says what it could not measure in the same sentence — the tail is half the claim, never a footnote. Joust and Arena have no outcome data: they show "No win data in Joust — model only" and an unranked build, never a tier.

**The Unmeasured-Is-Not-Zero Rule.** "Not measured here" and "measured as nothing" are different facts and never render the same way. An unscored signal is said in words, not printed as a neutral default; an unknown cost leaves the running total as `—`; threats that measured zero are distinguishable from threats never looked for.

**The Second-Track Rule.** The community is a constant second track. Its share is printed on each of Ichor's rows ("35% of Ra players buy it third"), its six is one tap away, and the comparison between them is the verdict, which reads the same on both sides. Amended 2026-11-09 (Jacob): the god page's whose-build switch does show one six *instead of* the other, which this rule used to forbid. What still holds: Ichor's is the default and the side a bare link opens on, and the community's side never borrows the model's marks (no adjusted or swapped rows).

**The Provenance Rule.** Wherever the community is cited, say which community and when: "Player percentages: Conquest games on SmiteBrain, refreshed …". Rendered only when the data supplies it; dates formatted from the ISO string's own parts, never through `Date`.

**The Aspect-Honesty Rule.** 72 gods have an aspect and only 7 have a build behind it. The switch shows for all 72 and states plainly, in its accessible name and in a line under the header, when it will not move the build.

**The Readable-Floor Rule** (see Colors): AA on every surface, 12px floor.

**The Structure Rule.** Every route has a skip link ("Skip to content" → `#main`), one `<main>`, and a real `<h1>` stating what the page is ("Who are you playing?", the god's name). The fan-project line — not affiliated with Hi-Rez — stays reachable from Help and More.

## Do's and Don'ts

### Do:
- **Do** give each screen one answer and put the reasoning one tap below it.
- **Do** spend violet only on selection, the primary action, or the model's voice — per the One Hue Rule.
- **Do** draw the enemy in an ink outline and say "Enemy" in words.
- **Do** set names, gold and controls in Sofia Sans Extra Condensed uppercase, and sentences in Sofia Sans.
- **Do** keep every tap target ≥44px and every text ≥12px at AA contrast.
- **Do** let overlays (suggestions, sheets) sit above the page; never let them push layout.
- **Do** put chosen state in the URL and flush queued writes before navigating.
- **Do** say what wasn't measured in the same sentence as what was.

### Don't:
- **Don't** bring back torchlight gold, Rajdhani, Inter, JetBrains Mono, the god-picker rail, lens tabs, or the floating draft dock.
- **Don't** add a second accent hue, or colour the enemy red. Carve-out (Jacob, 2026-11-09): Aspect Ember is not a second accent. It is the game's own marker for an aspect, drawn only as the aspect hexagon and the aspect switch's on-state frame, and it means "aspect" and nothing else.
- **Don't** print a bare decimal on the main path (`fit 0.69`, `quality 0.584`); write gold or "N% of players".
- **Don't** put an eyebrow over a heading, or a coloured border-left on a row.
- **Don't** add a second command field to a screen that already has one, or a field to the phone god page.
- **Don't** truncate a name a player needs to read (an aspect, a god, an item); wrap it.
- **Don't** shadow a resting surface; shadow means it floats.
- **Don't** rank or tier Joust or Arena.
