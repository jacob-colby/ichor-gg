import type { God } from "../types";

const STAT_LABELS: Record<string, string> = {
  health: "Health",
  mana: "Mana",
  physical_prot: "Physical Prot.",
  magical_prot: "Magical Prot.",
  attack_speed: "Attack Speed",
  move_speed: "Move Speed",
};

export function GodInfo({ god }: { god: God }) {
  const stats = Object.entries(god.base_stats ?? {});
  return (
    <div className="max-w-2xl">
      <div className="mb-4 text-xs text-muted">
        {[god.pantheon, god.role, god.damage_type, god.release_date].filter(Boolean).join(" · ")}
      </div>

      {stats.length > 0 && (
        <div className="mb-5">
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">BASE STATS</div>
          <div className="grid grid-cols-[auto_1fr_1fr] gap-x-4 gap-y-1 text-sm">
            <div className="text-[10px] uppercase text-muted">Stat</div>
            <div className="text-[10px] uppercase text-muted">Base</div>
            <div className="text-[10px] uppercase text-muted">/ level</div>
            {stats.map(([k, v]) => (
              <div key={k} className="contents">
                <div className="text-muted">{STAT_LABELS[k] ?? k}</div>
                <div className="font-mono text-ink">{v.base}</div>
                <div className="font-mono text-muted">+{v.per_level}</div>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="mb-5">
        <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">ABILITIES</div>
        <div className="flex flex-col gap-3">
          {(god.abilities ?? []).map((a, i) => (
            <div key={`${a.name}-${i}`} className="rounded border border-line bg-bg1 p-2">
              <div className="flex items-baseline gap-2">
                <span className="text-[10px] uppercase text-muted">{a.slot}</span>
                <span className="font-display text-sm font-semibold text-ink">{a.name}</span>
              </div>
              {a.description && <div className="mt-1 text-sm text-muted">{a.description}</div>}
              {a.details?.length ? (
                <div className="mt-1 flex flex-wrap gap-x-3 text-xs text-muted">
                  {a.details.map((d, j) => <span key={j} className="font-mono">{d}</span>)}
                </div>
              ) : null}
            </div>
          ))}
        </div>
      </div>

      {god.aspects?.[0] && (
        <div>
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">ASPECT</div>
          <div className="rounded border border-gold/40 bg-bg1 p-2 text-sm">
            <span className="font-display font-semibold text-gold">{god.aspects[0].name}</span>
            <span className="text-muted"> — {god.aspects[0].kit_changes}</span>
          </div>
        </div>
      )}
    </div>
  );
}
