/** "Who are you playing?" as a sheet over the match board.
 *
 * Opened from the you-slot, so picking a god never leaves the board: the
 * sheet closes and the six fills in under the slots. The search field takes
 * focus with the keyboard up (Enter takes the first match); the card-art grid
 * and role filter are the god list's own, so the god you recognise by face
 * is a tap away without typing. */
import { useMemo, useRef, useState } from "react";
import type { God } from "../../types";
import type { Lane } from "../../lib/roleAccent";
import { Sheet } from "../second/Sheet";
import { GodCards, RoleFilter } from "../second/GodGrid";
import { filterGods } from "../second/filterGods";
import { CloseGlyph, SearchGlyph } from "../second/art";

export function YouSheet({ gods, current, onPick, onClose }: {
  gods: God[]; current?: string; onPick: (name: string) => void; onClose: () => void;
}) {
  const [q, setQ] = useState("");
  const [role, setRole] = useState<Lane | "">("");
  const input = useRef<HTMLInputElement>(null);
  const shown = useMemo(() => filterGods(gods, q, role), [gods, q, role]);

  return (
    <Sheet title="Who are you playing?" onClose={onClose} initialFocus={input} testId="you-sheet" wide>
      <div className="sticky top-0 z-10 -mx-4 space-y-2 bg-surface px-4 pb-3 lg:-mx-5 lg:px-5">
        <label className="flex h-12 items-center gap-2 rounded-[12px] border border-line bg-ground px-3 focus-within:border-accent">
          <SearchGlyph size={20} className="text-quiet" />
          <span className="sr-only">Search gods</span>
          <input ref={input} type="search" value={q} onChange={(e) => setQ(e.target.value)}
            onKeyDown={(e) => { if (e.key === "Enter" && shown[0]) { e.preventDefault(); onPick(shown[0].name); } }}
            placeholder={`Search ${gods.length} gods`} autoComplete="off" enterKeyHint="go"
            className="min-w-0 flex-1 bg-transparent text-copy text-ink placeholder:text-quiet focus:outline-none focus-visible:outline-none" />
          {q && (
            <button type="button" aria-label="Clear search" onClick={() => { setQ(""); input.current?.focus(); }}
              className="press -mr-1 flex h-10 w-10 items-center justify-center text-quiet hover:text-ink">
              <CloseGlyph size={18} />
            </button>
          )}
        </label>
        <RoleFilter role={role} onChange={setRole} />
      </div>
      <p className="sr-only" aria-live="polite">{shown.length} gods shown</p>
      <GodCards gods={shown} onPick={onPick} current={current} cols="grid-cols-3 sm:grid-cols-4" />
      {shown.length === 0 && (
        <p className="py-8 text-center text-copy text-muted">No god matches “{q}”{role ? ` in ${role}` : ""}.</p>
      )}
    </Sheet>
  );
}
