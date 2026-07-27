/** The tier ladder, and the words that go with it.
 *
 * Home and the tier list both state "where we put this, where the meta puts
 * it, and which of us is higher". They render it from one component so the
 * two can't drift into two dialects of the same claim — the mark, the colours
 * and the words are defined once, here.
 *
 * The grammar: four rungs, worst to best, left to right. A white rule is the
 * meta's placement — the neutral baseline the reader already holds. The gold
 * kite is ours, the same shape as the wordmark's tittle, because gold marks
 * the model's own signal and shape carries it a second time so the pair never
 * depends on colour alone. A translucent run joins the two: the mark says
 * *whose*, the run says *which way*.
 */
import { stepPercent } from "../lib/divergence";
import { TIER_STEPS, type TierLetter, type Verdict } from "../lib/tierBands";

/** Left to right, worst to best. A tier list is drawn S-first, but an axis
 *  that improves rightward is the one people read off a scoreboard. */
const LADDER: TierLetter[] = ["C", "B", "A", "S"];

/** The empty rungs. Shared by the ladder and anything that needs to draw the
 *  same geometry beside it. */
function LadderCells() {
  return (
    <span className="absolute inset-0 grid grid-cols-4 gap-[3px]">
      {Array.from({ length: TIER_STEPS }, (_, i) => (
        <span key={i} className="rounded-[1px] bg-bg3" />
      ))}
    </span>
  );
}

/** The rungs, named under the bar they belong to. Taught once in a key above
 *  the board, every row was only readable by remembering something from
 *  elsewhere on the page. */
function LadderAxis() {
  return (
    <span aria-hidden="true" className="mt-1 grid grid-cols-4 gap-[3px]">
      {LADDER.map((t) => (
        <span key={t} className="text-center font-mono text-micro leading-none text-faint">{t}</span>
      ))}
    </span>
  );
}

export function TierLadder({ ourStep, theirStep, verdict, axis = true }: {
  ourStep: number;
  theirStep: number;
  verdict: Verdict;
  /** The tier letters underneath. Off where a caption already names them. */
  axis?: boolean;
}) {
  const from = Math.min(ourStep, theirStep);
  const to = Math.max(ourStep, theirStep);
  const under = verdict === "underrated";
  return (
    <span aria-hidden="true" className="block">
      <span className="relative block h-2.5">
        <LadderCells />
        {verdict !== "agreed" && (
          // Grows from the meta's rung toward ours: the animation traces the
          // argument in the direction the argument runs.
          <span
            className={`bar-grow absolute inset-y-0 rounded-[1px] ${
              under ? "origin-left bg-under/45" : "origin-right bg-premium/45"}`}
            style={{ left: `${stepPercent(from)}%`, width: `${stepPercent(to) - stepPercent(from)}%` }}
          />
        )}
        <span className="absolute -top-0.5 h-[14px] w-[2px] -translate-x-1/2 rounded-[1px] bg-ink"
          style={{ left: `${stepPercent(theirStep)}%` }} />
        {/* Drawn on agreement too, where it lands on the rule — which is what
            agreeing looks like. */}
        <span className="mark absolute -top-[3px] h-4 w-[9px] -translate-x-1/2 bg-gold"
          style={{ left: `${stepPercent(ourStep)}%` }} />
      </span>
      {axis && <LadderAxis />}
    </span>
  );
}
