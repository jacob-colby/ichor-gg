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
  /** `assemble.flex_slots` for THIS build — the pipeline's own verdict on
   *  which two of the six it is least sure about, scored under the archetype's
   *  own profile. Used only to break ties between equally-unbonused victims,
   *  so the draft spends the pipeline's own flexible slot before it spends a
   *  slot the pipeline was confident about. */
  flexSlots?: string[];
  /** How much MORE draft evidence an arrival must carry than the item it
   *  displaces. Defaults to `maxBonus`; see `adaptFromCore`. */
  swapBar?: number;
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

interface Priced { bonus: number; why: string }

/** The draft overlay's price for one item, given what the rest of the build
 *  already covers. This is the whole of what the viewer computes; everything
 *  else on this page is the pipeline's.
 *
 *  Split out of the old `adaptedCore` unchanged, because it is the half of
 *  that function that was never the problem. Its evidence is below and in
 *  draftBuild.test.ts; the half that WAS the problem — a greedy re-assembly of
 *  the six items from `god_item_scores` — is gone. See `adaptFromCore`. */
function pricer(itemsByName: Record<string, Item>, overlay: Overlay, opts: AdaptOpts) {
  const selfCovered = opts.selfCovered ?? 1;
  return (name: string, covered: Set<string>): Priced => {
    const it = itemsByName[name];
    let bonus = 0;
    // The largest single POSITIVE channel this item earned. The clamp is
    // raised to it, so a well-evidenced answer is never vetoed by the budget
    // it has to share with everything else — see the clamp note below.
    let strongest = 0;
    const why: string[] = [];
    const credit = (key: string, w: number, label: string) => {
      if (!w) return;
      // A bonus is damped only when the core already covers that exact key,
      // and only for a POSITIVE bonus. A penalty is not a job that can be
      // "already done" — damping it would quietly re-promote the very items
      // the overlay is trying to push down.
      const damp = w > 0 && covered.has(key) ? selfCovered : 1;
      const amount = w * damp;
      bonus += amount;
      if (amount > strongest) strongest = amount;
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
      if (w) { bonus += w; if (w > strongest) strongest = w; why.push(stat); }
    }
    const dmg = overlay.items?.[name];
    if (dmg) {
      // Per-item damage, not a job any other slot can do for you — never damped.
      bonus += dmg;
      // Deliberately NOT counted toward `strongest`. The threat channels are
      // bounded evidence ("4 of 5 enemies heal"); this one is a continuous
      // per-item measurement with no such ceiling, so letting it raise its own
      // clamp would let a single large damage figure rewrite the build
      // wholesale — which is the invariant the B6 tests already pin.
      why.push(dmg > 0 ? "damage vs their build" : "less damage vs their build");
    }
    /* CLAMP THE STACK, NOT THE STRONGEST SIGNAL.
     *
     * The clamp exists to bound how much a comp can rewrite a build, and the
     * failure it guards against is many weak channels summing into a rewrite.
     * Applied to the SUM alone it also vetoed a single well-evidenced one, and
     * that is the case it was hurting most.
     *
     * Measured before changing it. Against 4 of 5 healers, Divine Ruin earned
     * 0.8 share x 0.1 per_share x 2.0 weight x 1.5 ally_gap = 0.240 and was cut
     * to 0.120, landing 8th of 40 — 0.027 short of a core slot. Worse, because
     * a healer comp is also a CC and tank comp, anti-heal was sharing that one
     * fixed budget with penetration and cc-immunity and losing: of the 31 gods
     * who can buy anti-heal at all, only 13 did.
     *
     * The sharpest symptom: a 2-healer comp and a 4-healer comp produced
     * BYTE-IDENTICAL builds (29/89 both). The bonus doubled, the clamp ate it,
     * and the draft could not tell the difference between the two comps.
     *
     * So the ceiling is `max(maxBonus, strongest single channel)`. Stacking is
     * still bounded exactly as before; one channel that genuinely earned more
     * is allowed to keep it. Worst case is a 5-of-5 comp on the highest-weighted
     * threat, which reaches 0.30.
     *
     * Raising `max_bonus` instead was measured and rejected: it reaches the
     * same anti-heal numbers only by loosening every channel on every draft,
     * including comps with no threat at all (churn on a no-threat comp went
     * 2.35 -> 2.91, while this rule leaves it at 2.35).
     *
     * The negative side keeps the flat bound. A penalty is not a well-evidenced
     * answer to anything, and letting a strong positive channel widen the floor
     * would push items down harder than the overlay ever intended.
     */
    const ceiling = Math.max(opts.maxBonus, strongest);
    bonus = Math.max(-opts.maxBonus, Math.min(ceiling, bonus));
    return { bonus, why: why.join(", ") };
  };
}

/**
 * The pipeline's assembled core, with the draft allowed to argue with it.
 *
 * WHY THIS IS A DIFF AND NOT AN ASSEMBLY. The draft used to re-assemble the
 * six items itself: sort `god_item_scores` by score + overlay, fill greedily,
 * one boots, `maxLifesteal` sustain. With NO overlay at all that reproduced
 * the god page's core for 190 of 2,247 build groups (8.5%) — 22 of 90 on
 * Conquest `core` — at 61.3% item overlap, measured against the shipped index
 * on 2026-09-03. The two surfaces named one archetype for one god in one mode
 * and showed different builds, which is the One-Claim Rule broken eleven times
 * per god per mode.
 *
 * THE GAP WAS NEVER A MISSING OVERLAY. `assemble.assemble_core` re-prices
 * every remaining candidate against the stats the core already holds
 * (`coherence_multiplier`, `conversion_score_bonus`), charges it for gold
 * already committed (`time_value_multiplier`) and marks it down for a stat the
 * core has capped out (`cap_overflow_penalty`) — then `assemble_core_converged`
 * re-runs the whole thing until the core stops changing. All of that happens
 * DURING assembly, so none of it can be in `god_item_scores`, which ships
 * `total` from before it. A single greedy pass over those totals cannot
 * reproduce it and no setting of the overlay closes it: 09-02 C swept 21
 * (scale x ceiling) settings and turning the overlay UP took overlap down to
 * 33.3%.
 *
 * So the assembler is the pipeline's, full stop, and the shipped `slot_order`
 * is the input here. This function starts from it and may only SWAP.
 *
 * THE SWAP RULE, AND WHY IT HAS A BAR. Adaptation has to be able to bring in
 * an item the base core never contained — anti-heal against healers,
 * cc-immunity against heavy CC — or the feature is gone. So a swap is allowed,
 * and it is allowed on the DRAFT'S OWN EVIDENCE ONLY:
 *
 *     arrival replaces departure  iff  bonus(arrival) - bonus(departure) >= bar
 *
 * with `bar` defaulting to `draft.max_bonus` (0.12 shipped). Two things follow,
 * and both are the point:
 *
 *   - With an empty board every bonus is 0, the difference is 0, no swap can
 *     clear the bar, and the board shows the pipeline's core EXACTLY. That is
 *     `archetypeParity.test.ts`, and it is true by construction rather than by
 *     arithmetic that happens to agree.
 *   - The base score cannot move anything on its own. The draft does not get
 *     to re-litigate the model's ranking — that ranking already produced this
 *     core, through an assembler this file cannot see. It only gets to spend
 *     what the comp earned.
 *
 * The bar is `max_bonus` and not a new constant because `max_bonus` is already
 * the config's statement of how much one comp may move one item. Requiring a
 * full budget's ADVANTAGE says: an arrival must have earned more from this
 * draft than the whole overlay is nominally allowed to give anyone, over and
 * above what the item it displaces earned. Measured against the shipped index
 * (the counts are pinned in archetypeParity.test.ts): a 5-of-5 healer comp
 * brings 59 new items onto 58 of the 90 Conquest `core` boards and fires on
 * all 13 archetypes; a 1-of-5 healer comp moves nothing at all. That the two
 * comps differ AT ALL is the shape the clamp note above says the old code
 * could not produce, since a clamp on the absolute bonus made a 2-healer and
 * a 4-healer comp byte-identical.
 *
 * WHICH ITEM LEAVES. Among the incumbents a given arrival is allowed to
 * displace, the one with the lowest bonus; ties go to a `flex_slot` first —
 * the pipeline's own "least sure about these two" — then to the later slot,
 * then by name. `boots` and sustain are handled by restricting the victim
 * rather than by rejecting the arrival, so an arrival that would break
 * `assemble_core`'s one-boots / `maxLifesteal` rules displaces the item that
 * holds that budget instead of being dropped.
 *
 * WHICH ITEM ARRIVES. Every candidate that clears the bar is a legal answer;
 * the one that comes in is the highest `base + bonus` among them. The draft
 * decides WHETHER to swap, the model decides WHICH — `god_item_scores` is
 * internally consistent, so ranking candidates against each other in it is
 * sound even where comparing them to an incumbent would not be.
 *
 * BUY ORDER IS NOT TOUCHED. The arrival takes the departure's slot and nothing
 * else moves. `assemble.build_order` blends a tag-and-cost heuristic with this
 * god's own community slot centroid (STATE.md §4.24); the viewer has neither,
 * and inventing a third ordering here is the same mistake in a different
 * place. A consequence worth stating: the draft can no longer produce an
 * order-only change, because it no longer orders anything.
 */
export function adaptFromCore(
  shipped: string[],
  base: Record<string, number>,
  itemsByName: Record<string, Item>,
  overlay: Overlay,
  opts: AdaptOpts,
): AdaptedCore {
  const maxLifesteal = opts.maxLifesteal ?? 1;
  const bar = opts.swapBar ?? opts.maxBonus;
  const flex = new Set(opts.flexSlots ?? []);
  const price = pricer(itemsByName, overlay, opts);
  const core = [...shipped];

  /** The overlay keys an item supplies, so the core can know what it covers. */
  const keysOf = (name: string) => {
    const it = itemsByName[name];
    const out: string[] = [];
    for (const tag of it?.effect_tags ?? []) if (overlay.tags[tag] > 0) out.push(`tag:${tag}`);
    return out;
  };

  // Every item that has left the core. A departure never comes back: without
  // this a two-cycle is reachable, and it is also just true that the draft
  // having rejected an item once should not re-argue for it.
  const gone = new Set<string>();

  for (let round = 0; round < core.length; round += 1) {
    // An incumbent's own tags must not damp its own bonus, so each is priced
    // against what the OTHER five cover. A candidate is priced against all six.
    const incumbents = core.map((name, slot) => {
      const others = new Set<string>();
      core.forEach((n, i) => { if (i !== slot) keysOf(n).forEach((k) => others.add(k)); });
      return { name, slot, ...price(name, others) };
    });
    const covered = new Set<string>();
    for (const n of core) keysOf(n).forEach((k) => covered.add(k));
    const held = new Set(core);

    const victimFor = (cand: string) => {
      const it = itemsByName[cand];
      let pool = incumbents;
      if (isBoots(it) && core.some((n) => isBoots(itemsByName[n]))) {
        pool = pool.filter((x) => isBoots(itemsByName[x.name]));
      }
      if (isLifesteal(it)
          && core.filter((n) => isLifesteal(itemsByName[n])).length >= maxLifesteal) {
        pool = pool.filter((x) => isLifesteal(itemsByName[x.name]));
      }
      if (pool.length === 0) return undefined;
      return [...pool].sort((a, b) =>
        a.bonus - b.bonus
        || Number(flex.has(b.name)) - Number(flex.has(a.name))
        || b.slot - a.slot
        || a.name.localeCompare(b.name))[0];
    };

    let best: { name: string; victim: typeof incumbents[number]; rank: number } & Priced | undefined;
    for (const cand of Object.keys(base)) {
      if (held.has(cand) || gone.has(cand)) continue;
      const p = price(cand, covered);
      if (p.bonus <= 0) continue;
      const victim = victimFor(cand);
      if (!victim || p.bonus - victim.bonus < bar) continue;
      const rank = base[cand] + p.bonus;
      // Deterministic: adjusted score desc, then name asc — ties must never
      // depend on key insertion order in `base`.
      if (!best || rank > best.rank || (rank === best.rank && cand.localeCompare(best.name) < 0)) {
        best = { name: cand, victim, rank, ...p };
      }
    }
    if (!best) break;
    gone.add(best.victim.name);
    core[best.victim.slot] = best.name;
  }

  // Priced once more against the FINAL six, so the number a row shows is the
  // number that item is worth in the build the reader is looking at.
  const bonuses: Record<string, number> = {};
  const reasons: Record<string, string> = {};
  core.forEach((name, slot) => {
    const others = new Set<string>();
    core.forEach((n, i) => { if (i !== slot) keysOf(n).forEach((k) => others.add(k)); });
    const p = price(name, others);
    if (p.bonus !== 0) { bonuses[name] = p.bonus; reasons[name] = p.why; }
  });

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

/** An item both builds contain, bought at a different point in the order. */
export interface CoreMove {
  name: string;
  /** 1-based position in the un-adapted core. */
  from: number;
  /** 1-based position after the draft overlay. */
  to: number;
  /** Clamped score bonus the overlay gave it — 0 when it moved because
   *  something else did. */
  bonus: number;
  /** Tags/stats that earned the bonus, when it earned one. */
  reason?: string;
}

export interface CoreDiff {
  changes: CoreChange[];
  /** Items in both builds — the part the draft didn't touch. */
  unchanged: string[];
  /** Pushed out with no matching arrival (rare; only on odd-sized diffs). */
  droppedOnly: string[];
  /** Items in BOTH builds whose position changed, earliest arrival first.
   *  Order is a claim the build makes, so a change to it is a change.
   *
   *  EMPTY FOR EVERY DRAFT SINCE 2026-09-03, and that is a property of the
   *  producer rather than of this function: `adaptFromCore` seats an arrival
   *  in the departure's slot and never reorders, because buy order is
   *  `assemble.build_order`'s and the viewer has none of its inputs. Kept
   *  because this function is a diff of any two cores and a caller with two
   *  differently-ordered ones is entitled to the answer. */
  moved: CoreMove[];
  /** Same items, different sequence: `changes` is empty and `moved` is not. */
  orderOnly: boolean;
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

  const basePos = new Map(base.core.map((n, i) => [n, i + 1]));
  const moved: CoreMove[] = [];
  adapted.core.forEach((name, i) => {
    const from = basePos.get(name);
    if (from === undefined || from === i + 1) return;
    moved.push({
      name,
      from,
      to: i + 1,
      bonus: adapted.bonuses[name] ?? 0,
      reason: adapted.reasons[name],
    });
  });

  return {
    changes: added.map((name, i) => ({
      added: name,
      removed: removed[i],
      bonus: adapted.bonuses[name] ?? 0,
      reason: adapted.reasons[name],
    })),
    unchanged: adapted.core.filter((n) => baseSet.has(n)),
    droppedOnly: removed.slice(added.length),
    moved,
    orderOnly: added.length === 0 && removed.length === 0 && moved.length > 0,
  };
}
