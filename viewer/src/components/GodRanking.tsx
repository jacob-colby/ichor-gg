/* THESIS: this lens owns "where does this god sit, and who says otherwise?"
 * The tier list answers that for all 87 at once; from a god's own page there
 * was no way to ask it about that god, so arriving from Home mid-argument meant
 * leaving to check. Everything here derives from the same tierlist slice the
 * tier list reads, so the two can't drift.
 * OWN-WORLD: Arena Night. Hairline rules, mono for figures, gold on the model's
 * own score; `under`/`premium` carry divergence direction as everywhere else.
 * STORY: a player reads the model's placement, sees how far the meta disagrees
 * and in which direction, then sees who this god is actually next to.
 * FIRST VIEWPORT: the placement stated in words with both scores, then the two
 * neighbours, then the band and lane standing.
 */
import { useMemo } from "react";
import type { GodTierEntry } from "../types";
import { buildGodRanking, topPercent } from "../lib/godRanking";
import { godLane, laneTextClass } from "../lib/roleAccent";
import { deltaText } from "../lib/divergence";
import { toHash } from "../lib/useHashRoute";

const eyebrow = "font-mono text-label uppercase tracking-[0.1em] text-faint";

function divergenceClass(tierGap: number | null): string {
  if (tierGap == null || tierGap === 0) return "text-faint";
  return tierGap > 0 ? "text-under" : "text-premium";
}

/** One god next to this one on the model's scale. */
function NeighbourRow({ label, n, subject }: {
  label: string;
  n?: { name: string; ours: number; gap: number };
  subject: string;
}) {
  if (!n) {
    return (
      <div className="flex items-baseline justify-between gap-3 border-t border-line py-2">
        <span className="text-small text-faint">{label}</span>
        <span className="text-small text-muted">
          nothing — {subject} is {label === "Above" ? "the model’s top-rated god" : "the model’s lowest-rated god"}
        </span>
      </div>
    );
  }
  return (
    <a
      href={toHash.god(n.name)}
      className="press flex items-baseline justify-between gap-3 border-t border-line py-2 transition-colors duration-150 ease-standard hover:bg-bg1"
    >
      <span className="text-small text-faint">{label}</span>
      <span className="flex min-w-0 items-baseline gap-2">
        <span className="truncate font-display text-body font-semibold text-ink">{n.name}</span>
        <span className="shrink-0 font-mono text-label text-ink-soft">{n.ours.toFixed(2)}</span>
        {/* `deltaText`, not a hand-rolled sign: adjacent gods routinely sit
            within 0.005 of each other, and "+0.00" / "-0.00" would assert a
            direction the printed number doesn't show. */}
        <span className="shrink-0 font-mono text-label text-faint">
          {deltaText(n.gap)}
        </span>
      </span>
    </a>
  );
}

export function GodRanking({ god, role, entries, modeLabel }: {
  god: string;
  role?: string;
  /** The per-mode god rows from the tier list. */
  entries?: GodTierEntry[];
  modeLabel: string;
}) {
  const lane = godLane(role) ?? null;
  const r = useMemo(() => buildGodRanking(entries, god, lane), [entries, god, lane]);

  if (!r) {
    return (
      <section aria-labelledby="god-rank-h" className="max-w-[68ch]">
        <h2 id="god-rank-h" className="font-display text-title font-bold text-ink">
          {god} isn&rsquo;t ranked in {modeLabel}
        </h2>
        <p className="mt-2 text-body leading-relaxed text-muted">
          The model hasn&rsquo;t scored {god} for this mode, so there&rsquo;s no placement to report
          and nothing to compare against the community. That&rsquo;s a coverage gap in the tier
          list, not a verdict.
        </p>
        <a href={toHash.tiers()} className="press mt-3 inline-block rounded-sm py-1.5 text-label font-medium text-blue hover:underline">
          See the full tier list →
        </a>
      </section>
    );
  }

  const { entry } = r;
  const pct = r.overall != null ? topPercent(r.overall, r.scored) : null;

  return (
    <section aria-labelledby="god-rank-h">
      <header className="border-b border-line pb-4">
        <h2 id="god-rank-h" className="max-w-[30ch] text-balance font-display text-title font-bold leading-tight text-ink">
          {r.unranked ? (
            <>The model puts {god} at <span className="text-gold">{entry.tier_ours ?? "no tier"}</span>.
              The community hasn&rsquo;t rated {god}.</>
          ) : r.agrees ? (
            <>Both put {god} at <span className="text-gold">{entry.tier_ours}</span>.</>
          ) : (
            <>The model says <span className="text-gold">{entry.tier_ours}</span>; the community
              says <span className={divergenceClass(r.tierGap)}>{entry.tier_community}</span>.</>
          )}
        </h2>
        <p className="mt-2.5 flex flex-wrap items-baseline gap-x-4 gap-y-1 text-label text-faint">
          <span>model <span className="font-mono text-gold">{entry.ours?.toFixed(2)}</span></span>
          <span>
            community{" "}
            {r.unranked
              ? <span className="text-muted">unranked</span>
              : <span className="font-mono text-ink-soft">{entry.community!.toFixed(2)}</span>}
          </span>
          {r.delta != null && (
            <span className={divergenceClass(r.tierGap)}>
              {r.tierGap === 0 ? "same tier" : r.tierGap! > 0 ? "we rank higher" : "the meta ranks higher"}{" "}
              <span className="font-mono">{deltaText(r.delta)}</span>
            </span>
          )}
          <span>{modeLabel}</span>
        </p>
      </header>

      <div className="mt-5 flex flex-col gap-6 lg:flex-row">
        <div className="min-w-0 flex-1 lg:max-w-[520px]">
          <h3 className={eyebrow}>Who {god} sits between</h3>
          <p className="mt-1.5 max-w-[64ch] text-small leading-relaxed text-muted">
            By the model&rsquo;s score, across every god it rated in {modeLabel}.
          </p>
          <div className="mt-2.5">
            <NeighbourRow label="Above" n={r.above} subject={god} />
            <div className="flex items-baseline justify-between gap-3 border-t border-line bg-bg1 py-2 pl-2 pr-1">
              <span className="text-small text-gold">{god}</span>
              <span className="font-mono text-label text-gold">{entry.ours?.toFixed(2)}</span>
            </div>
            <NeighbourRow label="Below" n={r.below} subject={god} />
          </div>
        </div>

        <div className="flex flex-col gap-4 lg:w-[300px] lg:flex-none lg:border-l lg:border-line lg:pl-6">
          <div>
            <h3 className={eyebrow}>Standing</h3>
            <dl className="mt-2 flex flex-col">
              <div className="flex items-baseline justify-between gap-3 border-t border-line py-1.5">
                <dt className="text-small text-muted">Overall</dt>
                <dd className="text-small text-ink-soft">
                  <span className="font-mono">{r.overall}</span> of{" "}
                  <span className="font-mono">{r.scored}</span>
                  {pct != null && <span className="text-faint"> · top <span className="font-mono">{pct}%</span></span>}
                </dd>
              </div>
              {r.band && (
                <div className="flex items-baseline justify-between gap-3 border-t border-line py-1.5">
                  <dt className="text-small text-muted">In band {r.band}</dt>
                  <dd className="text-small text-ink-soft">
                    <span className="font-mono">{r.inBand}</span> of{" "}
                    <span className="font-mono">{r.bandSize}</span>
                  </dd>
                </div>
              )}
              {r.lane ? (
                <div className="flex items-baseline justify-between gap-3 border-t border-line py-1.5">
                  <dt className={`text-small ${laneTextClass(r.lane)}`}>In {r.lane}</dt>
                  <dd className="text-small text-ink-soft">
                    <span className="font-mono">{r.inLane}</span> of{" "}
                    <span className="font-mono">{r.laneSize}</span>
                  </dd>
                </div>
              ) : (
                <div className="border-t border-line py-1.5">
                  <p className="text-small text-muted">
                    No lane on record for {god}, so there&rsquo;s no lane standing to give.
                  </p>
                </div>
              )}
            </dl>
          </div>

          <p className="max-w-[46ch] text-small leading-relaxed text-muted">
            {r.unranked
              ? <>SmiteBrain hasn&rsquo;t rated {god} in {modeLabel}, so the model&rsquo;s placement
                  stands alone here — it isn&rsquo;t agreement.</>
              : r.agrees
                ? <>The two sources land on the same letter for {god}. Most of the argument on this
                    site is elsewhere.</>
                : <>Tier letters are the verdict; the raw gap can point the other way near a band
                    boundary, which is why the colour above follows the letters.</>}
          </p>

          <a href={toHash.tiers()} className="press rounded-sm py-1.5 text-label font-medium text-blue hover:underline">
            See every placement →
          </a>
        </div>
      </div>
    </section>
  );
}
