/** Where one god sits in the model's ranking, and how far the meta disagrees.
 *
 * The tier list answers this for all 87 at once; from a god's own page there
 * was no way to ask it about that god. Everything here is derived from the same
 * `tierlist` slice the tier list reads, so the two surfaces can never drift.
 */
import type { GodTierEntry } from "../types";
import { godInLane, type Lane } from "./roleAccent";
import { TIERS, type TierLetter } from "./tierBands";

export interface Neighbour {
  name: string;
  ours: number;
  /** Score gap to the subject; positive means this god scores higher. */
  gap: number;
}

export interface GodRanking {
  entry: GodTierEntry;
  /** 1-based position across every god the model scored. */
  overall: number | null;
  scored: number;
  /** Position inside the god's own model tier band. */
  inBand: number | null;
  bandSize: number;
  band: TierLetter | null;
  /** Position among gods sharing this lane. Null when the god has no lane. */
  inLane: number | null;
  laneSize: number;
  lane: Lane | null;
  /** ours - community, or null when the community hasn't rated this god. */
  delta: number | null;
  /** Tier letters apart, signed: positive means the model ranks it higher. */
  tierGap: number | null;
  unranked: boolean;
  agrees: boolean;
  /** The god immediately above and below on the model's scale. */
  above?: Neighbour;
  below?: Neighbour;
}

const TIER_INDEX: Record<TierLetter, number> = { S: 0, A: 1, B: 2, C: 3 };

/** Rank within a list already sorted best-first, or null if absent. */
function positionOf(sorted: GodTierEntry[], name: string): number | null {
  const i = sorted.findIndex((e) => e.name === name);
  return i < 0 ? null : i + 1;
}

const byScore = (a: GodTierEntry, b: GodTierEntry) =>
  (b.ours ?? -Infinity) - (a.ours ?? -Infinity) || a.name.localeCompare(b.name);

export function buildGodRanking(
  entries: GodTierEntry[] | undefined,
  godName: string,
  lane: Lane | null,
): GodRanking | null {
  const all = (entries ?? []).filter((e) => e.ours != null);
  const entry = all.find((e) => e.name === godName);
  // A god the model hasn't scored has no position to report. Callers say so in
  // words rather than rendering a page of dashes.
  if (!entry) return null;

  const sorted = [...all].sort(byScore);
  const overall = positionOf(sorted, godName);

  const band = (entry.tier_ours ?? null) as TierLetter | null;
  const inBandList = band ? sorted.filter((e) => e.tier_ours === band) : [];
  const laneList = lane ? sorted.filter((e) => godInLane(e.role, lane)) : [];

  const commIdx = entry.tier_community ? TIER_INDEX[entry.tier_community as TierLetter] : null;
  const oursIdx = band ? TIER_INDEX[band] : null;
  const unranked = entry.community == null || entry.tier_community == null;

  const i = overall != null ? overall - 1 : -1;
  const near = (n: GodTierEntry | undefined): Neighbour | undefined =>
    n && n.ours != null && entry.ours != null
      ? { name: n.name, ours: n.ours, gap: n.ours - entry.ours } : undefined;

  return {
    entry,
    overall,
    scored: sorted.length,
    inBand: band ? positionOf(inBandList, godName) : null,
    bandSize: inBandList.length,
    band,
    inLane: lane ? positionOf(laneList, godName) : null,
    laneSize: laneList.length,
    lane,
    delta: entry.ours != null && entry.community != null ? entry.ours - entry.community : null,
    // S=0..C=3, so a smaller index is a better tier: the model ranks it higher
    // when the community's index is larger.
    tierGap: oursIdx != null && commIdx != null ? commIdx - oursIdx : null,
    unranked,
    agrees: !unranked && entry.tier_ours === entry.tier_community,
    above: i > 0 ? near(sorted[i - 1]) : undefined,
    below: i >= 0 && i < sorted.length - 1 ? near(sorted[i + 1]) : undefined,
  };
}

/** Percentile from the top, as a whole number. "12th of 87" is exact but hard
 *  to feel; "top 14%" is the sentence people actually repeat. */
export function topPercent(overall: number, scored: number): number {
  if (scored <= 0) return 0;
  return Math.max(1, Math.round((overall / scored) * 100));
}

export const BAND_ORDER = TIERS;
