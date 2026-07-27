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
