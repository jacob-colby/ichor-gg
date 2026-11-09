/** Recent player builds for one god, newest first, with filters.
 *
 * Native selects: five filters in a phone-width column, each a 44px target and
 * each already accessible. Items are drawn as a set (the store holds inventory
 * slots, not a confirmed buy order) and the footnote says so. */
import { useMemo, useState } from "react";
import { ItemIcon } from "../ItemIcon";
import { toHash } from "../../lib/useHashRoute";
import {
  ALL, NO_ASPECT, NO_FILTERS, ago, filterBuilds, isFiltered,
  type RecentFile, type RecentFilters,
} from "../../lib/recentBuilds";
import { useJson } from "./useComparison";

const SHOWN = 20;
const shortAspect = (a: string) => a.replace(/^Aspect of /i, "").replace(/^the /i, "");

function Select({ label, value, onChange, children }: {
  label: string; value: string; onChange: (v: string) => void; children: React.ReactNode;
}) {
  return (
    <label className="block min-w-0">
      <span className="block px-1 text-cap text-quiet">{label}</span>
      <select value={value} onChange={(e) => onChange(e.target.value)}
        className="mt-0.5 h-11 w-full min-w-0 rounded-[10px] bg-surface px-2.5 font-cond text-[17px] font-bold uppercase text-ink ring-1 ring-line">
        {children}
      </select>
    </label>
  );
}

export function RecentBuilds({ god, file, now }: { god: string; file: RecentFile; now?: number }) {
  const [f, setF] = useState<RecentFilters>(NO_FILTERS);
  const [more, setMore] = useState(false);
  const set = (p: Partial<RecentFilters>) => { setF((x) => ({ ...x, ...p })); setMore(false); };
  const rows = useMemo(() => filterBuilds(file.builds, f), [file.builds, f]);
  const shown = more ? rows : rows.slice(0, SHOWN);

  return (
    <section aria-labelledby="recent-h" data-testid="recent-builds" className="mt-6">
      <h2 id="recent-h" className="px-1 font-cond text-[16px] font-bold uppercase text-muted">
        Recent {god} builds · Obsidian+
      </h2>
      <div role="group" aria-label="Filter recent builds" className="mt-1.5 grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-5">
        <Select label="Role" value={f.role} onChange={(role) => set({ role })}>
          <option value={ALL}>All roles</option>
          {file.roles.map((r) => <option key={r} value={r}>{r}</option>)}
        </Select>
        <Select label="Aspect" value={f.aspect} onChange={(aspect) => set({ aspect })}>
          <option value={ALL}>Any</option>
          {file.aspects.map((a) => <option key={a} value={a}>{shortAspect(a)}</option>)}
          <option value={NO_ASPECT}>No aspect</option>
        </Select>
        <Select label="Result" value={f.result} onChange={(result) => set({ result: result as RecentFilters["result"] })}>
          <option value="all">Any</option>
          <option value="win">Wins</option>
          <option value="loss">Losses</option>
        </Select>
        <Select label="Rank" value={f.master ? "master" : ALL} onChange={(v) => set({ master: v === "master" })}>
          <option value={ALL}>Obsidian+</option>
          <option value="master">Master+</option>
        </Select>
        <Select label="Patch" value={f.patch} onChange={(patch) => set({ patch })}>
          <option value={ALL}>All</option>
          {file.patches.map((p) => <option key={p} value={p}>{p.toUpperCase()}</option>)}
        </Select>
      </div>

      <p className="mt-2 flex items-center justify-between px-1 text-cap text-quiet" aria-live="polite" data-testid="recent-count">
        <span>{rows.length === file.builds.length ? `Latest ${rows.length} matches` : `${rows.length} of the latest ${file.builds.length} matches`}</span>
        {isFiltered(f) && (
          <button type="button" onClick={() => { setF(NO_FILTERS); setMore(false); }}
            className="press h-11 font-cond text-[16px] font-bold uppercase text-accent hover:text-ink">Clear filters</button>
        )}
      </p>

      {rows.length === 0 ? (
        <p className="mt-1 rounded-[12px] border border-dashed border-line p-4 text-copy text-muted">
          None of the latest {file.builds.length} matches fit those filters.
        </p>
      ) : (
        <ol className="mt-1 space-y-1.5" data-testid="recent-list">
          {shown.map((b) => (
            <li key={b.t + b.items.join()} data-testid="recent-row" data-win={b.win}
              className="rounded-[12px] bg-surface px-3 py-2.5">
              <div className="flex flex-wrap items-center gap-x-2 gap-y-0.5 text-note">
                <span className={`font-cond text-[17px] font-bold uppercase ${b.win ? "text-ink" : "text-muted"}`}>{b.win ? "Win" : "Loss"}</span>
                <span className="text-ink-soft">{b.role}</span>
                <span className="text-quiet">·</span>
                <span className="text-muted">{b.aspect ? shortAspect(b.aspect) : "No aspect"}</span>
                {b.master && <span className="rounded-[6px] bg-surface-2 px-1.5 text-cap text-ink-soft">Master+</span>}
                <span className="ml-auto text-cap text-quiet">{b.patch?.toUpperCase()} · {ago(b.t, now)}</span>
              </div>
              <ul className="mt-2 flex flex-wrap gap-1.5" aria-label="Items">
                {b.items.map((n, i) => (
                  <li key={n + i}>
                    <a href={toHash.item(n)} title={n} aria-label={n} className="press block">
                      <ItemIcon name={n} className="h-10 w-10" />
                    </a>
                  </li>
                ))}
              </ul>
              {(b.starter || b.relic) && (
                <p className="mt-1.5 text-cap text-quiet">
                  {b.starter && <>Start {b.starter}</>}{b.starter && b.relic && " · "}{b.relic && <>Relic {b.relic}</>}
                </p>
              )}
            </li>
          ))}
        </ol>
      )}
      {!more && rows.length > SHOWN && (
        <button type="button" onClick={() => setMore(true)}
          className="press mt-2 h-11 w-full rounded-[12px] bg-surface font-cond text-[17px] font-bold uppercase text-muted hover:text-ink">
          Show {rows.length - SHOWN} more
        </button>
      )}
      <p className="mt-3 text-cap text-quiet">
        Games from SmiteBrain, newest first. Almost all are played with an aspect, so base-kit games are a small sample.
        Items are what each player held, not the order they bought them. A game is not a player: a few one-tricks can fill a thin list.
      </p>
    </section>
  );
}

export function useRecent(god: string): RecentFile | null {
  const slug = god.toLowerCase().replace(/ /g, "-").replace(/'/g, "");
  const out = useJson<RecentFile>(`/recent/${slug}.json`);
  const v = out.state === "ready" ? out.value : null;
  // Shape-checked: a host that answers a missing file with some other JSON
  // (an SPA fallback, a test stub) must read as "no recent builds".
  return v && Array.isArray(v.builds) && v.builds.length > 0 && Array.isArray(v.roles)
    && Array.isArray(v.aspects) && Array.isArray(v.patches) ? v : null;
}
