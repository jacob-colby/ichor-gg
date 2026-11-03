import { describe, it, expect } from "vitest";
import { render, screen, within } from "@testing-library/react";
import { MethodPage } from "./MethodPage";
import type { Item, MethodData } from "../../types";

const method: MethodData = {
  signals: { efficiency: 0.35, win: 0.45, pick: 0.05, fit: 0.15 },
  kit_blend: 0.3,
  underrated: { max_pick: 0.15, top_quality_frac: 0.3 },
};
const items = [
  { name: "A", stats: { Penetration: "10", Strength: "40" } },
  { name: "B", stats: { Penetration: "10%", Strength: "30" } },
  { name: "C", stats: { Strength: "20" } },
] as unknown as Item[];
const gold = { _intercept: 1933, Strength: 10.88, Penetration: 8.63, "Penetration %": 38.92 };

describe("MethodPage", () => {
  it("is a reading page with a real h1", () => {
    render(<MethodPage method={method} goldValues={gold} items={items} godCount={89} />);
    expect(screen.getByRole("heading", { level: 1, name: "Method" })).toBeInTheDocument();
  });

  it("labels every blend weight with what it measures, read from the shipped weights", () => {
    render(<MethodPage method={method} goldValues={gold} items={items} godCount={89} />);
    const blend = within(screen.getByTestId("blend"));
    expect(blend.getByText("Gold efficiency").closest("li")).toHaveTextContent("weight 0.35 of the score");
    expect(blend.getByText("Community win rate").closest("li")).toHaveTextContent("weight 0.45 of the score");
    // The model build's renormalised blend is derived, not restated.
    expect(screen.getByText(/renormalised to weights/).textContent).toMatch(/0\.70.*0\.30/);
  });

  it("prices each penetration column on its own and marks a thin price", () => {
    render(<MethodPage method={method} goldValues={gold} items={items} godCount={89} />);
    const table = within(screen.getByTestId("gold-table"));
    expect(table.getByRole("columnheader", { name: "Gold a point" })).toBeInTheDocument();
    const pen = table.getByRole("rowheader", { name: "Penetration %" }).closest("tr")!;
    expect(pen).toHaveTextContent("38.92g");
    expect(pen).toHaveTextContent("thin");
    const str = table.getByRole("rowheader", { name: "Strength" }).closest("tr")!;
    expect(str).not.toHaveTextContent("thin");
  });

  it("states the intercept as a base price, never as a stat row", () => {
    render(<MethodPage method={method} goldValues={gold} items={items} godCount={89} />);
    expect(screen.queryByRole("rowheader", { name: /_intercept/ })).not.toBeInTheDocument();
    expect(screen.getByText(/base price of/).textContent).toContain("1,933g");
  });

  it("does not sell the model as out-ranking the community", () => {
    render(<MethodPage method={method} goldValues={gold} items={items} godCount={89} />);
    expect(document.body.textContent).not.toMatch(/disagreement between them is the product/i);
    expect(within(screen.getByTestId("limits")).getByText(/It is a filter, not a ranker/)).toBeInTheDocument();
  });

  it("renders without weights instead of inventing them", () => {
    render(<MethodPage goldValues={{}} items={items} godCount={89} />);
    expect(screen.queryByTestId("blend")).not.toBeInTheDocument();
    expect(screen.queryByTestId("gold-table")).not.toBeInTheDocument();
  });
});
