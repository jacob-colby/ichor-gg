/** One purchase in the six: icon, name, the reason in words, and the gold
 * spent by the time you own it.
 *
 * A row the enemy draft swapped in carries `swapped`. It mounts with the
 * lock-in motion (index.css `.lock-in`) and its reason follows a beat later;
 * keyed by item name upstream, so the motion plays when the item CHANGES and
 * not on every re-render. Under reduced motion it is simply there, still
 * outlined and still carrying its reason.
 *
 * A row the READER's focus or aspect put there carries `adjusted` instead:
 * surface-2 with a neutral 2px ring, and the reason line leads with what it
 * replaced ("In for Book of Thoth"). Not violet — violet is the model's voice
 * and the draft's swaps speak in it; a focus swap is the reader's own choice
 * playing out, so it is marked in words and a neutral ring, never in colour
 * alone. When both apply, the draft's mark wins: it is the newer change.
 *
 * A row of a BORROWED six (the community's Conquest six shown in Joust or
 * Arena) whose Conquest record doesn't describe it in this mode carries
 * `flags`: an asterisk after the name and the reason read out to a screen
 * reader. The reason is printed under the six for everyone, by the
 * most-picked list's rule. */
import { toHash } from "../../lib/useHashRoute";
import type { ItemReason } from "./itemReason";
import { Art } from "./art";

const gold = (n: number) => n.toLocaleString("en-US");

export function ItemRow({ position, name, cumulativeGold, reason, swapped = false, adjusted = false, flags }: {
  position: number;
  name: string;
  /** Gold spent once this item is complete; null when a cost is unknown. */
  cumulativeGold: number | null;
  reason: ItemReason;
  swapped?: boolean;
  /** The reader's focus or aspect moved this item in. */
  adjusted?: boolean;
  /** Why Conquest's record doesn't describe this item in this mode. */
  flags?: string[];
}) {
  const adjust = adjusted && !swapped;
  return (
    <li data-testid="item-row" data-swapped={swapped || undefined} data-adjusted={adjust || undefined}
      data-flagged={flags?.length ? true : undefined}
      className={`relative ${swapped ? "lock-in" : ""}`}>
      <a href={toHash.item(name)}
        className={`press grid min-h-[64px] grid-cols-[48px_minmax(0,1fr)_auto] items-center gap-3 rounded-[12px] py-2 pl-2.5 pr-3.5 ${
          swapped ? "bg-surface-2 ring-2 ring-accent"
            : adjust ? "bg-surface-2 ring-2 ring-line-strong" : "bg-surface hover:bg-surface-2"}`}>
        <span className="relative">
          <Art name={name} kind="item" className="h-12 w-12 rounded-[8px]" eager={position <= 3} />
          <span aria-hidden="true"
            className="num absolute -left-1.5 -top-1.5 flex h-5 min-w-5 items-center justify-center rounded-full bg-ground px-1 font-cond text-[13px] font-bold text-muted ring-1 ring-line">
            {position}
          </span>
        </span>
        <span className="min-w-0">
          <span data-testid="item-name" className="block font-cond text-row font-bold text-ink [overflow-wrap:anywhere]">
            <span className="sr-only">{position}. </span>{name}
            {flags?.length ? <><span aria-hidden="true" className="ml-0.5 text-muted">*</span>
              <span className="sr-only"> — {flags.join(" ")}</span></> : null}
          </span>
          {reason.text && (
            <span className={`lock-reason mt-0.5 block text-note ${
              reason.tone === "swap" ? "font-semibold text-accent"
                : reason.tone === "adjust" ? "font-semibold text-ink-soft" : "text-muted"}`}>
              {reason.text}
            </span>
          )}
        </span>
        <span className="num text-right font-cond text-[21px] font-bold text-muted">
          {cumulativeGold != null ? gold(cumulativeGold) : "—"}
          <span className="sr-only"> gold spent by this item</span>
        </span>
      </a>
    </li>
  );
}
