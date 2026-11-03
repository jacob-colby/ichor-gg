/** The one route this flow adds: the god list as its own tab.
 *
 *  `#/` is the match board now, so the roster needs a path of its own. It
 *  lives here rather than in lib/useHashRoute so the shared router (and every
 *  URL it keeps alive) is untouched: `#/roster` parses as the roster lens
 *  there, and the shell tells the two apart by path. `#/gods` stays retired. */
import { hashPath } from "../../lib/urlState";

export const ROSTER_HASH = "#/roster";

export function isRosterHash(hash: string): boolean {
  return hashPath(hash).replace(/\/$/, "") === ROSTER_HASH;
}
