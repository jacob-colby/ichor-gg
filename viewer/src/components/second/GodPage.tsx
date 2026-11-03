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
 */
import { useEffect, useMemo, useState } from "react";
import type { BuildNote, CommunityBuildEntry, CuratedBuildEntry, God, IndexData } from "../../types";
import { useDraft, MODE_TEAM_SIZE } from "../../lib/draft";
import { useDraftResult } from "../../lib/useDraftResult";
import { useUrlState } from "../../lib/urlState";
import { tabLabel } from "../../lib/builds";
import { toHash } from "../../lib/useHashRoute";
import { godLane, laneTextClass } from "../../lib/roleAccent";
import { useComparison } from "./useComparison";
import { verdictSentence, MODE_NAME } from "./verdict";
import { itemReason } from "./itemReason";
import { Art, ChevronGlyph, SwapGlyph } from "./art";
import { ModeSwitch } from "./ModeSwitch";
import { AspectToggle } from "./AspectToggle";
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

  const r = useDraftResult(comp, mode, data.gods, data.items, data.builds, data.god_item_scores,
    data.draft, data.god_item_damage, q.aspect, q.build);

  // ── Builds, community, aspect ──────────────────────────────────────────
  const note = noteFor(data.builds, god.name, modeLabel);
  const community = noteFor(data.builds, god.name, "Conquest")?.builds
    .find((b) => b.source === "community") as CommunityBuildEntry | undefined;
  const archetype = r.activeEntry?.archetype ?? q.build;
  const isMain = archetype === MAIN_ARCHETYPE;
  const aspectName = god.aspects?.[0]?.name ?? null;
  const suggested = (note?.builds ?? []).filter((b) => b.source === "suggested") as CuratedBuildEntry[];
  const baseOfArch = suggested.find((b) => b.archetype === archetype && !b.aspect);
  const aspectOfArch = suggested.find((b) => b.archetype === archetype && !!b.aspect);
  const aspectChangesBuild = !!aspectOfArch && !sameOrder(aspectOfArch.slot_order, baseOfArch?.slot_order);
  const aspectOnBuild = q.aspect && r.aspectScored && aspectChangesBuild;

  // ── Comparison + verdict ───────────────────────────────────────────────
  const cmp = useComparison(god.name);
  const shipped = (r.activeEntry?.slot_order as string[] | undefined) ?? [];
  const verdict = cmp.loading && mode === "conquest" ? null : verdictSentence({
    d: cmp.data, god: god.name, mode, archetype, shownSix: shipped,
    aspectBuild: aspectOnBuild ? aspectName : null, band: cmp.meta?.band, draftSwaps: r.changeCount,
  });
  const canSwap = mode === "conquest" && isMain && !aspectOnBuild && !!cmp.data;
  const [theirs, setTheirs] = useState(false);
  const showTheirs = theirs && canSwap;
  useEffect(() => { setTheirs(false); }, [god.name]);

  // ── The six on screen ──────────────────────────────────────────────────
  const swaps = new Map((r.result?.diff.changes ?? []).map((c) => [c.added, c]));
  const six = showTheirs ? cmp.data!.community.items : (r.result?.adapted.core ?? shipped);
  let running = 0;
  let unknownCost = false;
  const rows = six.map((name, i) => {
    const item = r.itemsByName[name];
    if (item?.cost == null) unknownCost = true;
    running += item?.cost ?? 0;
    const swap = showTheirs ? undefined : swaps.get(name);
    return {
      name, position: i + 1, cumulative: unknownCost ? null : running,
      reason: itemReason(name, { god: god.name, mode, community, item, swap }), swapped: !!swap,
    };
  });

  const starter = showTheirs ? community?.starter : (r.activeEntry?.starter ?? community?.starter);
  const starterPath = starter ? r.starters.find((p) => p.rootName === starter.base) : undefined;

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
  const pickEnemy = (i: number, name: string) => {
    if (draft.allies[0] !== god.name) setAlly(0, god.name);
    setEnemy(i, name);
  };
  const clearEnemies = () => enemies.forEach((_, i) => setEnemy(i, ""));

  const buildLabel = (a?: string) => (a === MAIN_ARCHETYPE ? "Ichor's main six" : r.archetypes.find((e) => e.archetype === a)
    ? tabLabel(r.archetypes.find((e) => e.archetype === a)!) : a ?? "");
  const listLabel = showTheirs ? "The community's six" : isMain ? "Ichor's six" : `${buildLabel(archetype)} build`;

  const why = (
    <WhyPanel god={god.name} mode={mode} isModel={isMain} buildLabel={buildLabel(archetype)}
      changes={r.result?.diff.changes ?? []} culprits={r.threatCulprits} enemiesKnown={r.enemiesKnown}
      comparison={cmp.data} meta={cmp.meta} kitLine={kitLine} />
  );
  const strip = (variant: "bar" | "panel") => (
    <EnemyStrip enemies={enemies} onOpen={setSheetAt} changeCount={r.changeCount} variant={variant}
      onClear={clearEnemies} />
  );

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
                <span className="text-quiet"> · </span>
                <span data-testid="god-record" className={mode === "conquest" && tier?.tier_score ? "text-ink" : ""}>{record}</span>
              </p>
            </div>
          </div>
          <div className="mt-3 flex gap-2 lg:mt-5">
            <ModeSwitch mode={mode} onChange={(m) => setQ((p) => ({ ...p, mode: m }))} className="min-w-0 flex-1 lg:max-w-[420px]" />
            {aspectName && (
              <AspectToggle aspect={aspectName} on={q.aspect} changesBuild={aspectChangesBuild}
                onChange={(on) => setQ((p) => ({ ...p, aspect: on }))} />
            )}
          </div>
          {q.aspect && aspectName && (
            <p className="mt-2 text-note text-muted" data-testid="aspect-note">
              {aspectNote(aspectName, aspectChangesBuild, god.name)}
            </p>
          )}
        </header>

        {/* ── The answer ── */}
        <section aria-labelledby="six-h" className="mt-4 lg:mt-7">
          <VerdictLine verdict={verdict} loading={mode === "conquest" && cmp.loading} action={canSwap ? (
            <button type="button" onClick={() => setTheirs((v) => !v)} aria-pressed={showTheirs}
              className="press -my-2.5 inline-flex h-11 items-center gap-1 whitespace-nowrap px-0.5 align-middle font-cond text-[18px] font-bold uppercase text-accent hover:text-ink">
              <SwapGlyph size={18} />{showTheirs ? "Show Ichor's" : "Show theirs"}
            </button>
          ) : undefined} />

          {starter && (
            <div className="mt-3 flex min-h-11 items-center gap-3" data-testid="starter">
              <span className="flex -space-x-2">
                <Art name={starter.base} kind="item" className="h-8 w-8 rounded-[7px] ring-2 ring-ground" />
                <Art name={starter.upgrade} kind="item" className="h-8 w-8 rounded-[7px] ring-2 ring-ground" />
              </span>
              <p className="min-w-0 text-note leading-snug text-muted">
                <span className="font-cond text-[16px] font-bold uppercase text-ink">Start</span>{" "}
                {starter.base} → {starter.upgrade}
                {starterPath && (
                  <span className="block text-quiet">
                    {r.startersAreConquest || mode !== "conquest" ? "In Conquest, " : ""}
                    {Math.round(starterPath.lead.pick_rate * 100)}% of {god.name} players open this way
                  </span>
                )}
              </p>
            </div>
          )}

          <div className="mt-2.5 flex items-baseline justify-between px-1 text-cap text-quiet">
            <h2 id="six-h" className="font-cond text-[16px] font-bold uppercase text-muted">{listLabel} · buy order</h2>
            <span aria-hidden="true">Gold spent</span>
          </div>
          {rows.length > 0 ? (
            <ol className="mt-1.5 space-y-1.5" data-testid="six">
              {rows.map((row) => (
                <ItemRow key={`${showTheirs ? "t" : "i"}-${row.name}`} position={row.position} name={row.name}
                  cumulativeGold={row.cumulative} reason={row.reason} swapped={row.swapped} />
              ))}
            </ol>
          ) : (
            <p className="mt-3 rounded-[12px] border border-dashed border-line p-4 text-copy text-muted">
              No {modeLabel} build has been made for {god.name} yet.
            </p>
          )}
        </section>

        {/* ── One tap away ── */}
        <div className="mt-6 divide-y divide-line border-y border-line">
          {r.archetypes.length > 1 && (
            <Disclosure title="Other builds" hint={`${r.archetypes.length - 1} more for ${god.name}`} testId="other-builds">
              <ul className="grid gap-2 sm:grid-cols-2">
                {r.archetypes.map((e) => {
                  const on = e.archetype === archetype;
                  return (
                    <li key={e.archetype}>
                      <button type="button" aria-pressed={on}
                        onClick={() => { setQ((p) => ({ ...p, build: e.archetype ?? MAIN_ARCHETYPE })); setTheirs(false); }}
                        className={`press flex min-h-14 w-full items-center gap-3 rounded-[12px] px-3 py-2 text-left ${
                          on ? "bg-surface-2 ring-2 ring-accent" : "bg-surface hover:bg-surface-2"}`}>
                        <span className="min-w-0 flex-1 font-cond text-[19px] font-bold uppercase text-ink">{buildLabel(e.archetype)}</span>
                        <span className="flex gap-0.5" aria-hidden="true">
                          {(e.slot_order as string[]).map((n) => <Art key={n} name={n} kind="item" className="h-6 w-6 rounded-[4px]" />)}
                        </span>
                      </button>
                    </li>
                  );
                })}
              </ul>
            </Disclosure>
          )}
          {!wide && <Disclosure title="Why this build" testId="why-disclosure">{why}</Disclosure>}
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
        <aside aria-label="Enemy team and reasoning" className="min-w-0">
          <div className="sticky top-[88px] space-y-6">
            {strip("panel")}
            <div className="rounded-[14px] border border-line p-4">{why}</div>
          </div>
        </aside>
      )}

      {sheetAt !== null && (
        <EnemySheet gods={data.gods} enemies={enemies} startIndex={sheetAt} self={god.name}
          onPick={pickEnemy} onRemove={(i) => setEnemy(i, "")} onClose={() => setSheetAt(null)} />
      )}
    </div>
  );
}
