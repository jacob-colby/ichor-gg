import { describe, it, expect } from "vitest";
import { deriveThreats, threatOverlay } from "./threats";
import type { God } from "../types";

const god = (name: string, damage_type: string, specs: string[] = []): God =>
  ({ name, damage_type, specializations: specs, pantheon: "", role: "",
     base_stats: {}, abilities: [], aspects: [] } as unknown as God);

const CFG = { max_bonus: 0.12, per_share: 0.1,
  tag_bonus: { healers: { "anti-heal": 1 }, lockdown: { "cc-immunity": 1 } },
  stat_bonus: { magical: { "Magical Protection": 1 } },
  ally_covered: -0.5, ally_gap: 0.5 };

const EMPTY: import("../types").ThreatModel = {
  magical: 0, physical: 0, healers: 0, lockdown: 0, crit: 0, tanks: 0,
  enemyCount: 0, allyCovers: {}, allyAllPhysical: false,
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
