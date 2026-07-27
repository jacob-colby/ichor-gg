/** The wordmark, in one place.
 *
 * The tittle of the `i` is the gold kite that marks our own placement on every
 * tier ladder, so the logo and the data carry one shape and the mark means
 * something before you learn it.
 *
 * **The geometry is measured off the face, not guessed.** With `leading-none`,
 * Rajdhani puts its baseline 0.79em below the box top and its x-height 0.515em
 * above the baseline, so the stem's top edge sits 0.275em down. The kite hangs
 * just clear of that. Positioning from the box *bottom* instead is 0.21em out —
 * that is the descender — and drives the mark straight through the stem; it is
 * the bug that shipped twice before this was written down.
 *
 * Everything is in `em`, so the whole mark scales with one font size.
 */

/** Stem top, as a fraction of the em box. See above. */
const STEM_TOP = 0.275;
/** Kite height, and the gap between its point and the stem. */
const KITE_H = 0.36;
const GAP = 0.04;
/** The drawn artwork's own ratio: 270 wide × 460 tall. */
const KITE_W = +(KITE_H * 0.587).toFixed(3);

export function Wordmark({ px = 19, className = "" }: {
  /** Font size in px; the kite scales with it. */
  px?: number;
  className?: string;
}) {
  return (
    // `role="img"` so the word survives as one accessible name rather than
    // being spelled out around a dotless i. A link wrapping this supplies its
    // own label, which wins — so nothing is announced twice.
    <span
      role="img"
      aria-label="ichor"
      style={{ fontSize: `${px}px` }}
      className={`inline-flex font-display font-bold leading-none tracking-tight text-ink ${className}`}
    >
      <span aria-hidden="true" className="relative inline-block">
        &#x131;
        <span
          className="mark absolute left-1/2 -translate-x-1/2 bg-gold"
          style={{
            height: `${KITE_H}em`,
            width: `${KITE_W}em`,
            top: `calc(${STEM_TOP}em - ${GAP}em - ${KITE_H}em)`,
          }}
        />
      </span>
      <span aria-hidden="true">chor</span>
    </span>
  );
}
