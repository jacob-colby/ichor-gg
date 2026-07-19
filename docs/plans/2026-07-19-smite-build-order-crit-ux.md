# Buy-order, flex swaps, crit-core, editor UX Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give suggested builds a recommended purchase order, make situational swaps target a marked flex slot, guarantee crit builds actually stack crit, and polish the editor (icons, stay-on-build-after-save) + move the mode toggle top-left.

**Architecture:** Python side — `assemble_core` gains a `require` constraint (crit min), a new `build_order` sorter reorders the core, and `flex_slots` are computed from score; `recommend` threads all three onto `suggested` entries. Viewer side — `applySwap` targets a flex slot, `BuildEditor` shows icons + reports the saved name, `DetailPanel` selects the just-saved tab and renders the mode toggle above the tabs.

**Tech Stack:** Python 3.10 (pytest), Vite + React 19 + TS + Vitest + RTL.

**Reference spec:** [2026-07-19-smite-build-order-crit-ux-design.md](../specs/2026-07-19-smite-build-order-crit-ux-design.md)

---

## File Structure
- `04. System/Data/SMITE/_weights.yaml` — add `build_order` block + `crit.require` (modify).
- `tools/smite/assemble.py` — `assemble_core(require=...)`, new `build_order()`, `flex_slots()` (modify).
- `tools/smite/recommend.py` — thread require/build_order/flex_slots into suggested entries (modify).
- `viewer/src/types.ts` — `flex_slots?` on curated entry (modify).
- `viewer/src/lib/builds.ts` — `applySwap(slotOrder, swapItem, flexSlots?)` (modify).
- `viewer/src/components/BuildEditor.tsx` — item icons + `onSaved(name)` (modify).
- `viewer/src/components/DetailPanel.tsx` — mode toggle placement, pendingSelect, flex markers, BUILD ORDER header, pass flexSlots to applySwap (modify).

---

## PHASE P — Python (scoring)

### Task P1: `_weights.yaml` config

**Files:** Modify `04. System/Data/SMITE/_weights.yaml`

- [ ] **Step 1: Add the `build_order` block** immediately before the `# ── Starters` comment (i.e. after the `modes:` block). Insert:
```yaml
# ── Build order (recommended purchase sequence) ─────────────────────────────
# Heuristic buy-order for suggested cores (we have no real build-path data).
# stage = default_stage + sum(tag_stage for the item's effect_tags) +
# cost * cost_weight. Core is sorted ascending by stage (ties: cost, then name).
# flex_count = how many lowest-scored core items situational swaps may replace.
build_order:
  default_stage: 0
  cost_weight: 0.0004
  flex_count: 2
  tag_stage:
    anti-heal: -1
    protection-shred: -1
    wave-clear: -1
    sustain: 0
    aura: 1
    mobility: 0
```

- [ ] **Step 2: Add `require` to the crit flavor.** Find the `crit:` flavor under `flavors:` and add a `require` line so it reads:
```yaml
  crit:
    damage_types: [physical]
    match_any: [Carry, Sharpshooter]
    stats: {Critical Chance: 1.5, Attack Speed: 1.2, Strength: 0.8}
    max_lifesteal: 1
    require: {stat: "Critical Chance", min: 3}
```

- [ ] **Step 3: Sanity-load** to confirm YAML is valid:

Run: `cd tools && python -c "from smite import scoring; w=scoring.load_weights('../04. System/Data/SMITE/_weights.yaml'); print(w['build_order']['flex_count'], w['flavors']['crit']['require'])"`
Expected: `2 {'stat': 'Critical Chance', 'min': 3}`

- [ ] **Step 4: Commit**
```bash
git add "04. System/Data/SMITE/_weights.yaml"
git commit -m "feat(smite): weights config for build-order + crit-core require"
```

---

### Task P2: `assemble_core` crit-require constraint

**Files:** Modify `tools/smite/assemble.py`; Test `tools/smite/tests/test_assemble.py`

- [ ] **Step 1: Write failing test** (append to `test_assemble.py`; check existing imports — it imports from `smite.assemble`):
```python
def test_assemble_core_require_seeds_minimum_stat_items():
    from smite.assemble import assemble_core
    items = {
        "Crit A": {"name": "Crit A", "stats": {"Critical Chance": "20%"}},
        "Crit B": {"name": "Crit B", "stats": {"Critical Chance": "20%"}},
        "Crit C": {"name": "Crit C", "stats": {"Critical Chance": "20%"}},
        "Pen X": {"name": "Pen X", "stats": {"Penetration": "15"}},
        "Pen Y": {"name": "Pen Y", "stats": {"Penetration": "15"}},
        "Pen Z": {"name": "Pen Z", "stats": {"Penetration": "15"}},
        "Pen W": {"name": "Pen W", "stats": {"Penetration": "15"}},
    }
    # Non-crit items score higher, so without `require` the core would be all pen.
    rows = [{"item": n, "tags": []} for n in
            ["Pen X", "Pen Y", "Pen Z", "Pen W", "Crit A", "Crit B", "Crit C"]]
    core = assemble_core(rows, items, n=6, require={"stat": "Critical Chance", "min": 3})
    crit_in_core = [n for n in core if "Critical Chance" in items[n]["stats"]]
    assert len(crit_in_core) >= 3
    assert len(core) == 6
    assert len(set(core)) == 6  # no dups


def test_assemble_core_require_handles_thin_pool():
    from smite.assemble import assemble_core
    items = {"Crit A": {"name": "Crit A", "stats": {"Critical Chance": "20%"}},
             "Pen X": {"name": "Pen X", "stats": {"Penetration": "15"}},
             "Pen Y": {"name": "Pen Y", "stats": {"Penetration": "15"}}}
    rows = [{"item": n, "tags": []} for n in ["Pen X", "Pen Y", "Crit A"]]
    core = assemble_core(rows, items, n=3, require={"stat": "Critical Chance", "min": 3})
    assert "Crit A" in core and len(core) == 3  # seeds the 1 available, fills rest
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_assemble.py -k require -v`

- [ ] **Step 3: Implement** — modify `assemble_core` in `assemble.py`. Change the signature and seed required items first. Replace the existing `def assemble_core(rows, items_by_name, n=6, max_lifesteal=1):` function body with:
```python
def assemble_core(rows, items_by_name, n=6, max_lifesteal=1, require=None):
    """Highest-total items filling n slots: at most one boots, at most
    `max_lifesteal` lifesteal/sustain items, no duplicates. rows must be
    pre-sorted by -total (score_god_items already does). When `require`
    {stat, min} is given, the core is seeded with the top-scored items carrying
    that stat (up to `min`, honoring the same rules) before filling by score."""
    core, used = [], set()
    have_boots = False
    lifesteal_count = 0

    def _try_add(name):
        nonlocal have_boots, lifesteal_count
        if name in used or len(core) >= n:
            return False
        item = items_by_name.get(name, {})
        if _is_boots(item):
            if have_boots:
                return False
            have_boots = True
        is_ls = _is_lifesteal(item, _row_tags.get(name))
        if is_ls and lifesteal_count >= max_lifesteal:
            return False
        if is_ls:
            lifesteal_count += 1
        core.append(name)
        used.add(name)
        return True

    _row_tags = {r["item"]: r.get("tags") for r in rows}

    if require:
        stat, need = require.get("stat"), require.get("min", 0)
        seeded = 0
        for r in rows:
            if seeded >= need:
                break
            item = items_by_name.get(r["item"], {})
            if stat in (item.get("stats") or {}) and _try_add(r["item"]):
                seeded += 1

    for r in rows:
        if len(core) >= n:
            break
        _try_add(r["item"])
    return core
```

- [ ] **Step 4: Run, confirm PASS**

Run: `cd tools && python -m pytest smite/tests/test_assemble.py -v`
(All existing assemble tests must still pass — the default `require=None` path is unchanged behavior.)

- [ ] **Step 5: Commit**
```bash
git add tools/smite/assemble.py tools/smite/tests/test_assemble.py
git commit -m "feat(smite): assemble_core require constraint (crit-core minimum)"
```

---

### Task P3: `build_order` + `flex_slots`

**Files:** Modify `tools/smite/assemble.py`; Test `tools/smite/tests/test_assemble.py`

- [ ] **Step 1: Write failing tests** (append):
```python
def test_build_order_sorts_cheap_early_aura_late():
    from smite.assemble import build_order
    items = {
        "Anti": {"name": "Anti", "cost": 2500, "stats": {}},
        "Aura": {"name": "Aura", "cost": 2500, "stats": {}},
        "Cheap": {"name": "Cheap", "cost": 1000, "stats": {}},
    }
    tags = {"Anti": ["anti-heal"], "Aura": ["aura"], "Cheap": []}
    weights = {"build_order": {"default_stage": 0, "cost_weight": 0.0004,
                               "tag_stage": {"anti-heal": -1, "aura": 1}}}
    order = build_order(["Aura", "Cheap", "Anti"], items, tags, weights)
    # Anti (stage -1+1.0) < Cheap (0.4) < Aura (1+1.0)
    assert order == ["Anti", "Cheap", "Aura"]


def test_flex_slots_are_lowest_scored_core():
    from smite.assemble import flex_slots
    core = ["A", "B", "C", "D", "E", "F"]  # rows are score-desc, so core is too
    rows = [{"item": n} for n in ["A", "B", "C", "D", "E", "F"]]
    assert flex_slots(core, rows, count=2) == ["E", "F"]
    # subset guarantee + count clamp
    assert set(flex_slots(core, rows, count=2)) <= set(core)
    assert flex_slots(["A"], [{"item": "A"}], count=2) == ["A"]
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_assemble.py -k "build_order or flex_slots" -v`

- [ ] **Step 3: Implement** — append to `assemble.py`:
```python
def build_order(core, items_by_name, tags_map, weights):
    """Recommended purchase order for a core (heuristic — we have no real
    build-path data). stage = default + sum(tag_stage for the item's tags) +
    cost*cost_weight; sorted ascending (ties: cost, then name)."""
    cfg = (weights or {}).get("build_order") or {}
    default_stage = cfg.get("default_stage", 0)
    cost_weight = cfg.get("cost_weight", 0)
    tag_stage = cfg.get("tag_stage") or {}

    def stage(name):
        item = items_by_name.get(name, {})
        tags = tags_map.get(name) or []
        s = default_stage + sum(tag_stage.get(t, 0) for t in tags)
        cost = item.get("cost") or 0
        return (s + cost * cost_weight, cost, name)

    return sorted(core, key=stage)


def flex_slots(core, rows, count=2):
    """The `count` least-essential core items — the lowest-scored ones (rows are
    score-descending, so the core's score order is its order in `rows`). Returns
    a subset of `core`."""
    order = [r["item"] for r in rows if r["item"] in set(core)]
    n = min(count, len(order))
    return order[-n:] if n else []
```

- [ ] **Step 4: Run, confirm PASS**

Run: `cd tools && python -m pytest smite/tests/test_assemble.py -v`

- [ ] **Step 5: Commit**
```bash
git add tools/smite/assemble.py tools/smite/tests/test_assemble.py
git commit -m "feat(smite): build_order + flex_slots helpers"
```

---

### Task P4: Thread into `build_suggested_entries`

**Files:** Modify `tools/smite/recommend.py`; Test `tools/smite/tests/test_recommend.py`

- [ ] **Step 1: Write failing test** (append to `test_recommend.py`):
```python
def test_suggested_entries_have_buy_order_flex_and_crit_core():
    from smite import recommend, scoring
    from pathlib import Path
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags = scoring.load_tags(recommend.TAGS_PATH)
    items_by_name = {it["name"]: it for it in items}
    god = next(g for g in recommend.load_gods() if g["name"] == "Chiron")  # physical carry
    build = recommend.load_build_note("Chiron")
    entries = recommend.build_suggested_entries(god, items, build, weights, tags, "Conquest")
    crit = next((e for e in entries if e["archetype"] == "crit"), None)
    assert crit is not None
    # crit-core guarantee: >=3 items with Critical Chance
    ncrit = sum(1 for n in crit["slot_order"]
                if "Critical Chance" in (items_by_name.get(n, {}).get("stats") or {}))
    assert ncrit >= 3
    # every suggested entry carries flex_slots ⊆ slot_order
    for e in entries:
        assert e.get("flex_slots"), f"{e['archetype']} missing flex_slots"
        assert set(e["flex_slots"]) <= set(e["slot_order"])
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -k buy_order_flex -v`

- [ ] **Step 3: Implement** — in `recommend.py`, replace the body of the `for flavor in ...` loop inside `build_suggested_entries` so it passes `require` into `assemble_core`, computes `build_order`, and stamps `flex_slots`. The full updated function:
```python
def build_suggested_entries(god, items, god_build, weights, tags_map, mode="Conquest"):
    eff_scores, _ = efficiency.efficiency_scores(items)
    items_by_name = {it["name"]: it for it in items}
    starter = scoring.pick_starter(god, weights)
    flex_count = ((weights.get("build_order") or {}).get("flex_count", 2))
    entries = []
    for flavor in [None] + scoring.eligible_flavors(god, weights):
        profile = scoring.resolve_profile(weights, mode, flavor)
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
        })
    return entries
```
(Note: `flex` is computed from `core`/`rows` — score order — before reordering to `ordered` buy-order, so flex marks the least-essential items regardless of display order.)

- [ ] **Step 4: Run, confirm PASS**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -v` then `cd tools && python -m pytest smite/tests/ -q -m "not live"`

- [ ] **Step 5: Commit**
```bash
git add tools/smite/recommend.py tools/smite/tests/test_recommend.py
git commit -m "feat(smite): suggested builds carry buy-order, flex_slots, crit-core"
```

---

## PHASE V — Viewer

### Task V1: `applySwap` flex target + types

**Files:** Modify `viewer/src/lib/builds.ts`, `viewer/src/types.ts`; Test `viewer/src/lib/builds.test.ts`

- [ ] **Step 1: Update `types.ts`** — add `flex_slots?: string[];` to `CuratedBuildEntry` (next to `situational_swaps?`).

- [ ] **Step 2: Failing test** (append to `builds.test.ts`, which already imports `applySwap`):
```typescript
describe("applySwap flex targeting", () => {
  it("removes the flex slot, not the last, when flexSlots is given", () => {
    const out = applySwap(["A", "B", "C", "D"], "SwapIn", ["B"]);
    const removed = out.find((s) => s.status === "removed");
    const added = out.find((s) => s.status === "added");
    expect(removed?.name).toBe("B");
    expect(added?.name).toBe("SwapIn");
    expect(out.filter((s) => s.status === "kept").map((s) => s.name)).toEqual(["A", "C", "D"]);
  });
  it("falls back to the last slot when no flexSlots supplied", () => {
    const out = applySwap(["A", "B", "C"], "SwapIn");
    expect(out.find((s) => s.status === "removed")?.name).toBe("C");
  });
  it("falls back to last when flex slot is not in the build", () => {
    const out = applySwap(["A", "B", "C"], "SwapIn", ["Z"]);
    expect(out.find((s) => s.status === "removed")?.name).toBe("C");
  });
});
```

- [ ] **Step 3: Implement** — replace `applySwap` in `builds.ts` with:
```typescript
/** Derive the effective build shown when a matchup is selected: a flex slot (or
 * the lowest-scored core slot if none is marked / present) is removed and the
 * swap item is added. A null swapItem is a no-op (all kept). */
export function applySwap(slotOrder: string[], swapItem: string | null, flexSlots?: string[]): PreviewSlot[] {
  const base: PreviewSlot[] = slotOrder.map((name) => ({ name, status: "kept" }));
  if (!swapItem) return base;
  if (base.length === 0) return [{ name: swapItem, status: "added" }];
  const flex = (flexSlots ?? []).find((f) => slotOrder.includes(f));
  const idx = flex ? slotOrder.indexOf(flex) : base.length - 1;
  base[idx] = { name: base[idx].name, status: "removed" };
  base.push({ name: swapItem, status: "added" });
  return base;
}
```

- [ ] **Step 4: Run, confirm PASS** + typecheck

Run: `cd viewer && npx vitest run src/lib/builds.test.ts && npx tsc --noEmit`

- [ ] **Step 5: Commit**
```bash
git add viewer/src/lib/builds.ts viewer/src/types.ts viewer/src/lib/builds.test.ts
git commit -m "feat(viewer): applySwap targets a flex slot"
```

---

### Task V2: `BuildEditor` icons + saved-name callback

**Files:** Modify `viewer/src/components/BuildEditor.tsx`; Test `viewer/src/components/BuildEditor.test.tsx`

- [ ] **Step 1: Update the failing test** — change the existing "saves a build" test's `onSaved` assertion to expect the saved name, and add an icon-presence test. In `BuildEditor.test.tsx`, replace the `await waitFor(() => expect(onSaved).toHaveBeenCalled());` line in the first test with:
```tsx
    await waitFor(() => expect(onSaved).toHaveBeenCalledWith("My Build"));
```
and append this test inside the `describe`:
```tsx
  it("shows an item icon in the search results and chosen slots", () => {
    render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                        onClose={() => {}} onSaved={() => {}} />);
    fireEvent.change(screen.getByPlaceholderText(/search items/i), { target: { value: "Death" } });
    const resultImg = screen.getAllByRole("img").find((i) => i.getAttribute("src")?.includes("deathbringer"));
    expect(resultImg).toBeTruthy();
    fireEvent.click(screen.getByText("Deathbringer"));
    // still an icon once it's a chosen slot
    expect(screen.getAllByRole("img").some((i) => i.getAttribute("src")?.includes("deathbringer"))).toBe(true);
  });
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/components/BuildEditor.test.tsx`

- [ ] **Step 3: Implement** — in `BuildEditor.tsx`:
  1. Add the import: `import { iconSlug } from "../lib/builds";`
  2. Change the `onSaved` prop type from `() => void` to `(name: string) => void`.
  3. In the `save` handler's success path (inside `post`), pass the name. Simplest: make `post` accept an `onOk` callback, OR change `save` to call `onSaved(name.trim())`. Concretely, change `post` so success calls a passed name. Replace the `post` + `save` + delete wiring with:
```tsx
  const post = async (payload: object, savedName?: string) => {
    setBusy(true);
    setError(null);
    const res = await fetch("/api/build", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    }).then((r) => r.json()).catch((e) => ({ ok: false, error: String(e) }));
    setBusy(false);
    if (res.ok) {
      onSaved(savedName ?? "");
      onClose();
    } else {
      setError(res.error || "Request failed");
    }
  };

  const save = () => {
    if (!name.trim()) return setError("Name required");
    if (slots.length === 0) return setError("Add at least one item");
    post({
      action: "save", god, mode, name: name.trim(), slot_order: slots,
      starter: starterIdx >= 0 ? starters[starterIdx] : undefined,
      notes: notes.trim() || undefined,
    }, name.trim());
  };
```
  and the Delete button's onClick becomes `onClick={() => post({ action: "delete", god, mode, name: initial.name })}` (unchanged — no savedName, so `onSaved("")` fires, which the parent treats as "no specific tab to select").
  4. Add an icon to each **search result** button — replace the result button's inner `{it.name}` with an icon + name:
```tsx
            <button
              key={it.name}
              type="button"
              onClick={() => {
                if (slots.length < 6) setSlots([...slots, it.name]);
                setQuery("");
              }}
              className="flex w-full items-center gap-2 px-2 py-1 text-left text-sm text-ink hover:bg-line"
            >
              <img src={`/icons/${iconSlug(it.name)}.png`} alt="" className="h-5 w-5 flex-none rounded bg-bg2"
                onError={(e) => { const i = e.currentTarget; if (i.dataset.r) { i.style.visibility = "hidden"; return; } i.dataset.r = "1"; i.src = `/icons/${iconSlug(it.name)}.png?r=1`; }} />
              {it.name}
            </button>
```
  5. Add an icon to each **chosen slot** row — in the `slots.map(...)` block, insert an icon before the `<span className="flex-1">{n}</span>`:
```tsx
          <div key={`${n}-${i}`} className="flex items-center gap-2 text-sm text-ink">
            <span className="w-4 text-muted">{i + 1}</span>
            <img src={`/icons/${iconSlug(n)}.png`} alt="" className="h-5 w-5 flex-none rounded bg-bg2"
              onError={(e) => { const im = e.currentTarget; if (im.dataset.r) { im.style.visibility = "hidden"; return; } im.dataset.r = "1"; im.src = `/icons/${iconSlug(n)}.png?r=1`; }} />
            <span className="flex-1">{n}</span>
            <button type="button" onClick={() => move(i, -1)} className="px-1 text-muted hover:text-ink">↑</button>
            <button type="button" onClick={() => move(i, 1)} className="px-1 text-muted hover:text-ink">↓</button>
            <button type="button" onClick={() => setSlots(slots.filter((_, j) => j !== i))} className="px-1 text-muted hover:text-ink">✕</button>
          </div>
```

- [ ] **Step 4: Run, confirm PASS** + typecheck

Run: `cd viewer && npx vitest run src/components/BuildEditor.test.tsx && npx tsc --noEmit`
(The `DetailPanel`'s call `onSaved={() => onReload?.()}` still type-checks since it ignores the arg — V3 updates it to use the name.)

- [ ] **Step 5: Commit**
```bash
git add viewer/src/components/BuildEditor.tsx viewer/src/components/BuildEditor.test.tsx
git commit -m "feat(viewer): editor item icons + saved-name callback"
```

---

### Task V3: DetailPanel — mode toggle placement, pendingSelect, flex markers, buy-order header

**Files:** Modify `viewer/src/components/DetailPanel.tsx`; Test `viewer/src/components/DetailPanel.test.tsx`

- [ ] **Step 1: Failing tests** (append inside the `describe` in `DetailPanel.test.tsx`):
```tsx
  it("passes flex_slots so a swap removes the flex slot, not the last", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A", "B", "C"], flex_slots: ["A"],
        situational_swaps: [{ vs_tag: "heavy_cc", swap: "Cloak — cc", swap_item: "Cloak" }], rationale: "x" },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    fireEvent.click(screen.getByRole("button", { name: /heavy cc/i }));
    expect(screen.getByText("A")).toHaveClass("line-through");   // flex slot removed
    expect(screen.getByText("C")).not.toHaveClass("line-through");
  });

  it("selects the just-saved build after onReload fires with its name", () => {
    // Simulate: editor saved 'My New', parent reloads with the new entry present.
    const withNew: BuildNote = { type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [{ name: "X", pick_rate: 0.5, win_rate: 0.5 }], source_url: "u" } as any,
      { source: "mine", name: "My New", slot_order: ["Rage"] } as any,
    ] };
    // Render already-reloaded note; the pendingSelect path is exercised via the
    // editor flow in the browser — here assert the mine tab is selectable by name.
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={[withNew]}
                        mode="Conquest" onModeChange={() => {}} />);
    expect(screen.getByRole("tab", { name: /My New/i })).toBeInTheDocument();
  });
```
(The pendingSelect auto-selection is fully verified in the browser step V4; the unit test asserts the named tab exists.)

- [ ] **Step 2: Run, confirm FAIL** (flex test fails — applySwap not yet passed flex_slots)

Run: `cd viewer && npx vitest run src/components/DetailPanel.test.tsx -t "flex slot"`

- [ ] **Step 3: Implement** — several edits in `DetailPanel.tsx`:

  **(a) pendingSelect state + name-aware reset.** Add near the other state: `const [pendingSelect, setPendingSelect] = useState<string | null>(null);`. Replace the reset effect body so it honors a pending name:
```tsx
  useEffect(() => {
    if (pendingSelect) {
      const i = note?.builds.findIndex(
        (b) => (b as { name?: string }).name === pendingSelect,
      );
      setActiveIndex(i != null && i >= 0 ? i : 0);
      setPendingSelect(null);
    } else {
      setActiveIndex(0);
    }
    setSelectedTag(null);
    setEditing(null);
  }, [god, note]);   // eslint-disable-line react-hooks/exhaustive-deps
```
  Wire the editor's onSaved to record the name before reload. Change the `onSaved` prop passed to `BuildEditor` (in the `if (editing)` block) from `onSaved={() => onReload?.()}` to:
```tsx
        onSaved={(name) => { if (name) setPendingSelect(name); onReload?.(); }}
```

  **(b) Move the mode toggle.** Remove the mode-toggle block from the header (`<div className="ml-auto flex overflow-hidden rounded-md border border-line">...modes.map...</div>`). Add a new toggle row just above the `role="tablist"` div:
```tsx
      {modes.length > 1 && (
        <div className="mb-3 flex overflow-hidden rounded-md border border-line w-fit">
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
```
  (Guard `modes.length > 1` so a god with a single mode shows no toggle. The header's `ml-auto` wrapper is gone; leave the headshot + name/role block as-is.)

  **(c) Pass flex_slots to applySwap + BUILD ORDER header.** The `active` for a suggested entry is `CuratedBuildEntry` with `flex_slots?`. Compute and pass it. Replace:
```tsx
  const preview = applySwap(baseNames, selectedSwap?.swap_item ?? null);
```
  with:
```tsx
  const flexList = !community ? active.flex_slots : undefined;
  const preview = applySwap(baseNames, selectedSwap?.swap_item ?? null, flexList);
```
  Change the SLOT ORDER header to reflect buy-order for suggested builds. Replace the `SLOT ORDER` header line:
```tsx
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">SLOT ORDER</div>
```
  with:
```tsx
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">
            {!community && active.source === "suggested" ? "BUILD ORDER" : "SLOT ORDER"}
          </div>
```

  **(d) Flex marker on slot rows.** In the `preview.map((slot, i) => {...})` block, add a small "flex" tag on flex slots. After the `{slot.status === "added" && <span ...>swap in</span>}` line, add:
```tsx
                    {flexList?.includes(slot.name) && slot.status === "kept" && (
                      <span className="text-[10px] text-muted">flex</span>
                    )}
```

- [ ] **Step 4: Run, confirm PASS** + full suite + typecheck

Run: `cd viewer && npx vitest run && npx tsc --noEmit`
Fix any pre-existing DetailPanel test that broke due to the toggle move: the existing "switches build set when the mode toggle changes" test clicks `getByRole("button", { name: /joust/i })` — still valid (button text unchanged, just relocated). The "renders one tab per available source" etc. are unaffected.

- [ ] **Step 5: Commit**
```bash
git add viewer/src/components/DetailPanel.tsx viewer/src/components/DetailPanel.test.tsx
git commit -m "feat(viewer): mode toggle above tabs, flex markers, buy-order header, select saved build"
```

---

### Task V4: Full regen + end-to-end browser verification

**Files:** generated — `Builds/*.md`, `Analysis/*.md`, `viewer/public/index.json`

- [ ] **Step 1: Regenerate**

Run from `tools/`: `python -m smite.recommend --all` then `python -m smite.build_index`.
Verify buy-order + flex + crit landed:
```bash
cd .. && python -c "
import json; d=json.load(open('viewer/public/index.json',encoding='utf-8'))
items={i['name']:i for i in d['items']}
for god in ['Chiron','Cernunnos','Ullr']:
    n=next(x for x in d['builds'] if x['god']==god and x['mode']=='Conquest')
    crit=next((b for b in n['builds'] if b.get('archetype')=='crit'), None)
    if crit:
        nc=sum(1 for s in crit['slot_order'] if 'Critical Chance' in (items.get(s,{}).get('stats') or {}))
        print(f'{god} crit: {nc}/6 crit -> {crit[\"slot_order\"]}  flex={crit.get(\"flex_slots\")}')
core=next(b for b in next(x for x in d['builds'] if x['god']=='Chiron' and x['mode']=='Conquest')['builds'] if b['archetype']=='core')
print('Chiron core buy-order:', core['slot_order'], 'flex:', core.get('flex_slots'))
"
```
Expected: each crit build shows ≥3 crit items; every suggested entry has a `flex_slots` list ⊆ its `slot_order`.

- [ ] **Step 2: Both suites green**

Run: `cd tools && python -m pytest smite/tests/ -q -m "not live"` and `cd ../viewer && npx vitest run`.

- [ ] **Step 3: End-to-end browser verification**

Start the **worktree's** dev server (run `npx vite --port 5178 --strictPort` from `viewer/` in the worktree, or via preview if it targets the worktree). In the browser, on a physical carry (e.g. Chiron):
  (a) confirm the Conquest/Joust toggle is top-left above the build tabs;
  (b) open the **crit** tab — confirm the build is now crit-heavy and the header reads BUILD ORDER;
  (c) click a situational chip — confirm the struck-through removed item is a **flex** slot (marked "flex"), not the final item;
  (d) **+ New build** → confirm item **icons** show in the search results and chosen slots; save it → confirm the app stays on the god and the **new build's tab is selected** (not community);
  (e) edit/delete still work.
Fix issues, re-verify. Screenshot the crit build + the editor with icons.

- [ ] **Step 4: Commit generated output**

```bash
git add "03. Workspaces/Gaming/SMITE 2/Builds/" "04. System/Data/SMITE/Analysis/" viewer/public/index.json
git commit -m "chore(smite): regenerate builds with buy-order, flex slots, crit cores"
```

---

## Self-Review

**Spec coverage:** editor icons + stay-on-save (V2, V3), mode toggle placement (V3), buy order (P1 config, P3 build_order, P4 thread, V3 header), flex swaps (P1 flex_count, P3 flex_slots, P4 thread, V1 applySwap, V3 markers/pass-through), crit core (P1 require, P2 assemble_core, P4 thread). Aspects correctly excluded. All spec sections mapped.

**Placeholder scan:** none — all code complete. The pendingSelect auto-selection and the full save→stay→select flow are integration-verified in V4 (the async reload can't be faithfully unit-tested without mocking the whole data hook); V3's unit test asserts the named tab exists, which is the testable invariant.

**Type/name consistency:** `assemble_core(..., require={stat,min})` (P2) ← `crit.require` (P1) ← threaded in P4. `build_order(core, items_by_name, tags_map, weights)` and `flex_slots(core, rows, count)` (P3) ← called in P4 with those exact args. `flex_slots` list on suggested entries (P4) → `flex_slots?` type (V1) → `applySwap(slotOrder, swapItem, flexSlots)` (V1) ← called with `active.flex_slots` (V3). `onSaved(name: string)` (V2) ← consumed as `onSaved={(name) => ...}` (V3). Buy-order `slot_order` is the ordered core (P4) rendered under the BUILD ORDER header (V3). No dangling names.

**Safety:** no destructive ops; `_weights.yaml` is a user-owned sidecar (edited additively); generated Builds/Analysis/index regenerated deterministically; no `_archive/` touched.
