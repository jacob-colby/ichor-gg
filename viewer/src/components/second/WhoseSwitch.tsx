/** Whose build: Ichor's or the community's, chosen before anything else about
 *  the build.
 *
 * It sits above the focus strip because it decides whether there is a strip:
 * Ichor's side has one six and the focuses that adjust it, and the community
 * has one six and nothing to adjust (`communityBuild.ts`). Jacob asked for it
 * on 2026-11-09, replacing the "Show theirs" text button inside the verdict
 * sentence, which only existed for Ichor's main six in Conquest and vanished
 * as soon as a focus was picked.
 *
 * The segmented-control grammar of the mode switch (DESIGN.md): one
 * `role="group"` holding `aria-pressed` buttons, never `role="tab"`. Both are
 * real buttons in the tab order, so Tab reaches each and Enter or Space picks
 * it. Each segment is 44px tall. */
export type Whose = "ichor" | "community";

const SIDES: { key: Whose; label: string }[] = [
  { key: "ichor", label: "Ichor's" },
  { key: "community", label: "Community" },
];

export function WhoseSwitch({ whose, onChange, className = "" }: {
  whose: Whose; onChange: (w: Whose) => void; className?: string;
}) {
  return (
    <div role="group" aria-label="Whose build" data-testid="whose-switch"
      className={`grid grid-cols-2 rounded-[12px] bg-surface p-1 ${className}`}>
      {SIDES.map(({ key, label }) => {
        const on = key === whose;
        return (
          <button key={key} type="button" aria-pressed={on} onClick={() => onChange(key)} data-whose={key}
            className={`press h-11 min-w-0 rounded-[9px] px-1.5 font-cond text-[18px] font-bold uppercase transition-colors duration-150 ${
              on ? "bg-accent text-accent-ink" : "text-muted hover:text-ink"}`}>
            {label}
          </button>
        );
      })}
    </div>
  );
}
