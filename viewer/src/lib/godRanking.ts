/** Where one god sits in the standings, and what that placement rests on.
 *
 * The tier list answers this for all 87 at once; from a god's own page there
 * was no way to ask it about that god. Everything here is derived from the same
 * `tierlist` slice the tier list reads, so the two surfaces can never drift.
 *
 * This used to be a comparison — our placement against the community's, with
 * the gap between them as the headline. That gap did not survive measurement
 * (see `pipeline/smite/tierlist.py`), so what is left is the one ranking there
 * is: real wins over real matches, with the sample size kept in view.
 */
import type { GodTierEntry } from "../types";
import { godInLane, type Lane } from "./roleAccent";
import { TIERS, type TierLetter } from "./tierBands";

export interface Neighbour {
  name: string;
  score: number;
  winRate: number | null;
  /** Score gap to the subject; positive means this god ranks higher. */
  gap: number;
}

export interface GodRanking {
  entry: GodTierEntry;
  /** 1-based position across every god with a measured record. */
  overall: number | null;
  scored: number;
  /** Position inside the god's own band. */
  inBand: number | null;
  bandSize: number;
  band: TierLetter | null;
  /** Position among gods sharing this lane. Null when the god has no lane. */
  inLane: number | null;
  laneSize: number;
  lane: Lane | null;
  /** No usable sample — placed nowhere rather than placed last. */
  unmeasured: boolean;
  /** The god immediately above and below on the measured scale. */
  above?: Neighbour;
  below?: Neighbour;
}

/** Rank within a list already sorted best-first, or null if absent. */
function positionOf(sorted: GodTierEntry[], name: string): number | null {
  const i = sorted.findIndex((e) => e.name === name);
  return i < 0 ? null : i + 1;
}

const byScore = (a: GodTierEntry, b: GodTierEntry) =>
  (b.score ?? -Infinity) - (a.score ?? -Infinity) || a.name.localeCompare(b.name);

export function buildGodRanking(
  entries: GodTierEntry[] | undefined,
  godName: string,
  lane: Lane | null,
): GodRanking | null {
  const all = entries ?? [];
  const entry = all.find((e) => e.name === godName);
  // A god absent from this mode's list has no position to report at all.
  // Callers say so in words rather than rendering a page of dashes.
  if (!entry) return null;

  // A god with no sample is still a real entry — it just isn't placed. It sits
  // out the ordering rather than sinking to the bottom of it, because
  // "unmeasured" and "worst" are different facts.
  const measured = all.filter((e) => e.score != null);
  const unmeasured = entry.score == null;
  const sorted = [...measured].sort(byScore);
  const overall = unmeasured ? null : positionOf(sorted, godName);

  const band = (entry.tier_score ?? null) as TierLetter | null;
  const inBandList = band ? sorted.filter((e) => e.tier_score === band) : [];
  const laneList = lane ? sorted.filter((e) => godInLane(e.role, lane)) : [];

  const i = overall != null ? overall - 1 : -1;
  const near = (n: GodTierEntry | undefined): Neighbour | undefined =>
    n && n.score != null && entry.score != null
      ? {
          name: n.name,
          score: n.score,
          winRate: typeof n.win_rate === "number" ? n.win_rate : null,
          gap: n.score - entry.score,
        }
      : undefined;

  return {
    entry,
    overall,
    scored: sorted.length,
    inBand: band && !unmeasured ? positionOf(inBandList, godName) : null,
    bandSize: inBandList.length,
    band,
    inLane: lane && !unmeasured ? positionOf(laneList, godName) : null,
    laneSize: laneList.length,
    lane,
    unmeasured,
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
