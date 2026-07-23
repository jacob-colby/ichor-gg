import { useEffect, useState } from "react";
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
      <div className="flex h-screen items-center justify-center bg-neutral-900 text-red-400">
        {error} — <button onClick={reload} className="ml-2 underline">retry</button>
      </div>
    );
  }
  if (!data) {
    return <div className="flex h-screen items-center justify-center bg-neutral-900 text-muted">Loading…</div>;
  }

  const god = route.god ? data.gods.find((g) => g.name === route.god) : undefined;
  const navBtn = (active: boolean) =>
    `rounded px-3 py-1 text-sm font-display font-semibold ${active ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"}`;
  const tabBtn = (active: boolean) =>
    `px-3 py-1 font-display text-xs font-semibold ${active ? "bg-gold text-bg0" : "bg-bg2 text-muted hover:text-ink"}`;

  return (
    <div className="flex h-screen flex-col bg-bg0 text-ink">
      <div className="flex items-center gap-2 border-b border-line px-3 py-2">
        <span className="mr-2 font-display text-sm font-bold text-gold">SMITE 2 Builds</span>
        <button type="button" onClick={() => navigate(route.god ? toHash.god(route.god) : toHash.home())} className={navBtn(route.view === "builds")}>Builds</button>
        <button type="button" onClick={() => navigate(toHash.gods())} className={navBtn(route.view === "gods")}>Gods</button>
        <button type="button" onClick={() => navigate(toHash.items())} className={navBtn(route.view === "items")}>Items</button>
        {data.data_updated && (
          <span className="ml-auto text-[10px] text-muted">Data from {data.data_updated}</span>
        )}
        <button type="button" onClick={reload} className={`${data.data_updated ? "" : "ml-auto"} rounded bg-bg2 px-3 py-1 text-sm hover:bg-line`}>Reload</button>
        <button type="button" onClick={() => setLegendOpen(true)} aria-label="Help" className="rounded bg-bg2 px-3 py-1 text-sm hover:bg-line">?</button>
      </div>

      {isDev && scraping && (
        <div className="border-b border-gold/40 bg-gold/10 px-3 py-1 text-center text-xs text-gold">
          Scraping new data… this can take a minute.
        </div>
      )}

      <div className="flex flex-1 overflow-hidden">
        {route.view === "items" ? (
          <div className="flex-1 overflow-y-auto"><ItemsShop items={data.items} openItem={route.item} /></div>
        ) : route.view === "gods" ? (
          <div className="flex-1 overflow-y-auto"><GodsIndex gods={data.gods} /></div>
        ) : (
          <>
            <div className="flex flex-col overflow-y-auto">
              <GodRail
                gods={data.gods}
                selectedGod={route.god ?? null}
                onSelect={(n) => navigate(toHash.god(n))}
                onRemove={isDev ? removeGod : undefined}
              />
              {isDev && (
                <button type="button" onClick={() => setAddOpen(true)}
                  className="m-2 rounded bg-bg2 px-2 py-1 text-xs text-blue hover:bg-line">＋ Add god</button>
              )}
            </div>
            <div className="flex-1 overflow-y-auto p-4">
              {god ? (
                <>
                  <div className="mb-3 flex w-fit overflow-hidden rounded-md border border-line">
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
          </>
        )}
      </div>
      <Footer />
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

export default App;
