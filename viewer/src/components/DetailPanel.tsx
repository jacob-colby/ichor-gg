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
import { useEffect, useMemo, useState } from "react";
import type {
  BuildEntry, BuildNote, CuratedBuildEntry, God, Item, SlotScore,
} from "../types";
import { isCommunityEntry, slotItemName, iconSlug, applySwap, tabLabel } from "../lib/builds";
import { toHash } from "../lib/useHashRoute";
import { tierLabel } from "../lib/itemFilters";
import { buildLedger, goldText, goldGap, type LedgerRow } from "../lib/ledger";
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
  { key: "pick", label: "pick", help: "How often this god's players buy it" },
  { key: "fit", label: "fit", help: "How well the item's stats match this god's kit" },
];

interface DetailPanelProps {
  god: string;
  godData?: God;
  items: Item[];
  builds: BuildNote[];
  mode: string;
  onModeChange: (mode: string) => void;
  starters?: { base: string; upgrade: string }[];
  onReload?: () => void;
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
function WhyScoreBlock({ score, measured, meta }: {
  score: SlotScore;
  measured: boolean;
  meta?: { position: number; pickRate: number | null; winRate: number | null; gap: number | null };
}) {
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
        {measured
          ? "Four signals, weighted into one score. Higher is better on every axis."
          : "No community data in this mode, so win and pick aren’t measured here."}
      </p>
      {measured && (
        <p className="mt-1.5 border-t border-line pt-1.5 text-label leading-relaxed text-faint">
          {meta ? (
            <>
              Community buys it {meta.position}
              {meta.pickRate != null && <> · {Math.round(meta.pickRate * 100)}% pick</>}
              {meta.winRate != null && <> · {Math.round(meta.winRate * 100)}% win</>}
              {meta.gap != null && Math.abs(meta.gap) >= 500 && (
                <span className={meta.gap < 0 ? "text-under" : "text-premium"}>
                  {" "}· {meta.gap < 0 ? "model buys it earlier" : "model buys it later"} by {goldText(Math.abs(meta.gap))}
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
function ItemDetailCard({ item, name, score, measured = true, meta }: {
  item?: Item;
  name: string;
  score?: SlotScore;
  measured?: boolean;
  meta?: { position: number; pickRate: number | null; winRate: number | null; gap: number | null };
}) {
  const scoreBlock = score && (
    <div className="mt-2 border-t border-line pt-2">
      <WhyScoreBlock score={score} measured={measured} meta={meta} />
    </div>
  );
  if (!item) {
    return <div><span className="font-display font-semibold text-ink">{name}</span>{scoreBlock}</div>;
  }
  return (
    <div>
      <div className="mb-1 flex items-baseline justify-between gap-2">
        <span className="font-display text-body font-semibold text-ink">{item.name}</span>
        <span className="shrink-0 font-mono text-label text-faint">
          <span className="text-gold">{item.cost}g</span> · {tierLabel(item.tier)}
        </span>
      </div>
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

const segBtn = (active: boolean) =>
  `press rounded-md px-2.5 py-1 font-display text-small font-semibold capitalize transition-colors duration-150 ease-standard ${
    active ? "bg-gold text-bg0" : "text-muted hover:text-ink"
  }`;

const eyebrow = "font-mono text-label uppercase tracking-[0.1em] text-faint";

/** One purchase: where it lands on the gold spine, what the model scores it,
 * and what the community does with the same item. */
function LedgerRowView({
  row, index, expanded, onToggle, item, showScores, measuredAxes, communityRates, ownRates, alternates,
}: {
  row: LedgerRow;
  index: number;
  expanded: boolean;
  onToggle: () => void;
  item?: Item;
  showScores: boolean;
  communityRates: boolean;
  /** There is community data behind the win/pick axes. Without it they carry a
   * neutral default rather than a measurement. */
  measuredAxes: boolean;
  /** This row's own pick/win, when the row *is* a community slot rather than
   * a model slot being compared against one. */
  ownRates?: { pick_rate: number; win_rate: number };
  /** Other items this god's players run in the same slot — only present on a
   * community-sourced row. */
  alternates?: { name: string; pick_rate: number; win_rate: number }[];
}) {
  const gap = goldGap(row);
  const removed = row.status === "removed";
  const added = row.status === "added";

  const label = [
    `${row.name}`,
    removed ? "swapped out" : added ? "swapped in" : `purchase ${index + 1}`,
    row.cumulative != null ? `at ${goldText(row.cumulative)} spent` : null,
    row.score ? `model score ${row.score.total.toFixed(2)}` : null,
    row.metaPosition != null
      ? `community buys it ${row.metaPosition}${row.metaPosition === 1 ? "st" : row.metaPosition === 2 ? "nd" : row.metaPosition === 3 ? "rd" : "th"}`
      : showScores ? "community does not buy it" : null,
  ].filter(Boolean).join(", ");

  return (
    <li>
      <button
        type="button"
        onClick={onToggle}
        aria-expanded={expanded}
        aria-label={label}
        className="press grid w-full grid-cols-[58px_28px_minmax(0,1fr)_auto] items-center gap-x-2.5 gap-y-1 rounded-md py-1.5 pr-1.5 text-left transition-colors duration-150 ease-standard hover:bg-bg1"
      >
        {/* The gold spine — a continuous hairline down the left of the ledger. */}
        <span aria-hidden="true" className={`self-stretch border-r border-line pr-2.5 text-right font-mono text-micro leading-5 ${removed ? "text-line-strong line-through" : "text-faint"}`}>
          {removed ? "—" : goldText(row.cumulative)}
        </span>

        <ItemIcon name={row.name} className={`h-7 w-7 ${removed ? "opacity-30" : ""}`} />

        <span className="flex min-w-0 flex-wrap items-center gap-x-1.5 gap-y-1">
          <span className={`truncate text-body ${
            removed ? "text-muted line-through" : added ? "font-medium text-under" : "text-ink"}`}>
            {row.name}
          </span>
          {added && <span className="text-micro font-semibold uppercase tracking-[0.06em] text-under">swap in</span>}
          {row.isFlex && row.status === "kept" && (
            <span className="rounded-sm bg-bg3 px-1 py-px text-micro font-semibold uppercase tracking-[0.06em] text-faint">flex</span>
          )}
          {showScores && !removed && !added && !row.inMeta && (
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
                // win and pick come from community data. Where there is none,
                // they're a neutral default rather than a measurement, and
                // printing "win 0.50 · pick 0.00" would read as a finding.
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
                meta buys <span className="font-mono">{row.metaPosition}</span>
                {row.metaPickRate != null && <> · <span className="font-mono">{Math.round(row.metaPickRate * 100)}% pick</span></>}
                {gap != null && Math.abs(gap) >= 500 && (
                  <span className={gap < 0 ? " text-under" : " text-premium"}>
                    {" "}· {gap < 0 ? "model buys earlier" : "model buys later"} by <span className="font-mono">{goldText(Math.abs(gap))}</span>
                  </span>
                )}
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
            measured={measuredAxes}
            meta={showScores && row.metaPosition != null
              ? { position: row.metaPosition, pickRate: row.metaPickRate, winRate: row.metaWinRate, gap }
              : undefined}
          />
        </div>
      )}
    </li>
  );
}

export function DetailPanel({
  god, godData, items, builds, mode, onModeChange, starters = [],
}: DetailPanelProps) {
  const godNotes = builds.filter((b) => b.god === god);
  const note = godNotes.find((n) => n.mode === mode) ?? godNotes[0];
  const modes = godNotes.map((n) => n.mode);
  const [activeIndex, setActiveIndex] = useState(0);
  const [selectedTag, setSelectedTag] = useState<string | null>(null);
  const [editing, setEditing] = useState<MineDraft | "new" | null>(null);
  const [aspectOn, setAspectOn] = useState(false);
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
    setActiveIndex(0);
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

  // Community is no longer one option among many — it's the constant
  // comparison track. Only the model's builds and the player's own are
  // selectable, which is why this surface now opens on the model's answer.
  const suggested = note.builds.filter((b) => {
    if (b.source !== "suggested") return false;
    const a = (b as { aspect?: string }).aspect;
    return aspectOn ? !!a : !a;
  });
  const selectable: BuildEntry[] = [...suggested, ...mineEntries];
  // A god with no suggested build at all still has to render something.
  const primaryIsCommunity = selectable.length === 0;
  const active: BuildEntry = selectable[activeIndex] ?? selectable[0] ?? (communityEntry as BuildEntry);

  // The aspect toggle used to test *all* builds, including community, so a god
  // whose community entry carried an aspect showed the toggle with no aspect
  // build behind it — and turning it on emptied the surface.
  const hasAspectBuild = note.builds.some((b) => b.source === "suggested" && !!(b as { aspect?: string }).aspect);
  const toggleAspect = () => {
    const next = !aspectOn;
    const cur = selectable[activeIndex];
    const curArch = cur && cur.source === "suggested" ? (cur as CuratedBuildEntry).archetype : undefined;
    const nextSuggested = note.builds.filter((b) => {
      if (b.source !== "suggested") return false;
      const a = (b as { aspect?: string }).aspect;
      return next ? !!a : !a;
    });
    const i = curArch ? nextSuggested.findIndex((e) => (e as CuratedBuildEntry).archetype === curArch) : -1;
    setAspectOn(next);
    setActiveIndex(i >= 0 ? i : 0);
    setSelectedTag(null);
  };

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
  // win/pick are community-derived. Joust ships no community entries at all,
  // so those axes carry a neutral default there rather than a measurement.
  const measuredAxes = !!communityEntry;

  const ledger = buildLedger({
    preview,
    itemsByName,
    scores,
    communityOrder: compareToMeta ? communityEntry!.slot_order : undefined,
    flexSlots: flexList,
  });

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
          const idx = name ? getMine(god, note.mode).findIndex((b) => b.name === name) : -1;
          setActiveIndex(idx >= 0 ? suggested.length + idx : 0);
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
          {hasAspectBuild && (
            <button type="button" onClick={toggleAspect} aria-pressed={aspectOn} className={`${segBtn(aspectOn)} border border-line`}>
              {aspectMeta ? `Aspect: ${aspectMeta.name.replace(/^Aspect of (the )?/i, "")}` : "Aspect"}
            </button>
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
              <button key={`${tabLabel(entry)}-${i}`} type="button" aria-pressed={i === activeIndex}
                onClick={() => setActiveIndex(i)} className={segBtn(i === activeIndex)}>
                {tabLabel(entry)}{(entry as { fun?: boolean }).fun ? " 🎲" : ""}
              </button>
            ))}
          </div>
          <button type="button" onClick={() => setEditing("new")}
            className="press rounded-md border border-line bg-bg2 px-2.5 py-1 text-small text-blue hover:border-line-strong">
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
          <span className="text-muted"> — deliberately off-class; not scored against the meta.</span>
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
              {compareToMeta && ledger.hasMeta && (
                <>
                  <span className="px-1">·</span>
                  <span className={ledger.shared === ledger.slots ? "text-faint" : "text-ink-soft"}>
                    shares {ledger.shared} of {ledger.slots}
                  </span>{" "}
                  with the meta
                </>
              )}
            </p>
          </div>

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
                measuredAxes={measuredAxes}
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
                What the meta buys instead
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
                        aria-label={`${m.name}, bought ${m.position} by the community at ${goldText(m.cumulative)} spent, not in this build`}
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
          {!community && !compareToMeta && !isFun && (
            <p className="mt-2 border-t border-line pt-2 text-small text-muted">
              No community build for {god} in {note.mode} — nothing to compare this against, so the
              rows show the model&rsquo;s score alone.
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

      {!community && (active as CuratedBuildEntry).rationale && (
        <p className="mt-6 max-w-[74ch] border-t border-line pt-3 text-small leading-relaxed text-muted">
          {(active as CuratedBuildEntry).rationale}
        </p>
      )}
    </article>
  );
}
