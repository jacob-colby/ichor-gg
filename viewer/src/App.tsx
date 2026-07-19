import { useState } from "react";
import { useIndexData } from "./hooks/useIndexData";
import { GodRail } from "./components/GodRail";
import { DetailPanel } from "./components/DetailPanel";
import { ManageGods } from "./components/ManageGods";
import { Footer } from "./components/Footer";

function App() {
  const { data, error, reload } = useIndexData();
  const [selectedGod, setSelectedGod] = useState<string | null>(null);
  const [mode, setMode] = useState("Conquest");
  const isDev = import.meta.env.DEV;

  const removeGod = async (name: string) => {
    await fetch("/api/gods", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "remove", name }),
    }).then((r) => r.json()).catch(() => ({ ok: false }));
    if (name === selectedGod) setSelectedGod(null);
    reload();
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

  return (
    <div className="flex h-screen bg-bg0 text-ink">
      <div className="flex flex-col overflow-y-auto">
        <GodRail
          gods={data.gods}
          selectedGod={selectedGod}
          onSelect={setSelectedGod}
          onRemove={isDev ? removeGod : undefined}
        />
        {isDev && <ManageGods onChanged={reload} />}
      </div>
      <div className="flex flex-1 flex-col overflow-hidden">
        <div className="flex-1 overflow-y-auto p-4">
          <button onClick={reload} className="mb-4 rounded bg-bg2 px-3 py-1 text-sm hover:bg-line">
            Reload data
          </button>
          {selectedGod ? (
            <DetailPanel
              god={selectedGod}
              godData={data.gods.find((g) => g.name === selectedGod)}
              items={data.items}
              builds={data.builds}
              mode={mode}
              onModeChange={setMode}
              starters={data.starters ?? []}
            />
          ) : (
            <p className="text-muted">Select a god from the rail.</p>
          )}
        </div>
        <Footer />
      </div>
    </div>
  );
}

export default App;
