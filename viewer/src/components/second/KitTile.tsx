/** The starter and the relic, as tiles in the build itself.
 *
 * They were a footnote: one 32px line above the six, and no relic at all. A
 * player buys the starter before item one and takes the relic at the fountain,
 * so both get the six's own treatment — the 64px row, the 48px icon, the name
 * in the caption face, one reason line — and sit at the head of the buy
 * order, not under it.
 *
 * The starter keeps its base → upgrade pairing: the base's icon carries the
 * upgrade's as an inset, and the name says both ("Conduit Gem → Archmage's
 * Gem"). Neither tile carries gold: the "Gold spent" column is the six's
 * running total, and folding the starter into it would move every figure
 * under it.
 *
 * THE SAME SIZE AS A ROW, NOT BIGGER (2026-11-09). What the god's other
 * players pick instead (by share of players, the same Conquest record the
 * reason line quotes, never a score) used to sit open under each tile. That
 * made each tile about twice an item row: on a 375×812 phone the two tiles
 * took 268px, and with a focus chosen not one of the six was on the first
 * screen. The alternatives are now one tap away. The whole tile is the
 * summary of a native <details>, so the tap target is the tile itself, with
 * keyboard and screen-reader behaviour for free. Its right edge, where an
 * item row prints gold, says how many others there are. */
import { Art, ChevronGlyph } from "./art";

export interface KitAlternative { name: string; icon: string; share: number }

const pct = (r: number) => `${Math.round(r * 100)}%`;

export function KitTile({ kind, icon, inset, name, reason, alternatives, altLabel, testId }: {
  kind: "Start" | "Relic";
  /** The tile's main icon (the starter's base, or the relic). */
  icon: string;
  /** A second icon set into the first's corner (the starter's upgrade). */
  inset?: string;
  name: string;
  reason?: string;
  alternatives: KitAlternative[];
  /** "Others" — names the list for the reader and for a screen reader. */
  altLabel: string;
  testId: string;
}) {
  const others = alternatives.length;
  const row = (
    <span className={`grid min-h-[64px] items-center gap-3 py-2 pl-2.5 pr-3.5 ${
      others ? "grid-cols-[48px_minmax(0,1fr)_auto]" : "grid-cols-[48px_minmax(0,1fr)]"}`}>
      <span className="relative h-12 w-12">
        <Art name={icon} kind="item" eager className="h-12 w-12 rounded-[8px]" />
        {inset && (
          <Art name={inset} kind="item" eager
            className="absolute -bottom-1.5 -right-1.5 h-7 w-7 rounded-[6px] ring-2 ring-surface" />
        )}
        {/* "Start" / "Relic" where an item row puts its position, so the buy
            order reads Start, Relic, 1 … 6, and the name gets the line. */}
        <span aria-hidden="true"
          className="absolute -left-1.5 -top-1.5 flex h-5 items-center rounded-full bg-ground px-1.5 font-cond text-[13px] font-bold uppercase text-muted ring-1 ring-line">
          {kind}
        </span>
      </span>
      <span className="min-w-0">
        <span className="block font-cond text-row font-bold text-ink [overflow-wrap:anywhere]">
          <span className="sr-only">{kind}: </span>{name}
        </span>
        {reason && <span className="mt-0.5 block text-note text-muted">{reason}</span>}
      </span>
      {others > 0 && (
        <span className="flex items-center text-note text-quiet" data-testid={`${testId}-others-count`}>
          <span className="num">+{others}</span>
          <span className="sr-only"> {altLabel.toLowerCase()}</span>
          <ChevronGlyph size={16} className="chev" />
        </span>
      )}
    </span>
  );

  if (!others) return <div data-testid={testId} className="rounded-[12px] bg-surface">{row}</div>;
  return (
    <details data-testid={testId} className="disclosure rounded-[12px] bg-surface">
      <summary className="press block cursor-pointer rounded-[12px] hover:bg-surface-2">{row}</summary>
      <div className="flex flex-wrap items-center gap-x-3 gap-y-1 border-t border-line px-3.5 py-2 text-note">
        <span className="text-quiet" id={`${testId}-alts`}>{altLabel}</span>
        <ul aria-labelledby={`${testId}-alts`} className="flex min-w-0 flex-wrap items-center gap-x-3 gap-y-1">
          {alternatives.map((a) => (
            <li key={a.name} className="inline-flex min-w-0 items-center gap-1.5 text-ink-soft">
              <Art name={a.icon} kind="item" className="h-5 w-5 rounded-[4px]" />
              <span className="[overflow-wrap:anywhere]">{a.name}</span>
              <span className="num text-quiet">{pct(a.share)}<span className="sr-only"> of players</span></span>
            </li>
          ))}
        </ul>
      </div>
    </details>
  );
}
