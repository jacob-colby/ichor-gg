import { useState } from "react";
import { useIndexData } from "./hooks/useIndexData";
import { GodRail } from "./components/GodRail";
import { DetailPanel } from "./components/DetailPanel";

function App() {
  const { data, error, reload } = useIndexData();
  const [selectedGod, setSelectedGod] = useState<string | null>(null);
  const [mode, setMode] = useState("Conquest");

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
      <GodRail gods={data.gods} selectedGod={selectedGod} onSelect={setSelectedGod} />
      <div className="flex-1 p-4">
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
            onReload={reload}
          />
        ) : (
          <p className="text-muted">Select a god from the rail.</p>
        )}
      </div>
    </div>
  );
}

export default App;
