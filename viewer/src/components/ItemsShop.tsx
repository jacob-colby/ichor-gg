import { useMemo, useState } from "react";
import type { Item } from "../types";
import {
  filterItems,
  sortItems,
  efficiencyLabel,
  tierLabel,
  EFFICIENCY,
  type SortKey,
  type ItemFilter,
} from "../lib/itemFilters";
import { iconSlug } from "../lib/builds";
import { toHash, navigate } from "../lib/useHashRoute";

export function ItemIcon({ name, size = "h-8 w-8" }: { name: string; size?: string }) {
  return (
    <img
      src={`/icons/${iconSlug(name)}.png`}
      alt=""
      className={`${size} flex-none rounded-sm bg-bg2`}
      onError={(e) => {
        const i = e.currentTarget;
        if (i.dataset.r) { i.style.visibility = "hidden"; return; }
        i.dataset.r = "1";
        i.src = `/icons/${iconSlug(name)}.png?r=1`;
      }}
    />
  );
}

function EffBadge({ tier }: { tier: string | null | undefined }) {
  const e = efficiencyLabel(tier);
  return <span className={`rounded-sm px-1.5 py-0.5 text-[10px] ${e.cls}`}>{e.text}</span>;
}

function MetaBadge({ meta }: { meta?: { win_avg: number; gods: number } }) {
  if (!meta) return null;
  return <span className="text-[10px] text-muted">{Math.round(meta.win_avg * 100)}% avg · {meta.gods}</span>;
}

/** Shared card language for the shop grid and the ItemPickerModal grid. */
export function ItemCard({ item, onClick }: { item: Item; onClick: () => void }) {
  return (
    <button
      type="button"
      onClick={onClick}
      className="press flex flex-col gap-1.5 rounded-md border border-line bg-bg2 p-2 text-left transition-colors duration-[180ms] ease-standard hover:border-line-strong"
    >
      <div className="flex items-center gap-2">
        <ItemIcon name={item.name} />
        <div className="min-w-0 flex-1">
          <div className="truncate text-sm text-ink">{item.name}</div>
          <div className="font-mono text-[10px] text-faint"><span className="text-gold">{item.cost}g</span> · {tierLabel(item.tier)}</div>
        </div>
      </div>
      <div className="flex items-center justify-between gap-1">
        <div className="flex items-center gap-1"><EffBadge tier={item.efficiency_tier} /><MetaBadge meta={item.meta} /></div>
        {(item.effect_tags?.length ?? 0) > 0 && (
          <span className="truncate text-[10px] text-blue">{item.effect_tags!.join(" · ")}</span>
        )}
      </div>
    </button>
  );
}

function ItemDetail({ item, byName }: { item: Item; byName: Map<string, Item> }) {
  const links = (names: string[]) =>
    names.filter((n) => byName.has(n)).map((n) => (
      <button
        key={n}
        type="button"
        onClick={() => navigate(toHash.item(n))}
        className="press inline-flex items-center gap-1 rounded-sm bg-bg2 px-1.5 py-0.5 text-xs text-blue hover:bg-line"
      >
        <ItemIcon name={n} size="h-4 w-4" />
        {n}
      </button>
    ));
  return (
    <div className="mb-4 rounded-lg border border-line bg-bg1 p-4 shadow-card">
      <div className="mb-2 flex items-center gap-3">
        <ItemIcon name={item.name} size="h-10 w-10" />
        <div>
          <div className="font-display text-lg font-semibold text-ink">{item.name}</div>
          <div className="font-mono text-xs text-faint"><span className="text-gold">{item.cost}g</span> · {tierLabel(item.tier)}</div>
        </div>
        <div className="ml-auto flex items-center gap-2"><MetaBadge meta={item.meta} /><EffBadge tier={item.efficiency_tier} /></div>
      </div>
      {Object.entries(item.stats || {}).map(([k, v]) => (
        <div key={k} className="flex justify-between text-sm text-muted">
          <span>{k}</span>
          <span className="font-mono text-ink">{v}</span>
        </div>
      ))}
      {item.passive && <div className="mt-2 text-sm text-muted">{item.passive}</div>}
      {(item.effect_tags?.length ?? 0) > 0 && (
        <div className="mt-2 flex flex-wrap gap-1">
          {item.effect_tags!.map((t) => (
            <span key={t} className="rounded-sm bg-line px-1.5 py-0.5 text-[10px] text-blue">{t}</span>
          ))}
        </div>
      )}
      {item.builds_from?.length ? (
        <div className="mt-3 text-xs text-muted">Builds from: <span className="ml-1 inline-flex flex-wrap gap-1">{links(item.builds_from)}</span></div>
      ) : null}
      {item.builds_into?.length ? (
        <div className="mt-2 text-xs text-muted">Builds into: <span className="ml-1 inline-flex flex-wrap gap-1">{links(item.builds_into)}</span></div>
      ) : null}
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
  const selCls = "rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-xs text-muted focus:border-blue focus:outline-none";
  const gridCls = "grid grid-cols-[repeat(auto-fill,minmax(140px,1fr))] gap-2 sm:grid-cols-[repeat(auto-fill,minmax(180px,1fr))]";

  return (
    <div className="p-4">
      {open && <ItemDetail item={open} byName={byName} />}
      <div className="mb-3 text-[11px] text-faint">
        Rating = stats-per-gold (not power). <b className="text-ink-soft">Premium</b> items are often worth overpaying for their passive. Avg = community win rate where used.
      </div>
      <div className="mb-3 flex flex-wrap items-center gap-2">
        <div className="flex items-center gap-2 rounded-md border border-line bg-bg2 px-3 py-2 focus-within:border-blue">
          <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2" className="text-muted"><circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" /></svg>
          <input placeholder="Search items…" value={filter.q ?? ""} onChange={(e) => set({ q: e.target.value })}
            className="w-36 bg-transparent text-xs text-ink placeholder:text-muted focus:outline-none" />
        </div>
        <select
          value={filter.tier ?? ""}
          onChange={(e) => {
            const v = e.target.value;
            set({ tier: v ? (/^\d+$/.test(v) ? Number(v) : v) : undefined });
          }}
          className={selCls}
        >
          <option value="">All tiers</option>
          <option value="3">Tier 3</option>
          <option value="2">Tier 2</option>
          <option value="1">Tier 1</option>
          <option value="Glyph">Glyph</option>
        </select>
        <select value={filter.efficiency ?? ""} onChange={(e) => set({ efficiency: e.target.value || undefined })} className={selCls}>
          <option value="">All ratings</option>
          {EFFICIENCY.map((e) => <option key={e.key} value={e.key}>{e.text}</option>)}
        </select>
        <select value={filter.tag ?? ""} onChange={(e) => set({ tag: e.target.value || undefined })} className={selCls}>
          <option value="">All tags</option>
          {tags.map((t) => <option key={t} value={t}>{t}</option>)}
        </select>
        <select value={filter.stat ?? ""} onChange={(e) => set({ stat: e.target.value || undefined })} className={selCls}>
          <option value="">Any stat</option>
          {stats.map((s) => <option key={s} value={s}>{s}</option>)}
        </select>
        <select value={sort} onChange={(e) => setSort(e.target.value as SortKey)} className={selCls}>
          <option value="name">Name</option>
          <option value="cost-asc">Cost ↑</option>
          <option value="cost-desc">Cost ↓</option>
          <option value="efficiency">Rating</option>
        </select>
        <span className="ml-auto font-mono text-[11px] text-faint">{shown.length} items</span>
      </div>
      <div className={gridCls}>
        {shown.map((it) => (
          <ItemCard key={it.name} item={it} onClick={() => navigate(toHash.item(it.name))} />
        ))}
      </div>
    </div>
  );
}
