import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { BuildEditor } from "./BuildEditor";
import { getMine } from "../lib/mineStore";
import type { Item } from "../types";

const items = [
  { name: "Deathbringer", tier: 3, cost: 3000, stats: {}, passive: "", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: "premium" },
  { name: "Rage", tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: "undervalued" },
] as unknown as Item[];

describe("BuildEditor", () => {
  beforeEach(() => localStorage.clear());

  it("saves a build (item added via the picker modal) and calls onSaved", () => {
    const onSaved = vi.fn();
    const onClose = vi.fn();
    render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                        onClose={onClose} onSaved={onSaved} />);
    fireEvent.change(screen.getByPlaceholderText(/build name/i), { target: { value: "My Build" } });
    fireEvent.click(screen.getByRole("button", { name: /add item/i }));       // opens modal
    fireEvent.change(screen.getByLabelText(/search items by name/i), { target: { value: "Death" } });
    fireEvent.click(screen.getByText("Deathbringer"));                        // picks + closes modal
    fireEvent.click(screen.getByRole("button", { name: /^save$/i }));
    expect(onSaved).toHaveBeenCalledWith("My Build");
    expect(onClose).toHaveBeenCalled();
    expect(getMine("Chiron", "Conquest")).toEqual([{ name: "My Build", slot_order: ["Deathbringer"] }]);
  });

  it("adds an item via the modal and shows it as a chosen slot with an icon", () => {
    const { container } = render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                        onClose={() => {}} onSaved={() => {}} />);
    fireEvent.click(screen.getByRole("button", { name: /add item/i }));
    fireEvent.click(screen.getByText("Deathbringer"));                        // modal closes, slot added
    expect(screen.getByText("Deathbringer")).toBeInTheDocument();             // chosen slot
    expect(Array.from(container.querySelectorAll("img")).some((i) => i.getAttribute("src")?.includes("deathbringer"))).toBe(true);
  });

  it("blocks saving with no name and surfaces an inline error", () => {
    render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                        onClose={() => {}} onSaved={() => {}} />);
    fireEvent.click(screen.getByRole("button", { name: /^save$/i }));
    expect(screen.getByText(/name required/i)).toBeInTheDocument();
    expect(getMine("Chiron", "Conquest")).toEqual([]);
  });

  it("deletes an existing build from the store", () => {
    const onSaved = vi.fn();
    render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                        initial={{ name: "Old", slot_order: ["Rage"] }}
                        onClose={() => {}} onSaved={onSaved} />);
    fireEvent.click(screen.getByRole("button", { name: /^delete$/i }));
    expect(onSaved).toHaveBeenCalled();
    expect(getMine("Chiron", "Conquest")).toEqual([]);
  });
});
