/** Method (`#/method`): how the model decides, as a page you read.
 *
 * The one route where decimals belong on screen, because they ARE the method:
 * the blend weights and the fitted gold a point. Each is labelled with what it
 * measures where it appears ("weight 0.35 of the score", "18.91g a point"),
 * never left bare. Everything else is Sofia Sans at a reading measure.
 *
 * Product truth kept from the old Method page: every figure is read from the
 * shipped index (`method`, `item_gold_values`, the item list) and nothing is
 * restated in TSX; a price fitted from fewer than three items is marked thin
 * rather than presented as solid; the intercept is a base price, never a stat
 * row; and the limits are written down as specific, directional gaps.
 *
 * One passage was rewritten rather than restyled: the old page called "the
 * disagreement between [model and community]" the product. PRODUCT.md retired
 * that positioning on 2026-08-05 — what ichor claims is the working and the
 * honesty, never that it out-ranks the community — so the tension is now
 * stated in those terms. */
import { useMemo, type ReactNode } from "react";
import type { Item, MethodData } from "../../types";
import { statKey, INTERCEPT_KEY } from "../../lib/itemFilters";
import { PageHead, Em } from "./PageParts";
import { PASSIVE_LABEL } from "./receipt";

const THIN_EVIDENCE = 3;

/** What each shipped `price_*` switch prices, in the order the page lists them.
 *  Read against `method.pricing`, so the page names exactly the classes the fit
 *  prices — it used to restate them here and named two while four were on. */
const PRICED_CLASSES: [string, string][] = [
  ["price_crit_multipliers", "a crit multiplier as the critical chance it is worth"],
  ["price_conversions", "a stat conversion against a typical build"],
  ["price_adaptive", "an Adaptive Stat grant as one of the two stats it offers"],
  ["price_stacks", "a stack that reaches its cap and keeps it"],
  ["price_stat_multipliers", "a percent-of-all-stats bonus against a typical five items"],
  ["price_on_hit", "flat on-hit damage as attack damage"],
  ["price_passive_sim", "a passive the fight simulation can run, at what it adds there"],
];
const COUNT_WORD = ["No", "One", "Two", "Three", "Four", "Five", "Six", "Seven"];

function Section({ id, title, children }: { id: string; title: string; children: ReactNode }) {
  return (
    <section aria-labelledby={id} className="scroll-mt-20 border-t border-line pt-6">
      <h2 id={id} className="font-cond text-head font-extrabold text-ink">{title}</h2>
      <div className="mt-3 flex flex-col gap-4">{children}</div>
    </section>
  );
}

/** A figure that is part of the method, set tabular in ink. */
const N = ({ children }: { children: ReactNode }) => <span className="num font-semibold text-ink">{children}</span>;

export function MethodPage({ method, goldValues, items, godCount }: {
  method?: MethodData;
  goldValues: Record<string, number>;
  items: Item[];
  godCount: number;
}) {
  const s = method?.signals;
  const counts = useMemo(() => {
    const c: Record<string, number> = {};
    for (const it of items) {
      // An item counts once per column, whether it carries the stat on its
      // stat line or the fit credits it through the passive (`priced_passive`).
      const cols = new Set(Object.entries(it.stats ?? {}).map(([stat, raw]) => statKey(stat, String(raw))));
      for (const k of Object.keys(it.efficiency?.priced_passive ?? {})) cols.add(k);
      for (const k of cols) c[k] = (c[k] ?? 0) + 1;
    }
    return c;
  }, [items]);
  const priced = useMemo(() => Object.entries(goldValues).filter(([k]) => k !== INTERCEPT_KEY).sort((a, b) => b[1] - a[1]), [goldValues]);
  const base = goldValues[INTERCEPT_KEY];
  const simulated = priced.filter(([k]) => k in PASSIVE_LABEL);
  const pricedClasses = method?.pricing ? PRICED_CLASSES.filter(([k]) => method.pricing![k]).map(([, words]) => words) : null;
  const scored = items.filter((it) => it.efficiency).length;
  const passivePriced = items.filter((it) => it.efficiency?.priced_passive).length;
  const ours = s ? s.efficiency + s.fit : 0;
  const theirs = s ? s.win + s.pick : 0;
  const qEff = ours ? s!.efficiency / ours : 0;
  const qFit = ours ? s!.fit / ours : 0;
  const signals = s ? [
    { label: "Gold efficiency", whose: "Ichor's arithmetic", w: s.efficiency },
    { label: "Fit for this god", whose: "Ichor's arithmetic", w: s.fit },
    { label: "Community win rate", whose: "The community's record", w: s.win },
    { label: "Community pick rate", whose: "The community's record", w: s.pick },
  ] : [];
  const toc = [
    ...(s ? [{ id: "blend-h", title: "Four signals, one score" }] : []),
    { id: "gold-h", title: "Is the item worth its gold?" },
    { id: "fit-h", title: "Does it suit this god?" },
    { id: "win-h", title: "Is it actually winning?" },
    ...(s ? [{ id: "builds-h", title: "The model, the community, and the measured gap" }] : []),
    { id: "limits-h", title: "What this model cannot see" },
  ];
  const max = Math.max(...signals.map((x) => x.w), 0.0001);

  return (
    <div className="mx-auto w-full max-w-[1240px] px-4 pb-16 lg:grid lg:grid-cols-[minmax(0,68ch)_minmax(0,1fr)] lg:gap-16 lg:px-6">
      <article className="mx-auto max-w-[68ch] text-[17px] leading-[1.6] text-muted lg:mx-0">
        <PageHead title="Method" testId="method-head">
          {s ? (
            <p>Every item is scored for every god on four signals: <Em>two are arithmetic Ichor does itself</Em>, two are what people actually win with and pick.</p>
          ) : (
            <p>How the model decides.</p>
          )}
        </PageHead>
        <p className="mt-3">
          The numbers on this page are the ones the pipeline used to build the page you were just on. Decimals here are the
          method itself, so each one says what it measures.
        </p>

        <div className="mt-8 flex flex-col gap-10">
          {s && (
            <Section id="blend-h" title="Four signals, one score">
              <ul data-testid="blend" className="border-b border-line">
                {signals.map((x) => (
                  <li key={x.label} className="grid grid-cols-[minmax(0,1fr)_auto] items-baseline gap-x-4 border-t border-line py-2.5">
                    <span>
                      <span className="block text-ink">{x.label}</span>
                      <span className="block text-cap text-quiet">{x.whose}</span>
                    </span>
                    <span className="text-right text-note">weight <N>{x.w.toFixed(2)}</N> of the score</span>
                    <span aria-hidden="true" className="col-span-2 mt-1.5 block h-1 rounded-full bg-surface-3">
                      <span className="block h-1 rounded-full bg-ink-soft" style={{ width: `${(x.w / max) * 100}%` }} />
                    </span>
                  </li>
                ))}
              </ul>
              <p>
                Efficiency and fit never see a win rate; together they carry weight <N>{ours.toFixed(2)}</N>. Win and pick
                rate are the community&rsquo;s, and carry the other <N>{theirs.toFixed(2)}</N>.
              </p>
              <p>
                <Em>This is the honest tension in the tool.</Em> Half of the blended score is the community&rsquo;s own
                record, so a blended build cannot claim to know better than the community, and Ichor doesn&rsquo;t. What it
                claims is the working: the model&rsquo;s half is shown on its own as Ichor&rsquo;s main six, the
                community&rsquo;s six sits one tap away, and the comparison between them says which is ahead and what it
                could not measure.
              </p>
            </Section>
          )}

          <Section id="gold-h" title="Is the item worth its gold?">
            <p>
              Nothing in the game says what a point of Strength costs, so Ichor works it out: it fits every item&rsquo;s
              price against the stats it carries, across all <N>{items.length}</N> items at once, and reads off the
              marginal gold value of each stat. An item&rsquo;s <Em>efficiency</Em> is the gap between what it costs and
              what that fit says its stats are worth &mdash; and, where the fit can put a number on it, its passive:
              cheaper is <Em>underpriced</Em>, dearer is <Em>overpriced</Em>.
            </p>
            {base != null && (
              <p>
                The fit also charges every item a base price of <N>{Math.round(base).toLocaleString("en-US")}g</N> before a
                single stat is counted &mdash; roughly what a finished item costs for being a finished item. It is why a
                receipt that listed only stat rows would never add up to the sticker price, and why every receipt on the
                Items page starts with it.
              </p>
            )}
            {priced.length > 0 && (
              <div className="overflow-x-auto">
                <table className="w-full min-w-[20rem] text-note" data-testid="gold-table">
                  <caption className="pb-2 text-left font-cond text-[18px] font-bold uppercase text-ink-soft">Fitted gold a point</caption>
                  <thead>
                    <tr className="border-b border-line-strong text-cap text-quiet">
                      <th scope="col" className="py-1.5 text-left font-normal">Stat</th>
                      <th scope="col" className="py-1.5 text-right font-normal">Gold a point</th>
                      <th scope="col" className="py-1.5 text-right font-normal">Items carrying it</th>
                    </tr>
                  </thead>
                  <tbody>
                    {priced.map(([stat, value]) => {
                      const n = counts[stat] ?? 0;
                      const thin = n > 0 && n < THIN_EVIDENCE;
                      return (
                        <tr key={stat} className="border-b border-line">
                          <th scope="row" className="py-2 text-left font-normal text-ink-soft">{PASSIVE_LABEL[stat] ?? stat}</th>
                          <td className="num py-2 text-right font-semibold text-ink">{value.toFixed(2)}g</td>
                          <td className="num py-2 text-right text-muted">
                            {n}{thin && <span className="ml-1.5 text-cap font-semibold text-ink-soft">thin</span>}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            )}
            {simulated.length > 0 && (
              <p data-testid="passive-rows">
                The <Em>Passive</Em> rows are not stats. They price what an item&rsquo;s passive adds in a simulated
                fight, measured across the shipped builds that hold the item: the damage it adds, and the effective health
                it adds against each damage type. Ichor prices <N>{passivePriced}</N> of its <N>{scored}</N> priced items
                partly on their passive, and every receipt on the Items page lists those rows.
                {simulated.some(([, v]) => v === 0) && <> A row at <N>0.00g</N> is one the fit found nothing to pay for.</>}
              </p>
            )}
            <p>
              Read the last column before trusting a price: a stat carried by one or two items has a coefficient the data
              can&rsquo;t really support, and it is marked <Em>thin</Em> rather than quietly presented as solid. A
              stat&rsquo;s unit is part of its identity &mdash; penetration ships both flat and as a percentage, and they
              are priced in separate rows, because regressed together they came out at one averaged price that credited
              every flat-penetration item with value it does not have.
            </p>
          </Section>

          <Section id="fit-h" title="Does it suit this god?">
            <p>
              <Em>Fit</Em> asks whether an item carries the stats this god turns into damage or survivability. It starts
              from what the role wants, then blends in what the god&rsquo;s own abilities scale off
              {method?.kit_blend != null && (
                <> &mdash; the kit carries weight <N>{method.kit_blend.toFixed(2)}</N> against the role&rsquo;s{" "}
                  <N>{(1 - method.kit_blend).toFixed(2)}</N></>
              )}. A god whose abilities scale off Intelligence is scored differently from one who only wants raw Strength,
              even in the same lane.
            </p>
            <p>
              <Em>Its real limit:</Em> fit asks whether an item <i>has</i> a stat, not how much of it. An item with 5
              Strength and one with 80 score the same here; magnitude reaches the model only through gold efficiency.
            </p>
          </Section>

          <Section id="win-h" title="Is it actually winning?">
            <p>
              Win rate and pick rate come from SmiteBrain&rsquo;s high-elo sample. Win rate carries almost all of that
              weight{s && <> (<N>{s.win.toFixed(2)}</N> against pick rate&rsquo;s <N>{s.pick.toFixed(2)}</N>)</>},
              deliberately: popularity is not evidence, and an item everyone builds out of habit should not outrank one
              that quietly wins.
            </p>
            <p>
              Small samples are held to the same standard. Where community records are compared, Ichor uses the lower
              bound of a Wilson interval rather than the raw rate, so an item that won two of three games is not treated as
              a 67% winner. The tier list ranks gods the same way.
            </p>
            <p>
              This data exists only for <Em>Conquest</Em>. Joust and Arena are scored on efficiency and fit alone, and
              say so on every page rather than borrowing Conquest&rsquo;s numbers to fill the gap.
            </p>
          </Section>

          {s && (
            <Section id="builds-h" title="The model, the community, and the measured gap">
              <p>
                Because the blend is half community, the model&rsquo;s half is also shown on its own. The{" "}
                <Em>Model</Em> build &mdash; Ichor&rsquo;s main six on every god page &mdash; is the score with the
                community switched off: efficiency and fit renormalised to weights <N>{qEff.toFixed(2)}</N> and{" "}
                <N>{qFit.toFixed(2)}</N>. The <Em>Community</Em> build is what people run. The <Em>Hybrid</Em> keeps the
                model&rsquo;s strongest picks and lets real evidence fill the slots where the model has no strong
                preference, naming the reason for every swap.
              </p>
              <p>
                An item is flagged <Em>underrated</Em> for a god when it scores in the top{" "}
                {method?.underrated?.top_quality_frac != null && <N>{Math.round(method.underrated.top_quality_frac * 100)}%</N>}{" "}
                on efficiency and fit while almost nobody builds it
                {method?.underrated?.max_pick != null && <> (pick rate at or below <N>{Math.round(method.underrated.max_pick * 100)}%</N>)</>}.
                That comparison is community-free on purpose: it would be circular if the community were in both halves of it.
              </p>
            </Section>
          )}

          <Section id="limits-h" title="What this model cannot see">
            <p>These are real gaps, not disclaimers. Each one makes the model wrong in a predictable direction.</p>
            <ul className="flex flex-col gap-3 border-l border-line pl-4" data-testid="limits">
              <li>
                <Em>It is a filter, not a ranker.</Em> Measured against random picks it finds items the community actually
                builds far more often than chance, but its ordering inside that set is indistinguishable from guessing.
                Trust &ldquo;these six are sensible&rdquo; more than &ldquo;this order is right&rdquo;.
              </li>
              <li>
                <Em>Most item passives are still unpriced.</Em>{" "}
                {pricedClasses && pricedClasses.length > 0 && (
                  <>{pricedClasses.length === 1 ? "One class is" : `${COUNT_WORD[pricedClasses.length] ?? pricedClasses.length} classes are`}: {pricedClasses.join("; ")}. </>
                )}
                {pricedClasses?.length ? "Everything else is" : "They are"} prose with no numbers extracted, priced as if it were free &mdash; so passive-heavy
                items read overpriced more often than they should.
                {!method?.pricing?.price_passives && <> Pricing every unconditional stat grant at once was tried, measured, and made the model worse.</>}
              </li>
              <li>
                <Em>The damage model is exact, and only the draft uses it.</Em> Damage through a given amount of
                protection is computed to 0.0% worst-case error against in-game readings. It decides which items rise
                against a tanky team; it does not feed the base build, where it was measured and made things worse.
              </li>
              <li><Em>Fit ignores magnitude.</Em> Stated above; it is the single biggest source of imprecision in a per-god score.</li>
              <li>
                <Em>The community sample is one mode and one skill band.</Em> Conquest, high elo. If you play something
                else, the two community signals describe somebody else&rsquo;s game.
              </li>
              <li>
                <Em><N>{godCount}</N> gods and <N>{items.length}</N> items move every patch.</Em> Everything above is
                recomputed from a scrape; between refreshes the figures are as old as the last one.
              </li>
            </ul>
          </Section>
        </div>
      </article>

      {/* Desktop: the page's sections, in reach while reading. Buttons, not
          `#id` links: the hash is the router's, and a fragment would navigate. */}
      <nav aria-label="Sections" className="hidden lg:block">
        <ul className="sticky top-[96px] mt-[200px] border-l border-line">
          {toc.map((t) => (
            <li key={t.id}>
              <button type="button" onClick={() => document.getElementById(t.id)?.scrollIntoView({ block: "start" })}
                className="press flex min-h-11 items-center pl-4 text-left text-note text-muted hover:text-ink">
                {t.title}
              </button>
            </li>
          ))}
        </ul>
      </nav>
    </div>
  );
}
