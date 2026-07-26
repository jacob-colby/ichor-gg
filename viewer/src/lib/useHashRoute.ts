import { useEffect, useState } from "react";

export interface Route {
  view: "builds" | "items" | "home" | "draft" | "tiers" | "patch";
  god?: string;
  tab: "builds" | "info";
  item?: string;
}

export function parseHash(hash: string): Route {
  const parts = hash.replace(/^#\/?/, "").split("/").filter(Boolean).map(decodeURIComponent);
  if (parts[0] === "items") {
    return { view: "items", tab: "builds", ...(parts[1] ? { item: parts[1] } : {}) };
  }
  if (parts[0] === "gods") {
    // #/gods is retired — the god sidebar absorbed it. Land on home instead
    // of a dead view; useHashRoute additionally replaces the URL itself.
    return { view: "home", tab: "builds" };
  }
  if (parts[0] === "draft") {
    return { view: "draft", tab: "builds" };
  }
  if (parts[0] === "builds") {
    return { view: "builds", tab: "builds" };
  }
  if (parts[0] === "tiers") {
    return { view: "tiers", tab: "builds" };
  }
  if (parts[0] === "patch") {
    return { view: "patch", tab: "builds" };
  }
  if (parts[0] === "god" && parts[1]) {
    return { view: "builds", god: parts[1], tab: parts[2] === "info" ? "info" : "builds" };
  }
  return { view: "home", tab: "builds" };
}

export const toHash = {
  home: () => "#/",
  builds: () => "#/builds",
  draft: () => "#/draft",
  god: (n: string) => `#/god/${encodeURIComponent(n)}`,
  godInfo: (n: string) => `#/god/${encodeURIComponent(n)}/info`,
  items: () => "#/items",
  item: (n: string) => `#/items/${encodeURIComponent(n)}`,
  tiers: () => "#/tiers",
  patch: () => "#/patch",
};

export function navigate(hash: string): void {
  window.location.hash = hash;
}

export function useHashRoute(): Route {
  const [route, setRoute] = useState<Route>(() => parseHash(window.location.hash));
  useEffect(() => {
    const sync = () => {
      const hash = window.location.hash;
      const parts = hash.replace(/^#\/?/, "").split("/").filter(Boolean);
      if (parts[0] === "gods") {
        // Redirect the dead #/gods URL to home without leaving it in history.
        window.history.replaceState(null, "", window.location.pathname + window.location.search + toHash.home());
      }
      setRoute(parseHash(window.location.hash));
    };
    sync();
    window.addEventListener("hashchange", sync);
    return () => window.removeEventListener("hashchange", sync);
  }, []);
  return route;
}
