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
import type { God, IndexData, PatchPeriod } from "../types";
import { toHash, navigate } from "../lib/useHashRoute";
import { usePins } from "../lib/pins";
import { iconSlug } from "../lib/builds";
import { godLane, laneTextClass } from "../lib/roleAccent";
import { relativeDate } from "../lib/relativeDate";
import { useDraft, encodeDraftHash, MODE_TEAM_SIZE } from "../lib/draft";
import {
  buildDivergenceBoard, stepPercent, deltaText,
  type Divergence, type LaneColumn, type Verdict,
} from "../lib/divergence";
import { TIER_STEPS, type TierLetter } from "../lib/tierBands";

/** The one label style shared by the sections below the board. */
const sectionLabel = "font-mono text-label uppercase tracking-[0.1em] text-faint";

/** The ladder, left to right. A tier list is drawn S-first, but an axis that
 *  improves rightward is the one people read off a scoreboard. */
const LADDER: TierLetter[] = ["C", "B", "A", "S"];

/* The verdict, in the words this audience already argues in.
 *
 * The page used to state a disagreement as a signed number (`+0.15`) beside
 * two raw scores, which asks the reader to know what 0.15 is worth before it
 * says anything at all. `under`/`premium` still carry the direction — the same
 * pair, meaning the same thing they mean on items and in the tier list — but
 * the row now leads with the claim and keeps the arithmetic in its tooltip and
 * its accessible name. */
const VERDICT_WORD: Record<Verdict, string> = {
  underrated: "Underrated",
  overrated: "Overrated",
  agreed: "Agreed",
};
const VERDICT_TEXT: Record<Verdict, string> = {
  underrated: "text-under",
  overrated: "text-premium",
  agreed: "text-faint",
};
/** Only the two directions get a mark of our own: on agreement the two
 *  placements coincide, and the ladder draws the single shared mark instead. */
const VERDICT_MARK: Record<Exclude<Verdict, "agreed">, string> = {
  underrated: "bg-under",
  overrated: "bg-premium",
};
/** Spoken form, for the row's accessible name — "Underrated" alone doesn't say
 *  who is doing the underrating. */
const VERDICT_SPOKEN: Record<Verdict, string> = {
  underrated: "we rate it higher",
  overrated: "we rate it lower",
  agreed: "both agree",
};

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

/* ── The evidence ────────────────────────────────────────────────────────
 * Which lanes the two sources argue about, compared side by side. The board
 * below answers "who, within a lane"; it cannot answer "which lane is the
 * argument" without reading five column headers and holding them in memory.
 * So the comparison lives here and the board's columns stop repeating it.
 */
function LaneLeans({ board }: { board: ReturnType<typeof buildDivergenceBoard> }) {
  return (
    <section aria-labelledby="home-leans-h" className="w-full lg:max-w-[600px] lg:flex-1">
      <div className="flex items-baseline justify-between gap-3">
        <h2 id="home-leans-h" className={sectionLabel}>Which lanes we argue about</h2>
        <span className="text-label text-faint">we&rsquo;d re-rank</span>
      </div>
      <ul className="mt-2 flex flex-col border-t border-line">
        {board.lanes.map((col) => {
          const n = col.rows.length;
          return (
            <li key={col.lane}
              className="grid grid-cols-[4.5rem_minmax(0,1fr)_3.5rem] items-center gap-x-2.5 border-b border-line py-1.5">
              <span className={`truncate text-small font-semibold ${laneTextClass(col.lane)}`}>
                {col.lane}
              </span>
              {n === 0 ? (
                <span className="col-span-2 text-label text-faint">no ranked gods</span>
              ) : (
                <>
                  {/* Counts, not an average. "Mean gap −0.05" is a sentence
                      about the model; "9 of 13 we'd move" is a sentence about
                      the lane, and it's the one a player can act on. */}
                  <span aria-hidden="true" className="flex h-[6px] overflow-hidden rounded-[1px] bg-bg3">
                    <span className="bar-grow h-full origin-left bg-under"
                      style={{ width: `${(col.underrated / n) * 100}%` }} />
                    <span className="bar-grow h-full origin-left bg-premium"
                      style={{ width: `${(col.overrated / n) * 100}%` }} />
                  </span>
                  <span className="text-right text-label text-faint">
                    <span className="font-mono text-muted">{col.tierDiffer}</span> of{" "}
                    <span className="font-mono">{n}</span>
                  </span>
                </>
              )}
            </li>
          );
        })}
      </ul>
      <p className="mt-2 max-w-[46ch] text-label leading-relaxed text-faint">
        Green is gods we&rsquo;d move up from where the meta has them, red gods we&rsquo;d move down.
        The longer the colour, the more of that lane we&rsquo;d argue about.
      </p>
    </section>
  );
}

/* ── The claim ───────────────────────────────────────────────────────────
 * The page's one argument, with every number in it computed from the index
 * rather than written down. When there's no tier list to compare against, the
 * claim steps back to what the model does instead of inventing a statistic.
 */
function StateBlock({ board, disagreements, ranked }: {
  board: ReturnType<typeof buildDivergenceBoard>;
  disagreements: number;
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
            {comparable ? (
              <>We disagree with the meta on{" "}
                <span className="text-gold">{disagreements} of {ranked}</span>{" "}
                ranked gods.
              </>
            ) : (
              <>Builds scored by a model, not by what&rsquo;s popular.</>
            )}
          </h1>
          <p className="mt-3 max-w-[64ch] text-body leading-relaxed text-ink-soft">
            ichor fits a gold-value model to item stats to find what&rsquo;s underpriced for a
            god&rsquo;s kit, then weighs that against the community&rsquo;s high-elo meta.
            {comparable
              ? " Where the two part ways, it says so — by lane, biggest argument first."
              : " Community comparison isn't in this index yet, so nothing below is ranked against the meta."}
          </p>
        </div>

        {comparable && <LaneLeans board={board} />}
      </div>
    </header>
  );
}

/** The empty ladder — four rungs, worst to best. Shared by the legend and
 *  every row so the cell geometry can't drift between the two. */
function LadderCells() {
  return (
    <span className="absolute inset-0 grid grid-cols-4 gap-[3px]">
      {Array.from({ length: TIER_STEPS }, (_, i) => (
        <span key={i} className="rounded-[1px] bg-bg3" />
      ))}
    </span>
  );
}

/**
 * One god's placement on the tier ladder: where the community puts them, where
 * we put them, and the run between the two.
 *
 * The old bar drew the *raw score gap* outward from a centre tick, which asked
 * the reader to already know what 0.17 was worth — and quietly compared two
 * numbers that aren't on a shared scale (0.53 is S-tier for the model, but the
 * community's S starts near 0.64). Rungs are the comparison this audience
 * already reads, and they're the honest one: each source is placed by its own
 * tier letter, so the distance between the marks means exactly what it looks
 * like it means.
 */
function Ladder({ row }: { row: Divergence }) {
  const from = Math.min(row.ourStep, row.theirStep);
  const to = Math.max(row.ourStep, row.theirStep);
  const under = row.verdict === "underrated";
  const agreed = row.verdict === "agreed";
  return (
    <span aria-hidden="true" className="relative block h-2.5">
      <LadderCells />
      {!agreed && (
        // Grows from the community's rung toward ours: the animation traces
        // the argument in the direction the argument runs.
        <span
          className={`bar-grow absolute inset-y-0 rounded-[1px] ${
            under ? "origin-left bg-under/40" : "origin-right bg-premium/40"}`}
          style={{ left: `${stepPercent(from)}%`, width: `${stepPercent(to) - stepPercent(from)}%` }}
        />
      )}
      {/* The community's placement — the baseline the reader already holds.
          When both agree the two marks coincide, so only this one is drawn:
          a single mark reads as "one answer", which is what agreement is. */}
      <span className="absolute -top-0.5 h-[14px] w-[2px] -translate-x-1/2 rounded-[1px] bg-ink"
        style={{ left: `${stepPercent(row.theirStep)}%` }} />
      {row.verdict !== "agreed" && (
        <span className={`absolute -top-0.5 h-[14px] w-[3px] -translate-x-1/2 rounded-[1px] ${VERDICT_MARK[row.verdict]}`}
          style={{ left: `${stepPercent(row.ourStep)}%` }} />
      )}
    </span>
  );
}

/** The encoding, decoded once, in place — so the rows below never need a
 * remembered schema. */
function BoardKey() {
  return (
    <div className="flex flex-wrap items-center gap-x-5 gap-y-2 text-label text-faint">
      <span className="flex items-center gap-2">
        <span aria-hidden="true" className="relative block h-2.5 w-[88px]">
          <LadderCells />
          <span className="absolute inset-0 grid grid-cols-4 gap-[3px]">
            {LADDER.map((t) => (
              <span key={t} className="text-center font-mono text-micro leading-[10px] text-faint">{t}</span>
            ))}
          </span>
        </span>
        Tier ladder
      </span>
      <span className="flex items-center gap-1.5">
        <span aria-hidden="true" className="inline-block h-3.5 w-[2px] rounded-[1px] bg-ink" />
        Where the meta puts them
      </span>
      <span className="flex items-center gap-1.5">
        <span aria-hidden="true" className="inline-block h-3.5 w-[3px] rounded-[1px] bg-under" />
        We&rsquo;d rank higher
      </span>
      <span className="flex items-center gap-1.5">
        <span aria-hidden="true" className="inline-block h-3.5 w-[3px] rounded-[1px] bg-premium" />
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
        <span className="col-span-3">
          <Ladder row={row} />
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
      <StateBlock
        board={board}
        disagreements={board.tierDisagreements}
        ranked={board.ranked}
      />
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
