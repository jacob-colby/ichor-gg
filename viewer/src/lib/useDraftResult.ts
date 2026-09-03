/** The draft's whole derivation, in one place.
 *
 * Two surfaces now render a view of "what has the draft done" — the full
 * `/draft` page and the persistent `DraftDock` in the shell. They have to
 * agree on every number: if the dock says "2 of 6 items moved" and the page
 * says something else for the same board, the product's central claim has
 * drifted from itself. So the derivation lives once, here, and both surfaces
 * call it rather than each computing their own.
 */
import { useCallback, useMemo } from "react";
import type { BuildNote, CuratedBuildEntry, DraftComp, DraftConfig, God, Item, LifestealCap } from "../types";
import { deriveThreats, threatOverlay, damageOverlay, threatCulprits, type ThreatKey } from "./threats";
import { adaptedCore, diffCore, type AdaptedCore, type CoreDiff } from "./draftBuild";
import type { DraftMode } from "./draft";
import { groupStarters, type StarterPath } from "./starters";

const MODE_LABEL: Record<DraftMode, string> = { conquest: "Conquest", joust: "Joust", arena: "Arena" };

/** Applies the shipped `lifesteal_caps` rules — the same data `god_max_lifesteal`
 *  reads, in the same first-match-wins order.
 *
 *  This used to hardcode the rule's conditions (physical, and one of
 *  Carry/Hunter/Sharpshooter, cap 2). That is a copy of a YAML row living in
 *  TypeScript, and nothing would have failed if someone edited the row: the
 *  pipeline would assemble cores under the new cap and the draft would keep
 *  re-ranking them under the old one, disagreeing quietly on the surface whose
 *  whole claim is "here is what changed". */
export function draftMaxLifesteal(godData: God | undefined, rules: LifestealCap[] | undefined): number {
  if (!godData) return 1;
  const tokens = new Set([...(godData.role ?? "").split(/\s+/), ...(godData.specializations ?? [])]);
  for (const rule of rules ?? []) {
    if (rule.damage_types?.length && !rule.damage_types.includes(godData.damage_type)) continue;
    if (rule.match_any?.length && !rule.match_any.some((t) => tokens.has(t))) continue;
    return rule.max_lifesteal ?? 1;
  }
  return 1;
}

/** An ally's own suggested core reduced to the effect_tags its items bring —
 *  the "team responsibility" signal that tells a covered job from a gap. */
function allyEffectTags(
  allyName: string, modeLabel: string, builds: BuildNote[], itemsByName: Record<string, Item>,
): string[] {
  const notes = builds.filter((b) => b.god === allyName);
  const note = notes.find((n) => n.mode === modeLabel) ?? notes[0];
  if (!note) return [];
  const core = note.builds.find(
    (b) => b.source === "suggested" && (b as CuratedBuildEntry).archetype === "core" && !(b as CuratedBuildEntry).fun,
  ) as CuratedBuildEntry | undefined;
  if (!core) return [];
  const tags = new Set<string>();
  for (const name of core.slot_order) {
    for (const t of itemsByName[name]?.effect_tags ?? []) tags.add(t);
  }
  return [...tags];
}

export interface DraftResult {
  meName: string;
  meGod?: God;
  godsByName: Record<string, God>;
  itemsByName: Record<string, Item>;
  /** Everyone on the board, either side. Only for "is the board empty" —
   *  NOT for deciding what can be picked; see `takenFor`. */
  taken: Set<string>;
  /** What your god's players open with, top 3 by pick rate. A build starts
   *  before item one and this page began at item one, so the first purchase of
   *  the match was the one thing it never showed. */
  /** Openers grouped into purchase paths — Leather Cowl and Hunter's Cowl are
   *  one opener, not two, and 84 of 89 gods had both halves in a three-slot
   *  list. See lib/starters.ts. */
  starters: StarterPath[];
  /** True when `starters` came from Conquest because the selected mode has no
   *  community data of its own. The row has to say so — see `starters`. */
  startersAreConquest: boolean;
  /** Relics this comp calls for. Not part of the core: `is_buildable` excludes
   *  relics from the six slots because the game gives them their own, so the
   *  tag overlay could never have recommended one. */
  relicPicks: { item: string; because: string; threat: string; count: number }[];
  /** The aspect is on and moved the build (only 7 gods have an overlay). */
  aspectScored: boolean;
  /** Gods a given slot may not take: the ones already on THAT team, minus
   *  whoever currently occupies the slot being edited.
   *
   *  Per TEAM, not per board. A team cannot field two Ymirs, but the two
   *  teams can absolutely mirror each other — every non-draft queue allows
   *  it, and Joust and Arena are non-draft. Blocking it board-wide made a
   *  legal and very common comp unenterable, and quietly asserted that this
   *  tool only models ranked Conquest. */
  takenFor: (kind: "ally" | "enemy", index: number) => Set<string>;
  enemiesKnown: number;
  roster: number;
  threatCulprits: Record<ThreatKey, string[]>;
  allyAllPhysical: boolean;
  allyCount: number;
  allyPhysical: number;
  /** Present once the you-slot is scored; absent gods (no `god_item_scores`
   *  entry, or no draftConfig at all) leave this null. */
  result: { base: AdaptedCore; adapted: AdaptedCore; diff: CoreDiff } | null;
  draftEnabled: boolean;
  changeCount: number;
  /** Items in both builds bought at a different point. A draft that only
   *  reorders is an adaptation, and the dock used to call it "nothing". */
  moveCount: number;
  coreSize: number;
}

export function useDraftResult(
  draft: DraftComp, mode: DraftMode,
  gods: God[], items: Item[], builds: BuildNote[],
  godItemScores: Record<string, Record<string, Record<string, number>>> | undefined,
  draftConfig: DraftConfig | undefined,
  godItemDamage?: Record<string, Record<string, [number, number]>>,
  /** Build for your god's aspect. Only the 7 gods with a hand-tuned overlay
   *  have an `<mode>:aspect` table; for anyone else this is inert by
   *  construction rather than by a separate guard. */
  aspectOn = false,
): DraftResult {
  const godsByName = useMemo(() => {
    const m: Record<string, God> = {};
    for (const g of gods) m[g.name] = g;
    return m;
  }, [gods]);
  const itemsByName = useMemo(() => {
    const m: Record<string, Item> = {};
    for (const it of items) m[it.name] = it;
    return m;
  }, [items]);

  const meName = draft.allies[0];
  const meGod = godsByName[meName];

  /** Openers for the selected mode, falling back to Conquest's.
   *
   *  Joust and Arena build notes carry NO community build at all — SmiteBrain
   *  is Conquest-only — so the mode-scoped lookup found nothing and the whole
   *  "Opens with" row silently vanished the moment you switched to Joust.
   *
   *  Conquest's openers are a real answer for the other modes (a Warrior's Axe
   *  opener is a Warrior's Axe opener), just not a measured one, so they are
   *  shown WITH the fallback flagged rather than dropped or passed off as
   *  native. Same judgement the build pages already make about Joust. */
  const { starters, startersAreConquest } = useMemo(() => {
    const openersFor = (label: string) => {
      const note = builds.find((b) => b.god === meName && b.mode === label);
      const community = note?.builds.find((b) => b.source === "community");
      return (community as { community_starters?: { name: string; pick_rate: number; win_rate: number }[] })
        ?.community_starters ?? [];
    };
    const own = openersFor(MODE_LABEL[mode]);
    if (own.length > 0 || MODE_LABEL[mode] === "Conquest") {
      return { starters: groupStarters(own, itemsByName), startersAreConquest: false };
    }
    const fallback = openersFor("Conquest");
    return {
      starters: groupStarters(fallback, itemsByName),
      startersAreConquest: fallback.length > 0,
    };
  }, [builds, meName, mode, itemsByName]);

  const allyCores = useMemo(() => {
    const out: Record<string, string[]> = {};
    for (const name of draft.allies) {
      if (name) out[name] = allyEffectTags(name, MODE_LABEL[mode], builds, itemsByName);
    }
    return out;
  }, [draft.allies, builds, itemsByName, mode]);

  const threats = useMemo(() => deriveThreats(draft, godsByName, allyCores), [draft, godsByName, allyCores]);

  /** A comp can call for a relic the build itself can never contain. Walls are
   *  the case that forced this: four gods create one, no role label describes
   *  it, and the only counter (Shell of Rebuke's passthrough field) is a relic.
   *  Keyed off the same threat counts the core overlay uses, so the two can
   *  never disagree about what the enemy is. */
  const relicPicks = useMemo(() => {
    const counts = threats as unknown as Record<string, number>;
    return Object.entries(draftConfig?.relics ?? {})
      .map(([threat, rec]) => ({ ...rec, threat, count: counts[threat] ?? 0 }))
      .filter((r) => r.count > 0)
      .sort((a, b) => b.count - a.count || a.item.localeCompare(b.item));
  }, [draftConfig, threats]);
  const culprits = useMemo(() => threatCulprits(draft, godsByName), [draft, godsByName]);

  // Scored items for THIS mode, and this god's aspect if they have one.
  // Conquest's table used to be the only one, so the Joust toggle changed the
  // label and left the model alone.
  const byMode = godItemScores?.[meName];
  const modeScores = (aspectOn ? byMode?.[`${mode}:aspect`] : undefined) ?? byMode?.[mode];
  /** True when the aspect is on AND actually has a table behind it — the
   *  board says which of the two it is rather than leaving a pressed control
   *  that changed nothing. */
  const aspectScored = aspectOn && !!byMode?.[`${mode}:aspect`];
  const draftEnabled = !!meName && !!modeScores && !!draftConfig;
  const result = useMemo(() => {
    if (!draftEnabled) return null;
    const opts = {
      maxBonus: draftConfig!.max_bonus,
      maxLifesteal: draftMaxLifesteal(meGod, draftConfig!.lifesteal_caps),
      // Defaults to 1 (pay in full) on an index built before the rule shipped,
      // so an older data file keeps behaving exactly as it did.
      selfCovered: draftConfig!.self_covered ?? 1,
    };
    const base = adaptedCore(modeScores!, itemsByName, { tags: {}, stats: {} }, opts);
    const overlay = threatOverlay(threats, draftConfig!, meGod);
    overlay.items = damageOverlay(threats, godItemDamage?.[meName], draftConfig!);
    const adapted = adaptedCore(modeScores!, itemsByName, overlay, opts);
    // Both builds survive: the diff is the product's whole claim.
    return { base, adapted, diff: diffCore(base, adapted) };
  }, [draftEnabled, draftConfig, modeScores, godItemDamage, meName, itemsByName, threats, meGod]);

  const taken = useMemo(
    () => new Set([...draft.allies, ...draft.enemies].filter(Boolean)),
    [draft.allies, draft.enemies],
  );

  const takenFor = useCallback(
    (kind: "ally" | "enemy", index: number) => {
      const side = kind === "ally" ? draft.allies : draft.enemies;
      // The slot's own occupant is excluded, so re-opening a filled slot
      // doesn't show the god sitting in it greyed out.
      return new Set(side.filter((n, i) => n && i !== index) as string[]);
    },
    [draft.allies, draft.enemies],
  );

  return {
    meName, meGod, godsByName, itemsByName, taken, takenFor, starters, startersAreConquest,
    relicPicks, aspectScored,
    enemiesKnown: threats.enemyCount, roster: threats.rosterSize,
    threatCulprits: culprits,
    allyAllPhysical: threats.allyAllPhysical, allyCount: threats.allyCount, allyPhysical: threats.allyPhysical,
    result, draftEnabled,
    changeCount: result?.diff.changes.length ?? 0,
    moveCount: result?.diff.moved.length ?? 0,
    coreSize: result?.adapted.core.length ?? 6,
  };
}
