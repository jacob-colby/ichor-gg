import { useMemo, useState } from "react";
import type { BuildNote, CuratedBuildEntry, DraftConfig, God, Item } from "../types";
import { iconSlug } from "../lib/builds";
import { useDraft, MODE_TEAM_SIZE, type DraftMode } from "../lib/draft";
import { deriveThreats, threatOverlay } from "../lib/threats";
import { adaptedCore } from "../lib/draftBuild";

type ThreatKey = "magical" | "physical" | "healers" | "lockdown" | "crit" | "tanks";
const CHIP_DEFS: { key: ThreatKey; label: (n: number, total: number) => string }[] = [
  { key: "magical", label: (n, t) => `${n}/${t} magical` },
  { key: "physical", label: (n, t) => `${n}/${t} physical` },
  { key: "healers", label: (n, t) => `${n}/${t} healer${n === 1 ? "" : "s"}` },
  { key: "lockdown", label: (n, t) => `${n}/${t} CC` },
  { key: "crit", label: (n, t) => `${n}/${t} crit` },
  { key: "tanks", label: (n, t) => `${n}/${t} tank${n === 1 ? "" : "s"}` },
];

const MODE_LABEL: Record<DraftMode, string> = { conquest: "Conquest", joust: "Joust" };
const MODES: DraftMode[] = ["conquest", "joust"];

/** Mirrors the `lifesteal_caps` rule in _weights.yaml (physical Carry/Hunter/
 * Sharpshooter get 2, everyone else 1) — not shipped per-god in the index,
 * so re-derived here from the god fields the client already has. Same logic
 * as DetailPanel's private helper of the same name. */
function draftMaxLifesteal(godData?: God): number {
  if (!godData || godData.damage_type !== "physical") return 1;
  const tokens = new Set([...(godData.role ?? "").split(/\s+/), ...(godData.specializations ?? [])]);
  return ["Carry", "Hunter", "Sharpshooter"].some((t) => tokens.has(t)) ? 2 : 1;
}

/** An ally's own suggested core for the current mode, reduced to the
 * effect_tags its items bring — the "team responsibility" signal
 * deriveThreats uses to tell a covered job from a gap. Falls back to
 * whatever mode that god has notes for. Same logic as DetailPanel's private
 * helper of the same name, parameterized by the draft's own mode. */
function allyEffectTags(
  allyName: string,
  modeLabel: string,
  builds: BuildNote[],
  itemsByName: Record<string, Item>,
): string[] {
  const notes = builds.filter((b) => b.god === allyName);
  const note = notes.find((n) => n.mode === modeLabel) ?? notes[0];
  if (!note) return [];
  const core = note.builds.find(
    (b) => b.source === "suggested" && (b as CuratedBuildEntry).archetype === "core" && !(b as CuratedBuildEntry).fun,
  ) as CuratedBuildEntry | undefined;
  if (!core) return [];
  const tags = new Set<string>();
  for (const name of core.slot_order) {
    for (const t of itemsByName[name]?.effect_tags ?? []) tags.add(t);
  }
  return [...tags];
}

/** Searchable grid of eligible gods — lifted from DraftBar's picker. */
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

type SlotKind = "you" | "ally" | "enemy";

/** A single ally/enemy slot. The "you" kind (ally slot 1) carries a gold
 * ring + a "You" caption so it reads as visually distinct from the rest of
 * the row in every state, filled or empty (see spec R6). */
function Slot({
  kind, position, name, onOpen,
}: {
  kind: SlotKind;
  /** 1-based position within its own row, used for the aria-label/caption. */
  position: number;
  name: string;
  onOpen: () => void;
}) {
  const row = kind === "enemy" ? "enemy" : "ally";
  const ariaLabel = kind === "you"
    ? (name ? `Change you (${name})` : "Add you")
    : (name ? `Change ${row} ${position} (${name})` : `Add ${row} ${position}`);
  const isYou = kind === "you";

  return (
    <div className="flex flex-col items-center gap-1">
      {isYou && (
        <span className="font-display text-[9px] font-bold uppercase tracking-wider text-gold">You</span>
      )}
      {!name ? (
        <button
          type="button"
          onClick={onOpen}
          aria-label={ariaLabel}
          className={`press flex h-14 w-14 flex-none items-center justify-center rounded-md text-lg leading-none text-faint hover:text-muted ${
            isYou ? "border-2 border-gold" : "border border-dashed border-line-strong"
          }`}
        >
          +
        </button>
      ) : (
        <button
          type="button"
          onClick={onOpen}
          aria-label={ariaLabel}
          className={`press flex h-14 w-14 flex-none flex-col items-center justify-center gap-1 rounded-md bg-bg2 p-1 ${
            isYou ? "border-2 border-gold shadow-glow" : "border border-line hover:border-line-strong"
          }`}
        >
          <img
            src={`/icons/${iconSlug(name)}-head.png`}
            alt=""
            className="h-7 w-7 rounded-sm object-cover"
            onError={(e) => { e.currentTarget.style.visibility = "hidden"; }}
          />
          <span className="w-full truncate text-center font-display text-[9px] text-ink">{name}</span>
        </button>
      )}
    </div>
  );
}

const segBtn = (active: boolean) =>
  `press flex flex-col items-center rounded-md px-3.5 py-1.5 font-display text-xs font-semibold transition-colors duration-150 ease-standard ${
    active ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"
  }`;

interface DraftPageProps {
  /** Full tracked roster — used for name/damage-type/specialization lookups
   * across ally + enemy slots. */
  gods: God[];
  items: Item[];
  /** Ally-side suggested cores, used to derive what each entered ally
   * already covers (so a threat an ally already answers is damped rather
   * than double-counted). */
  builds: BuildNote[];
  godItemScores?: Record<string, Record<string, number>>;
  draftConfig?: DraftConfig;
}

/** The standalone draft page (#/draft) — mode-aware team sizes, a
 * gold-ringed "you" slot for ally 1, a comp-adapted core once you're
 * entered, and a shareable URL. See spec section B + R2 + R6. */
export function DraftPage({ gods, items, builds, godItemScores, draftConfig }: DraftPageProps) {
  // The picker (both rows) is limited to gods with a derivable core, same
  // restriction the god-page draft bar already applies.
  const eligibleGods = useMemo(
    () => (godItemScores ? gods.filter((g) => godItemScores[g.name]) : []),
    [gods, godItemScores],
  );
  const isKnownGod = useMemo(() => {
    const names = new Set(eligibleGods.map((g) => g.name));
    return (name: string) => names.has(name);
  }, [eligibleGods]);

  const { draft, mode, setMode, setAlly, setEnemy } = useDraft({ syncUrl: true, isKnownGod });
  const [pickSlot, setPickSlot] = useState<{ kind: "ally" | "enemy"; index: number } | null>(null);
  const [copied, setCopied] = useState(false);

  const godsByName = useMemo(() => {
    const m: Record<string, God> = {};
    for (const g of gods) m[g.name] = g;
    return m;
  }, [gods]);
  const itemsByName = useMemo(() => {
    const m: Record<string, Item> = {};
    for (const it of items) m[it.name] = it;
    return m;
  }, [items]);

  const meName = draft.allies[0];
  const meGod = godsByName[meName];

  const allyCores = useMemo(() => {
    const out: Record<string, string[]> = {};
    for (const name of draft.allies) {
      if (name) out[name] = allyEffectTags(name, MODE_LABEL[mode], builds, itemsByName);
    }
    return out;
  }, [draft.allies, builds, itemsByName, mode]);

  const threats = useMemo(
    () => deriveThreats(draft, godsByName, allyCores),
    [draft, godsByName, allyCores],
  );
  const chips = CHIP_DEFS.map((c) => ({ ...c, n: threats[c.key] })).filter((c) => c.n > 0);

  const draftEnabled = !!meName && !!godItemScores?.[meName] && !!draftConfig;
  const draftResult = useMemo(() => {
    if (!draftEnabled) return null;
    const opts = { maxBonus: draftConfig!.max_bonus, maxLifesteal: draftMaxLifesteal(meGod) };
    const base = adaptedCore(godItemScores![meName], itemsByName, { tags: {}, stats: {} }, opts);
    const overlay = threatOverlay(threats, draftConfig!);
    const adapted = adaptedCore(godItemScores![meName], itemsByName, overlay, opts);
    return { adapted, baseCore: new Set(base.core) };
  }, [draftEnabled, draftConfig, godItemScores, meName, itemsByName, threats, meGod]);

  const copyLink = () => {
    if (!navigator.clipboard?.writeText) return;
    navigator.clipboard.writeText(window.location.href).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 1500);
    }).catch(() => { /* clipboard permission denied — button just does nothing */ });
  };

  const closePicker = () => setPickSlot(null);
  const pick = (name: string) => {
    if (!pickSlot) return;
    if (pickSlot.kind === "enemy") setEnemy(pickSlot.index, name);
    else setAlly(pickSlot.index, name);
    closePicker();
  };

  return (
    <div className="mx-auto flex w-full max-w-3xl flex-col gap-6 p-4 pb-10 pt-6 sm:p-6">
      <div>
        <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">MODE</div>
        <div className="flex w-fit gap-1 rounded-md border border-line bg-bg1 p-1">
          {MODES.map((m) => (
            <button key={m} type="button" onClick={() => setMode(m)} className={segBtn(mode === m)}>
              {MODE_LABEL[m]}
              <span className="font-mono text-[9px] font-normal opacity-70">
                {MODE_TEAM_SIZE[m]}v{MODE_TEAM_SIZE[m]}
              </span>
            </button>
          ))}
        </div>
      </div>

      <div>
        <div className="mb-2 flex items-center justify-between">
          <span className="font-mono text-[10px] uppercase tracking-wider text-faint">Allies</span>
          <button
            type="button"
            onClick={copyLink}
            className="press rounded-md bg-bg2 px-2.5 py-1 text-[11px] text-faint hover:text-ink"
          >
            {copied ? "Copied!" : "Copy link"}
          </button>
        </div>
        <div className="flex flex-wrap gap-3">
          {draft.allies.map((name, i) => (
            <Slot
              key={i}
              kind={i === 0 ? "you" : "ally"}
              position={i + 1}
              name={name}
              onOpen={() => setPickSlot({ kind: "ally", index: i })}
            />
          ))}
        </div>
      </div>

      <div>
        <div className="mb-2 font-mono text-[10px] uppercase tracking-wider text-faint">Enemies</div>
        <div className="flex flex-wrap gap-3">
          {draft.enemies.map((name, i) => (
            <Slot
              key={i}
              kind="enemy"
              position={i + 1}
              name={name}
              onOpen={() => setPickSlot({ kind: "enemy", index: i })}
            />
          ))}
        </div>
      </div>

      {chips.length > 0 && (
        <div className="flex flex-wrap gap-1.5">
          {chips.map((c) => (
            <span key={c.key} className="rounded-full bg-bg2 px-2.5 py-1 font-mono text-[11px] text-faint">
              {c.label(c.n, threats.enemyCount)}
            </span>
          ))}
        </div>
      )}

      {!meName ? (
        <div className="rounded-md border border-dashed border-line-strong bg-bg1 p-4 text-sm text-muted">
          This is your standalone draft board — the gold-ringed slot in Allies is you. Fill it with your god
          to see a comp-adapted 6-item core, then add the rest of the draft to refine it further.
        </div>
      ) : (
        <div>
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">YOUR ADAPTED CORE</div>
          {draftEnabled && draftResult ? (
            <div className="flex flex-col gap-1">
              {draftResult.adapted.core.map((name) => {
                const isAdded = !draftResult.baseCore.has(name);
                const reason = draftResult.adapted.reasons[name];
                const it = itemsByName[name];
                return (
                  <div key={name} className="flex flex-col">
                    <div className={`flex min-h-11 items-center gap-2 rounded-md px-1.5 ${isAdded ? "bg-blue/10" : ""}`}>
                      <img
                        src={`/icons/${iconSlug(name)}.png`}
                        alt=""
                        className="h-8 w-8 flex-none rounded-sm bg-bg2"
                        onError={(e) => { e.currentTarget.style.visibility = "hidden"; }}
                      />
                      <span className={`text-sm ${isAdded ? "font-medium text-blue" : "text-ink"}`}>{name}</span>
                      {isAdded && <span className="text-[10px] text-muted">swap in</span>}
                      {it && <span className="ml-auto font-mono text-[11px] text-faint">{it.cost}g</span>}
                    </div>
                    {isAdded && reason && (
                      <div className="ml-9 mb-1 text-[10px] text-faint">↑ {reason}</div>
                    )}
                  </div>
                );
              })}
            </div>
          ) : (
            <p className="text-sm text-muted">No draft data available for {meName} yet.</p>
          )}
        </div>
      )}

      {pickSlot && (
        <GodPickerModal gods={eligibleGods} onPick={pick} onClose={closePicker} />
      )}
    </div>
  );
}
