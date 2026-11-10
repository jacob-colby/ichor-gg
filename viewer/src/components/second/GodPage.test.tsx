import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { render, screen, fireEvent, waitFor, within, cleanup } from "@testing-library/react";
import App from "../../App";
import { toHash } from "../../lib/useHashRoute";

const SIX = ["Lotus Sickle", "Spear of Desolation", "Spear of the Magus", "Rod of Tahuti", "Obsidian Shard", "Soul Gem"];
const THEIRS = ["Spear of Desolation", "The World Stone", "Rod of Tahuti", "Nimble Ring", "Obsidian Shard", "Book of Thoth"];
const COST: Record<string, number> = {
  "Lotus Sickle": 2150, "Spear of Desolation": 2650, "Spear of the Magus": 2700, "Rod of Tahuti": 3000,
  "Obsidian Shard": 2900, "Soul Gem": 2500, "The World Stone": 2800, "Nimble Ring": 2600, "Book of Thoth": 2700,
  "Conduit Gem": 600, "Archmage's Gem": 1200,
};
const TAGS: Record<string, string[]> = { "Book of Thoth": ["stacking"] };
const item = (name: string) => ({ name, tier: 3, cost: COST[name], stats: {}, passive: "", builds_from: [], builds_into: [],
  effect_tags: TAGS[name] ?? [], efficiency_tier: name === "Soul Gem" ? "undervalued" : "fair" });

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
    // Identical to the main six: the strip still offers it, and says so.
    { source: "suggested", archetype: "cooldown", slot_order: SIX },
  ] }, { type: "build", god: "Ra", mode: "Arena", builds: [
    { source: "suggested", archetype: "model", slot_order: SIX, starter: { base: "Conduit Gem", upgrade: "Archmage's Gem" } },
  ] }],
  community_transfer: {
    Joust: { from: "Conquest", reject_tags: ["mobility"], excluded_items: [] },
    Arena: { from: "Conquest", reject_tags: ["stacking", "mobility"], excluded_items: ["Eye of Providence", "Eye of Erebus"] },
  },
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
  // The name alone: no position prefix, and no asterisk with its read-out reason.
  .map((r) => within(r).getByTestId("item-name").textContent?.replace(/^\d+\.\s*/, "").replace(/\*.*$/, ""));

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
    const whose = await screen.findByRole("group", { name: "Whose build" });
    await waitFor(() => expect(screen.getByTestId("verdict-line")).toHaveAttribute("data-kind", "measured"));
    fireEvent.click(within(whose).getByRole("button", { name: "Community" }));
    expect(rowNames()).toEqual(THEIRS);
    expect(screen.getByRole("heading", { name: /The community's six/ })).toBeInTheDocument();
    fireEvent.click(within(whose).getByRole("button", { name: "Ichor's" }));
    expect(rowNames()).toEqual(SIX);
  });

  it("prints no 0-1 score anywhere on the page, even in the opened detail", async () => {
    render(<App />);
    await waitFor(() => expect(screen.getByTestId("verdict-line")).toHaveAttribute("data-kind", "measured"));
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

  it("says when a god has no comparison at all, on both sides", async () => {
    serve(null);
    render(<App />);
    await waitFor(() => expect(screen.getByTestId("verdict-line")).toHaveTextContent("There's no measured comparison for Ra yet."));
    fireEvent.click(within(screen.getByRole("group", { name: "Whose build" })).getByRole("button", { name: "Community" }));
    // No stand-in from the raw record: it isn't six finished items.
    expect(screen.queryByTestId("six")).not.toBeInTheDocument();
    expect(screen.getByTestId("community-empty")).toHaveTextContent("There's no measured community six for Ra yet.");
  });
});

describe("God page — whose build", () => {
  const whoseGroup = () => screen.findByRole("group", { name: "Whose build" });
  const pick = async (label: "Ichor's" | "Community") => {
    fireEvent.click(within(await whoseGroup()).getByRole("button", { name: label }));
  };
  const measured = () => waitFor(() => expect(screen.getByTestId("verdict-line")).toHaveAttribute("data-kind", "measured"));

  it("is a two-button segmented control above every build option, on Ichor's to start", async () => {
    render(<App />);
    const whose = await whoseGroup();
    const buttons = within(whose).getAllByRole("button");
    expect(buttons.map((b) => b.textContent)).toEqual(["Ichor's", "Community"]);
    expect(buttons.map((b) => b.getAttribute("aria-pressed"))).toEqual(["true", "false"]);
    // Real buttons, so Tab reaches each and Enter or Space picks it.
    for (const b of buttons) expect(b.tagName).toBe("BUTTON");
    // Above the focus strip: you choose whose build before what adjusts it.
    const strip = screen.getByRole("group", { name: "Adjust the build" });
    expect(whose.compareDocumentPosition(strip) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy();
  });

  it("shows the community's measured six with nothing to adjust, and the same verdict", async () => {
    render(<App />);
    await measured();
    const before = screen.getByTestId("verdict-line").textContent;
    await pick("Community");
    expect(rowNames()).toEqual(THEIRS);
    expect(within(await whoseGroup()).getByRole("button", { name: "Community" })).toHaveAttribute("aria-pressed", "true");
    // One six and no focuses: no chips at all, not dead ones.
    expect(screen.queryByRole("group", { name: "Adjust the build" })).not.toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Burst" })).not.toBeInTheDocument();
    expect(screen.getByRole("switch", { name: /Aspect of Thermotherapy/ })).toBeInTheDocument();
    expect(screen.getByTestId("community-line")).toHaveTextContent("What Ra's Conquest players buy most in each slot.");
    expect(screen.getByTestId("verdict-line").textContent).toBe(before);
    // The record's rows read as records, never as the model's or the draft's.
    expect(screen.getAllByTestId("item-row").some((r) => r.hasAttribute("data-adjusted") || r.hasAttribute("data-swapped"))).toBe(false);
    expect(screen.getByTestId("starter")).toHaveTextContent("Conduit Gem → Archmage's Gem");
    await waitFor(() => expect(window.location.hash).toContain("whose=community"));
  });

  it("leaves a chosen focus behind on Ichor's side, and finds it there again", async () => {
    render(<App />);
    await measured();
    fireEvent.click(within(screen.getByRole("group", { name: "Adjust the build" })).getByRole("button", { name: "Burst" }));
    await waitFor(() => expect(screen.getByTestId("verdict-line")).toHaveTextContent(/measured for Ichor's main six/));
    await pick("Community");
    // The head-to-head holds the community's six, so it is quoted here, not refused.
    expect(screen.getByTestId("verdict-line")).toHaveAttribute("data-kind", "measured");
    expect(screen.queryByTestId("swap-line")).not.toBeInTheDocument();
    await pick("Ichor's");
    expect(within(screen.getByRole("group", { name: "Adjust the build" })).getByRole("button", { name: "Burst" }))
      .toHaveAttribute("aria-pressed", "true");
    expect(rowNames()[5]).toBe("Book of Thoth");
  });

  it("keeps the choice across a mode switch; off Conquest it is Conquest's six, asterisked", async () => {
    atUrl(`${toHash.god("Ra")}?whose=community`);
    render(<App />);
    await waitFor(() => expect(rowNames()).toEqual(THEIRS));
    fireEvent.click(screen.getByRole("button", { name: "Arena" }));
    await waitFor(() => expect(screen.getByTestId("verdict-line"))
      .toHaveTextContent("Arena has no community record of its own, so this is the six Ra's Conquest players buy."));
    expect(within(await whoseGroup()).getByRole("button", { name: "Community" })).toHaveAttribute("aria-pressed", "true");
    expect(rowNames()).toEqual(THEIRS);
    expect(screen.getByRole("heading", { name: /Conquest's community six/ })).toBeInTheDocument();
    const rows = screen.getAllByTestId("item-row");
    const flagged = rows.filter((r) => r.hasAttribute("data-flagged"));
    expect(flagged).toHaveLength(1);
    // The asterisk is drawn; a screen reader hears the reason in its place.
    expect(within(flagged[0]).getByTestId("item-name")).toHaveTextContent("Book of Thoth* — Stacking items.");
    expect(screen.getByTestId("six-notes")).toHaveTextContent("Book of Thoth — Stacking items. Conquest's record is for a finished stack");
    expect(rows[0]).toHaveTextContent("In Conquest, 55% of Ra players buy it first");
  });

  it("hands the whole build area to the aspect slot with the aspect on, never the any-aspect six", async () => {
    atUrl(`${toHash.god("Ra")}?whose=community`);
    render(<App />);
    await waitFor(() => expect(rowNames()).toEqual(THEIRS));
    const sw = screen.getByRole("switch", { name: "Aspect of Thermotherapy" });
    fireEvent.click(sw);
    expect(sw).toHaveAttribute("aria-checked", "true");
    const slot = screen.getByTestId("community-aspect-slot");
    // This index carries no per-aspect record for Ra: the slot says so, and
    // where the any-aspect six is.
    expect(slot).toHaveTextContent("No record yet of what Aspect of Thermotherapy players buy.");
    expect(slot).toHaveTextContent("Switch the aspect off to see what all Ra players buy, on any aspect.");
    // The slot owns starter, relic and six: nothing of the base six beside it.
    for (const id of ["six", "kit-tiles", "starter", "relic", "community-line", "six-notes"]) {
      expect(screen.queryByTestId(id)).not.toBeInTheDocument();
    }
    expect(screen.getByRole("heading", { name: "The community's Thermotherapy build" })).toBeInTheDocument();
    // Ichor's side is untouched by it.
    fireEvent.click(within(screen.getByRole("group", { name: "Whose build" })).getByRole("button", { name: "Ichor's" }));
    expect(screen.queryByTestId("community-aspect-slot")).not.toBeInTheDocument();
    expect(rowNames()).toEqual(SIX);
  });

  it("opens on Ichor's from a bare god link, as it opens on Conquest", async () => {
    atUrl(`${toHash.god("Ra")}?whose=community&mode=joust`);
    render(<App />);
    await waitFor(() => expect(rowNames()).toEqual(THEIRS));
    window.location.hash = toHash.god("Ra");
    await waitFor(() => expect(within(screen.getByRole("group", { name: "Whose build" }))
      .getByRole("button", { name: "Ichor's" })).toHaveAttribute("aria-pressed", "true"));
    expect(screen.getByRole("button", { name: "Conquest" })).toHaveAttribute("aria-pressed", "true");
  });

  it("isn't offered for a god with no community record", async () => {
    atUrl(toHash.god("Ymir"));
    render(<App />);
    await screen.findByTestId("god-header");
    expect(screen.queryByRole("group", { name: "Whose build" })).not.toBeInTheDocument();
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

  it("adjusts the one six with a focus: the swapped slot is marked and the swap is named", async () => {
    render(<App />);
    const strip = await screen.findByRole("group", { name: "Adjust the build" });
    expect(screen.queryByTestId("other-builds")).not.toBeInTheDocument();
    expect(within(strip).getByRole("button", { name: "Ichor's six" })).toHaveAttribute("aria-pressed", "true");
    fireEvent.click(within(strip).getByRole("button", { name: "Burst" }));
    await waitFor(() => expect(rowNames()[5]).toBe("Book of Thoth"));
    expect(within(strip).getByRole("button", { name: "Burst" })).toHaveAttribute("aria-pressed", "true");
    const line = screen.getByTestId("swap-line");
    // On a phone the swaps are one line, and the list is one tap away.
    const summary = line.querySelector("summary")!;
    expect(summary).toHaveTextContent(/^Burst Swaps 1 of 6$/);
    expect(line.querySelector("details")!.open).toBe(false);
    // The arrow is drawn; a screen reader hears "replaced by" instead.
    expect(within(line).getByRole("listitem")).toHaveTextContent("Soul Gem → replaced by Book of Thoth");
    const rows = screen.getAllByTestId("item-row");
    expect(rows[5]).toHaveAttribute("data-adjusted", "true");
    expect(rows[5]).toHaveTextContent("In for Soul Gem");
    expect(rows.filter((r) => r.hasAttribute("data-adjusted"))).toHaveLength(1);
    // The comparison is for the main six only, and the sentence says so.
    expect(screen.getByTestId("verdict-line")).toHaveTextContent(/measured for Ichor's main six/);
    await waitFor(() => expect(window.location.hash).toContain("build=burst"));
  });

  it("says a focus that changes nothing is the same build, rather than showing a duplicate", async () => {
    render(<App />);
    const strip = await screen.findByRole("group", { name: "Adjust the build" });
    fireEvent.click(within(strip).getByRole("button", { name: "Cooldown" }));
    await waitFor(() => expect(screen.getByTestId("swap-line")).toHaveTextContent("Same as Ichor's six for Ra."));
    expect(screen.queryByTestId("swap-list")).not.toBeInTheDocument();
    // Nothing behind it, so it is a line of text, not a control.
    expect(screen.getByTestId("swap-line").querySelector("details")).toBeNull();
    expect(screen.getAllByTestId("item-row").some((r) => r.hasAttribute("data-adjusted"))).toBe(false);
  });

  describe("on a desktop", () => {
    beforeEach(() => {
      Object.defineProperty(window, "matchMedia", {
        configurable: true, writable: true,
        value: (q: string) => ({ matches: q.includes("min-width: 1024px"), media: q,
          addEventListener() {}, removeEventListener() {}, addListener() {}, removeListener() {} }),
      });
    });
    afterEach(() => { delete (window as { matchMedia?: unknown }).matchMedia; });

    it("keeps the swap list open under its lead: the column has the room", async () => {
      render(<App />);
      const strip = await screen.findByRole("group", { name: "Adjust the build" });
      fireEvent.click(within(strip).getByRole("button", { name: "Burst" }));
      await waitFor(() => expect(rowNames()[5]).toBe("Book of Thoth"));
      const line = screen.getByTestId("swap-line");
      expect(line.querySelector("details")).toBeNull();
      expect(line).toHaveTextContent(/^Burst Swaps 1 of 6:Soul Gem/);
    });
  });

  it("keeps the aspect switch in the same strip as the focuses", async () => {
    render(<App />);
    const strip = await screen.findByTestId("focus-strip");
    expect(strip).toHaveAttribute("role", "group");
    expect(within(strip).getByRole("switch", { name: /Aspect of Thermotherapy/ })).toBeInTheDocument();
    expect(within(strip).getByRole("button", { name: "Burst" })).toBeInTheDocument();
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

describe("God page — the starter and the relic", () => {
  it("puts the starter in the build as a tile, base and upgrade together", async () => {
    render(<App />);
    const tile = await screen.findByTestId("starter");
    expect(tile).toHaveTextContent("Start");
    expect(tile).toHaveTextContent("Conduit Gem → Archmage's Gem");
    // The tile sits in the build's own section, ahead of the six.
    const section = tile.closest("section")!;
    expect(within(section).getByTestId("six")).toBeInTheDocument();
  });

  /* Ra's real record, 2026-11-08 (ob47). The tile said 41% — Pendulum of the
   * Ages, the larger end — for a path 58% of Ra players open with: SmiteBrain
   * counts each player once, holding the base OR the upgrade, so the path's
   * share is the two ends summed. */
  const RA_SIGHTINGS = [
    { name: "Pendulum of the Ages", pick_rate: 0.41, win_rate: 0.53 },
    { name: "Archmage's Gem", pick_rate: 0.24, win_rate: 0.54 },
    { name: "Sands Of Time", pick_rate: 0.17, win_rate: 0.46 },
    { name: "Conduit Gem", pick_rate: 0.15, win_rate: 0.39 },
    { name: "Selflessness", pick_rate: 0.01, win_rate: 0.6 },
  ];
  const withRaStarters = async (stamp: Record<string, unknown>, check: () => Promise<void>) => {
    const community = index.builds[0].builds[0] as Record<string, unknown>;
    const model = index.builds[0].builds[1] as Record<string, unknown>;
    const items = index.items as Record<string, unknown>[];
    const gem = items.find((i) => i.name === "Archmage's Gem")!;
    const was = { model: model.starter, gemFrom: gem.builds_from, items: items.length };
    community.starter_sightings = RA_SIGHTINGS;
    model.starter = { base: "Sands Of Time", upgrade: "Pendulum of the Ages", ...stamp };
    gem.builds_from = ["Conduit Gem"];
    items.push(
      { ...item("Conduit Gem"), name: "Sands Of Time", builds_into: ["Pendulum of the Ages"] },
      { ...item("Archmage's Gem"), name: "Pendulum of the Ages", builds_from: ["Sands Of Time"] });
    try {
      await check();
    } finally {
      delete community.starter_sightings;
      model.starter = was.model;
      gem.builds_from = was.gemFrom;
      items.length = was.items;
    }
  };

  it("states the whole path's share, base and upgrade summed", async () => {
    // No rate on the stamp (a saved or older build): summed from the sightings.
    await withRaStarters({}, async () => {
      render(<App />);
      const tile = await screen.findByTestId("starter");
      expect(tile).toHaveTextContent("Sands Of Time → Pendulum of the Ages");
      expect(tile).toHaveTextContent("58% of Ra players open this way");
      expect(tile).not.toHaveTextContent("41%");
    });
  });

  it("reads the pipeline's stamped share when the build carries one", async () => {
    await withRaStarters({ basis: "community", pick_rate: 0.6, win_rate: 0.51, matches: 248 }, async () => {
      render(<App />);
      expect(await screen.findByTestId("starter")).toHaveTextContent("60% of Ra players open this way");
    });
  });

  it("names each other opener by its base, beside that path's summed share", async () => {
    // Every Archmage's Gem holder opened with Conduit Gem, so "Conduit Gem 39%"
    // is true; "Archmage's Gem 39%" would claim 15 points of players it lacks.
    await withRaStarters({}, async () => {
      render(<App />);
      const alts = within(await screen.findByTestId("starter")).getByRole("list");
      expect(within(alts).getAllByRole("listitem").map((li) => li.textContent)).toEqual([
        "Conduit Gem39% of players", "Selflessness1% of players"]);
    });
  });

  it("keeps each tile to an item row: the other picks are one tap away, behind the tile itself", async () => {
    await withRaStarters({}, async () => {
      render(<App />);
      const tile = await screen.findByTestId("starter");
      expect(tile.tagName).toBe("DETAILS");
      expect((tile as HTMLDetailsElement).open).toBe(false);
      const summary = tile.querySelector("summary")!;
      // "Start" is the badge where a row prints its position; the name has the line.
      expect(summary).toHaveTextContent("Start: Sands Of Time → Pendulum of the Ages");
      expect(within(summary).getByTestId("starter-others-count")).toHaveTextContent("+2 others");
      expect(within(summary).queryByRole("list")).not.toBeInTheDocument();
    });
  });

  it("is a plain tile, not a control, when the record has no other picks", async () => {
    render(<App />);
    const tile = await screen.findByTestId("starter");
    expect(tile.tagName).toBe("DIV");
    expect(tile.querySelector("summary")).toBeNull();
  });

  it("renders no relic tile while the index carries no relic record", async () => {
    render(<App />);
    await screen.findByTestId("starter");
    expect(screen.queryByTestId("relic")).not.toBeInTheDocument();
  });

  it("renders the community's relic, with the alternatives by share of players", async () => {
    const community = index.builds[0].builds[0] as Record<string, unknown>;
    community.community_relics = [
      { name: "Purification Beads", pick_rate: 0.22, win_rate: 0.5 },
      { name: "Blink Rune", pick_rate: 0.41, win_rate: 0.52 },
      { name: "Aegis Amulet", pick_rate: 0.18, win_rate: 0.49 },
      { name: "Sundering Spear", pick_rate: 0.05, win_rate: 0.47 },
    ];
    try {
      render(<App />);
      const tile = await screen.findByTestId("relic");
      expect(tile).toHaveTextContent("Blink Rune");
      expect(tile).toHaveTextContent("41% of Ra players take it");
      const alts = within(tile).getByRole("list");
      expect(within(alts).getAllByRole("listitem").map((li) => li.textContent)).toEqual([
        "Purification Beads22% of players", "Aegis Amulet18% of players"]);
    } finally {
      delete community.community_relics;
    }
  });
});

describe("God page — most picked", () => {
  const openPicked = async () => {
    const d = await screen.findByTestId("picked-disclosure");
    (d as HTMLDetailsElement).open = true;
    return within(d).getByTestId("most-picked");
  };

  it("ranks the god's own players' items and ticks the ones in this build", async () => {
    render(<App />);
    const list = await openPicked();
    const rows = within(list).getAllByTestId("picked-row");
    expect(rows[0]).toHaveTextContent("Spear of Desolation");
    expect(rows[0]).toHaveTextContent("55% buy it first");
    expect(rows[0]).toHaveAttribute("data-in-build", "true");
    expect(rows[0]).toHaveTextContent("In this build");
    const nimble = rows.find((r) => r.textContent?.includes("Nimble Ring"))!;
    expect(nimble).not.toHaveAttribute("data-in-build");
    expect(screen.getByTestId("picked-disclosure")).toHaveTextContent("3 of Ra's top 6 are in this build");
    expect(within(list).queryByTestId("picked-notes")).not.toBeInTheDocument();
  });

  it("shows Conquest's list on Arena, labelled, with an asterisk and a reason where it doesn't transfer", async () => {
    atUrl(`${toHash.god("Ra")}?mode=arena`);
    render(<App />);
    const list = await openPicked();
    expect(list).toHaveTextContent("Arena has no record of its own, so this is Conquest data");
    const thoth = within(list).getAllByTestId("picked-row").find((r) => r.textContent?.includes("Book of Thoth"))!;
    expect(thoth).toHaveAttribute("data-flagged", "true");
    const notes = within(list).getByTestId("picked-notes");
    expect(notes).toHaveTextContent("Book of Thoth — Stacking items. Conquest's record is for a finished stack");
    // Only the tagged item is marked.
    expect(within(list).getAllByTestId("picked-row").filter((r) => r.hasAttribute("data-flagged"))).toHaveLength(1);
  });
});

describe("God page — what the aspect's players buy", () => {
  // Ra's record shaped like Tsukuyomi's Mangetsu on 2026-11-09: a pool of
  // three patches, a role shift, a starter path split over two ends, and
  // items whose stats moved after the oldest window read.
  const RECORD = {
    source: "SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)",
    minimum_matches: 30, complete_from: "2026-09-24", partial_windows: { ob44: "2026-09-24" },
    aspects: [{
      aspect: "Aspect of Thermotherapy", status: "shown",
      matches_by_window: { ob47: 6, ob46: 21, ob45: 30, ob44: 17 },
      windows: ["ob45", "ob46", "ob47"], patches: "OB45–OB47", window_rule: "pooled back", matches: 57,
      roles: [{ role: "Support", matches: 32, share: 0.56 }, { role: "Mid", matches: 15, share: 0.26 }],
      base_role: "Mid", base_role_share: 0.26,
      role_shift: { role: "Support", share: 0.56, says: "" },
      items: [
        { name: "Rod of Tahuti", share: 0.86, changed: { patch: "OB41–OB46", exact: false, older_matches: 27, matches: 49,
          says: "its stats moved between Ichor's OB40 and OB46 item data, at a patch not recorded; up to 27 of the 49 matches that bought it are older" } },
        { name: "Book of Thoth", share: 0.79 },
        { name: "Spear of the Magus", share: 0.72 },
        { name: "Obsidian Shard", share: 0.63 },
        { name: "Soul Gem", share: 0.33 },
        { name: "Spear of Desolation", share: 0.23 },
        { name: "The World Stone", share: 0.21 },
      ],
      starters: [
        { name: "Archmage's Gem", share: 0.42 }, { name: "Bluestone Pendant", share: 0.25 },
        { name: "Conduit Gem", share: 0.11 }, { name: "Bluestone Brooch", share: 0.05 },
      ],
      relics: [
        { name: "Purification Beads", share: 0.6, changed: { patch: "OB47", exact: true, older_matches: 20, matches: 34,
          says: "changed in OB47; 20 of the 34 matches that bought it are older" } },
        { name: "Aegis of Acceleration", share: 0.39 }, { name: "Phantom Shell", share: 0.02 },
      ],
    }],
  };
  const PATHS = [
    { ...item("Conduit Gem"), tier: 1, builds_into: ["Archmage's Gem"] },
    { ...item("Archmage's Gem"), tier: 2, builds_from: ["Conduit Gem"] },
    { ...item("Bluestone Pendant"), tier: 1, builds_into: ["Bluestone Brooch"] },
    { ...item("Bluestone Brooch"), tier: 2, builds_from: ["Bluestone Pendant"] },
  ];
  const conquestNote = index.builds[0] as Record<string, unknown>;
  // The fixture's items are typed with empty build paths; these four have one.
  const shop = index as unknown as { items: { name: string }[] };
  const withRecord = async (record: unknown, hash: string, check: () => Promise<void>) => {
    const items = shop.items;
    conquestNote.community_aspects = record;
    shop.items = [...items.filter((i) => !PATHS.some((p) => p.name === i.name)), ...PATHS];
    atUrl(hash);
    try {
      render(<App />);
      await check();
    } finally {
      delete conquestNote.community_aspects;
      shop.items = items;
    }
  };
  // The Community side with the aspect on: the aspect slot (`community-aspect-slot`).
  const on = `${toHash.god("Ra")}?aspect=1&whose=community`;

  it("draws it only on the Community side with the aspect on; Ichor's side points to it", async () => {
    await withRecord(RECORD, `${toHash.god("Ra")}?whose=community`, async () => {
      await screen.findByRole("switch", { name: /Aspect of Thermotherapy/ });
      expect(screen.queryByTestId("aspect-community")).not.toBeInTheDocument();
    });
    cleanup();
    await withRecord(RECORD, `${toHash.god("Ra")}?aspect=1`, async () => {
      await screen.findByTestId("aspect-note");
      expect(screen.queryByTestId("aspect-community")).not.toBeInTheDocument();
      expect(screen.getByTestId("aspect-note")).toHaveTextContent("What its players buy is on the Community side.");
    });
  });

  it("labels it community, not Ichor’s model, with the games and the patches it pools", async () => {
    await withRecord(RECORD, on, async () => {
      const slot = await screen.findByTestId("community-aspect-slot");
      const box = within(slot).getByTestId("aspect-community");
      expect(screen.getByRole("heading", { name: "The community's Thermotherapy build" })).toBeInTheDocument();
      expect(screen.getByTestId("aspect-community-span")).toHaveTextContent("57 games · OB45–OB47");
      expect(within(box).getByTestId("aspect-community-note")).toHaveTextContent(
        "Community, not Ichor’s model: what Conquest games with Aspect of Thermotherapy ended holding — pooled: no recent patch alone has 30 games.");
      expect(within(box).getByTestId("aspect-community-source")).toHaveTextContent("not a buy order");
      // It owns the build area: no second heading of its own, no any-aspect pointer.
      expect(within(slot).queryByRole("heading")).not.toBeInTheDocument();
      expect(within(slot).queryByTestId("any-aspect-line")).not.toBeInTheDocument();
    });
  });

  it("says when its players take the god into another role, and that Ichor's six cannot follow", async () => {
    await withRecord(RECORD, on, async () => {
      const shift = await screen.findByTestId("aspect-role-shift");
      expect(shift).toHaveTextContent("Most play it Support (56%), not Mid (26%).");
      expect(shift).toHaveTextContent("Ichor’s six above is built for Mid: the model can’t move a god’s role for an aspect yet.");
    });
  });

  it("puts the starter and relic in as tiles, the starter as a path with both ends summed", async () => {
    await withRecord(RECORD, on, async () => {
      const starter = await screen.findByTestId("aspect-starter");
      expect(starter).toHaveTextContent("Conduit Gem → Archmage's Gem");
      expect(starter).toHaveTextContent("53% of these games open this way");
      expect(within(starter).getByRole("list")).toHaveTextContent("Bluestone Pendant30% of these games");
      const relic = screen.getByTestId("aspect-relic");
      expect(relic).toHaveTextContent("Purification Beads");
      expect(relic).toHaveTextContent("60% of these games take it · changed OB47*");
      expect(within(relic).getAllByRole("listitem").map((li) => li.textContent)).toEqual([
        "Aegis of Acceleration39% of these games", "Phantom Shell2% of these games"]);
    });
  });

  it("lists the six most held, by share of games, with a changed item asterisked and explained", async () => {
    await withRecord(RECORD, on, async () => {
      const six = await screen.findByTestId("aspect-six");
      const rows = within(six).getAllByTestId("aspect-item");
      expect(rows.map((r) => within(r).getByTestId("aspect-item-name").textContent)).toEqual([
        "Rod of Tahuti", "Book of Thoth", "Spear of the Magus", "Obsidian Shard", "Soul Gem", "Spear of Desolation"]);
      expect(rows[0]).toHaveTextContent("In 86% of these games · changed OB41–OB46*");
      expect(rows[0]).toHaveAttribute("data-changed", "true");
      expect(rows[1]).not.toHaveAttribute("data-changed");
      const notes = screen.getByTestId("aspect-changed-notes");
      expect(notes).toHaveTextContent("Rod of Tahuti: its stats moved between Ichor's OB40 and OB46 item data, at a patch not recorded; up to 27 of the 49 matches that bought it are older.");
      expect(notes).toHaveTextContent("Purification Beads: changed in OB47; 20 of the 34 matches that bought it are older.");
      expect(notes).toHaveTextContent("a passive change is not flagged");
      // No gold column: this is not Ichor's buy order.
      expect(six).not.toHaveTextContent(/gold/i);
    });
  });

  it("folds the aspect's swaps to one line on a phone, the pointer behind it", async () => {
    // An aspect build that moves the six: one swap, Soul Gem -> Book of Thoth.
    const note = index.builds[0] as unknown as { builds: unknown[] };
    const builds = note.builds;
    const scored = index as unknown as { god_item_scores?: unknown };
    note.builds = [...builds, { source: "suggested", archetype: "model", aspect: "Aspect of Thermotherapy",
      slot_order: [...SIX.slice(0, 5), "Book of Thoth"] }];
    scored.god_item_scores = { Ra: { "conquest:aspect": { "Book of Thoth": 0.6 } } };
    try {
      await withRecord(RECORD, `${toHash.god("Ra")}?aspect=1`, async () => {
        const line = await screen.findByTestId("aspect-line");
        const summary = line.querySelector("summary")!;
        expect(summary).toHaveTextContent(/^Built for Thermotherapy\. Swaps 1 of 6$/);
        expect(line.querySelector("details")!.open).toBe(false);
        // Behind the tap: the swap, then where its players' build is.
        expect(within(line).getByRole("listitem")).toHaveTextContent("Soul Gem → replaced by Book of Thoth");
        expect(line).toHaveTextContent("What its players buy is on the Community side.");
      });
    } finally {
      note.builds = builds;
      delete scored.god_item_scores;
    }
  });

  it("says how few games there are when the record is below the minimum", async () => {
    const thin = { ...RECORD, aspects: [{ aspect: "Aspect Of Thermotherapy", status: "below minimum",
      matches_by_window: { ob47: 4, ob46: 13, ob45: 6, ob44: 5 } }] };
    await withRecord(thin, on, async () => {
      const box = await screen.findByTestId("aspect-community");
      expect(box).toHaveTextContent("Too few games to show: 28 Conquest games across OB44–OB47, and this needs 30.");
      expect(within(box).queryByTestId("aspect-six")).not.toBeInTheDocument();
      expect(screen.queryByTestId("aspect-community-span")).not.toBeInTheDocument();
      expect(screen.getByTestId("any-aspect-line")).toHaveTextContent("Switch the aspect off to see what all Ra players buy");
    });
  });

  it("says Joust has no aspect record instead of showing Conquest's", async () => {
    await withRecord(RECORD, `${toHash.god("Ra")}?mode=joust&aspect=1&whose=community`, async () => {
      const box = await screen.findByTestId("aspect-community");
      expect(box).toHaveTextContent("Only Conquest records what aspect players buy. Joust has no per-aspect record, so none is shown here.");
      expect(within(box).queryByTestId("aspect-six")).not.toBeInTheDocument();
      expect(within(box).queryByTestId("aspect-starter")).not.toBeInTheDocument();
    });
  });

  it("says so when the god's record holds nothing for this aspect", async () => {
    await withRecord(undefined, on, async () => {
      const box = await screen.findByTestId("aspect-community");
      expect(box).toHaveTextContent("No record yet of what Aspect of Thermotherapy players buy.");
    });
  });
});
