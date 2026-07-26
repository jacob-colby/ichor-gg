/** Filter state that lives in the address bar.
 *
 * Every filtering surface in this app kept its filters in `useState`, which
 * meant a filtered view could not be linked, bookmarked, or reloaded — you
 * could send someone "the tier list" but never "the Mid gods the meta and the
 * model disagree about". The draft page already proved the pattern works
 * (`#/draft?m=…&me=…`); this generalizes it.
 *
 * Writes use `replaceState`, never `pushState`: filters change on every
 * keystroke, and a Back button that walks a search box backwards one character
 * at a time is worse than no history at all.
 */
import { useCallback, useEffect, useRef, useState } from "react";

/** The path part of a hash, with its query string removed. */
export function hashPath(hash: string): string {
  return hash.split("?")[0] || "#/";
}

/** The query part of a hash. Empty params for a hash that carries none. */
export function hashQuery(hash: string): URLSearchParams {
  return new URLSearchParams(hash.split("?")[1] ?? "");
}

/** Serialize non-empty fields, in the order given, as `?a=1&b=2` — or "" when
 *  every field is at its default. Stable ordering matters: the hook compares
 *  encoded strings to decide whether the URL actually changed. */
export function queryString(fields: Record<string, string | undefined>): string {
  const params = new URLSearchParams();
  for (const [k, v] of Object.entries(fields)) if (v) params.set(k, v);
  const s = params.toString();
  return s ? `?${s}` : "";
}

/** `path` carrying whatever query the address bar holds right now.
 *
 * Navigating *within* a filtered view — picking another god from a filtered
 * sidebar, opening an item from a filtered shelf — must not silently clear the
 * filters that produced the thing you clicked. */
export function keepQuery(path: string, hash?: string): string {
  // A queued write must land before the address bar is read, or a click within
  // the debounce window composes its destination from a stale query.
  flushQuery();
  const current = (hash ?? (typeof window === "undefined" ? "" : window.location.hash)).split("?")[1];
  return current ? `${hashPath(path)}?${current}` : hashPath(path);
}

/* ── Writing ──────────────────────────────────────────────────────────────
 * Browsers rate-limit history writes: Safari throws above 100 `replaceState`
 * calls per 30s, Firefox silently drops them above 50 per 10s. A search box
 * bound straight to the URL writes once per keystroke, and holding backspace
 * on a long query clears that bar in about three seconds. So the write is
 * queued rather than immediate — while React state stays synchronous, so the
 * UI never lags the input.
 */
const WRITE_DELAY_MS = 150;
let pending: { query: string; timer: ReturnType<typeof setTimeout> } | null = null;
/** The query string the address bar is known to hold — what we last wrote, or
 *  what it arrived with. Queueing the write opens a window where the URL is
 *  behind the state, and a `hashchange` landing inside it needs to be told
 *  apart from a real navigation; this is the difference. */
let inUrl = "";

/** The live query, as `?a=1` or "". */
function urlQuery(): string {
  if (typeof window === "undefined") return "";
  const raw = window.location.hash.split("?")[1];
  return raw ? `?${raw}` : "";
}

function commitQuery(query: string): void {
  if (typeof window === "undefined") return;
  const { pathname, search, hash } = window.location;
  window.history.replaceState(null, "", `${pathname}${search}${hashPath(hash)}${query}`);
  inUrl = query;
}

/** Write any queued query immediately. Safe to call when nothing is queued. */
export function flushQuery(): void {
  if (!pending) return;
  const { query, timer } = pending;
  clearTimeout(timer);
  pending = null;
  commitQuery(query);
}

/** Drop a queued write — the URL has moved on and it is no longer wanted. */
function cancelQuery(): void {
  if (!pending) return;
  clearTimeout(pending.timer);
  pending = null;
}

function scheduleQuery(query: string): void {
  if (typeof window === "undefined") return;
  if (pending) clearTimeout(pending.timer);
  pending = { query, timer: setTimeout(flushQuery, WRITE_DELAY_MS) };
}

// A reload or a tab close mid-debounce would otherwise lose the last edit.
if (typeof window !== "undefined") window.addEventListener("pagehide", flushQuery);

/**
 * Surface filter state, mirrored into the hash query string.
 *
 * `decode` reads params into state; `encode` writes state back to params,
 * returning `undefined` for anything at its default so a pristine view keeps a
 * clean URL. Both must round-trip — the hook compares `encode` output to decide
 * whether an incoming `hashchange` (Back, a pasted link) actually differs.
 */
export function useUrlState<T>(
  decode: (params: URLSearchParams) => T,
  encode: (state: T) => Record<string, string | undefined>,
): [T, (next: T | ((prev: T) => T)) => void] {
  const [state, setInternal] = useState<T>(() => {
    // The URL this view opened at is the baseline every later `hashchange` is
    // judged against.
    inUrl = urlQuery();
    return decode(hashQuery(typeof window === "undefined" ? "" : window.location.hash));
  });

  // `encode` and the live state are read inside a listener registered once;
  // refs keep that listener from closing over a stale render.
  const stateRef = useRef(state);
  stateRef.current = state;
  const encodeRef = useRef(encode);
  encodeRef.current = encode;
  const decodeRef = useRef(decode);
  decodeRef.current = decode;

  const setState = useCallback((next: T | ((prev: T) => T)) => {
    setInternal((prev) => {
      const value = typeof next === "function" ? (next as (p: T) => T)(prev) : next;
      scheduleQuery(queryString(encodeRef.current(value)));
      return value;
    });
  }, []);

  // Leaving the view must not strand the last edit in the queue.
  useEffect(() => flushQuery, []);

  useEffect(() => {
    if (typeof window === "undefined") return;
    const sync = () => {
      // A queued write leaves the URL a step behind the state. An event that
      // arrives showing the *old* query is the address bar catching up on a
      // path change, not someone navigating — adopting it would discard the
      // edit still sitting in the queue. Anything else is a real navigation
      // (Back, a pasted link), and it supersedes the queued write.
      if (pending && urlQuery() === inUrl) return;
      cancelQuery();

      const incoming = decodeRef.current(hashQuery(window.location.hash));
      inUrl = urlQuery();
      // Our own `replaceState` doesn't fire `hashchange`, but a path change
      // within the view does — and it carries the same query, which must not
      // be treated as a reset.
      if (queryString(encodeRef.current(incoming)) === queryString(encodeRef.current(stateRef.current))) return;
      setInternal(incoming);
    };
    window.addEventListener("hashchange", sync);
    return () => window.removeEventListener("hashchange", sync);
  }, []);

  return [state, setState];
}
