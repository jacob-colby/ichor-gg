# SMITE 2 Build Editor + Community Starters Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the viewer read-write so users can save their own (`mine`) builds via an in-app editor, and show the recommended starter on community builds too.

**Architecture:** A Python `save_build` CLI upserts/deletes named `mine` entries (reusing the ownership-preserving note merge); a Vite dev-server middleware endpoint shells that CLI + rebuilds the index; a `BuildEditor` React component composes builds and POSTs to the endpoint, then reloads. `recommend` stamps the role starter on community entries; `build_index` exports the starter roster for the editor's dropdown.

**Tech Stack:** Python 3.10 (pytest), Vite + React 19 + TS + Vitest + RTL, Node child_process.

**Reference spec:** [2026-07-18-smite-build-editor-design.md](../specs/2026-07-18-smite-build-editor-design.md)

---

## File Structure
- `tools/smite/notes.py` — `upsert_mine_entry`, `delete_mine_entry` (modify).
- `tools/smite/save_build.py` — new CLI (create).
- `tools/smite/recommend.py` — stamp starter on community entries (modify).
- `tools/smite/build_index.py` — export `starters` (modify).
- `viewer/vite.config.ts` — `/api/build` middleware (modify).
- `viewer/src/types.ts` — `name` on curated, `starter` on community, `starters` on IndexData (modify).
- `viewer/src/lib/builds.ts` — `tabLabel` shows mine name (modify).
- `viewer/src/components/BuildEditor.tsx` — editor (create).
- `viewer/src/components/DetailPanel.tsx` — New/Edit/Delete + editor + community STARTER (modify).
- `viewer/src/App.tsx` — pass `starters` + `onReload` (modify).

---

## PHASE E — Pipeline (Python)

### Task E1: Community starter + `build_index` starters export

**Files:** Modify `tools/smite/recommend.py`, `tools/smite/build_index.py`; Test `tools/smite/tests/test_build_index.py`, `test_recommend.py`

- [ ] **Step 1: Write failing tests**

Append to `test_build_index.py`:
```python
def test_build_index_exports_starters(tmp_path, monkeypatch):
    # build_index reads the real vault via VAULT_ROOT-relative paths; assert the
    # returned dict carries a 'starters' key sourced from the weights.
    from smite import build_index
    from pathlib import Path
    result = build_index.build_index(Path(__file__).resolve().parents[3])
    assert "starters" in result
    assert isinstance(result["starters"], list)
```
Append to `test_recommend.py`:
```python
def test_stamp_community_starter_sets_starter_on_community(tmp_path):
    from smite import recommend, notes
    path = tmp_path / "Chiron-Conquest.md"
    notes.write_note(path, {"type": "smite-build", "god": "Chiron", "mode": "Conquest",
        "builds": [{"source": "community", "slot_order": [{"name": "X", "pick_rate": 0.5, "win_rate": 0.5}]}]}, "")
    recommend._stamp_community_starter(path, {"base": "Gilded Arrow", "upgrade": "Sharpshooter's Arrow"})
    fm, _ = notes.read_note(path)
    comm = next(b for b in fm["builds"] if b["source"] == "community")
    assert comm["starter"] == {"base": "Gilded Arrow", "upgrade": "Sharpshooter's Arrow"}
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_build_index.py -k starters smite/tests/test_recommend.py -k stamp_community -v`

- [ ] **Step 3: Implement**

In `build_index.py`, the module already imports `scoring`. In `build_index(vault_root)`, add the starters to the returned dict:
```python
    weights = scoring.load_weights(data_root / "_weights.yaml")
    return {"gods": _all(gods_dir), "items": items, "builds": _all(builds_dir),
            "starters": weights.get("starters", [])}
```
(Add the `weights = ...` line before the return; `data_root` already defined.)

In `recommend.py`, add the helper (after `load_build_note`):
```python
def _stamp_community_starter(path, starter):
    """Set `starter` on the community entry of a Build note (role-based, so the
    community build shows the same recommended starter as the suggested ones)."""
    if not starter:
        return
    fm, body = notes.read_note(path)
    if not fm:
        return
    changed = False
    for b in fm.get("builds", []):
        if b.get("source") == "community":
            b["starter"] = starter
            changed = True
    if changed:
        notes.write_note(path, fm, body)
```
In the `--all` branch's per-god loop, inside `if not args.report_only:`, after the per-mode write loop, add (Conquest only):
```python
                _stamp_community_starter(BUILDS_ROOT / f"{god['name']}-Conquest.md",
                                         scoring.pick_starter(god, weights))
```

- [ ] **Step 4: Run tests, confirm PASS**

Run: `cd tools && python -m pytest smite/tests/ -q -m "not live"`

- [ ] **Step 5: Commit**

```bash
git add tools/smite/build_index.py tools/smite/recommend.py tools/smite/tests/test_build_index.py tools/smite/tests/test_recommend.py
git commit -m "feat(smite): community starter stamp + starters export in index"
```

---

### Task E2: `upsert_mine_entry` + `delete_mine_entry`

**Files:** Modify `tools/smite/notes.py`; Test `tools/smite/tests/test_notes.py`

- [ ] **Step 1: Write failing tests** (append)

```python
def test_upsert_mine_entry_adds_and_replaces_by_name(tmp_path):
    path = tmp_path / "Chiron-Conquest.md"
    notes.write_note(path, {"type": "smite-build", "god": "Chiron", "mode": "Conquest",
        "builds": [{"source": "community", "slot_order": []},
                   {"source": "suggested", "archetype": "core", "slot_order": ["A"]}]}, "")
    notes.upsert_mine_entry(path, "Chiron", "Conquest",
        {"name": "My Crit", "slot_order": ["Deathbringer"]})
    fm, _ = notes.read_note(path)
    mine = [b for b in fm["builds"] if b["source"] == "mine"]
    assert len(mine) == 1 and mine[0]["name"] == "My Crit" and mine[0]["source"] == "mine"
    assert [b["source"] for b in fm["builds"]].count("community") == 1  # preserved
    # upsert same name -> replace, not duplicate
    notes.upsert_mine_entry(path, "Chiron", "Conquest", {"name": "My Crit", "slot_order": ["Rage"]})
    fm, _ = notes.read_note(path)
    mine = [b for b in fm["builds"] if b["source"] == "mine"]
    assert len(mine) == 1 and mine[0]["slot_order"] == ["Rage"]


def test_delete_mine_entry_removes_only_that_one(tmp_path):
    path = tmp_path / "Chiron-Conquest.md"
    notes.write_note(path, {"type": "smite-build", "god": "Chiron", "mode": "Conquest",
        "builds": [{"source": "community", "slot_order": []},
                   {"source": "mine", "name": "A", "slot_order": []},
                   {"source": "mine", "name": "B", "slot_order": []}]}, "")
    notes.delete_mine_entry(path, "A")
    fm, _ = notes.read_note(path)
    names = [b.get("name") for b in fm["builds"] if b["source"] == "mine"]
    assert names == ["B"]
    assert any(b["source"] == "community" for b in fm["builds"])
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_notes.py -k "mine_entry" -v`

- [ ] **Step 3: Implement** (append to `notes.py`)

```python
def upsert_mine_entry(path: Path, god: str, mode: str, entry: dict) -> None:
    """Add or replace (matched by name) a single source:mine build entry,
    preserving community/suggested/other-mine entries. Creates the note if
    missing."""
    frontmatter, body = read_note(path)
    if not frontmatter:
        frontmatter = {"type": "smite-build", "god": god, "mode": mode, "builds": []}
    name = entry.get("name")
    kept = [b for b in frontmatter.get("builds", [])
            if not (b.get("source") == "mine" and b.get("name") == name)]
    frontmatter["builds"] = kept + [{**entry, "source": "mine"}]
    write_note(path, frontmatter, body)


def delete_mine_entry(path: Path, name: str) -> None:
    """Remove the source:mine entry with the given name; leave all else intact."""
    frontmatter, body = read_note(path)
    if not frontmatter:
        return
    frontmatter["builds"] = [b for b in frontmatter.get("builds", [])
                             if not (b.get("source") == "mine" and b.get("name") == name)]
    write_note(path, frontmatter, body)
```

- [ ] **Step 4: Run tests, confirm PASS**

Run: `cd tools && python -m pytest smite/tests/test_notes.py -v`

- [ ] **Step 5: Commit**

```bash
git add tools/smite/notes.py tools/smite/tests/test_notes.py
git commit -m "feat(smite): upsert/delete named mine build entries"
```

---

### Task E3: `save_build` CLI

**Files:** Create `tools/smite/save_build.py`; Test `tools/smite/tests/test_save_build.py`

- [ ] **Step 1: Write failing test** (create the file)

```python
import io
import json
from pathlib import Path

from smite import save_build, notes


def _setup(tmp_path, monkeypatch):
    # Redirect the module's vault paths at a tmp tree with one god + item note.
    data = tmp_path / "data"
    (data / "Gods").mkdir(parents=True)
    (data / "Items").mkdir(parents=True)
    notes.write_note(data / "Gods" / "Chiron.md", {"name": "Chiron"}, "")
    notes.write_note(data / "Items" / "Deathbringer.md", {"name": "Deathbringer"}, "")
    builds = tmp_path / "builds"; builds.mkdir()
    monkeypatch.setattr(save_build, "DATA_ROOT", data)
    monkeypatch.setattr(save_build, "BUILDS_ROOT", builds)
    return builds


def _run(payload, monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO(json.dumps(payload)))
    return save_build.main()


def test_save_build_writes_mine_entry(tmp_path, monkeypatch):
    builds = _setup(tmp_path, monkeypatch)
    rc = _run({"action": "save", "god": "Chiron", "mode": "Conquest",
               "name": "My Build", "slot_order": ["Deathbringer", "Unknown Item"]}, monkeypatch)
    assert rc == 0
    fm, _ = notes.read_note(builds / "Chiron-Conquest.md")
    mine = next(b for b in fm["builds"] if b["source"] == "mine")
    assert mine["name"] == "My Build"
    assert mine["slot_order"] == ["Deathbringer"]  # unknown item filtered out


def test_save_build_rejects_unknown_god(tmp_path, monkeypatch):
    _setup(tmp_path, monkeypatch)
    rc = _run({"action": "save", "god": "../etc", "mode": "Conquest", "name": "x", "slot_order": []}, monkeypatch)
    assert rc == 1


def test_save_build_delete(tmp_path, monkeypatch):
    builds = _setup(tmp_path, monkeypatch)
    _run({"action": "save", "god": "Chiron", "mode": "Conquest", "name": "X", "slot_order": ["Deathbringer"]}, monkeypatch)
    rc = _run({"action": "delete", "god": "Chiron", "mode": "Conquest", "name": "X"}, monkeypatch)
    assert rc == 0
    fm, _ = notes.read_note(builds / "Chiron-Conquest.md")
    assert not [b for b in fm["builds"] if b["source"] == "mine"]
```

- [ ] **Step 2: Run, confirm FAIL** (no module)

Run: `cd tools && python -m pytest smite/tests/test_save_build.py -v`

- [ ] **Step 3: Implement `tools/smite/save_build.py`**

```python
"""Write or delete a user 'mine' build from a JSON payload on stdin. Invoked by
the viewer's local write endpoint. Validates god + mode + item names so a
malicious/mistyped payload can't traverse paths or inject junk. Data flows via
stdin JSON only — never shell-interpolated.

Payload: {"action": "save"|"delete", "god": str, "mode": str, "name": str,
          "slot_order": [str], "starter": {"base","upgrade"}?, "notes": str?}
"""
import json
import sys
from pathlib import Path

from smite import notes

VAULT_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = VAULT_ROOT / "04. System" / "Data" / "SMITE"
BUILDS_ROOT = VAULT_ROOT / "03. Workspaces" / "Gaming" / "SMITE 2" / "Builds"
MODES = {"Conquest", "Joust"}


def _known(dir_name):
    d = DATA_ROOT / dir_name
    return {notes.read_note(p)[0].get("name") for p in d.glob("*.md")} if d.exists() else set()


def _fail(msg):
    print(json.dumps({"ok": False, "error": msg}))
    return 1


def main(argv=None):
    try:
        payload = json.load(sys.stdin)
    except Exception as exc:
        return _fail(f"bad payload: {exc}")

    god, mode = payload.get("god"), payload.get("mode")
    if god not in _known("Gods") or mode not in MODES:
        return _fail("unknown god or mode")
    path = BUILDS_ROOT / f"{god}-{mode}.md"

    action = payload.get("action")
    if action == "delete":
        notes.delete_mine_entry(path, payload.get("name"))
    elif action == "save":
        name = (payload.get("name") or "").strip()
        if not name:
            return _fail("name required")
        items = _known("Items")
        entry = {"name": name, "slot_order": [s for s in (payload.get("slot_order") or []) if s in items]}
        starter = payload.get("starter") or {}
        if starter.get("base") in items and starter.get("upgrade") in items:
            entry["starter"] = {"base": starter["base"], "upgrade": starter["upgrade"]}
        if payload.get("notes"):
            entry["notes"] = str(payload["notes"])
        notes.upsert_mine_entry(path, god, mode, entry)
    else:
        return _fail("unknown action")

    print(json.dumps({"ok": True}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run tests, confirm PASS**

Run: `cd tools && python -m pytest smite/tests/test_save_build.py -v`

- [ ] **Step 5: Commit**

```bash
git add tools/smite/save_build.py tools/smite/tests/test_save_build.py
git commit -m "feat(smite): save_build CLI (validated JSON-stdin mine writer)"
```

---

## PHASE V — Endpoint + viewer

### Task E4: Vite `/api/build` write endpoint

**Files:** Modify `viewer/vite.config.ts`

- [ ] **Step 1: Replace `viewer/vite.config.ts`**

```typescript
import { defineConfig, type Plugin } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";

// Local-only write endpoint: shells the Python save_build CLI (fixed argv, body
// piped via stdin — no shell interpolation), then rebuilds index.json.
function saveBuildApi(): Plugin {
  const toolsDir = fileURLToPath(new URL("../tools", import.meta.url));
  const run = (mod: string, input: string | null) =>
    new Promise<void>((resolve, reject) => {
      const p = spawn("python", ["-m", mod], { cwd: toolsDir });
      let err = "";
      p.stderr.on("data", (d) => (err += d));
      if (input !== null) { p.stdin.write(input); p.stdin.end(); }
      p.on("close", (code) => (code === 0 ? resolve() : reject(new Error(err || `${mod} exit ${code}`))));
    });
  return {
    name: "save-build-api",
    configureServer(server) {
      server.middlewares.use("/api/build", (req, res) => {
        if (req.method !== "POST") { res.statusCode = 405; res.end(); return; }
        let body = "";
        req.on("data", (c) => (body += c));
        req.on("end", () => {
          run("smite.save_build", body)
            .then(() => run("smite.build_index", null))
            .then(() => { res.setHeader("Content-Type", "application/json"); res.end(JSON.stringify({ ok: true })); })
            .catch((e) => { res.statusCode = 500; res.setHeader("Content-Type", "application/json"); res.end(JSON.stringify({ ok: false, error: String(e) })); });
        });
      });
    },
  };
}

export default defineConfig({
  plugins: [react(), tailwindcss(), saveBuildApi()],
});
```

- [ ] **Step 2: Verify the config still builds/serves**

Run: `cd viewer && npx vite build` (expected: builds; the plugin only affects the dev server, not the build). Then confirm the dev server starts without error: `npx vite --port 5178 --strictPort &` … or just confirm `npx tsc -p tsconfig.node.json --noEmit` if present passes; otherwise rely on the build. (The endpoint itself is exercised end-to-end in E7.)

- [ ] **Step 3: Commit**

```bash
git add viewer/vite.config.ts
git commit -m "feat(viewer): local /api/build write endpoint"
```

---

### Task E5: Types + `tabLabel` + community STARTER

**Files:** Modify `viewer/src/types.ts`, `viewer/src/lib/builds.ts`, `viewer/src/components/DetailPanel.tsx`; Test `builds.test.ts`, `DetailPanel.test.tsx`

- [ ] **Step 1: Update `types.ts`**
- Add to `CuratedBuildEntry`: `name?: string;`
- Add to `CommunityBuildEntry`: `starter?: { base: string; upgrade: string };`
- Add to `IndexData`: `starters?: { base: string; upgrade: string }[];`

- [ ] **Step 2: Failing test for `tabLabel`** (append to `builds.test.ts`)

```typescript
it("labels a mine entry by its name", () => {
  expect(tabLabel({ source: "mine", name: "My Crit", slot_order: [] } as any)).toBe("My Crit");
  expect(tabLabel({ source: "mine", slot_order: [] } as any)).toBe("mine");
});
```

- [ ] **Step 3: Update `tabLabel` in `builds.ts`**

```typescript
export function tabLabel(entry: BuildEntry): string {
  if (entry.source === "suggested") return entry.archetype ?? "suggested";
  if (entry.source === "mine") return entry.name ?? "mine";
  return entry.source;
}
```

- [ ] **Step 4: Failing test for community starter** (append to `DetailPanel.test.tsx`)

```tsx
it("shows the starter line on a community build too", () => {
  const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
    { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
      slot_order: [{ name: "X", pick_rate: 0.5, win_rate: 0.5 }], source_url: "u",
      starter: { base: "Gilded Arrow", upgrade: "Sharpshooter's Arrow" } },
  ] }];
  render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                      mode="Conquest" onModeChange={() => {}} />);
  expect(screen.getByText(/STARTER/i)).toBeInTheDocument();
  expect(screen.getByText("Gilded Arrow")).toBeInTheDocument();
});
```

- [ ] **Step 5: Drop the `!community` guard on the STARTER block** in `DetailPanel.tsx`

Change `{!community && active.starter && (` to `{active.starter && (`. (The block already reads `active.starter.base/upgrade` — valid for both entry types now that `CommunityBuildEntry` has `starter`.)

- [ ] **Step 6: Run tests + typecheck, confirm PASS**

Run: `cd viewer && npx vitest run && npx tsc --noEmit`

- [ ] **Step 7: Commit**

```bash
git add viewer/src/types.ts viewer/src/lib/builds.ts viewer/src/components/DetailPanel.tsx viewer/src/lib/builds.test.ts viewer/src/components/DetailPanel.test.tsx
git commit -m "feat(viewer): mine-name tabs + starter on community builds"
```

---

### Task E6: `BuildEditor` component + wiring

**Files:** Create `viewer/src/components/BuildEditor.tsx`; Modify `viewer/src/components/DetailPanel.tsx`, `viewer/src/App.tsx`; Test `BuildEditor.test.tsx`

- [ ] **Step 1: Failing test** (create `viewer/src/components/BuildEditor.test.tsx`, matching the project's RTL style)

```tsx
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { BuildEditor } from "./BuildEditor";
import type { Item } from "../types";

const items = [{ name: "Deathbringer" }, { name: "Rage" }] as Item[];

it("saves a build via the endpoint and calls onSaved", async () => {
  const fetchMock = vi.fn().mockResolvedValue({ json: () => Promise.resolve({ ok: true }) });
  vi.stubGlobal("fetch", fetchMock);
  const onSaved = vi.fn(); const onClose = vi.fn();
  render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                      onClose={onClose} onSaved={onSaved} />);
  fireEvent.change(screen.getByPlaceholderText(/build name/i), { target: { value: "My Build" } });
  fireEvent.change(screen.getByPlaceholderText(/search items/i), { target: { value: "Death" } });
  fireEvent.click(screen.getByText("Deathbringer"));
  fireEvent.click(screen.getByRole("button", { name: /^save$/i }));
  await waitFor(() => expect(onSaved).toHaveBeenCalled());
  const body = JSON.parse(fetchMock.mock.calls[0][1].body);
  expect(body).toMatchObject({ action: "save", god: "Chiron", mode: "Conquest",
    name: "My Build", slot_order: ["Deathbringer"] });
  vi.unstubAllGlobals();
});
```

- [ ] **Step 2: Run, confirm FAIL** (no module)

Run: `cd viewer && npx vitest run src/components/BuildEditor.test.tsx`

- [ ] **Step 3: Create `viewer/src/components/BuildEditor.tsx`**

```tsx
import { useState } from "react";
import type { Item } from "../types";

interface StarterPair { base: string; upgrade: string }
export interface MineDraft { name: string; slot_order: string[]; starter?: StarterPair; notes?: string }

interface BuildEditorProps {
  god: string;
  mode: string;
  items: Item[];
  starters: StarterPair[];
  initial?: MineDraft | null;
  defaultStarter?: StarterPair;
  onClose: () => void;
  onSaved: () => void;
}

export function BuildEditor({ god, mode, items, starters, initial, defaultStarter, onClose, onSaved }: BuildEditorProps) {
  const [name, setName] = useState(initial?.name ?? "");
  const [slots, setSlots] = useState<string[]>(initial?.slot_order ?? []);
  const cur = initial?.starter ?? defaultStarter;
  const [starterIdx, setStarterIdx] = useState(() => {
    const i = starters.findIndex((s) => s.base === cur?.base);
    return i >= 0 ? i : -1;
  });
  const [notes, setNotes] = useState(initial?.notes ?? "");
  const [query, setQuery] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  const results = query.trim()
    ? items.filter((it) => it.name.toLowerCase().includes(query.toLowerCase()) && !slots.includes(it.name)).slice(0, 8)
    : [];

  const post = async (payload: object) => {
    setBusy(true); setError(null);
    const res = await fetch("/api/build", {
      method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload),
    }).then((r) => r.json()).catch((e) => ({ ok: false, error: String(e) }));
    setBusy(false);
    if (res.ok) { onSaved(); onClose(); } else { setError(res.error || "Request failed"); }
  };

  const save = () => {
    if (!name.trim()) return setError("Name required");
    if (slots.length === 0) return setError("Add at least one item");
    post({ action: "save", god, mode, name: name.trim(), slot_order: slots,
           starter: starterIdx >= 0 ? starters[starterIdx] : undefined,
           notes: notes.trim() || undefined });
  };

  const move = (i: number, d: number) => {
    const j = i + d; if (j < 0 || j >= slots.length) return;
    const next = [...slots]; [next[i], next[j]] = [next[j], next[i]]; setSlots(next);
  };

  return (
    <div className="max-w-md rounded-lg border border-line bg-bg1 p-4">
      <div className="mb-3 font-display text-lg font-semibold text-ink">
        {initial ? "Edit build" : "New build"} — {god} {mode}
      </div>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Build name"
        className="mb-3 w-full rounded border border-line bg-bg2 px-2 py-1 text-sm text-ink" />

      <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Search items…"
        className="w-full rounded border border-line bg-bg2 px-2 py-1 text-sm text-ink" />
      {results.length > 0 && (
        <div className="mt-1 rounded border border-line bg-bg2">
          {results.map((it) => (
            <button key={it.name} type="button" onClick={() => { if (slots.length < 6) setSlots([...slots, it.name]); setQuery(""); }}
              className="block w-full px-2 py-1 text-left text-sm text-ink hover:bg-line">{it.name}</button>
          ))}
        </div>
      )}
      <div className="my-3 flex flex-col gap-1">
        {slots.map((n, i) => (
          <div key={`${n}-${i}`} className="flex items-center gap-2 text-sm text-ink">
            <span className="w-4 text-muted">{i + 1}</span>
            <span className="flex-1">{n}</span>
            <button type="button" onClick={() => move(i, -1)} className="px-1 text-muted hover:text-ink">↑</button>
            <button type="button" onClick={() => move(i, 1)} className="px-1 text-muted hover:text-ink">↓</button>
            <button type="button" onClick={() => setSlots(slots.filter((_, j) => j !== i))} className="px-1 text-muted hover:text-ink">✕</button>
          </div>
        ))}
        {slots.length === 0 && <div className="text-xs text-muted">No items yet (max 6).</div>}
      </div>

      {starters.length > 0 && (
        <select value={starterIdx} onChange={(e) => setStarterIdx(Number(e.target.value))}
          className="mb-3 w-full rounded border border-line bg-bg2 px-2 py-1 text-sm text-ink">
          <option value={-1}>No starter</option>
          {starters.map((s, i) => <option key={s.base} value={i}>{s.base} → {s.upgrade}</option>)}
        </select>
      )}

      <textarea value={notes} onChange={(e) => setNotes(e.target.value)} placeholder="Notes (optional)"
        className="mb-3 w-full rounded border border-line bg-bg2 px-2 py-1 text-sm text-ink" rows={2} />

      {error && <div className="mb-2 text-xs text-red-400">{error}</div>}
      <div className="flex gap-2">
        <button type="button" disabled={busy} onClick={save}
          className="rounded bg-gold px-3 py-1 text-sm font-medium text-bg0 disabled:opacity-50">Save</button>
        {initial && (
          <button type="button" disabled={busy} onClick={() => post({ action: "delete", god, mode, name: initial.name })}
            className="rounded bg-bg2 px-3 py-1 text-sm text-red-400 hover:bg-line">Delete</button>
        )}
        <button type="button" onClick={onClose} className="rounded bg-bg2 px-3 py-1 text-sm text-muted hover:bg-line">Cancel</button>
      </div>
    </div>
  );
}
```

- [ ] **Step 4: Wire into `DetailPanel.tsx`**

Add imports + props:
```tsx
import { BuildEditor, type MineDraft } from "./BuildEditor";
```
Extend `DetailPanelProps` with:
```tsx
  starters: { base: string; upgrade: string }[];
  onReload: () => void;
```
Add editor state near the other `useState`s:
```tsx
  const [editing, setEditing] = useState<MineDraft | "new" | null>(null);
```
Reset it in the existing reset effect (add `setEditing(null);` inside the `useEffect(() => {...}, [god, note])`).

When `editing` is set, render the editor instead of the build body — right after the `if (!note ...)` guard, add:
```tsx
  if (editing) {
    const recStarter = entries.map((e) => (e as { starter?: { base: string; upgrade: string } }).starter).find(Boolean);
    return (
      <BuildEditor
        god={god}
        mode={note.mode}
        items={items}
        starters={starters}
        initial={editing === "new" ? null : editing}
        defaultStarter={recStarter}
        onClose={() => setEditing(null)}
        onSaved={onReload}
      />
    );
  }
```
(Place this after `const entries = note.builds;` etc. are computed, so `entries`/`note` are in scope. Move the `entries`/`active`/`community`/`swaps` computation above this block if needed.)

Add a **＋ New build** button in the header (next to the mode toggle) and Edit/Delete affordance on the active mine tab. Simplest: after the tablist, add:
```tsx
      <div className="mb-3 flex gap-2">
        <button type="button" onClick={() => setEditing("new")}
          className="rounded bg-bg2 px-3 py-1 text-xs text-blue hover:bg-line">+ New build</button>
        {!community && active.source === "mine" && (
          <button type="button" onClick={() => setEditing(active as MineDraft)}
            className="rounded bg-bg2 px-3 py-1 text-xs text-muted hover:bg-line">Edit this build</button>
        )}
      </div>
```

- [ ] **Step 5: Wire `App.tsx`** — pass the new props:
```tsx
          <DetailPanel
            god={selectedGod}
            godData={data.gods.find((g) => g.name === selectedGod)}
            items={data.items}
            builds={data.builds}
            mode={mode}
            onModeChange={setMode}
            starters={data.starters ?? []}
            onReload={reload}
          />
```

- [ ] **Step 6: Run tests + typecheck, confirm PASS**

Run: `cd viewer && npx vitest run && npx tsc --noEmit`
Fix any existing DetailPanel test that now needs `starters={[]} onReload={() => {}}` props — add them, keep assertions intact.

- [ ] **Step 7: Commit**

```bash
git add viewer/src/components/BuildEditor.tsx viewer/src/components/BuildEditor.test.tsx viewer/src/components/DetailPanel.tsx viewer/src/App.tsx viewer/src/components/DetailPanel.test.tsx
git commit -m "feat(viewer): in-app build editor (create/edit/delete mine builds)"
```

---

### Task E7: Full regen + end-to-end browser verification

**Files:** generated — `Builds/*.md`, `viewer/public/`

- [ ] **Step 1: Regen so community builds get their starter**

Run from `tools/`: `python -m smite.recommend --all` then `python -m smite.build_index`.
Verify: `cd .. && python -c "
import json; d=json.load(open('viewer/public/index.json',encoding='utf-8'))
print('index has starters roster:', bool(d.get('starters')))
for n in d['builds']:
    if n['god']=='Chiron' and n['mode']=='Conquest':
        comm=next((b for b in n['builds'] if b['source']=='community'), None)
        print('Chiron community starter:', comm and comm.get('starter'))
"`
Expected: starters roster present; community entry has the starter.

- [ ] **Step 2: Both suites green**

Run: `cd tools && python -m pytest smite/tests/ -q -m "not live"` and `cd ../viewer && npx vitest run`.

- [ ] **Step 3: End-to-end browser verification**

Start the dev server (real one — the endpoint needs it). In the browser: (a) confirm a community build now shows the STARTER line; (b) click **+ New build**, name it, add a few items, pick a starter, Save — confirm no error, the panel reloads, and a new named tab appears; (c) confirm the vault note `<god>-Conquest.md` gained the `mine` entry (check via a file read); (d) Edit the build (change an item, Save) and confirm it updates in place (not duplicated); (e) Delete it and confirm the tab disappears. Screenshot the editor + a saved build. Fix issues and re-verify.

- [ ] **Step 4: Commit generated output**

```bash
git add "03. Workspaces/Gaming/SMITE 2/Builds/" "04. System/Data/SMITE/Analysis/" viewer/public/
git commit -m "chore(smite): regenerate builds with community starters"
```

---

## Self-Review

**Spec coverage:** community starter stamp + index export (E1), mine upsert/delete (E2), save_build CLI with validation (E3), write endpoint (E4), types+tabLabel+community-starter display (E5), editor UI + wiring (E6), regen + e2e verify (E7). All spec sections mapped. Swap-editing correctly excluded (v1).

**Placeholder scan:** none — all code complete. The endpoint (E4) and full round-trip are verified in E7 (integration), which is appropriate for a dev-server middleware that can't be unit-tested.

**Type/name consistency:** `save_build` reads `{action,god,mode,name,slot_order,starter,notes}` — the same shape `BuildEditor` POSTs (E6) and the endpoint pipes (E4). `notes.upsert_mine_entry(path, god, mode, entry)` / `delete_mine_entry(path, name)` (E2) called by `save_build` (E3). `tabLabel` mine→name (E5) matches the `name` field written by the CLI. `index.starters` (E1 build_index) typed on `IndexData` (E5) and consumed by the editor's dropdown (E6). `DetailPanel` new props `starters`/`onReload` (E6) passed from `App` (E6 step 5).

**Safety:** the endpoint spawns a fixed argv (`python -m smite.save_build`) with the body on stdin — no shell string interpolation; `save_build` validates god against real gods and mode against the allowlist before building the path, and filters items to the known pool. Localhost dev-server only.
