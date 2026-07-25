import { describe, it, expect } from "vitest";
import { deriveThreats, threatOverlay } from "./threats";
import type { God } from "../types";

const god = (name: string, damage_type: string, specs: string[] = []): God =>
  ({ name, damage_type, specializations: specs, pantheon: "", role: "",
     base_stats: {}, abilities: [], aspects: [] } as unknown as God);

const CFG = { max_bonus: 0.12, per_enemy: 0.02,
  tag_bonus: { healers: { "anti-heal": 1 }, lockdown: { "cc-immunity": 1 } },
  stat_bonus: { magical: { "Magical Protection": 1 } },
  ally_covered: -0.5, ally_gap: 0.5 };

const EMPTY: import("../types").ThreatModel = {
  magical: 0, physical: 0, healers: 0, lockdown: 0, crit: 0, tanks: 0,
  allyCovers: {}, allyAllPhysical: false,
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
  });
});

describe("threatOverlay", () => {
  it("scales a tag bonus by enemy count", () => {
    const one = threatOverlay({ ...EMPTY, healers: 1 }, CFG);
    const two = threatOverlay({ ...EMPTY, healers: 2 }, CFG);
    expect(two.tags["anti-heal"]).toBeGreaterThan(one.tags["anti-heal"]);
  });

  it("raises an uncovered job and lowers a covered one", () => {
    const gap = threatOverlay({ ...EMPTY, healers: 2 }, CFG);
    const covered = threatOverlay(
      { ...EMPTY, healers: 2, allyCovers: { "anti-heal": true } }, CFG);
    expect(covered.tags["anti-heal"]).toBeLessThan(gap.tags["anti-heal"]);
  });
});
