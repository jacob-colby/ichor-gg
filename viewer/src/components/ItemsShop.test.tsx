import React from "react";
import { describe, it, expect } from "vitest";
import { render, screen, fireEvent, within, waitFor } from "@testing-library/react";
import { ItemsShop } from "./ItemsShop";
import type { Item, ItemTierEntry } from "../types";

const items = [
  { name: "Rage", tier: 3, cost: 2500, stats: { "Critical Chance": "20%" }, passive: "Crit up.",
    builds_from: [], builds_into: [], effect_tags: ["burst"], efficiency_tier: "undervalued",
    efficiency: { predicted_cost: 2900, residual: -400, score: 0.9 } },
  { name: "Aegis", tier: 3, cost: 2100, stats: { "Max Health": "200" }, passive: "Shield.",
    builds_from: [], builds_into: [], effect_tags: ["aura"], efficiency_tier: "premium",
    efficiency: { predicted_cost: 1800, residual: 300, score: 0.2 } },
  { name: "Pendant", tier: 1, cost: 700, stats: { "Max Health": "50" }, passive: "",
    builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: null, efficiency: null },
] as unknown as Item[];

const GOLD = { "Max Health": 0.88, "Critical Chance": 20 };

/** Load the page *at* a URL, rather than navigating to it: assigning
 *  `window.location.hash` queues a `hashchange`, which lands mid-test and is
 *  decoded by the URL-state hook as a filter reset. */
const atUrl = (hash: string) => window.history.replaceState(null, "", `/${hash}`);


const shop = (props: Partial<React.ComponentProps<typeof ItemsShop>> = {}) => (
  <ItemsShop items={items} openItem={undefined} goldValues={GOLD} {...props} />
);

describe("ItemsShop — the verdict, decomposed", () => {
  it("leads with how many items are underpriced", () => {
    render(shop());
    expect(screen.getByRole("heading", { level: 1 }))
      .toHaveTextContent(/1 of 3\s*items cost less than their stats are worth/i);
  });

  /* The card leads with the verdict in the same words the tier list and the
   * board use, then backs it with the arithmetic. The old "PREMIUM" chip said
   * the same thing in the shop's own private register. */
  it("leads with the verdict, then backs it with the gold", () => {
    render(shop());
    const rage = screen.getByRole("button", { name: /^Rage,/ });
    expect(rage).toHaveTextContent(/underpriced/i);
    expect(rage).toHaveTextContent("worth 2900g");
    expect(rage).toHaveTextContent("−400g");
    expect(rage).toHaveAccessibleName(/worth more than it costs/i);
    expect(rage).toHaveAccessibleName(/prices it at 2900 gold/i);
  });

  it("says an unscored item is unscored rather than showing a dash", () => {
    render(shop());
    const pendant = screen.getByRole("button", { name: /^Pendant,/ });
    expect(pendant).toHaveTextContent(/not priced by the model/i);
    expect(pendant).toHaveAccessibleName(/not scored by the gold model/i);
    expect(screen.getByText(/1 not priced \(starters\)/i)).toBeInTheDocument();
  });

  it("states the community coverage gap instead of leaving a blank", () => {
    render(shop());
    expect(screen.getByText(/0 of 3 have community data/i)).toBeInTheDocument();
    expect(screen.getAllByText(/no community data/i)).toHaveLength(3);
  });

  it("shows a community win rate where there is one", () => {
    const withMeta = [{ ...(items[0] as object), meta: { win_avg: 0.55, gods: 4 } }, items[1]] as unknown as Item[];
    render(shop({ items: withMeta }));
    expect(screen.getByText(/55% win · 4/)).toBeInTheDocument();
  });
});

describe("ItemsShop — the receipt", () => {
  it("prices each stat and closes the arithmetic", () => {
    render(shop({ openItem: "Aegis" }));
    // Scoped to the receipt: the Stats section below names the same stat.
    const receipt = within(screen.getByRole("table"));
    expect(receipt.getByText("Max Health")).toBeInTheDocument();
    expect(receipt.getByText("0.88g")).toBeInTheDocument();   // gold per unit
    expect(receipt.getByText("176g")).toBeInTheDocument();    // 200 x 0.88
    expect(receipt.getByText("Fair price")).toBeInTheDocument();
    expect(receipt.getByText("1800g")).toBeInTheDocument();
    expect(receipt.getByText("2100g")).toBeInTheDocument();   // also in the header
    expect(receipt.getByText("+300g")).toBeInTheDocument();
  });

  it("explains why a starter has no verdict rather than printing a dash", () => {
    render(shop({ openItem: "Pendant" }));
    expect(within(screen.getByRole("dialog"))
      .getByText(/tier-1 starters buy an ability rather than stats/i)).toBeInTheDocument();
  });

  it("names stats the fit never priced instead of silently dropping them", () => {
    const odd = [{ ...(items[0] as object), stats: { "Critical Chance": "20%", Mystery: "5" } }] as unknown as Item[];
    render(shop({ items: odd, openItem: "Rage" }));
    // The note names it; the Stats section lists it too.
    expect(within(screen.getByRole("dialog")).getByText(/not priced by the fit/i))
      .toHaveTextContent("Mystery");
  });

  it("shows where the community puts the item when the tier list has it", () => {
    const tierItems = [
      { name: "Rage", ours: 0.72, community: 0.44, tier_ours: "S", tier_community: "C" },
    ] as unknown as ItemTierEntry[];
    render(shop({ openItem: "Rage", tierItems }));
    const dialog = within(screen.getByRole("dialog"));
    expect(dialog.getByText("0.72")).toBeInTheDocument();
    expect(dialog.getByText("0.44")).toBeInTheDocument();
  });

  it("is a real dialog with a close control", () => {
    render(shop({ openItem: "Rage" }));
    const dialog = screen.getByRole("dialog");
    expect(dialog).toHaveAttribute("aria-modal", "true");
    expect(dialog).toHaveAccessibleName("Rage");
    expect(within(dialog).getByRole("button", { name: /close/i })).toBeInTheDocument();
  });

  it("closes on Escape by returning to the shop route", () => {
    atUrl("#/items/Rage");
    render(shop({ openItem: "Rage" }));
    fireEvent.keyDown(document, { key: "Escape" });
    expect(window.location.hash).toBe("#/items");
  });

  it("says so when a deep link names an item that is not here", () => {
    render(shop({ openItem: "Nonexistent Thing" }));
    expect(screen.getByText(/No item called/i)).toBeInTheDocument();
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });
});

describe("ItemsShop — filters", () => {
  it("searches tags and stats, not just names", () => {
    render(shop());
    fireEvent.change(screen.getByLabelText(/search items by name, tag, stat/i), { target: { value: "burst" } });
    expect(screen.getByText("Rage")).toBeInTheDocument();
    expect(screen.queryByText("Aegis")).not.toBeInTheDocument();
  });

  it("derives the tier control from the data, so no option is dead and none is missing", () => {
    render(shop());
    const tiers = within(screen.getByRole("group", { name: /item tier/i }));
    expect(tiers.getByRole("button", { name: "T3" })).toBeInTheDocument();
    expect(tiers.getByRole("button", { name: "T1" })).toBeInTheDocument();
    expect(tiers.queryByRole("button", { name: /glyph/i })).not.toBeInTheDocument();
  });

  it("filters by value rating from a pressed-state group", () => {
    render(shop());
    const rating = within(screen.getByRole("group", { name: /value rating/i }));
    fireEvent.click(rating.getByRole("button", { name: "Premium" }));
    expect(screen.getByText("Aegis")).toBeInTheDocument();
    expect(screen.queryByText("Rage")).not.toBeInTheDocument();
    expect(rating.getByRole("button", { name: "Premium" })).toHaveAttribute("aria-pressed", "true");
  });

  it("explains a no-match search and offers a way out", () => {
    render(shop());
    fireEvent.change(screen.getByLabelText(/search items by name/i), { target: { value: "zzzz" } });
    expect(screen.getByText(/No item matches/i)).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /clear filters/i }));
    expect(screen.getByText("Rage")).toBeInTheDocument();
  });

  it("reports the narrowed count against the whole set", () => {
    render(shop());
    fireEvent.change(screen.getByLabelText(/search items by name/i), { target: { value: "rage" } });
    // Scoped: the headline claim also reads "1 of 3".
    expect(screen.getByTestId("items-count")).toHaveTextContent("1 of 3");
  });
});

/* A filtered shelf is a thing worth sending someone. Before this it lived in
 * `useState`, so "the undervalued tier-3s" survived exactly as long as the tab
 * did — no link, no bookmark, no reload. */
describe("ItemsShop — filters live in the URL", () => {
  it("opens pre-filtered from a link", () => {
    atUrl("#/items?eff=premium");
    render(shop());
    expect(screen.getByText("Aegis")).toBeInTheDocument();
    expect(screen.queryByText("Rage")).not.toBeInTheDocument();
    const rating = within(screen.getByRole("group", { name: /value rating/i }));
    expect(rating.getByRole("button", { name: "Premium" })).toHaveAttribute("aria-pressed", "true");
  });

  it("decodes a numeric tier back to a number so it still matches", () => {
    atUrl("#/items?tier=1");
    render(shop());
    expect(screen.getByText("Pendant")).toBeInTheDocument();
    expect(screen.queryByText("Rage")).not.toBeInTheDocument();
  });

  it("writes a search into the hash and clears it back out again", async () => {
    atUrl("#/items");
    render(shop());
    fireEvent.change(screen.getByLabelText(/search items/i), { target: { value: "rage" } });
    await waitFor(() => expect(window.location.hash).toBe("#/items?q=rage"));
    fireEvent.click(screen.getByRole("button", { name: /^Clear$/ }));
    await waitFor(() => expect(window.location.hash).toBe("#/items"));
  });

  it("keeps the default sort out of the URL, and names any other", async () => {
    atUrl("#/items");
    render(shop());
    const sort = screen.getByLabelText(/sort items/i);
    fireEvent.change(sort, { target: { value: "cost-desc" } });
    await waitFor(() => expect(window.location.hash).toBe("#/items?sort=cost-desc"));
    fireEvent.change(sort, { target: { value: "value" } });
    await waitFor(() => expect(window.location.hash).toBe("#/items"));
  });

  // Clearing filters is not clearing the order — the order isn't a filter, and
  // resetting it would silently reshuffle the shelf under the visitor.
  it("leaves the chosen order alone when filters are cleared", async () => {
    atUrl("#/items?q=rage&sort=name");
    render(shop());
    fireEvent.click(screen.getByRole("button", { name: /^Clear$/ }));
    await waitFor(() => expect(window.location.hash).toBe("#/items?sort=name"));
  });

  it("carries the filters onto the item it opens, so closing comes back here", () => {
    atUrl("#/items?eff=premium");
    render(shop());
    fireEvent.click(screen.getByRole("button", { name: /^Aegis,/ }));
    expect(window.location.hash).toBe("#/items/Aegis?eff=premium");
  });
});
