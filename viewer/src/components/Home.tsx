/* THESIS: Home owns one idea — where this model disagrees with the meta, and
 * why that disagreement is the product. It refuses the category-default app
 * home (search box + recents + a row of stat tiles) and it refuses the flat
 * ranked list, because a flat list of 0.45–0.55 scores hides the fact that the
 * disagreement is systematic by lane rather than scattered.
 * OWN-WORLD: Arena Night, unchanged. Near-black stepped surfaces, hairline
 * rules instead of cards, mono micro-labels, torchlight gold kept rare and
 * load-bearing. Divergence direction reuses the existing `under`/`premium`
 * signal pair — same meaning as on items, widened to gods.
 * STORY: a player sees that we disagree with the meta on most ranked gods,
 * finds their own lane as a column, and spots one name they'll argue with in
 * seconds. Then they click it.
 * FIRST VIEWPORT: a claim in display type with its numbers computed live, a
 * mono instrument line, search on the right; beneath it the lane board — five
 * columns ranked by disagreement, each headed by that lane's mean lean, so the
 * systematic pattern is visible rather than asserted.
 * FORM: Lane Board, position 3 of the ordered list, seed key c96ae713.
 */
import { useEffect, useMemo, useRef, useState } from "react";
import type { God, IndexData, PatchPeriod } from "../types";
import { toHash, navigate } from "../lib/useHashRoute";
import { usePins } from "../lib/pins";
import { filterGods } from "../lib/godFilters";
import { iconSlug } from "../lib/builds";
import { godLane, laneTextClass } from "../lib/roleAccent";
import { relativeDate } from "../lib/relativeDate";
import {
  buildDivergenceBoard, barPercent, deltaText,
  type Divergence, type LaneColumn,
} from "../lib/divergence";

/** Direction of a disagreement, in the vocabulary the Legend already teaches:
 * `under` = we rate it above the meta, `premium` = the meta rates it above us.
 * A gap too small to survive rounding gets no direction colour — claiming one
 * would assert a lean the printed number doesn't show. */
function deltaTextClass(delta: number): string {
  if (Math.abs(delta) < 0.005) return "text-faint";
  return delta > 0 ? "text-under" : "text-premium";
}

/** God portrait with a real fallback. The icon set is generated per god, so a
 * missing file should degrade to an initial rather than leave a hole in the
 * grid — one retry with a cache-bust first, since a stale 404 is the common
 * cause. */
function GodIcon({ name, className }: { name: string; className: string }) {
  const [tries, setTries] = useState(0);
  if (tries > 1) {
    return (
      <span
        aria-hidden="true"
        className={`flex shrink-0 items-center justify-center rounded-md bg-bg3 font-display font-bold text-faint ${className}`}
      >
        {name.slice(0, 1)}
      </span>
    );
  }
  return (
    <img
      src={`/icons/${iconSlug(name)}-head.png${tries ? "?r=1" : ""}`}
      alt=""
      loading="lazy"
      onError={() => setTries((t) => t + 1)}
      className={`shrink-0 rounded-md object-cover ${className}`}
    />
  );
}

/* ── Search ──────────────────────────────────────────────────────────────
 * A combobox, not a text field with a list under it. The results overlay the
 * page instead of displacing it, and the keyboard can reach every one of them.
 */
function HomeSearch({ gods }: { gods: God[] }) {
  const [q, setQ] = useState("");
  const [active, setActive] = useState(0);
  const [open, setOpen] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const results = useMemo(() => (q.trim() ? filterGods(gods, { q }).slice(0, 6) : []), [gods, q]);
  const expanded = open && q.trim().length > 0;

  // A shrinking result list must never leave the cursor past its end.
  useEffect(() => { setActive(0); }, [q]);

  const go = (name: string) => {
    setQ("");
    setOpen(false);
    navigate(toHash.god(name));
  };

  // Home/End deliberately aren't bound: in an editable combobox those belong to
  // the text caret, and stealing them makes the field feel broken.
  const onKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Escape") { setQ(""); setOpen(false); return; }
    if (!expanded || results.length === 0) return;
    if (e.key === "ArrowDown") { e.preventDefault(); setActive((i) => (i + 1) % results.length); }
    else if (e.key === "ArrowUp") { e.preventDefault(); setActive((i) => (i - 1 + results.length) % results.length); }
  };

  // Dismiss when focus leaves the whole combobox — otherwise the overlay stays
  // parked over the board after a click elsewhere.
  const onBlur = (e: React.FocusEvent<HTMLDivElement>) => {
    if (!e.currentTarget.contains(e.relatedTarget as Node | null)) setOpen(false);
  };

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    if (results[active]) go(results[active].name);
  };

  return (
    <div data-testid="home-search" onBlur={onBlur} className="relative w-full sm:max-w-sm">
      <form
        onSubmit={submit}
        role="search"
        className="flex items-center gap-2.5 rounded-md border border-line bg-bg2 px-3 py-2 transition-colors duration-[180ms] ease-standard focus-within:border-blue"
      >
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true" className="shrink-0 text-muted">
          <circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" />
        </svg>
        <input
          ref={inputRef}
          value={q}
          onChange={(e) => { setQ(e.target.value); setOpen(true); }}
          onFocus={() => setOpen(true)}
          onKeyDown={onKeyDown}
          placeholder="Search gods…"
          aria-label="Search gods"
          role="combobox"
          aria-expanded={expanded}
          aria-controls="home-search-results"
          aria-autocomplete="list"
          aria-activedescendant={expanded && results[active] ? `home-search-opt-${active}` : undefined}
          autoComplete="off"
          className="w-full bg-transparent text-sm text-ink placeholder:text-muted focus:outline-none"
        />
        {q && (
          <button
            type="button"
            onClick={() => { setQ(""); inputRef.current?.focus(); }}
            aria-label="Clear search"
            className="press shrink-0 rounded-sm px-1 font-mono text-xs text-faint hover:text-ink"
          >
            ✕
          </button>
        )}
      </form>

      {/* Announced separately so a screen reader hears the count without the
          list stealing focus. */}
      <p aria-live="polite" className="sr-only">
        {expanded ? `${results.length} god${results.length === 1 ? "" : "s"} match` : ""}
      </p>

      {expanded && (
        <ul
          id="home-search-results"
          role="listbox"
          aria-label="Matching gods"
          className="absolute z-20 mt-1.5 flex w-full flex-col gap-0.5 rounded-md border border-line-strong bg-bg2 p-1.5 shadow-card"
        >
          {results.length === 0 ? (
            <li className="px-2.5 py-2 text-xs text-muted">
              No god matches “{q.trim()}”. Check the spelling, or browse the lanes below.
            </li>
          ) : results.map((g, i) => (
            <li key={g.name} role="presentation">
              <button
                type="button"
                id={`home-search-opt-${i}`}
                role="option"
                aria-selected={i === active}
                onClick={() => go(g.name)}
                onMouseEnter={() => setActive(i)}
                tabIndex={-1}
                className={`press flex w-full items-center gap-2.5 rounded-sm px-2.5 py-2 text-left transition-colors duration-[150ms] ease-standard ${i === active ? "bg-bg3" : ""}`}
              >
                <GodIcon name={g.name} className="h-7 w-7" />
                <span className="truncate font-display text-[13px] font-semibold text-ink">{g.name}</span>
                {g.role && (
                  <span className={`ml-auto shrink-0 font-mono text-[10px] ${laneTextClass(godLane(g.role))}`}>
                    {godLane(g.role) ?? g.role}
                  </span>
                )}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

/* ── The claim ───────────────────────────────────────────────────────────
 * The page's one argument, with every number in it computed from the index
 * rather than written down. When there's no tier list to compare against, the
 * claim steps back to what the model does instead of inventing a statistic.
 */
function StateBlock({ data, disagreements, ranked, unranked }: {
  data: IndexData; disagreements: number; ranked: number; unranked: number;
}) {
  const comparable = ranked > 0;
  return (
    <header className="border-b border-line pb-6">
      <div className="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
        <div className="min-w-0">
          <h1 className="max-w-[19ch] text-balance font-display text-[30px] font-bold leading-[1.1] tracking-[-0.01em] text-ink sm:text-[38px]">
            {comparable ? (
              <>We disagree with the meta on{" "}
                <span className="text-gold">{disagreements} of {ranked}</span>{" "}
                ranked gods.
              </>
            ) : (
              <>Builds scored by a model, not by what&rsquo;s popular.</>
            )}
          </h1>
          <p className="mt-3 max-w-[64ch] text-sm leading-relaxed text-ink-soft">
            ichor fits a gold-value model to item stats to find what&rsquo;s underpriced for a
            god&rsquo;s kit, then weighs that against the community&rsquo;s high-elo meta.
            {comparable
              ? " Where the two part ways, it says so — by lane, biggest argument first."
              : " Community comparison isn't in this index yet, so nothing below is ranked against the meta."}
          </p>
        </div>

        <div className="flex shrink-0 flex-col gap-3 lg:items-end">
          <HomeSearch gods={data.gods} />
          <ul className="flex flex-wrap items-center gap-x-3 gap-y-1 font-mono text-[10.5px] uppercase tracking-[0.09em] text-faint lg:justify-end">
            <li>{data.gods.length} gods</li>
            {comparable && <li className="before:mr-3 before:content-['·']">{ranked} ranked</li>}
            {unranked > 0 && <li className="before:mr-3 before:content-['·']">{unranked} unranked</li>}
            {/* The patch label is deliberately absent here: the app header
                carries it on every route, and `Freshness` repeats it at the
                foot of this page. Three copies is two too many. */}
          </ul>
        </div>
      </div>
    </header>
  );
}

/** The encoding, decoded once, in place — so the bars below never need a
 * remembered schema. */
function BoardKey() {
  return (
    <div className="flex flex-wrap items-center gap-x-4 gap-y-1.5 font-mono text-[10px] uppercase tracking-[0.09em] text-faint">
      <span className="flex items-center gap-1.5">
        <span className="inline-block h-[3px] w-6 bg-premium" />
        Meta rates higher
      </span>
      <span className="flex items-center gap-1.5">
        <span className="inline-block h-[3px] w-6 bg-under" />
        Model rates higher
      </span>
      <span>Model · community, then the gap</span>
    </div>
  );
}

/** A single god's disagreement: who it is, what each side called it, and how
 * far apart they are. */
function DivergenceRow({ row, scale }: { row: Divergence; scale: number }) {
  const pct = barPercent(row.delta, scale);
  const positive = row.delta > 0;
  return (
    <li>
      <button
        type="button"
        onClick={() => navigate(toHash.god(row.name))}
        aria-label={`${row.name}: model ${row.ours.toFixed(2)} (tier ${row.tierOurs ?? "unrated"}), community ${row.community.toFixed(2)} (tier ${row.tierCommunity ?? "unrated"}), gap ${deltaText(row.delta)}`}
        className="press grid w-full grid-cols-[20px_minmax(0,1fr)_auto] items-center gap-x-2 gap-y-1.5 rounded-md px-1.5 py-1.5 text-left transition-colors duration-[150ms] ease-standard hover:bg-bg2"
      >
        <GodIcon name={row.name} className="h-5 w-5" />
        <span className="truncate font-display text-[12.5px] font-semibold text-ink">{row.name}</span>
        {/* Tier letters lift out of the quiet tier only when they actually
            differ, so the headline's disagreement count is countable here. */}
        <span
          className={`font-mono text-[10px] tracking-[0.06em] ${row.tierDisagrees ? "text-ink-soft" : "text-faint"}`}
          aria-hidden="true"
        >
          {row.tierOurs ?? "–"}<span className="px-0.5">/</span>{row.tierCommunity ?? "–"}
        </span>

        <span className="col-span-3 flex items-center gap-2">
          {/* Both operands, not just the gap: "+0.12" alone could be 0.85 vs
              0.73 or 0.20 vs 0.08, and the reader came here to interrogate. */}
          <span aria-hidden="true" className="shrink-0 font-mono text-[10px] text-faint">
            <span className="text-ink-soft">{row.ours.toFixed(2)}</span>
            <span className="px-0.5">·</span>
            {row.community.toFixed(2)}
          </span>
          <span aria-hidden="true" className="relative h-[3px] min-w-0 flex-1 bg-bg3">
            <span className="absolute inset-y-[-2px] left-1/2 w-px -translate-x-1/2 bg-line-strong" />
            <span
              className={`bar-grow absolute top-0 h-full ${positive ? "left-1/2 origin-left bg-under" : "right-1/2 origin-right bg-premium"}`}
              style={{ width: `${pct / 2}%` }}
            />
          </span>
          <span aria-hidden="true" className={`w-[42px] shrink-0 text-right font-mono text-[10.5px] ${deltaTextClass(row.delta)}`}>
            {deltaText(row.delta)}
          </span>
        </span>
      </button>
    </li>
  );
}

const ROWS_PER_LANE = 6;

/** One lane, ranked by how hard the two sources disagree. The column header
 * carries the lane's overall lean, which is where a systematic pattern —
 * every Carry rated below the meta, say — becomes visible. */
function LaneBoardColumn({ col, scale, index }: { col: LaneColumn; scale: number; index: number }) {
  const shown = col.rows.slice(0, ROWS_PER_LANE);
  const rest = col.rows.length - shown.length;
  const leanClass = deltaTextClass(col.meanDelta);

  return (
    <section
      style={{ ["--bar-delay" as string]: `${index * 70}ms` }}
      className="min-w-0 xl:border-l xl:border-line xl:pl-4 xl:first:border-l-0 xl:first:pl-0"
    >
      <h3 className={`font-display text-[13px] font-bold tracking-[0.02em] ${laneTextClass(col.lane)}`}>
        {col.lane}
      </h3>
      <p className="mt-0.5 font-mono text-[10px] uppercase tracking-[0.08em] text-faint">
        {col.rows.length > 0 ? (
          <>
            <span className={leanClass}>mean {deltaText(col.meanDelta)}</span>
            <span className="px-1">·</span>
            {col.lower} below
            <span className="px-1">·</span>
            {col.tierDiffer} differ
          </>
        ) : (
          <>no ranked gods</>
        )}
      </p>

      <ul className="mt-2.5 flex flex-col border-t border-line pt-1.5">
        {shown.map((row) => <DivergenceRow key={row.name} row={row} scale={scale} />)}
      </ul>

      {(rest > 0 || col.unranked > 0) && (
        <p className="mt-1.5 px-1.5 font-mono text-[10px] uppercase tracking-[0.08em] text-faint">
          {rest > 0 && <>+{rest} more</>}
          {rest > 0 && col.unranked > 0 && <span className="px-1">·</span>}
          {col.unranked > 0 && <>{col.unranked} unranked</>}
        </p>
      )}
    </section>
  );
}

/** The board. Absent entirely on an index with no tier list — the same rule
 * the rest of this page follows, rather than an empty shell. */
function DivergenceBoard({ board }: { board: ReturnType<typeof buildDivergenceBoard> }) {
  // Nothing comparable means no board at all — five columns of "no ranked
  // gods" under a key explaining bar lengths is exactly the empty shell the
  // rest of this page refuses. StateBlock already reports the unranked count.
  if (board.ranked === 0) return null;

  return (
    <section data-testid="home-divergence" aria-labelledby="home-divergence-h" className="pt-7">
      <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-2">
        <h2 id="home-divergence-h" className="font-display text-base font-bold text-ink">
          Where we disagree
        </h2>
        <a
          href={toHash.tiers()}
          className="press -my-1 rounded-sm px-1 py-1.5 font-mono text-[10.5px] uppercase tracking-[0.09em] text-blue hover:underline"
        >
          Full tier list →
        </a>
      </div>
      <div className="mt-2.5">
        <BoardKey />
      </div>

      {/* Row gap rather than `divide-y`: at sm/lg the five lanes wrap, and a
          divider drawn per grid child lands in the wrong places once they do.
          Each column carries its own rule above its rows instead. */}
      <div className="mt-4 grid grid-cols-1 gap-x-5 gap-y-7 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5">
        {board.lanes.map((col, i) => (
          <LaneBoardColumn key={col.lane} col={col} scale={board.scale} index={i} />
        ))}
      </div>

      {board.unranked > 0 && (
        <p className="mt-6 max-w-[72ch] border-t border-line pt-3 text-xs leading-relaxed text-muted">
          <span className="text-ink-soft">{board.unranked} of {board.total} gods have no community data yet.</span>{" "}
          They&rsquo;re left unranked rather than given an invented tier, so they don&rsquo;t appear above —
          the model still scores them on their own.
        </p>
      )}
    </section>
  );
}

/* ── Pinned ──────────────────────────────────────────────────────────────
 * Your own shortlist. With nothing pinned this is an invitation rather than an
 * apology: pinning is a feature to try, not something you're missing out on.
 */
function PinnedSection({ gods }: { gods: God[] }) {
  const { pins, toggle } = usePins();
  const pinnedGods = pins
    .map((n) => gods.find((g) => g.name === n))
    .filter((g): g is God => !!g);

  return (
    <section data-testid="home-pinned" aria-labelledby="home-pinned-h" className="border-t border-line pt-6">
      <h2 id="home-pinned-h" className="font-mono text-[10.5px] uppercase tracking-[0.1em] text-faint">
        Your pinned gods
      </h2>
      {pinnedGods.length === 0 ? (
        <p className="mt-2 max-w-[68ch] text-sm text-muted">
          Pin a god from its page and it&rsquo;ll show up here — a quick jump back to the ones you play most.
        </p>
      ) : (
        <ul className="mt-3 flex flex-wrap gap-2">
          {pinnedGods.map((g) => {
            const lane = godLane(g.role);
            return (
              <li key={g.name} className="group relative">
                <button
                  type="button"
                  onClick={() => navigate(toHash.god(g.name))}
                  aria-label={`Go to ${g.name}`}
                  className="press flex items-center gap-2 rounded-md border border-line bg-bg2 py-1.5 pl-1.5 pr-7 transition-colors duration-[180ms] ease-standard hover:border-line-strong"
                >
                  <GodIcon name={g.name} className="h-7 w-7" />
                  <span className="max-w-[110px] truncate font-display text-[12.5px] font-semibold text-ink">{g.name}</span>
                  {lane && <span className={`font-mono text-[9.5px] ${laneTextClass(lane)}`}>{lane}</span>}
                </button>
                <button
                  type="button"
                  onClick={() => toggle(g.name)}
                  aria-label={`Unpin ${g.name}`}
                  className="press absolute right-0.5 top-1/2 -translate-y-1/2 rounded-sm px-1.5 py-1 font-mono text-[11px] leading-none text-faint opacity-0 transition-opacity duration-[150ms] hover:text-ink focus-visible:opacity-100 group-hover:opacity-100"
                >
                  ✕
                </button>
              </li>
            );
          })}
        </ul>
      )}
    </section>
  );
}

/** Newest patch period only — a one-glance "what changed", with a link to the
 * full history. Rendered nowhere at all when there's no history yet. */
function LatestPatch({ periods }: { periods: PatchPeriod[] | undefined }) {
  if (!periods || periods.length === 0) return null;
  const latest = periods[0];
  const counts = [
    latest.changed.length > 0 ? `${latest.changed.length} changed` : null,
    latest.added.length > 0 ? `${latest.added.length} added` : null,
    latest.removed.length > 0 ? `${latest.removed.length} removed` : null,
  ].filter(Boolean).join(" · ");

  return (
    <section data-testid="home-patch" aria-labelledby="home-patch-h" className="border-t border-line pt-6">
      <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-2">
        <h2 id="home-patch-h" className="font-mono text-[10.5px] uppercase tracking-[0.1em] text-faint">
          Latest patch changes
        </h2>
        <a href={toHash.patch()} className="press -my-1 rounded-sm px-1 py-1.5 font-mono text-[10.5px] uppercase tracking-[0.09em] text-blue hover:underline">
          All patch notes →
        </a>
      </div>
      <div className="mt-3 flex flex-wrap items-baseline gap-x-3 gap-y-1 font-mono text-[11px] text-faint">
        <span>{latest.from} → {latest.to}</span>
        {counts && <span className="text-muted">{counts}</span>}
      </div>
      <div className="mt-2 flex flex-wrap gap-1.5">
        {latest.changed.map((d) => (
          <span key={d.name} className="rounded-sm border border-line bg-bg2 px-2 py-1 text-[11px] text-ink-soft">{d.name}</span>
        ))}
        {latest.added.map((n) => (
          <span key={n} className="rounded-sm border border-blue/30 bg-blue/10 px-2 py-1 text-[11px] font-semibold text-blue">{n}</span>
        ))}
        {latest.removed.map((n) => (
          <span key={n} className="rounded-sm border border-line px-2 py-1 text-[11px] text-muted line-through">{n}</span>
        ))}
      </div>
    </section>
  );
}

/** Relative freshness with the absolute date on hover, plus the current game
 * patch label when the index carries one. Omitted entirely when the index
 * predates `data_updated`. */
function Freshness({ dataUpdated, dataPatch }: { dataUpdated?: string; dataPatch?: string }) {
  if (!dataUpdated) return null;
  return (
    <p data-testid="home-freshness" title={dataUpdated} className="border-t border-line pt-4 font-mono text-[10.5px] uppercase tracking-[0.09em] text-faint">
      Updated {relativeDate(dataUpdated)}{dataPatch ? ` · ${dataPatch}` : ""}
    </p>
  );
}

export function Home({ data }: { data: IndexData }) {
  const board = useMemo(() => buildDivergenceBoard(data.tierlist?.gods), [data.tierlist]);

  return (
    <div className="mx-auto w-full max-w-[1440px] px-4 pb-12 pt-7 sm:px-6 sm:pt-9">
      <StateBlock
        data={data}
        disagreements={board.tierDisagreements}
        ranked={board.ranked}
        unranked={board.unranked}
      />
      <DivergenceBoard board={board} />
      <div className="mt-7 flex flex-col gap-6">
        <PinnedSection gods={data.gods} />
        <LatestPatch periods={data.patch_notes} />
        <Freshness dataUpdated={data.data_updated} dataPatch={data.data_patch} />
      </div>
    </div>
  );
}
