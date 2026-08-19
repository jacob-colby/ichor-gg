import type { Item } from "../types";

/** One community opener as the pipeline ships it — a single item, with no idea
 *  that the item above or below it in the list is the same purchase later. */
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
  /** Whichever end of the path the community holds most often — the honest
   *  "how often do you see this opener at all". NOT a sum: a player who buys
   *  the base and upgrades it is counted in both rates, so adding them would
   *  invent a number larger than the truth. */
  lead: StarterSighting;
  /** Name of the tier-1 root, used as the stable identity of the path. */
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

  const byRoot = new Map<string, StarterPath>();
  for (const s of sightings) {
    const root = rootOf(s.name);
    const isRoot = s.name === root;
    const existing = byRoot.get(root);
    if (!existing) {
      byRoot.set(root, {
        rootName: root,
        base: isRoot ? s : undefined,
        upgrade: isRoot ? undefined : s,
        lead: s,
      });
      continue;
    }
    if (isRoot) existing.base = s;
    else existing.upgrade = s;
    // The lead is the end of the path the community actually holds most often.
    if (s.pick_rate > existing.lead.pick_rate) existing.lead = s;
  }

  // Order by the path's own lead rate, so grouping cannot reorder the list
  // against what the pick rates say. Ties break on the root name so the row is
  // deterministic across renders.
  return [...byRoot.values()].sort(
    (a, b) => b.lead.pick_rate - a.lead.pick_rate || a.rootName.localeCompare(b.rootName),
  );
}

/** How the path reads in one line: "Leather Cowl → Hunter's Cowl", or just the
 *  one item when only one end of it was ever seen. */
export function starterPathLabel(p: StarterPath): string {
  if (p.base && p.upgrade) return `${p.base.name} → ${p.upgrade.name}`;
  return (p.upgrade ?? p.base)!.name;
}
