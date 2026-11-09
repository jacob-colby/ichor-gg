/** The enemy picker: a bottom sheet with the keyboard already up.
 *
 * Mid-draft a player has seconds. The search field takes focus on open, three
 * letters narrow 94 gods to one or two, and Tab or Enter takes the top match
 * — the way the search bar completes a word — and the sheet moves itself to
 * the next EMPTY enemy slot (`nextEmptySlot`, the same rule the draft board
 * uses) so five enemies are five names, not fifteen taps. Re-opening a filled
 * slot is an edit: it doesn't advance. Escape closes.
 *
 * The typed name is ranked by `godMatches`, the search bar's own ranking, so
 * "ra" means the same god in both places. This sheet used to keep its own
 * starts-with-then-contains matcher, which put Hera under "ra" (the bar does
 * not) and ordered ties A–Z where the bar orders them shortest-first.
 *
 * Tab completes only while something is typed — the bar's `tail.trim()` rule —
 * and only when a god is left to take. Otherwise it is ordinary navigation,
 * which the Sheet's focus trap keeps inside the dialog. Shift+Tab is always
 * navigation. A god already on this team is skipped, as the bar skips an enemy
 * already typed: "ra" with Ra taken offers Rama.
 *
 * Each slot button IS its tile: square, the tile's radius, the violet ring at
 * the same 2px offset the focus outline uses. It was a full-width 48px-tall
 * row with a 44px tile inside, so its ring came out a wide rectangle around a
 * square portrait; and the row sat flush with the top of the Sheet's scrolling
 * body, which clips at its padding box, so the ring's top edge was cut off.
 * `pt-1` gives the ring and the focus outline the 4px they paint outside the
 * tile. */
import { useId, useMemo, useRef, useState } from "react";
import type { God } from "../../types";
import { nextEmptySlot } from "../../lib/draft";
import { godMatches } from "../command/query";
import { Art, CloseGlyph, SearchGlyph } from "./art";
import { Sheet } from "./Sheet";

export function EnemySheet({ gods, enemies, startIndex, self, onPick, onRemove, onClose, side = "enemy" }: {
  gods: God[];
  /** The team's slots ("" = empty). Named for the god page's use; the draft
   *  board passes your own team through `side="ally"` too. */
  enemies: string[];
  startIndex: number;
  /** Your god, shown but allowed: mirrors across teams are legal. */
  self?: string;
  onPick: (index: number, name: string) => void;
  onRemove: (index: number) => void;
  onClose: () => void;
  /** Which team the slots belong to. On `ally`, slot 1 is you. */
  side?: "enemy" | "ally";
}) {
  const [index, setIndex] = useState(startIndex);
  const [query, setQuery] = useState("");
  const input = useRef<HTMLInputElement>(null);
  const hintId = useId();

  const taken = useMemo(
    () => new Set(enemies.filter((n, i) => n && i !== index)), [enemies, index]);
  const matches = useMemo(() => {
    if (!query.trim()) return [...gods].sort((a, b) => a.name.localeCompare(b.name));
    return godMatches(query, gods);
  }, [gods, query]);

  const pick = (name: string) => {
    const wasEmpty = !enemies[index];
    onPick(index, name);
    const after = enemies.map((n, i) => (i === index ? name : n));
    const next = side === "ally"
      ? nextEmptySlot({ allies: after, enemies: [] }, "ally", index, wasEmpty)
      : nextEmptySlot({ allies: [], enemies: after }, "enemy", index, wasEmpty);
    if (!next) { onClose(); return; }
    setIndex(next.index);
    setQuery("");
    input.current?.focus();
  };

  const firstFree = matches.find((g) => !taken.has(g.name));
  // What Tab would take: only once something is typed.
  const completion = query.trim() ? firstFree : undefined;
  const slotWord = (i: number) => (side === "ally" ? (i === 0 ? "You" : `Ally ${i + 1}`) : `Enemy ${i + 1}`);
  const title = side === "ally" && index === 0 ? "Your god" : `${slotWord(index)} of ${enemies.length}`;

  const onKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" && firstFree) { e.preventDefault(); pick(firstFree.name); return; }
    if (e.key === "Tab" && !e.shiftKey && completion) { e.preventDefault(); pick(completion.name); }
  };

  return (
    <Sheet title={title} onClose={onClose} initialFocus={input} testId="enemy-sheet"
      footer={
        <div className="flex gap-2">
          {enemies[index] && (
            <button type="button" onClick={() => onRemove(index)}
              className="press h-11 flex-1 rounded-[10px] border border-line text-note font-semibold text-muted hover:text-ink">
              Remove {enemies[index]}
            </button>
          )}
          <button type="button" onClick={onClose}
            className="press h-11 flex-1 rounded-[10px] bg-ink font-cond text-[18px] font-bold uppercase text-ground">
            Done
          </button>
        </div>
      }>
      {/* Which slot you are filling, and a way to jump between them. */}
      <div role="group" aria-label={side === "ally" ? "Your team's slots" : "Enemy slots"} className="mb-3 grid gap-2 pt-1"
        style={{ gridTemplateColumns: `repeat(${enemies.length}, minmax(0, 1fr))` }}>
        {enemies.map((name, i) => (
          <button key={i} type="button" onClick={() => { setIndex(i); input.current?.focus(); }}
            aria-pressed={i === index} aria-label={side === "ally"
              ? `${slotWord(i)}: ${name || "empty"}`
              : name ? `Slot ${i + 1}: ${name}` : `Slot ${i + 1}: empty`}
            className={`press mx-auto block aspect-square w-full max-w-12 rounded-[10px] ${
              i === index ? "ring-2 ring-accent ring-offset-2 ring-offset-surface" : ""}`}>
            {name ? <Art name={name} kind="head" className={`h-full w-full rounded-[10px] ring-1 ${side === "ally" ? (i === 0 ? "ring-accent" : "ring-line-strong") : "ring-ink"}`} />
              : <span className="flex h-full w-full items-center justify-center rounded-[10px] border border-dashed border-quiet font-cond text-[17px] font-bold text-quiet">{i + 1}</span>}
          </button>
        ))}
      </div>

      <label className="flex h-12 items-center gap-2 rounded-[12px] border border-line bg-ground px-3 focus-within:border-accent">
        <SearchGlyph size={20} className="text-quiet" />
        <span className="sr-only">Search gods</span>
        <input ref={input} type="search" value={query} onChange={(e) => setQuery(e.target.value)}
          onKeyDown={onKeyDown} aria-describedby={hintId}
          placeholder="Type a god's name" autoComplete="off" enterKeyHint="go"
          className="min-w-0 flex-1 bg-transparent text-copy text-ink placeholder:text-quiet focus:outline-none focus-visible:outline-none" />
        {completion && (
          <kbd aria-hidden="true" title={`Tab or Enter adds ${completion.name}`}
            className="hidden flex-none rounded-[6px] border border-line px-1.5 py-0.5 text-cap font-semibold text-quiet sm:inline">Tab</kbd>
        )}
        {query && (
          <button type="button" onClick={() => { setQuery(""); input.current?.focus(); }} aria-label="Clear search"
            className="press -mr-1 flex h-10 w-10 items-center justify-center text-quiet hover:text-ink">
            <CloseGlyph size={18} />
          </button>
        )}
      </label>
      <span id={hintId} className="sr-only">{completion ? `Tab or Enter adds ${completion.name}.` : ""}</span>

      <ul className="mt-3 grid grid-cols-5 gap-x-2 gap-y-3 sm:grid-cols-6" aria-label="Gods">
        {matches.map((g) => {
          const isTaken = taken.has(g.name);
          const isNext = g === completion;
          return (
            <li key={g.name}>
              <button type="button" disabled={isTaken} onClick={() => pick(g.name)}
                aria-label={isTaken ? `${g.name} (already on ${side === "ally" ? "your" : "their"} team)` : g.name}
                data-completion={isNext || undefined}
                className="press flex w-full flex-col items-center gap-1 disabled:opacity-35">
                <Art name={g.name} kind="head" className="aspect-square w-full rounded-[10px]" />
                <span className={`w-full truncate text-center text-cap ${
                  isNext ? "font-semibold text-ink" : g.name === self ? "text-accent" : "text-muted"}`}>{g.name}</span>
              </button>
            </li>
          );
        })}
      </ul>
      {matches.length === 0 && <p className="py-6 text-center text-copy text-muted">No god called “{query}”.</p>}
    </Sheet>
  );
}
