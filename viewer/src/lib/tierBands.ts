import type { TierEntry } from "../types";

export const TIERS = ["S", "A", "B", "C"] as const;
export type TierLetter = (typeof TIERS)[number];

const TIER_INDEX: Record<TierLetter, number> = { S: 0, A: 1, B: 2, C: 3 };

/**
 * One entry inside a band, carrying where the *other* source places it.
 *
 * The bands are always the model's. The community isn't a second view you
 * toggle to — it's a ghost on every row, because the disagreement between the
 * two is the thing this product exists to show.
 */
export interface BandEntry<T extends TierEntry = TierEntry> {
  entry: T;
  /** ours - community. Null when the community hasn't scored it. */
  delta: number | null;
  /** Tier letters apart, signed: positive means the model ranks it higher
   * (a better letter) than the community does. */
  tierGap: number | null;
  agrees: boolean;
  unranked: boolean;
}

export interface Band<T extends TierEntry = TierEntry> {
  tier: TierLetter;
  entries: BandEntry<T>[];
  agreed: number;
  disagreed: number;
  unranked: number;
}

export interface BandsResult<T extends TierEntry = TierEntry> {
  bands: Band<T>[];
  /** Entries with no model tier at all — kept out of the bands rather than
   * bucketed somewhere arbitrary. */
  untiered: BandEntry<T>[];
  agreed: number;
  modelHigher: number;
  metaHigher: number;
  unranked: number;
  /** Entries both sources have placed — the only ones agreement is defined for. */
  ranked: number;
  total: number;
}

function describe<T extends TierEntry>(entry: T): BandEntry<T> {
  const unranked = entry.tier_community == null || entry.community == null;
  const oursIdx = entry.tier_ours ? TIER_INDEX[entry.tier_ours] : null;
  const commIdx = entry.tier_community ? TIER_INDEX[entry.tier_community] : null;
  return {
    entry,
    delta: entry.ours != null && entry.community != null ? entry.ours - entry.community : null,
    // Index runs S=0..C=3, so a *smaller* index is a better tier: the model
    // ranks it higher when the community's index is larger.
    tierGap: oursIdx != null && commIdx != null ? commIdx - oursIdx : null,
    agrees: !unranked && entry.tier_ours === entry.tier_community,
    unranked,
  };
}

/**
 * Biggest argument first: unranked entries sink, then order by how many tier
 * letters apart the two sources are, with the raw score gap as the tiebreak.
 *
 * Ordering on the score gap alone put agreeing entries at the top of a control
 * labelled "disputed first" — "disputed" means the tier letters differ
 * everywhere else on the page, so the sort has to use the same definition.
 */
function byDisagreement<T extends TierEntry>(a: BandEntry<T>, b: BandEntry<T>): number {
  if (a.unranked !== b.unranked) return a.unranked ? 1 : -1;
  const t = Math.abs(b.tierGap ?? 0) - Math.abs(a.tierGap ?? 0);
  if (t !== 0) return t;
  const d = Math.abs(b.delta ?? 0) - Math.abs(a.delta ?? 0);
  if (d !== 0) return d;
  return a.entry.name.localeCompare(b.entry.name);
}

/** Best score first — the conventional tier-list reading order. */
function byScore<T extends TierEntry>(a: BandEntry<T>, b: BandEntry<T>): number {
  const d = (b.entry.ours ?? -Infinity) - (a.entry.ours ?? -Infinity);
  if (d !== 0) return d;
  return a.entry.name.localeCompare(b.entry.name);
}

export type BandSort = "disagreement" | "score";

export function buildBands<T extends TierEntry>(
  entries: T[],
  sort: BandSort = "disagreement",
): BandsResult<T> {
  const described = entries.map(describe);
  const cmp = sort === "score" ? byScore : byDisagreement;

  const bands: Band<T>[] = TIERS.map((tier) => {
    const inBand = described.filter((d) => d.entry.tier_ours === tier).sort(cmp);
    return {
      tier,
      entries: inBand,
      agreed: inBand.filter((d) => d.agrees).length,
      disagreed: inBand.filter((d) => !d.agrees && !d.unranked).length,
      unranked: inBand.filter((d) => d.unranked).length,
    };
  }).filter((b) => b.entries.length > 0);

  const ranked = described.filter((d) => !d.unranked);
  return {
    bands,
    untiered: described.filter((d) => d.entry.tier_ours == null).sort(cmp),
    agreed: ranked.filter((d) => d.agrees).length,
    // tierGap > 0 means the community placed it in a worse tier than we did.
    modelHigher: ranked.filter((d) => (d.tierGap ?? 0) > 0).length,
    metaHigher: ranked.filter((d) => (d.tierGap ?? 0) < 0).length,
    unranked: described.filter((d) => d.unranked).length,
    ranked: ranked.length,
    total: described.length,
  };
}
