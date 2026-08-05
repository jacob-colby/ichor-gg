import type { GodTierEntry } from "../types";
import { LANES, godLane, type Lane } from "./roleAccent";
import { tierStep, TIER_STEPS, type TierLetter } from "./tierBands";

/**
 * The board, per lane, ranked by how gods actually perform.
 *
 * This replaces `divergence.ts`, which ranked lanes by how far our model
 * disagreed with the community and led the site with the result. The
 * disagreement was not evidence of anything: our god score correlated −0.117
 * with real god strength, and 59% of gods "placed differently" against the
 * 75% two unrelated rankings would produce. See `pipeline/smite/tierlist.py`.
 *
 * WHAT SURVIVED, AND WHY IT IS DIFFERENT
 *
 * "Underrated" is still here, but it is now a claim about the community's own
 * two numbers rather than about our disagreement with them: a god in the top
 * third by measured performance and the bottom third by how often it is
 * actually played. We are not saying we know better — we are pointing at a
 * gap inside their data.
 *
 * That claim survives the obvious objection. The usual worry is specialist
 * bias: rare gods look strong because only devotees play them. Measured on
 * this data the relationship runs the other way — play share against raw win
 * rate is +0.25, so popular gods win slightly MORE. And because the ranking
 * is a Wilson lower bound, a thin sample is already penalised (play share
 * against interval width is −0.999). A rarely-played god has to clear the bar
 * *despite* that penalty, which makes this flag conservative rather than a
 * machine for promoting noise.
 */
export interface Standing {
  name: string;
  lane: Lane | undefined;
  /** Wilson lower bound — the ranking. */
  score: number;
  /** Raw observed rate. Shown, never ranked on. */
  winRate: number | null;
  matches: number | null;
  /** Share of analysed matches this god appeared in. */
  playShare: number | null;
  band: TierLetter;
  /** Ladder position, C=0 … S=3. */
  step: number;
  /** Top third by performance, bottom third by play. */
  underplayed: boolean;
}

export interface LaneColumn {
  lane: Lane;
  rows: Standing[];
  /** Gods in this lane with no usable sample. */
  unmeasured: number;
}

export interface StandingsBoard {
  lanes: LaneColumn[];
  total: number;
  /** Gods with a real sample — the only ones placed at all. */
  ranked: number;
  unmeasured: number;
  /** Gods that perform well and are rarely played. */
  underplayed: number;
  /** God-match APPEARANCES the board rests on — the per-god samples summed.
   *  NOT the number of matches analysed: ten gods play every match, so this
   *  counts each separately and runs several times the match count. Labelling
   *  it "matches" put 22,840 on the same screen as the source line's 4,952 —
   *  one fact stated two incompatible ways. */
  appearances: number;
}

/** Best first, then most-played, then name — stable across renders. */
function byScore(a: Standing, b: Standing): number {
  const d = b.score - a.score;
  if (d !== 0) return d;
  const m = (b.matches ?? 0) - (a.matches ?? 0);
  if (m !== 0) return m;
  return a.name.localeCompare(b.name);
}

/** Value at a fraction through a sorted copy. Terciles are computed over the
 *  gods that HAVE the number, so a missing play share can never make a god
 *  look rare. */
function quantile(sorted: number[], q: number): number | null {
  if (sorted.length === 0) return null;
  const i = Math.min(sorted.length - 1, Math.max(0, Math.floor(q * sorted.length)));
  return sorted[i];
}

/** Fewest measured gods before terciles mean anything. Below this a "bottom
 *  third" is one or two names and the label is noise. */
export const MIN_FOR_TERCILES = 6;

/** The gods that win well and are rarely played, by name.
 *
 * Shared with the tier list so the two surfaces cannot disagree about who is
 * flagged. Computed over the WHOLE measured set, never a filtered view: "rare"
 * is a fact about the roster, and recomputing it inside a lane filter would
 * make Solo's quietest god look rare among five names.
 */
export function findUnderplayed(entries: GodTierEntry[] | undefined): Set<string> {
  const measured = (entries ?? []).filter(
    (e) => e.score != null && e.tier_score != null && typeof e.play_share === "number",
  );
  if (measured.length < MIN_FOR_TERCILES) return new Set();

  const scores = measured.map((e) => e.score!).sort((a, b) => a - b);
  const shares = measured.map((e) => e.play_share!).sort((a, b) => a - b);
  const strongFrom = quantile(scores, 2 / 3);
  const rareBelow = quantile(shares, 1 / 3);
  // With no spread in play share the bottom-third cut lands on the same value
  // as the top, and every god would qualify. A roster where everyone is played
  // equally has nobody who is rarely played.
  if (strongFrom == null || rareBelow == null || rareBelow >= shares[shares.length - 1]) {
    return new Set();
  }
  return new Set(
    measured
      .filter((e) => e.score! >= strongFrom && e.play_share! <= rareBelow)
      .map((e) => e.name),
  );
}

export function buildStandingsBoard(entries: GodTierEntry[] | undefined): StandingsBoard {
  const empty: StandingsBoard = {
    lanes: [], total: 0, ranked: 0, unmeasured: 0, underplayed: 0, appearances: 0,
  };
  if (!entries || entries.length === 0) return empty;

  const underplayedNames = findUnderplayed(entries);

  const unmeasuredByLane = new Map<Lane, number>();
  const rowsByLane = new Map<Lane, Standing[]>();
  for (const lane of LANES) {
    unmeasuredByLane.set(lane, 0);
    rowsByLane.set(lane, []);
  }

  let ranked = 0;
  let unmeasured = 0;
  let underplayed = 0;
  let appearances = 0;

  for (const e of entries) {
    const lane = godLane(e.role);
    const step = tierStep(e.tier_score);
    if (e.score == null || e.tier_score == null || step == null) {
      unmeasured += 1;
      if (lane) unmeasuredByLane.set(lane, (unmeasuredByLane.get(lane) ?? 0) + 1);
      continue;
    }
    ranked += 1;
    appearances += e.matches ?? 0;
    const isUnderplayed = underplayedNames.has(e.name);
    if (isUnderplayed) underplayed += 1;
    if (lane) {
      rowsByLane.get(lane)!.push({
        name: e.name,
        lane,
        score: e.score,
        winRate: typeof e.win_rate === "number" ? e.win_rate : null,
        matches: typeof e.matches === "number" ? e.matches : null,
        playShare: typeof e.play_share === "number" ? e.play_share : null,
        band: e.tier_score,
        step,
        underplayed: isUnderplayed,
      });
    }
  }

  const lanes: LaneColumn[] = LANES.map((lane) => ({
    lane,
    rows: rowsByLane.get(lane)!.sort(byScore),
    unmeasured: unmeasuredByLane.get(lane) ?? 0,
  })).filter((c) => c.rows.length > 0 || c.unmeasured > 0);

  return { lanes, total: entries.length, ranked, unmeasured, underplayed, appearances };
}

/** Where a rung sits along the track, as a percentage — the centre of its
 * cell, so a mark never straddles two tiers. */
export function stepPercent(step: number): number {
  return ((step + 0.5) / TIER_STEPS) * 100;
}

/** A rate as a whole-number percentage, em dash when absent. */
export function rateText(rate: number | null | undefined): string {
  return rate == null ? "—" : `${Math.round(rate * 100)}%`;
}

/** Sample size, abbreviated the way a scoreboard would. */
export function matchesText(n: number | null | undefined): string {
  if (n == null) return "—";
  return n >= 1000 ? `${(n / 1000).toFixed(1)}k` : String(n);
}
