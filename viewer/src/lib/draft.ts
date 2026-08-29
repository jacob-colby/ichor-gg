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

/** A draft decoded from a URL, plus the names that URL carried and this build
 *  could not place. Separate from `StoredDraft` because it is not part of the
 *  draft — it is what happened while reading one, and it has to reach the
 *  surface rather than the store. */
export interface DecodedDraft extends StoredDraft {
  /** Names in the link that failed `isKnownGod`, in the order the URL gave
   *  them. Empty on a clean decode. */
  dropped: string[];
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
 *  degrades gracefully instead of discarding the whole URL draft.
 *
 *  THE DROPPED NAMES COME BACK WITH THE DRAFT. Dropping them is right — a
 *  slot holding a god this build has never scored can only render as a hole —
 *  but doing it silently is not: the board came up short a god, the address
 *  bar was then rewritten without it, and nothing anywhere said so. Someone
 *  who pasted a five-enemy link got a four-enemy read of their match and no
 *  reason to distrust it. `dropped` is that reason, and the surface owes the
 *  reader a line about it (audit F11, 2026-08-23). */
export function decodeDraftHash(
  hash: string,
  isKnownGod?: (name: string) => boolean,
): DecodedDraft | null {
  const [path, query = ""] = hash.split("?");
  const clean = path.replace(/^#\/?/, "");
  if (clean !== "draft") return null;

  const params = new URLSearchParams(query);
  if (!params.has("me") && !params.has("a") && !params.has("e")) return null;

  const known = (name: string) => !isKnownGod || isKnownGod(name);
  const dropped: string[] = [];
  const names = (v: string | null) =>
    (v ?? "").split(",").map((s) => s.trim()).filter((s) => {
      if (!s) return false;
      if (known(s)) return true;
      dropped.push(s);
      return false;
    });

  const mode = normalizeMode(params.get("m"));
  const n = MODE_TEAM_SIZE[mode];
  const me = names(params.get("me"))[0] ?? "";
  const rest = names(params.get("a"));
  const enemies = names(params.get("e"));
  return { mode, allies: resize([me, ...rest], n), enemies: resize(enemies, n), dropped };
}

/** How the picker names the slot it is filling. Ally 1 is "you" everywhere
 *  else on the board, so it is "you" here rather than "ally 1".
 *
 *  The picker stays mounted while a pick advances it, so this heading is the
 *  only thing that can say it moved — and it is the dialog's accessible name,
 *  so it says so to a screen reader too. */
export function pickerSlotLabel(kind: "ally" | "enemy", index: number): string {
  if (kind === "ally") return index === 0 ? "for you" : `for ally ${index + 1}`;
  return `for enemy ${index + 1}`;
}

/** The slot a pick should move to, or `null` to close the picker.
 *
 * Adding a five-god enemy row cost ten clicks: every slot had to be opened
 * before a god could go in it, so the picker closed itself after every single
 * pick and the reader re-opened it five times to do one job.
 *
 * Two rules keep the advance from being a surprise:
 *
 *  - It moves FORWARD along the same side only. Rolling from the ally row into
 *    the enemy row would be a bigger jump than a pick implies, and rolling
 *    backwards to an earlier gap would move the picker somewhere the reader
 *    was not looking.
 *  - It only fires when the slot just filled was EMPTY. Re-opening a filled
 *    slot is an edit, not an addition, and an edit that then jumped to a
 *    different slot would look like it had changed the wrong one.
 *
 * Lives here rather than in either surface because both the page and the dock
 * render the same board, and a board that advances on one and not the other is
 * two boards. */
export function nextEmptySlot(
  draft: DraftComp, kind: "ally" | "enemy", index: number, wasEmpty: boolean,
): { kind: "ally" | "enemy"; index: number } | null {
  if (!wasEmpty) return null;
  const side = kind === "ally" ? draft.allies : draft.enemies;
  for (let i = index + 1; i < side.length; i += 1) {
    if (!side[i]) return { kind, index: i };
  }
  return null;
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

  /** Names the incoming link carried that this build could not place. Held
   *  apart from `state` so it never reaches localStorage or the broadcast
   *  channel: it describes one read of one URL, not the draft itself. */
  const [dropped, setDropped] = useState<string[]>(() => {
    if (syncUrl && typeof window !== "undefined") {
      return decodeDraftHash(window.location.hash, isKnownGod)?.dropped ?? [];
    }
    return [];
  });
  const dismissDropped = useCallback(() => setDropped([]), []);

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
      // A link arriving into a live page gets the same notice a link arriving
      // on load does — the drop is just as silent either way.
      setDropped(incoming.dropped);
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

  // Editing the board answers the notice: whatever the link failed to place,
  // the reader has now seen the board and moved on. Leaving it up would let a
  // sentence about a URL outlive the draft that URL produced.
  const setAlly = useCallback((i: number, name: string) => {
    setDropped([]);
    setState((prev) => {
      const allies = [...prev.allies];
      allies[i] = name;
      return { ...prev, allies };
    });
  }, []);

  const setEnemy = useCallback((i: number, name: string) => {
    setDropped([]);
    setState((prev) => {
      const enemies = [...prev.enemies];
      enemies[i] = name;
      return { ...prev, enemies };
    });
  }, []);

  const clear = useCallback(() => {
    setDropped([]);
    // Drop the stash too, or a later mode round-trip resurrects gods into a
    // board the visitor explicitly emptied.
    overflow.current = { allies: [], enemies: [] };
    setState((prev) => emptyDraft(prev.mode));
  }, []);

  const draft: DraftComp = useMemo(
    () => ({ allies: state.allies, enemies: state.enemies }),
    [state.allies, state.enemies],
  );

  return { draft, mode: state.mode, setMode, setAlly, setEnemy, clear, dropped, dismissDropped };
}
