import type { God } from "../types";
import { godInLane, type Lane } from "./roleAccent";

export interface GodFilter {
  q?: string;
  pantheon?: string;
  role?: string;
  damage_type?: string;
  lane?: Lane;
}

export function filterGods(gods: God[], f: GodFilter): God[] {
  const q = f.q?.trim().toLowerCase();
  return gods.filter((g) => {
    if (q && !g.name.toLowerCase().includes(q)) return false;
    if (f.pantheon && g.pantheon !== f.pantheon) return false;
    if (f.role && g.role !== f.role) return false;
    if (f.lane && !godInLane(g.role, f.lane)) return false;
    if (f.damage_type && g.damage_type !== f.damage_type) return false;
    return true;
  });
}

export function sortGods(gods: God[], by: "name" = "name"): God[] {
  void by;
  return [...gods].sort((a, b) => a.name.localeCompare(b.name));
}
