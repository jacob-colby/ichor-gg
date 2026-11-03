/** Shared fixtures for the god page and match board integration tests: Ra with
 *  a model six, a community six and a /side_by_side comparison. */
import { vi } from "vitest";

export const SIX = ["Lotus Sickle", "Spear of Desolation", "Spear of the Magus", "Rod of Tahuti", "Obsidian Shard", "Soul Gem"];
export const THEIRS = ["Spear of Desolation", "The World Stone", "Rod of Tahuti", "Nimble Ring", "Obsidian Shard", "Book of Thoth"];
export const COST: Record<string, number> = {
  "Lotus Sickle": 2150, "Spear of Desolation": 2650, "Spear of the Magus": 2700, "Rod of Tahuti": 3000,
  "Obsidian Shard": 2900, "Soul Gem": 2500, "The World Stone": 2800, "Nimble Ring": 2600, "Book of Thoth": 2700,
  "Conduit Gem": 600, "Archmage's Gem": 1200,
};
export const item = (name: string) => ({ name, tier: 3, cost: COST[name], stats: {}, passive: "", builds_from: [], builds_into: [],
  effect_tags: [], efficiency_tier: name === "Soul Gem" ? "undervalued" : "fair" });

export const index = {
  gods: [
    { name: "Ra", role: "Mid", damage_type: "magical", base_stats: {}, abilities: [],
      aspects: [{ name: "Aspect of Thermotherapy", kit_changes: "" }] },
    { name: "Ymir", role: "Support", damage_type: "magical", base_stats: {}, abilities: [], aspects: [] },
  ],
  items: Object.keys(COST).map(item),
  builds: [{ type: "build", god: "Ra", mode: "Conquest", builds: [
    { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null, source_url: "",
      slot_order: [
        { name: "Spear of Desolation", pick_rate: 0.55, win_rate: 0.54 },
        { name: "The World Stone", pick_rate: 0.39, win_rate: 0.54 },
        { name: "Rod of Tahuti", pick_rate: 0.35, win_rate: 0.55 },
        { name: "Nimble Ring", pick_rate: 0.23, win_rate: 0.57 },
        { name: "Obsidian Shard", pick_rate: 0.22, win_rate: 0.6 },
        { name: "Book of Thoth", pick_rate: 0.12, win_rate: 0.59 },
      ],
      starter: { base: "Conduit Gem", upgrade: "Archmage's Gem" } },
    { source: "suggested", archetype: "model", slot_order: SIX, starter: { base: "Conduit Gem", upgrade: "Archmage's Gem" },
      slot_scores: { "Lotus Sickle": { total: 0.55, efficiency: 0.57, win: 0.55, pick: 0, fit: 0.69 } } },
    { source: "suggested", archetype: "burst", slot_order: [...SIX.slice(0, 5), "Book of Thoth"] },
  ] }],
  tierlist: { gods: [], items: [],
    conquest: { gods: [{ name: "Ra", score: 0.5, win_rate: 0.53, matches: 1286, tier_score: "B" }], items: [] } },
};

export function side(items: string[], notSim: string[] = []) {
  return { items, gold: items.reduce((a, n) => a + COST[n], 0), mean_cooldown: null, ultimate_cooldown: null,
    crit_chance: 0, crit_multiplier: 0, crit_ev: 0, breakpoints: {},
    passives: items.map((n) => ({ item: n, status: notSim.includes(n) ? "not simulated" : "simulated", summary: "", assumptions: [] })),
    sustained_squishy: 100, sustained_tank: 100, burst_squishy: 100, burst_tank: 100, ehp_physical: 100, ehp_magical: 100 };
}
export const comparison = (over: Record<string, unknown> = {}) => ({
  god: "Ra", verdict: "community better", damage_axis: 0.9567, survival_axis: 1.0633, weighted_axes: [0.933, 1.0207],
  shared: [], substitutions: [], ichor: side(SIX, ["Lotus Sickle"]), community: side(THEIRS),
  coverage: { ichor: 0.86, community: 1, gap: 0.14, ok: true, reason: null },
  kit: { kit: "base", aspect: "Aspect of Thermotherapy", pick_rate: 0.04, win_rate: 0.59, simulated: true },
  diffs: [{ item: "The World Stone", side: "community", gold: 2800,
    community: { pick_rate: 0.39, win_rate: 0.54, where: "slot 2" },
    passive: { status: "simulated", summary: "-25% ultimate cooldown", assumptions: [] },
    model: { text: "model rank #10, quality 0.584 (efficiency 0.53, fit 0.72)" } }],
  ...over,
});

export const atUrl = (hash: string) => window.history.replaceState(null, "", `/${hash}`);
export const serve = (cmp: unknown) => vi.stubGlobal("fetch", vi.fn((url: string) => {
  const body = url.includes("/side_by_side/_meta") ? { band: 0.05, level: 20, window: 10, data: "OB46",
    targets: { squishy: { role: "Mid", max_health: 2200 }, tank: { role: "Support", max_health: 3300 } } }
    : url.includes("/side_by_side/") ? cmp : index;
  return Promise.resolve({ ok: body !== null, json: () => Promise.resolve(body) });
}));
