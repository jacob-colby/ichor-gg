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
    allyCovers,
    allyAllPhysical: allies.length > 0 && allies.every((g) => g.damage_type === "physical"),
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

  for (const [threat, map] of Object.entries(cfg.tag_bonus ?? {})) {
    const n = counts[threat] ?? 0;
    if (!n) continue;
    for (const [tag, w] of Object.entries(map)) {
      let mult = 1;
      if (t.allyCovers[tag]) mult += cfg.ally_covered; // covered -> damped
      else mult += cfg.ally_gap; // nobody covers -> raised
      tags[tag] = (tags[tag] ?? 0) + n * cfg.per_enemy * w * mult;
    }
  }
  for (const [threat, map] of Object.entries(cfg.stat_bonus ?? {})) {
    const n = counts[threat] ?? 0;
    if (!n) continue;
    for (const [stat, w] of Object.entries(map)) {
      stats[stat] = (stats[stat] ?? 0) + n * cfg.per_enemy * w;
    }
  }
  if (t.allyAllPhysical) {
    stats["Penetration"] = (stats["Penetration"] ?? 0) + cfg.per_enemy;
  }
  return { tags, stats };
}
