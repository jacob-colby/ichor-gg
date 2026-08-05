/* THESIS: this page owns one question — who actually wins, and how sure are we?
 * It used to own a different one: "where does the model disagree with the
 * meta?", with the model's bands and the community drawn as a ghost on every
 * card. That comparison was the product's headline and it did not survive
 * measurement — the model's god ranking correlated -0.117 with real god
 * strength, its item ranking -0.267 with item win rate, and 59% of gods
 * "placed differently" against the 75% two unrelated rankings produce. The
 * ghost is gone; what it argued with is now the ranking.
 * OWN-WORLD: Arena Night. Hairline rule-work, mono micro-labels, gold reserved
 * for selection and the top band. `under` marks the one editorial call left:
 * a god that wins well and is rarely played.
 * STORY: a player scans bands built from real outcomes, sees how much play each
 * placement rests on, and can pull out the gods worth learning because nobody
 * else is playing them.
 * FIRST VIEWPORT: a claim carrying its own sample size, then the S band with
 * cards showing win rate and matches.
 * FORM: tier bands over measured outcomes, position 7 of the ordered list.
 */
import { useMemo, useState } from "react";
import type { CommunitySource as CommunitySourceData, GodTierEntry, ItemTierEntry, TierEntry, TierListData } from "../types";
import { iconSlug } from "../lib/builds";
import { toHash } from "../lib/useHashRoute";
import { LANES, godLane, godInLane, laneTextClass, type Lane } from "../lib/roleAccent";
import { efficiencyLabel } from "../lib/itemFilters";
import { buildBands, type BandEntry, type BandSort, type TierLetter } from "../lib/tierBands";
import { rateText, matchesText, findUnderplayed } from "../lib/standings";
import { usePins } from "../lib/pins";
import { BookmarkIcon } from "./BookmarkIcon";
import { useUrlState } from "../lib/urlState";
import { CommunitySource } from "./CommunitySource";

type Subject = "gods" | "items";
type GameMode = "conquest" | "joust" | "arena";

const GAME_MODES: { key: GameMode; label: string }[] = [
  { key: "conquest", label: "Conquest" },
  { key: "joust", label: "Joust" },
  { key: "arena", label: "Arena" },
];

// A neutral ramp, not the signal palette. Gold marks only the top band.
const TIER_TEXT: Record<TierLetter, string> = {
  S: "text-gold",
  A: "text-ink",
  B: "text-ink-soft",
  C: "text-muted",
};

const segBtn = (active: boolean) =>
  `press rounded-sm px-3 py-2 font-display text-small font-semibold transition-colors duration-[150ms] ease-standard ${
    active ? "bg-gold text-bg0" : "text-muted hover:text-ink"
  }`;
const chip = (active: boolean, extra = "") =>
  `press rounded-full px-3 py-2 text-small transition-colors duration-[150ms] ease-standard ${
    active ? "bg-gold font-semibold text-bg0" : `border border-line hover:border-line-strong ${extra}`
  }`;
const selCls = "rounded-md border border-line bg-bg2 px-2.5 py-2 text-small text-muted focus:border-blue focus:outline-none";

const entityLabel = (s: Subject) => (s === "gods" ? "god" : "item");

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
 * One entry: what it won, and how much play that rests on.
 *
 * Both numbers, always. A card that shows only a rate reads equally sure at 44
 * matches and at 670, and the samples here span exactly that range.
 */
function EntryCard({ band, subject, underplayed, bookmarked }: {
  band: BandEntry<TierEntry>;
  subject: Subject;
  underplayed?: boolean;
  bookmarked?: boolean;
}) {
  const { entry, unmeasured } = band;
  const isGod = subject === "gods";
  const god = entry as GodTierEntry;
  const item = entry as ItemTierEntry;
  const eff = isGod ? null : efficiencyLabel(item.efficiency_tier);
  const lane = isGod ? godLane(god.role) : undefined;
  const matches = typeof entry.matches === "number" ? entry.matches : null;

  return (
    <li>
      <a
        href={isGod ? toHash.god(entry.name) : toHash.item(entry.name)}
        aria-label={unmeasured
          ? `${entry.name}: not enough matches to place`
          : `${entry.name}: ${entry.tier_score} tier, ${rateText(entry.win_rate)} win rate over ${
              matches?.toLocaleString("en-US") ?? "an unreported number of"} matches${
              underplayed ? " — wins well and is rarely played" : ""}${
              bookmarked ? " — bookmarked" : ""}`}
        title={unmeasured
          ? `${entry.name} — no usable sample`
          : `${entry.name} — ${rateText(entry.win_rate)} win over ${
              matches?.toLocaleString("en-US") ?? "?"} matches (ranked on the lower bound of that rate)`}
        // Stacked on a phone so the name gets the card's full width.
        // `w-full` for the same reason the shop's cards need it: a flex <a> is
        // shrink-to-fit and will size to its own text rather than to its grid
        // track.
        // The hover border is part of the same conditional, not a constant in
        // the base string. As a constant, `hover:border-line-strong` won over
        // `border-gold/40` on hover — hover utilities are emitted later, so a
        // bookmarked card lost its gold the moment you pointed at it. A
        // bookmarked card now hovers to MORE gold.
        className={`plane press flex h-full w-full flex-col items-center gap-1 rounded-md border bg-bg2 p-2 text-center transition-colors duration-[180ms] ease-standard sm:flex-row sm:items-start sm:gap-2.5 sm:text-left ${
          // A bookmark outranks the rarely-played emphasis on the border: it is
          // the reader's own mark, and "rarely played" still says itself in
          // words below. Gold for a saved god is the Torchlight Rule's first
          // permitted use — this is chosen — and the same treatment the god
          // picker already gives one.
          bookmarked ? "border-gold/40 hover:border-gold/70"
            : underplayed ? "border-line-strong hover:border-line-strong"
            : "border-line hover:border-line-strong"}`}
      >
        <EntryIcon name={entry.name} item={!isGod} />
        <span className="flex w-full min-w-0 flex-col items-center gap-0.5 sm:flex-1 sm:items-start">
          <span className="flex w-full min-w-0 items-center justify-center gap-1 sm:justify-start">
            {bookmarked && <span className="shrink-0 text-gold"><BookmarkIcon filled size={10} /></span>}
            <span className="min-w-0 truncate font-display text-small font-semibold leading-tight text-ink">{entry.name}</span>
          </span>
          {isGod
            ? lane && <span className={`text-label ${laneTextClass(lane)}`}>{lane}</span>
            : eff && <span className={`text-label ${eff.cls.replace(/bg-\S+/g, "")}`}>{eff.text}</span>}
          {unmeasured ? (
            <span className="mt-0.5 text-label leading-tight text-muted">not measured</span>
          ) : (
            <>
              <span className="mt-0.5 font-mono text-label leading-tight text-ink-soft">
                {rateText(entry.win_rate)} win
              </span>
              <span aria-hidden="true" className="font-mono text-micro leading-tight text-faint">
                {matches != null ? `${matchesText(matches)} matches` : " "}
              </span>
              {underplayed && (
                <span className="mt-0.5 text-label leading-tight text-under">rarely played</span>
              )}
            </>
          )}
        </span>
      </a>
    </li>
  );
}

function TierBand({ tier, entries, total, subject, underplayedNames, bookmarks }: {
  tier: TierLetter;
  entries: BandEntry<TierEntry>[];
  /** Whole-band size, which the count describes — `entries` may be narrowed. */
  total: number;
  subject: Subject;
  underplayedNames: Set<string>;
  bookmarks: Set<string>;
}) {
  // Appearances, not matches: ten gods play every match, so these sum to
  // several times the 4,952 the source line reports.
  const appearances = entries.reduce((n, b) => n + (b.entry.matches ?? 0), 0);
  return (
    <section data-testid={`band-${tier}`} aria-labelledby={`band-${tier}-h`} className="border-t border-line pt-3">
      <div className="mb-2.5 flex flex-wrap items-center gap-x-3 gap-y-1">
        <h2 id={`band-${tier}-h`} className="flex items-center gap-2">
          <span className={`flex h-7 w-7 items-center justify-center rounded-md bg-bg3 font-display text-body font-bold ${TIER_TEXT[tier]}`}>{tier}</span>
          <span className="text-label text-faint">
            {entries.length === total ? total : `${entries.length} of ${total}`}
          </span>
        </h2>
        {appearances > 0 && (
          <p className="font-mono text-label text-faint">
            {appearances.toLocaleString("en-US")} {subject === "gods" ? "god-games" : "purchases"}
          </p>
        )}
      </div>
      <ul className="grid auto-rows-fr grid-cols-[repeat(auto-fill,minmax(100px,1fr))] gap-2 sm:grid-cols-[repeat(auto-fill,minmax(140px,1fr))] lg:grid-cols-[repeat(auto-fill,minmax(152px,1fr))]">
        {entries.map((b) => (
          <EntryCard key={b.entry.name} band={b} subject={subject}
            underplayed={underplayedNames.has(b.entry.name)}
            bookmarked={bookmarks.has(b.entry.name)} />
        ))}
      </ul>
    </section>
  );
}

/* ── Board state in the URL ─────────────────────────────────────────────── */
interface BoardState {
  gameMode: GameMode;
  subject: Subject;
  sort: BandSort;
  underplayedOnly: boolean;
  q: string;
  lane?: Lane;
  efficiency?: string;
}

function decodeBoard(p: URLSearchParams): BoardState {
  const lane = p.get("lane");
  return {
    gameMode: p.get("mode") === "joust" ? "joust" : p.get("mode") === "arena" ? "arena" : "conquest",
    subject: p.get("of") === "items" ? "items" : "gods",
    sort: p.get("sort") === "matches" ? "matches" : "score",
    underplayedOnly: p.get("hidden") === "1",
    q: p.get("q") ?? "",
    lane: LANES.includes(lane as Lane) ? (lane as Lane) : undefined,
    efficiency: p.get("eff") ?? undefined,
  };
}

function encodeBoard(s: BoardState): Record<string, string | undefined> {
  return {
    mode: s.gameMode === "conquest" ? undefined : s.gameMode,
    of: s.subject === "gods" ? undefined : s.subject,
    sort: s.sort === "score" ? undefined : s.sort,
    hidden: s.underplayedOnly ? "1" : undefined,
    q: s.q.trim() || undefined,
    lane: s.lane,
    eff: s.efficiency,
  };
}

export function TierList({ tierlist, communitySource }: {
  tierlist?: TierListData;
  communitySource?: CommunitySourceData;
}) {
  const [board, setBoard] = useUrlState(decodeBoard, encodeBoard);
  const { gameMode, subject, sort, underplayedOnly, q, lane, efficiency } = board;
  const patch = (next: Partial<BoardState>) => setBoard((s) => ({ ...s, ...next }));

  const modeSlice = useMemo(() => tierlist?.[gameMode] ?? tierlist, [tierlist, gameMode]);
  const source: TierEntry[] = useMemo(
    () => (subject === "gods" ? modeSlice?.gods : modeSlice?.items) ?? [],
    [modeSlice, subject],
  );

  // Computed on the UNFILTERED set: "rarely played" is a fact about the whole
  // roster, and recomputing it inside a lane filter would make Solo's quietest
  // god look rare among five names.
  // Gods only: an item cannot be bookmarked, so an item board never marks one.
  const { pins } = usePins();
  const bookmarks = useMemo(
    () => new Set(subject === "gods" ? pins : []), [pins, subject]);

  const underplayedNames = useMemo(
    () => findUnderplayed(subject === "gods" ? (source as GodTierEntry[]) : []),
    [source, subject],
  );

  const query = q.trim().toLowerCase();
  const filtered = useMemo(() => source.filter((e) => {
    if (query && !e.name.toLowerCase().includes(query)) return false;
    if (subject === "gods" && lane && !godInLane((e as GodTierEntry).role, lane)) return false;
    if (subject === "items" && efficiency && ((e as ItemTierEntry).efficiency_tier ?? "") !== efficiency) return false;
    if (underplayedOnly && !underplayedNames.has(e.name)) return false;
    return true;
  }), [source, query, lane, efficiency, subject, underplayedOnly, underplayedNames]);

  const result = useMemo(() => buildBands(filtered, sort), [filtered, sort]);
  const untiered = result.untiered;
  const shown = result.bands.reduce((n, b) => n + b.entries.length, 0) + untiered.length;
  const anyFilter = !!query || !!lane || !!efficiency || underplayedOnly;
  const clear = () => patch({ q: "", lane: undefined, efficiency: undefined, underplayedOnly: false });
  // Only Conquest has outcome data. Every other mode comes back entirely
  // unmeasured, which is now stated rather than papered over with a ranking.
  const noOutcomes = result.ranked === 0 && result.total > 0;

  return (
    <div className="mx-auto w-full max-w-[1440px] p-4 sm:p-6">
      <header className="pb-4">
        <h1 className="max-w-[26ch] text-balance font-display text-display font-bold leading-[1.12] tracking-[-0.01em] text-ink sm:text-display">
          {result.ranked > 0 ? (
            <>Every {entityLabel(subject)}, ranked by{" "}
              <span className="text-gold">{result.appearances.toLocaleString("en-US")}</span>{" "}
              tracked {subject === "gods" ? "god-games" : "item purchases"}.
            </>
          ) : (
            <>No outcome data for this mode.</>
          )}
        </h1>
        {result.ranked > 0 && (
          <p className="mt-2.5 max-w-[70ch] text-body leading-relaxed text-ink-soft">
            Bands come from the lower bound of each {entityLabel(subject)}&rsquo;s real win rate, so a
            62% record over 133 matches doesn&rsquo;t outrank a 58% one over 2,000. Nothing this
            site models goes into the order.
          </p>
        )}
        {result.ranked > 0 && (
          <p data-testid="tier-summary" className="mt-2.5 flex flex-wrap items-center gap-x-3 gap-y-1 text-label text-faint">
            <span><span className="text-ink-soft">{result.ranked}</span> placed</span>
            {underplayedNames.size > 0 && subject === "gods" && (
              <span className="text-under">{underplayedNames.size} win well and are rarely played</span>
            )}
            {result.unmeasured > 0 && <span>{result.unmeasured} not measured</span>}
          </p>
        )}
        {result.ranked > 0 && <CommunitySource source={communitySource} className="mt-1.5" />}
      </header>

      {/* Controls */}
      <div className="sticky top-0 z-10 -mx-4 border-b border-line bg-bg0/90 px-4 py-3 backdrop-blur-md sm:-mx-6 sm:px-6">
        <div className="flex items-center gap-2 overflow-x-auto pb-0.5 sm:flex-wrap sm:overflow-visible [&>*]:shrink-0">
          <div role="group" aria-label="Game mode" className="flex items-center gap-1 rounded-md border border-line bg-bg2 p-1">
            {GAME_MODES.map((m) => (
              <button key={m.key} type="button" aria-pressed={gameMode === m.key}
                onClick={() => patch({ gameMode: m.key })} className={segBtn(gameMode === m.key)}>{m.label}</button>
            ))}
          </div>
          <div role="group" aria-label="Subject" className="flex items-center gap-1 rounded-md border border-line bg-bg2 p-1">
            <button type="button" aria-pressed={subject === "gods"} onClick={() => patch({ subject: "gods" })} className={segBtn(subject === "gods")}>Gods</button>
            <button type="button" aria-pressed={subject === "items"} onClick={() => patch({ subject: "items" })} className={segBtn(subject === "items")}>Items</button>
          </div>
          <div role="group" aria-label="Order within each band" className="flex items-center gap-1 rounded-md border border-line bg-bg2 p-1">
            <button type="button" aria-pressed={sort === "score"} onClick={() => patch({ sort: "score" })} className={segBtn(sort === "score")}>Best first</button>
            <button type="button" aria-pressed={sort === "matches"} onClick={() => patch({ sort: "matches" })} className={segBtn(sort === "matches")}>Most played</button>
          </div>
          <label className="flex cursor-text items-center gap-2 rounded-md border border-line bg-bg2 px-3 py-2 focus-within:border-blue">
            <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true" className="text-muted">
              <circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" />
            </svg>
            <input
              placeholder={`Search ${subject}…`}
              aria-label={`Search ${subject}`}
              value={q}
              onChange={(e) => patch({ q: e.target.value })}
              className="w-36 bg-transparent py-1 text-small text-ink placeholder:text-muted focus:outline-none"
            />
          </label>
          <span className="ml-auto text-label text-faint">
            {shown === filtered.length
              ? <>{filtered.length} {subject}</>
              : <>showing {shown} of {filtered.length}</>}
          </span>
        </div>

        <div className="mt-2 flex items-center gap-2 overflow-x-auto pb-0.5 sm:flex-wrap sm:overflow-visible [&>*]:shrink-0">
          {subject === "gods" ? (
            <>
              <button type="button" aria-pressed={!lane} onClick={() => patch({ lane: undefined })}
                className={`press rounded-full border px-3 py-2 text-small transition-colors duration-[150ms] ease-standard ${
                  !lane ? "border-line-strong text-ink" : "border-line text-muted hover:border-line-strong"}`}>
                All
              </button>
              {LANES.map((l) => (
                <button key={l} type="button" aria-pressed={lane === l}
                  onClick={() => patch({ lane: lane === l ? undefined : l })} className={chip(lane === l, laneTextClass(l))}>{l}</button>
              ))}
            </>
          ) : (
            <select value={efficiency ?? ""} onChange={(e) => patch({ efficiency: e.target.value || undefined })}
              aria-label="Filter by value rating" className={selCls}>
              <option value="">All value ratings</option>
              <option value="undervalued">Cheap for its stats</option>
              <option value="fair">Fairly priced</option>
              <option value="premium">Priced over its stats</option>
            </select>
          )}
          {subject === "gods" && underplayedNames.size > 0 && (
            <button type="button" aria-pressed={underplayedOnly}
              onClick={() => patch({ underplayedOnly: !underplayedOnly })}
              className={`${chip(underplayedOnly, "text-muted")} ml-auto`}>
              Only rarely played
            </button>
          )}
        </div>
      </div>

      {noOutcomes && (
        <p className="mt-4 max-w-[74ch] text-small leading-relaxed text-muted">
          SmiteBrain publishes no {GAME_MODES.find((m) => m.key === gameMode)?.label ?? gameMode} results,
          so there is nothing to rank these on. This page used to fill the gap with the site&rsquo;s own
          score; that score measured &minus;0.12 against real god strength, so an empty page is the more
          honest one. Builds for this mode still work &mdash; open any god.
        </p>
      )}

      {shown === 0 && !noOutcomes ? (
        <div className="flex flex-col items-start gap-2 py-16">
          <p className="max-w-[64ch] text-body leading-relaxed text-muted">
            No {subject} match those filters.
          </p>
          {anyFilter && (
            <button type="button" onClick={clear} className="press rounded-sm px-1 py-2 text-small text-blue hover:underline">
              Clear filters
            </button>
          )}
        </div>
      ) : (
        <div className="mt-4 flex flex-col gap-5">
          {result.bands.map((b) => (
            <TierBand key={b.tier} tier={b.tier} entries={b.entries}
              total={b.entries.length} subject={subject}
              underplayedNames={underplayedNames} bookmarks={bookmarks} />
          ))}
          {untiered.length > 0 && (
            <section data-testid="band-untiered" aria-labelledby="band-untiered-h" className="border-t border-line pt-3">
              <div className="mb-2.5 flex flex-wrap items-center gap-x-3 gap-y-1">
                <h2 id="band-untiered-h" className="font-mono text-label uppercase tracking-[0.1em] text-faint">
                  Not measured
                </h2>
                <p className="font-mono text-label text-faint">{untiered.length}</p>
              </div>
              <p className="mb-2.5 max-w-[70ch] text-small leading-relaxed text-muted">
                {subject === "gods"
                  ? "Too few tracked matches to place with any confidence. Shown rather than dropped, and never ranked low for it — “unmeasured” and “bad” are different facts."
                  : "No tracked win rate of their own — mostly starters and components, which players buy as a step on the way to something else."}
              </p>
              <ul className="grid auto-rows-fr grid-cols-[repeat(auto-fill,minmax(100px,1fr))] gap-2 sm:grid-cols-[repeat(auto-fill,minmax(140px,1fr))] lg:grid-cols-[repeat(auto-fill,minmax(152px,1fr))]">
                {untiered.map((b) => (
                  <EntryCard key={b.entry.name} band={b} subject={subject}
                    bookmarked={bookmarks.has(b.entry.name)} />
                ))}
              </ul>
            </section>
          )}
        </div>
      )}
    </div>
  );
}
