/* THESIS: this lens owns "what does the model think this god wants, and in what
 * order?" The index has carried 40 scored items per god for 87 gods all along,
 * and exactly one surface read them — the draft board, to decide displacements.
 * The question itself had no page.
 * OWN-WORLD: Arena Night. Hairline rule-work, mono for figures only, gold
 * reserved for the model's own signal; `under`/`premium` carry gold-price
 * direction, the same pair the items shelf uses.
 * STORY: a player on Ra's page asks what else the model rates for Ra, sees the
 * ranked 40 against the six the build actually takes, and finds the near-misses
 * — which is where an argument with the build starts.
 * FIRST VIEWPORT: a claim carrying the live count and the honest spread, then
 * the ranked list with the core marked in place.
 */
import { useMemo, useState } from "react";
import type { Item } from "../types";
import { buildGodItems, scoreBarPercent } from "../lib/godItems";
import { residualText } from "../lib/itemFilters";
import { toHash } from "../lib/useHashRoute";
import { ItemIcon } from "./ItemsShop";

function residualClass(residual: number | null | undefined): string {
  if (residual == null) return "text-faint";
  if (residual < 0) return "text-under";
  if (residual > 0) return "text-premium";
  return "text-faint";
}

export function GodItems({ god, scores, items, core }: {
  god: string;
  scores?: Record<string, number>;
  items: Item[];
  /** The god's suggested core, so the ranking can be read against the build. */
  core: string[];
}) {
  const itemsByName = useMemo(() => new Map(items.map((i) => [i.name, i])), [items]);
  const result = useMemo(
    () => buildGodItems(scores, itemsByName, core), [scores, itemsByName, core]);
  const [coreOnly, setCoreOnly] = useState(false);

  if (result.rows.length === 0) {
    return (
      <section aria-labelledby="god-items-h" className="max-w-[68ch]">
        <h2 id="god-items-h" className="font-display text-title font-bold text-ink">
          No item ranking for {god}
        </h2>
        <p className="mt-2 text-body leading-relaxed text-muted">
          The model scores items per god from the same fit that drives the build, but it hasn&rsquo;t
          scored any for {god} in this index. That&rsquo;s a gap in the pipeline&rsquo;s coverage,
          not a judgement that nothing suits this god.
        </p>
      </section>
    );
  }

  const best = result.rows[0].score;
  const worst = result.rows[result.rows.length - 1].score;
  const shown = coreOnly ? result.rows.filter((r) => r.inCore) : result.rows;

  return (
    <section aria-labelledby="god-items-h">
      <header className="border-b border-line pb-4">
        <h2 id="god-items-h" className="max-w-[26ch] text-balance font-display text-title font-bold leading-tight text-ink">
          The model ranks <span className="text-gold">{result.rows.length} items</span> for {god}.
        </h2>
        <p className="mt-2 max-w-[70ch] text-body leading-relaxed text-ink-soft">
          The same fit that picks the build, shown in full.{" "}
          {result.coreSize === 0
            ? <>{god} has no suggested core in this mode, so there&rsquo;s nothing to read it against.</>
            : result.coreIsTop
              ? <>The build takes the top <span className="text-ink">{result.coreSize}</span> exactly.</>
              : <><span className="text-ink">{result.coreCovered} of the build&rsquo;s {result.coreSize}</span>{" "}
                  core slots are ranked here, and they aren&rsquo;t simply the top {result.coreSize} —
                  item fit is one of four signals behind a build.</>}
        </p>
        {/* The scores occupy about a tenth of the scale. Saying so stops the
            bars below from implying precision the numbers don't carry. */}
        {result.spread != null && (
          <p className="mt-2 text-label text-faint">
            Scores run <span className="font-mono">{worst.toFixed(2)}</span> to{" "}
            <span className="font-mono">{best.toFixed(2)}</span> — a spread of{" "}
            <span className="font-mono">{result.spread.toFixed(2)}</span>, so the bars below are
            stretched across that range, not drawn from zero. Neighbouring ranks are close to
            indistinguishable.
          </p>
        )}
        {result.missing.length > 0 && (
          <p className="mt-2 max-w-[70ch] text-small leading-relaxed text-muted">
            {result.missing.length} scored {result.missing.length === 1 ? "item isn’t" : "items aren’t"}{" "}
            in this index ({result.missing.slice(0, 3).join(", ")}
            {result.missing.length > 3 ? ", …" : ""}) — {result.missing.length === 1 ? "it’s" : "they’re"}{" "}
            listed below without a price.
          </p>
        )}
      </header>

      {result.coreSize > 0 && (
        <div className="mt-4 flex flex-wrap items-center gap-2">
          <button
            type="button"
            aria-pressed={coreOnly}
            onClick={() => setCoreOnly((v) => !v)}
            className={`press rounded-full px-3 py-1.5 text-small transition-colors duration-[150ms] ease-standard ${
              coreOnly ? "bg-gold font-semibold text-bg0" : "border border-line text-muted hover:border-line-strong"}`}
          >
            Only the core
          </button>
          <span className="text-label text-faint">
            {shown.length === result.rows.length
              ? <>{result.rows.length} items</>
              : <>{shown.length} of {result.rows.length}</>}
          </span>
        </div>
      )}

      <ol className="mt-3 flex flex-col">
        {shown.map((row) => (
          <li key={row.name}>
            <a
              href={toHash.item(row.name)}
              aria-label={`Rank ${row.rank}, ${row.name}, model score ${row.score.toFixed(2)}${
                row.cost != null ? `, ${row.cost} gold` : ", not in this index"}${
                row.inCore ? ", in the suggested core" : ""}`}
              className="press grid grid-cols-[2.2rem_28px_minmax(0,1fr)_auto] items-center gap-x-2.5 gap-y-1 rounded-md border-t border-line py-2 pr-1.5 transition-colors duration-150 ease-standard hover:bg-bg1"
            >
              <span aria-hidden="true" className="text-right font-mono text-label text-faint">
                {row.rank}
              </span>
              <ItemIcon name={row.name} size="h-7 w-7" />
              <span className="flex min-w-0 items-center gap-2">
                <span className={`truncate text-body ${row.inCore ? "font-medium text-ink" : "text-ink-soft"}`}>
                  {row.name}
                </span>
                {row.inCore && (
                  <span className="shrink-0 text-micro font-semibold uppercase tracking-[0.06em] text-gold">
                    in core
                  </span>
                )}
              </span>
              <span aria-hidden="true" className="flex shrink-0 items-center gap-2.5">
                {row.cost != null ? (
                  <span className="font-mono text-label text-faint">{row.cost}g</span>
                ) : (
                  <span className="text-label text-faint">not in index</span>
                )}
                <span className={`w-[52px] text-right font-mono text-label ${residualClass(row.residual)}`}>
                  {row.residual != null ? residualText(row.residual) : "—"}
                </span>
                <span className="hidden h-1 w-16 shrink-0 bg-bg3 sm:block">
                  <span
                    className="bar-grow block h-1 origin-left bg-gold"
                    style={{ width: `${scoreBarPercent(row.score, best, worst)}%` }}
                  />
                </span>
                <span className="w-[38px] text-right font-mono text-label text-ink-soft">
                  {row.score.toFixed(2)}
                </span>
              </span>
            </a>
          </li>
        ))}
      </ol>

      {shown.length === 0 && (
        <p className="mt-4 max-w-[64ch] text-body leading-relaxed text-muted">
          None of {god}&rsquo;s core items are in the model&rsquo;s scored set for this mode.
        </p>
      )}
    </section>
  );
}
