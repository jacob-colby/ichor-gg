/** What the aspect's own PLAYERS buy, under the six, when the aspect is on.
 *
 * Community data, not the model, and it says so first: Ichor's six above is
 * built for the god's base role, and an aspect overlay cannot move a god's
 * role, so when most aspect players take it elsewhere (Tsukuyomi's Mangetsu:
 * 56% Mid on a Jungler) this is the only place on the page that says what
 * that build is. The record is `community_aspects` on the Conquest note
 * (`pipeline/smite/aspect_matches.py`):
 *
 *  - The entry reads the newest patch window, else the last closed one, else
 *    the newest windows POOLED until they hold the minimum (30). The label
 *    names the patches and the games ("57 games · OB45–OB47"), so a pooled
 *    entry never passes for one patch's.
 *  - Shares are of GAMES, and are what those games ended holding: not a buy
 *    order, and not players (a rare aspect can be a few people).
 *  - An item whose stats moved after the oldest window read carries an
 *    asterisk, and the notes under the list say when and how many of the
 *    games that bought it are older — printed, not a tooltip.
 *  - The starter keeps its base → upgrade pairing, the share summed over both
 *    ends (`lib/starters.groupStarters`, the main starter tile's rule), so
 *    the record ships every starter seen, not a top 3.
 *
 * Joust and Arena have no per-aspect record, so they say that in words and
 * show nothing: Conquest's aspect players are in Conquest's roles. Neutral
 * throughout — violet is the model's voice, and this is not the model. */
import type { ReactNode } from "react";
import type { AspectCommunityEntry, AspectShare, CommunityAspects, Item } from "../../types";
import { groupStarters, starterPathLabel } from "../../lib/starters";
import { toHash } from "../../lib/useHashRoute";
import { Art } from "./art";
import { KitTile } from "./KitTile";
import { MODE_NAME, type Mode } from "./verdict";

const pct = (r: number) => `${Math.round(r * 100)}%`;
const fold = (s: string) => s.toLowerCase().replace(/\s+/g, " ").trim();
const shortAspect = (a: string) => a.replace(/^Aspect of /i, "").replace(/^the /i, "");

/** The six the record shows: its most-held items. */
export const ASPECT_SIX = 6;

/** The aspect's entry in the god's record, matched on the name with case
 *  folded ("Aspect Of Valor" on the source, "Aspect of Valor" in a kit). */
export function aspectEntry(record: CommunityAspects | undefined, aspect: string): AspectCommunityEntry | undefined {
  return record?.aspects.find((a) => fold(a.aspect) === fold(aspect));
}

/** "OB44–OB47" over the windows an entry has any games in. */
function spanOf(byWindow: Record<string, number>): string {
  const ws = Object.keys(byWindow).filter((w) => byWindow[w] > 0)
    .sort((a, b) => Number(a.replace(/\D/g, "")) - Number(b.replace(/\D/g, "")));
  if (!ws.length) return "";
  const [first, last] = [ws[0].toUpperCase(), ws[ws.length - 1].toUpperCase()];
  return first === last ? first : `${first}–${last}`;
}

/** Why these windows, in one clause — only when it is not simply "this patch". */
function windowWhy(entry: AspectCommunityEntry, minimum: number): string | null {
  if (entry.window_rule === "pooled back") return `pooled: no recent patch alone has ${minimum} games`;
  if (entry.window_rule === "last closed") return `the last patch: this one has fewer than ${minimum} games so far`;
  return null;
}

export function AspectCommunity({ aspect, mode, record, itemsByName }: {
  aspect: string;
  mode: Mode;
  /** The god's Conquest `community_aspects`, or undefined when there is none. */
  record: CommunityAspects | undefined;
  itemsByName: Record<string, Item>;
}) {
  const short = shortAspect(aspect);
  const heading = (right?: string) => (
    <div className="flex items-baseline justify-between gap-3 px-1 text-cap text-quiet">
      <h2 id="aspect-community-h" className="font-cond text-[16px] font-bold uppercase text-muted">
        {short} players&rsquo; build
      </h2>
      {right && <span className="num whitespace-nowrap" data-testid="aspect-community-span">{right}</span>}
    </div>
  );
  const frame = (body: ReactNode, right?: string) => (
    <section aria-labelledby="aspect-community-h" data-testid="aspect-community" className="mt-6">
      {heading(right)}
      {body}
    </section>
  );
  const say = (text: string) => <p className="mt-1.5 px-1 text-note text-muted" data-testid="aspect-community-note">{text}</p>;

  if (mode !== "conquest") {
    return frame(say(`Only Conquest records what aspect players buy. ${MODE_NAME[mode]} has no per-aspect record, so none is shown here.`));
  }
  const entry = aspectEntry(record, aspect);
  if (!entry) return frame(say(`No record yet of what ${aspect} players buy.`));
  const minimum = record!.minimum_matches;
  if (entry.status !== "shown" || !entry.items) {
    const games = Object.values(entry.matches_by_window).reduce((a, n) => a + n, 0);
    const span = spanOf(entry.matches_by_window);
    return frame(say(`Too few games to show: ${games.toLocaleString("en-US")} Conquest ${games === 1 ? "game" : "games"}${span ? ` across ${span}` : ""}, and this needs ${minimum}.`));
  }

  const games = entry.matches ?? 0;
  const why = windowWhy(entry, minimum);
  const partial = (entry.windows ?? []).filter((w) => record!.partial_windows?.[w]);
  const six = entry.items.slice(0, ASPECT_SIX);

  // The starter as a PATH, its share both ends summed; the rest by root.
  const paths = groupStarters((entry.starters ?? []).map((s) => ({ name: s.name, pick_rate: s.share, win_rate: 0 })), itemsByName);
  const top = paths[0];
  const topEnds = top ? [top.base?.name, top.upgrade?.name].filter(Boolean) as string[] : [];
  const relic = entry.relics?.[0];

  // Everything flagged that is ON SCREEN — the six, the starter path's ends,
  // the relic — in screen order, each once.
  const starterFlagged = (entry.starters ?? []).filter((s) => topEnds.includes(s.name) && s.changed);
  const flagged: AspectShare[] = [...starterFlagged, ...(relic?.changed ? [relic] : []), ...six.filter((i) => i.changed)];
  const mark = (s?: AspectShare) => (s?.changed ? `changed ${s.changed.patch}*` : null);
  const starterMark = starterFlagged.map((s) => mark(s)).find(Boolean);

  return frame(
    <>
      <p className="mt-1.5 px-1 text-note text-muted" data-testid="aspect-community-note">
        Community, not Ichor&rsquo;s model: what Conquest games with {aspect} ended holding
        {why ? ` — ${why}` : ""}.
      </p>
      {entry.role_shift && entry.base_role && (
        <p className="mt-1.5 px-1 text-copy text-ink-soft" data-testid="aspect-role-shift">
          Most play it <span className="font-semibold text-ink">{entry.role_shift.role} ({pct(entry.role_shift.share)})</span>,
          {" "}not {entry.base_role.split(" ").join(" or ")} ({pct(entry.base_role_share ?? 0)}). Ichor&rsquo;s six above is
          built for {entry.base_role.split(" ").join(" and ")}: the model can&rsquo;t move a god&rsquo;s role for an aspect yet.
        </p>
      )}

      {(top || relic) && (
        <div className={`mt-2 grid gap-1.5 ${top && relic ? "sm:grid-cols-2" : ""}`} data-testid="aspect-kit-tiles">
          {top && (
            <KitTile kind="Start" testId="aspect-starter" icon={(top.base ?? top.upgrade)!.name}
              inset={top.base && top.upgrade ? top.upgrade.name : undefined}
              name={starterPathLabel(top)}
              reason={[`${pct(top.pick_rate)} of these games open this way`, starterMark].filter(Boolean).join(" · ")}
              alternatives={paths.slice(1, 3).map((p) => ({ name: p.rootName, icon: p.rootName, share: p.pick_rate }))}
              altLabel="Others" altUnit="of these games" />
          )}
          {relic && (
            <KitTile kind="Relic" testId="aspect-relic" icon={relic.name} name={relic.name}
              reason={[`${pct(relic.share)} of these games take it`, mark(relic)].filter(Boolean).join(" · ")}
              alternatives={(entry.relics ?? []).slice(1, 3).map((x) => ({ name: x.name, icon: x.name, share: x.share }))}
              altLabel="Others" altUnit="of these games" />
          )}
        </div>
      )}

      <ol className="mt-1.5 space-y-1.5" data-testid="aspect-six" aria-label={`What ${short} games hold most, most held first`}>
        {six.map((it) => (
          <li key={it.name} data-testid="aspect-item" data-changed={it.changed ? true : undefined}>
            <a href={toHash.item(it.name)}
              className="press grid min-h-[64px] grid-cols-[48px_minmax(0,1fr)] items-center gap-3 rounded-[12px] bg-surface py-2 pl-2.5 pr-3.5 hover:bg-surface-2">
              <Art name={it.name} kind="item" className="h-12 w-12 rounded-[8px]" />
              <span className="min-w-0">
                <span data-testid="aspect-item-name" className="block font-cond text-row font-bold text-ink [overflow-wrap:anywhere]">{it.name}</span>
                <span className="mt-0.5 block text-note text-muted">
                  In {pct(it.share)} of these games{it.changed && <> · {mark(it)}</>}
                </span>
              </span>
            </a>
          </li>
        ))}
      </ol>

      {flagged.length > 0 && (
        <div className="mt-2 space-y-1 px-1 text-cap text-muted" data-testid="aspect-changed-notes">
          {flagged.map((s) => (
            <p key={s.name}><span aria-hidden="true">* </span><span className="text-ink-soft">{s.name}</span>: {s.changed!.says}.</p>
          ))}
          <p className="text-quiet">Read from Ichor&rsquo;s item-stat snapshots, which don&rsquo;t record passives: a passive change is not flagged.</p>
        </div>
      )}

      <p className="mt-2 px-1 text-cap text-quiet" data-testid="aspect-community-source">
        Ranked by share of games, not a buy order. Games, not players: a rare aspect can be a few people.
        {" "}SmiteBrain, Obsidian and above{partial.length ? `; ${partial.map((w) => w.toUpperCase()).join(", ")} only in part` : ""}.
      </p>
    </>,
    `${games.toLocaleString("en-US")} games · ${entry.patches ?? ""}`,
  );
}
