import { describe, it, expect, vi, afterEach } from "vitest";
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { SideBySide, SideBySideView, type SideBySideData } from "./SideBySide";

const metrics = { sustained_squishy: 900, sustained_tank: 500, burst_squishy: 300,
  burst_tank: 200, ehp_physical: 4000, ehp_magical: 3500 };
const side = (items: string[], k = 1) => ({
  ...Object.fromEntries(Object.entries(metrics).map(([m, v]) => [m, v * k])),
  items, gold: 15000, mean_cooldown: 10, ultimate_cooldown: 80,
  crit_chance: 0, crit_multiplier: 1.5, crit_ev: 1,
  passives: [{ item: items[0], status: "not simulated", summary: "refund on kill",
    assumptions: ["no kill in a 10s duel"] }],
  breakpoints: { 2: metrics, 4: metrics, 6: metrics },
}) as unknown as SideBySideData["ichor"];

const data: SideBySideData = {
  god: "Medusa", verdict: "community better", damage_axis: 0.884, survival_axis: 1,
  shared: ["Shared"],
  ichor: side(["Jotunn's Revenge", "Shared"], 0.9),
  community: side(["Devourer's Gauntlet", "Shared"]),
  substitutions: [{ dropped: "Manchu Bow", used: "The Executioner" }],
  diffs: [{
    item: "Devourer's Gauntlet", side: "community", gold: 2500,
    community: { pick_rate: 0.67, win_rate: 0.54, where: "slot 1" },
    passive: { status: "simulated", summary: "75 stacks: +40 Strength", assumptions: [],
      worth: { ...metrics, sustained_squishy: 1418, burst_squishy: 129, ehp_physical: 0, ehp_magical: 0 } },
    model: { text: "model rank #79, quality 0.300" },
    best_swap: { replaces: "Soul Gem", damage_axis: 1.056, survival_axis: 1 },
  }],
};

afterEach(() => vi.unstubAllGlobals());

describe("SideBySide", () => {
  it("states the verdict and both axes", () => {
    render(<SideBySideView d={data} meta={null} />);
    expect(screen.getByTestId("verdict")).toHaveTextContent("Community better");
    expect(screen.getByTestId("side-by-side")).toHaveTextContent("−11.6%");
  });

  it("gives every differing item its community rates, passive worth and the model's reason", () => {
    render(<SideBySideView d={data} meta={null} />);
    const s = screen.getByTestId("side-by-side");
    expect(s).toHaveTextContent("67% pick · 54% win · slot 1");
    expect(s).toHaveTextContent("+1,418 dmg in 10s");
    expect(s).toHaveTextContent("Model rank #79");
    expect(s).toHaveTextContent("for Soul Gem: damage +5.6%");
  });

  it("names what is not simulated instead of rendering it as zero", () => {
    render(<SideBySideView d={data} meta={null} />);
    expect(screen.getByTestId("not-simulated")).toHaveTextContent("Jotunn's Revenge — not simulated: no kill in a 10s duel");
  });

  it("renders nothing for a god with no comparison file", async () => {
    vi.stubGlobal("fetch", vi.fn(async () => ({ ok: false, json: async () => null })));
    const { container } = render(<SideBySide god="Hel" />);
    await waitFor(() => expect(container).toBeEmptyDOMElement());
  });

  it("fetches the god's file by the icon slug", async () => {
    const f = vi.fn(async (url: string) => ({ ok: true,
      json: async () => (url.endsWith("_meta.json") ? null : data) }));
    vi.stubGlobal("fetch", f);
    render(<SideBySide god="Hou Yi" />);
    await waitFor(() => expect(screen.getByTestId("side-by-side")).toBeInTheDocument());
    expect(f).toHaveBeenCalledWith("/side_by_side/hou-yi.json", expect.anything());
  });
});

describe("SideBySide aspect matching", () => {
  it("names the kit and the aspect's pick rate on a base-kit comparison", () => {
    render(<SideBySideView d={{ ...data, kit: { kit: "base", aspect: "Aspect of X", pick_rate: 0.2,
      win_rate: 0.5, simulated: true } }} meta={null} />);
    expect(screen.getByTestId("kit")).toHaveTextContent("Base kit — the community plays Aspect of X in 20% of games");
  });

  it("shows coverage beside the verdict and withholds it when too little is simulated", () => {
    render(<SideBySideView d={{ ...data, verdict: "not enough simulated",
      verdict_unwithheld: "community better", weighted_axes: [0.9, 1],
      coverage: { ichor: 0.34, community: 0.84, gap: 0.5, ok: false,
        reason: "34% of one build's gold is simulated (minimum 50%)" } }} meta={null} />);
    expect(screen.getByTestId("verdict")).toHaveTextContent("Not enough simulated");
    expect(screen.getByTestId("coverage")).toHaveTextContent("34% of Ichor");
    expect(screen.getByTestId("coverage")).toHaveTextContent("minimum 50%");
    expect(screen.getByTestId("side-by-side")).toHaveTextContent("−10.0%");
  });

  it("names a phase verdict as an early-game build, not a loss", () => {
    render(<SideBySideView d={{ ...data, verdict: "early-game build" }} meta={null} />);
    expect(screen.getByTestId("verdict")).toHaveTextContent("Ichor: early-game build");
  });

  it("gives no verdict when the community's aspect cannot be simulated", () => {
    render(<SideBySideView d={{ ...data, verdict: "aspect not simulated",
      kit: { kit: "Aspect of Heartbreak", aspect: "Aspect of Heartbreak", pick_rate: 0.79,
        win_rate: 0.53, simulated: false } }} meta={null} />);
    expect(screen.getByTestId("verdict")).toHaveTextContent("No verdict");
    expect(screen.getByTestId("aspect-not-simulated")).toHaveTextContent("not a fair comparison");
    expect(screen.getByTestId("side-by-side")).not.toHaveTextContent("Ichor’s damage is");
  });

  it("labels a Joust comparison as against the BORROWED Conquest six", () => {
    const joust: SideBySideData = { ...data, mode: "Joust", community_borrowed_from: "Conquest",
      reference: { items: ["A", "B"], same_as_mode_build: false, available: true,
        mode_over_conquest: [1.03, 0.98], verdict_vs_community: "level" } };
    render(<SideBySideView d={joust} meta={null} />);
    expect(screen.getByTestId("side-by-side")).toHaveTextContent("Ichor’s Joust build vs the Conquest community");
    expect(screen.getByTestId("borrowed")).toHaveTextContent("Joust has no community record of its own");
    expect(screen.getByText("Community (Conquest)")).toBeInTheDocument();
    const ref = screen.getByTestId("reference");
    expect(ref).toHaveTextContent("A · B");
    expect(ref).toHaveTextContent("+3.0%");
    expect(ref).toHaveTextContent("Level");
  });

  it("a Conquest comparison carries no borrowed label", () => {
    render(<SideBySideView d={data} meta={null} />);
    expect(screen.queryByTestId("borrowed")).toBeNull();
    expect(screen.queryByTestId("reference")).toBeNull();
  });

  it("opens on the page's mode and switches to another mode's folder", async () => {
    const f = vi.fn(async (url: string) => ({ ok: true,
      json: async () => (url.endsWith("_meta.json") ? null : { ...data, mode: "Arena" }) }));
    vi.stubGlobal("fetch", f);
    render(<SideBySide god="Hou Yi" mode="Arena" />);
    await waitFor(() => expect(screen.getByTestId("side-by-side")).toBeInTheDocument());
    expect(f).toHaveBeenCalledWith("/side_by_side/arena/hou-yi.json", expect.anything());
    fireEvent.click(screen.getByRole("radio", { name: "Joust" }));
    await waitFor(() => expect(f).toHaveBeenCalledWith("/side_by_side/joust/hou-yi.json", expect.anything()));
  });
});
