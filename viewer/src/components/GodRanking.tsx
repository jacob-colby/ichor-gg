/* THESIS: this lens owns "where does this god sit, and on what evidence?"
 * The tier list answers that for all 87 at once; from a god's own page there
 * was no way to ask it about that god. Everything here derives from the same
 * tierlist slice the tier list reads, so the two can't drift.
 * It used to own a comparison — our placement against the community's, with the
 * gap as the headline. That gap did not survive measurement, so the page now
 * reports the record and how much play it rests on.
 * OWN-WORLD: Arena Night. Hairline rules, mono for figures, gold on the tier
 * letter; `under` marks the one editorial call left, rarely played.
 * STORY: a player reads where the god actually sits, sees how sure that is, and
 * sees who it is next to.
 * FIRST VIEWPORT: the placement in words with its sample, then the neighbours,
 * then the band and lane standing.
 */
import { useMemo } from "react";
import type { GodTierEntry } from "../types";
import { buildGodRanking, topPercent, type Neighbour } from "../lib/godRanking";
import { godLane, laneTextClass } from "../lib/roleAccent";
import { rateText, matchesText } from "../lib/standings";
import { toHash } from "../lib/useHashRoute";

const eyebrow = "font-mono text-label uppercase tracking-[0.1em] text-faint";

/** One god next to this one in the standings. */
function NeighbourRow({ label, n, subject }: {
  label: string;
  n?: Neighbour;
  subject: string;
}) {
  if (!n) {
    return (
      <div className="flex items-baseline justify-between gap-3 border-t border-line py-2">
        <span className="text-small text-faint">{label}</span>
        <span className="text-small text-muted">
          nothing — {subject} is the {label === "Above" ? "highest" : "lowest"}-placed god measured
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
        <span className="shrink-0 font-mono text-label text-ink-soft">{rateText(n.winRate)}</span>
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
          {god} isn&rsquo;t in the {modeLabel} standings
        </h2>
        <p className="mt-2 text-body leading-relaxed text-muted">
          This mode has no row for {god} at all, so there&rsquo;s no placement to report. That&rsquo;s
          a coverage gap, not a verdict.
        </p>
        <a href={toHash.tiers()} className="press mt-3 inline-block rounded-sm py-1.5 text-label font-medium text-blue hover:underline">
          See the full tier list →
        </a>
      </section>
    );
  }

  const { entry } = r;

  // No sample means no placement. Said plainly rather than drawn as a row of
  // dashes — and it is the whole roster outside Conquest, which publishes no
  // results at all.
  if (r.unmeasured) {
    return (
      <section aria-labelledby="god-rank-h" className="max-w-[68ch]">
        <h2 id="god-rank-h" className="font-display text-title font-bold text-ink">
          {god} isn&rsquo;t measured in {modeLabel}
        </h2>
        <p className="mt-2 text-body leading-relaxed text-muted">
          There aren&rsquo;t enough tracked {modeLabel} matches to place {god} with any confidence,
          so this page gives no tier rather than a made-up one. This site used to fill that gap
          with its own score; that score measured &minus;0.12 against real god strength, so a blank
          is the more honest answer. The build for {god} is unaffected.
        </p>
        <a href={toHash.tiers()} className="press mt-3 inline-block rounded-sm py-1.5 text-label font-medium text-blue hover:underline">
          See every placement →
        </a>
      </section>
    );
  }

  const pct = r.overall != null ? topPercent(r.overall, r.scored) : null;

  return (
    <section aria-labelledby="god-rank-h">
      <header className="border-b border-line pb-4">
        <h2 id="god-rank-h" className="max-w-[30ch] text-balance font-display text-title font-bold leading-tight text-ink">
          {god} wins <span className="text-gold">{rateText(entry.win_rate)}</span> of{" "}
          {matchesText(entry.matches)} tracked matches.
        </h2>
        <p className="mt-2.5 flex flex-wrap items-baseline gap-x-4 gap-y-1 text-label text-faint">
          {entry.tier_score && (
            <span>tier <span className="font-mono text-gold">{entry.tier_score}</span></span>
          )}
          {typeof entry.play_share === "number" && (
            <span>picked in <span className="font-mono text-ink-soft">{rateText(entry.play_share)}</span> of matches</span>
          )}
          <span>{modeLabel}</span>
        </p>
      </header>

      <div className="mt-5 flex flex-col gap-6 lg:flex-row">
        <div className="min-w-0 flex-1 lg:max-w-[520px]">
          <h3 className={eyebrow}>Who {god} sits between</h3>
          <p className="mt-1.5 max-w-[64ch] text-small leading-relaxed text-muted">
            Ordered by the lower bound of each god&rsquo;s win rate, so a thin sample can&rsquo;t
            leapfrog a thick one. Rates shown are the raw ones.
          </p>
          <div className="mt-2.5">
            <NeighbourRow label="Above" n={r.above} subject={god} />
            <div className="flex items-baseline justify-between gap-3 border-t border-line bg-bg1 py-2 pl-2 pr-1">
              <span className="text-small text-gold">{god}</span>
              <span className="font-mono text-label text-gold">{rateText(entry.win_rate)}</span>
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
            Placement comes from match results only. Nothing this site models — not the gold-value
            fit, not the build it suggests — goes into the order.
          </p>

          <a href={toHash.tiers()} className="press rounded-sm py-1.5 text-label font-medium text-blue hover:underline">
            See every placement →
          </a>
        </div>
      </div>
    </section>
  );
}
