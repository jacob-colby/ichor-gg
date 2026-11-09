import type { Item, StarterStamp } from "../types";

/** One community opener tile as the pipeline ships it — a single item, with no
 *  idea that the item above or below it in the list is the same purchase later. */
export interface StarterSighting {
  name: string;
  pick_rate: number;
  win_rate: number;
}

/** One opening PATH: the tier-1 starter and the tier-2 it becomes. */
export interface StarterPath {
  /** The tier-1 root. Absent when the community only ever holds the upgrade. */
  base?: StarterSighting;
  /** The tier-2 upgrade. Absent when nobody in this god's data upgraded. */
  upgrade?: StarterSighting;
  /** How many of this god's players open this way: the SUM of the two ends.
   *  SmiteBrain counts each player once, holding the base OR its upgrade, so
   *  the two rates are disjoint: a god's starter tiles sum to 98–103% of its
   *  matches on all 95 gods (ob47, 2026-11-08; the evidence is in
   *  `pipeline/smite/scoring.py`, above `pick_starter`). For Ra, Sands of
   *  Time 17% + Pendulum of the Ages 41% is a 58% path; the larger end alone
   *  said 41%. This is the same number the pipeline stamps on a build's
   *  `starter.pick_rate`. */
  pick_rate: number;
  /** The path's win rate: the two ends' rates weighted by their picks, as the
   *  pipeline computes it. Neither end speaks for the path on its own — only a
   *  game that went long or well reaches the upgrade, so the upgrade's rate is
   *  survivorship and the base's is its mirror. */
  win_rate: number;
  /** Name of the tier-1 root: the stable identity of the path, and the item
   *  every one of its players opened with. */
  rootName: string;
}

/**
 * Group a god's community openers into purchase paths.
 *
 * The "Opens with" row listed Leather Cowl and Hunter's Cowl as two separate
 * suggestions. They are one purchase — the second IS the first, later — and
 * the row only shows three entries, so a duplicate cost a third of the answer.
 * Measured across the shipped data, **84 of 89 gods** had a list containing
 * both halves of one path; Achilles' three openers were really two.
 *
 * Pass every sighting (`starter_sightings`), not the top 3 the page shows: a
 * path whose two ends sit 3rd and 4th is invisible in a top 3, and its share
 * would be read off one end. Ra's Conduit Gem is 4th.
 *
 * Grouping keys on the item graph (`builds_from` / `builds_into`), not on the
 * `starters` config in `_weights.yaml`. The config knows five pairs and the
 * graph knows all twelve — Leather Cowl -> Hunter's Cowl is not in the config
 * at all, and it is the pair the report was written about.
 *
 * Every starter root in the data is tier 1 with exactly one upgrade, so a path
 * is always at most two items and there is never an upgrade *choice* to show.
 */
export function groupStarters(
  sightings: StarterSighting[],
  itemsByName: Record<string, Item>,
): StarterPath[] {
  /** Walk down to the tier-1 root. Guarded against a cyclic `builds_from`,
   *  which would otherwise hang the render on a bad scrape. */
  const rootOf = (name: string): string => {
    const seen = new Set<string>();
    let cur = name;
    for (;;) {
      const from = itemsByName[cur]?.builds_from ?? [];
      if (!from.length || seen.has(cur)) return cur;
      seen.add(cur);
      cur = from[0];
    }
  };

  const ends = new Map<string, { base?: StarterSighting; upgrade?: StarterSighting }>();
  for (const s of sightings) {
    const root = rootOf(s.name);
    const path = ends.get(root) ?? {};
    // One sighting per end; a repeat replaces rather than adds, so a doubled
    // tile cannot double a share.
    if (s.name === root) path.base = s;
    else path.upgrade = s;
    ends.set(root, path);
  }

  const paths = [...ends].map(([rootName, { base, upgrade }]): StarterPath => {
    const held = [base, upgrade].filter((e): e is StarterSighting => !!e);
    const pick = held.reduce((a, e) => a + e.pick_rate, 0);
    const won = held.reduce((a, e) => a + e.pick_rate * e.win_rate, 0);
    return {
      rootName, base, upgrade,
      pick_rate: pick,
      // A path nobody picked has no record to weight; its one end's rate is
      // the only one there is.
      win_rate: pick > 0 ? won / pick : held[0].win_rate,
    };
  });

  // Most-picked path first — the pipeline's own order (`scoring.starter_paths`),
  // so the row and the stamped starter cannot disagree about which is #1. Ties
  // break on the root name so the row is deterministic across renders.
  return paths.sort((a, b) => b.pick_rate - a.pick_rate || a.rootName.localeCompare(b.rootName));
}

/**
 * How many of a god's players open with a build's starter, or undefined when
 * nothing here knows.
 *
 * The stamp's own `pick_rate` when the pipeline wrote one (a community pick:
 * the path's summed share, measured on the whole record). Otherwise — a build
 * saved in the editor, or a role-table starter — the grouped record's path
 * with the same root. Undefined means no player in the record opened that way.
 * The god page and the draft board both read this, so the two surfaces state
 * one number for one opener.
 */
export function starterShare(
  starter: StarterStamp | undefined,
  paths: StarterPath[],
): number | undefined {
  if (!starter) return undefined;
  if (typeof starter.pick_rate === "number") return starter.pick_rate;
  return paths.find((p) => p.rootName === starter.base)?.pick_rate;
}

/** How the path reads in one line: "Leather Cowl → Hunter's Cowl", or just the
 *  one item when only one end of it was ever seen. */
export function starterPathLabel(p: StarterPath): string {
  if (p.base && p.upgrade) return `${p.base.name} → ${p.upgrade.name}`;
  return (p.upgrade ?? p.base)!.name;
}
