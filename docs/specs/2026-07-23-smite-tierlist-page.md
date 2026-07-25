# SMITE 2 viewer — Tier-list page (Phase 4)

Status: design + implementation spec
Date: 2026-07-23

## Problem
Users want a ranked at-a-glance view of gods and items, filterable, and switchable
between **the community's view** and **our calculations** — one of the six
done-state criteria.

## Signals (grounded in the real index; no new scraping)
**Items**
- *ours* — the efficiency model's continuous score (gold-value residual). Every
  numeric-cost non-starter item has one; it already backs `efficiency_tier`.
- *community* — `item.meta.win_avg` (mean community win rate across the gods that
  build it). Present on **55 / 159** items; absent for the rest.

**Gods**
- *ours* — mean `slot_scores[item].total` across the god's suggested Conquest core
  (how strongly our model rates the items the god's kit wants). All 87 gods.
- *community* — `aspect_win_rate` from the god's community Conquest build.
  Present on **69 / 87** gods.

## Design
### Ranking (`tools/smite/tierlist.py`, pure + unit-tested)
- `god_rankings(gods, builds) -> [{name, ours, community, role, damage_type}]`
- `item_rankings(items, eff_scores) -> [{name, ours, community, tier, efficiency_tier}]`
- `assign_tiers(entries, key) -> entries + {tier_ours|tier_community}`: rank by the
  chosen score and bucket into **S/A/B/C** by *percentile* (top 10% = S, next 20% =
  A, next 40% = B, rest = C). Percentile (not absolute cutoffs) keeps buckets
  meaningful as the meta shifts. Entries missing that score are **unranked** and
  surface in a separate "no community data" group — never silently dropped or
  treated as zero (that would fake a bottom tier).
- Emitted into `index.json` as `tierlist: {gods: [...], items: [...]}` via
  `build_index`.

### Viewer (`TierList.tsx`, route `#/tiers`)
- Nav gains a **Tiers** entry (icon rail + mobile bottom bar).
- **Source toggle**: `Our calc ⇄ Community` (segmented pill, gold active). Switching
  re-buckets the same entries by the other score.
- **Subject toggle**: Gods ⇄ Items.
- **Tier rows**: S/A/B/C, each a labeled band (tier letter chip + the entries as
  cards — god head icon + name + role accent; item icon + name + cost/tier +
  efficiency badge). Reuses the existing card language and role/damage accents.
- **Filters**: gods → lane pills (reuse `roleAccent` LANES) + damage; items → tier
  + efficiency. Search box for both.
- **Unranked group** rendered last, muted, labeled "No community data" (only when
  the community source is active and some entries lack it).
- Clicking an entry navigates to that god/item.
- Mobile: same bands, cards wrap; toggles scroll horizontally.

## Data flow
`recommend`/`efficiency` (existing scores) → `tierlist.py` (rank + bucket) →
`build_index` → `index.json.tierlist` → `TierList.tsx`.

## Testing
- **Python**: percentile bucketing (S/A/B/C boundaries, ties, tiny sets); entries
  missing a score are unranked, not zero; god/item ranking shapes; `build_index`
  emits `tierlist`. `data_audit` extension: every god/item appears in the tier list.
- **Viewer**: source toggle re-buckets; subject toggle switches datasets; filters
  narrow; unranked group only shows for community; empty state; nav routes to
  `#/tiers`.
- **Manual**: browser-verify both toggle modes at desktop + 390px.

## Limitations
- Community item coverage is partial (55/159) and god coverage is 69/87 — the
  unranked group makes that visible rather than hiding it.
- `aspect_win_rate` is an aspect-level proxy for god strength (the closest
  community signal available without a new source); labeled as such in the UI.
- No new scraping; tier lists are only as fresh as the last refresh.
