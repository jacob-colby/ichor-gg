import { AspectHex } from "./art";

/** The god's aspect, as one switch in the header.
 *
 * 77 of 94 gods have an aspect and only a handful have a build behind it, so
 * the switch always says which kind this is: when it's on and the build did
 * not move, one line says so rather than leaving a pressed control that
 * changed nothing.
 *
 * Its mark is the game's own: the aspect hexagon (`AspectHex`), always in
 * Aspect Ember, outlined when off and filled when on. On, the frame takes a
 * low-alpha ember border and wash. It used to be a violet pill track until
 * 2026-11-09, when Jacob asked for the hexagon in bright orange. Violet is the
 * model's voice; the aspect is the player's own choice, and the game already
 * marks it in orange. */
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
      className={`press flex min-h-[52px] shrink-0 items-center gap-2 rounded-[12px] border py-1 pl-2.5 pr-3 text-left transition-colors duration-150 ease-[var(--ease-standard)] motion-reduce:transition-none ${
        on ? "border-aspect/45 bg-aspect/12 text-ink" : "border-line text-muted hover:border-quiet hover:text-ink"}`}>
      <AspectHex on={on} className="h-6 w-6" />
      <span className="flex flex-col items-start">
        <span className="text-cap leading-none text-quiet">Aspect</span>
        <span className="mt-0.5 line-clamp-2 max-w-[104px] font-cond text-[16px] font-bold uppercase leading-[0.95] [text-wrap:balance]">{short}</span>
      </span>
    </button>
  );
}
