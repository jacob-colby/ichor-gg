import { describe, it, expect } from "vitest";
import { adaptFromCore, diffCore } from "./draftBuild";
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
/** The candidate pool — `god_item_scores` for one god in one mode. It ranks
 *  candidates against each other and nothing else; it does NOT decide the six.
 *  Deliberately DISAGREES with SHIPPED below (Boots1 outscores Zeta), because
 *  that disagreement is the bug this module exists to stop the draft acting
 *  on: `assemble_core_converged` re-prices during assembly and these totals
 *  are from before it. */
const BASE: Record<string, number> = {
  Alpha: 0.6, Beta: 0.59, Gamma: 0.58, Delta: 0.57, Epsilon: 0.56, Zeta: 0.55,
  AntiHeal: 0.40, Boots1: 0.54, Boots2: 0.53, Sustain1: 0.52, Sustain2: 0.51,
};
/** What the pipeline actually assembled and the god page actually shows. */
const SHIPPED = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"];
const byName = Object.fromEntries(ITEMS.map((i) => [i.name, i]));

const adapt = (
  overlay: Parameters<typeof adaptFromCore>[3],
  opts: Partial<Parameters<typeof adaptFromCore>[4]> = {},
  shipped: string[] = SHIPPED,
  base: Record<string, number> = BASE,
) => adaptFromCore(shipped, base, byName, overlay, { maxBonus: 0.12, ...opts });

const NONE = { tags: {}, stats: {} };

it("returns the pipeline's core verbatim when there is no threat overlay", () => {
  expect(adapt(NONE).core).toEqual(SHIPPED);
});

/* THE BUG THIS MODULE EXISTS FOR. `Boots1` outranks `Zeta` in the score table
 * and the pipeline still did not put it in the core — because it re-prices as
 * it fills and the shipped totals are from before that. The old draft read the
 * table, re-assembled, and produced a different build from the god page for
 * 2,057 of 2,247 build groups. A disagreement in the table is the pipeline's
 * to have; it is not the draft's to act on. */
it("does not second-guess the pipeline with the score table", () => {
  const r = adapt(NONE, {}, SHIPPED, { ...BASE, Boots1: 0.99, AntiHeal: 0.98 });
  expect(r.core).toEqual(SHIPPED);
});

it("promotes an item whose tag the overlay rewards, with a reason", () => {
  const r = adapt({ tags: { "anti-heal": 0.3 }, stats: {} }, { maxBonus: 0.12 });
  expect(r.core).toContain("AntiHeal");
  expect(r.reasons["AntiHeal"]).toMatch(/anti-heal/i);
});

/* The draft may only spend what the comp earned. A bonus under the bar is
 * evidence too weak to displace a slot the pipeline chose, and the old code
 * had no such test at all — anything that out-scored the sixth item went in. */
it("refuses a swap the overlay did not pay for", () => {
  const r = adapt({ tags: { "anti-heal": 0.11 }, stats: {} }, { maxBonus: 0.12 });
  expect(r.core).toEqual(SHIPPED);
  const paid = adapt({ tags: { "anti-heal": 0.12 }, stats: {} }, { maxBonus: 0.12 });
  expect(paid.core).toContain("AntiHeal");
});

it("takes the slot the pipeline is least sure about, when it says which", () => {
  const withFlex = adapt({ tags: { "anti-heal": 0.3 }, stats: {} },
    { maxBonus: 0.12, flexSlots: ["Gamma"] });
  expect(withFlex.core).toEqual(["Alpha", "Beta", "AntiHeal", "Delta", "Epsilon", "Zeta"]);
  // With no flex marked it spends the LAST slot, which is the same rule the
  // god page's `applySwap` falls back to.
  const without = adapt({ tags: { "anti-heal": 0.3 }, stats: {} }, { maxBonus: 0.12 });
  expect(without.core).toEqual(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "AntiHeal"]);
});

it("clamps the total bonus so a huge overlay cannot fully rewrite the build", () => {
  const r = adapt({ tags: { "anti-heal": 99 }, stats: {} }, { maxBonus: 0.12 });
  expect(r.core.filter((n) => !SHIPPED.includes(n)).length).toBeLessThanOrEqual(3);
});

it("allows at most one boots — an arriving boots displaces the boots", () => {
  const shipped = ["Boots1", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"];
  const r = adapt({ tags: { "anti-heal": 0.3 }, stats: {} }, { maxBonus: 0.12 },
    shipped, { ...BASE, Boots2: 0.99 });
  expect(r.core.filter((n) => n.startsWith("Boots")).length).toBe(1);
});

it("respects the lifesteal cap", () => {
  const shipped = ["Sustain1", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"];
  const r = adapt({ tags: { sustain: 0.3 }, stats: {} }, { maxBonus: 0.12, maxLifesteal: 1 },
    shipped, { ...BASE, Sustain2: 0.99 });
  expect(r.core.filter((n) => n.startsWith("Sustain")).length).toBe(1);
});

it("always returns six unique items", () => {
  const r = adapt({ tags: { "anti-heal": 0.3 }, stats: {} });
  expect(r.core).toHaveLength(6);
  expect(new Set(r.core).size).toBe(6);
});

describe("determinism", () => {
  it("breaks ties between arrivals by name, not by base-object key order", () => {
    const its = { ...byName, Zed: item("Zed", {}, ["anti-heal"]), Ana: item("Ana", {}, ["anti-heal"]) };
    // Insert keys in an order that does NOT match alphabetical, equal score.
    const base = { ...BASE, Zed: 0.5, Ana: 0.5 };
    const r = adaptFromCore(SHIPPED, base, its, { tags: { "anti-heal": 0.3 }, stats: {} },
      { maxBonus: 0.12 });
    expect(r.core[5]).toBe("Ana");
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

  /* This test used to assert the opposite — "a pure reorder is unchanged, the
     same six items are the same build" — and that was the bug, written down.
     A build asserts an ORDER; `assemble.build_order` on the pipeline side
     treats buy order as something the community record can contradict. The
     board reported `added: []`, `removed: []` under a list that had visibly
     moved. */
  it("reports a pure reorder as a change, not as nothing", () => {
    const d = diffCore(core(["A", "B", "C"]), core(["C", "A", "B"]));
    expect(d.changes).toEqual([]);
    expect(d.unchanged).toEqual(["C", "A", "B"]);
    expect(d.orderOnly).toBe(true);
    expect(d.moved).toEqual([
      { name: "C", from: 3, to: 1, bonus: 0, reason: undefined },
      { name: "A", from: 1, to: 2, bonus: 0, reason: undefined },
      { name: "B", from: 2, to: 3, bonus: 0, reason: undefined },
    ]);
  });

  it("carries the reason a reordered item was promoted", () => {
    const d = diffCore(
      core(["A", "B"]),
      core(["B", "A"], { B: 0.09 }, { B: "anti-heal" }),
    );
    expect(d.orderOnly).toBe(true);
    expect(d.moved[0]).toEqual({ name: "B", from: 2, to: 1, bonus: 0.09, reason: "anti-heal" });
  });

  it("is not orderOnly when something actually swapped, even if others moved", () => {
    const d = diffCore(core(["A", "B", "C"]), core(["X", "C", "A"], { X: 0.1 }));
    expect(d.orderOnly).toBe(false);
    expect(d.moved.map((m) => m.name)).toEqual(["C", "A"]);
  });

  it("leaves `moved` empty when the order is identical", () => {
    const d = diffCore(core(["A", "B", "C"]), core(["A", "B", "C"]));
    expect(d.moved).toEqual([]);
    expect(d.orderOnly).toBe(false);
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
    expect(d).toEqual({ changes: [], unchanged: [], droppedOnly: [], moved: [], orderOnly: false });
  });
});

/* B6: the per-item damage channel. The tag/stat channels describe an item by
 * its properties; this one carries a number measured for THAT item against the
 * comp actually on the board. */
describe("adaptFromCore — the damage channel", () => {
  const items = { ...byName, Pen: item("Pen", { Penetration: "20%" }),
    Power: item("Power", { Intelligence: "100" }) };
  const base = { ...BASE, Pen: 0.5, Power: 0.52 };
  const shippedWithPen = ["Pen", "Alpha", "Beta", "Gamma", "Delta", "Epsilon"];
  const shippedWithout = ["Power", "Alpha", "Beta", "Gamma", "Delta", "Epsilon"];

  it("can bring an item in on damage alone", () => {
    const flat = adaptFromCore(shippedWithout, base, items, NONE, { maxBonus: 0.05 });
    expect(flat.core).toEqual(shippedWithout);
    const withDamage = adaptFromCore(shippedWithout, base, items,
      { tags: {}, stats: {}, items: { Pen: 0.05 } }, { maxBonus: 0.05 });
    expect(withDamage.core).toContain("Pen");
  });

  it("says why, in the diff's own language", () => {
    const r = adaptFromCore(shippedWithPen, base, items,
      { tags: {}, stats: {}, items: { Pen: 0.05 } }, { maxBonus: 0.12 });
    expect(r.reasons["Pen"]).toContain("damage vs their build");
  });

  it("names a negative shift as a loss rather than a gain", () => {
    const r = adaptFromCore(shippedWithout, base, items,
      { tags: {}, stats: {}, items: { Power: -0.05 } }, { maxBonus: 0.12 });
    expect(r.reasons["Power"]).toContain("less damage");
  });

  it("is still bounded by maxBonus, like every other channel", () => {
    const r = adaptFromCore(shippedWithPen, base, items,
      { tags: {}, stats: {}, items: { Pen: 5 } }, { maxBonus: 0.12 });
    expect(r.bonuses["Pen"]).toBe(0.12);
  });

  it("changes nothing when the overlay carries no item channel", () => {
    const without = adaptFromCore(shippedWithPen, base, items, NONE, { maxBonus: 0.12 });
    const empty = adaptFromCore(shippedWithPen, base, items,
      { tags: {}, stats: {}, items: {} }, { maxBonus: 0.12 });
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
describe("adaptFromCore — a job already done isn't paid for twice", () => {
  const items: Record<string, Item> = {
    AntiHeal1: { name: "AntiHeal1", stats: {}, effect_tags: ["anti-heal"] },
    AntiHeal2: { name: "AntiHeal2", stats: {}, effect_tags: ["anti-heal"] },
    Needed: { name: "Needed", stats: {}, effect_tags: [] },
    Filler: { name: "Filler", stats: {}, effect_tags: [] },
  } as unknown as Record<string, Item>;
  const base = { AntiHeal1: 0.60, Needed: 0.52, AntiHeal2: 0.50, Filler: 0.40 };
  const overlay = { tags: { "anti-heal": 0.10 }, stats: {} };
  // The pipeline already bought the first answer; `Needed` is the slot a second
  // copy would take.
  const shipped = ["AntiHeal1", "Needed"];

  it("pays in full for the FIRST answer to a threat", () => {
    const r = adaptFromCore(["AntiHeal1", "Filler"], base, items, overlay,
      { maxBonus: 1, selfCovered: 0 });
    expect(r.bonuses.AntiHeal1).toBeCloseTo(0.10);
  });

  it("does not let a second copy displace what the build still needs", () => {
    // The bar is `maxBonus`, so at 0.10 an UNDAMPED second copy clears it by
    // exactly the amount the first one earned — the old behaviour, kept
    // reachable so the damping is measured against something.
    const full = adaptFromCore(shipped, base, items, overlay,
      { maxBonus: 0.10, selfCovered: 1 });
    expect(full.core).toEqual(["AntiHeal1", "AntiHeal2"]);

    const damped = adaptFromCore(shipped, base, items, overlay,
      { maxBonus: 0.10, selfCovered: 0 });
    expect(damped.core).toEqual(shipped);
  });

  it("still answers a threat the core does NOT already cover", () => {
    // The damping is keyed on the exact overlay key, so a build with no
    // anti-heal in it pays in full and the swap goes through — which is the
    // half of this rule that has to keep working.
    const r = adaptFromCore(["Filler", "Needed"], base, items, overlay,
      { maxBonus: 0.10, selfCovered: 0 });
    expect(r.core).toContain("AntiHeal1");
  });

  it("names the damping in the reason, so the row can explain itself", () => {
    const r = adaptFromCore(["AntiHeal1", "AntiHeal2"], base, items, overlay,
      { maxBonus: 1, selfCovered: 0.5 });
    expect(r.reasons.AntiHeal1).toContain("already covered");
    expect(r.reasons.AntiHeal2).toContain("already covered");
  });

  /* A penalty is not a job that can be "already done". Damping it would
   * quietly re-promote the very items the overlay is pushing down. */
  it("never damps a negative bonus", () => {
    const its: Record<string, Item> = {
      A: { name: "A", stats: {}, effect_tags: ["mobility"] },
      B: { name: "B", stats: {}, effect_tags: ["mobility"] },
    } as unknown as Record<string, Item>;
    const r = adaptFromCore(["A", "B"], { A: 0.60, B: 0.59 }, its,
      { tags: { mobility: -0.10 }, stats: {} }, { maxBonus: 1, selfCovered: 0 });
    expect(r.bonuses.A).toBeCloseTo(-0.10);
    expect(r.bonuses.B).toBeCloseTo(-0.10);
  });

  /* Per-item damage is measured against the enemy build for THIS item; no
   * other slot can do that job for it. */
  it("never damps the per-item damage channel", () => {
    const its: Record<string, Item> = {
      A: { name: "A", stats: { Penetration: "20" }, effect_tags: [] },
      B: { name: "B", stats: { Penetration: "20" }, effect_tags: [] },
    } as unknown as Record<string, Item>;
    const r = adaptFromCore(["A", "B"], { A: 0.6, B: 0.5 }, its,
      { tags: {}, stats: {}, items: { A: 0.05, B: 0.05 } },
      { maxBonus: 1, selfCovered: 0 });
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
describe("adaptFromCore — the clamp bounds the stack, not the strongest channel", () => {
  const opts = { maxBonus: 0.12 };
  const MARK = item("Mark", { A: "1", B: "1", C: "1" }, ["anti-heal"]);
  const ITEMS2 = { ...byName, Mark: MARK };
  const BASE2 = { ...BASE, Mark: 0.9 };
  // Mark is IN the build, so its price is read off the build the reader sees.
  const SHIPPED2 = ["Mark", "Alpha", "Beta", "Gamma", "Delta", "Epsilon"];
  const priced = (overlay: Parameters<typeof adaptFromCore>[3]) =>
    adaptFromCore(SHIPPED2, BASE2, ITEMS2, overlay, opts);

  it("lets one well-evidenced channel exceed the flat clamp", () => {
    expect(priced({ tags: { "anti-heal": 0.24 }, stats: {} }).bonuses.Mark).toBeCloseTo(0.24, 6);
  });

  it("still bounds many weak channels stacking into a rewrite", () => {
    // Four small channels summing past the clamp is exactly the failure the
    // clamp exists for, and none of them individually earned more than 0.12.
    const r = priced({ tags: { "anti-heal": 0.05 }, stats: { A: 0.05, B: 0.05, C: 0.05 } });
    expect(r.bonuses.Mark).toBeCloseTo(0.12, 6);  // 0.20 earned, clamped
  });

  it("distinguishes a 2-of-5 threat from a 4-of-5 one", () => {
    // The old rule could not: both saturated the flat clamp and produced the
    // same build, so the draft was blind to twice the evidence.
    const weak = priced({ tags: { "anti-heal": 0.12 }, stats: {} });
    const strong = priced({ tags: { "anti-heal": 0.24 }, stats: {} });
    expect(strong.bonuses.Mark).toBeGreaterThan(weak.bonuses.Mark);
  });

  it("does not widen the floor for a penalty", () => {
    expect(priced({ tags: { "anti-heal": -0.4 }, stats: {} }).bonuses.Mark).toBeCloseTo(-0.12, 6);
  });

  it("leaves an item with no channels untouched", () => {
    expect(priced({ tags: { "anti-heal": 0.24 }, stats: {} }).bonuses.Alpha).toBeUndefined();
  });
});
