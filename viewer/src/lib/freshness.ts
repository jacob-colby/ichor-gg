/** The data-freshness stamp, in the two lengths the chrome needs.
 *
 * The desktop top bar used to print the whole sentence — "Updated yesterday ·
 * Open Beta 47", 173px in the same row as the reading links and the command
 * field (measured 2026-11-07 at 1280–1920px). The bar now prints `short`
 * ("OB47 · 1d"), and the sentence is never hover-only (DESIGN.md: "nothing
 * communicates on hover alone"): it is the stamp's screen-reader text and
 * tooltip, a line in Help, and the line in the phone's More sheet.
 *
 *  - `short`: the patch abbreviated and the age in days/weeks/months.
 *  - `full`:  the sentence, as the More sheet always printed it.
 *  - `title`: the sentence with the stamp's own ISO date, which the tooltip
 *    carried before (the exact day matters when checking a patch landed).
 */
import { relativeDate, shortAge } from "./relativeDate";

export interface Freshness {
  short: string;
  full: string;
  title: string;
}

/** "Open Beta 47" → "OB47", the community's own shorthand. Any other label is
 *  returned as it is: a guessed abbreviation would be a fabricated patch. */
export function shortPatch(label: string): string {
  const m = /^open beta\s*(\d+)$/i.exec(label.trim());
  return m ? `OB${m[1]}` : label;
}

/** Null when the index carries no `data_updated` — the stamp is omitted, not
 *  invented. */
export function freshness(updated?: string, patch?: string, now: Date = new Date()): Freshness | null {
  if (!updated) return null;
  const rel = relativeDate(updated, now);
  const tail = patch ? ` · ${patch}` : "";
  const age = shortAge(updated, now);
  const short = patch ? [shortPatch(patch), age].filter(Boolean).join(" · ") : `Updated ${age ?? rel}`;
  return {
    short,
    full: `Updated ${rel}${tail}`,
    title: `Updated ${rel}${rel === updated ? "" : ` (${updated})`}${tail}`,
  };
}
