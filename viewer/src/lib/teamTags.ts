/** TEAM-LEVEL TAGS on the draft board (2026-11-03).
 *
 * Anti-heal and auras are jobs a team does once: "Healing Reduction does not
 * stack with other similar effects", and a second copy of an aura gives the
 * same buff to the same allies. The static builds cannot see teammates, so the
 * pipeline scaled each mode's bonus for those tags by an EXPECTED share
 * (`team_tags` in data/_weights.yaml):
 *
 *     share = 1/N + (N - 1)/N x duplicate_value
 *
 * The draft can see them. This replaces that expectation with what the board
 * actually holds, per tag:
 *
 *   - a known teammate's build already carries it   -> worth duplicate_value
 *   - nobody known carries it, u seats still empty  -> 1/(u+1) + u/(u+1) x r
 *     (the same expectation over the seats still unknown; 1 when u = 0)
 *
 * and returns the DIFFERENCE from what the static build was given, times the
 * mode's unscaled bonus. On an empty board every seat is unknown, the value is
 * the static share, and every delta is 0 — the board shows the pipeline's
 * core exactly (archetypeParity.test.ts).
 *
 * "Teammates" excludes you: slot 0 is the build being adapted, and your own
 * second copy is `self_covered`'s job in `adaptFromCore`, not this one's. */

export interface TeamModeConfig {
  team_size: number | null;
  share: number;
  /** Each team tag's UNSCALED mode bonus. */
  bonus: Record<string, number>;
}

export interface TeamConfig {
  tags: string[];
  duplicate_value: number;
  modes: Record<string, TeamModeConfig>;
}

/** The value of YOUR copy of a team tag, given what the known teammates hold. */
export function teamValue(heldByTeammate: boolean, unknownSeats: number, duplicateValue: number) {
  if (heldByTeammate) return duplicateValue;
  const u = Math.max(0, unknownSeats);
  return 1 / (u + 1) + (u / (u + 1)) * duplicateValue;
}

/** `{tag: delta}` to add to every item carrying that tag, for this board. */
export function teamOverlay(
  cfg: TeamConfig | undefined,
  modeLabel: string,
  teammates: (string | null | undefined)[],
  teammateTags: Record<string, string[]>,
): Record<string, number> {
  const out: Record<string, number> = {};
  const m = cfg?.modes?.[modeLabel];
  if (!cfg || !m || !m.team_size) return out;
  const known = teammates.filter((n): n is string => !!n);
  const unknown = m.team_size - 1 - known.length;
  for (const tag of cfg.tags) {
    const b = m.bonus?.[tag];
    if (!b) continue;
    const held = known.some((n) => (teammateTags[n] ?? []).includes(tag));
    const delta = b * (teamValue(held, unknown, cfg.duplicate_value) - m.share);
    if (Math.abs(delta) > 1e-9) out[tag] = delta;
  }
  return out;
}
