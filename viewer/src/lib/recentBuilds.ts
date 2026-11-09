/** The god page's "Recent builds": types and the one pure filter.
 *
 * Shipped by `pipeline/smite/recent_builds.py` as `/recent/<slug>.json`.
 * Newest first. `win` is the team's result, `master` is rank >= 4400, and
 * `aspect` is null for a match with no aspect equipped (a small sample: the
 * store is an aspect feed). Items are what the player held, not a buy order. */
export interface RecentBuild {
  t: string;
  win: boolean;
  role: string;
  master: boolean;
  aspect: string | null;
  patch: string | null;
  items: string[];
  starter: string | null;
  relic: string | null;
}

export interface RecentFile {
  god: string;
  kept: number;
  aspects: string[];
  patches: string[];
  roles: string[];
  builds: RecentBuild[];
}

export const ALL = "all";
export const NO_ASPECT = "none";

export interface RecentFilters {
  role: string;
  aspect: string;
  result: "all" | "win" | "loss";
  master: boolean;
  patch: string;
}

export const NO_FILTERS: RecentFilters = { role: ALL, aspect: ALL, result: "all", master: false, patch: ALL };

export function filterBuilds(builds: RecentBuild[], f: RecentFilters): RecentBuild[] {
  return builds.filter((b) =>
    (f.role === ALL || b.role === f.role) &&
    (f.aspect === ALL || (f.aspect === NO_ASPECT ? b.aspect === null : b.aspect === f.aspect)) &&
    (f.result === "all" || (f.result === "win") === b.win) &&
    (!f.master || b.master) &&
    (f.patch === ALL || b.patch === f.patch));
}

export const isFiltered = (f: RecentFilters) =>
  f.role !== ALL || f.aspect !== ALL || f.result !== "all" || f.master || f.patch !== ALL;

/** "today", "yesterday", "5d ago" — against an injected clock so a test can pin it. */
export function ago(iso: string, now: number = Date.now()): string {
  const days = Math.floor((now - Date.parse(iso)) / 86_400_000);
  if (!(days >= 0)) return "just now";
  return days === 0 ? "today" : days === 1 ? "yesterday" : `${days}d ago`;
}
