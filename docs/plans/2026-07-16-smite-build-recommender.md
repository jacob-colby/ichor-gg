# SMITE 2 Build Recommender Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a signal-weighted item-scoring and build-assembly layer on top of the existing SMITE 2 pipeline that flags underrated items and emits suggested builds per god.

**Architecture:** Three new pure-computation modules under `tools/smite/` (`efficiency.py`, `scoring.py`, `assemble.py`) orchestrated by a `recommend.py` CLI that runs after `refresh.py` and consumes the local god/item/build notes plus two user-owned config sidecars (`_weights.yaml`, `_tags.yaml`). Layer 1 derives gold-value-per-stat empirically via NNLS regression (residual = underrated detector); Layer 2 applies hand-correctable effect-tags; Layer 3 applies archetype-based god-fit; a transparent weighted sum combines four signals. Outputs suggested build entries into the vault Build notes (flow to the viewer) plus per-god analysis reports.

**Tech Stack:** Python 3.10, numpy 2.2, scipy 1.15 (`scipy.optimize.nnls`), PyYAML, pytest. Viewer: existing Vite + React 19 + TS + Tailwind v4 + Vitest.

**Reference spec:** [2026-07-16-smite-build-recommender-design.md](../specs/2026-07-16-smite-build-recommender-design.md)

---

## File Structure

**New Python modules (`tools/smite/`):**
- `efficiency.py` — stat-value parsing, NNLS gold-value regression, residual → efficiency score + tier.
- `scoring.py` — config loaders, damage-type filter, god-fit, four-signal weighted score, underrated flag.
- `assemble.py` — scored items → named builds + situational-swap table under hard constraints.
- `recommend.py` — CLI orchestrator; grows across phases (A: efficiency report → B: per-god scoring report → C: write suggested builds).

**New tests (`tools/smite/tests/`):** `test_efficiency.py`, `test_scoring.py`, `test_assemble.py`, plus additions to `test_notes.py`.

**New config (`04. System/Data/SMITE/`):** `_weights.yaml`, `_tags.yaml` — user-owned, committed, refresh-safe sidecars.

**New output (`04. System/Data/SMITE/Analysis/`):** `<god>.md` generated reports.

**Modified:**
- `tools/smite/notes.py` — add `merge_suggested_entries` (replace-in-place for `source: suggested`, preserving `mine`/`community`).
- `viewer/src/types.ts` — extend `CuratedBuildEntry.source` union with `"suggested"`, add optional `archetype`/`rationale`.
- `viewer/src/components/DetailPanel.tsx` — render a `suggested` entry's rationale line.

**NOT modified:** `build_index.py` already reads whole Build-note frontmatter, so `suggested` entries flow into `index.json` with zero changes — a Phase C step verifies this rather than editing it.

---

## PHASE A — Efficiency engine (ships and is verifiable alone)

### Task A1: Stat-value parsing

**Files:**
- Create: `tools/smite/efficiency.py`
- Test: `tools/smite/tests/test_efficiency.py`

Real item `stats` values are strings, sometimes `%`-suffixed (`'45'`, `20%`, `'10'`), sometimes absent. Parsing must coerce to float and drop non-numeric.

- [ ] **Step 1: Write the failing test**

```python
# tools/smite/tests/test_efficiency.py
from smite import efficiency


def test_parse_stat_value_plain_number():
    assert efficiency.parse_stat_value("45") == 45.0


def test_parse_stat_value_percent_suffix():
    assert efficiency.parse_stat_value("20%") == 20.0


def test_parse_stat_value_whitespace():
    assert efficiency.parse_stat_value(" 10 ") == 10.0


def test_parse_stat_value_none_returns_none():
    assert efficiency.parse_stat_value(None) is None


def test_parse_stat_value_non_numeric_returns_none():
    assert efficiency.parse_stat_value("Aura") is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_efficiency.py -v`
Expected: FAIL with "module 'smite.efficiency' has no attribute 'parse_stat_value'" (or ImportError)

- [ ] **Step 3: Write minimal implementation**

```python
# tools/smite/efficiency.py
"""Empirical gold-efficiency scoring for SMITE 2 items.

Derives the marginal gold value the game assigns each stat by non-negative
least-squares regression of item cost onto item stats across the whole item
set, then scores each item by the residual between its actual cost and the
cost its raw stats predict. A negative residual (cheaper than predicted) is an
undervalued stat-stick; a large positive residual means you're paying a premium
for a passive — whether that premium is worth it is decided by the effect-tag
layer, not here. See the design spec for the full rationale.
"""


def parse_stat_value(raw):
    """Coerce a raw stats-dict value ('45', '20%', ' 10 ') to float, or None
    if absent/non-numeric. Stat values arrive as strings from YAML, some with
    a trailing % (Critical Chance, Cooldown Rate)."""
    if raw is None:
        return None
    try:
        return float(str(raw).strip().rstrip("%").strip())
    except ValueError:
        return None
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_efficiency.py -v`
Expected: PASS (5 passed)

- [ ] **Step 5: Commit**

```bash
git add tools/smite/efficiency.py tools/smite/tests/test_efficiency.py
git commit -m "feat(smite): parse_stat_value for efficiency engine"
```

---

### Task A2: NNLS gold-value regression

**Files:**
- Modify: `tools/smite/efficiency.py`
- Test: `tools/smite/tests/test_efficiency.py`

- [ ] **Step 1: Write the failing test**

The regression must recover planted gold values from a synthetic item set with known linear structure. Build items whose cost is exactly a known linear combination of stats; assert the fit recovers those coefficients.

```python
# append to tools/smite/tests/test_efficiency.py
import pytest


def _item(name, cost, **stats):
    return {"name": name, "cost": cost, "stats": {k: str(v) for k, v in stats.items()}}


def test_fit_gold_values_recovers_planted_coefficients():
    # cost = 20*Strength + 30*Intelligence exactly, no intercept.
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 3000, Intelligence=100),
        _item("C", 2600, Strength=40, Intelligence=60),
        _item("D", 1000, Strength=50),
        _item("E", 1500, Intelligence=50),
    ]
    gold, stat_names = efficiency.fit_gold_values(items)
    assert gold["Strength"] == pytest.approx(20.0, abs=0.5)
    assert gold["Intelligence"] == pytest.approx(30.0, abs=0.5)
    assert set(stat_names) == {"Strength", "Intelligence"}


def test_fit_gold_values_coefficients_never_negative():
    items = [
        _item("A", 100, Strength=50, Intelligence=50),
        _item("B", 100, Strength=50, Intelligence=10),
        _item("C", 100, Strength=10, Intelligence=50),
    ]
    gold, _ = efficiency.fit_gold_values(items)
    assert all(v >= 0 for v in gold.values())
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_efficiency.py -k fit_gold -v`
Expected: FAIL (no attribute `fit_gold_values`)

- [ ] **Step 3: Write minimal implementation**

```python
# append to tools/smite/efficiency.py
import numpy as np
from scipy.optimize import nnls

INTERCEPT_KEY = "_intercept"


def collect_stat_names(items):
    """Every distinct stat that parses to a number somewhere in the item set,
    sorted for deterministic column order."""
    names = set()
    for item in items:
        for stat, raw in (item.get("stats") or {}).items():
            if parse_stat_value(raw) is not None:
                names.add(stat)
    return sorted(names)


def _stat_matrix(items, stat_names):
    """Rows = items, columns = stat_names then a trailing all-ones intercept
    column. Absent/non-numeric stats are 0."""
    rows, costs = [], []
    for item in items:
        stats = item.get("stats") or {}
        row = [parse_stat_value(stats.get(s)) or 0.0 for s in stat_names]
        row.append(1.0)  # intercept
        rows.append(row)
        costs.append(float(item["cost"]))
    return np.array(rows, dtype=float), np.array(costs, dtype=float)


def fit_gold_values(items):
    """NNLS fit of cost onto stats. Returns (gold_values, stat_names) where
    gold_values maps each stat name (plus INTERCEPT_KEY) to its non-negative
    marginal gold value. Non-negative because a stat cannot rationally have a
    negative gold price; NNLS also tames collinear-stat coefficient blowups."""
    stat_names = collect_stat_names(items)
    A, b = _stat_matrix(items, stat_names)
    coef, _ = nnls(A, b)
    gold = {name: float(coef[i]) for i, name in enumerate(stat_names)}
    gold[INTERCEPT_KEY] = float(coef[-1])
    return gold, stat_names
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_efficiency.py -v`
Expected: PASS (7 passed)

- [ ] **Step 5: Commit**

```bash
git add tools/smite/efficiency.py tools/smite/tests/test_efficiency.py
git commit -m "feat(smite): NNLS gold-value regression"
```

---

### Task A3: Residual → efficiency score + tier

**Files:**
- Modify: `tools/smite/efficiency.py`
- Test: `tools/smite/tests/test_efficiency.py`

The efficiency score is a min-max normalization of the negative residual across the item set (cheaper-than-predicted → higher score, in [0, 1]); the tier (`undervalued`/`fair`/`premium`) is a human-readable label by residual z-score. The continuous score — not the discrete tier — feeds the aggregator, a deliberate refinement of the spec's "tier drives scoring" that avoids discretization cliffs; tiers remain the report's label.

- [ ] **Step 1: Write the failing test**

```python
# append to tools/smite/tests/test_efficiency.py
def test_efficiency_scores_flags_underpriced_as_undervalued():
    # F is a Strength stat-stick priced far below the ~20 gold/Strength the
    # rest of the set implies; it should land in the undervalued tier and score
    # higher than an on-curve item.
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 2000, Strength=100),
        _item("C", 2000, Strength=100),
        _item("Fair", 2000, Strength=100),
        _item("Underpriced", 1000, Strength=100),
    ]
    scores, _gold = efficiency.efficiency_scores(items)
    assert scores["Underpriced"]["tier"] == "undervalued"
    assert scores["Underpriced"]["score"] > scores["Fair"]["score"]


def test_efficiency_scores_flags_passive_heavy_as_premium():
    # A costly item carrying almost no raw stats (its price is in its passive)
    # has a large positive residual → premium tier, low efficiency score.
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 2000, Strength=100),
        _item("C", 2000, Strength=100),
        _item("D", 2000, Strength=100),
        _item("PassiveHeavy", 3000, Strength=5),
    ]
    scores, _ = efficiency.efficiency_scores(items)
    assert scores["PassiveHeavy"]["tier"] == "premium"
    assert scores["PassiveHeavy"]["score"] < 0.5


def test_efficiency_scores_returns_score_in_unit_range():
    items = [_item("A", 2000, Strength=100), _item("B", 1000, Strength=100)]
    scores, _ = efficiency.efficiency_scores(items)
    for s in scores.values():
        assert 0.0 <= s["score"] <= 1.0
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_efficiency.py -k efficiency_scores -v`
Expected: FAIL (no attribute `efficiency_scores`)

- [ ] **Step 3: Write minimal implementation**

```python
# append to tools/smite/efficiency.py
def predicted_cost(item, gold_values):
    total = gold_values.get(INTERCEPT_KEY, 0.0)
    for stat, raw in (item.get("stats") or {}).items():
        val = parse_stat_value(raw)
        if val is not None:
            total += val * gold_values.get(stat, 0.0)
    return total


def efficiency_scores(items):
    """Returns (scores, gold_values). scores maps item name → dict with:
      residual  actual_cost - predicted_cost (negative => undervalued)
      z         residual z-score across the set
      score     min-max normalized -residual in [0,1] (higher => better value)
      tier      'undervalued' | 'fair' | 'premium' by z threshold
    The continuous `score` is what the aggregator consumes; `tier` is the
    report label."""
    gold, _ = fit_gold_values(items)
    residuals = {it["name"]: it["cost"] - predicted_cost(it, gold) for it in items}
    vals = np.array(list(residuals.values()), dtype=float)
    mean = float(vals.mean())
    std = float(vals.std()) or 1.0
    lo, hi = float(vals.min()), float(vals.max())
    span = (hi - lo) or 1.0

    scores = {}
    for name, resid in residuals.items():
        z = (resid - mean) / std
        score = (hi - resid) / span  # cheapest-relative → 1.0, most-premium → 0.0
        tier = "undervalued" if z <= -0.5 else "premium" if z >= 0.5 else "fair"
        scores[name] = {"residual": resid, "z": z, "score": score, "tier": tier}
    return scores, gold
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_efficiency.py -v`
Expected: PASS (10 passed)

- [ ] **Step 5: Commit**

```bash
git add tools/smite/efficiency.py tools/smite/tests/test_efficiency.py
git commit -m "feat(smite): residual-based efficiency score + tier"
```

---

### Task A4: `recommend.py` efficiency report CLI

**Files:**
- Create: `tools/smite/recommend.py`
- Test: `tools/smite/tests/test_recommend.py`

Phase-A CLI: load all item notes, compute efficiency, write a god-agnostic efficiency report. Verifiable on real data.

- [ ] **Step 1: Write the failing test**

```python
# tools/smite/tests/test_recommend.py
from smite import recommend


def test_efficiency_report_ranks_undervalued_first():
    items = [
        {"name": "OnCurve", "cost": 2000, "stats": {"Strength": "100"}},
        {"name": "OnCurve2", "cost": 2000, "stats": {"Strength": "100"}},
        {"name": "OnCurve3", "cost": 2000, "stats": {"Strength": "100"}},
        {"name": "Bargain", "cost": 1000, "stats": {"Strength": "100"}},
    ]
    report = recommend.efficiency_report(items)
    assert "Bargain" in report
    assert "undervalued" in report
    # Bargain's row appears before the on-curve rows (sorted best value first).
    assert report.index("Bargain") < report.index("OnCurve3")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -v`
Expected: FAIL (no attribute `efficiency_report`)

- [ ] **Step 3: Write minimal implementation**

```python
# tools/smite/recommend.py
"""CLI: score SMITE 2 items and (later phases) assemble suggested builds.
Runs offline over local notes — no network. Run after refresh.py.

Phase A: `python -m smite.recommend --efficiency-report` writes a god-agnostic
item efficiency table.
"""
import argparse
import sys
from pathlib import Path

from smite import efficiency, notes

VAULT_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = VAULT_ROOT / "04. System" / "Data" / "SMITE"


def load_items():
    items_dir = DATA_ROOT / "Items"
    out = []
    for path in sorted(items_dir.glob("*.md")):
        frontmatter, _ = notes.read_note(path)
        if frontmatter.get("name"):
            out.append(frontmatter)
    return out


def efficiency_report(items):
    scores, _gold = efficiency.efficiency_scores(items)
    ranked = sorted(items, key=lambda it: -scores[it["name"]]["score"])
    lines = ["# Item efficiency\n", "| Item | Cost | Tier | Residual | Score |", "|---|---|---|---|---|"]
    for it in ranked:
        s = scores[it["name"]]
        lines.append(f"| {it['name']} | {it['cost']} | {s['tier']} | {s['residual']:+.0f} | {s['score']:.2f} |")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Score SMITE 2 items and build suggestions")
    parser.add_argument("--efficiency-report", action="store_true",
                        help="write the god-agnostic item efficiency table")
    args = parser.parse_args(argv)

    if args.efficiency_report:
        items = load_items()
        out_dir = DATA_ROOT / "Analysis"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "_efficiency.md"
        out_path.write_text(efficiency_report(items), encoding="utf-8")
        print(f"Wrote {out_path}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run test to verify it passes, then dry-run on real data**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -v`
Expected: PASS

Run: `cd tools && python -m smite.recommend --efficiency-report`
Expected: writes `04. System/Data/SMITE/Analysis/_efficiency.md`. Open it and sanity-check: pure stat-sticks (e.g. Deathbringer, Devourer's Gauntlet) vs. passive/utility items land in plausible tiers. This is a judgment check, not an assertion — note anything that looks wrong for the reviewer.

- [ ] **Step 5: Commit**

```bash
git add tools/smite/recommend.py tools/smite/tests/test_recommend.py "04. System/Data/SMITE/Analysis/_efficiency.md"
git commit -m "feat(smite): recommend.py efficiency report (Phase A)"
```

---

## PHASE B — Judgment layers + scoring

### Task B1: Config loaders + default weights

**Files:**
- Create: `tools/smite/scoring.py`
- Create: `04. System/Data/SMITE/_weights.yaml`
- Test: `tools/smite/tests/test_scoring.py`

- [ ] **Step 1: Write the failing test**

```python
# tools/smite/tests/test_scoring.py
from smite import scoring


def test_load_weights_missing_file_returns_defaults(tmp_path):
    w = scoring.load_weights(tmp_path / "nope.yaml")
    assert w["signals"]["efficiency"] == 0.35
    assert w["signals"]["win"] == 0.30
    assert w["signals"]["pick"] == 0.15
    assert w["signals"]["fit"] == 0.20


def test_load_weights_file_overrides_defaults(tmp_path):
    p = tmp_path / "_weights.yaml"
    p.write_text("signals:\n  efficiency: 0.5\n", encoding="utf-8")
    w = scoring.load_weights(p)
    assert w["signals"]["efficiency"] == 0.5
    # unspecified keys fall back to defaults
    assert w["signals"]["win"] == 0.30


def test_load_tags_missing_file_returns_empty(tmp_path):
    assert scoring.load_tags(tmp_path / "nope.yaml") == {}


def test_load_tags_reads_mapping(tmp_path):
    p = tmp_path / "_tags.yaml"
    p.write_text("Brawler's Ruin:\n  - anti-heal\n", encoding="utf-8")
    assert scoring.load_tags(p) == {"Brawler's Ruin": ["anti-heal"]}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -v`
Expected: FAIL (no module `smite.scoring`)

- [ ] **Step 3: Write minimal implementation**

```python
# tools/smite/scoring.py
"""Four-signal weighted item scoring for a given god: efficiency (hard math)
+ win rate + pick rate + archetype god-fit. Transparent, tunable weights in
_weights.yaml; effect-tags in _tags.yaml. See the design spec."""
import copy

import yaml

from smite.efficiency import parse_stat_value

DEFAULT_WEIGHTS = {
    "signals": {"efficiency": 0.35, "win": 0.30, "pick": 0.15, "fit": 0.20},
    # role/specialization → {stat: weight}. Extend as new roles enter the pool;
    # unknown roles simply contribute nothing to fit (graceful).
    "role_stats": {
        "Sharpshooter": {"Attack Speed": 1.0, "Critical Chance": 1.0, "Strength": 0.6},
        "Nuker": {"Intelligence": 1.0, "Penetration": 1.0, "Cooldown Rate": 0.5},
        "Mage": {"Intelligence": 1.0, "Penetration": 0.8, "Cooldown Rate": 0.5},
        "Hunter": {"Strength": 1.0, "Attack Speed": 0.8, "Critical Chance": 0.6},
        "Carry": {"Strength": 0.8, "Attack Speed": 0.6, "Critical Chance": 0.6},
        "Assassin": {"Strength": 1.0, "Penetration": 0.8},
        "Warrior": {"Strength": 0.8, "Physical Protection": 0.5, "Health": 0.5},
        "Guardian": {"Physical Protection": 1.0, "Magical Protection": 1.0, "Health": 0.8},
    },
    "underrated": {"min_score": 0.6, "max_pick": 0.15},
}


def _deep_merge(base, override):
    out = copy.deepcopy(base)
    for k, v in (override or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def load_weights(path):
    if not path.exists():
        return copy.deepcopy(DEFAULT_WEIGHTS)
    override = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return _deep_merge(DEFAULT_WEIGHTS, override)


def load_tags(path):
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -v`
Expected: PASS

- [ ] **Step 5: Create the committed default `_weights.yaml` and commit**

Write `04. System/Data/SMITE/_weights.yaml` documenting the defaults so Jacob has a file to tune (values identical to `DEFAULT_WEIGHTS`):

```yaml
# Tuning surface for the build recommender. Edit and re-run
# `python -m smite.recommend --all`. Anything omitted falls back to the
# built-in defaults in tools/smite/scoring.py.
signals:
  efficiency: 0.35   # gold-value residual (hard math)
  win: 0.30          # SmiteBrain high-elo win rate (performance)
  pick: 0.15         # SmiteBrain pick rate (popularity)
  fit: 0.20          # archetype god-fit
underrated:
  min_score: 0.6     # flag items scoring at least this...
  max_pick: 0.15     # ...whose pick rate is at most this
```

```bash
git add tools/smite/scoring.py tools/smite/tests/test_scoring.py "04. System/Data/SMITE/_weights.yaml"
git commit -m "feat(smite): scoring config loaders + default weights"
```

---

### Task B2: Seed `_tags.yaml` from item passives

**Files:**
- Create: `04. System/Data/SMITE/_tags.yaml`

This is a content/judgment task, not code. Read every `04. System/Data/SMITE/Items/*.md` note's `passive` field and assign zero or more tags from the FIXED vocabulary below. Do not invent tags outside it. Items with a purely-statistical passive (e.g. "+35% Critical Strike Damage") may legitimately get **no** tags — that is correct, not an omission.

Fixed vocabulary (exactly these):
```
burst · execute · anti-heal · protection-shred · peel · wave-clear ·
mobility · sustain · cc-immunity · aura · anti-crit
```

Tag meanings for calibration:
- `burst` — bonus on-hit/ability damage spikes (procs, stacking damage).
- `execute` — bonus damage scaling with target's missing/low health.
- `anti-heal` — reduces enemy healing.
- `protection-shred` — reduces enemy protections (not flat penetration stat — a passive shred).
- `peel` — self/ally protective on-hit slows/roots/knockback for peeling.
- `wave-clear` — cleave / bonus vs. minions.
- `mobility` — movement speed steroids, dashes, leaps from the item.
- `sustain` — lifesteal/HP5/shielding from the passive (not just a lifesteal stat).
- `cc-immunity` — cleanse/CC-reduction/immunity actives or passives.
- `aura` — team-wide aura effects.
- `anti-crit` — reduces incoming crit.

- [ ] **Step 1: Read all item passives**

Run: `cd tools && python -c "from smite import recommend; [print(repr(i['name']), '::', i.get('passive','')) for i in recommend.load_items()]"`

- [ ] **Step 2: Write `04. System/Data/SMITE/_tags.yaml`**

One top-level key per item name, value a list of tags (or `[]`). Example shape:

```yaml
# Effect-tags for the build recommender. LLM-seeded, hand-correctable.
# Sidecar so item refresh never clobbers it. Vocabulary is fixed — see
# docs/superpowers/plans/2026-07-16-smite-build-recommender.md Task B2.
Deathbringer: []            # pure crit-damage stat passive, no tag
Titan's Bane: [protection-shred]
Soul Gem: [sustain, burst]
# ...one line per item in Items/
```

Cover every item currently in `Items/`. Leave a comment at the top noting the seeding date so staleness is visible.

- [ ] **Step 3: Commit**

```bash
git add "04. System/Data/SMITE/_tags.yaml"
git commit -m "chore(smite): seed effect-tags for tracked items"
```

---

### Task B3: Damage-type filter + god-fit

**Files:**
- Modify: `tools/smite/scoring.py`
- Test: `tools/smite/tests/test_scoring.py`

- [ ] **Step 1: Write the failing test**

```python
# append to tools/smite/tests/test_scoring.py
def _god(name, damage_type, role, specs):
    return {"name": name, "damage_type": damage_type, "role": role, "specializations": specs}


def test_item_damage_type_from_primary_stat():
    assert scoring.item_damage_type({"stats": {"Strength": "40"}}) == "physical"
    assert scoring.item_damage_type({"stats": {"Intelligence": "70"}}) == "magical"
    assert scoring.item_damage_type({"stats": {"Physical Protection": "50"}}) == "neutral"


def test_passes_damage_filter_excludes_mismatched_offense():
    phys_god = _god("Ullr", "physical", "Hunter", ["Hunter"])
    int_item = {"stats": {"Intelligence": "70"}}
    str_item = {"stats": {"Strength": "40"}}
    neutral_item = {"stats": {"Physical Protection": "50"}}
    assert scoring.passes_damage_filter(str_item, phys_god)
    assert not scoring.passes_damage_filter(int_item, phys_god)
    assert scoring.passes_damage_filter(neutral_item, phys_god)  # neutral always passes


def test_god_fit_rewards_role_relevant_stats():
    weights = scoring.load_weights_default()
    sharpshooter = _god("Chiron", "physical", "Carry", ["Sharpshooter"])
    crit_item = {"stats": {"Critical Chance": "20%", "Attack Speed": "15"}}
    off_stat_item = {"stats": {"Magical Protection": "50"}}
    assert scoring.god_fit_score(crit_item, sharpshooter, weights, []) > \
        scoring.god_fit_score(off_stat_item, sharpshooter, weights, [])
```

Note: this test references `scoring.load_weights_default()`; add it as a thin helper returning `copy.deepcopy(DEFAULT_WEIGHTS)` so tests don't need a path.

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -k "damage or god_fit" -v`
Expected: FAIL

- [ ] **Step 3: Write minimal implementation**

```python
# append to tools/smite/scoring.py
def load_weights_default():
    return copy.deepcopy(DEFAULT_WEIGHTS)


def item_damage_type(item):
    stats = item.get("stats") or {}
    has_str = "Strength" in stats
    has_int = "Intelligence" in stats
    if has_str and not has_int:
        return "physical"
    if has_int and not has_str:
        return "magical"
    return "neutral"


def passes_damage_filter(item, god):
    dt = item_damage_type(item)
    return dt == "neutral" or dt == god.get("damage_type")


def _role_stat_map(god, weights):
    merged = {}
    roles = list(god.get("specializations") or [])
    if god.get("role"):
        roles.append(god["role"])
    for role in roles:
        for stat, w in weights["role_stats"].get(role, {}).items():
            merged[stat] = max(merged.get(stat, 0.0), w)
    return merged


def god_fit_score(item, god, weights, item_tags):
    """Archetype fit in [0,1]: weighted presence of role-relevant stats, plus a
    small bonus for archetype-relevant tags. NOT damage simulation — see spec."""
    stats = item.get("stats") or {}
    role_map = _role_stat_map(god, weights)
    denom = sum(role_map.values()) or 1.0
    stat_fit = 0.0
    for stat, w in role_map.items():
        if parse_stat_value(stats.get(stat)) is not None:
            stat_fit += w
    stat_fit = min(stat_fit / denom, 1.0)

    # Small tag bonus for offense-oriented tags on damage roles. Conservative.
    offense_tags = {"burst", "execute", "protection-shred"}
    tag_bonus = 0.1 if any(t in offense_tags for t in (item_tags or [])) else 0.0
    return min(stat_fit + tag_bonus, 1.0)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tools/smite/scoring.py tools/smite/tests/test_scoring.py
git commit -m "feat(smite): damage-type filter + archetype god-fit"
```

---

### Task B4: Four-signal aggregation + underrated flag

**Files:**
- Modify: `tools/smite/scoring.py`
- Test: `tools/smite/tests/test_scoring.py`

- [ ] **Step 1: Write the failing test**

```python
# append to tools/smite/tests/test_scoring.py
def _community_build(*slots):
    # slots: (name, pick_rate, win_rate)
    return {"builds": [{"source": "community",
                        "slot_order": [{"name": n, "pick_rate": p, "win_rate": w}
                                       for (n, p, w) in slots]}]}


def test_lookup_rates_from_community_entry():
    build = _community_build(("Transcendence", 0.9, 0.55))
    assert scoring.lookup_rates(build, "Transcendence") == (0.9, 0.55)
    assert scoring.lookup_rates(build, "Missing") == (0.0, None)


def test_signal_score_combines_all_four_signals():
    weights = scoring.load_weights_default()
    god = _god("Chiron", "physical", "Carry", ["Sharpshooter"])
    item = {"name": "Deathbringer", "stats": {"Critical Chance": "20%", "Strength": "45"}}
    build = _community_build(("Deathbringer", 0.5, 0.6))
    row = scoring.signal_score(item, god, build, eff_score=0.8, weights=weights, item_tags=[])
    # total is the weighted sum of the four component sub-scores it reports
    w = weights["signals"]
    expected = (w["efficiency"] * row["efficiency"] + w["win"] * row["win"]
                + w["pick"] * row["pick"] + w["fit"] * row["fit"])
    assert row["total"] == pytest.approx(expected)
    assert row["pick"] == 0.5 and row["win"] == 0.6


def test_underrated_flag_fires_only_high_score_low_pick():
    weights = scoring.load_weights_default()  # min_score 0.6, max_pick 0.15
    assert scoring.is_underrated({"total": 0.7, "pick": 0.1}, weights)
    assert not scoring.is_underrated({"total": 0.7, "pick": 0.5}, weights)   # popular
    assert not scoring.is_underrated({"total": 0.3, "pick": 0.1}, weights)   # weak
```

Add `import pytest` at the top of the test file if not already present.

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -k "lookup or signal or underrated" -v`
Expected: FAIL

- [ ] **Step 3: Write minimal implementation**

```python
# append to tools/smite/scoring.py
def lookup_rates(god_build, item_name):
    """(pick_rate, win_rate) for item_name from the god's community build entry,
    or (0.0, None) if the item isn't in that build."""
    for entry in god_build.get("builds", []):
        if entry.get("source") == "community":
            for slot in entry.get("slot_order", []):
                if isinstance(slot, dict) and slot.get("name") == item_name:
                    return slot.get("pick_rate", 0.0), slot.get("win_rate")
    return 0.0, None


def signal_score(item, god, god_build, eff_score, weights, item_tags):
    w = weights["signals"]
    pick, win = lookup_rates(god_build, item["name"])
    win_norm = win if win is not None else 0.5   # neutral when unknown
    fit = god_fit_score(item, god, weights, item_tags)
    total = (w["efficiency"] * eff_score + w["win"] * win_norm
             + w["pick"] * pick + w["fit"] * fit)
    return {"item": item["name"], "efficiency": eff_score, "win": win_norm,
            "pick": pick, "fit": fit, "total": total, "tags": list(item_tags or [])}


def is_underrated(row, weights):
    u = weights["underrated"]
    return row["total"] >= u["min_score"] and row["pick"] <= u["max_pick"]


def score_god_items(god, items, god_build, efficiency_scores_map, weights, tags_map):
    """Score every damage-filter-passing item for one god, ranked by total."""
    rows = []
    for item in items:
        if not passes_damage_filter(item, god):
            continue
        eff = efficiency_scores_map.get(item["name"], {}).get("score", 0.5)
        row = signal_score(item, god, god_build, eff, weights, tags_map.get(item["name"], []))
        row["underrated"] = is_underrated(row, weights)
        row["tier"] = efficiency_scores_map.get(item["name"], {}).get("tier", "fair")
        rows.append(row)
    return sorted(rows, key=lambda r: -r["total"])
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tools/smite/scoring.py tools/smite/tests/test_scoring.py
git commit -m "feat(smite): four-signal aggregation + underrated flag"
```

---

### Task B5: Per-god scoring report in `recommend.py`

**Files:**
- Modify: `tools/smite/recommend.py`
- Test: `tools/smite/tests/test_recommend.py`

- [ ] **Step 1: Write the failing test**

```python
# append to tools/smite/tests/test_recommend.py
from smite import scoring


def test_god_report_marks_underrated_items():
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
           "specializations": ["Sharpshooter"]}
    items = [
        {"name": "Sleeper", "cost": 1000, "stats": {"Strength": "100", "Critical Chance": "20%"}},
        {"name": "Popular", "cost": 2600, "stats": {"Strength": "60"}},
        {"name": "Filler", "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "Filler2", "cost": 2500, "stats": {"Strength": "55"}},
    ]
    build = {"builds": [{"source": "community", "slot_order": [
        {"name": "Popular", "pick_rate": 0.8, "win_rate": 0.55}]}]}
    weights = scoring.load_weights_default()
    report = recommend.god_report(god, items, build, weights, tags_map={})
    assert "Chiron" in report
    # The cheap, high-fit, unpicked stat-stick should be flagged underrated.
    assert "Sleeper" in report
    assert "UNDERRATED" in report.upper()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -k god_report -v`
Expected: FAIL (no attribute `god_report`)

- [ ] **Step 3: Write minimal implementation**

```python
# add to tools/smite/recommend.py imports
from smite import efficiency, notes, scoring

# add helpers
WEIGHTS_PATH = DATA_ROOT / "_weights.yaml"
TAGS_PATH = DATA_ROOT / "_tags.yaml"
BUILDS_ROOT = VAULT_ROOT / "03. Workspaces" / "Gaming" / "SMITE 2" / "Builds"


def load_gods():
    out = []
    for path in sorted((DATA_ROOT / "Gods").glob("*.md")):
        fm, _ = notes.read_note(path)
        if fm.get("name"):
            out.append(fm)
    return out


def load_build_note(god_name, mode="Conquest"):
    fm, _ = notes.read_note(BUILDS_ROOT / f"{god_name}-{mode}.md")
    return fm or {"builds": []}


def god_report(god, items, god_build, weights, tags_map):
    eff_scores, _ = efficiency.efficiency_scores(items)
    rows = scoring.score_god_items(god, items, god_build, eff_scores, weights, tags_map)
    lines = [f"# {god['name']} — item scoring\n",
             "| Item | Total | Eff | Win | Pick | Fit | Tier | Tags | Flag |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        flag = "**UNDERRATED**" if r["underrated"] else ""
        tags = ", ".join(r["tags"])
        lines.append(f"| {r['item']} | {r['total']:.2f} | {r['efficiency']:.2f} | "
                     f"{r['win']:.2f} | {r['pick']:.2f} | {r['fit']:.2f} | {r['tier']} | "
                     f"{tags} | {flag} |")
    return "\n".join(lines) + "\n"
```

Extend `main()` with an `--all` branch (report for every god). Untagged-item reporting: after loading tags, print names of items absent from `tags_map` so missing tags are visible.

```python
    # in main(), add:
    parser.add_argument("--all", action="store_true",
                        help="write a per-god scoring report for every god")
    # ...
    if args.all:
        items = load_items()
        weights = scoring.load_weights(WEIGHTS_PATH)
        tags_map = scoring.load_tags(TAGS_PATH)
        untagged = [it["name"] for it in items if it["name"] not in tags_map]
        if untagged:
            print(f"[tags] {len(untagged)} untagged items: {', '.join(sorted(untagged))}")
        out_dir = DATA_ROOT / "Analysis"
        out_dir.mkdir(parents=True, exist_ok=True)
        for god in load_gods():
            build = load_build_note(god["name"])
            (out_dir / f"{god['name']}.md").write_text(
                god_report(god, items, build, weights, tags_map), encoding="utf-8")
        print("Wrote per-god scoring reports")
        return 0
```

- [ ] **Step 4: Run test to verify it passes, then dry-run**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -v`
Expected: PASS

Run: `cd tools && python -m smite.recommend --all`
Expected: writes `Analysis/<god>.md` for all 10 gods; prints any untagged items. Spot-check Chiron's report against intuition — note anything off for the reviewer.

- [ ] **Step 5: Commit**

```bash
git add tools/smite/recommend.py tools/smite/tests/test_recommend.py "04. System/Data/SMITE/Analysis/"
git commit -m "feat(smite): per-god scoring report (Phase B)"
```

---

## PHASE C — Assembly + write + viewer

### Task C1: Build assembly under constraints

**Files:**
- Create: `tools/smite/assemble.py`
- Test: `tools/smite/tests/test_assemble.py`

The assembler takes scored rows (from `score_god_items`) plus an `items_by_name` map (for stat-based category checks) and produces core build + situational swaps. `vs_tag` values MUST match the viewer's existing taxonomy so chip-highlighting works: `heavy_cc`, `magic_heavy`, `physical_heavy`, `sustain`.

- [ ] **Step 1: Write the failing test**

```python
# tools/smite/tests/test_assemble.py
from smite import assemble


def _row(name, total, tags=None):
    return {"item": name, "total": total, "tags": tags or [], "pick": 0.0}


def _items_by_name(*items):
    return {it["name"]: it for it in items}


def test_assemble_core_respects_constraints():
    rows = [_row("A", 0.9), _row("Boots1", 0.85), _row("Boots2", 0.84),
            _row("B", 0.8), _row("C", 0.7), _row("D", 0.6), _row("E", 0.5),
            _row("F", 0.4)]
    ibn = _items_by_name(
        {"name": "Boots1", "stats": {"Movement Speed": "18"}},
        {"name": "Boots2", "stats": {"Movement Speed": "18"}},
        {"name": "A", "stats": {"Strength": "40"}},
        {"name": "B", "stats": {"Strength": "40"}},
        {"name": "C", "stats": {"Strength": "40"}},
        {"name": "D", "stats": {"Strength": "40"}},
        {"name": "E", "stats": {"Strength": "40"}},
        {"name": "F", "stats": {"Strength": "40"}},
    )
    core = assemble.assemble_core(rows, ibn, n=6)
    assert len(core) == 6
    assert len(set(core)) == 6                       # no duplicates
    assert sum(1 for x in core if x.startswith("Boots")) == 1   # exactly one boots
    assert core[0] == "A"                            # highest score first


def test_situational_table_reports_missing_tag():
    rows = [_row("A", 0.9), _row("B", 0.8)]
    ibn = _items_by_name(
        {"name": "A", "stats": {"Strength": "40"}},
        {"name": "B", "stats": {"Strength": "40"}},
    )
    table = assemble.situational_swaps(rows, ibn, tags_map={})
    sustain_row = next(r for r in table if r["vs_tag"] == "sustain")
    assert "no anti-heal" in sustain_row["swap"].lower()


def test_situational_table_picks_tagged_item():
    rows = [_row("A", 0.9), _row("Antiheal", 0.5, tags=["anti-heal"])]
    ibn = _items_by_name(
        {"name": "A", "stats": {"Strength": "40"}},
        {"name": "Antiheal", "stats": {"Strength": "30"}},
    )
    table = assemble.situational_swaps(rows, ibn, tags_map={"Antiheal": ["anti-heal"]})
    sustain_row = next(r for r in table if r["vs_tag"] == "sustain")
    assert "Antiheal" in sustain_row["swap"]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_assemble.py -v`
Expected: FAIL (no module `smite.assemble`)

- [ ] **Step 3: Write minimal implementation**

```python
# tools/smite/assemble.py
"""Turn scored item rows into a suggested build: a constrained core plus a
situational-swap table. Greedy-with-rules, not optimization — transparent and
debuggable. vs_tag values match the viewer's archetype taxonomy so the existing
chip-highlighting works unchanged."""
from smite.efficiency import parse_stat_value


def _is_boots(item):
    return "Movement Speed" in (item.get("stats") or {})


def _is_lifesteal(item, tags):
    stats = item.get("stats") or {}
    return "sustain" in (tags or []) or any("Lifesteal" in s for s in stats)


def assemble_core(rows, items_by_name, n=6, bruiser=False):
    """Highest-total items filling n slots: exactly one boots, at most one
    lifesteal (unless bruiser), no duplicates. rows must be pre-sorted by
    -total (score_god_items already does)."""
    core, used = [], set()
    have_boots = have_lifesteal = False
    for r in rows:
        if len(core) >= n:
            break
        name = r["item"]
        if name in used:
            continue
        item = items_by_name.get(name, {})
        if _is_boots(item):
            if have_boots:
                continue
            have_boots = True
        if _is_lifesteal(item, r.get("tags")) and have_lifesteal and not bruiser:
            continue
        if _is_lifesteal(item, r.get("tags")):
            have_lifesteal = True
        core.append(name)
        used.add(name)
    return core


# (vs_tag, needed_tag, protection_stat, human label). protection_stat is used
# instead of a tag for the burst situations (protections are a stat, not a
# passive effect).
_SITUATIONS = [
    ("heavy_cc", "cc-immunity", None, "CC-immunity / cleanse"),
    ("magic_heavy", None, "Magical Protection", "magical protection"),
    ("physical_heavy", None, "Physical Protection", "physical protection"),
    ("sustain", "anti-heal", None, "anti-heal"),
]


def situational_swaps(rows, items_by_name, tags_map):
    table = []
    for vs_tag, needed_tag, prot_stat, label in _SITUATIONS:
        pick = None
        for r in rows:
            item = items_by_name.get(r["item"], {})
            item_tags = tags_map.get(r["item"], r.get("tags") or [])
            if needed_tag and needed_tag in item_tags:
                pick = r["item"]
                break
            if prot_stat and parse_stat_value((item.get("stats") or {}).get(prot_stat)) is not None:
                pick = r["item"]
                break
        if pick:
            table.append({"vs_tag": vs_tag, "swap": f"{pick} — {label}"})
        else:
            table.append({"vs_tag": vs_tag, "swap": f"(no {label} available in pool)"})
    return table
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_assemble.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tools/smite/assemble.py tools/smite/tests/test_assemble.py
git commit -m "feat(smite): build assembly under constraints"
```

---

### Task C2: `merge_suggested_entries` in notes.py

**Files:**
- Modify: `tools/smite/notes.py`
- Test: `tools/smite/tests/test_notes.py`

- [ ] **Step 1: Write the failing test**

```python
# append to tools/smite/tests/test_notes.py
def test_merge_suggested_entries_replaces_only_suggested(tmp_path):
    path = tmp_path / "Chiron-Conquest.md"
    notes.write_note(path, {
        "type": "smite-build", "god": "Chiron", "mode": "Conquest",
        "builds": [
            {"source": "community", "slot_order": [{"name": "Trans", "pick_rate": 0.9, "win_rate": 0.5}]},
            {"source": "mine", "slot_order": ["Deathbringer"]},
            {"source": "suggested", "archetype": "core", "slot_order": ["OLD"]},
        ],
    }, "")

    notes.merge_suggested_entries(path, "Chiron", "Conquest", [
        {"source": "suggested", "archetype": "core", "slot_order": ["NEW"]},
    ])

    fm, _ = notes.read_note(path)
    sources = [b["source"] for b in fm["builds"]]
    assert sources.count("community") == 1
    assert sources.count("mine") == 1
    assert sources.count("suggested") == 1
    suggested = next(b for b in fm["builds"] if b["source"] == "suggested")
    assert suggested["slot_order"] == ["NEW"]      # regenerated in place
    mine = next(b for b in fm["builds"] if b["source"] == "mine")
    assert mine["slot_order"] == ["Deathbringer"]  # untouched


def test_merge_suggested_entries_creates_note_when_missing(tmp_path):
    path = tmp_path / "New-Conquest.md"
    notes.merge_suggested_entries(path, "New", "Conquest",
                                  [{"source": "suggested", "slot_order": ["X"]}])
    fm, _ = notes.read_note(path)
    assert fm["god"] == "New"
    assert [b["source"] for b in fm["builds"]] == ["suggested"]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_notes.py -k suggested -v`
Expected: FAIL (no attribute `merge_suggested_entries`)

- [ ] **Step 3: Write minimal implementation**

```python
# append to tools/smite/notes.py
def merge_suggested_entries(path: Path, god: str, mode: str, suggested_entries: list) -> None:
    """Replace all `source: suggested` entries in a Build note with the supplied
    list, preserving community/mine/pro entries verbatim. Mirrors
    merge_build_note's community replacement — only the recommender's own
    entries are regenerated, everything hand-owned survives."""
    frontmatter, body = read_note(path)
    if not frontmatter:
        frontmatter = {"type": "smite-build", "god": god, "mode": mode, "builds": []}
    kept = [b for b in frontmatter.get("builds", []) if b.get("source") != "suggested"]
    frontmatter["builds"] = kept + list(suggested_entries)
    write_note(path, frontmatter, body)
```

- [ ] **Step 4: Run test to verify it passes, and confirm no regression**

Run: `cd tools && python -m pytest smite/tests/test_notes.py -v`
Expected: PASS (all existing + 2 new)

- [ ] **Step 5: Commit**

```bash
git add tools/smite/notes.py tools/smite/tests/test_notes.py
git commit -m "feat(smite): merge_suggested_entries preserves hand-owned builds"
```

---

### Task C3: Wire assembly into `recommend.py --all`

**Files:**
- Modify: `tools/smite/recommend.py`
- Test: `tools/smite/tests/test_recommend.py`

- [ ] **Step 1: Write the failing test**

```python
# append to tools/smite/tests/test_recommend.py
def test_build_suggested_entries_shape():
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
           "specializations": ["Sharpshooter"]}
    items = [
        {"name": "A", "cost": 2000, "stats": {"Strength": "40", "Critical Chance": "20%"}},
        {"name": "Boots", "cost": 1200, "stats": {"Movement Speed": "18"}},
        {"name": "C", "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "D", "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "E", "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "F", "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "G", "cost": 2500, "stats": {"Strength": "55"}},
    ]
    build = {"builds": [{"source": "community", "slot_order": []}]}
    weights = scoring.load_weights_default()
    entries = recommend.build_suggested_entries(god, items, build, weights, tags_map={})
    assert entries and entries[0]["source"] == "suggested"
    assert entries[0]["archetype"] == "core"
    assert isinstance(entries[0]["slot_order"], list) and entries[0]["slot_order"]
    assert "rationale" in entries[0]
    # situational table uses viewer-compatible vs_tags
    tags = {s["vs_tag"] for s in entries[0]["situational_swaps"]}
    assert {"heavy_cc", "magic_heavy", "physical_heavy", "sustain"} <= tags
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -k build_suggested -v`
Expected: FAIL

- [ ] **Step 3: Write minimal implementation**

```python
# add to recommend.py imports: from smite import assemble
from smite import assemble, efficiency, notes, scoring


def build_suggested_entries(god, items, god_build, weights, tags_map):
    eff_scores, _ = efficiency.efficiency_scores(items)
    rows = scoring.score_god_items(god, items, god_build, eff_scores, weights, tags_map)
    items_by_name = {it["name"]: it for it in items}
    core = assemble.assemble_core(rows, items_by_name, n=6)
    swaps = assemble.situational_swaps(rows, items_by_name, tags_map)
    underrated = [r["item"] for r in rows if r.get("underrated")]
    rationale = "Top weighted-score core (efficiency + win/pick + fit)."
    if underrated:
        rationale += " Underrated for this god: " + ", ".join(underrated) + "."
    return [{
        "source": "suggested",
        "archetype": "core",
        "slot_order": core,
        "situational_swaps": swaps,
        "rationale": rationale,
    }]
```

Then extend the `--all` branch to also write suggested entries (guarded by a `--report-only` flag that skips writing):

```python
    parser.add_argument("--report-only", action="store_true",
                        help="write reports but do not modify Build notes")
    # ...in the --all branch, after writing each god's report:
        if not args.report_only:
            entries = build_suggested_entries(god, items, build, weights, tags_map)
            notes.merge_suggested_entries(
                BUILDS_ROOT / f"{god['name']}-Conquest.md", god["name"], "Conquest", entries)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tools/smite/recommend.py tools/smite/tests/test_recommend.py
git commit -m "feat(smite): assemble + write suggested build entries"
```

---

### Task C4: Viewer `suggested` support

**Files:**
- Modify: `viewer/src/types.ts`
- Modify: `viewer/src/components/DetailPanel.tsx`
- Test: `viewer/src/components/DetailPanel.test.tsx` (add a case)

- [ ] **Step 1: Write the failing test**

Add a test asserting a `suggested` entry renders a tab and its rationale. Match the existing test file's render/setup style (check the top of `DetailPanel.test.tsx` for the render helper and fixture shape before writing).

```tsx
// append a test to viewer/src/components/DetailPanel.test.tsx
it("renders a suggested build's rationale", () => {
  const builds = [{
    type: "smite-build", god: "Chiron", mode: "Conquest",
    builds: [{
      source: "suggested", archetype: "core",
      slot_order: ["Deathbringer"],
      situational_swaps: [{ vs_tag: "sustain", swap: "Brawler's — anti-heal" }],
      rationale: "Top weighted-score core.",
    }],
  }];
  render(<DetailPanel god="Chiron" builds={builds as any} />);
  expect(screen.getByText(/Top weighted-score core/)).toBeInTheDocument();
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd viewer && npx vitest run src/components/DetailPanel.test.tsx`
Expected: FAIL (rationale not rendered)

- [ ] **Step 3: Write minimal implementation**

In `types.ts`, extend the curated entry:

```typescript
export interface CuratedBuildEntry {
  source: "pro" | "mine" | "suggested";
  aspect?: string;
  archetype?: string;
  rationale?: string;
  slot_order: string[];
  situational_swaps?: SituationalSwap[];
  notes?: string;
}
```

In `DetailPanel.tsx`, render `rationale` when present (below the slot order, before/around the swaps block). Minimal addition — the source tab already displays `entry.source`, so the `suggested` tab appears automatically:

```tsx
{!community && active.rationale && (
  <p className="mt-2 text-xs italic text-neutral-400">{active.rationale}</p>
)}
```

Guard: `active.rationale` is only on curated entries — access under the existing `!community` narrowing.

- [ ] **Step 4: Run tests (viewer suite) to verify pass**

Run: `cd viewer && npx vitest run`
Expected: PASS (all existing + new)

- [ ] **Step 5: Commit**

```bash
git add viewer/src/types.ts viewer/src/components/DetailPanel.tsx viewer/src/components/DetailPanel.test.tsx
git commit -m "feat(viewer): render suggested build rationale"
```

---

### Task C5: Full live run + index + manual verification

**Files:**
- Modify (generated): Build notes, `viewer/public/index.json`, `Analysis/*.md`

- [ ] **Step 1: Full Python + viewer test suites green**

Run: `cd tools && python -m pytest smite/tests/ -q -m "not live"`
Expected: all pass (59 prior + new).

Run: `cd viewer && npx vitest run`
Expected: all pass.

- [ ] **Step 2: Real end-to-end recommender run**

Run: `cd tools && python -m smite.recommend --all`
Expected: per-god reports written; suggested entries merged into all 10 Build notes; any untagged items printed.

- [ ] **Step 3: Rebuild the viewer index and confirm suggested flows through**

Run: `cd tools && python -m smite.build_index`
Run: `cd .. && python3 -c "import json; d=json.load(open('viewer/public/index.json',encoding='utf-8')); print([[b['source'] for b in n['builds']] for n in d['builds']])"`
Expected: every god's build list now includes a `suggested` entry alongside `community`.

- [ ] **Step 4: Manual spot-check**

Verify a Build note (e.g. `Chiron-Conquest.md`): the `mine`/`community` entries are intact and a `suggested` entry was added with a sane core (one boots, no dupes, damage-type-correct), a situational table with the four `vs_tag`s, and a rationale. Read `Analysis/Chiron.md` and sanity-check the underrated flags. Note anything that looks wrong rather than asserting — this is the human judgment gate before merge.

- [ ] **Step 5: Commit generated output**

```bash
git add "03. Workspaces/Gaming/SMITE 2/Builds/" "04. System/Data/SMITE/Analysis/" viewer/public/
git commit -m "chore(smite): first recommender pass — suggested builds for 10 gods"
```

---

## Self-Review

**Spec coverage:** Layer 1 efficiency (A1–A3), Layer 2 tags (B1–B2), Layer 3 god-fit (B3), four-signal aggregation + underrated (B4), build assembly + situational table (C1), suggested-entry write with hand-owned preservation (C2–C3), analysis reports (A4/B5), viewer integration (C4), live verification (C5). Config sidecars (B1–B2). Phasing A/B/C matches spec. All spec sections map to tasks.

**Placeholder scan:** No TBD/TODO. Every code step has complete code; the one content task (B2) gives the full fixed vocabulary + rules + example shape rather than "tag the items."

**Type/name consistency:** `efficiency.efficiency_scores` returns `(scores, gold)` used consistently (A3, B5, C3). `scoring.score_god_items(god, items, god_build, efficiency_scores_map, weights, tags_map)` signature matches its callers in B5/C3. `assemble.assemble_core(rows, items_by_name, n)` and `situational_swaps(rows, items_by_name, tags_map)` match C3 calls. `vs_tag` values (`heavy_cc`, `magic_heavy`, `physical_heavy`, `sustain`) match the viewer's existing `ARCHETYPE_TAGS`. `merge_suggested_entries(path, god, mode, entries)` matches C3's call. `load_weights_default()` added in B3, used in B4/C3 tests.

**Note on a deliberate spec refinement:** scoring consumes the continuous `score` (normalized -residual), with `tier` as the report label — a faithful refinement of the spec's "tier drives scoring" that avoids discretization cliffs. Called out in Task A3.
