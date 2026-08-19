import { describe, it, expect } from "vitest";
import { renderHook } from "@testing-library/react";
import { useDraftResult, draftMaxLifesteal } from "./useDraftResult";
import type { BuildNote, DraftComp, DraftConfig, God, Item } from "../types";

const god = (name: string, overrides: Partial<God> = {}): God =>
  ({
    type: "god", name, pantheon: "Test", role: "Carry", specializations: [],
    damage_type: "physical", release_date: "", base_stats: {}, abilities: [], aspects: [],
    source_url: "", last_verified: "", ...overrides,
  }) as God;

const testGod = god("TestGod");
const healerGod = god("EnemyHealer", { role: "Support", specializations: ["Healing"], damage_type: "magical" });
const GODS = [testGod, healerGod];

const item = (name: string, tags: string[] = []): Item =>
  ({
    name, tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [],
    effect_tags: tags, efficiency_tier: null,
  }) as unknown as Item;

// Seven items ranking into a 6-item core: AntiHeal starts one rank outside
// it, so it only appears once a threat's bonus promotes it past Zeta — with
// fewer items than the core size, every item would be "in the core" in both
// the base and adapted build regardless of any bonus, and no promotion could
// ever be observed.
const ITEMS = [
  item("Alpha"), item("Beta"), item("Gamma"), item("Delta"), item("Epsilon"), item("Zeta"),
  item("AntiHeal", ["anti-heal"]),
  // A real starter path: the tier-1 root and the tier-2 it becomes. The
  // opener row groups on this graph, not on the `starters` config.
  { ...item("Conduit Gem"), tier: 1, builds_into: ["Archmage's Gem"] } as Item,
  { ...item("Archmage's Gem"), tier: 2, builds_from: ["Conduit Gem"] } as Item,
];
const SCORES = { Alpha: 0.6, Beta: 0.59, Gamma: 0.58, Delta: 0.57, Epsilon: 0.56, Zeta: 0.55, AntiHeal: 0.4 };
/** The index ships one score table per mode; these fixtures care about the
 *  draft's arithmetic rather than about mode weighting, so every mode gets the
 *  same numbers unless a test says otherwise. */
const perMode = <T,>(flat: Record<string, T>) =>
  Object.fromEntries(Object.entries(flat).map(([g, t]) => [g, { conquest: t, joust: t, arena: t }]));

const GOD_ITEM_SCORES = perMode({ TestGod: SCORES });

const DRAFT_CFG: DraftConfig = {
  max_bonus: 0.5, per_share: 0.5,
  tag_bonus: { healers: { "anti-heal": 1 } }, stat_bonus: {},
  ally_covered: -0.5, ally_gap: 0.5,
};

const comp = (allies: string[], enemies: string[]): DraftComp => ({ allies, enemies });

const run = (
  allies: string[], enemies: string[],
  scores: typeof GOD_ITEM_SCORES | { builds?: BuildNote[] } = GOD_ITEM_SCORES,
  cfg: DraftConfig | undefined = DRAFT_CFG,
) => {
  // Third arg doubles as an options bag so the starter cases can supply build
  // notes without every existing caller growing a parameter.
  const opts = (scores && "builds" in scores ? scores : {}) as { builds?: BuildNote[] };
  const useScores = (scores && "builds" in scores ? GOD_ITEM_SCORES : scores) as typeof GOD_ITEM_SCORES;
  return renderHook(() => useDraftResult(
    comp(allies, enemies), "conquest", GODS, ITEMS, opts.builds ?? [], useScores, cfg,
  )).result.current;
};

/* Two surfaces now render a view of the same draft — /draft and the dock.
 * This is the single derivation both call; DraftPage.test.tsx and
 * DraftDock.test.tsx each exercise it end-to-end through their own UI, so
 * this file only has to prove the derivation itself, not re-prove either
 * page renders it correctly. */
describe("useDraftResult", () => {
  it("is disabled with no god in the you-slot", () => {
    const r = run(["", "", "", "", ""], ["", "", "", "", ""]);
    expect(r.meName).toBe("");
    expect(r.draftEnabled).toBe(false);
    expect(r.result).toBeNull();
    expect(r.changeCount).toBe(0);
  });

  it("is disabled for a god with no scored items, even with a config", () => {
    const r = run(["EnemyHealer", "", "", "", ""], ["", "", "", "", ""]);
    expect(r.draftEnabled).toBe(false);
  });

  it("is disabled with a scored god but no draftConfig", () => {
    // Not routed through `run`: a default parameter substitutes its default
    // for an explicit `undefined` too, which would silently defeat the case
    // this test exists to cover.
    const { result } = renderHook(() => useDraftResult(
      comp(["TestGod", "", "", "", ""], ["", "", "", "", ""]),
      "conquest", GODS, ITEMS, [], GOD_ITEM_SCORES, undefined,
    ));
    expect(result.current.draftEnabled).toBe(false);
  });

  it("produces the default core with no enemies known", () => {
    const r = run(["TestGod", "", "", "", ""], ["", "", "", "", ""]);
    expect(r.draftEnabled).toBe(true);
    expect(r.changeCount).toBe(0);
    expect(r.enemiesKnown).toBe(0);
  });

  it("promotes a countering item once a threat is entered, and counts it as a change", () => {
    const r = run(["TestGod", "", "", "", ""], ["EnemyHealer", "", "", "", ""]);
    expect(r.changeCount).toBeGreaterThan(0);
    expect(r.result!.adapted.core).toContain("AntiHeal");
    expect(r.enemiesKnown).toBe(1);
    expect(r.roster).toBe(5); // the mode's slot count, not the number filled
  });

  it("names the enemy behind a threat through threatCulprits", () => {
    const r = run(["TestGod", "", "", "", ""], ["EnemyHealer", "", "", "", ""]);
    expect(r.threatCulprits.healers).toEqual(["EnemyHealer"]);
    expect(r.threatCulprits.tanks).toEqual([]);
  });

  it("tracks every name on the board, for the is-it-empty check", () => {
    const r = run(["TestGod", "", "", "", ""], ["EnemyHealer", "", "", "", ""]);
    expect(r.taken.has("TestGod")).toBe(true);
    expect(r.taken.has("EnemyHealer")).toBe(true);
    expect(r.taken.size).toBe(2);
  });

  /* The picker blocks a duplicate on the SAME team, never across the board.
   * A team cannot field two Ymirs; the two teams mirroring each other is
   * legal and routine — every non-draft queue allows it, and Joust and Arena
   * are non-draft. Blocking it board-wide made a common comp unenterable. */
  describe("takenFor — one team's duplicates, not the board's", () => {
    const r = () => run(["TestGod", "Ally2", "", "", ""], ["EnemyHealer", "", "", "", ""]);

    it("blocks a god already on the team being picked for", () => {
      expect(r().takenFor("ally", 2).has("Ally2")).toBe(true);
      expect(r().takenFor("enemy", 1).has("EnemyHealer")).toBe(true);
    });

    it("allows the same god on the other team", () => {
      expect(r().takenFor("enemy", 1).has("TestGod")).toBe(false);
      expect(r().takenFor("ally", 2).has("EnemyHealer")).toBe(false);
    });

    it("lets a mirror match be entered on both sides at once", () => {
      const mirror = run(["Ymir", "", "", "", ""], ["Ymir", "", "", "", ""]);
      expect(mirror.takenFor("ally", 0).has("Ymir")).toBe(false);
      expect(mirror.takenFor("enemy", 0).has("Ymir")).toBe(false);
      expect(mirror.taken.size).toBe(1);   // the board-empty check still counts names
    });

    it("does not grey out the god sitting in the slot being edited", () => {
      // Re-opening a filled slot showed its own occupant disabled.
      expect(r().takenFor("ally", 1).has("Ally2")).toBe(false);
      expect(r().takenFor("ally", 1).has("TestGod")).toBe(true);
    });

    it("ignores empty slots", () => {
      expect(r().takenFor("ally", 4).has("")).toBe(false);
    });
  });

  it("gives coreSize a sensible default (6) before anything is scored", () => {
    const r = run(["", "", "", "", ""], ["", "", "", "", ""]);
    expect(r.coreSize).toBe(6);
  });
});

/* The cap rule used to live twice — a YAML row and a TypeScript copy of its
 * conditions — and only the YAML side was under test. These pin the evaluator
 * against the rule shape the index actually ships. */
describe("draftMaxLifesteal — reads the shipped rule, not a copy of it", () => {
  const carry = { name: "Cernunnos", damage_type: "physical", role: "Carry", specializations: ["Sharpshooter"] } as God;
  const mage = { name: "Agni", damage_type: "magical", role: "Mid", specializations: ["Nuker"] } as God;
  const rules = [{ damage_types: ["physical"], match_any: ["Carry", "Hunter", "Sharpshooter"], max_lifesteal: 2 }];

  it("raises the cap for a god the rule matches", () => {
    expect(draftMaxLifesteal(carry, rules)).toBe(2);
  });

  it("leaves a god the rule doesn't match at the default", () => {
    expect(draftMaxLifesteal(mage, rules)).toBe(1);
    // Right specialization, wrong damage type — both conditions must hold.
    expect(draftMaxLifesteal({ ...mage, specializations: ["Sharpshooter"] } as God, rules)).toBe(1);
  });

  it("follows an edited rule instead of the old hardcoded one", () => {
    // The whole point: change the data, the draft changes with it.
    expect(draftMaxLifesteal(mage, [{ damage_types: null, match_any: null, max_lifesteal: 3 }])).toBe(3);
  });

  it("defaults safely when the index predates the shipped rule", () => {
    expect(draftMaxLifesteal(carry, undefined)).toBe(1);
    expect(draftMaxLifesteal(undefined, rules)).toBe(1);
  });
});

/* A build starts before item one, and the draft page began at item one — so
 * the first purchase of the match was the one thing it never showed. These
 * come from SmiteBrain's Starters section, which the parser had skipped since
 * day one; the starter the app used to show came from a role rule instead, so
 * every Carry got the same opener regardless of what Carry players bought. */
describe("useDraftResult — what your god opens with", () => {
  const withStarters = [{
    god: "TestGod", mode: "Conquest", type: "smite-build",
    builds: [{
      source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
      slot_order: [], source_url: "",
      community_starters: [
        { name: "Archmage's Gem", pick_rate: 0.25, win_rate: 0.64 },
        { name: "Conduit Gem", pick_rate: 0.22, win_rate: 0.46 },
      ],
    }],
  }] as unknown as BuildNote[];

  it("groups an opener with its own upgrade instead of listing both", () => {
    // Conduit Gem and Archmage's Gem are one purchase at two moments. Listed
    // separately they ate two of the three slots; measured across the shipped
    // data, 84 of 89 gods had both halves of one path in this row.
    const r = run(["TestGod", "", "", "", ""], ["", "", "", "", ""], { builds: withStarters });
    expect(r.starters).toHaveLength(1);
    const [path] = r.starters;
    expect(path.base?.name).toBe("Conduit Gem");
    expect(path.upgrade?.name).toBe("Archmage's Gem");
    // The lead is the end the community actually holds most often, never a sum
    // — a player who buys the base and upgrades is counted in both rates.
    expect(path.lead.pick_rate).toBe(0.25);
  });

  it("is empty when the god has no community starters rather than guessing one", () => {
    const r = run(["TestGod", "", "", "", ""], ["", "", "", "", ""]);
    expect(r.starters).toEqual([]);
  });

  it("is empty with no god in the you-slot", () => {
    const r = run(["", "", "", "", ""], ["Ymir", "", "", "", ""], { builds: withStarters });
    expect(r.starters).toEqual([]);
  });
});

/* The draft page has offered a Joust toggle since it shipped, and until now it
 * switched only which build NOTE was displayed: `god_item_scores` was a single
 * Conquest table, so the suggested core was Conquest-scored under every mode.
 * `modes.joust.tag_bonus` — including the -0.25 that exists specifically to
 * keep Eye of Providence out of builds that don't run the ward economy — never
 * reached this surface at all. */
describe("useDraftResult — the mode selector selects a model, not a label", () => {
  const PER_MODE = {
    TestGod: {
      conquest: { Alpha: 0.9, Beta: 0.1, Gamma: 0.1, Delta: 0.1, Epsilon: 0.1, Zeta: 0.1 },
      joust: { Alpha: 0.1, Beta: 0.9, Gamma: 0.1, Delta: 0.1, Epsilon: 0.1, Zeta: 0.1 },
      arena: { Alpha: 0.1, Beta: 0.1, Gamma: 0.9, Delta: 0.1, Epsilon: 0.1, Zeta: 0.1 },
    },
  };
  const at = (mode: "conquest" | "joust") => renderHook(() => useDraftResult(
    comp(["TestGod", "", "", "", ""], ["", "", "", "", ""]),
    mode, GODS, ITEMS, [], PER_MODE, DRAFT_CFG,
  )).result.current;

  it("reads the table for the selected mode", () => {
    expect(at("conquest").result?.adapted.core[0]).toBe("Alpha");
    expect(at("joust").result?.adapted.core[0]).toBe("Beta");
  });

  it("disables the draft for a god with no table in this mode", () => {
    const r = renderHook(() => useDraftResult(
      comp(["TestGod", "", "", "", ""], ["", "", "", "", ""]),
      "joust", GODS, ITEMS, [], { TestGod: { conquest: { Alpha: 0.9 } } }, DRAFT_CFG,
    )).result.current;
    expect(r.draftEnabled).toBe(false);
  });
});

/* SmiteBrain is Conquest-only, so a Joust build note carries no community
 * build and therefore no openers. Scoped strictly to the mode, the whole
 * "Opens with" row vanished the moment you switched to Joust. Conquest's
 * openers are a real answer there, just not a measured one — so they are shown
 * with the fallback flagged rather than dropped or passed off as native. */
describe("useDraftResult — openers fall back to Conquest, and say so", () => {
  const conquestOnly = [{
    god: "TestGod", mode: "Conquest", type: "smite-build",
    builds: [{
      source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
      slot_order: [], source_url: "",
      community_starters: [{ name: "Archmage's Gem", pick_rate: 0.25, win_rate: 0.64 }],
    }],
  }] as unknown as BuildNote[];
  const at = (mode: "conquest" | "joust") => renderHook(() => useDraftResult(
    comp(["TestGod", "", "", "", ""], ["", "", "", "", ""]),
    mode, GODS, ITEMS, conquestOnly, GOD_ITEM_SCORES, DRAFT_CFG,
  )).result.current;

  it("shows Conquest's openers in Joust, flagged as borrowed", () => {
    const r = at("joust");
    expect(r.starters.map((p) => p.lead.name)).toEqual(["Archmage's Gem"]);
    expect(r.startersAreConquest).toBe(true);
  });

  it("does not flag Conquest's own openers as borrowed", () => {
    const r = at("conquest");
    expect(r.starters.map((p) => p.lead.name)).toEqual(["Archmage's Gem"]);
    expect(r.startersAreConquest).toBe(false);
  });
});

/* A comp can call for an item the build itself can never contain. Walls forced
 * this: four gods create one, no role label describes it, and the only counter
 * (Shell of Rebuke's passthrough field) is a RELIC — which `is_buildable`
 * excludes from the six core slots because the game gives relics their own. A
 * tag bonus aimed at it could never have done anything. */
describe("useDraftResult — relics answer threats the six slots cannot", () => {
  const waller = god("Waller", {
    threat_kit: { hard_cc: 3, slow: 3, heal: 0, shield: 0, wall: 1 },
  } as never);
  const CFG: DraftConfig = { ...DRAFT_CFG, relics: { walls: { item: "Shell of Rebuke", because: "walls" } } };
  const at = (enemies: string[], cfg: DraftConfig = CFG) => renderHook(() => useDraftResult(
    comp(["TestGod", "", "", "", ""], enemies),
    "conquest", [...GODS, waller], ITEMS, [], GOD_ITEM_SCORES, cfg,
  )).result.current;

  it("suggests the relic once a wall-maker is on the board", () => {
    const r = at(["Waller", "", "", "", ""]);
    expect(r.relicPicks.map((p) => p.item)).toEqual(["Shell of Rebuke"]);
    expect(r.relicPicks[0].count).toBe(1);
  });

  it("suggests nothing when the threat is absent", () => {
    expect(at(["", "", "", "", ""]).relicPicks).toEqual([]);
  });

  it("keeps the relic out of the six", () => {
    expect(at(["Waller", "", "", "", ""]).result?.adapted.core).not.toContain("Shell of Rebuke");
  });

  it("suggests nothing on an index whose config has no relic table", () => {
    expect(at(["Waller", "", "", "", ""], DRAFT_CFG).relicPicks).toEqual([]);
  });
});

/* The draft builds for YOUR god, so only your aspect can move it. Only the 7
 * gods with a hand-tuned overlay in `_weights.yaml` get a `<mode>:aspect`
 * table; for the other 65 with an aspect the toggle is inert BY CONSTRUCTION
 * (there is no table to select) rather than by a separate guard — and the
 * board says which of the two it is. */
describe("useDraftResult — the aspect selects a different table when one exists", () => {
  const SCORED = {
    TestGod: {
      conquest: { Alpha: 0.9, Beta: 0.1, Gamma: 0.1, Delta: 0.1, Epsilon: 0.1, Zeta: 0.1 },
      "conquest:aspect": { Alpha: 0.1, Beta: 0.9, Gamma: 0.1, Delta: 0.1, Epsilon: 0.1, Zeta: 0.1 },
    },
  };
  const UNSCORED = { TestGod: { conquest: { Alpha: 0.9, Beta: 0.1, Gamma: 0.1 } } };
  const at = (scores: typeof SCORED | typeof UNSCORED, aspectOn: boolean) => renderHook(() => useDraftResult(
    comp(["TestGod", "", "", "", ""], ["", "", "", "", ""]),
    "conquest", GODS, ITEMS, [], scores as never, DRAFT_CFG, undefined, aspectOn,
  )).result.current;

  it("builds from the aspect table when the god has one", () => {
    expect(at(SCORED, false).result?.adapted.core[0]).toBe("Alpha");
    expect(at(SCORED, true).result?.adapted.core[0]).toBe("Beta");
    expect(at(SCORED, true).aspectScored).toBe(true);
  });

  it("keeps the base build, and says so, when the aspect has no table", () => {
    const r = at(UNSCORED, true);
    expect(r.result?.adapted.core[0]).toBe("Alpha");
    expect(r.aspectScored).toBe(false);
    expect(r.draftEnabled).toBe(true);
  });
});
