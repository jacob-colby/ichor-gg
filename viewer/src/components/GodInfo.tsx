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

const eyebrow = "font-mono text-label uppercase tracking-[0.1em] text-faint";

/** Compacts an ability slot name ("1st Ability", "Ultimate", ...) down to a
 * single glyph for the 20-cell level grid. Falls back to the first letter for
 * any slot name abilities.py might emit that isn't one of the four known
 * SMITE 2 slots, so an unrecognized label still renders instead of blanking. */
function abilityGlyph(slot: string): string {
  if (slot === "Ultimate") return "U";
  const m = /^(\d)/.exec(slot);
  return m ? m[1] : slot.charAt(0);
}

/** The four ability slots a full kit scrapes. Anything short of this is a
 * coverage gap worth stating rather than a shorter list to scroll past. */
const EXPECTED_SLOTS = ["Passive", "1st Ability", "2nd Ability", "3rd Ability", "Ultimate"];

export function GodInfo({ god }: { god: God }) {
  const stats = Object.entries(god.base_stats ?? {});
  const abilities = god.abilities ?? [];
  const missingSlots = EXPECTED_SLOTS.filter((s) => !abilities.some((a) => a.slot === s));

  return (
    <article className="max-w-3xl">
      {/* The Info tab renders instead of DetailPanel, so without this the route
          had no heading of any level at all. */}
      <header className="border-b border-line pb-4">
        <h1 className="font-display text-title font-bold leading-none text-ink">{god.name}</h1>
        <p className="mt-1.5 text-small text-muted">
          {god.pantheon}
          {god.role && <> · <span className={godRoleTextClass(god)}>{god.role}</span></>}
          {god.damage_type && <> · <span className={damageTextClass(god.damage_type)}>{god.damage_type}</span></>}
          {god.release_date && <> · released {god.release_date}</>}
        </p>
        {(god.specializations?.length ?? 0) > 0 && (
          <ul className="mt-2 flex flex-wrap gap-1">
            {god.specializations!.map((s) => (
              <li key={s} className="rounded-sm bg-bg3 px-1.5 py-0.5 text-label text-muted">{s}</li>
            ))}
          </ul>
        )}
      </header>

      {stats.length > 0 && (
        <section aria-labelledby="info-stats-h" className="mt-5 border-t border-line pt-4">
          <h2 id="info-stats-h" className={eyebrow}>Base stats</h2>
          <table className="mt-2.5 w-full text-body">
            <thead>
              <tr className={eyebrow}>
                <th scope="col" className="pb-1 text-left font-normal">Stat</th>
                <th scope="col" className="pb-1 text-right font-normal">Base</th>
                <th scope="col" className="pb-1 text-right font-normal">Per level</th>
                <th scope="col" className="pb-1 text-right font-normal">At 20</th>
              </tr>
            </thead>
            <tbody>
              {stats.map(([k, v]) => (
                <tr key={k} className="border-t border-line">
                  <td className="py-1 text-ink-soft">{STAT_LABELS[k] ?? k}</td>
                  <td className="py-1 text-right font-mono text-ink">{v.base}</td>
                  <td className="py-1 text-right font-mono text-muted">+{v.per_level}</td>
                  {/* Levels 2-20 apply the per-level gain, so 19 increments. */}
                  <td className="py-1 text-right font-mono text-ink-soft">
                    {Math.round((v.base + v.per_level * 19) * 100) / 100}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}

      <section aria-labelledby="info-abilities-h" className="mt-5 border-t border-line pt-4">
        <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
          <h2 id="info-abilities-h" className={eyebrow}>Abilities</h2>
          <p className="text-label text-faint">
            {abilities.length} of {EXPECTED_SLOTS.length + 1} slots scraped
          </p>
        </div>

        {abilities.length === 0 ? (
          <p className="mt-2 max-w-[64ch] text-small leading-relaxed text-muted">
            No abilities scraped for {god.name} yet.
          </p>
        ) : (
          <ul className="mt-2.5 flex flex-col divide-y divide-line">
            {abilities.map((a, i) => (
              <li key={`${a.name}-${i}`} className="py-3">
                <div className="flex flex-wrap items-baseline gap-x-2 gap-y-1">
                  <span className="font-mono text-label uppercase tracking-[0.08em] text-faint">{a.slot}</span>
                  <h3 className="font-display text-body font-semibold text-ink">{a.name}</h3>
                  {a.cooldown?.length ? (
                    <span className="ml-auto font-mono text-label text-faint">
                      {a.cooldown.join(" / ")}s cooldown
                    </span>
                  ) : null}
                </div>
                {a.description && (
                  <p className="mt-1 max-w-[72ch] text-small leading-relaxed text-ink-soft">{a.description}</p>
                )}
                {a.details?.length ? (
                  <ul className="mt-1.5 flex flex-wrap gap-x-3 gap-y-0.5">
                    {a.details.map((d, j) => (
                      <li key={j} className="text-label text-faint">{d}</li>
                    ))}
                  </ul>
                ) : null}
              </li>
            ))}
          </ul>
        )}

        {missingSlots.length > 0 && (
          <p className="mt-2.5 max-w-[68ch] text-small leading-relaxed text-muted">
            {missingSlots.join(", ")} {missingSlots.length === 1 ? "wasn’t" : "weren’t"} scraped
            from the wiki for {god.name} — a gap in the source page, not an empty kit.
          </p>
        )}
      </section>

      <section aria-labelledby="info-order-h" className="mt-5 border-t border-line pt-4">
        <h2 id="info-order-h" className={eyebrow}>Ability order</h2>
        {god.ability_order ? (
          <>
            <ol className="mt-2.5 grid grid-cols-10 gap-1">
              {god.ability_order.order.map((slot, i) => {
                const level = i + 1;
                const isUlt = god.ability_order!.summary.ult_levels.includes(level);
                return (
                  <li
                    key={level}
                    title={`Level ${level}: ${slot}`}
                    className={`flex flex-col items-center rounded-sm py-1 ${
                      isUlt ? "bg-gold/20 text-gold" : "bg-bg2 text-ink-soft"}`}
                  >
                    <span className="font-mono text-micro text-faint">{level}</span>
                    <span className="font-mono text-label font-semibold">{abilityGlyph(slot)}</span>
                  </li>
                );
              })}
            </ol>
            <p className="mt-2 text-label text-faint">
              max order · {god.ability_order.summary.max_order.join(" → ")}
            </p>
            <p className="mt-1 max-w-[68ch] text-small leading-relaxed text-muted">
              Derived from ability scaling — a heuristic, not community data.
            </p>
          </>
        ) : (
          /* Artio, Merlin and Ullr are stance gods with no levelable abilities.
             The section used to vanish, which reads as missing rather than as
             a fact about the kit. */
          <p className="mt-2 max-w-[68ch] text-small leading-relaxed text-muted">
            {god.name} has no levelable ability order — stance gods swap kits rather than
            ranking up individual abilities, so there is nothing to rank.
          </p>
        )}
      </section>

      {god.aspects?.[0] && (
        <section aria-labelledby="info-aspect-h" className="mt-5 border-t border-line pt-4">
          <h2 id="info-aspect-h" className={eyebrow}>Aspect</h2>
          <p className="mt-2 max-w-[72ch] text-small leading-relaxed">
            <span className="font-display font-semibold text-gold">{god.aspects[0].name}</span>
            <span className="text-muted"> — {god.aspects[0].kit_changes}</span>
          </p>
        </section>
      )}

      {god.source_url && (
        <a href={god.source_url} target="_blank" rel="noreferrer"
          className="press mt-5 inline-block rounded-sm py-1.5 text-label font-medium text-blue hover:underline">
          Wiki page →
        </a>
      )}
    </article>
  );
}
