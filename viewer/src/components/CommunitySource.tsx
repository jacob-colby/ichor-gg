/** Where the community figures came from, stated wherever they're compared.
 *
 * "The community" is not one thing: an Obsidian+ win rate and a Deity one
 * describe different populations, and a fortnight's window means something
 * different the week a patch lands. The numbers were being presented as
 * settled fact with none of that attached, so this says it in the open.
 *
 * Renders nothing at all when the index predates the scrape that supplies it —
 * an empty provenance line would be worse than none.
 */
import type { CommunitySource as Source } from "../types";

/** The source's own division keys, in its own words. */
const DIVISION_LABEL: Record<string, string> = {
  obsidian: "Obsidian+",
  master: "Master+",
  deity: "Demigod/Deity",
};

/** "2026-07-14" → "14 Jul". Parsed as parts rather than through `Date`, which
 *  would shift the day backwards for anyone west of UTC. */
function shortDate(iso?: string | null): string | null {
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(iso ?? "");
  if (!m) return null;
  const month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][Number(m[2]) - 1];
  return month ? `${Number(m[3])} ${month}` : null;
}

export function CommunitySource({ source, className = "" }: {
  source?: Source;
  className?: string;
}) {
  if (!source?.division) return null;
  const division = DIVISION_LABEL[source.division] ?? source.division;
  const from = shortDate(source.window_start);
  const to = shortDate(source.window_end);
  const matches = source.matches_analyzed;

  return (
    <p data-testid="community-source" className={`text-label leading-relaxed text-faint ${className}`}>
      Community figures:{" "}
      {typeof matches === "number" && (
        <><span className="font-mono text-muted">{matches.toLocaleString("en-US")}</span>{" "}</>
      )}
      <span className="text-ink-soft">{division}</span> Conquest matches
      {from && to && <> · <span className="font-mono">{from}–{to}</span></>}
    </p>
  );
}
