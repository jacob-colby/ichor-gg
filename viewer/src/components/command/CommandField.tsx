/** The command field: "ra vs hecate ymir joust", typed into one box.
 *
 * Direction C's typed query, inside direction A's chrome. It lives in two
 * places and nowhere else:
 *  - the desktop top bar (`variant="bar"`), as the global search — a god, a
 *    god vs a team, or an item;
 *  - the phone's "Who are you playing?" screen (`variant="page"`), where it
 *    replaces the plain search box. There the grid below IS the list for the
 *    first word, so the field holds its suggestions back until a god is
 *    committed; a plain name filters the grid exactly as the old box did.
 * The god page on a phone never gets one: A's enemy strip is the enemy UI
 * there, and one screen gets one control.
 *
 * Each finished word becomes a chip (you ringed in violet, enemies ringed in
 * ink, mode and aspect as plain chips; anything not understood stays visible,
 * struck through, with the reason as its name). The word being typed drives a
 * suggestion list that overlays the page — it never pushes layout. Tapping a
 * suggestion is the same as typing it. Enter takes the top suggestion for the
 * unfinished word and goes.
 *
 * It is an ARIA combobox: the input owns a listbox, arrows move the active
 * row, Escape closes and restores what was there. `data-command-input` marks
 * the input so the global `/` and Ctrl/⌘K shortcut can find it. */
import { useEffect, useId, useLayoutEffect, useMemo, useRef, useState } from "react";
import type { God, Item } from "../../types";
import type { Mode } from "../second/verdict";
import { Art, CloseGlyph, SearchGlyph } from "../second/art";
import {
  itemMatches, parseQuery, suggest, removeSpan, type ParsedQuery, type QueryToken, type Suggestion,
} from "./query";
import { useKeyboardInset } from "./useKeyboardInset";

interface Option {
  id: string;
  kind: "go" | "suggestion" | "recent" | "item";
  suggestion?: Suggestion;
  recent?: string;
  item?: string;
}

export interface CommandFieldProps {
  gods: God[];
  /** Items the field can open; omit to make it gods-only. */
  items?: Pick<Item, "name" | "cost">[];
  /** What the field holds when it mounts (a linked `?q=`), or "". */
  seedText?: string;
  /** The mode a query without a mode word is read in (sizes the enemy cap). */
  seedMode?: Mode;
  onSubmit: (q: ParsedQuery) => void;
  onItem?: (name: string) => void;
  /** Every edit, as the whole text and its parse — the grid filters on it. */
  onText?: (text: string, parsed: ParsedQuery) => void;
  /** Recent queries, newest first; offered when the field is empty. */
  recents?: string[];
  variant: "bar" | "page";
  label: string;
  placeholder: string;
  autoFocus?: boolean;
  /** Empty the field after a submit (the top bar is a search, not a header). */
  clearOnSubmit?: boolean;
  /** `page` on a phone: the grid below lists the first word's matches, so
   *  the field only suggests once a god is committed. */
  gridBelow?: boolean;
}

const roleOf = (gods: God[], name: string) => gods.find((g) => g.name === name)?.role;

export function CommandField({
  gods, items, seedText = "", seedMode = "conquest", onSubmit, onItem, onText, recents = [], variant,
  label, placeholder, autoFocus, clearOnSubmit, gridBelow,
}: CommandFieldProps) {
  const [committed, setCommitted] = useState(seedText ? `${seedText} ` : "");
  const [tail, setTail] = useState("");
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  const input = useRef<HTMLInputElement>(null);
  const root = useRef<HTMLDivElement>(null);
  const chipRow = useRef<HTMLDivElement>(null);
  const listId = useId();
  const page = variant === "page";

  const parsed = useMemo(() => parseQuery(committed, gods, seedMode), [committed, gods, seedMode]);
  const full = useMemo(() => parseQuery(committed + tail, gods, seedMode), [committed, tail, gods, seedMode]);
  const suggestions = useMemo(() => suggest(tail, parsed, gods), [tail, parsed, gods]);
  const itemHits = useMemo(
    () => (items && onItem && !parsed.you && !parsed.enemies.length ? itemMatches(committed + tail, items, gods) : []),
    [items, onItem, parsed, committed, tail, gods],
  );

  // The grid filters on every edit; report the text the player sees.
  const reported = useRef<string | null>(null);
  useEffect(() => {
    const text = `${committed}${tail}`;
    if (reported.current === text) return;
    reported.current = text;
    onText?.(text, full);
  }, [committed, tail, full, onText]);

  // On the grid page, the first word's matches are the grid itself.
  const holdBack = !!gridBelow && !parsed.you && !parsed.enemies.length && !parsed.tokens.some((t) => t.kind === "vs");

  const options: Option[] = useMemo(() => {
    const out: Option[] = [];
    const typing = !!tail.trim();
    if (!typing && (parsed.you || parsed.enemies.length > 0)) out.push({ id: "go", kind: "go" });
    itemHits.forEach((it, i) => out.push({ id: `i${i}`, kind: "item", item: it.name }));
    if (!holdBack) suggestions.forEach((s, i) => out.push({ id: `s${i}`, kind: "suggestion", suggestion: s }));
    if (!committed.trim() && !typing && !gridBelow) recents.forEach((r, i) => out.push({ id: `r${i}`, kind: "recent", recent: r }));
    return out;
  }, [tail, parsed, itemHits, holdBack, suggestions, committed, recents, gridBelow]);

  useEffect(() => { setActive(0); }, [tail, committed]);

  // Keep the word being typed in view as chips pile up.
  useEffect(() => {
    const row = chipRow.current;
    if (row) row.scrollLeft = row.scrollWidth;
  }, [committed]);

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

  // Phone keyboard: the list must end above the keys, not under them. iOS does
  // not shrink the layout viewport for the keyboard, so measure what's left.
  const inset = useKeyboardInset(page && open);
  const [room, setRoom] = useState<number | null>(null);
  useLayoutEffect(() => {
    if (!page || !open || !root.current) { setRoom(null); return; }
    const measure = () => {
      if (!root.current) return;
      const vv = window.visualViewport;
      const visibleBottom = vv ? vv.height + vv.offsetTop : window.innerHeight - inset;
      const bottom = root.current.getBoundingClientRect().bottom;
      setRoom(Math.max(168, Math.round(visibleBottom - bottom - 12)));
    };
    measure();
    window.addEventListener("scroll", measure, { passive: true });
    return () => window.removeEventListener("scroll", measure);
  }, [page, open, inset]);
  // Lift the field to the top of the screen while typing, so the list has
  // the most room above the keyboard.
  useEffect(() => {
    if (!page || !open || !root.current) return;
    if (typeof root.current.scrollIntoView === "function" && window.matchMedia?.("(max-width: 1023px)").matches) {
      root.current.scrollIntoView({ block: "start", behavior: "smooth" });
    }
  }, [page, open]);

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

  const reset = () => { setCommitted(seedText ? `${seedText} ` : ""); setTail(""); };

  const finish = () => {
    setOpen(false);
    input.current?.blur();
    if (clearOnSubmit) { setCommitted(""); setTail(""); }
  };

  const go = (q: ParsedQuery) => {
    if (!q.you && !q.enemies.length) {
      // Nothing to build: an item, if the text names one.
      if (itemHits[0] && onItem) { finish(); onItem(itemHits[0].name); }
      return;
    }
    finish();
    onSubmit(q);
  };

  const resolved = (): ParsedQuery => {
    if (!tail.trim()) return parsed;
    const pick = options[active]?.suggestion ?? suggestions[0];
    return parseQuery(`${committed}${pick ? pick.insert : tail} `, gods, seedMode);
  };

  const choose = (o: Option | undefined) => {
    if (!o) { go(resolved()); return; }
    if (o.kind === "go") go(parsed);
    else if (o.kind === "recent") go(parseQuery(o.recent!, gods));
    else if (o.kind === "item") { finish(); onItem?.(o.item!); }
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
      setActive((a) => (a + (e.key === "ArrowDown" ? 1 : options.length - 1)) % options.length);
      return;
    }
    if (e.key === "Enter") {
      e.preventDefault();
      const o = open ? options[active] : undefined;
      if (o && o.kind !== "suggestion") { choose(o); return; }
      go(resolved());
      return;
    }
    if (e.key === "Tab" && tail.trim() && open) {
      const o = options[active]?.suggestion ?? suggestions[0];
      if (o) { e.preventDefault(); take(o); }
      return;
    }
    if (e.key === "Escape") {
      if (!open && !committed && !tail) { input.current?.blur(); return; }
      setOpen(false);
      reset();
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
  const notes = full.notes;
  const activeId = open && options[active] ? `${listId}-${options[active].id}` : undefined;
  const hasText = !!(committed.trim() || tail);
  const h = page ? "h-14" : "h-11";
  const chipH = page ? "h-11" : "h-9";

  const chip = (t: QueryToken, i: number) => {
    const key = `${t.kind}-${t.start}-${i}`;
    const remove = (
      <button type="button" tabIndex={-1} aria-label={`Remove ${t.value ?? t.text}`}
        onPointerDown={(e) => e.preventDefault()} onClick={() => removeToken(t)}
        className="-mr-1 flex h-8 w-7 items-center justify-center text-quiet hover:text-ink">
        <CloseGlyph size={14} />
      </button>
    );
    if (t.kind === "you" || t.kind === "enemy") {
      const isYou = t.kind === "you";
      return (
        <span key={key} data-chip={t.kind} aria-label={`${isYou ? "You" : "Enemy"}: ${t.value}`} role="img"
          className={`flex ${chipH} flex-none items-center gap-1.5 rounded-[10px] pl-1 pr-1.5 ${
            isYou ? "bg-accent/15 ring-[1.5px] ring-accent" : "bg-surface-2"}`}>
          <Art name={t.value!} kind="head" className={`${page ? "h-8 w-8" : "h-7 w-7"} rounded-[7px] ${isYou ? "" : "ring-[1.5px] ring-ink"}`} />
          <span className={`font-cond font-bold leading-none text-ink ${page ? "text-[19px]" : "text-[17px]"}`}>{t.value}</span>
          {remove}
        </span>
      );
    }
    if (t.kind === "vs") {
      return <span key={key} data-chip="vs" className={`flex ${chipH} flex-none items-center px-0.5 font-cond text-[17px] font-bold text-quiet`}>vs</span>;
    }
    if (t.kind === "mode" || t.kind === "aspect") {
      const text = t.kind === "mode" ? t.value!.replace(/^./, (c) => c.toUpperCase()) : t.value === "on" ? "Aspect" : "No aspect";
      return (
        <span key={key} data-chip={t.kind}
          className={`flex ${chipH} flex-none items-center gap-0.5 rounded-[10px] border border-line px-2 font-cond text-[17px] font-bold text-muted`}>
          {text}{remove}
        </span>
      );
    }
    // unknown / dropped: kept visible, struck, with the reason as its name.
    return (
      <span key={key} data-chip={t.kind} title={t.note} aria-label={`${t.text}: ${t.note ?? "ignored"}`} role="img"
        className={`flex ${chipH} flex-none items-center gap-0.5 rounded-[10px] border border-dashed border-quiet px-2 text-copy text-quiet`}>
        <span className="line-through decoration-quiet">{t.text}</span>{remove}
      </span>
    );
  };

  const showHint = !options.length && !hasText && !page;
  const panel = open && (options.length > 0 || notes.length > 0 || showHint) ? (
    <div className="absolute inset-x-0 top-full z-50 mt-2 overflow-hidden rounded-[16px] border border-line bg-surface shadow-[var(--shadow-raised)]"
      data-testid="command-panel">
      <ul id={listId} role="listbox" aria-label="Suggestions"
        style={room ? { maxHeight: Math.min(room, 460) } : undefined}
        className="flex max-h-[min(60dvh,460px)] flex-col overflow-y-auto overscroll-contain p-1.5">
        {options.map((o, i) => (
          <li key={o.id} id={`${listId}-${o.id}`} role="option" aria-selected={i === active}
            onPointerDown={(e) => e.preventDefault()} onClick={() => choose(o)} onPointerMove={() => setActive(i)}
            className={`flex min-h-12 cursor-pointer items-center gap-3 rounded-[11px] px-2.5 py-1.5 ${i === active ? "bg-surface-2" : ""}`}>
            <OptionBody o={o} gods={gods} items={items} parsed={parsed} />
          </li>
        ))}
        {showHint && (
          <li role="presentation" className="px-2.5 py-3 text-note text-muted">
            A god opens its build. Add <span className="font-semibold text-ink">vs</span> and the enemy team to adapt it,
            and <span className="font-semibold text-ink">joust</span> or <span className="font-semibold text-ink">arena</span> for
            another mode. An item name opens the item.
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
    // In the top bar the field widens over the reading links while it is
    // open, so a whole matchup's chips fit; it never moves the bar's layout.
    <div ref={root} data-testid={page ? "command-page" : "command-bar"} data-command-open={open || undefined}
      className={`relative scroll-mt-3 ${page ? "" : `z-10 transition-[width] duration-150 ease-[var(--ease-standard)] ${
        open ? "w-[640px] max-w-[calc(100vw-420px)]" : "w-full"}`}`}>
      <div onClick={(e) => {
        // Anywhere on the field that isn't its own button starts typing.
        if (!(e.target as HTMLElement).closest("button")) { input.current?.focus(); setOpen(true); }
      }}
        className={`flex ${h} min-w-0 items-center gap-1 rounded-[12px] border bg-surface pl-3 pr-1.5 transition-colors duration-150 ${
          open ? "border-accent" : "border-line hover:border-quiet"}`}>
        <SearchGlyph size={page ? 20 : 18} className="flex-none text-quiet" />
        <div ref={chipRow} className="flex min-w-0 flex-1 items-center gap-1 overflow-x-auto px-[2px] py-[3px] [scrollbar-width:none]">
          {chips.map(chip)}
          <input ref={input} value={tail} role="combobox" aria-expanded={open && !!panel} aria-controls={listId}
            aria-autocomplete="list" aria-activedescendant={activeId} aria-label={label}
            data-command-input=""
            onChange={(e) => { setOpen(true); commitTyped(e.target.value); }}
            onFocus={() => { if (!quietFocus.current) setOpen(true); quietFocus.current = false; }}
            onClick={() => setOpen(true)} onKeyDown={onKeyDown}
            placeholder={chips.length ? "" : placeholder}
            autoComplete="off" autoCapitalize="none" autoCorrect="off" spellCheck={false} enterKeyHint="go"
            className={`${chipH} min-w-[64px] flex-1 bg-transparent font-medium text-ink placeholder:text-quiet focus:outline-none focus-visible:outline-none ${
              page ? "text-[17px]" : "text-copy"}`} />
        </div>
        {hasText ? (
          <>
            <button type="button" aria-label="Clear" onPointerDown={(e) => e.preventDefault()}
              onClick={() => { setCommitted(""); setTail(""); input.current?.focus(); }}
              className="press flex h-9 w-9 flex-none items-center justify-center rounded-[8px] text-quiet hover:text-ink">
              <CloseGlyph size={16} />
            </button>
            {(full.you || full.enemies.length > 0 || itemHits.length > 0 || (!holdBack && suggestions.length > 0)) && (
              <button type="button" onPointerDown={(e) => e.preventDefault()} onClick={() => choose(undefined)}
                className={`press ${page ? "h-11 px-3.5 text-[18px]" : "h-8 px-3 text-[16px]"} flex-none rounded-[9px] bg-accent font-cond font-bold uppercase text-accent-ink`}>
                Go
              </button>
            )}
          </>
        ) : !page ? (
          <kbd aria-hidden="true" title="Press / or Ctrl K to search"
            className="mr-1 flex-none rounded-[6px] border border-line px-1.5 py-0.5 text-cap font-semibold text-quiet">/</kbd>
        ) : null}
      </div>
      {panel}
    </div>
  );
}

function OptionBody({ o, gods, items, parsed }: {
  o: Option; gods: God[]; items?: Pick<Item, "name" | "cost">[]; parsed: ParsedQuery;
}) {
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
  if (o.kind === "item") {
    const it = items?.find((x) => x.name === o.item);
    return (
      <>
        <Art name={o.item!} kind="item" className="h-9 w-9 rounded-[8px]" />
        <span className="min-w-0 flex-1">
          <span className="block font-cond text-[20px] font-bold leading-tight text-ink">{o.item}</span>
          {it?.cost ? <span className="block text-cap text-quiet">{it.cost.toLocaleString("en-US")} gold</span> : null}
        </span>
        <span className="flex-none font-cond text-[15px] font-bold text-muted">Item</span>
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
