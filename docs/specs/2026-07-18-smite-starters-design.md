# SMITE 2 recommender: starter items

Status: approved, ready for implementation plan
Date: 2026-07-18

## Problem

Builds currently show only the 6 core Tier III items — no **starter**. Every real
SMITE 2 build opens with a role-appropriate starter (Tier 1, upgradeable at level
20). Jacob wants the recommender to pick a starter per god and the viewer to show
it above the core. This is Part 1 of a two-part request (Part 2, an in-app build
editor, is a separate spec).

## Verified facts (from live wiki + parser)

- The existing `wiki_parser.parse_item_page` **parses starters correctly** (tier,
  stats, passive) — no parser change needed.
- Base starters return **`cost: None`** on their pages. That's fine: null-cost
  items are already excluded from the efficiency regression, and the recommender
  selects starters by role, not efficiency.
- The existing **`is_buildable` filter (tier ≥ 3 or None) already excludes**
  starters (tier 1 base, tier 2 upgraded) from core-build scoring — so adding
  them to `Items/` cannot pollute core builds.
- Upgrade linkage: an upgraded starter's `builds_from` points at its base (e.g.
  Sharpshooter's Arrow → Gilded Arrow), and starters are role-flavored.

SMITE 2 starters (base, ~600–650g on the store; page cost null):
Selflessness, Leather Cowl, Bluestone Pendant, Vampiric Shroud, War Flag,
Conduit Gem, Gilded Arrow, Sands of Time, Bumba's Golden Dagger, Bumba's Cudgel,
Warrior's Axe, Death's Toll. Upgraded (level 20): Heroism, War Banner, Bluestone
Brooch, Hunter's Cowl, Blood-soaked Shroud, Sharpshooter's Arrow, Bumba's Spear,
Archmage's Gem, Sundering Axe, Death's Embrace, Bumba's Hammer, Pendulum of the Ages.

## Design

### Scrape

Add the base + upgraded starters to `Items/` via the existing `refresh_item`
(they parse). They live alongside other items; the tier filter keeps them out of
core builds. Icons download as usual. Tag them `[]` in `_tags.yaml` (starters
aren't selected by effect-tag) so the "untagged items" report stays quiet.

### Config — `starters` in `_weights.yaml`

A tunable block declaring, per base starter, its level-20 upgrade and the role
tokens it fits (same `match_any` token style as flavors, matched against the
god's tokenized `role` + `specializations`). A `priority` orders overlapping
matches so each god resolves to one starter:

```yaml
starters:
  - base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
    match_any: [Carry, Sharpshooter, Hunter]
    priority: 10
  - base: Conduit Gem
    upgrade: Archmage's Gem
    match_any: [Mid, Nuker, Mage, Sniper]
    priority: 10
  - base: Warrior's Axe
    upgrade: Sundering Axe
    match_any: [Solo, Warrior, Brawler, Tank]
    priority: 10
  - base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
    match_any: [Jungle, Slayer, Assassin]
    priority: 10
  # …remaining starters; a low-priority default (e.g. Death's Toll → Death's
  # Embrace) catches any god no rule matches, so a starter is always returned.
```

The exact upgrade pairings + role tokens are finalized during implementation by
scraping each starter and reading its `builds_from` upgrade link; the config is
the user-tunable source of truth.

### Recommender — `pick_starter(god, weights)`

Returns `{base, upgrade}` for the highest-`priority` starter whose `match_any`
intersects the god's token set (reusing the flavor `_god_tokens` logic), falling
back to the declared default. `recommend.build_suggested_entries` stamps a
`starter` field on each suggested entry (same value across a god's builds — it's
role-based, not flavor/mode-specific). Community/mine entries get no starter
(SmiteBrain doesn't provide one; the editor may add it later).

### Data model

Each `suggested` build entry gains an optional
`starter: {base: <name>, upgrade: <name>}`. `merge_suggested_entries`,
`build_index`, and the mode/flavor logic are unchanged (the field just rides
along). Community/mine entries omit it.

### Viewer

Above the "SLOT ORDER" header, a **"STARTER"** line renders `starter.base`
→ `starter.upgrade` with item icons and hover tooltips (reusing the existing
`Tooltip` + `ItemTooltipBody` and `iconSlug`). Shown only when the active entry
has a `starter`. Types gain the optional `starter` field on the curated entry.

## Recommender flow

`refresh` scrapes starters into `Items/` → `recommend --all` stamps each
suggested build's `starter` via `pick_starter` → `build_index` carries it into
`index.json` → viewer renders the STARTER line.

## Testing

- **Python**: `pick_starter` returns the role-matched starter per god (Chiron/
  Cernunnos/Ullr → Gilded Arrow; Ra/Agni/Morgan → Conduit Gem; Hercules →
  Warrior's Axe; Susano → Bumba's), and the declared default when nothing
  matches. `build_suggested_entries` stamps `starter` on suggested entries.
  Starters remain excluded from core `slot_order` (tier filter).
- **Viewer (vitest/RTL)**: a build with a `starter` renders the STARTER line with
  both base and upgrade; a build without one doesn't.
- **Manual**: regen, open the app, confirm each god shows a sensible starter.

## Limitations

- Starter choice is role-based (calibrated mapping), not meta/efficiency-derived —
  same honest ceiling as god-fit. Tunable in `_weights.yaml`.
- Base starters carry no cost on their wiki page → excluded from efficiency
  scoring (intended; they're not core items).
- Joust uses the same starter as Conquest (starter choice is role-driven, not
  mode-driven) — acceptable; revisit if Joust starter meta ever diverges.

## Open questions — resolved during design

- Where starters live → `Items/` (tier filter already excludes them from cores).
- How selected → role-token match in a tunable `_weights.yaml` `starters` block,
  with a priority + default so every god resolves to exactly one.
- Where shown → a STARTER line above the core on suggested builds, base → upgrade.
