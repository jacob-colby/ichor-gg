---
version: 1
slug: "viewer-src-components-detailpanel-tsx"
primary_target: "viewer/src/components/DetailPanel.tsx"
related_targets: ["viewer/src/lib/ledger.ts"]
---

# God detail — Builds

**Scope:** `viewer/src/components/DetailPanel.tsx` and its ledger logic (`viewer/src/lib/ledger.ts`). The Info tab (`GodInfo.tsx`) is a separate, un-redesigned surface. `App.tsx` supplies `tierEntry` from `data.tierlist`.

**Visitor mode:** Operate. The deepest data surface in the app; density is the point.

**Audience & job:** A player who arrived from Home mid-argument — they saw a divergence row and clicked it. They want to know what the model buys for this god and where the meta disagrees, then either accept it or interrogate it.

**Action:** Read the buy order; expand a row to see why that item scored what it did; select a matchup swap; switch flavor.

**Content / proof:** All computed from `index.json` at render. `tierlist.gods[god]` supplies the verdict; `slot_scores` supplies the composite plus four axes; item `cost` supplies the gold spine; the community entry's `slot_order` supplies the comparison track. Concretely: Ra spends 16,550g and shares 4 of 6 items with the meta; Cupid is model 0.45/C against community 0.68/S and shares only 2 of 6.

**Constraints:**
- **No timing data exists anywhere in the index** — no minutes, no spike marks. The spine is cumulative gold, which is derivable. Never render a time axis.
- The weights combining the four axes into `total` are not published — show them as contributions, never a sum.
- 18 gods have no community *rating* while still having a community *build*. Both facts must be stated; they are not the same thing.
- Joust has no community entry for most gods, so the comparison track disappears and the ledger must say so rather than silently dropping columns.
- A fun build is off-class by design and is never compared to the meta.

**Chosen direction:** Buy Timeline on a cumulative-gold axis (seed `d3f94782`, structure 7 of 7), fused with the model-vs-meta comparison that the user pinned. The tab rail is gone: community became the constant comparison track, flavors became a re-weighting control.

**Memorable moment:** The per-row order disagreement. Ra and the community both buy Soul Gem, but the model buys it last at 16,550g and the meta buys it third at 7,450g — so the row reads "model buys later by 9,100g". A side-by-side comparison would have reported "both buy Soul Gem" and missed the argument entirely.

**Unresolved:**
- The Info tab is untouched: zero headings, every ability rendered twice, and raw scraper chrome ("Expand Ability Video", "<God> Notes:") shipping as body copy. The text cleanup belongs in the Python pipeline, not the viewer.
- `ItemPickerModal` still isn't a real dialog — no focus trap, no Escape. `Legend.tsx` has the pattern to copy.
- `god_item_scores[god]` (40 ranked items per god) is still unused. It is the strongest candidate for replacing the trailing `rationale` prose with a ranked "underpriced for this god" strip.
- Mode still isn't in the URL, so a shared god link always reopens Conquest.
- The 87 sidebar rows are still `div[role="button"]` wrapping two focusable buttons — a nested-interactive violation outside this surface's scope.
