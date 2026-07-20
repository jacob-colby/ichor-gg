# Reference pages (items shop, god info, legend, routing) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the viewer into a reference: a filterable items shop with efficiency ratings, a god Info tab (abilities + base stats + aspect), a first-run legend, all reachable via shareable hash URLs — plus richer scraped ability data.

**Architecture:** Python — extend the wiki ability parser to capture description + detail lines. Viewer — a dependency-free hash router; `App` derives view/god/tab/item from the route and renders a top nav (Builds/Items/?) over the existing builds view, a new `ItemsShop` (client-side filter/sort), a `GodInfo` tab, and a `Legend` overlay.

**Tech Stack:** Python 3.10 (pytest); Vite + React 19 + TS + Vitest + RTL. Real viewer typecheck is `npm run build` (`tsc -b`) — `npx tsc --noEmit` is a no-op here.

**Reference spec:** [2026-07-19-smite-reference-pages-design.md](../specs/2026-07-19-smite-reference-pages-design.md)

---

## File Structure
- `tools/smite/wiki_parser.py` — `_parse_abilities` captures description + details (modify).
- `viewer/src/types.ts` — `Ability.description/details`, `IndexData` unchanged (modify).
- `viewer/src/lib/useHashRoute.ts` — route parse/hook/nav helpers (create).
- `viewer/src/lib/itemFilters.ts` — filter/sort/efficiency-label helpers (create).
- `viewer/src/components/ItemsShop.tsx` — shop grid + filter bar + detail (create).
- `viewer/src/components/GodInfo.tsx` — abilities + base stats + aspect (create).
- `viewer/src/components/Legend.tsx` — first-run legend overlay (create).
- `viewer/src/App.tsx` — nav + route wiring (modify).

---

## PHASE A — richer abilities (Python)

### Task A1: `_parse_abilities` captures description + details

**Files:** Modify `tools/smite/wiki_parser.py`; Test `tools/smite/tests/test_wiki_parser.py`

- [ ] **Step 1: Write failing test** (append to `test_wiki_parser.py`; check its imports — it imports `wiki_parser`):
```python
def test_parse_abilities_captures_description_and_details():
    from smite import wiki_parser
    html = """
    <h2><span id="Abilities">Abilities</span></h2>
    <table class="wikitable">
      <tr><th><span>1st Ability</span> <span>Training Exercise</span></th></tr>
      <tr><td>Chiron fires a volley that boosts allies and damages enemies.</td></tr>
      <tr><td><ul>
        <li>Cooldown: 14/13/12/11/10</li>
        <li>Cost: 60/65/70/75/80</li>
        <li>Damage: 90/140/190</li>
      </ul></td></tr>
    </table>
    """
    abilities = wiki_parser._parse_abilities(wiki_parser._soup(html)) \
        if hasattr(wiki_parser, "_soup") else _parse_via_bs(wiki_parser, html)
    a = next(x for x in abilities if x["name"] == "Training Exercise")
    assert a["cooldown"] == [14, 13, 12, 11, 10]
    assert a["cost"] == [60, 65, 70, 75, 80]
    assert "Damage: 90/140/190" in a["details"]
    assert "volley" in a["description"].lower()
    assert "Cooldown: 14" not in a["description"]  # detail lines stripped from prose


def _parse_via_bs(wiki_parser, html):
    from bs4 import BeautifulSoup
    return wiki_parser._parse_abilities(BeautifulSoup(html, "html.parser"))
```
(If the test file already constructs soup a particular way, mirror that; the helper falls back to a direct BeautifulSoup parse.)

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_wiki_parser.py -k description_and_details -v`

- [ ] **Step 3: Implement** — in `wiki_parser.py`, replace `_parse_abilities`'s per-ability body so it also collects `details` and `description`. New function:
```python
def _parse_abilities(soup) -> list:
    abilities = []
    for table in _section_tables(soup, "Abilities"):
        header_th = table.find("th")
        if header_th is None:
            continue
        spans = header_th.find_all("span")
        if len(spans) < 2:
            continue
        ability = {"slot": _clean(spans[0].get_text()), "name": _clean(spans[1].get_text())}

        details = []
        for li in table.find_all("li"):
            text = _clean(li.get_text())
            if not text:
                continue
            details.append(text)
            low = text.lower()
            if low.startswith("cooldown:"):
                ability["cooldown"] = _parse_number_list(text.split(":", 1)[1])
            elif low.startswith("cost:"):
                ability["cost"] = _parse_number_list(text.split(":", 1)[1])
        if details:
            ability["details"] = details

        # Description = the table's prose minus the header (slot+name) and the
        # detail lines. Robust to per-ability layout variation.
        prose = _clean(table.get_text(" "))
        for chunk in [ability["slot"], ability["name"], *details]:
            prose = prose.replace(chunk, " ")
        description = _clean(prose)
        if description:
            ability["description"] = description

        abilities.append(ability)
    return abilities
```

- [ ] **Step 4: Run tests, confirm PASS** + full suite

Run: `cd tools && python -m pytest smite/tests/test_wiki_parser.py -v` then `cd tools && python -m pytest smite/tests/ -q -m "not live"`

- [ ] **Step 5: Commit**
```bash
git add tools/smite/wiki_parser.py tools/smite/tests/test_wiki_parser.py
git commit -m "feat(smite): scrape ability descriptions + detail lines"
```

(The live re-scrape + regenerate happens in Task F1, which validates this end-to-end on real pages.)

---

## PHASE B — routing foundation

### Task B1: `useHashRoute`

**Files:** Create `viewer/src/lib/useHashRoute.ts`; Test `viewer/src/lib/useHashRoute.test.ts`

- [ ] **Step 1: Write failing tests** (`useHashRoute.test.ts`):
```typescript
import { describe, it, expect } from "vitest";
import { parseHash, toHash } from "./useHashRoute";

describe("parseHash", () => {
  it("defaults to the builds home", () => {
    expect(parseHash("")).toEqual({ view: "builds", tab: "builds" });
    expect(parseHash("#/")).toEqual({ view: "builds", tab: "builds" });
  });
  it("parses a god builds + info route", () => {
    expect(parseHash("#/god/Chiron")).toEqual({ view: "builds", god: "Chiron", tab: "builds" });
    expect(parseHash("#/god/Morgan%20Le%20Fay/info")).toEqual({ view: "builds", god: "Morgan Le Fay", tab: "info" });
  });
  it("parses the items shop + item detail", () => {
    expect(parseHash("#/items")).toEqual({ view: "items", tab: "builds" });
    expect(parseHash("#/items/Deathbringer")).toEqual({ view: "items", tab: "builds", item: "Deathbringer" });
  });
});

describe("toHash", () => {
  it("builds encoded hashes", () => {
    expect(toHash.god("Morgan Le Fay")).toBe("#/god/Morgan%20Le%20Fay");
    expect(toHash.godInfo("Chiron")).toBe("#/god/Chiron/info");
    expect(toHash.item("Death's Toll")).toBe("#/items/Death's%20Toll".replace("'", "%27"));
    expect(toHash.items()).toBe("#/items");
  });
});
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/lib/useHashRoute.test.ts`

- [ ] **Step 3: Implement `viewer/src/lib/useHashRoute.ts`**
```typescript
import { useEffect, useState } from "react";

export interface Route {
  view: "builds" | "items";
  god?: string;
  tab: "builds" | "info";
  item?: string;
}

export function parseHash(hash: string): Route {
  const parts = hash.replace(/^#\/?/, "").split("/").filter(Boolean).map(decodeURIComponent);
  if (parts[0] === "items") {
    return { view: "items", tab: "builds", ...(parts[1] ? { item: parts[1] } : {}) };
  }
  if (parts[0] === "god" && parts[1]) {
    return { view: "builds", god: parts[1], tab: parts[2] === "info" ? "info" : "builds" };
  }
  return { view: "builds", tab: "builds" };
}

export const toHash = {
  home: () => "#/",
  god: (n: string) => `#/god/${encodeURIComponent(n)}`,
  godInfo: (n: string) => `#/god/${encodeURIComponent(n)}/info`,
  items: () => "#/items",
  item: (n: string) => `#/items/${encodeURIComponent(n)}`,
};

export function navigate(hash: string): void {
  window.location.hash = hash;
}

export function useHashRoute(): Route {
  const [route, setRoute] = useState<Route>(() => parseHash(window.location.hash));
  useEffect(() => {
    const on = () => setRoute(parseHash(window.location.hash));
    window.addEventListener("hashchange", on);
    return () => window.removeEventListener("hashchange", on);
  }, []);
  return route;
}
```
Note: `encodeURIComponent` encodes spaces as `%20` and `'` as `%27`; the test's `toHash.item("Death's Toll")` expectation reflects that.

- [ ] **Step 4: Run, confirm PASS**

Run: `cd viewer && npx vitest run src/lib/useHashRoute.test.ts`

- [ ] **Step 5: Commit**
```bash
git add viewer/src/lib/useHashRoute.ts viewer/src/lib/useHashRoute.test.ts
git commit -m "feat(viewer): dependency-free hash router"
```

---

## PHASE C — items shop

### Task C1: item filter/sort helpers

**Files:** Create `viewer/src/lib/itemFilters.ts`; Test `viewer/src/lib/itemFilters.test.ts`

- [ ] **Step 1: Write failing tests** (`itemFilters.test.ts`):
```typescript
import { describe, it, expect } from "vitest";
import { filterItems, sortItems, efficiencyLabel, EFFICIENCY } from "./itemFilters";
import type { Item } from "../types";

const items = [
  { name: "Rage", tier: 3, cost: 2500, stats: { "Critical Chance": "20%" }, passive: "", builds_from: [], builds_into: [], effect_tags: ["burst"], efficiency_tier: "undervalued" },
  { name: "Aegis", tier: 3, cost: 2100, stats: { "Max Health": "200" }, passive: "", builds_from: [], builds_into: [], effect_tags: ["aura"], efficiency_tier: "premium" },
  { name: "Dagger", tier: 2, cost: 900, stats: { "Attack Speed": "15%" }, passive: "", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: null },
] as unknown as Item[];

describe("filterItems", () => {
  it("filters by text, tier, efficiency, tag, stat", () => {
    expect(filterItems(items, { q: "rag" }).map((i) => i.name)).toEqual(["Rage"]);
    expect(filterItems(items, { tier: 2 }).map((i) => i.name)).toEqual(["Dagger"]);
    expect(filterItems(items, { efficiency: "premium" }).map((i) => i.name)).toEqual(["Aegis"]);
    expect(filterItems(items, { tag: "burst" }).map((i) => i.name)).toEqual(["Rage"]);
    expect(filterItems(items, { stat: "Max Health" }).map((i) => i.name)).toEqual(["Aegis"]);
  });
  it("returns all with an empty filter", () => {
    expect(filterItems(items, {}).length).toBe(3);
  });
});

describe("sortItems", () => {
  it("sorts by cost and name", () => {
    expect(sortItems(items, "cost-asc").map((i) => i.name)).toEqual(["Dagger", "Aegis", "Rage"]);
    expect(sortItems(items, "name").map((i) => i.name)).toEqual(["Aegis", "Dagger", "Rage"]);
  });
});

describe("efficiencyLabel", () => {
  it("maps tiers to friendly labels", () => {
    expect(efficiencyLabel("undervalued").text).toBe("Underrated");
    expect(efficiencyLabel("premium").text).toBe("Overrated");
    expect(efficiencyLabel("fair").text).toBe("Fair");
    expect(efficiencyLabel(null).text).toBe("—");
    expect(EFFICIENCY.length).toBe(4);
  });
});
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/lib/itemFilters.test.ts`

- [ ] **Step 3: Implement `viewer/src/lib/itemFilters.ts`**
```typescript
import type { Item } from "../types";

export interface ItemFilter {
  q?: string;
  tier?: number;
  efficiency?: string;      // "undervalued" | "fair" | "premium" | "untiered"
  tag?: string;
  stat?: string;
}

export function filterItems(items: Item[], f: ItemFilter): Item[] {
  const q = f.q?.trim().toLowerCase();
  return items.filter((it) => {
    if (q && !it.name.toLowerCase().includes(q)) return false;
    if (f.tier != null && it.tier !== f.tier) return false;
    if (f.efficiency) {
      const eff = it.efficiency_tier ?? "untiered";
      if (f.efficiency === "untiered" ? eff !== "untiered" : eff !== f.efficiency) return false;
    }
    if (f.tag && !(it.effect_tags ?? []).includes(f.tag)) return false;
    if (f.stat && !(it.stats && f.stat in it.stats)) return false;
    return true;
  });
}

export type SortKey = "name" | "cost-asc" | "cost-desc" | "efficiency";
const EFF_ORDER: Record<string, number> = { undervalued: 0, fair: 1, premium: 2 };

export function sortItems(items: Item[], by: SortKey): Item[] {
  const arr = [...items];
  if (by === "name") arr.sort((a, b) => a.name.localeCompare(b.name));
  else if (by === "cost-asc") arr.sort((a, b) => (a.cost ?? 0) - (b.cost ?? 0));
  else if (by === "cost-desc") arr.sort((a, b) => (b.cost ?? 0) - (a.cost ?? 0));
  else if (by === "efficiency")
    arr.sort((a, b) => (EFF_ORDER[a.efficiency_tier ?? ""] ?? 9) - (EFF_ORDER[b.efficiency_tier ?? ""] ?? 9));
  return arr;
}

export interface EfficiencyMeta { key: string; text: string; cls: string }
export const EFFICIENCY: EfficiencyMeta[] = [
  { key: "undervalued", text: "Underrated", cls: "bg-under/20 text-under" },
  { key: "fair", text: "Fair", cls: "bg-line text-muted" },
  { key: "premium", text: "Overrated", cls: "bg-premium/20 text-premium" },
  { key: "untiered", text: "—", cls: "bg-line text-muted" },
];

export function efficiencyLabel(tier: string | null | undefined): EfficiencyMeta {
  return EFFICIENCY.find((e) => e.key === (tier ?? "untiered")) ?? EFFICIENCY[3];
}
```
(Uses the existing `bg-under/text-under` and `bg-premium/text-premium` theme tokens already used in DetailPanel's item tooltip.)

- [ ] **Step 4: Run, confirm PASS**

Run: `cd viewer && npx vitest run src/lib/itemFilters.test.ts`

- [ ] **Step 5: Commit**
```bash
git add viewer/src/lib/itemFilters.ts viewer/src/lib/itemFilters.test.ts
git commit -m "feat(viewer): item filter/sort/efficiency helpers"
```

---

### Task C2: `ItemsShop` component

**Files:** Create `viewer/src/components/ItemsShop.tsx`; Test `viewer/src/components/ItemsShop.test.tsx`

- [ ] **Step 1: Failing test** (`ItemsShop.test.tsx`):
```tsx
import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { ItemsShop } from "./ItemsShop";
import type { Item } from "../types";

const items = [
  { name: "Rage", tier: 3, cost: 2500, stats: { "Critical Chance": "20%" }, passive: "Crit up.", builds_from: [], builds_into: [], effect_tags: ["burst"], efficiency_tier: "undervalued" },
  { name: "Aegis", tier: 3, cost: 2100, stats: { "Max Health": "200" }, passive: "Shield.", builds_from: [], builds_into: [], effect_tags: ["aura"], efficiency_tier: "premium" },
] as unknown as Item[];

describe("ItemsShop", () => {
  it("renders a card per item with its efficiency label, and filters by search", () => {
    render(<ItemsShop items={items} openItem={undefined} />);
    expect(screen.getByText("Rage")).toBeInTheDocument();
    expect(screen.getByText("Aegis")).toBeInTheDocument();
    expect(screen.getByText("Underrated")).toBeInTheDocument();
    expect(screen.getByText("Overrated")).toBeInTheDocument();
    fireEvent.change(screen.getByPlaceholderText(/search items/i), { target: { value: "rage" } });
    expect(screen.getByText("Rage")).toBeInTheDocument();
    expect(screen.queryByText("Aegis")).not.toBeInTheDocument();
  });

  it("shows the item detail when openItem is set", () => {
    render(<ItemsShop items={items} openItem={"Rage"} />);
    expect(screen.getByText("Crit up.")).toBeInTheDocument();   // passive in the detail panel
  });
});
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/components/ItemsShop.test.tsx`

- [ ] **Step 3: Implement `viewer/src/components/ItemsShop.tsx`**
```tsx
import { useMemo, useState } from "react";
import type { Item } from "../types";
import { filterItems, sortItems, efficiencyLabel, EFFICIENCY, type SortKey, type ItemFilter } from "../lib/itemFilters";
import { iconSlug } from "../lib/builds";
import { toHash, navigate } from "../lib/useHashRoute";

function ItemIcon({ name, size = "h-8 w-8" }: { name: string; size?: string }) {
  return (
    <img src={`/icons/${iconSlug(name)}.png`} alt="" className={`${size} flex-none rounded bg-bg2`}
      onError={(e) => { const i = e.currentTarget; if (i.dataset.r) { i.style.visibility = "hidden"; return; } i.dataset.r = "1"; i.src = `/icons/${iconSlug(name)}.png?r=1`; }} />
  );
}

function EffBadge({ tier }: { tier: string | null | undefined }) {
  const e = efficiencyLabel(tier);
  return <span className={`rounded px-1.5 py-0.5 text-[10px] ${e.cls}`}>{e.text}</span>;
}

function ItemDetail({ item, byName }: { item: Item; byName: Map<string, Item> }) {
  const links = (names: string[]) =>
    names.filter((n) => byName.has(n)).map((n) => (
      <button key={n} type="button" onClick={() => navigate(toHash.item(n))}
        className="inline-flex items-center gap-1 rounded bg-bg2 px-1.5 py-0.5 text-xs text-blue hover:bg-line">
        <ItemIcon name={n} size="h-4 w-4" />{n}
      </button>
    ));
  return (
    <div className="mb-4 rounded-lg border border-line bg-bg1 p-4">
      <div className="mb-2 flex items-center gap-3">
        <ItemIcon name={item.name} size="h-10 w-10" />
        <div>
          <div className="font-display text-lg font-semibold text-ink">{item.name}</div>
          <div className="font-mono text-xs text-muted">{item.cost}g · T{item.tier}</div>
        </div>
        <div className="ml-auto"><EffBadge tier={item.efficiency_tier} /></div>
      </div>
      {Object.entries(item.stats || {}).map(([k, v]) => (
        <div key={k} className="flex justify-between text-sm text-muted"><span>{k}</span><span className="font-mono text-ink">{v}</span></div>
      ))}
      {item.passive && <div className="mt-2 text-sm text-muted">{item.passive}</div>}
      {(item.effect_tags?.length ?? 0) > 0 && (
        <div className="mt-2 flex flex-wrap gap-1">{item.effect_tags!.map((t) => <span key={t} className="rounded bg-line px-1.5 py-0.5 text-[10px] text-blue">{t}</span>)}</div>
      )}
      {item.builds_from?.length ? <div className="mt-3 text-xs text-muted">Builds from: <span className="ml-1 inline-flex flex-wrap gap-1">{links(item.builds_from)}</span></div> : null}
      {item.builds_into?.length ? <div className="mt-2 text-xs text-muted">Builds into: <span className="ml-1 inline-flex flex-wrap gap-1">{links(item.builds_into)}</span></div> : null}
    </div>
  );
}

export function ItemsShop({ items, openItem }: { items: Item[]; openItem?: string }) {
  const [filter, setFilter] = useState<ItemFilter>({});
  const [sort, setSort] = useState<SortKey>("name");
  const byName = useMemo(() => new Map(items.map((i) => [i.name, i])), [items]);
  const tags = useMemo(() => Array.from(new Set(items.flatMap((i) => i.effect_tags ?? []))).sort(), [items]);
  const stats = useMemo(() => Array.from(new Set(items.flatMap((i) => Object.keys(i.stats ?? {})))).sort(), [items]);
  const shown = useMemo(() => sortItems(filterItems(items, filter), sort), [items, filter, sort]);
  const open = openItem ? byName.get(openItem) : undefined;

  const set = (patch: Partial<ItemFilter>) => setFilter((f) => ({ ...f, ...patch }));
  const selCls = "rounded border border-line bg-bg2 px-2 py-1 text-xs text-ink";

  return (
    <div className="p-4">
      {open && <ItemDetail item={open} byName={byName} />}
      <div className="mb-3 flex flex-wrap items-center gap-2">
        <input placeholder="Search items…" value={filter.q ?? ""} onChange={(e) => set({ q: e.target.value })} className={selCls} />
        <select value={filter.tier ?? ""} onChange={(e) => set({ tier: e.target.value ? Number(e.target.value) : undefined })} className={selCls}>
          <option value="">All tiers</option><option value="3">Tier 3</option><option value="2">Tier 2</option><option value="1">Tier 1</option>
        </select>
        <select value={filter.efficiency ?? ""} onChange={(e) => set({ efficiency: e.target.value || undefined })} className={selCls}>
          <option value="">All ratings</option>{EFFICIENCY.map((e) => <option key={e.key} value={e.key}>{e.text}</option>)}
        </select>
        <select value={filter.tag ?? ""} onChange={(e) => set({ tag: e.target.value || undefined })} className={selCls}>
          <option value="">All tags</option>{tags.map((t) => <option key={t} value={t}>{t}</option>)}
        </select>
        <select value={filter.stat ?? ""} onChange={(e) => set({ stat: e.target.value || undefined })} className={selCls}>
          <option value="">Any stat</option>{stats.map((s) => <option key={s} value={s}>{s}</option>)}
        </select>
        <select value={sort} onChange={(e) => setSort(e.target.value as SortKey)} className={selCls}>
          <option value="name">Name</option><option value="cost-asc">Cost ↑</option><option value="cost-desc">Cost ↓</option><option value="efficiency">Rating</option>
        </select>
        <span className="text-xs text-muted">{shown.length} items</span>
      </div>
      <div className="grid grid-cols-[repeat(auto-fill,minmax(180px,1fr))] gap-2">
        {shown.map((it) => (
          <button key={it.name} type="button" onClick={() => navigate(toHash.item(it.name))}
            className="flex flex-col gap-1 rounded-lg border border-line bg-bg1 p-2 text-left hover:border-blue">
            <div className="flex items-center gap-2">
              <ItemIcon name={it.name} />
              <div className="min-w-0">
                <div className="truncate text-sm text-ink">{it.name}</div>
                <div className="font-mono text-[10px] text-muted">{it.cost}g · T{it.tier}</div>
              </div>
            </div>
            <div className="flex items-center justify-between"><EffBadge tier={it.efficiency_tier} />
              {(it.effect_tags?.length ?? 0) > 0 && <span className="truncate text-[10px] text-blue">{it.effect_tags!.join(" · ")}</span>}
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
```

- [ ] **Step 4: Run, confirm PASS**

Run: `cd viewer && npx vitest run src/components/ItemsShop.test.tsx`

- [ ] **Step 5: Commit**
```bash
git add viewer/src/components/ItemsShop.tsx viewer/src/components/ItemsShop.test.tsx
git commit -m "feat(viewer): items shop (filter/sort grid + item detail)"
```

---

## PHASE D — god info tab

### Task D1: `GodInfo` component

**Files:** Create `viewer/src/components/GodInfo.tsx`; Test `viewer/src/components/GodInfo.test.tsx`

- [ ] **Step 1: Failing test** (`GodInfo.test.tsx`):
```tsx
import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { GodInfo } from "./GodInfo";
import type { God } from "../types";

const god = {
  type: "god", name: "Chiron", pantheon: "Greek", role: "Carry", specializations: [],
  damage_type: "physical", release_date: "2024", source_url: "", last_verified: "",
  base_stats: { health: { base: 569, per_level: 86 }, mana: { base: 322, per_level: 48 } },
  abilities: [
    { slot: "1st Ability", name: "Training Exercise", cooldown: [14], cost: [60],
      description: "Fires a volley.", details: ["Cooldown: 14", "Damage: 90"] },
  ],
  aspects: [{ name: "Aspect of the Heroic Tutor", kit_changes: "Copies damage." }],
} as unknown as God;

describe("GodInfo", () => {
  it("renders base stats, abilities, and the aspect", () => {
    render(<GodInfo god={god} />);
    expect(screen.getByText(/health/i)).toBeInTheDocument();
    expect(screen.getByText("569")).toBeInTheDocument();        // base health
    expect(screen.getByText("Training Exercise")).toBeInTheDocument();
    expect(screen.getByText("Fires a volley.")).toBeInTheDocument();
    expect(screen.getByText(/Damage: 90/)).toBeInTheDocument();
    expect(screen.getByText(/Copies damage/)).toBeInTheDocument();
  });
});
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/components/GodInfo.test.tsx`

- [ ] **Step 3: Implement `viewer/src/components/GodInfo.tsx`**
```tsx
import type { God } from "../types";

const STAT_LABELS: Record<string, string> = {
  health: "Health", mana: "Mana", physical_prot: "Physical Prot.",
  magical_prot: "Magical Prot.", attack_speed: "Attack Speed", move_speed: "Move Speed",
};

export function GodInfo({ god }: { god: God }) {
  const stats = Object.entries(god.base_stats ?? {});
  return (
    <div className="max-w-2xl">
      <div className="mb-4 text-xs text-muted">
        {[god.pantheon, god.role, god.damage_type, god.release_date].filter(Boolean).join(" · ")}
      </div>

      {stats.length > 0 && (
        <div className="mb-5">
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">BASE STATS</div>
          <div className="grid grid-cols-[auto_1fr_1fr] gap-x-4 gap-y-1 text-sm">
            <div className="text-[10px] uppercase text-muted">Stat</div>
            <div className="text-[10px] uppercase text-muted">Base</div>
            <div className="text-[10px] uppercase text-muted">/ level</div>
            {stats.map(([k, v]) => (
              <div key={k} className="contents">
                <div className="text-muted">{STAT_LABELS[k] ?? k}</div>
                <div className="font-mono text-ink">{v.base}</div>
                <div className="font-mono text-muted">+{v.per_level}</div>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="mb-5">
        <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">ABILITIES</div>
        <div className="flex flex-col gap-3">
          {(god.abilities ?? []).map((a, i) => (
            <div key={`${a.name}-${i}`} className="rounded border border-line bg-bg1 p-2">
              <div className="flex items-baseline gap-2">
                <span className="text-[10px] uppercase text-muted">{a.slot}</span>
                <span className="font-display text-sm font-semibold text-ink">{a.name}</span>
              </div>
              {a.description && <div className="mt-1 text-sm text-muted">{a.description}</div>}
              {a.details?.length ? (
                <div className="mt-1 flex flex-wrap gap-x-3 text-xs text-muted">
                  {a.details.map((d, j) => <span key={j} className="font-mono">{d}</span>)}
                </div>
              ) : null}
            </div>
          ))}
        </div>
      </div>

      {god.aspects?.[0] && (
        <div>
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">ASPECT</div>
          <div className="rounded border border-gold/40 bg-bg1 p-2 text-sm">
            <span className="font-display font-semibold text-gold">{god.aspects[0].name}</span>
            <span className="text-muted"> — {god.aspects[0].kit_changes}</span>
          </div>
        </div>
      )}
    </div>
  );
}
```
(The `Ability` type must include `description?: string; details?: string[]` — add them in Step 4.)

- [ ] **Step 4: Add `description`/`details` to the `Ability` type** in `viewer/src/types.ts`:
```typescript
export interface Ability {
  slot: string;
  name: string;
  cooldown?: number[];
  cost?: number[];
  description?: string;
  details?: string[];
}
```

- [ ] **Step 5: Run, confirm PASS**

Run: `cd viewer && npx vitest run src/components/GodInfo.test.tsx`

- [ ] **Step 6: Commit**
```bash
git add viewer/src/components/GodInfo.tsx viewer/src/components/GodInfo.test.tsx viewer/src/types.ts
git commit -m "feat(viewer): god Info view (base stats + abilities + aspect)"
```

---

## PHASE E — first-run legend

### Task E1: `Legend` overlay

**Files:** Create `viewer/src/components/Legend.tsx`; Test `viewer/src/components/Legend.test.tsx`

- [ ] **Step 1: Failing test** (`Legend.test.tsx`):
```tsx
import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { Legend } from "./Legend";

describe("Legend", () => {
  it("renders content and calls onClose when dismissed", () => {
    const onClose = vi.fn();
    render(<Legend onClose={onClose} />);
    expect(screen.getByText(/how this works/i)).toBeInTheDocument();
    expect(screen.getByText(/suggested/i)).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /got it|close/i }));
    expect(onClose).toHaveBeenCalled();
  });
});
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/components/Legend.test.tsx`

- [ ] **Step 3: Implement `viewer/src/components/Legend.tsx`**
```tsx
export function Legend({ onClose }: { onClose: () => void }) {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" onClick={onClose}>
      <div className="max-h-[85vh] max-w-lg overflow-y-auto rounded-lg border border-line bg-bg1 p-5" onClick={(e) => e.stopPropagation()}>
        <h2 className="mb-3 font-display text-xl font-bold text-ink">How this works</h2>
        <ul className="flex flex-col gap-2 text-sm text-muted">
          <li><b className="text-ink">Pick a god</b> from the left rail to see builds; switch <b className="text-ink">Builds / Items</b> in the top nav.</li>
          <li><b className="text-ink">Suggested</b> tabs are our scoring engine's picks (a heuristic). <b className="text-ink">Community</b> is SmiteBrain's high-elo meta. <b className="text-ink">Your</b> saved builds are the named tabs.</li>
          <li><b className="text-ink">Flavors</b> (crit / burst / bruiser / anti-tank) re-weight the build; the <b className="text-ink">Aspect</b> toggle swaps to that god's aspect build; the <b className="text-ink">Conquest / Joust</b> toggle changes mode.</li>
          <li><b className="text-ink">BUILD ORDER</b> is a recommended buy order; <b className="text-ink">flex</b> slots are the ones situational swaps replace.</li>
          <li>The <b className="text-ink">Items</b> shop rates every item <b className="text-under">Underrated</b> / <b>Fair</b> / <b className="text-premium">Overrated</b> by gold efficiency, with filters.</li>
          <li>Your builds save in <b className="text-ink">your browser</b> (nothing is uploaded). Scores are heuristics — a fan project, not official.</li>
        </ul>
        <button type="button" onClick={onClose} className="mt-4 rounded bg-gold px-4 py-1.5 text-sm font-medium text-bg0">Got it</button>
      </div>
    </div>
  );
}
```

- [ ] **Step 4: Run, confirm PASS**

Run: `cd viewer && npx vitest run src/components/Legend.test.tsx`

- [ ] **Step 5: Commit**
```bash
git add viewer/src/components/Legend.tsx viewer/src/components/Legend.test.tsx
git commit -m "feat(viewer): first-run legend overlay"
```

---

## PHASE F — wire App + verify

### Task F1: App nav + routing wiring

**Files:** Modify `viewer/src/App.tsx`; Test `viewer/src/App.test.tsx`

- [ ] **Step 1: Failing test** (`App.test.tsx` — create; jsdom hash navigation):
```tsx
import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import App from "./App";

// Minimal index.json fetch stub
const data = {
  gods: [{ name: "Chiron", pantheon: "Greek", role: "Carry", damage_type: "physical",
           base_stats: { health: { base: 569, per_level: 86 } }, abilities: [], aspects: [] }],
  items: [{ name: "Rage", tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: "undervalued" }],
  builds: [], starters: [],
};

beforeEach(() => {
  window.location.hash = "";
  localStorage.clear();
  localStorage.setItem("smite:legend-seen", "1"); // suppress first-run legend in most tests
  vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ json: () => Promise.resolve(data) }));
});

describe("App routing", () => {
  it("navigates to the items shop via the nav", async () => {
    render(<App />);
    await screen.findByRole("button", { name: /items/i });
    fireEvent.click(screen.getByRole("button", { name: /^items$/i }));
    await waitFor(() => expect(screen.getByPlaceholderText(/search items/i)).toBeInTheDocument());
  });

  it("shows the legend on first run", async () => {
    localStorage.removeItem("smite:legend-seen");
    render(<App />);
    await waitFor(() => expect(screen.getByText(/how this works/i)).toBeInTheDocument());
  });
});
```
(Adjust the stub shape if `useIndexData` expects specific fields.)

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/App.test.tsx`

- [ ] **Step 3: Rewrite `viewer/src/App.tsx`** to add the nav + route-driven views. Keep the dev-only manage controls and localStorage/mine behavior. New App:
```tsx
import { useEffect, useState } from "react";
import { useIndexData } from "./hooks/useIndexData";
import { GodRail } from "./components/GodRail";
import { DetailPanel } from "./components/DetailPanel";
import { ManageGods } from "./components/ManageGods";
import { Footer } from "./components/Footer";
import { ItemsShop } from "./components/ItemsShop";
import { GodInfo } from "./components/GodInfo";
import { Legend } from "./components/Legend";
import { useHashRoute, toHash, navigate } from "./lib/useHashRoute";

function App() {
  const { data, error, reload } = useIndexData();
  const route = useHashRoute();
  const [mode, setMode] = useState("Conquest");
  const [legendOpen, setLegendOpen] = useState(false);
  const isDev = import.meta.env.DEV;

  useEffect(() => {
    if (!localStorage.getItem("smite:legend-seen")) setLegendOpen(true);
  }, []);
  const closeLegend = () => { localStorage.setItem("smite:legend-seen", "1"); setLegendOpen(false); };

  const removeGod = async (name: string) => {
    await fetch("/api/gods", { method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "remove", name }) }).then((r) => r.json()).catch(() => ({ ok: false }));
    if (name === route.god) navigate(toHash.home());
    reload();
  };

  if (error) return <div className="flex h-screen items-center justify-center bg-neutral-900 text-red-400">{error} — <button onClick={reload} className="ml-2 underline">retry</button></div>;
  if (!data) return <div className="flex h-screen items-center justify-center bg-neutral-900 text-muted">Loading…</div>;

  const god = route.god ? data.gods.find((g) => g.name === route.god) : undefined;
  const navBtn = (active: boolean) => `rounded px-3 py-1 text-sm font-display font-semibold ${active ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"}`;

  return (
    <div className="flex h-screen flex-col bg-bg0 text-ink">
      <div className="flex items-center gap-2 border-b border-line px-3 py-2">
        <span className="mr-2 font-display text-sm font-bold text-gold">SMITE 2 Builds</span>
        <button type="button" onClick={() => navigate(route.god ? toHash.god(route.god) : toHash.home())} className={navBtn(route.view === "builds")}>Builds</button>
        <button type="button" onClick={() => navigate(toHash.items())} className={navBtn(route.view === "items")}>Items</button>
        <button type="button" onClick={reload} className="ml-auto rounded bg-bg2 px-3 py-1 text-sm hover:bg-line">Reload</button>
        <button type="button" onClick={() => setLegendOpen(true)} aria-label="Help" className="rounded bg-bg2 px-3 py-1 text-sm hover:bg-line">?</button>
      </div>

      <div className="flex flex-1 overflow-hidden">
        {route.view === "items" ? (
          <div className="flex-1 overflow-y-auto"><ItemsShop items={data.items} openItem={route.item} /></div>
        ) : (
          <>
            <div className="flex flex-col overflow-y-auto">
              <GodRail gods={data.gods} selectedGod={route.god ?? null} onSelect={(n) => navigate(toHash.god(n))} onRemove={isDev ? removeGod : undefined} />
              {isDev && <ManageGods onChanged={reload} />}
            </div>
            <div className="flex-1 overflow-y-auto p-4">
              {god ? (
                <>
                  <div className="mb-3 flex w-fit overflow-hidden rounded-md border border-line">
                    <button type="button" onClick={() => navigate(toHash.god(god.name))} className={`px-3 py-1 font-display text-xs font-semibold ${route.tab === "builds" ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"}`}>Builds</button>
                    <button type="button" onClick={() => navigate(toHash.godInfo(god.name))} className={`px-3 py-1 font-display text-xs font-semibold ${route.tab === "info" ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"}`}>Info</button>
                  </div>
                  {route.tab === "info"
                    ? <GodInfo god={god} />
                    : <DetailPanel god={god.name} godData={god} items={data.items} builds={data.builds} mode={mode} onModeChange={setMode} starters={data.starters ?? []} />}
                </>
              ) : <p className="text-muted">Select a god from the rail.</p>}
            </div>
          </>
        )}
      </div>
      <Footer />
      {legendOpen && <Legend onClose={closeLegend} />}
    </div>
  );
}

export default App;
```

- [ ] **Step 4: Run tests + build, confirm PASS**

Run: `cd viewer && npx vitest run && npm run build`
Fix any fallout (e.g. an existing App-less test). `npm run build` is the real typecheck — it must pass.

- [ ] **Step 5: Commit**
```bash
git add viewer/src/App.tsx viewer/src/App.test.tsx
git commit -m "feat(viewer): top nav + hash routing (builds/items/god-info/legend)"
```

---

### Task F2: Re-scrape abilities, regenerate, end-to-end verify

**Files:** generated — god notes, `index.json`

- [ ] **Step 1: Re-scrape + regenerate**

From `tools/`: `python -m smite.refresh --all` (re-scrapes the 10 gods with the richer ability parser — Cloudflare-gated, a few minutes), then `python -m smite.build_index`.
Verify abilities got descriptions:
```bash
cd .. && python -c "
import json; d=json.load(open('viewer/public/index.json',encoding='utf-8'))
g=next(x for x in d['gods'] if x['name']=='Chiron')
for a in g['abilities']:
    print(a['slot'], '|', a['name'], '| desc:', (a.get('description') or '')[:60], '| details:', len(a.get('details') or []))
"
```
Expected: real abilities carry a non-empty `description` and some `details`. If descriptions are garbage (parser subtraction left noise), refine `_parse_abilities` (prefer a description `<td>`/`<p>` cell) and re-run — this is the point of the live check.

- [ ] **Step 2: Both suites green**

Run: `cd tools && python -m pytest smite/tests/ -q -m "not live"` and `cd ../viewer && npx vitest run`.

- [ ] **Step 3: End-to-end browser verification** (dev server, `npx vite --port 5178 --strictPort` from `viewer/`):
  (a) **Legend** shows on first load (clear `smite:legend-seen`); dismiss; reopen via **?**.
  (b) **Items** nav → shop renders cards with efficiency badges; filter by tier/rating/tag/stat + search narrow the grid; sort works.
  (c) click an item → **item detail** with stats/passive/tags and `builds from/into` links that navigate; URL shows `#/items/<name>`.
  (d) pick a god → **Builds** tab (existing view) and **Info** tab → base stats table + abilities (with descriptions from the re-scrape) + aspect; URL `#/god/<name>/info`.
  (e) deep-link: paste `#/items/Deathbringer` and `#/god/Chiron/info` into the URL → correct view loads.
  Screenshot the shop + a god Info tab. Fix issues, re-verify.

- [ ] **Step 4: Static-build check** — `npm run build && npx vite preview --port 5179`. Confirm routing + shop + god info + legend all work in the production build, and dev-only manage controls are absent.

- [ ] **Step 5: Commit generated data**
```bash
git add "04. System/Data/SMITE/Gods/" "03. Workspaces/Gaming/SMITE 2/Builds/" "04. System/Data/SMITE/Analysis/" viewer/public/index.json
git commit -m "chore(smite): regenerate with richer ability data"
```

---

## Self-Review

**Spec coverage:** A richer abilities (A1 parser + F2 re-scrape), B hash routing (B1 lib + F1 nav), C items shop (C1 helpers + C2 shop/detail), D god Info tab (D1 + F1 tab wiring), E legend (E1 + F1 first-run wiring). Efficiency labels (undervalued→Underrated, fair→Fair, premium→Overrated, null→—) in C1. Deep links for items + god info in B1/F1. All spec sections mapped.

**Placeholder scan:** none — full code per step. F2's parser-refinement note is a live-verification instruction (the subtraction-based description is a reasonable first cut that the real re-scrape validates), not a placeholder.

**Type/name consistency:** `Route {view,god?,tab,item?}` (B1) consumed by App (F1). `toHash`/`navigate` (B1) used by ItemsShop (C2), App (F1). `ItemFilter`/`SortKey`/`efficiencyLabel`/`EFFICIENCY` (C1) used by ItemsShop (C2). `Ability.description/details` (D1 step 4 type) produced by the parser (A1) and rendered by GodInfo (D1). `GodInfo`/`ItemsShop`/`Legend` imported in App (F1). ItemsShop props `{items, openItem}`; GodInfo props `{god}`; Legend props `{onClose}` — all match call sites. No dangling names.

**Safety:** no destructive ops; re-scrape is the same Cloudflare-gated refresh used to build the pool; regenerated data is deterministic; localStorage/mine and dev-gating unchanged; `_archive/` untouched. Real typecheck via `npm run build` is in F1/F2.
