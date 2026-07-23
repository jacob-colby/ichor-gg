# Modals, Gods tab, freshness UI, second source — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans. Steps use checkbox (`- [ ]`) tracking. The viewer was recently rewritten by another session — **read the current file before every "modify" step**; the snippets show intent, not necessarily verbatim surrounding code.

**Goal:** pick% popover fix, universal freshness stamp + dev scraping banner, a filterable Gods tab, an add-god icon modal (with a scraped roster), an item-picker modal with filters, and (spike-gated) a second community-build source.

**Architecture:** Python — `build_index` gains `data_updated` + `roster`; `refresh` gains a roster fetch; (gated) a second stats-site parser + list-valued community entries. Viewer — new `GodsIndex`, `AddGodModal`, `ItemPickerModal`, a freshness stamp, a community-build selector, and the popover fix. Real typecheck is `npm run build` (`tsc -b`).

**Tech Stack:** Python 3.10 (pytest); Vite + React + TS + Vitest; Chrome MCP for visual verification.

**Reference spec:** [2026-07-22-smite-modals-gods-tab-freshness-source-design.md](../specs/2026-07-22-smite-modals-gods-tab-freshness-source-design.md)

---

## PHASE A — pick% popover fix + chip cleanups

### Task A1: popover shows "off-meta" instead of a 0 pick bar
**Files:** Modify `viewer/src/components/DetailPanel.tsx`; Test `viewer/src/components/DetailPanel.test.tsx`. **Read DetailPanel.tsx first** (the `ScoreBar`/`ItemTooltipBody` block near the top, ~lines 20–85).

- [ ] **Step 1: Failing test** — add to `DetailPanel.test.tsx`: render a suggested build whose `slot_scores` has one item with `pick: 0` and one with `pick: 0.4`; hover isn't needed — assert the tooltip body renders "off-meta" text for the 0 item and a pick value for the other. If the popover is hover-only in tests, test the `ItemTooltipBody` component directly (export it or test via the rendered tooltip content the existing tests already use). Mirror the existing popover test at ~line 359.
```tsx
  it("pick bar reads off-meta when the pick signal is 0", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A", "B"], situational_swaps: [], rationale: "",
        slot_scores: { A: { total: .5, efficiency: .6, win: .5, pick: 0, fit: .7 },
                       B: { total: .5, efficiency: .6, win: .5, pick: 0.4, fit: .7 } } },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any} mode="Conquest" onModeChange={() => {}} />);
    // both slot tooltips are rendered in the DOM (Tooltip renders content); assert copy
    expect(screen.getByText(/off-meta/i)).toBeInTheDocument();
  });
```
(Adapt to however the current tests assert popover content — if the Tooltip only renders on hover, fire a mouseEnter on the slot row first.)

- [ ] **Step 2: Run, confirm FAIL** — `cd viewer && npx vitest run src/components/DetailPanel.test.tsx -t "off-meta"`

- [ ] **Step 3: Implement** — in the popover's score block, replace the plain pick `ScoreBar` with a conditional: when `score.pick > 0`, render `<ScoreBar label="pick" value={score.pick} />`; else render a muted line `pick — off-meta (not in community build)`. Keep value/win/fit bars unchanged.

- [ ] **Step 4: Run, confirm PASS** — `cd viewer && npx vitest run src/components/DetailPanel.test.tsx`

- [ ] **Step 5: Chip cleanups** — (a) in the off-meta marker's `title`, include the community pick% when the item is in the community build (you have `communityNames`; if you also have per-item community pick, show it). (b) In Python, grep for the dead `kit_blend` fallback literal (`grep -rn "kit_blend" tools/smite/`) and remove the unreachable default. (c) Fix the cosmetic type cast the reviewer flagged (grep the DetailPanel for an `as any`/double cast near slot_scores). (d) `grep -rn "�" viewer/public/index.json tools/smite` — if fun rationales contain a literal replacement char, fix the source string in the flavor config/recommend to a real UTF-8 `—` and note it regenerates in Phase G.

- [ ] **Step 6: Run suites** — `cd viewer && npx vitest run` and `cd ../tools && python -m pytest smite/tests/ -q -m "not live"`

- [ ] **Step 7: Commit**
```bash
git add viewer/src/components/DetailPanel.tsx viewer/src/components/DetailPanel.test.tsx tools/smite/*.py
git commit -m "fix(viewer): off-meta pick label in why-popover + chip cleanups"
```

---

## PHASE B — freshness UI

### Task B1: `data_updated` in build_index
**Files:** Modify `tools/smite/build_index.py`; Test `tools/smite/tests/test_build_index.py`. **Read `build_index.py` first.**

- [ ] **Step 1: Failing test**
```python
def test_build_index_emits_data_updated():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    assert "data_updated" in r and isinstance(r["data_updated"], str) and r["data_updated"]
```
- [ ] **Step 2: Run, confirm FAIL** — `cd tools && python -m pytest smite/tests/test_build_index.py -k data_updated -v`
- [ ] **Step 3: Implement** — in `build_index()`, compute the max `last_verified` across `gods` + each build note's community entries (they're `str` dates), and add `"data_updated": <max or "">` to the returned dict. Guard missing/None.
- [ ] **Step 4: PASS + full suite** — `cd tools && python -m pytest smite/tests/ -q -m "not live"`
- [ ] **Step 5: Commit** — `git add tools/smite/build_index.py tools/smite/tests/test_build_index.py && git commit -m "feat(smite): data_updated (max last_verified) in index"`

### Task B2: freshness stamp + dev scraping banner
**Files:** Modify `viewer/src/types.ts` (`IndexData.data_updated?: string`), `viewer/src/App.tsx`; Test `viewer/src/App.test.tsx`. **Read App.tsx first** (nav + ManageGods wiring).

- [ ] **Step 1: Failing test** — extend the App test stub data with `data_updated: "2026-07-19"`; assert `Data from` text appears in the nav.
- [ ] **Step 2: FAIL** — `cd viewer && npx vitest run src/App.test.tsx`
- [ ] **Step 3: Implement** — (a) add `data_updated?: string` to `IndexData`. (b) In the top nav (or footer), render `{data.data_updated && <span className="text-[10px] text-muted">Data from {data.data_updated}</span>}`. (c) **Dev scraping banner:** lift a `scraping` boolean to App state; pass a setter to `ManageGods`/add-god so it flips true during the `/api/gods` request and false on resolve; when true and `isDev`, render a small fixed banner "Scraping new data…". (Keep ManageGods' own busy state; App banner is the global signal.)
- [ ] **Step 4: PASS + build** — `cd viewer && npx vitest run && npm run build`
- [ ] **Step 5: Commit** — `git add viewer/src/types.ts viewer/src/App.tsx viewer/src/App.test.tsx && git commit -m "feat(viewer): data-freshness stamp + dev scraping banner"`

---

## PHASE C — Gods tab

### Task C1: `godFilters.ts`
**Files:** Create `viewer/src/lib/godFilters.ts`; Test `viewer/src/lib/godFilters.test.ts` (mirror `itemFilters`).
- [ ] **Step 1: Failing tests** — `filterGods(gods, {q, pantheon, role, damage_type})` narrows by each; `sortGods(gods, "name")`.
```typescript
import { describe, it, expect } from "vitest";
import { filterGods, sortGods } from "./godFilters";
import type { God } from "../types";
const gods = [
  { name: "Ymir", pantheon: "Norse", role: "Solo", damage_type: "magical" },
  { name: "Ra", pantheon: "Egyptian", role: "Mid", damage_type: "magical" },
  { name: "Chiron", pantheon: "Greek", role: "Carry", damage_type: "physical" },
] as unknown as God[];
describe("godFilters", () => {
  it("filters", () => {
    expect(filterGods(gods, { q: "ra" }).map(g => g.name)).toEqual(["Ra"]);
    expect(filterGods(gods, { role: "Mid" }).map(g => g.name)).toEqual(["Ra"]);
    expect(filterGods(gods, { pantheon: "Norse" }).map(g => g.name)).toEqual(["Ymir"]);
    expect(filterGods(gods, { damage_type: "physical" }).map(g => g.name)).toEqual(["Chiron"]);
  });
  it("sorts by name", () => { expect(sortGods(gods, "name").map(g => g.name)).toEqual(["Chiron", "Ra", "Ymir"]); });
});
```
- [ ] **Step 2: FAIL** — `cd viewer && npx vitest run src/lib/godFilters.test.ts`
- [ ] **Step 3: Implement** `godFilters.ts`:
```typescript
import type { God } from "../types";
export interface GodFilter { q?: string; pantheon?: string; role?: string; damage_type?: string }
export function filterGods(gods: God[], f: GodFilter): God[] {
  const q = f.q?.trim().toLowerCase();
  return gods.filter((g) => {
    if (q && !g.name.toLowerCase().includes(q)) return false;
    if (f.pantheon && g.pantheon !== f.pantheon) return false;
    if (f.role && g.role !== f.role) return false;
    if (f.damage_type && g.damage_type !== f.damage_type) return false;
    return true;
  });
}
export function sortGods(gods: God[], by: "name" = "name"): God[] {
  void by; return [...gods].sort((a, b) => a.name.localeCompare(b.name));
}
```
- [ ] **Step 4: PASS** — `cd viewer && npx vitest run src/lib/godFilters.test.ts`
- [ ] **Step 5: Commit** — `git add viewer/src/lib/godFilters.ts viewer/src/lib/godFilters.test.ts && git commit -m "feat(viewer): god filter/sort helpers"`

### Task C2: `GodsIndex` + route + nav
**Files:** Create `viewer/src/components/GodsIndex.tsx`; Test `GodsIndex.test.tsx`; Modify `viewer/src/lib/useHashRoute.ts` (add `gods` view), `viewer/src/App.tsx` (nav button + render). **Read useHashRoute.ts + App.tsx first.**
- [ ] **Step 1: Router** — in `parseHash`, add: `if (parts[0] === "gods") return { view: "gods", tab: "builds" };` and to the `Route.view` union add `"gods"`; add `toHash.gods = () => "#/gods"`. Update the useHashRoute test with a `#/gods` case.
- [ ] **Step 2: Failing GodsIndex test** — renders a card per god, filters by search:
```tsx
import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { GodsIndex } from "./GodsIndex";
import type { God } from "../types";
const gods = [
  { name: "Ymir", pantheon: "Norse", role: "Solo", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
  { name: "Ra", pantheon: "Egyptian", role: "Mid", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
] as unknown as God[];
describe("GodsIndex", () => {
  it("renders and filters", () => {
    render(<GodsIndex gods={gods} />);
    expect(screen.getByText("Ymir")).toBeInTheDocument();
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "ra" } });
    expect(screen.getByText("Ra")).toBeInTheDocument();
    expect(screen.queryByText("Ymir")).not.toBeInTheDocument();
  });
});
```
- [ ] **Step 3: FAIL** — `cd viewer && npx vitest run src/components/GodsIndex.test.tsx`
- [ ] **Step 4: Implement `GodsIndex.tsx`** — mirror `ItemsShop.tsx`: a filter bar (search + pantheon/role/damage selects built from `Array.from(new Set(gods.map(...)))`) over `filterGods`+`sortGods`, and a card grid. Each card: headshot `/icons/${iconSlug(g.name)}-head.png` (with the same onError retry used elsewhere), name, `pantheon · role · damage_type`; onClick `navigate(toHash.god(g.name))`. Use the same grid/card classes as ItemsShop for consistency.
- [ ] **Step 5: Wire App** — read App.tsx; add a **Gods** nav button (between Builds and Items) that `navigate(toHash.gods())` and is active when `route.view === "gods"`; in the view switch, add `route.view === "gods" ? <GodsIndex gods={data.gods} /> : …`. Update App.test if it asserts nav buttons.
- [ ] **Step 6: PASS + build** — `cd viewer && npx vitest run && npm run build`
- [ ] **Step 7: Commit** — `git add viewer/src/components/GodsIndex.tsx viewer/src/components/GodsIndex.test.tsx viewer/src/lib/useHashRoute.ts viewer/src/lib/useHashRoute.test.ts viewer/src/App.tsx viewer/src/App.test.tsx && git commit -m "feat(viewer): filterable Gods tab"`

---

## PHASE D — add-god roster + icon modal

### Task D1: roster fetch + index passthrough
**Files:** Modify `tools/smite/refresh.py`, `tools/smite/build_index.py`; Test `tools/smite/tests/test_build_index.py`. **Read both first.**
- [ ] **Step 1: Implement roster fetch in `refresh.py`** — a `refresh_roster()` that uses `BrowserFetcher` to fetch the wiki's list-of-gods page (try `https://wiki.smite2.com/w/Gods` or the god category; **verify the URL + parse live during implementation**), extracts every god's display name + portrait thumbnail URL, and writes `04. System/Data/SMITE/_roster.json` = `[{"name": str, "thumb": <url or "">}]`. Add a `--roster` flag to `main`. **Fallback:** if the page is impractical, write `_roster.json` from a hand-maintained list of current SMITE 2 god names (commit that list) — the modal only needs names; thumbs can be blank (modal falls back to initials).
- [ ] **Step 2: build_index passthrough test** (append):
```python
def test_build_index_exposes_roster_when_present(tmp_path):
    # roster is optional; assert build_index returns a list (possibly empty) under "roster"
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    assert "roster" in r and isinstance(r["roster"], list)
```
- [ ] **Step 3: FAIL** then **Implement** — `build_index()` reads `_roster.json` (if present, else `[]`) and returns it under `"roster"`.
- [ ] **Step 4: PASS + full suite** — `cd tools && python -m pytest smite/tests/ -q -m "not live"`
- [ ] **Step 5: Live roster run** — `cd tools && python -m smite.refresh --roster` (or fallback), confirm `_roster.json` has the full god list; `python -m smite.build_index`; check `index.json` `roster` length.
- [ ] **Step 6: Commit** — `git add tools/smite/refresh.py tools/smite/build_index.py tools/smite/tests/test_build_index.py "04. System/Data/SMITE/_roster.json" viewer/public/index.json && git commit -m "feat(smite): god roster fetch + index passthrough"`

### Task D2: `AddGodModal` (dev)
**Files:** Create `viewer/src/components/AddGodModal.tsx`; Test `AddGodModal.test.tsx`; Modify `viewer/src/App.tsx` + `viewer/src/types.ts` (`IndexData.roster?: {name:string; thumb?:string}[]`). Replace the dev text-input add flow with the modal. **Read the current ManageGods/add wiring in App.tsx first.**
- [ ] **Step 1: Failing test** — modal lists roster gods, marks tracked ones, calls `onAdd(name)` for an untracked one:
```tsx
import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { AddGodModal } from "./AddGodModal";
describe("AddGodModal", () => {
  it("lists untracked gods and adds on click", () => {
    const onAdd = vi.fn();
    render(<AddGodModal roster={[{ name: "Ymir" }, { name: "Thor" }]} tracked={["Ymir"]} onAdd={onAdd} onClose={() => {}} />);
    expect(screen.getByText("Ymir")).toBeInTheDocument(); // shown but marked tracked
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "thor" } });
    fireEvent.click(screen.getByText("Thor"));
    expect(onAdd).toHaveBeenCalledWith("Thor");
  });
});
```
- [ ] **Step 2: FAIL** — `cd viewer && npx vitest run src/components/AddGodModal.test.tsx`
- [ ] **Step 3: Implement `AddGodModal.tsx`** — a fixed overlay (like `Legend`), a search input, and a grid of roster gods; tracked gods rendered dimmed with a "✓ tracked" marker and non-clickable; untracked gods clickable → `onAdd(name)`. Each tile: thumb `<img src={g.thumb}>` if present else a circle with the initial; name below.
- [ ] **Step 4: Wire App** — read App.tsx: add `roster?` to `IndexData`; replace the dev add-god text input with an **"＋ Add god"** button that opens `<AddGodModal roster={data.roster ?? []} tracked={data.gods.map(g=>g.name)} onAdd={addGod} onClose={...} />`; `addGod(name)` flips the scraping banner (Part B), POSTs `/api/gods {action:"add", name}`, then `reload()` + closes on success. Keep it dev-gated.
- [ ] **Step 5: PASS + build** — `cd viewer && npx vitest run && npm run build`
- [ ] **Step 6: Commit** — `git add viewer/src/components/AddGodModal.tsx viewer/src/components/AddGodModal.test.tsx viewer/src/App.tsx viewer/src/types.ts && git commit -m "feat(viewer): dev add-god icon modal (roster picker)"`

---

## PHASE E — item-picker modal

### Task E1: `ItemPickerModal` + BuildEditor wiring
**Files:** Create `viewer/src/components/ItemPickerModal.tsx`; Test `ItemPickerModal.test.tsx`; Modify `viewer/src/components/BuildEditor.tsx`. **Read BuildEditor.tsx first** (the current item search block).
- [ ] **Step 1: Failing test** — modal filters items and calls `onPick(name)`:
```tsx
import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { ItemPickerModal } from "./ItemPickerModal";
import type { Item } from "../types";
const items = [
  { name: "Deathbringer", tier: 3, cost: 3000, stats: {}, passive: "", builds_from: [], builds_into: [], effect_tags: ["burst"], efficiency_tier: "premium" },
  { name: "Rage", tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: "undervalued" },
] as unknown as Item[];
describe("ItemPickerModal", () => {
  it("filters and picks", () => {
    const onPick = vi.fn();
    render(<ItemPickerModal items={items} onPick={onPick} onClose={() => {}} />);
    fireEvent.change(screen.getByPlaceholderText(/search items/i), { target: { value: "death" } });
    fireEvent.click(screen.getByText("Deathbringer"));
    expect(onPick).toHaveBeenCalledWith("Deathbringer");
  });
});
```
- [ ] **Step 2: FAIL** — `cd viewer && npx vitest run src/components/ItemPickerModal.test.tsx`
- [ ] **Step 3: Implement `ItemPickerModal.tsx`** — a fixed overlay with the shop's filter bar (reuse `filterItems`/`sortItems` + tier/rating/tag/stat/search) and a card grid; clicking a card calls `onPick(name)` (leaves the modal open so multiple can be added, or closes — keep open and let the parent close; simplest: `onPick` then `onClose`). Reuse the `EffBadge`/icon patterns (extract shared bits from ItemsShop if convenient, else duplicate the small card).
- [ ] **Step 4: Wire BuildEditor** — read BuildEditor.tsx; replace the free-text item search with an **"＋ Add item"** button that opens `<ItemPickerModal items={items} onPick={(n)=>{ if (slots.length<6 && !slots.includes(n)) setSlots([...slots,n]); }} onClose={...} />`. Keep the chosen-slot list (reorder/remove), starter, notes, and the 6-item cap. Remove the old search state if now unused.
- [ ] **Step 5: PASS + build** — `cd viewer && npx vitest run && npm run build`
- [ ] **Step 6: Commit** — `git add viewer/src/components/ItemPickerModal.tsx viewer/src/components/ItemPickerModal.test.tsx viewer/src/components/BuildEditor.tsx && git commit -m "feat(viewer): item-picker modal with filters in the build editor"`

---

## PHASE F — second community source (spike-gated)

### Task F1: SPIKE — is a second source viable?
**Files:** none (investigation).
- [ ] **Step 1:** From `tools/`, using the existing fetcher, pull one god page from the top candidates and inspect the HTML for **multiple distinct builds** with item lists (+ win/pick if present):
```python
python -c "
from smite.browser_fetch import BrowserFetcher
from pathlib import Path
f = BrowserFetcher(Path('04. System/Data/SMITE/_cache/spike'))
for url in ['https://smitesource.com/gods/ymir','https://prosmitebuilds.com/gods/ymir','https://smitetracker.com/gods/ymir']:
    try:
        html = f.get(url); print(url, 'len', len(html), 'builds?', html.lower().count('build'))
    except Exception as e: print(url, 'ERR', e)
"
```
  (Adjust URL slugs to each site's real god-page pattern — find them first.) Read the fetched HTML; decide if any site cleanly exposes ≥2 builds per god.
- [ ] **Step 2: Decision** — record the finding in the plan/commit message.
  - **If a source qualifies →** do F2 + F3.
  - **If none qualify →** do F2-alt (per-slot alternatives) + F3, and note the second source was not viable.

### Task F2 (source viable): second-source parser + list-valued community
**Files:** Create `tools/smite/<source>_parser.py`; Modify `tools/smite/refresh.py`, `tools/smite/notes.py` (community may be a list), `tools/smite/build_index.py` (per-item meta across all community entries); Tests with a saved HTML fixture.
- [ ] Parse the source's god page into `[{items:[{name,pick_rate?,win_rate?}], label, source}]`; a `refresh` hook writes these as **additional** `community` entries in the build note (each carrying `source` + `label`); `merge`/index handle a list; per-item `meta` aggregates across sources. Ground-truth for `validate` stays SmiteBrain only. Unit-test the parser on a saved fixture + a build_index test that N community entries survive.

### Task F2-alt (fallback): per-slot alternatives from SmiteBrain
**Files:** Modify `tools/smite/smitebrain_parser.py`; Test its test file.
- [ ] Change `_parse_core_recommended_build` to keep the **top-2** tiles per slot (it already collects all tiles in the first pass), exposing an `alternates: [{name,pick_rate,win_rate}]` per slot on the community entry. Unit-test that alternates are captured. (No new scraper.)

### Task F3: viewer community-build selector / alternates
**Files:** Modify `viewer/src/components/DetailPanel.tsx`, `viewer/src/types.ts`; Test. **Read DetailPanel first.**
- [ ] If community is now a list (F2): render a small **build selector** (sub-tabs or dropdown) above the community slot list when `>1` community entry, switching which entry's `slot_order` shows. If alternates (F2-alt): on each community slot, show the alternate item(s) as a secondary line / hover. One build & no alternates → unchanged. Type updates accordingly. Test the selector appears only when >1.
- [ ] **Commit** each of F2/F2-alt and F3 separately with clear messages.

---

## PHASE G — regenerate + full verification

### Task G1: regen, browser-verify (Chrome MCP), deploy build
- [ ] **Regenerate** — `cd tools && python -m smite.recommend --all && python -m smite.validate && python -m smite.build_index`. Confirm `index.json` has `data_updated`, `roster`, per-item meta, and (F) list/alternate community. Revert EOL-only churn (Builds/Analysis) with `git checkout`, keep real changes.
- [ ] **Suites** — `cd tools && python -m pytest smite/tests/ -q -m "not live"` and `cd ../viewer && npx vitest run && npm run build`.
- [ ] **Chrome MCP visual verification** (real browser, screenshots): (a) pick popover shows "off-meta" not 0; (b) "Data from <date>" in the nav; (c) Gods tab filters + click-through; (d) dev Add-god modal lists roster, marks tracked, scrapes an untracked god (banner shows during); (e) item-picker modal filters + adds to a build; (f) community selector/alternates. Desktop + ~390px. Screenshot each.
- [ ] **Static build check** — `npm run build && npx vite preview`: Gods tab + shop + freshness stamp work; **no** dev-only Add-god modal / manage controls.
- [ ] **Commit generated** — `git add "04. System/Data/SMITE/Analysis/" "04. System/Data/SMITE/_roster.json" "03. Workspaces/Gaming/SMITE 2/Builds/" viewer/public/index.json && git commit -m "chore(smite): regenerate with roster, data_updated, community sources"`

---

## Self-Review

**Spec coverage:** A pick fix + chip cleanups; B `data_updated` + freshness stamp + dev banner; C Gods tab (godFilters + GodsIndex + route + nav); D roster fetch + AddGodModal; E ItemPickerModal + BuildEditor; F spike → (viable) second-source parser + list community + selector, or (fallback) per-slot alternates; G regen + Chrome-MCP verify. All parts mapped; F explicitly gated with a stated fallback.

**Placeholder scan:** the "modify" steps intentionally give change-specs + snippets rather than full files because the viewer was just rewritten by another session — every such step says **read the current file first**; that's a correctness guard, not a placeholder. Greenfield files (godFilters, GodsIndex, AddGodModal, ItemPickerModal, roster) have full code or a precise mirror target.

**Type/name consistency:** `data_updated` (B1 build_index) → `IndexData.data_updated` (B2) → nav stamp. `roster` (D1) → `IndexData.roster` (D2) → AddGodModal. `GodFilter`/`filterGods`/`sortGods` (C1) → GodsIndex (C2). Route `"gods"` added to the union + `toHash.gods` (C2) used by App nav. `onPick`/`onAdd`/`onClose` props match call sites. Community-as-list / alternates types (F) match DetailPanel usage (F3).

**Safety:** dev-only surfaces (Add-god modal, scraping banner) stay behind `import.meta.env.DEV`; scraping goes through the existing Cloudflare-capable fetcher; roster fetch + second source are additive; generated data regenerated deterministically (revert EOL churn); `_archive/` untouched; real typecheck via `npm run build` in every viewer phase.
