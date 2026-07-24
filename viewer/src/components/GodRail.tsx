import type { God } from "../types";
import { iconSlug } from "../lib/builds";
import { Tooltip } from "./Tooltip";

interface GodRailProps {
  gods: God[];
  selectedGod: string | null;
  onSelect: (godName: string) => void;
  onRemove?: (godName: string) => void;
}

export function GodRail({ gods, selectedGod, onSelect, onRemove }: GodRailProps) {
  return (
    <div className="flex gap-2 overflow-x-auto border-b border-line bg-rail p-2 md:w-[76px] md:flex-col md:overflow-x-hidden md:overflow-y-auto md:border-b-0 md:border-r">
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
          <div className="relative shrink-0">
            <button
              type="button"
              aria-pressed={god.name === selectedGod}
              onClick={() => onSelect(god.name)}
              title={god.name}
              className={`press flex h-14 w-14 items-center justify-center overflow-hidden rounded-lg transition-all duration-150 ease-standard ${
                god.name === selectedGod
                  ? "shadow-glow ring-2 ring-gold"
                  : "ring-1 ring-line hover:brightness-110 hover:ring-line-strong"
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
            {onRemove && (
              <button
                type="button"
                onClick={(e) => {
                  e.stopPropagation();
                  if (confirm(`Remove ${god.name} from the pool?`)) onRemove(god.name);
                }}
                title={`Remove ${god.name}`}
                aria-label={`Remove ${god.name}`}
                className="press absolute -right-1 -top-1 flex items-center gap-0.5 rounded border border-dashed border-line-strong bg-bg0/90 px-1 py-px font-mono text-[8px] uppercase tracking-wider text-faint hover:text-muted"
              >
                <span>Dev</span>×
              </button>
            )}
          </div>
        </Tooltip>
      ))}
    </div>
  );
}
