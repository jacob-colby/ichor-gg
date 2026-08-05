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
/** The three builds that answer the same question three ways, in the order a
 *  reader should meet them: the model's own answer, that answer corrected where
 *  the community has real evidence, then what people actually run. Flavors and
 *  the player's own builds follow. */
export const HEADLINE_ARCHETYPES = ["model", "hybrid"] as const;

const ARCHETYPE_LABEL: Record<string, string> = {
  model: "Model",
  hybrid: "Hybrid",
  core: "Balanced",
  crit: "Crit",
  burst: "Burst",
  bruiser: "Bruiser",
  "anti-tank": "Anti-tank",
  "attack-speed": "Attack speed",
  cooldown: "Cooldown",
  // Off-type power builds, offered only where the god's own scaling supports
  // them — see `requires_scaling` in _weights.yaml.
  strength: "Strength",
  intelligence: "Intelligence",
  "str-int": "Str + Int",
};

export function tabLabel(entry: BuildEntry): string {
  if (entry.source === "community") return "Community";
  if (entry.source === "suggested") {
    const a = entry.archetype ?? "suggested";
    return ARCHETYPE_LABEL[a] ?? a;
  }
  if (entry.source === "mine") return entry.name ?? "mine";
  return entry.source;
}

/** Model, Hybrid, Community, then everything else in its existing order.
 *  `core` stays available — three other systems read it by name — but it is no
 *  longer the answer a visitor meets first. */
export function orderBuilds(suggested: BuildEntry[], community?: BuildEntry): BuildEntry[] {
  const rank = (e: BuildEntry) => {
    if (e.source === "community") return 2;
    const a = e.source === "suggested" ? e.archetype : undefined;
    const i = HEADLINE_ARCHETYPES.indexOf(a as typeof HEADLINE_ARCHETYPES[number]);
    return i >= 0 ? i : 3;
  };
  const all = community ? [...suggested, community] : [...suggested];
  return all
    .map((e, i) => ({ e, i }))
    .sort((x, y) => rank(x.e) - rank(y.e) || x.i - y.i)
    .map(({ e }) => e);
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
  // Insert where the swap actually happens rather than appending. Since the
  // ledger reads row position as purchase order, a swap for slot 2 pushed to
  // the end would claim it's bought last — and its cumulative gold with it.
  // Identical to appending in the common case, where the removed slot is last.
  base.splice(idx + 1, 0, { name: swapItem, status: "added" });
  return base;
}
