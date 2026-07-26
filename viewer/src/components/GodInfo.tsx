import type { God } from "../types";
import { godRoleTextClass, damageTextClass } from "../lib/roleAccent";

const STAT_LABELS: Record<string, string> = {
  health: "Health",
  mana: "Mana",
  physical_prot: "Physical Prot.",
  magical_prot: "Magical Prot.",
  attack_speed: "Attack Speed",
  move_speed: "Move Speed",
};

/** Compacts an ability slot name ("1st Ability", "Ultimate", ...) down to a
 * single glyph for the 20-cell level grid. Falls back to the first letter for
 * any slot name abilities.py might emit that isn't one of the four known
 * SMITE 2 slots, so an unrecognized label still renders instead of blanking. */
function abilityGlyph(slot: string): string {
  if (slot === "Ultimate") return "U";
  const m = /^(\d)/.exec(slot);
  return m ? m[1] : slot.charAt(0);
}

export function GodInfo({ god }: { god: God }) {
  const stats = Object.entries(god.base_stats ?? {});
  return (
    <div className="max-w-2xl">
      <div className="mb-4 text-xs text-muted">
        {god.pantheon}
        {god.role && <> · <span className={godRoleTextClass(god)}>{god.role}</span></>}
        {god.damage_type && <> · <span className={damageTextClass(god.damage_type)}>{god.damage_type}</span></>}
        {god.release_date && <> · {god.release_date}</>}
      </div>

      {stats.length > 0 && (
        <div className="mb-5">
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">BASE STATS</div>
          <div className="rounded-md border border-line bg-bg2 p-3">
            <div className="grid grid-cols-[auto_1fr_1fr] gap-x-4 gap-y-1.5 text-sm">
              <div className="text-[10px] uppercase tracking-wide text-faint">Stat</div>
              <div className="text-[10px] uppercase tracking-wide text-faint">Base</div>
              <div className="text-[10px] uppercase tracking-wide text-faint">/ level</div>
              {stats.map(([k, v]) => (
                <div key={k} className="contents">
                  <div className="text-ink-soft">{STAT_LABELS[k] ?? k}</div>
                  <div className="font-mono text-ink">{v.base}</div>
                  <div className="font-mono text-muted">+{v.per_level}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      <div className="mb-5">
        <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">ABILITIES</div>
        <div className="flex flex-col gap-3">
          {(god.abilities ?? []).map((a, i) => (
            <div key={`${a.name}-${i}`} className="rounded-md border border-line bg-bg2 p-3">
              <div className="flex items-baseline gap-2">
                <span className="text-[10px] uppercase tracking-wide text-faint">{a.slot}</span>
                <span className="font-display text-sm font-semibold text-ink">{a.name}</span>
              </div>
              {a.description && <div className="mt-1 text-sm text-ink-soft">{a.description}</div>}
              {a.details?.length ? (
                <div className="mt-1 flex flex-wrap gap-x-3 text-xs text-muted">
                  {a.details.map((d, j) => <span key={j} className="font-mono">{d}</span>)}
                </div>
              ) : null}
            </div>
          ))}
        </div>
      </div>

      {god.ability_order && (
        <div className="mb-5">
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">ABILITY ORDER</div>
          <div className="rounded-md border border-line bg-bg2 p-3">
            <div className="grid grid-cols-10 gap-1">
              {god.ability_order.order.map((slot, i) => {
                const level = i + 1;
                const isUlt = god.ability_order!.summary.ult_levels.includes(level);
                return (
                  <div
                    key={level}
                    title={slot}
                    className={`flex flex-col items-center rounded-sm py-1 ${
                      isUlt ? "bg-gold/20 text-gold" : "bg-bg1 text-ink-soft"
                    }`}
                  >
                    <span className="text-[9px] text-faint">{level}</span>
                    <span className="font-mono text-[11px] font-semibold">{abilityGlyph(slot)}</span>
                  </div>
                );
              })}
            </div>
            <div className="mt-2 text-xs text-muted">
              max order: {god.ability_order.summary.max_order.join(" → ")}
            </div>
            <div className="mt-1 text-[10px] italic text-faint">
              Derived from ability scaling — a heuristic, not community data.
            </div>
          </div>
        </div>
      )}

      {god.aspects?.[0] && (
        <div>
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">ASPECT</div>
          <div className="rounded-md border border-gold/40 bg-bg2 p-3 text-sm">
            <span className="font-display font-semibold text-gold">{god.aspects[0].name}</span>
            <span className="text-muted"> — {god.aspects[0].kit_changes}</span>
          </div>
        </div>
      )}
    </div>
  );
}
