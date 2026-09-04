/** Does the draft's build for a god equal the god page's build for that god?
 *
 * THE INVARIANT THIS HARNESS EXISTS FOR. The god page ships up to eleven
 * archetypes per god; the draft adapts one at a time. Offering them in the
 * draft is only honest if, WITH NO ENEMIES DRAFTED, the draft's "crit" build
 * is the same six items the god page's "crit" build is. Two surfaces naming
 * one archetype for one god in one mode and showing different builds is the
 * One-Claim Rule broken once per tab.
 *
 * The draft overlay is viewer-side and `calibrate` cannot see it (STATE.md),
 * so nothing in the pipeline's gates would ever catch that drift. This is the
 * only instrument that can, and it runs against the SHIPPED index — real gods,
 * real scores, real builds — through the real adaptation, because a fixture
 * cannot measure agreement with a pipeline it does not contain.
 *
 * WHAT IT MEASURED, 2026-08-29 at bec9d6b, when the draft re-assembled the six
 * items itself from `god_item_scores`:
 *
 *   core, no overlay at all      16/89 exact      79.8% item overlap
 *   crit, flavor overlay applied  0/16 exact      61.5% item overlap at best
 *
 * RE-MEASURED 2026-09-03 on the shipped index, over every archetype and every
 * mode rather than only Conquest `core` — the data has moved since (90 gods
 * now, and three `chore(data): daily community refresh` commits), so the
 * headline figure is 22/90 rather than 16/89 and this is the wider picture:
 *
 *   ALL archetypes x all modes    190/2247 exact  61.3% item overlap
 *   Conquest core                  22/90         80.2%
 *   Conquest bruiser                0/90         59.1%
 *   Arena bruiser                   0/90         38.1%
 *
 * The gap was NOT the missing flavor blocks. It was already there on `core`,
 * where the draft applied no overlay whatsoever and was reading the same score
 * table the pipeline scored the build from, because
 * `assemble.assemble_core_converged` re-prices every candidate DURING assembly
 * and `god_item_scores` ships `total` from before it. A sweep over 21 (overlay
 * scale x max_bonus) settings closed none of it — turning the overlay up moved
 * item overlap DOWN, to 33.3% at full strength.
 *
 * WHAT FIXED IT was not a better re-assembly. `adaptFromCore` starts from the
 * shipped `slot_order` and may only swap, on the draft's own evidence, so with
 * an empty board the equality below holds by construction. The second half of
 * this file is the other property, and it is the one a re-rank of a fixed six
 * would have lost: the draft can still bring in an item the base core never
 * contained.
 */
import { describe, expect, it } from "vitest";
import raw from "../../public/index.json?raw";
import { adaptFromCore } from "./draftBuild";
import { archetypeEntries, draftMaxLifesteal } from "./useDraftResult";
import { deriveThreats, threatOverlay } from "./threats";
import type { BuildNote, CuratedBuildEntry, DraftConfig, God, Item } from "../types";
import type { DraftMode } from "./draft";

const idx = JSON.parse(raw) as {
  gods: God[]; items: Item[]; builds: BuildNote[];
  god_item_scores: Record<string, Record<string, Record<string, number>>>;
  draft: DraftConfig;
};

const itemsByName: Record<string, Item> = {};
for (const it of idx.items) itemsByName[it.name] = it;
const godsByName: Record<string, God> = {};
for (const g of idx.gods) godsByName[g.name] = g;

const MODES: DraftMode[] = ["conquest", "joust", "arena"];

/** A build is its six items; `slot_order` is purchase order, which is the
 *  pipeline's (`assemble.build_order`) on both sides now. */
const sameSix = (a: string[], b: string[]) =>
  a.length === b.length && new Set([...a, ...b]).size === new Set(a).size;

function optsFor(g: God, entry: CuratedBuildEntry) {
  return {
    maxBonus: idx.draft.max_bonus,
    maxLifesteal: draftMaxLifesteal(g, idx.draft.lifesteal_caps),
    selfCovered: idx.draft.self_covered ?? 1,
    flexSlots: entry.flex_slots,
  };
}

/** Every (god, mode, archetype) the board can offer, paired with the god page's
 *  own build for it — which is the same object, because there is one. */
function everyBoard() {
  const out: { god: God; mode: DraftMode; entry: CuratedBuildEntry;
    scores: Record<string, number> }[] = [];
  for (const g of idx.gods) {
    for (const mode of MODES) {
      const scores = idx.god_item_scores?.[g.name]?.[mode];
      if (!scores) continue;
      for (const entry of archetypeEntries(idx.builds, g.name, mode, false)) {
        out.push({ god: g, mode, entry, scores });
      }
    }
  }
  return out;
}

describe("draft vs god page: archetype parity", () => {
  it("compares real six-item builds on both sides", () => {
    // Proves the harness before it proves anything about the model: if the
    // lookups silently returned nothing, every parity figure below would read
    // as a perfect score over an empty set.
    const boards = everyBoard();
    expect(boards.length).toBeGreaterThan(2000);
    expect(new Set(boards.map((b) => b.god.name)).size).toBeGreaterThan(80);
    expect(new Set(boards.map((b) => b.entry.archetype)).size).toBeGreaterThan(8);
    for (const b of boards) {
      expect(b.entry.slot_order).toHaveLength(6);
      expect(Object.keys(b.scores).length).toBeGreaterThan(0);
    }
  });

  it("A. with no enemies drafted, every board IS the god page's build", () => {
    const wrong: string[] = [];
    let compared = 0;
    for (const { god, mode, entry, scores } of everyBoard()) {
      const mine = adaptFromCore(entry.slot_order as string[], scores, itemsByName,
        { tags: {}, stats: {} }, optsFor(god, entry)).core;
      compared += 1;
      if (!sameSix(mine, entry.slot_order as string[])) {
        wrong.push(`${god.name}/${mode}/${entry.archetype}`);
      }
      // Order too, not only membership. Buy order is `assemble.build_order`'s
      // and the draft does not reorder, so the empty board must reproduce the
      // sequence and not merely the set.
      else expect(mine).toEqual(entry.slot_order);
    }
    expect({ compared, wrong: wrong.slice(0, 10) }).toEqual({ compared, wrong: [] });
  });
});

/* ── B. AND IT CAN STILL BRING IN SOMETHING NEW ─────────────────────────────
 *
 * The failure mode this half exists to catch is the one that looks like a
 * success: satisfy A by re-ranking the six items the pipeline handed over, and
 * the two surfaces agree perfectly while the draft quietly stops being able to
 * answer a comp at all. Anti-heal against healers is the case the whole
 * `threat_kit` exists for, and it is by definition an item the base core does
 * not contain.
 *
 * Run through the real overlay — `deriveThreats` then `threatOverlay`, the
 * same two calls `useDraftResult` makes — against a real five-healer enemy
 * team taken from the shipped roster. */
const healers = idx.gods.filter((g) => (g.specializations ?? []).some(
  (s) => /heal/i.test(s))).map((g) => g.name);

function boardWith(enemies: string[], god: God, mode: DraftMode, archetype: string) {
  const entry = archetypeEntries(idx.builds, god.name, mode, false)
    .find((e) => e.archetype === archetype);
  const scores = idx.god_item_scores?.[god.name]?.[mode];
  if (!entry || !scores) return undefined;
  const threats = deriveThreats(
    { allies: [god.name, "", "", "", ""], enemies }, godsByName, {});
  const overlay = threatOverlay(threats, idx.draft, god);
  const shipped = entry.slot_order as string[];
  const adapted = adaptFromCore(shipped, scores, itemsByName, overlay, optsFor(god, entry));
  return { shipped, adapted };
}

describe("draft adaptation still works", () => {
  it("has five real healers to draft against", () => {
    expect(healers.length).toBeGreaterThanOrEqual(5);
  });

  it("B. a healer comp brings in an item the base core did not contain, with a reason", () => {
    const five = healers.slice(0, 5);
    const brought: { god: string; item: string; reason: string }[] = [];
    for (const g of idx.gods) {
      const r = boardWith(five, g, "conquest", "core");
      if (!r) continue;
      const base = new Set(r.shipped);
      for (const name of r.adapted.core) {
        if (base.has(name)) continue;
        brought.push({ god: g.name, item: name, reason: r.adapted.reasons[name] ?? "" });
      }
    }
    // Not a corner case firing on one god: 59 arrivals across 58 of the 90
    // Conquest `core` boards, measured on the shipped index 2026-09-03.
    expect(brought.length).toBe(59);
    // Every arrival names what it answers. An item that appears with no reason
    // is the draft moving a build for a cause it cannot state.
    for (const b of brought) expect(b.reason).not.toBe("");
    // And the reason is the threat that was actually drafted.
    expect(brought.some((b) => /anti-heal/.test(b.reason))).toBe(true);
    // The arrival is genuinely outside the six, not a resort of them.
    expect(brought.every((b) => b.item !== "")).toBe(true);
  });

  it("B. it fires on the archetype tabs too, not only on `core`", () => {
    const five = healers.slice(0, 5);
    const hit = new Set<string>();
    for (const g of idx.gods) {
      for (const entry of archetypeEntries(idx.builds, g.name, "conquest", false)) {
        const r = boardWith(five, g, "conquest", entry.archetype!);
        if (!r) continue;
        const base = new Set(r.shipped);
        if (r.adapted.core.some((n) => !base.has(n))) hit.add(entry.archetype!);
      }
    }
    // Every archetype the index ships for Conquest, not a lucky one: a tab
    // that could never swap would be a tab the draft cannot adapt.
    expect([...hit].sort()).toEqual([
      "anti-tank", "attack-speed", "bruiser", "burst", "cooldown", "core", "crit",
      "hybrid", "intelligence", "mana-stack", "model", "str-int", "strength",
    ]);
  });

  it("the bar is evidence, not a threshold on the base score: one healer moves nothing", () => {
    // The count the old code could not produce. `adaptedCore` clamped a
    // 2-healer comp and a 4-healer comp to byte-identical builds; here the
    // comps are told apart because the bar is a DIFFERENCE in bonus.
    const swapped = (n: number) => idx.gods.filter((g) => {
      const r = boardWith(healers.slice(0, n).concat(Array(5 - n).fill("")), g, "conquest", "core");
      if (!r) return false;
      const base = new Set(r.shipped);
      return r.adapted.core.some((x) => !base.has(x));
    }).length;
    expect({ one: swapped(1), five: swapped(5) }).toEqual({ one: 0, five: 58 });
  });
});
