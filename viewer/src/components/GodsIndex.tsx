import { useMemo, useState } from "react";
import type { God } from "../types";
import { filterGods, sortGods, type GodFilter } from "../lib/godFilters";
import { iconSlug } from "../lib/builds";
import { toHash, navigate } from "../lib/useHashRoute";

export function GodsIndex({ gods }: { gods: God[] }) {
  const [filter, setFilter] = useState<GodFilter>({});
  const pantheons = useMemo(() => Array.from(new Set(gods.map((g) => g.pantheon).filter(Boolean))).sort(), [gods]);
  const roles = useMemo(() => Array.from(new Set(gods.map((g) => g.role).filter(Boolean))).sort(), [gods]);
  const damages = useMemo(() => Array.from(new Set(gods.map((g) => g.damage_type).filter(Boolean))).sort(), [gods]);
  const shown = useMemo(() => sortGods(filterGods(gods, filter)), [gods, filter]);

  const set = (patch: Partial<GodFilter>) => setFilter((f) => ({ ...f, ...patch }));
  const selCls = "rounded border border-line bg-bg2 px-2 py-1 text-xs text-ink";

  return (
    <div className="p-4">
      <div className="mb-3 flex flex-wrap items-center gap-2">
        <input placeholder="Search gods…" value={filter.q ?? ""} onChange={(e) => set({ q: e.target.value })} className={selCls} />
        <select value={filter.pantheon ?? ""} onChange={(e) => set({ pantheon: e.target.value || undefined })} className={selCls}>
          <option value="">All pantheons</option>
          {pantheons.map((p) => <option key={p} value={p}>{p}</option>)}
        </select>
        <select value={filter.role ?? ""} onChange={(e) => set({ role: e.target.value || undefined })} className={selCls}>
          <option value="">All roles</option>
          {roles.map((r) => <option key={r} value={r}>{r}</option>)}
        </select>
        <select value={filter.damage_type ?? ""} onChange={(e) => set({ damage_type: e.target.value || undefined })} className={selCls}>
          <option value="">All damage</option>
          {damages.map((d) => <option key={d} value={d}>{d}</option>)}
        </select>
        <span className="text-xs text-muted">{shown.length} gods</span>
      </div>
      <div className="grid grid-cols-[repeat(auto-fill,minmax(160px,1fr))] gap-2">
        {shown.map((g) => (
          <button
            key={g.name}
            type="button"
            onClick={() => navigate(toHash.god(g.name))}
            className="flex items-center gap-2 rounded-lg border border-line bg-bg1 p-2 text-left hover:border-blue"
          >
            <img
              src={`/icons/${iconSlug(g.name)}-head.png`}
              alt=""
              className="h-10 w-10 flex-none rounded-lg object-cover ring-1 ring-line"
              onError={(e) => {
                const i = e.currentTarget;
                if (i.dataset.r) { i.style.visibility = "hidden"; return; }
                i.dataset.r = "1";
                i.src = `/icons/${iconSlug(g.name)}-head.png?r=1`;
              }}
            />
            <div className="min-w-0">
              <div className="truncate text-sm text-ink">{g.name}</div>
              <div className="truncate text-[10px] text-muted">{[g.pantheon, g.role, g.damage_type].filter(Boolean).join(" · ")}</div>
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
