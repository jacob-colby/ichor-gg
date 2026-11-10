import { useCallback, useEffect, useRef, useState } from "react";
import { useIndexData } from "./hooks/useIndexData";
import { AddGodModal } from "./components/AddGodModal";
import { GodInfo } from "./components/GodInfo";
import { GodItems } from "./components/GodItems";
import { GodRanking } from "./components/GodRanking";
import { Legend } from "./components/Legend";
import { AppSkeleton, HomeSkeleton } from "./components/Skeleton";
import { AppNav, Mark, type MoreLink, type NavTab } from "./components/second/AppNav";
import { GodGrid } from "./components/second/GodGrid";
import { GodPage } from "./components/second/GodPage";
import { MAIN_ARCHETYPE } from "./components/second/pageState";
import { GodSubPage } from "./components/second/GodSubPage";
import { TiersPage } from "./components/second/TiersPage";
import { ItemsPage } from "./components/second/ItemsPage";
import { PatchPage } from "./components/second/PatchPage";
import { MethodPage } from "./components/second/MethodPage";
import { DraftBoard } from "./components/second/DraftBoard";
import { useWide } from "./components/second/useWide";
import { CommandField } from "./components/command/CommandField";
import { gridFilterText, queryHash, type ParsedQuery } from "./components/command/query";
import { clearRecentGods, pushRecentGod, readRecentGods } from "./components/command/recents";
import { useDraft, MODE_TEAM_SIZE } from "./lib/draft";
import { flushQuery, hashQuery } from "./lib/urlState";
import { freshness } from "./lib/freshness";
import { useHashRoute, toHash } from "./lib/useHashRoute";
import { documentTitle } from "./lib/documentTitle";
import type { CuratedBuildEntry } from "./types";

/* The Second Screen shell, with the typed query (direction A + C).
 *
 * The app opens on "Who are you playing?" and every other route sits inside
 * one chrome: a bottom tab bar on a phone (Gods · Draft · More), a slim
 * top bar from `lg` up. The old floating draft dock is gone from this shell —
 * the god page carries the enemy team itself, and Draft is one tab away
 * everywhere else, so the dock would only be a second copy of a control.
 *
 * One command field — "ra vs hecate ymir joust" — is the search. From `lg` up
 * it lives in the top bar on every route; on a phone it is the god-select
 * screen's search box and nowhere else (the god page's enemy strip is the
 * enemy UI there). `/` or Ctrl/⌘K focuses whichever one is on screen. */
function App() {
  const { data, error, reload } = useIndexData();
  const route = useHashRoute();
  const [legendOpen, setLegendOpen] = useState(false);
  const [scraping, setScraping] = useState(false);
  const [addOpen, setAddOpen] = useState(false);
  const wide = useWide();
  const { setMode: setDraftMode, setEnemy } = useDraft();
  const isDev = import.meta.env.DEV;

  /* Recent gods: every god whose build page is opened, by any route. Read
   * once the roster is in (the first read may seed from the retired query and
   * last-god stores, which name gods by text); set during render, so the row
   * is there on the first frame rather than pushing the grid down a frame
   * later. */
  const [recents, setRecents] = useState<string[] | null>(null);
  if (data && recents === null) setRecents(readRecentGods(data.gods));
  const viewed = data && route.god && route.lens === "builds" && data.gods.some((g) => g.name === route.god)
    ? route.god : null;
  useEffect(() => { if (data && viewed) setRecents(pushRecentGod(viewed, data.gods)); }, [data, viewed]);

  /* Submit a query. A god of your own lands on its page with the enemies as
   * `vs=` and the mode in the URL; that page writes them into the shared draft
   * (you in ally slot 1) — one writer, so a page still unmounting can't fight
   * it over the mode. A god alone lands on a bare god URL and leaves the
   * stored draft alone. Enemies with no god of your own open the draft board
   * on them, written here because the board has no `vs=` to read. */
  const run = useCallback((q: ParsedQuery) => {
    flushQuery(); // a queued filter write must not land on the page we open
    if (q.you) {
      window.location.hash = queryHash({ you: q.you, enemies: q.enemies, mode: q.mode, aspect: q.aspect });
      return;
    }
    const mode = q.mode ?? "conquest";
    setDraftMode(mode);
    for (let i = 0; i < MODE_TEAM_SIZE[mode]; i += 1) setEnemy(i, q.enemies[i] ?? "");
    window.location.hash = toHash.draft();
  }, [setDraftMode, setEnemy]);
  const openItem = useCallback((name: string) => { flushQuery(); window.location.hash = toHash.item(name); }, []);
  const forgetRecents = useCallback(() => { clearRecentGods(); setRecents([]); }, []);

  /* `/` (outside a text field) or Ctrl/⌘K focuses the command field. */
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      const t = e.target as HTMLElement | null;
      const typing = !!t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName));
      const combo = (e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k";
      if (!combo && (e.key !== "/" || typing || e.altKey || e.ctrlKey || e.metaKey)) return;
      const field = document.querySelector<HTMLInputElement>("[data-command-input]");
      if (!field) return;
      e.preventDefault();
      field.focus();
      field.select?.();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  /* From lg up the top bar's field drives the roster grid's filter. */
  const [boardText, setBoardText] = useState<string | null>(null);
  const onBarText = useCallback((text: string, q: ParsedQuery) => setBoardText(gridFilterText(text, q)), []);
  useEffect(() => { if (route.god || route.lens !== "board") setBoardText(null); }, [route.god, route.lens]);

  /* Refetching index.json is a pipeline affordance, not a visitor's control,
   * so it is dev-only — and it reports what it did, because a control that
   * runs silently is indistinguishable from one that is broken. */
  const [reloadState, setReloadState] = useState<"idle" | "busy" | "done">("idle");
  const doneTimer = useRef<number | undefined>(undefined);
  const runReload = useCallback(async () => {
    window.clearTimeout(doneTimer.current);
    setReloadState("busy");
    await reload();
    setReloadState("done");
    doneTimer.current = window.setTimeout(() => setReloadState("idle"), 1600);
  }, [reload]);
  useEffect(() => () => window.clearTimeout(doneTimer.current), []);

  useEffect(() => { document.title = documentTitle(route); }, [route]);
  // A new route starts at the top; the document scrolls, not a panel.
  useEffect(() => { window.scrollTo?.(0, 0); }, [route.god, route.lens]);

  const godsApi = async (action: "add" | "remove", name: string) => {
    setScraping(true);
    const res = await fetch("/api/gods", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action, name }),
    }).then((r) => r.json()).catch(() => ({ ok: false }));
    setScraping(false);
    reload();
    return res;
  };
  const addGod = async (name: string) => { setAddOpen(false); await godsApi("add", name); };

  if (error) {
    return (
      <div className="flex min-h-dvh flex-col items-center justify-center gap-4 px-6 text-center text-ink">
        <Mark size={30} />
        <div className="max-w-[46ch]">
          <h1 className="font-cond text-head font-extrabold text-ink">Couldn&rsquo;t load the build data</h1>
          <p className="mt-2 text-copy text-muted">
            ichor reads everything from a single data file, and that file didn&rsquo;t come back.
            It&rsquo;s usually a refresh away — if it keeps failing, the site is probably mid-deploy.
          </p>
        </div>
        <button type="button" onClick={reload}
          className="press h-11 rounded-[10px] bg-accent px-5 font-cond text-[18px] font-bold uppercase text-accent-ink">
          Try again
        </button>
        <p className="text-cap text-quiet">{error}</p>
      </div>
    );
  }

  if (!data) {
    return (
      <div className="min-h-dvh text-ink">
        <div className="flex h-14 items-center border-b border-line px-4 lg:px-6"><Mark /></div>
        {route.god ? <AppSkeleton /> : <HomeSkeleton />}
      </div>
    );
  }

  const god = route.god ? data.gods.find((g) => g.name === route.god) : undefined;
  const missingGod = !!route.god && !god;

  const active: NavTab = route.god || route.lens === "board" ? "gods"
    : route.lens === "draft" ? "draft" : "more";
  const activeMore = (["tiers", "items", "patch", "method"] as const).includes(route.lens as MoreLink)
    && !route.god ? (route.lens as MoreLink) : undefined;

  // The god's own Conquest core, so the per-god items lens reads against it.
  const godCore = god ? (data.builds.find((b) => b.god === god.name && b.mode === "Conquest")?.builds.find(
    (b) => b.source === "suggested" && (b as CuratedBuildEntry).archetype === "core" && !(b as CuratedBuildEntry).fun,
  ) as CuratedBuildEntry | undefined)?.slot_order : undefined;

  const onBoard = !route.god && route.lens === "board";
  const barField = wide ? (
    <CommandField key={onBoard ? "board" : "bar"} variant="bar" gods={data.gods} items={data.items}
      onSubmit={run} onItem={openItem} recents={recents ?? []} clearOnSubmit
      seedText={onBoard ? hashQuery(window.location.hash).get("q") ?? "" : ""}
      onText={onBoard ? onBarText : undefined} autoFocus={onBoard}
      label="Search a god, a matchup or an item" placeholder="ra vs hecate ymir" />
  ) : null;

  const devSlot = isDev ? (
    <>
      <button type="button" onClick={() => setAddOpen(true)}
        className="press h-10 rounded-full border border-dashed border-line px-3 text-cap text-quiet hover:text-muted">
        Dev · + Add god
      </button>
      <button type="button" onClick={runReload} disabled={reloadState === "busy"}
        className="press h-10 rounded-full border border-dashed border-line px-3 text-cap text-quiet hover:text-muted disabled:opacity-60">
        Dev · <span aria-live="polite">
          {reloadState === "busy" ? "Reloading…" : reloadState === "done" ? "Reloaded" : "Reload"}
        </span>
      </button>
    </>
  ) : null;

  return (
    <div className="min-h-dvh text-ink">
      <a href="#main"
        className="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[60] focus:rounded-[10px] focus:bg-accent focus:px-4 focus:py-3 focus:font-cond focus:text-[18px] focus:font-bold focus:uppercase focus:text-accent-ink">
        Skip to content
      </a>

      <AppNav active={active} activeMore={activeMore}
        currentGod={god?.name}
        onHelp={() => setLegendOpen(true)} dataUpdated={data.data_updated} dataPatch={data.data_patch}
        devSlot={devSlot} search={barField} />

      {isDev && scraping && (
        <p className="border-b border-dashed border-line px-4 py-2 text-center text-cap text-quiet">
          Dev · Scraping new data… this can take a minute.
        </p>
      )}

      <main id="main" tabIndex={-1} className="pb-tabbar focus:outline-none">
        {missingGod ? (
          <div className="mx-auto w-full max-w-[1240px] px-4 pt-8 lg:px-6">
            <h1 className="font-cond text-head font-extrabold text-ink">No god called “{route.god}”</h1>
            <p className="mt-2 max-w-[60ch] text-copy text-muted">
              Nothing in this index goes by that name. It may have been renamed or dropped since that link was made.
            </p>
            <a href={toHash.home()}
              className="press mt-4 inline-flex h-11 items-center rounded-[10px] bg-accent px-4 font-cond text-[18px] font-bold uppercase text-accent-ink">
              Choose a god
            </a>
          </div>
        ) : god ? (
          route.lens === "kit" ? (
            <GodSubPage god={god} title="Kit and abilities"><GodInfo god={god} /></GodSubPage>
          ) : route.lens === "items" ? (
            <GodSubPage god={god} title="Every item, ranked for this god">
              <GodItems god={god.name} scores={data.god_item_scores?.[god.name]?.conquest}
                items={data.items} core={godCore ?? []} />
            </GodSubPage>
          ) : route.lens === "ranking" ? (
            <GodSubPage god={god} title="Where this god ranks in Conquest">
              <GodRanking god={god.name} role={god.role} entries={data.tierlist?.conquest?.gods ?? data.tierlist?.gods}
                modeLabel="Conquest" />
            </GodSubPage>
          ) : (
            <GodPage key={god.name} god={god} data={data} />
          )
        ) : route.lens === "draft" ? (
          <DraftBoard gods={data.gods} items={data.items} builds={data.builds}
              godItemScores={data.god_item_scores} draftConfig={data.draft}
              godItemDamage={data.god_item_damage} initialArchetype={MAIN_ARCHETYPE} />
        ) : route.lens === "items" ? (
          <ItemsPage items={data.items} openItem={route.item}
              tierItems={(data.tierlist?.conquest ?? data.tierlist)?.items ?? []} goldValues={data.item_gold_values ?? {}} />
        ) : route.lens === "tiers" ? (
          <TiersPage tierlist={data.tierlist} communitySource={data.community_source} />
        ) : route.lens === "patch" ? (
          <PatchPage periods={data.patch_notes ?? []} itemNames={data.items.map((i) => i.name)} />
        ) : route.lens === "method" ? (
          <MethodPage method={data.method} goldValues={data.item_gold_values ?? {}}
              items={data.items} godCount={data.gods.length} />
        ) : (
          <GodGrid gods={data.gods} items={data.items} recents={recents ?? []}
            onRun={run} onItem={openItem} onClearRecents={forgetRecents}
            fieldInBar={wide} query={boardText} />
        )}
      </main>

      {legendOpen && <Legend onClose={() => setLegendOpen(false)}
        freshness={freshness(data.data_updated, data.data_patch)?.title} />}
      {isDev && addOpen && (
        <AddGodModal roster={data.roster ?? []} tracked={data.gods.map((g) => g.name)}
          onAdd={addGod} onClose={() => setAddOpen(false)} />
      )}
    </div>
  );
}

export default App;
