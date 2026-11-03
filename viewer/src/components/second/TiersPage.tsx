/** Tiers (`#/tiers`): who actually wins, and how much play that rests on.
 *
 * One claim with its live numbers, then the bands as rows — a band's letter is
 * the verdict and is set large in neutral ink; each row carries the two
 * numbers a placement rests on, the win rate and the games behind it, and
 * never a 0–1 score. A rate without its sample reads equally sure at 44 games
 * and at 2,000, and the samples here span that range.
 *
 * Product truth kept from the old TierList (its comments carry the evidence):
 *  - The ranking is the Wilson lower bound of REAL outcomes; nothing the model
 *    computes goes into the order (the model's god ranking measured −0.117
 *    against real god strength).
 *  - Only Conquest has outcome data. Joust and Arena are UNRANKED: no letter,
 *    no order beyond A–Z, and a sentence saying why. Their builds still ship.
 *  - An entry with no usable sample sits in its own "Not measured" group and
 *    is never bottom-ranked — unmeasured and bad are different facts.
 *  - "Rarely played" is computed over the WHOLE measured roster, never a
 *    filtered view (lib/standings `findUnderplayed`), gods only.
 *  - Board state (mode, subject, order, lane) lives in the hash query.
 */
import { useMemo } from "react";
import type { AspectTierEntry, CommunitySource, GodTierEntry, ItemTierEntry, TierEntry, TierListData } from "../../types";
import { LANES, godInLane, godLane, laneTextClass, type Lane } from "../../lib/roleAccent";
import { buildBands, type BandEntry, type BandSort } from "../../lib/tierBands";
import { findUnderplayed } from "../../lib/standings";
import { useUrlState } from "../../lib/urlState";
import { toHash } from "../../lib/useHashRoute";
import { priceVerdict, PRICE_WORD } from "../../lib/verdictWords";
import { Art } from "./art";
import { ModeSwitch } from "./ModeSwitch";
import { RoleFilter } from "./GodGrid";
import { MODE_NAME, type Mode } from "./verdict";
import { Em, PageHead, Seam, TextTabs } from "./PageParts";
import { shortDate } from "./shortDate";

type Subject = "gods" | "aspects" | "items";
interface Board { mode: Mode; of: Subject; sort: BandSort; lane?: Lane }

const decode = (p: URLSearchParams): Board => {
  const m = p.get("mode");
  const of = p.get("of");
  const lane = p.get("lane");
  return {
    mode: m === "joust" || m === "arena" ? m : "conquest",
    of: of === "items" || of === "aspects" ? of : "gods",
    sort: p.get("sort") === "matches" ? "matches" : "score",
    lane: (LANES as readonly string[]).includes(lane ?? "") ? (lane as Lane) : undefined,
  };
};
const encode = (b: Board) => ({
  mode: b.mode === "conquest" ? undefined : b.mode,
  of: b.of === "gods" ? undefined : b.of,
  sort: b.sort === "score" ? undefined : b.sort,
  lane: b.lane,
});

const NOUN: Record<Subject, [string, string]> = { gods: ["god", "gods"], aspects: ["aspect", "aspects"], items: ["item", "items"] };
const SAMPLE: Record<Subject, string> = { gods: "god-games", aspects: "aspect games", items: "item purchases" };
const DIVISION: Record<string, string> = { obsidian: "Obsidian+", master: "Master+", deity: "Demigod/Deity" };

const num = (n: number) => n.toLocaleString("en-US");
const pct = (r: number | null | undefined) => (r == null ? "—" : `${Math.round(r * 100)}%`);
const shortAspect = (a?: string) => (a ?? "").replace(/^Aspect of (the )?/i, "");

function hrefFor(e: TierEntry, of: Subject, mode: Mode): string {
  if (of === "items") return toHash.item(e.name);
  const q = new URLSearchParams();
  if (mode !== "conquest") q.set("mode", mode);
  if (of === "aspects") q.set("aspect", "1");
  const s = q.toString();
  return `${toHash.god(e.name)}${s ? `?${s}` : ""}`;
}

/** The line under a name: lane, aspect, or price verdict — and the one
 *  editorial call this page makes, in words. */
function subLine(e: TierEntry, of: Subject, rare: boolean) {
  if (of === "items") {
    const it = e as ItemTierEntry;
    return <span className="text-muted">{it.efficiency_tier ? PRICE_WORD[priceVerdict(it.efficiency_tier, 0)] : "Not priced by the model"}</span>;
  }
  const lane = godLane((e as GodTierEntry).role);
  return (
    <>
      {of === "aspects"
        ? <span className="text-ink-soft">{shortAspect((e as AspectTierEntry).aspect)}</span>
        : <span className={laneTextClass(lane)}>{lane ?? (e as GodTierEntry).role ?? ""}</span>}
      {rare && <span className="text-ink-soft"> · rarely played</span>}
    </>
  );
}

function Row({ band, of, mode, rare }: { band: BandEntry<TierEntry>; of: Subject; mode: Mode; rare: boolean }) {
  const e = band.entry;
  const games = typeof e.matches === "number" ? e.matches : null;
  const name = of === "aspects" ? `${e.name}, ${(e as AspectTierEntry).aspect}` : e.name;
  return (
    <li className="border-b border-line">
      <a href={hrefFor(e, of, mode)}
        aria-label={band.unmeasured
          ? `${name}: not enough games to place`
          : `${name}: tier ${e.tier_score}, ${pct(e.win_rate)} win rate over ${games != null ? num(games) : "an unreported number of"} games${rare ? " — wins well and is rarely played" : ""}`}
        className="press grid min-h-14 grid-cols-[40px_minmax(0,1fr)_auto] items-center gap-3 py-2 pr-1 hover:bg-surface">
        <Art name={e.name} kind={of === "items" ? "item" : "head"} className="h-10 w-10 rounded-[8px]" />
        <span className="min-w-0">
          <span className="block font-cond text-[20px] font-bold leading-none text-ink [overflow-wrap:anywhere]">{e.name}</span>
          <span className="mt-1 block text-cap">{subLine(e, of, rare)}</span>
        </span>
        {band.unmeasured ? (
          <span className="text-right text-cap text-quiet">Too few games</span>
        ) : (
          <span className="text-right">
            <span className="num block font-cond text-[21px] font-bold leading-none text-ink">{pct(e.win_rate)}</span>
            <span className="num mt-1 block text-cap text-quiet">{games != null ? `${num(games)} games` : "games unreported"}</span>
          </span>
        )}
      </a>
    </li>
  );
}

const rowGrid = "grid lg:grid-cols-2 lg:gap-x-8 xl:grid-cols-3";

export function TiersPage({ tierlist, communitySource }: { tierlist?: TierListData; communitySource?: CommunitySource }) {
  const [b, setB] = useUrlState(decode, encode);
  const patch = (next: Partial<Board>) => setB((p) => ({ ...p, ...next }));
  const { mode, of, sort, lane } = b;

  const slice = tierlist?.[mode] ?? (mode === "conquest" ? tierlist : undefined);
  const source: TierEntry[] = useMemo(
    () => (of === "gods" ? slice?.gods : of === "aspects" ? slice?.aspects : slice?.items) ?? [],
    [slice, of]);
  const rare = useMemo(() => findUnderplayed(of === "gods" ? (source as GodTierEntry[]) : []), [source, of]);
  const filtered = useMemo(() => source.filter((e) => of === "items" || !lane || godInLane((e as GodTierEntry).role, lane)),
    [source, of, lane]);
  const all = useMemo(() => buildBands(source, sort), [source, sort]);
  const result = useMemo(() => buildBands(filtered, sort), [filtered, sort]);

  // Only Conquest has outcomes. A slice with entries and nothing ranked is a
  // mode with no results, stated as a gap rather than papered over.
  const unranked = all.ranked === 0;
  const [one, many] = NOUN[of];
  const src = communitySource;
  const from = shortDate(src?.window_start);
  const to = shortDate(src?.window_end);

  const subjects = ([
    { key: "gods", label: "Gods" },
    { key: "aspects", label: "Aspects" },
    { key: "items", label: "Items" },
  ] as const).filter((s) => s.key === of || ((s.key === "gods" ? slice?.gods : s.key === "aspects" ? slice?.aspects : slice?.items)?.length ?? 0) > 0);

  return (
    <div className="mx-auto w-full max-w-[1240px] px-4 pb-12 lg:px-6">
      <PageHead title="Tiers" testId="tiers-head">
        {unranked ? (
          <p data-testid="tiers-claim"><Em>{MODE_NAME[mode]} has no win data</Em>, so nothing here is ranked.</p>
        ) : (
          <p data-testid="tiers-claim">
            <Em>{all.ranked} of {all.total} {many}</Em> placed on <Em>{num(all.appearances)}</Em> {MODE_NAME[mode]} {SAMPLE[of]}
            {of === "gods" && rare.size > 0 && <>; <Em>{rare.size}</Em> win well and are rarely played</>}.
          </p>
        )}
      </PageHead>

      {unranked ? (
        <p className="mt-2 max-w-[62ch] text-note text-muted lg:text-copy">
          SmiteBrain publishes no {MODE_NAME[mode]} results. This page used to fill the gap with the site&rsquo;s own
          score; that score measured &minus;0.12 against real god strength, so an empty ranking is the honest one.
          {of !== "items" && <> {MODE_NAME[mode]} builds still work, on the model alone &mdash; open any god.</>}
        </p>
      ) : (
        <p className="mt-2 max-w-[62ch] text-note text-muted lg:text-copy">
          A band is the lower bound of each {one}&rsquo;s real win rate, so 62% over 133 games doesn&rsquo;t outrank 58%
          over 2,000. Nothing this site models goes into the order.
        </p>
      )}
      {!unranked && src?.division && (
        <p className="mt-2 text-cap text-quiet" data-testid="tiers-provenance">
          Win rates: {typeof src.matches_analyzed === "number" ? `${num(src.matches_analyzed)} ` : ""}
          {DIVISION[src.division] ?? src.division} Conquest matches on SmiteBrain{from && to ? `, ${from}–${to}` : ""}.
        </p>
      )}
      <div className="mt-1">
        <Seam href={toHash.method()} testId="method-seam">What the model does decide</Seam>
      </div>

      {/* Controls: the mode first (it decides whether there is a ranking at
          all), then what is ranked, then the lane and the order. */}
      <div className="mt-4 flex flex-col gap-3 lg:flex-row lg:items-end lg:justify-between lg:gap-8">
        <ModeSwitch mode={mode} onChange={(m) => patch({ mode: m })} className="lg:w-[420px]" />
        {subjects.length > 1 && (
          <TextTabs label="Ranked subject" value={of} onChange={(k) => patch({ of: k })} options={[...subjects]} className="lg:flex-1 lg:justify-end lg:border-b-0" />
        )}
      </div>
      {!unranked && (
        <div className="mt-3 flex flex-col gap-2 lg:flex-row lg:items-center lg:justify-between">
          {of !== "items" ? (
            <RoleFilter role={lane ?? ""} onChange={(r) => patch({ lane: r || undefined })} className="lg:w-[520px]" />
          ) : <span />}
          <button type="button" aria-pressed={sort === "matches"} onClick={() => patch({ sort: sort === "matches" ? "score" : "matches" })}
            className="press inline-flex h-11 items-center gap-2 self-start text-note font-semibold text-muted hover:text-ink lg:self-auto">
            <span aria-hidden="true" className={`flex h-5 w-5 items-center justify-center rounded-[5px] border ${sort === "matches" ? "border-accent bg-accent text-accent-ink" : "border-quiet"}`}>
              {sort === "matches" && <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><path d="m5 12 5 5 9-10" /></svg>}
            </span>
            Most played first inside each band
          </button>
        </div>
      )}

      {unranked ? (
        <section aria-labelledby="az-h" className="mt-6" data-testid="tiers-unranked">
          <h2 id="az-h" className="font-cond text-[16px] font-bold uppercase text-muted">
            Every {one}, A to Z &middot; unranked
          </h2>
          {source.length === 0 ? (
            <p className="mt-2 text-copy text-muted">No {many} recorded for {MODE_NAME[mode]}.</p>
          ) : (
            <ul className="mt-1 grid grid-cols-2 gap-x-4 sm:grid-cols-3 lg:grid-cols-6">
              {[...source].sort((x, y) => x.name.localeCompare(y.name)).map((e) => (
                <li key={`${e.name}|${(e as AspectTierEntry).aspect ?? ""}`} className="border-b border-line">
                  <a href={hrefFor(e, of, mode)}
                    className="press flex min-h-11 items-center font-cond text-[18px] font-bold text-ink-soft hover:text-ink">
                    {e.name}
                  </a>
                </li>
              ))}
            </ul>
          )}
        </section>
      ) : (
        <div className="mt-6 flex flex-col gap-8">
          <p className="sr-only" aria-live="polite">{filtered.length} {many} shown</p>
          {result.bands.map((band) => {
            const games = band.entries.reduce((n, x) => n + (x.entry.matches ?? 0), 0);
            return (
              <section key={band.tier} aria-labelledby={`band-${band.tier}-h`} data-testid={`band-${band.tier}`}
                className="lg:grid lg:grid-cols-[96px_minmax(0,1fr)] lg:gap-6">
                <div className="flex items-baseline gap-3 border-b border-line-strong pb-1 lg:sticky lg:top-[72px] lg:block lg:self-start lg:border-b-0 lg:pb-0">
                  <h2 id={`band-${band.tier}-h`} className="font-cond text-[56px] font-extrabold leading-[0.85] text-ink lg:text-[80px]">
                    <span className="sr-only">Tier </span>{band.tier}
                  </h2>
                  <p className="num text-cap text-muted lg:mt-2">
                    {band.entries.length} {band.entries.length === 1 ? one : many}
                    <span className="text-quiet"> · {num(games)} {SAMPLE[of]}</span>
                  </p>
                </div>
                <ul className={rowGrid}>
                  {band.entries.map((x) => (
                    <Row key={`${x.entry.name}|${(x.entry as AspectTierEntry).aspect ?? ""}`} band={x} of={of} mode={mode}
                      rare={rare.has(x.entry.name)} />
                  ))}
                </ul>
              </section>
            );
          })}
          {result.untiered.length > 0 && (
            <section aria-labelledby="band-untiered-h" data-testid="band-untiered" className="lg:grid lg:grid-cols-[96px_minmax(0,1fr)] lg:gap-6">
              <div className="border-b border-line-strong pb-2 lg:border-b-0">
                <h2 id="band-untiered-h" className="font-cond text-[24px] font-extrabold leading-none text-ink">Not measured</h2>
                <p className="num mt-1 text-cap text-muted">{result.untiered.length} {result.untiered.length === 1 ? one : many}</p>
              </div>
              <div>
                <p className="max-w-[62ch] py-2 text-note text-muted">
                  {of === "items"
                    ? "No tracked win rate of their own — mostly starters and components, bought on the way to something else."
                    : of === "aspects"
                      ? "Played too rarely to place: an aspect's sample is its god's games times how often it's taken."
                      : "Too few tracked games to place with any confidence. Shown, never ranked low for it."}
                </p>
                <ul className={rowGrid}>
                  {result.untiered.map((x) => (
                    <Row key={`${x.entry.name}|${(x.entry as AspectTierEntry).aspect ?? ""}`} band={x} of={of} mode={mode} rare={false} />
                  ))}
                </ul>
              </div>
            </section>
          )}
          {filtered.length === 0 && (
            <p className="text-copy text-muted">No {many} in {lane}.</p>
          )}
        </div>
      )}
    </div>
  );
}
