/** Patch notes (`#/patch`): what changed between data refreshes, readably.
 *
 * Each period leads with its biggest changes as rows — the item, the kind of
 * change in a word, and the headline — and keeps the full list one tap below.
 *
 * Product truth kept from the old PatchNotes:
 *  - History is a diff between two refreshes, so the page STARTS EMPTY and
 *    says so; an empty page is not a loading state and never looks like one.
 *  - A period inside one game patch is Ichor catching up on its own data:
 *    items it adds there "entered Ichor's data", they are not new.
 *  - Official notes are linked only where the period carries a hand-checked
 *    URL. Gods and systems are not tracked, and the page says that.
 *  - Change kinds are words in ink, not green/red: positive/negative mean the
 *    model against the market and nothing else (the Semantic Color Rule). */
import type { PatchDelta, PatchHighlight, PatchPeriod } from "../../types";
import { toHash } from "../../lib/useHashRoute";
import { Art } from "./art";
import { Disclosure } from "./Disclosure";
import { Em, PageHead } from "./PageParts";
import { shortDate } from "./shortDate";

const KIND: Record<PatchHighlight["change"] | PatchDelta["verdict"], string> = {
  buff: "Buff", nerf: "Nerf", mixed: "Mixed", adjusted: "Adjusted", added: "Added", removed: "Removed",
};

function periodTitle(p: PatchPeriod): string {
  if (p.crosses_patch && p.patch_to) return p.patch_from ? `${p.patch_from} to ${p.patch_to}` : p.patch_to;
  if (p.patch_to) return `Data update within ${p.patch_to}`;
  return "Data update";
}

function ItemName({ name, linked }: { name: string; linked: boolean }) {
  const cls = "font-cond text-[20px] font-bold leading-none text-ink [overflow-wrap:anywhere]";
  return linked
    ? <a href={toHash.item(name)} className={`${cls} press hover:underline`}>{name}</a>
    : <span className={cls}>{name}</span>;
}

function Change({ label, from, to, cost }: { label: string; from: string | number | null; to: string | number | null; cost?: boolean }) {
  const fmt = (v: string | number | null) => (v == null ? "none" : cost && typeof v === "number" ? `${v.toLocaleString("en-US")}g` : String(v));
  return (
    <div className="flex items-baseline justify-between gap-3 border-t border-line py-1.5 text-note">
      <dt className="text-muted">{label}</dt>
      <dd className="num whitespace-nowrap text-right">
        <span className="text-quiet">{fmt(from)}</span>
        <span aria-hidden="true" className="px-1.5 text-quiet">→</span><span className="sr-only"> to </span>
        <span className="font-semibold text-ink">{fmt(to)}</span>
      </dd>
    </div>
  );
}

function Period({ p, known }: { p: PatchPeriod; known: Set<string> }) {
  const hl = p.highlights ?? [];
  const total = p.changed.length + p.added.length + p.removed.length;
  const from = shortDate(p.from) ?? p.from;
  const to = shortDate(p.to) ?? p.to;
  return (
    <section aria-labelledby={`p-${p.from}-${p.to}`} className="border-t border-line-strong pt-4" data-testid="patch-period">
      <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
        <h2 id={`p-${p.from}-${p.to}`} className="font-cond text-head font-extrabold text-ink">{periodTitle(p)}</h2>
        <p className="num text-cap text-quiet">{from} – {to}</p>
      </div>
      {p.official_url && (
        <a href={p.official_url} target="_blank" rel="noopener noreferrer"
          className="press inline-flex min-h-11 items-center text-note font-semibold text-blue hover:underline">
          Official patch notes
        </a>
      )}

      <h3 className="sr-only">Biggest changes</h3>
      {hl.length === 0 ? (
        <p className="mt-2 max-w-[62ch] text-copy text-muted">
          {!p.crosses_patch && p.added.length > 0
            ? `No item stats moved. ${p.added.length} item${p.added.length === 1 ? "" : "s"} entered Ichor’s data here; they were already in the game, so they are not listed as new.`
            : "No item cost or stat moved enough to call out."}
        </p>
      ) : (
        <ul className="mt-2" data-testid="patch-highlights">
          {hl.map((h) => (
            <li key={`${h.change}-${h.name}`} className="grid grid-cols-[40px_minmax(0,1fr)] items-center gap-3 border-b border-line py-2.5">
              <Art name={h.name} kind="item" className="h-10 w-10 rounded-[8px]" />
              <div className="min-w-0">
                <p className="flex flex-wrap items-baseline gap-x-2.5">
                  <ItemName name={h.name} linked={known.has(h.name)} />
                  <span className="text-cap font-semibold uppercase text-ink-soft">{KIND[h.change]}</span>
                </p>
                <p className="mt-0.5 text-note text-muted">{h.headline}</p>
              </div>
            </li>
          ))}
        </ul>
      )}

      {total > 0 && (
        <div className="mt-1">
          <Disclosure title={`All ${total} change${total === 1 ? "" : "s"}`} hint="Every cost and stat, old to new" testId="patch-all">
            <ul className="grid gap-x-8 gap-y-4 lg:grid-cols-2">
              {p.changed.map((d) => (
                <li key={d.name}>
                  <p className="flex items-baseline gap-2.5">
                    <ItemName name={d.name} linked={known.has(d.name)} />
                    <span className="text-cap font-semibold uppercase text-ink-soft">{KIND[d.verdict]}</span>
                  </p>
                  <dl className="mt-1">
                    {d.cost && <Change label="Cost" from={d.cost[0]} to={d.cost[1]} cost />}
                    {Object.entries(d.stats ?? {}).map(([s, [a, b]]) => <Change key={s} label={s} from={a} to={b} />)}
                  </dl>
                </li>
              ))}
            </ul>
            {p.added.length > 0 && (
              <div className="mt-4">
                <h4 className="font-cond text-[18px] font-bold uppercase text-muted">
                  {p.crosses_patch === false ? "Entered Ichor’s data" : "Added"}
                </h4>
                <p className="mt-1 text-copy text-ink-soft">{p.added.join(", ")}</p>
              </div>
            )}
            {p.removed.length > 0 && (
              <div className="mt-4">
                <h4 className="font-cond text-[18px] font-bold uppercase text-muted">Removed</h4>
                <p className="mt-1 text-copy text-muted">{p.removed.join(", ")}</p>
              </div>
            )}
          </Disclosure>
        </div>
      )}
    </section>
  );
}

export function PatchPage({ periods, itemNames = [] }: { periods: PatchPeriod[]; itemNames?: string[] }) {
  const known = new Set(itemNames);
  const patches = periods.filter((p) => p.crosses_patch).length;
  // Changes the game made: periods that cross a patch. A refresh inside one
  // patch is Ichor catching up on its own data, and its "added" items were
  // already in the game, so they are not counted as changes here.
  const changes = periods.filter((p) => p.crosses_patch)
    .reduce((n, p) => n + p.changed.length + p.added.length + p.removed.length, 0);

  return (
    <div className="mx-auto w-full max-w-[1240px] px-4 pb-12 lg:px-6">
      <div className="max-w-[760px]">
        <PageHead title="Patch notes" testId="patch-head">
          <p data-testid="patch-claim">
            {periods.length === 0
              ? <><Em>Nothing has changed yet.</Em></>
              : patches === 0
                ? <><Em>No patch has landed</Em> in Ichor&rsquo;s data yet.</>
                : <><Em>{changes} item change{changes === 1 ? "" : "s"}</Em> across <Em>{patches} patch{patches === 1 ? "" : "es"}</Em>, newest first.</>}
          </p>
        </PageHead>
        <p className="mt-2 max-w-[62ch] text-note text-muted lg:text-copy">
          {periods.length === 0
            ? "Patch history is a diff between two data refreshes, so it starts empty and fills in from the first snapshot onward. This isn’t a loading state."
            : "Each update leads with its biggest changes; every cost and stat is one tap below. Items only — gods and system changes are not tracked yet."}
        </p>

        {periods.length > 0 && (
          <div className="mt-6 flex flex-col gap-8">
            {periods.map((p) => <Period key={`${p.from}-${p.to}`} p={p} known={known} />)}
          </div>
        )}

        {periods.length > 0 && (
          <section aria-labelledby="picked-h" className="mt-10 border-t border-line pt-4">
            <h2 id="picked-h" className="font-cond text-[20px] font-extrabold text-ink">How the biggest changes are picked</h2>
            <p className="mt-1 max-w-[62ch] text-note text-muted">
              Automatically, up to five per update: removed items first, then new items, then the items whose cost
              or any one stat moved the most relative to its old value (20 to 30 power is a 50% move). Reworded
              passives with no number to compare stay in the full list. Official notes are linked only where the
              link has been checked by hand.
            </p>
          </section>
        )}
      </div>
    </div>
  );
}
