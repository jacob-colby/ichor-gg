/** What this god's players buy most, with the build's own items ticked.
 *
 * On every mode. Joust and Arena have no community record, so they show
 * Conquest's — said in the caption, not implied — and an item whose Conquest
 * record does not describe what it does in that mode carries an asterisk and
 * a note under the list that says why (`lib/mostPicked.ts`). The tick is a
 * glyph AND words for a screen reader; the asterisk's reason is printed, not
 * a tooltip. Ranking and its rule are in `mostPicked`; the caption states it.
 *
 * Desktop: a panel in the second column. Phone: the body of a disclosure, so
 * the heading lives on the disclosure's summary instead (`bare`). */
import type { PickedItem, TransferFlag } from "../../lib/mostPicked";
import { ORDINAL } from "../../lib/mostPicked";
import { toHash } from "../../lib/useHashRoute";
import { Art, CheckGlyph } from "./art";
import { MODE_NAME, type Mode } from "./verdict";

const pct = (r: number) => `${Math.round(r * 100)}%`;

export function MostPicked({ god, mode, items, total, inBuild, flags, bare = false }: {
  god: string;
  mode: Mode;
  items: PickedItem[];
  /** How many distinct items the record names (items may be the top slice). */
  total: number;
  inBuild: Set<string>;
  flags: TransferFlag[];
  bare?: boolean;
}) {
  const flagged = new Map<string, string[]>();
  for (const f of flags) for (const n of f.items) flagged.set(n, [...(flagged.get(n) ?? []), f.note]);
  const elsewhere = mode !== "conquest";
  return (
    <section aria-labelledby={bare ? undefined : "picked-h"} aria-label={bare ? "Most picked" : undefined}
      data-testid="most-picked">
      {!bare && <h2 id="picked-h" className="font-cond text-[22px] font-extrabold text-ink">Most picked</h2>}
      <p className={`${bare ? "" : "mt-1"} text-note text-muted`}>
        {elsewhere
          ? <>{god}&rsquo;s Conquest players — {MODE_NAME[mode]} has no record of its own, so this is Conquest data.</>
          : <>What {god}&rsquo;s Conquest players buy.</>}
        {" "}Ranked by the share who buy each item in its most common slot
        {total > items.length ? `; the top ${items.length} of ${total}` : ""}.
      </p>
      {items.length === 0 ? (
        <p className="mt-3 text-copy text-muted">No Conquest record of {god}&rsquo;s items yet.</p>
      ) : (
        <ol className="mt-2 divide-y divide-line border-y border-line">
          {items.map((p) => {
            const have = inBuild.has(p.name);
            const notes = flagged.get(p.name);
            return (
              <li key={p.name} data-testid="picked-row" data-in-build={have || undefined} data-flagged={notes ? true : undefined}>
                <a href={toHash.item(p.name)}
                  className="press grid min-h-11 grid-cols-[32px_minmax(0,1fr)_auto_20px] items-center gap-2.5 py-1.5 hover:bg-surface">
                  <Art name={p.name} kind="item" className="h-8 w-8 rounded-[6px]" />
                  <span className="min-w-0 font-cond text-[19px] font-bold leading-none text-ink [overflow-wrap:anywhere]">
                    {p.name}
                    {notes && <><span aria-hidden="true" className="ml-0.5 text-muted">*</span>
                      <span className="sr-only"> — {notes.join(" ")}</span></>}
                  </span>
                  <span className="num whitespace-nowrap text-right text-cap text-quiet">
                    {pct(p.pickRate)} buy it {ORDINAL[p.slot] ?? `in slot ${p.slot + 1}`}
                  </span>
                  <span className="flex justify-end text-ink">
                    {have && <><CheckGlyph size={18} /><span className="sr-only">In this build</span></>}
                  </span>
                </a>
              </li>
            );
          })}
        </ol>
      )}
      <p className="mt-2 flex items-center gap-1.5 text-cap text-quiet">
        <CheckGlyph size={14} className="text-ink" /> In the build on screen
        <span className="text-quiet">· {[...inBuild].filter((n) => items.some((p) => p.name === n)).length} of {items.length}</span>
      </p>
      {flags.length > 0 && (
        <div className="mt-3 space-y-1.5 text-cap text-muted" data-testid="picked-notes">
          {flags.map((f) => (
            <p key={f.reason}>
              <span aria-hidden="true" className="text-ink">* </span>
              <span className="text-ink-soft">{f.items.join(", ")}</span> — {f.note}
            </p>
          ))}
        </div>
      )}
    </section>
  );
}
