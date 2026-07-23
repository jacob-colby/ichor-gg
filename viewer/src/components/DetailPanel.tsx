import { useEffect, useMemo, useState } from "react";
import type { BuildEntry, BuildNote, CuratedBuildEntry, God, Item, SlotScore } from "../types";
import { isCommunityEntry, slotItemName, iconSlug, applySwap, tabLabel } from "../lib/builds";
import { Tooltip } from "./Tooltip";
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

function ItemTooltipBody({ item, name, score }: { item?: Item; name: string; score?: SlotScore }) {
  const scoreBlock = score && (
    <div className="mt-2 border-t border-line pt-2">
      <div className="mb-1 text-[10px] font-semibold tracking-widest text-muted">WHY THIS ITEM</div>
      <ScoreBar label="value" value={score.efficiency} />
      <ScoreBar label="win" value={score.win} />
      <ScoreBar label="pick" value={score.pick} />
      <ScoreBar label="fit" value={score.fit} />
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
      <div className="mb-1 flex items-baseline justify-between">
        <span className="font-display text-sm font-semibold text-ink">{item.name}</span>
        <span className="font-mono text-muted">{item.cost}g · T{item.tier}</span>
      </div>
      {Object.entries(item.stats || {}).map(([k, v]) => (
        <div key={k} className="flex justify-between text-muted">
          <span>{k}</span><span className="font-mono text-ink">{v}</span>
        </div>
      ))}
      {item.passive && <div className="mt-1 text-muted">{item.passive}</div>}
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

export function DetailPanel({ god, godData, items, builds, mode, onModeChange, starters = [] }: DetailPanelProps) {
  const godNotes = builds.filter((b) => b.god === god);
  const note = godNotes.find((n) => n.mode === mode) ?? godNotes[0];
  const modes = godNotes.map((n) => n.mode);
  const [activeIndex, setActiveIndex] = useState(0);
  const [selectedTag, setSelectedTag] = useState<string | null>(null);
  const [editing, setEditing] = useState<MineDraft | "new" | null>(null);
  const [aspectOn, setAspectOn] = useState(false);
  const [mineVersion, setMineVersion] = useState(0);
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

  return (
    <div>
      <div className="mb-4 flex items-center gap-3">
        <img
          src={`/icons/${iconSlug(god)}-head.png`}
          alt={god}
          className="h-12 w-12 rounded-lg object-cover ring-1 ring-line"
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
          <div className="text-xs text-muted">
            {godData ? `${godData.pantheon} · ${godData.role} · ${godData.damage_type}` : note.mode}
          </div>
        </div>
      </div>

      {(modes.length > 1 || hasAspect) && (
        <div className="mb-3 flex items-center gap-3">
          {modes.length > 1 && (
            <div className="flex w-fit overflow-hidden rounded-md border border-line">
              {modes.map((m) => (
                <button
                  key={m}
                  type="button"
                  onClick={() => onModeChange(m)}
                  className={`px-3 py-1 font-display text-xs font-semibold tracking-wide ${
                    m === note.mode ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"
                  }`}
                >
                  {m}
                </button>
              ))}
            </div>
          )}
          {hasAspect && (
            <button
              type="button"
              onClick={toggleAspect}
              className={`rounded-md border border-line px-3 py-1 font-display text-xs font-semibold tracking-wide ${
                aspectOn ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"
              }`}
            >
              {aspectMeta ? `Aspect: ${aspectMeta.name.replace(/^Aspect of (the )?/i, "")}` : "Aspect"}
            </button>
          )}
        </div>
      )}

      {aspectOn && aspectMeta && (
        <div className="mb-3 rounded border border-gold/40 bg-bg1 p-2 text-xs">
          <span className="font-display font-semibold text-gold">{aspectMeta.name}</span>
          <span className="text-muted"> — {aspectMeta.kit_changes}</span>
        </div>
      )}

      {!community && (active as CuratedBuildEntry).fun && (
        <div className="mb-3 rounded border border-premium/40 bg-bg1 p-2 text-xs">
          <span className="font-display font-semibold text-premium">For fun 🎲</span>
          <span className="text-muted"> — deliberately off-class; not scored against the meta.</span>
        </div>
      )}

      <div role="tablist" className="mb-4 flex gap-1">
        {entries.map((entry, i) => (
          <button
            key={i}
            type="button"
            role="tab"
            aria-selected={i === activeIndex}
            onClick={() => setActiveIndex(i)}
            className={`rounded px-3 py-1 text-xs font-medium capitalize transition-colors duration-150 ${
              i === activeIndex ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"
            }`}
          >
            {tabLabel(entry)}{(entry as { fun?: boolean }).fun ? " 🎲" : ""}
          </button>
        ))}
      </div>

      <div className="mb-3 flex gap-2">
        <button
          type="button"
          onClick={() => setEditing("new")}
          className="rounded bg-bg2 px-3 py-1 text-xs text-blue hover:bg-line"
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
            className="rounded bg-bg2 px-3 py-1 text-xs text-muted hover:bg-line"
          >
            Edit this build
          </button>
        )}
      </div>

      {active.starter && (
        <div className="mb-4">
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">STARTER</div>
          <div className="flex items-center gap-2">
            {[active.starter.base, active.starter.upgrade].map((name, i) => (
              <div key={name} className="flex items-center gap-2">
                {i === 1 && <span className="text-muted">→</span>}
                <Tooltip content={<ItemTooltipBody item={itemsByName.get(name)} name={name} />}>
                  <div className="flex items-center gap-2">
                    <img
                      src={`/icons/${iconSlug(name)}.png`}
                      alt=""
                      className="h-6 w-6 flex-none rounded bg-bg2"
                      onError={(e) => {
                        const img = e.currentTarget;
                        if (img.dataset.retried) { img.style.visibility = "hidden"; return; }
                        img.dataset.retried = "1";
                        img.src = `/icons/${iconSlug(name)}.png?r=${Date.now()}`;
                      }}
                    />
                    <span className="text-sm text-ink">{name}</span>
                  </div>
                </Tooltip>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="flex gap-6">
        <div className="min-w-[220px]">
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">
            {!community && active.source === "suggested" ? "BUILD ORDER" : "SLOT ORDER"}
          </div>
          <div className="flex flex-col gap-1.5">
            {preview.map((slot, i) => {
              const item = itemsByName.get(slot.name);
              const rates = !community ? null
                : (active.slot_order[i] as { pick_rate: number; win_rate: number } | undefined);
              return (
                <Tooltip
                  key={`${slot.name}-${i}`}
                  content={
                    <ItemTooltipBody
                      item={item}
                      name={slot.name}
                      score={!community ? (active as CuratedBuildEntry).slot_scores?.[slot.name] : undefined}
                    />
                  }
                >
                  <div className={`flex items-center gap-2 rounded px-1 py-0.5 transition-colors duration-150 ${
                    slot.status === "added" ? "bg-blue/10" : ""}`}>
                    <img
                      src={`/icons/${iconSlug(slot.name)}.png`}
                      alt=""
                      className={`h-7 w-7 flex-none rounded bg-bg2 ${slot.status === "removed" ? "opacity-30" : ""}`}
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
                      <span className="text-[10px] text-muted">flex</span>
                    )}
                    {!community && active.source === "suggested" && !(active as CuratedBuildEntry).fun &&
                      communityNames.size > 0 && slot.status !== "added" && !communityNames.has(slot.name) && (
                      <span className="text-[10px] text-muted/70" title="Not in this god's top community items">off-meta</span>
                    )}
                    {rates && (
                      <span className="ml-auto font-mono text-xs text-muted">
                        {Math.round(rates.pick_rate * 100)}% / {Math.round(rates.win_rate * 100)}%
                      </span>
                    )}
                  </div>
                </Tooltip>
              );
            })}
          </div>
        </div>

        {swaps && swaps.length > 0 && (
          <div className="flex-1 border-l border-line pl-6">
            <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">SITUATIONAL</div>
            <div className="flex flex-col gap-1.5">
              {swaps.map((swap) => {
                const clickable = !!swap.swap_item;
                const selected = swap.vs_tag === selectedTag;
                return (
                  <button
                    key={swap.vs_tag}
                    type="button"
                    disabled={!clickable}
                    onClick={() => clickable && setSelectedTag(selected ? null : swap.vs_tag)}
                    className={`rounded px-2 py-1 text-left text-xs transition-colors duration-150 ${
                      selected ? "bg-gold text-bg0"
                      : clickable ? "bg-bg2 text-ink hover:bg-line"
                      : "bg-bg1 text-muted"}`}
                  >
                    <span className="font-medium">{VS_LABELS[swap.vs_tag] ?? swap.vs_tag}</span>
                    {" — "}{swap.swap_item ?? swap.swap.replace(/^.*—\s*/, "").replace(/[()]/g, "")}
                  </button>
                );
              })}
            </div>
          </div>
        )}
      </div>

      {!community && active.rationale && (
        <p className="mt-4 text-xs italic text-muted">{active.rationale}</p>
      )}
    </div>
  );
}
