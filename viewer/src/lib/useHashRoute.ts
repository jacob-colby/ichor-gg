/** Routing for the Subject Frame shell.
 *
 * The top level of this app is no longer "which tool" but **who you're looking
 * at** — the whole roster, or one god. A route is therefore a subject plus a
 * lens on it, and the six flat destinations become two honest levels.
 *
 * Every URL the old tool-first shell produced still resolves, because these
 * links get pasted into Discord and none of them may rot: `#/items/Rage`,
 * `#/god/Ra`, `#/god/Ra/info`, `#/tiers`, `#/draft`, `#/patch` all land where
 * they always did. Only `#/builds` changes meaning, and only because in a
 * subject-first shell "builds with no god" isn't a place — picking a god *is*
 * the navigation. It lands on the roster board.
 */
import { useEffect, useState } from "react";

/** Lenses on the whole roster. Draft belongs here rather than among a god's
 *  lenses: a draft takes ten gods and only one of them is your subject, so
 *  filing it under one god would misdescribe it. */
export type RosterLens = "board" | "tiers" | "items" | "draft" | "patch";

/** Lenses on a single god. */
export type GodLens = "builds" | "kit" | "items" | "ranking";

export type Lens = RosterLens | GodLens;

export const ROSTER_LENSES: RosterLens[] = ["board", "tiers", "items", "draft", "patch"];
export const GOD_LENSES: GodLens[] = ["builds", "kit", "items", "ranking"];

export interface Route {
  /** The subject. `undefined` is the whole roster — a first-class state, not a
   *  lobby: it keeps the divergence board and the page's one claim. */
  god?: string;
  lens: Lens;
  /** Item deep-link, on the roster's items lens only. */
  item?: string;
}

const ROSTER_PATHS: Record<string, RosterLens> = {
  tiers: "tiers",
  items: "items",
  draft: "draft",
  patch: "patch",
};

/** Legacy god tabs. `info` was the old name for the kit lens. */
const GOD_PATHS: Record<string, GodLens> = {
  info: "kit",
  kit: "kit",
  items: "items",
  ranking: "ranking",
};

export function parseHash(hash: string): Route {
  // Strip the query before matching path segments: filter state and the draft
  // page's shareable comp both live there, and routing stays query-agnostic.
  const [path] = hash.split("?");
  const parts = path.replace(/^#\/?/, "").split("/").filter(Boolean).map(decodeURIComponent);

  if (parts[0] === "god" && parts[1]) {
    return { god: parts[1], lens: GOD_PATHS[parts[2] ?? ""] ?? "builds" };
  }
  if (parts[0] === "items") {
    return { lens: "items", ...(parts[1] ? { item: parts[1] } : {}) };
  }
  const roster = ROSTER_PATHS[parts[0] ?? ""];
  if (roster) return { lens: roster };

  // `#/gods` and `#/builds` are both retired: the roster board is where you
  // now arrive, and the god picker is one control away.
  return { lens: "board" };
}

/** Paths that no longer exist and are rewritten out of history on arrival. */
export function isRetiredPath(hash: string): boolean {
  const first = hash.split("?")[0].replace(/^#\/?/, "").split("/").filter(Boolean)[0];
  return first === "gods" || first === "builds";
}

export const toHash = {
  home: () => "#/",
  /** Retained so old callers and bookmarks keep resolving. */
  builds: () => "#/",
  draft: () => "#/draft",
  god: (n: string) => `#/god/${encodeURIComponent(n)}`,
  godKit: (n: string) => `#/god/${encodeURIComponent(n)}/kit`,
  /** The old name for the kit lens; still produced by nothing, still parsed. */
  godInfo: (n: string) => `#/god/${encodeURIComponent(n)}/kit`,
  godItems: (n: string) => `#/god/${encodeURIComponent(n)}/items`,
  godRanking: (n: string) => `#/god/${encodeURIComponent(n)}/ranking`,
  items: () => "#/items",
  item: (n: string) => `#/items/${encodeURIComponent(n)}`,
  tiers: () => "#/tiers",
  patch: () => "#/patch",
};

/** The hash for a lens, given the subject currently in view. */
export function lensHash(lens: Lens, god?: string): string {
  if (!god) {
    return { board: toHash.home(), tiers: toHash.tiers(), items: toHash.items(),
      draft: toHash.draft(), patch: toHash.patch() }[lens as RosterLens] ?? toHash.home();
  }
  return { builds: toHash.god(god), kit: toHash.godKit(god),
    items: toHash.godItems(god), ranking: toHash.godRanking(god) }[lens as GodLens]
    ?? toHash.god(god);
}

export function navigate(hash: string): void {
  window.location.hash = hash;
}

export function useHashRoute(): Route {
  const [route, setRoute] = useState<Route>(() => parseHash(window.location.hash));
  useEffect(() => {
    const sync = () => {
      if (isRetiredPath(window.location.hash)) {
        // Rewrite rather than push, so Back doesn't bounce off a dead URL.
        window.history.replaceState(
          null, "", window.location.pathname + window.location.search + toHash.home());
      }
      setRoute(parseHash(window.location.hash));
    };
    sync();
    window.addEventListener("hashchange", sync);
    return () => window.removeEventListener("hashchange", sync);
  }, []);
  return route;
}
