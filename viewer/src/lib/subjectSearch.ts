/** Ranking for the shell's one search field.
 *
 * Pure logic, kept out of the component so it can be tested directly and so
 * the module exports components only.
 */
import type { God, Item } from "../types";
import { godLane, laneTextClass } from "./roleAccent";

export interface Hit {
  kind: "god" | "item";
  name: string;
  /** The one fact worth showing beside the name for this kind. */
  note?: string;
  noteClass?: string;
  /** One of the reader's own saved gods. Marked in the list, and used only as
   *  a TIEBREAK — a bookmark should never outrank a better name match, or
   *  typing an exact item name would surface a god instead. */
  bookmarked?: boolean;
}

const MAX = 8;

/** Name matches only. Searching item passives here would put "Rage" behind six
 *  items whose passive mentions rage, which is not what a nav field is for —
 *  the items shelf still searches tags, stats and passives. */
export function searchSubjects(
  gods: God[], items: Item[], q: string, bookmarks: string[] = [],
): Hit[] {
  const saved = new Set(bookmarks);
  const needle = q.trim().toLowerCase();

  // An empty box is not an empty answer. With nothing typed the field offers
  // the reader's own gods, in the order they saved them — the fastest route
  // back to what they actually play, and the reason a bookmark is worth
  // setting at all.
  if (!needle) {
    return bookmarks
      .map((name) => gods.find((g) => g.name === name))
      .filter((g): g is God => !!g)
      .slice(0, MAX)
      .map((g) => {
        const lane = godLane(g.role);
        return {
          kind: "god" as const, name: g.name,
          note: lane ?? g.role, noteClass: laneTextClass(lane), bookmarked: true,
        };
      });
  }
  const score = (name: string) => {
    const n = name.toLowerCase();
    if (n === needle) return 0;
    if (n.startsWith(needle)) return 1;
    return n.includes(needle) ? 2 : -1;
  };
  const rank = <T,>(list: T[], nameOf: (x: T) => string) =>
    list
      .map((x) => ({ x, s: score(nameOf(x)) }))
      .filter((r) => r.s >= 0)
      .sort((a, b) =>
        a.s - b.s
        // Only among equally good matches: two prefix hits break toward the
        // one already saved, but a saved god never jumps an exact match.
        || Number(saved.has(nameOf(b.x))) - Number(saved.has(nameOf(a.x)))
        || nameOf(a.x).localeCompare(nameOf(b.x)));

  const godHits: Hit[] = rank(gods, (g) => g.name).map(({ x }) => {
    const lane = godLane(x.role);
    return {
      kind: "god", name: x.name, note: lane ?? x.role,
      noteClass: laneTextClass(lane), bookmarked: saved.has(x.name),
    };
  });
  const itemHits: Hit[] = rank(items, (i) => i.name).map(({ x }) => ({
    kind: "item", name: x.name, note: `${x.cost}g`,
  }));

  // Gods lead: the product's subject outranks its components, and an exact item
  // match still surfaces because it sorts to the top of its own group.
  return [...godHits, ...itemHits].slice(0, MAX);
}
