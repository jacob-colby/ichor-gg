import type { God, DraftComp, ThreatModel, DraftConfig } from "../types";
import type { Overlay } from "./draftBuild";

const HEAL = ["Healing", "Sustain"];
const LOCK = ["Lockdown", "Crowd Control", "Area Control"];
const CRIT = ["Carry", "Sharpshooter"];
const TANK = ["Tank"];

const hasSpec = (g: God | undefined, list: string[]) =>
  !!g && (g.specializations ?? []).some((s) => list.includes(s));

/* The role label and the measured kit are two independent, complementary
 * pieces of evidence, so a threat is the UNION of them rather than a choice
 * between them.
 *
 * Neither alone works. The label is precise and badly incomplete: `Healing` is
 * on 9 of 89 gods, while Chaac, Kali, Sun Wukong, Hercules and Thanatos all
 * heal off their kit without it — exactly the gap STATE.md §5 recorded as "a
 * god who is situationally a healer without the Healing label is not counted".
 * The measurement alone is worse in the other direction: counting any god with
 * one healing ability catches all 9 labelled healers and adds 33 more, most of
 * them incidental (a small heal on a leap is not a healing comp).
 *
 * At a threshold of two healing abilities the count catches only 4 of the 9 —
 * it misses Aphrodite, whose single heal is her entire identity. So: label OR
 * two-plus abilities. 18 of 89 gods, against 9 before.
 *
 * Same shape for lockdown, where the labels were already broad (40 gods) and
 * three-plus hard-CC abilities adds 8 more the labels missed. */
const HEAL_ABILITIES = 2;
const CC_ABILITIES = 3;

const healsHard = (g: God | undefined) =>
  hasSpec(g, HEAL) || (g?.threat_kit?.heal ?? 0) >= HEAL_ABILITIES;
const locksDown = (g: God | undefined) =>
  hasSpec(g, LOCK) || (g?.threat_kit?.hard_cc ?? 0) >= CC_ABILITIES;
const makesWalls = (g: God | undefined) => (g?.threat_kit?.wall ?? 0) > 0;

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
    healers: enemies.filter(healsHard).length,
    lockdown: enemies.filter(locksDown).length,
    walls: enemies.filter(makesWalls).length,
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

export type ThreatKey = "magical" | "physical" | "healers" | "lockdown" | "crit" | "tanks" | "walls";

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
    healers: named(healsHard),
    lockdown: named(locksDown),
    walls: named(makesWalls),
    crit: named((g) => hasSpec(g, CRIT)),
    tanks: named((g) => hasSpec(g, TANK)),
  };
}

/** Threat model -> {tags, stats} bonus overlay (pre-clamp; the clamp is applied
 *  per item in draftBuild, since it bounds an item's TOTAL bonus). */
export function threatOverlay(t: ThreatModel, cfg: DraftConfig): Overlay {
  const tags: Record<string, number> = {};
  const stats: Record<string, number> = {};
  const counts: Record<string, number> = {
    healers: t.healers, lockdown: t.lockdown, crit: t.crit, tanks: t.tanks,
    magical: t.magical, physical: t.physical, walls: t.walls,
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


/** B6: per-item bonus from the damage model, given how tanky the enemy is.
 *
 * The tag and stat channels can only express "penetration is good against
 * tanks", which is the hand-tuned rule this sits beside. The measurement is
 * sharper than that and disagrees with it in a specific way: against a
 * three-item tank, PERCENT penetration rises (Obsidian Shard, Titan's Bane)
 * while FLAT penetration falls (Spear of Desolation), because a flat subtraction
 * is worth proportionally less the more protection there is. A per-stat rule
 * rewards both equally and is therefore wrong for half of them.
 *
 * `table` holds each item's normalised damage against a squishy and against a
 * tank, on separate scales — so the difference between the two columns is the
 * relative shift, which is exactly what a comp should move. Interpolating by
 * the enemy's tank share and taking the delta from the neutral case gives a
 * bonus that is zero for an unknown comp and grows only as real tanks appear.
 */
export function damageOverlay(
  t: ThreatModel,
  table: Record<string, [number, number]> | undefined,
  cfg: DraftConfig,
): Record<string, number> {
  if (!table) return {};
  const denom = t.rosterSize > 0 ? t.rosterSize : t.enemyCount;
  if (denom <= 0) return {};
  const tankShare = t.tanks / denom;
  if (tankShare <= 0) return {};

  const out: Record<string, number> = {};
  for (const [name, pair] of Object.entries(table)) {
    const [squishy, tank] = pair;
    // How much this item's standing improves (or decays) as the enemy hardens,
    // scaled by how much of their roster is actually tanky.
    const shift = (tank - squishy) * tankShare * (cfg.per_share ?? 0.1) * 10;
    if (Math.abs(shift) > 1e-4) out[name] = shift;
  }
  return out;
}
