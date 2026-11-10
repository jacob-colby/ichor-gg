/** Recent gods, newest first, in this browser only.
 *
 * One list, one meaning of "recent": the gods whose build page you opened,
 * by any route (a grid card, the command field, a pasted link, the draft
 * board). God select shows it as the "Recent" row, whose first card is the
 * god you were last on, and the top bar's empty field offers the same list.
 * A card opens the god's build exactly as its grid card does: no enemies,
 * mode or aspect ride along (Jacob, 2026-11-09).
 *
 * It replaces two stores: `ichor:recent-queries` (the typed queries the row
 * used to show, enemies and all) and `ichor:last-god` (the separate "Back to"
 * card). Until the new list is first written, it is read from those two —
 * the last god first, then each old query's own god — so a returning
 * visitor keeps their row; the first write retires them.
 *
 * Every read and write is wrapped: private mode, blocked storage and a quota
 * error all degrade to "no recents", never to a broken landing page. */
import { parseQuery, type GodLike } from "./query";

const KEY = "ichor:recent-gods";
const OLD_QUERIES = "ichor:recent-queries";
const OLD_LAST_GOD = "ichor:last-god";
export const MAX_RECENT_GODS = 8;

type Roster = GodLike[];

const strings = (raw: unknown): string[] =>
  Array.isArray(raw) ? raw.filter((x): x is string => typeof x === "string") : [];

/** The stored list, or null when it has never been written. */
function stored(): string[] | null {
  try {
    const raw = localStorage.getItem(KEY);
    return raw === null ? null : strings(JSON.parse(raw));
  } catch {
    return [];
  }
}

/** What the two retired stores said, newest first. */
function seed(gods: Roster): string[] {
  const out: string[] = [];
  try {
    const last = localStorage.getItem(OLD_LAST_GOD);
    if (last) out.push(last);
  } catch { /* storage unavailable */ }
  try {
    for (const text of strings(JSON.parse(localStorage.getItem(OLD_QUERIES) ?? "[]"))) {
      const you = parseQuery(text, gods).you;
      if (you) out.push(you);
    }
  } catch { /* storage unavailable, or not JSON */ }
  return out;
}

/** Known gods only (a renamed or dropped god leaves the row), once each, capped. */
function tidy(names: string[], gods: Roster): string[] {
  const known = new Set(gods.map((g) => g.name));
  return [...new Set(names)].filter((n) => known.has(n)).slice(0, MAX_RECENT_GODS);
}

function write(list: string[]): void {
  try {
    localStorage.setItem(KEY, JSON.stringify(list));
    localStorage.removeItem(OLD_QUERIES);
    localStorage.removeItem(OLD_LAST_GOD);
  } catch { /* storage unavailable */ }
}

export function readRecentGods(gods: Roster): string[] {
  return tidy(stored() ?? seed(gods), gods);
}

/** Put `name` first; a god already in the list moves up rather than repeating. */
export function pushRecentGod(name: string, gods: Roster): string[] {
  const next = tidy([name, ...readRecentGods(gods)], gods);
  write(next);
  return next;
}

/** Written as an empty list, not removed, so the retired stores never seed it again. */
export function clearRecentGods(): void {
  write([]);
}
