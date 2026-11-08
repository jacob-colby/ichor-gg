/** The build's adjusters, as one strip: the aspect switch, then the focus
 *  chips, then the two other answers set apart.
 *
 * One `role="group"` ("Adjust the build") holding the switch and the chips
 * as siblings, so they flow as one line of controls. The chips are
 * single-select `aria-pressed` buttons — the same grammar as the mode switch
 * (DESIGN.md: never `role="tab"`). Every one is a real button in the tab
 * order, so a keyboard reaches each with Tab and picks it with Enter or
 * Space; nothing in the strip is revealed on hover. (The chips had a group of
 * their own beside the switch until it measured badly: at 1024px the switch
 * took a column of its own and the chips wrapped to three rows in what was
 * left, pushing the six's first row to the bottom of a 768px screen.)
 *
 * Phone: one row that scrolls sideways, bled to the screen edge, its right
 * edge faded so the next chip visibly continues past it; the chosen chip is
 * scrolled into view on load, so a shared `build=` link never opens on a
 * selection the reader can't see. From 1024px it wraps instead — the column
 * has the room, and a wrapped strip shows every option at once. */
import { useEffect, useRef, type ReactNode } from "react";
import type { FocusOption } from "../../lib/focus";

export function FocusStrip({ options, selected, onSelect, aspect }: {
  options: FocusOption[];
  selected: string;
  onSelect: (archetype: string) => void;
  /** The aspect switch, when the god has an aspect. */
  aspect?: ReactNode;
}) {
  const scroller = useRef<HTMLDivElement>(null);
  const chosen = useRef<HTMLButtonElement>(null);
  useEffect(() => {
    const box = scroller.current, chip = chosen.current;
    if (!box || !chip || box.scrollWidth <= box.clientWidth) return;
    // Horizontal only: scrollIntoView would also scroll the page vertically.
    const left = chip.offsetLeft - box.offsetLeft;
    if (left < box.scrollLeft || left + chip.offsetWidth > box.scrollLeft + box.clientWidth) {
      box.scrollLeft = Math.max(0, left - 16);
    }
    // Only when the selection changes, not on every render.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selected]);

  if (options.length < 2 && !aspect) return null;
  const focuses = options.filter((o) => o.kind !== "answer");
  const answers = options.filter((o) => o.kind === "answer");
  const chip = (o: FocusOption) => {
    const on = o.archetype === selected;
    return (
      <button key={o.archetype} type="button" aria-pressed={on} ref={on ? chosen : undefined}
        onClick={() => onSelect(o.archetype)} data-archetype={o.archetype}
        className={`press h-11 flex-none snap-start whitespace-nowrap rounded-[10px] px-3.5 font-cond text-[17px] font-bold uppercase transition-colors duration-150 ${
          on ? "bg-accent text-accent-ink" : "bg-surface text-muted ring-1 ring-line hover:text-ink hover:ring-line-strong"}`}>
        {o.label}
      </button>
    );
  };

  return (
    <div ref={scroller} data-testid="focus-strip" role="group" aria-label="Adjust the build"
      className="focus-strip -mx-4 flex snap-x items-center gap-2 overflow-x-auto px-4 py-1 pr-10 lg:mx-0 lg:flex-wrap lg:overflow-visible lg:px-0 lg:pr-0">
      {aspect}
      {options.length > 1 && focuses.map(chip)}
      {options.length > 1 && answers.length > 0 && (
        <>
          <span aria-hidden="true" className="mx-1 h-7 w-px flex-none bg-line-strong" />
          {answers.map(chip)}
        </>
      )}
    </div>
  );
}
