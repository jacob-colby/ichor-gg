import { useState } from "react";
import type { PatchDelta, PatchPeriod } from "../types";
import { iconSlug } from "../lib/builds";

const VERDICT_CLS: Record<PatchDelta["verdict"], string> = {
  buff: "bg-under/10 text-under",
  nerf: "bg-premium/10 text-premium",
  mixed: "bg-gold/10 text-gold",
  adjusted: "bg-line text-muted",
};

function parseLeadingNumber(v: string | number | null | undefined): number | null {
  if (v == null) return null;
  if (typeof v === "number") return v;
  const m = /-?\d+\.?\d*/.exec(v);
  return m ? parseFloat(m[0]) : null;
}

function fallbackIcon(name: string) {
  return (e: React.SyntheticEvent<HTMLImageElement>) => {
    const i = e.currentTarget;
    if (i.dataset.r) { i.style.visibility = "hidden"; return; }
    i.dataset.r = "1";
    i.src = `/icons/${iconSlug(name)}.png?r=1`;
  };
}

function DeltaRow({
  label,
  oldVal,
  newVal,
  inverted,
}: {
  label: string;
  oldVal: string | number | null;
  newVal: string | number | null;
  inverted?: boolean;
}) {
  const oldNum = parseLeadingNumber(oldVal);
  const newNum = parseLeadingNumber(newVal);
  let direction: "up" | "down" | null = null;
  if (oldNum != null && newNum != null) {
    if (newNum > oldNum) direction = "up";
    else if (newNum < oldNum) direction = "down";
  }
  const good = direction == null ? null : inverted ? direction === "down" : direction === "up";
  const newCls = good == null ? "text-ink-soft" : good ? "text-under" : "text-premium";

  return (
    <div className="flex items-baseline gap-1.5 font-mono text-label">
      <span className="w-28 shrink-0 truncate text-faint">{label}</span>
      <span className="text-ink-soft">{oldVal ?? "—"}</span>
      <span className="text-faint">→</span>
      <span className={newCls} data-direction={direction ?? undefined}>
        {newVal ?? "—"}
      </span>
    </div>
  );
}

function ChangedItemRow({ delta }: { delta: PatchDelta }) {
  const rows: { label: string; oldVal: string | number | null; newVal: string | number | null; inverted?: boolean }[] = [];
  if (delta.cost) {
    rows.push({ label: "Cost", oldVal: delta.cost[0], newVal: delta.cost[1], inverted: true });
  }
  for (const [stat, [oldVal, newVal]] of Object.entries(delta.stats)) {
    rows.push({ label: stat, oldVal, newVal });
  }

  return (
    <div className="flex items-start gap-2.5 rounded-lg border border-line bg-bg2 p-2.5">
      <img
        src={`/icons/${iconSlug(delta.name)}.png`}
        alt=""
        className="h-8 w-8 shrink-0 rounded-sm object-cover"
        onError={fallbackIcon(delta.name)}
      />
      <div className="min-w-0 flex-1">
        <div className="mb-1.5 flex flex-wrap items-center gap-2">
          <span className="font-display text-body font-semibold text-ink">{delta.name}</span>
          <span className={`rounded-sm px-1.5 py-0.5 text-micro font-semibold uppercase tracking-wide ${VERDICT_CLS[delta.verdict]}`}>
            {delta.verdict}
          </span>
        </div>
        {rows.length > 0 && (
          <div className="flex flex-col gap-0.5">
            {rows.map((r) => (
              <DeltaRow key={r.label} label={r.label} oldVal={r.oldVal} newVal={r.newVal} inverted={r.inverted} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

function ChevronIcon({ open }: { open: boolean }) {
  return (
    <svg
      viewBox="0 0 24 24"
      width="14"
      height="14"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      className={`shrink-0 text-faint transition-transform duration-[150ms] ease-standard ${open ? "rotate-90" : ""}`}
    >
      <path d="M9 6l6 6-6 6" />
    </svg>
  );
}

function PeriodSection({ period, defaultOpen }: { period: PatchPeriod; defaultOpen: boolean }) {
  const [open, setOpen] = useState(defaultOpen);

  const counts = [
    period.changed.length > 0 ? `${period.changed.length} changed` : null,
    period.added.length > 0 ? `${period.added.length} added` : null,
    period.removed.length > 0 ? `${period.removed.length} removed` : null,
  ].filter(Boolean).join(" · ");

  return (
    <div className="mb-3 overflow-hidden rounded-xl border border-line bg-bg1">
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        className="press flex w-full items-center gap-3 px-4 py-3 text-left"
        aria-expanded={open}
      >
        <ChevronIcon open={open} />
        <span className="font-mono text-small text-faint">{period.from} → {period.to}</span>
        <span className="ml-auto font-mono text-label text-faint">{counts}</span>
      </button>
      {open && (
        <div className="flex flex-col gap-3 border-t border-line px-4 py-3">
          {period.changed.length > 0 && (
            <div className="flex flex-col gap-2">
              {period.changed.map((d) => <ChangedItemRow key={d.name} delta={d} />)}
            </div>
          )}
          {period.added.length > 0 && (
            <div className="flex flex-wrap gap-1.5">
              {period.added.map((n) => (
                <span key={n} className="inline-flex items-center gap-1.5 rounded-sm bg-blue/10 px-1.5 py-0.5 text-micro font-semibold text-blue">
                  <span className="uppercase tracking-wide">new</span>
                  <span>{n}</span>
                </span>
              ))}
            </div>
          )}
          {period.removed.length > 0 && (
            <div className="flex flex-wrap gap-2">
              {period.removed.map((n) => (
                <span key={n} className="text-label text-muted line-through">{n}</span>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export function PatchNotes({ periods }: { periods: PatchPeriod[] }) {
  if (periods.length === 0) {
    return (
      <div className="flex flex-col items-center gap-2 px-4 py-20 text-center">
        <p className="font-display text-body font-semibold text-ink">No patch history yet</p>
        <p className="max-w-sm text-small text-muted">
          Changes appear after the next data refresh — patch history starts accruing from the first snapshot.
        </p>
      </div>
    );
  }

  return (
    <div className="p-4">
      {periods.map((p, i) => (
        <PeriodSection key={`${p.from}-${p.to}`} period={p} defaultOpen={i === 0} />
      ))}
    </div>
  );
}
