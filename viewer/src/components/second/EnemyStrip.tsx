/** The enemy team, carried on the god page.
 *
 * Five slots in one row (three in Joust). Tapping any slot opens the picker
 * sheet on that slot. The enemy side has no hue: an ink outline and the word
 * "Enemy" — violet stays the model's.
 *
 * Two layouts of the same control: `bar` is the phone's sticky strip above
 * the tab bar; `panel` is the desktop second column's, with names under the
 * portraits. Same props, same behaviour. */
import { Art, PlusGlyph } from "./art";

export function EnemyStrip({ enemies, onOpen, changeCount, variant = "bar", onClear }: {
  enemies: string[];
  onOpen: (index: number) => void;
  /** Items the team moved in the six, for the count line. */
  changeCount: number;
  variant?: "bar" | "panel";
  onClear?: () => void;
}) {
  const known = enemies.filter(Boolean).length;
  const status = known === 0
    ? "Add who you're facing"
    : changeCount > 0
      ? `${changeCount} item${changeCount === 1 ? "" : "s"} changed for them`
      : "No change to the six";

  const slots = (
    <ol className={`grid gap-2 ${variant === "panel" ? "mt-3" : ""}`}
      style={{ gridTemplateColumns: `repeat(${enemies.length}, minmax(0, 1fr))` }}>
      {enemies.map((name, i) => (
        <li key={i} className="min-w-0">
          <button type="button" onClick={() => onOpen(i)}
            aria-label={name ? `Enemy ${i + 1}: ${name}. Change` : `Add enemy ${i + 1}`}
            className={`press flex w-full flex-col items-center gap-1 ${variant === "bar" ? "" : "py-0.5"}`}>
            {name ? (
              <Art name={name} kind="head"
                className={`aspect-square w-full rounded-[10px] ring-[1.5px] ring-ink ${variant === "bar" ? "max-w-12" : ""}`} />
            ) : (
              <span className={`flex aspect-square w-full items-center justify-center rounded-[10px] border-[1.5px] border-dashed border-quiet text-muted ${variant === "bar" ? "max-w-12" : ""}`}>
                <PlusGlyph size={20} />
              </span>
            )}
            {variant === "panel" && (
              <span className={`w-full truncate text-center text-cap ${name ? "text-ink" : "text-quiet"}`}>
                {name || "Empty"}
              </span>
            )}
          </button>
        </li>
      ))}
    </ol>
  );

  if (variant === "panel") {
    return (
      <section aria-labelledby="enemy-h" data-testid="enemy-strip" className="rounded-[14px] border border-line bg-surface p-4">
        <div className="flex items-baseline justify-between gap-3">
          <h2 id="enemy-h" className="font-cond text-[24px] font-extrabold text-ink">Enemy team</h2>
          <span className="num text-note text-muted">{known} of {enemies.length} known</span>
        </div>
        <p className="mt-0.5 text-note text-muted" aria-live="polite">{status}</p>
        {slots}
        {known > 0 && onClear && (
          <button type="button" onClick={onClear}
            className="press mt-3 h-11 w-full rounded-[10px] border border-line text-note font-semibold text-muted hover:text-ink">
            Clear enemy team
          </button>
        )}
      </section>
    );
  }

  return (
    <section aria-label="Enemy team" data-testid="enemy-strip"
      className="grid grid-cols-[auto_minmax(0,1fr)] items-center gap-3 rounded-[14px] border border-line bg-surface/95 px-3 py-2 shadow-[var(--shadow-raised)] backdrop-blur-sm">
      <div className="w-[76px]">
        <p className="font-cond text-[19px] font-extrabold uppercase leading-none text-ink">Enemy</p>
        <p className="num mt-1 text-cap leading-tight text-muted" aria-live="polite">
          {known === 0 ? "Tap a slot" : `${known} of ${enemies.length}`}
          {known > 0 && changeCount > 0 && <span className="block text-accent">{changeCount} swap{changeCount === 1 ? "" : "s"}</span>}
        </p>
      </div>
      {slots}
    </section>
  );
}
