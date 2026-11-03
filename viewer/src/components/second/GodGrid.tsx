/** "Who are you playing?" — where the app opens.
 *
 * Big card art, because a player recognises their god by its face faster than
 * by its name. Search sits at the top for the keyboard; the role filter sits
 * at the bottom of a phone, inside thumb reach, just above the tab bar. Both
 * live in the hash query so a filtered roster can be linked. */
import { useMemo, useRef } from "react";
import type { God } from "../../types";
import { LANES, godLane, laneTextClass, type Lane } from "../../lib/roleAccent";
import { filterGods } from "./filterGods";
import { useUrlState } from "../../lib/urlState";
import { toHash } from "../../lib/useHashRoute";
import { Art, CloseGlyph, SearchGlyph } from "./art";
import { useWide } from "./useWide";

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

/** The card-art grid. Links to each god's page by default; with `onPick` the
 *  cards are buttons that hand the name back (the match board's you-slot). */
export function GodCards({ gods, onPick, current, className = "",
  cols = "grid-cols-3 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-7 lg:gap-3" }: {
  gods: God[]; onPick?: (name: string) => void; current?: string; className?: string; cols?: string;
}) {
  return (
    <ul className={`grid gap-2.5 ${cols} ${className}`} data-testid="god-grid">
      {gods.map((g, i) => {
        const lane = godLane(g.role);
        const on = g.name === current;
        const body = (
          <>
            <Art name={g.name} kind="card" eager={i < 12}
              className="aspect-[2/3] w-full transition-transform duration-300 ease-[var(--ease-out-expo)] group-hover:scale-[1.03]" />
            <span aria-hidden="true" className="absolute inset-x-0 bottom-0 h-2/3 bg-gradient-to-t from-black/90 via-black/45 to-transparent" />
            <span className="absolute inset-x-0 bottom-0 px-2 pb-2 text-left">
              <span className="block font-cond text-[21px] font-extrabold uppercase leading-[0.95] text-ink [overflow-wrap:anywhere]">{g.name}</span>
              <span className={`mt-0.5 block truncate text-cap ${laneTextClass(lane)}`}>{lane ?? g.role}</span>
            </span>
          </>
        );
        const cls = `press group relative block w-full overflow-hidden rounded-[12px] bg-surface ${on ? "ring-2 ring-accent" : ""}`;
        return (
          <li key={g.name}>
            {onPick ? (
              <button type="button" onClick={() => onPick(g.name)} aria-pressed={on} className={cls}>{body}</button>
            ) : (
              <a href={toHash.god(g.name)} className={cls}>{body}</a>
            )}
          </li>
        );
      })}
    </ul>
  );
}

export function GodGrid({ gods, lastGod, title = "Who are you playing?",
  lede = "Pick your god for the build, then add the enemy team as it locks in." }: {
  gods: God[]; lastGod?: string | null; title?: string; lede?: string;
}) {
  const [f, setF] = useUrlState(decode, encode);
  const input = useRef<HTMLInputElement>(null);
  const wide = useWide();
  const shown = useMemo(() => filterGods(gods, f.q, f.role), [gods, f]);
  const last = lastGod ? gods.find((g) => g.name === lastGod) : undefined;

  return (
    <div className="mx-auto w-full max-w-[1240px] px-4 pt-6 lg:px-6 lg:pt-10">
      <div className="lg:flex lg:items-end lg:justify-between lg:gap-8">
        <div>
          <h1 className="font-cond text-[52px] font-extrabold leading-[0.9] text-ink [text-wrap:balance] lg:text-hero">
            {title}
          </h1>
          <p className="mt-2 text-copy text-muted">{lede}</p>
        </div>
        <div className="mt-4 flex flex-col gap-3 lg:mt-0 lg:w-[460px]">
          <label className="flex h-12 items-center gap-2 rounded-[12px] border border-line bg-surface px-3 focus-within:border-accent">
            <SearchGlyph size={20} className="text-quiet" />
            <span className="sr-only">Search gods</span>
            <input ref={input} type="search" value={f.q} onChange={(e) => setF((p) => ({ ...p, q: e.target.value }))}
              onKeyDown={(e) => { if (e.key === "Enter" && shown[0]) window.location.hash = toHash.god(shown[0].name); }}
              placeholder={`Search ${gods.length} gods`} autoComplete="off" enterKeyHint="go"
              className="min-w-0 flex-1 bg-transparent text-copy text-ink placeholder:text-quiet focus:outline-none focus-visible:outline-none" />
            {f.q && (
              <button type="button" aria-label="Clear search" onClick={() => { setF((p) => ({ ...p, q: "" })); input.current?.focus(); }}
                className="press -mr-1 flex h-10 w-10 items-center justify-center text-quiet hover:text-ink">
                <CloseGlyph size={18} />
              </button>
            )}
          </label>
          {wide && <RoleFilter role={f.role} onChange={(role) => setF((p) => ({ ...p, role }))} />}
        </div>
      </div>

      {last && !f.q && !f.role && (
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
      <GodCards gods={shown} className="mt-5" />
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
