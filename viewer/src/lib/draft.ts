import { useCallback, useEffect, useState } from "react";
import type { DraftComp } from "../types";

const KEY = "smite:draft";
const ALLY_SLOTS = 4;
const ENEMY_SLOTS = 5;

const empty = (): DraftComp => ({
  allies: Array(ALLY_SLOTS).fill(""),
  enemies: Array(ENEMY_SLOTS).fill(""),
});

function load(): DraftComp {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return empty();
    const parsed = JSON.parse(raw) as Partial<DraftComp>;
    const allies = Array.isArray(parsed.allies) ? parsed.allies : [];
    const enemies = Array.isArray(parsed.enemies) ? parsed.enemies : [];
    return {
      allies: Array.from({ length: ALLY_SLOTS }, (_, i) => allies[i] ?? ""),
      enemies: Array.from({ length: ENEMY_SLOTS }, (_, i) => enemies[i] ?? ""),
    };
  } catch {
    return empty();
  }
}

/** The entered ally/enemy draft, persisted to localStorage. Fixed-length
 *  slots ("" = empty) exactly like a lineup — never sparse/reordering. */
export function useDraft() {
  const [draft, setDraft] = useState<DraftComp>(load);

  useEffect(() => {
    try {
      localStorage.setItem(KEY, JSON.stringify(draft));
    } catch {
      /* ignore quota / private-mode failures */
    }
  }, [draft]);

  const setAlly = useCallback((i: number, name: string) => {
    setDraft((prev) => {
      const allies = [...prev.allies];
      allies[i] = name;
      return { ...prev, allies };
    });
  }, []);

  const setEnemy = useCallback((i: number, name: string) => {
    setDraft((prev) => {
      const enemies = [...prev.enemies];
      enemies[i] = name;
      return { ...prev, enemies };
    });
  }, []);

  const clear = useCallback(() => setDraft(empty()), []);

  return { draft, setAlly, setEnemy, clear };
}
