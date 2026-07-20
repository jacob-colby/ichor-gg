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
    expect(screen.getByText("Efficient", { selector: "span" })).toBeInTheDocument();
    expect(screen.getByText("Premium", { selector: "span" })).toBeInTheDocument();
    fireEvent.change(screen.getByPlaceholderText(/search items/i), { target: { value: "rage" } });
    expect(screen.getByText("Rage")).toBeInTheDocument();
    expect(screen.queryByText("Aegis")).not.toBeInTheDocument();
  });

  it("shows the item detail when openItem is set", () => {
    render(<ItemsShop items={items} openItem={"Rage"} />);
    expect(screen.getByText("Crit up.")).toBeInTheDocument(); // passive in the detail panel
  });

  it("shows a meta win badge for items that have community meta", () => {
    const withMeta = [
      { ...(items[0] as object), meta: { win_avg: 0.55, gods: 4 } },
      items[1],
    ] as unknown as Item[];
    render(<ItemsShop items={withMeta} openItem={undefined} />);
    expect(screen.getByText(/55% avg · 4/)).toBeInTheDocument();
  });
});
