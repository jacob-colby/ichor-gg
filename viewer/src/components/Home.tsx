import { useMemo, useState, type ReactNode } from "react";
import type { God, IndexData, PatchPeriod } from "../types";
import { toHash, navigate } from "../lib/useHashRoute";
import { usePins } from "../lib/pins";
import { filterGods } from "../lib/godFilters";
import { iconSlug } from "../lib/builds";
import { godLane, laneTextClass } from "../lib/roleAccent";
import { relativeDate } from "../lib/relativeDate";

function scoreText(v: number | null | undefined): string {
  return v == null ? "—" : v.toFixed(2);
}

function godIcon(name: string) {
  return (e: React.SyntheticEvent<HTMLImageElement>) => {
    const i = e.currentTarget;
    if (i.dataset.r) { i.style.visibility = "hidden"; return; }
    i.dataset.r = "1";
    i.src = `/icons/${iconSlug(name)}-head.png?r=1`;
  };
}

function SectionHeader({ title, linkLabel, onLink }: { title: string; linkLabel?: string; onLink?: () => void }) {
  return (
    <div className="mb-3 flex items-center justify-between">
      <h2 className="font-display text-sm font-bold text-ink">{title}</h2>
      {linkLabel && onLink && (
        <button type="button" onClick={onLink} className="press text-xs text-blue hover:underline">
          {linkLabel} →
        </button>
      )}
    </div>
  );
}

function Section({ children }: { children: ReactNode }) {
  return <section className="w-full">{children}</section>;
}

/** Prominent top-of-page search. Typing narrows a dropdown of matches;
 * clicking a result (or submitting with a match) jumps straight to that
 * god's page — the fastest path for a repeat visitor. */
function HomeSearch({ gods }: { gods: God[] }) {
  const [q, setQ] = useState("");
  const results = useMemo(() => (q.trim() ? filterGods(gods, { q }).slice(0, 6) : []), [gods, q]);

  const go = (name: string) => {
    setQ("");
    navigate(toHash.god(name));
  };

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    if (results[0]) go(results[0].name);
  };

  return (
    <div data-testid="home-search" className="mx-auto w-full max-w-xl">
      <form
        onSubmit={submit}
        className="flex items-center gap-2.5 rounded-xl border border-line bg-bg2 px-4 py-3 shadow-card transition-colors duration-[180ms] ease-standard focus-within:border-blue"
      >
        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" className="shrink-0 text-muted">
          <circle cx="11" cy="11" r="7" />
          <path d="M21 21l-4.3-4.3" />
        </svg>
        <input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          placeholder="Search gods…"
          aria-label="Search gods"
          className="w-full bg-transparent text-sm text-ink placeholder:text-muted focus:outline-none"
        />
      </form>
      {results.length > 0 && (
        <ul className="mt-2 flex flex-col gap-0.5 rounded-xl border border-line bg-bg2 p-1.5 shadow-card">
          {results.map((g) => (
            <li key={g.name}>
              <button
                type="button"
                onClick={() => go(g.name)}
                className="press flex w-full items-center gap-2.5 rounded-lg px-2.5 py-2 text-left transition-colors duration-[150ms] ease-standard hover:bg-bg3"
              >
                <img src={`/icons/${iconSlug(g.name)}-head.png`} alt="" className="h-7 w-7 shrink-0 rounded object-cover" onError={godIcon(g.name)} />
                <span className="font-display text-[13px] font-semibold text-ink">{g.name}</span>
                {g.role && <span className={`ml-auto text-[10px] ${laneTextClass(godLane(g.role))}`}>{godLane(g.role) ?? g.role}</span>}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

function GodTile({ god, onClick }: { god: God; onClick: () => void }) {
  const lane = godLane(god.role);
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label={`Go to ${god.name}`}
      className="press flex flex-col items-center gap-1.5 rounded-lg border border-line bg-bg2 p-2 transition-colors duration-[180ms] ease-standard hover:border-line-strong"
    >
      <img src={`/icons/${iconSlug(god.name)}-head.png`} alt="" className="h-11 w-11 rounded-md object-cover" onError={godIcon(god.name)} />
      <span className="max-w-[84px] truncate font-display text-[11.5px] font-semibold text-ink">{god.name}</span>
      {lane && <span className={`text-[9.5px] ${laneTextClass(lane)}`}>{lane}</span>}
    </button>
  );
}

/** Your pinned gods, or — with none pinned yet — an invitation rather than
 * an apology: pinning is a feature to try, not something the user is
 * missing out on. */
function PinnedSection({ gods }: { gods: God[] }) {
  const { pins } = usePins();
  const pinnedGods = pins
    .map((n) => gods.find((g) => g.name === n))
    .filter((g): g is God => !!g);

  return (
    <Section>
      <div data-testid="home-pinned">
        <SectionHeader title="Your pinned gods" />
        {pinnedGods.length === 0 ? (
          <p className="text-sm text-muted">
            Pin a god from its page and it'll show up here — a quick jump back to the ones you play most.
          </p>
        ) : (
          <div className="flex flex-wrap gap-2.5">
            {pinnedGods.map((g) => (
              <GodTile key={g.name} god={g} onClick={() => navigate(toHash.god(g.name))} />
            ))}
          </div>
        )}
      </div>
    </Section>
  );
}

/** S-tier slice of the tier list, our calc's ranking, with the community
 * score alongside where we have one. Absent entirely on an older index that
 * hasn't been through a build with `tierlist` yet. */
function TierSlice({ tierlist }: { tierlist: IndexData["tierlist"] }) {
  if (!tierlist) return null;
  const sTier = tierlist.gods.filter((g) => g.tier_ours === "S");

  return (
    <Section>
      <div data-testid="home-tier">
        <SectionHeader title="Top of the tier list" linkLabel="See full tier list" onLink={() => navigate(toHash.tiers())} />
        {sTier.length === 0 ? (
          <p className="text-sm text-muted">No S-tier gods yet.</p>
        ) : (
          <div className="grid grid-cols-3 gap-2.5 sm:grid-cols-4 md:grid-cols-6">
            {sTier.map((g) => (
              <button
                key={g.name}
                type="button"
                onClick={() => navigate(toHash.god(g.name))}
                className="press flex flex-col items-center gap-1 rounded-lg border border-line bg-bg2 p-2 transition-colors duration-[180ms] ease-standard hover:border-line-strong"
              >
                <img src={`/icons/${iconSlug(g.name)}-head.png`} alt="" className="h-10 w-10 rounded-md object-cover" onError={godIcon(g.name)} />
                <span className="max-w-[84px] truncate font-display text-[11px] font-semibold text-ink">{g.name}</span>
                <span className="font-mono text-[9.5px] text-faint">
                  {scoreText(g.ours)}
                  {g.community != null && <> · {scoreText(g.community)}</>}
                </span>
              </button>
            ))}
          </div>
        )}
      </div>
    </Section>
  );
}

/** Newest patch period only — a one-glance "what changed", with a link to
 * the full history. Rendered nowhere at all when there's no history yet
 * (no empty shell). */
function LatestPatch({ periods }: { periods: PatchPeriod[] | undefined }) {
  if (!periods || periods.length === 0) return null;
  const latest = periods[0];
  const counts = [
    latest.changed.length > 0 ? `${latest.changed.length} changed` : null,
    latest.added.length > 0 ? `${latest.added.length} added` : null,
    latest.removed.length > 0 ? `${latest.removed.length} removed` : null,
  ].filter(Boolean).join(" · ");

  return (
    <Section>
      <div data-testid="home-patch">
        <SectionHeader title="Latest patch changes" linkLabel="See all patch notes" onLink={() => navigate(toHash.patch())} />
        <div className="rounded-xl border border-line bg-bg1 p-3.5">
          <div className="mb-2 flex items-center gap-2">
            <span className="font-mono text-xs text-faint">{latest.from} → {latest.to}</span>
            {counts && <span className="ml-auto font-mono text-[11px] text-faint">{counts}</span>}
          </div>
          <div className="flex flex-wrap gap-1.5">
            {latest.changed.map((d) => (
              <span key={d.name} className="rounded-sm bg-bg2 px-2 py-1 text-[11px] text-ink-soft">{d.name}</span>
            ))}
            {latest.added.map((n) => (
              <span key={n} className="rounded-sm bg-blue/10 px-2 py-1 text-[11px] font-semibold text-blue">{n}</span>
            ))}
            {latest.removed.map((n) => (
              <span key={n} className="rounded-sm px-2 py-1 text-[11px] text-muted line-through">{n}</span>
            ))}
          </div>
        </div>
      </div>
    </Section>
  );
}

/** Relative freshness with the absolute date on hover. Omitted entirely
 * when the index predates the `data_updated` field. */
function Freshness({ dataUpdated }: { dataUpdated?: string }) {
  if (!dataUpdated) return null;
  return (
    <p data-testid="home-freshness" title={dataUpdated} className="text-center font-mono text-[11px] text-faint">
      Updated {relativeDate(dataUpdated)}
    </p>
  );
}

export function Home({ data }: { data: IndexData }) {
  return (
    <div className="mx-auto flex w-full max-w-4xl flex-col gap-8 p-4 pb-10 pt-8 sm:p-6 sm:pt-10">
      <HomeSearch gods={data.gods} />
      <PinnedSection gods={data.gods} />
      <TierSlice tierlist={data.tierlist} />
      <LatestPatch periods={data.patch_notes} />
      <Freshness dataUpdated={data.data_updated} />
    </div>
  );
}
