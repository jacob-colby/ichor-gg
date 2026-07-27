import type { GodTierEntry } from "../types";
import { LANES, godLane, type Lane } from "./roleAccent";
import { tierStep, verdictOf, TIER_STEPS, type TierLetter, type Verdict } from "./tierBands";

/** One god both sources have placed, positioned on the tier ladder.
 *
 * **The tier letters own the verdict, not the score gap.** The two measures
 * genuinely disagree near a band boundary — a god can sit 0.00 apart on raw
 * score while the letters say we rank it a full tier higher — and the tier
 * list already resolved that conflict in the letters' favour (see
 * `TierList.divergenceClass`). Placing the bar by score while labelling it by
 * letter would have drawn a green "underrated" row with its mark to the left
 * of the community's. Everything here keys off the letters so the mark, the
 * colour and the word can't contradict each other.
 *
 * The raw scores survive as `delta`, which still breaks ties in the ordering
 * and still reaches the reader through the row's accessible name — demoted,
 * not deleted. */
export interface Divergence {
  name: string;
  lane: Lane | undefined;
  ours: number;
  community: number;
  /** ours - community, on raw scores. A tiebreak and a detail, no longer the
   * thing the bar draws — the two sources' scores aren't on a shared scale. */
  delta: number;
  tierOurs: TierLetter;
  tierCommunity: TierLetter;
  /** Rungs apart, signed: positive means we place it above the community. */
  tierGap: number;
  /** Ladder positions, C=0 … S=3. `ourStep` is the claim; `theirStep` is the
   * baseline the reader already has in their head. */
  ourStep: number;
  theirStep: number;
  verdict: Verdict;
  tierDisagrees: boolean;
}

/** One lane's slice of the board. */
export interface LaneColumn {
  lane: Lane;
  rows: Divergence[];
  /** Gods in this lane with no community score to compare against. */
  unranked: number;
}

export interface DivergenceBoard {
  lanes: LaneColumn[];
  /** Every god in the tier list, whether or not the community has scored it. */
  total: number;
  /** Gods with both placements — the only ones we can honestly compare. */
  ranked: number;
  unranked: number;
  /** Ranked gods whose model tier letter differs from the community's. */
  tierDisagreements: number;
}

/** Biggest argument first: how many rungs apart the two sources are, with the
 * raw score gap only breaking ties between equal-sized arguments. Ties break
 * on name so the order is stable across renders and refreshes.
 *
 * Ordering on the score gap alone contradicted the bars it ordered, once the
 * bars became rungs — a row drawn one rung wide could sort above a row drawn
 * three rungs wide. `tierBands.byDisagreement` sorts the tier list by this
 * same rule, so "biggest gap first" now means one thing in both places. */
function byDisagreement(a: Divergence, b: Divergence): number {
  const t = Math.abs(b.tierGap) - Math.abs(a.tierGap);
  if (t !== 0) return t;
  const d = Math.abs(b.delta) - Math.abs(a.delta);
  if (d !== 0) return d;
  return a.name.localeCompare(b.name);
}

/**
 * Split the tier list into per-lane columns ranked by model-vs-community
 * disagreement.
 *
 * Gods the community hasn't placed are counted (`unranked`) but never given an
 * invented position — they're absent from every column's rows, which is why
 * the board reports the count separately rather than quietly dropping them.
 * A god carrying a score but no tier letter is unranked for the same reason:
 * there is no rung to stand it on.
 */
export function buildDivergenceBoard(entries: GodTierEntry[] | undefined): DivergenceBoard {
  const empty: DivergenceBoard = {
    lanes: [], total: 0, ranked: 0, unranked: 0, tierDisagreements: 0,
  };
  if (!entries || entries.length === 0) return empty;

  const unrankedByLane = new Map<Lane, number>();
  const rowsByLane = new Map<Lane, Divergence[]>();
  for (const lane of LANES) {
    unrankedByLane.set(lane, 0);
    rowsByLane.set(lane, []);
  }

  let ranked = 0;
  let unranked = 0;
  let tierDisagreements = 0;

  for (const e of entries) {
    const lane = godLane(e.role);
    const ourStep = tierStep(e.tier_ours);
    const theirStep = tierStep(e.tier_community);
    if (e.ours == null || e.community == null || ourStep == null || theirStep == null) {
      unranked += 1;
      if (lane) unrankedByLane.set(lane, (unrankedByLane.get(lane) ?? 0) + 1);
      continue;
    }
    ranked += 1;
    const tierGap = ourStep - theirStep;
    if (tierGap !== 0) tierDisagreements += 1;
    if (lane) {
      rowsByLane.get(lane)!.push({
        name: e.name,
        lane,
        ours: e.ours,
        community: e.community,
        delta: e.ours - e.community,
        tierOurs: e.tier_ours!,
        tierCommunity: e.tier_community!,
        tierGap,
        ourStep,
        theirStep,
        verdict: verdictOf(tierGap),
        tierDisagrees: tierGap !== 0,
      });
    }
  }

  const lanes: LaneColumn[] = LANES.map((lane) => ({
    lane,
    rows: rowsByLane.get(lane)!.sort(byDisagreement),
    unranked: unrankedByLane.get(lane) ?? 0,
  })).filter((c) => c.rows.length > 0 || c.unranked > 0);

  return { lanes, total: entries.length, ranked, unranked, tierDisagreements };
}

/** Where a rung sits along the track, as a percentage — the centre of its
 * cell, so a mark never straddles two tiers. */
export function stepPercent(step: number): number {
  return ((step + 0.5) / TIER_STEPS) * 100;
}

/** Signed score formatted the way the page talks: always two decimals, always
 * carrying its sign, em dash when there's nothing to show. A delta that rounds
 * away to nothing prints unsigned — "-0.00" reads as a direction the data
 * doesn't actually support. */
export function deltaText(delta: number | null | undefined): string {
  if (delta == null) return "—";
  const s = delta.toFixed(2);
  if (Number(s) === 0) return "0.00";
  return delta > 0 ? `+${s}` : s;
}
