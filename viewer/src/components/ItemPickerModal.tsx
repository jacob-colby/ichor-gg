import { useMemo, useState } from "react";
import type { Item } from "../types";
import { filterItems, sortItems, efficiencyLabel, EFFICIENCY, type ItemFilter, type SortKey } from "../lib/itemFilters";
import { iconSlug } from "../lib/builds";

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
  const selCls = "rounded border border-line bg-bg2 px-2 py-1 text-xs text-ink";

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" onClick={onClose}>
      <div className="flex max-h-[85vh] w-full max-w-2xl flex-col rounded-lg border border-line bg-bg1 p-4" onClick={(e) => e.stopPropagation()}>
        <div className="mb-2 flex items-center">
          <div className="font-display text-lg font-semibold text-ink">Add item</div>
          <button type="button" onClick={onClose} className="ml-auto rounded bg-bg2 px-2 py-1 text-xs text-muted hover:bg-line">Close</button>
        </div>
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
          <span className="text-xs text-muted">{shown.length}</span>
        </div>
        <div className="grid flex-1 grid-cols-[repeat(auto-fill,minmax(150px,1fr))] gap-2 overflow-y-auto">
          {shown.map((it) => {
            const e = efficiencyLabel(it.efficiency_tier);
            return (
              <button
                key={it.name}
                type="button"
                onClick={() => onPick(it.name)}
                className="flex items-center gap-2 rounded-lg border border-line bg-bg2 p-2 text-left hover:border-blue"
              >
                <img src={`/icons/${iconSlug(it.name)}.png`} alt="" className="h-7 w-7 flex-none rounded bg-bg1"
                  onError={(ev) => { const i = ev.currentTarget; if (i.dataset.r) { i.style.visibility = "hidden"; return; } i.dataset.r = "1"; i.src = `/icons/${iconSlug(it.name)}.png?r=1`; }} />
                <div className="min-w-0">
                  <div className="truncate text-xs text-ink">{it.name}</div>
                  <div className="font-mono text-[10px] text-muted">{it.cost}g · <span className={e.cls.replace(/bg-\S+/, "")}>{e.text}</span></div>
                </div>
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
}
