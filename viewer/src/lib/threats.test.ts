import { describe, it, expect } from "vitest";
import { deriveThreats, threatOverlay, damageOverlay } from "./threats";
import type { God, DraftConfig, ThreatModel } from "../types";

const god = (name: string, damage_type: string, specs: string[] = []): God =>
  ({ name, damage_type, specializations: specs, pantheon: "", role: "",
     base_stats: {}, abilities: [], aspects: [] } as unknown as God);

const CFG = { max_bonus: 0.12, per_share: 0.1,
  tag_bonus: { healers: { "anti-heal": 1 }, lockdown: { "cc-immunity": 1 } },
  stat_bonus: { magical: { "Magical Protection": 1 } },
  ally_covered: -0.5, ally_gap: 0.5 };

const EMPTY: import("../types").ThreatModel = {
  magical: 0, physical: 0, healers: 0, lockdown: 0, crit: 0, tanks: 0,
  enemyCount: 0, rosterSize: 0, allyCovers: {}, allyAllPhysical: false,
  allyCount: 0, allyPhysical: 0,
};

describe("deriveThreats", () => {
  it("counts enemy damage types", () => {
    const t = deriveThreats({ allies: [], enemies: ["A", "B", "C"] },
      { A: god("A", "magical"), B: god("B", "magical"), C: god("C", "physical") }, {});
    expect(t.magical).toBe(2);
    expect(t.physical).toBe(1);
  });

  it("counts healers and lockdown from specializations", () => {
    const t = deriveThreats({ allies: [], enemies: ["H", "L"] },
      { H: god("H", "magical", ["Healing"]), L: god("L", "physical", ["Lockdown"]) }, {});
    expect(t.healers).toBe(1);
    expect(t.lockdown).toBe(1);
  });

  it("marks a job covered when an ally's core brings that tag", () => {
    const t = deriveThreats({ allies: ["Ally"], enemies: [] },
      { Ally: god("Ally", "magical") }, { Ally: ["anti-heal"] });
    expect(t.allyCovers["anti-heal"]).toBe(true);
  });

  it("returns an all-zero model for an empty comp", () => {
    const t = deriveThreats({ allies: [], enemies: [] }, {}, {});
    expect(t.magical + t.physical + t.healers + t.lockdown).toBe(0);
    expect(t.enemyCount).toBe(0);
  });

  it("records enemyCount as the number of recognised enemies", () => {
    const t = deriveThreats({ allies: [], enemies: ["A", "B", "C"] },
      { A: god("A", "magical"), B: god("B", "physical"), C: god("C", "physical") }, {});
    expect(t.enemyCount).toBe(3);
  });

  it("counts only recognised gods toward enemyCount (unknown names filtered)", () => {
    const t = deriveThreats({ allies: [], enemies: ["A", "Unknown", "B"] },
      { A: god("A", "magical"), B: god("B", "physical") }, {});
    expect(t.enemyCount).toBe(2);
  });
});

describe("threatOverlay", () => {
  it("scales a tag bonus by share of the enemy team, not raw count", () => {
    const one = threatOverlay({ ...EMPTY, healers: 1, enemyCount: 5 }, CFG);
    const two = threatOverlay({ ...EMPTY, healers: 2, enemyCount: 5 }, CFG);
    expect(two.tags["anti-heal"]).toBeGreaterThan(one.tags["anti-heal"]);
  });

  it("2 healers of 3 (Joust) produces a strictly larger bonus than 2 of 5 (Conquest)", () => {
    const of3 = threatOverlay({ ...EMPTY, healers: 2, enemyCount: 3 }, CFG);
    const of5 = threatOverlay({ ...EMPTY, healers: 2, enemyCount: 5 }, CFG);
    // share=2/3 * per_share 0.1 * w 1 * mult 1.5 (ally_gap) = 0.1
    expect(of3.tags["anti-heal"]).toBeCloseTo(0.1, 10);
    // share=2/5 * per_share 0.1 * w 1 * mult 1.5 = 0.06
    expect(of5.tags["anti-heal"]).toBeCloseTo(0.06, 10);
    expect(of3.tags["anti-heal"]).toBeGreaterThan(of5.tags["anti-heal"]);
  });

  it("a full 5-of-5 threat produces the same bonus as the pre-change per-enemy formula", () => {
    // Pinned to the Conquest-preservation claim: old formula was
    // n * per_enemy(0.02) * w * mult = 5 * 0.02 * 1 * 1.5 = 0.15.
    // New formula is share * per_share(0.1) * w * mult = 1 * 0.1 * 1 * 1.5 = 0.15.
    const full = threatOverlay({ ...EMPTY, healers: 5, enemyCount: 5 }, CFG);
    expect(full.tags["anti-heal"]).toBeCloseTo(0.15, 10);
  });

  it("raises an uncovered job and lowers a covered one", () => {
    const gap = threatOverlay({ ...EMPTY, healers: 2, enemyCount: 5 }, CFG);
    const covered = threatOverlay(
      { ...EMPTY, healers: 2, enemyCount: 5, allyCovers: { "anti-heal": true } }, CFG);
    expect(covered.tags["anti-heal"]).toBeLessThan(gap.tags["anti-heal"]);
  });

  it("an empty comp (enemyCount 0) yields no bonuses and never NaN", () => {
    const t = threatOverlay({ ...EMPTY, enemyCount: 0 }, CFG);
    expect(t.tags).toEqual({});
    expect(t.stats).toEqual({});
  });

  it("guards division by zero even if counts are inconsistent with enemyCount", () => {
    // Pathological/defensive case: a nonzero count with enemyCount 0 must not
    // produce NaN or Infinity.
    const t = threatOverlay({ ...EMPTY, healers: 2, enemyCount: 0 }, CFG);
    for (const v of Object.values(t.tags)) {
      expect(Number.isNaN(v)).toBe(false);
      expect(Number.isFinite(v)).toBe(true);
    }
  });
});

describe("threat share uses the enemy roster, not the enemies entered so far", () => {
  it("scales a single known healer by the mode's roster size", () => {
    // One healer known out of five slots is a 20% signal. Reading it as 100%
    // let a barely-started draft drive a maximal overlay.
    const early = threatOverlay({ ...EMPTY, healers: 1, enemyCount: 1, rosterSize: 5 }, CFG);
    const full = threatOverlay({ ...EMPTY, healers: 5, enemyCount: 5, rosterSize: 5 }, CFG);
    expect(early.tags["anti-heal"]).toBeCloseTo(full.tags["anti-heal"] / 5, 6);
  });

  it("does not shrink a threat as more (non-threatening) enemies are entered", () => {
    // The old denominator made the overlay *weaken* when you added information,
    // which reads as the model changing its mind.
    const oneOfOne = threatOverlay({ ...EMPTY, healers: 1, enemyCount: 1, rosterSize: 5 }, CFG);
    const oneOfFour = threatOverlay({ ...EMPTY, healers: 1, enemyCount: 4, rosterSize: 5 }, CFG);
    expect(oneOfFour.tags["anti-heal"]).toBeCloseTo(oneOfOne.tags["anti-heal"], 6);
  });

  it("still weighs a Joust threat heavier than the same count in Conquest", () => {
    const joust = threatOverlay({ ...EMPTY, healers: 2, enemyCount: 2, rosterSize: 3 }, CFG);
    const conquest = threatOverlay({ ...EMPTY, healers: 2, enemyCount: 2, rosterSize: 5 }, CFG);
    expect(joust.tags["anti-heal"]).toBeGreaterThan(conquest.tags["anti-heal"]);
  });

  it("falls back to the entered count when no roster size is supplied", () => {
    const withRoster = threatOverlay({ ...EMPTY, healers: 2, enemyCount: 2, rosterSize: 0 }, CFG);
    const legacy = threatOverlay({ ...EMPTY, healers: 2, enemyCount: 2 } as never, CFG);
    expect(withRoster.tags["anti-heal"]).toBeCloseTo(legacy.tags["anti-heal"], 6);
  });
});

describe("all-physical ally read", () => {
  const phys = (n: string) => god(n, "physical");
  it("does not call a lone entered god an all-physical team", () => {
    const t = deriveThreats({ allies: ["A"], enemies: [] }, { A: phys("A") }, {});
    expect(t.allyAllPhysical).toBe(false);
    expect(threatOverlay({ ...t, rosterSize: 5 }, CFG).stats["Penetration"]).toBeUndefined();
  });

  it("recognises it once two allies are known, scaled by roster share", () => {
    const t = deriveThreats({ allies: ["A", "B"], enemies: [] }, { A: phys("A"), B: phys("B") }, {});
    expect(t.allyAllPhysical).toBe(true);
    expect(t.allyPhysical).toBe(2);
    // 2 of 5 slots known -> 0.4 share of the full penetration nudge.
    expect(threatOverlay({ ...t, rosterSize: 5 }, CFG).stats["Penetration"]).toBeCloseTo(0.4 * CFG.per_share, 6);
  });

  it("is false when the known allies are mixed damage types", () => {
    const t = deriveThreats({ allies: ["A", "B"], enemies: [] }, { A: phys("A"), B: god("B", "magical") }, {});
    expect(t.allyAllPhysical).toBe(false);
  });
});

/* B6: the damage model applied where a target is actually known. The tag and
 * stat channels can only say "penetration is good against tanks"; this one
 * knows percent penetration rises and flat penetration falls. */
describe("damageOverlay", () => {
  const cfg = { per_share: 0.1 } as DraftConfig;
  const model = (tanks: number, rosterSize = 5) =>
    ({ tanks, rosterSize, enemyCount: tanks } as ThreatModel);
  // [vs squishy, vs tank], each column on its own scale.
  const table: Record<string, [number, number]> = {
    "Obsidian Shard": [0.648, 0.707],       // percent pen — rises
    "Spear of Desolation": [0.636, 0.562],  // flat pen — falls
    "Dreamer's Idol": [1.0, 1.0],           // best either way — no shift
  };

  it("does nothing until a tank is actually on the board", () => {
    expect(damageOverlay(model(0), table, cfg)).toEqual({});
  });

  it("rewards percent penetration and penalises flat as the enemy hardens", () => {
    const out = damageOverlay(model(3), table, cfg);
    expect(out["Obsidian Shard"]).toBeGreaterThan(0);
    expect(out["Spear of Desolation"]).toBeLessThan(0);
  });

  it("disagrees with the hand-tuned rule, which is the point", () => {
    // `stat_bonus.tanks.Penetration` rewards both items identically. The
    // measurement says they move in opposite directions.
    const out = damageOverlay(model(3), table, cfg);
    expect(Math.sign(out["Obsidian Shard"])).not.toBe(Math.sign(out["Spear of Desolation"]));
  });

  it("scales with how much of the roster is tanky", () => {
    const one = damageOverlay(model(1), table, cfg)["Obsidian Shard"];
    const three = damageOverlay(model(3), table, cfg)["Obsidian Shard"];
    expect(three).toBeGreaterThan(one);
  });

  it("emits nothing for an item whose standing does not move", () => {
    expect(damageOverlay(model(3), table, cfg)["Dreamer's Idol"]).toBeUndefined();
  });

  it("is inert for a god with no shipped table", () => {
    expect(damageOverlay(model(3), undefined, cfg)).toEqual({});
  });
});
