/** Human-friendly age of a `YYYY-MM-DD` stamp, for the data-freshness line.
 *
 * "Updated 2 days ago" reads better than a bare date, but the exact date still
 * matters when you're checking whether a patch landed — so callers pair this
 * with the raw string in a `title`. Day-granularity only; the pipeline stamps
 * dates, not times.
 */
export function relativeDate(iso: string, now: Date = new Date()): string {
  if (!iso) return "";
  const days = daysAgo(iso, now);
  if (days === null) return iso;

  if (days < 0) return iso;           // clock skew — don't claim "in 3 days"
  if (days === 0) return "today";
  if (days === 1) return "yesterday";
  if (days < 7) return `${days} days ago`;
  if (days < 14) return "last week";
  if (days < 60) return `${Math.floor(days / 7)} weeks ago`;
  const months = Math.floor(days / 30);
  return months === 1 ? "last month" : `${months} months ago`;
}

/** The same age in the header stamp's few characters: "today", "1d", "3w",
 *  "2mo". Null for a future stamp (clock skew) or an unreadable one, so the
 *  caller drops the age rather than printing a wrong one. */
export function shortAge(iso: string, now: Date = new Date()): string | null {
  const days = iso ? daysAgo(iso, now) : null;
  if (days === null || days < 0) return null;
  if (days === 0) return "today";
  if (days < 14) return `${days}d`;
  if (days < 60) return `${Math.floor(days / 7)}w`;
  return `${Math.floor(days / 30)}mo`;
}

/** Whole local days from `iso` to `now`; null when `iso` is not a date. */
function daysAgo(iso: string, now: Date): number | null {
  const then = new Date(`${iso}T00:00:00`);
  if (Number.isNaN(then.getTime())) return null;
  const startOfDay = (d: Date) => new Date(d.getFullYear(), d.getMonth(), d.getDate());
  return Math.round((startOfDay(now).getTime() - startOfDay(then).getTime()) / 86_400_000);
}
