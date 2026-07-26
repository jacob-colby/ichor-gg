import type { GodTierEntry } from "../types";
import { LANES, godLane, type Lane } from "./roleAccent";

/** One god where we have both a model score and a community score, plus the
 * gap between them. `delta > 0` means our model rates the god above the
 * community; `delta < 0` means the community rates it above us. */
export interface Divergence {
  name: string;
  lane: Lane | undefined;
  ours: number;
  community: number;
  /** ours - community. The whole point of the page. */
  delta: number;
  tierOurs: GodTierEntry["tier_ours"];
  tierCommunity: GodTierEntry["tier_community"];
  /** The two tier letters differ — a disagreement you could argue about. */
  tierDisagrees: boolean;
}

/** One lane's slice of the board, ranked by how hard we disagree. */
export interface LaneColumn {
  lane: Lane;
  rows: Divergence[];
  /** Mean signed delta across the lane — the systematic lean, if any. */
  meanDelta: number;
  /** Gods in this lane we rate above / below the community. */
  higher: number;
  lower: number;
  /** Gods in this lane whose tier letter differs between the two sources —
   * the per-lane share of the headline count. */
  tierDiffer: number;
  /** Gods in this lane with no community score to compare against. */
  unranked: number;
}

export interface DivergenceBoard {
  lanes: LaneColumn[];
  /** Every god in the tier list, whether or not the community has scored it. */
  total: number;
  /** Gods with both scores — the only ones we can honestly compare. */
  ranked: number;
  unranked: number;
  /** Ranked gods whose model tier letter differs from the community's. */
  tierDisagreements: number;
  /** Largest absolute delta present, used to scale the bars. Never 0. */
  scale: number;
}

/** Rank a lane's rows by the size of the disagreement, biggest first. Ties
 * break on name so the order is stable across renders and refreshes. */
function byDisagreement(a: Divergence, b: Divergence): number {
  const d = Math.abs(b.delta) - Math.abs(a.delta);
  return d !== 0 ? d : a.name.localeCompare(b.name);
}

/**
 * Split the tier list into per-lane columns ranked by model-vs-community
 * disagreement.
 *
 * Gods the community hasn't scored are counted (`unranked`) but never given an
 * invented delta — they're absent from every column's rows, which is why the
 * board reports the count separately rather than quietly dropping them.
 */
export function buildDivergenceBoard(entries: GodTierEntry[] | undefined): DivergenceBoard {
  const empty: DivergenceBoard = {
    lanes: [], total: 0, ranked: 0, unranked: 0, tierDisagreements: 0, scale: 1,
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
  let scale = 0;

  for (const e of entries) {
    const lane = godLane(e.role);
    if (e.ours == null || e.community == null) {
      unranked += 1;
      if (lane) unrankedByLane.set(lane, (unrankedByLane.get(lane) ?? 0) + 1);
      continue;
    }
    ranked += 1;
    const delta = e.ours - e.community;
    const tierDisagrees = e.tier_ours !== e.tier_community;
    if (tierDisagrees) tierDisagreements += 1;
    scale = Math.max(scale, Math.abs(delta));
    if (lane) {
      rowsByLane.get(lane)!.push({
        name: e.name,
        lane,
        ours: e.ours,
        community: e.community,
        delta,
        tierOurs: e.tier_ours,
        tierCommunity: e.tier_community,
        tierDisagrees,
      });
    }
  }

  const lanes: LaneColumn[] = LANES.map((lane) => {
    const rows = rowsByLane.get(lane)!.sort(byDisagreement);
    const meanDelta = rows.length
      ? rows.reduce((sum, r) => sum + r.delta, 0) / rows.length
      : 0;
    return {
      lane,
      rows,
      meanDelta,
      higher: rows.filter((r) => r.delta > 0).length,
      lower: rows.filter((r) => r.delta < 0).length,
      tierDiffer: rows.filter((r) => r.tierDisagrees).length,
      unranked: unrankedByLane.get(lane) ?? 0,
    };
  }).filter((c) => c.rows.length > 0 || c.unranked > 0);

  return {
    lanes,
    total: entries.length,
    ranked,
    unranked,
    tierDisagreements,
    // Guard the divisor: an index where every god matches exactly would
    // otherwise scale every bar by zero.
    scale: scale || 1,
  };
}

/** Bar width as a percentage of half the track, clamped so a record-setting
 * delta still fits inside its lane. */
export function barPercent(delta: number, scale: number): number {
  if (!scale) return 0;
  return Math.min(100, Math.round((Math.abs(delta) / scale) * 100));
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
