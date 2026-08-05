/** The vocabulary for a price verdict — the words and the two signal colours,
 *  defined once so the shop and the item page can't say the same thing two
 *  different ways.
 *
 * The tier-disagreement half of this file is gone. It named a comparison the
 * site no longer makes: our ranking against the community's, with "Underrated"
 * meaning "we rate it above them". That comparison did not survive measurement
 * — see `pipeline/smite/tierlist.py` — so the words for it went with it.
 *
 * `under`/`premium` keep the meaning they carry everywhere else: `under` is
 * the model valuing something above the market, `premium` the market above
 * the model.
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
