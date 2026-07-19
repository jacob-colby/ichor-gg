import type {
  BuildEntry,
  CommunityBuildEntry,
  SlotEntry,
} from "../types";

export function isCommunityEntry(entry: BuildEntry): entry is CommunityBuildEntry {
  return entry.source === "community";
}

/** Tab label for a build entry: suggested builds show their archetype
 * (Core / Crit / Burst / …); mine builds show their user-given name; community
 * shows its source. */
export function tabLabel(entry: BuildEntry): string {
  if (entry.source === "suggested") return entry.archetype ?? "suggested";
  if (entry.source === "mine") return entry.name ?? "mine";
  return entry.source;
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

/** Derive the effective build shown when a matchup is selected: a flex slot (or
 * the lowest-scored core slot if none is marked / present) is removed and the
 * swap item is added. A null swapItem is a no-op (all kept). */
export function applySwap(slotOrder: string[], swapItem: string | null, flexSlots?: string[]): PreviewSlot[] {
  const base: PreviewSlot[] = slotOrder.map((name) => ({ name, status: "kept" }));
  if (!swapItem) return base;
  if (base.length === 0) return [{ name: swapItem, status: "added" }];
  const flex = (flexSlots ?? []).find((f) => slotOrder.includes(f));
  const idx = flex ? slotOrder.indexOf(flex) : base.length - 1;
  base[idx] = { name: base[idx].name, status: "removed" };
  base.push({ name: swapItem, status: "added" });
  return base;
}
