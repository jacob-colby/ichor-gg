/* THESIS: the tier list owns "who does the model rank, and where does the meta
 * disagree?" It refuses the source toggle — a control that shows our ranking
 * *instead of* the community's makes the reader hold one in memory to compare,
 * when the comparison is the entire product. Bands stay, because bands are the
 * form this audience reads tier lists in; the community becomes a ghost on
 * every card instead of a second page.
 * OWN-WORLD: Arena Night. Hairline rule-work, mono micro-labels, gold reserved
 * for selection and the model's own score. `under`/`premium` carry divergence.
 * STORY: a player scans the model's bands, sees at a glance how much of each
 * band the meta agrees with, and finds the names worth arguing about — which
 * sort to the front of every band.
 * FIRST VIEWPORT: a summary line stating agreement across the whole list, then
 * the S band with its own agreement tally and cards carrying model score plus
 * the community's ghost placement.
 * FORM: tier bands with community ghosts, position 7 of the ordered list, seed
 * key f397d87a.
 */
import { useMemo, useState } from "react";
import type { GodTierEntry, ItemTierEntry, TierEntry, TierListData } from "../types";
import { iconSlug } from "../lib/builds";
import { toHash } from "../lib/useHashRoute";
import { LANES, godLane, godInLane, laneTextClass, type Lane } from "../lib/roleAccent";
import { efficiencyLabel } from "../lib/itemFilters";
import { buildBands, type BandEntry, type BandSort, type TierLetter } from "../lib/tierBands";
import { deltaText } from "../lib/divergence";

type Subject = "gods" | "items";
type GameMode = "conquest" | "joust";

const GAME_MODES: { key: GameMode; label: string }[] = [
  { key: "conquest", label: "Conquest" },
  { key: "joust", label: "Joust" },
];

// A neutral ramp, not the signal palette. `under`/`premium` mean "which way
// the model leans against the market" everywhere else in the app; borrowing
// one of them to mean "A tier" would break that. Gold marks only the top
// band — the model's strongest verdict, once per page.
const TIER_TEXT: Record<TierLetter, string> = {
  S: "text-gold",
  A: "text-ink",
  B: "text-ink-soft",
  C: "text-muted",
};

const segBtn = (active: boolean) =>
  `press rounded px-3 py-1.5 font-display text-small font-semibold transition-colors duration-[150ms] ease-standard ${
    active ? "bg-gold text-bg0" : "text-muted hover:text-ink"
  }`;
const chip = (active: boolean, extra = "") =>
  `press rounded-full px-3 py-1.5 text-small transition-colors duration-[150ms] ease-standard ${
    active ? "bg-gold font-semibold text-bg0" : `border border-line hover:border-line-strong ${extra}`
  }`;
const selCls = "rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-small text-muted focus:border-blue focus:outline-none";
function scoreText(v: number | null | undefined): string {
  return v == null ? "—" : v.toFixed(2);
}

const entityLabel = (s: Subject) => (s === "gods" ? "god" : "item");

/**
 * Direction of a tier disagreement, from the tier letters — the same basis the
 * ghost text and the header tallies use.
 *
 * Colouring from the raw score gap instead put `premium` ("the meta rates it
 * higher") next to letters saying the model ranked it two tiers higher: the
 * two measures disagree near a tier boundary, and they were being shown four
 * characters apart. The letters are the verdict, so they own the colour.
 */
function divergenceClass(tierGap: number | null): string {
  if (tierGap == null || tierGap === 0) return "text-faint";
  return tierGap > 0 ? "text-under" : "text-premium";
}

/** Entry art with a real fallback rather than a hidden hole in the grid. */
function EntryIcon({ name, item }: { name: string; item: boolean }) {
  const [tries, setTries] = useState(0);
  const cls = "h-10 w-10 flex-none rounded-md object-cover sm:h-11 sm:w-11";
  if (tries > 1) {
    return (
      <span aria-hidden="true" className={`${cls} flex items-center justify-center bg-bg3 font-display text-body font-bold text-faint`}>
        {name.slice(0, 1)}
      </span>
    );
  }
  return (
    <img
      src={`/icons/${iconSlug(name)}${item ? "" : "-head"}.png${tries ? "?r=1" : ""}`}
      alt=""
      loading="lazy"
      onError={() => setTries((t) => t + 1)}
      className={`${cls} bg-bg2`}
    />
  );
}

/**
 * One entry: the model's placement, and the community's as a ghost.
 *
 * The ghost is the whole point of the redesign — where the community puts this
 * is readable without leaving the model's band, so nothing has to be held in
 * memory across a toggle.
 */
function EntryCard({ band, subject }: { band: BandEntry<TierEntry>; subject: Subject }) {
  const { entry, delta, tierGap, agrees, unranked } = band;
  const isGod = subject === "gods";
  const god = entry as GodTierEntry;
  const item = entry as ItemTierEntry;
  const eff = isGod ? null : efficiencyLabel(item.efficiency_tier);
  const lane = isGod ? godLane(god.role) : undefined;

  const ghost = unranked
    ? <span className="text-muted">unranked</span>
    : agrees
      ? <span className="text-faint">meta agrees · {entry.tier_community}</span>
      : (
        <>
          <span className={divergenceClass(tierGap)}>meta {entry.tier_community}</span>
          {/* Neutral: the score gap can point the other way from the letters
              near a tier boundary, so only the letters carry direction. */}
          <span className="text-faint">{deltaText(delta)}</span>
        </>
      );

  return (
    <li>
      <a
        href={isGod ? toHash.god(entry.name) : toHash.item(entry.name)}
        aria-label={`${entry.name}, model tier ${entry.tier_ours ?? "unrated"} at ${scoreText(entry.ours)}, ${
          unranked ? "no community rating"
          : `community tier ${entry.tier_community} at ${scoreText(entry.community)}`}`}
        // Stacked on a phone so the name gets the card's full width — laid
        // out beside the icon it truncated at "Thanatos".
        className={`press flex h-full flex-col items-center gap-1 rounded-md border bg-bg2 p-2 text-center transition-colors duration-[180ms] ease-standard hover:border-line-strong sm:flex-row sm:items-start sm:gap-2.5 sm:text-left ${
          agrees || unranked ? "border-line" : "border-line-strong"}`}
      >
        <EntryIcon name={entry.name} item={!isGod} />
        <span className="flex w-full min-w-0 flex-col items-center gap-0.5 sm:flex-1 sm:items-start">
          <span className="max-w-full truncate font-display text-small font-semibold leading-tight text-ink">{entry.name}</span>
          {isGod
            ? lane && <span className={`font-mono text-micro ${laneTextClass(lane)}`}>{lane}</span>
            : eff && <span className={`font-mono text-micro ${eff.cls.replace(/bg-\S+/g, "")}`}>{eff.text}</span>}
          <span className="mt-0.5 flex flex-wrap items-baseline justify-center gap-x-1.5 font-mono text-micro leading-tight sm:justify-start">
            {/* Not gold: 87 gilded scores would make the accent decorative.
                The band letter already carries the model's verdict. */}
            <span className="text-ink-soft">{scoreText(entry.ours)}</span>
            {ghost}
          </span>
        </span>
      </a>
    </li>
  );
}

function TierBand({ tier, entries, total, agreed, disagreed, unranked, subject }: {
  tier: TierLetter;
  entries: BandEntry<TierEntry>[];
  /** Whole-band size, which the tally below describes — `entries` may be
   * narrowed by the disputed-only filter. */
  total: number;
  agreed: number;
  disagreed: number;
  unranked: number;
  subject: Subject;
}) {
  return (
    <section data-testid={`band-${tier}`} aria-labelledby={`band-${tier}-h`} className="border-t border-line pt-3">
      <div className="mb-2.5 flex flex-wrap items-center gap-x-3 gap-y-1">
        <h2 id={`band-${tier}-h`} className="flex items-center gap-2">
          <span className={`flex h-7 w-7 items-center justify-center rounded-md bg-bg3 font-display text-body font-bold ${TIER_TEXT[tier]}`}>{tier}</span>
          {/* One basis: when a filter narrows the band, say so rather than
              printing a drawn count beside a whole-band tally. */}
          <span className="font-mono text-label text-faint">
            {entries.length === total ? total : `${entries.length} of ${total}`}
          </span>
        </h2>
        <p className="font-mono text-micro uppercase tracking-[0.08em] text-faint">
          {disagreed > 0 && <span className="text-ink-soft">{disagreed} disputed</span>}
          {disagreed > 0 && agreed > 0 && <span className="px-1">·</span>}
          {agreed > 0 && <>{agreed} agreed</>}
          {unranked > 0 && <>{(disagreed > 0 || agreed > 0) && <span className="px-1">·</span>}{unranked} unranked</>}
        </p>
      </div>
      {/* Steps with viewport: a single 158px minimum gave 2 columns on a
          phone and inflated cards to 181px at 1440. */}
      <ul className="grid grid-cols-[repeat(auto-fill,minmax(100px,1fr))] gap-2 sm:grid-cols-[repeat(auto-fill,minmax(140px,1fr))] lg:grid-cols-[repeat(auto-fill,minmax(152px,1fr))]">
        {entries.map((b) => <EntryCard key={b.entry.name} band={b} subject={subject} />)}
      </ul>
    </section>
  );
}

export function TierList({ tierlist }: { tierlist?: TierListData }) {
  const [gameMode, setGameMode] = useState<GameMode>("conquest");
  const [subject, setSubject] = useState<Subject>("gods");
  const [sort, setSort] = useState<BandSort>("disagreement");
  const [disputedOnly, setDisputedOnly] = useState(false);
  const [q, setQ] = useState("");
  const [lane, setLane] = useState<Lane | undefined>();
  const [efficiency, setEfficiency] = useState<string | undefined>();

  // Per-mode slice, falling back to the legacy flat shape when the per-mode
  // key is absent — either an index predating it, or Conquest, which is the
  // same data mirrored at the top level.
  const modeSlice = useMemo(() => tierlist?.[gameMode] ?? tierlist, [tierlist, gameMode]);
  const source: TierEntry[] = useMemo(
    () => (subject === "gods" ? modeSlice?.gods : modeSlice?.items) ?? [],
    [modeSlice, subject],
  );

  const query = q.trim().toLowerCase();
  const filtered = useMemo(() => source.filter((e) => {
    if (query && !e.name.toLowerCase().includes(query)) return false;
    if (subject === "gods" && lane && !godInLane((e as GodTierEntry).role, lane)) return false;
    if (subject === "items" && efficiency && ((e as ItemTierEntry).efficiency_tier ?? "") !== efficiency) return false;
    return true;
  }), [source, query, lane, efficiency, subject]);

  const result = useMemo(() => buildBands(filtered, sort), [filtered, sort]);
  // Whether this mode/subject has any community coverage at all, judged on the
  // unfiltered set. Asking the filtered set instead made a search miss print
  // "0 gods · no community ratings to compare against" for Conquest, which has
  // 69 of them.
  const sourceHasCommunity = useMemo(() => source.some((e) => e.community != null), [source]);

  // Applied after the tally so the summary always describes the whole filtered
  // set, not the narrowed view — otherwise "agreed on 0" would be tautological.
  const bands = useMemo(() => (disputedOnly
    ? result.bands
        .map((b) => ({ ...b, entries: b.entries.filter((e) => !e.agrees && !e.unranked) }))
        .filter((b) => b.entries.length > 0)
    : result.bands), [result.bands, disputedOnly]);

  // Entries the model hasn't tiered (the starter items) — counted in the
  // header, so they have to be drawn rather than silently dropped.
  const untiered = useMemo(
    () => (disputedOnly ? [] : result.untiered),
    [result.untiered, disputedOnly],
  );
  const shown = bands.reduce((n, b) => n + b.entries.length, 0) + untiered.length;
  const anyFilter = !!query || !!lane || !!efficiency || disputedOnly;
  const clear = () => { setQ(""); setLane(undefined); setEfficiency(undefined); setDisputedOnly(false); };
  const joustCommunityGap = gameMode === "joust" && result.ranked === 0 && result.total > 0;

  // Item scores aren't recomputed per mode in the pipeline, so the Joust slice
  // can be the very same figures as Conquest. Derived rather than assumed, so
  // the note disappears by itself if that ever stops being true.
  const modeIsMirrored = useMemo(() => {
    if (gameMode !== "joust" || subject !== "items") return false;
    const a = tierlist?.conquest?.items ?? tierlist?.items;
    const b = tierlist?.joust?.items;
    if (!a || !b || a.length !== b.length) return false;
    return a.every((e, i) => e.name === b[i].name && e.ours === b[i].ours && e.community === b[i].community);
  }, [tierlist, gameMode, subject]);

  return (
    <div className="mx-auto w-full max-w-[1440px] p-4 sm:p-6">
      <header className="pb-4">
        {/* A claim carrying its own numbers, like Home's — not a route label. */}
        <h1 className="max-w-[24ch] text-balance font-display text-display font-bold leading-[1.12] tracking-[-0.01em] text-ink sm:text-display">
          {result.ranked > 0 ? (
            <>The meta agrees with{" "}
              <span className="text-gold">{result.agreed} of {result.ranked}</span>{" "}
              {entityLabel(subject)} placements.
            </>
          ) : (
            <>Every {entityLabel(subject)}, ranked by the model.</>
          )}
        </h1>
        <p className="mt-2.5 max-w-[70ch] text-body leading-relaxed text-ink-soft">
          Bands are the model&rsquo;s. Each card carries where the community places the same{" "}
          {entityLabel(subject)}, so the disagreement is readable without switching views.
        </p>
        {result.ranked > 0 ? (
          <p data-testid="tier-summary" className="mt-2.5 flex flex-wrap items-center gap-x-3 gap-y-1 font-mono text-label uppercase tracking-[0.09em] text-faint">
            <span><span className="text-ink-soft">{result.agreed} of {result.ranked}</span> agreed</span>
            <span className="text-under">{result.modelHigher} we rank higher</span>
            <span className="text-premium">{result.metaHigher} the meta ranks higher</span>
            {result.unranked > 0 && <span>{result.unranked} unranked</span>}
          </p>
        ) : !sourceHasCommunity ? (
          <p data-testid="tier-summary" className="mt-2.5 font-mono text-label uppercase tracking-[0.09em] text-faint">
            {source.length} {subject} · no community ratings to compare against
          </p>
        ) : null}
        {/* Directly under the tally it qualifies — not below the control bar. */}
        {modeIsMirrored && (
          <p className="mt-2 max-w-[74ch] text-small leading-relaxed text-muted">
            Items aren&rsquo;t scored per mode, so these are the same figures as Conquest —
            the community column reflects Conquest play. Only god tiers differ between modes.
          </p>
        )}
      </header>

      {/* Controls */}
      <div className="sticky top-0 z-10 -mx-4 border-b border-line bg-bg0/95 px-4 py-3 backdrop-blur sm:-mx-6 sm:px-6">
        {/* One scrolling line per row on a phone rather than three wrapped
            ones — the bar was 229px, 28% of a 812px viewport, permanently. */}
        <div className="flex items-center gap-2 overflow-x-auto pb-0.5 sm:flex-wrap sm:overflow-visible [&>*]:shrink-0">
          <div role="group" aria-label="Game mode" className="flex items-center gap-1 rounded-md border border-line bg-bg2 p-1">
            {GAME_MODES.map((m) => (
              <button key={m.key} type="button" aria-pressed={gameMode === m.key}
                onClick={() => setGameMode(m.key)} className={segBtn(gameMode === m.key)}>{m.label}</button>
            ))}
          </div>
          <div role="group" aria-label="Subject" className="flex items-center gap-1 rounded-md border border-line bg-bg2 p-1">
            <button type="button" aria-pressed={subject === "gods"} onClick={() => setSubject("gods")} className={segBtn(subject === "gods")}>Gods</button>
            <button type="button" aria-pressed={subject === "items"} onClick={() => setSubject("items")} className={segBtn(subject === "items")}>Items</button>
          </div>
          <div role="group" aria-label="Order within each band" className="flex items-center gap-1 rounded-md border border-line bg-bg2 p-1">
            <button type="button" aria-pressed={sort === "disagreement"} onClick={() => setSort("disagreement")} className={segBtn(sort === "disagreement")}>Disputed first</button>
            <button type="button" aria-pressed={sort === "score"} onClick={() => setSort("score")} className={segBtn(sort === "score")}>By score</button>
          </div>
          <label className="flex cursor-text items-center gap-2 rounded-md border border-line bg-bg2 px-3 py-2 focus-within:border-blue">
            <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true" className="text-muted">
              <circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" />
            </svg>
            <input
              placeholder={`Search ${subject}…`}
              aria-label={`Search ${subject}`}
              value={q}
              onChange={(e) => setQ(e.target.value)}
              className="w-36 bg-transparent py-1 text-small text-ink placeholder:text-muted focus:outline-none"
            />
          </label>
          <span className="ml-auto font-mono text-label text-faint">
            {shown === filtered.length
              ? <>{filtered.length} {subject}</>
              : <>showing {shown} of {filtered.length}</>}
          </span>
        </div>

        <div className="mt-2 flex items-center gap-2 overflow-x-auto pb-0.5 sm:flex-wrap sm:overflow-visible [&>*]:shrink-0">
          {subject === "gods" ? (
            <>
              {/* "All" is the absence of a filter, so it stays neutral —
                  gold marks a choice the reader made. */}
              <button type="button" aria-pressed={!lane} onClick={() => setLane(undefined)}
                className={`press rounded-full border px-3 py-1.5 text-small transition-colors duration-[150ms] ease-standard ${
                  !lane ? "border-line-strong text-ink" : "border-line text-muted hover:border-line-strong"}`}>
                All
              </button>
              {LANES.map((l) => (
                <button key={l} type="button" aria-pressed={lane === l}
                  onClick={() => setLane(lane === l ? undefined : l)} className={chip(lane === l, laneTextClass(l))}>{l}</button>
              ))}
            </>
          ) : (
            <select value={efficiency ?? ""} onChange={(e) => setEfficiency(e.target.value || undefined)}
              aria-label="Filter by efficiency rating" className={selCls}>
              <option value="">All ratings</option>
              <option value="undervalued">Efficient</option>
              <option value="fair">Fair</option>
              <option value="premium">Premium</option>
            </select>
          )}
          {result.ranked > 0 && (
            <button type="button" aria-pressed={disputedOnly} onClick={() => setDisputedOnly((v) => !v)}
              className={`${chip(disputedOnly, "text-muted")} ml-auto`}>
              Only disputed
            </button>
          )}
        </div>
      </div>

      {joustCommunityGap && (
        <p className="mt-4 max-w-[74ch] text-small leading-relaxed text-muted">
          SmiteBrain doesn&rsquo;t track Joust, so there are no community ratings for this mode at all —
          every card below shows the model&rsquo;s placement alone. That&rsquo;s a real coverage gap, not a
          loading state.
        </p>
      )}

      {shown === 0 ? (
        <div className="flex flex-col items-start gap-2 py-16">
          <p className="max-w-[64ch] text-body leading-relaxed text-muted">
            {disputedOnly && filtered.length > 0
              ? `Nothing disputed here — the model and the community agree on ${
                  filtered.length === 1 ? "the one" : `all ${filtered.length}`
                } ${filtered.length === 1 ? entityLabel(subject) : `${entityLabel(subject)}s`} matching those filters.`
              : `No ${subject} match those filters.`}
          </p>
          {anyFilter && (
            <button type="button" onClick={clear} className="press rounded-sm px-1 py-1 text-small text-blue hover:underline">
              Clear filters
            </button>
          )}
        </div>
      ) : (
        <div className="mt-4 flex flex-col gap-5">
          {bands.map((b) => (
            <TierBand key={b.tier} tier={b.tier} entries={b.entries}
              total={b.agreed + b.disagreed + b.unranked} agreed={b.agreed}
              disagreed={b.disagreed} unranked={b.unranked} subject={subject} />
          ))}
          {untiered.length > 0 && (
            <section data-testid="band-untiered" aria-labelledby="band-untiered-h" className="border-t border-line pt-3">
              <div className="mb-2.5 flex flex-wrap items-center gap-x-3 gap-y-1">
                <h2 id="band-untiered-h" className="font-mono text-label uppercase tracking-[0.1em] text-faint">
                  Not tiered
                </h2>
                <p className="font-mono text-micro uppercase tracking-[0.08em] text-faint">{untiered.length}</p>
              </div>
              <p className="mb-2.5 max-w-[70ch] text-small leading-relaxed text-muted">
                Starters and components the model doesn&rsquo;t rank against full items — they&rsquo;re
                counted above, so they&rsquo;re shown here rather than dropped.
              </p>
              <ul className="grid grid-cols-[repeat(auto-fill,minmax(100px,1fr))] gap-2 sm:grid-cols-[repeat(auto-fill,minmax(140px,1fr))] lg:grid-cols-[repeat(auto-fill,minmax(152px,1fr))]">
                {untiered.map((b) => <EntryCard key={b.entry.name} band={b} subject={subject} />)}
              </ul>
            </section>
          )}
        </div>
      )}
    </div>
  );
}
