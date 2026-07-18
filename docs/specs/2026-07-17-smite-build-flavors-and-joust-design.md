# SMITE 2 recommender: themed build flavors + Joust mode

Status: approved, ready for implementation plan
Date: 2026-07-17

## Problem

The recommender emits a single `suggested` "core" build per god, Conquest-only.
Jacob wants two additions:

1. **Themed "fun" build variants** per god (crit, burst, bruiser, anti-tank) —
   but only the ones that make sense for that god's damage type + role.
2. **Joust mode** — build suggestions tuned to how Joust actually plays, not
   relabeled Conquest. SmiteBrain (our community win/pick source) has no Joust
   data, so Joust must be driven by math + a mode profile, honestly labeled.

Both are extensions of the existing scorer (efficiency + win + pick + god-fit)
and assembler; neither needs new scraped data.

## Guiding principle (unchanged)

Rigorous where numbers exist, openly qualitative where they don't. Flavor and
Joust builds are **calibrated opinion, not meta-proven** — labeled as such. The
system still surfaces and explains; it never fakes precision.

## Design

### Build flavors

A flavor is a **scoring overlay + assembly constraint** applied on top of the
existing per-god scoring, producing a distinct `suggested` build. Flavors are
defined in `_weights.yaml` (user-tunable) so the roster and weights aren't
hardcoded:

```yaml
flavors:
  crit:
    damage_type: physical            # only physical gods
    roles: [Hunter, Carry, Sharpshooter]   # and a basic-attack role
    stats: {Critical Chance: 1.5, Attack Speed: 1.2, Strength: 0.8}
    max_lifesteal: 1
  burst:
    roles: [Mage, Nuker, Assassin, Warrior]   # any damage type
    stats: {Strength: 1.0, Intelligence: 1.0, Penetration: 1.5, Cooldown Rate: 1.0}
    max_lifesteal: 1
  bruiser:
    roles: null                      # all damage gods
    stats: {Health: 1.0, Physical Protection: 0.8, Magical Protection: 0.8}
    tag_bonus: {sustain: 0.3}
    max_lifesteal: 2
  anti-tank:
    roles: null
    stats: {Penetration: 2.0}
    tag_bonus: {protection-shred: 0.3}
    max_lifesteal: 1
```

**Eligibility** — `eligible_flavors(god)` returns the flavors where:
- the flavor's `damage_type` (if set) equals the god's, **and**
- the flavor's `roles` is `null`, **or** the god's `role`/`specializations`
  intersect the flavor's `roles`.

So Chiron (Carry/Sharpshooter/Nuker, physical) → crit, burst, bruiser,
anti-tank; Ra (Mage, magical) → burst, bruiser, anti-tank (no crit); Hercules
(Warrior, physical) → burst, bruiser, anti-tank (no crit).

**How a flavor scores** — the flavor's `stats` map is merged over the god's
`role_stats` (flavor weights win) when computing god-fit, and its `tag_bonus`
adds to items carrying those tags. Everything else (efficiency, win/pick for
Conquest, damage filter, buildable filter) is unchanged. Then `assemble_core`
runs with the flavor's `max_lifesteal`. The result is a distinct core skewed
toward the flavor's identity while still respecting efficiency and buildability.

The existing "core" build is the flavor-less balanced build (the current
behavior), always emitted first.

### Joust mode

Joust is a **mode profile** — a scoring overlay encoding how Joust differs
(3v3 single lane, constant fighting, shorter games, sustain wars). Also in
`_weights.yaml`:

```yaml
modes:
  conquest: {}   # default — no overlay, meta-backed as today
  joust:
    signals: {efficiency: 0.5, win: 0.0, pick: 0.0, fit: 0.5}   # no meta data
    tag_bonus: {sustain: 0.25, anti-heal: 0.3, aura: 0.2, wave-clear: -0.15, mobility: -0.1}
    label: "Joust — math + mode profile (no meta win/pick data)"
```

- **Signals:** win/pick drop to 0 (SmiteBrain is Conquest-only); efficiency +
  fit carry the score.
- **Tag bonuses:** boost sustain / anti-heal / aura (Joust fighting + sustain
  wars); penalize wave-clear / mobility (less split-push value on one lane).
- Conquest keeps its existing signal weights (the `conquest` profile is empty =
  no overlay).

Joust builds are `suggested` only (core + eligible flavors) — no community/mine
(those are Conquest concepts). Each Joust build's rationale carries the profile
`label` so the "no meta data" caveat is visible in the viewer.

### Composition

A build is `(mode, flavor)`: the mode profile sets signal weights + mode
tag-bonuses; the flavor adds stat weights + flavor tag-bonuses + `max_lifesteal`.
A "Joust Bruiser" build = Joust profile ⊕ bruiser flavor. Conquest Core = no
mode overlay + no flavor (today's build).

### Data model

- Build notes split by mode: `<god>-Conquest.md` (community + suggested[core +
  flavors] + mine) and `<god>-Joust.md` (suggested[core + flavors] only).
- Each `suggested` entry keeps its existing shape plus its `archetype` is now
  one of `core | crit | burst | bruiser | anti-tank`. `situational_swaps`,
  `swap_item`, and `rationale` unchanged.
- `merge_suggested_entries` already replaces the full `suggested` set in a note,
  so it writes core + flavors per mode file with no change.
- `build_index` already globs all Build notes → both mode files flow into
  `index.json` automatically. No change.

### Recommender flow

`recommend.py` iterates, per god: for each mode in (`conquest`, `joust`), build
`[core] + [flavor for flavor in eligible_flavors(god)]`, and write them to
`<god>-<mode>.md` via `merge_suggested_entries`. Conquest additionally keeps its
community entry (written by `refresh`, untouched) and any `mine` entries.

### Viewer

- **Mode toggle** (segmented Conquest | Joust, top-right of the detail header).
  Defaults to Conquest. Persists per session, resets sensibly on god change.
- **Build tabs** show the selected mode's entries. Suggested entries are
  labeled by `archetype` (Core / Crit / Burst / Bruiser / Anti-tank); community
  and mine keep their source labels. Tabs wrap to a second row if needed.
- Everything else (headshot header, item tooltips, live swap diff, rationale
  line) is unchanged — it just renders the selected build.
- A god with no Joust note (shouldn't happen after regen, but defensively)
  shows "No Joust data yet" rather than an empty panel.

Types: `BuildEntry.archetype` widened to the flavor union; the viewer groups
`builds` (now up to 2 notes per god) by `mode` and filters by the toggle.

## Testing approach

- **Python**: `eligible_flavors` returns the right subset per god archetype
  (physical basic-attack → includes crit; mage → excludes crit; all → bruiser/
  anti-tank). A flavor overlay changes the produced core vs. the flavor-less
  core on a fixture god (e.g. crit flavor pulls crit items up). Joust profile
  zeroes win/pick and applies tag bonuses (a sustain item outranks a
  same-efficiency non-sustain item under the Joust profile but not Conquest).
  `recommend` writes both `<god>-Conquest.md` and `<god>-Joust.md` with core +
  eligible flavors, idempotently.
- **Viewer (vitest/RTL)**: mode toggle switches the rendered build set; flavor
  tabs render by archetype label; selecting a Joust build shows its label/
  rationale; a mode with no note shows the empty state.
- **Manual**: regen, open the app, toggle Conquest/Joust, click each flavor tab,
  confirm builds differ sensibly and only god-appropriate flavors appear.

## Limitations (stated)

- Flavor and Joust builds are calibrated opinion, not meta-proven — labeled.
- Joust has **no meta win/pick backing**; it's efficiency + fit + a hand-tuned
  profile. If a real Joust data source appears later, it can slot into the
  `joust` profile's signals.
- Flavor identity is bounded by the current item pool (still no boots/anti-heal
  items scraped) — a flavor can only pick from what exists; gaps are reported
  the same honest way (e.g. anti-tank leans on penetration stats since no
  protection-shred items are tagged yet).
- Still archetype-based, not ability-damage simulation (the standing ceiling).

## Open questions — resolved during design

- Flavor set → crit, burst, bruiser, anti-tank; gated per god by damage type +
  role, defined tunably in `_weights.yaml`.
- Joust data → none available; encode a tunable mode profile (drop win/pick,
  boost sustain/anti-heal/aura, penalize wave-clear/mobility), labeled.
- Multiple builds per mode → `suggested` entries labeled by `archetype`;
  build notes split per mode; viewer gets a mode toggle + flavor tabs.
- Viewer layout → mode segmented toggle + wrapping flavor tab row (mockup
  approved).
