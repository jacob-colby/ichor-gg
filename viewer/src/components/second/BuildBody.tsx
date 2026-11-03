/** The build itself, shared by the god page and the match board: the verdict
 *  sentence with its "Show theirs" swap, the starter, the six in buy order,
 *  and the one-tap-away disclosures under it. Both surfaces render it from
 *  the same `useGodBuild` result, so the six cannot drift between them. */
import type { Dispatch, ReactNode, SetStateAction } from "react";
import type { God } from "../../types";
import { toHash } from "../../lib/useHashRoute";
import { Art, ChevronGlyph, SwapGlyph } from "./art";
import { VerdictLine } from "./VerdictLine";
import { ItemRow } from "./ItemRow";
import { Disclosure } from "./Disclosure";
import { CompareDetail } from "./CompareDetail";
import { WhyPanel } from "./WhyPanel";
import { MAIN_ARCHETYPE, type PageQuery } from "./pageState";
import type { GodBuild } from "./useGodBuild";

export function BuildAnswer({ b, god, headingId = "six-h" }: { b: GodBuild; god: God; headingId?: string }) {
  const { verdict, verdictLoading, canSwap, showTheirs, setTheirs, starter, starterPath, r, mode, rows, listLabel, modeLabel } = b;
  return (
    <section aria-labelledby={headingId}>
      <VerdictLine verdict={verdict} loading={verdictLoading} action={canSwap ? (
        <button type="button" onClick={() => setTheirs((v) => !v)} aria-pressed={showTheirs}
          className="press -my-2.5 inline-flex h-11 items-center gap-1 whitespace-nowrap px-0.5 align-middle font-cond text-[18px] font-bold uppercase text-accent hover:text-ink">
          <SwapGlyph size={18} />{showTheirs ? "Show Ichor's" : "Show theirs"}
        </button>
      ) : undefined} />

      {starter && (
        <div className="mt-2.5 flex min-h-11 items-center gap-3" data-testid="starter">
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

      <div className="mt-2 flex items-baseline justify-between px-1 text-cap text-quiet">
        <h2 id={headingId} className="font-cond text-[16px] font-bold uppercase text-muted">{listLabel} · buy order</h2>
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
  );
}

export function BuildWhy({ b, god }: { b: GodBuild; god: God }) {
  return (
    <WhyPanel god={god.name} mode={b.mode} isModel={b.isMain} buildLabel={b.buildLabel(b.archetype)}
      changes={b.r.result?.diff.changes ?? []} culprits={b.r.threatCulprits} enemiesKnown={b.r.enemiesKnown}
      comparison={b.cmp.data} meta={b.cmp.meta} kitLine={b.kitLine} />
  );
}

export function BuildMore({ b, god, setQ, showWhy, extraLinks }: {
  b: GodBuild; god: God;
  setQ: Dispatch<SetStateAction<PageQuery>>;
  /** The phone carries the reasoning as a disclosure; desktop has a column. */
  showWhy: boolean;
  extraLinks?: ReactNode;
}) {
  const { r, archetype, buildLabel, mode, cmp, community } = b;
  return (
    <>
      <div className="mt-6 divide-y divide-line border-y border-line">
        {r.archetypes.length > 1 && (
          <Disclosure title="Other builds" hint={`${r.archetypes.length - 1} more for ${god.name}`} testId="other-builds">
            <ul className="grid gap-2 sm:grid-cols-2">
              {r.archetypes.map((e) => {
                const on = e.archetype === archetype;
                return (
                  <li key={e.archetype}>
                    <button type="button" aria-pressed={on}
                      onClick={() => { setQ((p) => ({ ...p, build: e.archetype ?? MAIN_ARCHETYPE })); b.setTheirs(false); }}
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
        {showWhy && <Disclosure title="Why this build" testId="why-disclosure"><BuildWhy b={b} god={god} /></Disclosure>}
        {mode === "conquest" && cmp.data && (
          <Disclosure title="The comparison in detail" hint="Fight by fight, and what isn't measured" testId="compare-disclosure">
            <CompareDetail d={cmp.data} meta={cmp.meta} god={god.name} community={community} />
          </Disclosure>
        )}
        <nav aria-label={`More on ${god.name}`} className="flex flex-wrap gap-x-5 py-3">
          {extraLinks}
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
    </>
  );
}
