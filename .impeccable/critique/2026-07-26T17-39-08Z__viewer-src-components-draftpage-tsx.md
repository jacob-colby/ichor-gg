---
target: Draft board
total_score: 15
max_score: 40
na_heuristics: 
p0_count: 2
p1_count: 2
timestamp: 2026-07-26T17-39-08Z
slug: viewer-src-components-draftpage-tsx
---
Method: dual-agent (A: a11180d41cb3deab4 · B: a2e563be63ce3e920)

## Design Health Score

Surface mode: **Operate**. All ten heuristics apply.

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 2 | The build silently rewrites itself with no announcement, no live region, and no diff. `App.tsx` serves the sidebar+build-rows skeleton to a cold `#/draft` load — a route that has neither. |
| 2 | Match System / Real World | 2 | Raw internal `effect_tag` identifiers leak to the surface (`↑ protection-shred, peel`). SMITE 2 forbids duplicate gods in a draft; this board accepts `Ymir, Ymir, Ymir`. |
| 3 | User Control and Freedom | 1 | `clear()` exists at `draft.ts:160` and **is never referenced in DraftPage** — resetting means ten precise 20px taps. Switching Conquest→Joust silently destroys slots 4–5 of both rows; switching back does not restore them. Escape does not close the picker. |
| 4 | Consistency and Standards | 1 | **Zero headings in the entire document.** The mode control has no `role="group"`/`aria-pressed` — the same control is done correctly 60 lines away in `App.tsx:244`. The picker isn't a dialog; the search isn't a combobox. Two eyebrows are set in Rajdhani where the Mono-Label Rule requires mono. |
| 5 | Error Prevention | 1 | Duplicates accepted from URL and picker; destructive mode switch with no warning; unrecognized god names in a shared link are dropped in silence. |
| 6 | Recognition Rather Than Recall | 2 | "swap in" names half a transaction — the displaced item is never shown, so the base build must be held in memory. Chips never name which enemy triggered them. |
| 7 | Flexibility and Efficiency | 1 | An 87-god picker with no lane filter, no damage-type filter, no arrow keys, no Enter-to-pick, no recents, and no marking of gods already drafted — while `GodSidebar` ships those filters. |
| 8 | Aesthetic and Minimalist Design | 3 | Genuinely restrained and the cleanest craft floor of any surface this session (below). But **56.5% of a 1280 viewport is empty** on arrival, and the content column caps at 768px inside 1376px. |
| 9 | Error Recovery | 1 | "No draft data available for X yet." is a dead end. A no-match search collapses the panel to silence. Dropped URL gods are never mentioned. |
| 10 | Help and Documentation | 1 | One paragraph that disappears the instant slot 1 is filled. Nothing defines "adapted core", "swap in", the chips, or the `↑` tags. |
| **Total** | | **15/40** | **Poor** |

For calibration this session: Home 18/40, god detail 19/40, draft **15/40** — the lowest, on the product's most distinctive capability.

## Design Specificity Verdict

**The mechanism is computed on every keystroke and thrown away on the way to the DOM.** That is the finding.

Two lines, both verified:

- `DraftPage.tsx:276` — `return { adapted, baseCore: new Set(base.core) }`. The un-adapted build is computed in full and then reduced to a membership `Set`, discarding item order and every displaced item. So a row can say **"swap in"** and can never say *swap in for what*.
- `draftBuild.ts:74` — `return { core, reasons, bonuses }`. `bonuses` is the clamped per-item score delta: the number that literally quantifies how far the draft moved each item. A repo-wide grep finds it read **nowhere outside its own test file**.

The product's positioning sentence is "builds re-rank live based on the actual match". A player never sees a build change — they see a list with two blue rows. Every sibling surface was redesigned this session around showing *both sides* of a comparison: the tier list's community ghosts, the ledger's model-vs-community rows, Home's divergence deltas. This surface shows one side of its own comparison and deletes the other.

What survives to the screen is a 10px `faint` line reading `↑ protection-shred, peel, Magical Protection` — raw internal tag identifiers, un-glossed, in the smallest and quietest type the system permits, carrying the single most convincing sentence this product can write.

**The threat model is worse than buried — it overstates its own confidence.** `threats.ts:31` sets `enemyCount: enemies.length`, the number of enemies *entered*, and `threats.ts:50` divides by it. So a draft with **one** enemy locked in yields `1/1 magical` — a 100% share — and a maximal overlay that rewrites three of six core items, with nothing on screen admitting the other four enemies are unknown. Adding information then makes the build *calmer*, which reads as the model flip-flopping. This is the normal case: a player drafts with 2–3 enemies known. PRODUCT.md principle 5 is "be honest about coverage gaps"; here the model is loudest exactly when it knows least. Separately, `DraftPage.tsx:267` filters chips to `n > 0`, so a measured "0 of 5 crit" is deleted rather than stated — the exact failure DESIGN.md's "distinguish an unmeasured signal from a measured zero" rule was written this session to prevent.

**Deterministic scan:** `detect.mjs` returned **0 findings, exit 0** on `DraftPage.tsx`, and 0 on the modals. Verified non-vacuous — Assessment B planted a bait file which returned exit 2 with `gradient-text` and `ai-color-palette`, and confirmed no `.impeccable/config.json` suppression exists. Worth noting the scan covers only the static-source subset of the 59-rule registry; the DOM rules can't run from a file invocation, which is why the browser numbers carry the weight.

**And here the craft floor is genuinely the best of the four surfaces:**
- **Zero contrast failures** in both empty and populated states (48 text elements measured).
- **All border radii on scale** — `6/10/14/full` only. No `rounded-xl`, no bare `rounded`. The two off-scale radii in the document are in shared chrome outside this target.
- **Zero nested-interactive violations, zero `role="tab"`, zero unnamed interactive elements, zero images missing alt.** Slot labels are state-aware and well-formed: `"Add ally 2"` → `"Change ally 2 (Athena)"`.
- Slot buttons are **exactly 56×56** at every breakpoint. **No horizontal overflow** at 375/768/1280/1440.
- **Zero console errors or warnings** across every interaction.

So the defects below are almost entirely compositional, semantic, and factual — not token drift. That is now the third surface in a row where a clean detector sat on top of a 15–19/40 design.

What the browser caught that the detector cannot:
- **No `<h1>`, no headings of any level, zero `<section>` landmarks** — document-wide, in every state. The visible "Draft" title is a `<span>` in the app header.
- **56.5% dead space** at 1280 empty (455px of an 805px pane, and it doesn't scroll); 19.1% populated. Content height is *identical* at 1280 and 1440 — the extra 160px buys nothing.
- **9 remove buttons at 20×20**, each overlapping its own 56×56 slot button by 196px², below the 24×24 AA floor.
- **Non-text contrast**: the empty slots' only boundary is `line-strong` on `bg0` at **1.52:1** (needs 3:1) — mitigated by the `+` glyph at 5.11:1, but the slot outline itself is effectively invisible.
- **The picker has `role: null`, `aria-modal: null`, no heading, no focus trap, 89 tabbables, and Escape does not close it** (dispatched and confirmed).
- **`md:flex-row` doesn't take effect until ~1120px** — at 768 the two columns wrap and stack with ~250px of gutter each side.

## Overall Impression

This surface has the best craft floor and the worst design of the four. Nothing here is sloppy: the tokens are clean, the aria-labels are careful, the threat derivation damps a threat an ally already covers and clamps the *sum* rather than each term so a maximal overlay can't rewrite a build wholesale. Someone thought hard about the model.

And then the screen shows almost none of it. The single most convincing thing this product can do — change a build in front of you because of who you're playing against — happens, and is rendered as two blue rows and an un-glossed tag string.

**The biggest opportunity is a one-line change in the data flow with a page-sized payoff:** keep `base` whole instead of reducing it to a `Set`, and read the `bonuses` that are already computed. That turns "swap in" into *"Divine Ruin +0.07 → replaces Book of Thoth"* — the displacement, the magnitude, and the reason, in the vocabulary the ledger and tier list already established. The evidence is in memory on every render; it is thrown away three lines before the DOM.

## What's Working

1. **The "You" slot.** `DraftPage.tsx:143-154` reserves the caption row on *every* ally slot so the gold-ringed one doesn't sit a line lower than its neighbours — a real alignment bug found and fixed structurally rather than nudged with a margin. The gold ring is also a correct Torchlight use: it marks selection.
2. **Mode and persistence defaults.** Conquest default, localStorage restore, and the documented truncate-don't-clear rule mean a returning player lands on their last draft rather than a blank board. It's the one cognitive-load item that passes, and the one that matters most for repeat use.
3. **The model layer is honest even where the UI isn't.** `threats.ts:57-58` damps a threat an ally covers and raises one nobody answers; `draftBuild.ts:48` clamps the sum. The reasoning is careful and entirely renderable — it just isn't rendered.

## Priority Issues

### [P0] The re-rank shows the after and never the before
**What:** `DraftPage.tsx:276` discards item order and every displaced item; `draftBuild.ts:74`'s `bonuses` is read nowhere in the app.
**Why it matters:** "Builds re-rank live based on the actual draft" is the positioning. A player cannot see what was displaced, by how much, or why — so the claim is structurally unsayable in the current render.
**Fix:** keep `{ adapted, base }` whole and render each changed slot as a displacement row — `Divine Ruin ↑ +0.07 → replaces Book of Thoth` — with the bonus as a gold bar reusing the Data-bars vocabulary. Unchanged rows stay quiet. When nothing changed, say so as content: *"Your draft hasn't moved this build yet — add an enemy."* That sentence alone fixes the flat first-fill.
**Suggested command:** `/impeccable bolder`

### [P0] The model is most confident when it knows least
**What:** `threats.ts:31,50` divide by enemies *entered*, so one enemy gives a 1/1 share and a maximal overlay rewriting three of six items. `DraftPage.tsx:267` deletes measured zeros. Nothing states how complete the draft is.
**Why it matters:** 2–3 known enemies is the normal case. Adding a fourth makes the build calmer, which reads as flip-flopping, and PRODUCT.md's coverage-honesty principle is inverted precisely where it matters.
**Fix:** divide by roster size (5 Conquest / 3 Joust), render all threats including zeros, and state completeness as content: *"3 of 5 enemies known — this build will keep moving."* Name the culprits on each chip: `healers 2/5 · Aphrodite, Hel`.
**Suggested command:** `/impeccable harden`

### [P1] Shared links silently do nothing, and Copy link can copy a draft that isn't on screen
**What:** `draft.ts:115-121` reads the hash only in the `useState` initializer and there is **no `hashchange` listener**. Assessment B reproduced twice: setting the hash to a different draft left the board unchanged — including the wrong mode — and since the sync effect depends on `[syncUrl, state]`, the address bar never self-corrects. `DraftPage.tsx:281` then copies `window.location.href`, so in that desynced state **Copy link copies a draft the screen isn't showing.** Unrecognized names are dropped with no notice (`draft.ts:72-74`).
**Why it matters:** the URL is this surface's only distribution mechanism and its only route in. Both directions fail by producing wrong data rather than an error.
**Fix:** add a `hashchange` listener that re-decodes when the hash differs from encoded state; encode from state in `copyLink` rather than reading the address bar; report dropped names as content.
**Suggested command:** `/impeccable harden`

### [P1] The three patterns DESIGN.md rewrote this session are all violated here
**What:** mode control has no `role="group"`/`aria-label`/`aria-pressed` (`DraftPage.tsx:299-308`) while `App.tsx:244` does it correctly. `GodPickerModal` (`DraftPage.tsx:58-112`) has no `role="dialog"`, no `aria-modal`, no `aria-labelledby`, no focus trap, and Escape doesn't close it. The search has no combobox roles, no live count, and a no-match query collapses the panel to silence.
**Why it matters:** "Segmented controls (not tabs)", "Dialogs", and "Search (combobox)" were all written into DESIGN.md this session; `Legend.tsx` already ships the dialog pattern to copy. This is also the app's single heaviest decision point — 87 undifferentiated options — with the least support.
**Fix:** copy `App.tsx:244`'s group and `Legend.tsx`'s dialog shell; add a no-match row and a polite live count; filter out already-drafted gods; add the lane/damage-type chips `GodSidebar` already ships.
**Suggested command:** `/impeccable audit`

### [P2] Two destructive actions, no undo, one entirely silent
**What:** `draft.ts:29-31` truncates on Conquest→Joust and the round trip is lossy and irreversible — Assessment B measured `[Agni, Athena, Bellona, Artemis, Anhur]` → Joust → Conquest yielding `[Agni, Athena, Bellona, "", ""]`. The remove `×` is 20×20 overlapping its own slot, ten on the board, no confirm. `clear()` exists and is never wired.
**Why it matters:** a player mid-draft has seconds. A mistap that deletes an enemy they just entered, with no undo, costs the whole interaction.
**Fix:** warn before a truncating switch and keep the overflow in state so switching back restores it; take `×` to 24×24 with an inset hit area; wire the existing `clear()` to a single "Clear board" control.
**Suggested command:** `/impeccable harden`

## Persona Red Flags

**Alex (power user)** — Nothing to interrogate. No score, no bonus, no axes, no community track, no gold total — the four things god detail now gives him per row, zero of them here. He can't tell whether Divine Ruin entered at +0.02 or at the +0.12 clamp. He'll conclude the draft page is a toy and stay on the god page, which is exactly backwards.

**Sam (keyboard + screen reader)** — Measured: **no headings, no `<section>` landmarks, no live regions.** He can't tell which mode is selected (no `aria-pressed`). Escape doesn't close the picker and Tab leaks out of it into the page behind (89 tabbables, no trap). A no-match search produces silence. Changing a slot rewrites the entire build with **no announcement at all** — the product's core event is inaudible. The board is 20 tab stops in which every second stop is an unconfirmed destructive Remove at 20×20.

**Kira (Masters, mid-draft, ~25 seconds)** — The flagship feature is behind an unlabelled chevron in the desktop rail; Home never mentions the draft and nothing links to `#/draft` except the nav, so she may not know it exists. If she finds it, three enemies means three trips through an unfiltered 87-god grid with no keyboard entry. She gets back two blue rows and a 10px tag string, with the item she must *not* buy never named. And the model is loudest when her draft is least complete. At 25 seconds she reads two blue names and guesses the rest.

## Minor Observations

- `DraftPage.tsx:392` sets item cost in `text-gold` — not selection, not primary action, not the model's signal. A Torchlight violation that makes the *cost* louder than the *reason* on the same row.
- `DraftPage.tsx:383,390` use `bg-blue/10` + `text-blue` to mark the model's own decision — a second accent hue doing the one job DESIGN.md assigns to gold (or, for a directional signal, to `under`).
- `DraftPage.tsx:298,374` set the `MODE` and `YOUR ADAPTED CORE` eyebrows in Rajdhani while `Allies`/`Enemies` twenty lines away use JetBrains Mono — the Mono-Label Rule broken inconsistently within one screen.
- The core list is score-descending, not buy order, but presents as a build path with no ordinals and no cumulative gold — after the ledger established exactly that vocabulary one route away.
- `App.tsx:147` sets the header count to `""` for draft alone; every other route shows a figure.
- "Copied!" is visual-only, 1.5s, no live region.
- The picker offers all 87 gods regardless of what's already drafted, and `e=Ymir,Ymir,Ymir` decodes without complaint.
- Zero authored motion on the one surface where a build re-ordering itself *is* the moment.

## Questions to Consider

1. If a player can never see the item that got displaced, in what sense have you shown them a re-rank? Would a two-column `model default → your draft` layout — the exact form the tier list adopted for ghosts — be the whole redesign?
2. `bonuses` is computed on every render and displayed nowhere. Why is the number that *is* the mechanism the only number you've decided a player shouldn't see?
3. Home computes "we disagree with the meta on 53 of 69 gods" from live data. Draft's equivalent — "your draft moved 2 of 6 items" — is already computed on every render. Why isn't it the `<h1>`?
4. If one enemy produces `1/1 magical` and rewrites half the build, is the honest design one that withholds swaps until the draft crosses a confidence floor and says so, rather than adapting maximally and hoping nobody checks the denominator?
5. Why is this a separate page at all? Commit `8a6654b` retired the in-page draft bar, and the result is a cul-de-sac with no link in from Home, none from a god page, and none out to anything. If draft-awareness is the positioning, should the god page's build *be* the draft-aware build, with the board as a slide-out?
6. The picker is 87 undifferentiated squares. In a real draft Kira knows the enemy's lane. Why doesn't it open filtered to the slot's likely role, or accept "aph" + Enter?
