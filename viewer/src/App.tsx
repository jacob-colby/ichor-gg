import { useEffect, useState, type ReactNode } from "react";
import { useIndexData } from "./hooks/useIndexData";
import { GodRail } from "./components/GodRail";
import { DetailPanel } from "./components/DetailPanel";
import { AddGodModal } from "./components/AddGodModal";
import { Footer } from "./components/Footer";
import { ItemsShop } from "./components/ItemsShop";
import { GodsIndex } from "./components/GodsIndex";
import { GodInfo } from "./components/GodInfo";
import { Legend } from "./components/Legend";
import { useHashRoute, toHash, navigate } from "./lib/useHashRoute";

type View = "builds" | "gods" | "items";

const NAV: { view: View; label: string; icon: ReactNode }[] = [
  { view: "builds", label: "Builds", icon: (
    <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M14.5 17.5 3 6V3h3l11.5 11.5" /><path d="M13 19l6-6" /><path d="M16 16l4 4" /><path d="M19 21l2-2" /></svg>
  ) },
  { view: "gods", label: "Gods", icon: (
    <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="8" r="4" /><path d="M4 21c0-4 4-6 8-6s8 2 8 6" /></svg>
  ) },
  { view: "items", label: "Items", icon: (
    <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 2l8 4v6c0 5-3.5 8-8 10-4.5-2-8-5-8-10V6z" /></svg>
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
    if (view === "builds") navigate(route.god ? toHash.god(route.god) : toHash.home());
    else if (view === "gods") navigate(toHash.gods());
    else navigate(toHash.items());
  };

  const title = route.view === "gods" ? "Gods" : route.view === "items" ? "Items" : "Builds";
  const count =
    route.view === "gods" ? `${data.gods.length} tracked`
    : route.view === "items" ? `${data.items.length} items`
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
          {route.view === "items" ? (
            <div className="flex-1 overflow-y-auto"><ItemsShop items={data.items} openItem={route.item} /></div>
          ) : route.view === "gods" ? (
            <div className="flex-1 overflow-y-auto"><GodsIndex gods={data.gods} /></div>
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
