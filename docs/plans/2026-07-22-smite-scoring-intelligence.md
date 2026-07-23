# SMITE Scoring Intelligence Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the broken god-fit signal (kit-aware, vocabulary-complete), calibrate signal weights against the validation metric, add disagreement tooling, ship labeled fun off-class builds, and surface score explanations in the viewer.

**Architecture:** All scoring work happens in `tools/smite/` (pure-Python, offline over existing notes); new modules `kit.py`, `analysis.py`, `calibrate.py` sit beside `scoring.py`. Suggested-build notes gain `slot_scores` + `fun` fields stamped by `recommend.py` (files are the message bus); the viewer reads them from `index.json`. Every scoring change is gated on `python -m smite.validate` (baseline: **coverage 60% · win-weighted 62% · Spearman 0.26, n=54**).

**Tech Stack:** Python 3 + pytest (existing `tools/smite/tests/`), YAML sidecars, Vite/React/TS viewer (vitest; type-gate is `cd viewer && npm run build`, NOT `npx tsc`).

**Spec:** `docs/superpowers/specs/2026-07-22-smite-scoring-intelligence-design.md`

**Vault hygiene (from CLAUDE.md):** work in an isolated worktree (superpowers:using-git-worktrees), commit only your own paths (never `git add -A`), `git fetch` + integrate before pushing (30-min cron commits on main), never touch `_archive/`.

**Run tests from `tools/`:** `cd tools && python -m pytest smite/tests/ -q`

---

## Metrics log (append after every checkpoint task)

| After task | Coverage | Win-weighted | Spearman | Notes |
|---|---|---|---|---|
| baseline | 60% | 62% | 0.26 (n=54) | Ymir in pool since 2026-07-21 |
| Task 2 (tags) | 60% | 62% | 0.26 (n=54) | Added sustain (Hunter's Cowl) + aura (Soul Gem, Umbral Link, War Banner, War Flag); rejected 5 possible-missing candidates as unsupported by passive text — no measurable shift |

---

### Task 1: Worktree + baseline

**Files:** none (setup)

- [ ] **Step 1:** Create the isolated workspace via superpowers:using-git-worktrees, branch `smite-scoring-intelligence`.
- [ ] **Step 2:** Verify a clean test baseline:

Run: `cd tools && python -m pytest smite/tests/ -q`
Expected: all pass.

- [ ] **Step 3:** Re-run `python -m smite.validate` (from `tools/`) and confirm the metrics-log baseline row matches its output. If it differs (data moved overnight), update the baseline row and use the new numbers everywhere below.

---

### Task 2: Effect-tag fixes (quick win, measured)

**Files:**
- Modify: `04. System/Data/SMITE/_tags.yaml`

The `possible-missing` rows in `04. System/Data/SMITE/Analysis/_tag_audit.md` are candidates, not orders — verify each against the item's actual `passive` text in `04. System/Data/SMITE/Items/<Item>.md` before tagging.

- [ ] **Step 1:** For each of: Barbed Carver, Contagion, Gluttonous Grimoire, Hunter's Cowl, Sanguine Lash, Typhon's Heart (candidate `sustain`) and Soul Gem, Umbral Link, War Banner, War Flag (candidate `aura`) — read the item note's `passive` field. Add the tag in `_tags.yaml` only when the passive genuinely has the effect (lifesteal/heal-on-X for `sustain`; affects nearby allies for `aura`). Contagion's audit row is `sustain` (its anti-heal tag already exists) — check whether its passive actually sustains the *wearer*; if not, skip it.
- [ ] **Step 2:** Regenerate + measure:

```bash
cd tools && python -m smite.recommend --all && python -m smite.validate
```

Record the three numbers in the metrics log. Expected: small move either way; tags feed `_is_lifesteal` caps and tag bonuses, not raw scores, so don't expect much yet.

- [ ] **Step 3:** Check the vault diff — `git status` — and revert EOL-only churn in regenerated notes (`git checkout -- <paths>` for files whose diff is line-ending noise only).
- [ ] **Step 4:** Commit:

```bash
git add "04. System/Data/SMITE/_tags.yaml" "04. System/Data/SMITE/Analysis" "03. Workspaces/Gaming/SMITE 2/Builds" "docs/superpowers/plans/2026-07-22-smite-scoring-intelligence.md"
git commit -m "fix(smite): apply verified possible-missing effect tags"
```

---

### Task 3: Token-based role matching + damage-type guard

**Files:**
- Modify: `tools/smite/scoring.py` (`_role_stat_map`, `DEFAULT_WEIGHTS`)
- Test: `tools/smite/tests/test_scoring.py`

- [ ] **Step 1: Write the failing tests** (append to `test_scoring.py`; `_god` helper already exists there):

```python
def test_role_map_matches_tokens_in_multiword_roles():
    w = scoring.load_weights_default()
    cern = _god("Cernunnos", "physical", "Carry Jungle", ["Sharpshooter"])
    m = scoring._role_stat_map(cern, w)
    assert m["Attack Speed"] == 1.0          # Sharpshooter, exact match
    assert m["Penetration"] >= 0.8           # Jungle, token match


def test_role_map_drops_opposite_damage_type_offense():
    w = scoring.load_weights_default()
    cern = _god("Cernunnos", "physical", "Carry Jungle", ["Nuker", "Sharpshooter"])
    assert "Intelligence" not in scoring._role_stat_map(cern, w)
    ymir = _god("Ymir", "magical", "Support", ["Brawler", "Tank", "Lockdown"])
    m = scoring._role_stat_map(ymir, w)
    assert "Strength" not in m
    assert m["Physical Protection"] == 1.0
    assert m["Max Health"] == 0.8


def test_every_pool_role_vocabulary_produces_a_nonempty_map():
    w = scoring.load_weights_default()
    pool = [  # the real scraped vocabulary of all 11 gods
        ("magical", "Mid", ["Nuker", "Burst Damage", "Sniper"]),
        ("physical", "Carry Jungle", ["Nuker", "Sharpshooter", "Lockdown"]),
        ("physical", "Carry", ["Sharpshooter", "Nuker"]),
        ("magical", "Mid Carry", ["Constant Damage"]),
        ("physical", "Solo", ["Tank", "Brawler", "Lockdown"]),
        ("magical", "Mid", ["Nuker", "Burst Damage"]),
        ("magical", "Carry Mid", ["Sharpshooter", "Mobile", "Constant Damage"]),
        ("magical", "Mid", ["Sniper", "Healing", "Buffs"]),
        ("physical", "Jungle", ["Slayer", "Lockdown", "Mobile"]),
        ("physical", "Carry", ["Lockdown", "Burst Damage", "Pressure"]),
        ("magical", "Support", ["Brawler", "Tank", "Lockdown"]),
    ]
    for dt, role, specs in pool:
        m = scoring._role_stat_map(_god("X", dt, role, specs), w)
        assert m, f"empty fit map for role={role} specs={specs}"


def test_role_map_uses_max_health_not_health():
    # Items carry 'Max Health' (63 of them); no item has a 'Health' stat key.
    w = scoring.load_weights_default()
    for entry in w["role_stats"].values():
        assert "Health" not in entry, "use 'Max Health' — 'Health' matches no item"
```

- [ ] **Step 2: Run to verify they fail:**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -q`
Expected: the four new tests FAIL (empty maps, Health keys, Intelligence present).

- [ ] **Step 3: Implement.** In `scoring.py`, replace `DEFAULT_WEIGHTS["role_stats"]` and `_role_stat_map`:

```python
    # role/spec label → {stat: weight}. Labels match exactly first, then by
    # whitespace token ("Carry Jungle" → Carry + Jungle), so the scraped
    # vocabulary (Mid, Solo, Support, Slayer, "Burst Damage", …) always lands.
    # Stat keys must be real item stat keys ("Max Health", not "Health").
    "role_stats": {
        "Sharpshooter": {"Attack Speed": 1.0, "Critical Chance": 1.0, "Strength": 0.6, "Lifesteal": 0.5},
        "Nuker": {"Intelligence": 1.0, "Strength": 0.6, "Penetration": 1.0, "Cooldown Rate": 0.5},
        "Mage": {"Intelligence": 1.0, "Penetration": 0.8, "Cooldown Rate": 0.5},
        "Hunter": {"Strength": 1.0, "Attack Speed": 0.8, "Critical Chance": 0.6, "Lifesteal": 0.5},
        "Carry": {"Strength": 0.8, "Attack Speed": 0.6, "Critical Chance": 0.6, "Lifesteal": 0.5},
        "Assassin": {"Strength": 1.0, "Penetration": 0.8},
        "Warrior": {"Strength": 0.8, "Physical Protection": 0.5, "Max Health": 0.5},
        "Guardian": {"Physical Protection": 1.0, "Magical Protection": 1.0, "Max Health": 0.8},
        "Tank": {"Physical Protection": 1.0, "Magical Protection": 1.0, "Max Health": 0.8},
        "Support": {"Physical Protection": 0.9, "Magical Protection": 0.9, "Max Health": 0.8},
        "Brawler": {"Max Health": 0.8, "Physical Protection": 0.5, "Magical Protection": 0.5, "Strength": 0.4},
        "Solo": {"Max Health": 0.7, "Physical Protection": 0.5, "Magical Protection": 0.5, "Strength": 0.4},
        "Jungle": {"Strength": 1.0, "Penetration": 0.8},
        "Slayer": {"Strength": 1.0, "Penetration": 0.8},
        "Mid": {"Intelligence": 1.0, "Penetration": 0.8, "Cooldown Rate": 0.5},
        "Sniper": {"Intelligence": 1.0, "Penetration": 0.8},
        "Burst": {"Penetration": 0.8, "Cooldown Rate": 0.5},
        "Healing": {"Cooldown Rate": 0.8, "Intelligence": 0.4},
        "Buffs": {"Cooldown Rate": 0.6},
        "Constant": {"Attack Speed": 0.6},
        "Pressure": {"Attack Speed": 0.5},
    },
```

```python
# Offensive stats that are dead weight for the opposite damage type: an
# Intelligence entry on a physical god (Cernunnos's "Nuker" spec) would skew
# fit toward items the damage filter already forbids — drop them up front.
# Attack Speed stays for magical gods (hybrid Int+AS items are real).
_OPPOSITE_OFFENSE = {
    "physical": ("Intelligence",),
    "magical": ("Strength", "Critical Chance"),
}


def _role_stat_map(god, weights):
    role_stats = weights["role_stats"]
    labels = [str(s) for s in (god.get("specializations") or [])]
    if god.get("role"):
        labels.append(str(god["role"]))
    merged = {}
    for label in labels:
        keys = [label] if label in role_stats else [t for t in label.split() if t in role_stats]
        for key in keys:
            for stat, w in role_stats[key].items():
                merged[stat] = max(merged.get(stat, 0.0), w)
    for stat in _OPPOSITE_OFFENSE.get(god.get("damage_type"), ()):
        merged.pop(stat, None)
    return merged
```

- [ ] **Step 4: Run the full suite:**

Run: `cd tools && python -m pytest smite/tests/ -q`
Expected: PASS (if an existing test asserted the old Guardian "Health" key, update it — the rename is intended).

- [ ] **Step 5: Commit:**

```bash
git add tools/smite/scoring.py tools/smite/tests/test_scoring.py
git commit -m "feat(smite): token role matching, full role vocabulary, damage-type guard"
```

---

### Task 4: Checkpoint — regenerate + measure the vocabulary fix

**Files:** regenerated notes + Analysis reports

- [ ] **Step 1:** `cd tools && python -m smite.recommend --all && python -m smite.validate`
- [ ] **Step 2:** Record metrics in the log. Expected: **meaningful jump** — Ymir/Hercules/Chronos suggested cores should turn tanky/appropriate (spot-check `03. Workspaces/Gaming/SMITE 2/Builds/Ymir-Conquest.md`: the suggested core should now be protections/health items, not Ethereal Staff + Gluttonous Grimoire). If coverage does NOT improve, stop and investigate with `smite.recommend`'s per-god reports (`Analysis/<God>.md`) before proceeding.
- [ ] **Step 3:** Revert EOL-only churn; commit regenerated notes + reports + updated plan metrics log:

```bash
git add "04. System/Data/SMITE" "03. Workspaces/Gaming/SMITE 2/Builds" "docs/superpowers/plans/2026-07-22-smite-scoring-intelligence.md"
git commit -m "chore(smite): regenerate builds with fixed role vocabulary"
```

---

### Task 5: Kit-scaling parser (`kit.py`)

**Files:**
- Create: `tools/smite/kit.py`
- Test: `tools/smite/tests/test_kit.py`

- [ ] **Step 1: Write the failing tests** (`tools/smite/tests/test_kit.py`):

```python
from smite import kit


def _ability(slot, *details):
    return {"slot": slot, "details": list(details)}


def _god(damage_type, abilities):
    return {"name": "X", "damage_type": damage_type, "abilities": abilities}


def test_scaling_profile_parses_percent_stat_lines():
    god = _god("magical", [
        _ability("Basic Attack", "Damage Scaling: 100% Strength + 20% Intelligence"),
        _ability("1st Ability", "Damage Scaling: 70% Intelligence + 45% Strength"),
        _ability("2nd Ability", "Damage Scaling: 80% Intelligence"),
        _ability("Passive", "Damage Scaling: 175% Basic Attack Damage"),
    ])
    p = kit.scaling_profile(god)
    assert p["n_scaling_abilities"] == 3            # Basic Attack slot excluded
    assert p["int_share"] > p["str_share"]
    assert p["str_share"] + p["int_share"] == 1.0
    assert 0.0 < p["basic_attack_share"] < 1.0      # Frostbite-style 175% BAD


def test_scaling_profile_empty_kit_is_all_zero():
    p = kit.scaling_profile(_god("physical", []))
    assert p == {"str_share": 0.0, "int_share": 0.0,
                 "basic_attack_share": 0.0, "n_scaling_abilities": 0}


def test_overlay_low_confidence_returns_empty():
    # Ullr's stance kit scrapes only 1 scaling ability — fall back to role map.
    god = _god("physical", [_ability("1st Ability", "Damage Scaling: 100% Strength")])
    assert kit.kit_stat_overlay(kit.scaling_profile(god), god) == {}


def test_overlay_ability_kit_boosts_cdr_and_pen():
    god = _god("magical", [
        _ability("1st Ability", "Damage Scaling: 80% Intelligence"),
        _ability("2nd Ability", "Damage Scaling: 70% Intelligence"),
        _ability("Ultimate", "Damage Scaling: 120% Intelligence"),
    ])
    ov = kit.kit_stat_overlay(kit.scaling_profile(god), god)
    assert ov["Intelligence"] > 1.0                 # 0.6 + 0.6 * share=1.0
    assert ov["Cooldown Rate"] == 0.6
    assert ov["Penetration"] == 0.8
    assert "Attack Speed" not in ov


def test_overlay_basic_attack_kit_boosts_attack_speed_and_crit():
    god = _god("physical", [
        _ability("Passive", "Damage Scaling: 175% Basic Attack Damage"),
        _ability("1st Ability", "Damage Scaling: 100% Basic Attack Damage"),
        _ability("2nd Ability", "Damage Scaling: 60% Strength"),
    ])
    ov = kit.kit_stat_overlay(kit.scaling_profile(god), god)
    assert ov["Attack Speed"] > 0.5
    assert ov["Critical Chance"] > 0.4              # physical only
```

- [ ] **Step 2: Run to verify failure:**

Run: `cd tools && python -m pytest smite/tests/test_kit.py -q`
Expected: FAIL — `ModuleNotFoundError: smite.kit`.

- [ ] **Step 3: Implement** `tools/smite/kit.py`:

```python
"""Kit-scaling profiles: parse each ability's 'Damage Scaling: N% <Stat>'
lines into a per-god orientation (Strength vs Intelligence, basic-attack vs
ability) so god-fit reflects the actual kit, not only the archetype label.
Heuristic, not simulation — see the 2026-07-22 design spec."""
import re

_SCALING_LINE = re.compile(
    r"(\d+(?:\.\d+)?)\s*%\s*(Strength|Intelligence|Basic Attack Damage|Attack Damage)",
    re.IGNORECASE)
_CANON = {"strength": "Strength", "intelligence": "Intelligence",
          "basic attack damage": "Basic Attack Damage", "attack damage": "Attack Damage"}


def scaling_profile(god):
    """str/int/basic-attack scaling shares across the god's abilities.
    The Basic Attack slot itself is excluded — every god's basic carries
    ~100% Strength, so it says nothing about the kit. 'Basic Attack Damage' /
    'Attack Damage' references in *other* slots mark basic-attack orientation
    (steroids and on-hit passives like Ymir's Frostbite)."""
    str_t = int_t = basic_t = 0.0
    n = 0
    for ab in god.get("abilities") or []:
        if "basic attack" in str(ab.get("slot") or "").lower():
            continue
        sums = {}
        for detail in ab.get("details") or []:
            text = str(detail)
            if "scaling" not in text.lower():
                continue
            for m in _SCALING_LINE.finditer(text):
                stat = _CANON[m.group(2).lower()]
                sums[stat] = sums.get(stat, 0.0) + float(m.group(1))
        if not sums:
            continue
        n += 1
        str_t += sums.get("Strength", 0.0)
        int_t += sums.get("Intelligence", 0.0)
        basic_t += sums.get("Basic Attack Damage", 0.0) + sums.get("Attack Damage", 0.0)
    dmg = str_t + int_t
    total = dmg + basic_t
    return {
        "str_share": (str_t / dmg) if dmg else 0.0,
        "int_share": (int_t / dmg) if dmg else 0.0,
        "basic_attack_share": (basic_t / total) if total else 0.0,
        "n_scaling_abilities": n,
    }


def kit_stat_overlay(profile, god):
    """Offensive stat weights implied by the kit, or {} when confidence is low
    (< 3 abilities with scaling — sparse scrapes like Ullr's stance kit)."""
    if profile["n_scaling_abilities"] < 3:
        return {}
    out = {}
    dt = god.get("damage_type")
    if dt == "physical" and profile["str_share"] > 0:
        out["Strength"] = round(0.6 + 0.6 * profile["str_share"], 3)
    if dt == "magical" and profile["int_share"] > 0:
        out["Intelligence"] = round(0.6 + 0.6 * profile["int_share"], 3)
    if profile["basic_attack_share"] >= 0.2:
        out["Attack Speed"] = round(0.5 + profile["basic_attack_share"], 3)
        if dt == "physical":
            out["Critical Chance"] = round(0.4 + profile["basic_attack_share"], 3)
    else:
        out["Cooldown Rate"] = 0.6
        out["Penetration"] = 0.8
    return out
```

- [ ] **Step 4: Run:** `cd tools && python -m pytest smite/tests/test_kit.py -q` — Expected: PASS.
- [ ] **Step 5: Commit:**

```bash
git add tools/smite/kit.py tools/smite/tests/test_kit.py
git commit -m "feat(smite): kit-scaling profile parser (str/int/basic-attack orientation)"
```

---

### Task 6: Blend the kit overlay into god-fit

**Files:**
- Modify: `tools/smite/scoring.py` (`DEFAULT_WEIGHTS`, `god_fit_score`, `signal_score`, `score_god_items`)
- Test: `tools/smite/tests/test_scoring.py`

- [ ] **Step 1: Write the failing test** (append to `test_scoring.py`):

```python
def test_kit_overlay_blends_into_fit_via_score_god_items():
    weights = scoring.load_weights_default()
    int_item = {"name": "Staff", "tier": 3, "stats": {"Intelligence": "70"}}
    cdr_item = {"name": "Pendant", "tier": 3, "stats": {"Cooldown Rate": "10"}}
    eff = {"Staff": {"score": 0.5, "tier": "fair"}, "Pendant": {"score": 0.5, "tier": "fair"}}
    build = {"builds": []}
    kit_god = {"name": "K", "damage_type": "magical", "role": "Mid", "specializations": [],
               "abilities": [
                   {"slot": "1st Ability", "details": ["Damage Scaling: 80% Intelligence"]},
                   {"slot": "2nd Ability", "details": ["Damage Scaling: 70% Intelligence"]},
                   {"slot": "Ultimate", "details": ["Damage Scaling: 120% Intelligence"]},
               ]}
    no_kit_god = {**kit_god, "abilities": []}
    rows_kit = {r["item"]: r for r in scoring.score_god_items(
        kit_god, [int_item, cdr_item], build, eff, weights, {})}
    rows_plain = {r["item"]: r for r in scoring.score_god_items(
        no_kit_god, [int_item, cdr_item], build, eff, weights, {})}
    # A kit that is pure Intelligence scaling should shift fit relative to the
    # role map alone (the blended map differs from the plain role map).
    assert rows_kit["Staff"]["fit"] != rows_plain["Staff"]["fit"]
```

- [ ] **Step 2: Run to verify failure:** `cd tools && python -m pytest smite/tests/test_scoring.py -q` — the new test FAILS (fit identical: kit not wired in).
- [ ] **Step 3: Implement.** In `scoring.py`:

1. `from smite import kit` (top of file, after the efficiency import) and add `"kit_blend": 0.5,` to `DEFAULT_WEIGHTS` (top level, beside `"underrated"`).
2. Change `god_fit_score` to accept a precomputed base map:

```python
def god_fit_score(item, god, weights, item_tags, stat_overlay=None, tag_bonus=None,
                  base_map=None):
    """Archetype+kit fit in [0,1]. base_map (when given) replaces the role-map
    lookup — score_god_items passes the kit-blended map; flavor stat_overlay
    still wins on shared keys. NOT damage simulation — see spec."""
    stats = item.get("stats") or {}
    role_map = dict(base_map) if base_map is not None else _role_stat_map(god, weights)
    if stat_overlay:
        role_map = {**role_map, **stat_overlay}
    ...  # rest unchanged
```

3. Thread it through `signal_score` (add `base_map=None` param, pass to `god_fit_score`).
4. In `score_god_items`, before the item loop:

```python
    if profile.get("archetype_bypass"):
        base_map = {}
    else:
        base_map = _role_stat_map(god, weights)
        blend = eff_weights.get("kit_blend", 0.5)
        for stat, w in kit.kit_stat_overlay(kit.scaling_profile(god), god).items():
            base_map[stat] = (1 - blend) * base_map.get(stat, 0.0) + blend * w
```

(`archetype_bypass` arrives with Task 10; `profile.get()` on a missing key is already safe.) Pass `base_map=base_map` into `signal_score`.

- [ ] **Step 4: Run the full suite:** `cd tools && python -m pytest smite/tests/ -q` — Expected: PASS.
- [ ] **Step 5: Add `kit_blend: 0.5` with a one-line comment to `04. System/Data/SMITE/_weights.yaml`** (beside `signals:`) so the tunable is visible where opinions live:

```yaml
kit_blend: 0.5       # how much the parsed ability-scaling profile skews god-fit (0 = role map only)
```

- [ ] **Step 6: Commit:**

```bash
git add tools/smite/scoring.py tools/smite/tests/test_scoring.py "04. System/Data/SMITE/_weights.yaml"
git commit -m "feat(smite): blend kit-scaling overlay into god-fit (kit_blend tunable)"
```

---

### Task 7: Checkpoint — regenerate + measure kit-aware fit

- [ ] **Step 1:** `cd tools && python -m smite.recommend --all && python -m smite.validate`; record metrics.
- [ ] **Step 2:** If Spearman/coverage moved down vs Task 4, try `kit_blend: 0.3` in `_weights.yaml`, regenerate, re-measure; keep the better of {0, 0.3, 0.5} and note the choice in the metrics log. (`kit_blend: 0` must reproduce Task 4 numbers — if it doesn't, there's a bug; stop and debug.)
- [ ] **Step 3:** Revert EOL churn; commit regenerated artifacts + metrics log (same paths as Task 4, message `chore(smite): regenerate with kit-aware fit`).

---

### Task 8: Disagreement report (`analysis.py`)

**Files:**
- Create: `tools/smite/analysis.py`
- Test: `tools/smite/tests/test_analysis.py`

- [ ] **Step 1: Write the failing tests** (`tools/smite/tests/test_analysis.py`):

```python
from smite import analysis, scoring


def _items():
    return [
        {"name": f"Item{i}", "tier": 3, "cost": 2500,
         "stats": {"Strength": str(30 + i)}, "passive": ""}
        for i in range(12)
    ] + [{"name": "MetaDarling", "tier": 3, "cost": 2500,
          "stats": {"Magical Protection": "60"}, "passive": "Nearby allies gain 15 Strength."}]


def _god():
    return {"name": "G", "damage_type": "physical", "role": "Carry",
            "specializations": ["Sharpshooter"], "abilities": []}


def _build(community):
    return {"builds": [{"source": "community", "slot_order": community}]}


def test_missed_meta_flags_high_pick_items_we_rank_low():
    items = _items()
    eff = {it["name"]: {"score": 0.9 if it["name"] != "MetaDarling" else 0.1, "tier": "fair"}
           for it in items}
    build = _build([{"name": "MetaDarling", "pick_rate": 0.6, "win_rate": 0.55}])
    out = analysis.god_disagreements(
        _god(), items, build, scoring.load_weights_default(), {}, eff,
        {it["name"]: it for it in items})
    assert [m["item"] for m in out["missed_meta"]] == ["MetaDarling"]
    assert out["missed_meta"][0]["pick"] == 0.6


def test_off_meta_flags_core_items_nobody_picks():
    items = _items()
    eff = {it["name"]: {"score": 0.9, "tier": "fair"} for it in items}
    build = _build([{"name": "Item0", "pick_rate": 0.5, "win_rate": 0.5}])
    out = analysis.god_disagreements(
        _god(), items, build, scoring.load_weights_default(), {}, eff,
        {it["name"]: it for it in items})
    # 6-item core, only Item0 has community pick — the other 5 are off-meta.
    assert len(out["off_meta"]) >= 5
```

- [ ] **Step 2: Run to verify failure:** `cd tools && python -m pytest smite/tests/test_analysis.py -q` — FAIL (no module).
- [ ] **Step 3: Implement** `tools/smite/analysis.py`:

```python
"""Disagreement report: where the community meta and our scores part ways.
Read-only analysis tool — run it, form a hypothesis (tag gap? fit blind spot?
assembly rule?), encode the fix elsewhere, re-validate. Writes
Analysis/_disagreements.md."""
from smite import assemble, efficiency, recommend, scoring

PICK_MISSED = 0.10      # community pick rate that makes an item "meta"
RANK_CUT = 10           # our rank below this = we effectively don't suggest it
PICK_OFFMETA = 0.05     # community pick under this = "nobody runs it"


def god_disagreements(god, items, build_note, weights, tags_map, eff_scores, items_by_name):
    profile = scoring.resolve_profile(weights, "Conquest", None)
    rows = scoring.score_god_items(god, items, build_note, eff_scores, weights, tags_map, profile)
    rank = {r["item"]: i + 1 for i, r in enumerate(rows)}
    by_name = {r["item"]: r for r in rows}
    core = assemble.assemble_core(rows, items_by_name, n=6,
                                  max_lifesteal=profile["max_lifesteal"])
    community = [c for b in build_note.get("builds", []) if b.get("source") == "community"
                 for c in b.get("slot_order", []) if isinstance(c, dict)]
    missed = []
    for c in community:
        name = c.get("name")
        if (c.get("pick_rate") or 0.0) >= PICK_MISSED and rank.get(name, 10**6) > RANK_CUT:
            missed.append({"item": name, "pick": c.get("pick_rate"), "win": c.get("win_rate"),
                           "rank": rank.get(name), "row": by_name.get(name),
                           "filtered_out": name not in rank})
    comm_pick = {c.get("name"): (c.get("pick_rate") or 0.0) for c in community}
    off_meta = [{"item": n, "pick": comm_pick.get(n, 0.0), "row": by_name[n], "rank": rank[n]}
                for n in core if comm_pick.get(n, 0.0) < PICK_OFFMETA]
    top6 = [r["item"] for r in rows[:6]]
    conflicts = [n for n in top6
                 if n not in core and comm_pick.get(n, 0.0) >= PICK_MISSED]
    return {"missed_meta": missed, "off_meta": off_meta, "constraint_conflicts": conflicts}


def _fmt_row(r):
    if not r:
        return "filtered out (damage filter / not buildable)"
    return (f"total {r['total']:.2f} · eff {r['efficiency']:.2f} · win {r['win']:.2f} "
            f"· pick {r['pick']:.2f} · fit {r['fit']:.2f} · tags: {', '.join(r['tags']) or '—'}")


def write_report(per_god, items_by_name, out_path):
    lines = ["# Meta disagreements (community vs our scores)", "",
             "Hypothesis generator, not a verdict. `missed meta` = community runs it, "
             "we rank it low. `off-meta pick` = we suggest it, community doesn't. "
             "`constraint conflict` = scoring liked it but an assembly rule "
             "(lifesteal cap / boots / crit floor) kept it out of the core.", ""]
    from collections import Counter
    rollup = Counter()
    for god_name in sorted(per_god):
        d = per_god[god_name]
        if not (d["missed_meta"] or d["off_meta"] or d["constraint_conflicts"]):
            continue
        lines.append(f"## {god_name}")
        for m in d["missed_meta"]:
            rollup[m["item"]] += 1
            it = items_by_name.get(m["item"], {})
            lines += [f"- **missed meta:** {m['item']} — community pick {m['pick']:.0%}, "
                      f"win {(m['win'] or 0):.0%}, our rank {m['rank'] or 'filtered'}",
                      f"  - {_fmt_row(m['row'])}",
                      f"  - passive: {(it.get('passive') or '—')[:200]}"]
        for o in d["off_meta"]:
            lines.append(f"- off-meta pick: {o['item']} (our rank {o['rank']}, "
                         f"community pick {o['pick']:.0%})")
        for c in d["constraint_conflicts"]:
            lines.append(f"- **constraint conflict:** {c} — top-6 by score, "
                         f"meta-picked, excluded by assembly rules")
        lines.append("")
    if rollup:
        lines += ["## Cross-god rollup (items we repeatedly miss)", ""]
        lines += [f"- {name} × {n}" for name, n in rollup.most_common() if n > 1]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv=None):
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags_map = scoring.load_tags(recommend.TAGS_PATH)
    eff_scores, _ = efficiency.efficiency_scores(items)
    items_by_name = {it["name"]: it for it in items}
    per_god = {}
    for god in recommend.load_gods():
        build = recommend.load_build_note(god["name"])
        if any(b.get("source") == "community" for b in build.get("builds", [])):
            per_god[god["name"]] = god_disagreements(
                god, items, build, weights, tags_map, eff_scores, items_by_name)
    out = recommend.DATA_ROOT / "Analysis" / "_disagreements.md"
    write_report(per_god, items_by_name, out)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
```

- [ ] **Step 4: Run:** `cd tools && python -m pytest smite/tests/test_analysis.py -q` — PASS. Then run it for real: `python -m smite.analysis` and read `Analysis/_disagreements.md`.
- [ ] **Step 5: Commit:**

```bash
git add tools/smite/analysis.py tools/smite/tests/test_analysis.py "04. System/Data/SMITE/Analysis/_disagreements.md"
git commit -m "feat(smite): meta-disagreement report (missed meta / off-meta / constraint conflicts)"
```

---

### Task 9: Act on the disagreement report (metric-gated)

**Files:** `04. System/Data/SMITE/_weights.yaml`, possibly `_tags.yaml`, possibly `tools/smite/scoring.py`

This task is intentionally exploratory but bounded: pick the top 2–3 findings from `_disagreements.md`, encode each as a config/code change, and keep only changes that improve validation.

- [ ] **Step 1:** Known candidate to test first (visible in Cernunnos's community build — Devourer's Gauntlet 63% pick + Riptalon both sustain, core `max_lifesteal=1` forbids the pair): allow 2 sustain items for basic-attack carries. Mechanism: in `_weights.yaml`, this is what per-mode/flavor `max_lifesteal` exists for — but the *core* profile has no overlay. Add a top-level `core_max_lifesteal_by_role:` is NOT the way; instead test bumping the default: `resolve_profile` returns `max_lifesteal = 1` when nothing set. Add to `_weights.yaml` under `modes.conquest`: `{max_lifesteal: 2}` and extend `resolve_profile` to honor a mode-level `max_lifesteal` (mode < aspect < flavor precedence, one line in the existing chain, with a matching unit test in `test_scoring.py`).
- [ ] **Step 2:** For each candidate change: apply → `python -m smite.recommend --all && python -m smite.validate` → record in metrics log → keep or revert. At least 2 findings must be tried; keep only what helps.
- [ ] **Step 3:** Note each kept/rejected hypothesis in one line each at the top of `_disagreements.md` (the report is regenerated later — put the notes in the commit message too).
- [ ] **Step 4:** Commit (only files actually changed):

```bash
git add "04. System/Data/SMITE" "03. Workspaces/Gaming/SMITE 2/Builds" tools/smite
git commit -m "feat(smite): encode disagreement-report findings (kept: <list>; rejected: <list>)"
```

---

### Task 10: Fun-flavor engine (bypass flags, zeroed meta signals)

**Files:**
- Modify: `tools/smite/scoring.py` (`resolve_profile`, `score_god_items`)
- Test: `tools/smite/tests/test_scoring.py`

- [ ] **Step 1: Write the failing tests:**

```python
def test_fun_profile_zeroes_meta_signals_and_sets_bypass_flags():
    w = scoring.load_weights_default()
    w["flavors"] = {"fun-crit": {"fun": True, "bypass": ["damage_filter", "archetype_fit"],
                                 "stats": {"Critical Chance": 1.5}}}
    p = scoring.resolve_profile(w, "Conquest", "fun-crit")
    assert p["signals"]["win"] == 0.0 and p["signals"]["pick"] == 0.0
    assert p["bypass_damage_filter"] is True
    assert p["archetype_bypass"] is True
    assert p["fun"] is True
    assert p["suppress_underrated"] is True


def test_serious_profile_has_no_bypass():
    p = scoring.resolve_profile(scoring.load_weights_default(), "Conquest", None)
    assert p["bypass_damage_filter"] is False
    assert p["archetype_bypass"] is False
    assert p["fun"] is False


def test_bypass_damage_filter_lets_crit_items_reach_a_magical_god():
    w = scoring.load_weights_default()
    w["flavors"] = {"fun-crit": {"fun": True, "bypass": ["damage_filter", "archetype_fit"],
                                 "stats": {"Critical Chance": 1.5, "Attack Speed": 1.2}}}
    ymir = _god("Ymir", "magical", "Support", ["Tank"])
    crit_item = {"name": "Deathbringer", "tier": 3, "stats": {"Critical Chance": "25%"}}
    eff = {"Deathbringer": {"score": 0.5, "tier": "fair"}}
    fun = scoring.resolve_profile(w, "Conquest", "fun-crit")
    serious = scoring.resolve_profile(w, "Conquest", None)
    fun_rows = scoring.score_god_items(ymir, [crit_item], {"builds": []}, eff, w, {}, fun)
    serious_rows = scoring.score_god_items(ymir, [crit_item], {"builds": []}, eff, w, {}, serious)
    assert [r["item"] for r in fun_rows] == ["Deathbringer"]
    assert serious_rows == []                       # damage filter still guards serious builds
    assert fun_rows[0]["fit"] > 0                   # flavor stats drive fit despite empty role map
```

- [ ] **Step 2: Run to verify failure:** `cd tools && python -m pytest smite/tests/test_scoring.py -q`.
- [ ] **Step 3: Implement.** In `resolve_profile`, after `fl`/`asp` are read:

```python
    bypass = set(fl.get("bypass") or [])
    fun = bool(fl.get("fun"))
    if fun:
        # Off-class items have no meta data; a neutral 0.5 win rate would only
        # add noise, so fun builds are scored on efficiency + flavor fit alone.
        signals = {**signals, "win": 0.0, "pick": 0.0}
```

(place the `signals` fun-override after the existing `signals = {**weights["signals"], ...}` line) and extend the returned dict:

```python
        "bypass_damage_filter": "damage_filter" in bypass,
        "archetype_bypass": "archetype_fit" in bypass,
        "fun": fun,
```

In `score_god_items`, change the damage-filter line:

```python
        if not profile.get("bypass_damage_filter") and not passes_damage_filter(item, god):
            continue
```

(The `archetype_bypass` → `base_map = {}` branch already landed in Task 6.)

- [ ] **Step 4: Run full suite:** `cd tools && python -m pytest smite/tests/ -q` — PASS.
- [ ] **Step 5: Commit:**

```bash
git add tools/smite/scoring.py tools/smite/tests/test_scoring.py
git commit -m "feat(smite): fun-flavor engine — bypass flags, zeroed meta signals"
```

---

### Task 11: `fun-crit` flavor + emission in recommend

**Files:**
- Modify: `04. System/Data/SMITE/_weights.yaml` (flavors), `tools/smite/recommend.py`
- Test: `tools/smite/tests/test_recommend.py`

- [ ] **Step 1: Write the failing tests** (append to `test_recommend.py`, reusing its existing fixture style — check the top of the file for its god/items helpers and follow them):

```python
def _fun_weights():
    w = scoring.load_weights_default()
    w["flavors"] = {
        "crit": {"damage_types": ["physical"], "match_any": ["Carry", "Sharpshooter"],
                 "stats": {"Critical Chance": 1.5}, "require": {"stat": "Critical Chance", "min": 3}},
        "fun-crit": {"fun": True, "bypass": ["damage_filter", "archetype_fit"],
                     "redundant_with": "crit", "damage_types": None, "match_any": None,
                     "stats": {"Critical Chance": 1.5, "Attack Speed": 1.2, "Strength": 0.8},
                     "require": {"stat": "Critical Chance", "min": 3}},
    }
    return w


def test_fun_entry_emitted_for_offclass_god_with_flag_and_honest_rationale(tmp_items):
    ymir = {"name": "Ymir", "damage_type": "magical", "role": "Support",
            "specializations": ["Tank"], "abilities": []}
    entries = recommend.build_suggested_entries(ymir, tmp_items, {"builds": []},
                                                _fun_weights(), {})
    fun = [e for e in entries if e.get("fun")]
    assert len(fun) == 1 and fun[0]["archetype"] == "fun-crit"
    assert "fun" in fun[0]["rationale"].lower()


def test_fun_crit_skipped_when_serious_crit_applies(tmp_items):
    chiron = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
              "specializations": ["Sharpshooter"], "abilities": []}
    entries = recommend.build_suggested_entries(chiron, tmp_items, {"builds": []},
                                                _fun_weights(), {})
    assert not [e for e in entries if e.get("fun")]          # redundant_with: crit
    assert [e for e in entries if e["archetype"] == "crit"]  # serious crit still there
```

If `test_recommend.py` has no reusable items fixture, add one at module level: a `tmp_items` pytest fixture returning ~8 tier-3 dicts with mixed stats (at least 3 with `Critical Chance`, e.g. `{"name": "Crit1", "tier": 3, "cost": 2500, "stats": {"Critical Chance": "25%", "Attack Speed": "15"}}`).

- [ ] **Step 2: Run to verify failure**, then **Step 3: implement**:

1. `_weights.yaml` — append to `flavors:` (LAST entry, so fun builds render after serious ones):

```yaml
  fun-crit:
    # For-fun off-class build: crit for anyone, including guardians and mages.
    # Bypasses the damage filter and archetype fit ON PURPOSE; win/pick zeroed
    # by the engine (fun: true). Skipped for gods that already get the serious
    # crit flavor (redundant_with).
    fun: true
    bypass: [damage_filter, archetype_fit]
    redundant_with: crit
    damage_types: null
    match_any: null
    stats: {Critical Chance: 1.5, Attack Speed: 1.2, Strength: 0.8}
    max_lifesteal: 1
    require: {stat: "Critical Chance", min: 3}
```

2. `recommend.py` — in `_build_entry_set`, resolve the flavor config and gate:

```python
def _build_entry_set(god, items, god_build, weights, tags_map, mode, eff_scores,
                     items_by_name, starter, flex_count, aspect_overlay, aspect_name):
    entries = []
    eligible = scoring.eligible_flavors(god, weights)
    for flavor in [None] + eligible:
        cfg = ((weights.get("flavors") or {}).get(flavor) or {}) if flavor else {}
        if cfg.get("fun") and (aspect_overlay is not None
                               or cfg.get("redundant_with") in eligible):
            continue  # fun builds: base kit only, and never beside a serious twin
        ...
        entries.append({
            ...,
            **({"fun": True} if cfg.get("fun") else {}),
        })
```

3. `_rationale` — honest labeling; give it the profile it already receives:

```python
def _rationale(archetype, rows, profile):
    if profile.get("fun"):
        return (f"For fun — deliberately fights this god's kit "
                f"({_FLAVOR_BLURB.get(archetype, archetype)}). "
                "Scored on gold-value + flavor fit only; not meta-checked.")
    ...  # existing body unchanged
```

4. Add `"fun-crit": "Crit / attack-speed party build"` to `_FLAVOR_BLURB`.

- [ ] **Step 4: Run:** `cd tools && python -m pytest smite/tests/ -q` — PASS.
- [ ] **Step 5:** Regenerate (`python -m smite.recommend --all && python -m smite.validate`) and confirm: (a) validation numbers **unchanged** from Task 9 (fun builds never touch the core profile or validation), (b) `Ymir-Conquest.md` now contains a `fun-crit` suggested entry with `fun: true` and crit items. Record in metrics log.
- [ ] **Step 6: Commit** (weights, recommend.py, tests, regenerated notes):

```bash
git add tools/smite "04. System/Data/SMITE" "03. Workspaces/Gaming/SMITE 2/Builds" "docs/superpowers/plans/2026-07-22-smite-scoring-intelligence.md"
git commit -m "feat(smite): fun-crit off-class flavor, honestly labeled"
```

---

### Task 12: Weight calibration (`calibrate.py`)

**Files:**
- Create: `tools/smite/calibrate.py`
- Modify: `tools/smite/validate.py` (`compute` gains optional preloaded data)
- Test: `tools/smite/tests/test_calibrate.py`

- [ ] **Step 1: Write the failing tests** (`tools/smite/tests/test_calibrate.py`):

```python
from smite import calibrate


def test_weight_grid_respects_guardrails():
    grid = calibrate.weight_grid(step=0.05)
    assert grid, "grid must not be empty"
    for g in grid:
        total = g["efficiency"] + g["win"] + g["pick"] + g["fit"]
        assert abs(total - 1.0) < 1e-9
        assert g["pick"] <= 0.15 + 1e-9                      # popularity capped
        assert g["efficiency"] + g["fit"] >= 0.50 - 1e-9     # intrinsic quality floor
    # The current hand weights satisfy the guardrails and must be in the grid.
    assert {"efficiency": 0.35, "win": 0.30, "pick": 0.15, "fit": 0.20} in grid


def test_objective_blends_spearman_and_coverage():
    perfect = {"pooled_spearman": 1.0, "mean_coverage": 1.0}
    useless = {"pooled_spearman": None, "mean_coverage": 0.0}
    assert calibrate.objective(perfect) == 1.0
    assert calibrate.objective(useless) == 0.25   # (0+1)/2 * 0.5 + 0
    assert calibrate.objective(perfect) > calibrate.objective(
        {"pooled_spearman": 0.3, "mean_coverage": 0.6})
```

- [ ] **Step 2: Run to verify failure**, then **Step 3: implement**.

First the `validate.compute` speedup (it currently re-reads gods + build notes from disk per call — the grid makes ~500 calls):

```python
def compute(items=None, weights=None, tags_map=None, gods=None, builds_by_god=None):
    items = items if items is not None else recommend.load_items()
    weights = weights if weights is not None else scoring.load_weights(recommend.WEIGHTS_PATH)
    tags_map = tags_map if tags_map is not None else scoring.load_tags(recommend.TAGS_PATH)
    gods = gods if gods is not None else recommend.load_gods()
    if builds_by_god is None:
        builds_by_god = {g["name"]: recommend.load_build_note(g["name"]) for g in gods}
    eff_scores, _ = efficiency.efficiency_scores(items)
    items_by_name = {it["name"]: it for it in items}
    per_god = {}
    for god in gods:
        build = builds_by_god[god["name"]]
        if not _community_slots(build):
            continue
        per_god[god["name"]] = god_metrics(god, items, build, weights, tags_map, eff_scores, items_by_name)
    return per_god, aggregate(per_god)
```

Then `tools/smite/calibrate.py`:

```python
"""Grid-search the four signal weights against the validation metric, with
guardrails (efficiency + fit >= 0.50, pick <= 0.15) and a leave-one-god-out
stability check. Writes Analysis/_calibration.md. Applying the winner to
_weights.yaml stays a deliberate human edit — the weights file is the
recommender's opinion surface, not a cache."""
import copy

from smite import recommend, scoring, validate


def weight_grid(step=0.05, min_eff_fit=0.50, max_pick=0.15):
    n = round(1 / step)
    grid = []
    for e in range(n + 1):
        for w in range(n + 1 - e):
            for p in range(n + 1 - e - w):
                f = n - e - w - p
                we, ww, wp, wf = (x * step for x in (e, w, p, f))
                if wp > max_pick + 1e-9 or we + wf < min_eff_fit - 1e-9:
                    continue
                grid.append({"efficiency": round(we, 2), "win": round(ww, 2),
                             "pick": round(wp, 2), "fit": round(wf, 2)})
    return grid


def objective(agg):
    s = agg["pooled_spearman"] if agg.get("pooled_spearman") is not None else 0.0
    return 0.5 * ((s + 1) / 2) + 0.5 * agg["mean_coverage"]


def evaluate_grid(items, weights, tags_map, gods, builds_by_god, grid):
    results = []
    for sig in grid:
        w = copy.deepcopy(weights)
        w["signals"] = dict(sig)
        per_god, agg = validate.compute(items=items, weights=w, tags_map=tags_map,
                                        gods=gods, builds_by_god=builds_by_god)
        results.append({"signals": sig, "agg": agg, "per_god": per_god,
                        "objective": objective(agg)})
    return sorted(results, key=lambda r: -r["objective"])


def logo_winners(results):
    """Per held-out god: the signal combo that wins on the other gods. A top
    pick that flips wildly across folds is overfit — report, don't hide."""
    gods = sorted(results[0]["per_god"].keys()) if results else []
    out = {}
    for g in gods:
        best, best_obj = None, float("-inf")
        for r in results:
            sub = {k: v for k, v in r["per_god"].items() if k != g}
            if not sub:
                continue
            obj = objective(validate.aggregate(sub))
            if obj > best_obj:
                best, best_obj = r["signals"], obj
        out[g] = best
    return out


def write_report(results, logo, current, out_path, top_n=15):
    lines = ["# Signal-weight calibration", "",
             "Guardrails: efficiency+fit ≥ 0.50, pick ≤ 0.15, sum = 1. "
             "Objective = 0.5·norm(Spearman) + 0.5·coverage.", "",
             f"**Current hand weights:** {current}", "",
             "| eff | win | pick | fit | objective | Spearman | coverage |",
             "|---|---|---|---|---|---|---|"]
    for r in results[:top_n]:
        s = r["signals"]
        lines.append(f"| {s['efficiency']} | {s['win']} | {s['pick']} | {s['fit']} "
                     f"| {r['objective']:.3f} | {(r['agg']['pooled_spearman'] or 0):.2f} "
                     f"| {r['agg']['mean_coverage']:.0%} |")
    lines += ["", "## Leave-one-god-out winners", ""]
    lines += [f"- without {g}: {w}" for g, w in logo.items()]
    distinct = {tuple(sorted(w.items())) for w in logo.values() if w}
    lines += ["", f"**Stability:** {len(distinct)} distinct fold-winner(s) across "
              f"{len(logo)} folds — {'stable' if len(distinct) <= 3 else 'UNSTABLE, do not apply blindly'}."]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv=None):
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags_map = scoring.load_tags(recommend.TAGS_PATH)
    gods = recommend.load_gods()
    builds_by_god = {g["name"]: recommend.load_build_note(g["name"]) for g in gods}
    results = evaluate_grid(items, weights, tags_map, gods, builds_by_god, weight_grid())
    logo = logo_winners(results)
    out = recommend.DATA_ROOT / "Analysis" / "_calibration.md"
    write_report(results, logo, weights["signals"], out)
    best = results[0]
    print(f"Wrote {out}\nBest: {best['signals']} objective {best['objective']:.3f}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
```

- [ ] **Step 4: Run tests** (`python -m pytest smite/tests/test_calibrate.py smite/tests/test_validate.py -q`), then run the real thing: `python -m smite.calibrate` (expect a few minutes).
- [ ] **Step 5:** Read `_calibration.md`. **Only if** the top pick beats the current weights' objective AND the LOGO section says stable: apply the winning `signals:` to `_weights.yaml` (cite `_calibration.md` in a yaml comment), regenerate, re-validate, record in the metrics log. Otherwise keep hand weights and record why.
- [ ] **Step 6: Commit:**

```bash
git add tools/smite "04. System/Data/SMITE" "03. Workspaces/Gaming/SMITE 2/Builds" "docs/superpowers/plans/2026-07-22-smite-scoring-intelligence.md"
git commit -m "feat(smite): signal-weight calibration with guardrails + LOGO stability"
```

---

### Task 13: Stamp per-item score breakdowns into suggested entries

**Files:**
- Modify: `tools/smite/recommend.py` (`_build_entry_set`)
- Test: `tools/smite/tests/test_recommend.py`

- [ ] **Step 1: Write the failing test:**

```python
def test_suggested_entries_carry_slot_scores(tmp_items):
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
           "specializations": ["Sharpshooter"], "abilities": []}
    entries = recommend.build_suggested_entries(god, tmp_items, {"builds": []},
                                                scoring.load_weights_default(), {})
    core = entries[0]
    assert core["archetype"] == "core"
    for name in core["slot_order"]:
        s = core["slot_scores"][name]
        assert set(s) == {"total", "efficiency", "win", "pick", "fit"}
        assert 0.0 <= s["total"] <= 1.0
```

- [ ] **Step 2: verify failure. Step 3: implement** — in `_build_entry_set`, after `ordered` is computed:

```python
        by_name = {r["item"]: r for r in rows}
        slot_scores = {
            name: {k: round(by_name[name][k], 2)
                   for k in ("total", "efficiency", "win", "pick", "fit")}
            for name in ordered if name in by_name
        }
```

and add `"slot_scores": slot_scores,` to the appended entry dict.

- [ ] **Step 4:** Full suite green, regenerate notes, EOL cleanup.
- [ ] **Step 5: Commit** (code + tests + regenerated notes): `feat(smite): stamp slot_scores onto suggested entries`.

---

### Task 14: Viewer — types + score popover + fun badge + off-meta markers

**Files:**
- Modify: `viewer/src/types.ts`, `viewer/src/components/DetailPanel.tsx`
- Test: `viewer/src/components/DetailPanel.test.tsx`

- [ ] **Step 1: types.ts** — add and extend:

```ts
export interface SlotScore {
  total: number;
  efficiency: number;
  win: number;
  pick: number;
  fit: number;
}
```

and on `CuratedBuildEntry`:

```ts
  fun?: boolean;
  slot_scores?: Record<string, SlotScore>;
```

- [ ] **Step 2: Write failing vitest tests** (append to `DetailPanel.test.tsx`, following its existing fixture/render pattern — reuse its helpers for god/items/builds fixtures; the assertions that matter):

```tsx
it("shows the fun badge and rationale for fun builds", () => {
  // fixture: a suggested entry with fun: true, archetype "fun-crit"
  // render, click its tab
  expect(screen.getByText(/for fun/i)).toBeInTheDocument();
});

it("shows a why-this-item breakdown when slot_scores are present", async () => {
  // fixture entry with slot_scores for its first item; hover/point at the row
  // Tooltip content should include "fit" and the formatted score
  expect(await screen.findByText(/fit/i)).toBeInTheDocument();
});

it("marks suggested items missing from the community build as off-meta", () => {
  // fixture: community entry with items A,B; suggested entry with items B,C
  // C row shows the off-meta marker, B does not
  expect(screen.getByText(/off-meta/i)).toBeInTheDocument();
});
```

- [ ] **Step 3: Implement in DetailPanel.tsx:**

1. **Fun badge** — after the aspect banner block (`{aspectOn && aspectMeta && (...)}`), insert:

```tsx
      {!community && (active as CuratedBuildEntry).fun && (
        <div className="mb-3 rounded border border-premium/40 bg-bg1 p-2 text-xs">
          <span className="font-display font-semibold text-premium">For fun 🎲</span>
          <span className="text-muted"> — deliberately off-class; not scored against the meta.</span>
        </div>
      )}
```

(import `CuratedBuildEntry` and `SlotScore` from `../types`; if the `premium` color token doesn't exist in the Tailwind config, use the existing `gold` token instead — check `tailwind.config` first.)

2. **Tab dice** — in the tab button label: `{tabLabel(entry)}{(entry as CuratedBuildEntry).fun ? " 🎲" : ""}`.

3. **Why-this-item** — extend `ItemTooltipBody` with an optional score:

```tsx
function ScoreBar({ label, value }: { label: string; value: number }) {
  return (
    <div className="flex items-center gap-2">
      <span className="w-14 text-[10px] text-muted">{label}</span>
      <div className="h-1.5 flex-1 rounded bg-line">
        <div className="h-1.5 rounded bg-gold" style={{ width: `${Math.round(value * 100)}%` }} />
      </div>
      <span className="w-8 text-right font-mono text-[10px] text-ink">{value.toFixed(2)}</span>
    </div>
  );
}
```

and inside `ItemTooltipBody` (new prop `score?: SlotScore`), after the tags block:

```tsx
      {score && (
        <div className="mt-2 border-t border-line pt-2">
          <div className="mb-1 text-[10px] font-semibold tracking-widest text-muted">WHY THIS ITEM</div>
          <ScoreBar label="value" value={score.efficiency} />
          <ScoreBar label="win" value={score.win} />
          <ScoreBar label="pick" value={score.pick} />
          <ScoreBar label="fit" value={score.fit} />
        </div>
      )}
```

Pass it at the build-order row callsite: `content={<ItemTooltipBody item={item} name={slot.name} score={!community ? (active as CuratedBuildEntry).slot_scores?.[slot.name] : undefined} />}`.

4. **Off-meta marker** — before the return, compute:

```tsx
  const communityNames = new Set(
    note.builds.filter(isCommunityEntry).flatMap((b) => b.slot_order.map((s) => s.name)));
```

and in the row, next to the existing `flex` chip:

```tsx
                    {!community && active.source === "suggested" &&
                      !(active as CuratedBuildEntry).fun && communityNames.size > 0 &&
                      slot.status !== "added" && !communityNames.has(slot.name) && (
                      <span className="text-[10px] text-premium/80" title="Not in this god's top community items">off-meta</span>
                    )}
```

- [ ] **Step 4: Run tests + the real type gate:**

```bash
cd viewer && npx vitest run src/components/DetailPanel.test.tsx && npm run build
```

Expected: tests PASS, build clean (remember: `npm run build` is the only honest typecheck).

- [ ] **Step 5: Commit:** `git add viewer/src && git commit -m "feat(viewer): why-this-item popover, fun badge, off-meta markers"`.

---

### Task 15: Visual verification via Chrome MCP + polish pass

**Files:** whatever the screenshots reveal (viewer only)

- [ ] **Step 1:** Regenerate `viewer/public/index.json`: `cd tools && python -m smite.build_index` (module main). Start the dev server in the background (`cd viewer && npm run dev`, Bash `run_in_background: true`).
- [ ] **Step 2:** Drive a real browser via Chrome MCP (`mcp__claude-in-chrome__*` — the in-app browser pane hangs in this repo, don't use it): navigate to `http://localhost:5173/#/god/Ymir`, screenshot. Verify: fun-crit tab with 🎲, fun badge visible, crit items in slots, score popover renders on hover (use read_page/find to locate a slot row, hover, screenshot).
- [ ] **Step 3:** Same for a serious build (`#/god/Cernunnos`): off-meta markers appear only on non-community items; why-this-item bars look sane; nothing overflows.
- [ ] **Step 4:** Resize to mobile width (Chrome MCP resize_window) + toggle dark/light if the viewer supports it; screenshot each. Fix any layout breakage found (edit source, HMR, re-screenshot).
- [ ] **Step 5:** General polish sweep of `#/` and `#/items` at both widths — fix small rough edges found (each fix its own commit, message `fix(viewer): <what>`).
- [ ] **Step 6:** Kill the dev server. Final `npm run build`. Commit any remaining fixes + the regenerated `viewer/public/index.json`:

```bash
git add viewer && git commit -m "chore(viewer): regenerate index.json; polish from screenshot pass"
```

---

### Task 16: Final regeneration, full gates, finish the branch

- [ ] **Step 1:** Full pipeline from `tools/`: `python -m smite.recommend --all && python -m smite.validate && python -m smite.analysis && python -m smite.build_index`. EOL cleanup. Record FINAL metrics row.
- [ ] **Step 2:** All gates: `cd tools && python -m pytest smite/tests/ -q` and `cd viewer && npm run build`.
- [ ] **Step 3:** Confirm the metrics log shows the final numbers ≥ baseline (coverage/win-weighted/Spearman) and each kept change's contribution is traceable. If any final number is below baseline, that's a stop-and-investigate, not a ship.
- [ ] **Step 4:** Commit remaining artifacts; then invoke superpowers:finishing-a-development-branch (merge to main after `git fetch`/integrate — the 30-min cron commits on main — push promptly).
