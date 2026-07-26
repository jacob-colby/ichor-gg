/* THESIS: this surface owns one question — is this item worth its gold? It
 * answers with the model's arithmetic, not an adjective. It refuses the
 * three-bucket chip it shipped for a year: `Fair` on 80 of 159 items, with the
 * residual computed by the regression and discarded at the pipeline boundary.
 * OWN-WORLD: Arena Night. Hairline rule-work, mono micro-labels, gold reserved
 * for selection and the model's own signal; `under`/`premium` carry direction —
 * this is where that pair originated.
 * STORY: a player scans a shelf, sees which items are priced under what their
 * stats are worth, opens one, and reads the receipt: every stat at its fitted
 * gold price, summed against what the item actually costs.
 * FIRST VIEWPORT: a claim carrying its live count, a sticky filter bar, then
 * the shelf — each card showing cost, fair price and the gap.
 * FORM: enriched shelf, position 6 of the ordered list, seed key 962f880f.
 * The shelf survives because `ItemCard` is shared with ItemPickerModal; a
 * row-based ledger would have split that one good piece of reuse in two.
 */
import { useEffect, useMemo, useRef, useState } from "react";
import type { Item, ItemTierEntry } from "../types";
import {
  filterItems, sortItems, efficiencyLabel, tierLabel, tiersPresent,
  residualText, statValueLines, basePrice, EFFICIENCY,
  type SortKey, type ItemFilter,
} from "../lib/itemFilters";
import { iconSlug } from "../lib/builds";
import { toHash, navigate } from "../lib/useHashRoute";

const eyebrow = "font-mono text-[10.5px] uppercase tracking-[0.1em] text-faint";

export function ItemIcon({ name, size = "h-8 w-8" }: { name: string; size?: string }) {
  const [tries, setTries] = useState(0);
  if (tries > 1) {
    return (
      <span aria-hidden="true"
        className={`${size} flex flex-none items-center justify-center rounded-sm bg-bg3 font-display text-[11px] font-bold text-faint`}>
        {name.slice(0, 1)}
      </span>
    );
  }
  return (
    <img
      src={`/icons/${iconSlug(name)}.png${tries ? "?r=1" : ""}`}
      alt="" loading="lazy" onError={() => setTries((t) => t + 1)}
      className={`${size} flex-none rounded-sm bg-bg2 object-cover`}
    />
  );
}

function EffBadge({ tier }: { tier: string | null | undefined }) {
  const e = efficiencyLabel(tier);
  return (
    <span className={`rounded-sm px-1.5 py-0.5 font-mono text-[9.5px] uppercase tracking-[0.06em] ${e.cls}`}>
      {e.text}
    </span>
  );
}

function residualClass(residual: number): string {
  if (residual < 0) return "text-under";
  if (residual > 0) return "text-premium";
  return "text-faint";
}

/** How far this item's price sits from what its stats are worth, drawn from a
 * centre line — the same vocabulary Home uses for model-vs-meta divergence. */
function ResidualBar({ residual, scale }: { residual: number; scale: number }) {
  const pct = scale > 0 ? Math.min(100, Math.round((Math.abs(residual) / scale) * 100)) : 0;
  const under = residual < 0;
  return (
    <span aria-hidden="true" className="relative block h-[3px] w-full bg-bg3">
      <span className="absolute inset-y-[-2px] left-1/2 w-px -translate-x-1/2 bg-line-strong" />
      {/* under to the right, premium to the left — the same direction Home
          draws divergence. This ran backwards while claiming otherwise. */}
      <span
        className={`bar-grow absolute top-0 h-full ${under ? "left-1/2 origin-left bg-under" : "right-1/2 origin-right bg-premium"}`}
        style={{ width: `${pct / 2}%` }}
      />
    </span>
  );
}

/** Shared card language for the shop grid and the ItemPickerModal grid. */
export function ItemCard({ item, onClick, scale = 1000 }: {
  item: Item;
  onClick: () => void;
  /** Largest absolute residual on the board, for bar scaling. */
  scale?: number;
}) {
  const eff = item.efficiency;
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label={`${item.name}, ${item.cost} gold${
        eff ? `, fair price ${eff.predicted_cost} gold, ${
          eff.residual < 0 ? `${Math.abs(eff.residual)} under` : eff.residual > 0 ? `${eff.residual} over` : "exactly fair"}`
        : ", not scored by the gold model"}`}
      className="press flex flex-col gap-1.5 rounded-md border border-line-strong bg-bg2 p-2 text-left transition-colors duration-[180ms] ease-standard hover:border-blue/50"
    >
      <span className="flex items-center gap-2">
        <ItemIcon name={item.name} />
        <span className="min-w-0 flex-1">
          <span className="block truncate text-[13px] text-ink" title={item.name}>{item.name}</span>
          <span className="block font-mono text-[10px] text-faint">
            <span className="text-ink-soft">{item.cost}g</span> · {tierLabel(item.tier)}
          </span>
        </span>
      </span>

      {/* The verdict, decomposed. A three-value chip could say "Premium" but
          never by how much — which is the number that decides a purchase. */}
      {eff ? (
        <span className="flex flex-col gap-1">
          <ResidualBar residual={eff.residual} scale={scale} />
          <span className="flex items-baseline justify-between gap-2 font-mono text-[9.5px]">
            <span className="text-faint">fair {eff.predicted_cost}g</span>
            <span className={residualClass(eff.residual)}>{residualText(eff.residual)}</span>
          </span>
        </span>
      ) : (
        <span className="font-mono text-[9.5px] text-faint">not priced by the model</span>
      )}

      <span className="flex items-center justify-between gap-1">
        <EffBadge tier={item.efficiency_tier} />
        {item.meta
          ? <span className="font-mono text-[9.5px] text-muted">{Math.round(item.meta.win_avg * 100)}% win · {item.meta.gods}</span>
          : <span className="font-mono text-[9.5px] text-faint">no community data</span>}
      </span>

      {(item.effect_tags?.length ?? 0) > 0 && (
        <span className="truncate font-mono text-[9.5px] text-faint">{item.effect_tags!.join(" · ")}</span>
      )}
    </button>
  );
}

/* ── The receipt ──────────────────────────────────────────────────────────
 * A real dialog, not a panel injected above the grid — clicking a card mid-
 * scroll used to insert the detail 4000px above the viewport, so the surface's
 * only interaction produced nothing visible.
 */
function ItemDetail({ item, byName, goldValues, community, onClose }: {
  item: Item;
  byName: Map<string, Item>;
  goldValues: Record<string, number>;
  community?: ItemTierEntry;
  onClose: () => void;
}) {
  const panelRef = useRef<HTMLDivElement>(null);
  const headingRef = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
    const opener = document.activeElement as HTMLElement | null;
    headingRef.current?.focus();
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") { e.stopPropagation(); onClose(); return; }
      if (e.key !== "Tab") return;
      const f = panelRef.current?.querySelectorAll<HTMLElement>(
        'a[href], button:not([disabled]), input, [tabindex]:not([tabindex="-1"])');
      if (!f || f.length === 0) return;
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    };
    document.addEventListener("keydown", onKeyDown, true);
    return () => { document.removeEventListener("keydown", onKeyDown, true); opener?.focus?.(); };
  }, [onClose]);

  const lines = useMemo(() => statValueLines(item, goldValues), [item, goldValues]);
  const eff = item.efficiency;
  const priced = lines.filter((l) => l.subtotal != null);
  const base = basePrice(goldValues);
  const unpriced = lines.filter((l) => l.subtotal == null);

  // Components the index doesn't carry — 127 of 159 items reference at least
  // one. Counted and stated rather than silently dropped.
  const links = (names: string[]) => {
    const unique = [...new Set(names)];
    const known = unique.filter((n) => byName.has(n));
    const missing = unique.length - known.length;
    return { known, missing };
  };
  const from = links(item.builds_from ?? []);
  const into = links(item.builds_into ?? []);

  const chip = (n: string) => (
    <a key={n} href={toHash.item(n)}
      className="press inline-flex items-center gap-1 rounded-sm border border-line bg-bg2 px-1.5 py-1 text-xs text-ink-soft hover:border-line-strong">
      <ItemIcon name={n} size="h-4 w-4" />{n}
    </a>
  );

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center overflow-y-auto bg-black/60 p-4 sm:items-center" onClick={onClose}>
      <div
        ref={panelRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby="item-detail-title"
        className="my-auto w-full max-w-xl rounded-lg border border-line bg-bg1 p-4 shadow-raised"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-start gap-3">
          <ItemIcon name={item.name} size="h-11 w-11" />
          <div className="min-w-0 flex-1">
            <h2 id="item-detail-title" ref={headingRef} tabIndex={-1}
              className="font-display text-lg font-bold leading-tight text-ink focus:outline-none">
              {item.name}
            </h2>
            <p className="mt-0.5 font-mono text-[11px] text-faint">
              <span className="text-ink-soft">{item.cost}g</span> · {tierLabel(item.tier)}
              {item.meta && <> · {Math.round(item.meta.win_avg * 100)}% win across {item.meta.gods} gods</>}
            </p>
          </div>
          <button type="button" onClick={onClose} aria-label="Close"
            className="press -mr-1 -mt-1 rounded-sm px-2 py-1 font-mono text-sm text-faint hover:text-ink">✕</button>
        </div>

        {/* ── The receipt ── */}
        <section aria-labelledby="item-value-h" className="mt-4 border-t border-line pt-3">
          <h3 id="item-value-h" className={eyebrow}>What its stats are worth</h3>
          {eff && priced.length === 0 ? (
            <p className="mt-2 max-w-[64ch] text-xs leading-relaxed text-muted">
              This item carries no stats the fit prices, so the model values it at the base rate
              every item starts from — {Math.round(base)}g — and reads the remaining{" "}
              {residualText(eff.residual)} as the price of its passive.
            </p>
          ) : eff ? (
            <>
              <table className="mt-2 w-full font-mono text-[11px]">
                <thead>
                  <tr className="text-faint">
                    <th scope="col" className="pb-1 text-left font-normal">Stat</th>
                    <th scope="col" className="pb-1 text-right font-normal">Amount</th>
                    <th scope="col" className="pb-1 text-right font-normal">Gold each</th>
                    <th scope="col" className="pb-1 text-right font-normal">Value</th>
                  </tr>
                </thead>
                <tbody>
                  {/* The fit's intercept: what every item costs before a single
                      stat is counted. Omitting it left the rows short of the
                      total by exactly this much, on every item. */}
                  <tr className="border-t border-line">
                    <td className="py-1 pr-2 text-ink-soft">Base price</td>
                    <td className="py-1 text-right text-muted">every item</td>
                    <td className="py-1 text-right text-faint">—</td>
                    <td className="py-1 text-right text-ink">{Math.round(base)}g</td>
                  </tr>
                  {priced.map((l) => (
                    <tr key={l.stat} className="border-t border-line">
                      <td className="py-1 pr-2 text-ink-soft">{l.stat}</td>
                      <td className="py-1 text-right text-muted">{l.raw}</td>
                      <td className="py-1 text-right text-faint">{l.goldPerUnit!.toFixed(2)}g</td>
                      <td className="py-1 text-right text-ink">{Math.round(l.subtotal!)}g</td>
                    </tr>
                  ))}
                  <tr className="border-t border-line-strong">
                    <td colSpan={3} className="py-1 pr-2 text-faint">Fair price</td>
                    <td className="py-1 text-right text-ink-soft">{eff.predicted_cost}g</td>
                  </tr>
                  <tr>
                    <td colSpan={3} className="py-1 pr-2 text-faint">Actual price</td>
                    <td className="py-1 text-right text-ink-soft">{item.cost}g</td>
                  </tr>
                  <tr className="border-t border-line">
                    <td colSpan={3} className="py-1 pr-2 text-faint">
                      {eff.residual < 0 ? "Priced under its stats" : eff.residual > 0 ? "Priced over its stats" : "Priced exactly"}
                    </td>
                    <td className={`py-1 text-right ${residualClass(eff.residual)}`}>{residualText(eff.residual)}</td>
                  </tr>
                </tbody>
              </table>
              {unpriced.length > 0 && (
                <p className="mt-1.5 font-mono text-[9.5px] text-faint">
                  {unpriced.map((l) => l.stat).join(", ")} — not priced by the fit, so
                  {" "}{unpriced.length === 1 ? "it isn't" : "they aren't"} counted above.
                </p>
              )}
              <p className="mt-2 max-w-[64ch] text-xs leading-relaxed text-muted">
                Stats only. A passive can be worth paying over the odds for — that judgement is
                yours, and this is the number to make it against.
              </p>
            </>
          ) : (
            <p className="mt-2 max-w-[64ch] text-xs leading-relaxed text-muted">
              Not priced by the model. {item.tier === 1
                ? "Tier-1 starters buy an ability rather than stats, so they sit out the gold fit on purpose — pricing them against their token stats would skew every other item's verdict."
                : "This item has no usable cost to regress against."}
            </p>
          )}
        </section>

        {community && (community.ours != null || community.community != null) && (
          <section aria-labelledby="item-tier-h" className="mt-4 border-t border-line pt-3">
            <h3 id="item-tier-h" className={eyebrow}>Where it lands</h3>
            <p className="mt-1.5 flex flex-wrap items-baseline gap-x-4 gap-y-1 font-mono text-[11px]">
              <span className="text-faint">model <span className="text-gold">{community.ours?.toFixed(2) ?? "—"}</span>
                {community.tier_ours && <span className="text-ink-soft"> {community.tier_ours}</span>}</span>
              <span className="text-faint">community {community.community != null
                ? <><span className="text-ink-soft">{community.community.toFixed(2)}</span>
                    {community.tier_community && <span className="text-ink-soft"> {community.tier_community}</span>}</>
                : <span className="text-muted">unranked</span>}</span>
            </p>
          </section>
        )}

        {Object.keys(item.stats ?? {}).length > 0 && (
          <section className="mt-4 border-t border-line pt-3">
            <h3 className={eyebrow}>Stats</h3>
            <ul className="mt-1.5 flex flex-col gap-0.5">
              {Object.entries(item.stats).map(([k, v]) => (
                <li key={k} className="flex justify-between text-xs">
                  <span className="text-muted">{k}</span><span className="font-mono text-ink">{v}</span>
                </li>
              ))}
            </ul>
          </section>
        )}

        {item.passive && (
          <section className="mt-4 border-t border-line pt-3">
            <h3 className={eyebrow}>Passive</h3>
            <p className="mt-1.5 max-w-[68ch] text-xs leading-relaxed text-ink-soft">{item.passive}</p>
          </section>
        )}

        {(item.effect_tags?.length ?? 0) > 0 && (
          <div className="mt-3 flex flex-wrap gap-1">
            {item.effect_tags!.map((t) => (
              <span key={t} className="rounded-sm bg-bg3 px-1.5 py-0.5 font-mono text-[9.5px] text-muted">{t}</span>
            ))}
          </div>
        )}

        {(from.known.length > 0 || from.missing > 0 || into.known.length > 0) && (
          <section className="mt-4 border-t border-line pt-3">
            {(from.known.length > 0 || from.missing > 0) && (
              <div className="flex flex-wrap items-center gap-1.5">
                <span className={eyebrow}>Builds from</span>
                {from.known.map(chip)}
                {from.missing > 0 && (
                  <span className="font-mono text-[10px] text-faint">
                    {from.missing} component{from.missing === 1 ? "" : "s"} not in this index
                  </span>
                )}
              </div>
            )}
            {into.known.length > 0 && (
              <div className="mt-2 flex flex-wrap items-center gap-1.5">
                <span className={eyebrow}>Builds into</span>
                {into.known.map(chip)}
              </div>
            )}
          </section>
        )}

        {item.source_url && (
          <a href={item.source_url} target="_blank" rel="noreferrer"
            className="press mt-4 inline-block rounded-sm py-1 font-mono text-[10px] uppercase tracking-[0.08em] text-blue hover:underline">
            Wiki page →
          </a>
        )}
      </div>
    </div>
  );
}

const segBtn = (active: boolean) =>
  `press rounded px-2.5 py-1 font-display text-xs font-semibold transition-colors duration-150 ease-standard ${
    active ? "bg-gold text-bg0" : "text-muted hover:text-ink"}`;
const selCls = "rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-xs text-muted focus:border-blue focus:outline-none";

export function ItemsShop({ items, openItem, tierItems = [], goldValues = {} }: {
  items: Item[];
  openItem?: string;
  /** The tier list's item rows, so an item can show where the community puts
   * it — the same ghost the tier list draws. */
  tierItems?: ItemTierEntry[];
  goldValues?: Record<string, number>;
}) {
  const [filter, setFilter] = useState<ItemFilter>({});
  const [sort, setSort] = useState<SortKey>("value");

  const byName = useMemo(() => new Map(items.map((i) => [i.name, i])), [items]);
  const tierByName = useMemo(() => new Map(tierItems.map((i) => [i.name, i])), [tierItems]);
  const tiers = useMemo(() => tiersPresent(items), [items]);
  const tags = useMemo(() => Array.from(new Set(items.flatMap((i) => i.effect_tags ?? []))).sort(), [items]);
  const stats = useMemo(() => Array.from(new Set(items.flatMap((i) => Object.keys(i.stats ?? {})))).sort(), [items]);
  const shown = useMemo(() => sortItems(filterItems(items, filter), sort), [items, filter, sort]);

  // Bars scale against the whole set, not the filtered view, so a filter never
  // silently rescales what a bar length means.
  const scale = useMemo(
    () => items.reduce((m, i) => Math.max(m, Math.abs(i.efficiency?.residual ?? 0)), 0) || 1,
    [items],
  );
  // Counts what the sentence says: priced below what the stats are worth.
  // Counting the `undervalued` bucket (z <= -0.5) instead put 30 in a headline
  // that 71 cards on screen visibly contradicted.
  const underpriced = useMemo(
    () => items.filter((i) => (i.efficiency?.residual ?? 0) < 0).length, [items]);
  const withCommunity = useMemo(() => items.filter((i) => i.meta).length, [items]);
  const unscored = useMemo(() => items.filter((i) => !i.efficiency).length, [items]);

  const open = openItem ? byName.get(openItem) : undefined;
  const notFound = !!openItem && !open;
  const set = (patch: Partial<ItemFilter>) => setFilter((f) => ({ ...f, ...patch }));
  const anyFilter = !!(filter.q || filter.tier != null || filter.efficiency || filter.tag || filter.stat);
  const clear = () => setFilter({});

  return (
    <div className="mx-auto w-full max-w-[1440px] p-4 sm:p-6">
      <header className="pb-4">
        <h1 className="max-w-[26ch] text-balance font-display text-[26px] font-bold leading-[1.12] tracking-[-0.01em] text-ink sm:text-[32px]">
          <span className="text-gold">{underpriced} of {items.length}</span> items cost less than their stats are worth.
        </h1>
        <p className="mt-2.5 max-w-[72ch] text-sm leading-relaxed text-ink-soft">
          A regression prices every stat in gold, then compares what an item should cost to what it
          does. Open one to see the arithmetic.
        </p>
        <p className="mt-2 flex flex-wrap items-center gap-x-3 gap-y-1 font-mono text-[10.5px] uppercase tracking-[0.09em] text-faint">
          <span>{withCommunity} of {items.length} have community data</span>
          {unscored > 0 && <span className="before:mr-3 before:content-['·']">{unscored} not priced (starters)</span>}
        </p>
      </header>

      <div className="sticky top-0 z-10 -mx-4 border-b border-line bg-bg0/95 px-4 py-3 backdrop-blur sm:-mx-6 sm:px-6">
        <div className="flex items-center gap-2 overflow-x-auto pb-0.5 sm:flex-wrap sm:overflow-visible [&>*]:shrink-0">
          {/* A label, so the 34px bordered box is the hit area rather than
              just the 20px input inside it. */}
          <label className="flex cursor-text items-center gap-2 rounded-md border border-line bg-bg2 px-3 py-1.5 focus-within:border-blue">
            <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true" className="text-muted">
              <circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" />
            </svg>
            <input
              value={filter.q ?? ""}
              onChange={(e) => set({ q: e.target.value })}
              placeholder="Name, tag, stat…"
              aria-label="Search items by name, tag, stat or passive"
              className="w-40 bg-transparent py-1 text-xs text-ink placeholder:text-muted focus:outline-none"
            />
          </label>

          <div role="group" aria-label="Value rating" className="flex items-center gap-0.5 rounded-md border border-line bg-bg1 p-1">
            <button type="button" aria-pressed={!filter.efficiency} onClick={() => set({ efficiency: undefined })} className={segBtn(!filter.efficiency)}>All</button>
            {EFFICIENCY.map((e) => (
              <button key={e.key} type="button" aria-pressed={filter.efficiency === e.key}
                onClick={() => set({ efficiency: filter.efficiency === e.key ? undefined : e.key })}
                className={segBtn(filter.efficiency === e.key)}>{e.text}</button>
            ))}
          </div>

          <div role="group" aria-label="Item tier" className="flex items-center gap-0.5 rounded-md border border-line bg-bg1 p-1">
            <button type="button" aria-pressed={filter.tier == null} onClick={() => set({ tier: undefined })} className={segBtn(filter.tier == null)}>All</button>
            {tiers.map((t) => (
              <button key={String(t)} type="button" aria-pressed={filter.tier === t}
                onClick={() => set({ tier: filter.tier === t ? undefined : t })}
                className={segBtn(filter.tier === t)}>{tierLabel(t)}</button>
            ))}
          </div>

          <select value={filter.tag ?? ""} onChange={(e) => set({ tag: e.target.value || undefined })}
            aria-label="Filter by effect tag" className={selCls}>
            <option value="">All tags</option>
            {tags.map((t) => <option key={t} value={t}>{t}</option>)}
          </select>
          <select value={filter.stat ?? ""} onChange={(e) => set({ stat: e.target.value || undefined })}
            aria-label="Filter by stat" className={selCls}>
            <option value="">Any stat</option>
            {stats.map((s) => <option key={s} value={s}>{s}</option>)}
          </select>
          <select value={sort} onChange={(e) => setSort(e.target.value as SortKey)}
            aria-label="Sort items" className={selCls}>
            <option value="value">Best value first</option>
            <option value="name">Name</option>
            <option value="cost-asc">Cost ↑</option>
            <option value="cost-desc">Cost ↓</option>
          </select>

          <span data-testid="items-count" className="ml-auto font-mono text-[10.5px] text-faint">
            {shown.length === items.length ? `${items.length} items` : `${shown.length} of ${items.length}`}
          </span>
          {anyFilter && (
            <button type="button" onClick={clear}
              className="press rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-[11px] text-muted hover:text-ink">
              Clear
            </button>
          )}
        </div>
      </div>

      <p aria-live="polite" className="sr-only">{shown.length} items match</p>

      {notFound && (
        <p className="mt-4 max-w-[64ch] text-sm leading-relaxed text-muted">
          No item called &ldquo;{openItem}&rdquo; in this index. It may have been renamed or removed
          since that link was made.
        </p>
      )}

      {shown.length === 0 ? (
        <div className="flex flex-col items-start gap-2 py-16">
          <p className="max-w-[64ch] text-sm leading-relaxed text-muted">
            No item matches {filter.q?.trim() ? <>&ldquo;{filter.q.trim()}&rdquo;</> : "those filters"}
            {filter.efficiency || filter.tier != null || filter.tag || filter.stat ? " with the filters you have on" : ""}.
          </p>
          <button type="button" onClick={clear} className="press rounded-sm px-1 py-1 text-xs text-blue hover:underline">
            Clear filters
          </button>
        </div>
      ) : (
        <ul className="mt-4 grid grid-cols-[repeat(auto-fill,minmax(150px,1fr))] gap-2 sm:grid-cols-[repeat(auto-fill,minmax(172px,1fr))]">
          {shown.map((it) => (
            <li key={it.name}>
              <ItemCard item={it} scale={scale} onClick={() => navigate(toHash.item(it.name))} />
            </li>
          ))}
        </ul>
      )}

      {open && (
        <ItemDetail
          item={open}
          byName={byName}
          goldValues={goldValues}
          community={tierByName.get(open.name)}
          onClose={() => navigate(toHash.items())}
        />
      )}
    </div>
  );
}
