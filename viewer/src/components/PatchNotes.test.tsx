import { describe, it, expect } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { PatchNotes } from "./PatchNotes";
import type { PatchPeriod } from "../types";

function openAll(n = 0) {
  fireEvent.click(screen.getAllByRole("button", { name: /all changes/i })[n]);
}

const crossing = (over: Partial<PatchPeriod> = {}): PatchPeriod => ({
  from: "2026-07-10",
  to: "2026-07-17",
  patch_from: "Open Beta 40",
  patch_to: "Open Beta 41",
  crosses_patch: true,
  added: [],
  removed: [],
  changed: [],
  highlights: [],
  ...over,
});

describe("PatchNotes", () => {
  it("shows a friendly empty state and no period rows when there is no history", () => {
    render(<PatchNotes periods={[]} />);
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/nothing has changed yet/i);
    expect(screen.getByText(/starts empty and fills in/i)).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: /all changes/i })).not.toBeInTheDocument();
  });

  it("titles a patch-crossing period by its patches, with the dates beside it", () => {
    render(<PatchNotes periods={[crossing()]} />);
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent(/^Open Beta 41$/);
    expect(screen.getByText("2026-07-10 to 2026-07-17")).toBeInTheDocument();
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/1 patch\b/);
  });

  it("shows highlights up front, grouped, and keeps the full list collapsed", () => {
    const periods = [
      crossing({
        changed: [
          { name: "Rage", stats: { "Physical Power": ["20", "25"] }, verdict: "buff" },
          { name: "Quiet Item", stats: { Passive: ["a", "b"] }, verdict: "adjusted" },
        ],
        highlights: [
          { name: "Rage", group: "items", change: "buff", headline: "Physical Power 20 → 25", magnitude: 0.25 },
        ],
      }),
    ];
    render(<PatchNotes periods={periods} />);
    expect(screen.getByText("Items")).toBeInTheDocument();
    expect(screen.getByText("Physical Power 20 → 25")).toBeInTheDocument();
    expect(screen.queryByText("Quiet Item")).not.toBeInTheDocument();

    openAll();
    expect(screen.getByText("Quiet Item")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /all changes \(2\)/i })).toHaveAttribute("aria-expanded", "true");
  });

  it("links official notes only when the period carries a verified URL", () => {
    const url = "https://www.smite2.com/news/example";
    render(<PatchNotes periods={[crossing({ official_url: url }), crossing({ from: "2026-07-03", to: "2026-07-10" })]} />);
    const links = screen.getAllByRole("link", { name: /official patch notes/i });
    expect(links).toHaveLength(1);
    expect(links[0]).toHaveAttribute("href", url);
    expect(links[0]).toHaveAttribute("rel", expect.stringContaining("noopener"));
  });

  it("does not call items new when the period sits inside one patch", () => {
    const periods: PatchPeriod[] = [
      {
        from: "2026-08-01",
        to: "2026-08-29",
        patch_from: "Open Beta 40",
        patch_to: "Open Beta 40",
        crosses_patch: false,
        added: ["Axe", "Bow"],
        removed: [],
        changed: [],
        highlights: [],
      },
    ];
    render(<PatchNotes periods={periods} />);
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/no patch has landed/i);
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent("Data update within Open Beta 40");
    expect(screen.getByText(/2 items entered Ichor.s data here/i)).toBeInTheDocument();
    expect(screen.queryByText(/^new$/i)).not.toBeInTheDocument();
    openAll();
    expect(screen.getByText(/entered ichor.s data/i, { selector: "h4" })).toBeInTheDocument();
    expect(screen.getByText("Axe")).toBeInTheDocument();
  });

  it("still renders an older index with no patch fields", () => {
    const periods: PatchPeriod[] = [
      { from: "2026-07-10", to: "2026-07-17", added: [], removed: [], changed: [{ name: "Rage", stats: { "Physical Power": ["20", "25"] }, verdict: "buff" }] },
    ];
    render(<PatchNotes periods={periods} />);
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent("Data update");
    openAll();
    expect(screen.getByText("Rage")).toBeInTheDocument();
  });

  it("colors a stat increase as a buff (green, direction up)", () => {
    render(<PatchNotes periods={[crossing({ changed: [{ name: "Rage", stats: { "Physical Power": ["20", "25"] }, verdict: "buff" }] })]} />);
    openAll();
    const newVal = screen.getByText("25");
    expect(newVal).toHaveAttribute("data-direction", "up");
    expect(newVal.className).toContain("text-under");
  });

  it("colors a cost increase as a nerf (up is bad for cost)", () => {
    render(<PatchNotes periods={[crossing({ changed: [{ name: "Heavy Boots", cost: [2100, 2300], stats: {}, verdict: "nerf" }] })]} />);
    openAll();
    const newVal = screen.getByText("2300");
    expect(newVal).toHaveAttribute("data-direction", "up");
    expect(newVal.className).toContain("text-premium");
  });

  it("colors a cost decrease as a buff (down is good for cost)", () => {
    render(<PatchNotes periods={[crossing({ changed: [{ name: "Heavy Boots", cost: [2300, 2100], stats: {}, verdict: "buff" }] })]} />);
    openAll();
    const newVal = screen.getByText("2100");
    expect(newVal).toHaveAttribute("data-direction", "down");
    expect(newVal.className).toContain("text-under");
  });

  it("lists added and removed items in the full detail of a patch", () => {
    render(<PatchNotes periods={[crossing({ added: ["Fresh Blade"], removed: ["Stale Blade"] })]} />);
    openAll();
    const section = screen.getByRole("heading", { level: 2 }).closest("section")!;
    expect(within(section).getByText("Added", { selector: "h4" })).toBeInTheDocument();
    expect(within(section).getByText("Fresh Blade")).toBeInTheDocument();
    expect(within(section).getByText("Stale Blade").className).toContain("line-through");
  });
});
