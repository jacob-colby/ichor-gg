/** The comparison, as the one sentence under the god's header.
 *
 * The claim reads at `say` in ink; the measured gap is emphasised by weight,
 * not hue — violet stays on actions. The honesty tail follows in muted, never
 * dropped: a gap the model can't fully see is half the sentence. */
import type { ReactNode } from "react";
import type { Verdict } from "./verdict";

export function VerdictLine({ verdict, loading = false, className = "", action }: {
  verdict: Verdict | null; loading?: boolean; className?: string;
  /** Inline control after the sentence ("Show theirs"). */
  action?: ReactNode;
}) {
  if (loading || !verdict) {
    return (
      <p aria-busy="true" className={`text-say text-quiet ${className}`} data-testid="verdict-line">
        Measuring Ichor&rsquo;s six against the community&rsquo;s…
      </p>
    );
  }
  return (
    <p className={`max-w-[46ch] text-say text-ink [text-wrap:pretty] lg:max-w-[40ch] lg:text-[21px] ${className}`}
      data-testid="verdict-line" data-kind={verdict.kind}>
      {verdict.parts.map((p, i) =>
        p.em ? <strong key={i} className="font-semibold text-ink">{p.text}</strong> : <span key={i}>{p.text}</span>)}
      {verdict.tail && <span className="text-muted"> {verdict.tail}</span>}
      {action && <> {action}</>}
    </p>
  );
}
