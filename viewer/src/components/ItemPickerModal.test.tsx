import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { ItemPickerModal } from "./ItemPickerModal";
import type { Item } from "../types";

const items = [
  { name: "Deathbringer", tier: 3, cost: 3000, stats: {}, passive: "", builds_from: [], builds_into: [], effect_tags: ["burst"], efficiency_tier: "premium" },
  { name: "Rage", tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: "undervalued" },
] as unknown as Item[];

describe("ItemPickerModal", () => {
  it("filters by search and picks an item", () => {
    const onPick = vi.fn();
    render(<ItemPickerModal items={items} onPick={onPick} onClose={() => {}} />);
    fireEvent.change(screen.getByPlaceholderText(/search items/i), { target: { value: "death" } });
    expect(screen.queryByText("Rage")).not.toBeInTheDocument();
    fireEvent.click(screen.getByText("Deathbringer"));
    expect(onPick).toHaveBeenCalledWith("Deathbringer");
  });

  it("hides excluded items", () => {
    render(<ItemPickerModal items={items} exclude={["Rage"]} onPick={() => {}} onClose={() => {}} />);
    expect(screen.getByText("Deathbringer")).toBeInTheDocument();
    expect(screen.queryByText("Rage")).not.toBeInTheDocument();
  });
});
