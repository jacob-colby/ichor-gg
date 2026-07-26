/* THESIS: this page owns one claim — *your draft changed this build, here is
 * what changed and why*. It refuses the settings-form arrangement it replaced,
 * which computed the un-adapted build and the per-item bonus on every render
 * and then discarded both, leaving rows that could say "swap in" but never
 * swap in for what.
 * OWN-WORLD: Arena Night. Hairline rule-work, mono micro-labels, gold reserved
 * for selection and the model's own signal; `under`/`premium` carry direction.
 * STORY: a player fills the gold-ringed slot, adds the enemies they know, and
 * watches named items displace named items for stated reasons — with the
 * page honest about how much of the draft it still can't see.
 * FIRST VIEWPORT: a claim carrying its live count, the board, the threats
 * that drive it, then the displacement ledger.
 * FORM: guided progressive state while the board is empty or partial (the
 * assigned step-wizard, kept where it wins), giving way to a diff ledger once
 * populated. Seed key 2cd32ee3.
 */
import { useEffect, useMemo, useRef, useState } from "react";
import type { BuildNote, CuratedBuildEntry, DraftConfig, God, Item } from "../types";
import { iconSlug } from "../lib/builds";
import { toHash } from "../lib/useHashRoute";
import { useDraft, MODE_TEAM_SIZE, encodeDraftHash, type DraftMode } from "../lib/draft";
import { deriveThreats, threatOverlay, threatCulprits, type ThreatKey } from "../lib/threats";
import { adaptedCore, diffCore, type CoreChange } from "../lib/draftBuild";
import { godLane, laneTextClass, LANES, godInLane, type Lane } from "../lib/roleAccent";

const THREAT_DEFS: { key: ThreatKey; label: string; answer: string }[] = [
  { key: "magical", label: "magical", answer: "magical protection" },
  { key: "physical", label: "physical", answer: "physical protection" },
  { key: "healers", label: "healing", answer: "anti-heal" },
  { key: "lockdown", label: "crowd control", answer: "cc-immunity, peel" },
  { key: "crit", label: "crit", answer: "anti-crit" },
  { key: "tanks", label: "tanks", answer: "penetration, shred" },
];

const MODE_LABEL: Record<DraftMode, string> = { conquest: "Conquest", joust: "Joust" };
const MODES: DraftMode[] = ["conquest", "joust"];
const eyebrow = "font-mono text-[10.5px] uppercase tracking-[0.1em] text-faint";

/** Mirrors the `lifesteal_caps` rule in _weights.yaml. */
function draftMaxLifesteal(godData?: God): number {
  if (!godData || godData.damage_type !== "physical") return 1;
  const tokens = new Set([...(godData.role ?? "").split(/\s+/), ...(godData.specializations ?? [])]);
  return ["Carry", "Hunter", "Sharpshooter"].some((t) => tokens.has(t)) ? 2 : 1;
}

/** An ally's own suggested core reduced to the effect_tags its items bring —
 * the "team responsibility" signal that tells a covered job from a gap. */
function allyEffectTags(
  allyName: string, modeLabel: string, builds: BuildNote[], itemsByName: Record<string, Item>,
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

/** Art with a real fallback — an initial, never a hole in the row. */
function Icon({ name, className, item = false }: { name: string; className: string; item?: boolean }) {
  const [tries, setTries] = useState(0);
  if (tries > 1) {
    return (
      <span aria-hidden="true" className={`flex flex-none items-center justify-center rounded-sm bg-bg3 font-display text-[11px] font-bold text-faint ${className}`}>
        {name.slice(0, 1)}
      </span>
    );
  }
  return (
    <img
      src={`/icons/${iconSlug(name)}${item ? "" : "-head"}.png${tries ? "?r=1" : ""}`}
      alt="" loading="lazy" onError={() => setTries((t) => t + 1)}
      className={`flex-none rounded-sm bg-bg2 object-cover ${className}`}
    />
  );
}

/* ── God picker ───────────────────────────────────────────────────────────
 * A real dialog per the pattern DESIGN.md settled this session, plus lane
 * filters — 87 undifferentiated squares was the heaviest decision in the app
 * with the least support. Deliberately a filtered *grid*, not a combobox: the
 * results are two-dimensional, so listbox arrow semantics would misdescribe
 * them. Enter takes the first available match.
 */
function GodPickerModal({ gods, taken, onPick, onClose, opener }: {
  gods: God[];
  /** Already on the board — SMITE forbids duplicates, so they're disabled. */
  taken: Set<string>;
  onPick: (name: string) => void;
  onClose: () => void;
  /** The slot button that opened this. Captured by the parent at click time:
   * reading `document.activeElement` in this effect returns the search input,
   * because `autoFocus` commits before effects run — so focus was being
   * "restored" to an unmounting node and landing on <body>. */
  opener: HTMLElement | null;
}) {
  const [q, setQ] = useState("");
  const [lane, setLane] = useState<Lane | undefined>();
  const panelRef = useRef<HTMLDivElement>(null);
  const headingRef = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
    headingRef.current?.focus();
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") { e.stopPropagation(); onClose(); return; }
      if (e.key !== "Tab") return;
      const f = panelRef.current?.querySelectorAll<HTMLElement>(
        'a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])');
      if (!f || f.length === 0) return;
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    };
    document.addEventListener("keydown", onKeyDown, true);
    return () => { document.removeEventListener("keydown", onKeyDown, true); opener?.focus?.(); };
  }, [onClose, opener]);

  const shown = useMemo(() => {
    const ql = q.trim().toLowerCase();
    return gods.filter((g) => (!ql || g.name.toLowerCase().includes(ql)) && (!lane || godInLane(g.role, lane)));
  }, [gods, q, lane]);

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    const first = shown.find((g) => !taken.has(g.name));
    if (first) onPick(first.name);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" onClick={onClose}>
      <div
        ref={panelRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby="god-picker-title"
        className="flex max-h-[85vh] w-full max-w-2xl flex-col rounded-lg border border-line bg-bg1 p-4 shadow-raised"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="mb-3 flex items-center gap-2">
          <h2 id="god-picker-title" ref={headingRef} tabIndex={-1} className="font-display text-base font-semibold text-ink focus:outline-none">
            Pick a god
          </h2>
          <button type="button" onClick={onClose} aria-label="Close"
            className="press ml-auto rounded-md bg-bg2 px-2 py-1 font-mono text-xs text-faint hover:text-ink">✕</button>
        </div>

        <form onSubmit={submit} role="search"
          className="mb-2.5 flex items-center gap-2 rounded-md border border-line bg-bg2 px-3 py-2 focus-within:border-blue">
          <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true" className="text-muted">
            <circle cx="11" cy="11" r="7" /><path d="M21 21l-4.3-4.3" />
          </svg>
          <input
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="Search gods…"
            aria-label="Search gods"
            aria-controls="god-picker-results"
            autoComplete="off"
            className="w-full bg-transparent text-xs text-ink placeholder:text-muted focus:outline-none"
          />
        </form>

        <div className="mb-2.5 flex flex-wrap items-center gap-1.5">
          <button type="button" aria-pressed={!lane} onClick={() => setLane(undefined)}
            className={`press rounded-full border px-2.5 py-1 text-[11px] ${!lane ? "border-line-strong text-ink" : "border-line text-muted hover:border-line-strong"}`}>
            All lanes
          </button>
          {LANES.map((l) => (
            <button key={l} type="button" aria-pressed={lane === l} onClick={() => setLane(lane === l ? undefined : l)}
              className={`press rounded-full px-2.5 py-1 text-[11px] ${
                lane === l ? "bg-gold font-semibold text-bg0" : `border border-line hover:border-line-strong ${laneTextClass(l)}`}`}>
              {l}
            </button>
          ))}
        </div>

        <p aria-live="polite" className="sr-only">{shown.length} god{shown.length === 1 ? "" : "s"} match</p>

        {shown.length === 0 ? (
          <div className="flex flex-col items-center gap-2 py-8 text-center">
            <p className="text-sm text-muted">
              No {lane ? `${lane} ` : ""}god matches{q.trim() ? ` “${q.trim()}”` : " that filter"}.
            </p>
            {lane && (
              <button type="button" onClick={() => setLane(undefined)}
                className="press rounded-sm px-1 py-1 text-xs text-blue hover:underline">
                Search all lanes
              </button>
            )}
          </div>
        ) : (
          <ul id="god-picker-results" className="grid flex-1 grid-cols-[repeat(auto-fill,minmax(90px,1fr))] gap-2 overflow-y-auto">
            {shown.map((g) => {
              const isTaken = taken.has(g.name);
              const lane2 = godLane(g.role);
              return (
                <li key={g.name}>
                  <button
                    type="button"
                    disabled={isTaken}
                    onClick={() => onPick(g.name)}
                    aria-label={isTaken ? `${g.name} — already in this draft` : g.name}
                    className={`press flex w-full flex-col items-center gap-1.5 rounded-md border p-2 ${
                      isTaken ? "cursor-not-allowed border-line bg-bg2/40 opacity-40" : "border-line bg-bg2 hover:border-line-strong"}`}
                  >
                    <Icon name={g.name} className="h-9 w-9 rounded-md" />
                    <span className="max-w-full truncate text-center font-display text-[10px] text-ink">{g.name}</span>
                    {lane2 && <span className={`font-mono text-[9px] ${laneTextClass(lane2)}`}>{lane2}</span>}
                  </button>
                </li>
              );
            })}
          </ul>
        )}
      </div>
    </div>
  );
}

type SlotKind = "you" | "ally" | "enemy";

/** A single ally/enemy slot. The caption row is reserved on every ally slot so
 * the gold-ringed "you" slot's icon doesn't sit a line lower than its
 * neighbours. */
function Slot({ kind, position, name, onOpen, onRemove }: {
  kind: SlotKind; position: number; name: string; onOpen: () => void; onRemove?: () => void;
}) {
  const row = kind === "enemy" ? "enemy" : "ally";
  const rowPlural = row === "enemy" ? "enemies" : "allies";
  const ariaLabel = kind === "you"
    ? (name ? `Change you (${name})` : "Add you")
    : (name ? `Change ${row} ${position} (${name})` : `Add ${row} ${position}`);
  const isYou = kind === "you";

  return (
    <div className="flex flex-col items-center gap-1">
      {kind !== "enemy" && (
        <span aria-hidden={!isYou}
          className={`font-mono text-[9px] font-bold uppercase tracking-[0.1em] text-gold ${isYou ? "" : "invisible"}`}>
          You
        </span>
      )}
      {!name ? (
        <button type="button" onClick={onOpen} aria-label={ariaLabel}
          className={`press flex h-14 w-14 flex-none items-center justify-center rounded-md text-lg leading-none text-faint hover:border-line-strong hover:text-muted ${
            isYou ? "border-2 border-gold" : "border border-dashed border-line-strong"}`}>
          +
        </button>
      ) : (
        <div className="relative">
          <button type="button" onClick={onOpen} aria-label={ariaLabel}
            className={`press flex h-14 w-14 flex-none flex-col items-center justify-center gap-1 rounded-md bg-bg2 p-1 ${
              isYou ? "border-2 border-gold shadow-glow" : "border border-line hover:border-line-strong"}`}>
            <Icon name={name} className="h-7 w-7" />
            <span className="w-full truncate text-center font-display text-[9px] text-ink">{name}</span>
          </button>
          {/* Sibling, never nested, so it can't also fire the picker. 24×24
              minimum per WCAG 2.5.8; it was 20×20. */}
          {onRemove && (
            <button type="button" onClick={(e) => { e.stopPropagation(); onRemove(); }}
              aria-label={`Remove ${name} from ${rowPlural}`}
              className="press absolute -right-2 -top-2 flex h-6 w-6 items-center justify-center rounded-full border border-line bg-bg1 font-mono text-[10px] leading-none text-faint hover:border-line-strong hover:text-ink">
              ✕
            </button>
          )}
        </div>
      )}
    </div>
  );
}

const segBtn = (active: boolean) =>
  `press flex flex-col items-center rounded-md px-3.5 py-1.5 font-display text-xs font-semibold transition-colors duration-150 ease-standard ${
    active ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"}`;

/** One displacement: what arrived, what it pushed out, and by how much. */
function ChangeRow({ change, itemsByName, maxBonus }: {
  change: CoreChange; itemsByName: Record<string, Item>; maxBonus: number;
}) {
  const pct = maxBonus > 0 ? Math.min(100, Math.round((Math.abs(change.bonus) / maxBonus) * 100)) : 0;
  const cost = itemsByName[change.added]?.cost;
  return (
    <li className="grid grid-cols-[32px_minmax(0,1fr)_auto] items-center gap-x-2.5 gap-y-1 rounded-md px-1.5 py-2">
      <Icon name={change.added} item className="col-start-1 h-8 w-8" />
      <span className="col-start-2 flex min-w-0 flex-wrap items-baseline gap-x-2">
        <a href={toHash.item(change.added)}
          className="press -my-1 truncate rounded-sm py-1 text-[13px] font-medium text-under hover:underline">
          {change.added}
        </a>
        {change.removed && (
          <span className="font-mono text-[10px] text-faint">
            in place of <span className="text-muted line-through">{change.removed}</span>
          </span>
        )}
      </span>
      <span className="col-start-3 flex shrink-0 items-center gap-1.5">
        <span aria-hidden="true" className="h-1 w-10 rounded-sm bg-bg3">
          <span className="bar-grow block h-1 origin-left rounded-sm bg-under" style={{ width: `${pct}%` }} />
        </span>
        <span className="w-10 text-right font-mono text-[11px] text-under">+{change.bonus.toFixed(2)}</span>
      </span>
      {change.reason && (
        <span className="col-start-2 col-span-2 font-mono text-[9.5px] text-faint">
          answers {change.reason}
          {cost != null && <span className="text-faint"> · {cost}g</span>}
        </span>
      )}
    </li>
  );
}

interface DraftPageProps {
  gods: God[];
  items: Item[];
  builds: BuildNote[];
  godItemScores?: Record<string, Record<string, number>>;
  draftConfig?: DraftConfig;
}

export function DraftPage({ gods, items, builds, godItemScores, draftConfig }: DraftPageProps) {
  const eligibleGods = useMemo(
    () => (godItemScores ? gods.filter((g) => godItemScores[g.name]) : []),
    [gods, godItemScores],
  );
  const isKnownGod = useMemo(() => {
    const names = new Set(eligibleGods.map((g) => g.name));
    return (name: string) => names.has(name);
  }, [eligibleGods]);

  const { draft, mode, setMode, setAlly, setEnemy, clear } = useDraft({ syncUrl: true, isKnownGod });
  const [pickSlot, setPickSlot] = useState<{ kind: "ally" | "enemy"; index: number } | null>(null);
  const openerRef = useRef<HTMLElement | null>(null);
  const openPicker = (kind: "ally" | "enemy", index: number) => {
    openerRef.current = document.activeElement as HTMLElement | null;
    setPickSlot({ kind, index });
  };
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

  const threats = useMemo(() => deriveThreats(draft, godsByName, allyCores), [draft, godsByName, allyCores]);
  const culprits = useMemo(() => threatCulprits(draft, godsByName), [draft, godsByName]);

  const draftEnabled = !!meName && !!godItemScores?.[meName] && !!draftConfig;
  const result = useMemo(() => {
    if (!draftEnabled) return null;
    const opts = { maxBonus: draftConfig!.max_bonus, maxLifesteal: draftMaxLifesteal(meGod) };
    const base = adaptedCore(godItemScores![meName], itemsByName, { tags: {}, stats: {} }, opts);
    const adapted = adaptedCore(godItemScores![meName], itemsByName, threatOverlay(threats, draftConfig!), opts);
    // Both builds survive: the diff is the product's whole claim.
    return { base, adapted, diff: diffCore(base, adapted) };
  }, [draftEnabled, draftConfig, godItemScores, meName, itemsByName, threats, meGod]);

  const enemiesKnown = threats.enemyCount;
  const roster = threats.rosterSize;
  const taken = useMemo(
    () => new Set([...draft.allies, ...draft.enemies].filter(Boolean)),
    [draft.allies, draft.enemies],
  );

  const copyLink = () => {
    if (!navigator.clipboard?.writeText) return;
    // Encoded from state, not read off the address bar — those could disagree.
    const hash = encodeDraftHash(mode, { allies: draft.allies, enemies: draft.enemies });
    const url = window.location.origin + window.location.pathname + window.location.search + hash;
    navigator.clipboard.writeText(url).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 1500);
    }).catch(() => { /* permission denied — button just does nothing */ });
  };

  const pick = (name: string) => {
    if (!pickSlot) return;
    if (pickSlot.kind === "enemy") setEnemy(pickSlot.index, name);
    else setAlly(pickSlot.index, name);
    setPickSlot(null);
  };

  const changeCount = result?.diff.changes.length ?? 0;
  const coreSize = result?.adapted.core.length ?? 6;

  return (
    <article className="mx-auto flex w-full max-w-[1440px] flex-col gap-6 p-4 pb-12 pt-6 sm:p-6">
      <header className="border-b border-line pb-5">
        <h1 className="max-w-[26ch] text-balance font-display text-[26px] font-bold leading-[1.12] tracking-[-0.01em] text-ink sm:text-[32px]">
          {!meName
            ? <>Build for the match you&rsquo;re actually in.</>
            : changeCount > 0
              ? <>Your draft moved <span className="text-gold">{changeCount} of {coreSize}</span> items.</>
              : <>Your draft hasn&rsquo;t moved this build yet.</>}
        </h1>
        <p className="mt-2.5 max-w-[70ch] text-sm leading-relaxed text-ink-soft">
          {!meName
            ? "Put your god in the gold slot, then add the enemies as they lock in. Every item that changes shows what it displaced and which threat it answers."
            : enemiesKnown === 0
              ? changeCount > 0
                // Ally composition is draft information too — saying "nothing
                // is adapting yet" while showing changes was a contradiction.
                ? "Adapted to your ally line-up so far. Add enemies and it sharpens."
                : "The model's default core for your god. Add an enemy and it starts adapting."
              : `Scored against ${enemiesKnown} of ${roster} enemies. Each change below names what it displaced and why.`}
        </p>
      </header>

      {/* ── Board ─────────────────────────────────────────────────── */}
      <section aria-labelledby="draft-board-h">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <h2 id="draft-board-h" className={eyebrow}>The draft</h2>
          <div className="flex flex-wrap items-center gap-2">
            <div role="group" aria-label="Game mode" className="flex w-fit gap-1 rounded-md border border-line bg-bg1 p-1">
              {MODES.map((m) => (
                <button key={m} type="button" aria-pressed={mode === m} onClick={() => setMode(m)} className={segBtn(mode === m)}>
                  {MODE_LABEL[m]}
                  <span className="font-mono text-[9px] font-normal opacity-70">{MODE_TEAM_SIZE[m]}v{MODE_TEAM_SIZE[m]}</span>
                </button>
              ))}
            </div>
            <button type="button" onClick={copyLink}
              className="press rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-[11px] text-muted hover:text-ink">
              {copied ? "Copied!" : "Copy link"}
            </button>
            {taken.size > 0 && (
              <button type="button" onClick={clear}
                className="press rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-[11px] text-muted hover:text-ink">
                Clear board
              </button>
            )}
          </div>
        </div>
        <p aria-live="polite" className="sr-only">
          {meName ? `${changeCount} of ${coreSize} items changed by this draft.` : ""}
        </p>

        <div data-testid="draft-teams" className="mt-3 flex flex-col gap-5 lg:flex-row lg:gap-10">
          <div>
            <h3 className={`${eyebrow} mb-2`}>Allies</h3>
            <div className="flex flex-wrap gap-3">
              {draft.allies.map((name, i) => (
                <Slot key={i} kind={i === 0 ? "you" : "ally"} position={i + 1} name={name}
                  onOpen={() => openPicker("ally", i)}
                  onRemove={name ? () => setAlly(i, "") : undefined} />
              ))}
            </div>
          </div>
          <div>
            <h3 className={`${eyebrow} mb-2`}>Enemies</h3>
            <div className="flex flex-wrap gap-3">
              {draft.enemies.map((name, i) => (
                <Slot key={i} kind="enemy" position={i + 1} name={name}
                  onOpen={() => openPicker("enemy", i)}
                  onRemove={name ? () => setEnemy(i, "") : undefined} />
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ── Guided state ──────────────────────────────────────────
       * The board empty or barely started is the cold-start the assigned
       * step-wizard was right about: the regions below stay present as
       * labelled steps showing what will land in them, so the page teaches
       * its own mechanism instead of going blank. */}
      {(!meName || enemiesKnown === 0) && (
        <ol data-testid="draft-steps" className="grid grid-cols-1 gap-3 border-t border-line pt-5 sm:grid-cols-3">
          {[
            { n: 1, title: "Pick your god", body: "The gold-ringed slot. That alone gets you the model's default core.", done: !!meName },
            { n: 2, title: "Add the enemies you know", body: "Each one re-weights the score. Two of five is already enough to move items.", done: enemiesKnown > 0 },
            { n: 3, title: "Read what changed", body: "Every swap names the item it displaced and the threat it answers.", done: changeCount > 0 },
          ].map((step) => (
            <li key={step.n} className={`rounded-md border p-3 ${step.done ? "border-line bg-bg2/40" : "border-dashed border-line-strong"}`}>
              <p className="flex items-center gap-2 font-mono text-[10px] uppercase tracking-[0.1em]">
                <span className={step.done ? "text-under" : "text-faint"}>{step.done ? "✓" : step.n}</span>
                <span className={step.done ? "text-muted" : "text-ink-soft"}>{step.title}</span>
              </p>
              <p className="mt-1.5 text-xs leading-relaxed text-muted">{step.body}</p>
            </li>
          ))}
        </ol>
      )}

      {/* ── Threats + diff, side by side once there's room ───────── */}
      <div className="flex flex-col gap-6 xl:flex-row xl:gap-8">
      {meName && (
        <section aria-labelledby="draft-threats-h" data-testid="draft-threats" className="border-t border-line pt-5 xl:w-[340px] xl:flex-none">
          <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
            <h2 id="draft-threats-h" className={eyebrow}>What you&rsquo;re up against</h2>
            <p className="font-mono text-[10px] uppercase tracking-[0.08em] text-faint">
              {enemiesKnown} of {roster} enemies known
              {enemiesKnown < roster && <span className="text-muted"> · this build will keep moving</span>}
            </p>
          </div>
          {/* Zeros are rendered once at least one enemy is in, because a
              measured "0 of 5 crit" is a finding. With nothing entered they'd
              be the opposite error — unmeasured printed as measured. */}
          {enemiesKnown === 0 ? (
            <p className="mt-2 max-w-[64ch] text-sm leading-relaxed text-muted">
              Nothing scouted yet. Add an enemy and this fills in with what they threaten
              and which of your items answer it.
            </p>
          ) : (
          <ul className="mt-2.5 grid grid-cols-1 gap-x-5 gap-y-1.5 sm:grid-cols-2 xl:grid-cols-1">
            {THREAT_DEFS.map((t) => {
              const n = threats[t.key];
              const who = culprits[t.key];
              return (
                <li key={t.key} className="flex flex-wrap items-baseline gap-x-2 border-b border-line py-1 font-mono text-[10.5px]">
                  <span className={n > 0 ? "text-ink-soft" : "text-faint"}>{n}/{roster}</span>
                  <span className={n > 0 ? "text-muted" : "text-faint"}>{t.label}</span>
                  {who.length > 0
                    ? <span className="min-w-0 truncate text-faint">{who.join(", ")}</span>
                    : <span className="text-faint">—</span>}
                </li>
              );
            })}
          </ul>
          )}
          {threats.allyAllPhysical && threats.allyCount > 0 && (
            <p className="mt-2 font-mono text-[10px] uppercase tracking-[0.08em] text-faint">
              your side · {threats.allyPhysical} of {roster} physical · penetration raised
            </p>
          )}
        </section>
      )}

      {/* ── The diff ──────────────────────────────────────────────── */}
      {meName && (
        <section aria-labelledby="draft-core-h" data-testid="draft-core" className="min-w-0 flex-1 border-t border-line pt-5">
          <h2 id="draft-core-h" className={eyebrow}>What changed</h2>
          {!draftEnabled || !result ? (
            <p className="mt-2 max-w-[64ch] text-sm leading-relaxed text-muted">
              {meName} has no scored items in this index yet, so there&rsquo;s nothing to adapt.
              Pick a different god, or check back after the next data refresh.
            </p>
          ) : result.diff.changes.length === 0 ? (
            <div className="mt-2 max-w-[64ch]">
              <p className="text-sm leading-relaxed text-muted">
                {enemiesKnown === 0
                  ? "Nothing yet — add an enemy and the model starts re-ranking against them."
                  : "Nothing so far. This draft doesn't threaten anything the default core wasn't already handling."}
              </p>
            </div>
          ) : (
            <ul className="mt-2 flex flex-col divide-y divide-line">
              {result.diff.changes.map((c) => (
                <ChangeRow key={c.added} change={c} itemsByName={itemsByName} maxBonus={draftConfig!.max_bonus} />
              ))}
            </ul>
          )}

          {/* The build itself, with the changed rows marked in place. */}
          {result && (
            <div className="mt-5">
              <h3 className={eyebrow}>{changeCount > 0 ? "Your adapted core" : "The default core"}</h3>
              <ul className="mt-2 flex flex-col">
                {result.adapted.core.map((name, i) => {
                  const changed = result.diff.changes.some((c) => c.added === name);
                  const it = itemsByName[name];
                  return (
                    <li key={name}>
                      <a href={toHash.item(name)}
                        aria-label={`${name}${changed ? ", added by your draft" : ""}, ${it?.cost ?? "unknown"} gold`}
                        className="press grid grid-cols-[20px_32px_minmax(0,1fr)_auto] items-center gap-2.5 rounded-md py-1.5 pr-1.5 transition-colors duration-150 ease-standard hover:bg-bg1">
                        <span aria-hidden="true" className="text-right font-mono text-[10px] text-faint">{i + 1}</span>
                        <Icon name={name} item className="h-8 w-8" />
                        <span className="flex min-w-0 items-center gap-2">
                          <span className={`truncate text-[13px] ${changed ? "font-medium text-under" : "text-ink"}`}>{name}</span>
                          {changed && <span className="font-mono text-[9.5px] uppercase tracking-[0.06em] text-under">draft pick</span>}
                        </span>
                        {it && <span aria-hidden="true" className="font-mono text-[11px] text-faint">{it.cost}g</span>}
                      </a>
                    </li>
                  );
                })}
              </ul>
            </div>
          )}
        </section>
      )}

      </div>

      {pickSlot && (
        <GodPickerModal gods={eligibleGods} taken={taken} onPick={pick}
          onClose={() => setPickSlot(null)} opener={openerRef.current} />
      )}
    </article>
  );
}
