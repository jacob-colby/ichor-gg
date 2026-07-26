import { useMemo, useState } from "react";
import type { God } from "../types";
import { filterGods, sortGods, type GodFilter } from "../lib/godFilters";
import { iconSlug } from "../lib/builds";
import { usePins } from "../lib/pins";
import { LANES, godLane, laneTextClass, type Lane } from "../lib/roleAccent";

function PinIcon({ filled }: { filled: boolean }) {
  return (
    <svg viewBox="0 0 24 24" width="13" height="13" fill={filled ? "currentColor" : "none"} stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 17v5" /><path d="M9 10.76a2 2 0 0 1-1.11 1.79l-1.78.9A2 2 0 0 0 5 15.24V16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-.76a2 2 0 0 0-1.11-1.79l-1.78-.9A2 2 0 0 1 15 10.76V6h1a1 1 0 0 0 0-2H8a1 1 0 0 0 0 2h1z" />
    </svg>
  );
}

const LANE_DOT: Record<Lane, string> = {
  Solo: "bg-role-warrior",
  Jungle: "bg-role-assassin",
  Mid: "bg-role-mid",
  Carry: "bg-role-hunter",
  Support: "bg-role-guardian",
};

interface GodCardProps {
  god: God;
  selected: boolean;
  pinned: boolean;
  onSelect: () => void;
  onTogglePin: () => void;
  onRemove?: () => void;
}

function GodCard({ god, selected, pinned, onSelect, onTogglePin, onRemove }: GodCardProps) {
  const lane = godLane(god.role);
  return (
    <div
      role="button"
      tabIndex={0}
      aria-label={`Select ${god.name}`}
      aria-pressed={selected}
      onClick={onSelect}
      onKeyDown={(e) => { if (e.key === "Enter") onSelect(); }}
      className={`press group relative flex cursor-pointer flex-col items-center gap-1 rounded-lg border p-1.5 pt-2 transition-colors duration-[180ms] ease-standard ${
        selected
          ? "border-gold shadow-glow bg-bg3"
          : pinned
          ? "border-gold/40 bg-gradient-to-b from-bg3 to-bg2"
          : "border-line bg-bg2 hover:border-line-strong"
      }`}
    >
      <img
        src={`/icons/${iconSlug(god.name)}-head.png`}
        alt=""
        className="h-9 w-9 rounded-md object-cover"
        onError={(e) => {
          const i = e.currentTarget;
          if (i.dataset.r) { i.style.visibility = "hidden"; return; }
          i.dataset.r = "1";
          i.src = `/icons/${iconSlug(god.name)}-head.png?r=1`;
        }}
      />
      <div className="w-full truncate text-center font-display text-[10.5px] font-semibold leading-tight text-ink" title={god.name}>
        {god.name}
      </div>
      <div className={`h-[3px] w-5 rounded-full ${lane ? LANE_DOT[lane] : "bg-line-strong"}`} />
      <button
        type="button"
        onClick={(e) => { e.stopPropagation(); onTogglePin(); }}
        aria-label={pinned ? `Unpin ${god.name}` : `Pin ${god.name}`}
        className={`absolute right-0 top-0 flex h-8 w-8 items-center justify-center rounded transition-colors ${
          pinned ? "text-gold" : "text-muted hover:text-ink-soft focus-visible:text-ink-soft"
        }`}
      >
        <PinIcon filled={pinned} />
      </button>
      {onRemove && (
        <button
          type="button"
          onClick={(e) => { e.stopPropagation(); if (confirm(`Remove ${god.name} from the pool?`)) onRemove(); }}
          title={`Remove ${god.name}`}
          aria-label={`Remove ${god.name}`}
          className="press absolute -left-1 -top-1 flex items-center gap-0.5 rounded border border-dashed border-line-strong bg-bg0/90 px-1 py-px font-mono text-[7px] uppercase tracking-wider text-faint hover:text-muted"
        >
          ×
        </button>
      )}
    </div>
  );
}

interface GodPickerBodyProps {
  gods: God[];
  filter: GodFilter;
  setFilter: (patch: Partial<GodFilter>) => void;
  clear: () => void;
  filtersOpen: boolean;
  setFiltersOpen: (open: boolean) => void;
  pantheons: string[];
  damages: string[];
  selectedGod: string | null;
  isPinned: (name: string) => boolean;
  togglePin: (name: string) => void;
  onPick: (name: string) => void;
  onRemove?: (name: string) => void;
}

/** Search + filters + grid, shared by the desktop sidebar and the mobile
 * full-screen picker so filtering/pin behavior can't drift between them. */
function GodPickerBody({
  gods, filter, setFilter, clear, filtersOpen, setFiltersOpen, pantheons, damages,
  selectedGod, isPinned, togglePin, onPick, onRemove,
}: GodPickerBodyProps) {
  const shown = useMemo(() => sortGods(filterGods(gods, filter)), [gods, filter]);
  const pinned = shown.filter((g) => isPinned(g.name));
  const rest = shown.filter((g) => !isPinned(g.name));
  const selCls = "w-full rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-xs text-muted focus:border-blue focus:outline-none";
  const gridCls = "grid grid-cols-4 gap-2";

  return (
    <div className="flex flex-col">
      <div className="sticky top-0 z-10 bg-bg0/95 px-3 pb-2.5 pt-2.5 backdrop-blur">
        <div className="mb-2 flex items-center gap-2 rounded-md border border-line bg-bg2 px-3 py-2 focus-within:border-blue">
          <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2" className="text-muted shrink-0"><circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" /></svg>
          <input
            placeholder="Search gods…"
            value={filter.q ?? ""}
            onChange={(e) => setFilter({ q: e.target.value })}
            className="w-full bg-transparent text-xs text-ink placeholder:text-muted focus:outline-none"
          />
        </div>
        <div className="mb-2 flex flex-wrap items-center gap-1.5">
          <button type="button" onClick={() => setFilter({ lane: undefined })}
            className={`press rounded-full px-2.5 py-1 text-[11px] ${!filter.lane ? "bg-gold font-semibold text-bg0" : "border border-line text-muted"}`}>All</button>
          {LANES.map((lane: Lane) => {
            const active = filter.lane === lane;
            return (
              <button key={lane} type="button" onClick={() => setFilter({ lane: active ? undefined : lane })}
                className={`press rounded-full px-2.5 py-1 text-[11px] ${active ? "bg-gold font-semibold text-bg0" : `border border-line ${laneTextClass(lane)}`}`}>{lane}</button>
            );
          })}
        </div>
        <button type="button" onClick={() => setFiltersOpen(!filtersOpen)}
          className="flex items-center gap-1 font-mono text-[10px] uppercase tracking-[0.08em] text-faint hover:text-muted">
          <svg viewBox="0 0 24 24" width="10" height="10" fill="none" stroke="currentColor" strokeWidth="3" className={`transition-transform ${filtersOpen ? "rotate-90" : ""}`}><path d="M9 6l6 6-6 6" /></svg>
          Filters
        </button>
        {filtersOpen && (
          <div className="mt-2 flex flex-col gap-1.5">
            <select value={filter.pantheon ?? ""} onChange={(e) => setFilter({ pantheon: e.target.value || undefined })} className={selCls}>
              <option value="">All pantheons</option>
              {pantheons.map((p) => <option key={p} value={p}>{p}</option>)}
            </select>
            <select value={filter.damage_type ?? ""} onChange={(e) => setFilter({ damage_type: e.target.value || undefined })} className={selCls}>
              <option value="">All damage</option>
              {damages.map((d) => <option key={d} value={d}>{d}</option>)}
            </select>
          </div>
        )}
        <div className="mt-2 font-mono text-[10.5px] text-faint">{shown.length} gods</div>
      </div>

      <div className="px-3 pb-4">
        {shown.length === 0 ? (
          <div className="flex flex-col items-center gap-2 py-14 text-center">
            <p className="text-xs text-muted">No gods match those filters.</p>
            <button type="button" onClick={clear} className="text-xs text-blue hover:underline">Clear filters</button>
          </div>
        ) : (
          <>
            {pinned.length > 0 && (
              <>
                <div className="mb-1.5 font-mono text-[10px] uppercase tracking-[0.1em] text-gold">Pinned</div>
                <div className={`${gridCls} mb-4`}>
                  {pinned.map((g) => (
                    <GodCard key={g.name} god={g} selected={g.name === selectedGod} pinned
                      onSelect={() => onPick(g.name)} onTogglePin={() => togglePin(g.name)}
                      onRemove={onRemove ? () => onRemove(g.name) : undefined} />
                  ))}
                </div>
              </>
            )}
            <div className={gridCls}>
              {rest.map((g) => (
                <GodCard key={g.name} god={g} selected={g.name === selectedGod} pinned={false}
                  onSelect={() => onPick(g.name)} onTogglePin={() => togglePin(g.name)}
                  onRemove={onRemove ? () => onRemove(g.name) : undefined} />
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
}

export interface GodSidebarProps {
  gods: God[];
  selectedGod: string | null;
  onSelect: (name: string) => void;
  onRemove?: (name: string) => void;
}

/** Left-column god picker for the Builds view. Desktop: a sticky-header,
 * 4-column scrollable grid. Mobile: a header button showing the current god
 * that opens a full-screen picker (see spec section A). Absorbs GodsIndex's
 * search/filter/pin logic and GodRail's role as the builds-view chooser. */
export function GodSidebar({ gods, selectedGod, onSelect, onRemove }: GodSidebarProps) {
  const [filter, setFilterState] = useState<GodFilter>({});
  const [filtersOpen, setFiltersOpen] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);
  const { toggle, isPinned } = usePins();

  const pantheons = useMemo(() => Array.from(new Set(gods.map((g) => g.pantheon).filter(Boolean))).sort(), [gods]);
  const damages = useMemo(() => Array.from(new Set(gods.map((g) => g.damage_type).filter(Boolean))).sort(), [gods]);

  const setFilter = (patch: Partial<GodFilter>) => setFilterState((f) => ({ ...f, ...patch }));
  const clear = () => setFilterState({});

  const current = selectedGod ? gods.find((g) => g.name === selectedGod) : undefined;

  const pick = (name: string) => {
    onSelect(name);
    setMobileOpen(false);
  };

  const bodyProps = {
    gods, filter, setFilter, clear, filtersOpen, setFiltersOpen, pantheons, damages,
    selectedGod, isPinned, togglePin: toggle, onRemove,
  };

  return (
    <>
      {/* Desktop sidebar — fixed-width, scrollable column. */}
      <div className="hidden md:flex md:w-[300px] md:shrink-0 md:flex-col md:overflow-y-auto md:border-r md:border-line">
        <GodPickerBody {...bodyProps} onPick={onSelect} />
      </div>

      {/* Mobile trigger — replaces the sidebar with a compact header button. */}
      <div className="border-b border-line bg-rail p-2 md:hidden">
        <button
          type="button"
          onClick={() => setMobileOpen(true)}
          aria-label={current ? `Change god (currently ${current.name})` : "Select a god"}
          className="press flex w-full items-center justify-between gap-2 rounded-md border border-line bg-bg2 px-3 py-2"
        >
          <span className="flex min-w-0 items-center gap-2">
            {current && (
              <img src={`/icons/${iconSlug(current.name)}-head.png`} alt="" className="h-6 w-6 shrink-0 rounded object-cover" />
            )}
            <span className={`truncate text-sm ${current ? "text-ink" : "text-muted"}`}>{current ? current.name : "Select a god"}</span>
          </span>
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2" className="shrink-0 text-faint"><path d="M6 9l6 6 6-6" /></svg>
        </button>
      </div>

      {mobileOpen && (
        <div role="dialog" aria-modal="true" aria-label="Choose a god" className="fixed inset-0 z-50 flex flex-col overflow-hidden bg-bg0 md:hidden">
          <div className="flex items-center justify-between border-b border-line px-3 py-2.5">
            <span className="font-display text-sm font-semibold text-ink">Choose a god</span>
            <button type="button" onClick={() => setMobileOpen(false)} aria-label="Close" className="press flex h-8 w-8 items-center justify-center rounded-md bg-bg2 text-muted hover:text-ink">
              <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2"><path d="M6 6l12 12M18 6L6 18" /></svg>
            </button>
          </div>
          <div className="flex-1 overflow-y-auto">
            <GodPickerBody {...bodyProps} onPick={pick} />
          </div>
        </div>
      )}
    </>
  );
}
