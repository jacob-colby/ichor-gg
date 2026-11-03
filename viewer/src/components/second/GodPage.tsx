/** The god page, for browsing without a match.
 *
 * In the match-first flow the enemy team lives on the match board (`#/`),
 * not here: this page answers "what does Ichor build on Ra, and how does it
 * compare?" with no draft in play, and offers one way into a match — "Use in
 * my match" puts the god in your slot and goes to the board.
 *
 * Same build everywhere: the six is the `model` archetype — the build
 * `/side_by_side` measures — computed by the same `useGodBuild` the match
 * board uses, from an empty enemy team.
 *
 * Phone: header -> verdict -> starter -> six -> disclosures. Desktop: a real
 * second column carrying the match entry and the reasoning.
 */
import { useEffect, useMemo } from "react";
import type { God, IndexData } from "../../types";
import { useDraft } from "../../lib/draft";
import { useUrlState, queryString } from "../../lib/urlState";
import { godLane, laneTextClass } from "../../lib/roleAccent";
import { Art, ChevronGlyph } from "./art";
import { ModeSwitch } from "./ModeSwitch";
import { AspectToggle } from "./AspectToggle";
import { decodePageQuery, encodePageQuery, writeLastGod, aspectNote } from "./pageState";
import { useWide } from "./useWide";
import { useGodBuild } from "./useGodBuild";
import { BuildAnswer, BuildMore, BuildWhy } from "./BuildBody";

export function GodPage({ god, data }: { god: God; data: IndexData }) {
  const [q, setQ] = useUrlState(decodePageQuery, encodePageQuery);
  const { mode } = q;
  const wide = useWide();

  useEffect(() => { writeLastGod(god.name); }, [god.name]);

  // Browsing: no enemy team, so the six is the god's own.
  const comp = useMemo(() => ({ allies: [god.name], enemies: [] as string[] }), [god.name]);
  const b = useGodBuild(god, data, q, comp);

  // The way into a match: you in slot one, the shared draft's enemies kept.
  const { draft, mode: draftMode, setMode: setDraftMode, setAlly } = useDraft();
  const inMatch = draft.allies[0] === god.name;
  const enemiesKnown = draft.enemies.filter(Boolean).length;
  const useInMatch = () => {
    if (draftMode !== mode) setDraftMode(mode);
    if (!inMatch) setAlly(0, god.name);
    window.location.hash = `#/${queryString(encodePageQuery(q))}`;
  };
  const matchCta = (
    <button type="button" onClick={useInMatch} data-testid="use-in-match"
      className="press flex h-12 w-full items-center justify-center gap-2 rounded-[12px] bg-accent px-4 font-cond text-[19px] font-bold uppercase text-accent-ink hover:brightness-110 lg:w-auto">
      {inMatch ? "Back to my match" : "Use in my match"}
      <ChevronGlyph size={18} />
    </button>
  );
  const matchNote = enemiesKnown > 0
    ? `Your match has ${enemiesKnown} enem${enemiesKnown === 1 ? "y" : "ies"} in it; the six re-ranks against them there.`
    : "On the match board, add the enemy team as it locks in and the six re-ranks against it.";

  const lane = godLane(god.role);

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
                <span data-testid="god-record" className={b.ranked ? "text-ink" : ""}>{b.record}</span>
              </p>
            </div>
          </div>
          <div className="mt-3 flex gap-2 lg:mt-5">
            <ModeSwitch mode={mode} onChange={(m) => setQ((p) => ({ ...p, mode: m }))} className="min-w-0 flex-1 lg:max-w-[420px]" />
            {b.aspectName && (
              <AspectToggle aspect={b.aspectName} on={q.aspect} changesBuild={b.aspectChangesBuild}
                onChange={(on) => setQ((p) => ({ ...p, aspect: on }))} />
            )}
          </div>
          {q.aspect && b.aspectName && (
            <p className="mt-2 text-note text-muted" data-testid="aspect-note">
              {aspectNote(b.aspectName, b.aspectChangesBuild, god.name)}
            </p>
          )}
        </header>

        <div className="mt-4 lg:mt-7"><BuildAnswer b={b} god={god} /></div>

        {!wide && (
          <div className="mt-5">
            {matchCta}
            <p className="mt-2 text-note text-muted">{matchNote}</p>
          </div>
        )}

        <BuildMore b={b} god={god} setQ={setQ} showWhy={!wide} />
        <div className="h-6 lg:h-16" />
      </div>

      {wide && (
        <aside aria-label="Your match and reasoning" className="min-w-0">
          <div className="sticky top-[88px] space-y-6">
            <section aria-labelledby="match-cta-h" className="rounded-[14px] border border-line bg-surface p-4">
              <h2 id="match-cta-h" className="font-cond text-[24px] font-extrabold text-ink">Playing {god.name}?</h2>
              <p className="mb-3 mt-0.5 text-note text-muted">{matchNote}</p>
              {matchCta}
            </section>
            <div className="rounded-[14px] border border-line p-4"><BuildWhy b={b} god={god} /></div>
          </div>
        </aside>
      )}
    </div>
  );
}
