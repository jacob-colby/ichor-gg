import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { PatchNotes } from "./PatchNotes";
import type { PatchPeriod } from "../types";

describe("PatchNotes", () => {
  it("shows a friendly empty state and no period rows when there is no history", () => {
    render(<PatchNotes periods={[]} />);
    expect(screen.getByText(/no patch history yet/i)).toBeInTheDocument();
    expect(screen.queryByText(/→/)).not.toBeInTheDocument();
  });

  it("renders a period header with from → to", () => {
    const periods: PatchPeriod[] = [
      { from: "2026-07-10", to: "2026-07-17", added: [], removed: [], changed: [] },
    ];
    render(<PatchNotes periods={periods} />);
    expect(screen.getByText("2026-07-10 → 2026-07-17")).toBeInTheDocument();
  });

  it("expands the newest period by default and keeps older periods collapsed until clicked", () => {
    const periods: PatchPeriod[] = [
      {
        from: "2026-07-10",
        to: "2026-07-17",
        added: [],
        removed: [],
        changed: [{ name: "Rage", stats: { "Physical Power": ["20", "25"] }, verdict: "buff" }],
      },
      {
        from: "2026-07-03",
        to: "2026-07-10",
        added: [],
        removed: [],
        changed: [{ name: "Book of Thoth", stats: { Mana: ["300", "250"] }, verdict: "nerf" }],
      },
    ];
    render(<PatchNotes periods={periods} />);

    // newest period's contents visible by default
    expect(screen.getByText("Rage")).toBeInTheDocument();
    // older period's contents hidden
    expect(screen.queryByText("Book of Thoth")).not.toBeInTheDocument();

    fireEvent.click(screen.getByText("2026-07-03 → 2026-07-10"));
    expect(screen.getByText("Book of Thoth")).toBeInTheDocument();
  });

  it("shows a buff item's verdict chip and its old → new values", () => {
    const periods: PatchPeriod[] = [
      {
        from: "2026-07-10",
        to: "2026-07-17",
        added: [],
        removed: [],
        changed: [{ name: "Rage", stats: { "Physical Power": ["20", "25"] }, verdict: "buff" }],
      },
    ];
    render(<PatchNotes periods={periods} />);
    expect(screen.getByText("Rage")).toBeInTheDocument();
    expect(screen.getByText(/buff/i)).toBeInTheDocument();
    expect(screen.getByText("20")).toBeInTheDocument();
    expect(screen.getByText("25")).toBeInTheDocument();
  });

  it("colors a stat increase as a buff (green, direction up)", () => {
    const periods: PatchPeriod[] = [
      {
        from: "2026-07-10",
        to: "2026-07-17",
        added: [],
        removed: [],
        changed: [{ name: "Rage", stats: { "Physical Power": ["20", "25"] }, verdict: "buff" }],
      },
    ];
    render(<PatchNotes periods={periods} />);
    const newVal = screen.getByText("25");
    expect(newVal).toHaveAttribute("data-direction", "up");
    expect(newVal.className).toContain("text-under");
  });

  it("colors a cost increase as a nerf (inverted direction — up is bad for cost)", () => {
    const periods: PatchPeriod[] = [
      {
        from: "2026-07-10",
        to: "2026-07-17",
        added: [],
        removed: [],
        changed: [{ name: "Heavy Boots", cost: [2100, 2300], stats: {}, verdict: "nerf" }],
      },
    ];
    render(<PatchNotes periods={periods} />);
    const newVal = screen.getByText("2300");
    expect(newVal).toHaveAttribute("data-direction", "up");
    expect(newVal.className).toContain("text-premium");
  });

  it("colors a cost decrease as a buff (inverted direction — down is good for cost)", () => {
    const periods: PatchPeriod[] = [
      {
        from: "2026-07-10",
        to: "2026-07-17",
        added: [],
        removed: [],
        changed: [{ name: "Heavy Boots", cost: [2300, 2100], stats: {}, verdict: "buff" }],
      },
    ];
    render(<PatchNotes periods={periods} />);
    const newVal = screen.getByText("2100");
    expect(newVal).toHaveAttribute("data-direction", "down");
    expect(newVal.className).toContain("text-under");
  });

  it("renders added items with a 'new' chip and removed items struck through", () => {
    const periods: PatchPeriod[] = [
      {
        from: "2026-07-10",
        to: "2026-07-17",
        added: ["Fresh Blade"],
        removed: ["Stale Blade"],
        changed: [],
      },
    ];
    render(<PatchNotes periods={periods} />);
    expect(screen.getByText("Fresh Blade")).toBeInTheDocument();
    expect(screen.getByText(/new/i)).toBeInTheDocument();
    const removed = screen.getByText("Stale Blade");
    expect(removed.className).toContain("line-through");
  });
});
