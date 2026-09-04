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
import { useDraft, nextEmptySlot, pickerSlotLabel, type DraftMode } from "../lib/draft";
import { useDraftResult } from "../lib/useDraftResult";
import { Icon, Slot, GodPickerModal } from "./DraftControls";

const MODE_LABEL: Record<DraftMode, string> = { conquest: "Conquest", joust: "Joust", arena: "Arena" };
const MODES: DraftMode[] = ["conquest", "joust", "arena"];
const label = "font-mono text-micro uppercase tracking-[0.08em] text-faint";

/** Small, non-interactive portraits for the collapsed header — the slots
 *  themselves only become individually clickable once the panel is open.
 *
 *  `you` is explicit and undefaulted. The gold ring means "this one is yours"
 *  and a board has exactly one; keyed on `i === 0` alone it was drawn on the
 *  enemy row's first slot too, which said the enemy team had a you-slot. The
 *  mark also survives an EMPTY you-slot, so the dock at rest still shows where
 *  your god goes — the same shape /draft and Home's panel use. */
function ChipRow({ names, you = false }: { names: string[]; you?: boolean }) {
  return (
    <span className="flex shrink-0 items-center -space-x-1.5">
      {names.map((name, i) => {
        const mine = you && i === 0;
        return name ? (
          <Icon key={i} name={name}
            className={`h-5 w-5 ring-2 ${mine ? "ring-gold" : "ring-bg3"}`} />
        ) : (
          <span key={i} aria-hidden="true"
            className={`h-5 w-5 rounded-sm border border-dashed bg-bg2 ring-2 ring-bg3 ${
              mine ? "border-gold" : "border-line-strong"}`} />
        );
      })}
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
  godItemScores?: Record<string, Record<string, Record<string, number>>>;
  /** B6: per-item damage against a squishy vs a tank. Optional — an older
   *  index simply leaves the damage term out of the overlay. */
  godItemDamage?: Record<string, Record<string, [number, number]>>;
  draftConfig?: DraftConfig;
}

export function DraftDock({ gods, items, builds, godItemScores, godItemDamage, draftConfig }: DraftDockProps) {
  const { draft, mode, setMode, setAlly, setEnemy, clear } = useDraft();
  const { meName, taken, takenFor, enemiesKnown, roster, result, changeCount, coreSize, starters,
    startersAreConquest } =
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
  /* Advances to the next empty slot on that side, exactly as the full page
     does — see `nextEmptySlot`. Two surfaces render one board; a board that
     advances on one and not the other is two boards. */
  const pick = (name: string) => {
    if (!pickSlot) return;
    const side = pickSlot.kind === "enemy" ? draft.enemies : draft.allies;
    const wasEmpty = !side[pickSlot.index];
    if (pickSlot.kind === "enemy") setEnemy(pickSlot.index, name);
    else setAlly(pickSlot.index, name);
    setPickSlot(nextEmptySlot(draft, pickSlot.kind, pickSlot.index, wasEmpty));
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
        // No "same items, new order" state any more: the board starts from the
        // pipeline's build and a swap takes the departed item's slot, so the
        // draft cannot resequence anything. See `adaptFromCore`.
        : enemiesKnown === 0 ? "God page's build" : "Nothing moved yet";

  return (
    <div data-testid="draft-dock" className="fixed bottom-3 right-3 z-30 w-[min(94vw,420px)] sm:bottom-4 sm:right-4">
      {/* `.dock`, not `.plane` + `shadow-raised`: those two both set
          `box-shadow` and the plane won, so this floated with no lift at all.
          See index.css — and the surface steps up to bg3, the system's
          elevated tier, because bg1 measured 1.02:1 against the page. */}
      <div role="region" aria-label="Your draft"
        className={`dock overflow-hidden rounded-lg border bg-bg3 ${
          started ? "is-live border-gold/40" : "border-line-strong"}`}>
        <button
          ref={toggleRef}
          type="button"
          onClick={() => setExpanded((v) => !v)}
          aria-expanded={expanded}
          aria-controls="draft-dock-panel"
          className="press flex w-full items-center gap-2.5 px-3 py-2.5 text-left"
        >
          <ChipRow names={draft.allies} you />
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
                  slotId={`ally-${i}`}
                  onOpen={() => openPicker("ally", i)}
                  onRemove={name ? () => setAlly(i, "") : undefined} />
              ))}
            </div>
            <div className={label + " mt-2"}>Enemies</div>
            <div className="mt-1 flex flex-wrap gap-1.5">
              {draft.enemies.map((name, i) => (
                <Slot key={i} kind="enemy" position={i + 1} name={name} size="h-10 w-10"
                  slotId={`enemy-${i}`}
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
            {/* A build starts before item one, and the dock began at item one —
                so the first purchase of the match was the one thing the shell's
                copy of the build never showed, while /draft has shown it all
                along. Same data, same source, same "the draft doesn't move
                these" caveat; only the chip is tighter, because 420px is not
                the draft page. */}
            {starters.length > 0 && (
              <div data-testid="dock-starters" className="mt-2 border-t border-line pt-2">
                <div className={label}>
                  Opens with{startersAreConquest && ` · ${MODE_LABEL.conquest} data`}
                </div>
                {/* One chip per purchase PATH — see lib/starters.ts. The dock
                    is 420px, so it shows the path's end and its lead rate and
                    leaves the base/upgrade split to the full page. */}
                <ul className="mt-1 flex flex-wrap gap-1">
                  {starters.map((p) => {
                    const end = p.upgrade ?? p.base!;
                    return (
                      <li key={p.rootName}>
                        <a href={toHash.item(end.name)}
                          aria-label={p.base && p.upgrade
                            ? `${p.base.name} into ${p.upgrade.name} — ${Math.round(p.lead.pick_rate * 100)}% of ${meName} players`
                            : `${end.name} — opened with by ${Math.round(end.pick_rate * 100)}% of ${meName} players, winning ${Math.round(end.win_rate * 100)}%`}
                          className="press flex items-center gap-1 rounded-md border border-line bg-bg2 py-0.5 pl-0.5 pr-1.5 transition-colors duration-150 ease-standard hover:border-line-strong">
                          <Icon name={end.name} item className="h-5 w-5" />
                          <span className="max-w-[10ch] truncate text-label text-ink">{end.name}</span>
                          <span aria-hidden="true" className="font-mono text-micro text-gold">
                            {Math.round(p.lead.pick_rate * 100)}%
                          </span>
                        </a>
                      </li>
                    );
                  })}
                </ul>
              </div>
            )}

            {result && (
              <div className="mt-2 border-t border-line pt-2">
                <div className={label}>
                  {changeCount > 0 ? "Your adapted core" : "The god page's build"}
                </div>
                {/* No community record backs this mode's score at all (§1 of
                    STATE.md) — efficiency + kit-fit only. Same fact DetailPanel
                    states on the god page; the dock repeats it here rather than
                    letting the build read as meta-backed just because the tab
                    looks the same as Conquest's. */}
                {mode !== "conquest" && (
                  <p className="mt-0.5 text-micro leading-snug text-faint">
                    No outcome data for {MODE_LABEL[mode]} — ranked by efficiency and kit-fit alone.
                  </p>
                )}
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
        <GodPickerModal gods={eligibleGods} taken={takenFor(pickSlot.kind, pickSlot.index)} onPick={pick}
          onClose={() => setPickSlot(null)} opener={openerRef.current}
          slotLabel={pickerSlotLabel(pickSlot.kind, pickSlot.index)}
          restoreSlot={`${pickSlot.kind}-${pickSlot.index}`} />
      )}
    </div>
  );
}
