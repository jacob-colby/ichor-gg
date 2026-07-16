# SMITE 2 reference system: vault database + second-monitor viewer

Status: approved, ready for implementation plan
Date: 2026-07-16

## Problem

SMITE 2 is a beta game patching every 1-2 weeks. Jacob wants a reference
system that treats this as a data pipeline (refresh command, staleness
tracking) rather than a one-time wiki import, plus a lightweight second-monitor
viewer for build lookup mid-game. Two things need to exist:

1. A structured, Dataview-queryable knowledge base of gods/items/builds inside
   the vault, refreshed from `wiki.smite2.com` and `smitebrain.com`.
2. A small local Vite + React + TS + Tailwind app that reads that base and
   renders a glanceable, filterable build list for a second monitor.

## Housekeeping (do this regardless of implementation timing)

Add `docs/` to `.obsidian/app.json` → `userIgnoreFilters`, alongside the
existing `tools/` and `events/` entries — it currently holds only
`docs/superpowers/{specs,plans}`, the same machine/skill-surface category.
`viewer/` gets the same entry once it exists.

## Relationship to existing SMITE 2 content

`03. Workspaces/Gaming/SMITE 2/` already exists — a personal practice journal
(why-this-game, goals, session structure) with hand-written god notes
(Chiron, Ullr, Hou Yi), an items-meta file, and a Conquest-fundamentals file,
following the same shape as Jacob's other game folders (Overwatch, Valorant,
Rocket League, Deadlock, Kovaaks). This system does not replace it or create
a second parallel "SMITE" folder — it extends it, and puts the auto-refreshed
raw data in a separate, pipeline-owned location:

```
04. System/Data/SMITE/                    ← pipeline-owned, never hand-edited
  Gods/<god>.md
  Items/<item>.md
  _cache/                                  raw HTML cache, keyed by URL, 24h TTL
  _assets/                                 god portraits + item icons
  _logs/refresh-<date>.md                  per-run diff report

03. Workspaces/Gaming/SMITE 2/            ← existing journal, extended
  Builds/<god>-<mode>.md
  Reference/                              game-mode differences, economy cheat sheet
  00-Overview.md                          (existing, untouched)
  01-god-notes/{Chiron,Ullr,Hou Yi}.md    (existing, trimmed — see Migration)
  02-Items Meta.md                        (existing, untouched — hand-written meta commentary)
  03-Conquest Fundamentals.md             (existing, untouched)
  00-vod-reviews/                         (existing, untouched)
```

`04. System/` currently holds Daily-OS infrastructure (Backlog, Context,
Templates) — this is its first tenant of domain reference data, but the
principle holds: it's machine-maintained, not a place Jacob writes by hand,
same spirit as `tools/`.

**Assets scope:** only SMITE assets move into `04. System/Data/SMITE/_assets/`
(migrated from `Gaming/_assets/smite2/`, one embed-path update in existing
god-notes). Other games' `_assets/<game>/` folders are untouched — migrating
all of them into a shared `Data/` location is a separate, larger refactor
outside this project's scope.

**Migration:** `01-god-notes/*.md` currently contains a "Build Paths" section
duplicating what `Builds/<god>-Conquest.md` will now own. That section is
pulled out into the new Build note (tagged `source: mine` initially, until
refreshed data / pro curation is added), and `01-god-notes/*.md` is trimmed to
strengths/weaknesses, matchup feel, and playstyle notes — the personal-judgment
content that isn't a structured build. They link to `Builds/` for the item
order itself.

## Data sources

- **`wiki.smite2.com`** — MediaWiki-style, server-rendered, `/w/<Name>` URLs.
  Confirmed structure: god pages have an infobox (pantheon, role, damage type,
  base stats with per-level gains), an Abilities section (cooldown + cost per
  rank), and a **God Aspect** section (Smite 2's alternate-kit system — e.g.
  Chiron's "Aspect of the Heroic Tutor" reworks his passive and several
  abilities). No build/item-recommendation data on god pages. Items are listed
  categorically by tier with individual `/w/<Item_Name>` pages.
- **`smitebrain.com`** — aggregate build stats from ranked matches:
  pick_rate/win_rate per item slot and **per aspect**, at `/gods/<slug>/`.
  This is the concrete source for the "community" build tier — previously
  undefined in the original schema sketch, now backed by real data.

Both sites get their own local HTML cache (keyed by URL, 24h TTL) and their
own conservative rate limit (~1 request every 2-3 seconds per run). A full
refresh across the roster is a deliberate on-demand or weekly action, not
continuous polling.

**Fetch mechanics (confirmed against the live sites):** `smitebrain.com` is
plain server-rendered HTML (SvelteKit SSR) — a normal `requests` call already
returns full build/pick-rate/win-rate data, no bot protection encountered.
`wiki.smite2.com` sits behind a genuine Cloudflare JS challenge
(`Cf-Mitigated: challenge` header) — a plain HTTP client gets a 403.
Reaching it requires a headless browser: the wiki-fetch path uses
**Playwright** (one-time Chromium download) to load pages like a real
browser, while the SmiteBrain-fetch path stays a plain `requests` call. This
is the one place the tech stack needs an addition beyond `requests` +
`beautifulsoup4`.

## Frontmatter schemas

**God note** (`Gods/<god>.md`) — pipeline-owned entirely:

```yaml
---
type: smite-god
name: Chiron
pantheon: Greek
role: Hunter                 # Hunter | Mage | Warrior | Guardian | Assassin
damage_type: physical
release_date: 2026-01-27
base_stats:
  health: {base: 569.48, per_level: 86.48}
  mana: {base: 322.62, per_level: 48.3}
  attack_speed: {base: 1.0, per_level: 0.0151}
  physical_prot: {base: 18.76, per_level: 2.76}
  magical_prot: {base: 25.3, per_level: 1.38}
abilities:
  - slot: passive
    name: Herbal Medicine
  - slot: "1"
    name: Training Exercise
    cooldown: [13, 13, 13, 13, 13]
    cost: [55, 60, 65, 70, 75]
  # ...2, 3, ultimate
aspects:
  - name: Aspect of the Heroic Tutor
    kit_changes: >
      Target Mark applies to one target only; passively copies 10% of damage
      dealt to that target as Physical Damage. Training Exercise grants
      allies Strength/Intelligence. Centaurus gains a slow and shields +
      attack speed + passive heal to allies hit.
source_url: https://wiki.smite2.com/w/Chiron
last_verified: 2026-07-16
---
<!-- WIKI:START -->
(full ability text, passive description — pulled prose, rewritten on refresh)
<!-- WIKI:END -->

(anything below this line is Jacob's, untouched by refresh)
```

**Item note** (`Items/<item>.md`) — pipeline-owned entirely:

```yaml
---
type: smite-item
name: Deathbringer
tier: 3
cost: 2900
stats: {power: 40, crit_chance: 25, penetration_pct: 10}
passive: "Critical hits deal 175% damage instead of 150%"
builds_from: ["Brawler's Beat Stick", Executioner]
builds_into: []
source_url: https://wiki.smite2.com/w/Deathbringer
last_verified: 2026-07-16
---
```

**Build note** (`Builds/<god>-<mode>.md`) — mixed ownership, per-entry:

```yaml
---
type: smite-build
god: Chiron
mode: Conquest
builds:
  - source: community                    # pipeline-owned, refreshed from SmiteBrain
    aspect: Aspect of the Heroic Tutor
    aspect_pick_rate: 0.91
    aspect_win_rate: 0.53
    slot_order:
      - {item: Transcendence, pick_rate: 0.88, win_rate: 0.54}
      - {item: Ninja Tabi, pick_rate: 0.81, win_rate: 0.55}
      # ...
    source_url: https://smitebrain.com/gods/chiron/builds
    last_verified: 2026-07-16
  - source: pro                          # hand-curated, never touched by refresh
    aspect: Aspect of the Heroic Tutor
    slot_order: [Transcendence, "Devourer's Gauntlet", Wind Demon, Deathbringer, "Qin's Sais", Ninja Tabi]
    situational_swaps:
      - vs_tag: heavy_cc
        swap: Purification Beads earlier
      - vs_tag: magic_heavy
        swap: Magi's Cloak over Rage
    notes: "SPL hunter crit-core, Trans/Devourer opener"
  - source: mine                         # hand-curated, never touched by refresh
    aspect: Aspect of the Heroic Tutor
    slot_order: [...]
    situational_swaps: [...]
last_verified: 2026-07-16
---
```

`vs_tags` is an open list, not a fixed 4-value enum — it covers both the
threat-pattern axis (`heavy_cc`, `sustain`, `poke`) and the damage-type axis
(`magic_heavy`, `physical_heavy`), so an Arena/Joust team that's mostly one
damage type gets its own swap row alongside burst/CC/sustain/poke.

Refresh only ever rewrites the `source: community` entry in a Build note's
`builds` array (matched by that key) — `pro` and `mine` entries are never
touched by any automated process.

## Pipeline (Python)

- `refresh.py --refresh <god|item name>` — re-pulls one god or item, diffs
  against the existing frontmatter + WIKI block, overwrites pipeline-owned
  fields, logs the change to `_logs/refresh-<date>.md`. Body content outside
  the WIKI block is untouched.
- `refresh.py --refresh-builds <god>` — re-pulls SmiteBrain aggregate data,
  rewrites only the `source: community` entry in that god's Build notes.
- `refresh.py --all` — full roster refresh (gods + items + community builds),
  on-demand or weekly, respecting the same rate limits and cache.
- Local HTML cache under `_cache/`, keyed by URL, 24h TTL — a same-day rerun
  doesn't re-hit the network.
- Missing/failed fetches log to a `MISSING.md`-style report rather than
  silently skipping, same pattern as the existing Gaming asset downloader.

## Assets

Extends the existing `_download.py` pattern (currently pulls SMITE 2 god
icons from SmiteSource/Fandom into `Gaming/_assets/smite2/`): moved to
`04. System/Data/SMITE/_assets/`, extended to also pull item icons. No skins,
base portraits/icons only, capped at ~50-300KB per image, referenced by
relative path in frontmatter — never hotlinked.

## Reference notes

`03. Workspaces/Gaming/SMITE 2/Reference/` — game-mode differences (Joust vs
Conquest vs Arena vs Assault: gold curve, objective timers, itemization
priorities) and an economy/damage cheat sheet (penetration math, protection
diminishing returns, item cost curve). Hand-written once, then manually
updated — this content is stable game-design knowledge, not per-patch churn
like god kits or item costs, so it's outside the automated refresh loop.

## Viewer

Vite + React + TypeScript + Tailwind SPA at vault-root `viewer/` (sibling to
`tools/` — it's tooling, not vault content). Added to `.obsidian/app.json`
`userIgnoreFilters` alongside `docs/`, matching the existing treatment of
`tools/` and `events/`: physically at root, hidden from Obsidian's file
explorer so the vault still *feels* clean day-to-day.

**Layout** (confirmed via mockup): a narrow vertical rail of god portraits on
the left. Clicking a god opens its build(s) in a detail panel: slot order
(icon + item name, stacked) on the left, situational swap rows (each with its
own item icon) in a right-hand column. Archetype/damage-type chips (heavy CC /
magic-heavy / physical-heavy / sustain / poke) sit above the swap column —
clicking one highlights the matching row rather than filtering the rail.
Source badge (`pro`/`community`/`mine`) and mode shown in the panel header.

**Data flow:** a Python script walks `04. System/Data/SMITE/` and
`03. Workspaces/Gaming/SMITE 2/Builds/` frontmatter and writes one
`index.json`. The app fetches that JSON on load and on a manual "reload data"
button — no file-watcher, no backend server, since content only changes on
patch days.

## Testing

- Pipeline: unit tests against saved HTML fixtures (captured once from real
  pages) for the god-page parser, item-page parser, and SmiteBrain build
  parser — so tests don't hit the network and don't break when the live wiki
  changes mid-development.
- Refresh/diff logic: test that pipeline-owned fields update, WIKI block
  content updates, and content outside the WIKI block / non-community build
  entries survive a refresh unchanged (this is the core guarantee of the
  whole system — needs explicit test coverage, not just manual trust).
- Viewer: component tests for the rail + detail panel against a fixture
  `index.json`; manual check in a real browser for the glanceability goal
  (legible at a glance, second-monitor sized) since that's a visual judgment
  call, not something a unit test can verify.
