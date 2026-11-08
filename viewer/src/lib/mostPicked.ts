/** What a god's own players buy most, from the Conquest community record —
 *  the god page's most-picked list.
 *
 * RANKING. Each item is ranked by its pick rate at its COMMONEST slot: the
 * community entry records, per buy-order slot, the item most players put there
 * (`slot_order[i]`) and the next two (`alternates`), each with the share of
 * this god's players who bought it in that slot. An item can appear in several
 * slots; its highest share is the one ranked and printed ("38% buy it
 * fourth"), because that is a measured number about one slot. Summing an
 * item's slots is NOT done: the record does not say whether those players
 * overlap, so a sum could report more buyers than exist. This is the same
 * dedupe `build_index._attach_popular_items` applies to `popular_items`, done
 * here from the slots so the slot itself can be named.
 *
 * OTHER MODES. SmiteBrain publishes Conquest only, so Joust and Arena show the
 * same Conquest list, labelled as Conquest data. Some of it does not describe
 * what the item does in that mode, and which items is ALREADY DECIDED, with
 * reasons, in `_weights.yaml`: `modes.<mode>.borrow_community.reject_tags`
 * (the tags whose Conquest record the Hybrid refuses to borrow) and
 * `modes.arena.excluded_items` (not in Arena's shop). `build_index` ships both
 * as `community_transfer`; the words below are the reasons written next to
 * them there, and a test fails if a shipped tag has none.
 *
 * Pure. Tested in mostPicked.test.ts.
 */
import type { CommunityBuildEntry, CommunityTransfer, Item } from "../types";

export interface PickedItem {
  name: string;
  /** Share of this god's players who bought it in `slot`. */
  pickRate: number;
  /** 0-based buy-order slot where that share is highest. */
  slot: number;
}

export const ORDINAL = ["first", "second", "third", "fourth", "fifth", "sixth"];

/** Every item the record names, ranked by its peak per-slot pick rate. Ties
 *  break on the earlier slot, then the name, so the list is deterministic. */
export function mostPicked(community?: CommunityBuildEntry): PickedItem[] {
  const best = new Map<string, PickedItem>();
  (community?.slot_order ?? []).forEach((slot, i) => {
    for (const s of [slot, ...(slot.alternates ?? [])]) {
      if (!s?.name || typeof s.pick_rate !== "number") continue;
      const prev = best.get(s.name);
      if (!prev || s.pick_rate > prev.pickRate) best.set(s.name, { name: s.name, pickRate: s.pick_rate, slot: i });
    }
  });
  return [...best.values()].sort((a, b) => b.pickRate - a.pickRate || a.slot - b.slot || a.name.localeCompare(b.name));
}

/** Why Conquest's record doesn't describe an item in this mode. Keys are the
 *  `reject_tags` `build_index` ships, plus `excluded` for an item the mode's
 *  shop does not sell. The sentences are the reasons `_weights.yaml` gives. */
export const TRANSFER_NOTE: Record<string, Record<string, string>> = {
  Joust: {
    mobility: "Rotation items. Conquest's record is a record of rotations, and Joust has no camps or lanes to rotate between.",
  },
  Arena: {
    stacking: "Stacking items. Conquest's record is for a finished stack, and Arena's 17.5-minute match rarely finishes one.",
    mobility: "Rotation items. Arena has no camps or lanes to rotate between.",
    excluded: "Not sold in Arena: there are no wards to place or kill.",
  },
};

/** A tag the viewer has no sentence for still gets a true one. */
export const fallbackNote = (mode: string, from: string) =>
  `Ichor doesn't borrow ${from}'s record for these items in ${mode}.`;

export interface TransferFlag {
  /** Reason key: a tag, or `excluded`. In the order the rule lists them. */
  reason: string;
  items: string[];
  note: string;
}

/** Which listed items Conquest's record does not describe in `mode`, grouped
 *  by reason. Empty in Conquest, and whenever the index ships no rule. */
export function transferFlags(names: string[], mode: string, rule: CommunityTransfer | undefined,
  itemsByName: Record<string, Item>): TransferFlag[] {
  if (!rule) return [];
  const from = rule.from ?? "Conquest";
  const notes = TRANSFER_NOTE[mode] ?? {};
  const flags: TransferFlag[] = [];
  const excluded = new Set(rule.excluded_items ?? []);
  const shut = names.filter((n) => excluded.has(n));
  if (shut.length) flags.push({ reason: "excluded", items: shut, note: notes.excluded ?? `Not sold in ${mode}.` });
  for (const tag of rule.reject_tags ?? []) {
    const hit = names.filter((n) => !excluded.has(n) && (itemsByName[n]?.effect_tags ?? []).includes(tag));
    if (hit.length) flags.push({ reason: tag, items: hit, note: notes[tag] ?? fallbackNote(mode, from) });
  }
  return flags;
}
