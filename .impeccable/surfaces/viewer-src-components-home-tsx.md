---
version: 1
slug: "viewer-src-components-home-tsx"
primary_target: "viewer/src/components/Home.tsx"
related_targets: ["viewer/src/lib/divergence.ts"]
---

# Home

**Scope:** `viewer/src/components/Home.tsx` and its lane-board logic (`viewer/src/lib/divergence.ts`). The app shell (`App.tsx`) contributes the rail, header, skip link, and `<main>`.

**Visitor mode:** Operate, with a real arrival moment. This is the app's front door for a data tool, not a marketing page — density is a value, whitespace is not the goal.

**Audience & job:** Two readers at once. A newer player wants a fast, correct answer and a way into a god page. A competitive player wants to interrogate the model — to find a ranking they disagree with and see the evidence. The page must serve the second without slowing the first.

**Action:** Get to a god page, either by search (fast path for a repeat visitor) or by recognising a name in your own lane on the board.

**Content / proof:** Everything on this page is computed from `index.json` at render time — the disagreement count, the per-lane means, the unranked count. Nothing is written down. Concretely: 87 gods, 69 with community data, 18 unranked, 53 tier disagreements, and a Carry column where every ranked god sits below the meta.

**Constraints:**
- `patch_notes` is empty in the shipping index — Home must be authored for the empty case, not the full one.
- 18 gods have no community score and must never be given an invented delta or tier.
- `tierlist` may be absent entirely on an older index; the board disappears and the h1 steps back to a claim it can support.
- Multi-role gods land in exactly one column via `godLane`'s lane priority.

**Chosen direction:** Lane Board carrying the divergence thesis (seed `c96ae713`, structure 3 of 7). Five lane columns ranked by model-vs-meta disagreement, each headed by that lane's mean lean. The claim block above states the disagreement count in display type with the number in gold.

**Memorable moment:** The Carry column. Ten of ten ranked Carries sit below the meta, so the column reads as a solid block of `premium` bars leaning one way — the page *demonstrates* that the disagreement is systematic rather than asserting it. The bars draw outward from centre on load, staggered a lane at a time.

**Unresolved:**
- The board shows the top 6 per lane and reports `+n more`, but "more" links to the whole tier list rather than a lane-filtered view — a lane filter on the tier list would close that loop.
- Mode is not exposed here. `tierlist.conquest` / `tierlist.joust` both exist; Home currently reads the top-level (Conquest) slice without saying so. Either label it or add the toggle.
- Pins are a launcher strip below the board. If pinning gets heavier use, the pinned gods' own divergence rows may belong in the board itself.
