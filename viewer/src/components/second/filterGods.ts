import type { God } from "../../types";
import { godInLane, type Lane } from "../../lib/roleAccent";

/** Starts-with first ("ra" puts Ra before Hera), then alphabetical. */
export function filterGods(gods: God[], query: string, role: Lane | ""): God[] {
  const q = query.trim().toLowerCase();
  return [...gods]
    .filter((g) => (!role || godInLane(g.role, role)) && (!q || g.name.toLowerCase().includes(q)))
    .sort((a, b) => {
      if (q) {
        const as = a.name.toLowerCase().startsWith(q) ? 0 : 1;
        const bs = b.name.toLowerCase().startsWith(q) ? 0 : 1;
        if (as !== bs) return as - bs;
      }
      return a.name.localeCompare(b.name);
    });
}
