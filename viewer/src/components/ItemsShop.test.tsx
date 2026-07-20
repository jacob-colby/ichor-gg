import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { ItemsShop } from "./ItemsShop";
import type { Item } from "../types";

const items = [
  { name: "Rage", tier: 3, cost: 2500, stats: { "Critical Chance": "20%" }, passive: "Crit up.", builds_from: [], builds_into: [], effect_tags: ["burst"], efficiency_tier: "undervalued" },
  { name: "Aegis", tier: 3, cost: 2100, stats: { "Max Health": "200" }, passive: "Shield.", builds_from: [], builds_into: [], effect_tags: ["aura"], efficiency_tier: "premium" },
] as unknown as Item[];

describe("ItemsShop", () => {
  it("renders a card per item with its efficiency label, and filters by search", () => {
    render(<ItemsShop items={items} openItem={undefined} />);
    expect(screen.getByText("Rage")).toBeInTheDocument();
    expect(screen.getByText("Aegis")).toBeInTheDocument();
    expect(screen.getByText("Underrated", { selector: "span" })).toBeInTheDocument();
    expect(screen.getByText("Overrated", { selector: "span" })).toBeInTheDocument();
    fireEvent.change(screen.getByPlaceholderText(/search items/i), { target: { value: "rage" } });
    expect(screen.getByText("Rage")).toBeInTheDocument();
    expect(screen.queryByText("Aegis")).not.toBeInTheDocument();
  });

  it("shows the item detail when openItem is set", () => {
    render(<ItemsShop items={items} openItem={"Rage"} />);
    expect(screen.getByText("Crit up.")).toBeInTheDocument(); // passive in the detail panel
  });
});
