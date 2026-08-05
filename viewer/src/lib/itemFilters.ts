import type { Item } from "../types";

export interface ItemFilter {
  q?: string;
  tier?: number | string;
  efficiency?: string; // "undervalued" | "fair" | "premium" | "untiered"
  tag?: string;
  stat?: string;
}

/** Numeric tiers render as "T3"; non-numeric labels (e.g. Relic, whose wiki
 * "Item Type" row carries no tier number) render bare. */
export function tierLabel(tier: number | string): string {
  return typeof tier === "number" ? `T${tier}` : String(tier);
}

/** Every tier actually present, numerics descending then named ones.
 *
 * Derived rather than hardcoded: the filter used to offer a `Glyph` option
 * matching zero items while the one Relic in the set was unreachable.
 */
/** A purchase-path step rather than something you set out to buy.
 *
 *  Tier 1 and 2, with one exception that matters: a tier-1 item carrying a
 *  PASSIVE is a starter — Bumba's Cudgel, Gilded Arrow, Death's Toll — and
 *  those are things a player shops for deliberately. The twelve tier-1 items
 *  with no passive (Axe, Bow, Ring, Shield) are the actual path steps.
 *  Non-numeric tiers (Relic/Glyph) are finished items. */
export function isComponent(item: Item): boolean {
  if (typeof item.tier !== "number" || item.tier >= 3) return false;
  return !(item.tier === 1 && (item.passive ?? "").trim());
}

export function tiersPresent(items: Item[]): (number | string)[] {
  const seen = [...new Set(items.map((i) => i.tier))];
  const nums = seen.filter((t): t is number => typeof t === "number").sort((a, b) => b - a);
  const named = seen.filter((t): t is string => typeof t !== "number").sort();
  return [...nums, ...named];
}

export function filterItems(items: Item[], f: ItemFilter): Item[] {
  const q = f.q?.trim().toLowerCase();
  return items.filter((it) => {
    if (q) {
      // Name, tags, stat names and the passive — searching "anti-heal" used to
      // return nothing while a tag filter for it sat two controls away.
      const haystack = [
        it.name,
        ...(it.effect_tags ?? []),
        ...Object.keys(it.stats ?? {}),
        it.passive ?? "",
      ].join(" ").toLowerCase();
      if (!haystack.includes(q)) return false;
    }
    if (f.tier != null && it.tier !== f.tier) return false;
    if (f.efficiency) {
      const eff = it.efficiency_tier ?? "untiered";
      if (f.efficiency === "untiered" ? eff !== "untiered" : eff !== f.efficiency) return false;
    }
    if (f.tag && !(it.effect_tags ?? []).includes(f.tag)) return false;
    if (f.stat && !(it.stats && f.stat in it.stats)) return false;
    return true;
  });
}

export type SortKey = "value" | "name" | "cost-asc" | "cost-desc";

/**
 * `value` sorts by the continuous residual — most underpriced first.
 *
 * It used to sort by the three-bucket label, so 30 items tied for first in
 * alphabetical order and the most underpriced item in the game was not
 * findable.
 *
 * NOT-COMPARABLE ITEMS SINK. A god-specific item's residual is real —
 * Ashwhorl Acorn genuinely gives 3,211 gold of stats for 2,000 — but 86 of
 * the 87 gods cannot buy it, so heading a global "best value" board with it
 * answers a question nobody asked. Together with the statless items the
 * pipeline stopped scoring at all (Blink Rune read "worth 1,099g" for an item
 * with no stats), four of this board's top six were unbuyable or meaningless.
 * They still appear, and still show their own price; they just sort with
 * their own kind.
 */
export function sortItems(items: Item[], by: SortKey): Item[] {
  const arr = [...items];
  const byName = (a: Item, b: Item) => a.name.localeCompare(b.name);
  if (by === "name") arr.sort(byName);
  else if (by === "cost-asc") arr.sort((a, b) => (a.cost ?? 0) - (b.cost ?? 0) || byName(a, b));
  else if (by === "cost-desc") arr.sort((a, b) => (b.cost ?? 0) - (a.cost ?? 0) || byName(a, b));
  else {
    const rank = (i: Item): number =>
      i.efficiency == null ? 2 : i.efficiency.comparable === false ? 1 : 0;
    arr.sort((a, b) => {
      const ka = rank(a), kb = rank(b);
      if (ka !== kb) return ka - kb;
      const ra = a.efficiency?.residual, rb = b.efficiency?.residual;
      if (ra == null && rb == null) return byName(a, b);
      if (ra == null) return 1;
      if (rb == null) return -1;
      return ra - rb || byName(a, b);
    });
  }
  return arr;
}

export interface EfficiencyMeta {
  key: string;
  text: string;
  cls: string;
}

/** "Undervalued / Fair / Premium" — the same words the Legend teaches. The
 * shop used to say "Efficient", pairing a quality word with a price word, so
 * one signal had two names in two places. */
export const EFFICIENCY: EfficiencyMeta[] = [
  { key: "undervalued", text: "Undervalued", cls: "bg-under/20 text-under" },
  { key: "fair", text: "Fair", cls: "bg-bg3 text-muted" },
  { key: "premium", text: "Premium", cls: "bg-premium/20 text-premium" },
  { key: "untiered", text: "Not scored", cls: "bg-bg3 text-faint" },
];

export function efficiencyLabel(tier: string | null | undefined): EfficiencyMeta {
  return EFFICIENCY.find((e) => e.key === (tier ?? "untiered")) ?? EFFICIENCY[3];
}

/** Signed gold, always carrying its sign: "+244g" / "-310g". */
export function residualText(residual: number): string {
  return `${residual > 0 ? "+" : residual < 0 ? "−" : ""}${Math.abs(residual).toLocaleString("en-US")}g`;
}

/** What each stat on this item is worth at the fitted per-stat gold prices —
 * the line items behind a predicted cost. Stats the fit never priced (or
 * couldn't parse) are returned with a null value rather than a silent zero. */
export interface StatValueLine {
  stat: string;
  raw: string;
  amount: number | null;
  goldPerUnit: number | null;
  subtotal: number | null;
}

/** The regression's intercept — what the fit charges every item before a
 * single stat is counted. `predicted_cost` includes it, so a receipt that
 * lists only the stat rows is short by exactly this much on every item. */
export const INTERCEPT_KEY = "_intercept";

export function basePrice(goldValues: Record<string, number>): number {
  return goldValues[INTERCEPT_KEY] ?? 0;
}

/** Mirrors the pipeline's `efficiency.stat_key`: the unit is part of a stat's
 *  identity, so a percentage is priced in its own column. Penetration is the
 *  reason — it ships both flat and percent, worth ~4.5x different per point.
 *  A receipt that looked up the bare name would read the wrong price. */
export function statKey(stat: string, raw: string): string {
  return String(raw).trim().endsWith("%") ? `${stat} %` : stat;
}

export function statValueLines(item: Item, goldValues: Record<string, number>): StatValueLine[] {
  return Object.entries(item.stats ?? {}).map(([stat, raw]) => {
    const amount = parseStatAmount(raw);
    // The intercept is not a stat and must never be matched as one.
    const goldPerUnit = stat === INTERCEPT_KEY ? null : goldValues[statKey(stat, raw)] ?? null;
    return {
      stat,
      raw,
      amount,
      goldPerUnit,
      subtotal: amount != null && goldPerUnit != null ? amount * goldPerUnit : null,
    };
  });
}

/** Mirrors the pipeline's `parse_stat_value`: leading number, percent or not. */
function parseStatAmount(raw: string): number | null {
  const m = String(raw).match(/-?\d+(\.\d+)?/);
  return m ? Number(m[0]) : null;
}
