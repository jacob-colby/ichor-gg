/** Recent queries, newest first, in this browser only.
 *
 * Every read and write is wrapped: private mode, blocked storage and a quota
 * error all degrade to "no recents", never to a broken landing page. */
const KEY = "ichor:recent-queries";
export const MAX_RECENTS = 6;

export function readRecents(): string[] {
  try {
    const raw = JSON.parse(localStorage.getItem(KEY) ?? "[]");
    return Array.isArray(raw) ? raw.filter((x): x is string => typeof x === "string").slice(0, MAX_RECENTS) : [];
  } catch {
    return [];
  }
}

/** Put `text` first; a query already in the list moves up rather than repeating. */
export function pushRecent(text: string, list: string[] = readRecents()): string[] {
  const t = text.trim();
  if (!t) return list;
  const next = [t, ...list.filter((x) => x.toLowerCase() !== t.toLowerCase())].slice(0, MAX_RECENTS);
  try { localStorage.setItem(KEY, JSON.stringify(next)); } catch { /* storage unavailable */ }
  return next;
}

export function clearRecents(): void {
  try { localStorage.removeItem(KEY); } catch { /* storage unavailable */ }
}
