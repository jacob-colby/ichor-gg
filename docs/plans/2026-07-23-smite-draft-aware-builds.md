# Draft-aware builds Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let the player enter the 4 allies and 5 enemies of a match and get a comp-adapted 6-item core, re-ranked live in the browser.

**Architecture:** The viewer is a static site, so scoring can't re-run server-side. Python ships a per-god base-score table (`god_item_scores`) in `index.json`; the browser derives a threat model from the entered comps, converts it into a `tag_bonus`/`stat_bonus` overlay (the same shape `scoring.resolve_profile` produces), re-ranks, and re-assembles a core mirroring `assemble.assemble_core`'s constraints.

**Tech Stack:** Python (pytest) for the score-table emit; Vite + React + TS + Tailwind v4 (vitest/RTL) for derivation, re-ranking, and UI.

**Spec:** `docs/superpowers/specs/2026-07-23-smite-draft-aware-builds-design.md`

---

## File structure

- `tools/smite/build_index.py` — emit `god_item_scores` (top-N per god). Modify.
- `tools/smite/tests/test_build_index.py` — cover the emit + cap. Modify.
- `04. System/Data/SMITE/_weights.yaml` — new `draft:` tuning block. Modify.
- `viewer/src/types.ts` — `DraftComp`, `ThreatModel`, `DraftBuild`, index additions. Modify.
- `viewer/src/lib/threats.ts` — **new**, pure: comps → threat model → bonus overlay.
- `viewer/src/lib/draftBuild.ts` — **new**, pure: overlay + base scores → adapted core + reasons.
- `viewer/src/lib/draft.ts` — **new**: `useDraft()` localStorage state hook.
- `viewer/src/components/DraftBar.tsx` — **new**: ally/enemy slots + threat chips + Clear.
- `viewer/src/components/DetailPanel.tsx` — mount DraftBar + the Draft tab. Modify.

Rationale: all game logic lives in two dependency-free pure modules (`threats`, `draftBuild`) so it is exhaustively unit-testable without React; UI is a thin shell over them.

---

## Task 1: Ship per-god base scores

**Files:**
- Modify: `tools/smite/build_index.py`
- Modify: `tools/smite/tests/test_build_index.py`
- Modify: `04. System/Data/SMITE/_weights.yaml`

- [ ] **Step 1: Add the `draft` tuning block to `_weights.yaml`** (top level, after `kit_blend`):

```yaml
# Draft-aware builds: how an entered enemy/ally comp skews item scores. The
# browser applies these as a tag/stat overlay on the shipped base scores.
draft:
  score_cap: 40          # items shipped per god (a god's #60 item can't win a slot)
  max_bonus: 0.12        # clamp on the total bonus any one item can receive
  per_enemy: 0.02        # weight per matching enemy god (x count)
  tag_bonus:             # threat -> item effect_tag
    healers: {anti-heal: 1.0}
    lockdown: {cc-immunity: 1.0, peel: 0.4}
    crit: {anti-crit: 1.0}
    tanks: {protection-shred: 1.0}
  stat_bonus:            # threat -> item stat
    magical: {Magical Protection: 1.0}
    physical: {Physical Protection: 1.0}
    tanks: {Penetration: 0.6}
  ally_covered: -0.5     # multiplier when an ally already covers the job
  ally_gap: 0.5          # extra multiplier when NOBODY covers it
```

- [ ] **Step 2: Write the failing test** in `tools/smite/tests/test_build_index.py`:

```python
def test_build_index_emits_capped_god_item_scores():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    scores = r["god_item_scores"]
    assert set(scores) == {g["name"] for g in r["gods"]}
    cap = 40
    for god, table in scores.items():
        assert 0 < len(table) <= cap, f"{god} has {len(table)} entries"
        assert all(isinstance(v, float) for v in table.values())
```

- [ ] **Step 3: Run it, confirm it fails** with `KeyError: 'god_item_scores'`:

Run: `cd tools && python -m pytest smite/tests/test_build_index.py::test_build_index_emits_capped_god_item_scores -q`
Expected: FAIL

- [ ] **Step 4: Implement.** In `build_index.build_index`, after the existing `eff` computation, score every god and keep the top N:

```python
    draft_cfg = (weights.get("draft") or {})
    cap = int(draft_cfg.get("score_cap", 40))
    god_item_scores = {}
    for god in gods:
        build_note = builds_by_god.get(god["name"], {})
        rows = scoring.score_god_items(god, items, build_note, eff, weights, tags_map)
        god_item_scores[god["name"]] = {
            r["item"]: round(float(r["total"]), 4) for r in rows[:cap]
        }
```

Add `"god_item_scores": god_item_scores` to the returned dict. Reuse whatever
`weights` / `tags_map` / `builds_by_god` the function already has in scope — read
the file first and match its existing locals rather than re-loading.

- [ ] **Step 5: Run the test, confirm it passes.** Then the full suite:

Run: `cd tools && python -m pytest smite/tests/ -q -m "not live"`
Expected: PASS (258 prior + 1)

- [ ] **Step 6: Regenerate and check the size cost**

Run: `cd tools && python -m smite.build_index && python -c "import json,os;p='../viewer/public/index.json';d=json.load(open(p));print('MB %.2f'%(os.path.getsize(p)/1048576));print('gods scored',len(d['god_item_scores']))"`
Expected: index grows a few hundred KB; all 87 gods scored.

- [ ] **Step 7: Commit**

```bash
git add tools/smite/build_index.py tools/smite/tests/test_build_index.py "04. System/Data/SMITE/_weights.yaml" viewer/public/index.json
git commit -m "feat(smite): ship per-god item score table for draft-aware builds"
```

---

## Task 2: Threat derivation (pure TS)

**Files:**
- Create: `viewer/src/lib/threats.ts`
- Create: `viewer/src/lib/threats.test.ts`
- Modify: `viewer/src/types.ts`

- [ ] **Step 1: Add types** to `viewer/src/types.ts`:

```ts
export interface DraftComp { allies: string[]; enemies: string[]; }
export interface ThreatModel {
  magical: number; physical: number;      // enemy damage-type counts
  healers: number; lockdown: number; crit: number; tanks: number;
  allyCovers: Record<string, boolean>;    // effect_tag -> covered by an ally
  allyAllPhysical: boolean;
}
export interface DraftConfig {
  max_bonus: number; per_enemy: number;
  tag_bonus: Record<string, Record<string, number>>;
  stat_bonus: Record<string, Record<string, number>>;
  ally_covered: number; ally_gap: number;
}
```
Also add `god_item_scores?: Record<string, Record<string, number>>` and
`draft?: DraftConfig` to `IndexData` (the Python side ships `draft` from
`_weights.yaml` — if it does not, default it in the hook; see Task 4 note).

- [ ] **Step 2: Write the failing tests** in `viewer/src/lib/threats.test.ts`:

```ts
import { describe, it, expect } from "vitest";
import { deriveThreats, threatOverlay } from "./threats";
import type { God } from "../types";

const god = (name: string, damage_type: string, specs: string[] = []): God =>
  ({ name, damage_type, specializations: specs, pantheon: "", role: "",
     base_stats: {}, abilities: [], aspects: [] } as unknown as God);

const CFG = { max_bonus: 0.12, per_enemy: 0.02,
  tag_bonus: { healers: { "anti-heal": 1 }, lockdown: { "cc-immunity": 1 } },
  stat_bonus: { magical: { "Magical Protection": 1 } },
  ally_covered: -0.5, ally_gap: 0.5 };

describe("deriveThreats", () => {
  it("counts enemy damage types", () => {
    const t = deriveThreats({ allies: [], enemies: ["A", "B", "C"] },
      { A: god("A", "magical"), B: god("B", "magical"), C: god("C", "physical") }, {});
    expect(t.magical).toBe(2);
    expect(t.physical).toBe(1);
  });

  it("counts healers and lockdown from specializations", () => {
    const t = deriveThreats({ allies: [], enemies: ["H", "L"] },
      { H: god("H", "magical", ["Healing"]), L: god("L", "physical", ["Lockdown"]) }, {});
    expect(t.healers).toBe(1);
    expect(t.lockdown).toBe(1);
  });

  it("marks a job covered when an ally's core brings that tag", () => {
    const t = deriveThreats({ allies: ["Ally"], enemies: [] },
      { Ally: god("Ally", "magical") }, { Ally: ["anti-heal"] });
    expect(t.allyCovers["anti-heal"]).toBe(true);
  });

  it("returns an all-zero model for an empty comp", () => {
    const t = deriveThreats({ allies: [], enemies: [] }, {}, {});
    expect(t.magical + t.physical + t.healers + t.lockdown).toBe(0);
  });
});

describe("threatOverlay", () => {
  it("scales a tag bonus by enemy count", () => {
    const one = threatOverlay({ ...EMPTY, healers: 1 }, CFG);
    const two = threatOverlay({ ...EMPTY, healers: 2 }, CFG);
    expect(two.tags["anti-heal"]).toBeGreaterThan(one.tags["anti-heal"]);
  });

  it("raises an uncovered job and lowers a covered one", () => {
    const gap = threatOverlay({ ...EMPTY, healers: 2 }, CFG);
    const covered = threatOverlay(
      { ...EMPTY, healers: 2, allyCovers: { "anti-heal": true } }, CFG);
    expect(covered.tags["anti-heal"]).toBeLessThan(gap.tags["anti-heal"]);
  });
});

const EMPTY: import("../types").ThreatModel = {
  magical: 0, physical: 0, healers: 0, lockdown: 0, crit: 0, tanks: 0,
  allyCovers: {}, allyAllPhysical: false,
};
```

- [ ] **Step 3: Run, confirm failure**

Run: `cd viewer && npx vitest run src/lib/threats.test.ts`
Expected: FAIL — cannot resolve `./threats`

- [ ] **Step 4: Implement `viewer/src/lib/threats.ts`**

```ts
import type { God, DraftComp, ThreatModel, DraftConfig } from "../types";

const HEAL = ["Healing", "Sustain"];
const LOCK = ["Lockdown", "Crowd Control", "Area Control"];
const CRIT = ["Carry", "Sharpshooter"];
const TANK = ["Tank"];

const hasSpec = (g: God | undefined, list: string[]) =>
  !!g && (g.specializations ?? []).some((s) => list.includes(s));

/** Comps -> a graded threat model. `allyCores` maps an ally god name to the
 *  effect_tags its own suggested core brings (what that teammate likely covers). */
export function deriveThreats(
  comp: DraftComp,
  godsByName: Record<string, God>,
  allyCores: Record<string, string[]>,
): ThreatModel {
  const enemies = comp.enemies.map((n) => godsByName[n]).filter(Boolean);
  const allies = comp.allies.map((n) => godsByName[n]).filter(Boolean);
  const allyCovers: Record<string, boolean> = {};
  for (const name of comp.allies) {
    for (const tag of allyCores[name] ?? []) allyCovers[tag] = true;
  }
  return {
    magical: enemies.filter((g) => g.damage_type === "magical").length,
    physical: enemies.filter((g) => g.damage_type === "physical").length,
    healers: enemies.filter((g) => hasSpec(g, HEAL)).length,
    lockdown: enemies.filter((g) => hasSpec(g, LOCK)).length,
    crit: enemies.filter((g) => hasSpec(g, CRIT)).length,
    tanks: enemies.filter((g) => hasSpec(g, TANK)).length,
    allyCovers,
    allyAllPhysical: allies.length > 0 && allies.every((g) => g.damage_type === "physical"),
  };
}

/** Threat model -> {tags, stats} bonus overlay (pre-clamp; the clamp is applied
 *  per item in draftBuild, since it bounds an item's TOTAL bonus). */
export function threatOverlay(t: ThreatModel, cfg: DraftConfig) {
  const tags: Record<string, number> = {};
  const stats: Record<string, number> = {};
  const counts: Record<string, number> = {
    healers: t.healers, lockdown: t.lockdown, crit: t.crit, tanks: t.tanks,
    magical: t.magical, physical: t.physical,
  };
  const add = (into: Record<string, number>, key: string, weight: number) => {
    const n = counts[key] ?? 0;
    if (!n) return;
    into[key] = into[key] ?? 0;
  };
  void add; // (kept explicit below for clarity)

  for (const [threat, map] of Object.entries(cfg.tag_bonus ?? {})) {
    const n = counts[threat] ?? 0;
    if (!n) continue;
    for (const [tag, w] of Object.entries(map)) {
      let mult = 1;
      if (t.allyCovers[tag]) mult += cfg.ally_covered;   // covered -> damped
      else mult += cfg.ally_gap;                          // nobody covers -> raised
      tags[tag] = (tags[tag] ?? 0) + n * cfg.per_enemy * w * mult;
    }
  }
  for (const [threat, map] of Object.entries(cfg.stat_bonus ?? {})) {
    const n = counts[threat] ?? 0;
    if (!n) continue;
    for (const [stat, w] of Object.entries(map)) {
      stats[stat] = (stats[stat] ?? 0) + n * cfg.per_enemy * w;
    }
  }
  if (t.allyAllPhysical) {
    stats["Penetration"] = (stats["Penetration"] ?? 0) + cfg.per_enemy;
  }
  return { tags, stats };
}
```

- [ ] **Step 5: Run the tests, confirm they pass**

Run: `cd viewer && npx vitest run src/lib/threats.test.ts`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add viewer/src/lib/threats.ts viewer/src/lib/threats.test.ts viewer/src/types.ts
git commit -m "feat(viewer): derive a threat model from ally/enemy comps"
```

---

## Task 3: Adapted build assembly (pure TS)

**Files:**
- Create: `viewer/src/lib/draftBuild.ts`
- Create: `viewer/src/lib/draftBuild.test.ts`

- [ ] **Step 1: Write the failing tests** in `viewer/src/lib/draftBuild.test.ts`:

```ts
import { describe, it, expect } from "vitest";
import { adaptedCore } from "./draftBuild";
import type { Item } from "../types";

const item = (name: string, stats: Record<string, string> = {}, tags: string[] = []): Item =>
  ({ name, tier: 3, cost: 2500, stats, passive: "", builds_from: [], builds_into: [],
     effect_tags: tags, efficiency_tier: null } as unknown as Item);

const ITEMS = [
  item("Alpha"), item("Beta"), item("Gamma"), item("Delta"),
  item("Epsilon"), item("Zeta"), item("AntiHeal", {}, ["anti-heal"]),
  item("Boots1", { "Movement Speed": "18%" }), item("Boots2", { "Movement Speed": "18%" }),
  item("Sustain1", { Lifesteal: "10%" }), item("Sustain2", {}, ["sustain"]),
];
const BASE: Record<string, number> = {
  Alpha: 0.6, Beta: 0.59, Gamma: 0.58, Delta: 0.57, Epsilon: 0.56, Zeta: 0.55,
  AntiHeal: 0.40, Boots1: 0.54, Boots2: 0.53, Sustain1: 0.52, Sustain2: 0.51,
};
const byName = Object.fromEntries(ITEMS.map((i) => [i.name, i]));

it("returns the base top-6 when there is no threat overlay", () => {
  const r = adaptedCore(BASE, byName, { tags: {}, stats: {} }, { maxBonus: 0.12 });
  expect(r.core).toEqual(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"]);
});

it("promotes an item whose tag the overlay rewards, with a reason", () => {
  const r = adaptedCore(BASE, byName, { tags: { "anti-heal": 0.3 }, stats: {} },
    { maxBonus: 0.5 });
  expect(r.core).toContain("AntiHeal");
  expect(r.reasons["AntiHeal"]).toMatch(/anti-heal/i);
});

it("clamps the total bonus so a huge overlay cannot fully rewrite the build", () => {
  const r = adaptedCore(BASE, byName, { tags: { "anti-heal": 99 }, stats: {} },
    { maxBonus: 0.12 });
  const changed = r.core.filter((n) => !["Alpha","Beta","Gamma","Delta","Epsilon","Zeta"].includes(n));
  expect(changed.length).toBeLessThanOrEqual(3);
});

it("allows at most one boots", () => {
  const base = { ...BASE, Boots1: 0.99, Boots2: 0.98 };
  const r = adaptedCore(base, byName, { tags: {}, stats: {} }, { maxBonus: 0.12 });
  expect(r.core.filter((n) => n.startsWith("Boots")).length).toBe(1);
});

it("respects the lifesteal cap", () => {
  const base = { ...BASE, Sustain1: 0.99, Sustain2: 0.98 };
  const r = adaptedCore(base, byName, { tags: {}, stats: {} }, { maxBonus: 0.12, maxLifesteal: 1 });
  expect(r.core.filter((n) => n.startsWith("Sustain")).length).toBe(1);
});

it("always returns six unique items", () => {
  const r = adaptedCore(BASE, byName, { tags: {}, stats: {} }, { maxBonus: 0.12 });
  expect(r.core).toHaveLength(6);
  expect(new Set(r.core).size).toBe(6);
});
```

- [ ] **Step 2: Run, confirm failure**

Run: `cd viewer && npx vitest run src/lib/draftBuild.test.ts`
Expected: FAIL — cannot resolve `./draftBuild`

- [ ] **Step 3: Implement `viewer/src/lib/draftBuild.ts`**

```ts
import type { Item } from "../types";

export interface Overlay { tags: Record<string, number>; stats: Record<string, number>; }
export interface AdaptOpts { maxBonus: number; maxLifesteal?: number; n?: number; }
export interface AdaptedCore {
  core: string[];
  reasons: Record<string, string>;   // item -> why it gained
  bonuses: Record<string, number>;
}

// Mirrors assemble._is_boots / _is_lifesteal so the client build obeys the same
// constraints the Python assembler does.
const isBoots = (it: Item | undefined) => !!it && "Movement Speed" in (it.stats ?? {});
const isLifesteal = (it: Item | undefined) =>
  !!it && ((it.effect_tags ?? []).includes("sustain") ||
           Object.keys(it.stats ?? {}).some((s) => s.includes("Lifesteal")));

export function adaptedCore(
  base: Record<string, number>,
  itemsByName: Record<string, Item>,
  overlay: Overlay,
  opts: AdaptOpts,
): AdaptedCore {
  const n = opts.n ?? 6;
  const maxLifesteal = opts.maxLifesteal ?? 1;
  const bonuses: Record<string, number> = {};
  const reasons: Record<string, string> = {};

  const scored = Object.entries(base).map(([name, total]) => {
    const it = itemsByName[name];
    let bonus = 0;
    const why: string[] = [];
    for (const tag of it?.effect_tags ?? []) {
      const w = overlay.tags[tag];
      if (w) { bonus += w; why.push(tag); }
    }
    for (const stat of Object.keys(it?.stats ?? {})) {
      const w = overlay.stats[stat];
      if (w) { bonus += w; why.push(stat); }
    }
    bonus = Math.max(-opts.maxBonus, Math.min(opts.maxBonus, bonus));
    if (bonus > 0) { bonuses[name] = bonus; reasons[name] = why.join(", "); }
    return { name, score: total + bonus };
  });

  // Deterministic: score desc, then name — ties must not depend on object order.
  scored.sort((a, b) => b.score - a.score || a.name.localeCompare(b.name));

  const core: string[] = [];
  let haveBoots = false;
  let lifesteal = 0;
  for (const { name } of scored) {
    if (core.length >= n) break;
    const it = itemsByName[name];
    if (isBoots(it)) { if (haveBoots) continue; haveBoots = true; }
    if (isLifesteal(it)) { if (lifesteal >= maxLifesteal) continue; lifesteal += 1; }
    core.push(name);
  }
  return { core, reasons, bonuses };
}
```

- [ ] **Step 4: Run the tests, confirm they pass**

Run: `cd viewer && npx vitest run src/lib/draftBuild.test.ts`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add viewer/src/lib/draftBuild.ts viewer/src/lib/draftBuild.test.ts
git commit -m "feat(viewer): re-rank and assemble a draft-adapted core"
```

---

## Task 4: Draft state hook (localStorage)

**Files:**
- Create: `viewer/src/lib/draft.ts`
- Create: `viewer/src/lib/draft.test.ts`

Model it on the existing `viewer/src/lib/pins.ts` (same persistence idiom).

- [ ] **Step 1: Failing test** — `useDraft` starts empty, `setAlly(i, name)` /
  `setEnemy(i, name)` place a god at a slot, `clear()` empties, and state
  round-trips through `localStorage` under `smite:draft`. Use
  `@testing-library/react`'s `renderHook` + `act`.
- [ ] **Step 2: Run, confirm failure.** `cd viewer && npx vitest run src/lib/draft.test.ts`
- [ ] **Step 3: Implement** — `useDraft()` holding `{allies: string[4], enemies: string[5]}`
  (fixed-length arrays of names, `""` for an empty slot), persisted exactly like
  `pins.ts` (try/catch around storage; ignore quota/private-mode failures).
- [ ] **Step 4: Run, confirm pass.**
- [ ] **Step 5: Commit** `git add viewer/src/lib/draft.ts viewer/src/lib/draft.test.ts && git commit -m "feat(viewer): persist the entered draft"`

---

## Task 5: DraftBar component

**Files:**
- Create: `viewer/src/components/DraftBar.tsx`
- Create: `viewer/src/components/DraftBar.test.tsx`

- [ ] **Step 1: Failing tests** — renders 4 ally + 5 enemy slots; clicking a slot
  opens the god picker; picking a god fills that slot (assert its name/`aria-label`);
  threat chips render the derived summary (e.g. `2 healers`); Clear empties the slots.
- [ ] **Step 2: Run, confirm failure.**
- [ ] **Step 3: Implement.** Props: `{ gods, draft, onSetAlly, onSetEnemy, onClear, threats }`.
  Collapsible (`useState`), styled to the existing system: `bg-bg2 border-line rounded-md`,
  `.press` on slots, `font-mono text-[10px] text-faint` chips, role/damage accents via
  `roleAccent`. Reuse the god-picker pattern from `AddGodModal` (filter to gods that
  exist in `god_item_scores`, i.e. the 87 with data). Empty slot = a dashed outline
  `+` button with an `aria-label` like `Add enemy 3`.
- [ ] **Step 4: Run, confirm pass.**
- [ ] **Step 5: Commit.**

---

## Task 6: Wire the Draft tab into DetailPanel

**Files:**
- Modify: `viewer/src/components/DetailPanel.tsx`
- Modify: `viewer/src/components/DetailPanel.test.tsx`

- [ ] **Step 1: Failing test** — with `god_item_scores` + a draft containing an
  enemy healer, a **Draft** tab appears; selecting it renders 6 items; an item
  promoted by the overlay shows its reason; with an empty draft the tab renders a
  hint to enter a comp rather than a bogus build.
- [ ] **Step 2: Run, confirm failure.**
- [ ] **Step 3: Implement.** Mount `<DraftBar>` above the build tabs. Add a `Draft`
  entry to the existing variant tabs. On render: `deriveThreats` → `threatOverlay`
  → `adaptedCore(godItemScores[god], itemsByName, overlay, {maxBonus, maxLifesteal})`.
  Show the resulting 6 with the existing slot-row styling; mark items **not** in the
  base core using the established diff style (added = `text-blue`), and show
  `reasons[item]` beneath. Keep the starter row unchanged. The draft overlay must
  compose **on top of** the active mode/flavor selection, not replace it.
  Ally core tags for `deriveThreats` come from each ally god's suggested core in
  `builds` (map its `slot_order` items → their `effect_tags`).
- [ ] **Step 4: Run, confirm pass.**
- [ ] **Step 5: Commit.**

---

## Task 7: Full verification

- [ ] Run the full viewer suite: `cd viewer && npx vitest run` — all green.
- [ ] Type + build gate: `cd viewer && npm run build` — must pass (`tsc -b` type-checks tests too).
- [ ] Full Python suite: `cd tools && python -m pytest smite/tests/ -q -m "not live"` — all green.
- [ ] `cd tools && python -m smite.data_audit` — exit 0.
- [ ] Browser-verify on a real god: enter a comp with 2 healers + 3 magical enemies,
      confirm the Draft tab promotes anti-heal / magical protection with reasons, that
      changed slots are marked, that Clear resets, and that a reload restores the draft.
      Check desktop **and** 390px.
- [ ] Report the index size delta.

---

## Self-review notes

- **Spec coverage:** threat derivation (Task 2) · ally responsibility incl. damage
  mix (Task 2, `allyAllPhysical` + `ally_covered`/`ally_gap`) · live re-rank +
  constraint-mirroring assembly (Task 3) · persistence (Task 4) · draft bar +
  threat read-out (Task 5) · Draft tab, reasons, stacking with mode/flavor (Task 6)
  · payload cap + tunables (Task 1). All spec sections are covered.
- **Type consistency:** `DraftComp`/`ThreatModel`/`DraftConfig` are defined once in
  Task 2 and consumed unchanged in Tasks 3–6; `Overlay` is defined in Task 3 and is
  exactly the `{tags, stats}` object `threatOverlay` returns.
- **Known rough edge:** the `add` helper stub inside `threatOverlay` (Task 2, Step 4)
  is vestigial — delete it during implementation; the loops below it are the real logic.
