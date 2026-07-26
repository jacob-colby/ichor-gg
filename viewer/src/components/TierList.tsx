import { useMemo, useState, type ReactNode } from "react";
import type { GodTierEntry, ItemTierEntry, TierListData } from "../types";
import { iconSlug } from "../lib/builds";
import { toHash, navigate } from "../lib/useHashRoute";
import { LANES, godLane, godInLane, laneTextClass, type Lane } from "../lib/roleAccent";
import { efficiencyLabel } from "../lib/itemFilters";

type Subject = "gods" | "items";
type Source = "ours" | "community";
type GameMode = "conquest" | "joust";
const TIERS = ["S", "A", "B", "C"] as const;
type TierLetter = (typeof TIERS)[number];

const GAME_MODES: { key: GameMode; label: string }[] = [
  { key: "conquest", label: "Conquest" },
  { key: "joust", label: "Joust" },
];

const TIER_TEXT: Record<TierLetter, string> = {
  S: "text-gold",
  A: "text-under",
  B: "text-ink-soft",
  C: "text-muted",
};

const gridCls = "grid grid-cols-[repeat(auto-fill,minmax(105px,1fr))] gap-2.5 sm:grid-cols-[repeat(auto-fill,minmax(150px,1fr))]";
const selCls = "rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-xs text-muted focus:border-blue focus:outline-none";
const segBtn = (active: boolean) =>
  `press rounded px-3 py-1.5 text-xs font-display font-semibold transition-colors duration-[150ms] ease-standard ${
    active ? "bg-gold text-bg0" : "text-muted hover:text-ink"
  }`;

function scoreText(v: number | null): string {
  return v == null ? "—" : v.toFixed(2);
}

interface Filter {
  q?: string;
  lane?: Lane;
  efficiency?: string;
}

function EntryCard({
  icon,
  name,
  sub,
  score,
  onClick,
}: {
  icon: string;
  name: string;
  sub: ReactNode;
  score: number | null;
  onClick: () => void;
}) {
  return (
    <div
      className="press group relative cursor-pointer rounded-xl border border-line bg-bg2 transition-colors duration-[180ms] ease-standard hover:border-line-strong"
      onClick={onClick}
      role="button"
      tabIndex={0}
      onKeyDown={(e) => { if (e.key === "Enter") onClick(); }}
    >
      <div className="flex flex-col items-center gap-1.5 px-2 pb-2 pt-2.5">
        <img
          src={icon}
          alt=""
          className="h-11 w-11 rounded-md object-cover sm:h-[52px] sm:w-[52px]"
          onError={(e) => {
            const i = e.currentTarget;
            if (i.dataset.r) { i.style.visibility = "hidden"; return; }
            i.dataset.r = "1";
            i.src = `${icon}?r=1`;
          }}
        />
        <div className="text-center font-display text-[12.5px] font-semibold leading-tight text-ink">{name}</div>
        {sub}
        <div className="font-mono text-[10px] text-faint">{scoreText(score)}</div>
      </div>
    </div>
  );
}

function GodCard({ entry, score }: { entry: GodTierEntry; score: number | null }) {
  return (
    <EntryCard
      icon={`/icons/${iconSlug(entry.name)}-head.png`}
      name={entry.name}
      score={score}
      sub={<div className={`text-[9.5px] ${laneTextClass(godLane(entry.role))}`}>{godLane(entry.role) ?? entry.role ?? ""}</div>}
      onClick={() => navigate(toHash.god(entry.name))}
    />
  );
}

function ItemCard({ entry, score }: { entry: ItemTierEntry; score: number | null }) {
  const eff = efficiencyLabel(entry.efficiency_tier);
  return (
    <EntryCard
      icon={`/icons/${iconSlug(entry.name)}.png`}
      name={entry.name}
      score={score}
      sub={<span className={`rounded-sm px-1.5 py-0.5 text-[10px] ${eff.cls}`}>{eff.text}</span>}
      onClick={() => navigate(toHash.item(entry.name))}
    />
  );
}

function TierBand({ tier, count, children }: { tier: TierLetter; count: number; children: ReactNode }) {
  return (
    <div className="mb-5" data-testid={`band-${tier}`}>
      <div className="mb-2 flex items-center gap-2">
        <span className={`flex h-7 w-7 items-center justify-center rounded-md bg-bg3 font-display text-sm font-bold ${TIER_TEXT[tier]}`}>{tier}</span>
        <span className="font-mono text-[10px] text-faint">{count}</span>
      </div>
      <div className={gridCls}>{children}</div>
    </div>
  );
}

export function TierList({ tierlist }: { tierlist?: TierListData }) {
  const [gameMode, setGameMode] = useState<GameMode>("conquest");
  const [subject, setSubject] = useState<Subject>("gods");
  const [source, setSource] = useState<Source>("ours");
  const [filter, setFilter] = useState<Filter>({});

  // Per-mode slice (Task R2), falling back to the legacy flat top-level
  // shape when the per-mode key is absent — either because this index
  // predates R2, or (Conquest specifically) because it's the same data
  // mirrored at the top level anyway. Memoized so the `?? []` fallback
  // doesn't hand the filters below a fresh array identity every render.
  const modeSlice = useMemo(() => tierlist?.[gameMode] ?? tierlist, [tierlist, gameMode]);
  const gods = useMemo(() => modeSlice?.gods ?? [], [modeSlice]);
  const items = useMemo(() => modeSlice?.items ?? [], [modeSlice]);
  // Joust has no community source at all — SmiteBrain doesn't track it — so
  // every god is 0/87 covered there. Community `tier_ours` is unaffected;
  // this is specifically about the Community toggle being uniformly empty.
  const isJoustCommunityGap = gameMode === "joust" && source === "community";

  const set = (patch: Partial<Filter>) => setFilter((f) => ({ ...f, ...patch }));
  const clear = () => setFilter({});

  const tierKey = source === "ours" ? "tier_ours" : "tier_community";
  const scoreKey = source === "ours" ? "ours" : "community";
  const q = filter.q?.trim().toLowerCase();

  const godsFiltered = useMemo(
    () =>
      gods.filter((g) => {
        if (q && !g.name.toLowerCase().includes(q)) return false;
        if (filter.lane && !godInLane(g.role, filter.lane)) return false;
        return true;
      }),
    [gods, q, filter.lane],
  );

  const itemsFiltered = useMemo(
    () =>
      items.filter((it) => {
        if (q && !it.name.toLowerCase().includes(q)) return false;
        if (filter.efficiency && (it.efficiency_tier ?? "") !== filter.efficiency) return false;
        return true;
      }),
    [items, q, filter.efficiency],
  );

  const filtered: (GodTierEntry | ItemTierEntry)[] = subject === "gods" ? godsFiltered : itemsFiltered;

  const bands = TIERS.map((tier) => ({ tier, entries: filtered.filter((e) => e[tierKey] === tier) })).filter(
    (b) => b.entries.length > 0,
  );
  const unranked = source === "community" ? filtered.filter((e) => e.tier_community === null) : [];
  const isEmpty = bands.length === 0 && unranked.length === 0;

  return (
    <div className="p-4">
      {/* Toggle + filter bar */}
      <div className="sticky top-0 z-10 -mx-4 mb-4 bg-bg0/95 px-4 pb-3 pt-1 backdrop-blur">
        <div className="mb-3 flex flex-wrap items-center gap-2">
          <div className="flex items-center gap-1 rounded-md border border-line bg-bg2 p-1">
            {GAME_MODES.map((m) => (
              <button key={m.key} type="button" onClick={() => setGameMode(m.key)} className={segBtn(gameMode === m.key)}>{m.label}</button>
            ))}
          </div>
          <div className="flex items-center gap-1 rounded-md border border-line bg-bg2 p-1">
            <button type="button" onClick={() => setSubject("gods")} className={segBtn(subject === "gods")}>Gods</button>
            <button type="button" onClick={() => setSubject("items")} className={segBtn(subject === "items")}>Items</button>
          </div>
          <div className="flex items-center gap-1 rounded-md border border-line bg-bg2 p-1">
            <button type="button" onClick={() => setSource("ours")} className={segBtn(source === "ours")}>Our calc</button>
            <button type="button" onClick={() => setSource("community")} className={segBtn(source === "community")}>Community</button>
          </div>
          <div className="flex items-center gap-2 rounded-md border border-line bg-bg2 px-3 py-2 focus-within:border-blue">
            <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2" className="text-muted"><circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" /></svg>
            <input
              placeholder={`Search ${subject}…`}
              value={filter.q ?? ""}
              onChange={(e) => set({ q: e.target.value })}
              className="w-40 bg-transparent text-xs text-ink placeholder:text-muted focus:outline-none"
            />
          </div>
          <span className="ml-auto font-mono text-[11px] text-faint">{filtered.length} {subject}</span>
        </div>
        {isJoustCommunityGap && (
          <p className="mb-3 text-[11px] text-faint">
            Joust has no community build source — SmiteBrain doesn't track Joust. Showing our calculated tiers only.
          </p>
        )}
        {subject === "gods" ? (
          <div className="flex flex-wrap items-center gap-2 overflow-x-auto">
            <button type="button" onClick={() => set({ lane: undefined })}
              className={`press rounded-full px-3 py-1.5 text-xs font-semibold ${!filter.lane ? "bg-gold text-bg0" : "border border-line text-muted"}`}>All</button>
            {LANES.map((lane: Lane) => {
              const active = filter.lane === lane;
              return (
                <button key={lane} type="button" onClick={() => set({ lane: active ? undefined : lane })}
                  className={`press rounded-full px-3 py-1.5 text-xs ${active ? "bg-gold text-bg0 font-semibold" : `border border-line ${laneTextClass(lane)}`}`}>{lane}</button>
              );
            })}
          </div>
        ) : (
          <div className="flex flex-wrap items-center gap-2 overflow-x-auto">
            <select value={filter.efficiency ?? ""} onChange={(e) => set({ efficiency: e.target.value || undefined })} className={selCls}>
              <option value="">All ratings</option>
              <option value="undervalued">Efficient</option>
              <option value="fair">Fair</option>
              <option value="premium">Premium</option>
            </select>
          </div>
        )}
      </div>

      {isEmpty ? (
        <div className="flex flex-col items-center gap-2 py-16 text-center">
          <p className="text-sm text-muted">No {subject} match those filters.</p>
          <button type="button" onClick={clear} className="text-xs text-blue hover:underline">Clear filters</button>
        </div>
      ) : (
        <>
          {bands.map(({ tier, entries }) => (
            <TierBand key={tier} tier={tier} count={entries.length}>
              {entries.map((e) =>
                subject === "gods" ? (
                  <GodCard key={e.name} entry={e as GodTierEntry} score={e[scoreKey]} />
                ) : (
                  <ItemCard key={e.name} entry={e as ItemTierEntry} score={e[scoreKey]} />
                ),
              )}
            </TierBand>
          ))}
          {unranked.length > 0 && (
            <div className="mb-5" data-testid="band-unranked">
              <div className="mb-2 font-mono text-[10px] uppercase tracking-[0.1em] text-faint">No community data</div>
              <div className={gridCls}>
                {unranked.map((e) =>
                  subject === "gods" ? (
                    <GodCard key={e.name} entry={e as GodTierEntry} score={e[scoreKey]} />
                  ) : (
                    <ItemCard key={e.name} entry={e as ItemTierEntry} score={e[scoreKey]} />
                  ),
                )}
              </div>
            </div>
          )}
        </>
      )}
    </div>
  );
}
