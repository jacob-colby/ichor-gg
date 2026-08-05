/* THESIS: Home owns one idea — this roster is measured, and some of what wins
 * is not what gets played. It used to own a different one: "where this model
 * disagrees with the meta, and why that disagreement is the product." That
 * disagreement was the headline and it did not survive measurement. The god
 * ranking behind it correlated -0.117 with real god strength, the item ranking
 * -0.267 with item win rate, and "51 of 87 placed differently" was LESS
 * disagreement than two unrelated rankings produce (75%). What replaced it is
 * a claim about the community's own two numbers — how much a god wins, and how
 * often anyone plays it — which is a gap we can actually evidence.
 * OWN-WORLD: Arena Night, unchanged. Near-black stepped surfaces, hairline
 * rules instead of cards, mono micro-labels, torchlight gold kept rare. `under`
 * now marks one thing only: wins well, rarely played.
 * STORY: a player sees the roster ranked on real results, finds their lane, and
 * spots a god worth learning because nobody else has.
 * FIRST VIEWPORT: a claim in display type with its numbers computed live, the
 * sample it rests on, and the handful of names worth acting on.
 * FORM: Lane Board, position 3 of the ordered list, seed key c96ae713.
 */
import { useMemo, useState } from "react";
import type { God, IndexData, ItemTierEntry, PatchPeriod, TierListData } from "../types";
import { toHash, navigate } from "../lib/useHashRoute";
import { usePins } from "../lib/pins";
import { iconSlug } from "../lib/builds";
import { godLane, laneTextClass } from "../lib/roleAccent";
import { relativeDate } from "../lib/relativeDate";
import { useDraft, encodeDraftHash, MODE_TEAM_SIZE } from "../lib/draft";
import {
  buildStandingsBoard, rateText, matchesText,
  type Standing, type LaneColumn,
} from "../lib/standings";
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

/* ── Worth acting on ────────────────────────────────────────────────────
 * The handful of names a player can do something with.
 *
 * This block used to name "where we argue hardest" — the gods and items our
 * model placed furthest from the community. Those arguments turned out to be
 * noise dressed as insight, so what is named here is measured instead:
 *
 *   Gods   win well and are rarely played. Both figures are the community's
 *          own, so this points at a gap inside their data rather than claiming
 *          we know better than it. The usual objection — that rare gods look
 *          strong because only specialists play them — runs the other way in
 *          this data (play share against raw win rate is +0.25), and the
 *          ranking is a lower bound, so a thin sample is penalised before it
 *          can qualify.
 *   Items  carry the most stats per gold. That is exactly what the gold model
 *          measures and all it measures: it does NOT predict whether an item
 *          wins (correlation -0.267), so the label says what was measured and
 *          the item's own win rate is printed beside it.
 */
const NAMES_SHOWN = 3;

function NameRow({ name, item, figure, note, tone }: {
  name: string; item: boolean; figure: string; note: string; tone: string;
}) {
  return (
    <li>
      <a
        href={item ? toHash.item(name) : toHash.god(name)}
        aria-label={name + ": " + note}
        className="press grid grid-cols-[20px_minmax(0,1fr)_auto] items-center gap-x-2 rounded-md px-1.5 py-1.5 transition-colors duration-[150ms] ease-standard hover:bg-bg2"
      >
        <GodIcon name={name} item={item} className="h-5 w-5" />
        <span className="truncate font-display text-small font-semibold text-ink">{name}</span>
        <span aria-hidden="true" className={"text-right font-mono text-label " + tone}>{figure}</span>
      </a>
    </li>
  );
}

function WorthActingOn({ board, tierlist, source }: {
  board: ReturnType<typeof buildStandingsBoard>;
  tierlist?: TierListData;
  source?: IndexData["community_source"];
}) {
  const hidden = useMemo(
    () => board.lanes
      .flatMap((c) => c.rows)
      .filter((r) => r.underplayed)
      .sort((a, b) => b.score - a.score)
      .slice(0, NAMES_SHOWN),
    [board],
  );
  // Full items only. Tiers 1-2 are components and starters — things you pass
  // through, not things you choose — so "best value" among them is not a
  // choice anybody makes.
  const value = useMemo(
    () => ((tierlist?.items ?? []) as ItemTierEntry[])
      .filter((e) => e.tier === 3 && typeof e.value === "number")
      .sort((a, b) => (b.value ?? 0) - (a.value ?? 0))
      .slice(0, NAMES_SHOWN),
    [tierlist],
  );
  if (hidden.length === 0 && value.length === 0) return null;

  return (
    <section aria-labelledby="home-names-h" className="w-full lg:max-w-[600px] lg:flex-1">
      <h2 id="home-names-h" className={sectionLabel}>Worth a look</h2>

      {hidden.length > 0 && (
        <>
          <p className="mt-2.5 border-t border-line pt-2 text-label text-faint">
            <span className="text-ink-soft">Gods that win and nobody plays</span>
            <span className="px-1">·</span>
            <span className="font-mono">{board.underplayed}</span> of{" "}
            <span className="font-mono">{board.ranked}</span> measured
          </p>
          <ul className="mt-0.5 flex flex-col">
            {hidden.map((r) => (
              <NameRow key={r.name} name={r.name} item={false} tone="text-under"
                figure={rateText(r.winRate) + " · " + rateText(r.playShare) + " played"}
                note={"wins " + rateText(r.winRate) + " over " + matchesText(r.matches)
                      + " matches, played in " + rateText(r.playShare) + " of them"} />
            ))}
          </ul>
        </>
      )}

      {value.length > 0 && (
        <>
          <p className="mt-2.5 border-t border-line pt-2 text-label text-faint">
            <span className="text-ink-soft">Most stats per gold</span>
            <span className="px-1">·</span>
            what the item model measures, and all it measures
          </p>
          <ul className="mt-0.5 flex flex-col">
            {value.map((e) => (
              <NameRow key={e.name} name={e.name} item tone="text-ink-soft"
                figure={rateText(e.win_rate) + " win"}
                note={"cheap for its stats; wins " + rateText(e.win_rate)} />
            ))}
          </ul>
        </>
      )}

      <CommunitySource source={source} className="mt-2.5 border-t border-line pt-2" />
    </section>
  );
}

/* ── The claim ──────────────────────────────────────────────────────────
 * The page's one argument, every number in it computed from the index rather
 * than written down.
 *
 * It used to read "The community underrates 26 gods" — which rested on our
 * model out-ranking theirs, and measurement did not support that. What it says
 * now needs no such claim: both halves are the community's own figures, and
 * the sentence only points at the distance between them.
 */
function Claim({ board }: { board: ReturnType<typeof buildStandingsBoard> }) {
  const gold = (n: number) => <span className="text-gold">{n} god{n === 1 ? "" : "s"}</span>;
  if (board.underplayed > 0) {
    return <>{gold(board.underplayed)} win more than anyone plays them.</>;
  }
  return <>{gold(board.ranked)} ranked on results, not on guesswork.</>;
}

function StateBlock({ board, tierlist, source, ranked }: {
  board: ReturnType<typeof buildStandingsBoard>;
  tierlist?: TierListData;
  source?: IndexData["community_source"];
  ranked: number;
}) {
  const measured = ranked > 0;
  return (
    <header className="border-b border-line pb-6">
      <div className="flex flex-col gap-8 lg:flex-row lg:items-end lg:gap-12">
        <div className="min-w-0 lg:max-w-[46ch]">
          <h1 className="max-w-[19ch] text-balance font-display text-display font-bold leading-[1.1] tracking-[-0.01em] text-ink sm:text-display">
            {measured ? <Claim board={board} /> : <>Builds with the reasoning shown.</>}
          </h1>
          <p className="mt-3 max-w-[64ch] text-body leading-relaxed text-ink-soft">
            ichor builds every god a six-item core and shows its working — what each item costs
            against what its stats are worth, and what this god&rsquo;s players actually buy instead.
            {measured
              ? <> Gods are ranked on their own win rates in top-ranked Conquest play,
                  never on anything this site models.</>
              : " No community results in this index yet, so nothing below is ranked."}
          </p>
        </div>

        {measured && <WorthActingOn board={board} tierlist={tierlist} source={source} />}
      </div>
    </header>
  );
}

/** What the marks mean. One ranking now, not two, so the only things left to
 * explain are the direction of a bar and the one flag on the page. */
function BoardKey() {
  return (
    <div className="flex flex-wrap items-center gap-x-5 gap-y-2 text-label text-faint">
      <span className="flex items-center gap-1.5">
        <span aria-hidden="true" className="inline-block h-[3px] w-6 rounded-[1px] bg-gold/70" />
        Wins above even
      </span>
      <span className="flex items-center gap-1.5">
        <span aria-hidden="true" className="inline-block h-[3px] w-6 rounded-[1px] bg-line-strong" />
        Below even
      </span>
      <span className="flex items-center gap-1.5">
        <span aria-hidden="true" className="text-under">rare</span>
        Wins well, rarely played
      </span>
    </div>
  );
}

/** A win rate drawn as its distance from even.
 *
 * The old bar drew two placements on a tier ladder, which only meant something
 * while there were two rankings. This draws the one number the row is ranked
 * on. Even sits at the centre so the eye reads direction before magnitude: the
 * whole roster lives between about 36% and 58%, and a bar drawn from zero would
 * make every god look identical. */
const WIN_SPAN = 0.12;   // ±12 points covers the observed range with room.

function WinBar({ rate }: { rate: number | null }) {
  if (rate == null) return null;
  const offset = Math.max(-1, Math.min(1, (rate - 0.5) / WIN_SPAN));
  const pct = Math.abs(offset) * 50;
  const above = offset >= 0;
  return (
    <span aria-hidden="true" className="relative block h-[3px] w-full rounded-[1px] bg-bg3">
      <span
        className={"absolute top-0 h-full rounded-[1px] " + (above ? "bg-gold/70" : "bg-line-strong")}
        style={above ? { left: "50%", width: pct + "%" } : { right: "50%", width: pct + "%" }}
      />
      <span className="absolute left-1/2 top-[-2px] h-[7px] w-px -translate-x-1/2 bg-line" />
    </span>
  );
}

/** One god: who it is, what it wins, and how much play that rests on. */
function StandingRow({ row }: { row: Standing }) {
  return (
    <li>
      <button
        type="button"
        onClick={() => navigate(toHash.god(row.name))}
        aria-label={row.name + ": " + row.band + " tier, wins " + rateText(row.winRate)
          + " over " + (row.matches?.toLocaleString("en-US") ?? "an unreported number of")
          + " matches, played in " + rateText(row.playShare) + " of them"
          + (row.underplayed ? " — wins well and is rarely played" : "") + "."}
        title={row.name + " — " + rateText(row.winRate) + " win over "
          + (row.matches?.toLocaleString("en-US") ?? "?") + " matches · "
          + rateText(row.playShare) + " play share"}
        className="press grid w-full grid-cols-[20px_minmax(0,1fr)_auto_auto] items-center gap-x-2 gap-y-1.5 rounded-md px-1.5 py-1.5 text-left transition-colors duration-[150ms] ease-standard hover:bg-bg2"
      >
        <GodIcon name={row.name} className="h-5 w-5" />
        <span className="truncate font-display text-small font-semibold text-ink">
          {row.name}
          {row.underplayed && (
            <span aria-hidden="true" className="ml-1.5 align-middle text-label text-under">rare</span>
          )}
        </span>
        <span aria-hidden="true" className="shrink-0 font-mono text-label text-ink-soft">
          {rateText(row.winRate)}
        </span>
        {/* How much play the row rests on. Two rows read as equally sure
            without it, and these run from 44 matches to 670. */}
        <span aria-hidden="true" className="shrink-0 font-mono text-micro text-faint">
          {matchesText(row.matches)}
        </span>
        <span className="col-span-4 block">
          <WinBar rate={row.winRate} />
        </span>
      </button>
    </li>
  );
}

const ROWS_PER_LANE = 6;

/** One lane, best first. */
function LaneBoardColumn({ col, index }: { col: LaneColumn; index: number }) {
  const shown = col.rows.slice(0, ROWS_PER_LANE);
  const rest = col.rows.length - shown.length;

  return (
    <section
      style={{ ["--bar-delay" as string]: index * 70 + "ms" }}
      className="min-w-0 xl:border-l xl:border-line xl:pl-4 xl:first:border-l-0 xl:first:pl-0"
    >
      <h3 className={"font-display text-body font-bold tracking-[0.02em] " + laneTextClass(col.lane)}>
        {col.lane}
      </h3>
      {col.rows.length === 0 && (
        <p className="mt-0.5 text-label text-faint">no measured gods</p>
      )}

      <ul className="mt-2.5 flex flex-col border-t border-line pt-1.5">
        {shown.map((row) => <StandingRow key={row.name} row={row} />)}
      </ul>

      {(rest > 0 || col.unmeasured > 0) && (
        <p className="mt-1.5 px-1.5 text-label text-faint">
          {rest > 0 && <>+{rest} more</>}
          {rest > 0 && col.unmeasured > 0 && <span className="px-1">·</span>}
          {col.unmeasured > 0 && <>{col.unmeasured} not measured</>}
        </p>
      )}
    </section>
  );
}

/** The board. Absent entirely on an index with no results — the same rule the
 * rest of this page follows, rather than an empty shell. */
function StandingsBoard({ board }: { board: ReturnType<typeof buildStandingsBoard> }) {
  if (board.ranked === 0) return null;

  return (
    <section data-testid="home-standings" aria-labelledby="home-standings-h" className="pt-7">
      <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-2">
        <h2 id="home-standings-h" className="font-display text-lead font-bold text-ink">
          What actually wins
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

      <div className="mt-4 grid grid-cols-1 gap-x-5 gap-y-7 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5">
        {board.lanes.map((col, i) => (
          <LaneBoardColumn key={col.lane} col={col} index={i} />
        ))}
      </div>

      {board.unmeasured > 0 && (
        <p className="mt-6 max-w-[72ch] border-t border-line pt-3 text-small leading-relaxed text-muted">
          <span className="text-ink-soft">{board.unmeasured} of {board.total} gods have too few tracked matches to place.</span>{" "}
          They&rsquo;re left out rather than given an invented tier &mdash; &ldquo;we didn&rsquo;t measure this&rdquo;
          and &ldquo;this is bad&rdquo; are different facts. Their builds work the same.
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
 *
 * The seam existed and was still being missed, because it had opted out of
 * every strong move the page makes. Its heading used `sectionLabel` — 11px
 * mono in `faint`, the quietest tier the system has — while the board above it
 * gets display/lead/bold/`ink`; and it sat in one flat `gap-6` stack with the
 * pinned list and the "updated 4 days ago" line, hairline rule and all. The
 * app's only interactive surface was filed as footer chrome.
 *
 * Now a raised plane, in the system's own vocabulary and nothing new:
 *
 *   `.plane`        Ground Plane Rule — a real panel catching the page light.
 *                   Reserved for cards, dialogs and the subject header, which
 *                   is the company this belongs in, not chips and pills.
 *   `.is-selected`  the gold ring, but ONLY while a draft is live. "Torchlight
 *                   gold marks whatever matters right now" is the brief's own
 *                   sentence, and a comp the app is holding for you is exactly
 *                   that. At rest the panel is flat, so the ring stays a state
 *                   rather than decoration (Flat-Until-It-Matters).
 *   gold button     the Torchlight Rule's third permitted use, primary action.
 *                   This is Home's one thing to *do*; it was an 11px blue text
 *                   link.
 *
 * The empty state previews the board's own slot vocabulary — the gold "you"
 * ring, then dashed slots — so the skeleton says "a match, and something to do
 * about it" before a word is read. Decorative and aria-hidden: the button is
 * the affordance, and two competing ones would blunt both.
 *
 * Everything below it (pinned, patch, freshness) keeps the quiet treatment on
 * purpose. The promotion is only legible because they didn't get one.
 */

/** The board's slot shapes, at rest — the gold ring for your own slot, dashed
 *  for the rest. Mirrors `DraftControls`' real slots so the preview is the
 *  interface rather than an illustration of it.
 *
 *  `you` is deliberately not defaulted. Gold means "this one is yours" and
 *  there is exactly one of those on a board; drawn on both rows it said the
 *  enemy team had a you-slot too. */
function SlotPreview({ count, you = false }: { count: number; you?: boolean }) {
  return (
    <span aria-hidden="true" className="flex items-center gap-1.5">
      {Array.from({ length: count }, (_, i) => (
        <span
          key={i}
          className={`h-7 w-7 flex-none rounded-md ${
            you && i === 0 ? "border-2 border-gold" : "border border-dashed border-line-strong"
          }`}
        />
      ))}
    </span>
  );
}

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
    <section
      data-testid="home-draft"
      aria-labelledby="home-draft-h"
      className={`plane rounded-lg border bg-bg2 p-4 sm:p-5 ${
        started ? "is-selected border-gold/40" : "border-line"
      }`}
    >
      <div className="flex flex-wrap items-center justify-between gap-x-4 gap-y-3">
        <div className="min-w-0">
          <h2 id="home-draft-h" className="font-display text-lead font-bold text-ink">
            {started ? "Your draft in progress" : "Build for the match you're in"}
          </h2>
          {!started && (
            <p className="mt-0.5 text-small text-muted">
              The one place a build answers a specific match instead of the average one.
            </p>
          )}
        </div>
        <a
          href={started ? encodeDraftHash(mode, draft) : toHash.draft()}
          className="press shrink-0 rounded-md bg-gold px-4 py-2 font-display text-small font-semibold text-bg0 transition-opacity duration-[150ms] ease-standard hover:opacity-90"
        >
          {started ? "Resume draft →" : "Open the draft board →"}
        </a>
      </div>

      {started ? (
        <>
          <div className="mt-3.5 flex flex-wrap items-center gap-x-3 gap-y-2 border-t border-line pt-3.5">
            <span className="flex flex-wrap items-center gap-1.5">
              {allies.map((n) => <GodIcon key={n} name={n} className="h-8 w-8" />)}
              {allies.length === 0 && <span className="text-small text-faint">no allies yet</span>}
            </span>
            <span aria-hidden="true" className="font-display text-small font-semibold text-faint">vs</span>
            <span className="flex flex-wrap items-center gap-1.5">
              {enemies.map((n) => <GodIcon key={n} name={n} className="h-8 w-8" />)}
              {enemies.length === 0 && <span className="text-small text-faint">no enemies yet</span>}
            </span>
          </div>
          {/* Named, because two rows of portraits don't say which side is
              which — and the enemy count is what decides how much the build
              can actually adapt. */}
          <p className="mt-2.5 max-w-[68ch] text-small leading-relaxed text-muted">
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
        <div className="mt-3.5 flex flex-wrap items-center gap-x-3 gap-y-3 border-t border-line pt-3.5">
          <SlotPreview count={3} you />
          <span aria-hidden="true" className="font-display text-small font-semibold text-faint">vs</span>
          <SlotPreview count={3} />
          <p className="min-w-[24ch] max-w-[52ch] flex-1 text-small leading-relaxed text-muted">
            Enter your god and the enemies you know, and the model re-sorts that god&rsquo;s core
            around them — named items displacing named items, for stated reasons.
          </p>
        </div>
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
  const board = useMemo(() => buildStandingsBoard(data.tierlist?.gods), [data.tierlist]);

  return (
    <div className="mx-auto w-full max-w-[1440px] px-4 pb-12 pt-7 sm:px-6 sm:pt-9">
      <StateBlock board={board} tierlist={data.tierlist} source={data.community_source} ranked={board.ranked} />
      <StandingsBoard board={board} />
      <div className="mt-7">
        <DraftSeam />
      </div>
      <div className="mt-6 flex flex-col gap-6">
        <PinnedSection gods={data.gods} />
        <LatestPatch periods={data.patch_notes} />
        <Freshness dataUpdated={data.data_updated} dataPatch={data.data_patch} />
      </div>
    </div>
  );
}
