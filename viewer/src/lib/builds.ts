import type {
  BuildEntry,
  CommunityBuildEntry,
  SlotEntry,
  SituationalSwap,
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

/** Returns the index of the situational_swaps entry whose vs_tag matches
 * the currently-selected archetype chip, or -1 if none matches / nothing
 * is selected. */
export function matchingSwapIndex(
  swaps: SituationalSwap[] | undefined,
  selectedTag: string | null,
): number {
  if (!swaps || !selectedTag) return -1;
  return swaps.findIndex((s) => s.vs_tag === selectedTag);
}
