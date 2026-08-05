import { describe, it, expect } from "vitest";
import { buildBands, tierStep, TIER_STEPS } from "./tierBands";
import type { GodTierEntry } from "../types";

const g = (o: Partial<GodTierEntry> & { name: string }): GodTierEntry => ({
  score: 0.5, tier_score: "B", role: "Mid", ...o,
});

describe("buildBands", () => {
  it("buckets by the measured band", () => {
    const r = buildBands([
      g({ name: "Ymir", tier_score: "S", score: 0.56 }),
      g({ name: "Ra", tier_score: "B", score: 0.48 }),
    ]);
    expect(r.bands.map((b) => b.tier)).toEqual(["S", "B"]);
    expect(r.bands[0].entries[0].entry.name).toBe("Ymir");
  });

  it("drops empty bands", () => {
    const r = buildBands([g({ name: "Solo", tier_score: "A" })]);
    expect(r.bands.map((b) => b.tier)).toEqual(["A"]);
  });

  it("orders a band best first by default", () => {
    const r = buildBands([
      g({ name: "Lower", tier_score: "S", score: 0.55 }),
      g({ name: "Higher", tier_score: "S", score: 0.58 }),
    ]);
    expect(r.bands[0].entries.map((e) => e.entry.name)).toEqual(["Higher", "Lower"]);
  });

  it("can order a band by how much play it rests on instead", () => {
    const r = buildBands([
      g({ name: "Rare", tier_score: "S", score: 0.58, matches: 44 }),
      g({ name: "Common", tier_score: "S", score: 0.55, matches: 670 }),
    ], "matches");
    expect(r.bands[0].entries.map((e) => e.entry.name)).toEqual(["Common", "Rare"]);
  });

  it("leaves an unmeasured entry untiered rather than in the bottom band", () => {
    // Joust and Arena publish no results at all, so this is every god there.
    // "We didn't measure this" and "this is bad" are different facts.
    const r = buildBands([
      g({ name: "Measured", tier_score: "A", score: 0.54 }),
      g({ name: "Unknown", tier_score: null, score: null }),
    ]);
    expect(r.bands.flatMap((b) => b.entries).map((e) => e.entry.name)).toEqual(["Measured"]);
    expect(r.untiered.map((e) => e.entry.name)).toEqual(["Unknown"]);
    expect(r.untiered[0].unmeasured).toBe(true);
    expect(r.ranked).toBe(1);
    expect(r.unmeasured).toBe(1);
    expect(r.total).toBe(2);
  });

  it("sums APPEARANCES behind the placed entries only", () => {
    const r = buildBands([
      g({ name: "A", score: 0.55, matches: 300 }),
      g({ name: "B", score: 0.50, matches: 700 }),
      g({ name: "Unmeasured", score: null, tier_score: null, matches: 9999 }),
    ]);
    expect(r.appearances).toBe(1000);
  });

  it("breaks ties on name so the order is stable across renders", () => {
    const r = buildBands([
      g({ name: "Zeus", tier_score: "A", score: 0.5 }),
      g({ name: "Anubis", tier_score: "A", score: 0.5 }),
    ]);
    expect(r.bands[0].entries.map((e) => e.entry.name)).toEqual(["Anubis", "Zeus"]);
  });

  it("handles an empty list without inventing bands", () => {
    const r = buildBands([]);
    expect(r.bands).toEqual([]);
    expect(r.total).toBe(0);
    expect(r.appearances).toBe(0);
  });
});

describe("tierStep", () => {
  it("reads left-to-right, worst to best", () => {
    expect(tierStep("C")).toBe(0);
    expect(tierStep("S")).toBe(TIER_STEPS - 1);
    expect(tierStep(null)).toBeNull();
  });
});
