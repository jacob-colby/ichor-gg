import { describe, it, expect, beforeEach, vi } from "vitest";
import { render, screen, fireEvent, waitFor, within } from "@testing-library/react";
import App from "../../App";
import { toHash } from "../../lib/useHashRoute";

const SIX = ["Lotus Sickle", "Spear of Desolation", "Spear of the Magus", "Rod of Tahuti", "Obsidian Shard", "Soul Gem"];
const THEIRS = ["Spear of Desolation", "The World Stone", "Rod of Tahuti", "Nimble Ring", "Obsidian Shard", "Book of Thoth"];
const COST: Record<string, number> = {
  "Lotus Sickle": 2150, "Spear of Desolation": 2650, "Spear of the Magus": 2700, "Rod of Tahuti": 3000,
  "Obsidian Shard": 2900, "Soul Gem": 2500, "The World Stone": 2800, "Nimble Ring": 2600, "Book of Thoth": 2700,
  "Conduit Gem": 600, "Archmage's Gem": 1200,
};
const item = (name: string) => ({ name, tier: 3, cost: COST[name], stats: {}, passive: "", builds_from: [], builds_into: [],
  effect_tags: [], efficiency_tier: name === "Soul Gem" ? "undervalued" : "fair" });

const index = {
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

function side(items: string[], notSim: string[] = []) {
  return { items, gold: items.reduce((a, n) => a + COST[n], 0), mean_cooldown: null, ultimate_cooldown: null,
    crit_chance: 0, crit_multiplier: 0, crit_ev: 0, breakpoints: {},
    passives: items.map((n) => ({ item: n, status: notSim.includes(n) ? "not simulated" : "simulated", summary: "", assumptions: [] })),
    sustained_squishy: 100, sustained_tank: 100, burst_squishy: 100, burst_tank: 100, ehp_physical: 100, ehp_magical: 100 };
}
const comparison = (over: Record<string, unknown> = {}) => ({
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

const atUrl = (hash: string) => window.history.replaceState(null, "", `/${hash}`);
const serve = (cmp: unknown) => vi.stubGlobal("fetch", vi.fn((url: string) => {
  const body = url.includes("/side_by_side/_meta") ? { band: 0.05, level: 20, window: 10, data: "OB46",
    targets: { squishy: { role: "Mid", max_health: 2200 }, tank: { role: "Support", max_health: 3300 } } }
    : url.includes("/side_by_side/") ? cmp : index;
  return Promise.resolve({ ok: body !== null, json: () => Promise.resolve(body) });
}));

beforeEach(() => {
  localStorage.clear();
  atUrl(toHash.god("Ra"));
  serve(comparison());
});

const rowNames = () => within(screen.getByTestId("six")).getAllByTestId("item-row")
  .map((r) => within(r).getByTestId("item-name").textContent?.replace(/^\d+\.\s*/, ""));

describe("God page — the answer", () => {
  it("says the comparison in one honest sentence under the header", async () => {
    render(<App />);
    const line = await screen.findByTestId("verdict-line", {}, { timeout: 2000 });
    await waitFor(() => expect(line).toHaveTextContent(
      "The community's six deals 7% more damage; survival is about even. Lotus Sickle isn't simulated yet, so the damage gap is partly unmeasured."));
  });

  it("lists Ichor's six in buy order with gold spent and a reason in words", async () => {
    render(<App />);
    await screen.findByTestId("six");
    expect(rowNames()).toEqual(SIX);
    const rows = screen.getAllByTestId("item-row");
    expect(rows[0]).toHaveTextContent("Ra's players don't buy this");
    expect(rows[0]).toHaveTextContent("2,150");
    expect(rows[1]).toHaveTextContent("55% of Ra players buy it first");
    expect(rows[1]).toHaveTextContent("4,800");
    expect(rows[5]).toHaveTextContent("worth more than it costs");
    expect(screen.getByTestId("starter")).toHaveTextContent("Conduit Gem → Archmage's Gem");
  });

  it("swaps to the community's six in place, and back", async () => {
    render(<App />);
    const show = await screen.findByRole("button", { name: /Show theirs/ });
    fireEvent.click(show);
    expect(rowNames()).toEqual(THEIRS);
    expect(screen.getByRole("heading", { name: /The community's six/ })).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /Show Ichor's/ }));
    expect(rowNames()).toEqual(SIX);
  });

  it("prints no 0-1 score anywhere on the page, even in the opened detail", async () => {
    render(<App />);
    await screen.findByRole("button", { name: /Show theirs/ });
    for (const d of document.querySelectorAll("details")) d.open = true;
    expect(screen.getByTestId("compare-detail")).toBeInTheDocument();
    expect(document.querySelector("main")!.textContent).not.toMatch(/\b0\.\d+/);
  });

  it("withholds the call when coverage fails, in words", async () => {
    serve(comparison({ verdict: "not enough simulated",
      coverage: { ichor: 0.4, community: 1, gap: 0.6, ok: false, reason: "too much unsimulated" } }));
    render(<App />);
    await waitFor(() => expect(screen.getByTestId("verdict-line")).toHaveTextContent(/isn't measured enough to call/));
    expect(screen.getByTestId("verdict-line")).not.toHaveTextContent(/%/);
  });

  it("says when a god has no comparison at all", async () => {
    serve(null);
    render(<App />);
    await waitFor(() => expect(screen.getByTestId("verdict-line")).toHaveTextContent("There's no measured comparison for Ra yet."));
    expect(screen.queryByRole("button", { name: /Show theirs/ })).not.toBeInTheDocument();
  });
});

describe("God page — controls", () => {
  it("says in one line when the aspect doesn't change the build", async () => {
    render(<App />);
    const sw = await screen.findByRole("switch", { name: /Aspect of Thermotherapy/ });
    expect(sw).toHaveAttribute("aria-checked", "false");
    fireEvent.click(sw);
    expect(screen.getByTestId("aspect-note")).toHaveTextContent(/doesn't change Ra's six/);
    await waitFor(() => expect(window.location.hash).toContain("aspect=1"));
  });

  it("puts other builds behind a disclosure and swaps the six in place", async () => {
    render(<App />);
    const other = await screen.findByTestId("other-builds");
    fireEvent.click(within(other).getByRole("button", { name: /Burst/ }));
    await waitFor(() => expect(rowNames()[5]).toBe("Book of Thoth"));
    // The comparison is for the main six only, and the sentence says so.
    expect(screen.getByTestId("verdict-line")).toHaveTextContent(/measured for Ichor's main six/);
    await waitFor(() => expect(window.location.hash).toContain("build=burst"));
  });

  it("has five enemy slots in Conquest, three in Joust", async () => {
    render(<App />);
    const strip = await screen.findByTestId("enemy-strip");
    expect(within(strip).getAllByRole("button", { name: /Add enemy/ })).toHaveLength(5);
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    await waitFor(() => expect(within(screen.getByTestId("enemy-strip")).getAllByRole("button", { name: /Add enemy/ })).toHaveLength(3));
    expect(screen.getByTestId("verdict-line")).toHaveTextContent(/^Joust has no community build/);
  });
});
