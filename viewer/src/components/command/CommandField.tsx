/** The command field — this direction's whole navigation.
 *
 * "ra vs hecate ymir" typed into one box: each finished word becomes a chip
 * (you in violet, enemies in ink outline, the mode and aspect as plain
 * chips), and the word being typed drives a suggestion list with portraits.
 * Tapping a suggestion is the same as typing it, so the field works without
 * a keyboard too. Enter takes the top suggestion for the unfinished word and
 * goes.
 *
 * At rest on a god page the chips ARE the enemy team: tap an enemy to change
 * it in the picker, tap "+" to add one. That is why the god page drops its
 * own phone strip under this chrome — one screen, one control.
 *
 * It is an ARIA combobox: the input owns a listbox of suggestions, arrows
 * move the active row, Escape closes and restores what the page shows. */
import { Fragment, useEffect, useId, useMemo, useRef, useState, type ReactNode } from "react";
import type { God } from "../../types";
import type { Mode } from "../second/verdict";
import { Art, CloseGlyph, PlusGlyph, SearchGlyph } from "../second/art";
import { parseQuery, suggest, removeSpan, type ParsedQuery, type QueryToken, type Suggestion } from "./query";
import { useKeyboardInset } from "./useKeyboardInset";

interface Option {
  id: string;
  kind: "go" | "suggestion" | "recent";
  suggestion?: Suggestion;
  recent?: string;
}

export interface CommandFieldProps {
  gods: God[];
  /** Canonical text of what the page shows ("Ra vs Hecate Ymir Conquest"), or "". */
  seedText: string;
  /** The mode a query without a mode word is read in (sizes the enemy cap). */
  seedMode?: Mode;
  onSubmit: (q: ParsedQuery) => void;
  /** Recent queries, newest first; shown when the field is empty. */
  recents?: string[];
  /** Enemy slots on the page (with "" for empty), for chip taps at rest. */
  enemySlots?: string[];
  onEnemy?: (index: number) => void;
  /** `dock` sits at the bottom of a phone and opens upward; `bar` sits in
   *  the desktop top bar and opens downward. */
  placement: "dock" | "bar";
  autoFocus?: boolean;
  /** Rendered beside the field, inside the dock (the Menu button). */
  trailing?: ReactNode;
}

const roleOf = (gods: God[], name: string) => gods.find((g) => g.name === name)?.role;

export function CommandField({
  gods, seedText, seedMode = "conquest", onSubmit, recents = [], enemySlots, onEnemy, placement, autoFocus, trailing,
}: CommandFieldProps) {
  const seeded = seedText ? `${seedText} ` : "";
  const [committed, setCommitted] = useState(seeded);
  const [tail, setTail] = useState("");
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  const input = useRef<HTMLInputElement>(null);
  const root = useRef<HTMLDivElement>(null);
  const chipRow = useRef<HTMLDivElement>(null);
  const listId = useId();
  const dock = placement === "dock";
  const inset = useKeyboardInset(dock && open);

  // The page moved (a submit landed, the mode switched, the picker changed an
  // enemy): show what it shows now.
  useEffect(() => { setCommitted(seeded); setTail(""); }, [seeded]);

  const parsed = useMemo(() => parseQuery(committed, gods, seedMode), [committed, gods, seedMode]);
  const full = useMemo(() => parseQuery(committed + tail, gods, seedMode), [committed, tail, gods, seedMode]);
  const suggestions = useMemo(() => suggest(tail, parsed, gods), [tail, parsed, gods]);

  const resolved = (): ParsedQuery => {
    if (!tail.trim()) return parsed;
    const pick = options[active]?.suggestion ?? suggestions[0];
    return parseQuery(`${committed}${pick ? pick.insert : tail} `, gods, seedMode);
  };

  const options: Option[] = useMemo(() => {
    const out: Option[] = [];
    const showGo = !tail.trim() && (parsed.you || parsed.enemies.length > 0);
    if (showGo) out.push({ id: "go", kind: "go" });
    suggestions.forEach((s, i) => out.push({ id: `s${i}`, kind: "suggestion", suggestion: s }));
    if (!committed.trim() && !tail.trim()) recents.forEach((r, i) => out.push({ id: `r${i}`, kind: "recent", recent: r }));
    return out;
  }, [tail, parsed, suggestions, committed, recents]);

  useEffect(() => { setActive(0); }, [tail, committed]);

  // Keep the word being typed in view as chips pile up.
  useEffect(() => {
    const row = chipRow.current;
    if (row && open) row.scrollLeft = row.scrollWidth;
  }, [committed, open]);

  // Close on a press outside.
  useEffect(() => {
    if (!open) return;
    const onDown = (e: PointerEvent) => {
      if (root.current && !root.current.contains(e.target as Node)) setOpen(false);
    };
    document.addEventListener("pointerdown", onDown);
    return () => document.removeEventListener("pointerdown", onDown);
  }, [open]);

  // Autofocus puts the caret in the field without dropping the list over the
  // page; the list opens on the first key or press.
  const quietFocus = useRef(false);
  useEffect(() => {
    if (!autoFocus) return;
    quietFocus.current = true;
    input.current?.focus({ preventScroll: true });
  }, [autoFocus]);

  const commitTyped = (value: string) => {
    const lastSep = Math.max(value.lastIndexOf(" "), value.lastIndexOf(","), value.lastIndexOf("\t"));
    if (lastSep < 0) { setTail(value); return; }
    const done = value.slice(0, lastSep + 1);
    // Space finishes a word as the top suggestion would — "hec " is Hecate.
    setCommitted((c) => `${c}${done.replace(/,/g, " ")}`.replace(/\s{2,}/g, " "));
    setTail(value.slice(lastSep + 1));
  };

  const take = (s: Suggestion) => {
    setCommitted((c) => `${c}${c && !/\s$/.test(c) ? " " : ""}${s.insert} `);
    setTail("");
    input.current?.focus();
  };

  const go = (q: ParsedQuery) => {
    if (!q.you && !q.enemies.length) return;
    setOpen(false);
    input.current?.blur();
    onSubmit(q);
  };

  const choose = (o: Option | undefined) => {
    if (!o) { go(resolved()); return; }
    if (o.kind === "go") go(parsed);
    else if (o.kind === "recent") go(parseQuery(o.recent!, gods));
    else if (o.suggestion) take(o.suggestion);
  };

  const removeToken = (t: QueryToken) => {
    setCommitted((c) => removeSpan(c, t.start, t.end));
    input.current?.focus();
  };

  const onKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      e.preventDefault();
      setOpen(true);
      if (!options.length) return;
      // In the dock the list grows upward, so Up moves AWAY from the field.
      const forward = (e.key === "ArrowDown") !== dock;
      setActive((a) => (a + (forward ? 1 : options.length - 1)) % options.length);
      return;
    }
    if (e.key === "Enter") {
      e.preventDefault();
      const o = options[active];
      if (o?.kind === "recent") { choose(o); return; }
      go(resolved());
      return;
    }
    if (e.key === "Tab" && tail.trim() && open) {
      const o = options[active]?.suggestion ?? suggestions[0];
      if (o) { e.preventDefault(); take(o); }
      return;
    }
    if (e.key === "Escape") {
      setOpen(false);
      setCommitted(seeded); setTail("");
      return;
    }
    if (e.key === "Backspace" && !tail && committed.trim()) {
      // Pull the last chip back into the input to be fixed, not deleted.
      const last = [...parsed.tokens].reverse().find((t) => t.kind !== "filler");
      if (!last) return;
      e.preventDefault();
      setCommitted(committed.slice(0, last.start));
      setTail(last.text);
    }
  };

  const chips = parsed.tokens.filter((t) => t.kind !== "filler");
  const atRest = !open && !!enemySlots && !!onEnemy;
  const nextEmpty = enemySlots ? enemySlots.findIndex((n) => !n) : -1;
  const notes = full.notes;
  const lastGod = chips.reduce((at, t, i) => (t.kind === "you" || t.kind === "enemy" || (t.kind === "vs" && at >= 0) ? i : at), -1);
  const addButton = atRest && nextEmpty >= 0 && parsed.you ? (
    <button type="button" onClick={() => onEnemy!(nextEmpty)} aria-label={`Add enemy ${nextEmpty + 1}`}
      className="press flex h-11 w-11 flex-none items-center justify-center rounded-[11px] border-[1.5px] border-dashed border-quiet text-muted hover:text-ink">
      <PlusGlyph size={18} />
    </button>
  ) : null;
  const activeId = open && options[active] ? `${listId}-${options[active].id}` : undefined;

  const chip = (t: QueryToken, i: number) => {
    const removable = open;
    const key = `${t.kind}-${t.start}-${i}`;
    const remove = removable ? (
      <button type="button" tabIndex={-1} aria-label={`Remove ${t.value ?? t.text}`}
        onPointerDown={(e) => e.preventDefault()} onClick={() => removeToken(t)}
        className="-mr-1 flex h-8 w-7 items-center justify-center text-quiet hover:text-ink">
        <CloseGlyph size={14} />
      </button>
    ) : null;
    if (t.kind === "you" || t.kind === "enemy") {
      const isYou = t.kind === "you";
      const slot = !isYou && enemySlots ? enemySlots.indexOf(t.value!) : -1;
      // At rest in the phone dock the page header already names every god,
      // so the chips shrink to faces and the whole team fits in 300px.
      const compact = dock && atRest;
      const body = (
        <>
          <Art name={t.value!} kind="head" className={`h-8 w-8 rounded-[7px] ${isYou ? "" : "ring-[1.5px] ring-ink"}`} />
          {!compact && <span className="font-cond text-[19px] font-bold leading-none text-ink">{t.value}</span>}
        </>
      );
      const cls = `flex h-11 flex-none items-center gap-1.5 rounded-[11px] ${compact ? "px-1.5" : "pl-1.5 pr-2.5"} ${
        isYou ? "bg-accent/15 ring-[1.5px] ring-accent" : "bg-surface-2"}`;
      if (atRest && !isYou && slot >= 0) {
        return (
          <button key={key} type="button" data-chip={t.kind} onClick={() => onEnemy!(slot)}
            aria-label={`Enemy ${slot + 1}: ${t.value}. Change`} className={`press ${cls}`}>{body}</button>
        );
      }
      return (
        <span key={key} data-chip={t.kind} className={cls}
          aria-label={`${isYou ? "You" : "Enemy"}: ${t.value}`} role="img">
          {body}{remove}
        </span>
      );
    }
    if (t.kind === "vs") {
      return <span key={key} data-chip="vs" className="flex h-11 flex-none items-center px-0.5 font-cond text-[17px] font-bold text-quiet">vs</span>;
    }
    if (t.kind === "mode" || t.kind === "aspect") {
      const label = t.kind === "mode" ? t.value!.replace(/^./, (c) => c.toUpperCase()) : t.value === "on" ? "Aspect" : "No aspect";
      return (
        <span key={key} data-chip={t.kind} className={`flex h-11 flex-none items-center gap-0.5 rounded-[11px] border border-line font-cond font-bold text-muted ${
          dock && atRest ? "px-2 text-[16px]" : "px-2.5 text-[17px]"}`}>
          {label}{remove}
        </span>
      );
    }
    // unknown / dropped: kept visible, struck, with the reason as its name.
    return (
      <span key={key} data-chip={t.kind} title={t.note} aria-label={`${t.text}: ${t.note ?? "ignored"}`} role="img"
        className="flex h-11 flex-none items-center gap-0.5 rounded-[11px] border border-dashed border-quiet px-2.5 text-copy text-quiet">
        <span className="line-through decoration-quiet">{t.text}</span>{remove}
      </span>
    );
  };

  const panel = open && (options.length > 0 || notes.length > 0 || (!committed.trim() && !tail)) ? (
    <div className={`absolute inset-x-0 z-10 overflow-hidden rounded-[16px] border border-line bg-surface shadow-[var(--shadow-raised)] ${
      dock ? "bottom-full mb-2" : "top-full mt-2"}`}>
      <ul id={listId} role="listbox" aria-label="Suggestions"
        className={`flex max-h-[min(52dvh,440px)] overflow-y-auto p-1.5 ${dock ? "flex-col-reverse" : "flex-col"}`}>
        {options.map((o, i) => (
          <li key={o.id} id={`${listId}-${o.id}`} role="option" aria-selected={i === active}
            onPointerDown={(e) => e.preventDefault()} onClick={() => choose(o)} onPointerMove={() => setActive(i)}
            className={`flex min-h-12 cursor-pointer items-center gap-3 rounded-[11px] px-2.5 py-1.5 ${i === active ? "bg-surface-2" : ""}`}>
            <OptionBody o={o} gods={gods} parsed={parsed} />
          </li>
        ))}
        {!options.length && !committed.trim() && !tail && (
          <li role="presentation" className="px-2.5 py-3 text-note text-muted">
            Type your god, then <span className="font-semibold text-ink">vs</span> and who you&rsquo;re facing.
          </li>
        )}
      </ul>
      {notes.length > 0 && (
        <p className="border-t border-line px-4 py-2 text-cap text-muted" data-testid="query-notes" aria-live="polite">
          {notes.join(" · ")}
        </p>
      )}
    </div>
  ) : null;

  return (
    <>
      {dock && open && <div aria-hidden="true" className="fixed inset-0 z-[-1] bg-black/60" onPointerDown={() => setOpen(false)} />}
      <div ref={root} className="relative flex items-center gap-2" data-testid="command"
        style={dock && inset ? { transform: `translateY(-${inset}px)` } : undefined}>
        {panel}
        <div onClick={(e) => {
          // Anywhere on the field that isn't its own button starts typing.
          if (!(e.target as HTMLElement).closest("button")) { input.current?.focus(); setOpen(true); }
        }}
          className={`flex min-w-0 flex-1 items-center gap-1 rounded-[14px] border bg-surface pl-3 pr-1.5 transition-colors duration-150 ${
            open ? "border-accent" : "border-line hover:border-quiet"} ${dock && atRest ? "pl-1.5" : ""} h-14`}>
          {!(dock && atRest) && <SearchGlyph size={20} className="flex-none text-quiet" onClick={() => input.current?.focus()} />}
          <div ref={chipRow} className="flex min-w-0 flex-1 items-center gap-1 overflow-x-auto [scrollbar-width:none]">
            {chips.map((t, i) => (
              <Fragment key={`${t.kind}-${t.start}-${i}`}>
                {chip(t, i)}
                {i === lastGod && addButton}
              </Fragment>
            ))}
            <input ref={input} value={tail} role="combobox" aria-expanded={open} aria-controls={listId}
              aria-autocomplete="list" aria-activedescendant={activeId}
              aria-label="Your god, vs the enemy team, and the mode"
              onChange={(e) => { setOpen(true); commitTyped(e.target.value); }}
              onFocus={() => { if (!quietFocus.current) setOpen(true); quietFocus.current = false; }}
              onClick={() => setOpen(true)} onKeyDown={onKeyDown}
              placeholder={chips.length ? "" : "ra vs hecate ymir"}
              autoComplete="off" autoCapitalize="none" autoCorrect="off" spellCheck={false} enterKeyHint="go"
              className={`h-11 ${dock && atRest ? "w-2 min-w-2" : "min-w-[72px]"} flex-1 bg-transparent font-medium text-ink placeholder:text-quiet focus:outline-none focus-visible:outline-none ${
                chips.length ? "text-[17px]" : "text-[19px]"}`} />
          </div>
          {(open && (committed.trim() || tail)) ? (
            <button type="button" onPointerDown={(e) => e.preventDefault()} onClick={() => choose(undefined)}
              disabled={!full.you && !full.enemies.length && !suggestions.length}
              className="press h-11 flex-none rounded-[10px] bg-accent px-3.5 font-cond text-[18px] font-bold uppercase text-accent-ink disabled:opacity-40">
              Go
            </button>
          ) : null}
        </div>
        {trailing}
      </div>
    </>
  );
}

function OptionBody({ o, gods, parsed }: { o: Option; gods: God[]; parsed: ParsedQuery }) {
  if (o.kind === "go") {
    return (
      <>
        <Art name={parsed.you ?? parsed.enemies[0]} kind="head" className="h-9 w-9 rounded-[8px]" />
        <span className="min-w-0 flex-1">
          <span className="block font-cond text-[19px] font-bold leading-tight text-ink">
            {parsed.you ? `Open ${parsed.you}'s build` : "Open the draft board"}
          </span>
          {parsed.enemies.length > 0 && (
            <span className="block truncate text-note text-muted">against {parsed.enemies.join(", ")}</span>
          )}
        </span>
        <kbd className="hidden rounded-[6px] border border-line px-1.5 py-0.5 text-cap font-semibold text-quiet sm:inline">Enter</kbd>
      </>
    );
  }
  if (o.kind === "recent") {
    const q = parseQuery(o.recent!, gods);
    return (
      <>
        <span className="flex flex-none -space-x-2">
          {[q.you, ...q.enemies].filter(Boolean).slice(0, 4).map((n, i) => (
            <Art key={n! + i} name={n!} kind="head" className={`h-9 w-9 rounded-[8px] ring-2 ring-surface ${i ? "" : "relative z-10"}`} />
          ))}
        </span>
        <span className="min-w-0 flex-1 truncate text-copy text-ink">{o.recent}</span>
        <span className="flex-none text-cap text-quiet">Recent</span>
      </>
    );
  }
  const s = o.suggestion!;
  if (s.kind === "god") {
    return (
      <>
        <Art name={s.label} kind="head" className={`h-9 w-9 rounded-[8px] ${s.side === "enemy" ? "ring-[1.5px] ring-ink" : ""}`} />
        <span className="min-w-0 flex-1">
          <span className="block font-cond text-[20px] font-bold leading-tight text-ink">{s.label}</span>
          <span className="block text-cap text-quiet">{roleOf(gods, s.label)}</span>
        </span>
        <span className={`flex-none font-cond text-[15px] font-bold ${s.side === "you" ? "text-accent" : "text-muted"}`}>
          {s.side === "you" ? "You" : "Enemy"}
        </span>
      </>
    );
  }
  return (
    <>
      <span aria-hidden="true" className="flex h-9 w-9 flex-none items-center justify-center rounded-[8px] border border-line font-cond text-[15px] font-bold text-muted">
        {s.kind === "vs" ? "vs" : s.kind === "mode" ? s.label.slice(0, 1) : "A"}
      </span>
      <span className="min-w-0 flex-1 font-cond text-[20px] font-bold leading-tight text-ink">{s.label}</span>
      <span className="flex-none text-cap text-quiet">
        {s.kind === "vs" ? "Start the enemy team" : s.kind === "mode" ? "Mode" : "Aspect"}
      </span>
    </>
  );
}
