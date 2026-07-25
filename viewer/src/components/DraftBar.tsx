import { useMemo, useState } from "react";
import type { God, DraftComp, ThreatModel } from "../types";
import { iconSlug } from "../lib/builds";

type SlotKind = "ally" | "enemy";
interface OpenSlot {
  kind: SlotKind;
  index: number;
}

type ThreatKey = "magical" | "physical" | "healers" | "lockdown" | "crit" | "tanks";
const CHIP_DEFS: { key: ThreatKey; label: (n: number) => string }[] = [
  { key: "magical", label: (n) => `${n} magical` },
  { key: "physical", label: (n) => `${n} physical` },
  { key: "healers", label: (n) => `${n} healer${n === 1 ? "" : "s"}` },
  { key: "lockdown", label: (n) => `${n} CC` },
  { key: "crit", label: (n) => `${n} crit` },
  { key: "tanks", label: (n) => `${n} tank${n === 1 ? "" : "s"}` },
];

/** Searchable grid of eligible gods — the same idiom as AddGodModal, adapted
 * to pick-a-god-for-a-slot instead of add-to-roster. */
function GodPickerModal({
  gods, onPick, onClose,
}: {
  gods: God[];
  onPick: (name: string) => void;
  onClose: () => void;
}) {
  const [q, setQ] = useState("");
  const shown = useMemo(() => {
    const ql = q.trim().toLowerCase();
    return gods.filter((g) => !ql || g.name.toLowerCase().includes(ql));
  }, [gods, q]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" onClick={onClose}>
      <div
        className="flex max-h-[85vh] w-full max-w-2xl flex-col rounded-lg border border-line bg-bg1 p-4 shadow-raised"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="mb-3 flex items-center gap-2">
          <div className="font-display text-base font-semibold text-ink-soft">Pick a god</div>
          <button type="button" onClick={onClose} className="press ml-auto rounded-md bg-bg2 px-2 py-1 text-xs text-faint hover:text-muted">Close</button>
        </div>
        <div className="mb-3 flex items-center gap-2 rounded-md border border-line bg-bg2 px-3 py-2 focus-within:border-blue">
          <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2" className="text-muted"><circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" /></svg>
          <input
            placeholder="Search gods…"
            value={q}
            onChange={(e) => setQ(e.target.value)}
            className="w-full bg-transparent text-xs text-ink placeholder:text-muted focus:outline-none"
            autoFocus
          />
        </div>
        <div className="grid flex-1 grid-cols-[repeat(auto-fill,minmax(90px,1fr))] gap-2 overflow-y-auto">
          {shown.map((g) => (
            <button
              key={g.name}
              type="button"
              onClick={() => onPick(g.name)}
              className="press flex flex-col items-center gap-1.5 rounded-lg border border-line bg-bg2 p-2 hover:border-line-strong"
            >
              <img
                src={`/icons/${iconSlug(g.name)}-head.png`}
                alt=""
                className="h-9 w-9 rounded-md object-cover ring-1 ring-line"
                onError={(e) => { e.currentTarget.style.visibility = "hidden"; }}
              />
              <span className="truncate text-center font-display text-[10px] text-ink">{g.name}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}

function Slot({
  kind, index, name, onOpen,
}: {
  kind: SlotKind;
  index: number;
  name: string;
  onOpen: () => void;
}) {
  const n = index + 1;
  if (!name) {
    return (
      <button
        type="button"
        onClick={onOpen}
        aria-label={`Add ${kind} ${n}`}
        className="press flex h-14 w-14 flex-none items-center justify-center rounded-md border border-dashed border-line-strong text-lg leading-none text-faint hover:text-muted"
      >
        +
      </button>
    );
  }
  return (
    <button
      type="button"
      onClick={onOpen}
      aria-label={`Change ${kind} ${n} (${name})`}
      className="press flex h-14 w-14 flex-none flex-col items-center justify-center gap-1 rounded-md border border-line bg-bg2 p-1 hover:border-line-strong"
    >
      <img
        src={`/icons/${iconSlug(name)}-head.png`}
        alt=""
        className="h-7 w-7 rounded-sm object-cover"
        onError={(e) => { e.currentTarget.style.visibility = "hidden"; }}
      />
      <span className="w-full truncate text-center font-display text-[9px] text-ink">{name}</span>
    </button>
  );
}

/** Collapsible ally/enemy draft entry bar + derived threat read-out. Purely
 * controlled — all state (the draft itself) lives in the parent's useDraft(). */
export function DraftBar({
  gods, draft, onSetAlly, onSetEnemy, onClear, threats,
}: {
  /** Gods eligible to be entered — callers should already have filtered this
   * to the set with `god_item_scores` data (the 87 with a derivable core). */
  gods: God[];
  draft: DraftComp;
  onSetAlly: (i: number, name: string) => void;
  onSetEnemy: (i: number, name: string) => void;
  onClear: () => void;
  threats: ThreatModel;
}) {
  const [open, setOpen] = useState(true);
  const [pickSlot, setPickSlot] = useState<OpenSlot | null>(null);

  const chips = CHIP_DEFS.map((c) => ({ ...c, n: threats[c.key] })).filter((c) => c.n > 0);
  const hasAny = draft.allies.some(Boolean) || draft.enemies.some(Boolean);

  return (
    <div className="mb-4 rounded-md border border-line bg-bg1 p-3">
      <div className="flex items-center gap-2">
        <button
          type="button"
          onClick={() => setOpen((o) => !o)}
          aria-expanded={open}
          className="press flex items-center gap-1.5 font-display text-xs font-semibold tracking-widest text-muted hover:text-ink"
        >
          <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"
            className={`shrink-0 transition-transform duration-150 ease-standard ${open ? "rotate-90" : ""}`}>
            <path d="M9 6l6 6-6 6" />
          </svg>
          DRAFT
        </button>
        {!open && chips.length > 0 && (
          <div className="flex flex-wrap gap-1.5">
            {chips.map((c) => (
              <span key={c.key} className="rounded-full bg-bg2 px-2 py-0.5 font-mono text-[10px] text-faint">{c.label(c.n)}</span>
            ))}
          </div>
        )}
        {hasAny && (
          <button type="button" onClick={onClear} className="press ml-auto rounded-md bg-bg2 px-2 py-1 text-[11px] text-faint hover:text-ink">
            Clear
          </button>
        )}
      </div>

      {open && (
        <>
          <div className="mt-3 flex items-center gap-2 overflow-x-auto">
            <span className="w-14 flex-none font-mono text-[10px] uppercase tracking-wider text-faint">Allies</span>
            {draft.allies.map((name, i) => (
              <Slot key={i} kind="ally" index={i} name={name} onOpen={() => setPickSlot({ kind: "ally", index: i })} />
            ))}
          </div>
          <div className="mt-2 flex items-center gap-2 overflow-x-auto">
            <span className="w-14 flex-none font-mono text-[10px] uppercase tracking-wider text-faint">Enemies</span>
            {draft.enemies.map((name, i) => (
              <Slot key={i} kind="enemy" index={i} name={name} onOpen={() => setPickSlot({ kind: "enemy", index: i })} />
            ))}
          </div>
          {chips.length > 0 && (
            <div className="mt-2 flex flex-wrap gap-1.5">
              {chips.map((c) => (
                <span key={c.key} className="rounded-full bg-bg2 px-2 py-0.5 font-mono text-[10px] text-faint">{c.label(c.n)}</span>
              ))}
            </div>
          )}
        </>
      )}

      {pickSlot && (
        <GodPickerModal
          gods={gods}
          onPick={(name) => {
            if (pickSlot.kind === "ally") onSetAlly(pickSlot.index, name);
            else onSetEnemy(pickSlot.index, name);
            setPickSlot(null);
          }}
          onClose={() => setPickSlot(null)}
        />
      )}
    </div>
  );
}
