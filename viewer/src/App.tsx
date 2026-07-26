import { useEffect, useState, type ReactNode } from "react";
import { useIndexData } from "./hooks/useIndexData";
import { GodSidebar } from "./components/GodSidebar";
import { Home } from "./components/Home";
import { DraftPage } from "./components/DraftPage";
import { DetailPanel } from "./components/DetailPanel";
import { AddGodModal } from "./components/AddGodModal";
import { Footer } from "./components/Footer";
import { ItemsShop } from "./components/ItemsShop";
import { GodInfo } from "./components/GodInfo";
import { Legend } from "./components/Legend";
import { TierList } from "./components/TierList";
import { PatchNotes } from "./components/PatchNotes";
import { AppSkeleton, HomeSkeleton } from "./components/Skeleton";
import { relativeDate } from "./lib/relativeDate";
import { useHashRoute, toHash, navigate } from "./lib/useHashRoute";
import { documentTitle } from "./lib/documentTitle";

type View = "home" | "builds" | "draft" | "items" | "tiers" | "patch";

const NAV: { view: View; label: string; icon: ReactNode }[] = [
  { view: "home", label: "Home", icon: (
    <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M4 11.5 12 4l8 7.5" /><path d="M6 10v10a1 1 0 0 0 1 1h3v-6h4v6h3a1 1 0 0 0 1-1V10" /></svg>
  ) },
  { view: "builds", label: "Builds", icon: (
    <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M14.5 17.5 3 6V3h3l11.5 11.5" /><path d="M13 19l6-6" /><path d="M16 16l4 4" /><path d="M19 21l2-2" /></svg>
  ) },
  { view: "draft", label: "Draft", icon: (
    <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M3 6l7 6-7 6" /><path d="M21 6l-7 6 7 6" /></svg>
  ) },
  { view: "items", label: "Items", icon: (
    <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 2l8 4v6c0 5-3.5 8-8 10-4.5-2-8-5-8-10V6z" /></svg>
  ) },
  { view: "tiers", label: "Tiers", icon: (
    <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M4 20V10" /><path d="M12 20V4" /><path d="M20 20v-6" /></svg>
  ) },
  { view: "patch", label: "Patch", icon: (
    <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M9 12h6" /><path d="M9 16h6" /><path d="M13 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z" /><path d="M13 3v5h5" /></svg>
  ) },
];

function App() {
  const { data, error, reload } = useIndexData();
  const route = useHashRoute();
  const [mode, setMode] = useState("Conquest");
  const [legendOpen, setLegendOpen] = useState(false);
  const [scraping, setScraping] = useState(false);
  const [addOpen, setAddOpen] = useState(false);
  const isDev = import.meta.env.DEV;

  // Per-route tab/history title — these links get pasted into Discord, and a
  // history full of identical "ichor" entries is useless.
  useEffect(() => {
    document.title = documentTitle(route);
  }, [route]);

  // The Legend used to open itself on first load, so a first-time visitor met
  // 700 characters of body copy about a screen they weren't on before seeing
  // anything. Home explains itself in place now; this stays on demand.
  const closeLegend = () => setLegendOpen(false);

  const godsApi = async (action: "add" | "remove", name: string) => {
    setScraping(true);
    const res = await fetch("/api/gods", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action, name }),
    }).then((r) => r.json()).catch(() => ({ ok: false }));
    setScraping(false);
    if (action === "remove" && name === route.god) navigate(toHash.home());
    reload();
    return res;
  };
  const removeGod = (name: string) => godsApi("remove", name);
  const addGod = async (name: string) => {
    setAddOpen(false);
    await godsApi("add", name);
  };

  if (error) {
    return (
      <div className="flex h-screen flex-col items-center justify-center gap-4 bg-bg0 px-6 text-center text-ink">
        <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-gold font-display text-base font-bold text-bg0">S2</div>
        <div className="max-w-[46ch]">
          <h1 className="font-display text-2xl font-bold text-ink">Couldn&rsquo;t load the build data</h1>
          <p className="mt-2 text-sm leading-relaxed text-muted">
            ichor reads everything from a single data file, and that file didn&rsquo;t come back.
            It&rsquo;s usually a refresh away — if it keeps failing, the site is probably mid-deploy.
          </p>
        </div>
        <button type="button" onClick={reload} className="press rounded-md bg-gold px-4 py-1.5 text-sm font-medium text-bg0">
          Try again
        </button>
        {/* The technical detail stays available without leading with it. */}
        <p className="font-mono text-[10.5px] text-faint">{error}</p>
      </div>
    );
  }
  if (!data) {
    return (
      <div className="flex h-screen bg-bg0 text-ink">
        {/* Same outer chrome as the loaded shell (icon rail + header bar) so
            the page doesn't jump once index.json lands — only the content
            area is a placeholder. */}
        <nav className="hidden w-16 shrink-0 flex-col items-center gap-3.5 border-r border-line bg-rail py-3.5 md:flex">
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-gold font-display text-[15px] font-bold text-bg0">S2</div>
        </nav>
        <div className="flex min-w-0 flex-1 flex-col overflow-hidden">
          <header className="flex items-center gap-3 border-b border-line px-4 py-2.5">
            <span className="font-display text-base font-bold text-ink">ichor</span>
            <div className="ml-auto flex items-center gap-3">
              <button type="button" onClick={reload} className="press rounded-md bg-bg2 px-3 py-1.5 text-xs text-muted hover:text-ink">Reload</button>
            </div>
          </header>
          {/* Shaped like the route that's actually coming, so nothing jumps
              when index.json lands. */}
          <div className="flex min-h-0 flex-1 overflow-hidden">
            {route.view === "home"
              ? <div className="flex-1 overflow-y-auto"><HomeSkeleton /></div>
              : <AppSkeleton />}
          </div>
        </div>
      </div>
    );
  }

  const god = route.god ? data.gods.find((g) => g.name === route.god) : undefined;
  const goTo = (view: View) => {
    if (view === "home") navigate(toHash.home());
    else if (view === "builds") navigate(route.god ? toHash.god(route.god) : toHash.builds());
    else if (view === "draft") navigate(toHash.draft());
    else if (view === "items") navigate(toHash.items());
    else if (view === "tiers") navigate(toHash.tiers());
    else navigate(toHash.patch());
  };

  const patchNotes = data.patch_notes ?? [];
  const title =
    route.view === "home" ? "Home"
    : route.view === "draft" ? "Draft"
    : route.view === "items" ? "Items"
    : route.view === "tiers" ? "Tiers"
    : route.view === "patch" ? "Patch"
    : "Builds";
  const count =
    route.view === "home" ? `${data.gods.length} gods`
    : route.view === "draft" ? ""
    : route.view === "items" ? `${data.items.length} items`
    : route.view === "tiers" ? `${data.tierlist?.gods.length ?? 0} gods · ${data.tierlist?.items.length ?? 0} items`
    : route.view === "patch" ? (patchNotes.length > 0 ? `${patchNotes.length} patches` : "")
    : god ? god.pantheon ?? "" : `${data.gods.length} gods`;

  return (
    <div className="flex h-screen bg-bg0 text-ink">
      {/* First focusable on the page — the icon rail is seven stops deep. */}
      <a
        href="#main"
        className="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-50 focus:rounded-md focus:bg-gold focus:px-3 focus:py-2 focus:font-display focus:text-sm focus:font-semibold focus:text-bg0"
      >
        Skip to content
      </a>

      {/* Desktop icon rail */}
      <nav className="hidden w-16 shrink-0 flex-col items-center gap-3.5 border-r border-line bg-rail py-3.5 md:flex">
        <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-gold font-display text-[15px] font-bold text-bg0">S2</div>
        {NAV.map((n) => {
          const active = route.view === n.view;
          return (
            <button key={n.view} type="button" onClick={() => goTo(n.view)} aria-label={n.label} aria-current={active}
              className={`press flex h-9 w-9 items-center justify-center rounded-[11px] transition-colors duration-[180ms] ease-standard ${active ? "border border-gold bg-bg2 text-gold" : "bg-bg2 text-muted hover:text-ink-soft"}`}>
              {n.icon}
            </button>
          );
        })}
        <button type="button" onClick={() => setLegendOpen(true)} aria-label="Help"
          className="press mt-auto flex h-9 w-9 items-center justify-center rounded-[11px] bg-bg2 text-muted hover:text-ink-soft">?</button>
      </nav>

      <div className="flex min-w-0 flex-1 flex-col overflow-hidden">
        {/* Header */}
        <header className="flex items-center gap-3 border-b border-line px-4 py-2.5">
          <span className="font-display text-base font-bold text-ink">{title}</span>
          {count && <span className="font-mono text-[11px] text-faint">{count}</span>}
          <div className="ml-auto flex items-center gap-3">
            {data.data_updated && (
              <span
                data-testid="header-freshness"
                title={data.data_updated}
                className="hidden font-mono text-[10.5px] text-faint sm:inline"
              >
                Updated {relativeDate(data.data_updated)}{data.data_patch ? ` · ${data.data_patch}` : ""}
              </span>
            )}
            {isDev && (
              <button type="button" onClick={() => setAddOpen(true)}
                className="press hidden items-center justify-center gap-1.5 rounded-md border border-dashed border-line-strong px-2.5 py-1.5 text-xs text-faint hover:text-muted md:flex">
                <span className="rounded border border-line-strong px-1 py-px font-mono text-[8px] uppercase tracking-wider">Dev</span>+ Add god
              </button>
            )}
            <button type="button" onClick={reload} className="press rounded-md bg-bg2 px-3 py-1.5 text-xs text-muted hover:text-ink">Reload</button>
            <button type="button" onClick={() => setLegendOpen(true)} aria-label="Help" className="press rounded-md bg-bg2 px-2.5 py-1.5 text-xs text-muted hover:text-ink md:hidden">?</button>
          </div>
        </header>

        {/* Dev-only scraping banner — quiet tier, flat fade */}
        {isDev && scraping && (
          <div className="flex items-center justify-center gap-2 border-b border-dashed border-line-strong bg-bg1 px-3 py-1.5 text-[11.5px] text-faint">
            <span className="rounded border border-line-strong px-1.5 py-px font-mono text-[9px] uppercase tracking-wider text-faint">Dev</span>
            Scraping new data… this can take a minute.
          </div>
        )}

        {/* Content */}
        <main id="main" tabIndex={-1} className="flex min-h-0 flex-1 overflow-hidden focus:outline-none">
          {route.view === "home" ? (
            <div className="flex-1 overflow-y-auto"><Home data={data} /></div>
          ) : route.view === "draft" ? (
            <div className="flex-1 overflow-y-auto">
              <DraftPage
                gods={data.gods}
                items={data.items}
                builds={data.builds}
                godItemScores={data.god_item_scores}
                draftConfig={data.draft}
              />
            </div>
          ) : route.view === "items" ? (
            <div className="flex-1 overflow-y-auto"><ItemsShop
                items={data.items}
                openItem={route.item}
                tierItems={data.tierlist?.items ?? []}
                goldValues={data.item_gold_values ?? {}}
              /></div>
          ) : route.view === "tiers" ? (
            <div className="flex-1 overflow-y-auto"><TierList tierlist={data.tierlist} /></div>
          ) : route.view === "patch" ? (
            <div className="flex-1 overflow-y-auto"><PatchNotes periods={patchNotes} /></div>
          ) : (
            <div className="flex min-w-0 flex-1 flex-col overflow-hidden md:flex-row">
              <GodSidebar
                gods={data.gods}
                selectedGod={route.god ?? null}
                onSelect={(n) => navigate(toHash.god(n))}
                onRemove={isDev ? removeGod : undefined}
              />
              <div className="min-w-0 flex-1 overflow-y-auto p-4">
                {god ? (
                  <>
                    <div role="group" aria-label="God detail section" className="mb-4 flex w-fit gap-1.5">
                      <button type="button" aria-pressed={route.tab === "builds"} onClick={() => navigate(toHash.god(god.name))} className={tabBtn(route.tab === "builds")}>Builds</button>
                      <button type="button" aria-pressed={route.tab === "info"} onClick={() => navigate(toHash.godInfo(god.name))} className={tabBtn(route.tab === "info")}>Info</button>
                    </div>
                    {route.tab === "info" ? (
                      <GodInfo god={god} />
                    ) : (
                      <DetailPanel
                        god={god.name}
                        godData={god}
                        items={data.items}
                        builds={data.builds}
                        mode={mode}
                        onModeChange={setMode}
                        starters={data.starters ?? []}
                        // Per-mode slice, never the Conquest-mirroring top
                        // level: Joust has no community ratings at all, so
                        // reading `tierlist.gods` there would assert a
                        // community score that doesn't exist for that mode.
                        tierEntry={(
                          (mode === "Joust" ? data.tierlist?.joust : data.tierlist?.conquest)
                          ?? data.tierlist
                        )?.gods.find((g) => g.name === god.name)}
                      />
                    )}
                  </>
                ) : (
                  <p className="text-muted">Select a god from the sidebar.</p>
                )}
              </div>
            </div>
          )}
        </main>

        <Footer />

        {/* Mobile bottom tab bar */}
        <nav className="flex border-t border-line bg-rail md:hidden">
          {NAV.map((n) => {
            const active = route.view === n.view;
            return (
              <button key={n.view} type="button" onClick={() => goTo(n.view)} aria-current={active}
                className={`press flex flex-1 flex-col items-center gap-1 py-2 font-display text-[11px] font-semibold ${active ? "border-t-2 border-gold text-gold" : "border-t-2 border-transparent text-muted"}`}>
                {n.icon}{n.label}
              </button>
            );
          })}
        </nav>
      </div>

      {legendOpen && <Legend onClose={closeLegend} />}
      {isDev && addOpen && (
        <AddGodModal
          roster={data.roster ?? []}
          tracked={data.gods.map((g) => g.name)}
          onAdd={addGod}
          onClose={() => setAddOpen(false)}
        />
      )}
    </div>
  );
}

const tabBtn = (active: boolean) =>
  `press rounded-md px-3.5 py-1.5 font-display text-xs font-semibold transition-colors duration-[150ms] ease-standard ${active ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"}`;

export default App;
