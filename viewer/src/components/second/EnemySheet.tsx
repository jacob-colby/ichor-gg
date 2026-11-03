/** The enemy picker: a bottom sheet with the keyboard already up.
 *
 * Mid-draft a player has seconds. The search field takes focus on open, three
 * letters narrow 94 gods to one or two, Enter takes the first match, and the
 * sheet moves itself to the next EMPTY enemy slot (`nextEmptySlot`, the same
 * rule the draft board uses) so five enemies are five names, not fifteen taps.
 * Re-opening a filled slot is an edit: it doesn't advance. */
import { useMemo, useRef, useState } from "react";
import type { God } from "../../types";
import { nextEmptySlot } from "../../lib/draft";
import { Art, CloseGlyph, SearchGlyph } from "./art";
import { Sheet } from "./Sheet";

export function EnemySheet({ gods, enemies, startIndex, self, onPick, onRemove, onClose }: {
  gods: God[];
  enemies: string[];
  startIndex: number;
  /** Your god, shown but allowed: mirrors across teams are legal. */
  self?: string;
  onPick: (index: number, name: string) => void;
  onRemove: (index: number) => void;
  onClose: () => void;
}) {
  const [index, setIndex] = useState(startIndex);
  const [query, setQuery] = useState("");
  const input = useRef<HTMLInputElement>(null);

  const taken = useMemo(
    () => new Set(enemies.filter((n, i) => n && i !== index)), [enemies, index]);
  const matches = useMemo(() => {
    const q = query.trim().toLowerCase();
    const sorted = [...gods].sort((a, b) => a.name.localeCompare(b.name));
    if (!q) return sorted;
    // Starts-with first: "ra" should put Ra before Hera.
    const starts = sorted.filter((g) => g.name.toLowerCase().startsWith(q));
    const rest = sorted.filter((g) => !g.name.toLowerCase().startsWith(q) && g.name.toLowerCase().includes(q));
    return [...starts, ...rest];
  }, [gods, query]);

  const pick = (name: string) => {
    const wasEmpty = !enemies[index];
    onPick(index, name);
    const after = enemies.map((n, i) => (i === index ? name : n));
    const next = nextEmptySlot({ allies: [], enemies: after }, "enemy", index, wasEmpty);
    if (!next) { onClose(); return; }
    setIndex(next.index);
    setQuery("");
    input.current?.focus();
  };

  const firstFree = matches.find((g) => !taken.has(g.name));

  return (
    <Sheet title={`Enemy ${index + 1} of ${enemies.length}`} onClose={onClose} initialFocus={input} testId="enemy-sheet"
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
      <div role="group" aria-label="Enemy slots" className="mb-3 grid gap-2"
        style={{ gridTemplateColumns: `repeat(${enemies.length}, minmax(0, 1fr))` }}>
        {enemies.map((name, i) => (
          <button key={i} type="button" onClick={() => { setIndex(i); input.current?.focus(); }}
            aria-pressed={i === index} aria-label={name ? `Slot ${i + 1}: ${name}` : `Slot ${i + 1}: empty`}
            className={`press flex h-12 items-center justify-center rounded-[10px] ${
              i === index ? "ring-2 ring-accent" : ""}`}>
            {name ? <Art name={name} kind="head" className="h-11 w-11 rounded-[8px] ring-1 ring-ink" />
              : <span className="flex h-11 w-11 items-center justify-center rounded-[8px] border border-dashed border-quiet font-cond text-[17px] font-bold text-quiet">{i + 1}</span>}
          </button>
        ))}
      </div>

      <label className="flex h-12 items-center gap-2 rounded-[12px] border border-line bg-ground px-3 focus-within:border-accent">
        <SearchGlyph size={20} className="text-quiet" />
        <span className="sr-only">Search gods</span>
        <input ref={input} type="search" value={query} onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => { if (e.key === "Enter" && firstFree) { e.preventDefault(); pick(firstFree.name); } }}
          placeholder="Type a god's name" autoComplete="off" enterKeyHint="go"
          className="min-w-0 flex-1 bg-transparent text-copy text-ink placeholder:text-quiet focus:outline-none focus-visible:outline-none" />
        {query && (
          <button type="button" onClick={() => { setQuery(""); input.current?.focus(); }} aria-label="Clear search"
            className="press -mr-1 flex h-10 w-10 items-center justify-center text-quiet hover:text-ink">
            <CloseGlyph size={18} />
          </button>
        )}
      </label>

      <ul className="mt-3 grid grid-cols-5 gap-x-2 gap-y-3 sm:grid-cols-6" aria-label="Gods">
        {matches.map((g) => {
          const isTaken = taken.has(g.name);
          return (
            <li key={g.name}>
              <button type="button" disabled={isTaken} onClick={() => pick(g.name)}
                aria-label={isTaken ? `${g.name} (already on their team)` : g.name}
                className="press flex w-full flex-col items-center gap-1 disabled:opacity-35">
                <Art name={g.name} kind="head" className="aspect-square w-full rounded-[10px]" />
                <span className={`w-full truncate text-center text-cap ${g.name === self ? "text-accent" : "text-muted"}`}>{g.name}</span>
              </button>
            </li>
          );
        })}
      </ul>
      {matches.length === 0 && <p className="py-6 text-center text-copy text-muted">No god called “{query}”.</p>}
    </Sheet>
  );
}
