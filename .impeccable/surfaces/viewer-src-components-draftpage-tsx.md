---
version: 1
slug: "viewer-src-components-draftpage-tsx"
primary_target: "viewer/src/components/DraftPage.tsx"
related_targets: ["viewer/src/lib/draftBuild.ts","viewer/src/lib/threats.ts"]
---

# Draft board

**Scope:** `viewer/src/components/DraftPage.tsx`, with logic in `viewer/src/lib/draft.ts` (state + URL/localStorage), `viewer/src/lib/threats.ts` (threat model + culprits), `viewer/src/lib/draftBuild.ts` (`adaptedCore`, `diffCore`).

**Visitor mode:** Operate, under time pressure. A player is mid-draft with seconds to act.

**Audience & job:** Someone who knows 2–3 enemies and wants one actionable sentence: what should I buy differently, and why. Per PRODUCT.md this is the product's only capability no competitor has.

**Action:** Fill the gold slot, add enemies as they lock in, read the displacement list, share the link.

**Content / proof:** All computed live. `diffCore` pairs each arrival with what it displaced; the magnitude is `adaptedCore`'s own clamped `bonus`. Live example — Ra vs Aphrodite/Cupid/Athena/Ares/Ymir: *"Divine Ruin replaces Rod of Tahuti +0.12, answers anti-heal"* and *"Screeching Gargoyle replaces Spear of the Magus +0.12, answers protection-shred, peel, Magical Protection."*

**Constraints:**
- **No timing or ordering data** — the adapted core is score-descending, not a buy order. Don't present it as a purchase sequence.
- Threat share must divide by **roster size** (5 Conquest / 3 Joust), never by enemies entered. The latter made one known healer a 100% signal.
- The `max_bonus` clamp (0.12) bounds how far any comp can move a single item; 2 of 5 healers already reaches it.
- Enemy names not in the tracked roster are dropped by `isKnownGod` — a real coverage gap.
- The board must stay editable in any order and survive reload, shared links, and mode switches.

**Chosen direction:** Diff ledger with a guided progressive empty/partial state (seed `2cd32ee3`, assigned structure 7 of 7 — a step wizard — kept where it wins and rejected as a spine, because draft input is out-of-order and continuously revised).

**Memorable moment:** The h1 counting its own effect — *"Your draft moved 2 of 6 items"* — over two rows that each name a casualty and a reason. The mechanism was previously computed on every render and discarded three lines before the DOM.

**Unresolved:**
- No link in from Home or a god page; the draft is still a cul-de-sac reachable only from the nav rail.
- The adapted core has no cumulative-gold spine, unlike god detail's ledger — the two build views use different vocabularies.
- `AppSkeleton` still serves a sidebar+build-rows placeholder to a cold `#/draft` load.
- Dropped unknown god names from a shared link are still silent.
- No authored motion beyond the bar draw on the diff rows.
