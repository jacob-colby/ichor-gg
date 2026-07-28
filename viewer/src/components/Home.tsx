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
import { useMemo, useState } from "react";
import type { God, IndexData, ItemTierEntry, PatchPeriod, TierEntry, TierListData } from "../types";
import { toHash, navigate } from "../lib/useHashRoute";
import { usePins } from "../lib/pins";
import { iconSlug } from "../lib/builds";
import { godLane, laneTextClass } from "../lib/roleAccent";
import { relativeDate } from "../lib/relativeDate";
import { useDraft, encodeDraftHash, MODE_TEAM_SIZE } from "../lib/draft";
import {
  buildDivergenceBoard, deltaText,
  type Divergence, type LaneColumn,
} from "../lib/divergence";
import { biggestArguments, type Argument } from "../lib/tierBands";
import { TierLadder } from "./TierLadder";
import { VERDICT_TEXT, VERDICT_WORD, VERDICT_SPOKEN } from "../lib/verdictWords";
import { CommunitySource } from "./CommunitySource";

/** The one label style shared by the sections below the board. */
const sectionLabel = "font-mono text-label uppercase tracking-[0.1em] text-faint";


/** God portrait with a real fallback. The icon set is generated per god, so a
 * missing file should degrade to an initial rather than leave a hole in the
 * grid — one retry with a cache-bust first, since a stale 404 is the common
 * cause. */
function GodIcon({ name, className, item = false }: { name: string; className: string; item?: boolean }) {
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
      src={`/icons/${iconSlug(name)}${item ? "" : "-head"}.png${tries ? "?r=1" : ""}`}
      alt=""
      loading="lazy"
      onError={() => setTries((t) => t + 1)}
      className={`shrink-0 rounded-md object-cover ${className}`}
    />
  );
}

/* ── The evidence ────────────────────────────────────────────────────────
 * The half-dozen arguments actually worth having, named.
 *
 * This block used to compare the five lanes by how much each one leans. That
 * was a chart about the model's behaviour in aggregate: true, but it named
 * nobody, and "Solo leans −0.05" is not a thing anyone can act on. Six real
 * names — three gods, three items, furthest apart in either direction — is the
 * same claim told as the thing a player came for.
 *
 * Gods and items are ranked separately and never pooled: see
 * `biggestArguments` for why one merged list would be all items, every time.
 */
const ARGUMENTS_SHOWN = 3;

function ArgumentRow({ arg, item }: { arg: Argument<TierEntry>; item: boolean }) {
  const { entry, verdict } = arg;
  const tone = VERDICT_TEXT[verdict];
  return (
    <li>
      <a
        href={item ? toHash.item(entry.name) : toHash.god(entry.name)}
        aria-label={`${entry.name}: the community places it ${entry.tier_community}, we place it ${entry.tier_ours} — ${VERDICT_SPOKEN[verdict]}`}
        className="press grid grid-cols-[20px_minmax(0,1fr)_auto_4.75rem] items-center gap-x-2 rounded-md px-1.5 py-1 transition-colors duration-[150ms] ease-standard hover:bg-bg2"
      >
        <GodIcon name={entry.name} item={item} className="h-5 w-5" />
        <span className="truncate font-display text-small font-semibold text-ink">{entry.name}</span>
        {/* The movement, not a gap figure: the tier they'd be at, and the tier
            we'd put them at. Only the destination takes the colour — the
            community's placement is the neutral starting point. */}
        <span aria-hidden="true" className="font-mono text-label text-faint">
          {entry.tier_community}
          <span className="px-1 text-muted">→</span>
          <span className={tone}>{entry.tier_ours}</span>
        </span>
        <span aria-hidden="true" className={`text-right text-label ${tone}`}>
          {VERDICT_WORD[verdict]}
        </span>
      </a>
    </li>
  );
}

function ArgumentGroup({ label, set, item }: {
  label: string; set: ReturnType<typeof biggestArguments<TierEntry>>; item: boolean;
}) {
  if (set.top.length === 0) return null;
  return (
    <>
      <p className="mt-2.5 border-t border-line pt-2 text-label text-faint">
        <span className="text-ink-soft">{label}</span>
        <span className="px-1">·</span>
        {/* What the three are a sample of, so a short list can't read as the
            whole disagreement. */}
        <span className="font-mono">{set.disputed}</span> of{" "}
        <span className="font-mono">{set.ranked}</span> placed differently
      </p>
      <ul className="mt-0.5 flex flex-col">
        {set.top.map((a) => <ArgumentRow key={a.entry.name} arg={a} item={item} />)}
      </ul>
    </>
  );
}

function BiggestArguments({ tierlist, source }: { tierlist?: TierListData; source?: IndexData["community_source"] }) {
  const gods = useMemo(() => biggestArguments(tierlist?.gods ?? [], ARGUMENTS_SHOWN), [tierlist]);
  // Full items only. Tiers 1–2 are components and starters — things you pass
  // through on the way to a build, not things you choose — so an argument
  // about one isn't an argument anybody can act on. Unfiltered, two of the
  // three loudest item disagreements were components.
  const items = useMemo(
    () => biggestArguments(
      (tierlist?.items ?? []).filter((e) => (e as ItemTierEntry).tier === 3),
      ARGUMENTS_SHOWN,
    ),
    [tierlist],
  );
  if (gods.top.length === 0 && items.top.length === 0) return null;

  return (
    <section aria-labelledby="home-args-h" className="w-full lg:max-w-[600px] lg:flex-1">
      <div className="flex items-baseline justify-between gap-3">
        <h2 id="home-args-h" className={sectionLabel}>Where we argue hardest</h2>
        <span className="text-label text-faint">community tier → ours</span>
      </div>
      <ArgumentGroup label="Gods" set={gods} item={false} />
      <ArgumentGroup label="Items" set={items} item={true} />
      {/* Stated where the comparison is, not buried in a help page. */}
      <CommunitySource source={source} className="mt-2.5 border-t border-line pt-2" />
    </section>
  );
}

/* ── The claim ───────────────────────────────────────────────────────────
 * The page's one argument, with every number in it computed from the index
 * rather than written down. When there's no tier list to compare against, the
 * claim steps back to what the model does instead of inventing a statistic.
 */
/* The claim, led by the half a player can act on.
 *
 * It used to read "We disagree with the meta on 53 of 69 ranked gods" — a
 * sentence about the model's aggregate behaviour, true and inert. Nobody
 * opens a build site to find out how often two rankings differ; they open it
 * to find the god the meta is sleeping on. Same numbers, counted the same
 * way, pointed at the reader instead of at the method. */
function Claim({ board }: { board: ReturnType<typeof buildDivergenceBoard> }) {
  const { modelHigher, metaHigher, ranked } = board;
  const gold = (n: number) => <span className="text-gold">{n} god{n === 1 ? "" : "s"}</span>;

  if (modelHigher > 0) {
    return <>The community underrates {gold(modelHigher)}.</>;
  }
  // Degenerate but real: an index where the model never rates a god above the
  // community still has to say something true rather than "underrates 0".
  if (metaHigher > 0) {
    return <>The community overrates {gold(metaHigher)}.</>;
  }
  return <>The community and this model agree on all {gold(ranked)}.</>;
}

function StateBlock({ board, tierlist, source, ranked }: {
  board: ReturnType<typeof buildDivergenceBoard>;
  tierlist?: TierListData;
  source?: IndexData["community_source"];
  ranked: number;
}) {
  const comparable = ranked > 0;
  return (
    <header className="border-b border-line pb-6">
      {/* Two columns that do different jobs: the argument, and the evidence
          for it. This used to be the claim beside a search field; when search
          moved into the shell the right column was left holding a single
          16px line of counts, leaving a 645px hole across the middle of the
          page's most important block — and those counts already appeared in
          the subject header two rules above. */}
      <div className="flex flex-col gap-8 lg:flex-row lg:items-end lg:gap-12">
        <div className="min-w-0 lg:max-w-[46ch]">
          <h1 className="max-w-[19ch] text-balance font-display text-display font-bold leading-[1.1] tracking-[-0.01em] text-ink sm:text-display">
            {comparable ? <Claim board={board} /> : <>Builds scored by a model, not by what&rsquo;s popular.</>}
          </h1>
          {/* "the community's high-elo meta" overclaimed twice over: the
              signal is win rates from top-ranked Conquest play, not a meta
              anyone published, and "meta" implied a considered consensus
              ranking. And "it'd move N the other way" collides with the
              headline's own count whenever the two happen to match — as they
              currently do, at 24 each — so it says "another". */}
          <p className="mt-3 max-w-[64ch] text-body leading-relaxed text-ink-soft">
            ichor fits a gold-value model to item stats to find what&rsquo;s underpriced for a
            god&rsquo;s kit, then weighs that against community win rates from top-ranked
            Conquest play.
            {comparable
              ? <> It&rsquo;d move another {board.metaHigher} the other way, and it agrees on the rest.</>
              : " Community comparison isn't in this index yet, so nothing below is ranked against it."}
          </p>
        </div>

        {comparable && <BiggestArguments tierlist={tierlist} source={source} />}
      </div>
    </header>
  );
}

/** What the two marks are. The rungs no longer need explaining here — each bar
 * now names its own tiers underneath, so the only thing left to say is which
 * mark belongs to whom. */
function BoardKey() {
  return (
    <div className="flex flex-wrap items-center gap-x-5 gap-y-2 text-label text-faint">
      <span className="flex items-center gap-1.5">
        <span aria-hidden="true" className="inline-block h-3.5 w-[2px] rounded-[1px] bg-ink" />
        Community
      </span>
      <span className="flex items-center gap-1.5">
        <span aria-hidden="true" className="mark inline-block h-4 w-[9px] bg-gold" />
        Us
      </span>
      <span className="flex items-center gap-1.5">
        <span aria-hidden="true" className="inline-block h-[3px] w-6 rounded-[1px] bg-under/45" />
        We&rsquo;d rank higher
      </span>
      <span className="flex items-center gap-1.5">
        <span aria-hidden="true" className="inline-block h-[3px] w-6 rounded-[1px] bg-premium/45" />
        We&rsquo;d rank lower
      </span>
    </div>
  );
}

/** A single god's disagreement: who it is, our verdict on it, and the two
 * placements that verdict comes from. */
function DivergenceRow({ row }: { row: Divergence }) {
  return (
    <li>
      <button
        type="button"
        onClick={() => navigate(toHash.god(row.name))}
        // The arithmetic isn't gone, it's demoted: spoken in full here, on
        // hover in the tooltip, and in full on the god's own page.
        aria-label={`${row.name}: we place it ${row.tierOurs}, the community places it ${row.tierCommunity} — ${VERDICT_SPOKEN[row.verdict]}. Model score ${row.ours.toFixed(2)}, community ${row.community.toFixed(2)}.`}
        title={`${row.name} — model ${row.ours.toFixed(2)} · community ${row.community.toFixed(2)} (${deltaText(row.delta)})`}
        className="press grid w-full grid-cols-[20px_minmax(0,1fr)_auto] items-center gap-x-2 gap-y-1.5 rounded-md px-1.5 py-1.5 text-left transition-colors duration-[150ms] ease-standard hover:bg-bg2"
      >
        <GodIcon name={row.name} className="h-5 w-5" />
        <span className="truncate font-display text-small font-semibold text-ink">{row.name}</span>
        <span aria-hidden="true" className={`shrink-0 text-label ${VERDICT_TEXT[row.verdict]}`}>
          {VERDICT_WORD[row.verdict]}
        </span>
        <span className="col-span-3 block">
          <TierLadder ourStep={row.ourStep} theirStep={row.theirStep} verdict={row.verdict} />
        </span>
      </button>
    </li>
  );
}

const ROWS_PER_LANE = 6;

/** One lane, ranked by how hard the two sources disagree. The column header
 * carries the lane's overall lean, which is where a systematic pattern —
 * every Carry rated below the meta, say — becomes visible. */
function LaneBoardColumn({ col, index }: { col: LaneColumn; index: number }) {
  const shown = col.rows.slice(0, ROWS_PER_LANE);
  const rest = col.rows.length - shown.length;

  return (
    <section
      style={{ ["--bar-delay" as string]: `${index * 70}ms` }}
      className="min-w-0 xl:border-l xl:border-line xl:pl-4 xl:first:border-l-0 xl:first:pl-0"
    >
      <h3 className={`font-display text-body font-bold tracking-[0.02em] ${laneTextClass(col.lane)}`}>
        {col.lane}
      </h3>
      {/* The lane's lean moved up into `LaneLeans`, which compares all five
          at once; repeating it here put the same figure 200px from itself. */}
      {col.rows.length === 0 && (
        <p className="mt-0.5 text-label text-faint">no ranked gods</p>
      )}

      <ul className="mt-2.5 flex flex-col border-t border-line pt-1.5">
        {shown.map((row) => <DivergenceRow key={row.name} row={row} />)}
      </ul>

      {(rest > 0 || col.unranked > 0) && (
        <p className="mt-1.5 px-1.5 text-label text-faint">
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
        <h2 id="home-divergence-h" className="font-display text-lead font-bold text-ink">
          Where we disagree
        </h2>
        <a
          href={toHash.tiers()}
          className="press -my-1 rounded-sm px-1 py-1.5 text-label font-medium text-blue hover:underline"
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
          <LaneBoardColumn key={col.lane} col={col} index={i} />
        ))}
      </div>

      {board.unranked > 0 && (
        <p className="mt-6 max-w-[72ch] border-t border-line pt-3 text-small leading-relaxed text-muted">
          <span className="text-ink-soft">{board.unranked} of {board.total} gods have no community data yet.</span>{" "}
          They&rsquo;re left unranked rather than given an invented tier, so they don&rsquo;t appear above —
          the model still scores them on their own.
        </p>
      )}
    </section>
  );
}

/* ── Draft ───────────────────────────────────────────────────────────────
 * The draft board is the one surface that *changes* a build rather than
 * reporting one, and nothing in the app pointed at it — you met it by clicking
 * an icon in the rail and guessing. It also remembers a comp across sessions,
 * so a half-entered draft is worth handing back rather than leaving parked in
 * localStorage where only the rail icon can find it.
 */
function DraftSeam() {
  const { draft, mode } = useDraft();
  const allies = draft.allies.filter(Boolean);
  const enemies = draft.enemies.filter(Boolean);
  const started = allies.length + enemies.length > 0;
  const size = MODE_TEAM_SIZE[mode];
  const modeLabel = mode === "joust" ? "Joust" : "Conquest";
  // Only the first ally slot has a build behind it — that god's core is the
  // one thing the draft page adapts. With the slot empty there is nothing to
  // adapt, however many enemies are entered, so the two cases read differently.
  const you = draft.allies[0];

  return (
    <section data-testid="home-draft" aria-labelledby="home-draft-h" className="border-t border-line pt-6">
      <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-2">
        <h2 id="home-draft-h" className={sectionLabel}>
          {started ? "Your draft in progress" : "Drafting a match"}
        </h2>
        <a
          href={started ? encodeDraftHash(mode, draft) : toHash.draft()}
          className="press -my-1 rounded-sm px-1 py-1.5 text-label font-medium text-blue hover:underline"
        >
          {started ? "Resume draft →" : "Open the draft board →"}
        </a>
      </div>

      {started ? (
        <>
          <div className="mt-3 flex flex-wrap items-center gap-x-3 gap-y-2">
            <span className="flex flex-wrap items-center gap-1.5">
              {allies.map((n) => <GodIcon key={n} name={n} className="h-7 w-7" />)}
              {allies.length === 0 && <span className="text-small text-faint">no allies yet</span>}
            </span>
            <span aria-hidden="true" className="text-small text-faint">vs</span>
            <span className="flex flex-wrap items-center gap-1.5">
              {enemies.map((n) => <GodIcon key={n} name={n} className="h-7 w-7" />)}
              {enemies.length === 0 && <span className="text-small text-faint">no enemies yet</span>}
            </span>
          </div>
          {/* Named, because two rows of portraits don't say which side is
              which — and the enemy count is what decides how much the build
              can actually adapt. */}
          <p className="mt-2 max-w-[68ch] text-small leading-relaxed text-muted">
            {modeLabel} · <span className="text-ink-soft">{allies.length} of {size}</span> allies
            {" · "}<span className="text-ink-soft">{enemies.length} of {size}</span> enemies.
            {/* Never "the build already answers those picks" — whether any item
                actually moved is what the board is for, and it may well
                report that nothing did. */}
            {!you
              ? " Your own slot is empty, so there's no build to adapt yet."
              : enemies.length === 0
                ? ` Add an enemy and it starts weighing ${you}'s core against them.`
                : ` It's weighing ${you}'s core against ${enemies.length === 1 ? "that pick" : "those picks"}.`}
          </p>
        </>
      ) : (
        <p className="mt-2 max-w-[68ch] text-body leading-relaxed text-muted">
          Enter your god and the enemies you know, and the model re-sorts that god&rsquo;s core around
          them — named items displacing named items, for stated reasons. It&rsquo;s the one place a
          build answers a specific match instead of the average one.
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
      <h2 id="home-pinned-h" className={sectionLabel}>Your pinned gods</h2>
      {pinnedGods.length === 0 ? (
        <p className="mt-2 max-w-[68ch] text-body text-muted">
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
                  <span className="max-w-[110px] truncate font-display text-small font-semibold text-ink">{g.name}</span>
                  {lane && <span className={`text-label ${laneTextClass(lane)}`}>{lane}</span>}
                </button>
                <button
                  type="button"
                  onClick={() => toggle(g.name)}
                  aria-label={`Unpin ${g.name}`}
                  className="press absolute right-0.5 top-1/2 -translate-y-1/2 rounded-sm px-1.5 py-1 text-label leading-none text-faint opacity-0 transition-opacity duration-[150ms] hover:text-ink focus-visible:opacity-100 group-hover:opacity-100"
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
        <h2 id="home-patch-h" className={sectionLabel}>Latest patch changes</h2>
        <a href={toHash.patch()} className="press -my-1 rounded-sm px-1 py-1.5 text-label font-medium text-blue hover:underline">
          All patch notes →
        </a>
      </div>
      <div className="mt-3 flex flex-wrap items-baseline gap-x-3 gap-y-1 text-label text-faint">
        <span className="font-mono">{latest.from} → {latest.to}</span>
        {counts && <span className="text-muted">{counts}</span>}
      </div>
      <div className="mt-2 flex flex-wrap gap-1.5">
        {latest.changed.map((d) => (
          <span key={d.name} className="rounded-sm border border-line bg-bg2 px-2 py-1 text-label text-ink-soft">{d.name}</span>
        ))}
        {latest.added.map((n) => (
          <span key={n} className="rounded-sm border border-blue/30 bg-blue/10 px-2 py-1 text-label font-semibold text-blue">{n}</span>
        ))}
        {latest.removed.map((n) => (
          <span key={n} className="rounded-sm border border-line px-2 py-1 text-label text-muted line-through">{n}</span>
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
    <p data-testid="home-freshness" title={dataUpdated} className="border-t border-line pt-4 text-label text-faint">
      Updated {relativeDate(dataUpdated)}{dataPatch ? ` · ${dataPatch}` : ""}
    </p>
  );
}

export function Home({ data }: { data: IndexData }) {
  const board = useMemo(() => buildDivergenceBoard(data.tierlist?.gods), [data.tierlist]);

  return (
    <div className="mx-auto w-full max-w-[1440px] px-4 pb-12 pt-7 sm:px-6 sm:pt-9">
      <StateBlock board={board} tierlist={data.tierlist} source={data.community_source} ranked={board.ranked} />
      <DivergenceBoard board={board} />
      <div className="mt-7 flex flex-col gap-6">
        <DraftSeam />
        <PinnedSection gods={data.gods} />
        <LatestPatch periods={data.patch_notes} />
        <Freshness dataUpdated={data.data_updated} dataPatch={data.data_patch} />
      </div>
    </div>
  );
}
