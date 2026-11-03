/** "Who are you playing?" — where the app opens.
 *
 * Big card art, because a player recognises their god by its face faster than
 * by its name. The role filter sits at the bottom of a phone, inside thumb
 * reach, just above the tab bar. Both the text and the role live in the hash
 * query so a filtered roster can be linked.
 *
 * The search box is the command field (A + typed query). On a phone it sits
 * here; from `lg` up the top bar's field is the one field and drives this
 * grid through `query`. Either way a plain name filters the grid exactly as
 * the old box did, and the grid's first card is what Enter opens — the grid
 * sorts by the same rank the parser resolves a word with. Typing "vs …" turns
 * Enter into the adapted build instead. */
import { useCallback, useEffect, useMemo, useRef } from "react";
import type { God, Item } from "../../types";
import { LANES, godInLane, godLane, laneTextClass, type Lane } from "../../lib/roleAccent";
import { useUrlState } from "../../lib/urlState";
import { toHash } from "../../lib/useHashRoute";
import { Art } from "./art";
import { useWide } from "./useWide";
import { CommandField } from "../command/CommandField";
import { godRank, gridFilterText, parseQuery, queryHash, type ParsedQuery } from "../command/query";

interface Filter { q: string; role: Lane | "" }
const decode = (p: URLSearchParams): Filter => {
  const role = p.get("role") ?? "";
  return { q: p.get("q") ?? "", role: (LANES as readonly string[]).includes(role) ? (role as Lane) : "" };
};
const encode = (f: Filter) => ({ q: f.q || undefined, role: f.role || undefined });

export function RoleFilter({ role, onChange, className = "" }: {
  role: Lane | ""; onChange: (r: Lane | "") => void; className?: string;
}) {
  const opts: (Lane | "")[] = ["", ...LANES];
  return (
    <div role="group" aria-label="Filter by role" className={`grid grid-cols-6 gap-1 rounded-[14px] bg-surface p-1 ${className}`}>
      {opts.map((l) => {
        const on = l === role;
        return (
          <button key={l || "all"} type="button" aria-pressed={on} onClick={() => onChange(l)}
            className={`press h-11 min-w-0 rounded-[10px] px-1 font-cond text-[16px] font-bold uppercase transition-colors duration-150 ${
              on ? "bg-accent text-accent-ink" : "text-muted hover:text-ink"}`}>
            {l || "All"}
          </button>
        );
      })}
    </div>
  );
}

export interface GodGridProps {
  gods: God[];
  lastGod?: string | null;
  items?: Item[];
  /** Recent queries, newest first (this browser only). */
  recents?: string[];
  onRun?: (q: ParsedQuery) => void;
  onItem?: (name: string) => void;
  onClearRecents?: () => void;
  /** True when the top bar carries the field (lg up): this page then has none
   *  of its own, and `query` is the bar field's filter text (null = untouched). */
  fieldInBar?: boolean;
  query?: string | null;
}

export function GodGrid({ gods, lastGod, items, recents = [], onRun, onItem, onClearRecents, fieldInBar = false, query = null }: GodGridProps) {
  const [f, setF] = useUrlState(decode, encode);
  const wide = useWide();

  // The top bar's field drives the filter from lg up.
  useEffect(() => {
    if (!fieldInBar || query === null) return;
    setF((p) => (p.q === query ? p : { ...p, q: query }));
  }, [query, fieldInBar, setF]);

  const onText = useCallback((text: string, parsed: ParsedQuery) => {
    const q = gridFilterText(text, parsed);
    setF((p) => (p.q === q ? p : { ...p, q }));
  }, [setF]);
  // The field mounts once, with whatever the link carried.
  const seed = useRef(f.q).current;

  const run = onRun ?? ((q: ParsedQuery) => { if (q.you) window.location.hash = queryHash({ ...q, you: q.you }); });

  const shown = useMemo(() => {
    const q = f.q.trim().toLowerCase();
    // The parser's rank, so the first card is what Enter opens.
    // Ranked names first (shortest first within a rank, as the parser does),
    // then the rest of the substring matches A–Z.
    const rank = (name: string) => (q ? godRank(q, name) ?? 9 : 9);
    const byLength = (a: God, b: God) => (rank(a.name) < 9 ? a.name.length - b.name.length : 0);
    return [...gods]
      .filter((g) => (!f.role || godInLane(g.role, f.role)) && (!q || g.name.toLowerCase().includes(q)))
      .sort((a, b) => rank(a.name) - rank(b.name) || byLength(a, b) || a.name.localeCompare(b.name));
  }, [gods, f]);
  const last = lastGod ? gods.find((g) => g.name === lastGod) : undefined;
  const parsedRecents = useMemo(() => recents.map((text) => ({ text, q: parseQuery(text, gods) }))
    .filter((r) => r.q.you), [recents, gods]);
  const idle = !f.q && !f.role;
  const lastInRecents = parsedRecents.some((r) => r.q.you === last?.name);

  return (
    <div className="mx-auto w-full max-w-[1240px] px-4 pt-6 lg:px-6 lg:pt-10">
      <div className="lg:flex lg:items-end lg:justify-between lg:gap-8">
        <div>
          <h1 className="font-cond text-[52px] font-extrabold leading-[0.9] text-ink [text-wrap:balance] lg:text-hero">
            Who are you playing?
          </h1>
          <p className="mt-2 text-copy text-muted">
            Pick your god for the build, or type it with <span className="font-semibold text-ink">vs</span> and the enemy team.
          </p>
        </div>
        <div className="mt-4 flex flex-col gap-3 lg:mt-0 lg:w-[460px]">
          {!fieldInBar && (
            <CommandField variant="page" gridBelow gods={gods} items={items} onItem={onItem}
              seedText={seed} onSubmit={run} onText={onText}
              label="Search gods, or type your god vs the enemy team"
              placeholder={`Search ${gods.length} gods · ra vs hecate`} />
          )}
          {wide && <RoleFilter role={f.role} onChange={(role) => setF((p) => ({ ...p, role }))} />}
        </div>
      </div>

      {idle && parsedRecents.length > 0 && (
        <section aria-labelledby="recent-h" className="mt-5">
          <div className="flex items-baseline justify-between">
            <h2 id="recent-h" className="font-cond text-[16px] font-bold uppercase text-muted">Recent</h2>
            {onClearRecents && (
              <button type="button" onClick={onClearRecents}
                className="press -my-3 h-11 px-1 text-cap font-semibold text-quiet hover:text-ink">Clear</button>
            )}
          </div>
          <ul className="-mx-4 mt-2 flex snap-x scroll-px-4 gap-2 overflow-x-auto px-4 pb-1 [scrollbar-width:none] lg:mx-0 lg:px-0" data-testid="recents">
            {parsedRecents.map(({ text, q }) => (
              <li key={text} className="snap-start">
                <a href={queryHash({ you: q.you!, enemies: q.enemies, mode: q.mode, aspect: q.aspect })}
                  onClick={(e) => { if (onRun) { e.preventDefault(); onRun(q); } }}
                  className="press flex h-14 items-center gap-2.5 rounded-[12px] border border-line bg-surface pl-1.5 pr-3 hover:bg-surface-2">
                  <span className="flex flex-none items-center -space-x-1.5">
                    <Art name={q.you!} kind="head" className="relative z-10 h-10 w-10 rounded-[9px] ring-[1.5px] ring-accent" />
                    {q.enemies.slice(0, 3).map((n) => (
                      <Art key={n} name={n} kind="head" className="h-8 w-8 rounded-[7px] ring-2 ring-surface" />
                    ))}
                  </span>
                  <span className="max-w-[24ch]">
                    <span className="block whitespace-nowrap font-cond text-[18px] font-bold leading-none text-ink">{q.you}</span>
                    <span className="mt-0.5 block truncate text-cap text-muted">
                      {q.enemies.length ? `vs ${q.enemies.join(", ")}` : "Build"}
                      {q.mode && q.mode !== "conquest" ? ` · ${q.mode[0].toUpperCase()}${q.mode.slice(1)}` : ""}
                      {q.aspect ? " · Aspect" : ""}
                    </span>
                  </span>
                </a>
              </li>
            ))}
          </ul>
        </section>
      )}

      {last && idle && !lastInRecents && (
        <a href={toHash.god(last.name)} aria-label={`Back to ${last.name}'s build`}
          className="press mt-5 flex min-h-14 items-center gap-3 rounded-[14px] border border-line bg-surface px-3 py-2 hover:bg-surface-2">
          <Art name={last.name} kind="head" eager className="h-10 w-10 rounded-[10px]" />
          <span className="min-w-0 flex-1">
            <span className="block text-cap text-quiet">Back to</span>
            <span className="block font-cond text-[22px] font-extrabold uppercase leading-none text-ink">{last.name}</span>
          </span>
          <span className="font-cond text-[16px] font-bold uppercase text-accent">Build</span>
        </a>
      )}

      <p className="sr-only" aria-live="polite">{shown.length} gods shown</p>
      <ul className="mt-5 grid grid-cols-3 gap-2.5 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-7 lg:gap-3" data-testid="god-grid">
        {shown.map((g, i) => {
          const lane = godLane(g.role);
          // With text in the field, the first card is Enter's target: say so.
          const target = i === 0 && !!f.q.trim();
          return (
            <li key={g.name}>
              <a href={toHash.god(g.name)} data-enter-target={target || undefined}
                className={`press group relative block overflow-hidden rounded-[12px] bg-surface ${target ? "ring-2 ring-accent" : ""}`}>
                <Art name={g.name} kind="card" eager={i < 12}
                  className="aspect-[2/3] w-full transition-transform duration-300 ease-[var(--ease-out-expo)] group-hover:scale-[1.03]" />
                <span aria-hidden="true" className="absolute inset-x-0 bottom-0 h-2/3 bg-gradient-to-t from-black/90 via-black/45 to-transparent" />
                <span className="absolute inset-x-0 bottom-0 px-2 pb-2">
                  <span className="block font-cond text-[21px] font-extrabold uppercase leading-[0.95] text-ink [overflow-wrap:anywhere]">{g.name}</span>
                  <span className={`mt-0.5 block truncate text-cap ${laneTextClass(lane)}`}>{lane ?? g.role}</span>
                </span>
                {target && (
                  <span aria-hidden="true" className="absolute right-1.5 top-1.5 rounded-[6px] bg-accent px-1.5 py-0.5 font-cond text-[13px] font-bold uppercase text-accent-ink">
                    Enter
                  </span>
                )}
              </a>
            </li>
          );
        })}
      </ul>
      {shown.length === 0 && (
        <p className="py-10 text-center text-copy text-muted">
          No god matches “{f.q}”{f.role ? ` in ${f.role}` : ""}.
        </p>
      )}

      {/* Phone: role filter in thumb reach, above the tab bar. */}
      <div className="h-24 lg:h-16" />
      {!wide && <div className="fixed inset-x-0 bottom-[calc(64px+env(safe-area-inset-bottom))] z-30 border-t border-line bg-ground/95 px-4 py-2 backdrop-blur-sm lg:hidden">
        <RoleFilter role={f.role} onChange={(role) => setF((p) => ({ ...p, role }))} />
      </div>}
    </div>
  );
}
