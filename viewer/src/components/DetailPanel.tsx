/* THESIS: this page owns one question — what does the model buy for this god,
 * and where does the meta disagree? It refuses the tabbed detail pane, because
 * tabs made the model and the community mutually exclusive when the comparison
 * between them is the entire product.
 * OWN-WORLD: Arena Night. Hairline rule-work, mono micro-labels, gold rare and
 * load-bearing (the model's own score). `under`/`premium` carry divergence,
 * exactly as on Home.
 * STORY: a player arrives from Home mid-argument. The header states the
 * model's verdict in Home's vocabulary; the ledger shows what it buys, in
 * order, against what the meta buys; every row carries its own math.
 * FIRST VIEWPORT: verdict header (model · community, tier pair, delta), then
 * the buy ledger on a cumulative-gold spine — each row showing its total
 * score, its four axes, and where the community buys the same item.
 * FORM: Buy Timeline, position 7 of the ordered list, seed key d3f94782,
 * rendered on a cumulative-gold axis because no timing data exists to render.
 */
import { useEffect, useMemo, useRef, useState } from "react";
import type {
  BuildEntry, BuildNote, CuratedBuildEntry, God, Item, SlotScore,
} from "../types";
import { isCommunityEntry, slotItemName, iconSlug, applySwap, tabLabel, orderBuilds,
  dedupeCoreAgainstModel, communityRecordedItems, splitRationale } from "../lib/builds";
import { toHash } from "../lib/useHashRoute";
import { tierLabel } from "../lib/itemFilters";
import { buildLedger, goldText, ordinal, type LedgerRow } from "../lib/ledger";
import { GodOnlyAsterisk, GodOnlyBadge } from "./GodOnlyMark";
import { BuildEditor, type MineDraft } from "./BuildEditor";
import { getMine } from "../lib/mineStore";

const VS_LABELS: Record<string, string> = {
  heavy_cc: "vs heavy CC",
  magic_heavy: "vs magic",
  physical_heavy: "vs physical",
  sustain: "vs sustain",
};

/** The four axes behind a score, named the way the app talks about them. The
 * weights that combine them into `total` aren't published, so these are shown
 * as contributions — never summed, never implied to add up. */
const AXES: { key: keyof Omit<SlotScore, "total">; label: string; help: string }[] = [
  { key: "efficiency", label: "value", help: "Gold efficiency — stats returned per gold spent" },
  { key: "win", label: "win", help: "Community win rate with this item on this god" },
  // Not the same number as the "% pick" printed beside it on the row, and the
  // difference is the point. That one is the observation — the share of all
  // tracked matches that ended holding the item. This one conditions on
  // reaching the slot, because a sixth item is otherwise divided by a
  // denominator most of which never bought a sixth item. See
  // `scoring.SLOT_REACH`.
  { key: "pick", label: "pick", help: "How often this god's players buy it, among matches that got that far" },
  { key: "fit", label: "fit", help: "How well the item's stats match this god's kit" },
];

/** Whether `win` and `pick` on one row are a measurement, and if not, why not.
 *
 * F2. There are two different absences behind the same pair of numbers and
 * PRODUCT.md Principle 3 forbids rendering them the same way as a measurement:
 *  - `mode-unmeasured` — Joust and Arena ship no community entry at all.
 *  - `item-unmeasured` — the mode has one, but it carries no record of THIS
 *    item on THIS god. 236 of the 582 Conquest core rows in the shipped index.
 *    These used to print `win 0.56 · pick 0.00`, and the whole of Medusa’s
 *    core read as six items measured at the same win rate when in fact none of
 *    the six had ever been measured. */
type AxisState = "measured" | "mode-unmeasured" | "item-unmeasured";

interface DetailPanelProps {
  god: string;
  godData?: God;
  items: Item[];
  builds: BuildNote[];
  mode: string;
  onModeChange: (mode: string) => void;
  /** Mode display order from the pipeline, so the strip isn't ordered by
   *  whatever the build filenames sorted to. */
  modeOrder?: string[];
  starters?: { base: string; upgrade: string }[];
  onReload?: () => void;
  /** Controlled by App — the portrait carries the toggle now, so this panel
   *  reads the state rather than owning it. Defaults keep the component
   *  usable standalone in tests. */
  aspectOn?: boolean;
  onAspectChange?: (on: boolean) => void;
}

/** Item art with a real fallback — one cache-bust retry, then the item's
 * initial, never a hole in the row. State-based rather than imperative so a
 * different item landing at the same index can't inherit a hidden node. */
function ItemIcon({ name, className }: { name: string; className: string }) {
  const [tries, setTries] = useState(0);
  if (tries > 1) {
    return (
      <span aria-hidden="true"
        className={`flex flex-none items-center justify-center rounded-sm bg-bg3 font-display text-label font-bold text-faint ${className}`}>
        {name.slice(0, 1)}
      </span>
    );
  }
  return (
    <img
      src={`/icons/${iconSlug(name)}.png${tries ? "?r=1" : ""}`}
      alt=""
      loading="lazy"
      onError={() => setTries((t) => t + 1)}
      className={`flex-none rounded-sm bg-bg2 object-cover ${className}`}
    />
  );
}

function ScoreBar({ label, value, help }: { label: string; value: number; help?: string }) {
  return (
    <div className="flex items-center gap-2">
      <span className="w-12 shrink-0 text-label text-muted" title={help}>{label}</span>
      <div className="h-1.5 min-w-0 flex-1 rounded-sm bg-bg3">
        <div className="h-1.5 rounded-sm bg-gold" style={{ width: `${Math.round(Math.min(Math.max(value, 0), 1) * 100)}%` }} />
      </div>
      <span className="w-8 shrink-0 text-right font-mono text-micro text-ink">{value.toFixed(2)}</span>
    </div>
  );
}

/** The score decomposition, with the composite the model actually ranks by as
 * its headline. `total` used to be dropped here, which left four components
 * with no weights, no sum, and nothing to check them against.
 *
 * The row already prints these four numbers, so the bars here earn their place
 * by showing relative magnitude — and the block adds what the row can't fit:
 * what the community did with the same item. */
function WhyScoreBlock({ score, axisState, meta }: {
  score: SlotScore;
  axisState: AxisState;
  meta?: { position: number; pickRate: number | null; winRate: number | null; modelPosition: number | null };
}) {
  const measured = axisState === "measured";
  const axes = measured ? AXES : AXES.filter((a) => a.key !== "win" && a.key !== "pick");
  return (
    <div>
      <div className="mb-1.5 flex items-baseline justify-between gap-2">
        <span className="font-mono text-label uppercase tracking-[0.1em] text-faint">Why this item</span>
        <span className="font-mono text-label text-gold">{score.total.toFixed(2)}</span>
      </div>
      <div className="flex flex-col gap-1">
        {axes.map((a) => (
          <ScoreBar key={a.key} label={a.label} value={score[a.key]} help={a.help} />
        ))}
      </div>
      <p className="mt-1.5 text-label leading-relaxed text-faint">
        {axisState === "measured"
          ? "Four signals, weighted into one score. Higher is better on every axis."
          : axisState === "mode-unmeasured"
            ? "No community data in this mode, so win and pick aren’t measured here."
            /* F2. The mode HAS community data; this item is not in it. The two
               axes still carry their weight in the total above — win on the
               god’s own median, pick on a literal zero — so saying only
               “not measured” would leave the score looking like it was
               computed on the other two. */
            : "No community record for this item on this god, so win and pick aren’t measured here. The score still spends their weight on a stand-in."}
      </p>
      {measured && (
        <p className="mt-1.5 border-t border-line pt-1.5 text-label leading-relaxed text-faint">
          {meta ? (
            <>
              Community buys it {ordinal(meta.position)}
              {meta.pickRate != null && <> · {Math.round(meta.pickRate * 100)}% pick</>}
              {meta.winRate != null && <> · {Math.round(meta.winRate * 100)}% win</>}
              {/* Only when the two orders actually disagree. Printing
                  "community 3rd · model 3rd" would spend a line on agreement. */}
              {meta.modelPosition != null && meta.modelPosition !== meta.position && (
                <span className={meta.modelPosition < meta.position ? "text-under" : "text-premium"}>
                  {" "}· model buys it {ordinal(meta.modelPosition)}
                </span>
              )}
            </>
          ) : (
            <span className="text-under">The community build doesn&rsquo;t include this item.</span>
          )}
        </p>
      )}
    </div>
  );
}

/** Item identity plus, when the item is scored, its breakdown — one panel,
 * one disclosure, the same on every breakpoint. */
function ItemDetailCard({ item, name, score, axisState = "measured", meta }: {
  item?: Item;
  name: string;
  score?: SlotScore;
  axisState?: AxisState;
  meta?: { position: number; pickRate: number | null; winRate: number | null; modelPosition: number | null };
}) {
  const scoreBlock = score && (
    <div className="mt-2 border-t border-line pt-2">
      <WhyScoreBlock score={score} axisState={axisState} meta={meta} />
    </div>
  );
  if (!item) {
    return <div><span className="font-display font-semibold text-ink">{name}</span>{scoreBlock}</div>;
  }
  return (
    <div>
      <div className="mb-1 flex items-baseline justify-between gap-2">
        <span className="font-display text-body font-semibold text-ink">
          {item.name}{item.god && <GodOnlyAsterisk god={item.god} />}
        </span>
        <span className="shrink-0 font-mono text-label text-faint">
          <span className="text-gold">{item.cost}g</span> · {tierLabel(item.tier)}
        </span>
      </div>
      {item.god && <GodOnlyBadge god={item.god} className="mb-1.5" />}
      {Object.entries(item.stats || {}).map(([k, v]) => (
        <div key={k} className="flex justify-between text-small text-muted">
          <span>{k}</span><span className="font-mono text-ink">{v}</span>
        </div>
      ))}
      {item.passive && <div className="mt-1 text-small leading-relaxed text-muted">{item.passive}</div>}
      {(item.effect_tags?.length || item.efficiency_tier) && (
        <div className="mt-2 flex flex-wrap gap-1">
          {item.efficiency_tier && (
            <span className={`rounded-sm px-1.5 py-0.5 text-micro font-semibold uppercase tracking-[0.06em] ${
              item.efficiency_tier === "undervalued" ? "bg-under/20 text-under"
              : item.efficiency_tier === "premium" ? "bg-premium/20 text-premium"
              : "bg-bg3 text-muted"}`}>{item.efficiency_tier}</span>
          )}
          {item.effect_tags?.map((t) => (
            <span key={t} className="rounded-sm bg-bg3 px-1.5 py-0.5 text-label text-muted">{t}</span>
          ))}
        </div>
      )}
      {scoreBlock}
    </div>
  );
}

// A swap only earns an order-shift note when its cost differs meaningfully
// from what it replaces — a few hundred gold on a multi-thousand-gold item
// wouldn't actually move its purchase slot in a real build order.
const SWAP_ORDER_SHIFT_THRESHOLD = 0.15;

/** null inside the no-op band: where nothing shifts, print nothing. */
function swapOrderShiftNote(swapCost: number | undefined, replacedCost: number | undefined): string | null {
  if (!swapCost || !replacedCost) return null;
  const diff = (swapCost - replacedCost) / replacedCost;
  if (diff <= -SWAP_ORDER_SHIFT_THRESHOLD) return "buy earlier";
  if (diff >= SWAP_ORDER_SHIFT_THRESHOLD) return "buy later";
  return null;
}

// py-2, not py-1: at py-1 these came out 26px tall, and they are the primary
// control on the page a phone actually uses — mode, build, flavour. 26px is
// under every touch-target guideline going, and there are eleven of them in a
// row.
const segBtn = (active: boolean) =>
  `press rounded-md px-2.5 py-2 font-display text-small font-semibold capitalize transition-colors duration-150 ease-standard ${
    active ? "bg-gold text-bg0" : "text-muted hover:text-ink"
  }`;

const eyebrow = "font-mono text-label uppercase tracking-[0.1em] text-faint";

/** One purchase: where it lands on the gold spine, what the model scores it,
 * and what the community does with the same item. */
function LedgerRowView({
  row, index, expanded, onToggle, item, showScores, axisState, communityRates, ownRates, alternates,
}: {
  row: LedgerRow;
  index: number;
  expanded: boolean;
  onToggle: () => void;
  item?: Item;
  showScores: boolean;
  communityRates: boolean;
  /** Whether the win/pick axes on THIS row are a measurement — and when they
   * are not, which of the two absences it is. See `AxisState`. */
  axisState: AxisState;
  /** This row's own pick/win, when the row *is* a community slot rather than
   * a model slot being compared against one. */
  ownRates?: { pick_rate: number; win_rate: number };
  /** Other items this god's players run in the same slot — only present on a
   * community-sourced row. */
  alternates?: { name: string; pick_rate: number; win_rate: number }[];
}) {
  const removed = row.status === "removed";
  const added = row.status === "added";
  const measuredAxes = axisState === "measured";

  const label = [
    `${row.name}`,
    removed ? "swapped out" : added ? "swapped in" : `purchase ${index + 1}`,
    row.cumulative != null ? `at ${goldText(row.cumulative)} spent` : null,
    row.score ? `model score ${row.score.total.toFixed(2)}` : null,
    row.metaPosition != null
      ? `community buys it ${ordinal(row.metaPosition)}`
      : showScores ? "community does not buy it" : null,
  ].filter(Boolean).join(", ");

  return (
    <li>
      <button
        type="button"
        onClick={onToggle}
        aria-expanded={expanded}
        aria-label={label}
        /* The ledger row is the build, and it carried the same presence as a
           caption: a 13px name beside a 28px icon, flat on the page ground.
           It reads as an object now — its own surface, art at 36px, the name
           a step up the scale.

           A swap is marked ON THE GOLD SPINE rather than with a coloured left
           border. The border was the generic dashboard accent-bar, and this
           surface already has the better device: the cumulative-gold hairline
           running down the ledger. A rotated square on that rule is the tier
           ladder's own grammar for "the model's mark", so the pair never
           depends on colour alone. */
        className={`press grid w-full grid-cols-[58px_36px_minmax(0,1fr)_auto] items-center gap-x-3 gap-y-1 rounded-md bg-bg2/40 py-2 pr-2 text-left transition-colors duration-150 ease-standard hover:bg-bg2 ${
          removed ? "opacity-70" : ""}`}
      >
        {/* The gold spine — a continuous hairline down the left of the ledger. */}
        <span aria-hidden="true" className={`relative self-stretch border-r border-line pr-2.5 text-right font-mono text-micro leading-5 ${
          removed ? "text-line-strong line-through" : added ? "text-under" : "text-faint"}`}>
          {removed ? "—" : goldText(row.cumulative)}
          {added && (
            <span className="absolute -right-[3px] top-1/2 h-1.5 w-1.5 -translate-y-1/2 rotate-45 bg-under" />
          )}
        </span>

        <ItemIcon name={row.name} className={`h-9 w-9 ${removed ? "opacity-30" : ""}`} />

        <span className="flex min-w-0 flex-wrap items-center gap-x-1.5 gap-y-1">
          <span className={`truncate font-display text-lead font-semibold ${
            removed ? "text-muted line-through" : added ? "text-under" : "text-ink"}`}>
            {row.name}{item?.god && <GodOnlyAsterisk god={item.god} />}
          </span>
          {added && <span className="text-micro font-semibold uppercase tracking-[0.06em] text-under">swap in</span>}
          {row.isFlex && row.status === "kept" && (
            <span className="rounded-sm bg-bg3 px-1 py-px text-micro font-semibold uppercase tracking-[0.06em] text-faint">flex</span>
          )}
          {/* Named on the row it applies to, not just counted in the header:
              "4 of 6 finished" tells you how many, this tells you which. */}
          {row.unfinished && (
            <span
              title="A component, not a finished item — the match ended before it was upgraded"
              className="rounded-sm bg-premium/15 px-1 py-px text-micro font-semibold uppercase tracking-[0.06em] text-premium">
              unfinished
            </span>
          )}
          {/* Only for items the community genuinely never buys. An item they
              buy as a slot alternate gets the rate printed on the line below
              instead, which says more than the badge did and — unlike the
              badge — is true. */}
          {showScores && !removed && !added && !row.inMeta
            && row.metaAlternatePickRate == null && (
            <span className="rounded-sm bg-under/15 px-1 py-px text-micro font-semibold uppercase tracking-[0.06em] text-under"
              title="The model buys this; this god's community build doesn't">
              off-meta
            </span>
          )}
        </span>

        {row.score && !removed ? (
          <span aria-hidden="true" className="flex shrink-0 items-center gap-1.5">
            <span className="h-1 w-10 rounded-sm bg-bg3">
              <span className="bar-grow block h-1 origin-left rounded-sm bg-gold" style={{ width: `${Math.round(Math.min(Math.max(row.score.total, 0), 1) * 100)}%` }} />
            </span>
            <span className="w-7 text-right font-mono text-label text-ink">{row.score.total.toFixed(2)}</span>
          </span>
        ) : communityRates && ownRates ? (
          <span aria-hidden="true" className="shrink-0 font-mono text-label text-muted">
            {Math.round(ownRates.pick_rate * 100)}% / {Math.round(ownRates.win_rate * 100)}%
          </span>
        ) : <span />}

        {/* Second line: the four axes, and what the meta does with this item. */}
        <span aria-hidden="true" className="col-start-3 col-span-2 flex flex-wrap items-center gap-x-3 gap-y-0.5 text-label text-faint">
          {row.score && !removed && (
            <span className="flex gap-x-2">
              {AXES.map((a) => (
                // win and pick come from community data. Where there is none
                // — for the whole mode, or for this one item on this one god
                // — they are a stand-in rather than a measurement, and
                // printing "win 0.56 · pick 0.00" would read as a finding.
                measuredAxes || (a.key !== "win" && a.key !== "pick") ? (
                  <span key={a.key}>
                    {a.label} <span className="font-mono text-muted">{row.score![a.key].toFixed(2)}</span>
                  </span>
                ) : null
              ))}
              {!measuredAxes && <span className="text-faint">win/pick not measured here</span>}
            </span>
          )}
          {showScores && !removed && (
            row.metaPosition != null ? (
              <span>
                meta buys <span className="font-mono">{ordinal(row.metaPosition)}</span>
                {row.metaPickRate != null && <> · <span className="font-mono">{Math.round(row.metaPickRate * 100)}% pick</span></>}
                {row.modelPosition != null && row.modelPosition !== row.metaPosition && (
                  <span className={row.modelPosition < row.metaPosition ? " text-under" : " text-premium"}>
                    {" "}· model buys <span className="font-mono">{ordinal(row.modelPosition)}</span>
                  </span>
                )}
              </span>
            ) : row.metaAlternatePickRate != null ? (
              // Bought, just never the headline pick in any one slot.
              <span>
                meta buys this <span className="font-mono">{Math.round(row.metaAlternatePickRate * 100)}%</span>
                {row.metaAlternateWinRate != null && <> · <span className="font-mono">{Math.round(row.metaAlternateWinRate * 100)}% win</span></>}
                {" "}· not in their order
              </span>
            ) : <span className="text-under">meta doesn&rsquo;t buy this</span>
          )}
          {alternates?.length ? (
            <span className="min-w-0 truncate text-muted">
              or {alternates.map((a) => `${a.name} (${Math.round(a.pick_rate * 100)}%)`).join(", ")}
            </span>
          ) : null}
        </span>
      </button>

      {expanded && (
        <div className="mb-1 ml-[58px] rounded-md border border-line bg-bg1 p-2.5">
          <ItemDetailCard
            item={item}
            name={row.name}
            score={row.score}
            axisState={axisState}
            meta={showScores && row.metaPosition != null
              ? { position: row.metaPosition, pickRate: row.metaPickRate, winRate: row.metaWinRate,
                  modelPosition: row.modelPosition }
              : undefined}
          />
        </div>
      )}
    </li>
  );
}

/** How many underrated items read as a recommendation rather than a category.
 *  The lists themselves run to 39. */
const UNDERRATED_SHOWN = 5;

/** F7. "Underrated for this god" as a short ranked list instead of a run-on
 * sentence naming a median of 25 items.
 *
 * The claim was always fine — the Method page's definition (top 30% on
 * efficiency and fit, pick at or below 15%) makes every name on it legitimate,
 * and the lists are recomputed from current data rather than stale. What broke
 * was the format: 25 undifferentiated names, in prose, against a pool of 226,
 * with no ordering visible, no cut-off stated, and the build's own items among
 * them. That is a category, not a recommendation, and "underrated" is a claim.
 *
 * So: the strongest few, in the pipeline's own ranking order, with the count it
 * came from, a route to the definition (nothing else on this page has one), and
 * the remainder one press away rather than dropped.
 */
function UnderratedList({ god, names }: { god: string; names: string[] }) {
  const [showAll, setShowAll] = useState(false);
  const shown = showAll ? names : names.slice(0, UNDERRATED_SHOWN);
  const more = names.length - UNDERRATED_SHOWN;
  return (
    <div className="mt-3.5">
      <div className="flex flex-wrap items-baseline gap-x-2 gap-y-0.5">
        <h3 className={eyebrow}>Underrated for {god}</h3>
        <p className="text-label text-muted">
          <span className="font-mono">{shown.length}</span> of{" "}
          <span className="font-mono">{names.length}</span> the model rates highly and this
          god&rsquo;s players rarely buy ·{" "}
          <a href={toHash.method()} className="press rounded-sm text-blue hover:underline">
            how that&rsquo;s decided
          </a>
        </p>
      </div>
      <ul className="mt-1.5 flex flex-wrap gap-1.5">
        {shown.map((name) => (
          <li key={name}>
            <a href={toHash.item(name)}
              className="press flex items-center gap-1.5 rounded-md border border-line bg-bg2 py-1 pl-1 pr-2 transition-colors duration-150 ease-standard hover:border-line-strong">
              <ItemIcon name={name} className="h-6 w-6" />
              <span className="max-w-[18ch] truncate text-small text-ink">{name}</span>
            </a>
          </li>
        ))}
      </ul>
      {more > 0 && (
        <button type="button" onClick={() => setShowAll((v) => !v)}
          className="press mt-1.5 rounded-sm px-1 py-1 text-small text-blue hover:underline">
          {showAll ? `Show the top ${UNDERRATED_SHOWN}` : `Show all ${names.length}`}
        </button>
      )}
    </div>
  );
}

export function DetailPanel({
  god, godData, items, builds, mode, onModeChange, modeOrder, starters = [],
  aspectOn: aspectProp, onAspectChange,
}: DetailPanelProps) {
  const godNotes = builds.filter((b) => b.god === god);
  const note = godNotes.find((n) => n.mode === mode) ?? godNotes[0];
  // Ordered by the pipeline's own mode list, not by however the build
  // filenames sorted — which put Arena at the head of the strip the moment it
  // was added, ahead of Conquest. Anything the order doesn't name keeps its
  // original position at the end rather than disappearing.
  const modes = useMemo(() => {
    const rank = (m: string) => {
      const i = (modeOrder ?? []).indexOf(m);
      return i === -1 ? Number.MAX_SAFE_INTEGER : i;
    };
    return godNotes.map((n) => n.mode).sort((a, b) => rank(a) - rank(b));
  }, [godNotes, modeOrder]);
  const [activeIndex, setActiveIndex] = useState<number | null>(null);
  const [selectedTag, setSelectedTag] = useState<string | null>(null);
  const [editing, setEditing] = useState<MineDraft | "new" | null>(null);
  /* Controlled when App passes the state (the portrait's hexagon owns it),
     uncontrolled otherwise so the panel still stands alone. */
  const [aspectLocal, setAspectLocal] = useState(false);
  const aspectOn = aspectProp ?? aspectLocal;
  const setAspectOn = (on: boolean) => {
    setAspectLocal(on);
    onAspectChange?.(on);
  };
  const [mineVersion, setMineVersion] = useState(0);
  const [expandedIndex, setExpandedIndex] = useState<number | null>(null);

  const itemsByName = useMemo(() => {
    const m = new Map<string, Item>();
    for (const it of items) m.set(it.name, it);
    return m;
  }, [items]);
  const mineEntries = useMemo(
    () => getMine(god, note?.mode ?? mode).map((b) => ({ source: "mine" as const, ...b })),
    [god, note?.mode, mode, mineVersion],
  );

  useEffect(() => {
    // null, not 0: index 0 is now whichever build sorts first, and the default
    // has to be the first *model-side* one. Resetting to 0 would open a new god
    // on the community's build.
    setActiveIndex(null);
    setSelectedTag(null);
    setEditing(null);
    setAspectOn(false);
  }, [god, note]);

  useEffect(() => { setExpandedIndex(null); }, [god, note, activeIndex, selectedTag]);

  if (!note || note.builds.length === 0) {
    return (
      <div className="max-w-[52ch]">
        <h2 className="font-display text-title font-bold text-ink">{god}</h2>
        <p className="mt-2 text-body leading-relaxed text-muted">
          No build data for {god} in this index yet. The pipeline builds one per god per mode —
          this god either hasn&rsquo;t been scraped or has no items scored for {mode}.
        </p>
      </div>
    );
  }

  const aspectMeta = godData?.aspects?.[0];
  const communityEntry = note.builds.find(isCommunityEntry);

  // Three builds answer the same question three ways, and the reader should be
  // able to hold each one whole: the model's own answer, that answer corrected
  // where the community has real evidence, and what people actually run.
  //
  // Community used to be excluded from this list deliberately — it was only a
  // comparison track drawn alongside a model build. That was right when there
  // were two answers; with three it left one of them unreadable on its own
  // terms. It is selectable now, and the comparison track still runs whenever a
  // model-side build is the active one.
  /* Aspect-on selects the aspect family — but only if there IS one. The
     control now shows for all 72 gods that have an aspect, while only the 7
     with a scoring overlay in `_weights.yaml` have builds behind it, so
     filtering strictly would blank the model side for the other 65. Falling
     back to the base family means the badge always shows the kit text and
     never costs the reader the build. */
  const aspectFamily = note.builds.filter(
    (b) => b.source === "suggested" && !!(b as { aspect?: string }).aspect);
  const useAspect = aspectOn && aspectFamily.length > 0;
  const suggested = note.builds.filter((b) => {
    if (b.source !== "suggested") return false;
    const a = (b as { aspect?: string }).aspect;
    return useAspect ? !!a : !a;
  });
  const selectable: BuildEntry[] = [
    ...orderBuilds(dedupeCoreAgainstModel(suggested), communityEntry), ...mineEntries,
  ];
  // Nothing to select at all still has to render something.
  const primaryIsCommunity = selectable.length === 0;
  // Community is selectable, never the default: this surface opens on the
  // model's answer, and the community's build is the thing that answer is
  // being compared against. Only a god with no model build at all opens there.
  const defaultIndex = Math.max(0, selectable.findIndex((b) => b.source === "suggested"));
  const active: BuildEntry =
    selectable[activeIndex ?? defaultIndex] ?? selectable[defaultIndex] ?? (communityEntry as BuildEntry);

  // The aspect toggle used to test *all* builds, including community, so a god
  // whose community entry carried an aspect showed the toggle with no aspect
  // build behind it — and turning it on emptied the surface.
  const hasAspectBuild = note.builds.some((b) => b.source === "suggested" && !!(b as { aspect?: string }).aspect);
  /* The control moved to the portrait (see AspectBadge.tsx), so this panel no
     longer renders a button — but the build strip still has to follow. When
     the aspect flips, re-point the selection at the SAME archetype in the
     other family, so a reader comparing the bruiser build across aspects
     doesn't get silently dropped back to the core one. */
  const aspectRef = useRef(aspectOn);
  useEffect(() => {
    if (aspectRef.current === aspectOn) return;
    aspectRef.current = aspectOn;
    const cur = selectable[activeIndex ?? defaultIndex];
    const curArch = cur && cur.source === "suggested" ? (cur as CuratedBuildEntry).archetype : undefined;
    const nextSuggested = note.builds.filter((b) => {
      if (b.source !== "suggested") return false;
      const a = (b as { aspect?: string }).aspect;
      return useAspect ? !!a : !a;
    });
    // Index into the ORDERED list, which is what the tab strip renders.
    // Searching the raw filtered list silently pointed at a different build
    // once community joined the strip and the order stopped matching.
    const nextSelectable = [...orderBuilds(dedupeCoreAgainstModel(nextSuggested), communityEntry), ...mineEntries];
    const i = curArch
      ? nextSelectable.findIndex(
          (e) => e.source === "suggested" && (e as CuratedBuildEntry).archetype === curArch)
      : -1;
    setActiveIndex(i >= 0 ? i : null);
    setSelectedTag(null);
    // Depends only on the aspect flip; re-running on every selection change
    // would fight the reader for control of the strip.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [aspectOn]);

  const community = isCommunityEntry(active);
  const swaps = !community ? (active as CuratedBuildEntry).situational_swaps : undefined;
  const selectedSwap = swaps?.find((s) => s.vs_tag === selectedTag) ?? null;
  const baseNames = active.slot_order.map(slotItemName);
  const flexList = !community ? (active as CuratedBuildEntry).flex_slots : undefined;
  const preview = applySwap(baseNames, selectedSwap?.swap_item ?? null, flexList);

  const isFun = !community && !!(active as CuratedBuildEntry).fun;
  const scores = !community ? (active as CuratedBuildEntry).slot_scores : undefined;
  // A fun build is off-class by design; comparing it to the meta would mark
  // every row and say nothing. A `mine` build isn't the model's either — the
  // comparison copy says "model", so it may only run on the model's builds.
  const compareToMeta = active.source === "suggested" && !isFun && !!communityEntry;
  // win/pick are community-derived, and there are two ways to have none of it.
  // Joust and Arena ship no community entry at all, so the whole mode is
  // unmeasured. Inside a mode that HAS one, an item the entry has never seen is
  // unmeasured too — pick falls to a literal zero and win to this god's median,
  // and both then print exactly like a measurement. F2.
  const recordedItems = communityRecordedItems(communityEntry);
  const axisStateFor = (name: string): AxisState =>
    !communityEntry ? "mode-unmeasured"
      : recordedItems.has(name) ? "measured"
        : "item-unmeasured";

  const ledger = buildLedger({
    preview,
    itemsByName,
    scores,
    communityOrder: compareToMeta ? communityEntry!.slot_order : undefined,
    flexSlots: flexList,
  });

  /* F7. The pipeline appends every underrated item to the rationale string,
     and the page printed all of them as one run-on sentence — a median of 25
     names, an average of 2.8 of which are in the six-item core directly above.
     Items already on this ledger are dropped: the row carries `off-meta` for
     exactly that fact, and naming them again is the part of the list that
     reads as an error. */
  const rationale = splitRationale(!community ? (active as CuratedBuildEntry).rationale : undefined);
  const onLedger = new Set(ledger.rows.filter((r) => r.status !== "removed").map((r) => r.name));
  const underrated = rationale.underrated.filter((n) => !onLedger.has(n));

  const popularItems = communityEntry?.popular_items ?? [];
  const suggestedCore = note.builds.find(
    (b) => b.source === "suggested" && (b as CuratedBuildEntry).archetype === "core" && !(b as CuratedBuildEntry).fun,
  ) as CuratedBuildEntry | undefined;
  const suggestedCoreNames = new Set(suggestedCore?.slot_order ?? []);

  if (editing) {
    const recStarter = [...selectable, communityEntry]
      .map((e) => (e as { starter?: { base: string; upgrade: string } } | undefined)?.starter)
      .find(Boolean);
    return (
      <BuildEditor
        god={god}
        mode={note.mode}
        items={items}
        starters={starters}
        initial={editing === "new" ? null : editing}
        defaultStarter={recStarter}
        onClose={() => setEditing(null)}
        onSaved={(name) => {
          setMineVersion((v) => v + 1);
          // Offset by the ordered suggested-plus-community group, not by
          // `suggested.length` — community sits inside that group now.
          const idx = name ? getMine(god, note.mode).findIndex((b) => b.name === name) : -1;
          const before = orderBuilds(dedupeCoreAgainstModel(suggested), communityEntry).length;
          setActiveIndex(idx >= 0 ? before + idx : null);
        }}
      />
    );
  }

  return (
    <article>
      {/* The god's identity, its verdict and the draft hand-off all moved up
          into the shell's subject header, where they're true of every lens
          rather than only of this one. What's left here is what actually
          belongs to the build: which mode, and which kit. */}
      {(modes.length > 1 || hasAspectBuild) && (
        <div className="flex flex-wrap items-center gap-2 border-b border-line pb-4">
          {modes.length > 1 && (
            <div className="flex w-fit gap-0.5 rounded-md border border-line bg-bg1 p-0.5" role="group" aria-label="Game mode">
              {modes.map((m) => (
                <button key={m} type="button" onClick={() => onModeChange(m)}
                  aria-pressed={m === note.mode} className={segBtn(m === note.mode)}>
                  {m}
                </button>
              ))}
            </div>
          )}

        </div>
      )}

      {aspectOn && aspectMeta && (
        <div className="mt-3 rounded-md border border-gold/40 bg-bg1 p-2.5 text-small">
          <span className="font-display font-semibold text-gold">{aspectMeta.name}</span>
          <span className="text-muted"> — {aspectMeta.kit_changes}</span>
        </div>
      )}

      {/* ── Which build ────────────────────────────────────────────── */}
      {!primaryIsCommunity && (
        <div className="mt-4 flex flex-wrap items-center gap-2">
          <div role="group" aria-label="Build flavor" className="flex flex-wrap gap-0.5 rounded-md border border-line bg-bg1 p-1">
            {selectable.map((entry, i) => (
              <button key={`${tabLabel(entry)}-${i}`} type="button" aria-pressed={i === (activeIndex ?? defaultIndex)}
                onClick={() => setActiveIndex(i)} className={segBtn(i === (activeIndex ?? defaultIndex))}>
                {tabLabel(entry)}{(entry as { fun?: boolean }).fun ? " 🎲" : ""}
              </button>
            ))}
          </div>
          <button type="button" onClick={() => setEditing("new")}
            className="press rounded-md border border-line bg-bg2 px-2.5 py-2 text-small text-blue hover:border-line-strong">
            + New build
          </button>
          {active.source === "mine" && (
            <button type="button"
              onClick={() => setEditing({
                name: (active as CuratedBuildEntry).name ?? "",
                slot_order: active.slot_order as string[],
                starter: (active as CuratedBuildEntry).starter,
                notes: (active as CuratedBuildEntry).notes,
              })}
              className="press rounded-md border border-line bg-bg2 px-2.5 py-1 text-small text-muted hover:text-ink">
              Edit this build
            </button>
          )}
        </div>
      )}

      {isFun && (
        <div className="mt-3 rounded-md border border-premium/40 bg-bg1 p-2.5 text-small">
          <span className="font-display font-semibold text-premium">For fun 🎲</span>
          <span className="text-muted"> — deliberately off-class; not scored against the community.</span>
        </div>
      )}

      {/* ── The ledger ─────────────────────────────────────────────── */}
      <div className="mt-5 flex flex-col gap-6 lg:flex-row">
        {/* Capped so rows stay tight at wide viewports instead of stretching
            the name column across empty space. */}
        <div className="min-w-0 flex-1 lg:max-w-[720px]">
          <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
            <h2 className={eyebrow}>{community ? "Slot order" : "Buy order"}</h2>
            <p data-testid="ledger-total" className="text-label text-faint">
              {/* "core", not "total": the starter is bought first and isn't on
                  this spine, so calling it a total would misstate the build. */}
              <span className="font-mono">{goldText(ledger.totalGold)}</span> core
              {community && ledger.unfinishedSlots > 0 && (
                <>
                  <span className="px-1">·</span>
                  <span className="text-ink-soft">
                    {ledger.slots - ledger.unfinishedSlots} of {ledger.slots} finished
                  </span>
                </>
              )}
              {compareToMeta && ledger.hasMeta && (
                <>
                  <span className="px-1">·</span>
                  <span className={ledger.shared === ledger.slots ? "text-faint" : "text-ink-soft"}>
                    shares {ledger.shared} of {ledger.slots}
                  </span>{" "}
                  with the community
                </>
              )}
            </p>
          </div>

          {/* Said once, where the build is, because the shape of this data is
              not obvious and reads as a recommendation otherwise. Measured:
              slot 6 holds a component in 70% of the 87 Conquest builds and
              slot 5 in 9%, while slots 1-4 never do — matches end before six
              items are built, so the tail of a community build is whatever was
              half-finished at the whistle. */}
          {community && ledger.unfinishedSlots > 0 && (
            <p data-testid="community-tail-note" className="mt-2 max-w-[70ch] text-small leading-relaxed text-muted">
              {ledger.unfinishedSlots === 1
                ? "The last slot is a component, not a finished item."
                : `The last ${ledger.unfinishedSlots} slots are components, not finished items.`}
              {" "}This is what players actually had when the match ended, and most matches end before a
              sixth item is built — so read the tail of this build as where the game got to, not as
              something to buy.
            </p>
          )}

          {active.starter && (
            <div className="mt-2.5 flex flex-wrap items-center gap-2 border-b border-line pb-2.5">
              <span className={eyebrow}>Starter</span>
              {[active.starter.base, active.starter.upgrade].map((name, i) => (
                <span key={name} className="flex items-center gap-2">
                  {i === 1 && <span aria-hidden="true" className="text-faint">→</span>}
                  <span className="flex items-center gap-1.5">
                    <ItemIcon name={name} className="h-5 w-5" />
                    <span className="text-small text-ink-soft">{name}</span>
                  </span>
                </span>
              ))}
            </div>
          )}

          <ul className="mt-1.5 flex flex-col">
            {ledger.rows.map((row, i) => (
              <LedgerRowView
                key={`${row.name}-${i}`}
                row={row}
                index={i}
                expanded={expandedIndex === i}
                onToggle={() => setExpandedIndex((cur) => (cur === i ? null : i))}
                item={itemsByName.get(row.name)}
                showScores={compareToMeta}
                axisState={axisStateFor(row.name)}
                communityRates={community}
                ownRates={community
                  ? (active.slot_order[i] as { pick_rate?: number; win_rate?: number } | undefined)?.pick_rate != null
                    ? (active.slot_order[i] as { pick_rate: number; win_rate: number })
                    : undefined
                  : undefined}
                alternates={community
                  ? (active.slot_order[i] as { alternates?: { name: string; pick_rate: number; win_rate: number }[] })?.alternates
                  : undefined}
              />
            ))}
          </ul>

          {compareToMeta && ledger.hasMeta && (
            <div className="mt-3 border-t border-line pt-2.5">
              <p className="text-label text-faint">
                What the community buys instead
                <span className="px-1">·</span>
                {ledger.metaTotalGold != null
                  ? <><span className="font-mono">{goldText(ledger.metaTotalGold)}</span> over {ledger.metaSlots} slots</>
                  : <>{ledger.metaSlots} slots · core cost unavailable</>}
              </p>
              {ledger.metaOnly.length === 0 ? (
                <p className="mt-1.5 text-small text-muted">
                  Nothing — the model buys every item the community does, in a different order.
                </p>
              ) : (
                <ul className="mt-1.5 flex flex-col">
                  {ledger.metaOnly.map((m) => (
                    <li key={m.name}>
                      <a
                        href={toHash.item(m.name)}
                        aria-label={`${m.name}, bought ${ordinal(m.position)} by the community at ${goldText(m.cumulative)} spent, not in this build`}
                        className="press grid w-full grid-cols-[58px_28px_minmax(0,1fr)_auto] items-center gap-x-2.5 rounded-md py-1.5 pr-1.5 text-left transition-colors duration-150 ease-standard hover:bg-bg1"
                      >
                        <span aria-hidden="true" className="self-stretch border-r border-line pr-2.5 text-right font-mono text-micro leading-5 text-faint">
                          {goldText(m.cumulative)}
                        </span>
                        <ItemIcon name={m.name} className="h-7 w-7 opacity-60" />
                        <span className="min-w-0 truncate text-body text-ink-soft">{m.name}</span>
                        <span aria-hidden="true" className="shrink-0 font-mono text-micro text-faint">
                          {m.pickRate != null && <>{Math.round(m.pickRate * 100)}% pick</>}
                          {m.winRate != null && <> · {Math.round(m.winRate * 100)}% win</>}
                        </span>
                      </a>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          )}
          {/* The tier list has admitted this about Joust and Arena since it
              stopped ranking them; the BUILDS never did, and the builds are
              the product. Two thirds of the shipped build groups are these
              modes. Saying "nothing to compare against" understated it — that
              reads as a missing convenience, when what is missing is the
              evidence that the ordering means anything. The 5-6x and
              "unproven" figures are `smite.calibrate`'s, measured leakage-free
              on Conquest; no per-mode outcome data exists anywhere to measure
              these modes directly (checked 2026-08-10: SmiteBrain is Conquest
              only, smite2.live offers a Joust/Arena selector with no data
              behind it, SmiteTracker's meta report is Conquest only). */}
          {!community && !compareToMeta && !isFun && (
            <p className="mt-2 border-t border-line pt-2 text-small leading-relaxed text-muted">
              <span className="text-premium">No outcome data exists for {note.mode}.</span>{" "}
              These rows are efficiency and kit-fit alone. Measured on the modes that do have
              data, that pairing finds community-worthy items about 6&times; better than chance —
              but its <em>ordering</em> is unproven, so read this as a shortlist rather than a
              buy order.
            </p>
          )}
        </div>

        {/* Fixed-width column so the ledger never reflows when this changes. */}
        {swaps && swaps.length > 0 && (
          <div className="lg:w-[260px] lg:flex-none lg:border-l lg:border-line lg:pl-6">
            <h2 className={eyebrow}>Situational</h2>
            <div className="mt-2 flex flex-col gap-1.5">
              {swaps.map((swap) => {
                const clickable = !!swap.swap_item;
                const selected = swap.vs_tag === selectedTag;
                const swapPreview = swap.swap_item ? applySwap(baseNames, swap.swap_item, flexList) : null;
                const replacedName = swapPreview?.find((s) => s.status === "removed")?.name;
                const orderNote = swap.swap_item && replacedName
                  ? swapOrderShiftNote(itemsByName.get(swap.swap_item)?.cost, itemsByName.get(replacedName)?.cost)
                  : null;
                return (
                  <button key={swap.vs_tag} type="button" disabled={!clickable} aria-pressed={selected}
                    onClick={() => clickable && setSelectedTag(selected ? null : swap.vs_tag)}
                    className={`press rounded-md px-2 py-1.5 text-left text-small transition-colors duration-150 ease-standard ${
                      selected ? "bg-gold font-medium text-bg0"
                      : clickable ? "bg-bg2 text-ink-soft hover:bg-bg3"
                      : "bg-bg2 text-faint"}`}>
                    <span className="font-medium">{VS_LABELS[swap.vs_tag] ?? swap.vs_tag}</span>
                    {" — "}{swap.swap_item ?? swap.swap.replace(/^.*—\s*/, "").replace(/[()]/g, "")}
                    {replacedName && (
                      <span className={`mt-0.5 block text-micro ${selected ? "text-bg0/70" : "text-faint"}`}>
                        in for {replacedName}{orderNote ? ` — ${orderNote}` : ""}
                      </span>
                    )}
                    {!clickable && (
                      <span className="mt-0.5 block text-micro text-faint">no single item covers this — play around it</span>
                    )}
                  </button>
                );
              })}
            </div>
          </div>
        )}
      </div>

      {/* ── What the playerbase buys ───────────────────────────────── */}
      {popularItems.length > 0 && (
        <section className="mt-7 border-t border-line pt-5">
          <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
            <h2 className={eyebrow}>Popular items</h2>
            <p className="text-label text-faint">what this god&rsquo;s players actually buy — not an ordered build</p>
          </div>
          <ul className="mt-3 grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-5">
            {popularItems.map((p) => {
              const inCore = suggestedCoreNames.has(p.name);
              return (
                <li key={p.name}
                  className={`flex items-center gap-2 rounded-md border p-2 ${
                    inCore ? "border-gold/40 bg-gold/5" : "border-line bg-bg2"}`}>
                  <ItemIcon name={p.name} className="h-7 w-7" />
                  <span className="flex min-w-0 flex-col">
                    <span className="truncate text-label text-ink">{p.name}</span>
                    <span className="font-mono text-micro text-faint">
                      {Math.round(p.pick_rate * 100)}% pick · {Math.round(p.win_rate * 100)}% win
                    </span>
                    {inCore && <span className="text-micro font-semibold uppercase tracking-[0.06em] text-gold">in core</span>}
                  </span>
                </li>
              );
            })}
          </ul>
        </section>
      )}

      {/* What the community's record changed, and what earned it. This is the
          hybrid's entire claim — without it the build is a third list of six
          items with no account of where it came from. */}
      {!community && !!(active as CuratedBuildEntry).swaps?.length && (
        <div className="mt-4 rounded-md border border-line bg-bg1 p-3">
          <h3 className={eyebrow}>Where the community overruled the model</h3>
          {/* Joust and Arena have no community record of their own, so this
              build borrows Conquest's. Saying so is not a footnote — it is the
              difference between "measured here" and "measured somewhere else
              and judged to transfer", and this app does not blur that. */}
          {(active as CuratedBuildEntry).borrowed_from && (
            <p className="mt-1.5 text-small leading-relaxed text-muted">
              No {note.mode} record exists, so this uses{" "}
              <span className="text-ink-soft">{(active as CuratedBuildEntry).borrowed_from}</span>&rsquo;s —
              minus items whose value arrives too late for {note.mode}, and those
              that only answer a {(active as CuratedBuildEntry).borrowed_from} problem.
            </p>
          )}
          <ul className="mt-2 flex flex-col gap-2">
            {(active as CuratedBuildEntry).swaps!.map((s) => (
              <li key={s.added} className="text-small leading-relaxed">
                <span className="font-medium text-under">{s.added}</span>
                <span className="px-1.5 text-faint">replaced</span>
                <span className="text-ink-soft">{s.removed}</span>
                <p className="mt-0.5 text-label leading-relaxed text-muted">{s.reason}</p>
              </li>
            ))}
          </ul>
        </div>
      )}

      {!community && (active as CuratedBuildEntry).rationale && (
        <div className="mt-6 max-w-[74ch] border-t border-line pt-3">
          {rationale.lead && (
            <p className="text-small leading-relaxed text-muted">{rationale.lead}</p>
          )}
          {underrated.length > 0 && (
            <UnderratedList god={god} names={underrated} />
          )}
        </div>
      )}
    </article>
  );
}
