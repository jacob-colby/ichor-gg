/** Conquest / Joust / Arena as one segmented control. Selected = ink on
 *  violet, the app's one selection colour. Each segment is 44px tall. */
import type { Mode } from "./verdict";

const MODES: { key: Mode; label: string }[] = [
  { key: "conquest", label: "Conquest" },
  { key: "joust", label: "Joust" },
  { key: "arena", label: "Arena" },
];

export function ModeSwitch({ mode, onChange, className = "" }: {
  mode: Mode; onChange: (m: Mode) => void; className?: string;
}) {
  return (
    <div role="group" aria-label="Game mode"
      className={`grid grid-cols-[1.3fr_1fr_1fr] rounded-[12px] bg-surface p-1 ${className}`}>
      {MODES.map(({ key, label }) => {
        const on = key === mode;
        return (
          <button key={key} type="button" aria-pressed={on} onClick={() => onChange(key)}
            className={`press h-11 min-w-0 rounded-[9px] px-1.5 font-cond text-[18px] font-bold uppercase transition-colors duration-150 ${
              on ? "bg-accent text-accent-ink" : "text-muted hover:text-ink"}`}>
            {label}
          </button>
        );
      })}
    </div>
  );
}
