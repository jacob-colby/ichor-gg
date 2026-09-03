# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Players of SMITE 2, across the skill spectrum, evenly: newer players who don't know the meta and want a clear, correct build without doing the math themselves, and experienced/competitive players who already know builds and want the underlying signals (efficiency, win rate, pick rate, kit fit) surfaced so they can agree, disagree, or refine on the evidence. The design should give a fast, confident answer up front while keeping the reasoning one step away for whoever wants it, not force everyone through the same depth of detail.

## Product Purpose

ichor is a build recommender for SMITE 2 that shows its working: what every item costs against what its stats are worth, what a god's own players buy instead, and how the build changes for the match being drafted. It exists because most build sites hand over six icons with no reasoning attached. ichor's own honesty about what it can and cannot demonstrate is part of the product, not a caveat bolted on — see `docs/STATE.md`.

## Positioning

Every other build site shows popularity. ichor fits a gold-value regression to item stats to find what's *underpriced* for a god's kit, blends that with community win/pick rate and kit fit, and prints the decomposition next to the answer. It is also draft-aware: builds re-rank live on the actual allies and enemies in the match, not a static per-god page.

**The positioning changed on 2026-08-05 and the old version must not come back.** ichor used to sell the *disagreement* between its model and the meta — "the community underrates 26 gods" was the home page. That claim rested on a god ranking which measured −0.117 against real god strength, and its 59% disagreement rate was *below* the 75% two unrelated rankings produce. The tier list now ranks on real match outcomes only. What ichor claims is reasoning and honesty, never that it out-ranks the community.

## Operating Context

Two halves: a Python pipeline (`pipeline/smite/`) that scrapes wiki.smite2.com and SmiteBrain, scores items/gods, and generates static data; and a Vite + React + TypeScript viewer (`viewer/`) that is the public-facing site. Core workflows: suggested builds per god/mode/flavor (Conquest / Joust / Arena), draft-aware build re-ranking, per-item "why this item" signal breakdowns, a tier list ranked on the Wilson lower bound of real match outcomes, patch-note diffs between data refreshes, and an items shop rating what an item's stats are worth against what it costs.

## Capabilities and Constraints

- Covers all 90 gods on the roster that have a wiki page; the grid lists 92, and Hachiman and Hel are entries with nothing behind them yet. Ravana was added 2026-08-29. Cu Chulainn and Ix Chel had empty wiki pages for months and were scraped on 2026-08-19 once those filled in; Hachiman and Hel are in that state now.
- The model is a working **filter** and not a working **ranker**: measured against a random-baseline control it finds community-worthy items ~7x better than chance (40.9% against a 5.7% random core), while its ordering skill inside the community's own item set is indistinguishable from zero. "Sensible items" is supported; "right order" is not.
- Joust and Arena have no outcome data whatsoever. Their gods ship *unranked* rather than given an invented tier — but their builds still ship, resting on the model alone. That is two thirds of the shipped builds.
- The headline agreement metric cannot be used to tune the model: both its targets are also model inputs, so it is maximised by deleting the model. Use the leakage-free measure in `smite.calibrate`. Twenty-four correct-looking improvements have been measured against it, and all but two shipped off (one shipped on; one implements nothing and audits a community-derived constant the leakage-free measure does not neutralise); see `docs/STATE.md` section 4 before re-attempting any of them.
- Patch-notes diffs only exist between data refreshes, so that page starts empty and fills in over time.
- 72 of the 89 gods have an aspect, and only the 7 with a hand-tuned scoring overlay in `data/_weights.yaml` have a build behind it. The aspect control shows for all 72 — the kit text and the community's pick rate are real information — and states plainly when it will not move the build.
- Threat detection reads the scraped **ability text**, not just the wiki's role labels, and takes the union of the two — `Healing` is on 9 of 89 gods while 42 actually heal, and player-made walls (Cabrakan, Odin, Thor, Ymir) have no label at all. The counts say a kit *contains* an effect, not how often it lands or how long it lasts; that is the honest ceiling on text classification.
- Four relics are structurally unrecommendable. An upgraded relic does take one of the six item slots — the community holds Shell of Rebuke in 62 tracked builds — but all four carry a `+7.5% of all Stats from Items` multiplier that nothing here can price, so the gold model reads them 698–1416g overpriced and they never win a slot on score. Genie's Lamp is the same failure.
- All scoring weights, role stat maps, flavors, and the draft overlay are tunable via `data/_weights.yaml`.

## Brand Commitments

Name: **ichor**. Explicitly a fan project — not affiliated with or endorsed by Hi-Rez Studios; SMITE is Hi-Rez's trademark, and this must stay disclosed. Suggested builds are presented as heuristic, not official.

## Evidence on Hand

- Per-god scraped analysis notes: `data/Analysis/*.md`.
- Tuning/config source of truth: `data/_weights.yaml`.
- Design specs and implementation plans for prior viewer work: `docs/specs/`, `docs/plans/`.
- Living engineering doc — current state, design decisions with their evidence, negative-results register, what's left: `docs/STATE.md`. The dated files in `docs/specs/` and `docs/plans/` are point-in-time and never updated.
- The combat model is calibrated against twelve in-game readings at 0.0% worst-case error (`pipeline/smite/combat.py`, gated by `smite.calibrate_combat`).
- Test suites back the pipeline and viewer: 860 Python tests (`pipeline/smite/tests`), 753 viewer tests.
- No invented testimonials, customer logos, or pricing exist and none should be fabricated — this is a free fan tool, not a commercial product.

## Product Principles

1. Show the math, not just the answer — every recommendation decomposes into its signals so a player can disagree with evidence.
2. Default to one confident answer, but never hide the reasoning behind it.
3. Claim only what has been measured, and say plainly where it hasn't. "We didn't measure this" and "this is bad" are different facts and must never be rendered the same way.
4. Serve both a newcomer wanting a fast correct build and a veteran wanting to interrogate it, without forcing either into the other's depth of detail.
5. Be honest about coverage gaps (missing gods, unmeasured modes, thin patch history) rather than papering over them — an empty page beats a fabricated ranking.
