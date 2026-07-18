import type { God } from "../types";
import { iconSlug } from "../lib/builds";
import { Tooltip } from "./Tooltip";

interface GodRailProps {
  gods: God[];
  selectedGod: string | null;
  onSelect: (godName: string) => void;
}

export function GodRail({ gods, selectedGod, onSelect }: GodRailProps) {
  return (
    <div className="flex w-[72px] flex-col gap-2 overflow-y-auto border-r border-line bg-bg0 p-2">
      {gods.map((god) => (
        <Tooltip
          key={god.name}
          content={
            <div>
              <div className="font-display text-sm font-semibold text-ink">{god.name}</div>
              <div className="text-muted">{god.pantheon} · {god.role} · {god.damage_type}</div>
              <div className="mt-1 text-muted">
                {god.abilities?.map((a) => a.name).filter(Boolean).join(" · ")}
              </div>
            </div>
          }
        >
          <button
            type="button"
            aria-pressed={god.name === selectedGod}
            onClick={() => onSelect(god.name)}
            title={god.name}
            className={`flex h-14 w-14 items-center justify-center overflow-hidden rounded-lg transition-all duration-150 ${
              god.name === selectedGod
                ? "ring-2 ring-gold"
                : "ring-1 ring-line hover:ring-blue"
            }`}
          >
            <img
              src={`/icons/${iconSlug(god.name)}-head.png`}
              alt={god.name}
              className="h-full w-full object-cover"
              // Retry once with a cache-bust before giving up — a transient
              // miss (e.g. the dev server still optimizing deps when the tab
              // first opens, or a stale cached 404) otherwise leaves the icon
              // permanently hidden until a full reload.
              onError={(e) => {
                const img = e.currentTarget;
                if (img.dataset.retried) {
                  img.style.display = "none";
                  return;
                }
                img.dataset.retried = "1";
                img.src = `/icons/${iconSlug(god.name)}-head.png?r=${Date.now()}`;
              }}
            />
          </button>
        </Tooltip>
      ))}
    </div>
  );
}
