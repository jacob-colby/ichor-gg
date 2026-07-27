import { describe, it, expect } from "vitest";
import { buildDivergenceBoard, stepPercent, deltaText } from "./divergence";
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

  it("ranks each lane by how many rungs apart the two sources are", () => {
    const b = buildDivergenceBoard([
      entry({ name: "OneRung", tier_ours: "B", tier_community: "A", ours: 0.5, community: 0.51 }),
      // A smaller score gap but a bigger argument — the bar is drawn in rungs,
      // so the order has to be in rungs too or a short bar sorts above a long.
      entry({ name: "ThreeRungs", tier_ours: "S", tier_community: "C", ours: 0.53, community: 0.52 }),
      entry({ name: "Agrees", tier_ours: "B", tier_community: "B", ours: 0.4, community: 0.7 }),
    ]);
    expect(b.lanes[0].rows.map((r) => r.name)).toEqual(["ThreeRungs", "OneRung", "Agrees"]);
  });

  it("falls back to the raw score gap only between equal-sized arguments", () => {
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

  it("places each source on its own rung and names the verdict from the letters", () => {
    const b = buildDivergenceBoard([
      entry({ name: "Geb", tier_ours: "A", tier_community: "C", role: "Support" }),
    ]);
    const row = b.lanes[0].rows[0];
    // C=0 … S=3, read left to right.
    expect(row.theirStep).toBe(0);
    expect(row.ourStep).toBe(2);
    expect(row.tierGap).toBe(2);
    expect(row.verdict).toBe("underrated");
  });

  it("lets the tier letters own the verdict when the score gap disagrees", () => {
    // The real boundary case: identical scores, but the letters put it a full
    // tier apart. Colouring from the score would print a grey "agreed" beside
    // a bar drawn one rung wide.
    const b = buildDivergenceBoard([
      entry({ name: "NeZha", ours: 0.51, community: 0.51, tier_ours: "A", tier_community: "B" }),
    ]);
    const row = b.lanes[0].rows[0];
    expect(row.delta).toBeCloseTo(0, 5);
    expect(row.verdict).toBe("underrated");
    expect(row.tierDisagrees).toBe(true);
  });

  it("treats a god with a score but no tier letter as unranked", () => {
    // There is no rung to stand it on, so it cannot be drawn — counted, not
    // given an invented placement.
    const b = buildDivergenceBoard([
      entry({ name: "Untiered", ours: 0.5, community: 0.5, tier_ours: null }),
    ]);
    expect(b.unranked).toBe(1);
    expect(b.ranked).toBe(0);
  });

  it("counts tier disagreements independently of score distance", () => {
    const b = buildDivergenceBoard([
      // Tiny delta, but the tier letters still differ.
      entry({ name: "Edge", ours: 0.5, community: 0.49, tier_ours: "A", tier_community: "B" }),
      entry({ name: "Agree", ours: 0.5, community: 0.4, tier_ours: "B", tier_community: "B" }),
    ]);
    expect(b.tierDisagreements).toBe(1);
    // The headline count has to decompose into the rows beneath it.
    const rows = b.lanes[0].rows;
    expect(rows.filter((r) => r.tierDisagrees)).toHaveLength(1);
    expect(rows.find((r) => r.name === "Edge")!.tierDisagrees).toBe(true);
    expect(rows.find((r) => r.name === "Agree")!.tierDisagrees).toBe(false);
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

describe("stepPercent", () => {
  it("centres a mark in its own rung, never on a boundary", () => {
    // Four rungs, so each is 25% wide and its centre sits 12.5% in.
    expect(stepPercent(0)).toBeCloseTo(12.5, 5);
    expect(stepPercent(1)).toBeCloseTo(37.5, 5);
    expect(stepPercent(2)).toBeCloseTo(62.5, 5);
    expect(stepPercent(3)).toBeCloseTo(87.5, 5);
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
