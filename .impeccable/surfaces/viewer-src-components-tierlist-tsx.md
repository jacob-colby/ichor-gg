---
version: 1
slug: "viewer-src-components-tierlist-tsx"
primary_target: "viewer/src/components/TierList.tsx"
related_targets: ["viewer/src/lib/tierBands.ts"]
---

# Tier list

**Scope:** `viewer/src/components/TierList.tsx` and its band logic (`viewer/src/lib/tierBands.ts`).

**Visitor mode:** Operate. A browse-and-scan surface over 87 gods / 159 items.

**Audience & job:** A player who wants the ranking, and — increasingly, after Home — wants to know where the model and the meta part ways. Both readings must work without switching views.

**Action:** Scan a band, spot a name worth arguing about, click through to that god or item.

**Content / proof:** All computed from `index.json` at render. Live figures: 16 of 69 gods agreed, 28 the model ranks higher, 25 the meta ranks higher, 18 unranked. Per-band disputed counts (6/13/18/16) sum to 53 — the same disagreement count Home states in its headline, from the same data.

**Constraints:**
- Joust has **zero** community ratings for gods (0 of 87). The summary must not claim agreement it has no basis for, and the "only disputed" control must not appear.
- Item slices are **byte-identical between modes** — the pipeline doesn't re-score items per mode. This is derived at runtime, not assumed, so the note disappears if that ever changes.
- 18 gods and 106 items have no community rating; they stay in the model's own band with an `unranked` ghost rather than being bucketed into a separate group.
- An index predating the per-mode keys falls back to the flat top-level shape.

**Chosen direction:** Tier bands with community ghosts (seed `f397d87a`, structure 7 of 7). The roll landed on the most conventional form on my list and was right to: a player clicking "Tiers" expects bands, not the 4×4 disagreement matrix I'd ranked first. The matrix survives as the per-band and page-level agreement tallies.

**Memorable moment:** The S band reading `6 disputed · 1 agreed · 2 unranked`. One god in the model's top tier is also the community's top tier — that single number is the product's whole position, stated where a player is already looking.

**Unresolved:**
- No lane-filtered deep link, so Home's `+n more` still lands on the unfiltered list.
- Filter state isn't in the URL, so a filtered view can't be shared.
- Items have no lane/role dimension, so the chip row is replaced by a single select — the two subjects have visibly different control affordances.
