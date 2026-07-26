/** Human-friendly age of a `YYYY-MM-DD` stamp, for the data-freshness line.
 *
 * "Updated 2 days ago" reads better than a bare date, but the exact date still
 * matters when you're checking whether a patch landed — so callers pair this
 * with the raw string in a `title`. Day-granularity only; the pipeline stamps
 * dates, not times.
 */
export function relativeDate(iso: string, now: Date = new Date()): string {
  if (!iso) return "";
  const then = new Date(`${iso}T00:00:00`);
  if (Number.isNaN(then.getTime())) return iso;

  const startOfDay = (d: Date) => new Date(d.getFullYear(), d.getMonth(), d.getDate());
  const days = Math.round(
    (startOfDay(now).getTime() - startOfDay(then).getTime()) / 86_400_000,
  );

  if (days < 0) return iso;           // clock skew — don't claim "in 3 days"
  if (days === 0) return "today";
  if (days === 1) return "yesterday";
  if (days < 7) return `${days} days ago`;
  if (days < 14) return "last week";
  if (days < 60) return `${Math.floor(days / 7)} weeks ago`;
  const months = Math.floor(days / 30);
  return months === 1 ? "last month" : `${months} months ago`;
}
