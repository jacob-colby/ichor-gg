/* The subject switcher.
 *
 * In the tool-first shell this was a permanent 300px column that existed only
 * on the builds route — 300px of chrome beside a 92px rail, on the one route
 * people use most. In a subject-first shell the god is named in the header of
 * every screen, so the picker only has to appear when you're changing it.
 *
 * Its filters are deliberately local rather than URL-backed (see DESIGN.md §
 * The Linkable-State Rule): the rule covers state that changes what a *surface*
 * shows, and a transient dialog isn't one. The god you pick is in the URL; how
 * you found it isn't worth a link.
 */
import { useEffect, useMemo, useRef, useState } from "react";
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

function GodCard({ god, selected, pinned, onSelect, onTogglePin, onRemove }: {
  god: God; selected: boolean; pinned: boolean;
  onSelect: () => void; onTogglePin: () => void; onRemove?: () => void;
}) {
  const lane = godLane(god.role);
  return (
    // The card used to be a div[role="button"] wrapping two focusable buttons —
    // 87 nested-interactive violations, one per god. Select is a real button and
    // the pin/remove controls are siblings layered over it, so nothing nests and
    // every control keeps its own tab stop.
    <div className="group relative">
      <button
        type="button"
        aria-label={`Select ${god.name}`}
        aria-pressed={selected}
        onClick={onSelect}
        className={`plane press flex w-full cursor-pointer flex-col items-center gap-1 rounded-lg border p-1.5 pt-2 transition-colors duration-[180ms] ease-standard ${
          selected ? "is-selected border-gold bg-bg3"
          : pinned ? "border-gold/40 bg-gradient-to-b from-bg3 to-bg2"
          : "border-line bg-bg2 hover:border-line-strong"}`}
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
        <div className="w-full truncate text-center font-display text-label font-semibold leading-tight text-ink" title={god.name}>
          {god.name}
        </div>
        <div className={`h-[3px] w-5 rounded-full ${lane ? LANE_DOT[lane] : "bg-line-strong"}`} />
      </button>

      <button
        type="button"
        onClick={(e) => { e.stopPropagation(); onTogglePin(); }}
        aria-label={pinned ? `Unpin ${god.name}` : `Pin ${god.name}`}
        className={`absolute right-0 top-0 flex h-8 w-8 items-center justify-center rounded-sm transition-colors ${
          pinned ? "text-gold" : "text-muted hover:text-ink-soft focus-visible:text-ink-soft"}`}
      >
        <PinIcon filled={pinned} />
      </button>
      {onRemove && (
        <button
          type="button"
          onClick={(e) => { e.stopPropagation(); if (confirm(`Remove ${god.name} from the pool?`)) onRemove(); }}
          title={`Remove ${god.name}`}
          aria-label={`Remove ${god.name}`}
          className="press absolute -left-1.5 -top-1.5 flex h-6 w-6 items-center justify-center rounded-full border border-dashed border-line-strong bg-bg0/90 text-micro text-faint hover:text-ink"
        >
          ✕
        </button>
      )}
    </div>
  );
}

export interface GodPickerDialogProps {
  gods: God[];
  selectedGod: string | null;
  onPick: (name: string) => void;
  onClose: () => void;
  onRemove?: (name: string) => void;
}

/** Full picker, as a real dialog: labelled, focus-trapped, Escape-dismissed,
 *  and returning focus to whatever opened it. */
export function GodPickerDialog({ gods, selectedGod, onPick, onClose, onRemove }: GodPickerDialogProps) {
  const [filter, setFilter] = useState<GodFilter>({});
  const [filtersOpen, setFiltersOpen] = useState(false);
  const { toggle, isPinned } = usePins();
  const panelRef = useRef<HTMLDivElement>(null);
  const headingRef = useRef<HTMLHeadingElement>(null);

  const pantheons = useMemo(
    () => Array.from(new Set(gods.map((g) => g.pantheon).filter(Boolean))).sort(), [gods]);
  const damages = useMemo(
    () => Array.from(new Set(gods.map((g) => g.damage_type).filter(Boolean))).sort(), [gods]);
  const shown = useMemo(() => sortGods(filterGods(gods, filter)), [gods, filter]);
  const pinned = shown.filter((g) => isPinned(g.name));
  const rest = shown.filter((g) => !isPinned(g.name));

  const patch = (p: Partial<GodFilter>) => setFilter((f) => ({ ...f, ...p }));
  const clear = () => setFilter({});

  useEffect(() => {
    const opener = document.activeElement as HTMLElement | null;
    headingRef.current?.focus();
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") { e.stopPropagation(); onClose(); return; }
      if (e.key !== "Tab") return;
      const f = panelRef.current?.querySelectorAll<HTMLElement>(
        'a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])');
      if (!f || f.length === 0) return;
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    };
    document.addEventListener("keydown", onKeyDown, true);
    return () => { document.removeEventListener("keydown", onKeyDown, true); opener?.focus?.(); };
  }, [onClose]);

  const selCls = "w-full rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-small text-muted focus:border-blue focus:outline-none";

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center overflow-y-auto bg-black/60 p-4" onClick={onClose}>
      <div
        ref={panelRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby="god-picker-title"
        className="my-auto flex w-full max-w-3xl flex-col rounded-lg border border-line bg-bg1 shadow-raised"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center gap-3 border-b border-line px-4 py-3">
          <h2 id="god-picker-title" ref={headingRef} tabIndex={-1}
            className="font-display text-lead font-bold text-ink focus:outline-none">
            Choose a god
          </h2>
          <span className="text-label text-faint">
            <span className="font-mono">{shown.length}</span> of <span className="font-mono">{gods.length}</span>
          </span>
          <button type="button" onClick={onClose} aria-label="Close"
            className="press ml-auto flex h-8 w-8 items-center justify-center rounded-md bg-bg2 text-muted hover:text-ink">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2"><path d="M6 6l12 12M18 6L6 18" /></svg>
          </button>
        </div>

        <div className="flex flex-col gap-2 border-b border-line px-4 py-3">
          <div className="flex items-center gap-2 rounded-md border border-line bg-bg2 px-3 py-2 focus-within:border-blue">
            <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2" className="shrink-0 text-muted" aria-hidden="true">
              <circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" />
            </svg>
            <input
              autoFocus
              placeholder="Search gods…"
              aria-label="Search gods"
              value={filter.q ?? ""}
              onChange={(e) => patch({ q: e.target.value })}
              className="w-full bg-transparent py-1 text-small text-ink placeholder:text-muted focus:outline-none"
            />
          </div>
          <div className="flex flex-wrap items-center gap-1.5">
            <button type="button" aria-pressed={!filter.lane} onClick={() => patch({ lane: undefined })}
              className={`press rounded-full px-2.5 py-1.5 text-label ${!filter.lane ? "bg-gold font-semibold text-bg0" : "border border-line text-muted"}`}>All</button>
            {LANES.map((lane) => {
              const active = filter.lane === lane;
              return (
                <button key={lane} type="button" aria-pressed={active}
                  onClick={() => patch({ lane: active ? undefined : lane })}
                  className={`press rounded-full px-2.5 py-1.5 text-label ${active ? "bg-gold font-semibold text-bg0" : `border border-line ${laneTextClass(lane)}`}`}>{lane}</button>
              );
            })}
            <button type="button" onClick={() => setFiltersOpen((v) => !v)} aria-expanded={filtersOpen}
              className="press ml-auto flex items-center gap-1 rounded-sm px-1 py-1.5 text-label font-medium text-faint hover:text-muted">
              <svg viewBox="0 0 24 24" width="10" height="10" fill="none" stroke="currentColor" strokeWidth="3" aria-hidden="true"
                className={`transition-transform ${filtersOpen ? "rotate-90" : ""}`}><path d="M9 6l6 6-6 6" /></svg>
              More filters
            </button>
          </div>
          {filtersOpen && (
            <div className="grid grid-cols-1 gap-1.5 sm:grid-cols-2">
              <select value={filter.pantheon ?? ""} aria-label="Filter by pantheon"
                onChange={(e) => patch({ pantheon: e.target.value || undefined })} className={selCls}>
                <option value="">All pantheons</option>
                {pantheons.map((p) => <option key={p} value={p}>{p}</option>)}
              </select>
              <select value={filter.damage_type ?? ""} aria-label="Filter by damage type"
                onChange={(e) => patch({ damage_type: e.target.value || undefined })} className={selCls}>
                <option value="">All damage</option>
                {damages.map((d) => <option key={d} value={d}>{d}</option>)}
              </select>
            </div>
          )}
        </div>

        <div className="max-h-[60vh] overflow-y-auto px-4 py-3">
          {shown.length === 0 ? (
            <div className="flex flex-col items-center gap-2 py-14 text-center">
              <p className="text-small text-muted">No gods match those filters.</p>
              <button type="button" onClick={clear} className="press rounded-sm px-1 py-1 text-small text-blue hover:underline">
                Clear filters
              </button>
            </div>
          ) : (
            <>
              {pinned.length > 0 && (
                <>
                  <div className="mb-1.5 font-mono text-label uppercase tracking-[0.1em] text-gold">Pinned</div>
                  <div className="mb-4 grid grid-cols-4 gap-2 sm:grid-cols-6 lg:grid-cols-8">
                    {pinned.map((g) => (
                      <GodCard key={g.name} god={g} selected={g.name === selectedGod} pinned
                        onSelect={() => onPick(g.name)} onTogglePin={() => toggle(g.name)}
                        onRemove={onRemove ? () => onRemove(g.name) : undefined} />
                    ))}
                  </div>
                </>
              )}
              <div className="grid grid-cols-4 gap-2 sm:grid-cols-6 lg:grid-cols-8">
                {rest.map((g) => (
                  <GodCard key={g.name} god={g} selected={g.name === selectedGod} pinned={false}
                    onSelect={() => onPick(g.name)} onTogglePin={() => toggle(g.name)}
                    onRemove={onRemove ? () => onRemove(g.name) : undefined} />
                ))}
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
