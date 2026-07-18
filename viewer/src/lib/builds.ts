import type {
  BuildEntry,
  CommunityBuildEntry,
  SlotEntry,
} from "../types";

export function isCommunityEntry(entry: BuildEntry): entry is CommunityBuildEntry {
  return entry.source === "community";
}

/** slot_order entries are plain strings for pro/mine, {name, pick_rate,
 * win_rate} objects for community — this normalizes either shape down to
 * just the item name. */
export function slotItemName(entry: SlotEntry): string {
  return typeof entry === "string" ? entry : entry.name;
}

/** Matches the Python pipeline's slug convention exactly (see
 * tools/smite/refresh.py and every other slug-construction call site in
 * that codebase) — must stay in sync so icon filenames resolve. */
export function iconSlug(name: string): string {
  return name.toLowerCase().replace(/ /g, "-").replace(/'/g, "");
}

export type SlotStatus = "kept" | "removed" | "added";
export interface PreviewSlot {
  name: string;
  status: SlotStatus;
}

/** Derive the effective build shown when a matchup is selected: the
 * lowest-scored core slot (the last one — slot_order is score-sorted) is
 * removed and the swap item is added. A null swapItem is a no-op (all kept). */
export function applySwap(slotOrder: string[], swapItem: string | null): PreviewSlot[] {
  const base: PreviewSlot[] = slotOrder.map((name) => ({ name, status: "kept" }));
  if (!swapItem) return base;
  if (base.length === 0) return [{ name: swapItem, status: "added" }];
  base[base.length - 1] = { name: base[base.length - 1].name, status: "removed" };
  base.push({ name: swapItem, status: "added" });
  return base;
}
