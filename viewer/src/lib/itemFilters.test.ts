import { describe, it, expect } from "vitest";
import { filterItems, sortItems, efficiencyLabel, tiersPresent, residualText, statValueLines, statKey, EFFICIENCY } from "./itemFilters";
import type { Item } from "../types";

const items = [
  { name: "Rage", tier: 3, cost: 2500, stats: { "Critical Chance": "20%" }, passive: "", builds_from: [], builds_into: [], effect_tags: ["burst"], efficiency_tier: "undervalued" },
  { name: "Aegis", tier: 3, cost: 2100, stats: { "Max Health": "200" }, passive: "", builds_from: [], builds_into: [], effect_tags: ["aura"], efficiency_tier: "premium" },
  { name: "Dagger", tier: 2, cost: 900, stats: { "Attack Speed": "15%" }, passive: "", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: null },
  { name: "Blinking Abyss", tier: "Glyph", cost: 0, stats: {}, passive: "", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: null },
] as unknown as Item[];

describe("filterItems", () => {
  it("filters by text, tier, efficiency, tag, stat", () => {
    expect(filterItems(items, { q: "rag" }).map((i) => i.name)).toEqual(["Rage"]);
    expect(filterItems(items, { tier: 2 }).map((i) => i.name)).toEqual(["Dagger"]);
    expect(filterItems(items, { efficiency: "premium" }).map((i) => i.name)).toEqual(["Aegis"]);
    expect(filterItems(items, { efficiency: "untiered" }).map((i) => i.name)).toEqual(["Dagger", "Blinking Abyss"]);
    expect(filterItems(items, { tag: "burst" }).map((i) => i.name)).toEqual(["Rage"]);
    expect(filterItems(items, { stat: "Max Health" }).map((i) => i.name)).toEqual(["Aegis"]);
  });
  it("returns all with an empty filter", () => {
    expect(filterItems(items, {}).length).toBe(4);
  });
  it("filters by a non-numeric string tier label (e.g. Glyph)", () => {
    expect(filterItems(items, { tier: "Glyph" }).map((i) => i.name)).toEqual(["Blinking Abyss"]);
    expect(filterItems(items, { tier: 3 }).map((i) => i.name)).toEqual(["Rage", "Aegis"]);
  });
});

describe("sortItems", () => {
  it("sorts by cost and name", () => {
    expect(sortItems(items, "cost-asc").map((i) => i.name)).toEqual(["Blinking Abyss", "Dagger", "Aegis", "Rage"]);
    expect(sortItems(items, "name").map((i) => i.name)).toEqual(["Aegis", "Blinking Abyss", "Dagger", "Rage"]);
  });
});

describe("efficiencyLabel", () => {
  it("maps tiers to stat-value labels", () => {
    expect(efficiencyLabel("undervalued").text).toBe("Undervalued");
    expect(efficiencyLabel("premium").text).toBe("Premium");
    expect(efficiencyLabel("fair").text).toBe("Fair");
    // Not an em dash: a filter option named after a punctuation mark, on a
    // verdict that is null for a stateable reason.
    expect(efficiencyLabel(null).text).toBe("Not scored");
    expect(EFFICIENCY.length).toBe(4);
  });
});

describe("tiersPresent", () => {
  it("derives the tier options from the data, numerics first", () => {
    // The filter used to hardcode a Glyph option matching zero items while the
    // one Relic in the set was unreachable.
    expect(tiersPresent(items)).toEqual([3, 2, "Glyph"]);
  });
  it("returns nothing for an empty set rather than inventing tiers", () => {
    expect(tiersPresent([])).toEqual([]);
  });
});

describe("sortItems by value", () => {
  const priced = [
    { name: "Bargain", cost: 1000, efficiency: { predicted_cost: 1400, residual: -400, score: 1 } },
    { name: "Fairish", cost: 2000, efficiency: { predicted_cost: 2010, residual: -10, score: 0.5 } },
    { name: "Tax", cost: 3000, efficiency: { predicted_cost: 2100, residual: 900, score: 0 } },
    { name: "Starter", cost: 700, efficiency: null },
  ] as unknown as Parameters<typeof sortItems>[0];

  it("orders by the continuous residual, most underpriced first", () => {
    // Sorting by the three-value bucket tied 30 items for first alphabetically.
    expect(sortItems(priced, "value").map((i) => i.name)).toEqual(["Bargain", "Fairish", "Tax", "Starter"]);
  });

  it("sinks unscored items rather than treating them as a zero residual", () => {
    expect(sortItems(priced, "value").at(-1)!.name).toBe("Starter");
  });
});

describe("filterItems search", () => {
  it("matches tags, stat names and passive text, not just the name", () => {
    expect(filterItems(items, { q: "burst" }).map((i) => i.name)).toEqual(["Rage"]);
    expect(filterItems(items, { q: "max health" }).map((i) => i.name)).toEqual(["Aegis"]);
  });
});

describe("residualText", () => {
  it("always carries its sign and separates thousands", () => {
    expect(residualText(244)).toBe("+244g");
    expect(residualText(-1310)).toBe("−1,310g");
    expect(residualText(0)).toBe("0g");
  });
});

describe("statValueLines", () => {
  const gold = { "Max Health": 0.88, Intelligence: 6.59 };
  it("prices each stat at its fitted gold value", () => {
    const item = { name: "X", stats: { "Max Health": "200" } } as never;
    const [line] = statValueLines(item, gold);
    expect(line.amount).toBe(200);
    expect(line.goldPerUnit).toBe(0.88);
    expect(line.subtotal).toBeCloseTo(176, 6);
  });
  it("parses a percent stat's leading number", () => {
    const item = { name: "X", stats: { Intelligence: "30%" } } as never;
    expect(statValueLines(item, gold)[0].amount).toBe(30);
  });
  it("returns null rather than a silent zero for a stat the fit never priced", () => {
    const item = { name: "X", stats: { Unpriced: "10" } } as never;
    const [line] = statValueLines(item, gold);
    expect(line.goldPerUnit).toBeNull();
    expect(line.subtotal).toBeNull();
  });
});

/* Flat and percent of the same stat are different goods — the pipeline prices
 * them in separate columns, and a receipt that looked up the bare name would
 * read the wrong price. Penetration ships both ways, ~4.5x apart per point. */
describe("statKey / statValueLines — units are part of a stat's identity", () => {
  const gold = { Penetration: 8.63, "Penetration %": 38.92, _intercept: 1900 };

  it("keys a percentage separately from its flat namesake", () => {
    expect(statKey("Penetration", "10")).toBe("Penetration");
    expect(statKey("Penetration", "10%")).toBe("Penetration %");
    expect(statKey("Strength", " 40 ")).toBe("Strength");
  });

  it("prices each item against its own column", () => {
    const flat = { name: "F", stats: { Penetration: "10" } } as unknown as Item;
    const pct = { name: "P", stats: { Penetration: "10%" } } as unknown as Item;
    expect(statValueLines(flat, gold)[0].subtotal).toBeCloseTo(86.3);
    expect(statValueLines(pct, gold)[0].subtotal).toBeCloseTo(389.2);
  });

  it("still labels the row with the stat's own name, not the column's", () => {
    const pct = { name: "P", stats: { Penetration: "10%" } } as unknown as Item;
    expect(statValueLines(pct, gold)[0].stat).toBe("Penetration");
  });
});
