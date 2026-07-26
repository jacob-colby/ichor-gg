import { describe, it, expect } from "vitest";
import { buildDivergenceBoard, barPercent, deltaText } from "./divergence";
import type { GodTierEntry } from "../types";

const entry = (o: Partial<GodTierEntry> & { name: string }): GodTierEntry => ({
  ours: 0.5, community: 0.5, tier_ours: "B", tier_community: "B", role: "Mid", ...o,
});

describe("buildDivergenceBoard", () => {
  it("returns an empty board for missing or empty input", () => {
    for (const input of [undefined, []]) {
      const b = buildDivergenceBoard(input);
      expect(b.lanes).toEqual([]);
      expect(b.total).toBe(0);
      expect(b.ranked).toBe(0);
      expect(b.scale).toBe(1);
    }
  });

  it("computes delta as ours minus community", () => {
    const b = buildDivergenceBoard([entry({ name: "Geb", ours: 0.51, community: 0.36, role: "Support" })]);
    expect(b.lanes[0].rows[0].delta).toBeCloseTo(0.15, 5);
  });

  it("counts gods without a community score as unranked and gives them no delta", () => {
    const b = buildDivergenceBoard([
      entry({ name: "Awilix", community: null, tier_community: null, role: "Jungle" }),
      entry({ name: "Loki", ours: 0.54, community: 0.5, role: "Jungle" }),
    ]);
    expect(b.unranked).toBe(1);
    expect(b.ranked).toBe(1);
    expect(b.total).toBe(2);
    const jungle = b.lanes.find((l) => l.lane === "Jungle")!;
    expect(jungle.rows.map((r) => r.name)).toEqual(["Loki"]);
    expect(jungle.unranked).toBe(1);
  });

  it("treats a missing model score as unranked too", () => {
    const b = buildDivergenceBoard([entry({ name: "Ghost", ours: null })]);
    expect(b.unranked).toBe(1);
    expect(b.ranked).toBe(0);
  });

  it("ranks each lane by the size of the disagreement, not its direction", () => {
    const b = buildDivergenceBoard([
      entry({ name: "Small", ours: 0.5, community: 0.48, role: "Mid" }),
      entry({ name: "BigNegative", ours: 0.4, community: 0.6, role: "Mid" }),
      entry({ name: "Medium", ours: 0.6, community: 0.5, role: "Mid" }),
    ]);
    expect(b.lanes[0].rows.map((r) => r.name)).toEqual(["BigNegative", "Medium", "Small"]);
  });

  it("breaks ties on name so ordering is stable", () => {
    const b = buildDivergenceBoard([
      entry({ name: "Zeus", ours: 0.6, community: 0.5, role: "Mid" }),
      entry({ name: "Agni", ours: 0.4, community: 0.5, role: "Mid" }),
    ]);
    expect(b.lanes[0].rows.map((r) => r.name)).toEqual(["Agni", "Zeus"]);
  });

  it("reports the systematic lean of a lane as a mean signed delta", () => {
    const b = buildDivergenceBoard([
      entry({ name: "A", ours: 0.4, community: 0.6, role: "Carry" }),
      entry({ name: "B", ours: 0.45, community: 0.55, role: "Carry" }),
    ]);
    const carry = b.lanes.find((l) => l.lane === "Carry")!;
    expect(carry.meanDelta).toBeCloseTo(-0.15, 5);
    expect(carry.lower).toBe(2);
    expect(carry.higher).toBe(0);
  });

  it("counts tier disagreements independently of score distance", () => {
    const b = buildDivergenceBoard([
      // Tiny delta, but the tier letters still differ.
      entry({ name: "Edge", ours: 0.5, community: 0.49, tier_ours: "A", tier_community: "B" }),
      entry({ name: "Agree", ours: 0.5, community: 0.4, tier_ours: "B", tier_community: "B" }),
    ]);
    expect(b.tierDisagreements).toBe(1);
    // The headline count has to decompose into the columns beneath it.
    expect(b.lanes[0].tierDiffer).toBe(1);
    const rows = b.lanes[0].rows;
    expect(rows.find((r) => r.name === "Edge")!.tierDisagrees).toBe(true);
    expect(rows.find((r) => r.name === "Agree")!.tierDisagrees).toBe(false);
  });

  it("scales to the largest absolute delta on the board", () => {
    const b = buildDivergenceBoard([
      entry({ name: "A", ours: 0.45, community: 0.68, role: "Carry" }),
      entry({ name: "B", ours: 0.5, community: 0.48, role: "Mid" }),
    ]);
    expect(b.scale).toBeCloseTo(0.23, 5);
  });

  it("never scales by zero when every god matches exactly", () => {
    const b = buildDivergenceBoard([entry({ name: "Same", ours: 0.5, community: 0.5 })]);
    expect(b.scale).toBe(1);
    expect(barPercent(0, b.scale)).toBe(0);
  });

  it("uses the primary lane so multi-role gods land in exactly one column", () => {
    const b = buildDivergenceBoard([entry({ name: "Guan Yu", role: "Solo Support", ours: 0.47, community: 0.64 })]);
    expect(b.lanes.map((l) => l.lane)).toEqual(["Solo"]);
    expect(b.lanes[0].rows).toHaveLength(1);
  });

  it("drops lanes with nothing to show but keeps a lane that is only unranked", () => {
    const b = buildDivergenceBoard([
      entry({ name: "Ranked", role: "Mid", ours: 0.5, community: 0.4 }),
      entry({ name: "NoData", role: "Support", community: null }),
    ]);
    expect(b.lanes.map((l) => l.lane)).toEqual(["Mid", "Support"]);
    expect(b.lanes.find((l) => l.lane === "Support")!.rows).toEqual([]);
  });

  it("ignores a god whose role matches no known lane", () => {
    const b = buildDivergenceBoard([entry({ name: "Mystery", role: "Announcer", ours: 0.6, community: 0.4 })]);
    expect(b.ranked).toBe(1);
    expect(b.lanes).toEqual([]);
  });
});

describe("barPercent", () => {
  it("is proportional to the delta and clamps at the scale", () => {
    expect(barPercent(0.1, 0.2)).toBe(50);
    expect(barPercent(-0.1, 0.2)).toBe(50);
    expect(barPercent(0.4, 0.2)).toBe(100);
    expect(barPercent(0, 0.2)).toBe(0);
  });
});

describe("deltaText", () => {
  it("always carries a sign and two decimals", () => {
    expect(deltaText(0.15)).toBe("+0.15");
    expect(deltaText(-0.23)).toBe("-0.23");
    expect(deltaText(0)).toBe("0.00");
    // A lean too small to survive rounding must not claim a direction.
    expect(deltaText(-0.003)).toBe("0.00");
    expect(deltaText(0.004)).toBe("0.00");
    expect(deltaText(null)).toBe("—");
    expect(deltaText(undefined)).toBe("—");
  });
});
