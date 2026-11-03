/** The draft board (`#/draft`), on the enemy strip's grammar.
 *
 * Two rows of five slots — your team (you in violet, then four allies) and the
 * enemy (ink outline, never a hue) — each slot opening the same picker sheet
 * the god page uses. Under them, the six the god page ships for you (the
 * `model` archetype), adapted to the team, with every swap ringed and its
 * reason on the row; above them, the swaps said as sentences: "Divine Ruin
 * replaces Spear of the Magus · answers healing".
 *
 * Product truth kept from the old DraftPage (its comments carry the evidence):
 *  - Threats are denominated by the ROSTER ("2 of 5 heal"), never by how many
 *    enemies are entered — one known healer is not a 100% threat.
 *  - Measured zeros print once anything is scouted, and not before: "0 of 5"
 *    is a finding after a scout and unmeasured-printed-as-measured before one.
 *  - "N of 5 enemies known", and while any are unknown the page says the build
 *    will keep moving.
 *  - A threat that changed nothing says it was weighed; one no item can answer
 *    says so and names the relic.
 *  - The draft changes WHAT you buy, never WHEN: a swap takes the slot of the
 *    item it replaced.
 *  - Joust and Arena have no outcome data; the six there rests on the model
 *    alone and says so. A borrowed record is disclosed, never passed off.
 *  - A shared link that named gods this index can't place says which, next to
 *    the board, and the board's state is the link (`#/draft?m=…&me=…&e=…`).
 */
import { useEffect, useMemo, useState, type ReactNode } from "react";
import type { BuildNote, CommunityBuildEntry, DraftConfig, God, Item } from "../../types";
import { useDraft, MODE_TEAM_SIZE, encodeDraftHash } from "../../lib/draft";
import { useDraftResult } from "../../lib/useDraftResult";
import { threatAnswer } from "../../lib/threats";
import { toHash } from "../../lib/useHashRoute";
import { queryHash } from "../command/query";
import { Art, CloseGlyph, PlusGlyph } from "./art";
import { ModeSwitch } from "./ModeSwitch";
import { AspectToggle } from "./AspectToggle";
import { ItemRow } from "./ItemRow";
import { EnemySheet } from "./EnemySheet";
import { itemReason } from "./itemReason";
import { MAIN_ARCHETYPE, aspectNote } from "./pageState";
import { listWords, MODE_NAME } from "./verdict";
import { useWide } from "./useWide";
import { Em, PageHead, Seam } from "./PageParts";
import { THREATS, displacement, displacementText } from "./displacement";

type Side = "ally" | "enemy";

function Slot({ name, index, side, onOpen }: { name: string; index: number; side: Side; onOpen: () => void }) {
  const you = side === "ally" && index === 0;
  const word = you ? "You" : side === "ally" ? `Ally ${index + 1}` : `Enemy ${index + 1}`;
  const ring = you ? "ring-2 ring-accent" : side === "enemy" ? "ring-[1.5px] ring-ink" : "ring-1 ring-line-strong";
  return (
    <li className="min-w-0">
      <button type="button" onClick={onOpen} data-slot={`${side}-${index}`}
        aria-label={name ? `${word}: ${name}. Change` : `Add ${you ? "your god" : word.toLowerCase()}`}
        className="press flex w-full flex-col items-center gap-1.5">
        {name ? (
          <Art name={name} kind="head" className={`aspect-square w-full max-w-[72px] rounded-[10px] ${ring}`} />
        ) : (
          <span className={`flex aspect-square w-full max-w-[72px] items-center justify-center rounded-[10px] border-[1.5px] border-dashed ${
            you ? "border-accent text-accent" : "border-quiet text-muted"}`}>
            <PlusGlyph size={20} />
          </span>
        )}
        <span className={`w-full text-center text-cap leading-tight [overflow-wrap:anywhere] ${
          you ? "font-semibold text-accent" : name ? "text-ink" : "text-quiet"}`}>
          {you ? (name || "You") : name || "Empty"}
        </span>
      </button>
    </li>
  );
}

function TeamRow({ title, side, slots, onOpen, meta }: {
  title: string; side: Side; slots: string[]; onOpen: (i: number) => void; meta?: ReactNode;
}) {
  return (
    <section aria-label={title} data-testid={`team-${side}`}>
      <div className="flex items-baseline justify-between gap-3">
        <h2 className="font-cond text-[20px] font-extrabold text-ink">{title}</h2>
        {meta}
      </div>
      <ol className="mt-2 grid gap-2" style={{ gridTemplateColumns: `repeat(${slots.length}, minmax(0, 1fr))` }}>
        {slots.map((n, i) => <Slot key={i} name={n} index={i} side={side} onOpen={() => onOpen(i)} />)}
      </ol>
    </section>
  );
}

interface DraftBoardProps {
  gods: God[];
  items: Item[];
  builds: BuildNote[];
  godItemScores?: Record<string, Record<string, Record<string, number>>>;
  godItemDamage?: Record<string, Record<string, [number, number]>>;
  draftConfig?: DraftConfig;
  /** The build the board adapts — the god page's own six. */
  initialArchetype?: string;
}

export function DraftBoard({ gods, items, builds, godItemScores, godItemDamage, draftConfig, initialArchetype = MAIN_ARCHETYPE }: DraftBoardProps) {
  const wide = useWide();
  const eligible = useMemo(() => (godItemScores ? gods.filter((g) => godItemScores[g.name]) : []), [gods, godItemScores]);
  const isKnownGod = useMemo(() => {
    const names = new Set(eligible.map((g) => g.name));
    return (n: string) => names.has(n);
  }, [eligible]);
  const { draft, mode, setMode, setAlly, setEnemy, clear, dropped, dismissDropped } = useDraft({ syncUrl: true, isKnownGod });

  const [aspectOn, setAspectOn] = useState(false);
  const r = useDraftResult(draft, mode, gods, items, builds, godItemScores, draftConfig, godItemDamage, aspectOn, initialArchetype);
  const me = r.meName;
  useEffect(() => { setAspectOn(false); }, [me]);
  const meAspect = r.meGod?.aspects?.[0]?.name;
  const aspectChanges = !!(me && godItemScores?.[me]?.[`${mode}:aspect`]);

  const [sheet, setSheet] = useState<{ side: Side; index: number } | null>(null);
  const [copied, setCopied] = useState(false);
  const copyLink = () => {
    if (!navigator.clipboard?.writeText) return;
    // Encoded from state, not read off the address bar — those could disagree.
    const hash = encodeDraftHash(mode, { allies: draft.allies, enemies: draft.enemies });
    navigator.clipboard.writeText(window.location.origin + window.location.pathname + window.location.search + hash)
      .then(() => { setCopied(true); window.setTimeout(() => setCopied(false), 1500); })
      .catch(() => { /* permission denied: the button stays as it was */ });
  };

  const roster = r.roster;
  const known = r.enemiesKnown;
  const changes = r.result?.diff.changes ?? [];
  const lines = changes.map((c) => displacement(c, draftConfig, r.threatCulprits));
  const swaps = new Map(changes.map((c) => [c.added, c]));
  const community = builds.find((b) => b.god === me && b.mode === "Conquest")?.builds
    .find((b) => b.source === "community") as CommunityBuildEntry | undefined;

  const six = r.result?.adapted.core ?? [];
  let running = 0;
  let unknownCost = false;
  const rows = six.map((name, i) => {
    const item = r.itemsByName[name];
    if (item?.cost == null) unknownCost = true;
    running += item?.cost ?? 0;
    const swap = swaps.get(name);
    return { name, position: i + 1, cumulative: unknownCost ? null : running, swapped: !!swap,
      reason: itemReason(name, { god: me, mode, community, item, swap }) };
  });
  const starterPath = r.starters[0];

  const unknownLine = known < roster
    ? `${roster - known} still unknown, so this six will keep moving`
    : "The whole team is in";

  const head = (
    <PageHead title="Draft" testId="draft-head">
      <p data-testid="draft-claim">
        {!me
          ? <><Em>Build for the match you&rsquo;re actually in.</Em> Put your god in the violet slot, then add the enemies as they lock in.</>
          : r.changeCount > 0
            ? <>This team moved <Em>{r.changeCount} of {r.coreSize}</Em> items in {me}&rsquo;s six.</>
            : known === 0
              ? <>{me}&rsquo;s six, as the god page ships it. <Em>Add an enemy</Em> and it starts adapting.</>
              : <><Em>No change to {me}&rsquo;s six.</Em> Nothing this team does earned enough to displace an item.</>}
      </p>
      {lines.length > 0 && (
        <ul className="mt-3 flex flex-col" data-testid="draft-changes">
          {lines.map((d) => (
            <li key={d.added} aria-label={displacementText(d)}
              className="grid grid-cols-[32px_minmax(0,1fr)] items-center gap-3 border-t border-line py-2 text-copy text-muted last:border-b">
              <Art name={d.added} kind="item" className="h-8 w-8 rounded-[6px] ring-2 ring-accent" />
              <span aria-hidden="true">
                <span className="font-semibold text-ink">{d.added}</span>{" "}
                {d.removed ? <>replaces <span className="text-ink-soft">{d.removed}</span></> : "comes in"}
                {d.why && <span className="text-accent"> · {d.why}</span>}
              </span>
            </li>
          ))}
        </ul>
      )}
    </PageHead>
  );

  const board = (
    <div className="mt-5 flex flex-col gap-5" data-testid="draft-board">
      <ModeSwitch mode={mode} onChange={setMode} className="w-full lg:w-[420px]" />

      {dropped.length > 0 && (
        <div role="status" className="flex items-start gap-2 border-y border-line py-2">
          <p className="min-w-0 flex-1 text-note text-muted">
            <span className="text-ink">{listWords(dropped)}</span> {dropped.length === 1 ? "has" : "have"} no scored build here,
            so {dropped.length === 1 ? "that slot" : "those slots"} came up empty. The rest of the link loaded.
          </p>
          <button type="button" onClick={dismissDropped} aria-label="Dismiss"
            className="press -my-1 flex h-11 w-11 flex-none items-center justify-center text-quiet hover:text-ink"><CloseGlyph size={18} /></button>
        </div>
      )}

      <TeamRow title="Your team" side="ally" slots={draft.allies} onOpen={(i) => setSheet({ side: "ally", index: i })}
        meta={<span className="num text-cap text-muted">{draft.allies.filter(Boolean).length} of {draft.allies.length}</span>} />
      <TeamRow title="Enemy" side="enemy" slots={draft.enemies} onOpen={(i) => setSheet({ side: "enemy", index: i })}
        meta={<span className="num text-cap text-muted" data-testid="enemies-known">{known} of {roster} enemies known</span>} />
      {me && known > 0 && <p className="-mt-3 text-cap text-quiet" data-testid="unknown-line">{unknownLine}.</p>}

      <div className="-mt-1 flex items-center gap-2">
        <button type="button" onClick={copyLink}
          className="press h-11 rounded-[10px] border border-line px-3.5 text-note font-semibold text-muted hover:text-ink">
          <span aria-live="polite">{copied ? "Link copied" : "Copy link"}</span>
        </button>
        {r.taken.size > 0 && (
          <button type="button" onClick={clear}
            className="press h-11 rounded-[10px] border border-line px-3.5 text-note font-semibold text-muted hover:text-ink">
            Clear the board
          </button>
        )}
      </div>

      {me && meAspect && (
        <div>
          <AspectToggle aspect={meAspect} on={aspectOn} changesBuild={aspectChanges} onChange={setAspectOn} />
          {aspectOn && <p className="mt-2 text-note text-muted">{aspectNote(meAspect, aspectChanges && r.aspectScored, me)}</p>}
        </div>
      )}
    </div>
  );

  const sixBlock = me ? (
    <section aria-labelledby="draft-six-h" className="mt-6" data-testid="draft-core">
      {mode !== "conquest" && (
        <p className="mb-2 text-note text-muted" data-testid="model-only">
          <Em>No win data in {MODE_NAME[mode]} — model only.</Em> This six is ranked on gold efficiency and kit fit, not on
          what {MODE_NAME[mode]} players buy.
        </p>
      )}
      {r.activeEntry?.borrowed_from && (
        <p className="mb-2 text-note text-muted">
          No {MODE_NAME[mode]} record exists, so this build uses {r.activeEntry.borrowed_from}&rsquo;s, minus items whose
          value arrives too late for {MODE_NAME[mode]}.
        </p>
      )}
      {starterPath && r.result && (
        <div className="flex min-h-11 items-center gap-3" data-testid="draft-starter">
          <span className="flex -space-x-2">
            {starterPath.base && <Art name={starterPath.base.name} kind="item" className="h-8 w-8 rounded-[7px] ring-2 ring-ground" />}
            {starterPath.upgrade && <Art name={starterPath.upgrade.name} kind="item" className="h-8 w-8 rounded-[7px] ring-2 ring-ground" />}
          </span>
          <p className="min-w-0 text-note leading-snug text-muted">
            <span className="font-cond text-[16px] font-bold uppercase text-ink">Start</span>{" "}
            {[starterPath.base?.name, starterPath.upgrade?.name].filter(Boolean).join(" → ")}
            <span className="block text-quiet">
              {r.startersAreConquest ? "In Conquest, " : ""}{Math.round(starterPath.lead.pick_rate * 100)}% of {me} players open this way · the draft doesn&rsquo;t move it
            </span>
          </p>
        </div>
      )}
      <div className="mt-2.5 flex items-baseline justify-between px-1 text-cap text-quiet">
        <h2 id="draft-six-h" className="font-cond text-[16px] font-bold uppercase text-muted">
          {r.changeCount > 0 ? `${me}'s adapted six` : `${me}'s six`} · buy order
        </h2>
        <span aria-hidden="true">Gold spent</span>
      </div>
      {!r.draftEnabled || !r.result ? (
        <p className="mt-2 rounded-[12px] border border-dashed border-line p-4 text-copy text-muted">
          {me} has no scored build for {MODE_NAME[mode]} in this index yet, so there&rsquo;s nothing to adapt. The board
          starts from the build the god page ships and never assembles one of its own.
        </p>
      ) : (
        <>
          <ol className="mt-1.5 space-y-1.5" data-testid="six">
            {rows.map((row) => (
              <ItemRow key={row.name} position={row.position} name={row.name} cumulativeGold={row.cumulative}
                reason={row.reason} swapped={row.swapped} />
            ))}
          </ol>
          <p className="mt-2 px-1 text-cap text-quiet">
            Buy order is the model&rsquo;s and the draft doesn&rsquo;t move it — an item that swaps in takes the slot of the one it replaced.
          </p>
        </>
      )}
      {r.relicPicks.length > 0 && (
        <div className="mt-5" data-testid="draft-relics">
          <h3 className="font-cond text-[18px] font-extrabold text-ink">Relic</h3>
          <p className="text-note text-muted">Takes one of your six. The model can&rsquo;t price it, so it won&rsquo;t pick it for you.</p>
          <ul className="mt-1.5">
            {r.relicPicks.map((p) => (
              <li key={p.item} className="border-t border-line">
                <a href={toHash.item(p.item)} className="press flex min-h-12 items-center gap-3 py-1.5">
                  <Art name={p.item} kind="item" className="h-8 w-8 rounded-[6px]" />
                  <span className="min-w-0 flex-1">
                    <span className="block font-cond text-[19px] font-bold leading-none text-ink">{p.item}</span>
                    <span className="mt-0.5 block text-note text-muted">{p.because}</span>
                  </span>
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </section>
  ) : null;

  /* The threat table: every threat, denominated by the roster. */
  const threats = me ? (
    <section aria-labelledby="threats-h" data-testid="draft-threats" className={wide ? "" : "mt-8"}>
      <div className="flex items-baseline justify-between gap-3">
        <h2 id="threats-h" className="font-cond text-[24px] font-extrabold text-ink">Against this team</h2>
        <span className="num text-cap text-muted">{known} of {roster} known</span>
      </div>
      {known === 0 ? (
        <p className="mt-1.5 text-copy text-muted">
          Nothing scouted yet. Add an enemy and this fills in with what they threaten and which of your items answer it.
        </p>
      ) : (
        <ul className="mt-2">
          {THREATS.map((t) => {
            const who = r.threatCulprits[t.key] ?? [];
            const answer = who.length > 0 ? threatAnswer(t.key, six, r.itemsByName, draftConfig) : null;
            return (
              <li key={t.key} data-testid={`threat-${t.key}`}
                className="grid grid-cols-[52px_minmax(0,1fr)] gap-x-3 border-t border-line py-2">
                <span className={`num font-cond text-[19px] font-bold leading-tight ${who.length ? "text-ink" : "text-quiet"}`}>
                  {who.length}<span className="font-sans text-cap normal-case text-quiet"> of {roster}</span>
                </span>
                <span className="min-w-0 text-note">
                  <span className={who.length ? "font-semibold text-ink" : "text-quiet"}>{t.noun[0].toUpperCase() + t.noun.slice(1)}</span>
                  {who.length > 0 && <span className="text-muted"> — {listWords(who)}</span>}
                  {answer && (
                    <span className="block text-muted">
                      {answer.kind === "answered"
                        ? <>Answered by <span className="text-ink-soft">{listWords(answer.by.slice(0, 2))}</span>{answer.by.length > 2 ? ` and ${answer.by.length - 2} more` : ""}</>
                        : answer.kind === "weighed"
                          ? <>Weighed — nothing with {t.answer} outscored the six</>
                          : <>No item answers this{draftConfig?.relics?.[t.key] ? ` — ${draftConfig.relics[t.key].item} does, as a relic` : ""}</>}
                    </span>
                  )}
                </span>
              </li>
            );
          })}
        </ul>
      )}
      {r.allyAllPhysical && r.allyCount > 0 && (
        <p className="mt-2 text-cap text-quiet">Your side: {r.allyPhysical} of {roster} physical, so penetration is raised.</p>
      )}
    </section>
  ) : null;

  const seams = (
    <nav aria-label="From this draft" className="mt-6 flex flex-wrap gap-x-5">
      {me && (
        <Seam href={queryHash({ you: me, enemies: draft.enemies.filter(Boolean), mode, aspect: aspectOn })}>
          {me}&rsquo;s page, against this team
        </Seam>
      )}
      <Seam href={toHash.method()} testId="method-seam">Where these scores come from</Seam>
    </nav>
  );

  return (
    <div className={`mx-auto w-full max-w-[1240px] px-4 pb-12 lg:px-6 ${wide ? "grid grid-cols-[minmax(0,1fr)_380px] gap-12" : ""}`}>
      <div className="min-w-0 lg:max-w-[680px]">
        {head}
        {board}
        {sixBlock}
        {!wide && threats}
        {!wide && seams}
      </div>
      {wide && (
        <aside aria-label="Threats" className="min-w-0 pt-10">
          <div className="sticky top-[88px]">
            {threats ?? (
              <p className="text-copy text-muted">Pick your god and the enemies you know; what they threaten lands here.</p>
            )}
            {seams}
          </div>
        </aside>
      )}

      {sheet && (
        <EnemySheet gods={eligible} side={sheet.side} startIndex={sheet.index} self={me || undefined}
          enemies={sheet.side === "ally" ? draft.allies : draft.enemies}
          onPick={(i, n) => (sheet.side === "ally" ? setAlly(i, n) : setEnemy(i, n))}
          onRemove={(i) => (sheet.side === "ally" ? setAlly(i, "") : setEnemy(i, ""))}
          onClose={() => setSheet(null)} />
      )}
      <p className="sr-only" aria-live="polite">{me ? `${r.changeCount} of ${r.coreSize} items changed by this draft. ${known} of ${MODE_TEAM_SIZE[mode]} enemies known.` : ""}</p>
    </div>
  );
}
