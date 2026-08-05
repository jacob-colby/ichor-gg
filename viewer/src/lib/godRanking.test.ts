import { describe, it, expect } from "vitest";
import { buildGodRanking, topPercent } from "./godRanking";
import type { GodTierEntry } from "../types";

const gods: GodTierEntry[] = [
  { name: "Ymir", score: 0.56, win_rate: 0.60, matches: 400, tier_score: "S", role: "Solo" },
  { name: "Ra", score: 0.52, win_rate: 0.55, matches: 380, tier_score: "A", role: "Mid" },
  { name: "Agni", score: 0.50, win_rate: 0.53, matches: 300, tier_score: "A", role: "Mid" },
  { name: "Anubis", score: 0.42, win_rate: 0.45, matches: 250, tier_score: "C", role: "Mid" },
];

describe("buildGodRanking", () => {
  it("places the god across everything measured", () => {
    const r = buildGodRanking(gods, "Ra", "Mid")!;
    expect(r.overall).toBe(2);
    expect(r.scored).toBe(4);
  });

  it("places it inside its own band and its own lane", () => {
    const r = buildGodRanking(gods, "Agni", "Mid")!;
    expect(r.band).toBe("A");
    expect(r.inBand).toBe(2);       // Ra 0.52 then Agni 0.50
    expect(r.bandSize).toBe(2);
    expect(r.inLane).toBe(2);       // Ra, Agni, Anubis are Mid
    expect(r.laneSize).toBe(3);
  });

  it("names the gods immediately above and below, with their raw rates", () => {
    const r = buildGodRanking(gods, "Ra", "Mid")!;
    expect(r.above?.name).toBe("Ymir");
    expect(r.above?.winRate).toBeCloseTo(0.60, 5);
    expect(r.above?.gap).toBeCloseTo(0.04, 5);
    expect(r.below?.name).toBe("Agni");
    expect(r.below?.gap).toBeCloseTo(-0.02, 5);
  });

  it("has no neighbour above for the top god, or below for the bottom", () => {
    expect(buildGodRanking(gods, "Ymir", "Solo")!.above).toBeUndefined();
    expect(buildGodRanking(gods, "Anubis", "Mid")!.below).toBeUndefined();
  });

  it("returns null for a god absent from this mode's list", () => {
    expect(buildGodRanking(gods, "Loki", "Jungle")).toBeNull();
    expect(buildGodRanking(undefined, "Ra", "Mid")).toBeNull();
  });

  it("gives no lane standing for a god with no lane", () => {
    const r = buildGodRanking(gods, "Ra", null)!;
    expect(r.inLane).toBeNull();
    expect(r.laneSize).toBe(0);
  });

  describe("a god with no usable sample", () => {
    // Every god outside Conquest, which publishes no results at all. It is a
    // real entry that simply isn't placed — not the worst-placed one.
    const withHole: GodTierEntry[] = [
      ...gods,
      { name: "Ghost", score: null, tier_score: null, role: "Mid" },
    ];

    it("is marked unmeasured and given no position", () => {
      const r = buildGodRanking(withHole, "Ghost", "Mid")!;
      expect(r.unmeasured).toBe(true);
      expect(r.overall).toBeNull();
      expect(r.inBand).toBeNull();
      expect(r.inLane).toBeNull();
    });

    it("does not sink to the bottom of anyone else's ordering", () => {
      const r = buildGodRanking(withHole, "Anubis", "Mid")!;
      expect(r.scored).toBe(4);
      expect(r.below).toBeUndefined();   // Anubis is still last among measured
    });
  });
});

describe("topPercent", () => {
  it("reads as a top-N%", () => {
    expect(topPercent(12, 87)).toBe(14);
    expect(topPercent(87, 87)).toBe(100);
  });

  // "top 0%" would be nonsense for the best-placed god.
  it("never reports zero", () => {
    expect(topPercent(1, 500)).toBe(1);
  });
});
