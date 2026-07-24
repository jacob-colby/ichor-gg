import { useCallback, useEffect, useState } from "react";

const KEY = "smite:pinnedGods";

function load(): string[] {
  try {
    const raw = localStorage.getItem(KEY);
    return raw ? (JSON.parse(raw) as string[]) : [];
  } catch {
    return [];
  }
}

/** Pinned god names, persisted to localStorage. Pinned gods sort to the top. */
export function usePins() {
  const [pins, setPins] = useState<string[]>(load);

  useEffect(() => {
    try {
      localStorage.setItem(KEY, JSON.stringify(pins));
    } catch {
      /* ignore quota / private-mode failures */
    }
  }, [pins]);

  const toggle = useCallback((name: string) => {
    setPins((prev) => (prev.includes(name) ? prev.filter((n) => n !== name) : [...prev, name]));
  }, []);

  const isPinned = useCallback((name: string) => pins.includes(name), [pins]);

  return { pins, toggle, isPinned };
}
