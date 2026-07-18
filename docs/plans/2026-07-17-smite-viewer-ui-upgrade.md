# SMITE 2 Viewer UI Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the second-monitor build viewer with the Arena Night visual system, scoreboard headshots, hover tooltips, a live situational-swap build preview, a community-build dedup fix, and a one-click launcher.

**Architecture:** Pipeline enablers (Python: dedup parser, headshot fetch, structured `swap_item`, richer item payload) put the right data/assets into `index.json`, then a viewer redesign (React 19 + TS + Tailwind v4) consumes them. A `run.bat` + Obsidian note provide one-click launch.

**Tech Stack:** Python 3.10 (bs4, pytest), Vite + React 19 + TypeScript + Tailwind v4 + Vitest + RTL. Fonts via Google Fonts (Rajdhani, Inter, JetBrains Mono).

**Reference spec:** [2026-07-17-smite-viewer-ui-upgrade-design.md](../specs/2026-07-17-smite-viewer-ui-upgrade-design.md)

---

## File Structure

**Pipeline (modify):**
- `tools/smite/smitebrain_parser.py` — dedup Core slots via next-best substitution.
- `tools/smite/build_index.py` — fold `effect_tags` + `efficiency_tier` into each index item.
- `tools/smite/assemble.py` — add `swap_item` to each situational-swap entry.
- `tools/smite/wiki_parser.py` — add `derive_headshot_url`.
- `tools/smite/refresh.py` — download the headshot asset in `refresh_god`.

**Viewer (modify/create):**
- `viewer/src/index.css` — Arena Night tokens + font imports (modify).
- `viewer/src/types.ts` — `swap_item`, item `effect_tags`/`efficiency_tier` (modify).
- `viewer/src/lib/builds.ts` — `applySwap` preview helper (modify).
- `viewer/src/components/Tooltip.tsx` — reusable hover/focus tooltip (create).
- `viewer/src/components/GodRail.tsx` — headshots + god tooltip (modify).
- `viewer/src/components/DetailPanel.tsx` — header, slot styling, item tooltip, live swap diff (modify).
- `viewer/src/App.tsx` — pass god/item data down; shell restyle (modify).

**Launcher (create/modify):**
- `run.bat` (create), `03. Workspaces/Gaming/SMITE 2/Open Build Viewer.md` (create), `.claude/launch.json` (fix path).

---

## PHASE P — Pipeline enablers

### Task P1: Dedup community Core builds

**Files:**
- Modify: `tools/smite/smitebrain_parser.py`
- Test: `tools/smite/tests/test_smitebrain_parser.py`

`_parse_core_recommended_build` takes only the top pick per slot, so an item that wins two slots appears twice (Chiron → Titan's Bane ×2). Collect each slot's ranked alternatives, then pick the first not-yet-used item per slot.

- [ ] **Step 1: Write the failing test** (append to the test file)

```python
def test_core_build_dedups_via_next_best_alternative():
    # Slot 1 and slot 2 both top-pick Titan's Bane; slot 2 must fall to its
    # next-best alternative so the build has no duplicate item.
    html = """
    <h2>Core</h2>
    <div class="font-semibold">1</div>
    <div>
      <div class="flex"><img alt="Titan's Bane"><div class="text-xs">40% pick 58% win</div></div>
      <div class="flex"><img alt="Deathbringer"><div class="text-xs">30% pick 55% win</div></div>
    </div>
    <div class="font-semibold">2</div>
    <div>
      <div class="flex"><img alt="Titan's Bane"><div class="text-xs">27% pick 52% win</div></div>
      <div class="flex"><img alt="The Crusher"><div class="text-xs">26% pick 67% win</div></div>
    </div>
    """
    from smite import smitebrain_parser
    result = smitebrain_parser.parse_build_page(html)
    names = [e["name"] for e in result["items"]]
    assert names == ["Titan's Bane", "The Crusher"]   # no duplicate
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_smitebrain_parser.py -k dedup -v`
Expected: FAIL — current code returns `["Titan's Bane", "Titan's Bane"]`.

- [ ] **Step 3: Replace `_parse_core_recommended_build`**

```python
def _parse_core_recommended_build(soup) -> list:
    heading = soup.find("h2", string=re.compile(r"^\s*Core\s*$"))
    if heading is None:
        return []

    # First pass: collect each numbered slot's alternatives in rank order.
    slot_alternatives = {}
    for el in heading.find_all_next():
        if el.name == "h2":
            break
        if el.name != "div":
            continue
        if "font-semibold" not in (el.get("class") or []):
            continue
        text = el.get_text(strip=True)
        if not text.isdigit():
            continue
        tile_list = el.find_next_sibling("div")
        if tile_list is None:
            continue
        entries = []
        for tile in tile_list.find_all("div", class_="flex"):
            entry = _tile_entry(tile)
            if entry is not None:
                entries.append(entry)
        if entries:
            slot_alternatives[int(text)] = entries

    # Second pass: per slot in order, take the first item not already chosen.
    # If every alternative in a slot is already used, drop the slot (a rare,
    # correct fallback — a real build never lists the same item twice).
    chosen, used = [], set()
    for n in sorted(slot_alternatives):
        for entry in slot_alternatives[n]:
            if entry["name"] not in used:
                chosen.append(entry)
                used.add(entry["name"])
                break
    return chosen
```

Note: `_tile_entry` already requires both an `img[alt]` and a `div.text-xs` in the container, so inner icon-wrapper `div.flex` nodes (which lack the stat div) return `None` and are filtered — the ranked `entries` list ends up in document (rank) order with one entry per real tile.

- [ ] **Step 4: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_smitebrain_parser.py -v`
Expected: PASS (all existing + new).

- [ ] **Step 5: Commit**

```bash
git add tools/smite/smitebrain_parser.py tools/smite/tests/test_smitebrain_parser.py
git commit -m "fix(smite): dedup community Core builds via next-best alternative"
```

---

### Task P2: Fold effect-tags + efficiency tier into index items

**Files:**
- Modify: `tools/smite/build_index.py`
- Test: `tools/smite/tests/test_build_index.py`

Tooltips need to show *why* an item is good. Enrich each index item with `effect_tags` (from `_tags.yaml`) and `efficiency_tier` (from the regression). Extract a pure `_enrich_items` for testability.

- [ ] **Step 1: Write the failing test** (append)

```python
def test_enrich_items_adds_tags_and_tier():
    from smite import build_index
    items = [
        {"name": "Deathbringer", "cost": 2900, "stats": {"Strength": "45"}},
        {"name": "Cheapo", "cost": 900, "stats": {"Strength": "45"}},
    ]
    tags = {"Deathbringer": ["burst"], "Cheapo": []}
    enriched = build_index._enrich_items(items, tags)
    by = {it["name"]: it for it in enriched}
    assert by["Deathbringer"]["effect_tags"] == ["burst"]
    assert by["Cheapo"]["effect_tags"] == []
    # tier is one of the efficiency labels (computed from the item set)
    assert by["Cheapo"]["efficiency_tier"] in {"undervalued", "fair", "premium"}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_build_index.py -k enrich -v`
Expected: FAIL (no attribute `_enrich_items`).

- [ ] **Step 3: Implement**

Add imports at the top of `build_index.py`:
```python
from smite import efficiency, notes, scoring
```
(the module already imports `notes`; add `efficiency, scoring`).

Add the pure helper and call it in `build_index`:
```python
def _enrich_items(items, tags):
    """Attach god-agnostic effect_tags + efficiency_tier to each item so the
    viewer's tooltips can explain an item without recomputing anything."""
    eff, _ = efficiency.efficiency_scores(items)
    for it in items:
        it["effect_tags"] = tags.get(it["name"], [])
        it["efficiency_tier"] = eff.get(it["name"], {}).get("tier")
    return items
```

In `build_index(vault_root)`, after building the item list, enrich it:
```python
def build_index(vault_root: Path) -> dict:
    data_root = vault_root / "04. System" / "Data" / "SMITE"
    gods_dir = data_root / "Gods"
    items_dir = data_root / "Items"
    builds_dir = vault_root / "03. Workspaces" / "Gaming" / "SMITE 2" / "Builds"

    def _all(dir_path: Path) -> list:
        if not dir_path.exists():
            return []
        return [notes.read_note(p)[0] for p in sorted(dir_path.glob("*.md"))]

    items = _enrich_items(_all(items_dir), scoring.load_tags(data_root / "_tags.yaml"))
    return {"gods": _all(gods_dir), "items": items, "builds": _all(builds_dir)}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_build_index.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add tools/smite/build_index.py tools/smite/tests/test_build_index.py
git commit -m "feat(smite): index items carry effect_tags + efficiency_tier"
```

---

### Task P3: Structured `swap_item` on situational swaps

**Files:**
- Modify: `tools/smite/assemble.py`
- Test: `tools/smite/tests/test_assemble.py`

The viewer needs a clean item name to drive the swap diff. Add `swap_item` (name for a real swap, `None` for covered/none rows) alongside the prose `swap`.

- [ ] **Step 1: Write the failing test** (append)

```python
def test_situational_swaps_include_swap_item_name():
    rows = [_row("A", 0.9), _row("Antiheal", 0.5, tags=["anti-heal"])]
    ibn = _items_by_name(
        {"name": "A", "stats": {"Strength": "40"}},
        {"name": "Antiheal", "stats": {"Strength": "30"}},
    )
    table = assemble.situational_swaps(rows, ibn, tags_map={"Antiheal": ["anti-heal"]})
    sustain = next(r for r in table if r["vs_tag"] == "sustain")
    assert sustain["swap_item"] == "Antiheal"
    # a "none available" row carries an explicit null swap_item
    cc = next(r for r in table if r["vs_tag"] == "heavy_cc")
    assert cc["swap_item"] is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_assemble.py -k swap_item -v`
Expected: FAIL (`KeyError: 'swap_item'`).

- [ ] **Step 3: Add `swap_item` in `situational_swaps`**

In the three `table.append(...)` sites of `situational_swaps`, add the field:
```python
        if pick:
            chosen.add(pick)
            table.append({"vs_tag": vs_tag, "swap": f"{pick} — {label}", "swap_item": pick})
            continue
        covered = next((n for n in core
                        if _item_qualifies(n, items_by_name, tags_map, needed_tag, prot_stat)), None)
        if covered:
            table.append({"vs_tag": vs_tag, "swap": f"core already covers {label} ({covered})", "swap_item": None})
        else:
            table.append({"vs_tag": vs_tag, "swap": f"(no {label} available in pool)", "swap_item": None})
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_assemble.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add tools/smite/assemble.py tools/smite/tests/test_assemble.py
git commit -m "feat(smite): situational swaps carry structured swap_item"
```

---

### Task P4: Headshot URL derivation + download

**Files:**
- Modify: `tools/smite/wiki_parser.py`, `tools/smite/refresh.py`
- Test: `tools/smite/tests/test_wiki_parser.py`

The portrait URL looks like `/images/thumb/T_Ullr%28S2%29_Default.png/280px-T_Ullr%28S2%29_Default.png?1914c`. The square scoreboard icon is the same asset with `_Default_Icon.png`. Derive it and download to `<slug>-head.png`.

- [ ] **Step 1: Write the failing test** (append to `test_wiki_parser.py`)

```python
def test_derive_headshot_url_from_portrait_thumb():
    from smite import wiki_parser
    portrait = "/images/thumb/T_Ullr%28S2%29_Default.png/280px-T_Ullr%28S2%29_Default.png?1914c"
    assert wiki_parser.derive_headshot_url(portrait) == "/images/T_Ullr%28S2%29_Default_Icon.png"


def test_derive_headshot_url_handles_missing():
    from smite import wiki_parser
    assert wiki_parser.derive_headshot_url(None) is None
    assert wiki_parser.derive_headshot_url("/images/no_match_here.png") is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_wiki_parser.py -k headshot -v`
Expected: FAIL (no attribute `derive_headshot_url`).

- [ ] **Step 3: Implement derivation** in `wiki_parser.py`

```python
def derive_headshot_url(portrait_url):
    """From a god portrait URL, derive the square scoreboard-icon asset URL
    (the wiki serves it as the same asset name with _Default_Icon.png). Returns
    the full-res (non-thumb) /images path, or None if the portrait URL doesn't
    match the expected _Default.png asset shape."""
    if not portrait_url:
        return None
    m = re.search(r"([^/]+)_Default\.png", portrait_url)
    if not m:
        return None
    return f"/images/{m.group(1)}_Default_Icon.png"
```
(`re` is already imported in `wiki_parser.py`.)

- [ ] **Step 4: Run the derivation test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_wiki_parser.py -v`
Expected: PASS.

- [ ] **Step 5: Wire the download into `refresh_god`**

In `refresh.py` `refresh_god`, after the existing portrait `_download_icon` call, add the headshot download:
```python
    slug = name.lower().replace(" ", "-").replace("'", "")
    _download_icon(parsed.get("image_url"), slug)
    _download_icon(wiki_parser.derive_headshot_url(parsed.get("image_url")), slug + "-head")
```
(Replace the existing single `_download_icon(parsed.get("image_url"), name.lower()...)` line with these three; `_download_icon` already no-ops on a `None`/empty url and try/excepts a bad fetch, so a god without an icon asset simply gets no headshot rather than crashing.)

- [ ] **Step 6: LIVE verify the headshot actually resolves**

Run: `cd tools && python -m smite.refresh --refresh Chiron --kind god && python -m smite.refresh --refresh Ra --kind god`
Then check the files exist and are roughly square (headshots are ~square, portraits are 2:3 tall):
```bash
cd .. && python -c "
import struct
from pathlib import Path
def size(p):
    b=open(p,'rb').read(24); return struct.unpack('>II', b[16:24])
for slug in ['chiron','ra']:
    p=Path('04. System/Data/SMITE/_assets/icons')/f'{slug}-head.png'
    print(slug, p.exists() and size(p))
"
```
Expected: both `-head.png` exist and are near-square (e.g. 128×128 / 256×256), clearly not 280×420. **If a headshot did NOT download** (file missing / still 2:3), the `_Default_Icon` asset name guess is wrong for this wiki — inspect a cached god page for the real square-icon asset name (`grep -o 'T_[A-Za-z]*%28S2%29[^"]*Icon[^"]*\.png'` on a cached HTML file), adjust `derive_headshot_url` accordingly, and re-run. Report what you found rather than shipping a broken derivation.

- [ ] **Step 7: Commit** (code only; the regenerated assets are committed in P5)

```bash
git add tools/smite/wiki_parser.py tools/smite/refresh.py tools/smite/tests/test_wiki_parser.py
git commit -m "feat(smite): fetch square scoreboard headshots for gods"
```

---

### Task P5: Full pipeline regen + commit generated data

**Files:** generated — `Builds/*.md`, `_assets/icons/*-head.png`, `viewer/public/index.json`, `viewer/public/icons/`

- [ ] **Step 1: Regenerate everything from cache**

Run (from `tools/`):
```bash
python -m smite.refresh --all
python -m smite.recommend --all
python -m smite.build_index
```
`refresh --all` re-parses cached HTML (applying the P1 dedup and downloading P4 headshots); `recommend --all` re-emits suggested builds with P3 `swap_item`; `build_index` enriches items (P2) and copies icons (including `-head`).

- [ ] **Step 2: Verify the generated data**

Run: `cd .. && python -c "
import json
d=json.load(open('viewer/public/index.json',encoding='utf-8'))
# dedup: no community slot_order has a duplicate item
for n in d['builds']:
    for b in n['builds']:
        if b['source']=='community':
            names=[s['name'] for s in b['slot_order']]
            assert len(names)==len(set(names)), f'DUP in {n[\"god\"]}: {names}'
# swap_item present on suggested swaps
sug=[b for n in d['builds'] for b in n['builds'] if b['source']=='suggested']
assert all('swap_item' in s for b in sug for s in b['situational_swaps'])
# items enriched
assert all('effect_tags' in it and 'efficiency_tier' in it for it in d['items'])
print('OK: no dupes, swap_item present, items enriched')
"`
Also confirm `ls viewer/public/icons/*-head.png | wc -l` shows 10 headshots.
Expected: prints OK; 10 headshots.

- [ ] **Step 3: Full Python suite green**

Run: `cd tools && python -m pytest smite/tests/ -q -m "not live"`
Expected: all pass.

- [ ] **Step 4: Commit generated output**

```bash
git add "03. Workspaces/Gaming/SMITE 2/Builds/" "04. System/Data/SMITE/_assets/" viewer/public/
git commit -m "chore(smite): regenerate builds, headshots, and index for viewer upgrade"
```

---

## PHASE V — Viewer redesign

### Task V1: Arena Night tokens, fonts, and type updates

**Files:**
- Modify: `viewer/src/index.css`, `viewer/src/types.ts`

- [ ] **Step 1: Replace `viewer/src/index.css`** with the Arena Night theme

```css
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap');
@import "tailwindcss";

@theme {
  --color-bg0: #0b0e13;
  --color-bg1: #0e1116;
  --color-bg2: #12161d;
  --color-line: #1e2530;
  --color-gold: #e3b23c;
  --color-blue: #4ea3ff;
  --color-ink: #e8edf4;
  --color-muted: #8b95a5;
  --color-under: #63c088;
  --color-premium: #c58b8b;
  --font-display: "Rajdhani", sans-serif;
  --font-sans: "Inter", sans-serif;
  --font-mono: "JetBrains Mono", monospace;
}

:root { color-scheme: dark; }
body { background: var(--color-bg0); font-family: var(--font-sans); }
```

This registers Tailwind utilities `bg-bg1`, `text-gold`, `font-display`, `font-mono`, `text-under`, etc. used by later tasks.

- [ ] **Step 2: Verify the dev build compiles**

Run: `cd viewer && npx vite build`
Expected: builds without CSS errors.

- [ ] **Step 3: Update `viewer/src/types.ts`**

Add `swap_item` to `SituationalSwap`, and `effect_tags`/`efficiency_tier` to `Item`:
```typescript
export interface SituationalSwap {
  vs_tag: string;
  swap: string;
  swap_item?: string | null;
}
```
```typescript
export interface Item {
  type: string;
  name: string;
  tier: number;
  cost: number;
  stats: Record<string, string>;
  passive: string;
  builds_from: string[];
  builds_into: string[];
  source_url: string;
  last_verified: string;
  effect_tags?: string[];
  efficiency_tier?: string | null;
}
```

- [ ] **Step 4: Typecheck**

Run: `cd viewer && npx tsc --noEmit`
Expected: passes.

- [ ] **Step 5: Commit**

```bash
git add viewer/src/index.css viewer/src/types.ts
git commit -m "feat(viewer): Arena Night design tokens + swap/item type fields"
```

---

### Task V2: `applySwap` build-preview helper

**Files:**
- Modify: `viewer/src/lib/builds.ts`
- Test: `viewer/src/lib/builds.test.ts`

- [ ] **Step 1: Write the failing test** (append, matching the file's existing import/vitest style)

```typescript
import { applySwap } from "./builds";

describe("applySwap", () => {
  it("replaces the last (lowest-scored) slot and marks the diff", () => {
    const out = applySwap(["A", "B", "C"], "X");
    expect(out).toEqual([
      { name: "A", status: "kept" },
      { name: "B", status: "kept" },
      { name: "C", status: "removed" },
      { name: "X", status: "added" },
    ]);
  });
  it("is a no-op when swapItem is null", () => {
    expect(applySwap(["A", "B"], null)).toEqual([
      { name: "A", status: "kept" },
      { name: "B", status: "kept" },
    ]);
  });
  it("adds to an empty build", () => {
    expect(applySwap([], "X")).toEqual([{ name: "X", status: "added" }]);
  });
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd viewer && npx vitest run src/lib/builds.test.ts`
Expected: FAIL (no export `applySwap`).

- [ ] **Step 3: Implement in `builds.ts`**

```typescript
export type SlotStatus = "kept" | "removed" | "added";
export interface PreviewSlot {
  name: string;
  status: SlotStatus;
}

/** Derive the effective build shown when a matchup is selected: the
 * lowest-scored core slot (the last one — slot_order is score-sorted) is
 * removed and the swap item is added. A null swapItem is a no-op (all kept). */
export function applySwap(slotOrder: string[], swapItem: string | null): PreviewSlot[] {
  const base: PreviewSlot[] = slotOrder.map((name) => ({ name, status: "kept" }));
  if (!swapItem) return base;
  if (base.length === 0) return [{ name: swapItem, status: "added" }];
  base[base.length - 1] = { name: base[base.length - 1].name, status: "removed" };
  base.push({ name: swapItem, status: "added" });
  return base;
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd viewer && npx vitest run src/lib/builds.test.ts`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add viewer/src/lib/builds.ts viewer/src/lib/builds.test.ts
git commit -m "feat(viewer): applySwap build-preview helper"
```

---

### Task V3: Tooltip component

**Files:**
- Create: `viewer/src/components/Tooltip.tsx`, `viewer/src/components/Tooltip.test.tsx`

A reusable hover/focus tooltip with edge-flip and a11y. Content is passed as children; the trigger wraps arbitrary children.

- [ ] **Step 1: Write the failing test** (match the project's existing RTL/vitest render style — check `GodRail.test.tsx` for the import lines and `test-setup`)

```tsx
import { render, screen, fireEvent } from "@testing-library/react";
import { Tooltip } from "./Tooltip";

it("shows tooltip content on focus and hides on blur", () => {
  render(
    <Tooltip content={<span>Cost 2900</span>}>
      <button>Deathbringer</button>
    </Tooltip>,
  );
  const trigger = screen.getByText("Deathbringer");
  fireEvent.focus(trigger);
  expect(screen.getByRole("tooltip")).toHaveTextContent("Cost 2900");
  fireEvent.blur(trigger);
  expect(screen.queryByRole("tooltip")).toBeNull();
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd viewer && npx vitest run src/components/Tooltip.test.tsx`
Expected: FAIL (no module).

- [ ] **Step 3: Implement `Tooltip.tsx`**

```tsx
import { useRef, useState, type ReactNode } from "react";

interface TooltipProps {
  content: ReactNode;
  children: ReactNode;
}

/** Hover/focus tooltip. Opens after a short delay; flips above the trigger and
 * shifts horizontally so it never clips at the viewport edge. Keyboard-
 * accessible (focus/blur) and screen-reader friendly (role="tooltip"). */
export function Tooltip({ content, children }: TooltipProps) {
  const [open, setOpen] = useState(false);
  const [pos, setPos] = useState<{ left: number; top: number }>({ left: 0, top: 0 });
  const timer = useRef<number | undefined>(undefined);
  const wrapRef = useRef<HTMLSpanElement>(null);

  const show = () => {
    timer.current = window.setTimeout(() => {
      const el = wrapRef.current;
      if (!el) return;
      const r = el.getBoundingClientRect();
      const width = 260;
      let left = r.left + r.width / 2 - width / 2;
      left = Math.max(8, Math.min(left, window.innerWidth - width - 8));
      const top = r.top > 220 ? r.top - 8 : r.bottom + 8; // flip above if room
      setPos({ left, top });
      setOpen(true);
    }, 150);
  };
  const hide = () => {
    window.clearTimeout(timer.current);
    setOpen(false);
  };

  return (
    <span
      ref={wrapRef}
      onMouseEnter={show}
      onMouseLeave={hide}
      onFocus={show}
      onBlur={hide}
      onKeyDown={(e) => e.key === "Escape" && hide()}
      className="relative inline-flex"
      tabIndex={0}
    >
      {children}
      {open && (
        <div
          role="tooltip"
          style={{ position: "fixed", left: pos.left, top: pos.top, width: 260 }}
          className={`z-50 rounded-lg border border-line bg-bg2 p-3 text-xs text-ink shadow-xl ${
            pos.top < 220 ? "" : "-translate-y-full"
          }`}
        >
          {content}
        </div>
      )}
    </span>
  );
}
```

Note: `position: fixed` + viewport-relative coords keeps the tooltip out of the app's scroll/overflow containers. The `-translate-y-full` when flipping above anchors the bottom edge to the computed `top`.

- [ ] **Step 4: Run test to verify it passes**

Run: `cd viewer && npx vitest run src/components/Tooltip.test.tsx`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add viewer/src/components/Tooltip.tsx viewer/src/components/Tooltip.test.tsx
git commit -m "feat(viewer): reusable hover/focus Tooltip"
```

---

### Task V4: GodRail headshots + god tooltip

**Files:**
- Modify: `viewer/src/components/GodRail.tsx`
- Test: `viewer/src/components/GodRail.test.tsx`

- [ ] **Step 1: Update the test** (adjust the existing icon-src assertion + add a tooltip check)

Find the existing test that asserts the rail `<img>` `src`. Change the expected src to the `-head` variant, and add:
```tsx
it("uses the headshot icon variant", () => {
  render(<GodRail gods={[chiron]} selectedGod={null} onSelect={() => {}} />);
  const img = screen.getByRole("img", { name: "Chiron" });
  expect(img).toHaveAttribute("src", "/icons/chiron-head.png");
});
```
(Use the file's existing `chiron` fixture; if the old test hard-coded `/icons/chiron.png`, update it to `/icons/chiron-head.png`.)

- [ ] **Step 2: Run test to verify it fails**

Run: `cd viewer && npx vitest run src/components/GodRail.test.tsx`
Expected: FAIL on the src.

- [ ] **Step 3: Update `GodRail.tsx`**

```tsx
import type { God } from "../types";
import { iconSlug } from "../lib/builds";
import { Tooltip } from "./Tooltip";

interface GodRailProps {
  gods: God[];
  selectedGod: string | null;
  onSelect: (godName: string) => void;
}

export function GodRail({ gods, selectedGod, onSelect }: GodRailProps) {
  return (
    <div className="flex w-[72px] flex-col gap-2 overflow-y-auto border-r border-line bg-bg0 p-2">
      {gods.map((god) => (
        <Tooltip
          key={god.name}
          content={
            <div>
              <div className="font-display text-sm font-semibold text-ink">{god.name}</div>
              <div className="text-muted">{god.pantheon} · {god.role} · {god.damage_type}</div>
              <div className="mt-1 text-muted">
                {god.abilities?.map((a) => a.name).filter(Boolean).join(" · ")}
              </div>
            </div>
          }
        >
          <button
            type="button"
            aria-pressed={god.name === selectedGod}
            onClick={() => onSelect(god.name)}
            title={god.name}
            className={`flex h-14 w-14 items-center justify-center overflow-hidden rounded-lg transition-all duration-150 ${
              god.name === selectedGod
                ? "ring-2 ring-gold"
                : "ring-1 ring-line hover:ring-blue"
            }`}
          >
            <img
              src={`/icons/${iconSlug(god.name)}-head.png`}
              alt={god.name}
              className="h-full w-full object-cover"
              onError={(e) => {
                (e.target as HTMLImageElement).style.display = "none";
              }}
            />
          </button>
        </Tooltip>
      ))}
    </div>
  );
}
```

- [ ] **Step 4: Run tests to verify pass**

Run: `cd viewer && npx vitest run src/components/GodRail.test.tsx`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add viewer/src/components/GodRail.tsx viewer/src/components/GodRail.test.tsx
git commit -m "feat(viewer): GodRail headshots + god hover tooltip"
```

---

### Task V5: DetailPanel — header, item tooltips, live swap diff

**Files:**
- Modify: `viewer/src/components/DetailPanel.tsx`, `viewer/src/App.tsx`
- Test: `viewer/src/components/DetailPanel.test.tsx`

DetailPanel now needs god metadata (header/tooltip) and item data (tooltips), so its props expand. It renders the effective (swapped) build via `applySwap`.

- [ ] **Step 1: Update App to pass god + items** (`App.tsx`)

Change the `DetailPanel` usage:
```tsx
{selectedGod ? (
  <DetailPanel
    god={selectedGod}
    godData={data.gods.find((g) => g.name === selectedGod)}
    items={data.items}
    builds={data.builds}
  />
) : (
  <p className="text-muted">Select a god from the rail.</p>
)}
```
Also restyle the App shell surfaces to Arena Night: root `bg-bg0 text-ink`, the reload button `bg-bg2 hover:bg-line`, error text stays red. (Swap the existing `bg-neutral-900`/`text-neutral-*` classes for the tokens.)

- [ ] **Step 2: Write/adjust the failing test** (`DetailPanel.test.tsx`)

Add a test for the swap diff (adapt fixtures to the file's style; DetailPanel now takes `godData` + `items`):
```tsx
it("reflows the build when a matchup chip is clicked", () => {
  const builds = [{
    type: "smite-build", god: "Chiron", mode: "Conquest",
    builds: [{
      source: "suggested", archetype: "core",
      slot_order: ["A", "B", "C"],
      situational_swaps: [{ vs_tag: "heavy_cc", swap: "Cloak — cc", swap_item: "Cloak" }],
      rationale: "x",
    }],
  }];
  render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any} />);
  fireEvent.click(screen.getByRole("button", { name: /heavy cc/i }));
  expect(screen.getByText("Cloak")).toBeInTheDocument();     // added
  expect(screen.getByText("C")).toHaveClass("line-through");  // removed slot struck
});
```
Update existing DetailPanel tests to pass the new `godData`/`items` props (e.g. `godData={undefined} items={[]}`), keeping their assertions.

- [ ] **Step 3: Run test to verify it fails**

Run: `cd viewer && npx vitest run src/components/DetailPanel.test.tsx`
Expected: FAIL (prop/behavior not present).

- [ ] **Step 4: Rewrite `DetailPanel.tsx`**

```tsx
import { useEffect, useMemo, useState } from "react";
import type { BuildEntry, BuildNote, God, Item } from "../types";
import { isCommunityEntry, slotItemName, iconSlug, applySwap } from "../lib/builds";
import { Tooltip } from "./Tooltip";

const VS_LABELS: Record<string, string> = {
  heavy_cc: "vs heavy CC",
  magic_heavy: "vs magic",
  physical_heavy: "vs physical",
  sustain: "vs sustain",
};

interface DetailPanelProps {
  god: string;
  godData?: God;
  items: Item[];
  builds: BuildNote[];
}

function ItemTooltipBody({ item, name }: { item?: Item; name: string }) {
  if (!item) return <span className="font-display font-semibold">{name}</span>;
  return (
    <div>
      <div className="mb-1 flex items-baseline justify-between">
        <span className="font-display text-sm font-semibold text-ink">{item.name}</span>
        <span className="font-mono text-muted">{item.cost}g · T{item.tier}</span>
      </div>
      {Object.entries(item.stats || {}).map(([k, v]) => (
        <div key={k} className="flex justify-between text-muted">
          <span>{k}</span><span className="font-mono text-ink">{v}</span>
        </div>
      ))}
      {item.passive && <div className="mt-1 text-muted">{item.passive}</div>}
      {(item.effect_tags?.length || item.efficiency_tier) && (
        <div className="mt-2 flex flex-wrap gap-1">
          {item.efficiency_tier && (
            <span className={`rounded px-1.5 py-0.5 text-[10px] ${
              item.efficiency_tier === "undervalued" ? "bg-under/20 text-under"
              : item.efficiency_tier === "premium" ? "bg-premium/20 text-premium"
              : "bg-line text-muted"}`}>{item.efficiency_tier}</span>
          )}
          {item.effect_tags?.map((t) => (
            <span key={t} className="rounded bg-line px-1.5 py-0.5 text-[10px] text-blue">{t}</span>
          ))}
        </div>
      )}
    </div>
  );
}

export function DetailPanel({ god, godData, items, builds }: DetailPanelProps) {
  const note = builds.find((b) => b.god === god);
  const [activeIndex, setActiveIndex] = useState(0);
  const [selectedTag, setSelectedTag] = useState<string | null>(null);
  const itemsByName = useMemo(() => {
    const m = new Map<string, Item>();
    for (const it of items) m.set(it.name, it);
    return m;
  }, [items]);

  // Reset on god OR data-identity change (reload). See prior notes.
  useEffect(() => {
    setActiveIndex(0);
    setSelectedTag(null);
  }, [god, note]);

  if (!note || note.builds.length === 0) {
    return <p className="text-muted">No build data yet for {god}.</p>;
  }

  const entries = note.builds;
  const active: BuildEntry = entries[activeIndex] ?? entries[0];
  const community = isCommunityEntry(active);
  const swaps = !community ? active.situational_swaps : undefined;

  const selectedSwap = swaps?.find((s) => s.vs_tag === selectedTag) ?? null;
  const baseNames = active.slot_order.map(slotItemName);
  const preview = applySwap(baseNames, selectedSwap?.swap_item ?? null);

  return (
    <div>
      <div className="mb-4 flex items-center gap-3">
        <img
          src={`/icons/${iconSlug(god)}-head.png`}
          alt={god}
          className="h-12 w-12 rounded-lg object-cover ring-1 ring-line"
          onError={(e) => ((e.target as HTMLImageElement).style.display = "none")}
        />
        <div>
          <h2 className="font-display text-2xl font-bold leading-none text-ink">{god}</h2>
          <div className="text-xs text-muted">
            {godData ? `${godData.pantheon} · ${godData.role} · ${godData.damage_type}` : note.mode}
          </div>
        </div>
        <span className="ml-auto rounded bg-bg2 px-2 py-0.5 text-xs text-muted">{note.mode}</span>
      </div>

      <div role="tablist" className="mb-4 flex gap-1">
        {entries.map((entry, i) => (
          <button
            key={i}
            type="button"
            role="tab"
            aria-selected={i === activeIndex}
            onClick={() => setActiveIndex(i)}
            className={`rounded px-3 py-1 text-xs font-medium capitalize transition-colors duration-150 ${
              i === activeIndex ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"
            }`}
          >
            {entry.source}
          </button>
        ))}
      </div>

      <div className="flex gap-6">
        <div className="min-w-[220px]">
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">SLOT ORDER</div>
          <div className="flex flex-col gap-1.5">
            {preview.map((slot, i) => {
              const item = itemsByName.get(slot.name);
              const rates = !community ? null
                : (active.slot_order[i] as { pick_rate: number; win_rate: number } | undefined);
              return (
                <Tooltip key={`${slot.name}-${i}`} content={<ItemTooltipBody item={item} name={slot.name} />}>
                  <div className={`flex items-center gap-2 rounded px-1 py-0.5 transition-colors duration-150 ${
                    slot.status === "added" ? "bg-blue/10" : ""}`}>
                    <img
                      src={`/icons/${iconSlug(slot.name)}.png`}
                      alt=""
                      className={`h-7 w-7 flex-none rounded bg-bg2 ${slot.status === "removed" ? "opacity-30" : ""}`}
                      onError={(e) => ((e.target as HTMLImageElement).style.visibility = "hidden")}
                    />
                    <span className={`text-sm ${
                      slot.status === "removed" ? "text-muted line-through"
                      : slot.status === "added" ? "font-medium text-blue" : "text-ink"}`}>
                      {slot.name}
                    </span>
                    {slot.status === "added" && <span className="text-[10px] text-muted">swap in</span>}
                    {rates && (
                      <span className="ml-auto font-mono text-xs text-muted">
                        {Math.round(rates.pick_rate * 100)}% / {Math.round(rates.win_rate * 100)}%
                      </span>
                    )}
                  </div>
                </Tooltip>
              );
            })}
          </div>
        </div>

        {swaps && swaps.length > 0 && (
          <div className="flex-1 border-l border-line pl-6">
            <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">SITUATIONAL</div>
            <div className="flex flex-col gap-1.5">
              {swaps.map((swap) => {
                const clickable = !!swap.swap_item;
                const selected = swap.vs_tag === selectedTag;
                return (
                  <button
                    key={swap.vs_tag}
                    type="button"
                    disabled={!clickable}
                    onClick={() => clickable && setSelectedTag(selected ? null : swap.vs_tag)}
                    className={`rounded px-2 py-1 text-left text-xs transition-colors duration-150 ${
                      selected ? "bg-gold text-bg0"
                      : clickable ? "bg-bg2 text-ink hover:bg-line"
                      : "bg-bg1 text-muted"}`}
                  >
                    <span className="font-medium">{VS_LABELS[swap.vs_tag] ?? swap.vs_tag}</span>
                    {" — "}{swap.swap_item ?? swap.swap.replace(/^.*—\s*/, "").replace(/[()]/g, "")}
                  </button>
                );
              })}
            </div>
          </div>
        )}
      </div>

      {!community && active.rationale && (
        <p className="mt-4 text-xs italic text-muted">{active.rationale}</p>
      )}
    </div>
  );
}
```

- [ ] **Step 5: Run tests to verify pass**

Run: `cd viewer && npx vitest run src/components/DetailPanel.test.tsx`
Expected: PASS.

- [ ] **Step 6: Typecheck + commit**

Run: `cd viewer && npx tsc --noEmit` (expected: passes)
```bash
git add viewer/src/components/DetailPanel.tsx viewer/src/App.tsx viewer/src/components/DetailPanel.test.tsx
git commit -m "feat(viewer): detail header, item tooltips, live swap diff"
```

---

### Task V6: Full suite + manual browser verification

**Files:** none (verification), possible small style fixes

- [ ] **Step 1: Full viewer + Python suites**

Run: `cd viewer && npx vitest run` (all pass) and `cd ../tools && python -m pytest smite/tests/ -q -m "not live"` (all pass).

- [ ] **Step 2: Launch and verify in the browser**

Start the dev server and drive it with the browser preview tool: verify (a) headshots render in the rail and detail header, (b) hovering an item shows the tooltip with stats/passive/tier/tags, positioned without clipping at the window edge, (c) hovering a god in the rail shows its tooltip, (d) clicking a matchup chip reflows the build with the struck-out slot + gold "swap in" item, clicking again resets, (e) the Arena Night palette/fonts are applied. Fix any visual issues in the component styles and re-verify. Capture a screenshot as proof.

- [ ] **Step 3: Commit any fixes**

```bash
git add viewer/src
git commit -m "polish(viewer): browser-verification fixes"
```
(Skip if no fixes were needed.)

---

## PHASE L — Launcher

### Task L1: run.bat + Obsidian launcher note + fix launch.json

**Files:**
- Create: `run.bat`, `03. Workspaces/Gaming/SMITE 2/Open Build Viewer.md`
- Modify: `.claude/launch.json`

- [ ] **Step 1: Create `run.bat`** at the vault root

```bat
@echo off
cd /d "%~dp0viewer"
if not exist node_modules (
  echo Installing dependencies (first run only)...
  call npm install
)
call npm run dev -- --open
```

- [ ] **Step 2: Create the Obsidian launcher note** `03. Workspaces/Gaming/SMITE 2/Open Build Viewer.md`

```markdown
# Open Build Viewer

[▶ Launch the SMITE build viewer](file:///C:/Users/jacob/Desktop/obsidian-vault/run.bat)

First launch installs dependencies (~30s), then your browser opens to the
viewer automatically. Leave the terminal window open while you use it; close
it (or Ctrl+C) when you're done. After a data refresh, click **Reload data**
in the app — no restart needed.
```

- [ ] **Step 3: Fix `.claude/launch.json`** — repoint the stale worktree path

Change the `smite-viewer-dev` config's `runtimeArgs` from `["--prefix", ".claude/worktrees/smite-viewer/viewer", "run", "dev", ...]` to point at the real viewer, and align the port with Vite's default open flow:
```json
{
  "name": "smite-viewer-dev",
  "runtimeExecutable": "npm",
  "runtimeArgs": ["--prefix", "viewer", "run", "dev"],
  "port": 5173
}
```

- [ ] **Step 4: Verify the launcher works**

Double-check `run.bat` starts the server and opens the browser (run it once manually, confirm the app loads, then stop the server). Confirm the Obsidian note renders the link.

- [ ] **Step 5: Commit**

```bash
git add run.bat "03. Workspaces/Gaming/SMITE 2/Open Build Viewer.md" .claude/launch.json
git commit -m "feat(smite): one-click run.bat launcher + Obsidian note"
```

---

## Self-Review

**Spec coverage:** headshots (P4 fetch, V4 rail, V5 header), tooltips (V3 component, V4 god, V5 item), Arena Night polish (V1 tokens, applied V4–V6), live swaps (P3 swap_item, V2 applySwap, V5 diff), dedup bug (P1), launcher (L1). Richer item payload for tooltips (P2). Every spec section maps to a task.

**Placeholder scan:** none — every code step has complete code; the one risk area (P4 headshot asset name) has an explicit live-verify-and-adapt step rather than an assumption.

**Type/name consistency:** `applySwap(slotOrder: string[], swapItem: string|null): PreviewSlot[]` defined in V2, consumed in V5. `swap_item` added in P3 (Python), typed in V1 (`SituationalSwap.swap_item`), read in V5. Item `effect_tags`/`efficiency_tier` added in P2 (Python), typed in V1, read in V5's `ItemTooltipBody`. `derive_headshot_url` defined P4, used in `refresh_god`. `-head` slug suffix consistent across P4 (write), V4 (rail), V5 (header). Tailwind tokens (`bg-bg1`, `text-gold`, `text-under`, `font-display`, `font-mono`) defined in V1 `@theme`, used V4–V5. Tooltip props (`content`, `children`) consistent V3→V4/V5.

**Sequencing:** pipeline (P1–P5) lands real data first so viewer tasks verify against it; V1 (tokens+types) precedes all viewer tasks that use the tokens/types; V2/V3 (pure helper + component) precede V4/V5 that consume them.
