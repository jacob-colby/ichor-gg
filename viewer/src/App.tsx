import { useEffect, useState, type ReactNode } from "react";
import { useIndexData } from "./hooks/useIndexData";
import { GodRail } from "./components/GodRail";
import { DetailPanel } from "./components/DetailPanel";
import { AddGodModal } from "./components/AddGodModal";
import { Footer } from "./components/Footer";
import { ItemsShop } from "./components/ItemsShop";
import { GodInfo } from "./components/GodInfo";
import { Legend } from "./components/Legend";
import { TierList } from "./components/TierList";
import { PatchNotes } from "./components/PatchNotes";
import { useHashRoute, toHash, navigate } from "./lib/useHashRoute";

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

  useEffect(() => {
    if (!localStorage.getItem("smite:legend-seen")) setLegendOpen(true);
  }, []);
  const closeLegend = () => {
    localStorage.setItem("smite:legend-seen", "1");
    setLegendOpen(false);
  };

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
      <div className="flex h-screen items-center justify-center bg-bg0 text-premium">
        {error} — <button onClick={reload} className="ml-2 underline">retry</button>
      </div>
    );
  }
  if (!data) {
    return <div className="flex h-screen items-center justify-center bg-bg0 text-muted">Loading…</div>;
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
            {data.data_updated && <span className="hidden font-mono text-[10.5px] text-faint sm:inline">Data from {data.data_updated}</span>}
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
        <div className="flex min-h-0 flex-1 overflow-hidden">
          {route.view === "home" ? (
            // Placeholder — Task V6 replaces this with the real home page
            // (search, pinned gods, tier slice, patch slice, freshness).
            <div className="flex-1 overflow-y-auto p-6"><p className="text-muted">Home — coming next.</p></div>
          ) : route.view === "draft" ? (
            // Placeholder — Task V4 replaces this with the real draft page.
            <div className="flex-1 overflow-y-auto p-6"><p className="text-muted">Draft — coming next.</p></div>
          ) : route.view === "items" ? (
            <div className="flex-1 overflow-y-auto"><ItemsShop items={data.items} openItem={route.item} /></div>
          ) : route.view === "tiers" ? (
            <div className="flex-1 overflow-y-auto"><TierList gods={data.tierlist?.gods ?? []} items={data.tierlist?.items ?? []} /></div>
          ) : route.view === "patch" ? (
            <div className="flex-1 overflow-y-auto"><PatchNotes periods={patchNotes} /></div>
          ) : (
            <div className="flex min-w-0 flex-1 flex-col overflow-hidden md:flex-row">
              <div className="flex shrink-0 flex-col overflow-hidden">
                <GodRail
                  gods={data.gods}
                  selectedGod={route.god ?? null}
                  onSelect={(n) => navigate(toHash.god(n))}
                  onRemove={isDev ? removeGod : undefined}
                />
                {isDev && (
                  <button type="button" onClick={() => setAddOpen(true)}
                    className="press m-2 hidden items-center justify-center gap-1.5 rounded-md border border-dashed border-line-strong px-2 py-1.5 text-xs text-faint hover:text-muted md:flex">
                    <span className="rounded border border-line-strong px-1 py-px font-mono text-[8px] uppercase tracking-wider">Dev</span>+ Add god
                  </button>
                )}
              </div>
              <div className="min-w-0 flex-1 overflow-y-auto p-4">
                {god ? (
                  <>
                    <div className="mb-4 flex w-fit gap-1.5">
                      <button type="button" onClick={() => navigate(toHash.god(god.name))} className={tabBtn(route.tab === "builds")}>Builds</button>
                      <button type="button" onClick={() => navigate(toHash.godInfo(god.name))} className={tabBtn(route.tab === "info")}>Info</button>
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
                        allGods={data.gods}
                        godItemScores={data.god_item_scores}
                        draftConfig={data.draft}
                      />
                    )}
                  </>
                ) : (
                  <p className="text-muted">Select a god from the rail.</p>
                )}
              </div>
            </div>
          )}
        </div>

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
