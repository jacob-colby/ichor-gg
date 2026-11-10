/** Non-component state for the god page: what the URL query holds, which
 *  build is "the" build, and the aspect line. The god you were last on is the
 *  first of the recent gods (`command/recents.ts`), which the app records. */
import type { Mode } from "./verdict";
import type { Whose } from "./WhoseSwitch";

/** The god page's build — the one `/side_by_side` measures and the draft
 *  board opens on. Passed explicitly to `useDraftResult` (the lib default is
 *  `core`, and stays that way). */
export const MAIN_ARCHETYPE = "model";

export interface PageQuery {
  mode: Mode; aspect: boolean; build: string;
  /** Whose build is on screen. In the link, so a shared page opens on the
   *  side it was shared from; a bare god link opens on Ichor's, the same way
   *  it opens on Conquest. Switching mode keeps it. `build` is kept under
   *  Community too, so switching back returns to the focus you had. */
  whose: Whose;
  /** Enemies named by the link (`vs=Hecate,Ymir`), or null when the link
   *  names none — then the page shows whatever the shared draft holds. */
  vs: string[] | null;
}

/** `#/god/Ra?mode=joust&aspect=1&build=burst&whose=community&vs=Hecate,Ymir` — defaults leave a clean URL. */
export const decodePageQuery = (p: URLSearchParams): PageQuery => {
  const m = p.get("mode");
  return {
    mode: m === "joust" || m === "arena" ? m : "conquest",
    aspect: p.get("aspect") === "1",
    build: p.get("build") || MAIN_ARCHETYPE,
    whose: p.get("whose") === "community" ? "community" : "ichor",
    vs: p.get("vs") ? p.get("vs")!.split(",").map((s) => s.trim()).filter(Boolean) : null,
  };
};
export const encodePageQuery = (q: PageQuery) => ({
  mode: q.mode === "conquest" ? undefined : q.mode,
  aspect: q.aspect ? "1" : undefined,
  build: q.build === MAIN_ARCHETYPE ? undefined : q.build,
  whose: q.whose === "community" ? "community" : undefined,
  vs: q.vs?.length ? q.vs.join(",") : undefined,
});

/** The one line under the header when the aspect is on. */
export function aspectNote(aspect: string, changesBuild: boolean, god: string): string {
  return changesBuild
    ? `Built for ${aspect}. ${god}'s six changes with it.`
    : `${aspect} plays differently, but it doesn't change ${god}'s six — same build either way.`;
}
