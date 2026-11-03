/** Fetches a god's `/side_by_side/<slug>.json` and the shared `_meta.json`.
 *
 * The same files SideBySide.tsx reads, read the same way (no-store, a missing
 * file is "none" rather than an error). Kept separate so the new god page can
 * hold the data once and hand it to the verdict line, the swap and the
 * detail table — the old page fetched it once per section. */
import { useEffect, useState } from "react";
import { iconSlug } from "../../lib/builds";
import type { SideBySideData } from "../SideBySide";

export interface ComparisonMeta {
  data: string; level: number; window: number; band: number;
  targets: Record<"squishy" | "tank", { role: string; max_health: number }>;
}

export type Load<T> = { state: "loading" } | { state: "none" } | { state: "ready"; value: T };

function useJson<T>(url: string | null): Load<T> {
  const [out, setOut] = useState<Load<T>>({ state: url ? "loading" : "none" });
  useEffect(() => {
    if (!url) { setOut({ state: "none" }); return; }
    let live = true;
    setOut({ state: "loading" });
    fetch(url, { cache: "no-store" })
      .then((r) => (r.ok ? r.json() : null))
      .then((v) => live && setOut(v ? { state: "ready", value: v as T } : { state: "none" }))
      .catch(() => live && setOut({ state: "none" }));
    return () => { live = false; };
  }, [url]);
  return out;
}

export function useComparison(god: string | undefined) {
  const one = useJson<SideBySideData>(god ? `/side_by_side/${iconSlug(god)}.json` : null);
  const meta = useJson<ComparisonMeta>(god ? "/side_by_side/_meta.json" : null);
  return {
    loading: one.state === "loading",
    // Shape-checked: a host that answers a missing file with some other JSON
    // (an SPA fallback, a test stub) must read as "no comparison", not crash.
    data: one.state === "ready" && Array.isArray(one.value?.ichor?.items) ? one.value : null,
    meta: meta.state === "ready" && typeof meta.value?.band === "number" ? meta.value : null,
  };
}
