/* One search field for the whole app.
 *
 * There used to be four "Search gods…" inputs — Home's combobox, the picker's
 * filter, the draft board's and the tier list's — with four different
 * behaviours: one was keyboard-navigable, the rest weren't. This is the single
 * field in the shell, and it addresses both nouns the product has, because
 * "Rage" is as likely a thing to be looking for as "Ra".
 *
 * A combobox, not a text field with a list under it: the results overlay the
 * page rather than displacing it, and the keyboard reaches every one.
 */
import { useEffect, useMemo, useRef, useState } from "react";
import type { God, Item } from "../types";
import { toHash, navigate } from "../lib/useHashRoute";
import { iconSlug } from "../lib/builds";
import { searchSubjects, type Hit } from "../lib/subjectSearch";

function Art({ hit }: { hit: Hit }) {
  const [failed, setFailed] = useState(false);
  const cls = "h-6 w-6 shrink-0 rounded-sm object-cover";
  if (failed) {
    return (
      <span aria-hidden="true" className={`${cls} flex items-center justify-center bg-bg3 font-display text-micro font-bold text-faint`}>
        {hit.name.slice(0, 1)}
      </span>
    );
  }
  return (
    <img src={`/icons/${iconSlug(hit.name)}${hit.kind === "god" ? "-head" : ""}.png`}
      alt="" loading="lazy" onError={() => setFailed(true)} className={cls} />
  );
}

export function SubjectSearch({ gods, items }: { gods: God[]; items: Item[] }) {
  const [q, setQ] = useState("");
  const [active, setActive] = useState(0);
  const [open, setOpen] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const results = useMemo(() => searchSubjects(gods, items, q), [gods, items, q]);
  const expanded = open && q.trim().length > 0;

  // A shrinking result list must never leave the cursor past its end.
  useEffect(() => { setActive(0); }, [q]);

  // ⌘K / Ctrl-K focuses the field. Deliberately not a separate palette: one
  // field that the mouse and the keyboard both reach beats two things to learn.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        inputRef.current?.focus();
        inputRef.current?.select();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  const go = (hit: Hit) => {
    setQ("");
    setOpen(false);
    inputRef.current?.blur();
    navigate(hit.kind === "god" ? toHash.god(hit.name) : toHash.item(hit.name));
  };

  // Home/End aren't bound: in an editable combobox those belong to the caret,
  // and stealing them makes the field feel broken.
  const onKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Escape") { setQ(""); setOpen(false); return; }
    if (!expanded || results.length === 0) return;
    if (e.key === "ArrowDown") { e.preventDefault(); setActive((i) => (i + 1) % results.length); }
    else if (e.key === "ArrowUp") { e.preventDefault(); setActive((i) => (i - 1 + results.length) % results.length); }
  };

  const onBlur = (e: React.FocusEvent<HTMLDivElement>) => {
    if (!e.currentTarget.contains(e.relatedTarget as Node | null)) setOpen(false);
  };

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    if (results[active]) go(results[active]);
  };

  return (
    <div data-testid="subject-search" onBlur={onBlur} className="relative w-full max-w-md">
      <form onSubmit={submit} role="search"
        className="flex items-center gap-2 rounded-md border border-line bg-bg2 px-2.5 py-1 transition-colors sm:py-1.5 duration-[180ms] ease-standard focus-within:border-blue">
        <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true" className="shrink-0 text-muted">
          <circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" />
        </svg>
        <input
          ref={inputRef}
          value={q}
          onChange={(e) => { setQ(e.target.value); setOpen(true); }}
          onFocus={() => setOpen(true)}
          onKeyDown={onKeyDown}
          placeholder="Search gods and items…"
          aria-label="Search gods and items"
          role="combobox"
          aria-expanded={expanded}
          aria-controls="subject-search-results"
          aria-autocomplete="list"
          aria-activedescendant={expanded && results[active] ? `subject-search-opt-${active}` : undefined}
          autoComplete="off"
          className="w-full bg-transparent py-1 text-small text-ink placeholder:text-muted focus:outline-none"
        />
        {q ? (
          <button type="button" onClick={() => { setQ(""); inputRef.current?.focus(); }}
            aria-label="Clear search"
            className="press shrink-0 rounded-sm px-1 text-small text-faint hover:text-ink">✕</button>
        ) : (
          <span aria-hidden="true" className="hidden shrink-0 rounded-sm border border-line px-1 font-mono text-micro text-faint sm:inline">
            ⌘K
          </span>
        )}
      </form>

      <p aria-live="polite" className="sr-only">
        {expanded ? `${results.length} result${results.length === 1 ? "" : "s"}` : ""}
      </p>

      {expanded && (
        <ul id="subject-search-results" role="listbox" aria-label="Search results"
          className="absolute z-40 mt-1.5 flex w-full flex-col gap-0.5 rounded-md border border-line-strong bg-bg2 p-1.5 shadow-card">
          {results.length === 0 ? (
            <li className="px-2.5 py-2 text-small text-muted">
              Nothing called “{q.trim()}” — no god and no item. Check the spelling.
            </li>
          ) : results.map((hit, i) => (
            <li key={`${hit.kind}-${hit.name}`} role="presentation">
              <button type="button" id={`subject-search-opt-${i}`} role="option"
                aria-selected={i === active}
                onClick={() => go(hit)} onMouseEnter={() => setActive(i)} tabIndex={-1}
                className={`press flex w-full items-center gap-2.5 rounded-sm px-2 py-1.5 text-left transition-colors duration-[150ms] ease-standard ${
                  i === active ? "bg-bg3" : ""}`}>
                <Art hit={hit} />
                <span className="truncate font-display text-small font-semibold text-ink">{hit.name}</span>
                {hit.note && (
                  <span className={`ml-auto shrink-0 text-label ${
                    hit.kind === "item" ? "font-mono text-faint" : hit.noteClass}`}>
                    {hit.note}
                  </span>
                )}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
