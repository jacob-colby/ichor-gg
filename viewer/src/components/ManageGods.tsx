import { useState } from "react";

/** Owner-only (dev) control to scrape a new god into the pool. POSTs to the
 * dev-server /api/gods endpoint; absent from the hosted static build. */
export function ManageGods({ onChanged }: { onChanged: () => void }) {
  const [name, setName] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const add = async () => {
    const n = name.trim();
    if (!n) return;
    setBusy(true);
    setError(null);
    const res = await fetch("/api/gods", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "add", name: n }),
    }).then((r) => r.json()).catch((e) => ({ ok: false, error: String(e) }));
    setBusy(false);
    if (res.ok) {
      setName("");
      onChanged();
    } else {
      setError(res.error || "Add failed");
    }
  };

  return (
    <div className="border-t border-line p-2">
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && add()}
        placeholder="Add a god…"
        disabled={busy}
        className="w-full rounded border border-line bg-bg2 px-2 py-1 text-xs text-ink"
      />
      <button
        type="button"
        onClick={add}
        disabled={busy}
        className="mt-1 w-full rounded bg-bg2 px-2 py-1 text-xs text-blue hover:bg-line disabled:opacity-50"
      >
        {busy ? "Scraping…" : "+ Add"}
      </button>
      {error && <div className="mt-1 text-[10px] text-red-400">{error}</div>}
    </div>
  );
}
