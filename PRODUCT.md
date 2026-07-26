# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Players of SMITE 2, across the skill spectrum, evenly: newer players who don't know the meta and want a clear, correct build without doing the math themselves, and experienced/competitive players who already know builds and want the underlying signals (efficiency, win rate, pick rate, kit fit) surfaced so they can agree, disagree, or refine on the evidence. The design should give a fast, confident answer up front while keeping the reasoning one step away for whoever wants it, not force everyone through the same depth of detail.

## Product Purpose

ichor is a build recommender for SMITE 2 that scores items with a mathematical model instead of copying the community meta, then adapts the build to the actual match (draft) the player is in. It exists because most build sites only report what's popular; ichor also surfaces what's mathematically underpriced for a given god and is honest when the model and the meta disagree.

## Positioning

Every other build site shows popularity. ichor fits a gold-value regression to item stats to find what's *underpriced* for a god's kit, blends that with community win/pick rate and kit fit, and explicitly flags disagreement between its model and the meta rather than hiding it. It is also draft-aware: builds re-rank live based on the actual 4 allies / 5 enemies in the match, not a static per-god page.

## Operating Context

Two halves: a Python pipeline (`pipeline/smite/`) that scrapes wiki.smite2.com and SmiteBrain, scores items/gods, and generates static data; and a Vite + React + TypeScript viewer (`viewer/`) that is the public-facing site. Core workflows: suggested builds per god/mode/flavor, draft-aware build re-ranking, per-item "why this item" signal breakdowns, tier lists (model score vs. community win rate shown side by side), patch-note diffs between data refreshes, and an items shop with an efficiency rating.

## Capabilities and Constraints

- Covers 87 of 89 gods (Cu Chulainn and Ix Chel have no wiki content to scrape).
- Community signal is partial: 18 gods and 104 items have no community data and are shown as *unranked* rather than given an invented tier.
- Deliberately diverges from popularity by design (current validation: win-weighted 0.47, rank correlation 0.36 across 411 pairs) — low agreement with the meta is expected, not a bug to chase toward 1.0.
- Patch-notes diffs only exist between data refreshes, so that page starts empty and fills in over time.
- Threat detection (e.g. flagging enemy healers) relies on wiki ability tags; a god who is situationally a healer without the `Healing` tag won't be counted.
- All scoring weights, role stat maps, flavors, and the draft overlay are tunable via `data/_weights.yaml`.

## Brand Commitments

Name: **ichor**. Explicitly a fan project — not affiliated with or endorsed by Hi-Rez Studios; SMITE is Hi-Rez's trademark, and this must stay disclosed. Suggested builds are presented as heuristic, not official.

## Evidence on Hand

- Per-god scraped analysis notes: `data/Analysis/*.md`.
- Tuning/config source of truth: `data/_weights.yaml`.
- Design specs and implementation plans for prior viewer work: `docs/specs/`, `docs/plans/`.
- Test suites back the pipeline and viewer: 259 Python tests (`pipeline/smite/tests`), 133 viewer tests.
- No invented testimonials, customer logos, or pricing exist and none should be fabricated — this is a free fan tool, not a commercial product.

## Product Principles

1. Show the math, not just the answer — every recommendation decomposes into its signals so a player can disagree with evidence.
2. Default to one confident answer, but never hide the reasoning behind it.
3. Say when the model and the community disagree instead of smoothing it over.
4. Serve both a newcomer wanting a fast correct build and a veteran wanting to interrogate it, without forcing either into the other's depth of detail.
5. Be honest about coverage gaps (missing gods, unranked items, thin patch history) rather than papering over them.
