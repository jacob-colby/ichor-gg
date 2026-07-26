---
version: 1
slug: "viewer-src-components-itemsshop-tsx"
primary_target: "viewer/src/components/ItemsShop.tsx"
related_targets: ["viewer/src/lib/itemFilters.ts"]
---

# Items shop

**Scope:** `viewer/src/components/ItemsShop.tsx` and `viewer/src/lib/itemFilters.ts`. Reaches into the pipeline: `pipeline/smite/build_index.py` `_enrich_items` and the `item_gold_values` index key.

**Visitor mode:** Operate. A browse-and-decide surface over 159 items.

**Audience & job:** A player asking one question — is this item worth its gold? — and a power user who wants to find the most underpriced item in the game.

**Action:** Scan the shelf, filter, open an item and read the arithmetic; jump to its components or the wiki.

**Content / proof:** All computed. Live figures: 30 of 159 underpriced, 53 of 159 with community data, 12 not priced. Rod of Tahuti: Intelligence 80 × 6.59g = 527g, Max Mana 250 × 0.57g = 143g, Mana Regen 2 × 5.61g = 11g, Penetration 5% × 26.57g = 133g → fair 2756g against an actual 3000g, +244g over.

**Constraints:**
- `efficiency` is null for 12 items — tier-1 starters sit out the regression on purpose (`efficiency.py:61-68`) because their gold buys an ability, not stats. State that; never render a dash.
- 106 of 159 items have no community data.
- 127 of 159 reference `builds_from` components absent from the index; 7 have duplicated entries. Dedupe and count the missing rather than dropping them silently.
- `cost - predicted_cost === residual` must hold exactly — the pipeline rounds the residual and derives the predicted cost back from it for this reason.
- `ItemCard` is shared with `ItemPickerModal`. Any change to the card language changes both.

**Chosen direction:** Enriched shelf (seed `962f880f`, structure 6 of 7) with the receipt as its detail. The roll chose the shelf over my row-based Price Ledger, and was right for a reason my ranking missed: a row layout would have split the shared `ItemCard` in two.

**Memorable moment:** The receipt. Four stat rows priced in gold, subtotalled to a fair price, set against what the item actually costs. The model's working, line by line, on the surface whose entire job is that judgement.

**Unresolved:**
- `god_item_scores` (40 ranked items per god) is still unused. A god selector would turn "underpriced" into "underpriced *for Ra*", which is closer to PRODUCT.md's actual positioning.
- Filter state isn't in the URL, so a filtered view can't be shared.
- All 159 cards render at once; no windowing. Fine at this size, not free.
- The shop page itself has only an `<h1>` — the grid has no heading of its own.
