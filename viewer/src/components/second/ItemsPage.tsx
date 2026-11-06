/** Items (`#/items`, `#/items/<Item>`): is this item worth its gold?
 *
 * A ledger of rows, not a shelf of cards. Each row says the verdict in a word
 * and then the arithmetic behind it, decomposed: `2,500g · worth 2,241g ·
 * +259g` — what it costs, what its stats are worth at the fitted prices, and
 * the difference. Opening a row shows the receipt: every stat at its price,
 * summed to the worth, and the worth against the cost, closing exactly
 * (receipt.ts).
 *
 * Product truth kept from the old ItemsShop (its comments carry the evidence):
 *  - The verdict WORD comes from the pipeline's own bucket (`priceVerdict`),
 *    so a row can never read "Fair" while the Overpriced filter selected it.
 *  - The order is the continuous residual (`sortItems` "value"), not the
 *    bucket, so the most underpriced item in the game is findable; items only
 *    one god can buy sink with their own kind and say whose they are.
 *  - Unscored is said in words. A tier-1 starter is not priced on purpose and
 *    the receipt says why; it never prints a dash where a verdict would be.
 *  - Filters are derived from the data (tiers, verdicts, tags, stats actually
 *    present), live in the hash query, and survive opening an item.
 *  - Components (tier 1–2 path steps) show only once a tier is chosen.
 */
import { useMemo, useState, type MouseEvent } from "react";
import type { Item, ItemTierEntry } from "../../types";
import {
  filterItems, sortItems, tierLabel, tiersPresent, isComponent, EFFICIENCY,
  type ItemFilter, type SortKey,
} from "../../lib/itemFilters";
import { priceVerdict, PRICE_WORD } from "../../lib/verdictWords";
import { useUrlState, keepQuery } from "../../lib/urlState";
import { navigate, toHash } from "../../lib/useHashRoute";
import { Art, CloseGlyph, SearchGlyph } from "./art";
import { Sheet } from "./Sheet";
import { useWide } from "./useWide";
import { Em, PageHead, Seam } from "./PageParts";
import { buildReceipt, gold, signedGold } from "./receipt";

type Shelf = ItemFilter & { sort: SortKey };
const SORTS: { key: SortKey; label: string }[] = [
  { key: "value", label: "Best value first" },
  { key: "name", label: "Name, A to Z" },
  { key: "cost-asc", label: "Cheapest first" },
  { key: "cost-desc", label: "Dearest first" },
];

const decode = (p: URLSearchParams): Shelf => {
  const tier = p.get("tier");
  const sort = p.get("sort") as SortKey | null;
  return {
    q: p.get("q") ?? undefined,
    tier: tier == null ? undefined : /^\d+$/.test(tier) ? Number(tier) : tier,
    efficiency: p.get("eff") ?? undefined,
    tag: p.get("tag") ?? undefined,
    stat: p.get("stat") ?? undefined,
    sort: sort && SORTS.some((s) => s.key === sort) ? sort : "value",
  };
};
const encode = (s: Shelf) => ({
  q: s.q?.trim() || undefined,
  tier: s.tier == null ? undefined : String(s.tier),
  eff: s.efficiency,
  tag: s.tag,
  stat: s.stat,
  sort: s.sort === "value" ? undefined : s.sort,
});

/** The bucket's word. The pipeline's keys are `undervalued`/`premium`; the
 *  page says what they mean about a price. */
const BUCKET_WORD: Record<string, string> = {
  undervalued: PRICE_WORD.underpriced, fair: PRICE_WORD.fair, premium: PRICE_WORD.overpriced, untiered: "Not priced",
};

/** A gold figure in the caption face. `.font-cond` uppercases everything,
 *  and "2,500G" reads as a different unit, so the g stays lower case. */
const Fig = ({ text }: { text: string }) => <>{text.slice(0, -1)}<span className="normal-case">g</span></>;

/** Opening an item keeps the filters that produced the row, so closing the
 *  receipt comes back to the same list. Read at click time, not render. */
const openKeeping = (name: string) => (e: MouseEvent) => {
  if (e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
  e.preventDefault();
  navigate(keepQuery(toHash.item(name)));
};

const verdictOf = (it: Item) => (it.efficiency ? PRICE_WORD[priceVerdict(it.efficiency_tier, it.efficiency.residual)] : "Not priced");

/* ── A row ────────────────────────────────────────────────────────────── */
function ItemLine({ item, wide }: { item: Item; wide: boolean }) {
  const eff = item.efficiency;
  const verdict = verdictOf(item);
  const win = item.meta ? `${Math.round(item.meta.win_avg * 100)}%` : null;
  const games = typeof item.meta?.matches === "number" ? `${item.meta.matches.toLocaleString("en-US")} games` : null;
  const spoken = eff
    ? `${item.name}${item.god ? `, ${item.god} only` : ""}: ${verdict}. Costs ${gold(item.cost)}, worth ${gold(eff.predicted_cost)}, ${signedGold(eff.residual)}`
    : `${item.name}${item.god ? `, ${item.god} only` : ""}: not priced by the gold model. Costs ${gold(item.cost)}`;
  return (
    <li className="border-b border-line">
      <a href={toHash.item(item.name)} onClick={openKeeping(item.name)} aria-label={spoken} data-testid="item-line"
        className={`press grid min-h-14 items-center gap-3 py-2 pr-1 hover:bg-surface ${wide
          ? "grid-cols-[40px_minmax(0,1fr)_128px_84px_84px_84px_96px]"
          : "grid-cols-[40px_minmax(0,1fr)_auto]"}`}>
        <Art name={item.name} kind="item" className="h-10 w-10 rounded-[8px]" />
        <span className="min-w-0">
          <span className="block font-cond text-[20px] font-bold leading-none text-ink [overflow-wrap:anywhere]">{item.name}</span>
          <span className="mt-0.5 block text-cap text-muted">
            {wide ? (
              <>{tierLabel(item.tier)}{item.god && <span className="text-ink-soft"> · {item.god} only</span>}</>
            ) : (
              <>
                <span className={`block text-note ${eff ? "font-semibold text-ink" : "text-quiet"}`}>
                  {verdict}{item.god && <span className="font-normal text-ink-soft"> · {item.god} only</span>}
                </span>
                {eff
                  ? <span className="num block">{gold(item.cost)} · worth {gold(eff.predicted_cost)} · <span className="text-ink">{signedGold(eff.residual)}</span></span>
                  : <span className="num block">{gold(item.cost)}</span>}
              </>
            )}
          </span>
        </span>
        {wide && (
          <>
            <span className={`text-note ${eff ? "font-semibold text-ink" : "text-quiet"}`}>{verdict}</span>
            <span className="num text-right font-cond text-[19px] font-bold text-muted"><Fig text={gold(item.cost)} /></span>
            <span className="num text-right font-cond text-[19px] font-bold text-muted">{eff ? <Fig text={gold(eff.predicted_cost)} /> : "—"}</span>
            <span className="num text-right font-cond text-[19px] font-bold text-ink">{eff ? <Fig text={signedGold(eff.residual)} /> : "—"}</span>
          </>
        )}
        <span className="text-right">
          {win ? (
            <>
              <span className="num block font-cond text-[19px] font-bold leading-none text-ink-soft">{win}<span className="sr-only"> win rate</span></span>
              <span className="num mt-1 block text-cap text-quiet">{games ?? (item.meta?.gods != null ? `${item.meta.gods} gods` : "")}</span>
            </>
          ) : (
            <span className="text-cap text-quiet">No record</span>
          )}
        </span>
      </a>
    </li>
  );
}

/* ── Filters ──────────────────────────────────────────────────────────── */
function Choice({ on, label, count, onClick }: { on: boolean; label: string; count?: number; onClick: () => void }) {
  return (
    <button type="button" aria-pressed={on} onClick={onClick}
      className={`press flex h-11 w-full items-center gap-2.5 text-left text-copy ${on ? "font-semibold text-ink" : "text-muted hover:text-ink"}`}>
      <span aria-hidden="true" className={`flex h-[18px] w-[18px] flex-none items-center justify-center rounded-[5px] border ${on ? "border-accent bg-accent text-accent-ink" : "border-quiet"}`}>
        {on && <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><path d="m5 12 5 5 9-10" /></svg>}
      </span>
      <span className="min-w-0 flex-1">{label}</span>
      {count != null && <span className="num text-cap text-quiet">{count}</span>}
    </button>
  );
}

const selectCls = "h-11 w-full rounded-[10px] border border-line bg-surface px-3 text-copy text-ink focus:border-accent";

function Filters({ shelf, set, items, pool }: {
  shelf: Shelf; set: (p: Partial<Shelf>) => void; items: Item[]; pool: Item[];
}) {
  const tiers = useMemo(() => tiersPresent(items), [items]);
  const tags = useMemo(() => [...new Set(items.flatMap((i) => i.effect_tags ?? []))].sort(), [items]);
  const stats = useMemo(() => [...new Set(items.flatMap((i) => Object.keys(i.stats ?? {})))].sort(), [items]);
  // Only verdicts the data actually holds, each with how many it would show.
  const verdicts = EFFICIENCY.map((e) => ({
    key: e.key, label: BUCKET_WORD[e.key] ?? e.text,
    count: pool.filter((i) => (i.efficiency_tier ?? "untiered") === e.key).length,
  })).filter((v) => v.count > 0 || shelf.efficiency === v.key);
  const head = "font-cond text-[16px] font-bold uppercase text-muted";
  return (
    <div className="flex flex-col gap-5">
      <div role="group" aria-label="Verdict">
        <h2 className={head}>Verdict</h2>
        {verdicts.map((v) => (
          <Choice key={v.key} on={shelf.efficiency === v.key} label={v.label} count={v.count}
            onClick={() => set({ efficiency: shelf.efficiency === v.key ? undefined : v.key })} />
        ))}
      </div>
      <div role="group" aria-label="Item tier">
        <h2 className={head}>Tier</h2>
        <div className="grid grid-cols-2 gap-x-3">
          {tiers.map((t) => (
            <Choice key={String(t)} on={shelf.tier === t} label={tierLabel(t)}
              onClick={() => set({ tier: shelf.tier === t ? undefined : t })} />
          ))}
        </div>
        <p className="mt-1 text-cap text-quiet">Components show once a tier is chosen.</p>
      </div>
      <label className="block">
        <span className={head}>Effect</span>
        <select value={shelf.tag ?? ""} onChange={(e) => set({ tag: e.target.value || undefined })}
          aria-label="Filter by effect" className={`mt-1.5 ${selectCls}`}>
          <option value="">Any effect</option>
          {tags.map((t) => <option key={t} value={t}>{t}</option>)}
        </select>
      </label>
      <label className="block">
        <span className={head}>Stat</span>
        <select value={shelf.stat ?? ""} onChange={(e) => set({ stat: e.target.value || undefined })}
          aria-label="Filter by stat" className={`mt-1.5 ${selectCls}`}>
          <option value="">Any stat</option>
          {stats.map((s) => <option key={s} value={s}>{s}</option>)}
        </select>
      </label>
      <label className="block">
        <span className={head}>Order</span>
        <select value={shelf.sort} onChange={(e) => set({ sort: e.target.value as SortKey })}
          aria-label="Sort items" className={`mt-1.5 ${selectCls}`}>
          {SORTS.map((s) => <option key={s.key} value={s.key}>{s.label}</option>)}
        </select>
      </label>
    </div>
  );
}

/* ── The receipt ──────────────────────────────────────────────────────── */
function ItemDetail({ item, byName, goldValues, record, onClose }: {
  item: Item; byName: Map<string, Item>; goldValues: Record<string, number>; record?: ItemTierEntry; onClose: () => void;
}) {
  const r = useMemo(() => buildReceipt(item, goldValues), [item, goldValues]);
  const verdict = verdictOf(item);
  const statsOnlyBase = r && r.lines.length === 1;
  const link = (names: string[]) => {
    const unique = [...new Set(names)];
    return { known: unique.filter((n) => byName.has(n)), missing: unique.filter((n) => !byName.has(n)).length };
  };
  const from = link(item.builds_from ?? []);
  const into = link(item.builds_into ?? []);
  const sub = "font-cond text-[20px] font-extrabold text-ink";

  return (
    <Sheet title={item.name} onClose={onClose} testId="item-sheet" wide>
      <div className="flex items-center gap-3">
        <Art name={item.name} kind="item" eager className="h-12 w-12 rounded-[10px]" />
        <p className="text-note text-muted">
          <span className="num font-cond text-[19px] font-bold text-ink"><Fig text={gold(item.cost)} /></span>
          <span className="text-quiet"> · </span>{tierLabel(item.tier)}
          {item.god && <span className="block text-ink-soft">Only {item.god} can buy this — it takes one of the six.</span>}
        </p>
      </div>

      <section aria-labelledby="receipt-h" className="mt-4" data-testid="receipt">
        <h3 id="receipt-h" className={sub}>{r?.passive ? "What its stats and passive are worth" : "What its stats are worth"}</h3>
        {r ? (
          <>
            <p className="mt-1 text-say text-muted">
              <Em>{verdict}.</Em>{" "}
              <span className="num">{gold(r.cost)} · worth {gold(r.worth)} · <Em>{signedGold(r.gap)}</Em></span>
            </p>
            {statsOnlyBase && (
              <p className="mt-2 text-copy text-muted">
                It carries no stat the fit prices, so it is worth the base every item starts from, and the
                remaining {signedGold(r.gap)} is the price of its passive.
              </p>
            )}
            <table className="mt-3 w-full text-note">
              <caption className="sr-only">Stat by stat, at the fitted gold prices</caption>
              <tbody>
                {r.lines.map((l) => (
                  <tr key={l.label} className="border-t border-line align-baseline">
                    <th scope="row" className="py-2 pr-3 text-left font-normal">
                      <span className="block text-copy text-ink-soft">{l.label}</span>
                      {l.detail && <span className="num block text-cap text-quiet">{l.detail}</span>}
                    </th>
                    <td className="num py-2 text-right font-cond text-[19px] font-bold text-ink-soft"><Fig text={gold(l.gold)} /></td>
                  </tr>
                ))}
                <tr className="border-t-2 border-line-strong align-baseline">
                  <th scope="row" className="py-2 text-left text-copy font-semibold text-ink">Worth</th>
                  <td className="num py-2 text-right font-cond text-[21px] font-extrabold text-ink"><Fig text={gold(r.worth)} /></td>
                </tr>
                <tr className="align-baseline">
                  <th scope="row" className="py-1 text-left text-copy font-normal text-muted">Costs</th>
                  <td className="num py-1 text-right font-cond text-[21px] font-bold text-muted"><Fig text={gold(r.cost)} /></td>
                </tr>
                <tr className="border-t border-line align-baseline">
                  <th scope="row" className="py-2 text-left text-copy font-semibold text-ink">
                    {r.gap > 0 ? `Costs more than ${r.passive ? "it is worth" : "its stats"}` : r.gap < 0 ? `Costs less than ${r.passive ? "it is worth" : "its stats"}` : "Priced exactly"}
                  </th>
                  <td className="num py-2 text-right font-cond text-[21px] font-extrabold text-ink"><Fig text={signedGold(r.gap)} /></td>
                </tr>
              </tbody>
            </table>
            {r.unpriced.length > 0 && (
              <p className="mt-2 text-note text-muted">
                {r.unpriced.join(", ")} — not priced by the fit, so {r.unpriced.length === 1 ? "it isn't" : "they aren't"} counted above.
              </p>
            )}
            <p className="mt-2 text-note text-quiet">
              {r.passive
                ? "Stats, plus the part of its passive the fit can price — the Passive rows. Anything else the passive does is not counted: that judgement is yours, and this is the number to make it against."
                : "Stats only. A passive can be worth paying over the odds for — that judgement is yours, and this is the number to make it against."}
            </p>
          </>
        ) : (
          <p className="mt-1 text-copy text-muted" data-testid="not-scored">
            <Em>Not priced by the model.</Em>{" "}
            {item.tier === 1
              ? "Tier-1 starters buy an ability rather than stats, so they sit out the gold fit on purpose — pricing them against their token stats would skew every other item's verdict."
              : "This item has no usable stats or cost to price, so it has no verdict rather than a made-up one."}
          </p>
        )}
      </section>

      <section aria-labelledby="record-h" className="mt-5">
        <h3 id="record-h" className={sub}>How it does</h3>
        {item.meta || (record && record.score != null) ? (
          <p className="mt-1 text-copy text-muted">
            {item.meta && <><Em>{Math.round(item.meta.win_avg * 100)}%</Em> win rate{typeof item.meta.matches === "number"
              ? <> over <Em>{item.meta.matches.toLocaleString("en-US")}</Em> Conquest games</>
              : typeof item.meta.gods === "number" ? <> across {item.meta.gods} gods&rsquo; builds</> : null}. </>}
            {record?.tier_score && <>Tier <Em>{record.tier_score}</Em> among items. </>}
            A separate question from the price: an item can be dear and still win.
          </p>
        ) : (
          <p className="mt-1 text-copy text-muted">No community record for this item — not measured, which is not the same as losing.</p>
        )}
      </section>

      {Object.keys(item.stats ?? {}).length > 0 && (
        <section aria-labelledby="stats-h" className="mt-5">
          <h3 id="stats-h" className={sub}>Stats</h3>
          <dl className="mt-1">
            {Object.entries(item.stats).map(([k, v]) => (
              <div key={k} className="flex justify-between border-t border-line py-1.5 text-copy">
                <dt className="text-muted">{k}</dt><dd className="num font-semibold text-ink">{v}</dd>
              </div>
            ))}
          </dl>
        </section>
      )}

      {item.passive && (
        <section aria-labelledby="passive-h" className="mt-5">
          <h3 id="passive-h" className={sub}>Passive</h3>
          <p className="mt-1 max-w-[62ch] text-copy text-ink-soft">{item.passive}</p>
          {item.passive_uncatalogued && (
            <p className="mt-1.5 text-note text-muted">New item, passive not yet catalogued — valued on its stats alone.</p>
          )}
          {(item.effect_tags?.length ?? 0) > 0 && (
            <p className="mt-1.5 text-note text-quiet">Read as: {item.effect_tags!.join(", ")}</p>
          )}
        </section>
      )}

      {(from.known.length > 0 || from.missing > 0 || into.known.length > 0) && (
        <section aria-labelledby="tree-h" className="mt-5">
          <h3 id="tree-h" className={sub}>Builds from and into</h3>
          <ul className="mt-1">
            {from.known.map((n) => (
              <li key={`f-${n}`} className="border-t border-line">
                <a href={toHash.item(n)} onClick={openKeeping(n)} className="press flex min-h-11 items-center gap-2.5 text-copy text-ink-soft hover:text-ink">
                  <Art name={n} kind="item" className="h-7 w-7 rounded-[6px]" />
                  <span className="min-w-0 flex-1">{n}</span><span className="text-cap text-quiet">from</span>
                </a>
              </li>
            ))}
            {into.known.map((n) => (
              <li key={`i-${n}`} className="border-t border-line">
                <a href={toHash.item(n)} onClick={openKeeping(n)} className="press flex min-h-11 items-center gap-2.5 text-copy text-ink-soft hover:text-ink">
                  <Art name={n} kind="item" className="h-7 w-7 rounded-[6px]" />
                  <span className="min-w-0 flex-1">{n}</span><span className="text-cap text-quiet">into</span>
                </a>
              </li>
            ))}
          </ul>
          {from.missing > 0 && (
            <p className="mt-1 text-cap text-quiet">{from.missing} component{from.missing === 1 ? "" : "s"} not in this index.</p>
          )}
        </section>
      )}

      {item.source_url && (
        <p className="mt-4">
          <a href={item.source_url} target="_blank" rel="noreferrer"
            className="press inline-flex min-h-11 items-center text-note font-semibold text-blue hover:underline">
            Wiki page for {item.name}
          </a>
        </p>
      )}
    </Sheet>
  );
}

/* ── The page ─────────────────────────────────────────────────────────── */
export function ItemsPage({ items, openItem, tierItems = [], goldValues = {} }: {
  items: Item[];
  openItem?: string;
  tierItems?: ItemTierEntry[];
  goldValues?: Record<string, number>;
}) {
  const [shelf, setShelf] = useUrlState(decode, encode);
  const set = (p: Partial<Shelf>) => setShelf((s) => ({ ...s, ...p }));
  const wide = useWide();
  const [filtersOpen, setFiltersOpen] = useState(false);

  const byName = useMemo(() => new Map(items.map((i) => [i.name, i])), [items]);
  const records = useMemo(() => new Map(tierItems.map((i) => [i.name, i])), [tierItems]);
  const pool = useMemo(() => (shelf.tier === undefined ? items.filter((i) => !isComponent(i)) : items), [items, shelf.tier]);
  const shown = useMemo(() => sortItems(filterItems(pool, shelf), shelf.sort), [pool, shelf]);

  // The claim counts what it says: buyable by every god, and Underpriced by
  // the pipeline's bucket. Never the raw residual: a residual of -40g is noise
  // the bucket calls "Fairly priced", and counting it made the claim (84)
  // disagree with the Underpriced filter (13) on the same screen.
  const priceable = useMemo(() => items.filter((i) => i.efficiency && i.efficiency.comparable !== false), [items]);
  const under = priceable.filter((i) => priceVerdict(i.efficiency_tier, i.efficiency!.residual) === "underpriced").length;
  const withRecord = items.filter((i) => i.meta).length;
  const unscored = items.filter((i) => !i.efficiency).length;

  const open = openItem ? byName.get(openItem) : undefined;
  const notFound = !!openItem && !open;
  const active = [shelf.efficiency, shelf.tier, shelf.tag, shelf.stat].filter((v) => v != null && v !== "").length;
  const anyFilter = active > 0 || !!shelf.q?.trim();
  const clear = () => setShelf((s) => ({ sort: s.sort }));

  const filters = <Filters shelf={shelf} set={set} items={items} pool={pool} />;

  return (
    <div className="mx-auto w-full max-w-[1240px] px-4 pb-12 lg:px-6">
      <PageHead title="Items" testId="items-head">
        <p data-testid="items-claim"><Em>{under} of {priceable.length}</Em> items are underpriced: they cost clearly less than their stats are worth.</p>
      </PageHead>
      <p className="mt-2 max-w-[62ch] text-note text-muted lg:text-copy">
        A regression prices every stat in gold, then sets what an item should cost against what it does. That says
        whether an item is cheap for what it gives &mdash; not whether it wins, which is the separate number on the right.
      </p>
      <p className="mt-2 text-cap text-quiet" data-testid="items-coverage">
        {withRecord} of {items.length} have a community record
        {unscored > 0 && <> · {unscored} not priced: tier-1 starters and items with no stats to price</>}.
      </p>
      <div className="mt-1"><Seam href={toHash.method()} testId="method-seam">How every stat gets its gold price</Seam></div>

      <div className={`mt-5 ${wide ? "grid grid-cols-[232px_minmax(0,1fr)] gap-10" : ""}`}>
        {wide && <aside aria-label="Filters" className="sticky top-[80px] self-start">{filters}</aside>}

        <div className="min-w-0">
          <div className="flex gap-2">
            <label className="flex h-12 min-w-0 flex-1 items-center gap-2 rounded-[12px] border border-line bg-surface px-3 focus-within:border-accent">
              <SearchGlyph size={20} className="flex-none text-quiet" />
              <span className="sr-only">Search items by name, effect, stat or passive</span>
              <input type="search" value={shelf.q ?? ""} onChange={(e) => set({ q: e.target.value })}
                placeholder="Name, effect, stat…" autoComplete="off"
                className="min-w-0 flex-1 bg-transparent text-copy text-ink placeholder:text-quiet focus:outline-none focus-visible:outline-none" />
              {shelf.q && (
                <button type="button" onClick={() => set({ q: undefined })} aria-label="Clear search"
                  className="press -mr-1 flex h-10 w-10 items-center justify-center text-quiet hover:text-ink"><CloseGlyph size={18} /></button>
              )}
            </label>
            {!wide && (
              <button type="button" onClick={() => setFiltersOpen(true)} aria-haspopup="dialog"
                className="press h-12 flex-none rounded-[12px] border border-line px-4 font-cond text-[18px] font-bold uppercase text-ink hover:border-quiet">
                Filters{active > 0 && <span className="ml-1.5 text-accent">{active}</span>}
              </button>
            )}
          </div>

          <div className="mt-3 flex min-h-11 items-center justify-between gap-3">
            <p className="text-note text-muted" data-testid="items-count">
              <span className="num font-semibold text-ink">{shown.length}</span> of {items.length} items
              <span className="text-quiet"> · {SORTS.find((s) => s.key === shelf.sort)?.label.toLowerCase()}</span>
            </p>
            {anyFilter && (
              <button type="button" onClick={clear} className="press h-11 px-1 text-note font-semibold text-muted hover:text-ink">Clear all</button>
            )}
          </div>
          <p className="sr-only" aria-live="polite">{shown.length} items match</p>

          {notFound && (
            <p className="mb-3 max-w-[62ch] text-copy text-muted">
              No item called &ldquo;{openItem}&rdquo; in this index. It may have been renamed or removed since that link was made.
            </p>
          )}

          {wide && shown.length > 0 && (
            <div aria-hidden="true" className="grid grid-cols-[40px_minmax(0,1fr)_128px_84px_84px_84px_96px] gap-3 border-b border-line-strong pb-1.5 pr-1 text-cap text-quiet">
              <span /><span>Item</span><span>Verdict</span><span className="text-right">Costs</span>
              <span className="text-right">Worth</span><span className="text-right">Gap</span><span className="text-right">Wins</span>
            </div>
          )}
          {shown.length === 0 ? (
            <div className="py-10">
              <p className="max-w-[62ch] text-copy text-muted">
                {shelf.q?.trim()
                  ? <>No item matches &ldquo;{shelf.q.trim()}&rdquo;{active > 0 ? " with the filters you have on" : ""}.</>
                  : "No item matches those filters."}
              </p>
              <button type="button" onClick={clear}
                className="press mt-3 h-11 rounded-[10px] border border-line px-4 text-note font-semibold text-muted hover:text-ink">Clear filters</button>
            </div>
          ) : (
            <ul data-testid="item-list">
              {shown.map((it) => <ItemLine key={it.name} item={it} wide={wide} />)}
            </ul>
          )}
        </div>
      </div>

      {filtersOpen && !wide && (
        <Sheet title="Filters" onClose={() => setFiltersOpen(false)} testId="filter-sheet"
          footer={
            <button type="button" onClick={() => setFiltersOpen(false)}
              className="press h-11 w-full rounded-[10px] bg-accent font-cond text-[18px] font-bold uppercase text-accent-ink">
              Show {shown.length} items
            </button>
          }>
          {filters}
        </Sheet>
      )}

      {open && (
        <ItemDetail item={open} byName={byName} goldValues={goldValues} record={records.get(open.name)}
          onClose={() => navigate(keepQuery(toHash.items()))} />
      )}
    </div>
  );
}
