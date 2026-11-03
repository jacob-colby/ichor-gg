/** Where the app opens: the field is empty, so this page says what to type,
 *  lists what you typed before, and keeps the whole roster below as the
 *  browsable fallback for anyone who would rather tap a face. */
import { useMemo } from "react";
import type { God } from "../../types";
import { LANES, godInLane, godLane, laneTextClass, type Lane } from "../../lib/roleAccent";
import { useUrlState } from "../../lib/urlState";
import { toHash } from "../../lib/useHashRoute";
import { Art, ChevronGlyph } from "../second/art";
import { RoleFilter } from "../second/GodGrid";
import { Mark } from "../second/AppNav";
import { GrammarHint } from "./CommandChrome";
import { parseQuery, queryHash, type ParsedQuery } from "./query";

interface Filter { role: Lane | "" }
const decode = (p: URLSearchParams): Filter => {
  const role = p.get("role") ?? "";
  return { role: (LANES as readonly string[]).includes(role) ? (role as Lane) : "" };
};
const encode = (f: Filter) => ({ role: f.role || undefined });

const EXAMPLES = ["ra vs hecate ymir", "baron joust", "hou yi vs ares arena"];

export function Landing({ gods, recents, onRun, onClearRecents, stamp, updated, wide }: {
  gods: God[];
  recents: string[];
  onRun: (q: ParsedQuery) => void;
  onClearRecents: () => void;
  stamp: string | null;
  updated?: string;
  wide: boolean;
}) {
  const [f, setF] = useUrlState(decode, encode);
  const shown = useMemo(() => gods
    .filter((g) => !f.role || godInLane(g.role, f.role))
    .sort((a, b) => a.name.localeCompare(b.name)), [gods, f.role]);
  const parsedRecents = useMemo(() => recents.map((r) => ({ text: r, q: parseQuery(r, gods) }))
    .filter((r) => r.q.you), [recents, gods]);

  const run = (e: React.MouseEvent, q: ParsedQuery) => { e.preventDefault(); onRun(q); };

  return (
    <div className="mx-auto w-full max-w-[1240px] px-4 pt-6 lg:px-6 lg:pt-12">
      {!wide && <div className="mb-6"><Mark size={24} /></div>}
      <div className="lg:grid lg:grid-cols-[minmax(0,1fr)_420px] lg:gap-14">
        <div>
          <h1 className="font-cond text-[56px] font-extrabold leading-[0.88] text-ink [text-wrap:balance] lg:text-[84px]">
            Type your matchup
          </h1>
          <p className="mt-3 max-w-[48ch] text-copy text-muted">
            Your god first, then <span className="font-semibold text-ink">vs</span> and whoever&rsquo;s locked in.
            Three letters is usually enough. The build re-ranks for that team.
          </p>
          <div className="mt-4"><GrammarHint /></div>
          <div className="mt-5 flex flex-wrap gap-2" aria-label="Try one" role="group">
            {EXAMPLES.map((ex) => {
              const q = parseQuery(ex, gods);
              if (!q.you) return null;
              return (
                <a key={ex} href={queryHash({ you: q.you, enemies: q.enemies, mode: q.mode, aspect: q.aspect })}
                  onClick={(e) => run(e, q)}
                  className="press inline-flex h-11 items-center gap-2 rounded-full border border-line px-4 text-copy text-muted hover:border-quiet hover:text-ink">
                  <span className="font-medium">{ex}</span>
                </a>
              );
            })}
          </div>
        </div>

        <section aria-labelledby="recent-h" className="mt-8 lg:mt-1">
          <div className="flex items-baseline justify-between">
            <h2 id="recent-h" className="font-cond text-head font-extrabold text-ink">Recent</h2>
            {parsedRecents.length > 0 && (
              <button type="button" onClick={onClearRecents}
                className="press -mr-2 h-11 px-2 text-note font-semibold text-quiet hover:text-ink">Clear</button>
            )}
          </div>
          {parsedRecents.length ? (
            <ul className="mt-2 divide-y divide-line border-y border-line" data-testid="recents">
              {parsedRecents.map(({ text, q }) => (
                <li key={text}>
                  <a href={queryHash({ you: q.you!, enemies: q.enemies, mode: q.mode, aspect: q.aspect })} onClick={(e) => run(e, q)}
                    className="press group flex min-h-16 items-center gap-3 py-2.5">
                    <Art name={q.you!} kind="head" className="h-11 w-11 rounded-[10px] ring-[1.5px] ring-accent" />
                    <span className="min-w-0 flex-1">
                      <span className="block font-cond text-row font-bold text-ink">{q.you}</span>
                      <span className="block truncate text-note text-muted">
                        {q.enemies.length ? `vs ${q.enemies.join(", ")}` : "No enemies yet"}
                        {q.mode && q.mode !== "conquest" ? ` · ${q.mode[0].toUpperCase()}${q.mode.slice(1)}` : ""}
                        {q.aspect ? " · Aspect" : ""}
                      </span>
                    </span>
                    {q.enemies.length > 0 && (
                      <span className="hidden flex-none -space-x-1.5 sm:flex">
                        {q.enemies.slice(0, 5).map((n) => (
                          <Art key={n} name={n} kind="head" className="h-7 w-7 rounded-[6px] ring-[1.5px] ring-ink" />
                        ))}
                      </span>
                    )}
                    <ChevronGlyph size={18} className="flex-none text-quiet group-hover:text-ink" />
                  </a>
                </li>
              ))}
            </ul>
          ) : (
            <p className="mt-2 rounded-[14px] border border-dashed border-line p-4 text-note text-muted">
              Matchups you open land here, in this browser only, so the next draft is one tap.
            </p>
          )}
        </section>
      </div>

      <section aria-labelledby="roster-h" className="mt-10 lg:mt-14">
        <div className="flex flex-col gap-3 lg:flex-row lg:items-end lg:justify-between">
          <div>
            <h2 id="roster-h" className="font-cond text-head font-extrabold text-ink">Or tap your god</h2>
            <p className="mt-1 text-note text-muted">{gods.length} gods. The build opens with your last enemy team, if you entered one.</p>
          </div>
          <RoleFilter role={f.role} onChange={(role) => setF({ role })} className="lg:w-[460px]" />
        </div>
        <p className="sr-only" aria-live="polite">{shown.length} gods shown</p>
        <ul className="mt-4 grid grid-cols-3 gap-2.5 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-8 lg:gap-3" data-testid="god-grid">
          {shown.map((g, i) => {
            const lane = godLane(g.role);
            return (
              <li key={g.name}>
                <a href={toHash.god(g.name)} className="press group relative block overflow-hidden rounded-[12px] bg-surface">
                  <Art name={g.name} kind="card" eager={i < 9}
                    className="aspect-[2/3] w-full transition-transform duration-300 ease-[var(--ease-out-expo)] group-hover:scale-[1.03]" />
                  <span aria-hidden="true" className="absolute inset-x-0 bottom-0 h-2/3 bg-gradient-to-t from-black/90 via-black/45 to-transparent" />
                  <span className="absolute inset-x-0 bottom-0 px-2 pb-2">
                    <span className="block font-cond text-[21px] font-extrabold uppercase leading-[0.95] text-ink [overflow-wrap:anywhere]">{g.name}</span>
                    <span className={`mt-0.5 block truncate text-cap ${laneTextClass(lane)}`}>{lane ?? g.role}</span>
                  </span>
                </a>
              </li>
            );
          })}
        </ul>
        {stamp && (
          <p className="mt-6 text-cap text-quiet" title={updated} data-testid="freshness">{stamp}</p>
        )}
      </section>
      <div className="h-8 lg:h-16" />
    </div>
  );
}
