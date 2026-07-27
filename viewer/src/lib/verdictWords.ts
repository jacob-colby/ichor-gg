/** The vocabulary for a tier disagreement — the words and the two signal
 *  colours, defined once so Home and the tier list can't say the same thing
 *  two different ways.
 *
 * `under`/`premium` keep the meaning they carry everywhere else in the app:
 * `under` is the model rating something above the market, `premium` the market
 * rating it above the model. Agreement takes no colour at all — on a page
 * about disagreement, the rows that agree should recede rather than light up.
 */
import type { Verdict } from "./tierBands";

export const VERDICT_WORD: Record<Verdict, string> = {
  underrated: "Underrated",
  overrated: "Overrated",
  agreed: "Agreed",
};

export const VERDICT_TEXT: Record<Verdict, string> = {
  underrated: "text-under",
  overrated: "text-premium",
  agreed: "text-faint",
};

/** Spoken form, for accessible names — "Underrated" alone doesn't say who is
 *  doing the underrating. */
export const VERDICT_SPOKEN: Record<Verdict, string> = {
  underrated: "we rate it higher",
  overrated: "we rate it lower",
  agreed: "both agree",
};

/* ── The same question, asked about a price ───────────────────────────────
 * The shop compares an item's cost against what the gold model says its stats
 * are worth. That's a different comparison from model-vs-meta, so it gets its
 * own words — but the same shape of sentence, and the same two colours meaning
 * the same two things: `under` is the model valuing something above the
 * market, `premium` the market above the model.
 */
export type PriceVerdict = "underpriced" | "overpriced" | "fair";

/**
 * The pipeline's own bucket owns the verdict, not the raw residual.
 *
 * This is the pricing twin of the rule that tier letters own a placement: the
 * continuous residual and the bucket can land on opposite sides of a boundary,
 * and the bucket is already what the filters, the sort and the shop's own
 * chips are built on. Deriving the word from the residual instead would let a
 * card read "Fair" while the Premium filter had just selected it.
 */
export function priceVerdict(tier: string | null | undefined, residual: number): PriceVerdict {
  if (tier === "undervalued") return "underpriced";
  if (tier === "premium") return "overpriced";
  if (tier === "fair") return "fair";
  return residual < 0 ? "underpriced" : residual > 0 ? "overpriced" : "fair";
}

export const PRICE_WORD: Record<PriceVerdict, string> = {
  underpriced: "Underpriced",
  overpriced: "Overpriced",
  fair: "Fairly priced",
};

export const PRICE_TEXT: Record<PriceVerdict, string> = {
  underpriced: "text-under",
  overpriced: "text-premium",
  fair: "text-faint",
};

export const PRICE_SPOKEN: Record<PriceVerdict, string> = {
  underpriced: "worth more than it costs",
  overpriced: "costs more than it's worth",
  fair: "priced about right",
};
