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

/* B6: the per-item damage channel. The tag/stat channels describe an item by
 * its properties; this one carries a number measured for THAT item against the
 * comp actually on the board. */
describe("adaptedCore — the damage channel", () => {
  const items = [item("Pen", { Penetration: "20%" }), item("Power", { Intelligence: "100" })];
  const byName = Object.fromEntries(items.map((i) => [i.name, i]));
  const base = { Pen: 0.5, Power: 0.52 };

  it("can promote an item on damage alone", () => {
    const flat = adaptedCore(base, byName, { tags: {}, stats: {} }, { maxBonus: 0.12, n: 1 });
    expect(flat.core).toEqual(["Power"]);
    const withDamage = adaptedCore(base, byName,
      { tags: {}, stats: {}, items: { Pen: 0.05 } }, { maxBonus: 0.12, n: 1 });
    expect(withDamage.core).toEqual(["Pen"]);
  });

  it("says why, in the diff's own language", () => {
    const r = adaptedCore(base, byName,
      { tags: {}, stats: {}, items: { Pen: 0.05 } }, { maxBonus: 0.12, n: 2 });
    expect(r.reasons["Pen"]).toContain("damage vs their build");
  });

  it("names a negative shift as a loss rather than a gain", () => {
    const r = adaptedCore(base, byName,
      { tags: {}, stats: {}, items: { Power: -0.05 } }, { maxBonus: 0.12, n: 2 });
    expect(r.reasons["Power"]).toContain("less damage");
  });

  it("is still bounded by maxBonus, like every other channel", () => {
    const r = adaptedCore(base, byName,
      { tags: {}, stats: {}, items: { Pen: 5 } }, { maxBonus: 0.12, n: 2 });
    expect(r.bonuses["Pen"]).toBe(0.12);
  });

  it("changes nothing when the overlay carries no item channel", () => {
    const without = adaptedCore(base, byName, { tags: {}, stats: {} }, { maxBonus: 0.12, n: 2 });
    const empty = adaptedCore(base, byName, { tags: {}, stats: {}, items: {} }, { maxBonus: 0.12, n: 2 });
    expect(empty).toEqual(without);
  });
});

/* THE SWAP HAS TO BE BETTER GIVEN THE OTHER FIVE SLOTS.
 *
 * `threats.ts` already damps a threat one of your ALLIES covers (`ally_covered`)
 * — but nothing asked whether your own core already covered it, so the overlay
 * paid the full anti-heal bonus to a second anti-heal item while the first was
 * sitting in the build, and that second copy displaced whatever the build still
 * genuinely needed. */
describe("adaptedCore — a job already done isn't paid for twice", () => {
  const items: Record<string, Item> = {
    AntiHeal1: { name: "AntiHeal1", stats: {}, effect_tags: ["anti-heal"] },
    AntiHeal2: { name: "AntiHeal2", stats: {}, effect_tags: ["anti-heal"] },
    Needed: { name: "Needed", stats: {}, effect_tags: [] },
  } as unknown as Record<string, Item>;
  // Needed out-scores AntiHeal2 on merit; the overlay is what promotes it.
  const base = { AntiHeal1: 0.60, Needed: 0.52, AntiHeal2: 0.50 };
  const overlay = { tags: { "anti-heal": 0.10 }, stats: {} };

  it("pays in full for the FIRST answer to a threat", () => {
    const r = adaptedCore(base, items, overlay, { maxBonus: 1, n: 1, selfCovered: 0 });
    expect(r.core).toEqual(["AntiHeal1"]);
    expect(r.bonuses.AntiHeal1).toBeCloseTo(0.10);
  });

  it("does not let a second copy displace what the build still needs", () => {
    const full = adaptedCore(base, items, overlay, { maxBonus: 1, n: 2, selfCovered: 1 });
    expect(full.core).toEqual(["AntiHeal1", "AntiHeal2"]);   // the old behaviour

    const damped = adaptedCore(base, items, overlay, { maxBonus: 1, n: 2, selfCovered: 0 });
    expect(damped.core).toEqual(["AntiHeal1", "Needed"]);
  });

  it("still lets a second copy in when it is better on merit anyway", () => {
    // AntiHeal2 now beats Needed without any overlay help at all.
    const strong = { AntiHeal1: 0.60, AntiHeal2: 0.55, Needed: 0.50 };
    const r = adaptedCore(strong, items, overlay, { maxBonus: 1, n: 2, selfCovered: 0 });
    expect(r.core).toEqual(["AntiHeal1", "AntiHeal2"]);
  });

  it("names the damping in the reason, so the row can explain itself", () => {
    const r = adaptedCore(base, items, overlay, { maxBonus: 1, n: 2, selfCovered: 0.5 });
    expect(r.reasons.AntiHeal1).toBe("anti-heal");
    expect(r.reasons.AntiHeal2).toContain("already covered");
  });

  /* A penalty is not a job that can be "already done". Damping it would
   * quietly re-promote the very items the overlay is pushing down. */
  it("never damps a negative bonus", () => {
    const penalised = { A: 0.60, B: 0.59 };
    const its: Record<string, Item> = {
      A: { name: "A", stats: {}, effect_tags: ["mobility"] },
      B: { name: "B", stats: {}, effect_tags: ["mobility"] },
    } as unknown as Record<string, Item>;
    const r = adaptedCore(penalised, its, { tags: { mobility: -0.10 }, stats: {} },
                          { maxBonus: 1, n: 2, selfCovered: 0 });
    expect(r.bonuses.A).toBeCloseTo(-0.10);
    expect(r.bonuses.B).toBeCloseTo(-0.10);
  });

  it("is unchanged from the old single-sort behaviour at selfCovered = 1", () => {
    const r = adaptedCore(base, items, overlay, { maxBonus: 1, n: 3, selfCovered: 1 });
    expect(r.core).toEqual(["AntiHeal1", "AntiHeal2", "Needed"]);
  });

  /* Per-item damage is measured against the enemy build for THIS item; no
   * other slot can do that job for it. */
  it("never damps the per-item damage channel", () => {
    const its: Record<string, Item> = {
      A: { name: "A", stats: { Penetration: "20" }, effect_tags: [] },
      B: { name: "B", stats: { Penetration: "20" }, effect_tags: [] },
    } as unknown as Record<string, Item>;
    const r = adaptedCore({ A: 0.6, B: 0.5 }, its,
      { tags: {}, stats: {}, items: { A: 0.05, B: 0.05 } },
      { maxBonus: 1, n: 2, selfCovered: 0 });
    expect(r.bonuses.A).toBeCloseTo(0.05);
    expect(r.bonuses.B).toBeCloseTo(0.05);
  });
});

/* The clamp bounds how much a comp may rewrite a build. Applied to the SUM
 * alone it also vetoed a single well-evidenced channel, and that was the case
 * it hurt most: because a healer comp is also a CC and tank comp, anti-heal
 * shared one fixed budget with penetration and cc-immunity and lost.
 *
 * Measured on the shipped data before and after, with the real overlay: of the
 * 31 gods who can buy anti-heal at all, 16 did against 4 of 5 healers; now 31
 * do. Nothing else moved — a 2-healer comp, a 1-healer comp and a no-healer
 * comp are byte-identical either way. The sharpest symptom of the old rule was
 * that 2 healers and 4 healers produced the SAME build: the bonus doubled and
 * the clamp ate the difference. */
describe("adaptedCore — the clamp bounds the stack, not the strongest channel", () => {
  const opts = { maxBonus: 0.12 };
  // `bonuses` only records items that made the core, so the item under test
  // carries a base high enough to survive even the penalty case.
  const MARK = item("Mark", { A: "1", B: "1", C: "1" }, ["anti-heal"]);
  const ITEMS2 = { ...byName, Mark: MARK };
  const BASE2 = { ...BASE, Mark: 0.9 };

  it("lets one well-evidenced channel exceed the flat clamp", () => {
    const r = adaptedCore(BASE2, ITEMS2, { tags: { "anti-heal": 0.24 }, stats: {} }, opts);
    expect(r.bonuses.Mark).toBeCloseTo(0.24, 6);
  });

  it("still bounds many weak channels stacking into a rewrite", () => {
    // Four small channels summing past the clamp is exactly the failure the
    // clamp exists for, and none of them individually earned more than 0.12.
    const r = adaptedCore(BASE2, ITEMS2, {
      tags: { "anti-heal": 0.05 }, stats: { A: 0.05, B: 0.05, C: 0.05 },
    }, opts);
    expect(r.bonuses.Mark).toBeCloseTo(0.12, 6);  // 0.20 earned, clamped
  });

  it("distinguishes a 2-of-5 threat from a 4-of-5 one", () => {
    // The old rule could not: both saturated the flat clamp and produced the
    // same build, so the draft was blind to twice the evidence. Measured on
    // the shipped data, 2 healers and 4 healers gave 16/31 gods either way.
    const weak = adaptedCore(BASE2, ITEMS2, { tags: { "anti-heal": 0.12 }, stats: {} }, opts);
    const strong = adaptedCore(BASE2, ITEMS2, { tags: { "anti-heal": 0.24 }, stats: {} }, opts);
    expect(strong.bonuses.Mark).toBeGreaterThan(weak.bonuses.Mark);
  });

  it("does not widen the floor for a penalty", () => {
    // A penalty is not a well-evidenced answer to anything, and letting a
    // strong positive channel widen the negative bound would push items down
    // harder than the overlay intended.
    const r = adaptedCore(BASE2, ITEMS2, { tags: { "anti-heal": -0.4 }, stats: {} }, opts);
    expect(r.bonuses.Mark).toBeCloseTo(-0.12, 6);
  });

  it("leaves an item with no channels untouched", () => {
    const r = adaptedCore(BASE2, ITEMS2, { tags: { "anti-heal": 0.24 }, stats: {} }, opts);
    expect(r.bonuses.Alpha).toBeUndefined();
  });
});
