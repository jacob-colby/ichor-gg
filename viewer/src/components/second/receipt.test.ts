import { describe, it, expect } from "vitest";
import { buildReceipt, signedGold } from "./receipt";
import type { Item } from "../../types";

const item = (over: Partial<Item>): Item => ({
  type: "item", name: "X", tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [],
  source_url: "", last_verified: "", ...over,
}) as Item;

const sum = (r: NonNullable<ReturnType<typeof buildReceipt>>) => r.lines.reduce((a, l) => a + l.gold, 0);

describe("buildReceipt — the receipt closes exactly", () => {
  it("rounds the rows onto the pipeline's own total", () => {
    // 1086.64 + 85 × 13.58 = 2240.94 → the pipeline ships 2241.
    const r = buildReceipt(item({ stats: { Intelligence: "85" },
      efficiency: { predicted_cost: 2241, residual: 259, score: 0.4 } }), { _intercept: 1086.64, Intelligence: 13.58 })!;
    expect(sum(r)).toBe(2241);
    expect(r.worth).toBe(2241);
    expect(r.cost - r.worth).toBe(r.gap);
    expect(r.lines.map((l) => l.label)).toEqual(["Base price", "Intelligence"]);
  });

  it("gives a lost gold back to the row that lost most, so three .5s still add up", () => {
    const r = buildReceipt(item({ stats: { A: "1", B: "1", C: "1" },
      efficiency: { predicted_cost: 1002, residual: 0, score: 0 } }), { _intercept: 0.5, A: 333.5, B: 333.5, C: 334.5 })!;
    expect(sum(r)).toBe(1002);
  });

  it("prints a gap the rows cannot explain as its own line, never inside a row", () => {
    const r = buildReceipt(item({ stats: { "Max Health": "200" },
      efficiency: { predicted_cost: 1800, residual: 300, score: 0.2 } }), { "Max Health": 0.88 })!;
    expect(r.lines.at(-1)?.label).toBe("Not itemised");
    expect(sum(r)).toBe(1800);
  });

  it("names a stat the fit never priced instead of counting it as zero", () => {
    const r = buildReceipt(item({ stats: { Strength: "40", Mystery: "3" },
      efficiency: { predicted_cost: 1840, residual: 660, score: 0.1 } }), { _intercept: 1000, Strength: 21 })!;
    expect(r.unpriced).toEqual(["Mystery"]);
  });

  it("returns nothing for an item the model does not price", () => {
    expect(buildReceipt(item({ tier: 1, efficiency: null }), {})).toBeNull();
  });

  it("signs the gap in gold", () => {
    expect(signedGold(244)).toBe("+244g");
    expect(signedGold(-1200)).toBe("−1,200g");
    expect(signedGold(0)).toBe("0g");
  });
});
