# The site, as a player

**2026-08-23 · audit, no changes made · viewer at `npm run dev`, data stamped `2026-08-23 / Open Beta 40`**

Driven, not read. Every claim below comes from the running app at 1280×900 and
375×812, with DOM/CSSOM measurements taken in-page. Where I quote a number from
`viewer/public/index.json` I say so.

**On screenshots.** The deliverable asked for them and I could not produce any:
the browser pane never composited in this session, so `computer{screenshot}`
timed out on every attempt. This is the same limitation the 2026-07-26 critiques
hit ("the browser pane is not composited in this session"), so it looks
environmental rather than incidental. Everything visual below is therefore
evidenced by measurement — computed colours, contrast ratios, bounding boxes,
rendered `innerText`, `aria-*` state — which for the contrast and overflow
claims is stronger evidence than a picture. Two claims I would normally have
screenshotted are marked **[unshot]** and stated conservatively.

---

## The central question

> Does a player who has never seen this model get that ichor shows its working —
> or do they get numbers they have to take on faith?

**They get numbers on faith, and the working is one unlinked click away.**

The working exists. It is excellent. `#/method` gives the exact blend weights
(0.35 / 0.45 / 0.05 / 0.15), the fitted gold-per-point table with a support
column, the 1084g base-price explanation, the definition of "underrated", and a
LIMITS section that names the passive blind spot outright. The items shop gives,
per item, a full stat-by-stat gold receipt.

The problem is placement. Measured across `#/`, `#/god/Ra`, `#/items`,
`#/draft`, `#/tiers`:

```
methodLinkInBody: []   anyMethodMention: false     ← all five surfaces
```

**Not one surface on the site links to, or even mentions, the Method page.** It
is reachable only from the nav rail, last of six, behind a word a confused
player has no reason to click. DESIGN.md's own Seam Rule names this exact
failure — *"A destination reachable only from the nav rail is a destination most
visitors never form an intent to reach — the draft board sat unlinked for a
year."* The draft board got fixed. The page that explains the entire product did
not.

---

# WHAT I FOUND

Ranked by player impact. **[confusing]** = the player can't follow it.
**[wrong]** = the site says something untrue or contradicts itself.

---

## F1 — The four numbers that carry the product are defined only in hover tooltips  [confusing]

Every build row prints `value 0.55  win 0.55  pick 0.00  fit 0.69`. A new player
has no anchor: no scale, no direction, no idea whether 0.69 is good.

There are exactly two places in the app that define them:

1. `title=` attributes on the labels inside the expanded panel — and nowhere else:

```
title="Gold efficiency — stats returned per gold spent"          → value
title="Community win rate with this item on this god"            → win
title="How often this god's players buy it, among matches…"      → pick
title="How well the item's stats match this god's kit"           → fit
```

2. The Method page, which nothing links to (above).

`title` requires hover. **On any touch device the definitions do not exist** —
`title` never fires, and the collapsed row that carries the same four numbers is
`aria-hidden="true"` with no title at all. The prompt's own framing is the test:
*a draft happens on whatever screen is to hand.* At 375px I confirmed all four
signals still render on the row, with no route to their meaning.

The panel that should close this gap does not. `WHY THIS ITEM` for Chronos'
Pendant on Ra contains **zero links and zero buttons** (measured), and reads:

> Chronos' Pendant · 2400g · T3 · Intelligence 55 · Cooldown Rate 25 ·
> *Every 10s: -1s Ability Cooldowns.* · **FAIR** · ability-uptime ·
> **WHY THIS ITEM** 0.54 · value 0.55 · win 0.55 · pick 0.00 · fit 0.69 ·
> *"Four signals, weighted into one score. Higher is better on every axis."*
> *"The community build doesn't include this item."*

It repeats the four numbers already on the row, adds one generic sentence, and
gives the verdict word **FAIR** with no arithmetic. Two routes away, the same
item shows:

| Stat | Amount | Gold each | Value |
|---|---|---|---|
| Base price | every item | — | 1084g |
| Intelligence | 55 | 13.65g | 751g |
| Cooldown Rate | 25 | 26.51g | 663g |
| **Fair price** | | | **2498g** |
| **Actual price** | | | **2400g** |
| **Priced under its stats** | | | **−98g** |

That table *is* PRODUCT.md's headline promise — "what every item costs against
what its stats are worth". It is absent from the surface where the build lives,
and the panel offers no way to reach it. Note the inconsistency: the *community*
build rows on the same page **are** links to that dialog; the model's own six
core rows are buttons that expand into a dead end.

**Player impact:** the highest on the site. This is the difference between
ichor's pitch and every other build site's six icons.

---

## F2 — "We didn't measure this" renders as a number  [wrong]

PRODUCT.md Principle 3: *"'We didn't measure this' and 'this is bad' are
different facts and must never be rendered the same way."*

The tier list honours this beautifully (see WHAT WORKS). The Conquest god page
breaks it.

From `index.json`, across the 89 Conquest `core` builds:

```
core rows: 534      rows with pick == 0.00: 228   (42.7%)
```

For those 228 rows the god page prints `pick 0.00` — a measured-looking zero. It
means *no community pick data for this item on this god*, which is a different
fact from *players had the option and declined it*. The items shop renders the
same absence honestly, as the string `no community data`. The Joust god page
renders it honestly too, as `win/pick not measured here`. The Conquest god page
renders it as a number.

Worse for `win`. STATE.md §5 records that `unknown_win_per_god` imputes the
god's own median when an item has no win record. That imputation is displayed
identically to a measurement. On Medusa's default Conquest build every one of
the six rows reads `win 0.56` — the same value six times, because all six are
imputed — beside `pick 0.00`:

```
15,500g core · shares 0 of 6 with the community
Lernaean Bow      0.50   value 0.52  win 0.56  pick 0.00  fit 0.49   meta doesn't buy this
Jotunn's Revenge  0.56   value 0.72  win 0.56  pick 0.00  fit 0.39   meta doesn't buy this
Nimble Ring       0.53   value 0.65  win 0.56  pick 0.00  fit 0.37   meta doesn't buy this
Death Metal       0.53   value 0.61  win 0.56  pick 0.00  fit 0.43   meta doesn't buy this
Rod of Tahuti     0.58   value 0.86  win 0.56  pick 0.00  fit …      meta doesn't buy this
```

A skeptical player reads that as "the model has win-rate evidence for six items
and it's uniformly 56%." The truth is "there is no win-rate evidence for any of
these six." Those are opposite statements. And because `win` carries the largest
weight in the blend (0.45), the imputed constant is doing half the scoring work
on this build while looking like data.

**Player impact:** very high, and it is the one finding that damages ichor
*specifically* — honesty about coverage is the differentiator, and this is the
main surface.

---

## F3 — "How this works" teaches the positioning that was retired on evidence  [wrong]

The `?` dialog — the single most likely destination for a confused new player —
opens with:

> **"Home ranks every lane by how far our model and the community's meta
> disagree. Pick a god anywhere to see its builds."**

Home actually says, in its own `<h1>` and standfirst:

> "7 gods win more than anyone plays them." …
> "Gods are ranked on their own win rates in top-ranked Conquest play,
> **never on anything this site models**."

These are direct contradictions, and PRODUCT.md is unambiguous about which one
is correct: *"The positioning changed on 2026-08-05 and the old version must not
come back… That claim rested on a god ranking which measured −0.117 against real
god strength."* The Legend is still shipping it.

Three more stale strings in the same dialog:

- "**Suggested** tabs are our scoring engine's picks" — the UI's chips are
  `Model / Community / Balanced / …`. There is no "Suggested" tab.
- "**BUILD ORDER** is a recommended buy order" — the heading reads `BUY ORDER`.
- "the Aspect toggle swaps to that god's aspect build" — true for 7 gods of 72
  (see F6).

**Player impact:** high. A new player's first act when lost is to press `?`, and
it hands them a retired claim, two labels that don't exist, and one that's false
for 90% of gods.

---

## F4 — The default build is labelled "Model" and shows the community's numbers  [wrong]

`Model` is `aria-pressed="true"` on arrival for every god. Its rationale string,
on all 89 Conquest gods, is self-contradictory in a single sentence:

> "The model's own answer — **no meta signal** (efficiency + fit **+ win/pick**)."

`win` and `pick` *are* the meta signals. The Joust and Arena versions of the same
string are correct — "no meta signal (efficiency + fit)" — so the Conquest
variant appends the two signals to a phrase that denies them.

It is not only the copy. The Method page states:

> "The Model build is the score with the community switched off — efficiency and
> fit renormalized to 0.70 / 0.30."

Tested against the shipped `slot_scores` for the `model` archetype, all 534
Conquest rows:

```
mean |total − (0.70·eff + 0.30·fit)|            = 0.0532
mean |total − (0.35·eff + 0.45·win + 0.05·pick + 0.15·fit)| = 0.0027
```

The displayed totals are the **blended** score, not the model-only score. So a
skeptical player who takes the Method page at its word — and it invites exactly
that, by publishing the weights — will do the arithmetic on the "Model" build
and find it doesn't reconcile.

*Scoped honestly:* this says what is **displayed** is blended. Whether item
**selection** for that archetype uses the model-only score is a pipeline
question I did not audit. Either way the page is telling the player something
that doesn't check out.

**Player impact:** high for user type 2, who is the one most likely to try the
arithmetic — and the one who bounces hardest when it fails.

---

## F5 — The same URL renders two different builds  [wrong]

Reproduced:

1. `#/god/Ra?m=joust` → Joust. Fine.
2. Navigate to `#/god/Medusa`. Hash is exactly `#/god/Medusa`, no query.
   `aria-pressed` → `Joust: true`. Renders the Joust build (15,300g, 6 items).
3. Reload that identical URL → `Conquest: true`, a completely different build
   (15,500g, different six items).

Mode is held in component state, is not written to the hash, and is not in
`localStorage` (checked: only `smite:draft` and `smite:pinnedGods`). So the mode
leaks across god navigation invisibly, and DESIGN.md's Linkable-State Rule is
broken in the way that matters most — **send someone `#/god/Medusa` and they see
a different build than you do.**

Second-order and worse: a player who looked at one god in Joust now sees *every*
subsequent god in Joust, with no URL evidence. They are reading builds with no
outcome data behind them. The per-row `win/pick not measured here` disclosure
(F-WORKS-2) is what rescues them — which is a good argument for that disclosure,
not for this bug.

---

## F6 — 65 of 72 aspects change the kit text and silently leave the build alone  [wrong]

PRODUCT.md: *"The aspect control shows for all 72 … and **states plainly when it
will not move the build**."*

It does not. On Achilles (Aspect of Prowess), toggling the control on:

```
aspectOn : [Jotunn's Revenge, Kinetic Cuirass, Shield Splitter,
            Eye of the Storm, Runeforged Hammer, Amanita Charm]
aspectOff: [Jotunn's Revenge, Kinetic Cuirass, Shield Splitter,
            Eye of the Storm, Runeforged Hammer, Amanita Charm]
identical: true
```

Header identical too (`14,600g core · shares 1 of 6 with the community`). I
searched the full rendered page for ten phrasings of the disclosure — *won't
move / will not move / same build / unchanged / not tuned / doesn't change /
kit only / does not affect* — and got **zero hits**.

Only 7 gods have an overlay in `_weights.yaml` (Cernunnos, Hercules, Ra,
Chronos, Morgan Le Fay, Agni, Chiron); 72 have an aspect. So for **65 gods** the
control presents itself as a build control, produces a visible change (the kit
prose), and does nothing to the six items — while the product doc believes it
says so. Ra, one of the 7, *does* move (16,300g → 15,750g, shares 4→3), which
makes the silent case more misleading, not less: the control demonstrably works
sometimes.

---

## F7 — "Underrated for this god" names a median of 25 items  [confusing]

Every Conquest god page ends with a run-on sentence. Ra's names 23 items. Across
all 96 Conquest groups (`index.json`):

```
min 22 · median 25 · mean 27.7 · max 40   (Chaac: 40)
```

Against a pool of 226. No scores, no ordering shown, no cut-off explained, and
it includes items already sitting in the six-item core directly above it (Ra's
list opens with Spear of the Magus and Chronos' Pendant, both in his core). It
also names items that read as errors to anyone who knows the game — Breastplate
of Valor, a protection item, "underrated for" Ra.

By the Method page's definition (top 30% on efficiency+fit, pick ≤ 15%) it is
all legitimate. But that definition is on the page nothing links to, and a
25-item undifferentiated list is not a recommendation — it's a category with no
scarcity, rendered as prose. Given the word "underrated" is a claim, this is the
place the site most looks like it is asserting things it hasn't earned.

*Checked against the prompt's concern:* these lists are **not** stale w.r.t.
`offmap_efficiency`. They recompute from current data — Berserker's Shield now
appears in Carry "underrated" lists precisely because it left the cores. The
copy is current; the format is the problem.

---

## F8 — Scores silently change scale between modes  [confusing]

Same god, same item, same session:

| | Conquest | Joust |
|---|---|---|
| Chronos' Pendant | 0.54 | **0.62** |
| Spear of Desolation | 0.62 | **0.79** |
| Soul Gem | 0.61 | **0.76** |

Nothing on the page says the denominator changed. Joust drops `win`/`pick` and
renormalises over efficiency+fit, so everything inflates ~0.1–0.17. A player
switching modes reasonably concludes the build is *better* in Joust. It isn't —
it's measured against less.

The mode disclosure block explains that win/pick are missing. It does not
explain that the remaining number is therefore on a different scale.

---

## F9 — Patch notes cannot populate, and the copy implies it will  [wrong]

`#/patch` renders:

> "Nothing has changed yet. Patch history is a diff between two data refreshes,
> so it starts empty and fills in from the first snapshot onward — this isn't a
> loading state."

Honest-sounding, and the last clause is a genuinely good touch. But:

```
data/Analysis/snapshots/   →  2026-08-01.json      (1 file)
index.json patch_notes     →  []
index.json data_updated    →  2026-08-23
```

`build_index.py:319` builds the page from `snapshots.report_from_dir(...)`. A
diff needs two snapshots. One has been written, 22 days ago, across a period
with daily `chore(data)` refreshes in the log. The feature is structurally dead,
not merely young — and the copy ("fills in from the first snapshot onward")
tells the player to wait for something that is not coming.

The player cost is concrete and it is exactly the prompt's scenario: on
2026-08-22 `offmap_efficiency` shipped and **Berserker's Shield left 17 of 18
Carry cores**. A returning Carry player whose build silently changed had one
surface that existed to tell them, and it said "Nothing has changed yet."

---

## F10 — The draft names a threat and then ignores it without saying so  [confusing, minor]

`#/draft?m=conquest&me=Ra&e=Aphrodite,Ares,Ymir,Cabrakan`:

- `WHAT YOU'RE UP AGAINST` → `1/5 healing · Aphrodite`
- `WHAT CHANGED` → Dreamer's Idol (cc-immunity), Totem of Death (percent-health)
- No anti-heal, and no mention of why not.

The model is behaving correctly — with `5/5 healing` it pulls Divine Ruin in as
the *first* buy at `+0.29 · answers anti-heal`, so the threshold works. The gap
is that the threat panel raises a flag the build silently drops. The player
can't tell "considered and judged not worth a slot" from "not considered". Given
that this surface is otherwise the best on the site at naming its reasoning,
that silence stands out.

---

## F11 — Small, real, and cheap

- **Aspect toggle is a 20×20 tap target** at 375px — under the 24px floor of
  WCAG 2.2 SC 2.5.8. It was the only genuine offender; the one other sub-24px
  hit was the 1×1 skip link, which is correct.
- **No-results copy doubles back on itself**: *"No item matches those filters
  with the filters you have on."*
- **Unknown god names vanish from a pasted draft URL with no notice.** I passed
  `…&e=Aphrodite,Ares,Ymir,Cabrakan,Hel`; `Hel` (not on the SMITE 2 roster) was
  dropped and the hash rewritten. Validation is right; the silence is the same
  sub-point the 2026-07-26 DraftPage critique raised and it remains unfixed.
- **[unshot] A god-picker modal survived a hash change** when I set
  `location.hash` directly while it was open. Clicking a nav link closes it
  correctly, so I could not construct a realistic user path. Low confidence,
  low impact — noting it only so it isn't rediscovered as new.

---

# WHAT WORKS

Four things worth protecting. The first two are, to my reading, better than
anything else in this product category.

### 1. The item dialog is the entire pitch, delivered

`#/items` → any item. The gold receipt (F1) is the thesis made concrete, and the
page around it opens with a claim rather than a title — *"81 of 188 items cost
less than their stats are worth. A regression prices every stat in gold, then
compares what an item should cost to what it does. Open one to see the
arithmetic."* Plain language, states the mechanism, and offers the proof.

And it closes with the sentence that answers the prompt's blind-spot question:

> **"Stats only. A passive can be worth paying over the odds for — that
> judgement is yours, and this is the number to make it against."**

That is the 90%-of-the-pool passive gap, disclosed at the exact point of the
claim, in the player's terms, framed as a handoff rather than an apology. **Yes,
the site says it.** It just says it in only this one place — the god page, where
a player compares our build to their own, does not.

### 2. Joust and Arena honesty — the best expression of Principle 3 anywhere

`#/tiers?mode=joust` makes the disclosure the *headline*, not a footnote:

> **"No outcome data for this mode."**
> "SmiteBrain publishes no Joust results, so there is nothing to rank these on.
> This page used to fill the gap with the site's own score; that score measured
> −0.12 against real god strength, so an empty page is the more honest one.
> Builds for this mode still work — open any god."

and the band itself is named `NOT MEASURED`, with:

> "Shown rather than dropped, and never ranked low for it — **'unmeasured' and
> 'bad' are different facts**."

**Does a player register it, or scroll past it as boilerplate?** They register
it, for three structural reasons: it is the page's one-and-only claim, so there
is nothing above it to scroll past; it publishes a negative result about ichor's
own retired feature, which reads as candour rather than legalese; and on the
build side it is not a block at all but a **per-row** annotation — every single
item row carries `win/pick not measured here`. A caveat repeated on the object
it qualifies cannot be scrolled past. This is the opposite of boilerplate.

**This also directly closes an open item in STATE.md §5**, which still reads
*"The tier list now admits this; the builds do not, and the builds are the
product."* The builds now do. §5 is out of date on that point.

### 3. The draft page

Best-composed surface on the site. It names its own claim with a live number
("Your draft moved 2 of 6 items"), states its coverage ("Scored against 4 of 5
enemies · this build will keep moving"), renders **measured zeros** rather than
hiding them (`0/5 physical —`), names the culprit gods on every threat chip, and
gives every swap a displacement, a magnitude and a reason:

> `Divine Ruin` in place of `Chronos' Pendant` · **+0.29** · answers anti-heal
> `Dreamer's Idol` in place of `The World Stone` · **+0.11** · answers cc-immunity, Penetration

Plus the relic row, which is PRODUCT.md's four-unrecommendable-relics problem
turned into player-facing help: *"takes one of your six · **the model can't price
it, so it won't pick it for you**"* → Shell of Rebuke, *"walks your team out of
their walls"* — surfaced only when the enemy comp actually has walls. That is a
known model limitation converted into a recommendation. It is the best single
idea in the app.

The empty state is a numbered three-step guide, and it is genuinely good.

### 4. The craft floor is real, and it holds under measurement

- **Contrast: zero AA failures.** I computed rendered foreground against the
  nearest opaque ancestor background for every text-bearing element on `#/`,
  `#/items`, `#/tiers`, `#/draft`, `#/method`, `#/patch` at 375px, against a
  4.5:1 floor (3.0:1 for large text). **0 failures on all six.** The
  Readable-Floor Rule is not aspirational; it is enforced in the shipped CSS.
- **Zero horizontal overflow** at 375px on the god page and home
  (`scrollWidth === clientWidth`, 0 offending elements).
- **Dialogs are real dialogs**: `role="dialog"`, `aria-modal="true"`,
  `aria-labelledby`, focus moved to the heading on open.
- **`aria-label`s resolve ambiguity the visual can't.** The buy-order row's gold
  column is cumulative, which is genuinely ambiguous on sight — and the label
  says `"Chronos' Pendant, purchase 1, **at 2,400g spent**, model score 0.54,
  community does not buy it"`. Someone thought about this.
- **Dev affordances are correctly gated** behind `isDev`, dashed-bordered and
  labelled `DEV`.

---

# WHAT GOT FIXED SINCE 2026-07-26 (and what did not)

Against the four critiques in `.impeccable/critique/`.

| Critique | Status |
|---|---|
| **Home** P0 · disagreement rendered as illegible grey; promote model↔meta delta to headline | **Superseded — deliberately.** The 2026-08-05 positioning change retired that claim on evidence. Home now leads on real win rates. *This critique should not be actioned; doing so would restore what PRODUCT.md says must not come back.* |
| **Home** P0 · blocking Legend modal auto-opens on first load, describes a different page | **Fixed.** No auto-open on cold load; behind `?`; correct dialog semantics. *But its content is now stale — see F3.* |
| **Home** P1 · no `<h1>`/`<main>`/skip link/focus ring; 14→9.5px type range | **Fixed.** One `<h1>` per surface carrying a live claim, `<main>`, skip link present. Formalised as the One-Claim Rule. |
| **Home** P1 · 32–48% empty, doesn't scroll | **Fixed.** Home is full and authored for the empty-patch case. |
| **DetailPanel** P0 · every god opens on the community build | **Fixed.** `Model` is `aria-pressed="true"` by default. |
| **DetailPanel** P0 · surface never states the model's verdict on this god | **Fixed.** Subject header carries `tier A · wins 55% · over 1.5k matches · picked in 10%`, plus a `Ranking` lens and a `Draft with Ra →` seam. |
| **DetailPanel** P0 · decomposition hover-only, drops the composite, 414px shove | **Fixed.** Click-to-expand, in-flow, and `total` is now the panel headline. |
| **DetailPanel** P0 sub-point · *"name the scale somewhere — `value/win/pick/fit` are explained nowhere in the app"* | **Half-fixed, and this is F1.** Now explained on Method and in `title` tooltips. Still unexplained on touch, and Method is unlinked. |
| **DetailPanel** P1 · broken tab ARIA, unguarded modals | **Fixed.** |
| **DraftPage** P0 · re-rank shows the after and never the before | **Fixed, exactly as prescribed** — displacement + magnitude + reason. |
| **DraftPage** P0 · model loudest when it knows least; measured zeros deleted | **Fixed, exactly as prescribed** — divides by roster size, states completeness, renders zeros, names culprits. |
| **DraftPage** P1 · shared links do nothing (no `hashchange` listener) | **Fixed** for the board. **Not fixed:** dropped names still silent (F11). |
| **ItemsShop** P0 · efficiency model is a label with the math amputated | **Fixed, into the pipeline.** `worth 2498g · −98g` on cards; full gold receipt in the dialog. The single biggest improvement in this ledger. |
| **ItemsShop** P0 · clicking an item does nothing visible | **Fixed.** Real dialog with ✕. |
| **ItemsShop** P1 · three coverage gaps, all silent | **Fixed.** `217 of 226 have community data`, `35 not priced (starters and statless items)`, `no community data` as content. |
| **ItemsShop** P1 · no no-results state; `Glyph` filter matches zero items | **Fixed.** `Glyph` gone, `Relic` added, no-results block with `Clear filters` (copy nit in F11). |

Net: the 2026-07-26 round was acted on thoroughly. Almost every P0 is closed.
The one that isn't — *"the scale is explained nowhere"* — is the one that
survived into F1, because it was answered by building a new page rather than by
labelling the numbers in place.

---

# Journeys, in brief

**1 · New player, cold, wants a build for one god.**
One click from home to a build (god cards on home link straight to `#/god/<n>`);
the picker has search + lane filters + bookmarks. **Speed is not the problem.**
Comprehension is. Unexplained on arrival, in order of appearance: `T3`, `FLEX`,
`OFF-META`, `value`, `win`, `pick`, `fit`, `FAIR`, `ability-uptime`, `Model` vs
`Community` vs `Balanced`, `Mana-Stack`, `core`, `underrated`, and a gold column
that is cumulative spend rather than item price. Of those, `title` tooltips cover
four — on desktop only. Can they say *why* these six items? No. They can say the
site is confident about them.

**2 · Experienced, skeptical.**
Well served, and this is the strongest journey after the draft. The disagreement
is findable in one glance — `shares 4 of 6 with the community`, per-row
`meta buys 1st · 52% pick · model buys 2nd`, `OFF-META` badges, and a
`What the community buys instead` block. They can interrogate it via Method,
*if they find it*. Two things make them bounce: F4 (the arithmetic on the
"Model" build doesn't reconcile with the published weights) and F2 (`win 0.56`
six times on a build with no win data). Both are failures of the exact rigour
this user came for.

**3 · Drafting, in a hurry, heavy CC + a healer.**
Fast enough and it says what changed. Cost is ~2 clicks per god (slot → picker,
with search) — 12 for a full board, though the value arrives from the first
enemy. With a real heal-heavy comp it pulled Divine Ruin to first buy at
`+0.29 · answers anti-heal`. Best surface on the site. One gap: F10.

**4 · Joust / Arena.**
The disclosure lands, and lands per-row. See WHAT WORKS §2. The one thing that
undercuts it is F5 — a player can end up in Joust without the URL saying so.

---

# WHAT I COULD NOT ASSESS, AND WHY

- **Anything purely visual.** The browser pane never composited
  (`screenshot failed: … the page is not compositing frames`), so no screenshots
  and no visual overlays. Composition, rhythm, icon rendering, glow/selection
  states, the Ground Plane Rule's 1px inset highlight, and z-order collisions
  that don't change box geometry are **unassessed**. My contrast, overflow,
  tap-target and hierarchy claims are measurements and stand on their own; my
  aesthetic claims are deliberately absent rather than guessed.
- **"Both themes" — there is no second theme.** No toggle exists, `data-theme`
  is unset, `color-scheme: dark`, `body` is `rgb(7,9,16)`. Dark-only is
  DESIGN.md's "Arena Night" position, so this is by design, not a gap. I did not
  test rendering under a forced `prefers-color-scheme: light`.
- **Real touch behaviour.** 375px was emulated. My claim that `title` tooltips
  are unreachable on touch is from the platform behaviour of `title`, not from a
  device.
- **Keyboard focus rings.** I could not deliver real Tab focus, so I did not
  verify the focus ring visually — the same limitation the 2026-07-26 round hit.
- **Whether the `model` archetype's item *selection* uses the model-only score.**
  F4 establishes only that the **displayed** totals are the blended score. The
  selection path is pipeline-side and out of scope here.
- **Whether F9's dead snapshot store is a cron/ops gap or intended.** I
  established that one snapshot exists, that a diff needs two, and that
  `patch_notes` is `[]`. I did not chase why the daily refresh isn't writing one.
- **Cross-browser.** One engine, one session.

---

# WHAT I DID NOT DO

- **Changed nothing.** No component, CSS, pipeline, weight, data or doc edit.
  This file is the only addition, on branch `audit/site-as-a-player`, unmerged.
- **Did not run the pipeline, `calibrate`, or `calibrate --control`.** No model
  change was proposed, so the CLAUDE.md control-re-measurement command has
  nothing to guard here. No number in this report is a model-quality claim.
- **Did not re-derive prior design work.** The 2026-07-26 critiques were read and
  reconciled, not repeated.
- **Did not act on DESIGN.md's named rules.** The Torchlight, Readable-Floor,
  Measurement and Subject Rules bind. I found no reason to dispute any of them —
  the Readable-Floor Rule in particular measures as fully upheld. F1 and F9 are
  Seam Rule and One-Claim consequences, reported as findings against the rules,
  not arguments against them.
- **Did not scope fixes.** F1's placement, F2's rendering and F4's labelling each
  have several plausible resolutions with different costs, and choosing between
  them is a design decision, not an audit finding.
