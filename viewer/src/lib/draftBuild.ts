import type { Item } from "../types";

export interface Overlay { tags: Record<string, number>; stats: Record<string, number>; }
export interface AdaptOpts { maxBonus: number; maxLifesteal?: number; n?: number; }
export interface AdaptedCore {
  core: string[];
  reasons: Record<string, string>;   // item -> why it gained (tags/stats that scored)
  bonuses: Record<string, number>;   // item -> clamped total bonus
}

// Mirrors assemble._is_boots / _is_lifesteal so the client build obeys the same
// constraints the Python assembler does.
const isBoots = (it: Item | undefined) => !!it && "Movement Speed" in (it.stats ?? {});
const isLifesteal = (it: Item | undefined) =>
  !!it && ((it.effect_tags ?? []).includes("sustain") ||
           Object.keys(it.stats ?? {}).some((s) => s.includes("Lifesteal")));

/** base item scores + a draft-derived tag/stat overlay -> a re-ranked,
 * re-assembled 6-item core mirroring assemble.assemble_core's constraints
 * (at most one boots, at most `maxLifesteal` lifesteal/sustain items, no
 * duplicates, fill by adjusted score). Pure function, no side effects. */
export function adaptedCore(
  base: Record<string, number>,
  itemsByName: Record<string, Item>,
  overlay: Overlay,
  opts: AdaptOpts,
): AdaptedCore {
  const n = opts.n ?? 6;
  const maxLifesteal = opts.maxLifesteal ?? 1;
  const bonuses: Record<string, number> = {};
  const reasons: Record<string, string> = {};

  const scored = Object.entries(base).map(([name, total]) => {
    const it = itemsByName[name];
    let bonus = 0;
    const why: string[] = [];
    for (const tag of it?.effect_tags ?? []) {
      const w = overlay.tags[tag];
      if (w) { bonus += w; why.push(tag); }
    }
    for (const stat of Object.keys(it?.stats ?? {})) {
      const w = overlay.stats[stat];
      if (w) { bonus += w; why.push(stat); }
    }
    // Clamp the SUM, not each term — this is what bounds how much a comp can
    // rewrite the build (a maximal overlay still only moves an item by
    // opts.maxBonus, never the raw unbounded total).
    bonus = Math.max(-opts.maxBonus, Math.min(opts.maxBonus, bonus));
    if (bonus !== 0) { bonuses[name] = bonus; reasons[name] = why.join(", "); }
    return { name, score: total + bonus };
  });

  // Deterministic: score desc, then name asc — ties must never depend on
  // Object.entries iteration order (i.e. on `base`'s key insertion order).
  scored.sort((a, b) => b.score - a.score || a.name.localeCompare(b.name));

  const core: string[] = [];
  let haveBoots = false;
  let lifesteal = 0;
  for (const { name } of scored) {
    if (core.length >= n) break;
    const it = itemsByName[name];
    if (isBoots(it)) {
      if (haveBoots) continue;
      haveBoots = true;
    }
    if (isLifesteal(it)) {
      if (lifesteal >= maxLifesteal) continue;
      lifesteal += 1;
    }
    core.push(name);
  }

  return { core, reasons, bonuses };
}

/** One line of the draft's effect on a build. */
export interface CoreChange {
  /** The item the draft promoted into the core. */
  added: string;
  /** The item it pushed out, when the swap pairs one-for-one. */
  removed?: string;
  /** Clamped score bonus that moved it — the number that *is* the mechanism. */
  bonus: number;
  /** Tags/stats that earned the bonus, e.g. "anti-heal, Magical Protection". */
  reason?: string;
}

export interface CoreDiff {
  changes: CoreChange[];
  /** Items in both builds — the part the draft didn't touch. */
  unchanged: string[];
  /** Pushed out with no matching arrival (rare; only on odd-sized diffs). */
  droppedOnly: string[];
}

/**
 * What the draft did to the build, as pairs.
 *
 * The page used to reduce the un-adapted core to a membership `Set`, so a row
 * could say "swap in" but never *swap in for what* — the displaced item and
 * the magnitude were both computed and then discarded. Both sides of the
 * comparison are the product's whole claim, so both have to survive.
 *
 * Arrivals and departures are paired by rank within their own lists: the
 * highest-scoring newcomer takes the place of the highest-scoring casualty.
 * That's a presentational pairing, not a claim the assembler made it.
 */
export function diffCore(base: AdaptedCore, adapted: AdaptedCore): CoreDiff {
  const baseSet = new Set(base.core);
  const adaptedSet = new Set(adapted.core);
  const added = adapted.core.filter((n) => !baseSet.has(n));
  const removed = base.core.filter((n) => !adaptedSet.has(n));

  return {
    changes: added.map((name, i) => ({
      added: name,
      removed: removed[i],
      bonus: adapted.bonuses[name] ?? 0,
      reason: adapted.reasons[name],
    })),
    unchanged: adapted.core.filter((n) => baseSet.has(n)),
    droppedOnly: removed.slice(added.length),
  };
}
