import { useState } from "react";
import type { Item } from "../types";
import { iconSlug } from "../lib/builds";
import { saveMine, deleteMine } from "../lib/mineStore";
import { ItemPickerModal } from "./ItemPickerModal";

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
  const [error, setError] = useState<string | null>(null);
  const [picking, setPicking] = useState(false);

  const addItem = (n: string) => {
    if (slots.length < 6 && !slots.includes(n)) setSlots([...slots, n]);
    setPicking(false);
  };

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

      <button
        type="button"
        onClick={() => setPicking(true)}
        disabled={slots.length >= 6}
        className="w-full rounded border border-line bg-bg2 px-2 py-1 text-sm text-blue hover:bg-line disabled:opacity-50"
      >
        + Add item{slots.length >= 6 ? " (max 6)" : ""}
      </button>
      {picking && (
        <ItemPickerModal items={items} exclude={slots} onPick={addItem} onClose={() => setPicking(false)} />
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
        <button type="button" onClick={save}
          className="rounded bg-gold px-3 py-1 text-sm font-medium text-bg0">Save</button>
        {initial && (
          <button type="button" onClick={remove}
            className="rounded bg-bg2 px-3 py-1 text-sm text-red-400 hover:bg-line">Delete</button>
        )}
        <button type="button" onClick={onClose} className="rounded bg-bg2 px-3 py-1 text-sm text-muted hover:bg-line">Cancel</button>
      </div>
    </div>
  );
}
