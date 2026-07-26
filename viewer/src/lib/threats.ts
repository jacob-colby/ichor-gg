import type { God, DraftComp, ThreatModel, DraftConfig } from "../types";

const HEAL = ["Healing", "Sustain"];
const LOCK = ["Lockdown", "Crowd Control", "Area Control"];
const CRIT = ["Carry", "Sharpshooter"];
const TANK = ["Tank"];

const hasSpec = (g: God | undefined, list: string[]) =>
  !!g && (g.specializations ?? []).some((s) => list.includes(s));

/** Comps -> a graded threat model. `allyCores` maps an ally god name to the
 *  effect_tags its own suggested core brings (what that teammate likely covers). */
export function deriveThreats(
  comp: DraftComp,
  godsByName: Record<string, God>,
  allyCores: Record<string, string[]>,
): ThreatModel {
  const enemies = comp.enemies.map((n) => godsByName[n]).filter(Boolean);
  const allies = comp.allies.map((n) => godsByName[n]).filter(Boolean);
  const allyCovers: Record<string, boolean> = {};
  for (const name of comp.allies) {
    for (const tag of allyCores[name] ?? []) allyCovers[tag] = true;
  }
  return {
    magical: enemies.filter((g) => g.damage_type === "magical").length,
    physical: enemies.filter((g) => g.damage_type === "physical").length,
    healers: enemies.filter((g) => hasSpec(g, HEAL)).length,
    lockdown: enemies.filter((g) => hasSpec(g, LOCK)).length,
    crit: enemies.filter((g) => hasSpec(g, CRIT)).length,
    tanks: enemies.filter((g) => hasSpec(g, TANK)).length,
    enemyCount: enemies.length,
    // The slot count for this mode, not how many are filled in — see the note
    // on ThreatModel.rosterSize.
    rosterSize: comp.enemies.length,
    allyCovers,
    // Two known allies minimum: "every ally is physical" is technically true
    // of a lone entered god, but it isn't a team composition, and treating it
    // as one had the board reporting moved items before any enemy existed.
    allyAllPhysical: allies.length >= 2 && allies.every((g) => g.damage_type === "physical"),
    allyCount: allies.length,
    allyPhysical: allies.filter((g) => g.damage_type === "physical").length,
  };
}

export type ThreatKey = "magical" | "physical" | "healers" | "lockdown" | "crit" | "tanks";

/** Which enemies actually triggered each threat. A chip reading "2/5 healers"
 * says nothing actionable; "healers 2/5 · Aphrodite, Hel" names the reason the
 * build changed. */
export function threatCulprits(
  comp: DraftComp,
  godsByName: Record<string, God>,
): Record<ThreatKey, string[]> {
  const enemies = comp.enemies.map((n) => godsByName[n]).filter(Boolean);
  const named = (pred: (g: God) => boolean) => enemies.filter(pred).map((g) => g.name);
  return {
    magical: named((g) => g.damage_type === "magical"),
    physical: named((g) => g.damage_type === "physical"),
    healers: named((g) => hasSpec(g, HEAL)),
    lockdown: named((g) => hasSpec(g, LOCK)),
    crit: named((g) => hasSpec(g, CRIT)),
    tanks: named((g) => hasSpec(g, TANK)),
  };
}

/** Threat model -> {tags, stats} bonus overlay (pre-clamp; the clamp is applied
 *  per item in draftBuild, since it bounds an item's TOTAL bonus). */
export function threatOverlay(t: ThreatModel, cfg: DraftConfig) {
  const tags: Record<string, number> = {};
  const stats: Record<string, number> = {};
  const counts: Record<string, number> = {
    healers: t.healers, lockdown: t.lockdown, crit: t.crit, tanks: t.tanks,
    magical: t.magical, physical: t.physical,
  };

  // Share of the enemy *roster*, not of the enemies entered so far — 2 of 3
  // (Joust) is a bigger threat than 2 of 5 (Conquest), and 1 known healer out
  // of 5 slots is a 20% signal, not a 100% one. Dividing by the entered count
  // made a one-enemy draft drive a maximal overlay, then grow *calmer* as more
  // enemies were added, which reads as the model flip-flopping. Guarded
  // against div-by-zero.
  const denom = t.rosterSize > 0 ? t.rosterSize : t.enemyCount;
  const share = denom > 0 ? (n: number) => n / denom : () => 0;

  for (const [threat, map] of Object.entries(cfg.tag_bonus ?? {})) {
    const n = counts[threat] ?? 0;
    if (!n) continue;
    for (const [tag, w] of Object.entries(map)) {
      let mult = 1;
      if (t.allyCovers[tag]) mult += cfg.ally_covered; // covered -> damped
      else mult += cfg.ally_gap; // nobody covers -> raised
      tags[tag] = (tags[tag] ?? 0) + share(n) * cfg.per_share * w * mult;
    }
  }
  for (const [threat, map] of Object.entries(cfg.stat_bonus ?? {})) {
    const n = counts[threat] ?? 0;
    if (!n) continue;
    for (const [stat, w] of Object.entries(map)) {
      stats[stat] = (stats[stat] ?? 0) + share(n) * cfg.per_share * w;
    }
  }
  // An all-physical team wants penetration — but scaled by how much of the
  // team we can actually see. Applied flat, this fired the moment a single
  // physical god filled the "you" slot, so a board with no enemies at all
  // reported four items "moved by your draft".
  if (t.allyAllPhysical && t.allyCount > 0) {
    stats["Penetration"] = (stats["Penetration"] ?? 0) + share(t.allyCount) * cfg.per_share;
  }
  return { tags, stats };
}
