import type { Item } from "../types";

export interface Overlay {
  tags: Record<string, number>;
  stats: Record<string, number>;
  /** B6: a bonus keyed directly by item, from the damage model. The tag and
   *  stat channels can only say "penetration is good against tanks"; this one
   *  knows that PERCENT penetration rises against a tank while FLAT
   *  penetration falls, because it is measured per item rather than per stat. */
  items?: Record<string, number>;
}
export interface AdaptOpts {
  maxBonus: number;
  maxLifesteal?: number;
  n?: number;
  /** How much of a draft bonus survives when the core ALREADY covers the tag
   *  or stat earning it. 1 = the old behaviour (pay in full, every time);
   *  0 = a job answered once is never paid for again.
   *
   *  This is the same judgement `threats.ts` already makes about ALLIES —
   *  `ally_covered` damps a threat one of your teammates handles — applied to
   *  the one build the overlay is actually rewriting. Without it the draft
   *  paid the full anti-heal bonus to a SECOND anti-heal item while the first
   *  was already in the core, and that second copy displaced whatever the
   *  build genuinely still needed. A recommendation has to be better than what
   *  it removes GIVEN the other five slots, not in isolation.
   *
   *  Measured before believing it: across four enemy comps x 87 gods the old
   *  behaviour doubled up on a bonused tag exactly ONCE (Mercury, two `peel`
   *  items, against five healers). `max_bonus` already bounds the overlay
   *  tightly enough that this is a guard, not a repair — see `self_covered` in
   *  _weights.yaml for why it is kept anyway. */
  selfCovered?: number;
}
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
  const selfCovered = opts.selfCovered ?? 1;
  const bonuses: Record<string, number> = {};
  const reasons: Record<string, string> = {};

  /** This item's draft bonus, given what the core already covers. `covered`
   *  is the set of overlay keys some already-chosen item supplies. */
  const scoreOf = (name: string, covered: Set<string>) => {
    const it = itemsByName[name];
    let bonus = 0;
    const why: string[] = [];
    const credit = (key: string, w: number, label: string) => {
      if (!w) return;
      // A bonus is damped only when the core already covers that exact key,
      // and only for a POSITIVE bonus. A penalty is not a job that can be
      // "already done" — damping it would quietly re-promote the very items
      // the overlay is trying to push down.
      const damp = w > 0 && covered.has(key) ? selfCovered : 1;
      bonus += w * damp;
      why.push(damp === 1 ? label : `${label} (already covered)`);
    };
    // TAGS ONLY. A tag is a job — you have anti-heal or you don't, and the
    // second copy mostly answers a question already answered. A STAT is a
    // quantity: 60 magical protection really is better than 30 against a magic
    // comp, so damping the second protection item would be saying "you already
    // have some" about something that scales. `threats.ts` draws the same line
    // — `ally_covered` is applied in its tag_bonus loop and not in its
    // stat_bonus loop. Measured with stats included as well: 70-79 of 87 cores
    // changed per comp, which is not a targeted correction, it is a different
    // model.
    for (const tag of it?.effect_tags ?? []) credit(`tag:${tag}`, overlay.tags[tag], tag);
    for (const stat of Object.keys(it?.stats ?? {})) {
      const w = overlay.stats[stat];
      if (w) { bonus += w; why.push(stat); }
    }
    const dmg = overlay.items?.[name];
    if (dmg) {
      // Per-item damage, not a job any other slot can do for you — never damped.
      bonus += dmg;
      why.push(dmg > 0 ? "damage vs their build" : "less damage vs their build");
    }
    // Clamp the SUM, not each term — this is what bounds how much a comp can
    // rewrite the build (a maximal overlay still only moves an item by
    // opts.maxBonus, never the raw unbounded total).
    bonus = Math.max(-opts.maxBonus, Math.min(opts.maxBonus, bonus));
    return { score: base[name] + bonus, bonus, why: why.join(", ") };
  };

  /** The overlay keys an item supplies, so the core can know what it covers. */
  const keysOf = (name: string) => {
    const it = itemsByName[name];
    const out: string[] = [];
    for (const tag of it?.effect_tags ?? []) if (overlay.tags[tag] > 0) out.push(`tag:${tag}`);
    return out;
  };

  const core: string[] = [];
  const covered = new Set<string>();
  const remaining = Object.keys(base);
  let haveBoots = false;
  let lifesteal = 0;

  // Selected one slot at a time rather than sorted once, because an item's
  // bonus now depends on what the core already holds. With selfCovered = 1
  // nothing is damped and this picks exactly what the single sort picked.
  while (core.length < n && remaining.length > 0) {
    let bestIndex = -1;
    let best: { score: number; bonus: number; why: string } | null = null;
    for (let i = 0; i < remaining.length; i += 1) {
      const cand = scoreOf(remaining[i], covered);
      // Deterministic: score desc, then name asc — ties must never depend on
      // key insertion order in `base`.
      if (!best || cand.score > best.score
          || (cand.score === best.score && remaining[i].localeCompare(remaining[bestIndex]) < 0)) {
        best = cand;
        bestIndex = i;
      }
    }
    const name = remaining.splice(bestIndex, 1)[0];
    const it = itemsByName[name];
    if (isBoots(it)) {
      if (haveBoots) continue;
      haveBoots = true;
    }
    if (isLifesteal(it)) {
      if (lifesteal >= maxLifesteal) continue;
      lifesteal += 1;
    }
    if (best && best.bonus !== 0) { bonuses[name] = best.bonus; reasons[name] = best.why; }
    for (const key of keysOf(name)) covered.add(key);
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
