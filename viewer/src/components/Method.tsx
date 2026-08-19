import { useMemo } from "react";
import type { Item, MethodData } from "../types";
import { statKey, INTERCEPT_KEY } from "../lib/itemFilters";

/**
 * How the model decides, stated in the model's own numbers.
 *
 * Every figure on this page is read from the shipped index — the signal
 * weights, the fitted gold prices, the item counts behind each one. Nothing is
 * restated in TSX, because a method page that describes a blend the pipeline
 * stopped using is worse than no method page at all.
 *
 * It is also where the model's limits are written down. Those are easy to
 * leave out and they are the part a reader most needs: a build tool that
 * cannot see most item passives will be systematically wrong about
 * passive-heavy items, and someone comparing our verdict to their own
 * experience deserves to know that before they conclude the model is simply
 * bad.
 *
 * The limits list is a claim about the code and goes stale the same way a
 * weights table would. Two entries here already had: crit multipliers and stat
 * conversions are both priced now, and `combat.py` is exact to 0.0% and feeds
 * the draft, while this page still said neither existed. Re-read it whenever a
 * pricing flag flips.
 */

/** Stats fitted from very few items get a coefficient the data can't really
 *  support. Not hidden — labelled, so a reader can discount it themselves. */
const THIN_EVIDENCE = 3;

function Bar({ parts }: { parts: { label: string; weight: number; className: string }[] }) {
  const total = parts.reduce((s, p) => s + p.weight, 0) || 1;
  return (
    <div>
      <div className="flex h-3 w-full overflow-hidden rounded-sm border border-line" role="presentation">
        {parts.map((p) => (
          <div key={p.label} className={p.className} style={{ width: `${(p.weight / total) * 100}%` }} />
        ))}
      </div>
      <ul className="mt-2 flex flex-wrap gap-x-4 gap-y-1">
        {parts.map((p) => (
          <li key={p.label} className="inline-flex items-center gap-1.5 text-label text-muted">
            <span className={`inline-block h-2 w-2 rounded-full ${p.className}`} />
            {p.label}
            <span className="font-mono tabular-nums text-ink-soft">{p.weight.toFixed(2)}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

function Section({ eyebrow, title, children }: {
  eyebrow: string; title: string; children: React.ReactNode;
}) {
  return (
    <section className="border-t border-line pt-6">
      <p className="text-label uppercase tracking-[0.08em] text-faint">{eyebrow}</p>
      <h2 className="mt-1 font-display text-title font-bold text-ink">{title}</h2>
      <div className="mt-3 flex flex-col gap-3 text-body leading-relaxed text-muted">{children}</div>
    </section>
  );
}

export function Method({ method, goldValues, items, godCount }: {
  method?: MethodData;
  goldValues: Record<string, number>;
  items: Item[];
  godCount: number;
}) {
  const signals = method?.signals;

  /** How many items carry each priced column — the evidence behind a price.
   *  Derived here rather than shipped so it can never disagree with the item
   *  list the same page is rendering. */
  const statCounts = useMemo(() => {
    const counts: Record<string, number> = {};
    for (const it of items) {
      for (const [stat, raw] of Object.entries(it.stats ?? {})) {
        counts[statKey(stat, String(raw))] = (counts[statKey(stat, String(raw))] ?? 0) + 1;
      }
    }
    return counts;
  }, [items]);

  const priced = useMemo(
    () => Object.entries(goldValues)
      .filter(([k]) => k !== INTERCEPT_KEY)
      .sort((a, b) => b[1] - a[1]),
    [goldValues],
  );

  const base = goldValues[INTERCEPT_KEY];
  const math = signals ? signals.efficiency + signals.fit : 0;
  const meta = signals ? signals.win + signals.pick : 0;
  // The model build's own blend: efficiency and fit renormalized with the meta
  // switched off. Derived from the same weights, never a second constant.
  const qEff = math ? signals!.efficiency / math : 0;
  const qFit = math ? signals!.fit / math : 0;

  return (
    <div className="mx-auto w-full max-w-[1440px] p-4 sm:p-6">
      <header className="pb-6">
        <h1 className="max-w-[26ch] text-balance font-display text-display font-bold leading-[1.12] tracking-[-0.01em] text-ink">
          {signals ? (
            <>Half of an item&rsquo;s score is{" "}
              <span className="text-gold">math</span>. Half is what the community wins with.
            </>
          ) : (
            <>How the model decides.</>
          )}
        </h1>
        <p className="mt-3 max-w-[74ch] text-body leading-relaxed text-muted">
          Every buildable item is scored for every god, on four signals. Two are arithmetic we do
          ourselves and two come from what people actually play. The numbers below are the ones
          the pipeline used to build the page you were just on.
        </p>
      </header>

      <div className="flex flex-col gap-8">
        {signals && (
          <Section eyebrow="The blend" title="Four signals, one score">
            <div className="max-w-[74ch]">
              <Bar parts={[
                { label: "Gold efficiency", weight: signals.efficiency, className: "bg-gold" },
                { label: "Community win rate", weight: signals.win, className: "bg-premium" },
                { label: "Community pick rate", weight: signals.pick, className: "bg-line-strong" },
                { label: "Fit for this god", weight: signals.fit, className: "bg-under" },
              ]} />
            </div>
            <p>
              Gold efficiency and fit are ours — they never see a win rate. Together they are{" "}
              <b className="font-mono tabular-nums text-ink">{math.toFixed(2)}</b> of the score.
              Win and pick rate are the community&rsquo;s, and they are the other{" "}
              <b className="font-mono tabular-nums text-ink">{meta.toFixed(2)}</b>.
            </p>
            <p className="rounded-md border border-line bg-bg2 p-3 text-small">
              <b className="text-ink">This is the honest tension in the tool.</b> A site whose whole
              claim is that the community is sometimes wrong scores its items half on the
              community&rsquo;s own data. We don&rsquo;t resolve that by picking a side — we show
              both, and the disagreement between them is the product.
            </p>
          </Section>
        )}

        <Section eyebrow="Signal one" title="Is the item worth its gold?">
          <p>
            Nothing in the game tells us what a point of Strength costs. So we work it out: fit
            every item&rsquo;s price against the stats it carries, across all{" "}
            <b className="text-ink">{items.length}</b> of them at once, and read off the marginal
            gold value of each stat. An item&rsquo;s <b className="text-ink">efficiency</b> is the
            gap between what it costs and what that fit says its stats are worth — cheaper than
            modelled is <b className="text-under">undervalued</b>, dearer is{" "}
            <b className="text-premium">premium</b>.
          </p>
          {base != null && (
            <p>
              The fit also charges every item{" "}
              <b className="font-mono tabular-nums text-ink">{Math.round(base)}g</b> before a single
              stat is counted. That is not a bug — it is roughly what a finished item costs for
              being a finished item, and it is why a receipt listing only stat rows never adds up
              to the sticker price.
            </p>
          )}
          {priced.length > 0 && (
            <div className="max-w-[74ch] overflow-x-auto">
              <table className="w-full min-w-[26rem] border-collapse text-small">
                <caption className="pb-2 text-left text-label uppercase tracking-[0.08em] text-faint">
                  Fitted gold per point
                </caption>
                <thead>
                  <tr className="border-b border-line text-label uppercase tracking-[0.06em] text-faint">
                    <th scope="col" className="py-1.5 text-left font-normal">Stat</th>
                    <th scope="col" className="py-1.5 text-right font-normal">Gold / point</th>
                    <th scope="col" className="py-1.5 text-right font-normal">Items</th>
                  </tr>
                </thead>
                <tbody>
                  {priced.map(([stat, value]) => {
                    const n = statCounts[stat] ?? 0;
                    const thin = n > 0 && n < THIN_EVIDENCE;
                    return (
                      <tr key={stat} className="border-b border-line/60">
                        <td className="py-1.5 text-ink-soft">{stat}</td>
                        <td className="py-1.5 text-right font-mono tabular-nums text-ink">{value.toFixed(2)}</td>
                        <td className="py-1.5 text-right font-mono tabular-nums text-muted">
                          {n}
                          {thin && <span className="ml-1.5 text-label text-faint">thin</span>}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          )}
          <p className="text-small">
            Read the <b className="text-ink">Items</b> column before trusting a price: a stat
            carried by one or two items has a coefficient the data can&rsquo;t really support, and
            it is marked <b className="text-ink">thin</b> rather than quietly presented as solid.
          </p>
          <p className="text-small">
            A stat&rsquo;s unit is part of its identity. Penetration ships both flat and as a
            percentage, and they are priced in separate rows above — regressed together they came
            out at one averaged price, which credited every flat-penetration item with gold value
            it does not have.
          </p>
        </Section>

        <Section eyebrow="Signal two" title="Does it suit this god?">
          <p>
            <b className="text-ink">Fit</b> asks whether an item carries the stats this particular
            god turns into damage or survivability. It starts from what the role wants, then blends
            in what the god&rsquo;s own abilities actually scale off
            {method?.kit_blend != null && (
              <> — the kit is weighted{" "}
                <b className="font-mono tabular-nums text-ink">{method.kit_blend.toFixed(2)}</b>{" "}
                against the role&rsquo;s{" "}
                <b className="font-mono tabular-nums text-ink">{(1 - method.kit_blend).toFixed(2)}</b></>
            )}
            . A god whose abilities scale off Intelligence is scored differently from one who only
            wants raw Strength, even in the same lane.
          </p>
          <p className="rounded-md border border-line bg-bg2 p-3 text-small">
            <b className="text-ink">Its real limit:</b> fit currently asks whether an item{" "}
            <i>has</i> a stat, not how much of it. An item with 5 Strength and one with 80 score
            the same here. Magnitude reaches the model only through gold efficiency, and closing
            that gap is the next piece of work.
          </p>
        </Section>

        <Section eyebrow="Signals three and four" title="Is it actually winning?">
          <p>
            Win rate and pick rate come from SmiteBrain&rsquo;s high-elo sample. Win rate carries
            almost all of that weight
            {signals && (
              <> (<b className="font-mono tabular-nums text-ink">{signals.win.toFixed(2)}</b> against
                pick rate&rsquo;s <b className="font-mono tabular-nums text-ink">{signals.pick.toFixed(2)}</b>)</>
            )}
            , deliberately: popularity is not evidence. An item everyone builds out of habit should
            not outrank one that quietly wins.
          </p>
          <p>
            Small samples are held to the same standard. Where we compare community records we use
            the lower bound of a Wilson interval rather than the raw rate, so an item that won two
            of three games is not treated as a 67% winner.
          </p>
          <p>
            This data only exists for <b className="text-ink">Conquest</b>. Joust and Arena are
            scored on efficiency and fit alone, and say so on the page rather than borrowing
            Conquest&rsquo;s numbers to fill the gap.
          </p>
        </Section>

        {signals && (
          <Section eyebrow="Why three builds" title="The model, the community, and the argument between them">
            <p>
              Because the blend is half meta, we also show what each half says on its own. The{" "}
              <b className="text-ink">Model</b> build is the score with the community switched
              off — efficiency and fit renormalized to{" "}
              <b className="font-mono tabular-nums text-ink">{qEff.toFixed(2)}</b> /{" "}
              <b className="font-mono tabular-nums text-ink">{qFit.toFixed(2)}</b>. The{" "}
              <b className="text-ink">Community</b> build is what people run. The{" "}
              <b className="text-ink">Hybrid</b> keeps the model&rsquo;s strongest picks and lets
              real evidence fill the slots where the model has no strong preference, naming the
              reason for every swap.
            </p>
            <p>
              An item is flagged <b className="text-ink">underrated</b> for a god when it scores in
              the top{" "}
              {method?.underrated?.top_quality_frac != null && (
                <b className="font-mono tabular-nums text-ink">
                  {Math.round(method.underrated.top_quality_frac * 100)}%
                </b>
              )}{" "}
              on efficiency and fit while almost nobody builds it
              {method?.underrated?.max_pick != null && (
                <> (pick rate at or below{" "}
                  <b className="font-mono tabular-nums text-ink">
                    {Math.round(method.underrated.max_pick * 100)}%
                  </b>)</>
              )}
              . That comparison is meta-free on purpose — it is the one claim that would be
              circular if the meta were in both halves of it.
            </p>
          </Section>
        )}

        <Section eyebrow="Limits" title="What this model cannot see">
          <p>
            These are real gaps, not disclaimers. Each one makes the model wrong in a predictable
            direction, which is more useful to know than a general warning.
          </p>
          <ul className="flex max-w-[74ch] flex-col gap-2">
            <li>
              <b className="text-ink">Most item passives are still unpriced.</b> Two classes are
              not: a crit multiplier is converted to the critical chance it is worth and priced
              (Deathbringer&rsquo;s +35% reads as +14% chance), and a stat conversion is priced
              against a typical build (Transcendence&rsquo;s mana into Strength). Everything else —
              The Executioner&rsquo;s protection shred, Qin&rsquo;s Blade&rsquo;s percent-health
              damage — is prose we extract no numbers from, and is priced as if it were free, so
              those items read as <b className="text-premium">premium</b> more often than they
              should. Pricing the whole class was tried, measured, and made the model worse.
            </li>
            <li>
              <b className="text-ink">The damage model is exact, and only the draft uses it.</b>{" "}
              Ability and basic-attack damage through a given amount of protection is computed
              exactly — calibrated against in-game readings to 0.0% worst-case error, which
              overturned several published constants along the way. It decides which items rise
              against a tanky enemy comp and which fall. It does <i>not</i> feed the base build:
              as a global fit signal it was measured and it halved the gate, because it cannot
              price defence at all.
            </li>
            <li>
              <b className="text-ink">Fit ignores magnitude.</b> Stated above, repeated here
              because it is the single biggest source of imprecision in a per-god score.
            </li>
            <li>
              <b className="text-ink">The community sample is one mode and one skill band.</b>{" "}
              Conquest, high elo. If you play something else, the two meta signals describe
              somebody else&rsquo;s game — which is a good reason to read the Model build beside
              them.
            </li>
            <li>
              <b className="text-ink">{godCount} gods and {items.length} items move every patch.</b>{" "}
              Everything above is recomputed from a scrape; between patches the figures are as old
              as the last refresh.
            </li>
          </ul>
        </Section>
      </div>
    </div>
  );
}
