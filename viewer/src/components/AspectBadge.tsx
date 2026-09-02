/* The aspect control, as the game draws it.
 *
 * It used to be a text button in the build header — "Aspect: Prowess" — which
 * had two problems. It lived on one surface only (the god page), so the draft
 * could not express an aspect at all; and it named the aspect without saying
 * what it belonged to, so on a page already carrying a mode strip and a flavor
 * strip it read as a third unrelated filter.
 *
 * SMITE marks an aspect with an orange hexagon on the god's portrait. Putting
 * it back where the game puts it makes the control self-describing: it is
 * attached to the face it modifies, and a player who has seen the game once
 * already knows what it means. That is also why it is orange rather than gold
 * — see `--color-aspect`, and the Torchlight Rule in DESIGN.md.
 *
 * Two components, because the two jobs are genuinely different and conflating
 * them is how a decorative badge ends up with button semantics: `AspectMark`
 * is a static marker, `AspectToggle` is a real toggle button.
 */

/** Pointy-top hexagon, the shape SMITE uses. Drawn rather than shipped as an
 *  asset so it inherits `currentColor` and stays crisp at 14px. */
function Hex({ filled }: { filled: boolean }) {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true" className="h-full w-full">
      <path
        d="M12 1.6 21 6.8v10.4L12 22.4 3 17.2V6.8z"
        fill={filled ? "currentColor" : "none"}
        stroke="currentColor"
        strokeWidth={filled ? 0 : 2.4}
        strokeLinejoin="round"
      />
      {filled && (
        // A notch out of the middle, so the "on" state is legible as a shape
        // and not only as a fill — the badge is 14px and sits on artwork whose
        // colour we do not control.
        <path d="M12 6.4 17 9.3v5.4L12 17.6 7 14.7V9.3z" fill="var(--color-bg0)" />
      )}
    </svg>
  );
}

/** Non-interactive "this god has an aspect" marker, for a face that is not a
 *  control (a picker tile, a threat row). */
export function AspectMark({ on = true, className = "" }: { on?: boolean; className?: string }) {
  return (
    <span aria-hidden="true"
      className={`pointer-events-none absolute -bottom-0.5 -right-0.5 h-3.5 w-3.5 text-aspect drop-shadow-[0_1px_2px_rgba(0,0,0,0.7)] ${className}`}>
      <Hex filled={on} />
    </span>
  );
}

/**
 * The toggle itself, positioned over the bottom-right of a god icon.
 *
 * The parent must be `relative`. Deliberately NOT wrapping the icon in its own
 * positioned element here: the icon already sits inside a slot/button on both
 * surfaces, and adding a wrapper would put a button inside a button on the
 * draft board.
 *
 * `title` and the label both name the aspect, because the hexagon alone says
 * "aspect" and not *which* aspect, and 65 of the 72 gods that have one have no
 * scoring overlay behind it — a reader deserves to know which of those they
 * are looking at, which is what `changesBuild` carries.
 *
 * F11. The TARGET is 24px and the MARK inside it is 20px, which is why the
 * size is fixed here rather than passed in. Both call sites used to send
 * `h-5 w-5`, and a class that beats the component's own `h-4 w-4` in
 * Tailwind's cascade rather than in the class attribute is not a size a
 * caller can reason about — it measured 20×20 at 375px, under WCAG 2.2
 * SC 2.5.8's 24px floor, and it was the only element on the site that was.
 * (The other sub-24px hit, the 1×1 skip link, is exempt and correct.) The
 * padding grows the hit area outward without moving the hexagon: the offsets
 * carry the extra 2px so the mark still sits where it sat on the portrait.
 */
export function AspectToggle({ aspectName, on, onToggle, changesBuild = true, className = "" }: {
  aspectName?: string;
  on: boolean;
  onToggle: () => void;
  /** False when this god's aspect has no scoring overlay, so the toggle shows
   *  the kit text and does not move the build. Stated, never silent. */
  changesBuild?: boolean;
  className?: string;
}) {
  const short = aspectName?.replace(/^Aspect of (the )?/i, "") ?? "aspect";
  const label = on
    ? `Turn off ${short} aspect`
    : changesBuild
      ? `Build for the ${short} aspect`
      : `Show the ${short} aspect (no build change — this aspect has no scoring overlay)`;
  return (
    <button
      type="button"
      onClick={(e) => { e.stopPropagation(); onToggle(); }}
      aria-pressed={on}
      aria-label={label}
      title={label}
      className={`press absolute -bottom-1.5 -right-1.5 z-10 h-6 w-6 p-0.5 rounded-sm transition-colors duration-150 ease-standard
        ${on ? "text-aspect" : "text-faint hover:text-aspect"}
        drop-shadow-[0_1px_2px_rgba(0,0,0,0.7)] ${className}`}
    >
      <Hex filled={on} />
    </button>
  );
}
