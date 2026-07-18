import { useEffect, useMemo, useState } from "react";
import type { BuildEntry, BuildNote, God, Item } from "../types";
import { isCommunityEntry, slotItemName, iconSlug, applySwap, tabLabel } from "../lib/builds";
import { Tooltip } from "./Tooltip";

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
}

function ItemTooltipBody({ item, name }: { item?: Item; name: string }) {
  if (!item) return <span className="font-display font-semibold">{name}</span>;
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
    </div>
  );
}

export function DetailPanel({ god, godData, items, builds, mode, onModeChange }: DetailPanelProps) {
  const godNotes = builds.filter((b) => b.god === god);
  const note = godNotes.find((n) => n.mode === mode) ?? godNotes[0];
  const modes = godNotes.map((n) => n.mode);
  const [activeIndex, setActiveIndex] = useState(0);
  const [selectedTag, setSelectedTag] = useState<string | null>(null);
  const itemsByName = useMemo(() => {
    const m = new Map<string, Item>();
    for (const it of items) m.set(it.name, it);
    return m;
  }, [items]);

  useEffect(() => {
    setActiveIndex(0);
    setSelectedTag(null);
  }, [god, note]);

  if (!note || note.builds.length === 0) {
    return <p className="text-muted">No build data yet for {god}.</p>;
  }

  const entries = note.builds;
  const active: BuildEntry = entries[activeIndex] ?? entries[0];
  const community = isCommunityEntry(active);
  const swaps = !community ? active.situational_swaps : undefined;

  const selectedSwap = swaps?.find((s) => s.vs_tag === selectedTag) ?? null;
  const baseNames = active.slot_order.map(slotItemName);
  const preview = applySwap(baseNames, selectedSwap?.swap_item ?? null);

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
        <div className="ml-auto flex overflow-hidden rounded-md border border-line">
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
      </div>

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
            {tabLabel(entry)}
          </button>
        ))}
      </div>

      {!community && active.starter && (
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
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">SLOT ORDER</div>
          <div className="flex flex-col gap-1.5">
            {preview.map((slot, i) => {
              const item = itemsByName.get(slot.name);
              const rates = !community ? null
                : (active.slot_order[i] as { pick_rate: number; win_rate: number } | undefined);
              return (
                <Tooltip key={`${slot.name}-${i}`} content={<ItemTooltipBody item={item} name={slot.name} />}>
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
