import { useEffect, useMemo, useState } from "react";
import type { BuildEntry, BuildNote, CuratedBuildEntry, God, Item, SlotScore } from "../types";
import { isCommunityEntry, slotItemName, iconSlug, applySwap, tabLabel } from "../lib/builds";
import { tierLabel } from "../lib/itemFilters";
import { godRoleTextClass, damageTextClass } from "../lib/roleAccent";
import { BuildEditor, type MineDraft } from "./BuildEditor";
import { getMine } from "../lib/mineStore";

const VS_LABELS: Record<string, string> = {
  heavy_cc: "vs heavy CC",
  magic_heavy: "vs magic",
  physical_heavy: "vs physical",
  sustain: "vs sustain",
};

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

function ScoreBar({ label, value }: { label: string; value: number }) {
  return (
    <div className="flex items-center gap-2">
      <span className="w-14 text-[10px] text-muted">{label}</span>
      <div className="h-1.5 flex-1 rounded bg-line">
        <div className="h-1.5 rounded bg-gold" style={{ width: `${Math.round(Math.min(value, 1) * 100)}%` }} />
      </div>
      <span className="w-8 text-right font-mono text-[10px] text-ink">{value.toFixed(2)}</span>
    </div>
  );
}

/** The "WHY THIS ITEM" score breakdown — shared by the desktop side card and
 * the mobile inline disclosure. */
function WhyScoreBlock({ score }: { score: SlotScore }) {
  return (
    <div>
      <div className="mb-1.5 font-display text-[10px] font-semibold tracking-widest text-muted">WHY THIS ITEM</div>
      <div className="flex flex-col gap-1">
        <ScoreBar label="value" value={score.efficiency} />
        <ScoreBar label="win" value={score.win} />
        {score.pick > 0 ? (
          <ScoreBar label="pick" value={score.pick} />
        ) : (
          <div className="flex items-center gap-2">
            <span className="w-14 text-[10px] text-muted">pick</span>
            <span className="text-[10px] text-faint">off-meta — not in community build</span>
          </div>
        )}
        <ScoreBar label="fit" value={score.fit} />
      </div>
    </div>
  );
}

/** Item identity + (when available) its WHY score breakdown, folded into one
 * card — the regression fix for spec E. Previously this was split across a
 * separate `<Tooltip>` on the starter row and a score-only panel on build-
 * order rows, so slot rows never showed stats/passive/effect tags and two
 * hover mechanisms competed for the same real estate. Now every consumer
 * (desktop hover panel, mobile inline disclosure) renders through here:
 * one hover/tap, one panel, full identity plus score bars when scored. */
function ItemDetailCard({ item, name, score }: { item?: Item; name: string; score?: SlotScore }) {
  const scoreBlock = score && (
    <div className="mt-2 border-t border-line pt-2">
      <WhyScoreBlock score={score} />
    </div>
  );
  if (!item) {
    return (
      <div>
        <span className="font-display font-semibold">{name}</span>
        {scoreBlock}
      </div>
    );
  }
  return (
    <div>
      <div className="mb-1 flex items-baseline justify-between gap-2">
        <span className="font-display text-sm font-semibold text-ink">{item.name}</span>
        <span className="shrink-0 font-mono text-[11px] text-faint"><span className="text-gold">{item.cost}g</span> · {tierLabel(item.tier)}</span>
      </div>
      {Object.entries(item.stats || {}).map(([k, v]) => (
        <div key={k} className="flex justify-between text-xs text-muted">
          <span>{k}</span><span className="font-mono text-ink">{v}</span>
        </div>
      ))}
      {item.passive && <div className="mt-1 text-xs text-muted">{item.passive}</div>}
      {(item.effect_tags?.length || item.efficiency_tier) && (
        <div className="mt-2 flex flex-wrap gap-1">
          {item.efficiency_tier && (
            <span className={`rounded px-1.5 py-0.5 text-[10px] ${
              item.efficiency_tier === "undervalued" ? "bg-under/20 text-under"
              : item.efficiency_tier === "premium" ? "bg-premium/20 text-premium"
              : "bg-line text-muted"}`}>{item.efficiency_tier}</span>
          )}
          {item.effect_tags?.map((t) => (
            <span key={t} className="rounded bg-line px-1.5 py-0.5 text-[10px] text-blue">{t}</span>
          ))}
        </div>
      )}
      {scoreBlock}
    </div>
  );
}

// Situational swaps (spec C): a swap only earns an order-shift note when its
// cost differs meaningfully from the item it replaces — a few hundred gold
// on a multi-thousand-gold item wouldn't actually move its purchase slot in
// a real build order. 15% is "materially different" without flagging two
// near-identical-cost components as a shift.
const SWAP_ORDER_SHIFT_THRESHOLD = 0.15;

/** null when the cost difference is inside the no-op band (spec C: "where
 * nothing shifts, print nothing — no filler text"). */
function swapOrderShiftNote(swapCost: number | undefined, replacedCost: number | undefined): string | null {
  if (!swapCost || !replacedCost) return null;
  const diff = (swapCost - replacedCost) / replacedCost;
  if (diff <= -SWAP_ORDER_SHIFT_THRESHOLD) return "buy earlier";
  if (diff >= SWAP_ORDER_SHIFT_THRESHOLD) return "buy later";
  return null;
}

const segBtn = (active: boolean) =>
  `press rounded-md px-3 py-1 font-display text-xs font-semibold tracking-wide transition-colors duration-150 ease-standard ${
    active ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"
  }`;

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
  // Desktop: which slot row's score card is shown in the WHY THIS ITEM panel
  // (set on hover/focus). Mobile: which row has its inline disclosure open
  // (set on tap) — a separate piece of state since the two interactions are
  // independent (see design spec's "hover vs tap" motion split).
  const [whyIndex, setWhyIndex] = useState<number | null>(null);
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

  useEffect(() => {
    setWhyIndex(null);
    setExpandedIndex(null);
  }, [god, note, activeIndex, selectedTag]);

  if (!note || note.builds.length === 0) {
    return <p className="text-muted">No build data yet for {god}.</p>;
  }

  const aspectMeta = godData?.aspects?.[0];
  const hasAspect = note.builds.some((b) => (b as { aspect?: string }).aspect);
  const entries = [
    ...note.builds.filter((b) => {
      if (b.source === "mine") return false; // mine builds live in localStorage now
      if (b.source !== "suggested") return true;
      const a = (b as { aspect?: string }).aspect;
      return aspectOn ? !!a : !a;
    }),
    ...mineEntries,
  ];
  const toggleAspect = () => {
    const next = !aspectOn;
    const cur = entries[activeIndex] ?? entries[0];
    const curArch = cur && cur.source === "suggested" ? (cur as { archetype?: string }).archetype : undefined;
    const nextEntries = note.builds.filter((b) => {
      if (b.source !== "suggested") return true;
      const a = (b as { aspect?: string }).aspect;
      return next ? !!a : !a;
    });
    const i = curArch
      ? nextEntries.findIndex((e) => e.source === "suggested" && (e as { archetype?: string }).archetype === curArch)
      : -1;
    setAspectOn(next);
    setActiveIndex(i >= 0 ? i : 0);
    setSelectedTag(null);
  };
  const active: BuildEntry = entries[activeIndex] ?? entries[0];
  const community = isCommunityEntry(active);
  const swaps = !community ? active.situational_swaps : undefined;

  const selectedSwap = swaps?.find((s) => s.vs_tag === selectedTag) ?? null;
  const baseNames = active.slot_order.map(slotItemName);
  const communityNames = new Set(
    note.builds.filter(isCommunityEntry).flatMap((b) => b.slot_order.map((s) => s.name)));
  const flexList = !community ? active.flex_slots : undefined;
  const preview = applySwap(baseNames, selectedSwap?.swap_item ?? null, flexList);

  // Popular items (spec F): what this god's playerbase actually buys, as
  // items rather than an ordered build — distinct from the community build
  // tab above. Always read off the community entry for this mode (not
  // whichever tab is active), and mark overlap against the suggested core
  // specifically, matching "already in the suggested core" in the spec.
  const communityEntry = note.builds.find(isCommunityEntry);
  const popularItems = communityEntry?.popular_items ?? [];
  const suggestedCore = note.builds.find(
    (b) => b.source === "suggested" && (b as CuratedBuildEntry).archetype === "core" && !(b as CuratedBuildEntry).fun,
  ) as CuratedBuildEntry | undefined;
  const suggestedCoreNames = new Set(suggestedCore?.slot_order ?? []);

  if (editing) {
    const recStarter = entries
      .map((e) => (e as { starter?: { base: string; upgrade: string } }).starter)
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
          const nonMineCount = note.builds.filter((b) => {
            if (b.source === "mine") return false;
            if (b.source !== "suggested") return true;
            const a = (b as { aspect?: string }).aspect;
            return aspectOn ? !!a : !a;
          }).length;
          const idx = name ? getMine(god, note.mode).findIndex((b) => b.name === name) : -1;
          setActiveIndex(idx >= 0 ? nonMineCount + idx : 0);
        }}
      />
    );
  }

  const whySlot = whyIndex !== null ? preview[whyIndex] : undefined;
  const whyScore = whySlot && !community ? (active as CuratedBuildEntry).slot_scores?.[whySlot.name] : undefined;
  const whyItemData = whySlot ? itemsByName.get(whySlot.name) : undefined;
  // Any hovered/focused row earns the panel now (spec E fold-in), not just
  // scored ones — item identity (name/cost/stats/passive) is useful even
  // for community-source rows that have no slot_scores.
  const hasRightColumn = !!whySlot || (!!swaps && swaps.length > 0);

  return (
    <div>
      <div className="mb-4 flex flex-wrap items-start justify-between gap-3">
        <div className="flex items-center gap-3">
          <img
            src={`/icons/${iconSlug(god)}-head.png`}
            alt={god}
            className="h-[52px] w-[52px] flex-none rounded-lg object-cover shadow-card"
            onError={(e) => {
              const img = e.currentTarget;
              if (img.dataset.retried) {
                img.style.display = "none";
                return;
              }
              img.dataset.retried = "1";
              img.src = `/icons/${iconSlug(god)}-head.png?r=${Date.now()}`;
            }}
          />
          <div>
            <h2 className="font-display text-2xl font-bold leading-none text-ink">{god}</h2>
            <div className="mt-1 text-xs text-muted">
              {godData ? (
                <>
                  {godData.pantheon} · <span className={godRoleTextClass(godData)}>{godData.role}</span> ·{" "}
                  <span className={damageTextClass(godData.damage_type)}>{godData.damage_type}</span>
                </>
              ) : note.mode}
            </div>
          </div>
        </div>

        {(modes.length > 1 || hasAspect) && (
          <div className="flex items-center gap-2">
            {modes.length > 1 && (
              <div className="flex w-fit gap-0.5 rounded-md border border-line bg-bg1 p-0.5">
                {modes.map((m) => (
                  <button key={m} type="button" onClick={() => onModeChange(m)} className={segBtn(m === note.mode)}>
                    {m}
                  </button>
                ))}
              </div>
            )}
            {hasAspect && (
              <button type="button" onClick={toggleAspect} className={segBtn(aspectOn)}>
                {aspectMeta ? `Aspect: ${aspectMeta.name.replace(/^Aspect of (the )?/i, "")}` : "Aspect"}
              </button>
            )}
          </div>
        )}
      </div>

      {aspectOn && aspectMeta && (
        <div className="mb-3 rounded-md border border-gold/40 bg-bg1 p-2.5 text-xs">
          <span className="font-display font-semibold text-gold">{aspectMeta.name}</span>
          <span className="text-muted"> — {aspectMeta.kit_changes}</span>
        </div>
      )}

      <div role="tablist" className="mb-4 flex flex-wrap gap-1 rounded-md border border-line bg-bg1 p-1">
        {entries.map((entry, i) => (
          <button
            key={i}
            type="button"
            role="tab"
            aria-selected={i === activeIndex}
            onClick={() => setActiveIndex(i)}
            className={`press rounded px-3 py-1 font-display text-xs font-semibold capitalize transition-colors duration-150 ease-standard ${
              i === activeIndex ? "bg-gold text-bg0" : "text-muted hover:text-ink"
            }`}
          >
            {tabLabel(entry)}{(entry as { fun?: boolean }).fun ? " 🎲" : ""}
          </button>
        ))}
      </div>

      {!community && (active as CuratedBuildEntry).fun && (
        <div className="mb-3 rounded-md border border-premium/40 bg-bg1 p-2.5 text-xs">
          <span className="font-display font-semibold text-premium">For fun 🎲</span>
          <span className="text-muted"> — deliberately off-class; not scored against the meta.</span>
        </div>
      )}

      <div className="mb-3 flex gap-2">
        <button
          type="button"
          onClick={() => setEditing("new")}
          className="press rounded-md bg-bg2 px-3 py-1 text-xs text-blue hover:bg-line"
        >
          + New build
        </button>
        {active.source === "mine" && (
          <button
            type="button"
            onClick={() =>
              setEditing({
                name: active.name ?? "",
                slot_order: active.slot_order,
                starter: active.starter,
                notes: active.notes,
              })
            }
            className="press rounded-md bg-bg2 px-3 py-1 text-xs text-muted hover:bg-line"
          >
            Edit this build
          </button>
        )}
      </div>

      {active.starter && (
        <div className="mb-4">
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">STARTER</div>
          <div className="flex flex-wrap items-center gap-2">
            {[active.starter.base, active.starter.upgrade].map((name, i) => (
              <div key={name} className="flex items-center gap-2">
                {i === 1 && <span className="text-muted">→</span>}
                {/* No hover tooltip here (spec E) — starter items aren't part
                    of the scored build order, and the fix for the hover
                    regression is exactly one hover pattern for item info:
                    the build-order rows' WHY card below. A second, competing
                    mechanism on this row was the bug. */}
                <div className="flex items-center gap-2 rounded-md px-1 py-0.5">
                  <img
                    src={`/icons/${iconSlug(name)}.png`}
                    alt=""
                    className="h-6 w-6 flex-none rounded-sm bg-bg2"
                    onError={(e) => {
                      const img = e.currentTarget;
                      if (img.dataset.retried) { img.style.visibility = "hidden"; return; }
                      img.dataset.retried = "1";
                      img.src = `/icons/${iconSlug(name)}.png?r=${Date.now()}`;
                    }}
                  />
                  <span className="text-sm text-ink">{name}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="flex flex-col gap-6 md:flex-row">
        <div className="min-w-0 flex-1 md:max-w-[380px]">
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">
            {!community && active.source === "suggested" ? "BUILD ORDER" : "SLOT ORDER"}
          </div>
          <div className="flex flex-col gap-1">
            {preview.map((slot, i) => {
              const item = itemsByName.get(slot.name);
              const rates = !community ? null
                : (active.slot_order[i] as {
                    pick_rate: number; win_rate: number;
                    alternates?: { name: string; pick_rate: number; win_rate: number }[];
                  } | undefined);
              const rowScore = !community ? (active as CuratedBuildEntry).slot_scores?.[slot.name] : undefined;
              const expanded = expandedIndex === i;
              return (
                <div key={`${slot.name}-${i}`} className="flex flex-col">
                  <div
                    tabIndex={0}
                    role="button"
                    aria-expanded={expanded}
                    onMouseEnter={() => setWhyIndex(i)}
                    onFocus={() => setWhyIndex(i)}
                    onClick={() => setExpandedIndex((cur) => (cur === i ? null : i))}
                    onKeyDown={(e) => {
                      if (e.key === "Enter" || e.key === " ") {
                        e.preventDefault();
                        setExpandedIndex((cur) => (cur === i ? null : i));
                      }
                    }}
                    className={`press flex min-h-11 cursor-pointer items-center gap-2 rounded-md px-1.5 transition-colors duration-150 ease-standard hover:bg-bg1 ${
                      slot.status === "added" ? "bg-blue/10" : ""}`}
                  >
                    <img
                      src={`/icons/${iconSlug(slot.name)}.png`}
                      alt=""
                      className={`h-8 w-8 flex-none rounded-sm bg-bg2 ${slot.status === "removed" ? "opacity-30" : ""}`}
                      onError={(e) => {
                        const img = e.currentTarget;
                        if (img.dataset.retried) {
                          img.style.visibility = "hidden";
                          return;
                        }
                        img.dataset.retried = "1";
                        img.src = `/icons/${iconSlug(slot.name)}.png?r=${Date.now()}`;
                      }}
                    />
                    <span className={`text-sm ${
                      slot.status === "removed" ? "text-muted line-through"
                      : slot.status === "added" ? "font-medium text-blue" : "text-ink"}`}>
                      {slot.name}
                    </span>
                    {slot.status === "added" && <span className="text-[10px] text-muted">swap in</span>}
                    {flexList?.includes(slot.name) && slot.status === "kept" && (
                      <span className="rounded-sm bg-bg2 px-1 py-0.5 text-[10px] text-faint">flex</span>
                    )}
                    {rates?.alternates?.length ? (
                      <span className="truncate text-[10px] text-muted/70"
                        title={rates.alternates.map((a) => `${a.name} (${Math.round(a.pick_rate * 100)}% pick)`).join(", ")}>
                        or {rates.alternates[0].name}
                      </span>
                    ) : null}
                    {!community && active.source === "suggested" && !(active as CuratedBuildEntry).fun &&
                      communityNames.size > 0 && slot.status !== "added" && !communityNames.has(slot.name) && (
                      <span className="rounded-sm bg-bg2 px-1 py-0.5 text-[10px] text-faint" title="Not in this god's top community items">off-meta</span>
                    )}
                    {rates && (
                      <span className="ml-auto font-mono text-xs text-muted">
                        {Math.round(rates.pick_rate * 100)}% / {Math.round(rates.win_rate * 100)}%
                      </span>
                    )}
                    <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" strokeWidth="2.5"
                      strokeLinecap="round" strokeLinejoin="round"
                      className={`ml-1 shrink-0 text-faint transition-transform duration-150 ease-standard md:hidden ${expanded ? "rotate-90" : ""}`}>
                      <path d="M9 6l6 6-6 6" />
                    </svg>
                  </div>
                  {expanded && (
                    <div className="mb-1 ml-1 rounded-md border border-line bg-bg1 p-2.5 md:hidden">
                      <ItemDetailCard item={item} name={slot.name} score={rowScore} />
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>

        {hasRightColumn && (
          <div className="flex flex-col gap-4 md:w-[260px] md:flex-none md:border-l md:border-line md:pl-6">
            {whySlot && (
              <div className="hidden rounded-md border border-line bg-bg2 p-3 md:block">
                <ItemDetailCard item={whyItemData} name={whySlot.name} score={whyScore} />
              </div>
            )}
            {swaps && swaps.length > 0 && (
              <div>
                <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">SITUATIONAL</div>
                <div className="flex flex-col gap-1.5">
                  {swaps.map((swap) => {
                    const clickable = !!swap.swap_item;
                    const selected = swap.vs_tag === selectedTag;
                    // The replaced item is whatever applySwap itself targets
                    // (flex slot, else the last core slot) — reuse it rather
                    // than inventing a second rule (spec C).
                    const swapPreview = swap.swap_item ? applySwap(baseNames, swap.swap_item, flexList) : null;
                    const replacedName = swapPreview?.find((s) => s.status === "removed")?.name;
                    const orderNote = swap.swap_item && replacedName
                      ? swapOrderShiftNote(itemsByName.get(swap.swap_item)?.cost, itemsByName.get(replacedName)?.cost)
                      : null;
                    return (
                      <button
                        key={swap.vs_tag}
                        type="button"
                        disabled={!clickable}
                        onClick={() => clickable && setSelectedTag(selected ? null : swap.vs_tag)}
                        className={`press rounded-sm px-2 py-1.5 text-left text-xs transition-colors duration-150 ease-standard ${
                          selected ? "bg-gold text-bg0 font-medium"
                          : clickable ? "bg-bg2 text-ink-soft hover:bg-line"
                          : "bg-bg2 text-faint"}`}
                      >
                        <div>
                          <span className="font-medium">{VS_LABELS[swap.vs_tag] ?? swap.vs_tag}</span>
                          {" — "}{swap.swap_item ?? swap.swap.replace(/^.*—\s*/, "").replace(/[()]/g, "")}
                        </div>
                        {replacedName && (
                          <div className={`mt-0.5 text-[10px] ${selected ? "text-bg0/70" : "text-faint"}`}>
                            in for {replacedName}{orderNote ? ` — ${orderNote}` : ""}
                          </div>
                        )}
                      </button>
                    );
                  })}
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      {popularItems.length > 0 && (
        <div className="mt-6">
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">POPULAR ITEMS</div>
          <p className="mb-2 text-[10px] text-faint">What this god's playerbase actually buys — not an ordered build.</p>
          <div className="grid grid-cols-3 gap-2 sm:grid-cols-4 md:grid-cols-5">
            {popularItems.map((p) => {
              const inCore = suggestedCoreNames.has(p.name);
              return (
                <div
                  key={p.name}
                  className={`flex flex-col items-center gap-1 rounded-md border p-2 text-center ${
                    inCore ? "border-gold/40 bg-gold/5" : "border-line bg-bg2"}`}
                >
                  <img
                    src={`/icons/${iconSlug(p.name)}.png`}
                    alt=""
                    className="h-8 w-8 flex-none rounded-sm bg-bg2"
                    onError={(e) => {
                      const img = e.currentTarget;
                      if (img.dataset.retried) { img.style.visibility = "hidden"; return; }
                      img.dataset.retried = "1";
                      img.src = `/icons/${iconSlug(p.name)}.png?r=${Date.now()}`;
                    }}
                  />
                  <span className="text-xs text-ink">{p.name}</span>
                  <span className="font-mono text-[10px] text-muted">{Math.round(p.pick_rate * 100)}% pick</span>
                  <span className="font-mono text-[10px] text-faint">{Math.round(p.win_rate * 100)}% win</span>
                  {inCore && <span className="text-[9px] font-semibold text-gold">in core</span>}
                </div>
              );
            })}
          </div>
        </div>
      )}

      {!community && active.rationale && (
        <p className="mt-4 text-xs italic text-muted">{active.rationale}</p>
      )}
    </div>
  );
}
