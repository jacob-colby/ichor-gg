import { useMemo, useState } from "react";
import type { Item } from "../types";
import { filterItems, sortItems, EFFICIENCY, type ItemFilter, type SortKey } from "../lib/itemFilters";
import { ItemCard } from "./ItemsShop";

/** Filterable item grid in a modal for the build editor. `exclude` hides items
 * already in the build. `onPick` adds an item; the parent decides when to close. */
export function ItemPickerModal({
  items, exclude = [], onPick, onClose,
}: {
  items: Item[];
  exclude?: string[];
  onPick: (name: string) => void;
  onClose: () => void;
}) {
  const [filter, setFilter] = useState<ItemFilter>({});
  const [sort, setSort] = useState<SortKey>("name");
  const excl = useMemo(() => new Set(exclude), [exclude]);
  const tags = useMemo(() => Array.from(new Set(items.flatMap((i) => i.effect_tags ?? []))).sort(), [items]);
  const stats = useMemo(() => Array.from(new Set(items.flatMap((i) => Object.keys(i.stats ?? {})))).sort(), [items]);
  const shown = useMemo(
    () => sortItems(filterItems(items, filter), sort).filter((i) => !excl.has(i.name)),
    [items, filter, sort, excl],
  );
  const set = (patch: Partial<ItemFilter>) => setFilter((f) => ({ ...f, ...patch }));
  const selCls = "rounded-md border border-line bg-bg2 px-2 py-1 text-xs text-muted focus:border-blue focus:outline-none";

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" onClick={onClose}>
      <div
        className="flex max-h-[85vh] w-full max-w-2xl flex-col rounded-lg border border-line bg-bg1 p-4 shadow-raised"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="mb-2 flex items-center">
          <div className="font-display text-lg font-semibold text-ink">Add item</div>
          <button type="button" onClick={onClose} className="press ml-auto rounded-md bg-bg2 px-2 py-1 text-xs text-muted hover:text-ink">Close</button>
        </div>
        <div className="mb-3 flex flex-wrap items-center gap-2">
          <div className="flex items-center gap-2 rounded-md border border-line bg-bg2 px-2.5 py-1.5 focus-within:border-blue">
            <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" strokeWidth="2" className="text-muted"><circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" /></svg>
            <input placeholder="Search items…" value={filter.q ?? ""} onChange={(e) => set({ q: e.target.value })}
              className="w-32 bg-transparent text-xs text-ink placeholder:text-muted focus:outline-none" />
          </div>
          <select
            value={filter.tier ?? ""}
            onChange={(e) => {
              const v = e.target.value;
              set({ tier: v ? (/^\d+$/.test(v) ? Number(v) : v) : undefined });
            }}
            className={selCls}
          >
            <option value="">All tiers</option><option value="3">Tier 3</option><option value="2">Tier 2</option><option value="1">Tier 1</option><option value="Glyph">Glyph</option>
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
          <span className="ml-auto font-mono text-[11px] text-faint">{shown.length}</span>
        </div>
        <div className="grid flex-1 grid-cols-[repeat(auto-fill,minmax(140px,1fr))] gap-2 overflow-y-auto sm:grid-cols-[repeat(auto-fill,minmax(160px,1fr))]">
          {shown.map((it) => (
            <ItemCard key={it.name} item={it} onClick={() => onPick(it.name)} />
          ))}
        </div>
      </div>
    </div>
  );
}
