import { useMemo, useState } from "react";
import type { God } from "../types";
import { filterGods, sortGods, type GodFilter } from "../lib/godFilters";
import { iconSlug } from "../lib/builds";
import { toHash, navigate } from "../lib/useHashRoute";
import { usePins } from "../lib/pins";
import { LANES, godLane, laneTextClass, godRoleTextClass, type Lane } from "../lib/roleAccent";

function PinIcon({ filled }: { filled: boolean }) {
  return (
    <svg viewBox="0 0 24 24" width="14" height="14" fill={filled ? "currentColor" : "none"} stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 17v5" /><path d="M9 10.76a2 2 0 0 1-1.11 1.79l-1.78.9A2 2 0 0 0 5 15.24V16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-.76a2 2 0 0 0-1.11-1.79l-1.78-.9A2 2 0 0 1 15 10.76V6h1a1 1 0 0 0 0-2H8a1 1 0 0 0 0 2h1z" />
    </svg>
  );
}

function GodCard({ god, pinned, onTogglePin }: { god: God; pinned: boolean; onTogglePin: () => void }) {
  return (
    <div
      className={`press group relative cursor-pointer rounded-xl border transition-colors duration-[180ms] ease-standard ${
        pinned
          ? "border-gold/40 bg-gradient-to-b from-bg3 to-bg2 shadow-glow"
          : "border-line bg-bg2 hover:border-line-strong"
      }`}
      onClick={() => navigate(toHash.god(god.name))}
      role="button"
      tabIndex={0}
      onKeyDown={(e) => { if (e.key === "Enter") navigate(toHash.god(god.name)); }}
    >
      <div className="flex flex-col items-center gap-1.5 px-2 pb-2 pt-2.5">
        <img
          src={`/icons/${iconSlug(god.name)}-head.png`}
          alt=""
          className="h-11 w-11 rounded-md object-cover sm:h-[52px] sm:w-[52px]"
          onError={(e) => {
            const i = e.currentTarget;
            if (i.dataset.r) { i.style.visibility = "hidden"; return; }
            i.dataset.r = "1";
            i.src = `/icons/${iconSlug(god.name)}-head.png?r=1`;
          }}
        />
        <div className="text-center font-display text-[12.5px] font-semibold leading-tight text-ink">{god.name}</div>
        <div className={`text-[9.5px] ${godRoleTextClass(god)}`}>{godLane(god.role) ?? god.role}</div>
      </div>
      <button
        type="button"
        onClick={(e) => { e.stopPropagation(); onTogglePin(); }}
        aria-label={pinned ? `Unpin ${god.name}` : `Pin ${god.name}`}
        className={`absolute right-1.5 top-1.5 flex h-8 w-8 items-center justify-center rounded-md transition-opacity ${
          pinned ? "text-gold opacity-100" : "text-faint opacity-60 hover:text-ink-soft hover:opacity-100"
        }`}
      >
        <PinIcon filled={pinned} />
      </button>
    </div>
  );
}

export function GodsIndex({ gods }: { gods: God[] }) {
  const [filter, setFilter] = useState<GodFilter>({});
  const { toggle, isPinned } = usePins();
  const pantheons = useMemo(() => Array.from(new Set(gods.map((g) => g.pantheon).filter(Boolean))).sort(), [gods]);
  const damages = useMemo(() => Array.from(new Set(gods.map((g) => g.damage_type).filter(Boolean))).sort(), [gods]);
  const shown = useMemo(() => sortGods(filterGods(gods, filter)), [gods, filter]);
  const pinned = shown.filter((g) => isPinned(g.name));
  const rest = shown.filter((g) => !isPinned(g.name));

  const set = (patch: Partial<GodFilter>) => setFilter((f) => ({ ...f, ...patch }));
  const clear = () => setFilter({});
  const selCls = "rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-xs text-muted focus:border-blue focus:outline-none";
  const gridCls = "grid grid-cols-[repeat(auto-fill,minmax(105px,1fr))] gap-2.5 sm:grid-cols-[repeat(auto-fill,minmax(150px,1fr))]";

  return (
    <div className="p-4">
      {/* Filter bar */}
      <div className="sticky top-0 z-10 -mx-4 mb-4 bg-bg0/95 px-4 pb-3 pt-1 backdrop-blur">
        <div className="mb-3 flex flex-wrap items-center gap-2">
          <div className="flex items-center gap-2 rounded-md border border-line bg-bg2 px-3 py-2 focus-within:border-blue">
            <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2" className="text-muted"><circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" /></svg>
            <input placeholder="Search gods…" value={filter.q ?? ""} onChange={(e) => set({ q: e.target.value })}
              className="w-40 bg-transparent text-xs text-ink placeholder:text-muted focus:outline-none" />
          </div>
          <select value={filter.pantheon ?? ""} onChange={(e) => set({ pantheon: e.target.value || undefined })} className={selCls}>
            <option value="">All pantheons</option>
            {pantheons.map((p) => <option key={p} value={p}>{p}</option>)}
          </select>
          <select value={filter.damage_type ?? ""} onChange={(e) => set({ damage_type: e.target.value || undefined })} className={selCls}>
            <option value="">All damage</option>
            {damages.map((d) => <option key={d} value={d}>{d}</option>)}
          </select>
          <span className="ml-auto font-mono text-[11px] text-faint">{shown.length} gods</span>
        </div>
        {/* Lane pills */}
        <div className="flex flex-wrap items-center gap-2 overflow-x-auto">
          <button type="button" onClick={() => set({ lane: undefined })}
            className={`press rounded-full px-3 py-1.5 text-xs font-semibold ${!filter.lane ? "bg-gold text-bg0" : "border border-line text-muted"}`}>All</button>
          {LANES.map((lane: Lane) => {
            const active = filter.lane === lane;
            return (
              <button key={lane} type="button" onClick={() => set({ lane: active ? undefined : lane })}
                className={`press rounded-full px-3 py-1.5 text-xs ${active ? "bg-gold text-bg0 font-semibold" : `border border-line ${laneTextClass(lane)}`}`}>{lane}</button>
            );
          })}
        </div>
      </div>

      {shown.length === 0 ? (
        <div className="flex flex-col items-center gap-2 py-16 text-center">
          <p className="text-sm text-muted">No gods match those filters.</p>
          <button type="button" onClick={clear} className="text-xs text-blue hover:underline">Clear filters</button>
        </div>
      ) : (
        <>
          {pinned.length > 0 && (
            <>
              <div className="mb-2 font-mono text-[10px] uppercase tracking-[0.1em] text-gold">Pinned</div>
              <div className={`${gridCls} mb-5`}>
                {pinned.map((g) => <GodCard key={g.name} god={g} pinned onTogglePin={() => toggle(g.name)} />)}
              </div>
            </>
          )}
          <div className={gridCls}>
            {rest.map((g) => <GodCard key={g.name} god={g} pinned={false} onTogglePin={() => toggle(g.name)} />)}
          </div>
        </>
      )}
    </div>
  );
}
