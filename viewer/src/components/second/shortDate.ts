/** "2026-07-14" → "14 Jul", from the string's own parts — never through
 *  `Date`, which shifts the day for anyone west of UTC. */
export function shortDate(iso?: string | null): string | null {
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(iso ?? "");
  if (!m) return null;
  const month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][Number(m[2]) - 1];
  return month ? `${Number(m[3])} ${month}` : null;
}
