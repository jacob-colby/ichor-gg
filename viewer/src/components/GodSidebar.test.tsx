import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { GodSidebar } from "./GodSidebar";
import type { God } from "../types";

const gods = [
  { name: "Ymir", pantheon: "Norse", role: "Solo", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
  { name: "Ra", pantheon: "Egyptian", role: "Mid", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
  { name: "Cupid", pantheon: "Roman", role: "Support", damage_type: "physical", abilities: [], aspects: [], base_stats: {} },
] as unknown as God[];

beforeEach(() => {
  localStorage.clear();
});

describe("GodSidebar", () => {
  it("renders gods in a grid", () => {
    render(<GodSidebar gods={gods} selectedGod={null} onSelect={() => {}} />);
    expect(screen.getByRole("button", { name: "Select Ymir" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Select Ra" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Select Cupid" })).toBeInTheDocument();
  });

  it("narrows results with search", () => {
    render(<GodSidebar gods={gods} selectedGod={null} onSelect={() => {}} />);
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "ra" } });
    expect(screen.getByRole("button", { name: "Select Ra" })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Select Ymir" })).not.toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Select Cupid" })).not.toBeInTheDocument();
  });

  it("filters by a lane pill", () => {
    render(<GodSidebar gods={gods} selectedGod={null} onSelect={() => {}} />);
    fireEvent.click(screen.getByRole("button", { name: "Support" }));
    expect(screen.getByRole("button", { name: "Select Cupid" })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Select Ymir" })).not.toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Select Ra" })).not.toBeInTheDocument();
  });

  it("shows pinned gods in a PINNED group above the rest", () => {
    localStorage.setItem("smite:pinnedGods", JSON.stringify(["Cupid"]));
    render(<GodSidebar gods={gods} selectedGod={null} onSelect={() => {}} />);
    expect(screen.getByText(/pinned/i)).toBeInTheDocument();
    // Cupid should render exactly once (in the pinned group, not duplicated below).
    expect(screen.getAllByRole("button", { name: "Select Cupid" })).toHaveLength(1);
  });

  it("calls onSelect when a god is clicked", () => {
    const onSelect = vi.fn();
    render(<GodSidebar gods={gods} selectedGod={null} onSelect={onSelect} />);
    fireEvent.click(screen.getByRole("button", { name: "Select Ra" }));
    expect(onSelect).toHaveBeenCalledWith("Ra");
  });

  it("marks the selected god distinctly", () => {
    render(<GodSidebar gods={gods} selectedGod="Ymir" onSelect={() => {}} />);
    const ymirBtn = screen.getByRole("button", { name: "Select Ymir" });
    const raBtn = screen.getByRole("button", { name: "Select Ra" });
    expect(ymirBtn).toHaveAttribute("aria-pressed", "true");
    expect(ymirBtn.className).toMatch(/shadow-glow/);
    expect(ymirBtn.className).toMatch(/border-gold/);
    expect(raBtn).toHaveAttribute("aria-pressed", "false");
  });

  it("shows a clear-filters affordance when no gods match", () => {
    render(<GodSidebar gods={gods} selectedGod={null} onSelect={() => {}} />);
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "zzzznotagod" } });
    expect(screen.getByText(/no gods match/i)).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /clear filters/i }));
    expect(screen.getByRole("button", { name: "Select Ymir" })).toBeInTheDocument();
  });

  it("keeps the pin control visible at rest (not opacity-0) with a >=32px hit target, gold only when pinned", () => {
    render(<GodSidebar gods={gods} selectedGod={null} onSelect={() => {}} />);
    const unpinned = screen.getByRole("button", { name: "Pin Ymir" });
    expect(unpinned.className).not.toMatch(/opacity-0/);
    expect(unpinned.className).toMatch(/h-8 w-8/);
    expect(unpinned.className).not.toMatch(/text-gold/);

    localStorage.setItem("smite:pinnedGods", JSON.stringify(["Ymir"]));
    render(<GodSidebar gods={gods} selectedGod={null} onSelect={() => {}} />);
    const pinnedButtons = screen.getAllByRole("button", { name: "Unpin Ymir" });
    expect(pinnedButtons[0].className).toMatch(/text-gold/);
  });

  it("opens and closes the mobile god picker", () => {
    const onSelect = vi.fn();
    render(<GodSidebar gods={gods} selectedGod={null} onSelect={onSelect} />);
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();

    fireEvent.click(screen.getByRole("button", { name: "Select a god" }));
    const dialog = screen.getByRole("dialog");
    expect(dialog).toBeInTheDocument();

    fireEvent.click(within(dialog).getByRole("button", { name: "Select Cupid" }));
    expect(onSelect).toHaveBeenCalledWith("Cupid");
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });
});
