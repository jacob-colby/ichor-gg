/** The community's build on the god page: what the "Community" side of the
 *  whose-build switch shows, in every mode.
 *
 * WHICH SIX. The six the head-to-head measured: `/side_by_side/<god>.json`'s
 * `community.items`. That is the Conquest record CLEANED by the pipeline's one
 * rule (`community_target.comparison_six`): its slots in bought order, with any
 * slot that isn't a distinct finished item (a tier-2 component, a statless
 * relic, a duplicate) refilled by the record's next finished pick. It is not
 * the raw `slot_order` in the index. On 2026-11-09 data that list differs from
 * the measured six on 79 of 95 gods, nearly always by a component or a relic
 * in slot 5 or 6. Showing the raw list would put a 1,000-gold component in
 * "the community's six" while the verdict above it quotes a different six.
 * With no comparison file there is no community six to show, and the page
 * says so instead of falling back to the raw list.
 *
 * OTHER MODES. SmiteBrain publishes Conquest only, so Joust and Arena show
 * Conquest's six, labelled as Conquest's. Items whose Conquest record doesn't
 * describe them in that mode are flagged by the rule the most-picked list
 * already uses (`mostPicked.transferFlags`).
 *
 * THE ASPECT. This six is every player of the god, on any aspect: SmiteBrain's
 * aggregates ignore `aspect=`. So it is never shown as an aspect's build. With
 * the aspect on, the Community side hands its whole build area (starter,
 * relic and six) to one slot in GodPage.tsx, `data-testid=
 * "community-aspect-slot"`, which draws the god's per-aspect record from the
 * SmiteBrain match records (`AspectCommunity`, `pipeline/smite/
 * aspect_matches.py`). When that record has no build to show, the slot says
 * why and points at the any-aspect six (`anyAspectLine`).
 *
 * Pure. Tested in communityBuild.test.ts.
 */
import type { SideBySideData } from "../SideBySide";
import type { Mode } from "./verdict";

export interface CommunitySix {
  items: string[];
  /** "Conquest" when the six is borrowed into Joust or Arena, else null. */
  borrowedFrom: string | null;
  /** Record slots the cleaning rule refilled, in slot order. */
  refilled: { dropped: string; used: string }[];
}

export function communitySix({ comparison, mode }: {
  /** The god's Conquest comparison file, or null when it has none. */
  comparison: SideBySideData | null;
  mode: Mode;
}): CommunitySix | null {
  const items = comparison?.community?.items ?? [];
  if (!items.length) return null;
  const refilled = (comparison?.substitutions ?? [])
    .filter((s): s is { dropped: string; used: string } => !!s.used && !!s.dropped)
    .map(({ dropped, used }) => ({ dropped, used }));
  return { items, borrowedFrom: mode === "conquest" ? null : "Conquest", refilled };
}

/** The lines under the switch on the Community side: what this six is, in
 *  words, one sentence per fact. */
export function communityLines(c: CommunitySix, god: string): string[] {
  const lines = [`What ${god}'s ${c.borrowedFrom ?? "Conquest"} players buy most in each slot.`];
  if (c.refilled.length) {
    lines.push(`Where the record's slot isn't a finished item, its next finished pick fills in: ${
      c.refilled.map((r) => `${r.dropped} → ${r.used}`).join(", ")}.`);
  }
  return lines;
}

/** Where the any-aspect six is, when the aspect slot has no aspect build to
 *  show (below the minimum, no record, or a mode with no per-aspect record). */
export function anyAspectLine(god: string): string {
  return `Switch the aspect off to see what all ${god} players buy, on any aspect.`;
}
