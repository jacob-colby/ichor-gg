import { describe, it, expect } from "vitest";
import { filterItems, sortItems, efficiencyLabel, EFFICIENCY } from "./itemFilters";
import type { Item } from "../types";

const items = [
  { name: "Rage", tier: 3, cost: 2500, stats: { "Critical Chance": "20%" }, passive: "", builds_from: [], builds_into: [], effect_tags: ["burst"], efficiency_tier: "undervalued" },
  { name: "Aegis", tier: 3, cost: 2100, stats: { "Max Health": "200" }, passive: "", builds_from: [], builds_into: [], effect_tags: ["aura"], efficiency_tier: "premium" },
  { name: "Dagger", tier: 2, cost: 900, stats: { "Attack Speed": "15%" }, passive: "", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: null },
] as unknown as Item[];

describe("filterItems", () => {
  it("filters by text, tier, efficiency, tag, stat", () => {
    expect(filterItems(items, { q: "rag" }).map((i) => i.name)).toEqual(["Rage"]);
    expect(filterItems(items, { tier: 2 }).map((i) => i.name)).toEqual(["Dagger"]);
    expect(filterItems(items, { efficiency: "premium" }).map((i) => i.name)).toEqual(["Aegis"]);
    expect(filterItems(items, { efficiency: "untiered" }).map((i) => i.name)).toEqual(["Dagger"]);
    expect(filterItems(items, { tag: "burst" }).map((i) => i.name)).toEqual(["Rage"]);
    expect(filterItems(items, { stat: "Max Health" }).map((i) => i.name)).toEqual(["Aegis"]);
  });
  it("returns all with an empty filter", () => {
    expect(filterItems(items, {}).length).toBe(3);
  });
});

describe("sortItems", () => {
  it("sorts by cost and name", () => {
    expect(sortItems(items, "cost-asc").map((i) => i.name)).toEqual(["Dagger", "Aegis", "Rage"]);
    expect(sortItems(items, "name").map((i) => i.name)).toEqual(["Aegis", "Dagger", "Rage"]);
  });
});

describe("efficiencyLabel", () => {
  it("maps tiers to friendly labels", () => {
    expect(efficiencyLabel("undervalued").text).toBe("Underrated");
    expect(efficiencyLabel("premium").text).toBe("Overrated");
    expect(efficiencyLabel("fair").text).toBe("Fair");
    expect(efficiencyLabel(null).text).toBe("—");
    expect(EFFICIENCY.length).toBe(4);
  });
});
