import type { Route } from "./useHashRoute";

export const SITE_NAME = "ichor";
export const SITE_TITLE = "ichor — SMITE 2 build recommender";

const VIEW_LABEL: Record<string, string> = {
  builds: "Builds",
  draft: "Draft",
  items: "Items",
  tiers: "Tier list",
  patch: "Patch notes",
};

/** Tab/History title for a route.
 *
 * These get pasted into Discord and sit in browser history, so a page about
 * one god should say so — "Agni — ichor" beats six identical entries reading
 * "ichor". Home keeps the full tagline since that's the shareable landing.
 */
export function documentTitle(route: Route, godName?: string): string {
  if (route.view === "home") return SITE_TITLE;
  if (route.view === "builds") {
    const god = godName ?? route.god;
    return god ? `${god} — ${SITE_NAME}` : `Builds — ${SITE_NAME}`;
  }
  if (route.view === "items" && route.item) return `${route.item} — ${SITE_NAME}`;
  const label = VIEW_LABEL[route.view];
  return label ? `${label} — ${SITE_NAME}` : SITE_TITLE;
}
