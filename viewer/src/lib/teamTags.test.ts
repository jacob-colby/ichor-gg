import { describe, expect, it } from "vitest";
import raw from "../../public/index.json?raw";
import { teamOverlay, teamValue, type TeamConfig } from "./teamTags";
import { adaptFromCore } from "./draftBuild";
import { archetypeEntries, draftMaxLifesteal } from "./useDraftResult";
import type { BuildNote, CuratedBuildEntry, DraftConfig, God, Item } from "../types";

const cfg: TeamConfig = {
  tags: ["anti-heal", "aura"], duplicate_value: 0.25,
  modes: {
    Joust: { team_size: 3, share: 0.5, bonus: { "anti-heal": 0.3, aura: 0.2 } },
    Conquest: { team_size: 5, share: 0.4, bonus: {} },
  },
};

describe("team-level tags", () => {
  it("values your copy by what the known teammates hold", () => {
    expect(teamValue(true, 0, 0.25)).toBe(0.25);
    expect(teamValue(false, 0, 0.25)).toBe(1);
    expect(teamValue(false, 2, 0.25)).toBeCloseTo(1 / 3 + (2 / 3) * 0.25);
  });

  it("an empty board is the static assumption exactly: every delta is zero", () => {
    expect(teamOverlay(cfg, "Joust", [null, null], {})).toEqual({});
    expect(teamOverlay(cfg, "Joust", [], {})).toEqual({});
  });

  it("a teammate's anti-heal makes yours worth less; a full team without it, more", () => {
    const tags = { A: ["anti-heal"], B: ["burst"] };
    const withIt = teamOverlay(cfg, "Joust", ["A", "B"], tags);
    expect(withIt["anti-heal"]).toBeCloseTo(0.3 * (0.25 - 0.5));
    expect(withIt.aura).toBeCloseTo(0.2 * (1 - 0.5));   // nobody has an aura: you are the carrier
    const without = teamOverlay(cfg, "Joust", ["B", "B2"], tags);
    expect(without["anti-heal"]).toBeCloseTo(0.3 * 0.5);
  });

  it("a mode with no team bonus moves nothing, and an older index has no config", () => {
    expect(teamOverlay(cfg, "Conquest", ["A", "B", "C", "D"], { A: ["anti-heal"] })).toEqual({});
    expect(teamOverlay(undefined, "Joust", ["A"], {})).toEqual({});
  });
});

/** Measured on the SHIPPED index, Joust `core`: give every god two
 *  teammates and count the cores holding anti-heal. Two boards, the two ends:
 *  teammates that both carry anti-heal, and teammates that carry none.
 *
 *  2026-11-03, no enemies drafted: shipped 13 of 94; teammates without it 93;
 *  teammates with it 10. The 93 is the blunt end and is stated, not hidden:
 *  "you are your team's only anti-heal" is worth +0.15 here, which clears the
 *  0.12 swap bar for nearly every god, because the swap rule spends draft
 *  evidence and leaves WHICH item arrives to the model. Properties are pinned
 *  below rather than the counts, which move with every refresh. */
const idx = JSON.parse(raw) as {
  gods: God[]; items: Item[]; builds: BuildNote[];
  god_item_scores: Record<string, Record<string, Record<string, number>>>;
  draft: DraftConfig;
};

describe("team-level tags on the shipped Joust index", () => {
  const items: Record<string, Item> = Object.fromEntries(idx.items.map((i) => [i.name, i]));
  const gods: Record<string, God> = Object.fromEntries(idx.gods.map((g) => [g.name, g]));
  const anti = (n: string) => (items[n]?.effect_tags ?? []).includes("anti-heal");
  const holds = (core: string[]) => core.some(anti);

  const run = (teamHolds: boolean) => {
    let before = 0, after = 0, n = 0;
    const overlay = { tags: {}, stats: {},
      team: teamOverlay(idx.draft.team, "Joust", ["T1", "T2"],
        teamHolds ? { T1: ["anti-heal"], T2: ["anti-heal"] } : { T1: [], T2: [] }) };
    for (const g of idx.gods) {
      // The board's default tab, as `useDraftResult` picks it: `core`, which
      // `dedupeCoreAgainstModel` folds into `model` when the two are the same six.
      const entries = archetypeEntries(idx.builds, g.name, "joust", false);
      const entry = entries.find((e: CuratedBuildEntry) => e.archetype === "core")
        ?? entries.find((e: CuratedBuildEntry) => e.archetype === "model") ?? entries[0];
      const scores = idx.god_item_scores[g.name]?.joust;
      if (!entry || !scores) continue;
      n += 1;
      const shipped = entry.slot_order as string[];
      const out = adaptFromCore(shipped, scores, items, overlay, {
        maxBonus: idx.draft.max_bonus, selfCovered: idx.draft.self_covered ?? 1,
        maxLifesteal: draftMaxLifesteal(gods[g.name], idx.draft.lifesteal_caps),
        flexSlots: entry.flex_slots });
      before += Number(holds(shipped));
      after += Number(holds(out.core));
    }
    return { n, before, after };
  };

  it("a team without anti-heal pulls it into more cores; a team with it, into fewer or none", () => {
    expect(idx.draft.team?.modes?.Joust?.share).toBeCloseTo(0.5);
    const none = run(false);
    const both = run(true);
    expect(none.after).toBeGreaterThan(none.before);
    expect(both.after).toBeLessThanOrEqual(both.before);
  });
});
