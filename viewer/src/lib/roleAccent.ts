import type { God } from "../types";

// The scraped `role` field is lane-based (Solo / Jungle / Mid / Carry / Support,
// plus combos like "Solo Jungle"). Map each lane to a design role-accent token.
// Class strings are literal so Tailwind's JIT keeps them.
export const LANES = ["Solo", "Jungle", "Mid", "Carry", "Support"] as const;
export type Lane = (typeof LANES)[number];

const LANE_TEXT: Record<Lane, string> = {
  Solo: "text-role-warrior",
  Jungle: "text-role-assassin",
  Mid: "text-role-mid",
  Carry: "text-role-hunter",
  Support: "text-role-guardian",
};
const LANE_BORDER: Record<Lane, string> = {
  Solo: "border-role-warrior",
  Jungle: "border-role-assassin",
  Mid: "border-role-mid",
  Carry: "border-role-hunter",
  Support: "border-role-guardian",
};

/** The primary lane of a god (first lane token in its role string). */
export function godLane(role: string | undefined): Lane | undefined {
  if (!role) return undefined;
  return LANES.find((l) => role.split(/\s+/).includes(l));
}

/** True if a god belongs to `lane` (its role string contains that lane token). */
export function godInLane(role: string | undefined, lane: Lane): boolean {
  return !!role && role.split(/\s+/).includes(lane);
}

export function laneTextClass(lane: Lane | undefined): string {
  return lane ? LANE_TEXT[lane] : "text-muted";
}
export function laneBorderClass(lane: Lane | undefined): string {
  return lane ? LANE_BORDER[lane] : "border-line";
}

export function godRoleTextClass(god: God): string {
  return laneTextClass(godLane(god.role));
}

/** Damage-type accent text class. */
export function damageTextClass(dmg: string | undefined): string {
  return dmg === "magical" ? "text-dmg-magical" : dmg === "physical" ? "text-dmg-physical" : "text-muted";
}
