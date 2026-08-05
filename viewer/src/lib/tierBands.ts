import type { TierEntry } from "../types";

export const TIERS = ["S", "A", "B", "C"] as const;
export type TierLetter = (typeof TIERS)[number];

const TIER_INDEX: Record<TierLetter, number> = { S: 0, A: 1, B: 2, C: 3 };

/** How many rungs the ladder has. */
export const TIER_STEPS = TIERS.length;

/** Position on the ladder read left-to-right, worst to best: C=0 … S=3.
 *
 * This is the *reading* order, the reverse of `TIER_INDEX`'s ranking order —
 * a tier list is drawn with S at the top, but a horizontal axis that improves
 * rightward is the one people already read off a scoreboard. */
export function tierStep(t: TierLetter | null | undefined): number | null {
  return t ? TIER_STEPS - 1 - TIER_INDEX[t] : null;
}

/**
 * One entry inside a band.
 *
 * The bands used to be the model's, with the community's placement drawn as a
 * ghost on every row, because the disagreement between them was what the
 * product claimed to be for. That claim did not survive measurement: the
 * model's god ranking correlated −0.117 with real god strength, its item
 * ranking −0.267 with item win rate, and the resulting "51 of 87 placed
 * differently" was *less* disagreement than two unrelated rankings produce
 * (75%). There is one ranking now and it is the measured one.
 */
export interface BandEntry<T extends TierEntry = TierEntry> {
  entry: T;
  /** No usable sample. Kept visible and unplaced rather than ranked badly —
   *  "we didn't measure this" and "this is bad" are different facts. */
  unmeasured: boolean;
}

export interface Band<T extends TierEntry = TierEntry> {
  tier: TierLetter;
  entries: BandEntry<T>[];
}

export interface BandsResult<T extends TierEntry = TierEntry> {
  bands: Band<T>[];
  /** Entries with no band at all — kept out of the bands rather than bucketed
   *  somewhere arbitrary. */
  untiered: BandEntry<T>[];
  /** Entries with a real sample behind them. */
  ranked: number;
  unmeasured: number;
  total: number;
  /** The ranked entries' samples summed — APPEARANCES, not matches. Ten gods
   *  play every match, so this counts each separately; calling it "matches"
   *  contradicted the source line on the same screen. */
  appearances: number;
}

/** Best first, which for a tier list is also the reading order. */
function byScore<T extends TierEntry>(a: BandEntry<T>, b: BandEntry<T>): number {
  if (a.unmeasured !== b.unmeasured) return a.unmeasured ? 1 : -1;
  const d = (b.entry.score ?? -Infinity) - (a.entry.score ?? -Infinity);
  if (d !== 0) return d;
  return a.entry.name.localeCompare(b.entry.name);
}

/** Most-played first — the other question a reader actually asks of a tier
 *  list, and one this data can answer honestly. */
function byMatches<T extends TierEntry>(a: BandEntry<T>, b: BandEntry<T>): number {
  if (a.unmeasured !== b.unmeasured) return a.unmeasured ? 1 : -1;
  const d = (b.entry.matches ?? -Infinity) - (a.entry.matches ?? -Infinity);
  if (d !== 0) return d;
  return a.entry.name.localeCompare(b.entry.name);
}

export type BandSort = "score" | "matches";

function describe<T extends TierEntry>(entry: T): BandEntry<T> {
  return { entry, unmeasured: entry.score == null || entry.tier_score == null };
}

export function buildBands<T extends TierEntry>(
  entries: T[],
  sort: BandSort = "score",
): BandsResult<T> {
  const described = entries.map(describe);
  const cmp = sort === "matches" ? byMatches : byScore;

  const bands: Band<T>[] = TIERS.map((tier) => ({
    tier,
    entries: described.filter((d) => d.entry.tier_score === tier).sort(cmp),
  })).filter((b) => b.entries.length > 0);

  const ranked = described.filter((d) => !d.unmeasured);
  return {
    bands,
    untiered: described.filter((d) => d.entry.tier_score == null).sort(cmp),
    ranked: ranked.length,
    unmeasured: described.filter((d) => d.unmeasured).length,
    total: described.length,
    appearances: ranked.reduce((n, d) => n + (d.entry.matches ?? 0), 0),
  };
}
