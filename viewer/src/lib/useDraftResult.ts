/** The draft's whole derivation, in one place.
 *
 * Two surfaces now render a view of "what has the draft done" — the full
 * `/draft` page and the persistent `DraftDock` in the shell. They have to
 * agree on every number: if the dock says "2 of 6 items moved" and the page
 * says something else for the same board, the product's central claim has
 * drifted from itself. So the derivation lives once, here, and both surfaces
 * call it rather than each computing their own.
 */
import { useMemo } from "react";
import type { BuildNote, CuratedBuildEntry, DraftComp, DraftConfig, God, Item } from "../types";
import { deriveThreats, threatOverlay, threatCulprits, type ThreatKey } from "./threats";
import { adaptedCore, diffCore, type AdaptedCore, type CoreDiff } from "./draftBuild";
import type { DraftMode } from "./draft";

const MODE_LABEL: Record<DraftMode, string> = { conquest: "Conquest", joust: "Joust" };

/** Mirrors the `lifesteal_caps` rule in _weights.yaml. */
function draftMaxLifesteal(godData?: God): number {
  if (!godData || godData.damage_type !== "physical") return 1;
  const tokens = new Set([...(godData.role ?? "").split(/\s+/), ...(godData.specializations ?? [])]);
  return ["Carry", "Hunter", "Sharpshooter"].some((t) => tokens.has(t)) ? 2 : 1;
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
  /** Already on the board — SMITE forbids duplicates. */
  taken: Set<string>;
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
  coreSize: number;
}

export function useDraftResult(
  draft: DraftComp, mode: DraftMode,
  gods: God[], items: Item[], builds: BuildNote[],
  godItemScores: Record<string, Record<string, number>> | undefined,
  draftConfig: DraftConfig | undefined,
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

  const allyCores = useMemo(() => {
    const out: Record<string, string[]> = {};
    for (const name of draft.allies) {
      if (name) out[name] = allyEffectTags(name, MODE_LABEL[mode], builds, itemsByName);
    }
    return out;
  }, [draft.allies, builds, itemsByName, mode]);

  const threats = useMemo(() => deriveThreats(draft, godsByName, allyCores), [draft, godsByName, allyCores]);
  const culprits = useMemo(() => threatCulprits(draft, godsByName), [draft, godsByName]);

  const draftEnabled = !!meName && !!godItemScores?.[meName] && !!draftConfig;
  const result = useMemo(() => {
    if (!draftEnabled) return null;
    const opts = { maxBonus: draftConfig!.max_bonus, maxLifesteal: draftMaxLifesteal(meGod) };
    const base = adaptedCore(godItemScores![meName], itemsByName, { tags: {}, stats: {} }, opts);
    const adapted = adaptedCore(godItemScores![meName], itemsByName, threatOverlay(threats, draftConfig!), opts);
    // Both builds survive: the diff is the product's whole claim.
    return { base, adapted, diff: diffCore(base, adapted) };
  }, [draftEnabled, draftConfig, godItemScores, meName, itemsByName, threats, meGod]);

  const taken = useMemo(
    () => new Set([...draft.allies, ...draft.enemies].filter(Boolean)),
    [draft.allies, draft.enemies],
  );

  return {
    meName, meGod, godsByName, itemsByName, taken,
    enemiesKnown: threats.enemyCount, roster: threats.rosterSize,
    threatCulprits: culprits,
    allyAllPhysical: threats.allyAllPhysical, allyCount: threats.allyCount, allyPhysical: threats.allyPhysical,
    result, draftEnabled,
    changeCount: result?.diff.changes.length ?? 0,
    coreSize: result?.adapted.core.length ?? 6,
  };
}
