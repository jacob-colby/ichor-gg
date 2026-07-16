import { useState } from "react";
import { useIndexData } from "./hooks/useIndexData";
import { GodRail } from "./components/GodRail";
import { DetailPanel } from "./components/DetailPanel";

function App() {
  const { data, error, reload } = useIndexData();
  const [selectedGod, setSelectedGod] = useState<string | null>(null);

  if (error) {
    return (
      <div className="flex h-screen items-center justify-center bg-neutral-900 text-red-400">
        {error} — <button onClick={reload} className="ml-2 underline">retry</button>
      </div>
    );
  }

  if (!data) {
    return <div className="flex h-screen items-center justify-center bg-neutral-900 text-neutral-400">Loading…</div>;
  }

  return (
    <div className="flex h-screen bg-neutral-900 text-neutral-100">
      <GodRail gods={data.gods} selectedGod={selectedGod} onSelect={setSelectedGod} />
      <div className="flex-1 p-4">
        <button onClick={reload} className="mb-4 rounded bg-neutral-800 px-3 py-1 text-sm hover:bg-neutral-700">
          Reload data
        </button>
        {selectedGod ? (
          <DetailPanel god={selectedGod} builds={data.builds} />
        ) : (
          <p className="text-neutral-500">Select a god from the rail.</p>
        )}
      </div>
    </div>
  );
}

export default App;
