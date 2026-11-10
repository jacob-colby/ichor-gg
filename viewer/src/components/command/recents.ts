/** Recent gods, newest first, in this browser only.
 *
 * One list, one meaning of "recent": the gods whose build page you opened,
 * by any route (a grid card, the command field, a pasted link, the draft
 * board), each with the mode and aspect state you last viewed it in. God
 * select shows it as the "Recent" row, whose first card is the god you were
 * last on, and the top bar's empty field offers the same entries. A card
 * reopens the god in that mode with that aspect state; the enemies do not
 * ride along (Jacob, 2026-11-09). One entry per god: a newer visit moves the
 * god to the front and replaces its mode and aspect.
 *
 * It replaces two stores: `ichor:recent-queries` (the typed queries the row
 * used to show, enemies and all) and `ichor:last-god` (the separate "Back to"
 * card). Until the new list is first written, it is read from those two, so a
 * returning visitor keeps their row: the last god first, then each old
 * query's own god with the query's mode and aspect. The last god carries
 * neither, so it reads as Conquest with the aspect off, unless an old query
 * names it too. Then it takes that query's state, which is where its old card
 * linked. The first write retires both.
 *
 * Every read and write is wrapped: private mode, blocked storage and a quota
 * error all degrade to "no recents", never to a broken landing page. */
import { MODE_NAME, type Mode } from "../second/verdict";
import { parseQuery, queryHash, type GodLike, type ParsedQuery } from "./query";

const KEY = "ichor:recent-gods";
const OLD_QUERIES = "ichor:recent-queries";
const OLD_LAST_GOD = "ichor:last-god";
export const MAX_RECENT_GODS = 8;

export interface RecentGod { god: string; mode: Mode; aspect: boolean }

type Roster = GodLike[];
const MODES: readonly Mode[] = ["conquest", "joust", "arena"];

/** One stored entry, or null for anything that isn't one. */
function entry(x: unknown): RecentGod | null {
  if (typeof x === "string") return { god: x, mode: "conquest", aspect: false };
  if (!x || typeof x !== "object") return null;
  const { god, mode, aspect } = x as Record<string, unknown>;
  if (typeof god !== "string") return null;
  return { god, mode: MODES.includes(mode as Mode) ? (mode as Mode) : "conquest", aspect: aspect === true };
}
const entries = (raw: unknown): RecentGod[] =>
  Array.isArray(raw) ? raw.map(entry).filter((e): e is RecentGod => e !== null) : [];

/** The stored list, or null when it has never been written. */
function stored(): RecentGod[] | null {
  try {
    const raw = localStorage.getItem(KEY);
    return raw === null ? null : entries(JSON.parse(raw));
  } catch {
    return [];
  }
}

/** What the two retired stores said, newest first. */
function seed(gods: Roster): RecentGod[] {
  const fromQueries: RecentGod[] = [];
  try {
    const raw: unknown = JSON.parse(localStorage.getItem(OLD_QUERIES) ?? "[]");
    for (const text of Array.isArray(raw) ? raw : []) {
      if (typeof text !== "string") continue;
      const q = parseQuery(text, gods);
      if (q.you) fromQueries.push({ god: q.you, mode: q.mode ?? "conquest", aspect: q.aspect });
    }
  } catch { /* storage unavailable, or not JSON */ }
  let last: string | null = null;
  try { last = localStorage.getItem(OLD_LAST_GOD); } catch { /* storage unavailable */ }
  if (!last) return fromQueries;
  const asQueried = fromQueries.find((e) => e.god === last);
  return [asQueried ?? { god: last, mode: "conquest", aspect: false }, ...fromQueries];
}

/** Known gods only (a renamed or dropped god leaves the row), once each, capped. */
function tidy(list: RecentGod[], gods: Roster): RecentGod[] {
  const known = new Set(gods.map((g) => g.name));
  const out: RecentGod[] = [];
  for (const e of list) {
    if (out.length === MAX_RECENT_GODS) break;
    if (known.has(e.god) && !out.some((o) => o.god === e.god)) out.push(e);
  }
  return out;
}

function write(list: RecentGod[]): void {
  try {
    localStorage.setItem(KEY, JSON.stringify(list));
    localStorage.removeItem(OLD_QUERIES);
    localStorage.removeItem(OLD_LAST_GOD);
  } catch { /* storage unavailable */ }
}

export function readRecentGods(gods: Roster): RecentGod[] {
  return tidy(stored() ?? seed(gods), gods);
}

/** Put this view first. A god already in the list moves up and takes the
 *  newer mode and aspect, rather than repeating. */
export function pushRecentGod(view: RecentGod, gods: Roster): RecentGod[] {
  const next = tidy([view, ...readRecentGods(gods)], gods);
  write(next);
  return next;
}

/** Written as an empty list, not removed, so the retired stores never seed it again. */
export function clearRecentGods(): void {
  write([]);
}

/** The page a recent entry reopens: the god in that mode with that aspect
 *  state, no enemies, written by the app's one god-page hash helper so the
 *  defaults (Conquest, aspect off, Ichor's six) stay out of the URL. */
export const recentHash = (e: RecentGod): string => queryHash({ you: e.god, enemies: [], mode: e.mode, aspect: e.aspect });

/** The parsed query a recent entry submits, for the command field. */
export const recentQuery = (e: RecentGod): ParsedQuery =>
  ({ you: e.god, enemies: [], mode: e.mode, aspect: e.aspect, tokens: [], notes: [] });

/** The mode word a recent card prints under the name: none for Conquest. */
export const recentModeWord = (e: RecentGod): string | null => (e.mode === "conquest" ? null : MODE_NAME[e.mode]);
