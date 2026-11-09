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
 * Gem"). Under each tile, what the god's other players pick instead, as a
 * share of players — the same Conquest record the reason line quotes, never a
 * score. Neither tile carries gold: the "Gold spent" column is the six's
 * running total, and folding the starter into it would move every figure
 * under it. */
import { Art } from "./art";

export interface KitAlternative { name: string; icon: string; share: number }

const pct = (r: number) => `${Math.round(r * 100)}%`;

export function KitTile({ kind, icon, inset, name, reason, alternatives, altLabel, testId, altUnit = "of players" }: {
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
  /** What an alternative's share is OF, for a screen reader: players on the
   *  main build's record, games on an aspect's (`AspectCommunity`). */
  altUnit?: string;
}) {
  return (
    <div data-testid={testId} className="rounded-[12px] bg-surface">
      <div className="grid min-h-[64px] grid-cols-[48px_minmax(0,1fr)] items-center gap-3 py-2 pl-2.5 pr-3.5">
        <span className="relative h-12 w-12">
          <Art name={icon} kind="item" eager className="h-12 w-12 rounded-[8px]" />
          {inset && (
            <Art name={inset} kind="item" eager
              className="absolute -bottom-1.5 -right-1.5 h-7 w-7 rounded-[6px] ring-2 ring-surface" />
          )}
        </span>
        <span className="min-w-0">
          <span className="block font-cond text-row font-bold text-ink [overflow-wrap:anywhere]">
            <span className="mr-1.5 text-[17px] text-quiet">{kind}</span>{name}
          </span>
          {reason && <span className="mt-0.5 block text-note text-muted">{reason}</span>}
        </span>
      </div>
      {alternatives.length > 0 && (
        // One flowing line, not a list block: the six sits under these tiles,
        // and every row of chrome here is a row of the six pushed off a phone.
        <div className="flex flex-wrap items-center gap-x-3 gap-y-1 border-t border-line px-3.5 py-2 text-note">
          <span className="text-quiet" id={`${testId}-alts`}>{altLabel}</span>
          <ul aria-labelledby={`${testId}-alts`} className="flex min-w-0 flex-wrap items-center gap-x-3 gap-y-1">
            {alternatives.map((a) => (
              <li key={a.name} className="inline-flex min-w-0 items-center gap-1.5 text-ink-soft">
                <Art name={a.icon} kind="item" className="h-5 w-5 rounded-[4px]" />
                <span className="[overflow-wrap:anywhere]">{a.name}</span>
                <span className="num text-quiet">{pct(a.share)}<span className="sr-only"> {altUnit}</span></span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
