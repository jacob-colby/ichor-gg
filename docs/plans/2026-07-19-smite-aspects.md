# God Aspects Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Factor god aspects into build suggestions via tunable overlays, add a per-god Aspect toggle that swaps the suggested builds to aspect-tuned versions, and display what the aspect does.

**Architecture:** Python — `resolve_profile` composes mode ⊕ aspect ⊕ flavor; `build_suggested_entries` emits a parallel `aspect`-tagged suggested set for gods with an aspect overlay. Viewer — DetailPanel shows an Aspect toggle that filters suggested tabs to the aspect set and reveals a kit-change banner (from existing `God.aspects`).

**Tech Stack:** Python 3.10 (pytest), Vite + React 19 + TS + Vitest + RTL.

**Reference spec:** [2026-07-19-smite-aspects-design.md](../specs/2026-07-19-smite-aspects-design.md)

---

## File Structure
- `04. System/Data/SMITE/_weights.yaml` — `aspects` block (modify).
- `tools/smite/scoring.py` — `resolve_profile(..., aspect_overlay=None)` (modify).
- `tools/smite/recommend.py` — emit aspect-tagged suggested set (modify).
- `viewer/src/types.ts` — `aspect?` on curated entry (modify).
- `viewer/src/components/DetailPanel.tsx` — Aspect toggle, filtering, kit banner (modify).

---

## PHASE A — Python

### Task A1: `aspects` config in `_weights.yaml`

**Files:** Modify `04. System/Data/SMITE/_weights.yaml`

- [ ] **Step 1: Add the `aspects` block** immediately after the `flavors:` block (before `# ── Game modes`). Insert:
```yaml
# ── God aspects ─────────────────────────────────────────────────────────────
# Per-god scoring overlay (same shape as a flavor) applied when the viewer's
# Aspect toggle is on. Keyed by god name. Hand-tuned from each aspect's kit text;
# light where the aspect barely changes the build. Stat keys match item stats
# (Strength / Intelligence / Attack Speed / Max Health / Cooldown Rate /
# Lifesteal / Physical Protection / Magical Protection / …).
aspects:
  Cernunnos:      # Strife — basics become melee cleave autos
    stats: {Strength: 1.0, Attack Speed: 0.8, Lifesteal: 0.8, Max Health: 0.6}
    tag_bonus: {sustain: 0.2}
    max_lifesteal: 2
  Hercules:       # Preservation — ally-heal bruiser/tank
    stats: {Max Health: 1.2, Physical Protection: 0.9, Magical Protection: 0.9}
    tag_bonus: {aura: 0.3, sustain: 0.2}
    max_lifesteal: 2
  Ra:             # Thermotherapy — heals allies, abilities lose scaling -> support
    stats: {Cooldown Rate: 0.8, Magical Protection: 0.5, Max Health: 0.6, Intelligence: 0.4}
    tag_bonus: {aura: 0.3, sustain: 0.2}
  Chronos:        # Relativity — team time-field, loses Time Lord Int -> support mage
    stats: {Cooldown Rate: 0.8, Intelligence: 0.6, Magical Protection: 0.4, Max Health: 0.4}
    tag_bonus: {aura: 0.3}
  Morgan Le Fay:  # Cursed Crown — melee, %max-HP damage
    stats: {Max Health: 1.0, Intelligence: 0.8, Magical Protection: 0.4}
    tag_bonus: {sustain: 0.2}
    max_lifesteal: 2
  Agni:           # Combustion — ignite via basics; still a burst mage
    stats: {Attack Speed: 0.4}
  Chiron:         # Heroic Tutor — damage copy + ally buffs; still a carry
    stats: {Attack Speed: 0.3}
    tag_bonus: {aura: 0.1}
```

- [ ] **Step 2: Sanity-load**

Run: `cd tools && python -c "from pathlib import Path; from smite import scoring; w=scoring.load_weights(Path('../04. System/Data/SMITE/_weights.yaml')); print(sorted(w['aspects'])); print(w['aspects']['Hercules'])"`
Expected: the 7 god names, and Hercules's overlay dict.

- [ ] **Step 3: Commit**
```bash
git add "04. System/Data/SMITE/_weights.yaml"
git commit -m "feat(smite): aspect overlays config"
```

---

### Task A2: `resolve_profile` aspect composition

**Files:** Modify `tools/smite/scoring.py`; Test `tools/smite/tests/test_scoring.py`

- [ ] **Step 1: Write failing tests** (append to `test_scoring.py`; it imports `scoring` — confirm the import line):
```python
def test_resolve_profile_composes_aspect_overlay():
    weights = {"signals": {"efficiency": 0.35, "win": 0.30, "pick": 0.15, "fit": 0.20},
               "flavors": {"crit": {"stats": {"Critical Chance": 1.5}, "tag_bonus": {"x": 0.1}}},
               "modes": {"conquest": {}}}
    aspect = {"stats": {"Max Health": 1.0, "Critical Chance": 0.5}, "tag_bonus": {"aura": 0.3}, "max_lifesteal": 2}
    p = scoring.resolve_profile(weights, "Conquest", "crit", aspect_overlay=aspect)
    # flavor stat wins on the shared key; aspect contributes its own
    assert p["stat_overlay"]["Critical Chance"] == 1.5
    assert p["stat_overlay"]["Max Health"] == 1.0
    # tags merge from aspect + flavor
    assert p["tag_bonus"]["aura"] == 0.3 and p["tag_bonus"]["x"] == 0.1
    # flavor sets max_lifesteal(1 default absent) -> here flavor has none, aspect=2
    assert p["max_lifesteal"] == 2


def test_resolve_profile_flavor_max_lifesteal_beats_aspect():
    weights = {"signals": {"efficiency": 1}, "flavors": {"f": {"max_lifesteal": 1}}, "modes": {"conquest": {}}}
    p = scoring.resolve_profile(weights, "Conquest", "f", aspect_overlay={"max_lifesteal": 2})
    assert p["max_lifesteal"] == 1  # flavor's explicit value wins


def test_resolve_profile_no_aspect_unchanged():
    weights = {"signals": {"efficiency": 1}, "flavors": {}, "modes": {"conquest": {}}}
    p = scoring.resolve_profile(weights, "Conquest", None)
    assert p["stat_overlay"] == {} and p["max_lifesteal"] == 1
```
(If `test_scoring.py` doesn't exist, create it with `from smite import scoring` at the top.)

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -k resolve_profile -v`

- [ ] **Step 3: Implement** — replace `resolve_profile` in `scoring.py` with:
```python
def resolve_profile(weights, mode="Conquest", flavor=None, aspect_overlay=None):
    """Compose a mode profile ⊕ aspect ⊕ flavor into an effective scoring overlay.
    Mode sets signal overrides + tag bonuses; the aspect overlay and flavor each
    add stat weights + tag bonuses (flavor wins on a shared key) + a lifesteal
    cap (flavor's explicit cap wins, else the aspect's, else 1). suppress_underrated
    is true when the mode zeroes the pick signal."""
    mode_prof = (weights.get("modes") or {}).get(mode.lower(), {}) or {}
    fl = ((weights.get("flavors") or {}).get(flavor) or {}) if flavor else {}
    asp = aspect_overlay or {}
    signals = {**weights["signals"], **(mode_prof.get("signals") or {})}
    tag_bonus = {**(mode_prof.get("tag_bonus") or {}),
                 **(asp.get("tag_bonus") or {}),
                 **(fl.get("tag_bonus") or {})}
    stat_overlay = {**(asp.get("stats") or {}), **(fl.get("stats") or {})}
    if "max_lifesteal" in fl:
        max_ls = fl["max_lifesteal"]
    elif "max_lifesteal" in asp:
        max_ls = asp["max_lifesteal"]
    else:
        max_ls = 1
    return {
        "signals": signals,
        "stat_overlay": stat_overlay,
        "tag_bonus": tag_bonus,
        "max_lifesteal": max_ls,
        "suppress_underrated": signals.get("pick", 1) == 0,
        "label": mode_prof.get("label"),
        "flavor": flavor,
    }
```

- [ ] **Step 4: Run, confirm PASS** + full suite

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -v` then `cd tools && python -m pytest smite/tests/ -q -m "not live"`

- [ ] **Step 5: Commit**
```bash
git add tools/smite/scoring.py tools/smite/tests/test_scoring.py
git commit -m "feat(smite): resolve_profile composes an aspect overlay"
```

---

### Task A3: `build_suggested_entries` emits an aspect set

**Files:** Modify `tools/smite/recommend.py`; Test `tools/smite/tests/test_recommend.py`

- [ ] **Step 1: Write failing test** (append to `test_recommend.py`):
```python
def test_aspect_god_emits_base_and_aspect_sets():
    from smite import recommend, scoring
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags = scoring.load_tags(recommend.TAGS_PATH)
    herc = next(g for g in recommend.load_gods() if g["name"] == "Hercules")
    build = recommend.load_build_note("Hercules")
    entries = recommend.build_suggested_entries(herc, items, build, weights, tags, "Conquest")
    base_cores = [e for e in entries if e["archetype"] == "core" and not e.get("aspect")]
    aspect_cores = [e for e in entries if e["archetype"] == "core" and e.get("aspect")]
    assert len(base_cores) == 1 and len(aspect_cores) == 1
    assert aspect_cores[0]["aspect"] == herc["aspects"][0]["name"]
    # aspect entries still carry buy-order/flex machinery
    assert aspect_cores[0].get("flex_slots") and aspect_cores[0]["slot_order"]


def test_non_aspect_god_emits_only_base():
    from smite import recommend, scoring
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags = scoring.load_tags(recommend.TAGS_PATH)
    susano = next(g for g in recommend.load_gods() if g["name"] == "Susano")
    entries = recommend.build_suggested_entries(susano, items, recommend.load_build_note("Susano"),
                                                weights, tags, "Conquest")
    assert all(not e.get("aspect") for e in entries)
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -k "aspect_god or non_aspect" -v`

- [ ] **Step 3: Implement** — in `recommend.py`, refactor `build_suggested_entries` to build an entry set for a given overlay, then call it for base + aspect. Replace the whole function with:
```python
def _build_entry_set(god, items, god_build, weights, tags_map, mode, eff_scores,
                     items_by_name, starter, flex_count, aspect_overlay, aspect_name):
    entries = []
    for flavor in [None] + scoring.eligible_flavors(god, weights):
        profile = scoring.resolve_profile(weights, mode, flavor, aspect_overlay=aspect_overlay)
        rows = scoring.score_god_items(god, items, god_build, eff_scores, weights, tags_map, profile)
        require = ((weights.get("flavors") or {}).get(flavor) or {}).get("require") if flavor else None
        core = assemble.assemble_core(rows, items_by_name, n=6,
                                      max_lifesteal=profile["max_lifesteal"], require=require)
        flex = assemble.flex_slots(core, rows, count=flex_count)
        ordered = assemble.build_order(core, items_by_name, tags_map, weights)
        swaps = assemble.situational_swaps(rows, items_by_name, tags_map, core=core)
        archetype = flavor or "core"
        entries.append({
            "source": "suggested",
            "archetype": archetype,
            "slot_order": ordered,
            "flex_slots": flex,
            "situational_swaps": swaps,
            "rationale": _rationale(archetype, rows, profile),
            **({"starter": starter} if starter else {}),
            **({"aspect": aspect_name} if aspect_name else {}),
        })
    return entries


def build_suggested_entries(god, items, god_build, weights, tags_map, mode="Conquest"):
    eff_scores, _ = efficiency.efficiency_scores(items)
    items_by_name = {it["name"]: it for it in items}
    starter = scoring.pick_starter(god, weights)
    flex_count = (weights.get("build_order") or {}).get("flex_count", 2)
    entries = _build_entry_set(god, items, god_build, weights, tags_map, mode, eff_scores,
                               items_by_name, starter, flex_count, None, None)
    aspect_overlay = (weights.get("aspects") or {}).get(god["name"])
    god_aspects = god.get("aspects") or []
    if aspect_overlay and god_aspects:
        aspect_name = god_aspects[0].get("name")
        entries += _build_entry_set(god, items, god_build, weights, tags_map, mode, eff_scores,
                                    items_by_name, starter, flex_count, aspect_overlay, aspect_name)
    return entries
```

- [ ] **Step 4: Run, confirm PASS** + full suite

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -v` then `cd tools && python -m pytest smite/tests/ -q -m "not live"`

- [ ] **Step 5: Commit**
```bash
git add tools/smite/recommend.py tools/smite/tests/test_recommend.py
git commit -m "feat(smite): emit aspect-tuned suggested set for aspect gods"
```

---

## PHASE V — Viewer

### Task V1: Aspect toggle, filtering, kit banner

**Files:** Modify `viewer/src/types.ts`, `viewer/src/components/DetailPanel.tsx`; Test `viewer/src/components/DetailPanel.test.tsx`

- [ ] **Step 1: Update `types.ts`** — add `aspect?: string;` to `CuratedBuildEntry` (next to `flex_slots?`).

- [ ] **Step 2: Failing tests** (append inside the `describe` in `DetailPanel.test.tsx`):
```tsx
  const godWithAspect = {
    type: "god", name: "Hercules", pantheon: "Roman", role: "Solo", specializations: [],
    damage_type: "physical", release_date: "", base_stats: {}, abilities: [],
    aspects: [{ name: "Aspect of Preservation", kit_changes: "Becomes an ally-heal tank." }],
    source_url: "", last_verified: "",
  } as any;

  function aspectBuild(): BuildNote {
    return { type: "smite-build", god: "Hercules", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [{ name: "X", pick_rate: 0.5, win_rate: 0.5 }], source_url: "u" } as any,
      { source: "suggested", archetype: "core", slot_order: ["BaseItem"], situational_swaps: [], rationale: "" } as any,
      { source: "suggested", archetype: "core", slot_order: ["AspectItem"], situational_swaps: [], rationale: "",
        aspect: "Aspect of Preservation" } as any,
    ] };
  }

  it("shows the Aspect toggle and swaps to the aspect build + kit banner when on", () => {
    render(<DetailPanel god="Hercules" godData={godWithAspect} items={[]} builds={[aspectBuild()]}
                        mode="Conquest" onModeChange={() => {}} />);
    // base build visible, aspect build hidden by default
    expect(screen.getByText("BaseItem")).toBeInTheDocument();
    expect(screen.queryByText("AspectItem")).not.toBeInTheDocument();
    const toggle = screen.getByRole("button", { name: /aspect/i });
    fireEvent.click(toggle);
    expect(screen.getByText("AspectItem")).toBeInTheDocument();
    expect(screen.queryByText("BaseItem")).not.toBeInTheDocument();
    expect(screen.getByText(/ally-heal tank/i)).toBeInTheDocument();       // kit banner
    // community stays visible in both states
    expect(screen.getByRole("tab", { name: /community/i })).toBeInTheDocument();
  });

  it("shows no Aspect toggle for a god with no aspect builds", () => {
    const builds = [{ type: "smite-build", god: "Susano", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "" },
    ] }];
    render(<DetailPanel god="Susano" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    expect(screen.queryByRole("button", { name: /^aspect/i })).not.toBeInTheDocument();
  });
```

- [ ] **Step 3: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/components/DetailPanel.test.tsx -t "Aspect"`

- [ ] **Step 4: Implement** in `DetailPanel.tsx`:

  **(a) Aspect state + reset.** Add `const [aspectOn, setAspectOn] = useState(false);` next to the other state. In the god/note reset effect, add `setAspectOn(false);` (so switching god/mode clears it).

  **(b) Filter entries by aspect.** Replace `const entries = note.builds;` with:
```tsx
  const aspectMeta = godData?.aspects?.[0];
  const hasAspect = note.builds.some((b) => (b as { aspect?: string }).aspect);
  const entries = note.builds.filter((b) => {
    if (b.source !== "suggested") return true;
    const a = (b as { aspect?: string }).aspect;
    return aspectOn ? !!a : !a;
  });
```
  (The `active`/`community`/`swaps`/`preview` lines below already derive from `entries` — they now operate on the filtered set. `activeIndex` is clamped by the existing `entries[activeIndex] ?? entries[0]`.)

  **(c) Toggle handler.** Add near the component's other handlers (before the return):
```tsx
  const toggleAspect = () => { setAspectOn((v) => !v); setActiveIndex(0); setSelectedTag(null); };
```

  **(d) Toggle UI + kit banner.** Replace the existing mode-toggle block:
```tsx
      {modes.length > 1 && (
        <div className="mb-3 flex w-fit overflow-hidden rounded-md border border-line">
          {modes.map((m) => (
            <button ...>{m}</button>
          ))}
        </div>
      )}
```
  with a combined row that also holds the Aspect toggle, then the banner:
```tsx
      {(modes.length > 1 || hasAspect) && (
        <div className="mb-3 flex items-center gap-3">
          {modes.length > 1 && (
            <div className="flex w-fit overflow-hidden rounded-md border border-line">
              {modes.map((m) => (
                <button
                  key={m}
                  type="button"
                  onClick={() => onModeChange(m)}
                  className={`px-3 py-1 font-display text-xs font-semibold tracking-wide ${
                    m === note.mode ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"
                  }`}
                >
                  {m}
                </button>
              ))}
            </div>
          )}
          {hasAspect && (
            <button
              type="button"
              onClick={toggleAspect}
              className={`rounded-md border border-line px-3 py-1 font-display text-xs font-semibold tracking-wide ${
                aspectOn ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"
              }`}
            >
              {aspectMeta ? `Aspect: ${aspectMeta.name.replace(/^Aspect of (the )?/i, "")}` : "Aspect"}
            </button>
          )}
        </div>
      )}

      {aspectOn && aspectMeta && (
        <div className="mb-3 rounded border border-gold/40 bg-bg1 p-2 text-xs">
          <span className="font-display font-semibold text-gold">{aspectMeta.name}</span>
          <span className="text-muted"> — {aspectMeta.kit_changes}</span>
        </div>
      )}
```
  (Keep the existing keys/handlers exactly; only the wrapping row changed. The mode-toggle buttons are unchanged in behavior.)

- [ ] **Step 5: Run, confirm PASS** + full suite + typecheck

Run: `cd viewer && npx vitest run && npx tsc --noEmit`
Fix any existing DetailPanel test broken by the toggle-row rewrap (button text/roles are unchanged, so the "mode toggle changes" test still passes).

- [ ] **Step 6: Commit**
```bash
git add viewer/src/types.ts viewer/src/components/DetailPanel.tsx viewer/src/components/DetailPanel.test.tsx
git commit -m "feat(viewer): per-god Aspect toggle, aspect-build swap, kit banner"
```

---

### Task V2: Full regen + browser verification

**Files:** generated — `Builds/*.md`, `Analysis/*.md`, `viewer/public/index.json`

- [ ] **Step 1: Regenerate**

Run from `tools/`: `python -m smite.recommend --all` then `python -m smite.build_index`.
Verify aspect entries landed + differ from base:
```bash
cd .. && python -c "
import json; d=json.load(open('viewer/public/index.json',encoding='utf-8'))
for god in ['Hercules','Ra','Cernunnos','Susano']:
    n=next((x for x in d['builds'] if x['god']==god and x['mode']=='Conquest'), None)
    if not n: print(god,'no note'); continue
    base=next((b for b in n['builds'] if b.get('archetype')=='core' and not b.get('aspect')), None)
    asp=next((b for b in n['builds'] if b.get('archetype')=='core' and b.get('aspect')), None)
    print(god, '| aspect entry:', bool(asp), '| aspect name:', asp and asp.get('aspect'))
    if base and asp:
        print('   base :', base['slot_order'])
        print('   aspect:', asp['slot_order'], '(differs:', base['slot_order']!=asp['slot_order'], ')')
"
```
Expected: Hercules/Ra/Cernunnos have an aspect core that differs from base; Susano has none.

- [ ] **Step 2: Both suites green**

Run: `cd tools && python -m pytest smite/tests/ -q -m "not live"` and `cd ../viewer && npx vitest run`.

- [ ] **Step 3: End-to-end browser verification**

Start the worktree dev server (`npx vite --port 5178 --strictPort` from `viewer/`). On **Hercules** (a strong aspect-changer):
  (a) confirm an **Aspect: Preservation** toggle appears next to the mode toggle;
  (b) toggle it on — confirm the build swaps to a tankier/support set, a **kit banner** shows the real aspect text, and the tabs are the aspect set;
  (c) toggle off — base build returns;
  (d) on **Susano**, confirm there is **no** Aspect toggle;
  (e) confirm community/mine tabs remain visible in both toggle states.
Fix issues, re-verify. Screenshot Hercules with the aspect toggle on (banner + build).

- [ ] **Step 4: Commit generated output**
```bash
git add "03. Workspaces/Gaming/SMITE 2/Builds/" "04. System/Data/SMITE/Analysis/" viewer/public/index.json
git commit -m "chore(smite): regenerate builds with aspect variants"
```

---

## Self-Review

**Spec coverage:** aspect overlays config (A1), mode⊕aspect⊕flavor composition (A2), parallel aspect suggested set tagged `aspect` (A3), types `aspect?` + Aspect toggle + filter-swap + kit banner (V1), regen + verify (V2). Toggle swaps (not extra tabs) and all 7 aspect gods — both honored (any god with an `aspects[<name>]` overlay + wiki aspect emits the set; the viewer shows the toggle whenever aspect entries exist). All spec sections mapped.

**Placeholder scan:** none — full code in every step. The mode-toggle buttons inside V1 step (d) are shown complete in the combined row; the "…" in the *old* block being replaced is only marking what to remove.

**Type/name consistency:** `resolve_profile(weights, mode, flavor, aspect_overlay=None)` (A2) ← called by `_build_entry_set` (A3). `aspects[god_name]` overlay (A1) ← read in `build_suggested_entries` via `weights["aspects"].get(god["name"])` (A3). `aspect: <name>` on entries (A3) → `CuratedBuildEntry.aspect?` type (V1) → filtered in DetailPanel by `(b as {aspect?}).aspect` (V1). Kit text from `godData.aspects[0]` (V1) — the `God.aspects` type already exists. `hasAspect`/`aspectOn`/`aspectMeta` all defined in V1 step (b)/(a)/(b). No dangling names.

**Safety:** `_weights.yaml` is a user-owned sidecar (edited additively); base builds unchanged when no aspect overlay (regression-safe); generated files regenerated deterministically; no `_archive/` touched.
