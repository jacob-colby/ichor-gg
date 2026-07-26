import { describe, it, expect } from "vitest";
import { adaptedCore, diffCore } from "./draftBuild";
import type { Item } from "../types";

const item = (name: string, stats: Record<string, string> = {}, tags: string[] = []): Item =>
  ({ name, tier: 3, cost: 2500, stats, passive: "", builds_from: [], builds_into: [],
     effect_tags: tags, efficiency_tier: null } as unknown as Item);

const ITEMS = [
  item("Alpha"), item("Beta"), item("Gamma"), item("Delta"),
  item("Epsilon"), item("Zeta"), item("AntiHeal", {}, ["anti-heal"]),
  item("Boots1", { "Movement Speed": "18%" }), item("Boots2", { "Movement Speed": "18%" }),
  item("Sustain1", { Lifesteal: "10%" }), item("Sustain2", {}, ["sustain"]),
];
const BASE: Record<string, number> = {
  Alpha: 0.6, Beta: 0.59, Gamma: 0.58, Delta: 0.57, Epsilon: 0.56, Zeta: 0.55,
  AntiHeal: 0.40, Boots1: 0.54, Boots2: 0.53, Sustain1: 0.52, Sustain2: 0.51,
};
const byName = Object.fromEntries(ITEMS.map((i) => [i.name, i]));

it("returns the base top-6 when there is no threat overlay", () => {
  const r = adaptedCore(BASE, byName, { tags: {}, stats: {} }, { maxBonus: 0.12 });
  expect(r.core).toEqual(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"]);
});

it("promotes an item whose tag the overlay rewards, with a reason", () => {
  const r = adaptedCore(BASE, byName, { tags: { "anti-heal": 0.3 }, stats: {} },
    { maxBonus: 0.5 });
  expect(r.core).toContain("AntiHeal");
  expect(r.reasons["AntiHeal"]).toMatch(/anti-heal/i);
});

it("clamps the total bonus so a huge overlay cannot fully rewrite the build", () => {
  const r = adaptedCore(BASE, byName, { tags: { "anti-heal": 99 }, stats: {} },
    { maxBonus: 0.12 });
  const changed = r.core.filter((n) => !["Alpha","Beta","Gamma","Delta","Epsilon","Zeta"].includes(n));
  expect(changed.length).toBeLessThanOrEqual(3);
});

it("allows at most one boots", () => {
  const base = { ...BASE, Boots1: 0.99, Boots2: 0.98 };
  const r = adaptedCore(base, byName, { tags: {}, stats: {} }, { maxBonus: 0.12 });
  expect(r.core.filter((n) => n.startsWith("Boots")).length).toBe(1);
});

it("respects the lifesteal cap", () => {
  const base = { ...BASE, Sustain1: 0.99, Sustain2: 0.98 };
  const r = adaptedCore(base, byName, { tags: {}, stats: {} }, { maxBonus: 0.12, maxLifesteal: 1 });
  expect(r.core.filter((n) => n.startsWith("Sustain")).length).toBe(1);
});

it("always returns six unique items", () => {
  const r = adaptedCore(BASE, byName, { tags: {}, stats: {} }, { maxBonus: 0.12 });
  expect(r.core).toHaveLength(6);
  expect(new Set(r.core).size).toBe(6);
});

describe("determinism", () => {
  it("sorts ties by name ascending regardless of base-object key order", () => {
    const tiedItems = [item("Zed"), item("Ana"), item("Mno")];
    const tiedByName = Object.fromEntries(tiedItems.map((i) => [i.name, i]));
    // Insert keys in an order that does NOT match alphabetical, all equal score.
    const tiedBase: Record<string, number> = { Zed: 0.5, Ana: 0.5, Mno: 0.5 };
    const r = adaptedCore(tiedBase, tiedByName, { tags: {}, stats: {} },
      { maxBonus: 0.12, n: 3 });
    expect(r.core).toEqual(["Ana", "Mno", "Zed"]);
  });
});

describe("diffCore", () => {
  const core = (names: string[], bonuses: Record<string, number> = {}, reasons: Record<string, string> = {}) =>
    ({ core: names, bonuses, reasons });

  it("pairs each arrival with the departure it displaced", () => {
    const d = diffCore(
      core(["A", "B", "C"]),
      core(["A", "X", "C"], { X: 0.07 }, { X: "anti-heal" }),
    );
    expect(d.changes).toEqual([{ added: "X", removed: "B", bonus: 0.07, reason: "anti-heal" }]);
    expect(d.unchanged).toEqual(["A", "C"]);
    expect(d.droppedOnly).toEqual([]);
  });

  it("carries the bonus that moved each item — the number the page used to discard", () => {
    const d = diffCore(core(["A", "B"]), core(["X", "Y"], { X: 0.12, Y: 0.03 }));
    expect(d.changes.map((c) => c.bonus)).toEqual([0.12, 0.03]);
  });

  it("reports no changes when the draft moved nothing", () => {
    const d = diffCore(core(["A", "B", "C"]), core(["A", "B", "C"]));
    expect(d.changes).toEqual([]);
    expect(d.unchanged).toEqual(["A", "B", "C"]);
  });

  it("treats a pure reorder as unchanged — the same six items are the same build", () => {
    const d = diffCore(core(["A", "B", "C"]), core(["C", "A", "B"]));
    expect(d.changes).toEqual([]);
    expect(d.unchanged).toEqual(["C", "A", "B"]);
  });

  it("pairs multiple swaps by rank within each list", () => {
    const d = diffCore(core(["A", "B", "C"]), core(["X", "Y", "C"], { X: 0.1, Y: 0.05 }));
    expect(d.changes).toEqual([
      { added: "X", removed: "A", bonus: 0.1, reason: undefined },
      { added: "Y", removed: "B", bonus: 0.05, reason: undefined },
    ]);
  });

  it("records a departure with no matching arrival rather than dropping it silently", () => {
    const d = diffCore(core(["A", "B", "C"]), core(["X", "C"], { X: 0.1 }));
    expect(d.changes).toEqual([{ added: "X", removed: "A", bonus: 0.1, reason: undefined }]);
    expect(d.droppedOnly).toEqual(["B"]);
  });

  it("defaults a missing bonus to zero rather than undefined", () => {
    const d = diffCore(core(["A"]), core(["X"]));
    expect(d.changes[0].bonus).toBe(0);
  });

  it("handles empty builds", () => {
    const d = diffCore(core([]), core([]));
    expect(d).toEqual({ changes: [], unchanged: [], droppedOnly: [] });
  });
});
