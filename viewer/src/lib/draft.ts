import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { DraftComp } from "../types";

export type DraftMode = "conquest" | "joust" | "arena";

/** Team size per mode — Conquest 5v5, Joust 3v3, Arena 5v5. Switching mode
 *  resizes both rows; see `resize` below for the truncate-don't-clear rule. */
export const MODE_TEAM_SIZE: Record<DraftMode, number> = {
  conquest: 5,
  joust: 3,
  arena: 5,
};

const KEY = "smite:draft";
const DEFAULT_MODE: DraftMode = "conquest";

interface StoredDraft {
  mode: DraftMode;
  allies: string[];
  enemies: string[];
}

function normalizeMode(m: unknown): DraftMode {
  return m === "joust" ? "joust" : m === "arena" ? "arena" : "conquest";
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

function sameDraft(a: StoredDraft, b: StoredDraft): boolean {
  return a.mode === b.mode && a.allies.join() === b.allies.join() && a.enemies.join() === b.enemies.join();
}

/** In-tab pub/sub so every mounted `useDraft()` instance sees every other
 *  one's writes.
 *
 * Until the dock, only `DraftPage` ever called `setAlly`/`setEnemy`/`clear` —
 * every other mount (Home's draft seam, a god page's "Draft with X" link) was
 * read-only, so two instances never needed to agree while both were live. The
 * dock is a second writer, mounted on the same page as those read-only
 * consumers, so an edit there has to reach them without a remount. A `storage`
 * event only fires in *other* tabs, never this one, so same-tab instances need
 * their own channel. */
const listeners = new Set<(d: StoredDraft) => void>();
function broadcast(state: StoredDraft): void {
  for (const l of listeners) l(state);
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
    // Runs on mount too, with every other live instance's own state — each
    // one bails via `sameDraft` below if it's already showing this, so the
    // redundant round-trip is a no-op rather than a flicker.
    broadcast(state);
  }, [state]);

  // The other half of the channel: adopt a write another mounted instance
  // just made, unless it's the one that made it (setState with an equal
  // value still re-renders, so bail out rather than pay for that on every
  // keystroke in every other mounted instance).
  useEffect(() => {
    const onUpdate = (incoming: StoredDraft) => {
      setState((prev) => (sameDraft(prev, incoming) ? prev : incoming));
    };
    listeners.add(onUpdate);
    return () => { listeners.delete(onUpdate); };
  }, []);

  useEffect(() => {
    if (!syncUrl || typeof window === "undefined") return;
    const hash = encodeDraftHash(state.mode, { allies: state.allies, enemies: state.enemies });
    window.history.replaceState(null, "", window.location.pathname + window.location.search + hash);
  }, [syncUrl, state]);

  /** Slots dropped by a shrinking mode switch, kept so switching back restores
   * them. Conquest→Joust→Conquest used to be silently lossy. */
  const overflow = useRef<{ allies: string[]; enemies: string[] }>({ allies: [], enemies: [] });

  // Someone opening a shared draft link while the app is already loaded gets a
  // `hashchange`, not a remount — without this the board silently kept showing
  // the old draft (wrong mode and all) while the address bar showed the new
  // one, and Copy link would then copy a draft that wasn't on screen.
  useEffect(() => {
    if (!syncUrl || typeof window === "undefined") return;
    const onHashChange = () => {
      const incoming = decodeDraftHash(window.location.hash, isKnownGod);
      if (!incoming) return;
      setState((prev) => {
        // Bail on an identical decode so our own replaceState can't loop.
        if (sameDraft(prev, incoming)) return prev;
        // A draft arriving from a link brings no truncation history with it.
        overflow.current = { allies: [], enemies: [] };
        return incoming;
      });
    };
    window.addEventListener("hashchange", onHashChange);
    return () => window.removeEventListener("hashchange", onHashChange);
  }, [syncUrl, isKnownGod]);

  const setMode = useCallback((mode: DraftMode) => {
    setState((prev) => {
      const n = MODE_TEAM_SIZE[mode];
      if (n < prev.allies.length) {
        overflow.current = {
          allies: prev.allies.slice(n),
          enemies: prev.enemies.slice(n),
        };
        return { mode, allies: resize(prev.allies, n), enemies: resize(prev.enemies, n) };
      }
      // Growing back: refill the tail from whatever the last shrink stashed.
      const restore = (cur: string[], stashed: string[]) => {
        const out = resize(cur, n);
        for (let i = cur.length; i < n; i += 1) out[i] = stashed[i - cur.length] ?? "";
        return out;
      };
      return {
        mode,
        allies: restore(prev.allies, overflow.current.allies),
        enemies: restore(prev.enemies, overflow.current.enemies),
      };
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
    // Drop the stash too, or a later mode round-trip resurrects gods into a
    // board the visitor explicitly emptied.
    overflow.current = { allies: [], enemies: [] };
    setState((prev) => emptyDraft(prev.mode));
  }, []);

  const draft: DraftComp = useMemo(
    () => ({ allies: state.allies, enemies: state.enemies }),
    [state.allies, state.enemies],
  );

  return { draft, mode: state.mode, setMode, setAlly, setEnemy, clear };
}
