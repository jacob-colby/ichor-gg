import { useState } from "react";
import type { PatchDelta, PatchHighlight, PatchPeriod } from "../types";
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
    <div className="flex items-baseline gap-1.5 text-label">
      <span className="w-28 shrink-0 truncate text-faint">{label}</span>
      <span className="font-mono text-ink-soft">{oldVal ?? "none"}</span>
      <span className="text-faint">→</span>
      <span className={`font-mono ${newCls}`} data-direction={direction ?? undefined}>
        {newVal ?? "none"}
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
    <div className="plane flex items-start gap-2.5 rounded-lg border border-line bg-bg2 p-2.5">
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

const CHANGE_CLS: Record<PatchHighlight["change"], string> = {
  ...VERDICT_CLS,
  added: "bg-blue/10 text-blue",
  removed: "bg-line text-muted",
};

const GROUP_LABEL: Record<PatchHighlight["group"], string> = {
  items: "Items",
  gods: "Gods",
  systems: "Systems",
};

function periodTitle(p: PatchPeriod): string {
  if (p.crosses_patch && p.patch_to) {
    return p.patch_from ? `${p.patch_from} to ${p.patch_to}` : p.patch_to;
  }
  if (p.patch_to) return `Data update within ${p.patch_to}`;
  return "Data update";
}

function HighlightRow({ h }: { h: PatchHighlight }) {
  return (
    <li className="flex items-center gap-2.5 py-1.5">
      <img
        src={`/icons/${iconSlug(h.name)}.png`}
        alt=""
        className="h-7 w-7 shrink-0 rounded-sm object-cover"
        onError={fallbackIcon(h.name)}
      />
      <div className="min-w-0 flex-1">
        <div className="flex flex-wrap items-center gap-x-2 gap-y-0.5">
          <span className="font-display text-body font-semibold text-ink">{h.name}</span>
          <span className={`rounded-sm px-1.5 py-0.5 text-micro font-semibold uppercase tracking-wide ${CHANGE_CLS[h.change]}`}>
            {h.change}
          </span>
        </div>
        <div className="truncate font-mono text-label text-ink-soft">{h.headline}</div>
      </div>
    </li>
  );
}

function Highlights({ period }: { period: PatchPeriod }) {
  const hl = period.highlights ?? [];
  if (hl.length === 0) {
    const note = !period.crosses_patch && period.added.length > 0
      ? `No item stats moved. ${period.added.length} item${period.added.length === 1 ? "" : "s"} entered Ichor\u2019s data here; they were already in the game, so they are not listed as new.`
      : "No item cost or stat moved enough to call out.";
    return <p className="text-label leading-relaxed text-muted">{note}</p>;
  }
  const groups = (Object.keys(GROUP_LABEL) as PatchHighlight["group"][])
    .map((g) => [g, hl.filter((h) => h.group === g)] as const)
    .filter(([, rows]) => rows.length > 0);
  return (
    <div className="flex flex-col gap-2">
      {groups.map(([g, rows]) => (
        <div key={g}>
          <h4 className="text-micro font-semibold uppercase tracking-wide text-faint">{GROUP_LABEL[g]}</h4>
          <ul className="divide-y divide-line">
            {rows.map((h) => <HighlightRow key={`${h.change}-${h.name}`} h={h} />)}
          </ul>
        </div>
      ))}
    </div>
  );
}

function FullDetail({ period }: { period: PatchPeriod }) {
  return (
    <div className="flex flex-col gap-3">
      {period.changed.length > 0 && (
        <div className="flex flex-col gap-2">
          {period.changed.map((d) => <ChangedItemRow key={d.name} delta={d} />)}
        </div>
      )}
      {period.added.length > 0 && (
        <div>
          <h4 className="mb-1.5 text-micro font-semibold uppercase tracking-wide text-faint">
            {period.crosses_patch === false ? "Entered Ichor\u2019s data" : "Added"}
          </h4>
          <div className="flex flex-wrap gap-1.5">
            {period.added.map((n) => (
              <span key={n} className="inline-flex items-center rounded-sm bg-line px-1.5 py-0.5 text-micro text-ink-soft">
                {n}
              </span>
            ))}
          </div>
        </div>
      )}
      {period.removed.length > 0 && (
        <div>
          <h4 className="mb-1.5 text-micro font-semibold uppercase tracking-wide text-faint">Removed</h4>
          <div className="flex flex-wrap gap-2">
            {period.removed.map((n) => (
              <span key={n} className="text-label text-muted line-through">{n}</span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

function PeriodSection({ period }: { period: PatchPeriod }) {
  const [open, setOpen] = useState(false);
  const total = period.changed.length + period.added.length + period.removed.length;

  return (
    <section className="mb-3 overflow-hidden rounded-lg border border-line bg-bg1">
      <header className="flex flex-wrap items-baseline gap-x-3 gap-y-1 px-4 pt-3">
        <h2 className="font-display text-title font-semibold text-ink">{periodTitle(period)}</h2>
        <span className="font-mono text-label text-faint">{period.from} to {period.to}</span>
        {period.official_url && (
          <a
            href={period.official_url}
            target="_blank"
            rel="noopener noreferrer"
            className="ml-auto text-label font-semibold text-gold underline-offset-2 hover:underline"
          >
            Official patch notes
          </a>
        )}
      </header>
      <div className="px-4 pb-3 pt-2">
        <h3 className="sr-only">Biggest changes</h3>
        <Highlights period={period} />
      </div>
      {total > 0 && (
        <>
          <button
            type="button"
            onClick={() => setOpen((o) => !o)}
            className="press flex w-full items-center gap-2 border-t border-line px-4 py-2.5 text-left text-label text-muted"
            aria-expanded={open}
          >
            <ChevronIcon open={open} />
            <span>All changes ({total})</span>
          </button>
          {open && (
            <div className="border-t border-line px-4 py-3">
              <FullDetail period={period} />
            </div>
          )}
        </>
      )}
    </section>
  );
}

export function PatchNotes({ periods }: { periods: PatchPeriod[] }) {
  const patches = periods.filter((p) => p.crosses_patch).length;

  return (
    <div className="mx-auto w-full max-w-3xl p-4 sm:p-6">
      <header className="border-b border-line pb-4">
        <h1 className="max-w-[26ch] text-balance font-display text-display font-bold leading-[1.12] tracking-[-0.01em] text-ink">
          {periods.length === 0
            ? "Nothing has changed yet."
            : patches === 0
              ? "No patch has landed in Ichor\u2019s data yet."
              : <>The biggest item changes, across <span className="text-gold">{patches}</span> patch{patches === 1 ? "" : "es"}.</>}
        </h1>
        <p className="mt-2.5 max-w-[70ch] text-body leading-relaxed text-ink-soft">
          {periods.length === 0
            ? "Patch history is a diff between two data refreshes, so it starts empty and fills in from the first snapshot onward. This isn\u2019t a loading state."
            : "Each update lists its biggest changes first, newest at the top. The full list is one tap below."}
        </p>
        {periods.length > 0 && (
          <details className="mt-2 text-label text-muted">
            <summary className="cursor-pointer text-faint">How the biggest changes are picked</summary>
            <p className="mt-1.5 max-w-[70ch] leading-relaxed">
              Automatically, up to five per update: removed items first, then new items, then the
              items whose cost or any one stat moved the most relative to its old value (20 to 30
              power is a 50% move). Reworded passives with no number to compare stay in the full
              list. An update that falls inside a single game patch is Ichor catching up on its own
              data, so items it adds there are not called new. Gods and system changes are not
              tracked yet. Official notes are linked only where the link has been checked by hand.
            </p>
          </details>
        )}
      </header>

      {periods.length > 0 && (
        <div className="mt-4">
          {periods.map((p) => (
            <PeriodSection key={`${p.from}-${p.to}`} period={p} />
          ))}
        </div>
      )}
    </div>
  );
}
