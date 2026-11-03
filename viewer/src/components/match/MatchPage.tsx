/** Match first: the app opens on the match, not on a god.
 *
 * One screen holds the whole job. The draft board sits at the top — your slot
 * and the enemy's five — and the moment your slot has a god, the build fills
 * in BELOW it on the same screen: the verdict sentence, the starter, the six.
 * Every enemy added re-ranks that six in place (the swapped row locks in), so
 * land -> your god -> five enemies never changes the route.
 *
 * Same build everywhere: the board is the shared draft (`useDraft`, the one
 * the full draft page reads — you are ally slot 1), and the six is the
 * `model` archetype passed into `useDraftResult` via `useGodBuild`, the same
 * hook the god page uses. Mode, aspect and build live in the hash query.
 *
 * Phone: board, then the build, then one-tap disclosures. Desktop: the board
 * across the top, the build left, the reasoning right. */
import { useEffect, useMemo, useState, type Dispatch, type SetStateAction } from "react";
import type { God, IndexData } from "../../types";
import { useDraft, MODE_TEAM_SIZE, encodeDraftHash } from "../../lib/draft";
import { useUrlState } from "../../lib/urlState";
import { toHash } from "../../lib/useHashRoute";
import { AspectToggle } from "../second/AspectToggle";
import { EnemySheet } from "../second/EnemySheet";
import { ChevronGlyph } from "../second/art";
import { MAIN_ARCHETYPE, decodePageQuery, encodePageQuery, writeLastGod, aspectNote, type PageQuery } from "../second/pageState";
import { useWide } from "../second/useWide";
import { useGodBuild } from "../second/useGodBuild";
import { BuildAnswer, BuildMore, BuildWhy } from "../second/BuildBody";
import { MatchBoard, type BoardProps } from "./MatchBoard";
import { YouSheet } from "./YouSheet";
import { ROSTER_HASH } from "./routes";

type Open = { kind: "you" } | { kind: "enemy" | "ally"; index: number } | null;

const linkCls = "press inline-flex h-11 items-center gap-1 font-cond text-[18px] font-bold uppercase text-muted hover:text-ink";

export function MatchPage({ data }: { data: IndexData }) {
  const [q, setQ] = useUrlState(decodePageQuery, encodePageQuery);
  const { mode } = q;
  const wide = useWide();

  const { draft, mode: draftMode, setMode: setDraftMode, setAlly, setEnemy, clear } = useDraft();
  // The address bar names the mode; the shared draft follows it.
  useEffect(() => { if (draftMode !== mode) setDraftMode(mode); }, [draftMode, mode, setDraftMode]);
  const n = MODE_TEAM_SIZE[mode];
  const allies = useMemo(() => Array.from({ length: n }, (_, i) => draft.allies[i] ?? ""), [draft.allies, n]);
  const enemies = useMemo(() => Array.from({ length: n }, (_, i) => draft.enemies[i] ?? ""), [draft.enemies, n]);
  const god = allies[0] ? data.gods.find((g) => g.name === allies[0]) : undefined;

  const [open, setOpen] = useState<Open>(null);
  const [alliesOpen, setAlliesOpen] = useState(() => draft.allies.slice(1).some(Boolean));

  const pickYou = (name: string) => {
    setAlly(0, name);
    writeLastGod(name);
    setOpen(null);
    // A different god's builds have different names; the main six is the default.
    setQ((p) => ({ ...p, build: MAIN_ARCHETYPE, aspect: false }));
  };

  const board: Omit<BoardProps, "changeCount" | "record" | "ranked" | "aspect" | "aspectNote"> = {
    mode, onMode: (m) => setQ((p) => ({ ...p, mode: m })), god, allies, enemies, alliesOpen, wide,
    onToggleAllies: () => setAlliesOpen((v) => !v),
    onYou: () => setOpen({ kind: "you" }),
    onAlly: (i) => setOpen({ kind: "ally", index: i }),
    onEnemy: (i) => setOpen({ kind: "enemy", index: i }),
    actions: (allies.some(Boolean) || enemies.some(Boolean)) ? (
      <button type="button" onClick={clear}
        className="press h-[52px] rounded-[12px] px-3 text-note font-semibold text-muted hover:text-ink">
        New match
      </button>
    ) : undefined,
  };
  const draftHref = encodeDraftHash(mode, { allies, enemies });

  return (
    <div className="mx-auto w-full max-w-[1240px] px-4 lg:px-6 lg:pt-8">
      {god ? (
        <MatchBuild key={god.name} god={god} data={data} q={q} setQ={setQ} board={board}
          comp={{ allies, enemies }} wide={wide} draftHref={draftHref} onClear={clear} />
      ) : (
        <>
          <MatchBoard {...board} changeCount={0} />
          <div className="mt-6 max-w-[56ch] lg:mt-8" data-testid="match-empty">
            <p className="text-copy text-muted">
              Your build appears under the board the moment you pick. Add enemies as they lock in —
              each one re-ranks the six in place, without leaving this screen.
            </p>
            <a href={ROSTER_HASH} className={`${linkCls} mt-2`}>Browse every god<ChevronGlyph size={16} /></a>
          </div>
        </>
      )}

      {open?.kind === "you" && (
        <YouSheet gods={data.gods} current={god?.name} onPick={pickYou} onClose={() => setOpen(null)} />
      )}
      {open?.kind === "enemy" && (
        <EnemySheet gods={data.gods} enemies={enemies} startIndex={open.index} self={god?.name}
          onPick={setEnemy} onRemove={(i) => setEnemy(i, "")} onClose={() => setOpen(null)} />
      )}
      {open?.kind === "ally" && (
        <EnemySheet side="Ally" gods={data.gods} enemies={allies.slice(1)} startIndex={open.index} self={god?.name}
          onPick={(i, name) => setAlly(i + 1, name)} onRemove={(i) => setAlly(i + 1, "")} onClose={() => setOpen(null)} />
      )}
    </div>
  );
}

function MatchBuild({ god, data, q, setQ, board, comp, wide, draftHref, onClear }: {
  god: God; data: IndexData; q: PageQuery; setQ: Dispatch<SetStateAction<PageQuery>>;
  board: Omit<BoardProps, "changeCount" | "record" | "ranked" | "aspect" | "aspectNote">;
  comp: { allies: string[]; enemies: string[] }; wide: boolean; draftHref: string; onClear: () => void;
}) {
  const b = useGodBuild(god, data, q, comp);

  const aspect = b.aspectName ? (
    <AspectToggle aspect={b.aspectName} on={q.aspect} changesBuild={b.aspectChangesBuild}
      onChange={(on) => setQ((p) => ({ ...p, aspect: on }))} />
  ) : undefined;
  const note = q.aspect && b.aspectName ? (
    <p className="mt-2 text-note text-muted" data-testid="aspect-note">
      {aspectNote(b.aspectName, b.aspectChangesBuild, god.name)}
    </p>
  ) : undefined;

  const links = (
    <>
      <a href={draftHref} className={linkCls}>Full draft board<ChevronGlyph size={16} /></a>
      <a href={toHash.god(god.name)} className={linkCls}>{god.name}&rsquo;s page<ChevronGlyph size={16} /></a>
      {!wide && (
        <button type="button" onClick={onClear} className={linkCls}>New match</button>
      )}
    </>
  );

  return (
    <>
      <MatchBoard {...board} record={b.record} ranked={b.ranked} aspect={aspect} aspectNote={note}
        changeCount={b.r.changeCount} />
      <div className="lg:mt-8 lg:grid lg:grid-cols-[minmax(0,1fr)_380px] lg:gap-12">
        <div className="min-w-0 lg:max-w-[680px]">
          <div className="mt-3.5 lg:mt-0"><BuildAnswer b={b} god={god} /></div>
          <BuildMore b={b} god={god} setQ={setQ} showWhy={!wide} extraLinks={links} />
          <div className="h-6 lg:h-16" />
        </div>
        {wide && (
          <aside aria-label="Why this build" className="min-w-0">
            <div className="sticky top-[88px] rounded-[14px] border border-line p-4"><BuildWhy b={b} god={god} /></div>
          </aside>
        )}
      </div>
    </>
  );
}
