/** The god's aspect, as one switch in the header.
 *
 * 77 of 94 gods have an aspect and only a handful have a build behind it, so
 * the switch always says which kind this is: when it's on and the build did
 * not move, one line says so rather than leaving a pressed control that
 * changed nothing. */
export function AspectToggle({ aspect, on, onChange, changesBuild }: {
  aspect: string; on: boolean; onChange: (on: boolean) => void; changesBuild: boolean;
}) {
  const short = aspect.replace(/^Aspect of /, "");
  return (
    <button type="button" role="switch" aria-checked={on} onClick={() => onChange(!on)}
      aria-label={`${aspect}${changesBuild ? "" : " (doesn't change the build)"}`}
      title={aspect}
      className={`press flex h-[52px] shrink-0 items-center gap-2 rounded-[12px] border px-3 transition-colors duration-150 ${
        on ? "border-accent bg-accent/12 text-ink" : "border-line text-muted hover:border-quiet hover:text-ink"}`}>
      <span aria-hidden="true"
        className={`relative block h-5 w-8 flex-none rounded-full transition-colors duration-150 ${on ? "bg-accent" : "bg-surface-3"}`}>
        <span className={`absolute left-0 top-0.5 block h-4 w-4 rounded-full bg-ink transition-transform duration-150 ${on ? "translate-x-3.5" : "translate-x-0.5"}`} />
      </span>
      <span className="flex flex-col items-start leading-none">
        <span className="font-cond text-[17px] font-bold uppercase">Aspect</span>
        <span className="max-w-[9ch] truncate text-cap text-quiet">{short}</span>
      </span>
    </button>
  );
}

