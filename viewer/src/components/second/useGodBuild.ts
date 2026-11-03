/** Everything a surface needs to show one god's six against one team.
 *
 * Lifted out of the god page so the match board and the god page compute the
 * SAME six from the same inputs: the `model` archetype (passed into
 * useDraftResult explicitly), adapted by whatever enemies the comp carries,
 * compared against `/side_by_side`. Two surfaces, one answer. */
import { useEffect, useState } from "react";
import type { BuildNote, CommunityBuildEntry, CuratedBuildEntry, DraftComp, God, IndexData } from "../../types";
import { useDraftResult } from "../../lib/useDraftResult";
import { tabLabel } from "../../lib/builds";
import { useComparison } from "./useComparison";
import { verdictSentence, MODE_NAME } from "./verdict";
import { itemReason, type ItemReason } from "./itemReason";
import { MAIN_ARCHETYPE, type PageQuery } from "./pageState";

const sameOrder = (a: string[] = [], b: string[] = []) => a.length === b.length && a.every((x, i) => x === b[i]);

function noteFor(builds: BuildNote[], god: string, label: string) {
  return builds.find((b) => b.god === god && b.mode === label);
}

export interface SixRow {
  name: string; position: number; cumulative: number | null; reason: ItemReason; swapped: boolean;
}

export function useGodBuild(god: God, data: IndexData, q: PageQuery, comp: DraftComp) {
  const { mode } = q;
  const modeLabel = MODE_NAME[mode];

  const r = useDraftResult(comp, mode, data.gods, data.items, data.builds, data.god_item_scores,
    data.draft, data.god_item_damage, q.aspect, q.build);

  // ── Builds, community, aspect ──────────────────────────────────────────
  const note = noteFor(data.builds, god.name, modeLabel);
  const community = noteFor(data.builds, god.name, "Conquest")?.builds
    .find((b) => b.source === "community") as CommunityBuildEntry | undefined;
  const archetype = r.activeEntry?.archetype ?? q.build;
  const isMain = archetype === MAIN_ARCHETYPE;
  const aspectName = god.aspects?.[0]?.name ?? null;
  const suggested = (note?.builds ?? []).filter((b) => b.source === "suggested") as CuratedBuildEntry[];
  const baseOfArch = suggested.find((b) => b.archetype === archetype && !b.aspect);
  const aspectOfArch = suggested.find((b) => b.archetype === archetype && !!b.aspect);
  const aspectChangesBuild = !!aspectOfArch && !sameOrder(aspectOfArch.slot_order, baseOfArch?.slot_order);
  const aspectOnBuild = q.aspect && r.aspectScored && aspectChangesBuild;

  // ── Comparison + verdict ───────────────────────────────────────────────
  const cmp = useComparison(god.name);
  const shipped = (r.activeEntry?.slot_order as string[] | undefined) ?? [];
  const verdictLoading = mode === "conquest" && cmp.loading;
  const verdict = verdictLoading ? null : verdictSentence({
    d: cmp.data, god: god.name, mode, archetype, shownSix: shipped,
    aspectBuild: aspectOnBuild ? aspectName : null, band: cmp.meta?.band, draftSwaps: r.changeCount,
  });
  const canSwap = mode === "conquest" && isMain && !aspectOnBuild && !!cmp.data;
  const [theirs, setTheirs] = useState(false);
  const showTheirs = theirs && canSwap;
  useEffect(() => { setTheirs(false); }, [god.name]);

  // ── The six on screen ──────────────────────────────────────────────────
  const swaps = new Map((r.result?.diff.changes ?? []).map((c) => [c.added, c]));
  const six = showTheirs ? cmp.data!.community.items : (r.result?.adapted.core ?? shipped);
  let running = 0;
  let unknownCost = false;
  const rows: SixRow[] = six.map((name, i) => {
    const item = r.itemsByName[name];
    if (item?.cost == null) unknownCost = true;
    running += item?.cost ?? 0;
    const swap = showTheirs ? undefined : swaps.get(name);
    return {
      name, position: i + 1, cumulative: unknownCost ? null : running,
      reason: itemReason(name, { god: god.name, mode, community, item, swap }), swapped: !!swap,
    };
  });

  const starter = showTheirs ? community?.starter : (r.activeEntry?.starter ?? community?.starter);
  const starterPath = starter ? r.starters.find((p) => p.rootName === starter.base) : undefined;

  // ── Header facts ───────────────────────────────────────────────────────
  // Conquest's slice, or the top level on an index that predates per-mode
  // slices (it mirrored Conquest). Never another mode's: only Conquest has
  // outcome data.
  const tier = (data.tierlist?.conquest ?? data.tierlist)?.gods.find((g) => g.name === god.name);
  const ranked = mode === "conquest" && !!tier?.tier_score;
  const record = mode !== "conquest"
    ? `No win data in ${modeLabel} — model only`
    : tier?.tier_score
      ? `Tier ${tier.tier_score} on ${(tier.matches ?? 0).toLocaleString("en-US")} Conquest games`
      : "Not enough Conquest games to rank";

  const kitLine = cmp.data?.kit
    ? cmp.data.kit.kit === "base"
      ? `Measured on the base kit${cmp.data.kit.aspect && cmp.data.kit.pick_rate != null
        ? `; ${Math.round(cmp.data.kit.pick_rate * 100)}% of ${god.name} players run ${cmp.data.kit.aspect}` : ""}.`
      : `Measured on ${cmp.data.kit.aspect}.`
    : undefined;

  const buildLabel = (a?: string) => (a === MAIN_ARCHETYPE ? "Ichor's main six" : r.archetypes.find((e) => e.archetype === a)
    ? tabLabel(r.archetypes.find((e) => e.archetype === a)!) : a ?? "");
  const listLabel = showTheirs ? "The community's six" : isMain ? "Ichor's six" : `${buildLabel(archetype)} build`;

  return {
    r, mode, modeLabel, community, archetype, isMain, aspectName, aspectChangesBuild,
    cmp, verdict, verdictLoading, canSwap, showTheirs, setTheirs,
    rows, starter, starterPath, ranked, record, kitLine, buildLabel, listLabel,
  };
}

export type GodBuild = ReturnType<typeof useGodBuild>;
