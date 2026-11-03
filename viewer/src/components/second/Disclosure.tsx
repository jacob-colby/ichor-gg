/** Everything beyond the six is one tap away, behind a native <details>:
 *  keyboard and screen-reader behaviour come free, and closed content costs
 *  no screen. The summary row is 56px. */
import type { ReactNode } from "react";
import { ChevronGlyph } from "./art";

export function Disclosure({ title, hint, children, testId, defaultOpen = false }: {
  title: string; hint?: string; children: ReactNode; testId?: string; defaultOpen?: boolean;
}) {
  return (
    <details className="disclosure group" data-testid={testId} open={defaultOpen || undefined}>
      <summary className="press flex min-h-14 cursor-pointer items-center gap-3 py-2">
        <span className="min-w-0 flex-1">
          <span className="block font-cond text-[22px] font-extrabold uppercase text-ink">{title}</span>
          {hint && <span className="block text-note text-quiet">{hint}</span>}
        </span>
        <ChevronGlyph size={20} className="chev text-muted" />
      </summary>
      <div className="pb-5 pt-1">{children}</div>
    </details>
  );
}
