import { describe, it, expect } from "vitest";
import { buildGodRanking, topPercent } from "./godRanking";
import type { GodTierEntry } from "../types";

const gods: GodTierEntry[] = [
  { name: "Ymir", ours: 0.90, community: 0.30, tier_ours: "S", tier_community: "C", role: "Solo" },
  { name: "Ra", ours: 0.70, community: 0.80, tier_ours: "A", tier_community: "S", role: "Mid" },
  { name: "Agni", ours: 0.60, community: 0.60, tier_ours: "A", tier_community: "A", role: "Mid" },
  { name: "Anubis", ours: 0.40, community: null, tier_ours: "C", tier_community: null, role: "Mid" },
];

describe("buildGodRanking", () => {
  it("places the god across everything the model scored", () => {
    const r = buildGodRanking(gods, "Ra", "Mid")!;
    expect(r.overall).toBe(2);
    expect(r.scored).toBe(4);
  });

  it("places it inside its own band and its own lane", () => {
    const r = buildGodRanking(gods, "Agni", "Mid")!;
    expect(r.band).toBe("A");
    expect(r.inBand).toBe(2);       // Ra 0.70 then Agni 0.60
    expect(r.bandSize).toBe(2);
    expect(r.inLane).toBe(2);       // Ra, Agni, Anubis are Mid
    expect(r.laneSize).toBe(3);
  });

  it("names the gods immediately above and below on the model's scale", () => {
    const r = buildGodRanking(gods, "Ra", "Mid")!;
    expect(r.above?.name).toBe("Ymir");
    expect(r.above?.gap).toBeCloseTo(0.20, 5);
    expect(r.below?.name).toBe("Agni");
    expect(r.below?.gap).toBeCloseTo(-0.10, 5);
  });

  it("has no neighbour above for the top god, or below for the bottom", () => {
    expect(buildGodRanking(gods, "Ymir", "Solo")!.above).toBeUndefined();
    expect(buildGodRanking(gods, "Anubis", "Mid")!.below).toBeUndefined();
  });

  /* S=0..C=3, so a smaller index is a better tier. Getting this backwards
   * would colour "the meta rates higher" onto a god the model ranks two tiers
   * above the community — the exact bug the tier list already carries a
   * regression note about. */
  it("signs the tier gap so positive means the model ranks it higher", () => {
    expect(buildGodRanking(gods, "Ymir", "Solo")!.tierGap).toBe(3);   // S vs C
    expect(buildGodRanking(gods, "Ra", "Mid")!.tierGap).toBe(-1);     // A vs S
    expect(buildGodRanking(gods, "Agni", "Mid")!.tierGap).toBe(0);
  });

  it("reports agreement only when both sources placed it", () => {
    expect(buildGodRanking(gods, "Agni", "Mid")!.agrees).toBe(true);
    expect(buildGodRanking(gods, "Ra", "Mid")!.agrees).toBe(false);
    expect(buildGodRanking(gods, "Anubis", "Mid")!.agrees).toBe(false);
  });

  it("marks a god the community hasn't rated as unranked, with no delta", () => {
    const r = buildGodRanking(gods, "Anubis", "Mid")!;
    expect(r.unranked).toBe(true);
    expect(r.delta).toBeNull();
    expect(r.tierGap).toBeNull();
  });

  it("returns null for a god the model hasn't scored at all", () => {
    expect(buildGodRanking(gods, "Loki", "Jungle")).toBeNull();
    expect(buildGodRanking(undefined, "Ra", "Mid")).toBeNull();
  });

  it("gives no lane standing for a god with no lane", () => {
    const r = buildGodRanking(gods, "Ra", null)!;
    expect(r.inLane).toBeNull();
    expect(r.laneSize).toBe(0);
  });

  // A god the model left unscored can't sit anywhere on the model's scale.
  it("ignores unscored entries when ranking", () => {
    const withHole = [...gods, { name: "Ghost", ours: null, community: 0.5, tier_ours: null, tier_community: "B" } as unknown as GodTierEntry];
    const r = buildGodRanking(withHole, "Ra", "Mid")!;
    expect(r.scored).toBe(4);
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
