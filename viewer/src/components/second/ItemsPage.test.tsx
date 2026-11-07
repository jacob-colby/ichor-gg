import React from "react";
import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { ItemsPage } from "./ItemsPage";
import type { Item } from "../../types";

const items = [
  { name: "Rage", tier: 3, cost: 2500, stats: { "Critical Chance": "20%" }, passive: "Crit up.",
    builds_from: [], builds_into: [], effect_tags: ["burst"], efficiency_tier: "undervalued",
    efficiency: { predicted_cost: 2900, residual: -400, score: 0.9 }, meta: { win_avg: 0.55, matches: 1200 } },
  // Bucket says fair while the residual is +300: the bucket owns the word.
  { name: "Aegis", tier: 3, cost: 2100, stats: { "Max Health": "200" }, passive: "Shield.",
    builds_from: [], builds_into: [], effect_tags: ["aura"], efficiency_tier: "fair",
    efficiency: { predicted_cost: 1800, residual: 300, score: 0.2 } },
  { name: "Pendant", tier: 1, cost: 700, stats: { "Max Health": "50" }, passive: "Gain 1 stack on minion kill.",
    builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: null, efficiency: null },
  { name: "Acorn", tier: "God Specific", cost: 2000, stats: { "Max Health": "400" }, god: "Ratatoskr",
    passive: "Only one god can buy this.", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: "undervalued",
    efficiency: { predicted_cost: 3200, residual: -1200, score: 1, comparable: false } },
  { name: "Gem", tier: 3, cost: 2300, stats: { Intelligence: "85" }, passive: "",
    builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: "undervalued",
    efficiency: { predicted_cost: 2400, residual: -100, score: 0.6 } },
] as unknown as Item[];

const GOLD = { _intercept: 1100, "Max Health": 0.88, "Critical Chance %": 90, Intelligence: 15.29 };
const atUrl = (hash: string) => window.history.replaceState(null, "", `/${hash}`);
const page = (props: Partial<React.ComponentProps<typeof ItemsPage>> = {}) => (
  <ItemsPage items={items} goldValues={GOLD} {...props} />
);

beforeEach(() => atUrl("#/items"));

describe("ItemsPage — the ledger", () => {
  it("names itself and states the claim with live numbers, counting only items every god can buy", () => {
    render(page());
    expect(screen.getByRole("heading", { level: 1, name: "Items" })).toBeInTheDocument();
    // Rage and Gem are under; Acorn is too, but only Ratatoskr can act on it.
    expect(screen.getByTestId("items-claim")).toHaveTextContent("2 of 3 items are underpriced: they cost clearly less than their stats are worth.");
  });

  it("counts the claim by the pipeline's bucket, never the raw residual", () => {
    const noise = { ...items[1], name: "Ward", efficiency_tier: "fair", efficiency: { predicted_cost: 2140, residual: -40, score: 0.5 } };
    render(<ItemsPage items={[...items, noise] as typeof items} goldValues={GOLD} />);
    // Ward costs 40g less than its stats are worth, but the bucket calls it fair.
    expect(screen.getByTestId("items-claim")).toHaveTextContent("2 of 4 items are underpriced");
  });

  it("decomposes the arithmetic on every priced row: cost · worth · gap", () => {
    render(page());
    const aegis = screen.getAllByTestId("item-line").find((l) => l.textContent?.includes("Aegis"))!;
    expect(aegis).toHaveTextContent("2,100g · worth 1,800g · +300g");
  });

  it("takes the verdict word from the pipeline's bucket, not the residual's sign", () => {
    render(page());
    const aegis = screen.getAllByTestId("item-line").find((l) => l.textContent?.includes("Aegis"))!;
    expect(aegis).toHaveTextContent(/Fairly priced/);
    expect(aegis).not.toHaveTextContent(/Overpriced/);
  });

  it("sorts on the continuous residual, with a one-god item sinking to its own kind", () => {
    render(page());
    const order = screen.getAllByTestId("item-line").map((l) => l.getAttribute("aria-label")?.match(/^(\w+)/)?.[1]);
    expect(order).toEqual(["Rage", "Gem", "Aegis", "Acorn", "Pendant"]);
  });

  it("says a starter is not priced, in words", () => {
    render(page());
    const pendant = screen.getAllByTestId("item-line").find((l) => l.textContent?.includes("Pendant"))!;
    expect(pendant).toHaveTextContent(/Not priced/);
  });

  it("says whose a one-god item is", () => {
    render(page());
    expect(screen.getAllByTestId("item-line").find((l) => l.textContent?.includes("Acorn"))).toHaveTextContent("Ratatoskr only");
  });

  it("links to the working in the visitor's own words", () => {
    render(page());
    expect(screen.getByTestId("method-seam")).toHaveAttribute("href", "#/method");
  });
});

describe("ItemsPage — filters", () => {
  it("offers only the tiers and verdicts the data holds, behind a Filters sheet on a phone", () => {
    render(page());
    fireEvent.click(screen.getByRole("button", { name: /^Filters/ }));
    const sheet = within(screen.getByRole("dialog", { name: "Filters" }));
    const tiers = within(sheet.getByRole("group", { name: "Item tier" })).getAllByRole("button").map((b) => b.textContent);
    expect(tiers).toEqual(["T3", "T1", "God Specific"]);
    const verdicts = within(sheet.getByRole("group", { name: "Verdict" })).getAllByRole("button").map((b) => b.textContent?.replace(/\d+$/, ""));
    expect(verdicts).toEqual(["Underpriced", "Fairly priced", "Not priced"]);
  });

  it("opens pre-filtered from a link and narrows the list", () => {
    atUrl("#/items?eff=fair");
    render(page());
    expect(screen.getAllByTestId("item-line")).toHaveLength(1);
    expect(screen.getByTestId("items-count")).toHaveTextContent("1 of 5 items");
  });

  it("explains an empty search and offers a way out", () => {
    atUrl("#/items?q=zzz");
    render(page());
    expect(screen.getByText(/No item matches “zzz”/)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Clear filters" })).toBeInTheDocument();
  });
});

describe("ItemsPage — the receipt", () => {
  it("opens as a dialog whose rows add up to the worth, and whose worth and gap close on the cost", () => {
    atUrl("#/items/Gem");
    render(page({ openItem: "Gem" }));
    const dialog = screen.getByRole("dialog", { name: "Gem" });
    const receipt = within(within(dialog).getByTestId("receipt"));
    expect(receipt.getByText("Base price")).toBeInTheDocument();
    expect(receipt.getByText("85 × 15.29g a point")).toBeInTheDocument();
    // 1100 + 85 × 15.29 = 2399.65 → rounded onto the pipeline's 2,400.
    // Figures in the caption face split their "g" off to keep it lower case,
    // so the cells are read whole.
    const cells = receipt.getAllByRole("cell").map((c) => c.textContent);
    expect(cells).toEqual(["1,100g", "1,300g", "2,400g", "2,300g", "−100g"]);
    // Rows sum to the worth; cost − worth is the gap. The receipt closes.
    const n = (t: string | null) => Number((t ?? "").replace("−", "-").replace(/[^\d-]/g, ""));
    expect(n(cells[0]) + n(cells[1])).toBe(n(cells[2]));
    expect(n(cells[3]) - n(cells[2])).toBe(n(cells[4]));
    expect(receipt.getByText(/2,300g · worth 2,400g ·/)).toBeInTheDocument();
  });

  it("itemises a priced passive as its own row and stops calling the worth 'stats only'", () => {
    // 1100 + 40 × 15.29 + 500 × 0.97 = 2196.6 → the pipeline's 2,197.
    const edge = { name: "Edge", tier: 3, cost: 2000, stats: { Intelligence: "40" }, passive: "Hits harder.",
      builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: "undervalued",
      efficiency: { predicted_cost: 2197, residual: -197, score: 0.7, priced_passive: { "Passive Damage": 500 } } };
    render(<ItemsPage items={[...items, edge] as typeof items} goldValues={{ ...GOLD, "Passive Damage": 0.97 }} openItem="Edge" />);
    const receipt = within(within(screen.getByRole("dialog", { name: "Edge" })).getByTestId("receipt"));
    expect(receipt.getByRole("heading", { name: "What its stats and passive are worth" })).toBeInTheDocument();
    expect(receipt.getByText("Passive: damage it adds")).toBeInTheDocument();
    expect(receipt.getByText("500 × 0.97g a point")).toBeInTheDocument();
    expect(receipt.queryByText("Not itemised")).not.toBeInTheDocument();
    expect(receipt.queryByText(/^Stats only/)).not.toBeInTheDocument();
    const cells = receipt.getAllByRole("cell").map((c) => c.textContent);
    expect(cells).toEqual(["1,100g", "612g", "485g", "2,197g", "2,000g", "−197g"]);
  });

  it("explains why a tier-1 starter has no verdict rather than printing a dash", () => {
    render(page({ openItem: "Pendant" }));
    expect(within(screen.getByRole("dialog")).getByTestId("not-scored"))
      .toHaveTextContent(/Tier-1 starters buy an ability rather than stats/);
  });

  it("says an item with no community record is unmeasured, not losing", () => {
    render(page({ openItem: "Aegis" }));
    expect(within(screen.getByRole("dialog")).getByText(/not measured, which is not the same as losing/)).toBeInTheDocument();
  });

  it("closes on Escape back to the list, keeping its filters", () => {
    atUrl("#/items/Rage?eff=undervalued");
    render(page({ openItem: "Rage" }));
    fireEvent.keyDown(screen.getByRole("dialog"), { key: "Escape" });
    expect(window.location.hash).toBe("#/items?eff=undervalued");
  });

  it("says so when a link names an item that is not here", () => {
    render(page({ openItem: "Nope" }));
    expect(screen.getByText(/No item called “Nope”/)).toBeInTheDocument();
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });
});
