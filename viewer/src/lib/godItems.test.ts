import { describe, it, expect } from "vitest";
import { buildGodItems, scoreBarPercent } from "./godItems";
import type { Item } from "../types";

const item = (name: string, cost: number, residual: number | null = null): Item => ({
  type: "item", name, tier: 3, cost, stats: {}, passive: "",
  builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: null,
  efficiency: residual == null ? null : { predicted_cost: cost - residual, residual, score: 0.5 },
} as unknown as Item);

const byName = new Map([
  ["Rage", item("Rage", 2500, -400)],
  ["Aegis", item("Aegis", 2100, 300)],
  ["Deathbringer", item("Deathbringer", 3000)],
]);

describe("buildGodItems", () => {
  it("ranks best score first", () => {
    const r = buildGodItems({ Aegis: 0.41, Rage: 0.49, Deathbringer: 0.45 }, byName);
    expect(r.rows.map((x) => x.name)).toEqual(["Rage", "Deathbringer", "Aegis"]);
    expect(r.rows.map((x) => x.rank)).toEqual([1, 2, 3]);
  });

  /* The index rounds scores to four places and they genuinely tie — Eye of
   * Providence and Eye of the Storm both sit at 0.4592 for Achilles. Falling
   * back to JSON key order would make the ranking depend on the serializer. */
  it("breaks ties by name rather than by insertion order", () => {
    const r = buildGodItems({ Rage: 0.45, Aegis: 0.45, Deathbringer: 0.45 }, byName);
    expect(r.rows.map((x) => x.name)).toEqual(["Aegis", "Deathbringer", "Rage"]);
  });

  it("joins price and gold-model residual from the index", () => {
    const r = buildGodItems({ Rage: 0.49 }, byName);
    expect(r.rows[0].cost).toBe(2500);
    expect(r.rows[0].residual).toBe(-400);
  });

  it("reports an unpriced item as unpriced rather than zero", () => {
    const r = buildGodItems({ Deathbringer: 0.45 }, byName);
    expect(r.rows[0].cost).toBe(3000);
    expect(r.rows[0].residual).toBeNull();
  });

  // Counted rather than dropped: a shorter list with no explanation reads as
  // the model having fewer opinions than it does.
  it("keeps a scored item the index has no entry for, and names it", () => {
    const r = buildGodItems({ Rage: 0.49, Phantom: 0.42 }, byName);
    expect(r.missing).toEqual(["Phantom"]);
    expect(r.rows.map((x) => x.name)).toContain("Phantom");
    expect(r.rows.find((x) => x.name === "Phantom")!.cost).toBeUndefined();
  });

  it("marks the god's own core in place", () => {
    const r = buildGodItems({ Rage: 0.49, Aegis: 0.41 }, byName, ["Rage"]);
    expect(r.rows.find((x) => x.name === "Rage")!.inCore).toBe(true);
    expect(r.rows.find((x) => x.name === "Aegis")!.inCore).toBe(false);
  });

  it("reports how much of the core the ranking actually covers", () => {
    const r = buildGodItems({ Rage: 0.49 }, byName, ["Rage", "Aegis", "Deathbringer"]);
    expect(r.coreCovered).toBe(1);
    expect(r.coreSize).toBe(3);
  });

  it("reports the spread, so a surface can say how close the ranking is", () => {
    const r = buildGodItems({ Rage: 0.49, Aegis: 0.41 }, byName);
    expect(r.spread).toBeCloseTo(0.08, 5);
  });

  /* Item fit is one of four signals behind a build, so the core usually isn't
   * the top of this ranking — Ra's skips rank 4. A surface saying "the build
   * takes the top six" has to check rather than assume. */
  it("knows whether the core really is the top of the ranking", () => {
    const top = buildGodItems({ Rage: 0.49, Aegis: 0.41, Deathbringer: 0.45 }, byName, ["Rage", "Deathbringer"]);
    expect(top.coreIsTop).toBe(true);

    const skips = buildGodItems({ Rage: 0.49, Aegis: 0.41, Deathbringer: 0.45 }, byName, ["Rage", "Aegis"]);
    expect(skips.coreIsTop).toBe(false);   // Deathbringer outranks Aegis
  });

  it("is never top-of-ranking with no core, or an incompletely scored one", () => {
    expect(buildGodItems({ Rage: 0.49 }, byName, []).coreIsTop).toBe(false);
    expect(buildGodItems({ Rage: 0.49 }, byName, ["Rage", "Ghost"]).coreIsTop).toBe(false);
  });

  it("survives a god with no scores at all", () => {
    const r = buildGodItems(undefined, byName);
    expect(r.rows).toEqual([]);
    expect(r.spread).toBeNull();
    expect(r.coreCovered).toBe(0);
  });

  it("has no spread to report for a single scored item", () => {
    expect(buildGodItems({ Rage: 0.49 }, byName).spread).toBeNull();
  });
});

describe("scoreBarPercent", () => {
  /* Real scores cluster inside about 0.1. Drawn from zero, all 40 bars would
   * be full and the ordering invisible; stretched across the actual range,
   * the ranking is the thing you see. */
  it("stretches the observed range across the track", () => {
    expect(scoreBarPercent(0.49, 0.49, 0.39)).toBe(100);
    expect(scoreBarPercent(0.39, 0.49, 0.39)).toBe(8);
  });

  it("keeps the worst bar visible rather than zero-width", () => {
    expect(scoreBarPercent(0.39, 0.49, 0.39)).toBeGreaterThan(0);
  });

  it("falls back to a full bar when every score is identical", () => {
    expect(scoreBarPercent(0.45, 0.45, 0.45)).toBe(100);
  });
});
