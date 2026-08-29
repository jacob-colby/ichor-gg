/** Does the draft's build for a god equal the god page's build for that god?
 *
 * THE INVARIANT THIS HARNESS EXISTS FOR. The god page ships eleven archetypes
 * per god; the draft adapts exactly one. Offering the other ten in the draft
 * is only honest if, WITH NO ENEMIES DRAFTED, the draft's "crit" build is the
 * same six items the god page's "crit" build is. Two surfaces naming one
 * archetype for one god in one mode and showing different builds is the
 * One-Claim Rule broken ten times over.
 *
 * The draft overlay is viewer-side and `calibrate` cannot see it (STATE.md),
 * so nothing in the pipeline's gates would ever catch that drift. This is the
 * only instrument that can, and it runs against the SHIPPED index — real gods,
 * real scores, real builds — through the real `adaptedCore`, because a fixture
 * cannot measure agreement with a pipeline it does not contain.
 *
 * WHAT IT MEASURED, 2026-08-29 at bec9d6b:
 *
 *   core, no overlay at all      16/89 exact      79.8% item overlap
 *   crit, flavor overlay applied  0/16 exact      61.5% item overlap at best
 *
 * The gap is NOT the missing flavor blocks. It is already there on `core`,
 * where the draft applies no overlay whatsoever and is reading the same score
 * table the pipeline scored the build from. `adaptedCore` is a single-pass
 * greedy fill; `assemble.assemble_core_converged` re-prices every candidate
 * against the stats the core already holds (`price_conversions`, three passes)
 * and marks items down for stats the core has capped out (`cap_overflow`),
 * then runs to a fixed point. Those adjustments happen DURING assembly and so
 * are not in `god_item_scores`, which ships `total` from before it.
 *
 * That is why the second test asserts the gap instead of the equality: the
 * equality is what we want, and it is not true today. A sweep over 21
 * (overlay scale x max_bonus) settings closes none of it — turning the overlay
 * up moves item overlap DOWN, to 33.3% at full strength — so the flavor blocks
 * are not the missing piece and shipping them would only make ten tabs that
 * each contradict the god page.
 *
 * WHEN THESE TESTS START FAILING, the split was fixed and that is the good
 * news: replace the `toBeLessThan` with the equality this file describes and
 * delete the sweep. Until then they pin a known disagreement so it cannot
 * quietly get worse, and so nobody re-derives the measurement from scratch.
 */
import { describe, expect, it } from "vitest";
import raw from "../../public/index.json?raw";
import { adaptedCore } from "./draftBuild";
import { draftMaxLifesteal } from "./useDraftResult";
import type { BuildNote, CuratedBuildEntry, DraftConfig, God, Item } from "../types";

const idx = JSON.parse(raw) as {
  gods: God[]; items: Item[]; builds: BuildNote[];
  god_item_scores: Record<string, Record<string, Record<string, number>>>;
  draft: DraftConfig;
};

const itemsByName: Record<string, Item> = {};
for (const it of idx.items) itemsByName[it.name] = it;

/** The god page's own build for this archetype, in Conquest. */
function shipped(god: string, archetype: string): string[] | undefined {
  const note = idx.builds.find((b) => b.god === god && b.mode === "Conquest");
  const entry = note?.builds.find(
    (b) => b.source === "suggested" && (b as CuratedBuildEntry).archetype === archetype,
  ) as CuratedBuildEntry | undefined;
  return entry?.slot_order as string[] | undefined;
}

/** A build is its six items; `slot_order` is purchase order, which the draft
 *  does not claim to reproduce and which is not what the tabs disagree about. */
const sameSix = (a: string[], b: string[]) =>
  a.length === b.length && new Set([...a, ...b]).size === new Set(a).size;

/** The draft's build for one god with an empty board, optionally skewed by a
 *  flavor's stat block — i.e. exactly what shipping the flavors to
 *  `adaptedCore` would produce. */
function draftBuildFor(g: God, stats: Record<string, number>, maxBonus: number, maxLifesteal?: number) {
  const base = idx.god_item_scores?.[g.name]?.conquest;
  if (!base) return undefined;
  return adaptedCore(base, itemsByName, { tags: {}, stats }, {
    maxBonus,
    maxLifesteal: maxLifesteal ?? draftMaxLifesteal(g, idx.draft.lifesteal_caps),
    selfCovered: idx.draft.self_covered ?? 1,
  }).core;
}

function parity(archetype: string, stats: Record<string, number>, maxBonus: number, maxLifesteal?: number) {
  let compared = 0, exact = 0, shared = 0;
  for (const g of idx.gods) {
    const page = shipped(g.name, archetype);
    const mine = draftBuildFor(g, stats, maxBonus, maxLifesteal);
    if (!page || !mine) continue;
    compared += 1;
    const pageSet = new Set(page);
    shared += mine.filter((n) => pageSet.has(n)).length;
    if (sameSix(mine, page)) exact += 1;
  }
  return { compared, exact, overlap: compared ? shared / (compared * 6) : 0 };
}

/** The flavor block `_weights.yaml` ships for `crit`, verbatim. */
const CRIT_STATS = { "Critical Chance": 1.5, "Attack Speed": 1.2, Strength: 0.8 };

describe("draft vs god page: archetype parity", () => {
  it("compares real six-item builds on both sides", () => {
    // Proves the harness before it proves anything about the model: if the
    // lookups silently returned nothing, every parity figure below would read
    // as a perfect score over an empty set.
    let compared = 0;
    for (const g of idx.gods) {
      const page = shipped(g.name, "core");
      const mine = draftBuildFor(g, {}, idx.draft.max_bonus);
      if (!page || !mine) continue;
      compared += 1;
      expect(page).toHaveLength(6);
      expect(mine).toHaveLength(6);
    }
    expect(compared).toBeGreaterThan(80);
  });

  it("does not hold today, and the gap is there before any flavor is applied", () => {
    const r = parity("core", {}, idx.draft.max_bonus);
    // The assertion this file wants to make is `expect(r.exact).toBe(r.compared)`.
    // It cannot yet: the draft re-assembles from `god_item_scores` with a
    // greedy single pass, and the pipeline's assembler re-prices as it fills.
    expect(r.exact).toBeLessThan(r.compared);
    // Not adrift either — the two builds mostly agree, which is what makes the
    // disagreement worth fixing rather than worth abandoning.
    expect(r.overlap).toBeGreaterThan(0.7);
  });

  it("no setting of the crit flavor overlay closes it", () => {
    // 21 settings: seven overlay strengths (0 = the flavor switched off
    // entirely) against three bonus ceilings, the shipped 0.12 and two far
    // looser ones. Not one produces a single god whose draft crit build is the
    // god page's crit build.
    for (const maxBonus of [0.12, 0.3, 1.0]) {
      for (const scale of [0, 0.02, 0.05, 0.1, 0.25, 0.5, 1]) {
        const stats = Object.fromEntries(
          Object.entries(CRIT_STATS).map(([k, v]) => [k, v * scale]));
        const r = parity("crit", stats, maxBonus, 1);
        expect(r.compared).toBeGreaterThan(10);
        expect({ scale, maxBonus, exact: r.exact }).toEqual({ scale, maxBonus, exact: 0 });
      }
    }
  });
});
