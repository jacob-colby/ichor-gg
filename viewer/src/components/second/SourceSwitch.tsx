/** Ichor / Community as one segmented control, above the buy order. Same
 *  grammar as the mode switch (single-select `aria-pressed` buttons, never
 *  `role="tab"`). "Community" is the six that players actually build; it is a
 *  place to look, not a toggle on the sentence above it. */
export type BuildSource = "ichor" | "community";

const SOURCES: { key: BuildSource; label: string }[] = [
  { key: "ichor", label: "Ichor" },
  { key: "community", label: "Community" },
];

export function SourceSwitch({ source, onChange, className = "" }: {
  source: BuildSource; onChange: (s: BuildSource) => void; className?: string;
}) {
  return (
    <div role="group" aria-label="Whose build" data-testid="source-switch"
      className={`grid grid-cols-2 rounded-[12px] bg-surface p-1 ${className}`}>
      {SOURCES.map(({ key, label }) => {
        const on = key === source;
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
