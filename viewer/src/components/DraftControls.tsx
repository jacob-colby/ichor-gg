/** Shared pieces of the draft board: the god picker, the ally/enemy slot, the
 *  portrait fallback. Two surfaces render a draft now — the full `/draft` page
 *  and the persistent `DraftDock` — and they render it identically rather
 *  than drifting into two slightly different boards. */
import { useEffect, useMemo, useRef, useState } from "react";
import { AspectToggle } from "./AspectBadge";
import type { God } from "../types";
import { iconSlug } from "../lib/builds";
import { godLane, laneTextClass, LANES, godInLane, type Lane } from "../lib/roleAccent";
import { usePins } from "../lib/pins";
import { BookmarkIcon } from "./BookmarkIcon";

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
export function GodPickerModal({ gods, taken, onPick, onClose, opener, slotLabel, restoreSlot }: {
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
  /** `data-slot` of the slot currently being filled. On close the picker
   *  returns focus HERE rather than to `opener`, because `opener` is usually
   *  gone: an empty slot renders a `+` button and a filled one renders a
   *  different button in a different branch, so the node that opened the
   *  dialog is unmounted by the very pick it took, and focusing a detached
   *  node drops the reader on <body>. Advancing made that the terminal state
   *  of the main flow — fill five slots, land nowhere — rather than an
   *  occasional one, which is how it was found.
   *
   *  Resolved by `data-slot` query rather than a ref because the node this
   *  needs does not exist yet when the picker opens. Unambiguous: the dock is
   *  suppressed on the draft page, so only one board is ever mounted. */
  restoreSlot?: string;
  /** Which slot is being filled, e.g. "enemy 3". The dialog stays mounted
   *  while a pick advances it to the next empty slot, so the heading is the
   *  only thing that can say it moved — and being the dialog's accessible
   *  name, it says so to a screen reader too. */
  slotLabel?: string;
}) {
  const [q, setQ] = useState("");
  const [lane, setLane] = useState<Lane | undefined>();
  const panelRef = useRef<HTMLDivElement>(null);
  const headingRef = useRef<HTMLHeadingElement>(null);
  // Read at unmount, so it has to be a ref: the teardown below closes over the
  // props from the render its effect last ran on, and the slot changes on
  // every advance without re-running it.
  const restoreRef = useRef(restoreSlot);
  restoreRef.current = restoreSlot;

  // Advancing to the next slot is a fresh question, so it gets a fresh search
  // box and the focus back on the heading — the same state a re-open would
  // give. The lane filter deliberately SURVIVES: filling five enemy slots is
  // one job, and re-picking "Support" for each of them would be the ten
  // clicks the advance exists to remove. Runs on mount too, which is where
  // the heading focus used to live.
  useEffect(() => {
    setQ("");
    headingRef.current?.focus();
  }, [slotLabel]);

  useEffect(() => {
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
    return () => {
      document.removeEventListener("keydown", onKeyDown, true);
      const id = restoreRef.current;
      const slot = id ? document.querySelector<HTMLElement>(`[data-slot="${id}"]`) : null;
      (slot ?? (opener?.isConnected ? opener : null))?.focus?.();
    };
  }, [onClose, opener]);

  const { isPinned } = usePins();
  const shown = useMemo(() => {
    const ql = q.trim().toLowerCase();
    const matches = gods.filter(
      (g) => (!ql || g.name.toLowerCase().includes(ql)) && (!lane || godInLane(g.role, lane)));
    // Bookmarked gods lead. Filling a draft slot is the one place a reader is
    // reaching for a specific god they play rather than browsing 87 of them,
    // and Enter still takes the first available match — which is now theirs.
    return [...matches].sort((a, b) => Number(isPinned(b.name)) - Number(isPinned(a.name)));
  }, [gods, q, lane, isPinned]);

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
            Pick a god{" "}
            {slotLabel && <span className="ml-1 text-small font-normal text-muted">{slotLabel}</span>}
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
              const saved = isPinned(g.name);
              const lane2 = godLane(g.role);
              return (
                <li key={g.name}>
                  <button
                    type="button"
                    disabled={isTaken}
                    onClick={() => onPick(g.name)}
                    aria-label={isTaken ? `${g.name} — already on this team` : saved ? `${g.name} — bookmarked` : g.name}
                    className={`press relative flex w-full flex-col items-center gap-1.5 rounded-md border p-2 ${
                      isTaken ? "cursor-not-allowed border-line bg-bg2/40 opacity-40"
                        : saved ? "border-gold/40 bg-bg2 hover:border-gold/70"
                        : "border-line bg-bg2 hover:border-line-strong"}`}
                  >
                    {/* Corner-marked rather than inline: the tile is 90px and
                        the name already truncates, so the mark takes space the
                        art can spare instead of space the name cannot. */}
                    {saved && (
                      <span className="absolute right-1 top-1 text-gold">
                        <BookmarkIcon filled size={10} />
                      </span>
                    )}
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
export function Slot({ kind, position, name, size = "h-16 w-16", onOpen, onRemove, slotId,
  aspectName, aspectOn, onToggleAspect, aspectChangesBuild }: {
  kind: SlotKind; position: number; name: string; size?: string; onOpen: () => void; onRemove?: () => void;
  /** Stable handle on this slot across the empty/filled branch swap, so the
   *  picker can hand focus back to it — see `restoreSlot`. */
  slotId?: string;
  /** Aspect controls, wired only on the "you" slot — the draft builds for
   *  your god, so nobody else's aspect changes anything it can show. */
  aspectName?: string; aspectOn?: boolean; onToggleAspect?: () => void;
  aspectChangesBuild?: boolean;
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
        <button type="button" onClick={onOpen} aria-label={ariaLabel} data-slot={slotId}
          className={`press flex ${size} flex-none items-center justify-center rounded-md text-title leading-none text-faint hover:border-line-strong hover:text-muted ${
            isYou ? "border-2 border-gold" : "border border-dashed border-line-strong"}`}>
          +
        </button>
      ) : (
        <>
          <button type="button" onClick={onOpen} aria-label={ariaLabel} title={name} data-slot={slotId}
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
      {/* The aspect hexagon, where SMITE puts it. Sibling of the picker
          button for the same reason the remove control is. */}
      {name && aspectName && onToggleAspect && (
        <AspectToggle
          aspectName={aspectName}
          on={!!aspectOn}
          onToggle={onToggleAspect}
          changesBuild={aspectChangesBuild}
        />
      )}
      {/* Centred ON the bottom edge, not tucked inside it: sitting 2px above
          the border the badge read as a label floating in the portrait, and it
          covered the art it was labelling. Straddling the edge makes it read
          as a tab attached to the slot, and gives the icon its full height
          back. `translate-y-1/2` against `bottom-0` puts the badge's own
          centre line exactly on the border whatever the badge's height. */}
      {isYou && (
        <span aria-hidden="true"
          className="pointer-events-none absolute bottom-0 left-1/2 -translate-x-1/2 translate-y-1/2 rounded-sm bg-gold px-1.5 py-px text-micro font-bold uppercase leading-none tracking-[0.08em] text-bg0">
          You
        </span>
      )}
    </div>
  );
}
