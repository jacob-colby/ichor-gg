/** The god's aspect, as one switch in the header.
 *
 * 77 of 94 gods have an aspect and only a handful have a build behind it, so
 * the switch always says which kind this is: when it's on and the build did
 * not move, one line says so rather than leaving a pressed control that
 * changed nothing. */
export function AspectToggle({ aspect, on, onChange, changesBuild }: {
  aspect: string; on: boolean; onChange: (on: boolean) => void; changesBuild: boolean;
}) {
  // "Aspect of the Passionate Storm" → "Passionate Storm": the small "Aspect"
  // above it already says what kind of name this is. The name wraps at its
  // spaces (two lines at most) instead of truncating — "Thermoth…" told a
  // player nothing.
  const short = aspect.replace(/^Aspect of /, "").replace(/^the /i, "");
  return (
    <button type="button" role="switch" aria-checked={on} onClick={() => onChange(!on)}
      aria-label={`${aspect}${changesBuild ? "" : " (doesn't change the build)"}`}
      title={aspect}
      className={`press flex min-h-[52px] shrink-0 items-center gap-2 rounded-[12px] border py-1 pl-3 pr-2.5 text-left transition-colors duration-150 ${
        on ? "border-accent bg-accent/12 text-ink" : "border-line text-muted hover:border-quiet hover:text-ink"}`}>
      <span aria-hidden="true"
        className={`relative block h-5 w-8 flex-none rounded-full transition-colors duration-150 ${on ? "bg-accent" : "bg-surface-3"}`}>
        <span className={`absolute left-0 top-0.5 block h-4 w-4 rounded-full bg-ink transition-transform duration-150 ${on ? "translate-x-3.5" : "translate-x-0.5"}`} />
      </span>
      <span className="flex flex-col items-start">
        <span className="text-cap leading-none text-quiet">Aspect</span>
        <span className="mt-0.5 line-clamp-2 max-w-[104px] font-cond text-[16px] font-bold uppercase leading-[0.95] [text-wrap:balance]">{short}</span>
      </span>
    </button>
  );
}

