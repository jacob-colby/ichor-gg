import { useEffect, useState } from "react";
import type { BuildEntry, BuildNote } from "../types";
import { isCommunityEntry, slotItemName, iconSlug, matchingSwapIndex } from "../lib/builds";

const ARCHETYPE_TAGS = ["heavy_cc", "magic_heavy", "physical_heavy", "sustain", "poke"];
const TAG_LABELS: Record<string, string> = {
  heavy_cc: "heavy CC",
  magic_heavy: "magic-heavy",
  physical_heavy: "physical-heavy",
  sustain: "sustain",
  poke: "poke",
};

interface DetailPanelProps {
  god: string;
  builds: BuildNote[];
}

export function DetailPanel({ god, builds }: DetailPanelProps) {
  const note = builds.find((b) => b.god === god);
  // Tracked by index, not by `source` string: a single build note can (and
  // in practice does — see Chiron-Conquest.md) contain more than one entry
  // with the same source (e.g. two "mine" curated builds), so matching by
  // source would always resolve to the first entry with that source and
  // clicking a later tab with the same label would silently do nothing.
  const [activeIndex, setActiveIndex] = useState(0);
  const [selectedTag, setSelectedTag] = useState<string | null>(null);

  // Reset the active tab whenever the selected god changes, OR when the
  // build note object for the currently-selected god changes identity
  // (e.g. the "Reload data" button re-fetches index.json and produces a
  // brand-new object graph). Depending on `god` alone missed the reload
  // case: if the current god's entries shrink or get reordered on reload,
  // `activeIndex` would silently point at the wrong entry (or none),
  // showing stale/mismatched content with no tab marked selected. Every
  // reload lands back on tab 0 — losing the tab selection across a reload
  // is an acceptable tradeoff for never showing an inconsistent state.
  useEffect(() => {
    setActiveIndex(0);
    setSelectedTag(null);
  }, [god, note]);

  if (!note || note.builds.length === 0) {
    return <p className="text-neutral-500">No build data yet for {god}.</p>;
  }

  const entries = note.builds;
  const active: BuildEntry = entries[activeIndex] ?? entries[0];
  const community = isCommunityEntry(active);
  const swaps = !community ? active.situational_swaps : undefined;

  return (
    <div>
      <div className="mb-3 flex items-center gap-2">
        <h2 className="text-lg font-semibold">{god}</h2>
        <span className="rounded bg-neutral-800 px-2 py-0.5 text-xs text-neutral-400">
          {note.mode}
        </span>
      </div>

      <div role="tablist" className="mb-3 flex gap-1">
        {entries.map((entry, i) => (
          <button
            key={i}
            type="button"
            role="tab"
            aria-selected={i === activeIndex}
            onClick={() => setActiveIndex(i)}
            className={`rounded px-2 py-1 text-xs capitalize ${
              i === activeIndex ? "bg-sky-700 text-white" : "bg-neutral-800 text-neutral-300"
            }`}
          >
            {entry.source}
          </button>
        ))}
      </div>

      <div className="flex gap-4">
        <div>
          <div className="mb-1 text-xs text-neutral-500">SLOT ORDER</div>
          <div className="flex flex-col gap-1">
            {active.slot_order.map((slotEntry, i) => {
              const name = slotItemName(slotEntry);
              const rates = typeof slotEntry !== "string" ? slotEntry : null;
              return (
                <div key={i} className="flex items-center gap-2">
                  <img
                    src={`/icons/${iconSlug(name)}.png`}
                    alt=""
                    className="h-6 w-6 flex-none rounded bg-neutral-800"
                    onError={(e) => {
                      (e.target as HTMLImageElement).style.visibility = "hidden";
                    }}
                  />
                  <span className="text-sm">{name}</span>
                  {rates && (
                    <span className="text-xs text-neutral-500">
                      {Math.round(rates.pick_rate * 100)}% pick / {Math.round(rates.win_rate * 100)}% win
                    </span>
                  )}
                </div>
              );
            })}
          </div>
        </div>

        {swaps && swaps.length > 0 && (
          <div className="flex-1 border-l border-neutral-800 pl-4">
            <div className="mb-1 text-xs text-neutral-500">SITUATIONAL SWAPS</div>
            <div className="mb-1 flex flex-wrap gap-1">
              {ARCHETYPE_TAGS.map((tag) => (
                <button
                  key={tag}
                  type="button"
                  onClick={() => setSelectedTag(tag === selectedTag ? null : tag)}
                  className={`rounded-full px-2 py-0.5 text-xs ${
                    tag === selectedTag ? "bg-sky-700 text-white" : "bg-neutral-800 text-neutral-400"
                  }`}
                >
                  {TAG_LABELS[tag] ?? tag}
                </button>
              ))}
            </div>
            <div className="flex flex-col gap-1">
              {swaps.map((swap, i) => {
                const matchIndex = matchingSwapIndex(swaps, selectedTag);
                const highlighted = i === matchIndex;
                return (
                  <div
                    key={i}
                    data-highlighted={highlighted}
                    className={`rounded px-2 py-1 text-xs ${
                      highlighted ? "bg-sky-900 text-white" : "bg-neutral-800 text-neutral-300"
                    }`}
                  >
                    <span className="text-neutral-500">{TAG_LABELS[swap.vs_tag] ?? swap.vs_tag}</span>{" "}
                    — {swap.swap}
                  </div>
                );
              })}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
