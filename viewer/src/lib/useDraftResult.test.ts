import { describe, it, expect } from "vitest";
import { renderHook } from "@testing-library/react";
import { useDraftResult, draftMaxLifesteal } from "./useDraftResult";
import type { DraftComp, DraftConfig, God, Item } from "../types";

const god = (name: string, overrides: Partial<God> = {}): God =>
  ({
    type: "god", name, pantheon: "Test", role: "Carry", specializations: [],
    damage_type: "physical", release_date: "", base_stats: {}, abilities: [], aspects: [],
    source_url: "", last_verified: "", ...overrides,
  }) as God;

const testGod = god("TestGod");
const healerGod = god("EnemyHealer", { role: "Support", specializations: ["Healing"], damage_type: "magical" });
const GODS = [testGod, healerGod];

const item = (name: string, tags: string[] = []): Item =>
  ({
    name, tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [],
    effect_tags: tags, efficiency_tier: null,
  }) as unknown as Item;

// Seven items ranking into a 6-item core: AntiHeal starts one rank outside
// it, so it only appears once a threat's bonus promotes it past Zeta — with
// fewer items than the core size, every item would be "in the core" in both
// the base and adapted build regardless of any bonus, and no promotion could
// ever be observed.
const ITEMS = [
  item("Alpha"), item("Beta"), item("Gamma"), item("Delta"), item("Epsilon"), item("Zeta"),
  item("AntiHeal", ["anti-heal"]),
];
const SCORES = { Alpha: 0.6, Beta: 0.59, Gamma: 0.58, Delta: 0.57, Epsilon: 0.56, Zeta: 0.55, AntiHeal: 0.4 };
const GOD_ITEM_SCORES = { TestGod: SCORES };

const DRAFT_CFG: DraftConfig = {
  max_bonus: 0.5, per_share: 0.5,
  tag_bonus: { healers: { "anti-heal": 1 } }, stat_bonus: {},
  ally_covered: -0.5, ally_gap: 0.5,
};

const comp = (allies: string[], enemies: string[]): DraftComp => ({ allies, enemies });

const run = (allies: string[], enemies: string[], scores = GOD_ITEM_SCORES, cfg: DraftConfig | undefined = DRAFT_CFG) =>
  renderHook(() => useDraftResult(comp(allies, enemies), "conquest", GODS, ITEMS, [], scores, cfg)).result.current;

/* Two surfaces now render a view of the same draft — /draft and the dock.
 * This is the single derivation both call; DraftPage.test.tsx and
 * DraftDock.test.tsx each exercise it end-to-end through their own UI, so
 * this file only has to prove the derivation itself, not re-prove either
 * page renders it correctly. */
describe("useDraftResult", () => {
  it("is disabled with no god in the you-slot", () => {
    const r = run(["", "", "", "", ""], ["", "", "", "", ""]);
    expect(r.meName).toBe("");
    expect(r.draftEnabled).toBe(false);
    expect(r.result).toBeNull();
    expect(r.changeCount).toBe(0);
  });

  it("is disabled for a god with no scored items, even with a config", () => {
    const r = run(["EnemyHealer", "", "", "", ""], ["", "", "", "", ""]);
    expect(r.draftEnabled).toBe(false);
  });

  it("is disabled with a scored god but no draftConfig", () => {
    // Not routed through `run`: a default parameter substitutes its default
    // for an explicit `undefined` too, which would silently defeat the case
    // this test exists to cover.
    const { result } = renderHook(() => useDraftResult(
      comp(["TestGod", "", "", "", ""], ["", "", "", "", ""]),
      "conquest", GODS, ITEMS, [], GOD_ITEM_SCORES, undefined,
    ));
    expect(result.current.draftEnabled).toBe(false);
  });

  it("produces the default core with no enemies known", () => {
    const r = run(["TestGod", "", "", "", ""], ["", "", "", "", ""]);
    expect(r.draftEnabled).toBe(true);
    expect(r.changeCount).toBe(0);
    expect(r.enemiesKnown).toBe(0);
  });

  it("promotes a countering item once a threat is entered, and counts it as a change", () => {
    const r = run(["TestGod", "", "", "", ""], ["EnemyHealer", "", "", "", ""]);
    expect(r.changeCount).toBeGreaterThan(0);
    expect(r.result!.adapted.core).toContain("AntiHeal");
    expect(r.enemiesKnown).toBe(1);
    expect(r.roster).toBe(5); // the mode's slot count, not the number filled
  });

  it("names the enemy behind a threat through threatCulprits", () => {
    const r = run(["TestGod", "", "", "", ""], ["EnemyHealer", "", "", "", ""]);
    expect(r.threatCulprits.healers).toEqual(["EnemyHealer"]);
    expect(r.threatCulprits.tanks).toEqual([]);
  });

  it("tracks taken names across both rows, for the picker's disabled state", () => {
    const r = run(["TestGod", "", "", "", ""], ["EnemyHealer", "", "", "", ""]);
    expect(r.taken.has("TestGod")).toBe(true);
    expect(r.taken.has("EnemyHealer")).toBe(true);
    expect(r.taken.size).toBe(2);
  });

  it("gives coreSize a sensible default (6) before anything is scored", () => {
    const r = run(["", "", "", "", ""], ["", "", "", "", ""]);
    expect(r.coreSize).toBe(6);
  });
});

/* The cap rule used to live twice — a YAML row and a TypeScript copy of its
 * conditions — and only the YAML side was under test. These pin the evaluator
 * against the rule shape the index actually ships. */
describe("draftMaxLifesteal — reads the shipped rule, not a copy of it", () => {
  const carry = { name: "Cernunnos", damage_type: "physical", role: "Carry", specializations: ["Sharpshooter"] } as God;
  const mage = { name: "Agni", damage_type: "magical", role: "Mid", specializations: ["Nuker"] } as God;
  const rules = [{ damage_types: ["physical"], match_any: ["Carry", "Hunter", "Sharpshooter"], max_lifesteal: 2 }];

  it("raises the cap for a god the rule matches", () => {
    expect(draftMaxLifesteal(carry, rules)).toBe(2);
  });

  it("leaves a god the rule doesn't match at the default", () => {
    expect(draftMaxLifesteal(mage, rules)).toBe(1);
    // Right specialization, wrong damage type — both conditions must hold.
    expect(draftMaxLifesteal({ ...mage, specializations: ["Sharpshooter"] } as God, rules)).toBe(1);
  });

  it("follows an edited rule instead of the old hardcoded one", () => {
    // The whole point: change the data, the draft changes with it.
    expect(draftMaxLifesteal(mage, [{ damage_types: null, match_any: null, max_lifesteal: 3 }])).toBe(3);
  });

  it("defaults safely when the index predates the shipped rule", () => {
    expect(draftMaxLifesteal(carry, undefined)).toBe(1);
    expect(draftMaxLifesteal(undefined, rules)).toBe(1);
  });
});
