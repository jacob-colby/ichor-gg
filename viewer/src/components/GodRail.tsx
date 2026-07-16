import type { God } from "../types";
import { iconSlug } from "../lib/builds";

interface GodRailProps {
  gods: God[];
  selectedGod: string | null;
  onSelect: (godName: string) => void;
}

export function GodRail({ gods, selectedGod, onSelect }: GodRailProps) {
  return (
    <div className="flex w-16 flex-col gap-2 overflow-y-auto border-r border-neutral-800 bg-neutral-950 p-2">
      {gods.map((god) => (
        <button
          key={god.name}
          type="button"
          aria-pressed={god.name === selectedGod}
          onClick={() => onSelect(god.name)}
          title={god.name}
          className={`flex h-12 w-12 items-center justify-center overflow-hidden rounded ${
            god.name === selectedGod
              ? "ring-2 ring-sky-400"
              : "ring-1 ring-neutral-800 hover:ring-neutral-600"
          }`}
        >
          <img
            src={`/icons/${iconSlug(god.name)}.png`}
            alt={god.name}
            className="h-full w-full object-cover"
            onError={(e) => {
              (e.target as HTMLImageElement).style.display = "none";
            }}
          />
        </button>
      ))}
    </div>
  );
}
