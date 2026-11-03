/** Non-component state for the god page: what the URL query holds, which
 *  build is "the" build, the last god you opened, and the aspect line. */
import type { Mode } from "./verdict";

/** The god page's build — the one `/side_by_side` measures and the draft
 *  board opens on. Passed explicitly to `useDraftResult` (the lib default is
 *  `core`, and stays that way). */
export const MAIN_ARCHETYPE = "model";

export interface PageQuery { mode: Mode; aspect: boolean; build: string }

/** `#/god/Ra?mode=joust&aspect=1&build=burst` — defaults leave a clean URL. */
export const decodePageQuery = (p: URLSearchParams): PageQuery => {
  const m = p.get("mode");
  return {
    mode: m === "joust" || m === "arena" ? m : "conquest",
    aspect: p.get("aspect") === "1",
    build: p.get("build") || MAIN_ARCHETYPE,
  };
};
export const encodePageQuery = (q: PageQuery) => ({
  mode: q.mode === "conquest" ? undefined : q.mode,
  aspect: q.aspect ? "1" : undefined,
  build: q.build === MAIN_ARCHETYPE ? undefined : q.build,
});

const LAST_GOD_KEY = "ichor:last-god";
export function readLastGod(): string | null {
  try { return localStorage.getItem(LAST_GOD_KEY); } catch { return null; }
}
export function writeLastGod(name: string): void {
  try { localStorage.setItem(LAST_GOD_KEY, name); } catch { /* private mode */ }
}

/** The one line under the header when the aspect is on. */
export function aspectNote(aspect: string, changesBuild: boolean, god: string): string {
  return changesBuild
    ? `Built for ${aspect}. ${god}'s six changes with it.`
    : `${aspect} plays differently, but it doesn't change ${god}'s six — same build either way.`;
}
