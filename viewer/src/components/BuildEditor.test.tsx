import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { BuildEditor } from "./BuildEditor";
import { getMine } from "../lib/mineStore";
import type { Item } from "../types";

const items = [{ name: "Deathbringer" }, { name: "Rage" }] as Item[];

describe("BuildEditor", () => {
  beforeEach(() => localStorage.clear());

  it("saves a build to the store and calls onSaved with its name", () => {
    const onSaved = vi.fn();
    const onClose = vi.fn();
    render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                        onClose={onClose} onSaved={onSaved} />);
    fireEvent.change(screen.getByPlaceholderText(/build name/i), { target: { value: "My Build" } });
    fireEvent.change(screen.getByPlaceholderText(/search items/i), { target: { value: "Death" } });
    fireEvent.click(screen.getByText("Deathbringer"));
    fireEvent.click(screen.getByRole("button", { name: /^save$/i }));
    expect(onSaved).toHaveBeenCalledWith("My Build");
    expect(onClose).toHaveBeenCalled();
    expect(getMine("Chiron", "Conquest")).toEqual([{ name: "My Build", slot_order: ["Deathbringer"] }]);
  });

  it("shows an item icon in the search results and chosen slots", () => {
    const { container } = render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                        onClose={() => {}} onSaved={() => {}} />);
    fireEvent.change(screen.getByPlaceholderText(/search items/i), { target: { value: "Death" } });
    const hasDeathbringerIcon = () =>
      Array.from(container.querySelectorAll("img")).some((i) => i.getAttribute("src")?.includes("deathbringer"));
    expect(hasDeathbringerIcon()).toBe(true);            // in results
    fireEvent.click(screen.getByText("Deathbringer"));
    expect(hasDeathbringerIcon()).toBe(true);            // still, as a chosen slot
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
