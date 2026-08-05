/* THESIS: the draft is the one surface that changes a build, and until now it
 * only existed on one route out of five — leave /draft and the comp you built
 * vanished with no trace anywhere else in the shell. This makes it a
 * persistent, editable part of the chrome instead: a small dock, present on
 * every route but the draft page itself, carrying the same "N of M items
 * moved" claim /draft makes — computed once by `useDraftResult`, so the two
 * can never disagree — with enough of the real board reachable in place that
 * filling a slot doesn't require leaving whatever page you're reading.
 * OWN-WORLD: Arena Night. A floating plane on its own layer, not a fixed
 * strip claiming a permanent band of chrome. `.plane`'s top-edge highlight
 * marks it as raised, the same vocabulary as any other card. Gold marks only
 * the "you" slot, exactly as it does on /draft — nowhere here is it spent
 * on the dock's own chrome.
 */
import { useEffect, useRef, useState } from "react";
import type { BuildNote, DraftConfig, God, Item } from "../types";
import { toHash } from "../lib/useHashRoute";
import { useDraft, type DraftMode } from "../lib/draft";
import { useDraftResult } from "../lib/useDraftResult";
import { Icon, Slot, GodPickerModal } from "./DraftControls";

const MODE_LABEL: Record<DraftMode, string> = { conquest: "Conquest", joust: "Joust" };
const MODES: DraftMode[] = ["conquest", "joust"];
const label = "font-mono text-micro uppercase tracking-[0.08em] text-faint";

/** Small, non-interactive portraits for the collapsed header — the slots
 *  themselves only become individually clickable once the panel is open. */
function ChipRow({ names }: { names: string[] }) {
  return (
    <span className="flex shrink-0 items-center -space-x-1.5">
      {names.map((name, i) => (
        name ? (
          <Icon key={i} name={name}
            className={`h-5 w-5 ring-2 ring-bg1 ${i === 0 ? "ring-2 ring-gold" : ""}`} />
        ) : (
          <span key={i} aria-hidden="true"
            className="h-5 w-5 rounded-sm border border-dashed border-line-strong bg-bg2 ring-2 ring-bg1" />
        )
      ))}
    </span>
  );
}

/** One displacement, compact: the app's fuller `ChangeRow` (a bar, a bonus
 *  figure, the reason it fired) doesn't fit a panel this narrow — this keeps
 *  only what identifies the swap, and links to /draft for the rest. */
function MiniChange({ added, removed }: { added: string; removed?: string }) {
  return (
    <li className="flex items-center gap-2 py-1">
      <Icon name={added} item className="h-6 w-6 shrink-0" />
      <span className="min-w-0 flex-1 truncate text-small font-medium text-under">{added}</span>
      {removed && (
        <span className="shrink-0 truncate text-label text-faint">for {removed}</span>
      )}
    </li>
  );
}

interface DraftDockProps {
  gods: God[];
  items: Item[];
  builds: BuildNote[];
  godItemScores?: Record<string, Record<string, number>>;
  /** B6: per-item damage against a squishy vs a tank. Optional — an older
   *  index simply leaves the damage term out of the overlay. */
  godItemDamage?: Record<string, Record<string, [number, number]>>;
  draftConfig?: DraftConfig;
}

export function DraftDock({ gods, items, builds, godItemScores, godItemDamage, draftConfig }: DraftDockProps) {
  const { draft, mode, setMode, setAlly, setEnemy, clear } = useDraft();
  const { meName, taken, enemiesKnown, roster, result, changeCount, coreSize } =
    useDraftResult(draft, mode, gods, items, builds, godItemScores, draftConfig, godItemDamage);

  const [expanded, setExpanded] = useState(false);
  const [pickSlot, setPickSlot] = useState<{ kind: "ally" | "enemy"; index: number } | null>(null);
  const openerRef = useRef<HTMLElement | null>(null);
  const toggleRef = useRef<HTMLButtonElement>(null);
  const headingRef = useRef<HTMLHeadingElement>(null);

  const eligibleGods = gods.filter((g) => godItemScores?.[g.name]);
  const started = draft.allies.some(Boolean) || draft.enemies.some(Boolean);

  const openPicker = (kind: "ally" | "enemy", index: number) => {
    openerRef.current = document.activeElement as HTMLElement | null;
    setPickSlot({ kind, index });
  };
  const pick = (name: string) => {
    if (!pickSlot) return;
    if (pickSlot.kind === "enemy") setEnemy(pickSlot.index, name);
    else setAlly(pickSlot.index, name);
    setPickSlot(null);
  };

  // Escape collapses the panel — but only when the picker isn't the thing
  // actually open. The picker owns Escape while it's up (and returns focus
  // to whichever slot opened it); this listener would otherwise also fire on
  // the same keypress and collapse the dock out from under it.
  useEffect(() => {
    if (!expanded || pickSlot) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") { setExpanded(false); toggleRef.current?.focus(); }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [expanded, pickSlot]);

  useEffect(() => {
    if (expanded) headingRef.current?.focus();
  }, [expanded]);

  // One dock, in every state. There used to be a separate empty-state card
  // showing a *mock* of the board that linked to /draft — a picture of a
  // control beside the real control it was a picture of. The board is small
  // enough to just be here, so the invitation is the working thing rather
  // than an advertisement for it.
  const statusTitle = !started
    ? "Start a draft"
    : !meName
      ? "Add your god"
      : changeCount > 0
        ? `${changeCount} of ${coreSize} items moved`
        : enemiesKnown === 0 ? "Default core" : "Nothing moved yet";

  return (
    <div data-testid="draft-dock" className="fixed bottom-3 right-3 z-30 w-[min(94vw,420px)] sm:bottom-4 sm:right-4">
      <div role="region" aria-label="Your draft" className="plane overflow-hidden rounded-lg border border-line bg-bg1 shadow-raised">
        <button
          ref={toggleRef}
          type="button"
          onClick={() => setExpanded((v) => !v)}
          aria-expanded={expanded}
          aria-controls="draft-dock-panel"
          className="press flex w-full items-center gap-2.5 px-3 py-2.5 text-left"
        >
          <ChipRow names={draft.allies} />
          <span aria-hidden="true" className="shrink-0 text-label text-faint">vs</span>
          <ChipRow names={draft.enemies} />
          <span className={`min-w-0 flex-1 truncate text-small font-medium ${started ? "text-ink-soft" : "text-blue"}`}>
            {statusTitle}
          </span>
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2"
            aria-hidden="true" className={`shrink-0 text-faint transition-transform duration-150 ease-standard ${expanded ? "rotate-180" : ""}`}>
            <path d="M6 9l6 6 6-6" />
          </svg>
        </button>

        {expanded && (
          <div id="draft-dock-panel"
            className="max-h-[min(70vh,560px)] overflow-y-auto border-t border-line px-3 pb-3 pt-2.5">
            <div className="flex items-center justify-between gap-2">
              <h2 ref={headingRef} tabIndex={-1} className="font-display text-small font-semibold text-ink focus:outline-none">
                Your draft
              </h2>
              <div className="flex items-center gap-1.5">
                <div role="group" aria-label="Game mode" className="flex gap-0.5 rounded-md border border-line bg-bg2 p-0.5">
                  {MODES.map((m) => (
                    <button key={m} type="button" aria-pressed={mode === m} onClick={() => setMode(m)}
                      className={`press flex min-h-6 items-center rounded-sm px-2 text-micro font-semibold transition-colors duration-150 ease-standard ${
                        mode === m ? "bg-gold text-bg0" : "text-muted hover:text-ink"}`}>
                      {MODE_LABEL[m]}
                    </button>
                  ))}
                </div>
                <button type="button" onClick={() => setExpanded(false)} aria-label="Collapse"
                  className="press flex h-6 w-6 items-center justify-center rounded-sm text-small text-faint hover:text-ink">✕</button>
              </div>
            </div>

            <div className={label + " mt-2.5"}>Allies</div>
            <div className="mt-1 flex flex-wrap gap-1.5">
              {draft.allies.map((name, i) => (
                <Slot key={i} kind={i === 0 ? "you" : "ally"} position={i + 1} name={name} size="h-10 w-10"
                  onOpen={() => openPicker("ally", i)}
                  onRemove={name ? () => setAlly(i, "") : undefined} />
              ))}
            </div>
            <div className={label + " mt-2"}>Enemies</div>
            <div className="mt-1 flex flex-wrap gap-1.5">
              {draft.enemies.map((name, i) => (
                <Slot key={i} kind="enemy" position={i + 1} name={name} size="h-10 w-10"
                  onOpen={() => openPicker("enemy", i)}
                  onRemove={name ? () => setEnemy(i, "") : undefined} />
              ))}
            </div>

            <p className="mt-2.5 text-label text-faint">
              {meName
                ? <>{enemiesKnown} of {roster} enemies known</>
                : "Put your god in the gold slot to start adapting"}
            </p>

            {/* The build itself, not a teaser for it. Without this the dock
                could report that six items moved but never say which, so the
                claim it makes was unverifiable without leaving the page —
                which is the one thing this dock exists to avoid. */}
            {result && (
              <div className="mt-2 border-t border-line pt-2">
                <div className={label}>{changeCount > 0 ? "Your adapted core" : "The default core"}</div>
                <ul className="mt-1 flex flex-col">
                  {result.adapted.core.map((name, i) => {
                    const changed = result.diff.changes.some((c) => c.added === name);
                    return (
                      <li key={name}>
                        <a href={toHash.item(name)}
                          aria-label={`${name}${changed ? ", added by your draft" : ""}`}
                          className="press grid grid-cols-[14px_24px_minmax(0,1fr)_auto] items-center gap-2 rounded-sm py-0.5 pr-1 transition-colors duration-150 ease-standard hover:bg-bg2">
                          <span aria-hidden="true" className="text-right font-mono text-micro text-faint">{i + 1}</span>
                          <Icon name={name} item className="h-6 w-6" />
                          <span className={`truncate text-small ${changed ? "font-medium text-under" : "text-ink"}`}>{name}</span>
                          {changed && (
                            <span className="text-micro font-semibold uppercase tracking-[0.06em] text-under">new</span>
                          )}
                        </a>
                      </li>
                    );
                  })}
                </ul>
              </div>
            )}

            {result && changeCount > 0 && (
              <ul className="mt-2 flex flex-col divide-y divide-line border-t border-line pt-1">
                {result.diff.changes.slice(0, 3).map((c) => (
                  <MiniChange key={c.added} added={c.added} removed={c.removed} />
                ))}
              </ul>
            )}

            <div className="mt-2.5 flex items-center justify-between gap-2 border-t border-line pt-2">
              <a href={toHash.draft()} className="press flex min-h-6 items-center rounded-sm text-label font-medium text-blue hover:underline">
                Full board &amp; reasons →
              </a>
              {taken.size > 0 && (
                <button type="button" onClick={clear}
                  className="press flex min-h-6 items-center rounded-sm text-label text-faint hover:text-ink">
                  Clear board
                </button>
              )}
            </div>
          </div>
        )}
      </div>

      {pickSlot && (
        <GodPickerModal gods={eligibleGods} taken={taken} onPick={pick}
          onClose={() => setPickSlot(null)} opener={openerRef.current} />
      )}
    </div>
  );
}
