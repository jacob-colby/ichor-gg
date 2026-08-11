import type { Item, SlotScore, SlotEntry } from "../types";
import { slotItemName } from "./builds";
import type { PreviewSlot } from "./builds";

/**
 * The buy ledger: the model's build laid out on a cumulative-gold spine, with
 * the community's own order joined onto each row.
 *
 * There is no timing data anywhere in the index — no minutes, no spike marks —
 * so the spine is gold spent, which is fully derivable from item cost. That
 * keeps the "when" axis true rather than invented.
 */
export interface LedgerRow {
  name: string;
  /** From applySwap: "kept" | "removed" | "added". */
  status: PreviewSlot["status"];
  cost: number | null;
  /** Gold spent through this purchase. Null when any earlier cost is unknown,
   * because a running total with a hole in it is worse than no total. */
  cumulative: number | null;
  score?: SlotScore;
  isFlex: boolean;
  /** 1-based position in the MODEL's own build order — counted over purchased
   * slots only, so a struck-through removed slot doesn't shift the numbers the
   * reader can see. Null on a removed row, which is not bought at all.
   *
   * This is the same spine `cumulative` runs on, stated as an ordinal. The row
   * used to compare the two orders in gold ("model buys later by 2,550g"),
   * which is precise and answers a question nobody asks: a build is bought in
   * slots, and "sixth" is the unit players actually think and talk in. */
  modelPosition: number | null;
  /** 1-based position in the community's own build order, if they buy it. */
  metaPosition: number | null;
  metaPickRate: number | null;
  metaWinRate: number | null;
  /** Gold the community has spent by the time they buy this item. */
  metaCumulative: number | null;
  /** The community buys this item at all (in their ordered build). */
  inMeta: boolean;
  /** A tier-1/2 item — a component, not something you finish a build with.
   *
   * It appears in a COMMUNITY slot because that data is what players actually
   * had when the match ended, and matches end before six items are built.
   * Measured across the 87 Conquest builds: slot 6 holds an unfinished item in
   * 70% of them and slot 5 in 9%, while slots 1-4 never do. Pick rate decays
   * the same way, 40% at slot 1 down to 9% at slot 6.
   *
   * So a community "six-item build" is really four or five finished items plus
   * whatever was half-built at the final whistle. Presented as six equals it
   * reads as a recommendation to buy a component last, which nobody means. */
  unfinished: boolean;
  /** The community buys this item, but as a SLOT ALTERNATE rather than in
   * their headline order, so it has no `metaPosition`. Its best sighting's
   * pick rate, or null if they genuinely never buy it.
   *
   * Without this the row claimed "meta doesn't buy this" about items the
   * popular-items panel on the same screen reported at 27% pick — Ratatoskr's
   * Thistlethorn Acorn is the community's second choice in three separate
   * slots and the winner in none. "No position in their order" and "nobody
   * buys it" are different statements, and only the first one was true. */
  metaAlternatePickRate: number | null;
  metaAlternateWinRate: number | null;
}

/** An item the community buys that the model's build never reaches — the
 * other half of the comparison, which a model-only row list can't show. */
export interface MetaOnlyRow {
  name: string;
  position: number;
  cumulative: number | null;
  pickRate: number | null;
  winRate: number | null;
}

export interface Ledger {
  rows: LedgerRow[];
  /** Community purchases absent from the model's build, in their own order. */
  metaOnly: MetaOnlyRow[];
  /** Total gold for the model's build (excluding removed slots). */
  totalGold: number | null;
  metaTotalGold: number | null;
  /** Items present in both orders. */
  shared: number;
  /** Effective slot count for the model's build (excluding removed). */
  slots: number;
  metaSlots: number;
  /** There is a community order to compare against at all. */
  hasMeta: boolean;
  /** Slots holding a component rather than a finished item. Only ever
   *  non-zero on a community build; see `LedgerRow.unfinished`. */
  unfinishedSlots: number;
}

/** Cumulative cost per position for an ordered list of item names. A missing
 * cost poisons the running total from that point on. */
function runningGold(names: string[], itemsByName: Map<string, Item>): (number | null)[] {
  let sum = 0;
  let broken = false;
  return names.map((n) => {
    const cost = itemsByName.get(n)?.cost;
    if (cost == null || broken) { broken = true; return null; }
    sum += cost;
    return sum;
  });
}

export function buildLedger({
  preview, itemsByName, scores, communityOrder, flexSlots,
}: {
  preview: PreviewSlot[];
  itemsByName: Map<string, Item>;
  scores?: Record<string, SlotScore>;
  communityOrder?: SlotEntry[];
  flexSlots?: string[];
}): Ledger {
  const metaNames = (communityOrder ?? []).map(slotItemName);
  const metaGold = runningGold(metaNames, itemsByName);
  const metaTotalGold = metaNames.length > 0 ? metaGold[metaGold.length - 1] : null;

  // A removed slot is struck through in the UI and must not consume gold, so
  // the spine is computed over what the player actually buys.
  const purchased = preview.filter((s) => s.status !== "removed");
  const purchasedGold = runningGold(purchased.map((s) => s.name), itemsByName);
  const goldByName = new Map<string, number | null>();
  const positionByName = new Map<string, number>();
  purchased.forEach((s, i) => {
    if (!goldByName.has(s.name)) goldByName.set(s.name, purchasedGold[i]);
    if (!positionByName.has(s.name)) positionByName.set(s.name, i + 1);
  });

  // The community's slot ALTERNATES, keyed by item, keeping the best sighting.
  // Mirrors pipeline `scoring.lookup_rates` and `build_index.popular_items`,
  // which is what makes the row and the popular-items panel agree.
  const altRates = new Map<string, { pick_rate: number; win_rate: number | null }>();
  for (const entry of communityOrder ?? []) {
    if (typeof entry === "string") continue;
    for (const alt of entry.alternates ?? []) {
      const seen = altRates.get(alt.name);
      if (!seen || alt.pick_rate > seen.pick_rate) {
        altRates.set(alt.name, { pick_rate: alt.pick_rate, win_rate: alt.win_rate ?? null });
      }
    }
  }

  const rows: LedgerRow[] = preview.map((slot) => {
    const metaIdx = metaNames.indexOf(slot.name);
    const metaEntry = metaIdx >= 0 ? communityOrder?.[metaIdx] : undefined;
    const rates = metaEntry && typeof metaEntry !== "string" ? metaEntry : undefined;
    // A slot pick is authoritative; only fall back to alternates.
    const alt = metaIdx >= 0 ? undefined : altRates.get(slot.name);
    return {
      name: slot.name,
      status: slot.status,
      cost: itemsByName.get(slot.name)?.cost ?? null,
      unfinished: (() => {
        const tier = itemsByName.get(slot.name)?.tier;
        return typeof tier === "number" && tier < 3;
      })(),
      cumulative: slot.status === "removed" ? null : goldByName.get(slot.name) ?? null,
      score: scores?.[slot.name],
      isFlex: !!flexSlots?.includes(slot.name),
      modelPosition: slot.status === "removed" ? null : positionByName.get(slot.name) ?? null,
      metaPosition: metaIdx >= 0 ? metaIdx + 1 : null,
      metaPickRate: rates?.pick_rate ?? null,
      metaWinRate: rates?.win_rate ?? null,
      metaCumulative: metaIdx >= 0 ? metaGold[metaIdx] : null,
      inMeta: metaIdx >= 0,
      metaAlternatePickRate: alt?.pick_rate ?? null,
      metaAlternateWinRate: alt?.win_rate ?? null,
    };
  });

  const kept = rows.filter((r) => r.status !== "removed");
  const modelNames = new Set(kept.map((r) => r.name));
  const metaOnly: MetaOnlyRow[] = metaNames
    .map((name, i) => ({ name, i }))
    .filter(({ name }) => !modelNames.has(name))
    .map(({ name, i }) => {
      const e = communityOrder?.[i];
      const rates = e && typeof e !== "string" ? e : undefined;
      return {
        name,
        position: i + 1,
        cumulative: metaGold[i],
        pickRate: rates?.pick_rate ?? null,
        winRate: rates?.win_rate ?? null,
      };
    });

  return {
    rows,
    metaOnly,
    totalGold: purchased.length > 0 ? purchasedGold[purchasedGold.length - 1] : null,
    metaTotalGold,
    shared: kept.filter((r) => r.inMeta).length,
    slots: kept.length,
    metaSlots: metaNames.length,
    hasMeta: metaNames.length > 0,
    unfinishedSlots: kept.filter((r) => r.unfinished).length,
  };
}

/** "16,550g" — thousands separated, because a six-slot build runs five digits
 * and an unseparated number is unreadable at 10px. */
export function goldText(v: number | null | undefined): string {
  if (v == null) return "—";
  return `${v.toLocaleString("en-US")}g`;
}

/** "1st", "2nd", "6th" — a build is six slots long, so no 11-13 special case
 * can ever fire here, but it is handled anyway rather than left as a trap for
 * the first caller who counts something longer. */
export function ordinal(n: number): string {
  const rem100 = n % 100;
  if (rem100 >= 11 && rem100 <= 13) return `${n}th`;
  const suffix = { 1: "st", 2: "nd", 3: "rd" }[n % 10] ?? "th";
  return `${n}${suffix}`;
}
