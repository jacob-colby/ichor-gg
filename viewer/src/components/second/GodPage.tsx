/** The god page: one answer per screen.
 *
 * Phone (390 first): header -> the verdict sentence -> starter -> the six in
 * buy order with gold spent -> disclosures. The enemy strip rides above the
 * tab bar the whole way down, so a player mid-draft glances, taps a slot,
 * types three letters, and glances back at a six that re-ranked in place.
 *
 * Desktop: a real second column — the enemy team as a panel and the
 * reasoning beside the build, instead of a stretched phone column.
 *
 * Same build everywhere: the six on this page is the `model` archetype,
 * because that is the build `/side_by_side` measures; the enemy strip adapts
 * THAT six (archetype passed into useDraftResult explicitly), and the Draft
 * tab opens the board on it too.
 *
 * ONE SIX, ADJUSTED (2026-11-08). Every other build is an adjustment of that
 * six, chosen in one strip beside the aspect switch (`FocusStrip`): the six
 * changes in place, the slots that moved are marked, and a line names the
 * swaps. The starter and the relic are tiles at the head of the buy order,
 * and a most-picked list (the second column; a disclosure on a phone) ticks
 * which of the god's most-bought items the six on screen holds, on every
 * mode. Why `model` stays the main six and where Balanced and Hybrid sit:
 * `lib/focus.ts`.
 *
 * WHOSE BUILD (2026-11-09, Jacob). Above the focus strip, "Ichor's |
 * Community" chooses whose six the page shows before anything adjusts it
 * (`WhoseSwitch`). Ichor's side is the page above. The community has one six
 * and nothing to adjust, so its side drops the focus chips and keeps only the
 * aspect switch. In Joust and Arena it shows Conquest's six with the
 * most-picked list's asterisks. What the six is: `communityBuild.ts`. With
 * the aspect on, one slot owns the Community side's whole build area for the
 * per-aspect community build (see "THE ASPECT SLOT" below).
 */
import { useEffect, useMemo, useState, type ReactNode } from "react";
import type { BuildNote, CommunityBuildEntry, CuratedBuildEntry, God, IndexData, PopularItem } from "../../types";
import { useDraft, MODE_TEAM_SIZE } from "../../lib/draft";
import { archetypeEntries, useDraftResult } from "../../lib/useDraftResult";
import { useUrlState } from "../../lib/urlState";
import { toHash } from "../../lib/useHashRoute";
import { diffSix, focusOptions, hybridEvidence, swapLead, MAIN_LABEL, type SlotSwap } from "../../lib/focus";
import { mostPicked, transferFlags } from "../../lib/mostPicked";
import { starterShare } from "../../lib/starters";
import { godLane, laneTextClass } from "../../lib/roleAccent";
import { useComparison } from "./useComparison";
import { verdictSentence, MODE_NAME } from "./verdict";
import { itemReason } from "./itemReason";
import { Art, ChevronGlyph } from "./art";
import { ModeSwitch } from "./ModeSwitch";
import { WhoseSwitch } from "./WhoseSwitch";
import { AspectToggle } from "./AspectToggle";
import { FocusStrip } from "./FocusStrip";
import { KitTile, type KitAlternative } from "./KitTile";
import { MostPicked, TransferNotes } from "./MostPicked";
import { communityLines, communitySix, noAspectBuildLine } from "./communityBuild";
import { MAIN_ARCHETYPE, decodePageQuery, encodePageQuery, writeLastGod, aspectNote } from "./pageState";
import { VerdictLine } from "./VerdictLine";
import { ItemRow } from "./ItemRow";
import { EnemyStrip } from "./EnemyStrip";
import { EnemySheet } from "./EnemySheet";
import { CompareDetail } from "./CompareDetail";
import { WhyPanel } from "./WhyPanel";
import { useWide } from "./useWide";
import { Disclosure } from "./Disclosure";

const sameOrder = (a: string[] = [], b: string[] = []) => a.length === b.length && a.every((x, i) => x === b[i]);

function noteFor(builds: BuildNote[], god: string, label: string) {
  return builds.find((b) => b.god === god && b.mode === label);
}

/** How many of the god's most-bought items the list shows. */
const MOST_PICKED = 10;

const pctOf = (r: number) => `${Math.round(r * 100)}%`;
const shortAspect = (a: string) => a.replace(/^Aspect of /, "").replace(/^the /i, "");

export function GodPage({ god, data }: { god: God; data: IndexData }) {
  const [q, setQ] = useUrlState(decodePageQuery, encodePageQuery);
  const { mode } = q;
  const modeLabel = MODE_NAME[mode];
  const wide = useWide();

  useEffect(() => { writeLastGod(god.name); }, [god.name]);

  // ── The enemy team: the shared draft, with you in ally slot 1. ──────────
  const { draft, mode: draftMode, setMode: setDraftMode, setEnemy, setAlly } = useDraft();
  useEffect(() => { if (draftMode !== mode) setDraftMode(mode); }, [draftMode, mode, setDraftMode]);
  const enemies = useMemo(() => {
    const n = MODE_TEAM_SIZE[mode];
    return Array.from({ length: n }, (_, i) => draft.enemies[i] ?? "");
  }, [draft.enemies, mode]);
  const comp = useMemo(() => ({ allies: [god.name, ...draft.allies.slice(1)], enemies }), [god.name, draft.allies, enemies]);

  // A link that names the enemies (`vs=`, which the command field writes) is
  // applied to the shared draft with you in ally slot 1, so the strip, the
  // six and the Draft page all agree with the address bar. A bare
  // `#/god/Ra` names none and leaves the stored draft alone.
  const vsKey = q.vs?.join(",") ?? null;
  useEffect(() => {
    if (!q.vs) return;
    const known = q.vs.filter((n) => data.gods.some((g) => g.name === n));
    if (draft.allies[0] !== god.name) setAlly(0, god.name);
    const n = MODE_TEAM_SIZE[mode];
    if (draft.enemies.slice(0, n).filter(Boolean).join(",") === known.slice(0, n).join(",")) return;
    for (let i = 0; i < n; i += 1) setEnemy(i, known[i] ?? "");
    // Only a new link re-applies; the picker's own edits write `vs` themselves.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [vsKey, god.name]);

  const r = useDraftResult(comp, mode, data.gods, data.items, data.builds, data.god_item_scores,
    data.draft, data.god_item_damage, q.aspect, q.build);

  // ── Builds, community, aspect ──────────────────────────────────────────
  const note = noteFor(data.builds, god.name, modeLabel);
  const community = noteFor(data.builds, god.name, "Conquest")?.builds
    .find((b) => b.source === "community") as CommunityBuildEntry | undefined;
  // The strip's options: the main six first, every other build measured
  // against it. `r.archetypes` is the deduped list for THIS kit (aspect or
  // base), so a focus the dedupe folded away comes back as its own chip here.
  const options = useMemo(() => focusOptions(r.archetypes, MAIN_ARCHETYPE), [r.archetypes]);
  const mainOpt = options[0];
  const selected = options.find((o) => o.archetype === q.build) ?? mainOpt;
  // The entry `useDraftResult` is adapting — the survivor when `build=` names
  // a collapsed alias, so this can read `core` while the chip reads Burst.
  const archetype = r.activeEntry?.archetype ?? q.build;
  const isMain = !selected || selected.kind === "main";
  const aspectName = god.aspects?.[0]?.name ?? null;
  const suggested = (note?.builds ?? []).filter((b) => b.source === "suggested") as CuratedBuildEntry[];
  // The raw note, by the CHIP's name: every archetype is stored there, aliases
  // included, so "does the aspect move this build" is asked of the right one.
  const chipArch = selected?.archetype ?? archetype;
  const baseOfArch = suggested.find((b) => b.archetype === chipArch && !b.aspect);
  const aspectOfArch = suggested.find((b) => b.archetype === chipArch && !!b.aspect);
  const aspectChangesBuild = !!aspectOfArch && !sameOrder(aspectOfArch.slot_order, baseOfArch?.slot_order);
  const aspectOnBuild = q.aspect && r.aspectScored && aspectChangesBuild;
  // The same question of the main six, which is what the Community side's
  // verdict speaks for whatever focus Ichor's side was left on.
  const baseOfMain = suggested.find((b) => b.archetype === MAIN_ARCHETYPE && !b.aspect);
  const aspectOfMain = suggested.find((b) => b.archetype === MAIN_ARCHETYPE && !!b.aspect);
  const aspectOnMain = q.aspect && r.aspectScored && !!aspectOfMain && !sameOrder(aspectOfMain.slot_order, baseOfMain?.slot_order);
  // The base kit's main six: what the aspect is measured against.
  const baseMainSix = useMemo(
    () => focusOptions(archetypeEntries(data.builds, god.name, mode, false), MAIN_ARCHETYPE)[0]?.six ?? [],
    [data.builds, god.name, mode]);

  // ── Comparison + verdict ───────────────────────────────────────────────
  const cmp = useComparison(god.name);
  const shipped = (r.activeEntry?.slot_order as string[] | undefined) ?? [];

  // ── Whose build ────────────────────────────────────────────────────────
  // Offered whenever the god has a Conquest community record (95 of 95 gods
  // on 2026-11-09), in every mode: Joust and Arena borrow Conquest's.
  const hasCommunity = !!community;
  const onCommunity = hasCommunity && q.whose === "community";
  // Community with the aspect on: the base six is every player on any aspect,
  // so it is not shown as the aspect's. The whole build area goes to the
  // aspect slot below instead (communityBuild.ts, THE ASPECT).
  const aspectSlot = onCommunity && q.aspect && !!aspectName;
  const theirSix = communitySix({ comparison: cmp.data, mode });

  const verdict = cmp.loading && mode === "conquest" ? null : verdictSentence({
    d: cmp.data, god: god.name, mode,
    // The Community side reads the sentence Ichor's main six reads: the
    // measurement holds both sixes, and the community has no focuses.
    archetype: onCommunity ? MAIN_ARCHETYPE : archetype,
    shownSix: onCommunity ? mainOpt?.six ?? [] : shipped,
    aspectBuild: (onCommunity ? aspectOnMain : aspectOnBuild) ? aspectName : null,
    band: cmp.meta?.band, draftSwaps: onCommunity ? 0 : r.changeCount,
    side: onCommunity ? "community" : "ichor",
  });

  // ── What the reader's choices changed ──────────────────────────────────
  // A focus is marked against the main six of the same kit; with no focus,
  // the aspect is marked against the base kit's main six. One level at a
  // time, so a mark always means "your last choice put this here".
  const aspectSwaps: SlotSwap[] = q.aspect && r.aspectScored && isMain ? diffSix(baseMainSix, mainOpt?.six ?? []) : [];
  const marks: SlotSwap[] = onCommunity ? [] : !isMain ? selected.swaps : aspectSwaps;
  const markedFor = new Map(marks.filter((m) => m.added).map((m) => [m.added!, m]));

  // ── The six on screen ──────────────────────────────────────────────────
  // The community's six is never adapted to the enemy team: it is a record
  // of what players bought, not an answer the model re-ranks.
  const swaps = new Map((r.result?.diff.changes ?? []).map((c) => [c.added, c]));
  // Empty in the aspect slot: the slot owns its own six.
  const six = aspectSlot ? [] : onCommunity ? theirSix?.items ?? [] : (r.result?.adapted.core ?? shipped);
  // Joust and Arena borrow Conquest's six; an item whose Conquest record
  // doesn't describe it there is marked, by the most-picked list's rule.
  const sixFlags = onCommunity
    ? transferFlags(six, modeLabel, data.community_transfer?.[modeLabel], r.itemsByName) : [];
  let running = 0;
  let unknownCost = false;
  const rows = six.map((name, i) => {
    const item = r.itemsByName[name];
    if (item?.cost == null) unknownCost = true;
    running += item?.cost ?? 0;
    const swap = onCommunity ? undefined : swaps.get(name);
    const mark = swap ? undefined : markedFor.get(name);
    const base = itemReason(name, { god: god.name, mode, community, item, swap });
    const reason = mark
      ? { tone: "adjust" as const, text: [mark.removed ? `In for ${mark.removed}` : "Added", base.text].filter(Boolean).join(" · ") }
      : base;
    const flags = sixFlags.filter((f) => f.items.includes(name)).map((f) => f.note);
    return { name, position: i + 1, cumulative: unknownCost ? null : running, reason, swapped: !!swap, adjusted: !!mark, flags };
  });

  // Ichor's side opens with its build's own starter stamp; the community's
  // with the community record's. Today the pipeline stamps every build with
  // the community's most-taken path (basis "community", 95 of 95 gods), so
  // the two agree; a build stamped by the role rule would differ here. The
  // relic is the community's most-taken on both sides: no build carries one.
  const starter = onCommunity ? community?.starter : (r.activeEntry?.starter ?? community?.starter);
  // The whole path's share (base + upgrade), the same number the draft board
  // prints for the same opener — see lib/starters.starterShare.
  const starterPct = starterShare(starter, r.starters);
  const inConquest = r.startersAreConquest || mode !== "conquest" ? "In Conquest, " : "";
  // Each other opener by its base, with the path's share: every player on the
  // path opened with the base, so "Conduit Gem 39%" is true where the upgrade's
  // name would claim its holders were all of them. The full "base → upgrade"
  // label stays on the starter tile itself, where the pairing is the point;
  // here it doubled the line and wrapped it on a phone.
  const starterAlts: KitAlternative[] = r.starters
    .filter((p) => p.rootName !== starter?.base)
    .slice(0, 2)
    .map((p) => ({ name: p.rootName, icon: p.rootName, share: p.pick_rate }));

  // The relic: the community's own record, when the index carries one. Same
  // fallback as the starters — Joust and Arena read Conquest's, and say so.
  // Absent from the index, the tile is absent: nothing stands in for it.
  const relicsOf = (label: string) => (noteFor(data.builds, god.name, label)?.builds
    .find((b) => b.source === "community") as CommunityBuildEntry | undefined)?.community_relics;
  const ownRelics = relicsOf(modeLabel);
  const relicRecord: PopularItem[] = [...((ownRelics?.length ? ownRelics : relicsOf("Conquest")) ?? [])]
    .sort((a, b) => b.pick_rate - a.pick_rate || a.name.localeCompare(b.name));
  const relicsAreConquest = mode !== "conquest" && !ownRelics?.length;
  const topRelic = relicRecord[0];

  // ── Header facts ───────────────────────────────────────────────────────
  // Conquest's slice, or the top level on an index that predates per-mode
  // slices (it mirrored Conquest). Never another mode's: only Conquest has
  // outcome data.
  const tier = (data.tierlist?.conquest ?? data.tierlist)?.gods.find((g) => g.name === god.name);
  const lane = godLane(god.role);
  const record = mode !== "conquest"
    ? `No win data in ${modeLabel} — model only`
    : tier?.tier_score
      ? `Tier ${tier.tier_score} on ${(tier.matches ?? 0).toLocaleString("en-US")} Conquest games`
      : "Not enough Conquest games to rank";

  const kitLine = cmp.data?.kit
    ? cmp.data.kit.kit === "base"
      ? `Measured on the base kit${cmp.data.kit.aspect && cmp.data.kit.pick_rate != null
        ? `; ${Math.round(cmp.data.kit.pick_rate * 100)}% of ${god.name} players run ${cmp.data.kit.aspect}` : ""}.`
      : `Measured on ${cmp.data.kit.aspect}.`
    : undefined;

  // ── Enemy picker ───────────────────────────────────────────────────────
  const [sheetAt, setSheetAt] = useState<number | null>(null);
  // Picker edits write back to the address bar, so the link reproduces the
  // team on screen; emptying the team leaves a bare URL again.
  const writeVs = (next: string[]) => setQ((p) => ({ ...p, vs: next.filter(Boolean) }));
  const pickEnemy = (i: number, name: string) => {
    if (draft.allies[0] !== god.name) setAlly(0, god.name);
    setEnemy(i, name);
    writeVs(enemies.map((n, j) => (j === i ? name : n)));
  };
  const removeEnemy = (i: number) => {
    setEnemy(i, "");
    writeVs(enemies.map((n, j) => (j === i ? "" : n)));
  };
  const clearEnemies = () => { enemies.forEach((_, i) => setEnemy(i, "")); writeVs([]); };

  const buildLabel = isMain ? "Ichor's main six" : selected.label;
  const listLabel = onCommunity ? (mode === "conquest" ? "The community's six" : "Conquest's community six")
    : isMain ? MAIN_LABEL : `${selected.label} build`;

  // ── The line under the strip: what the choice changed, in words ────────
  const of = mainOpt?.six.length ?? 6;
  const hybridSwaps = selected?.kind === "answer" && selected.archetype === "hybrid" ? selected.entry.swaps ?? [] : [];
  const evidenceFor = (s: SlotSwap) => hybridEvidence(
    hybridSwaps.find((h) => h.added === s.added && h.removed === s.removed), god.name, selected?.entry.borrowed_from);
  const adjustNote = isMain || !selected ? null
    : selected.archetype === "core"
      ? `Balanced weighs ${god.name} players' win and pick rates beside gold value and kit fit; ${MAIN_LABEL} leaves them out.`
      : selected.archetype === "hybrid"
        ? `Hybrid keeps the model's strongest picks and lets a strong ${selected.entry.borrowed_from ? `${selected.entry.borrowed_from} ` : ""}player record take a weaker slot.`
        : mode === "conquest"
          ? `In Conquest every focus is a lean on Balanced, which weighs players' win and pick rates; ${MAIN_LABEL} leaves them out.`
          : null;
  const swapList = (list: SlotSwap[], evidence?: (s: SlotSwap) => string | null) => (
    <ul className="mt-1 space-y-0.5" data-testid="swap-list">
      {list.map((s, i) => {
        const why = evidence?.(s);
        return (
          <li key={`${s.removed}-${s.added}-${i}`} className="text-note text-muted">
            {s.removed && <span>{s.removed}</span>}
            {s.removed && s.added && <span aria-hidden="true"> → </span>}
            {s.removed && s.added && <span className="sr-only"> replaced by </span>}
            {!s.removed && <span>Adds </span>}
            {s.added ? <span className="font-semibold text-ink">{s.added}</span> : <span> leaves</span>}
            {why && <span className="text-quiet"> · {why}</span>}
          </li>
        );
      })}
    </ul>
  );
  // On a phone the swap detail is one line, and the list behind it is one tap
  // away: the six's own rows already carry every swap ("In for Soul Gem"), and
  // the open list pushed all six of them under the enemy bar (2026-11-09,
  // Ullr Cooldown at 375×812: 125px of swap detail, the first row at y=747
  // against the bar at 683). The desktop column has the room, so it stays open
  // there. With nothing behind it, the line is plain text, not a control.
  // `head` is the lead without its closing colon; the colon only introduces
  // a list that is open under it.
  const swapDetail = (head: ReactNode, body: ReactNode, headClass: string) => !body ? (
    <p className={headClass}>{head}</p>
  ) : wide ? (
    <>
      <p className={headClass}>{head}:</p>
      {body}
    </>
  ) : (
    <details className="disclosure">
      <summary className={`press -mx-1 flex min-h-11 cursor-pointer items-center gap-1 rounded-[10px] px-1 ${headClass}`}>
        <span className="min-w-0 flex-1">{head}</span>
        <ChevronGlyph size={18} className="chev flex-none text-muted" />
      </summary>
      <div className="pb-1">{body}</div>
    </details>
  );
  const noColon = (s: string) => s.replace(/:$/, "");

  // ── Most picked ─────────────────────────────────────────────────────────
  const picked = useMemo(() => mostPicked(community), [community]);
  const topPicked = picked.slice(0, MOST_PICKED);
  const pickFlags = transferFlags(topPicked.map((p) => p.name), modeLabel,
    data.community_transfer?.[modeLabel], r.itemsByName);
  const inBuild = new Set(six);
  const pickedHave = topPicked.filter((p) => inBuild.has(p.name)).length;
  const mostPickedPanel = (bare: boolean) => (
    <MostPicked god={god.name} mode={mode} items={topPicked} total={picked.length} inBuild={inBuild}
      flags={pickFlags} bare={bare} />
  );

  const why = (
    <WhyPanel god={god.name} mode={mode} isModel={isMain} buildLabel={buildLabel}
      changes={r.result?.diff.changes ?? []} culprits={r.threatCulprits} enemiesKnown={r.enemiesKnown}
      comparison={cmp.data} meta={cmp.meta} kitLine={kitLine} />
  );
  // The count is of swaps in the six ON SCREEN, so the community's side,
  // which the team never moves, reads none.
  const strip = (variant: "bar" | "panel") => (
    <EnemyStrip enemies={enemies} onOpen={setSheetAt} changeCount={onCommunity ? 0 : r.changeCount} variant={variant}
      onClear={clearEnemies} />
  );

  const choose = (a: string) => setQ((p) => ({ ...p, build: a }));
  const aspectSwitch = (changesBuild: boolean) => aspectName ? (
    <AspectToggle aspect={aspectName} on={q.aspect} changesBuild={changesBuild}
      onChange={(on) => setQ((p) => ({ ...p, aspect: on }))} />
  ) : undefined;
  const aspectLine = q.aspect && aspectName ? (
    isMain && aspectSwaps.length > 0 ? `Built for ${shortAspect(aspectName)}.` : aspectNote(aspectName, aspectChangesBuild, god.name)
  ) : null;

  return (
    <div className="mx-auto w-full max-w-[1240px] px-4 lg:grid lg:grid-cols-[minmax(0,1fr)_380px] lg:gap-12 lg:px-6 lg:pt-8">
      <div className="min-w-0 lg:max-w-[680px]">
        {/* ── Header ── */}
        <header className="pt-4 lg:pt-0" data-testid="god-header">
          <div className="flex items-center gap-3 lg:gap-5">
            <Art name={god.name} kind="head" eager className="h-16 w-16 rounded-[14px] lg:h-24 lg:w-24 lg:rounded-[18px]" />
            <div className="min-w-0">
              <h1 className="font-cond text-god font-extrabold text-ink lg:text-[68px]">{god.name}</h1>
              <p className="mt-1.5 text-note text-muted lg:text-copy">
                <span className={laneTextClass(lane)}>{god.role}</span>
                <span className="text-quiet"> · </span>{god.damage_type === "magical" ? "Magical" : "Physical"}
                {/* The record is its own line: as a third clause it broke
                    mid-phrase beside the aspect switch. */}
                <span data-testid="god-record" className={`block ${mode === "conquest" && tier?.tier_score ? "text-ink" : ""}`}>{record}</span>
              </p>
            </div>
          </div>
          <ModeSwitch mode={mode} onChange={(m) => setQ((p) => ({ ...p, mode: m }))} className="mt-3 lg:mt-5 lg:max-w-[420px]" />
        </header>

        {/* ── The answer ── */}
        <section aria-labelledby="six-h" className="mt-3 lg:mt-6">
          <VerdictLine verdict={verdict} loading={mode === "conquest" && cmp.loading} />

          {/* ── Whose build, before anything adjusts it ── */}
          {hasCommunity && (
            <WhoseSwitch whose={onCommunity ? "community" : "ichor"} className="mt-3 lg:mt-4 lg:max-w-[420px]"
              onChange={(w) => setQ((p) => ({ ...p, whose: w }))} />
          )}

          {/* ── Adjust it: the aspect, then a focus. The community has one six
              and no focuses, so its side keeps the aspect switch alone. ── */}
          {onCommunity ? (
            <div className="mt-2 lg:mt-3">
              {/* On the community's side the aspect always changes what is
                  shown: the any-aspect six gives way to the aspect slot. */}
              {aspectSwitch(true)}
              {theirSix && !aspectSlot && (
                <div className={`space-y-1 ${aspectName ? "mt-2" : ""}`} data-testid="community-line" aria-live="polite">
                  {communityLines(theirSix, god.name).map((l) => <p key={l} className="text-note text-muted">{l}</p>)}
                </div>
              )}
            </div>
          ) : (
            <div className="mt-2 lg:mt-3">
              <FocusStrip options={options} selected={selected?.archetype ?? MAIN_ARCHETYPE} onSelect={choose}
                aspect={aspectSwitch(aspectChangesBuild)} />
              {(aspectLine || !isMain) && (
                <div className="mt-1 space-y-2 lg:mt-2" data-testid="adjust-line" aria-live="polite">
                  {aspectLine && (
                    <div data-testid="aspect-note">
                      {isMain && aspectSwaps.length > 0
                        ? swapDetail(<>{aspectLine} {noColon(swapLead({ swaps: aspectSwaps, sameAs: null, reordered: false, six: [] }, god.name, of))}</>,
                          swapList(aspectSwaps), "text-note text-muted")
                        : <p className="text-note text-muted">{aspectLine}</p>}
                    </div>
                  )}
                  {!isMain && selected && (
                    <div data-testid="swap-line" data-swaps={selected.swaps.length}>
                      {swapDetail(
                        <><span className="font-cond text-[17px] font-bold uppercase text-ink">{selected.label}</span>{" "}
                          {noColon(swapLead(selected, god.name, of))}</>,
                        selected.swaps.length > 0 && <>
                          {swapList(selected.swaps, hybridSwaps.length ? evidenceFor : undefined)}
                          {/* The note explains where swaps came from; over "Same as Ichor's six" it explains nothing. */}
                          {adjustNote && <p className="mt-1 text-cap text-quiet">{adjustNote}</p>}
                        </>,
                        "text-copy text-ink-soft")}
                    </div>
                  )}
                </div>
              )}
            </div>
          )}

          <div className="mt-2 flex items-baseline justify-between px-1 text-cap text-quiet lg:mt-3">
            <h2 id="six-h" className="font-cond text-[16px] font-bold uppercase text-muted">
              {aspectSlot ? `The community's ${shortAspect(aspectName!)} build` : `${listLabel} · buy order`}
            </h2>
            {!aspectSlot && <span aria-hidden="true">Gold spent</span>}
          </div>

          {aspectSlot ? (
            /* THE ASPECT SLOT — a contract with the per-aspect community
               session. On Community with the aspect on, this one block owns
               the whole build area: starter, relic and six. Nothing else
               renders beside it (no KitTile, no ItemRow list, no asterisk
               notes). That session replaces its contents with
               <AspectCommunity aspect={aspectName} mode={mode}
                 communityAspects={<the Conquest note's community_aspects>}
                 itemsByName={r.itemsByName} />.
               Until then it says there is no per-aspect community build. */
            <div className="mt-1.5" data-testid="community-aspect-slot">
              <p className="rounded-[12px] border border-dashed border-line p-4 text-copy text-muted">
                {noAspectBuildLine(shortAspect(aspectName!), god.name)}
              </p>
            </div>
          ) : (
            <>
              {/* The starter and the relic open the buy order, as tiles. Side by
                  side wherever half the column still holds a starter's name in
                  two lines. Stacked at 1024–1279, where the aside narrows the
                  column to ~550px: there a half-width starter tile measured
                  121px against a row's 64. */}
              {(starter || topRelic) && (
                <div className={`mt-1.5 grid gap-1.5 ${starter && topRelic ? "sm:grid-cols-2 lg:grid-cols-1 xl:grid-cols-2" : ""}`} data-testid="kit-tiles">
                  {starter && (
                    <KitTile kind="Start" testId="starter" icon={starter.base} inset={starter.upgrade}
                      name={`${starter.base} → ${starter.upgrade}`}
                      reason={starterPct != null ? `${inConquest}${pctOf(starterPct)} of ${god.name} players open this way` : undefined}
                      alternatives={starterAlts}
                      altLabel={`Others${inConquest ? " in Conquest" : ""}`} />
                  )}
                  {topRelic && (
                    <KitTile kind="Relic" testId="relic" icon={topRelic.name} name={topRelic.name}
                      reason={`${relicsAreConquest ? "In Conquest, " : ""}${pctOf(topRelic.pick_rate)} of ${god.name} players take it`}
                      alternatives={relicRecord.slice(1, 3).map((x) => ({ name: x.name, icon: x.name, share: x.pick_rate }))}
                      altLabel={`Others${relicsAreConquest ? " in Conquest" : ""}`} />
                  )}
                </div>
              )}

              {rows.length > 0 ? (
                <ol className="mt-1.5 space-y-1.5" data-testid="six">
                  {rows.map((row) => (
                    <ItemRow key={`${onCommunity ? "c" : "i"}-${row.name}`} position={row.position} name={row.name}
                      cumulativeGold={row.cumulative} reason={row.reason} swapped={row.swapped} adjusted={row.adjusted}
                      flags={row.flags} />
                  ))}
                </ol>
              ) : onCommunity ? (
                // No stand-in: the raw record isn't six finished items (communityBuild.ts).
                <p className="mt-3 rounded-[12px] border border-dashed border-line p-4 text-copy text-muted"
                  data-testid="community-empty" aria-busy={cmp.loading || undefined}>
                  {cmp.loading ? "Loading the community's six…" : `There's no measured community six for ${god.name} yet.`}
                </p>
              ) : (
                <p className="mt-3 rounded-[12px] border border-dashed border-line p-4 text-copy text-muted">
                  No {modeLabel} build has been made for {god.name} yet.
                </p>
              )}
              <TransferNotes flags={sixFlags} testId="six-notes" className="mt-2 px-1" />
            </>
          )}
        </section>

        {/* ── One tap away ── */}
        <div className="mt-6 divide-y divide-line border-y border-line">
          {!wide && (
            <Disclosure title="Most picked" testId="picked-disclosure"
              hint={!topPicked.length ? `No Conquest record for ${god.name} yet`
                // The aspect slot draws its own six, which this page can't tick.
                : aspectSlot ? `${god.name}'s top ${topPicked.length} Conquest picks, any aspect`
                  : `${pickedHave} of ${god.name}'s top ${topPicked.length} ${mode === "conquest" ? "are" : "Conquest picks are"} in this build`}>
              {mostPickedPanel(true)}
            </Disclosure>
          )}
          {/* The reasoning is Ichor's; on the community's side it says whose. */}
          {!wide && <Disclosure title={onCommunity ? "Why Ichor's build" : "Why this build"} testId="why-disclosure">{why}</Disclosure>}
          {mode === "conquest" && cmp.data && (
            <Disclosure title="The comparison in detail" hint="Fight by fight, and what isn't measured" testId="compare-disclosure">
              <CompareDetail d={cmp.data} meta={cmp.meta} god={god.name} community={community} />
            </Disclosure>
          )}
          <nav aria-label={`More on ${god.name}`} className="flex flex-wrap gap-x-5 py-3">
            {[
              { href: toHash.godKit(god.name), label: "Kit" },
              { href: toHash.godItems(god.name), label: "Every item ranked" },
              { href: toHash.godRanking(god.name), label: "Ranking" },
            ].map((l) => (
              <a key={l.href} href={l.href}
                className="press inline-flex h-11 items-center gap-1 font-cond text-[18px] font-bold uppercase text-muted hover:text-ink">
                {l.label}<ChevronGlyph size={16} />
              </a>
            ))}
          </nav>
        </div>
        {community && (
          <p className="mt-3 text-cap text-quiet">
            Player percentages: Conquest games on SmiteBrain, refreshed {community.last_verified ?? "recently"}.
          </p>
        )}

        {/* Phone: the enemy strip rides above the tab bar. */}
        {!wide && (
          <div className="sticky bottom-[calc(72px+env(safe-area-inset-bottom))] z-30 mt-5">{strip("bar")}</div>
        )}
        <div className="h-6 lg:h-16" />
      </div>

      {wide && (
        // Not sticky: with the most-picked list in it the column is taller
        // than a laptop screen, and a sticky column that tall hides its own
        // bottom until the page ends.
        <aside aria-label="Enemy team, most picked and reasoning" className="min-w-0 space-y-6">
          {strip("panel")}
          <div className="rounded-[14px] border border-line p-4">{mostPickedPanel(false)}</div>
          <div className="rounded-[14px] border border-line p-4">{why}</div>
        </aside>
      )}

      {sheetAt !== null && (
        <EnemySheet gods={data.gods} enemies={enemies} startIndex={sheetAt} self={god.name}
          onPick={pickEnemy} onRemove={removeEnemy} onClose={() => setSheetAt(null)} />
      )}
    </div>
  );
}
