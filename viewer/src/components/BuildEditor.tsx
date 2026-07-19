import { useState } from "react";
import type { Item } from "../types";
import { iconSlug } from "../lib/builds";

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
  onSaved: (name: string) => void;
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
      action: "save",
      god,
      mode,
      name: name.trim(),
      slot_order: slots,
      starter: starterIdx >= 0 ? starters[starterIdx] : undefined,
      notes: notes.trim() || undefined,
    }, name.trim());
  };

  const move = (i: number, d: number) => {
    const j = i + d;
    if (j < 0 || j >= slots.length) return;
    const next = [...slots];
    [next[i], next[j]] = [next[j], next[i]];
    setSlots(next);
  };

  return (
    <div className="max-w-md rounded-lg border border-line bg-bg1 p-4">
      <div className="mb-3 font-display text-lg font-semibold text-ink">
        {initial ? "Edit build" : "New build"} — {god} {mode}
      </div>
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Build name"
        className="mb-3 w-full rounded border border-line bg-bg2 px-2 py-1 text-sm text-ink"
      />

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search items…"
        className="w-full rounded border border-line bg-bg2 px-2 py-1 text-sm text-ink"
      />
      {results.length > 0 && (
        <div className="mt-1 rounded border border-line bg-bg2">
          {results.map((it) => (
            <button
              key={it.name}
              type="button"
              onClick={() => {
                if (slots.length < 6) setSlots([...slots, it.name]);
                setQuery("");
              }}
              className="flex w-full items-center gap-2 px-2 py-1 text-left text-sm text-ink hover:bg-line"
            >
              <img
                src={`/icons/${iconSlug(it.name)}.png`}
                alt=""
                className="h-5 w-5 flex-none rounded bg-bg2"
                onError={(e) => {
                  const i = e.currentTarget;
                  if (i.dataset.r) { i.style.visibility = "hidden"; return; }
                  i.dataset.r = "1";
                  i.src = `/icons/${iconSlug(it.name)}.png?r=1`;
                }}
              />
              {it.name}
            </button>
          ))}
        </div>
      )}

      <div className="my-3 flex flex-col gap-1">
        {slots.map((n, i) => (
          <div key={`${n}-${i}`} className="flex items-center gap-2 text-sm text-ink">
            <span className="w-4 text-muted">{i + 1}</span>
            <img
              src={`/icons/${iconSlug(n)}.png`}
              alt=""
              className="h-5 w-5 flex-none rounded bg-bg2"
              onError={(e) => {
                const im = e.currentTarget;
                if (im.dataset.r) { im.style.visibility = "hidden"; return; }
                im.dataset.r = "1";
                im.src = `/icons/${iconSlug(n)}.png?r=1`;
              }}
            />
            <span className="flex-1">{n}</span>
            <button type="button" onClick={() => move(i, -1)} className="px-1 text-muted hover:text-ink">↑</button>
            <button type="button" onClick={() => move(i, 1)} className="px-1 text-muted hover:text-ink">↓</button>
            <button type="button" onClick={() => setSlots(slots.filter((_, j) => j !== i))} className="px-1 text-muted hover:text-ink">✕</button>
          </div>
        ))}
        {slots.length === 0 && <div className="text-xs text-muted">No items yet (max 6).</div>}
      </div>

      {starters.length > 0 && (
        <select
          value={starterIdx}
          onChange={(e) => setStarterIdx(Number(e.target.value))}
          className="mb-3 w-full rounded border border-line bg-bg2 px-2 py-1 text-sm text-ink"
        >
          <option value={-1}>No starter</option>
          {starters.map((s, i) => (
            <option key={s.base} value={i}>{s.base} → {s.upgrade}</option>
          ))}
        </select>
      )}

      <textarea
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
        placeholder="Notes (optional)"
        className="mb-3 w-full rounded border border-line bg-bg2 px-2 py-1 text-sm text-ink"
        rows={2}
      />

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
