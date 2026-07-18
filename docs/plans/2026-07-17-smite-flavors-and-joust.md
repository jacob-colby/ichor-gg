# SMITE 2 Build Flavors + Joust Mode Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add themed suggested-build variants (crit/burst/bruiser/anti-tank, gated per god) and a Joust mode (tunable profile, no meta data) to the recommender, surfaced in the viewer via a mode toggle + flavor tabs.

**Architecture:** Flavors and modes are *scoring overlays* on the existing scorer. A build is `(mode, flavor)`: the mode profile overrides signal weights + adds tag bonuses; the flavor adds stat-weight overlays + tag bonuses + a lifesteal cap. All new params are optional/backward-compatible. Build notes split per mode; the viewer groups by mode and labels suggested builds by archetype.

**Tech Stack:** Python 3.10 (pytest), Vite + React 19 + TS + Vitest + RTL.

**Reference spec:** [2026-07-17-smite-build-flavors-and-joust-design.md](../specs/2026-07-17-smite-build-flavors-and-joust-design.md)

---

## File Structure

**Pipeline (modify):**
- `tools/smite/scoring.py` — `eligible_flavors`, `_god_tokens`, overlay params on `god_fit_score`/`signal_score`, `resolve_profile`, `profile` param on `score_god_items`.
- `tools/smite/assemble.py` — `assemble_core` `bruiser` → `max_lifesteal`.
- `tools/smite/recommend.py` — `build_suggested_entries` mode+flavor aware; `--all` writes per-mode notes.
- `04. System/Data/SMITE/_weights.yaml` — add `flavors` + `modes` sections.

**Viewer (modify):**
- `viewer/src/lib/builds.ts` — `tabLabel` helper.
- `viewer/src/components/DetailPanel.tsx` — mode toggle + archetype tab labels.
- `viewer/src/App.tsx` — mode state (persists across god changes).

**No change needed:** `notes.merge_suggested_entries` (already replaces the full suggested set in a note, creating it if missing), `build_index.py` (globs all Build notes → both mode files flow in), `viewer/src/types.ts` (`BuildNote.mode` and `archetype?` already exist).

---

## PHASE F — Recommender (flavors + modes)

### Task F1: `eligible_flavors` + `_god_tokens`

**Files:**
- Modify: `tools/smite/scoring.py`
- Test: `tools/smite/tests/test_scoring.py`

Match flavors against the god's tokenized role+specs. Real vocabulary: `role` like "Mid"/"Carry Jungle"/"Solo"; `specializations` like "Nuker"/"Sharpshooter"/"Burst Damage".

- [ ] **Step 1: Write the failing test** (append)

```python
def test_eligible_flavors_gates_by_damage_type_and_tokens():
    weights = scoring.load_weights_default()
    weights["flavors"] = {
        "crit": {"damage_types": ["physical"], "match_any": ["Carry", "Sharpshooter"]},
        "burst": {"damage_types": None, "match_any": ["Nuker", "Burst", "Slayer", "Sniper", "Mid"]},
        "bruiser": {"damage_types": None, "match_any": None},
        "anti-tank": {"damage_types": None, "match_any": None},
    }
    chiron = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
              "specializations": ["Sharpshooter", "Nuker"]}
    ra = {"name": "Ra", "damage_type": "magical", "role": "Mid",
          "specializations": ["Sniper", "Healing"]}
    herc = {"name": "Hercules", "damage_type": "physical", "role": "Solo",
            "specializations": ["Tank", "Brawler", "Lockdown"]}
    assert set(scoring.eligible_flavors(chiron, weights)) == {"crit", "burst", "bruiser", "anti-tank"}
    assert set(scoring.eligible_flavors(ra, weights)) == {"burst", "bruiser", "anti-tank"}   # no crit (magical)
    assert set(scoring.eligible_flavors(herc, weights)) == {"bruiser", "anti-tank"}          # no crit/burst
```

- [ ] **Step 2: Run and confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -k eligible_flavors -v`

- [ ] **Step 3: Implement** (append to `scoring.py`)

```python
def _god_tokens(god):
    """Every whitespace-separated token across the god's role + specializations,
    for matching flavor eligibility against the real lane/spec vocabulary."""
    toks = set()
    for spec in (god.get("specializations") or []):
        toks.update(str(spec).split())
    toks.update(str(god.get("role") or "").split())
    return toks


def eligible_flavors(god, weights):
    """Flavor names whose damage_types (or null=any) include the god's damage
    type, and whose match_any (or null=any) intersects the god's token set."""
    out = []
    for name, f in (weights.get("flavors") or {}).items():
        dts = f.get("damage_types")
        if dts and god.get("damage_type") not in dts:
            continue
        match_any = f.get("match_any")
        if match_any and not (_god_tokens(god) & set(match_any)):
            continue
        out.append(name)
    return out
```

- [ ] **Step 4: Run and confirm PASS**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -v`

- [ ] **Step 5: Commit**

```bash
git add tools/smite/scoring.py tools/smite/tests/test_scoring.py
git commit -m "feat(smite): eligible_flavors gates flavors per god archetype"
```

---

### Task F2: Scoring overlays — fit/signal params, `resolve_profile`, `score_god_items` profile

**Files:**
- Modify: `tools/smite/scoring.py`
- Test: `tools/smite/tests/test_scoring.py`

Add optional overlay params (all default to current behavior). `resolve_profile` composes a mode profile ⊕ flavor into `{signals, stat_overlay, tag_bonus, max_lifesteal, suppress_underrated, label, flavor}`. `score_god_items` gains a `profile` param.

- [ ] **Step 1: Write the failing tests** (append)

```python
def test_god_fit_stat_overlay_and_tag_bonus():
    weights = scoring.load_weights_default()
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
           "specializations": ["Sharpshooter"]}
    crit_item = {"stats": {"Critical Chance": "20%"}}
    # With a crit stat_overlay, a pure-crit item scores higher fit than with the
    # base role map alone.
    base = scoring.god_fit_score(crit_item, god, weights, [])
    boosted = scoring.god_fit_score(crit_item, god, weights, [],
                                    stat_overlay={"Critical Chance": 3.0})
    assert boosted >= base
    # A negative tag_bonus (e.g. Joust penalizing wave-clear) lowers fit, floored at 0.
    penalized = scoring.god_fit_score({"stats": {"Strength": "40"}}, god, weights,
                                      ["wave-clear"], tag_bonus={"wave-clear": -0.15})
    assert penalized >= 0.0


def test_resolve_profile_composes_mode_and_flavor():
    weights = scoring.load_weights_default()
    weights["modes"] = {"joust": {"signals": {"win": 0.0, "pick": 0.0},
                                  "tag_bonus": {"sustain": 0.25}, "label": "Joust profile"}}
    weights["flavors"] = {"bruiser": {"stats": {"Health": 1.0}, "tag_bonus": {"sustain": 0.3},
                                      "max_lifesteal": 2}}
    p = scoring.resolve_profile(weights, "Joust", "bruiser")
    assert p["signals"]["win"] == 0.0 and p["signals"]["pick"] == 0.0
    assert p["signals"]["efficiency"] == weights["signals"]["efficiency"]  # unspecified kept
    assert p["stat_overlay"] == {"Health": 1.0}
    assert p["tag_bonus"]["sustain"] == 0.3   # flavor wins over mode on the same tag
    assert p["max_lifesteal"] == 2
    assert p["suppress_underrated"] is True    # pick zeroed
    assert p["label"] == "Joust profile"


def test_score_god_items_profile_suppresses_underrated():
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry", "specializations": ["Sharpshooter"]}
    items = [{"name": "A", "tier": 3, "stats": {"Strength": "40"}},
             {"name": "B", "tier": 3, "stats": {"Strength": "40"}}]
    eff = {n: {"score": 0.5, "tier": "fair"} for n in ["A", "B"]}
    weights = scoring.load_weights_default()
    profile = {"signals": {**weights["signals"], "win": 0.0, "pick": 0.0}, "suppress_underrated": True}
    rows = scoring.score_god_items(god, items, {"builds": []}, eff, weights, {}, profile=profile)
    assert all(r["underrated"] is False for r in rows)
```

- [ ] **Step 2: Run and confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -k "overlay or resolve_profile or profile_suppresses" -v`

- [ ] **Step 3: Implement** — edit `scoring.py`:

(a) Replace `god_fit_score` with (adds `stat_overlay`, `tag_bonus`, both defaulting to `None`; clamps to [0,1]):
```python
def god_fit_score(item, god, weights, item_tags, stat_overlay=None, tag_bonus=None):
    """Archetype fit in [0,1]: weighted presence of role-relevant stats, plus a
    small bonus for archetype-relevant tags. An optional stat_overlay (flavor
    weights, which win over the god's role map) and tag_bonus (per-tag deltas,
    may be negative) skew the fit. NOT damage simulation — see spec."""
    stats = item.get("stats") or {}
    role_map = _role_stat_map(god, weights)
    if stat_overlay:
        role_map = {**role_map, **stat_overlay}
    denom = sum(role_map.values()) or 1.0
    stat_fit = 0.0
    for stat, w in role_map.items():
        if parse_stat_value(stats.get(stat)) is not None:
            stat_fit += w
    stat_fit = min(stat_fit / denom, 1.0)

    offense_tags = {"burst", "execute", "protection-shred"}
    bonus = 0.1 if any(t in offense_tags for t in (item_tags or [])) else 0.0
    if tag_bonus:
        for t in (item_tags or []):
            bonus += tag_bonus.get(t, 0.0)
    return max(0.0, min(stat_fit + bonus, 1.0))
```

(b) Replace `signal_score` signature/body to thread the overlays into fit (rest unchanged):
```python
def signal_score(item, god, god_build, eff_score, weights, item_tags,
                 stat_overlay=None, tag_bonus=None):
    w = weights["signals"]
    pick, win = lookup_rates(god_build, item["name"])
    win_norm = win if win is not None else 0.5
    fit = god_fit_score(item, god, weights, item_tags, stat_overlay, tag_bonus)
    total = (w["efficiency"] * eff_score + w["win"] * win_norm
             + w["pick"] * pick + w["fit"] * fit)
    quality = (w["efficiency"] * eff_score + w["fit"] * fit) / ((w["efficiency"] + w["fit"]) or 1.0)
    return {"item": item["name"], "efficiency": eff_score, "win": win_norm,
            "pick": pick, "fit": fit, "quality": quality, "total": total,
            "tags": list(item_tags or [])}
```

(c) Add `resolve_profile`:
```python
def resolve_profile(weights, mode="Conquest", flavor=None):
    """Compose a mode profile ⊕ flavor into an effective scoring overlay. Mode
    sets signal-weight overrides + tag bonuses; flavor adds stat weights + tag
    bonuses (flavor wins on a shared tag) + a lifesteal cap. suppress_underrated
    is true when the mode zeroes the pick signal (underrated needs pick data)."""
    mode_prof = (weights.get("modes") or {}).get(mode.lower(), {}) or {}
    fl = ((weights.get("flavors") or {}).get(flavor) or {}) if flavor else {}
    signals = {**weights["signals"], **(mode_prof.get("signals") or {})}
    tag_bonus = {**(mode_prof.get("tag_bonus") or {}), **(fl.get("tag_bonus") or {})}
    return {
        "signals": signals,
        "stat_overlay": fl.get("stats") or {},
        "tag_bonus": tag_bonus,
        "max_lifesteal": fl.get("max_lifesteal", 1),
        "suppress_underrated": signals.get("pick", 1) == 0,
        "label": mode_prof.get("label"),
        "flavor": flavor,
    }
```

(d) Replace `score_god_items` to accept `profile=None`:
```python
def score_god_items(god, items, god_build, efficiency_scores_map, weights, tags_map, profile=None):
    """Score every buildable, damage-filter-passing item for one god, ranked by
    total descending. An optional profile (from resolve_profile) applies mode
    signal overrides + stat/tag overlays and can suppress the underrated flag."""
    profile = profile or {}
    eff_weights = weights
    if profile.get("signals"):
        eff_weights = _deep_merge(weights, {"signals": profile["signals"]})
    stat_overlay = profile.get("stat_overlay")
    tag_bonus = profile.get("tag_bonus")

    rows = []
    for item in items:
        if not is_buildable(item):
            continue
        if not passes_damage_filter(item, god):
            continue
        eff = efficiency_scores_map.get(item["name"], {}).get("score", 0.5)
        row = signal_score(item, god, god_build, eff, eff_weights,
                           tags_map.get(item["name"], []), stat_overlay, tag_bonus)
        row["tier"] = efficiency_scores_map.get(item["name"], {}).get("tier", "fair")
        rows.append(row)

    if profile.get("suppress_underrated"):
        for r in rows:
            r["underrated"] = False
    else:
        mark_underrated(rows, weights)
    return sorted(rows, key=lambda r: -r["total"])
```

- [ ] **Step 4: Run the FULL scoring test file, confirm ALL PASS** (existing + new — the defaults keep old callers identical)

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -v`

- [ ] **Step 5: Commit**

```bash
git add tools/smite/scoring.py tools/smite/tests/test_scoring.py
git commit -m "feat(smite): scoring overlays for modes + flavors"
```

---

### Task F3: `assemble_core` lifesteal cap

**Files:**
- Modify: `tools/smite/assemble.py`
- Test: `tools/smite/tests/test_assemble.py`

Generalize the `bruiser` boolean to a `max_lifesteal` count so a bruiser flavor can allow 2 lifesteal items.

- [ ] **Step 1: Write the failing test** (append)

```python
def test_assemble_core_respects_max_lifesteal():
    rows = [_row("LS1", 0.9, tags=["sustain"]), _row("LS2", 0.85, tags=["sustain"]),
            _row("A", 0.8), _row("B", 0.7), _row("C", 0.6), _row("D", 0.5), _row("E", 0.4)]
    ibn = _items_by_name(
        {"name": "LS1", "stats": {"Strength": "30"}}, {"name": "LS2", "stats": {"Strength": "30"}},
        {"name": "A", "stats": {"Strength": "40"}}, {"name": "B", "stats": {"Strength": "40"}},
        {"name": "C", "stats": {"Strength": "40"}}, {"name": "D", "stats": {"Strength": "40"}},
        {"name": "E", "stats": {"Strength": "40"}},
    )
    one = assemble.assemble_core(rows, ibn, n=6, max_lifesteal=1)
    assert sum(1 for x in one if x in {"LS1", "LS2"}) == 1
    two = assemble.assemble_core(rows, ibn, n=6, max_lifesteal=2)
    assert sum(1 for x in two if x in {"LS1", "LS2"}) == 2
```

- [ ] **Step 2: Run and confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_assemble.py -k max_lifesteal -v`
(Fails: `assemble_core` has no `max_lifesteal` kwarg.)

- [ ] **Step 3: Replace `assemble_core`**

```python
def assemble_core(rows, items_by_name, n=6, max_lifesteal=1):
    """Highest-total items filling n slots: at most one boots, at most
    `max_lifesteal` lifesteal/sustain items, no duplicates. rows must be
    pre-sorted by -total (score_god_items already does)."""
    core, used = [], set()
    have_boots = False
    lifesteal_count = 0
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
        is_ls = _is_lifesteal(item, r.get("tags"))
        if is_ls and lifesteal_count >= max_lifesteal:
            continue
        if is_ls:
            lifesteal_count += 1
        core.append(name)
        used.add(name)
    return core
```

- [ ] **Step 4: Run the FULL assemble test file, confirm ALL PASS** (the old default `bruiser=False` == `max_lifesteal=1`; check no existing test passed `bruiser=` — if one does, update it to `max_lifesteal=`)

Run: `cd tools && python -m pytest smite/tests/test_assemble.py -v`

- [ ] **Step 5: Commit**

```bash
git add tools/smite/assemble.py tools/smite/tests/test_assemble.py
git commit -m "feat(smite): assemble_core max_lifesteal cap (generalizes bruiser)"
```

---

### Task F4: `_weights.yaml` flavor + mode config

**Files:**
- Modify: `04. System/Data/SMITE/_weights.yaml`

- [ ] **Step 1: Append `flavors` + `modes` sections** to `04. System/Data/SMITE/_weights.yaml`

```yaml

# ── Build flavors ─────────────────────────────────────────────────────────
# Each flavor is a scoring overlay producing an extra "suggested" build. It's
# emitted only for gods whose damage type is in `damage_types` (null = any) and
# whose tokenized role+specs intersect `match_any` (null = any). `stats` skews
# god-fit; `tag_bonus` rewards tagged items; `max_lifesteal` caps sustain items.
flavors:
  crit:
    damage_types: [physical]
    match_any: [Carry, Sharpshooter]
    stats: {Critical Chance: 1.5, Attack Speed: 1.2, Strength: 0.8}
    max_lifesteal: 1
  burst:
    damage_types: null
    match_any: [Nuker, Burst, Slayer, Sniper, Mid]
    stats: {Strength: 1.0, Intelligence: 1.0, Penetration: 1.5, Cooldown Rate: 1.0}
    max_lifesteal: 1
  bruiser:
    damage_types: null
    match_any: null
    stats: {Health: 1.0, Physical Protection: 0.8, Magical Protection: 0.8}
    tag_bonus: {sustain: 0.3}
    max_lifesteal: 2
  anti-tank:
    damage_types: null
    match_any: null
    stats: {Penetration: 2.0}
    tag_bonus: {protection-shred: 0.3}
    max_lifesteal: 1

# ── Game modes ────────────────────────────────────────────────────────────
# `conquest` is the default (empty = no overlay, meta-backed). `joust` drops the
# win/pick signals (SmiteBrain has no Joust data) and reweights toward what wins
# on a single lane: sustain / anti-heal / aura up, wave-clear / mobility down.
modes:
  conquest: {}
  joust:
    signals: {efficiency: 0.5, win: 0.0, pick: 0.0, fit: 0.5}
    tag_bonus: {sustain: 0.25, anti-heal: 0.3, aura: 0.2, wave-clear: -0.15, mobility: -0.1}
    label: "Joust — math + mode profile (no meta win/pick data)"
```

- [ ] **Step 2: Verify it loads + eligibility works on real gods**

Run: `cd tools && python -c "
from smite import scoring, recommend
w = scoring.load_weights(recommend.WEIGHTS_PATH)
for g in recommend.load_gods():
    print(g['name'], scoring.eligible_flavors(g, w))
"`
Expected: crit only on physical carries (Chiron, Cernunnos, Ullr); burst on all but Hercules; bruiser+anti-tank on all. Note anything surprising.

- [ ] **Step 3: Commit**

```bash
git add "04. System/Data/SMITE/_weights.yaml"
git commit -m "feat(smite): flavor + Joust mode profiles in _weights.yaml"
```

---

### Task F5: `recommend` mode + flavor builds

**Files:**
- Modify: `tools/smite/recommend.py`
- Test: `tools/smite/tests/test_recommend.py`

`build_suggested_entries` becomes mode+flavor aware (core + eligible flavors). `--all` writes `<god>-Conquest.md` and `<god>-Joust.md`.

- [ ] **Step 1: Write the failing test** (append)

```python
def test_build_suggested_entries_emits_core_plus_flavors():
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
           "specializations": ["Sharpshooter", "Nuker"]}
    items = [
        {"name": "Crit1", "tier": 3, "cost": 2000, "stats": {"Critical Chance": "20%", "Strength": "40"}},
        {"name": "Pen1", "tier": 3, "cost": 2000, "stats": {"Strength": "40", "Penetration": "15"}},
        {"name": "A", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "B", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "C", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "D", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
        {"name": "E", "tier": 3, "cost": 2500, "stats": {"Strength": "55"}},
    ]
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    entries = recommend.build_suggested_entries(god, items, {"builds": []}, weights, {}, "Conquest")
    archetypes = [e["archetype"] for e in entries]
    assert archetypes[0] == "core"
    assert set(archetypes) >= {"core", "crit", "burst", "bruiser", "anti-tank"}
    assert all(e["source"] == "suggested" and e["slot_order"] for e in entries)


def test_build_suggested_entries_joust_omits_underrated_and_labels():
    god = {"name": "Ra", "damage_type": "magical", "role": "Mid", "specializations": ["Sniper"]}
    items = [{"name": f"I{i}", "tier": 3, "cost": 2500, "stats": {"Intelligence": "70"}} for i in range(7)]
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    entries = recommend.build_suggested_entries(god, items, {"builds": []}, weights, {}, "Joust")
    core = next(e for e in entries if e["archetype"] == "core")
    assert "Underrated" not in core["rationale"]         # suppressed (no pick data)
    assert "no meta" in core["rationale"].lower()         # profile label present
    assert "crit" not in [e["archetype"] for e in entries]  # Ra is magical
```

- [ ] **Step 2: Run and confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -k "core_plus_flavors or joust_omits" -v`

- [ ] **Step 3: Implement** — edit `recommend.py`:

(a) Add near the top (after `BUILDS_ROOT`):
```python
MODES = ["Conquest", "Joust"]

_FLAVOR_BLURB = {
    "core": "Top weighted-score core",
    "crit": "Crit / auto-attack skew",
    "burst": "Ability / burst skew",
    "bruiser": "Lifesteal bruiser skew",
    "anti-tank": "Full-penetration anti-tank skew",
}


def _rationale(archetype, rows, profile):
    meta = "" if profile.get("suppress_underrated") else " + win/pick"
    text = f"{_FLAVOR_BLURB.get(archetype, archetype)} (efficiency + fit{meta})."
    if profile.get("label"):
        text += f" {profile['label']}."
    if not profile.get("suppress_underrated"):
        underrated = [r["item"] for r in rows if r.get("underrated")]
        if underrated:
            text += " Underrated for this god: " + ", ".join(underrated) + "."
    return text
```

(b) Replace `build_suggested_entries`:
```python
def build_suggested_entries(god, items, god_build, weights, tags_map, mode="Conquest"):
    eff_scores, _ = efficiency.efficiency_scores(items)
    items_by_name = {it["name"]: it for it in items}
    entries = []
    for flavor in [None] + scoring.eligible_flavors(god, weights):
        profile = scoring.resolve_profile(weights, mode, flavor)
        rows = scoring.score_god_items(god, items, god_build, eff_scores, weights, tags_map, profile)
        core = assemble.assemble_core(rows, items_by_name, n=6, max_lifesteal=profile["max_lifesteal"])
        swaps = assemble.situational_swaps(rows, items_by_name, tags_map, core=core)
        archetype = flavor or "core"
        entries.append({
            "source": "suggested",
            "archetype": archetype,
            "slot_order": core,
            "situational_swaps": swaps,
            "rationale": _rationale(archetype, rows, profile),
        })
    return entries
```

(c) In the `--all` branch, replace the single Conquest write with a per-mode loop. The god report stays Conquest-based. Replace:
```python
            if not args.report_only:
                entries = build_suggested_entries(god, items, build, weights, tags_map)
                notes.merge_suggested_entries(
                    BUILDS_ROOT / f"{god['name']}-Conquest.md", god["name"], "Conquest", entries)
```
with:
```python
            if not args.report_only:
                for mode in MODES:
                    # Conquest uses the community build note for win/pick lookups;
                    # Joust has no community data (SmiteBrain is Conquest-only).
                    mode_build = build if mode == "Conquest" else {"builds": []}
                    entries = build_suggested_entries(god, items, mode_build, weights, tags_map, mode)
                    notes.merge_suggested_entries(
                        BUILDS_ROOT / f"{god['name']}-{mode}.md", god["name"], mode, entries)
```
(`build` is the already-loaded Conquest note from `load_build_note(god["name"])` above in the loop.)

- [ ] **Step 4: Run and confirm PASS**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -v`

- [ ] **Step 5: Commit**

```bash
git add tools/smite/recommend.py tools/smite/tests/test_recommend.py
git commit -m "feat(smite): recommend emits per-mode core + flavor builds"
```

---

### Task F6: Full regen + verify + commit generated

**Files:** generated — `Builds/*.md` (incl. new `*-Joust.md`), `viewer/public/index.json`, `Analysis/*.md`

- [ ] **Step 1: Regenerate**

Run (from `tools/`):
```bash
python -m smite.recommend --all
python -m smite.build_index
```

- [ ] **Step 2: Verify the generated data**

Run: `cd .. && python -c "
import json
d=json.load(open('viewer/public/index.json',encoding='utf-8'))
bykey={(n['god'], n['mode']): n for n in d['builds']}
# every god has a Conquest and a Joust note
gods={g['name'] for g in d['gods']}
for g in sorted(gods):
    con=bykey.get((g,'Conquest')); jou=bykey.get((g,'Joust'))
    assert con and jou, f'{g} missing a mode note'
    con_arch=[b.get('archetype') for b in con['builds'] if b['source']=='suggested']
    jou_arch=[b.get('archetype') for b in jou['builds'] if b['source']=='suggested']
    assert con_arch[0]=='core' and jou_arch[0]=='core'
    print(f\"{g:14} Conquest={con_arch}  Joust={jou_arch}\")
# Joust builds never claim 'underrated'
for n in d['builds']:
    if n['mode']=='Joust':
        for b in n['builds']:
            assert 'Underrated' not in b.get('rationale',''), f\"{n['god']} Joust rationale leaks underrated\"
print('OK')
"`
Expected: each god prints its Conquest + Joust archetype lists (core + eligible flavors), crit only on physical carries, no Joust underrated. Eyeball a couple: do the flavor builds visibly differ from core?

- [ ] **Step 3: Full Python suite green**

Run: `cd tools && python -m pytest smite/tests/ -q -m "not live"`

- [ ] **Step 4: Commit generated output**

```bash
git add "03. Workspaces/Gaming/SMITE 2/Builds/" "04. System/Data/SMITE/Analysis/" viewer/public/
git commit -m "chore(smite): regenerate per-mode flavor builds + index"
```

---

## PHASE VW — Viewer (mode toggle + flavor tabs)

### Task VW1: `tabLabel` helper

**Files:**
- Modify: `viewer/src/lib/builds.ts`
- Test: `viewer/src/lib/builds.test.ts`

- [ ] **Step 1: Write the failing test** (append; extend the existing `./builds` import to include `tabLabel`)

```typescript
import { tabLabel } from "./builds";

describe("tabLabel", () => {
  it("labels a suggested entry by its archetype", () => {
    expect(tabLabel({ source: "suggested", archetype: "crit", slot_order: [] } as any)).toBe("crit");
  });
  it("falls back to source for community/mine", () => {
    expect(tabLabel({ source: "community", slot_order: [] } as any)).toBe("community");
    expect(tabLabel({ source: "mine", slot_order: [] } as any)).toBe("mine");
  });
  it("falls back to 'suggested' when a suggested entry has no archetype", () => {
    expect(tabLabel({ source: "suggested", slot_order: [] } as any)).toBe("suggested");
  });
});
```

- [ ] **Step 2: Run and confirm FAIL**

Run: `cd viewer && npx vitest run src/lib/builds.test.ts`

- [ ] **Step 3: Implement** (append to `builds.ts`)

```typescript
import type { BuildEntry } from "../types";

/** Tab label for a build entry: suggested builds show their archetype
 * (Core / Crit / Burst / …); community and mine show their source. */
export function tabLabel(entry: BuildEntry): string {
  if (entry.source === "suggested") return entry.archetype ?? "suggested";
  return entry.source;
}
```
(If `BuildEntry` is already imported at the top of `builds.ts`, add `tabLabel` to the existing import rather than duplicating it.)

- [ ] **Step 4: Run and confirm PASS + typecheck**

Run: `cd viewer && npx vitest run src/lib/builds.test.ts && npx tsc --noEmit`

- [ ] **Step 5: Commit**

```bash
git add viewer/src/lib/builds.ts viewer/src/lib/builds.test.ts
git commit -m "feat(viewer): tabLabel helper for archetype-labeled tabs"
```

---

### Task VW2: Mode toggle + flavor tabs

**Files:**
- Modify: `viewer/src/App.tsx`, `viewer/src/components/DetailPanel.tsx`
- Test: `viewer/src/components/DetailPanel.test.tsx`

Mode state lives in `App` (persists across god changes). `DetailPanel` picks the note matching the mode, renders a mode toggle (from the god's available modes), and labels tabs via `tabLabel`.

- [ ] **Step 1: Update `App.tsx`** — add mode state and pass it down

Add `const [mode, setMode] = useState("Conquest");` next to `selectedGod`, and pass to DetailPanel:
```tsx
  <DetailPanel
    god={selectedGod}
    godData={data.gods.find((g) => g.name === selectedGod)}
    items={data.items}
    builds={data.builds}
    mode={mode}
    onModeChange={setMode}
  />
```
(Do NOT reset `mode` when `selectedGod` changes — it persists by design.)

- [ ] **Step 2: Write the failing test** (append to `DetailPanel.test.tsx`; existing tests pass `god/godData/items/builds` — add `mode="Conquest"` and `onModeChange={()=>{}}` to those calls too)

```tsx
it("switches build set when the mode toggle changes", () => {
  const builds = [
    { type: "smite-build", god: "Chiron", mode: "Conquest",
      builds: [{ source: "suggested", archetype: "core", slot_order: ["ConItem"], situational_swaps: [], rationale: "c" }] },
    { type: "smite-build", god: "Chiron", mode: "Joust",
      builds: [{ source: "suggested", archetype: "core", slot_order: ["JoustItem"], situational_swaps: [], rationale: "j" }] },
  ];
  function Harness() {
    const [mode, setMode] = React.useState("Conquest");
    return <DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode={mode} onModeChange={setMode} />;
  }
  render(<Harness />);
  expect(screen.getByText("ConItem")).toBeInTheDocument();
  fireEvent.click(screen.getByRole("button", { name: /joust/i }));
  expect(screen.getByText("JoustItem")).toBeInTheDocument();
});

it("labels suggested tabs by archetype", () => {
  const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
    { source: "suggested", archetype: "core", slot_order: ["X"], situational_swaps: [], rationale: "" },
    { source: "suggested", archetype: "crit", slot_order: ["Y"], situational_swaps: [], rationale: "" },
  ] }];
  render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                      mode="Conquest" onModeChange={() => {}} />);
  expect(screen.getByRole("tab", { name: /crit/i })).toBeInTheDocument();
});
```
(Add `import React from "react";` if the test file doesn't already import it.)

- [ ] **Step 3: Run and confirm FAIL**

Run: `cd viewer && npx vitest run src/components/DetailPanel.test.tsx`

- [ ] **Step 4: Edit `DetailPanel.tsx`**

(a) Props + imports:
```tsx
import { isCommunityEntry, slotItemName, iconSlug, applySwap, tabLabel } from "../lib/builds";
```
```tsx
interface DetailPanelProps {
  god: string;
  godData?: God;
  items: Item[];
  builds: BuildNote[];
  mode: string;
  onModeChange: (mode: string) => void;
}
```
(b) At the top of the component body, replace the single `note` lookup with mode-aware selection:
```tsx
export function DetailPanel({ god, godData, items, builds, mode, onModeChange }: DetailPanelProps) {
  const godNotes = builds.filter((b) => b.god === god);
  const note = godNotes.find((n) => n.mode === mode) ?? godNotes[0];
  const modes = godNotes.map((n) => n.mode);
  const [activeIndex, setActiveIndex] = useState(0);
  const [selectedTag, setSelectedTag] = useState<string | null>(null);
  // ...itemsByName useMemo unchanged...

  useEffect(() => {
    setActiveIndex(0);
    setSelectedTag(null);
  }, [god, note]);   // note identity changes on god OR mode change
```
(c) In the header row, add the mode toggle before/after the mode badge (replace the static `note.mode` badge with the segmented toggle when there's more than one mode):
```tsx
        <div className="ml-auto flex overflow-hidden rounded-md border border-line">
          {modes.map((m) => (
            <button
              key={m}
              type="button"
              onClick={() => onModeChange(m)}
              className={`px-3 py-1 font-display text-xs font-semibold tracking-wide ${
                m === (note?.mode ?? mode) ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"
              }`}
            >
              {m}
            </button>
          ))}
        </div>
```
(d) In the source-tab row, label by `tabLabel(entry)` instead of `entry.source`:
```tsx
            {tabLabel(entry)}
```
Everything else (slot order, item tooltips, swap diff, rationale) is unchanged.

Guard the empty case: if `!note`, keep the existing `No build data yet for {god}` message.

- [ ] **Step 5: Run tests + typecheck, confirm PASS**

Run: `cd viewer && npx vitest run && npx tsc --noEmit`
Fix any existing DetailPanel test that needs the new `mode`/`onModeChange` props (add them; keep assertions intact).

- [ ] **Step 6: Commit**

```bash
git add viewer/src/App.tsx viewer/src/components/DetailPanel.tsx viewer/src/components/DetailPanel.test.tsx
git commit -m "feat(viewer): mode toggle + archetype-labeled flavor tabs"
```

---

### Task VW3: Full suite + browser verification

**Files:** none (verification)

- [ ] **Step 1: Both suites green**

Run: `cd viewer && npx vitest run` and `cd ../tools && python -m pytest smite/tests/ -q -m "not live"`.

- [ ] **Step 2: Browser verify**

Start the dev server and drive the browser: select a god, confirm (a) the mode toggle shows Conquest | Joust and switching it swaps the build set, (b) suggested tabs are labeled Core / Crit / Burst / Bruiser / Anti-tank and only god-appropriate flavors appear (a mage shows no Crit), (c) each flavor tab shows a visibly different core, (d) Joust rationale shows the "no meta data" label and no underrated claim, (e) the mode persists when you click a different god. Capture a screenshot. Fix any issues and re-verify.

- [ ] **Step 3: Commit any fixes**

```bash
git add viewer/src
git commit -m "polish(viewer): flavor/mode browser-verification fixes"
```
(Skip if none needed.)

---

## Self-Review

**Spec coverage:** flavor eligibility (F1), scoring overlays + profile composition + underrated suppression (F2), lifesteal cap for bruiser (F3), tunable flavor/mode config (F4), per-mode core+flavor emission (F5), regen (F6), viewer tab labels (VW1), mode toggle + flavor tabs + persistence (VW2), verification (VW3). Every spec section maps to a task.

**Placeholder scan:** none — all code complete; the one judgment step (do flavor builds visibly differ) is a verification eyeball, not a code gap.

**Type/name consistency:** `resolve_profile(weights, mode, flavor)` → `{signals, stat_overlay, tag_bonus, max_lifesteal, suppress_underrated, label, flavor}` consumed by `score_god_items(…, profile)` (F2) and `build_suggested_entries` (F5). `eligible_flavors(god, weights)` (F1) used in F5. `assemble_core(…, max_lifesteal)` (F3) called in F5 with `profile["max_lifesteal"]`. `_weights.yaml` keys (`flavors.<name>.{damage_types,match_any,stats,tag_bonus,max_lifesteal}`, `modes.<mode>.{signals,tag_bonus,label}`) match what `resolve_profile`/`eligible_flavors` read (F4). Viewer: `tabLabel(entry)` (VW1) used in DetailPanel (VW2); `mode`/`onModeChange` props threaded from App (VW2). All new Python params default to current behavior so existing tests stay green.

**Backward-compat note:** `score_god_items`, `god_fit_score`, `signal_score` all gain optional trailing params defaulting to `None`; `assemble_core`'s `bruiser` becomes `max_lifesteal=1` (same default behavior). Existing callers/tests unaffected — F2/F3 steps verify the full prior suite still passes.
