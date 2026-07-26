/** The model's item ranking for one god.
 *
 * `god_item_scores` carries 40 scored items for each of the 87 gods, and until
 * now exactly one surface read it: the draft board, to decide what a comp
 * displaces. Nowhere could you simply ask "what does the model think Ra wants,
 * and in what order?" — which is the most direct question this data answers.
 */
import type { Item } from "../types";

export interface GodItemRow {
  name: string;
  /** The model's fit score for this god. Absolute values sit in a narrow band
   *  (~0.39–0.50 across the set), so rank matters more than the figure. */
  score: number;
  rank: number;
  item?: Item;
  cost?: number;
  /** Gold-model residual: negative means priced under what its stats are worth. */
  residual?: number | null;
  /** In the god's own suggested core build. */
  inCore: boolean;
}

export interface GodItemsResult {
  rows: GodItemRow[];
  /** Scored names the index has no item for. Counted rather than dropped —
   *  a shorter list with no explanation reads as the model having fewer
   *  opinions than it does. */
  missing: string[];
  /** Core items the model scored, over the core's size: how much of the
   *  suggested build this ranking actually accounts for. */
  coreCovered: number;
  coreSize: number;
  /** The spread between best and worst score, so a surface can say whether the
   *  ranking is decisive or nearly flat instead of implying precision. */
  spread: number | null;
  /** Whether the core is exactly the top of this ranking. It usually isn't —
   *  item fit is one of four signals behind a build — and a surface claiming
   *  "the build takes the top six" without checking is wrong for most gods.
   *  Ra's core skips rank 4. */
  coreIsTop: boolean;
}

/**
 * Rank a god's scored items, best first.
 *
 * Ties break alphabetically rather than by insertion order: the scores are
 * rounded to four places in the index and genuinely tie (Eye of Providence and
 * Eye of the Storm both sit at 0.4592 for Achilles), so a stable, stated rule
 * beats whatever order the JSON happened to serialize.
 */
export function buildGodItems(
  scores: Record<string, number> | undefined,
  itemsByName: Map<string, Item>,
  core: string[] = [],
): GodItemsResult {
  const entries = Object.entries(scores ?? {});
  const coreSet = new Set(core);

  const sorted = [...entries].sort((a, b) => (b[1] - a[1]) || a[0].localeCompare(b[0]));
  const rows: GodItemRow[] = [];
  const missing: string[] = [];

  sorted.forEach(([name, score], i) => {
    const item = itemsByName.get(name);
    if (!item) missing.push(name);
    rows.push({
      name,
      score,
      rank: i + 1,
      item,
      cost: item?.cost,
      residual: item?.efficiency?.residual ?? null,
      inCore: coreSet.has(name),
    });
  });

  const values = sorted.map(([, s]) => s);
  const coreCovered = core.filter((n) => scores?.[n] != null).length;
  return {
    rows,
    missing,
    coreCovered,
    coreSize: core.length,
    spread: values.length > 1 ? values[0] - values[values.length - 1] : null,
    coreIsTop: core.length > 0
      && coreCovered === core.length
      && rows.slice(0, core.length).every((r) => r.inCore),
  };
}

/** Scores cluster inside ~0.1, so a bar drawn from zero would show 40 identical
 *  full bars. This stretches the actual range across the track instead, which
 *  is the only way the ordering is visible at all. */
export function scoreBarPercent(score: number, best: number, worst: number): number {
  if (!(best > worst)) return 100;
  return Math.round(((score - worst) / (best - worst)) * 92) + 8;
}
