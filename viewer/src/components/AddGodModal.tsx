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

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" onClick={onClose}>
      <div className="flex max-h-[85vh] w-full max-w-2xl flex-col rounded-lg border border-line bg-bg1 p-4" onClick={(e) => e.stopPropagation()}>
        <div className="mb-2 flex items-center">
          <div className="font-display text-lg font-semibold text-ink">Add a god</div>
          <button type="button" onClick={onClose} className="ml-auto rounded bg-bg2 px-2 py-1 text-xs text-muted hover:bg-line">Close</button>
        </div>
        <input placeholder="Search gods…" value={q} onChange={(e) => setQ(e.target.value)}
          className="mb-3 w-full rounded border border-line bg-bg2 px-2 py-1 text-sm text-ink" />
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
                className={`flex flex-col items-center gap-1 rounded-lg border border-line p-2 ${
                  isTracked ? "cursor-default bg-bg2 opacity-40" : "bg-bg2 hover:border-blue"
                }`}
              >
                {g.thumb ? (
                  <img src={g.thumb} alt="" className="h-10 w-10 rounded-lg object-cover ring-1 ring-line" />
                ) : (
                  <img
                    src={`/icons/${iconSlug(g.name)}-head.png`}
                    alt=""
                    className="h-10 w-10 rounded-lg object-cover ring-1 ring-line"
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
                  className="h-10 w-10 items-center justify-center rounded-lg bg-bg1 font-display text-lg text-muted ring-1 ring-line"
                >
                  {g.name[0]}
                </span>
                <span className="truncate text-center text-[10px] text-ink">{g.name}</span>
                {isTracked && <span className="text-[9px] text-under">✓ tracked</span>}
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
}
