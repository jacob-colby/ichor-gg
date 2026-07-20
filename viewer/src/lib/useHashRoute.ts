import { useEffect, useState } from "react";

export interface Route {
  view: "builds" | "items";
  god?: string;
  tab: "builds" | "info";
  item?: string;
}

export function parseHash(hash: string): Route {
  const parts = hash.replace(/^#\/?/, "").split("/").filter(Boolean).map(decodeURIComponent);
  if (parts[0] === "items") {
    return { view: "items", tab: "builds", ...(parts[1] ? { item: parts[1] } : {}) };
  }
  if (parts[0] === "god" && parts[1]) {
    return { view: "builds", god: parts[1], tab: parts[2] === "info" ? "info" : "builds" };
  }
  return { view: "builds", tab: "builds" };
}

export const toHash = {
  home: () => "#/",
  god: (n: string) => `#/god/${encodeURIComponent(n)}`,
  godInfo: (n: string) => `#/god/${encodeURIComponent(n)}/info`,
  items: () => "#/items",
  item: (n: string) => `#/items/${encodeURIComponent(n)}`,
};

export function navigate(hash: string): void {
  window.location.hash = hash;
}

export function useHashRoute(): Route {
  const [route, setRoute] = useState<Route>(() => parseHash(window.location.hash));
  useEffect(() => {
    const on = () => setRoute(parseHash(window.location.hash));
    window.addEventListener("hashchange", on);
    return () => window.removeEventListener("hashchange", on);
  }, []);
  return route;
}
