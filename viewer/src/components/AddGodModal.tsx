import { useMemo, useState } from "react";
import type { RosterGod } from "../types";
import { iconSlug } from "../lib/builds";

/** Dev-only add-god picker: a searchable grid of the full roster. Tracked gods
 * are dimmed + marked; untracked gods are clickable to scrape + add. */
export function AddGodModal({
  roster, tracked, onAdd, onClose,
}: {
  roster: RosterGod[];
  tracked: string[];
  onAdd: (name: string) => void;
  onClose: () => void;
}) {
  const [q, setQ] = useState("");
  const trackedSet = useMemo(() => new Set(tracked), [tracked]);
  const shown = useMemo(() => {
    const ql = q.trim().toLowerCase();
    return roster.filter((g) => !ql || g.name.toLowerCase().includes(ql));
  }, [roster, q]);

  const devTag = "rounded border border-line-strong px-1.5 py-px font-mono text-micro uppercase tracking-wider text-faint";

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" onClick={onClose}>
      <div
        className="flex max-h-[85vh] w-full max-w-2xl flex-col rounded-lg border border-dashed border-line-strong bg-bg1 p-4 shadow-raised"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="mb-1 flex items-center gap-2">
          <span className={devTag}>Dev</span>
          <div className="font-display text-lead font-semibold text-ink-soft">Add a god</div>
          <button type="button" onClick={onClose} className="press ml-auto rounded-md bg-bg2 px-2 py-1 text-small text-faint hover:text-muted">Close</button>
        </div>
        <p className="mb-3 text-label text-faint">Adding a new god scrapes fresh build data — this can take a minute.</p>
        <div className="mb-3 flex items-center gap-2 rounded-md border border-line bg-bg2 px-3 py-2 focus-within:border-blue">
          <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2" className="text-muted"><circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" /></svg>
          <input
            placeholder="Search gods…"
            value={q}
            onChange={(e) => setQ(e.target.value)}
            className="w-full bg-transparent text-small text-ink placeholder:text-muted focus:outline-none"
          />
        </div>
        <div className="grid flex-1 grid-cols-[repeat(auto-fill,minmax(100px,1fr))] gap-2 overflow-y-auto">
          {shown.map((g) => {
            const isTracked = trackedSet.has(g.name);
            return (
              <button
                key={g.name}
                type="button"
                disabled={isTracked}
                onClick={() => onAdd(g.name)}
                aria-label={isTracked ? `${g.name} (already tracked)` : `Add ${g.name}`}
                title={isTracked ? `${g.name} (already tracked)` : `Add ${g.name}`}
                className={`press flex flex-col items-center gap-1.5 rounded-lg border p-2 transition-colors duration-[180ms] ease-standard ${
                  isTracked ? "cursor-default border-line bg-bg2 opacity-40" : "border-line bg-bg2 hover:border-line-strong"
                }`}
              >
                {g.thumb ? (
                  <img src={g.thumb} alt="" className="h-10 w-10 rounded-md object-cover ring-1 ring-line" />
                ) : (
                  <img
                    src={`/icons/${iconSlug(g.name)}-head.png`}
                    alt=""
                    className="h-10 w-10 rounded-md object-cover ring-1 ring-line"
                    onError={(e) => {
                      // untracked gods have no local icon — fall back to an initial disc
                      const img = e.currentTarget;
                      const span = img.nextElementSibling as HTMLElement | null;
                      img.style.display = "none";
                      if (span) span.style.display = "flex";
                    }}
                  />
                )}
                <span
                  style={{ display: "none" }}
                  className="h-10 w-10 items-center justify-center rounded-md bg-bg1 font-display text-title text-muted ring-1 ring-line"
                >
                  {g.name[0]}
                </span>
                <span className="truncate text-center font-display text-label text-ink">{g.name}</span>
                {isTracked && <span className="text-micro text-under">✓ tracked</span>}
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
}
