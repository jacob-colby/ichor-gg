/** The value receipt: an item's fitted worth, itemised, closing exactly.
 *
 * `predicted_cost` is the pipeline's own rounded total, and `cost -
 * predicted_cost === residual` holds exactly in the data. The rows behind it
 * are not integers — 85 Intelligence at 13.58g is 1,154.3g — so rounding each
 * row on its own can leave the column a gold or two away from the total it
 * sits above. A receipt that does not add up is the one thing the items page
 * cannot print, so the rows are rounded by largest remainder onto the
 * pipeline's own total. When the rows differ from it by more than rounding can
 * explain, the difference is printed as its own line rather than hidden inside
 * a row.
 *
 * Pure. Tested in receipt.test.ts. */
import type { Item } from "../../types";
import { basePrice, statValueLines } from "../../lib/itemFilters";

export interface ReceiptLine {
  label: string;
  /** "85 × 13.58g a point" — the arithmetic, when the line is a stat. */
  detail?: string;
  gold: number;
}

export interface Receipt {
  lines: ReceiptLine[];
  /** Stats on the item the fit never priced — named, never counted as zero. */
  unpriced: string[];
  worth: number;
  cost: number;
  /** cost − worth. Positive: costs more than its stats are worth. */
  gap: number;
}

export const gold = (n: number) => `${Math.round(n).toLocaleString("en-US")}g`;
export const signedGold = (n: number) => `${n > 0 ? "+" : n < 0 ? "−" : ""}${gold(Math.abs(n))}`;

export function buildReceipt(item: Item, goldValues: Record<string, number>): Receipt | null {
  const eff = item.efficiency;
  if (!eff) return null;
  const stat = statValueLines(item, goldValues);
  const raw = [
    { label: "Base price", detail: "what the fit charges every item", value: basePrice(goldValues) },
    ...stat.filter((l) => l.subtotal != null).map((l) => ({
      label: l.stat, detail: `${l.raw} × ${l.goldPerUnit!.toFixed(2)}g a point`, value: l.subtotal!,
    })),
  ];
  const target = eff.predicted_cost;
  const floors = raw.map((r) => Math.floor(r.value));
  const short = target - floors.reduce((a, b) => a + b, 0);
  let lines: ReceiptLine[];
  if (short >= 0 && short <= raw.length) {
    // Largest remainder: the rows that lost most to the floor get the gold back.
    const order = raw.map((r, i) => ({ i, frac: r.value - Math.floor(r.value) }))
      .sort((a, b) => b.frac - a.frac || a.i - b.i);
    const bump = new Set(order.slice(0, short).map((o) => o.i));
    lines = raw.map((r, i) => ({ label: r.label, detail: r.detail, gold: floors[i] + (bump.has(i) ? 1 : 0) }));
  } else {
    lines = raw.map((r) => ({ label: r.label, detail: r.detail, gold: Math.round(r.value) }));
    const rest = target - lines.reduce((a, l) => a + l.gold, 0);
    if (rest !== 0) lines.push({ label: "Not itemised", detail: "the fit's total, less the rows above", gold: rest });
  }
  return {
    lines,
    unpriced: stat.filter((l) => l.subtotal == null).map((l) => l.stat),
    worth: target,
    cost: item.cost,
    gap: eff.residual,
  };
}
