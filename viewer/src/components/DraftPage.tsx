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
import type { BuildNote, DraftConfig, God, Item } from "../types";
import { toHash } from "../lib/useHashRoute";
import { useDraft, MODE_TEAM_SIZE, encodeDraftHash, nextEmptySlot, pickerSlotLabel, type DraftMode } from "../lib/draft";
import { useDraftResult } from "../lib/useDraftResult";
import { threatAnswer, type ThreatKey } from "../lib/threats";
import { Icon, Slot, GodPickerModal } from "./DraftControls";

const THREAT_DEFS: { key: ThreatKey; label: string; answer: string }[] = [
  { key: "magical", label: "magical", answer: "magical protection" },
  { key: "physical", label: "physical", answer: "physical protection" },
  { key: "healers", label: "healing", answer: "anti-heal" },
  { key: "lockdown", label: "crowd control", answer: "cc-immunity, peel" },
  { key: "crit", label: "crit", answer: "anti-crit" },
  { key: "tanks", label: "tanks", answer: "penetration, shred" },
  { key: "walls", label: "player-made walls", answer: "Shell of Rebuke" },
];

const MODE_LABEL: Record<DraftMode, string> = { conquest: "Conquest", joust: "Joust", arena: "Arena" };
const MODES: DraftMode[] = ["conquest", "joust", "arena"];
const eyebrow = "font-mono text-label uppercase tracking-[0.1em] text-faint";

const segBtn = (active: boolean) =>
  `press flex flex-col items-center rounded-md px-3.5 py-1.5 font-display text-small font-semibold transition-colors duration-150 ease-standard ${
    active ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"}`;

/** One displacement: what arrived, what it pushed out, and by how much. */
function ChangeRow({ change, itemsByName, maxBonus }: {
  change: { added: string; removed?: string; bonus: number; reason?: string };
  itemsByName: Record<string, Item>; maxBonus: number;
}) {
  const pct = maxBonus > 0 ? Math.min(100, Math.round((Math.abs(change.bonus) / maxBonus) * 100)) : 0;
  const cost = itemsByName[change.added]?.cost;
  return (
    <li className="grid grid-cols-[36px_minmax(0,1fr)_auto] items-center gap-x-3 gap-y-1 rounded-md border border-line bg-bg2/50 px-2 py-2.5">
      <Icon name={change.added} item className="col-start-1 h-9 w-9" />
      <span className="col-start-2 flex min-w-0 flex-wrap items-baseline gap-x-2">
        <a href={toHash.item(change.added)}
          className="press -my-1 truncate rounded-sm py-1 text-body font-medium text-under hover:underline">
          {change.added}
        </a>
        {change.removed && (
          <span className="text-label text-faint">
            in place of <span className="text-muted line-through">{change.removed}</span>
          </span>
        )}
      </span>
      <span className="col-start-3 flex shrink-0 items-center gap-1.5">
        <span aria-hidden="true" className="h-1 w-10 rounded-sm bg-bg3">
          <span className="bar-grow block h-1 origin-left rounded-sm bg-under" style={{ width: `${pct}%` }} />
        </span>
        <span className="w-10 text-right font-mono text-label text-under">+{change.bonus.toFixed(2)}</span>
      </span>
      {/* WHY an item was promoted is the page's whole claim, and it was set in
          `faint` at 11px — the app's quietest tier, the same one incidental
          captions use. It reads at `small`/`muted` now, with the threat names
          in `ink-soft` so the answer stands out inside its own sentence. */}
      {change.reason && (
        <span className="col-start-2 col-span-2 text-small text-muted">
          answers <span className="text-ink-soft">{change.reason}</span>
          {cost != null && <span className="font-mono text-faint"> · {cost}g</span>}
        </span>
      )}
    </li>
  );
}

/** An item both builds buy, at a different point in the order.
 *
 *  Deliberately quieter than `ChangeRow`: a swap changes WHAT you buy and a
 *  move changes WHEN, and the page should not spend the same emphasis on both.
 *  No bonus bar — an item can move because something else did, in which case
 *  its own bonus is 0.00 and a bar would imply a force that wasn't applied. */
function MoveRow({ move, itemsByName }: {
  move: { name: string; from: number; to: number; bonus: number; reason?: string };
  itemsByName: Record<string, Item>;
}) {
  const earlier = move.to < move.from;
  const cost = itemsByName[move.name]?.cost;
  return (
    <li
      data-testid="draft-moved"
      className="grid grid-cols-[36px_minmax(0,1fr)_auto] items-center gap-x-3 gap-y-1 rounded-md border border-line bg-bg2/50 px-2 py-2.5"
    >
      <Icon name={move.name} item className="col-start-1 h-9 w-9" />
      <span className="col-start-2 flex min-w-0 flex-wrap items-baseline gap-x-2">
        <a href={toHash.item(move.name)}
          className="press -my-1 truncate rounded-sm py-1 text-body font-medium text-ink hover:underline">
          {move.name}
        </a>
        <span className="text-label text-faint">
          {earlier ? "earlier" : "later"} — slot{" "}
          <span className="font-mono text-muted">{move.from}</span>
          <span aria-hidden="true"> → </span>
          <span className="font-mono text-ink-soft">{move.to}</span>
        </span>
      </span>
      <span className="col-start-3 shrink-0 font-mono text-label text-faint">
        {move.bonus > 0 ? `+${move.bonus.toFixed(2)}` : "—"}
      </span>
      {move.reason && (
        <span className="col-start-2 col-span-2 text-small text-muted">
          answers <span className="text-ink-soft">{move.reason}</span>
          {cost != null && <span className="font-mono text-faint"> · {cost}g</span>}
        </span>
      )}
    </li>
  );
}

interface DraftPageProps {
  gods: God[];
  items: Item[];
  builds: BuildNote[];
  godItemScores?: Record<string, Record<string, Record<string, number>>>;
  /** B6: per-item damage against a squishy vs a tank. Optional — an older
   *  index simply leaves the damage term out of the overlay. */
  godItemDamage?: Record<string, Record<string, [number, number]>>;
  draftConfig?: DraftConfig;
}

export function DraftPage({ gods, items, builds, godItemScores, godItemDamage, draftConfig }: DraftPageProps) {
  const eligibleGods = useMemo(
    () => (godItemScores ? gods.filter((g) => godItemScores[g.name]) : []),
    [gods, godItemScores],
  );
  const isKnownGod = useMemo(() => {
    const names = new Set(eligibleGods.map((g) => g.name));
    return (name: string) => names.has(name);
  }, [eligibleGods]);

  const { draft, mode, setMode, setAlly, setEnemy, clear, dropped, dismissDropped } =
    useDraft({ syncUrl: true, isKnownGod });
  const [pickSlot, setPickSlot] = useState<{ kind: "ally" | "enemy"; index: number } | null>(null);
  const openerRef = useRef<HTMLElement | null>(null);
  const openPicker = (kind: "ally" | "enemy", index: number) => {
    openerRef.current = document.activeElement as HTMLElement | null;
    setPickSlot({ kind, index });
  };
  const [copied, setCopied] = useState(false);
  /* The draft builds for YOUR god, so only your aspect can change anything it
     shows. Reset when the you-slot changes — an aspect describes a god. */
  const [aspectOn, setAspectOn] = useState(false);

  const {
    meName, itemsByName, taken, takenFor, enemiesKnown, roster, threatCulprits: culprits,
    allyAllPhysical, allyCount, allyPhysical, result, draftEnabled, changeCount, moveCount, coreSize, starters,
    startersAreConquest, relicPicks, aspectScored, meGod,
  } = useDraftResult(draft, mode, gods, items, builds, godItemScores, draftConfig, godItemDamage,
    aspectOn);
  const meAspect = meGod?.aspects?.[0]?.name;
  useEffect(() => { setAspectOn(false); }, [meName]);

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

  /* Fill the slot, then move to the next empty one on that side rather than
     closing — see `nextEmptySlot`. `draft` is read before the write on
     purpose: the rule looks FORWARD of the slot just filled, and those slots
     are the ones this pick cannot have changed. */
  const pick = (name: string) => {
    if (!pickSlot) return;
    const side = pickSlot.kind === "enemy" ? draft.enemies : draft.allies;
    const wasEmpty = !side[pickSlot.index];
    if (pickSlot.kind === "enemy") setEnemy(pickSlot.index, name);
    else setAlly(pickSlot.index, name);
    setPickSlot(nextEmptySlot(draft, pickSlot.kind, pickSlot.index, wasEmpty));
  };

  return (
    <article className="mx-auto flex w-full max-w-[1440px] flex-col gap-6 p-4 pb-12 pt-6 sm:p-6">
      <header className="border-b border-line pb-5">
        <h1 className="max-w-[26ch] text-balance font-display text-display font-bold leading-[1.12] tracking-[-0.01em] text-ink sm:text-display">
          {!meName
            ? <>Build for the match you&rsquo;re actually in.</>
            : changeCount > 0
              ? <>Your draft moved <span className="text-gold">{changeCount} of {coreSize}</span> items.</>
              // Reordering the same six IS moving the build. The headline said
              // it had not, above a list that had.
              : moveCount > 0
                ? <>Your draft <span className="text-gold">resequenced</span> this build.</>
                : <>Your draft hasn&rsquo;t moved this build yet.</>}
        </h1>
        <p className="mt-2.5 max-w-[70ch] text-body leading-relaxed text-ink-soft">
          {!meName
            ? "Put your god in the gold slot, then add the enemies as they lock in. Every item that changes shows what it displaced and which threat it answers."
            : enemiesKnown === 0
              ? changeCount > 0 || moveCount > 0
                // Ally composition is draft information too — saying "nothing
                // is adapting yet" while showing changes was a contradiction.
                ? "Adapted to your ally line-up so far. Add enemies and it sharpens."
                : "The model's default core for your god. Add an enemy and it starts adapting."
              : `Scored against ${enemiesKnown} of ${roster} enemies. Each change below names what it displaced and why.`}
        </p>
          {/* Seam to the working (DESIGN.md, the Seam Rule; audit's central
              finding). Named as the visitor's own question, not as the route. */}
        <p className="mt-2.5">
          <a
            href={toHash.method()}
            data-testid="method-seam"
            className="press -mx-1 rounded-sm px-1 py-1.5 text-label font-medium text-blue hover:underline"
          >
            Where these scores come from &rarr;
          </a>
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
                  <span className="text-micro font-normal opacity-70">{MODE_TEAM_SIZE[m]}v{MODE_TEAM_SIZE[m]}</span>
                </button>
              ))}
            </div>
            <button type="button" onClick={copyLink}
              className="press rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-label text-muted hover:text-ink">
              {copied ? "Copied!" : "Copy link"}
            </button>
            {taken.size > 0 && (
              <button type="button" onClick={clear}
                className="press rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-label text-muted hover:text-ink">
                Clear board
              </button>
            )}
          </div>
        </div>
        <p aria-live="polite" className="sr-only">
          {meName ? `${changeCount} of ${coreSize} items changed by this draft.` : ""}
        </p>

        {/* A shared link that quietly came up a god short. The validation is
            right — a slot holding a god with no scored build can only render
            as a hole — but the board silently disagreed with the link that
            produced it, and the address bar was then rewritten to match the
            board, erasing the evidence. Says which names and why, next to the
            row that is missing them. Not gold: this is the page reporting on
            its own input, not the model talking (audit F11). */}
        {dropped.length > 0 && (
          <div role="status"
            className="mt-3 flex items-start gap-3 rounded-md border border-line-strong bg-bg2 px-3 py-2.5">
            <p className="min-w-0 text-small text-muted">
              <span className="text-ink-soft">{dropped.join(", ")}</span>
              {dropped.length === 1 ? " has" : " have"} no scored build here, so{" "}
              {dropped.length === 1 ? "that slot" : "those slots"} came up empty. The rest of the
              link loaded.
            </p>
            <button type="button" onClick={dismissDropped} aria-label="Dismiss"
              className="press ml-auto flex h-6 w-6 flex-none items-center justify-center rounded-sm text-small text-faint hover:text-ink">
              ✕
            </button>
          </div>
        )}

        <div data-testid="draft-teams" className="mt-3 flex flex-col gap-5 lg:flex-row lg:gap-10">
          <div>
            <h3 className={`${eyebrow} mb-2`}>Allies</h3>
            <div className="flex flex-wrap gap-3">
              {draft.allies.map((name, i) => (
                <Slot key={i} kind={i === 0 ? "you" : "ally"} position={i + 1} name={name}
                  slotId={`ally-${i}`}
                  onOpen={() => openPicker("ally", i)}
                  onRemove={name ? () => setAlly(i, "") : undefined}
                  aspectName={i === 0 ? meAspect : undefined}
                  aspectOn={i === 0 ? aspectOn : undefined}
                  onToggleAspect={i === 0 && meAspect ? () => setAspectOn((v) => !v) : undefined}
                  aspectChangesBuild={i === 0
                    ? !!godItemScores?.[name]?.[`${mode}:aspect`] : undefined} />
              ))}
            </div>
          </div>
          <div>
            <h3 className={`${eyebrow} mb-2`}>Enemies</h3>
            <div className="flex flex-wrap gap-3">
              {draft.enemies.map((name, i) => (
                <Slot key={i} kind="enemy" position={i + 1} name={name}
                  slotId={`enemy-${i}`}
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
              <p className="flex items-center gap-2 text-label font-semibold uppercase tracking-[0.08em]">
                <span className={step.done ? "text-under" : "text-faint"}>{step.done ? "✓" : step.n}</span>
                <span className={step.done ? "text-muted" : "text-ink-soft"}>{step.title}</span>
              </p>
              <p className="mt-1.5 text-small leading-relaxed text-muted">{step.body}</p>
            </li>
          ))}
        </ol>
      )}

      {/* ── The core, then why it moved — side by side once there's room ── */}
      {/* The core leads: it is what this page produces. The threats explain
          why it moved, so they follow. Reading input, then explanation, then
          answer put the answer last — and below the fold under 1280px. */}
      <div className="flex flex-col gap-6 xl:flex-row xl:gap-8">
      {meName && (
        <section aria-labelledby="draft-core-h" data-testid="draft-core"
          className="plane min-w-0 flex-1 rounded-lg border border-line bg-bg1 p-4 sm:p-5">
          {/* The build leads. It is the thing the page exists to produce, and
              it used to sit UNDER the diff that explains it — so the answer was
              below the footnote, and on a narrow screen the first thing a
              reader saw was a list of items they hadn't been shown yet. The
              diff still earns its place; it just isn't the headline. */}
          {/* Measured before changing it: this heading, the reasoning line and
              the incidental captions were all 11px / weight 400 / `faint` —
              the same size, weight AND colour, so there was no ratio anywhere
              between the deliverable and its chrome. That is what "the UI
              feels flat" describes.
              The eyebrow stays an eyebrow: DESIGN.md's convention is a quiet
              mono label over loud content, and the loud content here is the
              item list, not the word "core". It moves off `faint` only so it
              stops matching the reasoning line exactly. */}
          <h2 id="draft-core-h" className="font-mono text-label uppercase tracking-[0.1em] text-muted">
            {changeCount > 0 ? "Your adapted core" : "The default core"}
            {/* 65 of the 72 gods with an aspect have no scoring overlay behind
                it, so the toggle can be pressed and change nothing. Saying so
                beats a control that looks broken. */}
            {aspectOn && (
              <span className="ml-2 normal-case tracking-normal text-aspect">
                {aspectScored
                  ? `· ${meAspect?.replace(/^Aspect of (the )?/i, "")}`
                  : `· ${meAspect?.replace(/^Aspect of (the )?/i, "")} — kit only, no build change scored`}
              </span>
            )}
          </h2>
          {/* No community data exists for this mode's own build note — see §1
              of STATE.md — so the score behind this core is efficiency and
              kit-fit alone, same as `DetailPanel`'s "No outcome data exists"
              line on the god page. Without this the tab looks identical to
              Conquest's and reads as equally meta-backed, which it isn't. */}
          {mode !== "conquest" && (
            <p className="mt-1 max-w-[64ch] text-label leading-relaxed text-muted">
              <span className="text-premium">No outcome data exists for {MODE_LABEL[mode]}.</span>{" "}
              This core is ranked by efficiency and kit-fit alone — not by what {MODE_LABEL[mode]} players buy.
            </p>
          )}
          {!draftEnabled || !result ? (
            <p className="mt-2 max-w-[64ch] text-body leading-relaxed text-muted">
              {meName} has no scored items in this index yet, so there&rsquo;s nothing to adapt.
              Pick a different god, or check back after the next data refresh.
            </p>
          ) : (
            <>
            <div>

              {/* A build starts before item one, and this page began at item
                  one — so the first purchase of the match was the one thing it
                  never showed. These are what this god's players actually open
                  with, scraped from the same source as the build itself; the
                  draft doesn't move them, which is why they sit apart from the
                  numbered core rather than as slot zero. */}
              {starters.length > 0 && (
                <div data-testid="draft-starters" className="mt-2 border-b border-line pb-3">
                  <div className="flex flex-wrap items-baseline gap-x-2">
                    <span className="text-label text-faint">Opens with</span>
                    <span className="text-label text-muted">
                      · by pick rate, not adapted by your draft
                      {startersAreConquest &&
                        ` · ${MODE_LABEL.conquest} data, no ${MODE_LABEL[mode]} openers are tracked`}
                    </span>
                  </div>
                  {/* One chip per PURCHASE PATH, not per item. Leather Cowl and
                      Hunter's Cowl are the same opener at two moments, and 84
                      of 89 gods had both halves inside this three-slot row —
                      so a third of the answer was spent restating one pick.
                      The two rates are shown, never summed: a player who buys
                      the base and upgrades it is counted in both, so adding
                      them would invent a number bigger than the truth. */}
                  <ul className="mt-1.5 flex flex-wrap gap-1.5">
                    {starters.map((p) => {
                      const end = p.upgrade ?? p.base!;
                      const both = !!(p.base && p.upgrade);
                      return (
                        <li key={p.rootName}>
                          <a href={toHash.item(end.name)}
                            title={both
                              ? `${Math.round(p.base!.pick_rate * 100)}% open with ${p.base!.name}; ${Math.round(p.upgrade!.pick_rate * 100)}% are holding ${p.upgrade!.name}`
                              : `${Math.round(end.pick_rate * 100)}% open with ${end.name}, winning ${Math.round(end.win_rate * 100)}%`}
                            aria-label={both
                              ? `${p.base!.name} into ${p.upgrade!.name} — ${Math.round(p.base!.pick_rate * 100)}% of ${meName} players open with it, ${Math.round(p.upgrade!.pick_rate * 100)}% are holding the upgrade`
                              : `${end.name} — opened with by ${Math.round(end.pick_rate * 100)}% of ${meName} players, winning ${Math.round(end.win_rate * 100)}%`}
                            className="press flex items-center gap-1.5 rounded-md border border-line bg-bg2 py-1 pl-1 pr-2 transition-colors duration-150 ease-standard hover:border-line-strong">
                            {p.base && <Icon name={p.base.name} item className="h-6 w-6" />}
                            {both && (
                              // The path's own arrow, in `faint` — it separates
                              // two icons rather than labelling either.
                              <span aria-hidden="true" className="-mx-0.5 text-label text-faint">›</span>
                            )}
                            {p.upgrade && <Icon name={p.upgrade.name} item className="h-6 w-6" />}
                            <span className="max-w-[13ch] truncate text-small text-ink">{end.name}</span>
                            <span aria-hidden="true" className="font-mono text-label text-gold">
                              {Math.round(p.lead.pick_rate * 100)}%
                            </span>
                            {both && (
                              // Where along the path people actually end up.
                              <span aria-hidden="true" className="font-mono text-micro text-faint">
                                {Math.round(p.base!.pick_rate * 100)}→{Math.round(p.upgrade!.pick_rate * 100)}
                              </span>
                            )}
                          </a>
                        </li>
                      );
                    })}
                  </ul>
                </div>
              )}
              {/* The purchase spine: one continuous hairline the whole build
                  hangs off, the same device the god page's ledger uses for
                  cumulative gold. A draft pick notches it. */}
              <ul className="mt-2 flex flex-col border-l border-line pl-1">
                {result.adapted.core.map((name, i) => {
                  const changed = result.diff.changes.some((c) => c.added === name);
                  const it = itemsByName[name];
                  return (
                    <li key={name}>
                      {/* The build row is the product. It was a 13px name and
                          a 32px icon on the page ground, which is the same
                          presence as a caption. Bigger art and a name a step up
                          the scale fix that.

                          The draft pick is marked ON THE SPINE, not with a
                          coloured left border. The border was a 2px `under`
                          rule down the row — the generic accent-bar every
                          dashboard reaches for, and a shape this world does not
                          otherwise use. The tier ladder already owns the
                          grammar for "the model's own mark": a rotated square
                          sitting on a rule, so the pair never depends on colour
                          alone. The purchase column is that rule here. */}
                      <a href={toHash.item(name)}
                        aria-label={`${name}${changed ? ", added by your draft" : ""}, ${it?.cost ?? "unknown"} gold`}
                        className="press relative grid grid-cols-[18px_40px_minmax(0,1fr)_auto] items-center gap-3 rounded-md bg-bg2/40 py-2 pl-1.5 pr-2 transition-colors duration-150 ease-standard hover:bg-bg2">
                        <span aria-hidden="true"
                          className={`relative text-right font-mono text-label ${changed ? "text-under" : "text-faint"}`}>
                          {i + 1}
                          {changed && (
                            <span aria-hidden="true"
                              className="absolute -right-2 top-1/2 h-1.5 w-1.5 -translate-y-1/2 rotate-45 bg-under" />
                          )}
                        </span>
                        <Icon name={name} item className="h-10 w-10" />
                        <span className="flex min-w-0 flex-wrap items-baseline gap-x-2">
                          <span className={`truncate font-display text-lead font-semibold ${changed ? "text-under" : "text-ink"}`}>{name}</span>
                          {changed && <span className="text-micro font-semibold uppercase tracking-[0.06em] text-under">draft pick</span>}
                        </span>
                        {it && <span aria-hidden="true" className="font-mono text-small text-muted">{it.cost}g</span>}
                      </a>
                    </li>
                  );
                })}
              </ul>
            </div>

            {/* An UPGRADED relic does take one of the six -- only the free
                base relic gets the game's own slot -- so this is a genuine
                build suggestion, not a parallel one. It still needs its own
                line because the model will not pick it for you: its "+7.5% of
                all Stats from Items" is a multiplier nothing here can price,
                so the gold model reads it as 698g overpriced and it never wins
                a slot on score. Same blindness as Genie's Lamp. */}
            {relicPicks.length > 0 && (
              <div data-testid="draft-relics" className="mt-3 border-t border-line pt-3">
                <div className="flex flex-wrap items-baseline gap-x-2">
                  <span className="text-label text-faint">Relic</span>
                  <span className="text-label text-muted">· takes one of your six · the model can&rsquo;t price it, so it won&rsquo;t pick it for you</span>
                </div>
                <ul className="mt-1.5 flex flex-col gap-1">
                  {relicPicks.map((r) => (
                    <li key={r.item}>
                      <a href={toHash.item(r.item)}
                        aria-label={`${r.item} — ${r.because}, against ${r.count} enemies`}
                        className="press flex items-center gap-2 rounded-md border border-line bg-bg2 py-1 pl-1 pr-2.5 transition-colors duration-150 ease-standard hover:border-line-strong">
                        <Icon name={r.item} item className="h-7 w-7" />
                        <span className="min-w-0 flex-1 truncate text-small text-ink">{r.item}</span>
                        <span className="truncate text-label text-faint">{r.because}</span>
                      </a>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            <div className="mt-5" data-testid="draft-changed">
              <h3 className={eyebrow}>What changed</h3>
              {result.diff.changes.length === 0 && !result.diff.orderOnly ? (
                <p className="mt-2 max-w-[64ch] text-body leading-relaxed text-muted">
                  {enemiesKnown === 0
                    ? "Nothing yet — add an enemy and the model starts re-ranking against them."
                    : "Nothing so far. This draft doesn't threaten anything the default core wasn't already handling."}
                </p>
              ) : (
                <>
                  {/* A draft that reorders the same six items used to land in
                      the branch above — "nothing changed", printed under a
                      build that had visibly changed. The order is a claim the
                      page makes, so it gets a sentence rather than silence. */}
                  {result.diff.orderOnly && (
                    <p className="mt-2 max-w-[64ch] text-body leading-relaxed text-muted">
                      Same six items, <span className="text-ink-soft">different order</span> — this
                      draft doesn&rsquo;t change what to buy, it changes when.
                    </p>
                  )}
                  <ul className="mt-2 flex flex-col gap-1.5">
                    {result.diff.changes.map((c) => (
                      <ChangeRow key={c.added} change={c} itemsByName={itemsByName} maxBonus={draftConfig!.max_bonus} />
                    ))}
                    {result.diff.moved.map((m) => (
                      <MoveRow key={`move-${m.name}`} move={m} itemsByName={itemsByName} />
                    ))}
                  </ul>
                </>
              )}
            </div>
            </>
          )}
        </section>
      )}


      {meName && (
        <section aria-labelledby="draft-threats-h" data-testid="draft-threats" className="border-t border-line pt-5 xl:w-[340px] xl:flex-none xl:border-l xl:border-t-0 xl:pl-8 xl:pt-0">
          <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
            <h2 id="draft-threats-h" className={eyebrow}>What you&rsquo;re up against</h2>
            <p className="text-label text-faint">
              {enemiesKnown} of {roster} enemies known
              {enemiesKnown < roster && <span className="text-muted"> · this build will keep moving</span>}
            </p>
          </div>
          {/* Zeros are rendered once at least one enemy is in, because a
              measured "0 of 5 crit" is a finding. With nothing entered they'd
              be the opposite error — unmeasured printed as measured. */}
          {enemiesKnown === 0 ? (
            <p className="mt-2 max-w-[64ch] text-body leading-relaxed text-muted">
              Nothing scouted yet. Add an enemy and this fills in with what they threaten
              and which of your items answer it.
            </p>
          ) : (
          <ul className="mt-2.5 grid grid-cols-1 gap-x-5 gap-y-1.5 sm:grid-cols-2 xl:grid-cols-1">
            {THREAT_DEFS.map((t) => {
              // `deriveThreats`' count and `threatCulprits`' list use the same
              // predicate over the same enemies, so the list's length is the
              // count — one source, not two that could disagree.
              const who = culprits[t.key];
              /* F10. A named threat that changed nothing left the reader
                 unable to tell "weighed and nothing beat the core" from "never
                 considered". Every other row on this page states its
                 reasoning; this one went quiet exactly where it mattered. */
              const answer = who.length > 0
                ? threatAnswer(t.key, result?.adapted.core ?? [], itemsByName, draftConfig)
                : null;
              return (
                <li key={t.key} className="flex flex-wrap items-baseline gap-x-2 border-b border-line py-1 text-label">
                  <span className={`font-mono ${who.length > 0 ? "text-ink-soft" : "text-faint"}`}>{who.length}/{roster}</span>
                  <span className={who.length > 0 ? "text-muted" : "text-faint"}>{t.label}</span>
                  {who.length > 0
                    ? <span className="min-w-0 truncate text-faint">{who.join(", ")}</span>
                    : <span className="text-faint">—</span>}
                  {answer && (
                    <span className="basis-full truncate text-label text-faint">
                      {answer.kind === "answered" ? (
                        // Two names and a count, not the whole list: against a
                        // three-tank comp six of Ra's items carry penetration
                        // or shred, and naming all six in a 340px column is the
                        // dump F7 is about. `truncate` would hide the tail
                        // silently, which is worse than saying how long it is.
                        <>
                          <span className="text-under">answered</span> ·{" "}
                          {answer.by.slice(0, 2).join(", ")}
                          {answer.by.length > 2 && ` +${answer.by.length - 2}`}
                        </>
                      ) : answer.kind === "weighed" ? (
                        // True by construction: `threatOverlay` raises every
                        // item carrying this threat's tags or stats the moment
                        // the count is non-zero. Nothing carrying them won a slot.
                        <>weighed · nothing that answers it outscored the core</>
                      ) : (
                        // `walls` is the only one, and the relic row above says
                        // what the model offers instead.
                        <>no item answers this{draftConfig?.relics?.[t.key] ? " · relic only" : ""}</>
                      )}
                    </span>
                  )}
                </li>
              );
            })}
          </ul>
          )}
          {allyAllPhysical && allyCount > 0 && (
            <p className="mt-2 text-label text-faint">
              your side · {allyPhysical} of {roster} physical · penetration raised
            </p>
          )}
        </section>
      )}

      </div>

      {pickSlot && (
        <GodPickerModal gods={eligibleGods} taken={takenFor(pickSlot.kind, pickSlot.index)} onPick={pick}
          onClose={() => setPickSlot(null)} opener={openerRef.current}
          slotLabel={pickerSlotLabel(pickSlot.kind, pickSlot.index)}
          restoreSlot={`${pickSlot.kind}-${pickSlot.index}`} />
      )}
    </article>
  );
}
