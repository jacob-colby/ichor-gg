import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { Home } from "./Home";
import type { God, GodTierEntry, IndexData, PatchPeriod } from "../types";
import { toHash } from "../lib/useHashRoute";

const gods = [
  { name: "Agni", pantheon: "Hindu", role: "Mid", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
  { name: "Zeus", pantheon: "Greek", role: "Mid", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
  { name: "Ymir", pantheon: "Norse", role: "Solo", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
] as unknown as God[];

function baseData(overrides: Partial<IndexData> = {}): IndexData {
  return { gods, items: [], builds: [], ...overrides };
}

beforeEach(() => {
  window.location.hash = "";
  localStorage.clear();
});

describe("Home", () => {
  it("narrows search results and navigates to the selected god", () => {
    render(<Home data={baseData()} />);
    const search = within(screen.getByTestId("home-search"));
    fireEvent.change(search.getByPlaceholderText(/search gods/i), { target: { value: "zeu" } });
    expect(search.getByRole("button", { name: /zeus/i })).toBeInTheDocument();
    expect(search.queryByRole("button", { name: /^agni$/i })).not.toBeInTheDocument();

    fireEvent.click(search.getByRole("button", { name: /zeus/i }));
    expect(window.location.hash).toBe(toHash.god("Zeus"));
  });

  it("renders pinned gods", () => {
    localStorage.setItem("smite:pinnedGods", JSON.stringify(["Ymir"]));
    render(<Home data={baseData()} />);
    expect(within(screen.getByTestId("home-pinned")).getByText("Ymir")).toBeInTheDocument();
  });

  it("shows an inviting prompt when there are no pinned gods", () => {
    render(<Home data={baseData()} />);
    const pinned = within(screen.getByTestId("home-pinned"));
    expect(pinned.getByText(/pin a god from its page/i)).toBeInTheDocument();
  });

  it("renders an S-tier slice from the tier list, showing both scores", () => {
    const tierlist = {
      gods: [
        { name: "Ymir", ours: 1.23, community: 0.98, tier_ours: "S", tier_community: "A" },
        { name: "Zeus", ours: 0.5, community: 0.4, tier_ours: "A", tier_community: "A" },
      ] as GodTierEntry[],
      items: [],
    };
    render(<Home data={baseData({ tierlist })} />);
    const tier = within(screen.getByTestId("home-tier"));
    expect(tier.getByText("Ymir")).toBeInTheDocument();
    expect(tier.queryByText("Zeus")).not.toBeInTheDocument();
    expect(tier.getByText(/1\.23/)).toBeInTheDocument();
    expect(tier.getByText(/0\.98/)).toBeInTheDocument();
  });

  it("omits the tier section entirely when there is no tierlist", () => {
    render(<Home data={baseData()} />);
    expect(screen.queryByTestId("home-tier")).not.toBeInTheDocument();
  });

  it("renders the latest patch period when patch_notes is non-empty", () => {
    const patch_notes: PatchPeriod[] = [
      { from: "2026-07-17", to: "2026-07-24", added: [], removed: [], changed: [{ name: "Rage", stats: {}, verdict: "buff" }] },
      { from: "2026-07-10", to: "2026-07-17", added: [], removed: [], changed: [{ name: "Book of Thoth", stats: {}, verdict: "nerf" }] },
    ];
    render(<Home data={baseData({ patch_notes })} />);
    const patch = within(screen.getByTestId("home-patch"));
    expect(patch.getByText(/2026-07-17.*2026-07-24/)).toBeInTheDocument();
    expect(patch.getByText("Rage")).toBeInTheDocument();
    expect(patch.queryByText("Book of Thoth")).not.toBeInTheDocument();
  });

  it("omits the patch section entirely when patch_notes is empty", () => {
    render(<Home data={baseData({ patch_notes: [] })} />);
    expect(screen.queryByTestId("home-patch")).not.toBeInTheDocument();
  });

  it("shows the freshness line with the absolute date available on hover", () => {
    render(<Home data={baseData({ data_updated: "2026-07-23" })} />);
    const freshness = screen.getByTestId("home-freshness");
    expect(freshness.textContent).toMatch(/updated/i);
    expect(freshness).toHaveAttribute("title", "2026-07-23");
  });

  it("omits the freshness line when data_updated is missing", () => {
    render(<Home data={baseData()} />);
    expect(screen.queryByTestId("home-freshness")).not.toBeInTheDocument();
  });

  it("appends the current game patch to the freshness line when data_patch is present", () => {
    render(<Home data={baseData({ data_updated: "2026-07-23", data_patch: "Open Beta 39" })} />);
    const freshness = screen.getByTestId("home-freshness");
    expect(freshness.textContent).toMatch(/^Updated .+ · Open Beta 39$/);
  });

  it("omits the patch clause cleanly when data_patch is absent", () => {
    render(<Home data={baseData({ data_updated: "2026-07-23" })} />);
    const freshness = screen.getByTestId("home-freshness");
    expect(freshness.textContent).not.toContain("·");
  });
});
