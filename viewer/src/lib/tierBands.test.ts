import { describe, it, expect } from "vitest";
import { buildBands, biggestArguments } from "./tierBands";
import type { GodTierEntry } from "../types";

const g = (o: Partial<GodTierEntry> & { name: string }): GodTierEntry => ({
  ours: 0.5, community: 0.5, tier_ours: "B", tier_community: "B", role: "Mid", ...o,
});

describe("buildBands", () => {
  it("buckets by the model's tier, never the community's", () => {
    const r = buildBands([
      g({ name: "Ymir", tier_ours: "S", tier_community: "C", ours: 0.9, community: 0.3 }),
      g({ name: "Ra", tier_ours: "B", tier_community: "A", ours: 0.5, community: 0.8 }),
    ]);
    expect(r.bands.map((b) => b.tier)).toEqual(["S", "B"]);
    expect(r.bands[0].entries[0].entry.name).toBe("Ymir");
  });

  it("drops empty bands", () => {
    const r = buildBands([g({ name: "Solo", tier_ours: "A" })]);
    expect(r.bands.map((b) => b.tier)).toEqual(["A"]);
  });

  it("signs the tier gap so positive means the model ranks it higher", () => {
    const r = buildBands([
      g({ name: "ModelLikes", tier_ours: "S", tier_community: "C" }),
      g({ name: "MetaLikes", tier_ours: "C", tier_community: "S" }),
      g({ name: "Same", tier_ours: "A", tier_community: "A" }),
    ]);
    const find = (n: string) => r.bands.flatMap((b) => b.entries).find((e) => e.entry.name === n)!;
    expect(find("ModelLikes").tierGap).toBe(3);
    expect(find("MetaLikes").tierGap).toBe(-3);
    expect(find("Same").tierGap).toBe(0);
    expect(find("Same").agrees).toBe(true);
    expect(find("ModelLikes").agrees).toBe(false);
  });

  it("counts agreement only across entries both sources placed", () => {
    const r = buildBands([
      g({ name: "Agree", tier_ours: "A", tier_community: "A" }),
      g({ name: "ModelUp", tier_ours: "S", tier_community: "B" }),
      g({ name: "MetaUp", tier_ours: "C", tier_community: "A" }),
      g({ name: "NoData", tier_community: null, community: null }),
    ]);
    expect(r.total).toBe(4);
    expect(r.ranked).toBe(3);
    expect(r.agreed).toBe(1);
    expect(r.modelHigher).toBe(1);
    expect(r.metaHigher).toBe(1);
    expect(r.unranked).toBe(1);
  });

  it("treats a missing community score as unranked even when a tier letter survives", () => {
    const r = buildBands([g({ name: "Half", community: null, tier_community: "A" })]);
    const e = r.bands[0].entries[0];
    expect(e.unranked).toBe(true);
    expect(e.delta).toBeNull();
    expect(e.agrees).toBe(false);
  });

  it("orders each band by the size of the disagreement, sinking unranked entries", () => {
    const r = buildBands([
      g({ name: "Small", tier_ours: "A", tier_community: "B", ours: 0.5, community: 0.48 }),
      g({ name: "NoData", tier_ours: "A", community: null, tier_community: null }),
      g({ name: "Big", tier_ours: "A", tier_community: "C", ours: 0.4, community: 0.7 }),
    ]);
    expect(r.bands[0].entries.map((e) => e.entry.name)).toEqual(["Big", "Small", "NoData"]);
  });

  it("ranks by tier distance, not raw score gap, so an agreeing entry never leads", () => {
    // "Disputed" means the tier letters differ. An entry both sources place in
    // the same tier must not outrank a real disagreement just because its
    // underlying scores happen to sit further apart.
    const r = buildBands([
      g({ name: "AgreesWideGap", tier_ours: "S", tier_community: "S", ours: 0.53, community: 0.72 }),
      g({ name: "DisputedNarrow", tier_ours: "S", tier_community: "B", ours: 0.55, community: 0.51 }),
    ]);
    expect(r.bands[0].entries.map((e) => e.entry.name)).toEqual(["DisputedNarrow", "AgreesWideGap"]);
  });

  it("falls back to the score gap when two entries are the same tier distance apart", () => {
    const r = buildBands([
      g({ name: "Near", tier_ours: "S", tier_community: "A", ours: 0.6, community: 0.58 }),
      g({ name: "Far", tier_ours: "S", tier_community: "A", ours: 0.6, community: 0.35 }),
    ]);
    expect(r.bands[0].entries.map((e) => e.entry.name)).toEqual(["Far", "Near"]);
  });

  it("can order by score instead, for the conventional reading", () => {
    const r = buildBands([
      g({ name: "Low", tier_ours: "A", ours: 0.4, community: 0.1 }),
      g({ name: "High", tier_ours: "A", ours: 0.9, community: 0.88 }),
    ], "score");
    expect(r.bands[0].entries.map((e) => e.entry.name)).toEqual(["High", "Low"]);
  });

  it("breaks ties on name so ordering is stable across renders", () => {
    const r = buildBands([
      g({ name: "Zeus", tier_ours: "A", ours: 0.5, community: 0.4 }),
      g({ name: "Agni", tier_ours: "A", ours: 0.6, community: 0.5 }),
    ]);
    expect(r.bands[0].entries.map((e) => e.entry.name)).toEqual(["Agni", "Zeus"]);
  });

  it("tallies per-band agreement", () => {
    const r = buildBands([
      g({ name: "A1", tier_ours: "S", tier_community: "S" }),
      g({ name: "A2", tier_ours: "S", tier_community: "B" }),
      g({ name: "A3", tier_ours: "S", community: null, tier_community: null }),
    ]);
    const s = r.bands[0];
    expect(s.agreed).toBe(1);
    expect(s.disagreed).toBe(1);
    expect(s.unranked).toBe(1);
  });

  it("keeps entries the model hasn't tiered out of the bands", () => {
    const r = buildBands([
      g({ name: "Tiered", tier_ours: "B" }),
      g({ name: "Untiered", tier_ours: null }),
    ]);
    expect(r.bands.flatMap((b) => b.entries.map((e) => e.entry.name))).toEqual(["Tiered"]);
    expect(r.untiered.map((e) => e.entry.name)).toEqual(["Untiered"]);
  });

  it("handles an empty list without inventing bands", () => {
    const r = buildBands([]);
    expect(r.bands).toEqual([]);
    expect(r.total).toBe(0);
    expect(r.ranked).toBe(0);
    expect(r.agreed).toBe(0);
  });
});

/* Home names six real arguments — three gods, three items — instead of
 * charting how far each lane leans. This is the pick. */
describe("biggestArguments", () => {
  it("ranks by rungs apart, in either direction, biggest first", () => {
    const r = biggestArguments([
      g({ name: "OneRung", tier_ours: "B", tier_community: "A" }),
      g({ name: "ThreeUp", tier_ours: "S", tier_community: "C" }),
      g({ name: "TwoDown", tier_ours: "C", tier_community: "A" }),
    ], 3);
    expect(r.top.map((a) => a.entry.name)).toEqual(["ThreeUp", "TwoDown", "OneRung"]);
    expect(r.top.map((a) => a.verdict)).toEqual(["underrated", "overrated", "overrated"]);
  });

  it("never offers an agreement as an argument", () => {
    const r = biggestArguments([
      g({ name: "Agrees", tier_ours: "B", tier_community: "B", ours: 0.9, community: 0.1 }),
      g({ name: "Argues", tier_ours: "A", tier_community: "B" }),
    ], 3);
    // A huge raw-score gap inside one tier is still not a disagreement about
    // placement, which is what this list is about.
    expect(r.top.map((a) => a.entry.name)).toEqual(["Argues"]);
  });

  it("reports what the shown few are a sample of", () => {
    const r = biggestArguments([
      g({ name: "A", tier_ours: "S", tier_community: "C" }),
      g({ name: "B", tier_ours: "A", tier_community: "C" }),
      g({ name: "C", tier_ours: "B", tier_community: "C" }),
      g({ name: "Agrees", tier_ours: "B", tier_community: "B" }),
      g({ name: "NoData", tier_ours: "B", tier_community: null, community: null }),
    ], 2);
    expect(r.top).toHaveLength(2);
    // Disputed counts every disagreement, not just the two drawn; unranked
    // entries are outside the comparison entirely.
    expect(r.disputed).toBe(3);
    expect(r.ranked).toBe(4);
  });

  it("handles an empty or absent list without inventing an argument", () => {
    for (const input of [undefined, []]) {
      const r = biggestArguments(input, 3);
      expect(r).toEqual({ top: [], disputed: 0, ranked: 0 });
    }
  });
});

/* A reader generalises from the handful they're shown, so a list whose
 * extremes all run one way would assert a lean the full set doesn't have. */
describe("biggestArguments — showing both directions", () => {
  it("gives the last slot to the other direction when the extremes all agree", () => {
    const r = biggestArguments([
      g({ name: "Over3", tier_ours: "C", tier_community: "S" }),
      g({ name: "Over2", tier_ours: "C", tier_community: "A" }),
      g({ name: "Over1", tier_ours: "B", tier_community: "A", ours: 0.5, community: 0.9 }),
      g({ name: "Under1", tier_ours: "A", tier_community: "B" }),
    ], 3);
    // Over1 is the third-biggest, but it would have made the list uniformly
    // one-directional, so the strongest argument the other way takes the slot.
    expect(r.top.map((a) => a.entry.name)).toEqual(["Over3", "Over2", "Under1"]);
  });

  it("leaves a naturally mixed list alone", () => {
    const r = biggestArguments([
      g({ name: "Over3", tier_ours: "C", tier_community: "S" }),
      g({ name: "Under2", tier_ours: "S", tier_community: "B" }),
      g({ name: "Over1", tier_ours: "B", tier_community: "A" }),
      g({ name: "Under1", tier_ours: "A", tier_community: "B" }),
    ], 3);
    expect(r.top.map((a) => a.entry.name)).toEqual(["Over3", "Under2", "Over1"]);
  });

  it("stays one-directional when the data genuinely only runs one way", () => {
    const r = biggestArguments([
      g({ name: "Over2", tier_ours: "C", tier_community: "A" }),
      g({ name: "Over1", tier_ours: "B", tier_community: "A" }),
    ], 3);
    expect(r.top.map((a) => a.verdict)).toEqual(["overrated", "overrated"]);
  });
});
