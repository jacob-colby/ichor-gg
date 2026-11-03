import { describe, expect, it } from "vitest";
import raw from "../../public/index.json?raw";
import { teamFitItems, teamOverlay, teamValue, type TeamConfig } from "./teamTags";
import { threatOverlay } from "./threats";
import { adaptFromCore } from "./draftBuild";
import { archetypeEntries, draftMaxLifesteal } from "./useDraftResult";
import type { BuildNote, CuratedBuildEntry, DraftConfig, God, Item, ThreatModel } from "../types";

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
 *  teammates, with and without anti-heal, against no enemies and against
 *  three healers, and count the boards holding anti-heal. Counts move with
 *  every refresh, so properties are pinned and the 2026-11-03 numbers are in
 *  the PR and in STATE.md. */
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

  const run = (teamHolds: boolean, healers: number) => {
    let before = 0, after = 0, n = 0, unfit = 0;
    const teammateTags = teamHolds ? { T1: ["anti-heal"], T2: ["anti-heal"] } : { T1: [], T2: [] };
    const threats = { magical: 0, physical: 0, healers, lockdown: 0, walls: 0, crit: 0, tanks: 0,
      enemyCount: healers, rosterSize: 3, allyCovers: teamHolds ? { "anti-heal": true } : {},
      allyAllPhysical: false, allyCount: 2, allyPhysical: 0 } as unknown as ThreatModel;
    for (const g of idx.gods) {
      const entries = archetypeEntries(idx.builds, g.name, "joust", false);
      const entry = entries.find((e: CuratedBuildEntry) => e.archetype === "core")
        ?? entries.find((e: CuratedBuildEntry) => e.archetype === "model") ?? entries[0];
      const scores = idx.god_item_scores[g.name]?.joust;
      if (!entry || !scores) continue;
      n += 1;
      const overlay = { ...threatOverlay(threats, idx.draft, gods[g.name]),
        team: teamOverlay(idx.draft.team, "Joust", ["T1", "T2"], teammateTags),
        teamFit: teamFitItems(idx.draft.team, g.name, "Joust"), teamGated: idx.draft.team?.tags };
      const shipped = entry.slot_order as string[];
      const out = adaptFromCore(shipped, scores, items, overlay, {
        maxBonus: idx.draft.max_bonus, selfCovered: idx.draft.self_covered ?? 1,
        maxLifesteal: draftMaxLifesteal(gods[g.name], idx.draft.lifesteal_caps),
        flexSlots: entry.flex_slots });
      before += Number(holds(shipped));
      after += Number(holds(out.core));
      const fit = new Set(overlay.teamFit ?? []);
      unfit += out.core.filter((x) => anti(x) && !shipped.includes(x) && !fit.has(x)).length;
    }
    return { n, before, after, unfit };
  };

  it("the static share is calibrated near one core in three", () => {
    const none = run(false, 0);
    expect(none.before / none.n).toBeGreaterThan(0.25);
    expect(none.before / none.n).toBeLessThan(0.42);
  });

  it("teammates without anti-heal never pull in fewer; teammates with it never more", () => {
    for (const h of [0, 3]) {
      expect(run(false, h).after).toBeGreaterThanOrEqual(run(true, h).after);
      expect(run(true, h).after).toBeLessThanOrEqual(run(true, h).before + run(true, h).n);
    }
  });

  it("against healers, anti-heal arrives only where it fits the kit, and more without a teammate's copy", () => {
    const none = run(false, 3);
    const both = run(true, 3);
    expect(none.after).toBeGreaterThan(both.after);
    // Neither channel adds an anti-heal item the kit check rejected.
    expect(none.unfit).toBe(0);
  });
});
