# Manage gods + share-ready Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Move "my" builds to browser localStorage (so the app is fully static/hostable), add an owner-only in-app add/remove-gods flow, and make the site deploy-ready.

**Architecture:** Viewer — a `mineStore` (localStorage) is the sole home for mine builds; DetailPanel merges them and BuildEditor writes to them (no backend). Python — a `manage_gods` CLI (add = scrape+regen, remove = move to `_removed/`) behind a dev-only `/api/gods` Vite endpoint that replaces `/api/build`. A `Manage gods` UI is gated to `import.meta.env.DEV`.

**Tech Stack:** Vite + React 19 + TS + Vitest + RTL; Python 3.10 (pytest).

**Reference spec:** [2026-07-19-smite-manage-gods-share-ready-design.md](../specs/2026-07-19-smite-manage-gods-share-ready-design.md)

---

## File Structure
- `viewer/src/lib/mineStore.ts` — localStorage CRUD for mine builds (create).
- `viewer/src/components/BuildEditor.tsx` — save/delete via mineStore, drop fetch (modify).
- `viewer/src/components/DetailPanel.tsx` — merge mineStore builds; bump on save (modify).
- `viewer/src/components/GodRail.tsx` — dev-only Add/Remove controls (modify).
- `viewer/src/components/ManageGods.tsx` — add-god input + busy state (create).
- `viewer/vite.config.ts` — `/api/gods` middleware replaces `/api/build` (modify).
- `viewer/src/App.tsx` — wire ManageGods (dev) + reload (modify).
- `viewer/src/components/Footer.tsx` — attribution footer (create).
- `tools/smite/manage_gods.py` — add/remove CLI (create).
- `viewer/DEPLOY.md` — hosting doc (create).

---

## PHASE A — mine builds in localStorage

### Task A1: `mineStore`

**Files:** Create `viewer/src/lib/mineStore.ts`; Test `viewer/src/lib/mineStore.test.ts`

- [ ] **Step 1: Write failing tests** (`mineStore.test.ts`):
```typescript
import { describe, it, expect, beforeEach } from "vitest";
import { getMine, saveMine, deleteMine } from "./mineStore";

beforeEach(() => localStorage.clear());

describe("mineStore", () => {
  it("saves, reads back, and replaces by name within a god+mode", () => {
    saveMine("Chiron", "Conquest", { name: "Crit", slot_order: ["Deathbringer"] });
    expect(getMine("Chiron", "Conquest")).toEqual([{ name: "Crit", slot_order: ["Deathbringer"] }]);
    saveMine("Chiron", "Conquest", { name: "Crit", slot_order: ["Rage"] }); // replace
    expect(getMine("Chiron", "Conquest")).toEqual([{ name: "Crit", slot_order: ["Rage"] }]);
    saveMine("Chiron", "Conquest", { name: "Other", slot_order: ["X"] });
    expect(getMine("Chiron", "Conquest").map((b) => b.name)).toEqual(["Crit", "Other"]);
  });
  it("scopes builds by god and mode", () => {
    saveMine("Chiron", "Conquest", { name: "A", slot_order: [] });
    expect(getMine("Chiron", "Joust")).toEqual([]);
    expect(getMine("Ra", "Conquest")).toEqual([]);
  });
  it("deletes by name", () => {
    saveMine("Ra", "Conquest", { name: "A", slot_order: [] });
    saveMine("Ra", "Conquest", { name: "B", slot_order: [] });
    deleteMine("Ra", "Conquest", "A");
    expect(getMine("Ra", "Conquest").map((b) => b.name)).toEqual(["B"]);
  });
  it("returns [] on empty / malformed storage", () => {
    expect(getMine("Nobody", "Conquest")).toEqual([]);
    localStorage.setItem("smite:mine-builds", "not json");
    expect(getMine("Chiron", "Conquest")).toEqual([]);
  });
});
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/lib/mineStore.test.ts`

- [ ] **Step 3: Implement `viewer/src/lib/mineStore.ts`**
```typescript
export interface MineBuild {
  name: string;
  slot_order: string[];
  starter?: { base: string; upgrade: string };
  notes?: string;
}

const KEY = "smite:mine-builds";
const scope = (god: string, mode: string) => `${god}||${mode}`;

type Store = Record<string, MineBuild[]>;

function read(): Store {
  try {
    const raw = localStorage.getItem(KEY);
    const parsed = raw ? JSON.parse(raw) : {};
    return parsed && typeof parsed === "object" ? (parsed as Store) : {};
  } catch {
    return {};
  }
}

function write(store: Store): void {
  localStorage.setItem(KEY, JSON.stringify(store));
}

export function getMine(god: string, mode: string): MineBuild[] {
  return read()[scope(god, mode)] ?? [];
}

export function saveMine(god: string, mode: string, build: MineBuild): void {
  const store = read();
  const k = scope(god, mode);
  const kept = (store[k] ?? []).filter((b) => b.name !== build.name);
  store[k] = [...kept, build];
  write(store);
}

export function deleteMine(god: string, mode: string, name: string): void {
  const store = read();
  const k = scope(god, mode);
  store[k] = (store[k] ?? []).filter((b) => b.name !== name);
  write(store);
}
```

- [ ] **Step 4: Run, confirm PASS**

Run: `cd viewer && npx vitest run src/lib/mineStore.test.ts`

- [ ] **Step 5: Commit**
```bash
git add viewer/src/lib/mineStore.ts viewer/src/lib/mineStore.test.ts
git commit -m "feat(viewer): localStorage mineStore for personal builds"
```

---

### Task A2: BuildEditor + DetailPanel use the store

**Files:** Modify `viewer/src/components/BuildEditor.tsx`, `viewer/src/components/DetailPanel.tsx`; Test both test files

- [ ] **Step 1: Update BuildEditor test** — replace the fetch-mock assertions with store assertions. In `BuildEditor.test.tsx`, replace the three existing tests' bodies to use the store (import `getMine` from `../lib/mineStore`, `beforeEach(() => localStorage.clear())`). New tests:
```tsx
import { getMine } from "../lib/mineStore";
// ...inside describe, add: beforeEach(() => localStorage.clear());

it("saves a build to the store and calls onSaved with its name", async () => {
  const onSaved = vi.fn(); const onClose = vi.fn();
  render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                      onClose={onClose} onSaved={onSaved} />);
  fireEvent.change(screen.getByPlaceholderText(/build name/i), { target: { value: "My Build" } });
  fireEvent.change(screen.getByPlaceholderText(/search items/i), { target: { value: "Death" } });
  fireEvent.click(screen.getByText("Deathbringer"));
  fireEvent.click(screen.getByRole("button", { name: /^save$/i }));
  expect(onSaved).toHaveBeenCalledWith("My Build");
  expect(getMine("Chiron", "Conquest")).toEqual([{ name: "My Build", slot_order: ["Deathbringer"] }]);
});

it("blocks saving with no name", () => {
  render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                      onClose={() => {}} onSaved={() => {}} />);
  fireEvent.click(screen.getByRole("button", { name: /^save$/i }));
  expect(screen.getByText(/name required/i)).toBeInTheDocument();
  expect(getMine("Chiron", "Conquest")).toEqual([]);
});

it("deletes from the store", () => {
  const onSaved = vi.fn();
  render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                      initial={{ name: "Old", slot_order: ["Rage"] }} onClose={() => {}} onSaved={onSaved} />);
  fireEvent.click(screen.getByRole("button", { name: /^delete$/i }));
  expect(onSaved).toHaveBeenCalled();
  expect(getMine("Chiron", "Conquest")).toEqual([]);
});
```
(Keep the item-icon test as-is; remove the `vi.stubGlobal("fetch", …)` usage.)

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/components/BuildEditor.test.tsx`

- [ ] **Step 3: Implement BuildEditor** — replace the `post`/`save`/delete wiring so it writes to the store instead of fetching. Add import `import { saveMine, deleteMine } from "../lib/mineStore";`. Replace the `post` function and `save` handler with:
```tsx
  const save = () => {
    if (!name.trim()) return setError("Name required");
    if (slots.length === 0) return setError("Add at least one item");
    saveMine(god, mode, {
      name: name.trim(),
      slot_order: slots,
      ...(starterIdx >= 0 ? { starter: starters[starterIdx] } : {}),
      ...(notes.trim() ? { notes: notes.trim() } : {}),
    });
    onSaved(name.trim());
    onClose();
  };

  const remove = () => {
    if (initial) deleteMine(god, mode, initial.name);
    onSaved("");
    onClose();
  };
```
  Remove the `busy`/`error`-from-fetch async state usage in the buttons: the Save button `onClick={save}`, the Delete button (rendered when `initial`) `onClick={remove}`, and drop the `disabled={busy}` (or keep a no-op). Keep the `error` state for the name/slots validation. Delete any now-unused `useState` for `busy` and the `fetch` code.

- [ ] **Step 4: Update DetailPanel to merge store builds.** In `DetailPanel.test.tsx`, add a test (import `saveMine` from `../lib/mineStore`, `beforeEach(() => localStorage.clear())` at the top of the describe):
```tsx
  it("shows a localStorage mine build as a tab", () => {
    saveMine("Chiron", "Conquest", { name: "My Local", slot_order: ["Deathbringer"] });
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "" },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    expect(screen.getByRole("tab", { name: /My Local/i })).toBeInTheDocument();
  });
```

- [ ] **Step 5: Implement DetailPanel merge.** Add import `import { getMine } from "../lib/mineStore";`. Add a `mineVersion` state (`const [mineVersion, setMineVersion] = useState(0);`). After `note` is resolved (and before computing `entries`), build the mine entries from the store and merge:
```tsx
  const mineEntries = useMemo(
    () => getMine(god, note?.mode ?? mode).map((b) => ({ source: "mine" as const, ...b })),
    [god, note?.mode, mode, mineVersion],
  );
```
  Then change the `entries` computation to append mine entries and drop any stale `source:"mine"` from `note.builds` (there won't be any, but be defensive):
```tsx
  const entries = [
    ...note.builds.filter((b) => {
      if (b.source === "mine") return false;
      if (b.source !== "suggested") return true;
      const a = (b as { aspect?: string }).aspect;
      return aspectOn ? !!a : !a;
    }),
    ...mineEntries,
  ];
```
  Wire the editor's `onSaved` to bump the store version + select:
```tsx
        onSaved={(name) => { if (name) setPendingSelect(name); setMineVersion((v) => v + 1); }}
```
  (Remove the `onReload?.()` call from the editor's onSaved — mine builds no longer round-trip through the index. `onReload` stays as a prop for the manage-gods flow in Task B3.) The "Edit this build" button already builds a `MineDraft` from `active`; that still works since mine entries carry `name`/`slot_order`/`starter`/`notes`.

- [ ] **Step 6: Run, confirm PASS** + typecheck

Run: `cd viewer && npx vitest run && npx tsc --noEmit`

- [ ] **Step 7: Commit**
```bash
git add viewer/src/components/BuildEditor.tsx viewer/src/components/BuildEditor.test.tsx viewer/src/components/DetailPanel.tsx viewer/src/components/DetailPanel.test.tsx
git commit -m "feat(viewer): mine builds via localStorage (no backend, hostable)"
```

---

## PHASE B — owner add/remove gods (dev only)

### Task B1: `manage_gods` CLI

**Files:** Create `tools/smite/manage_gods.py`; Test `tools/smite/tests/test_manage_gods.py`

- [ ] **Step 1: Write failing test** (`test_manage_gods.py`) — covers `remove` (which is pure file-move + rebuild; `add` scrapes live and is manual-verified):
```python
import json
from pathlib import Path
from smite import manage_gods, notes


def _setup(tmp_path, monkeypatch):
    data = tmp_path / "data"; (data / "Gods").mkdir(parents=True)
    builds = tmp_path / "builds"; builds.mkdir()
    notes.write_note(data / "Gods" / "Chiron.md", {"name": "Chiron"}, "")
    notes.write_note(builds / "Chiron-Conquest.md", {"god": "Chiron"}, "")
    notes.write_note(builds / "Chiron-Joust.md", {"god": "Chiron"}, "")
    monkeypatch.setattr(manage_gods, "GODS_ROOT", data / "Gods")
    monkeypatch.setattr(manage_gods, "BUILDS_ROOT", builds)
    monkeypatch.setattr(manage_gods, "_reindex", lambda: None)  # skip the real rebuild
    return data, builds


def test_remove_moves_god_and_builds(tmp_path, monkeypatch):
    data, builds = _setup(tmp_path, monkeypatch)
    rc = manage_gods.remove("Chiron")
    assert rc == 0
    assert not (data / "Gods" / "Chiron.md").exists()
    assert (data / "Gods" / "_removed" / "Chiron.md").exists()
    assert (builds / "_removed" / "Chiron-Conquest.md").exists()
    assert (builds / "_removed" / "Chiron-Joust.md").exists()


def test_remove_unknown_god_fails(tmp_path, monkeypatch):
    _setup(tmp_path, monkeypatch)
    assert manage_gods.remove("Nobody") == 1
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_manage_gods.py -v`

- [ ] **Step 3: Implement `tools/smite/manage_gods.py`**
```python
"""Add or remove a god from the tracked pool. Invoked by the viewer's dev-only
/api/gods endpoint (owner operation — add scrapes the wiki via Playwright).

Usage: python -m smite.manage_gods add "<God Name>"
       python -m smite.manage_gods remove "<God Name>"
"""
import json
import shutil
import sys
from pathlib import Path

from smite import recommend, build_index
from smite.refresh import (DATA_ROOT, refresh_god, refresh_god_builds,
                           BrowserFetcher)
from smite.cache import CachedFetcher

GODS_ROOT = DATA_ROOT / "Gods"
BUILDS_ROOT = recommend.BUILDS_ROOT


def _reindex():
    recommend.main(["--all"])
    build_index.write_index(build_index.VAULT_ROOT if hasattr(build_index, "VAULT_ROOT")
                            else DATA_ROOT.parents[2],
                            DATA_ROOT.parents[2] / "viewer" / "public" / "index.json")


def _fail(msg):
    print(json.dumps({"ok": False, "error": msg}))
    return 1


def add(name):
    name = (name or "").strip()
    if not name:
        return _fail("name required")
    try:
        wiki = BrowserFetcher(DATA_ROOT / "_cache" / "wiki")
        refresh_god(name, wiki)
        community = CachedFetcher(DATA_ROOT / "_cache" / "smitebrain")
        refresh_god_builds(name, "Conquest", community)
    except Exception as exc:  # scrape failure -> no partial pool entry
        return _fail(f"scrape failed for {name!r}: {exc}")
    _reindex()
    print(json.dumps({"ok": True}))
    return 0


def remove(name):
    name = (name or "").strip()
    god_note = GODS_ROOT / f"{name}.md"
    if not god_note.exists():
        return _fail(f"not a tracked god: {name!r}")
    (GODS_ROOT / "_removed").mkdir(exist_ok=True)
    shutil.move(str(god_note), str(GODS_ROOT / "_removed" / f"{name}.md"))
    removed_builds = BUILDS_ROOT / "_removed"
    removed_builds.mkdir(exist_ok=True)
    for p in BUILDS_ROOT.glob(f"{name}-*.md"):
        shutil.move(str(p), str(removed_builds / p.name))
    _reindex()
    print(json.dumps({"ok": True}))
    return 0


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) < 2 or argv[0] not in ("add", "remove"):
        return _fail("usage: manage_gods add|remove <name>")
    return add(argv[1]) if argv[0] == "add" else remove(argv[1])


if __name__ == "__main__":
    sys.exit(main())
```
  NOTE during implementation: verify the real symbols — `recommend.BUILDS_ROOT`, `build_index.write_index(vault_root, out_path)` signature, and that `BrowserFetcher`/`CachedFetcher` import paths match (adjust imports to the actual module names, e.g. `from smite.browser_fetch import BrowserFetcher`). Fix `_reindex`'s vault-root derivation to whatever `build_index`'s `__main__` uses (read it). The tests monkeypatch `_reindex`, `GODS_ROOT`, `BUILDS_ROOT`, so unit tests don't touch the real rebuild.

- [ ] **Step 4: Run, confirm PASS** + full suite

Run: `cd tools && python -m pytest smite/tests/test_manage_gods.py -v` then `cd tools && python -m pytest smite/tests/ -q -m "not live"`

- [ ] **Step 5: Commit**
```bash
git add tools/smite/manage_gods.py tools/smite/tests/test_manage_gods.py
git commit -m "feat(smite): manage_gods add/remove CLI"
```

---

### Task B2: `/api/gods` endpoint (replaces `/api/build`)

**Files:** Modify `viewer/vite.config.ts`

- [ ] **Step 1: Replace the middleware** — in `vite.config.ts`, rename/repoint the endpoint from `/api/build` (`smite.save_build`) to `/api/gods` (`smite.manage_gods`). The body is `{action:"add"|"remove", name}`; pass it as **argv** (fixed `["-m","smite.manage_gods", action, name]`) rather than stdin. Replace the `saveBuildApi` plugin with:
```typescript
function manageGodsApi(): Plugin {
  const toolsDir = fileURLToPath(new URL("../tools", import.meta.url));
  return {
    name: "manage-gods-api",
    configureServer(server) {
      server.middlewares.use("/api/gods", (req, res) => {
        if (req.method !== "POST") { res.statusCode = 405; res.end(); return; }
        let body = "";
        req.on("data", (c) => (body += c));
        req.on("end", () => {
          let payload: { action?: string; name?: string } = {};
          try { payload = JSON.parse(body); } catch { /* empty */ }
          const action = payload.action === "add" || payload.action === "remove" ? payload.action : null;
          const name = typeof payload.name === "string" ? payload.name : "";
          if (!action || !name) { res.statusCode = 400; res.end(JSON.stringify({ ok: false, error: "bad request" })); return; }
          const p = spawn("python", ["-m", "smite.manage_gods", action, name], { cwd: toolsDir });
          let err = "";
          p.stderr.on("data", (d) => (err += d));
          p.on("close", (code) => {
            res.setHeader("Content-Type", "application/json");
            if (code === 0) res.end(JSON.stringify({ ok: true }));
            else { res.statusCode = 500; res.end(JSON.stringify({ ok: false, error: err || `exit ${code}` })); }
          });
        });
      });
    },
  };
}
```
  Update the `plugins` array to use `manageGodsApi()` instead of `saveBuildApi()`. Keep the existing `server.watch.ignored` block (add-god still rewrites `public/`). Keep the `spawn`/`fileURLToPath` imports.

- [ ] **Step 2: Verify config builds**

Run: `cd viewer && npx vite build` (expected: succeeds; endpoint only affects the dev server).

- [ ] **Step 3: Commit**
```bash
git add viewer/vite.config.ts
git commit -m "feat(viewer): /api/gods dev endpoint (replaces /api/build)"
```

---

### Task B3: Manage-gods UI (dev-gated) + App wiring

**Files:** Create `viewer/src/components/ManageGods.tsx`; Modify `viewer/src/components/GodRail.tsx`, `viewer/src/App.tsx`; Test `viewer/src/components/ManageGods.test.tsx`

- [ ] **Step 1: Failing test** (`ManageGods.test.tsx`):
```tsx
import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { ManageGods } from "./ManageGods";

describe("ManageGods", () => {
  it("posts an add request and calls onChanged on success", async () => {
    const fetchMock = vi.fn().mockResolvedValue({ json: () => Promise.resolve({ ok: true }) });
    vi.stubGlobal("fetch", fetchMock);
    const onChanged = vi.fn();
    render(<ManageGods onChanged={onChanged} />);
    fireEvent.change(screen.getByPlaceholderText(/add a god/i), { target: { value: "Thor" } });
    fireEvent.click(screen.getByRole("button", { name: /add/i }));
    await waitFor(() => expect(onChanged).toHaveBeenCalled());
    const [url, opts] = fetchMock.mock.calls[0];
    expect(url).toBe("/api/gods");
    expect(JSON.parse(opts.body)).toEqual({ action: "add", name: "Thor" });
    vi.unstubAllGlobals();
  });

  it("surfaces an error and does not call onChanged on failure", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ json: () => Promise.resolve({ ok: false, error: "scrape failed" }) }));
    const onChanged = vi.fn();
    render(<ManageGods onChanged={onChanged} />);
    fireEvent.change(screen.getByPlaceholderText(/add a god/i), { target: { value: "Xyz" } });
    fireEvent.click(screen.getByRole("button", { name: /add/i }));
    await waitFor(() => expect(screen.getByText(/scrape failed/i)).toBeInTheDocument());
    expect(onChanged).not.toHaveBeenCalled();
    vi.unstubAllGlobals();
  });
});
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/components/ManageGods.test.tsx`

- [ ] **Step 3: Implement `viewer/src/components/ManageGods.tsx`**
```tsx
import { useState } from "react";

export function ManageGods({ onChanged }: { onChanged: () => void }) {
  const [name, setName] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const add = async () => {
    const n = name.trim();
    if (!n) return;
    setBusy(true); setError(null);
    const res = await fetch("/api/gods", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "add", name: n }),
    }).then((r) => r.json()).catch((e) => ({ ok: false, error: String(e) }));
    setBusy(false);
    if (res.ok) { setName(""); onChanged(); } else setError(res.error || "Add failed");
  };

  return (
    <div className="border-t border-line p-2">
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && add()}
        placeholder="Add a god…"
        disabled={busy}
        className="w-full rounded border border-line bg-bg2 px-2 py-1 text-xs text-ink"
      />
      <button
        type="button"
        onClick={add}
        disabled={busy}
        className="mt-1 w-full rounded bg-bg2 px-2 py-1 text-xs text-blue hover:bg-line disabled:opacity-50"
      >
        {busy ? "Scraping…" : "+ Add"}
      </button>
      {error && <div className="mt-1 text-[10px] text-red-400">{error}</div>}
    </div>
  );
}
```

- [ ] **Step 4: Add a dev-only remove control to `GodRail.tsx`.** Extend `GodRailProps` with `onRemove?: (god: string) => void;`. When `onRemove` is provided, render a tiny "×" button overlaid on each god tile (stops propagation, confirms):
```tsx
        {onRemove && (
          <button
            type="button"
            onClick={(e) => { e.stopPropagation(); if (confirm(`Remove ${god.name} from the pool?`)) onRemove(god.name); }}
            title={`Remove ${god.name}`}
            className="absolute right-0 top-0 rounded-bl bg-bg0/80 px-1 text-[10px] text-red-400 hover:text-red-300"
          >
            ×
          </button>
        )}
```
  Wrap the god `<button>` + this control in a `relative` container so the overlay positions. (Put the existing tile button and the remove button inside `<div className="relative">…</div>` under the `Tooltip`.)

- [ ] **Step 5: Wire `App.tsx`** — only in dev, pass `onRemove` to GodRail and render `ManageGods`; both call a `manageGod` handler that POSTs remove (for onRemove) and, on any change, calls `reload()`:
```tsx
  const isDev = import.meta.env.DEV;
  const removeGod = async (name: string) => {
    await fetch("/api/gods", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "remove", name }),
    }).then((r) => r.json()).catch(() => ({ ok: false }));
    reload();
  };
```
  Pass `onRemove={isDev ? removeGod : undefined}` to `<GodRail>` and render `{isDev && <ManageGods onChanged={reload} />}` beneath the rail (inside the rail column, or just after `<GodRail>`).

- [ ] **Step 6: Run, confirm PASS** + full suite + typecheck

Run: `cd viewer && npx vitest run && npx tsc --noEmit`
(Existing GodRail/App tests: `onRemove` is optional so they still pass; if an App test asserts DOM, `isDev` is true under vitest so ManageGods renders — adjust any snapshot/count if needed.)

- [ ] **Step 7: Commit**
```bash
git add viewer/src/components/ManageGods.tsx viewer/src/components/ManageGods.test.tsx viewer/src/components/GodRail.tsx viewer/src/App.tsx
git commit -m "feat(viewer): dev-only add/remove-gods UI"
```

---

## PHASE C — hosting readiness

### Task C1: Attribution footer + DEPLOY.md

**Files:** Create `viewer/src/components/Footer.tsx`, `viewer/DEPLOY.md`; Modify `viewer/src/App.tsx`

- [ ] **Step 1: Create `viewer/src/components/Footer.tsx`**
```tsx
export function Footer() {
  return (
    <div className="border-t border-line px-4 py-2 text-[10px] text-muted">
      Build data derived from{" "}
      <a href="https://wiki.smite2.com" className="text-blue hover:underline" target="_blank" rel="noreferrer">wiki.smite2.com</a>
      {" "}and{" "}
      <a href="https://smitebrain.com" className="text-blue hover:underline" target="_blank" rel="noreferrer">SmiteBrain</a>.
      Suggested builds are heuristic — not official. A fan project, not affiliated with Hi-Rez.
    </div>
  );
}
```

- [ ] **Step 2: Render it in `App.tsx`** — wrap the main content column so the footer sits at the bottom. Import `Footer` and add `<Footer />` at the end of the main content area (below the DetailPanel region), e.g. change the right-hand `<div className="flex-1 p-4">…</div>` to a column that ends with `<Footer />`. Keep existing layout otherwise.

- [ ] **Step 3: Create `viewer/DEPLOY.md`**
```markdown
# Deploying the SMITE 2 build viewer

The viewer is a static site — no server needed for friends. Personal ("my")
builds live in each visitor's browser (localStorage). God management (add/remove)
is owner-only and works only in local dev (`npm run dev`), not in the hosted build.

## Host it (recommended: Vercel or Cloudflare Pages)
1. Push this repo to GitHub.
2. New project → import the repo. Set:
   - Root directory: `viewer`
   - Build command: `npm run build`
   - Output directory: `dist`
3. Deploy. You get a URL to share. Pushing to the repo auto-redeploys.

## One-off (no account)
`cd viewer && npm run build`, then drag the `viewer/dist/` folder onto
https://app.netlify.com/drop .

## Updating data on a patch
From `tools/`:
```
python -m smite.refresh --all      # re-scrape gods/items/builds
python -m smite.recommend --all    # recompute suggested builds
python -m smite.build_index        # rewrite viewer/public/index.json
```
Commit + push → the host redeploys. Friends see the new data on reload.
```

- [ ] **Step 4: Typecheck + build**

Run: `cd viewer && npx tsc --noEmit && npx vite build`

- [ ] **Step 5: Commit**
```bash
git add viewer/src/components/Footer.tsx viewer/src/App.tsx viewer/DEPLOY.md
git commit -m "feat(viewer): attribution footer + deploy doc"
```

---

### Task C2: End-to-end verification

**Files:** none (verification)

- [ ] **Step 1: Both suites green**

Run: `cd viewer && npx vitest run` and `cd ../tools && python -m pytest smite/tests/ -q -m "not live"`.

- [ ] **Step 2: Dev browser check** — start the dev server (`npx vite --port 5178 --strictPort` from `viewer/`). Verify:
  (a) **mine build persists** — create a build on a god, reload the page (F5), confirm the tab is still there (localStorage);
  (b) **add god** — type a real god not in the pool (e.g. "Thor") in the Add-a-god box, submit; after the scrape (~30–90s) confirm it appears in the rail with builds;
  (c) **remove god** — click a god's × , confirm; it drops from the rail and its notes are under `Gods/_removed/` + `Builds/_removed/` (verify via a file read);
  (d) confirm no console errors.

- [ ] **Step 3: Static-build check** — `cd viewer && npm run build && npx vite preview --port 5179`. In the preview (production build): confirm the **Add-a-god box and × controls are absent** (dev-gated), a mine build still saves + persists across reload, and the footer shows. This proves the hosted experience.

- [ ] **Step 4: Commit any generated data** (if a god was added/removed during (b)/(c) and you want to keep the pool change) or revert it to leave the pool as-is:
```bash
# to keep the test god removal/addition: git add the Gods/Builds/index changes + commit
# to discard: git checkout -- "04. System/Data/SMITE" "03. Workspaces/Gaming/SMITE 2/Builds" viewer/public/index.json
```
State which you did.

---

## Self-Review

**Spec coverage:** Part A localStorage mine builds — `mineStore` (A1), editor writes + DetailPanel merges, `/api/build` retired (A2). Part B — `manage_gods` add/remove (B1), `/api/gods` endpoint replacing `/api/build` (B2), dev-gated Manage-gods UI (B3). Part C — attribution footer + DEPLOY.md (C1), dev vs static verification (C2). All spec sections mapped.

**Placeholder scan:** none — full code in each step. `add` is intentionally integration-verified (it scrapes live) rather than unit-tested; `remove` is unit-tested. The `manage_gods` module has an explicit "verify the real symbols" note because it wires into existing refresh/build_index internals whose exact signatures must be confirmed at implementation time — that's a verification instruction, not a placeholder.

**Type/name consistency:** `MineBuild {name, slot_order, starter?, notes?}` (A1) ← written by `saveMine` in BuildEditor (A2) ← read by `getMine` merged in DetailPanel (A2), shape matches `CuratedBuildEntry` (source "mine", already has `name`/`flex`-free). `/api/gods` body `{action, name}` (B2) ← posted by ManageGods add (B3) + App removeGod (B3) → consumed by `manage_gods.main([action, name])` (B1). `onChanged`/`onRemove`/`reload` wired in B3. `Footer` imported in C1. No dangling names.

**Safety:** remove **moves** (never deletes) to `_removed/`, reversible; `_archive/` untouched; the god-management endpoint is dev-only and spawns fixed argv (no shell); localStorage is per-browser (no server data). The scraper only runs on the owner's explicit add action.
