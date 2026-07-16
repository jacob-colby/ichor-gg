import { useCallback, useEffect, useState } from "react";
import type { IndexData } from "../types";

interface UseIndexDataResult {
  data: IndexData | null;
  error: string | null;
  reload: () => Promise<void>;
}

export function useIndexData(): UseIndexDataResult {
  const [data, setData] = useState<IndexData | null>(null);
  const [error, setError] = useState<string | null>(null);

  const load = useCallback(async () => {
    try {
      const response = await fetch("/index.json", { cache: "no-store" });
      if (!response.ok) {
        setError(`Failed to load index.json (HTTP ${response.status})`);
        setData(null);
        return;
      }
      const json = (await response.json()) as IndexData;
      setData(json);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load index.json");
      setData(null);
    }
  }, []);

  useEffect(() => {
    load();
  }, [load]);

  return { data, error, reload: load };
}
