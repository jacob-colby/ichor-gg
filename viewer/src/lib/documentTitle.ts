import type { Route } from "./useHashRoute";

export const SITE_NAME = "ichor";
export const SITE_TITLE = "ichor — SMITE 2 build recommender";

const ROSTER_LABEL: Record<string, string> = {
  tiers: "Tier list",
  items: "Items",
  draft: "Draft",
  patch: "Patch notes",
};

/** What each lens is called once it's scoped to one god. The god's name leads,
 *  because that is what the reader is looking at. */
const GOD_LABEL: Record<string, string> = {
  kit: "kit",
  items: "items",
  ranking: "ranking",
};

/** Tab/History title for a route.
 *
 * These get pasted into Discord and sit in browser history, so a page about one
 * god should say so — "Ra — ichor" beats six identical entries reading "ichor",
 * and now that a god has four lenses, "Ra’s items — ichor" beats four identical
 * "Ra" entries. The roster board keeps the full tagline; it's the landing.
 */
export function documentTitle(route: Route, godName?: string): string {
  const god = godName ?? route.god;
  if (god) {
    const label = GOD_LABEL[route.lens];
    return label ? `${god}’s ${label} — ${SITE_NAME}` : `${god} — ${SITE_NAME}`;
  }
  if (route.lens === "items" && route.item) return `${route.item} — ${SITE_NAME}`;
  const label = ROSTER_LABEL[route.lens];
  return label ? `${label} — ${SITE_NAME}` : SITE_TITLE;
}
