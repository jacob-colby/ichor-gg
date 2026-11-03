import { describe, it, expect } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { PatchPage } from "./PatchPage";
import type { PatchPeriod } from "../../types";

const period = (over: Partial<PatchPeriod> = {}): PatchPeriod => ({
  from: "2026-08-29", to: "2026-11-02", patch_from: "Open Beta 40", patch_to: "Open Beta 46", crosses_patch: true,
  added: [], removed: [], changed: [], highlights: [], ...over,
});

describe("PatchPage", () => {
  it("starts empty and says so, rather than looking like it is loading", () => {
    render(<PatchPage periods={[]} />);
    expect(screen.getByRole("heading", { level: 1, name: "Patch notes" })).toBeInTheDocument();
    expect(screen.getByTestId("patch-claim")).toHaveTextContent("Nothing has changed yet.");
    expect(screen.getByText(/starts empty and fills in.*This isn.t a loading state/)).toBeInTheDocument();
    expect(screen.queryByTestId("patch-period")).not.toBeInTheDocument();
  });

  it("is honest when updates exist but no patch has landed", () => {
    render(<PatchPage periods={[period({ crosses_patch: false, patch_from: "Open Beta 46", added: ["Rage"] })]} />);
    expect(screen.getByTestId("patch-claim")).toHaveTextContent("No patch has landed in Ichor’s data yet.");
    // Items that entered the data inside one patch are not called new.
    expect(screen.getByText(/1 item entered Ichor.s data here; they were already in the game/)).toBeInTheDocument();
    expect(screen.getByRole("heading", { level: 2, name: "Data update within Open Beta 46" })).toBeInTheDocument();
  });

  it("titles a period by its patches, dates beside it from the ISO parts", () => {
    render(<PatchPage periods={[period()]} />);
    expect(screen.getByRole("heading", { level: 2, name: "Open Beta 46" })).toBeInTheDocument();
    expect(screen.getByText("29 Aug – 2 Nov")).toBeInTheDocument();
  });

  it("leads with the biggest changes as rows, kinds in words, and links the items it knows", () => {
    render(<PatchPage itemNames={["Arondight"]} periods={[period({
      changed: [{ name: "Arondight", cost: [2650, 2550], stats: {}, verdict: "buff" }],
      highlights: [{ name: "Arondight", group: "items", change: "buff", headline: "Cost 2650 → 2550" },
        { name: "Gone Thing", group: "items", change: "removed", headline: "Removed from the shop" }],
    })]} />);
    const hl = within(screen.getByTestId("patch-highlights"));
    expect(hl.getByText("Buff")).toBeInTheDocument();
    expect(hl.getByText("Removed")).toBeInTheDocument();
    expect(hl.getByRole("link", { name: "Arondight" })).toHaveAttribute("href", "#/items/Arondight");
    expect(hl.queryByRole("link", { name: "Gone Thing" })).not.toBeInTheDocument();
    expect(screen.getByTestId("patch-claim")).toHaveTextContent("1 item change across 1 patch, newest first.");
  });

  it("keeps every cost and stat one tap below, old to new", () => {
    render(<PatchPage periods={[period({
      changed: [{ name: "Bloodforge", stats: { Strength: ["45", "55"] }, verdict: "buff" }],
      highlights: [{ name: "Bloodforge", group: "items", change: "buff", headline: "Strength 45 → 55" }],
    })]} />);
    const all = screen.getByTestId("patch-all");
    expect(all).not.toHaveAttribute("open");
    fireEvent.click(within(all).getByText(/All 1 change/));
    expect(within(all).getByText("Strength")).toBeInTheDocument();
    expect(within(all).getByText("55")).toBeInTheDocument();
  });

  it("links official notes only when the period carries a checked URL", () => {
    const { rerender } = render(<PatchPage periods={[period()]} />);
    expect(screen.queryByRole("link", { name: /official patch notes/i })).not.toBeInTheDocument();
    rerender(<PatchPage periods={[period({ official_url: "https://example.com/ob46" })]} />);
    expect(screen.getByRole("link", { name: /official patch notes/i })).toHaveAttribute("href", "https://example.com/ob46");
  });
});
