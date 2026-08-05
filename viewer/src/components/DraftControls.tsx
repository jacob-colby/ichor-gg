/** Shared pieces of the draft board: the god picker, the ally/enemy slot, the
 *  portrait fallback. Two surfaces render a draft now — the full `/draft` page
 *  and the persistent `DraftDock` — and they render it identically rather
 *  than drifting into two slightly different boards. */
import { useEffect, useMemo, useRef, useState } from "react";
import type { God } from "../types";
import { iconSlug } from "../lib/builds";
import { godLane, laneTextClass, LANES, godInLane, type Lane } from "../lib/roleAccent";

/** Art with a real fallback — an initial, never a hole in the row. */
export function Icon({ name, className, item = false }: { name: string; className: string; item?: boolean }) {
  const [tries, setTries] = useState(0);
  if (tries > 1) {
    return (
      <span aria-hidden="true" className={`flex flex-none items-center justify-center rounded-sm bg-bg3 font-display text-label font-bold text-faint ${className}`}>
        {name.slice(0, 1)}
      </span>
    );
  }
  return (
    <img
      src={`/icons/${iconSlug(name)}${item ? "" : "-head"}.png${tries ? "?r=1" : ""}`}
      alt="" loading="lazy" onError={() => setTries((t) => t + 1)}
      className={`flex-none rounded-sm bg-bg2 object-cover ${className}`}
    />
  );
}

/* ── God picker ───────────────────────────────────────────────────────────
 * A real dialog, plus lane filters — 87 undifferentiated squares was the
 * heaviest decision in the app with the least support. Deliberately a
 * filtered *grid*, not a combobox: the results are two-dimensional, so
 * listbox arrow semantics would misdescribe them. Enter takes the first
 * available match.
 */
export function GodPickerModal({ gods, taken, onPick, onClose, opener }: {
  gods: God[];
  /** Gods this slot may not take — already on the SAME team, so they're
   *  disabled. Not the whole board: the two teams may mirror each other, and
   *  in every non-draft queue they routinely do. */
  taken: Set<string>;
  onPick: (name: string) => void;
  onClose: () => void;
  /** The slot button that opened this. Captured by the parent at click time:
   * reading `document.activeElement` in this effect returns the search input,
   * because `autoFocus` commits before effects run — so focus was being
   * "restored" to an unmounting node and landing on <body>. */
  opener: HTMLElement | null;
}) {
  const [q, setQ] = useState("");
  const [lane, setLane] = useState<Lane | undefined>();
  const panelRef = useRef<HTMLDivElement>(null);
  const headingRef = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
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
  }, [onClose, opener]);

  const shown = useMemo(() => {
    const ql = q.trim().toLowerCase();
    return gods.filter((g) => (!ql || g.name.toLowerCase().includes(ql)) && (!lane || godInLane(g.role, lane)));
  }, [gods, q, lane]);

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    const first = shown.find((g) => !taken.has(g.name));
    if (first) onPick(first.name);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" onClick={onClose}>
      <div
        ref={panelRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby="god-picker-title"
        className="flex max-h-[85vh] w-full max-w-2xl flex-col rounded-lg border border-line bg-bg1 p-4 shadow-raised"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="mb-3 flex items-center gap-2">
          <h2 id="god-picker-title" ref={headingRef} tabIndex={-1} className="font-display text-lead font-semibold text-ink focus:outline-none">
            Pick a god
          </h2>
          <button type="button" onClick={onClose} aria-label="Close"
            className="press ml-auto rounded-md bg-bg2 px-2 py-1 text-small text-faint hover:text-ink">✕</button>
        </div>

        <form onSubmit={submit} role="search"
          className="mb-2.5 flex items-center gap-2 rounded-md border border-line bg-bg2 px-3 py-2 focus-within:border-blue">
          <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true" className="text-muted">
            <circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" />
          </svg>
          <input
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="Search gods…"
            aria-label="Search gods"
            aria-controls="god-picker-results"
            autoComplete="off"
            className="w-full bg-transparent text-small text-ink placeholder:text-muted focus:outline-none"
          />
        </form>

        <div className="mb-2.5 flex flex-wrap items-center gap-1.5">
          <button type="button" aria-pressed={!lane} onClick={() => setLane(undefined)}
            className={`press rounded-full border px-2.5 py-1 text-label ${!lane ? "border-line-strong text-ink" : "border-line text-muted hover:border-line-strong"}`}>
            All lanes
          </button>
          {LANES.map((l) => (
            <button key={l} type="button" aria-pressed={lane === l} onClick={() => setLane(lane === l ? undefined : l)}
              className={`press rounded-full px-2.5 py-1 text-label ${
                lane === l ? "bg-gold font-semibold text-bg0" : `border border-line hover:border-line-strong ${laneTextClass(l)}`}`}>
              {l}
            </button>
          ))}
        </div>

        <p aria-live="polite" className="sr-only">{shown.length} god{shown.length === 1 ? "" : "s"} match</p>

        {shown.length === 0 ? (
          <div className="flex flex-col items-center gap-2 py-8 text-center">
            <p className="text-body text-muted">
              No {lane ? `${lane} ` : ""}god matches{q.trim() ? ` “${q.trim()}”` : " that filter"}.
            </p>
            {lane && (
              <button type="button" onClick={() => setLane(undefined)}
                className="press rounded-sm px-1 py-1 text-small text-blue hover:underline">
                Search all lanes
              </button>
            )}
          </div>
        ) : (
          <ul id="god-picker-results" className="grid flex-1 grid-cols-[repeat(auto-fill,minmax(90px,1fr))] gap-2 overflow-y-auto">
            {shown.map((g) => {
              const isTaken = taken.has(g.name);
              const lane2 = godLane(g.role);
              return (
                <li key={g.name}>
                  <button
                    type="button"
                    disabled={isTaken}
                    onClick={() => onPick(g.name)}
                    aria-label={isTaken ? `${g.name} — already in this draft` : g.name}
                    className={`press flex w-full flex-col items-center gap-1.5 rounded-md border p-2 ${
                      isTaken ? "cursor-not-allowed border-line bg-bg2/40 opacity-40" : "border-line bg-bg2 hover:border-line-strong"}`}
                  >
                    <Icon name={g.name} className="h-9 w-9 rounded-md" />
                    <span className="max-w-full truncate text-center font-display text-micro text-ink">{g.name}</span>
                    {lane2 && <span className={`text-label ${laneTextClass(lane2)}`}>{lane2}</span>}
                  </button>
                </li>
              );
            })}
          </ul>
        )}
      </div>
    </div>
  );
}

export type SlotKind = "you" | "ally" | "enemy";

/** A single ally/enemy slot.
 *
 * The portrait is the slot: the god's name lives in the button's accessible
 * name and its tooltip, not as a caption that costs the icon half its height.
 *
 * "You" is a badge on the slot rather than a caption above it — as a caption
 * it only existed on ally slots, which pushed the whole ally row a line below
 * the enemy row it's meant to be read against. */
export function Slot({ kind, position, name, size = "h-16 w-16", onOpen, onRemove }: {
  kind: SlotKind; position: number; name: string; size?: string; onOpen: () => void; onRemove?: () => void;
}) {
  const row = kind === "enemy" ? "enemy" : "ally";
  const rowPlural = row === "enemy" ? "enemies" : "allies";
  const ariaLabel = kind === "you"
    ? (name ? `Change you (${name})` : "Add you")
    : (name ? `Change ${row} ${position} (${name})` : `Add ${row} ${position}`);
  const isYou = kind === "you";

  return (
    <div className="relative">
      {!name ? (
        <button type="button" onClick={onOpen} aria-label={ariaLabel}
          className={`press flex ${size} flex-none items-center justify-center rounded-md text-title leading-none text-faint hover:border-line-strong hover:text-muted ${
            isYou ? "border-2 border-gold" : "border border-dashed border-line-strong"}`}>
          +
        </button>
      ) : (
        <>
          <button type="button" onClick={onOpen} aria-label={ariaLabel} title={name}
            className={`press flex ${size} flex-none items-center justify-center overflow-hidden rounded-md bg-bg2 p-0.5 ${
              isYou ? "border-2 border-gold shadow-glow" : "border border-line hover:border-line-strong"}`}>
            <Icon name={name} className="h-full w-full rounded-sm" />
          </button>
          {/* Sibling, never nested, so it can't also fire the picker. 24×24
              minimum per WCAG 2.5.8; it was 20×20. */}
          {onRemove && (
            <button type="button" onClick={(e) => { e.stopPropagation(); onRemove(); }}
              aria-label={`Remove ${name} from ${rowPlural}`}
              className="press absolute -right-2 -top-2 flex h-6 w-6 items-center justify-center rounded-full border border-line bg-bg1 text-micro leading-none text-faint hover:border-line-strong hover:text-ink">
              ✕
            </button>
          )}
        </>
      )}
      {isYou && (
        <span aria-hidden="true"
          className="pointer-events-none absolute bottom-0.5 left-1/2 -translate-x-1/2 rounded-sm bg-gold px-1 py-px text-micro font-bold uppercase leading-none tracking-[0.08em] text-bg0">
          You
        </span>
      )}
    </div>
  );
}
