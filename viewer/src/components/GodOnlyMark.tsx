/* A `God Specific` item, marked as one.
 *
 * Four items in the pool are unbuyable by 86 of the 87 gods — Ratatoskr's three
 * acorns and Aladdin's Genie's Lamp. The pipeline has always known this
 * (`scoring.is_buildable` admits them for their owner only, and the gold model
 * sorts them apart because a price only one god can act on doesn't belong on a
 * board against prices everyone can), and `god` has always been in index.json.
 * The viewer simply never declared the field, so a reader met "Briskberry
 * Acorn" on a shelf of items they could buy with nothing saying otherwise.
 *
 * Two marks, because they answer different questions at different distances.
 * The asterisk rides the name and survives truncation, so a scan across a grid
 * shows *which* rows are conditional; the badge names the god and carries their
 * portrait, so a reader stopped on one card learns *whose* it is without
 * knowing the item. The asterisk is decorative — the badge is the accessible
 * statement, and every surface that shows one shows the other.
 */
import { useState } from "react";
import { iconSlug } from "../lib/builds";

/** The asterisk itself, sized to ride a name without disturbing its baseline.
 *  Decorative: `GodOnlyBadge` is what a screen reader reads. */
export function GodOnlyAsterisk({ god }: { god: string }) {
  return (
    <span aria-hidden="true" title={`${god} only`}
      className="ml-0.5 align-super font-mono text-micro text-gold">*</span>
  );
}

/** The named badge: the god's portrait, then whose item it is.
 *
 *  Falls back to a monogram on a missing portrait rather than a broken image —
 *  the same one-retry pattern `GodArt` and `ItemIcon` use, because a hole here
 *  reads as a rendering fault rather than as missing art. */
export function GodOnlyBadge({ god, className = "" }: { god: string; className?: string }) {
  const [tries, setTries] = useState(0);
  return (
    <span
      title={`Only ${god} can buy this — it takes one of the six core slots, and no other god can build it`}
      className={`inline-flex items-center gap-1 rounded-sm bg-gold/15 py-px pl-px pr-1.5 text-micro font-semibold uppercase tracking-[0.06em] text-gold ${className}`}
    >
      {tries > 1 ? (
        <span aria-hidden="true" className="flex h-4 w-4 items-center justify-center rounded-sm bg-bg3 font-display text-micro font-bold text-faint">
          {god.slice(0, 1)}
        </span>
      ) : (
        <img src={`/icons/${iconSlug(god)}-head.png${tries ? "?r=1" : ""}`} alt="" loading="lazy"
          onError={() => setTries((t) => t + 1)}
          className="h-4 w-4 shrink-0 rounded-sm object-cover" />
      )}
      {god} only
    </span>
  );
}
