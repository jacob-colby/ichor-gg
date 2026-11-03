/** The draft board the app opens on: your slot and theirs, in one piece.
 *
 * You are the big slot with the violet ring — violet is the model's colour
 * and this is the god the model is building for. The enemy team is five
 * outlined slots in one row (three in Joust), drawn in ink and named "Enemy"
 * in words, never a hue. Allies are optional and fold away behind one
 * button: they barely move a build, and a phone mid-draft has no room to
 * spare for them.
 *
 * Pure layout: every tap is handed back up, the draft lives in `useDraft`. */
import type { ReactNode } from "react";
import type { God } from "../../types";
import { godLane, laneTextClass } from "../../lib/roleAccent";
import { Art, PlusGlyph } from "../second/art";
import { ModeSwitch } from "../second/ModeSwitch";
import type { Mode } from "../second/verdict";

export interface BoardProps {
  mode: Mode;
  onMode: (m: Mode) => void;
  god?: God;
  /** "Tier B on 1,286 Conquest games", or the Joust/Arena refusal. */
  record?: string;
  ranked?: boolean;
  /** The aspect switch (and its one-line note), when your god has one. */
  aspect?: ReactNode;
  aspectNote?: ReactNode;
  allies: string[];
  enemies: string[];
  alliesOpen: boolean;
  onToggleAllies: () => void;
  onYou: () => void;
  onAlly: (i: number) => void;
  onEnemy: (i: number) => void;
  /** Items the enemy team moved in the six, for the status line. */
  changeCount: number;
  wide: boolean;
  /** Desktop header extras ("New match"). */
  actions?: ReactNode;
}

function Slot({ name, label, ally = false, onClick, showName }: {
  name: string; label: string; ally?: boolean; onClick: () => void; showName: boolean;
}) {
  return (
    <button type="button" onClick={onClick} aria-label={label}
      className="press flex w-full min-w-0 flex-col items-center gap-1">
      {name ? (
        <Art name={name} kind="head"
          className={`aspect-square w-full rounded-[10px] ${ally ? "ring-1 ring-quiet" : "ring-[1.5px] ring-ink"}`} />
      ) : (
        <span className="flex aspect-square w-full items-center justify-center rounded-[10px] border-[1.5px] border-dashed border-quiet text-muted">
          <PlusGlyph size={20} />
        </span>
      )}
      {showName && (
        <span className={`w-full truncate text-center text-cap ${name ? "text-ink" : "text-quiet"}`}>{name || "Empty"}</span>
      )}
    </button>
  );
}

function SlotRow({ side, names, onOpen, status, wide, offset = 0 }: {
  side: "Enemy" | "Allies"; names: string[]; onOpen: (i: number) => void; status: ReactNode; wide: boolean; offset?: number;
}) {
  const ally = side === "Allies";
  return (
    <div className={wide ? "w-fit" : "grid grid-cols-[60px_minmax(0,1fr)] items-center gap-3"}>
      <div className={wide ? "mb-2 flex items-baseline justify-between gap-3" : ""}>
        <p className={`font-cond font-extrabold uppercase leading-none ${ally ? "text-muted" : "text-ink"} ${wide ? "text-[22px]" : "text-[19px]"}`}>
          {side}
        </p>
        <p className="num mt-1 text-cap leading-tight text-muted" aria-live="polite">{status}</p>
      </div>
      <ol className="grid gap-2" style={{ gridTemplateColumns: `repeat(${names.length}, ${wide ? "84px" : "minmax(0, 1fr)"})` }}>
        {names.map((name, i) => (
          <li key={i} className="min-w-0">
            <Slot name={name} ally={ally} onClick={() => onOpen(i)} showName={wide}
              label={ally
                ? (name ? `Ally ${i + 1 + offset}: ${name}. Change` : `Add ally ${i + 1 + offset}`)
                : (name ? `Enemy ${i + 1}: ${name}. Change` : `Add enemy ${i + 1}`)} />
          </li>
        ))}
      </ol>
    </div>
  );
}

export function MatchBoard(p: BoardProps) {
  const { god, wide } = p;
  const known = p.enemies.filter(Boolean).length;
  const alliesKnown = p.allies.slice(1).filter(Boolean).length;
  const enemyStatus = known === 0
    ? (wide ? "Add them as they lock in" : "Tap a slot")
    : <>
        {known} of {p.enemies.length}
        {god && p.changeCount > 0 && (
          <span className={`${wide ? "ml-2" : "block"} text-accent`}>
            {p.changeCount} swap{p.changeCount === 1 ? "" : "s"}
          </span>
        )}
      </>;
  const lane = god ? godLane(god.role) : undefined;

  const you = (
    <div className="flex items-center gap-3">
      <button type="button" onClick={p.onYou} data-testid="you-slot"
        className="press group flex min-w-0 flex-1 items-center gap-3 text-left lg:gap-5">
        {god ? (
          <Art name={god.name} kind="head" eager
            className="h-16 w-16 rounded-[14px] ring-[3px] ring-accent ring-offset-2 ring-offset-surface lg:h-24 lg:w-24 lg:rounded-[18px]" />
        ) : (
          <span className="flex h-16 w-16 flex-none items-center justify-center rounded-[14px] border-2 border-dashed border-accent text-accent lg:h-24 lg:w-24 lg:rounded-[18px]">
            <PlusGlyph size={28} />
          </span>
        )}
        <span className="min-w-0">
          <span className="sr-only">{god ? "You are playing " : ""}</span>
          {god ? (
            <>
              <span className="block font-cond text-[36px] font-extrabold uppercase leading-[0.9] text-ink [overflow-wrap:anywhere] lg:text-[64px]">{god.name}</span>
              <span className="mt-1 block text-note text-muted lg:text-copy">
                <span className={laneTextClass(lane)}>{god.role}</span>
                <span className="text-quiet"> · </span>
                <span data-testid="god-record" className={p.ranked ? "text-ink" : ""}>{p.record}</span>
              </span>
              <span className="sr-only">. Change god</span>
            </>
          ) : (
            <>
              <span className="block font-cond text-[34px] font-extrabold uppercase leading-[0.92] text-ink [text-wrap:balance] lg:text-[56px]">
                Who are you playing?
              </span>
              <span className="mt-1 block text-note text-muted lg:text-copy">Tap to pick your god. The build fills in here.</span>
            </>
          )}
        </span>
      </button>
      {p.aspect}
    </div>
  );

  const alliesToggle = (
    <button type="button" onClick={p.onToggleAllies} aria-expanded={p.alliesOpen} data-testid="allies-toggle"
      className={`press flex h-[52px] flex-none items-center gap-1.5 rounded-[12px] border px-3 font-cond text-[17px] font-bold uppercase ${
        p.alliesOpen ? "border-quiet text-ink" : "border-line text-muted hover:border-quiet hover:text-ink"}`}>
      {!p.alliesOpen && <PlusGlyph size={16} />}
      {p.alliesOpen ? "Hide allies" : alliesKnown ? `Allies · ${alliesKnown}` : "Add allies"}
    </button>
  );

  const allyRow = p.alliesOpen && (
    <div data-testid="ally-row" className={wide ? "mt-5" : "mt-3"}>
      <SlotRow side="Allies" names={p.allies.slice(1)} onOpen={p.onAlly} offset={1} wide={wide}
        status={`${alliesKnown} of ${p.allies.length - 1}`} />
    </div>
  );

  const enemyRow = (
    <section aria-label="Enemy team" data-testid="enemy-strip" className={wide ? "justify-self-end" : ""}>
      <SlotRow side="Enemy" names={p.enemies} onOpen={p.onEnemy} status={enemyStatus} wide={wide} />
    </section>
  );

  if (wide) {
    return (
      <section aria-labelledby="match-h" data-testid="match-board">
        <div className="flex items-end justify-between gap-6">
          <h1 id="match-h" className="font-cond text-[40px] font-extrabold leading-none text-ink">Your match</h1>
          <div className="flex items-center gap-2">
            {p.actions}
            {alliesToggle}
            <ModeSwitch mode={p.mode} onChange={p.onMode} className="w-[360px]" />
          </div>
        </div>
        <div className="mt-4 grid grid-cols-[minmax(0,1fr)_auto_minmax(0,1fr)] items-start gap-8 rounded-[18px] border border-line bg-surface p-6">
          <div className="min-w-0">
            {you}
            {p.aspectNote}
            {allyRow}
          </div>
          <span aria-hidden="true" className="self-center font-cond text-[28px] font-extrabold uppercase text-quiet">vs</span>
          {enemyRow}
        </div>
      </section>
    );
  }

  return (
    <section aria-labelledby="match-h" data-testid="match-board" className="pt-2">
      <h1 id="match-h" className="sr-only">Your match</h1>
      <div className="flex gap-2">
        <ModeSwitch mode={p.mode} onChange={p.onMode} className="min-w-0 flex-1" />
        {alliesToggle}
      </div>
      <div className="mt-2 rounded-[16px] border border-line bg-surface p-3">
        {you}
        {p.aspectNote}
        {allyRow}
        <div className="mt-2.5 border-t border-line pt-2.5">{enemyRow}</div>
      </div>
    </section>
  );
}
