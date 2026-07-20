import type { Item } from "../types";

export interface ItemFilter {
  q?: string;
  tier?: number;
  efficiency?: string; // "undervalued" | "fair" | "premium" | "untiered"
  tag?: string;
  stat?: string;
}

export function filterItems(items: Item[], f: ItemFilter): Item[] {
  const q = f.q?.trim().toLowerCase();
  return items.filter((it) => {
    if (q && !it.name.toLowerCase().includes(q)) return false;
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

export type SortKey = "name" | "cost-asc" | "cost-desc" | "efficiency";
const EFF_ORDER: Record<string, number> = { undervalued: 0, fair: 1, premium: 2 };

export function sortItems(items: Item[], by: SortKey): Item[] {
  const arr = [...items];
  if (by === "name") arr.sort((a, b) => a.name.localeCompare(b.name));
  else if (by === "cost-asc") arr.sort((a, b) => (a.cost ?? 0) - (b.cost ?? 0));
  else if (by === "cost-desc") arr.sort((a, b) => (b.cost ?? 0) - (a.cost ?? 0));
  else if (by === "efficiency")
    arr.sort((a, b) => (EFF_ORDER[a.efficiency_tier ?? ""] ?? 9) - (EFF_ORDER[b.efficiency_tier ?? ""] ?? 9));
  return arr;
}

export interface EfficiencyMeta {
  key: string;
  text: string;
  cls: string;
}
export const EFFICIENCY: EfficiencyMeta[] = [
  { key: "undervalued", text: "Efficient", cls: "bg-under/20 text-under" },
  { key: "fair", text: "Fair", cls: "bg-line text-muted" },
  { key: "premium", text: "Premium", cls: "bg-premium/20 text-premium" },
  { key: "untiered", text: "—", cls: "bg-line text-muted" },
];

export function efficiencyLabel(tier: string | null | undefined): EfficiencyMeta {
  return EFFICIENCY.find((e) => e.key === (tier ?? "untiered")) ?? EFFICIENCY[3];
}
