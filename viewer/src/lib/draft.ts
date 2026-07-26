import { useCallback, useEffect, useMemo, useState } from "react";
import type { DraftComp } from "../types";

export type DraftMode = "conquest" | "joust";

/** Team size per mode — Conquest 5v5, Joust 3v3. Switching mode resizes both
 *  rows; see `resize` below for the truncate-don't-clear rule. */
export const MODE_TEAM_SIZE: Record<DraftMode, number> = {
  conquest: 5,
  joust: 3,
};

const KEY = "smite:draft";
const DEFAULT_MODE: DraftMode = "conquest";

interface StoredDraft {
  mode: DraftMode;
  allies: string[];
  enemies: string[];
}

function normalizeMode(m: unknown): DraftMode {
  return m === "joust" ? "joust" : "conquest";
}

/** Fixed-length slots ("" = empty) exactly like a lineup — resizing keeps the
 *  existing prefix (truncate on shrink, pad with "" on grow) so switching
 *  mode never clears entries, it only drops the ones that no longer fit. */
function resize(arr: string[], n: number): string[] {
  return Array.from({ length: n }, (_, i) => arr[i] ?? "");
}

function emptyDraft(mode: DraftMode): StoredDraft {
  const n = MODE_TEAM_SIZE[mode];
  return { mode, allies: Array(n).fill(""), enemies: Array(n).fill("") };
}

function loadLocal(): StoredDraft {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return emptyDraft(DEFAULT_MODE);
    const parsed = JSON.parse(raw) as Partial<StoredDraft>;
    const mode = normalizeMode(parsed.mode);
    const n = MODE_TEAM_SIZE[mode];
    const allies = Array.isArray(parsed.allies) ? parsed.allies : [];
    const enemies = Array.isArray(parsed.enemies) ? parsed.enemies : [];
    return { mode, allies: resize(allies, n), enemies: resize(enemies, n) };
  } catch {
    return emptyDraft(DEFAULT_MODE);
  }
}

/** Parse a `#/draft?...` hash into a draft, or `null` when the hash isn't a
 *  draft URL carrying any god names at all — callers fall back to
 *  localStorage in that case rather than silently clobbering a saved draft
 *  every time someone lands on the bare `#/draft` nav link. `me` is ally
 *  slot 1; `a`/`e` are comma-separated lists for the rest of the allies and
 *  the enemies. Names failing `isKnownGod` (when supplied) are dropped
 *  rather than surfacing a broken slot, so a stale or unrecognized god name
 *  degrades gracefully instead of discarding the whole URL draft. */
export function decodeDraftHash(
  hash: string,
  isKnownGod?: (name: string) => boolean,
): StoredDraft | null {
  const [path, query = ""] = hash.split("?");
  const clean = path.replace(/^#\/?/, "");
  if (clean !== "draft") return null;

  const params = new URLSearchParams(query);
  if (!params.has("me") && !params.has("a") && !params.has("e")) return null;

  const known = (name: string) => !isKnownGod || isKnownGod(name);
  const names = (v: string | null) =>
    (v ?? "").split(",").map((s) => s.trim()).filter((s) => s && known(s));

  const mode = normalizeMode(params.get("m"));
  const n = MODE_TEAM_SIZE[mode];
  const me = names(params.get("me"))[0] ?? "";
  const rest = names(params.get("a"));
  const enemies = names(params.get("e"));
  return { mode, allies: resize([me, ...rest], n), enemies: resize(enemies, n) };
}

/** Encode a draft into a `#/draft?...` hash. Empty rows/slots are omitted
 *  from the query entirely (never a literal empty param). */
export function encodeDraftHash(mode: DraftMode, draft: DraftComp): string {
  const [me, ...rest] = draft.allies;
  const params = new URLSearchParams();
  params.set("m", mode);
  if (me) params.set("me", me);
  const a = rest.filter(Boolean);
  if (a.length) params.set("a", a.join(","));
  const e = draft.enemies.filter(Boolean);
  if (e.length) params.set("e", e.join(","));
  return `#/draft?${params.toString()}`;
}

export interface UseDraftOptions {
  /** When true, an existing `#/draft` URL (carrying at least one god name)
   *  wins over localStorage on load, and every draft/mode change re-syncs
   *  the URL via `replaceState` (never `pushState`, so drafting doesn't
   *  spam history). Off by default so other mounts of this hook (e.g. the
   *  god page's own draft bar) never fight over the address bar on routes
   *  that aren't the standalone draft page. */
  syncUrl?: boolean;
  /** Restricts URL decoding to gods the caller actually tracks — names that
   *  fail this check are dropped instead of producing a broken slot. */
  isKnownGod?: (name: string) => boolean;
}

/** The entered ally/enemy draft plus its mode, persisted to localStorage
 *  and — opt-in via `syncUrl` — mirrored in the URL hash for sharing. */
export function useDraft(options: UseDraftOptions = {}) {
  const { syncUrl = false, isKnownGod } = options;
  const [state, setState] = useState<StoredDraft>(() => {
    if (syncUrl && typeof window !== "undefined") {
      const fromUrl = decodeDraftHash(window.location.hash, isKnownGod);
      if (fromUrl) return fromUrl;
    }
    return loadLocal();
  });

  useEffect(() => {
    try {
      localStorage.setItem(KEY, JSON.stringify(state));
    } catch {
      /* ignore quota / private-mode failures */
    }
  }, [state]);

  useEffect(() => {
    if (!syncUrl || typeof window === "undefined") return;
    const hash = encodeDraftHash(state.mode, { allies: state.allies, enemies: state.enemies });
    window.history.replaceState(null, "", window.location.pathname + window.location.search + hash);
  }, [syncUrl, state]);

  const setMode = useCallback((mode: DraftMode) => {
    setState((prev) => {
      const n = MODE_TEAM_SIZE[mode];
      return { mode, allies: resize(prev.allies, n), enemies: resize(prev.enemies, n) };
    });
  }, []);

  const setAlly = useCallback((i: number, name: string) => {
    setState((prev) => {
      const allies = [...prev.allies];
      allies[i] = name;
      return { ...prev, allies };
    });
  }, []);

  const setEnemy = useCallback((i: number, name: string) => {
    setState((prev) => {
      const enemies = [...prev.enemies];
      enemies[i] = name;
      return { ...prev, enemies };
    });
  }, []);

  const clear = useCallback(() => {
    setState((prev) => emptyDraft(prev.mode));
  }, []);

  const draft: DraftComp = useMemo(
    () => ({ allies: state.allies, enemies: state.enemies }),
    [state.allies, state.enemies],
  );

  return { draft, mode: state.mode, setMode, setAlly, setEnemy, clear };
}
