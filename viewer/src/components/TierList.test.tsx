import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { TierList } from "./TierList";
import type { GodTierEntry, ItemTierEntry } from "../types";
import { toHash } from "../lib/useHashRoute";

const gods: GodTierEntry[] = [
  { name: "Ymir", ours: 0.9, community: 0.3, tier_ours: "S", tier_community: "C", role: "Solo", damage_type: "magical" },
  { name: "Ra", ours: 0.5, community: 0.8, tier_ours: "B", tier_community: "A", role: "Mid", damage_type: "magical" },
  { name: "Anubis", ours: 0.2, community: null, tier_ours: "C", tier_community: null, role: "Mid", damage_type: "magical" },
];

const items: ItemTierEntry[] = [
  { name: "Rage", ours: 0.9, community: 0.5, tier_ours: "S", tier_community: "B", tier: 3, efficiency_tier: "undervalued" },
  { name: "Book of Thoth", ours: 0.1, community: null, tier_ours: "C", tier_community: null, tier: 3, efficiency_tier: "premium" },
];

beforeEach(() => {
  window.location.hash = "";
});

describe("TierList", () => {
  it("renders S/A/B/C bands from stub entries (gods, our calc)", () => {
    render(<TierList gods={gods} items={items} />);
    expect(within(screen.getByTestId("band-S")).getByText("Ymir")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-B")).getByText("Ra")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-C")).getByText("Anubis")).toBeInTheDocument();
    expect(screen.queryByTestId("band-A")).not.toBeInTheDocument();
  });

  it("re-buckets entries when the source toggle switches to Community", () => {
    render(<TierList gods={gods} items={items} />);
    fireEvent.click(screen.getByRole("button", { name: "Community" }));
    expect(within(screen.getByTestId("band-C")).getByText("Ymir")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-A")).getByText("Ra")).toBeInTheDocument();
    expect(screen.queryByTestId("band-S")).not.toBeInTheDocument();
  });

  it("switches subject from gods to items", () => {
    render(<TierList gods={gods} items={items} />);
    expect(screen.getByText("Ymir")).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "Items" }));
    expect(screen.queryByText("Ymir")).not.toBeInTheDocument();
    expect(screen.getByText("Rage")).toBeInTheDocument();
    expect(screen.getByText("Book of Thoth")).toBeInTheDocument();
  });

  it("narrows results with search", () => {
    render(<TierList gods={gods} items={items} />);
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "ra" } });
    expect(screen.getByText("Ra")).toBeInTheDocument();
    expect(screen.queryByText("Ymir")).not.toBeInTheDocument();
    expect(screen.queryByText("Anubis")).not.toBeInTheDocument();
  });

  it("shows the unranked group only under Community, labeled 'No community data'", () => {
    render(<TierList gods={gods} items={items} />);
    expect(screen.queryByText(/no community data/i)).not.toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "Community" }));
    expect(screen.getByText(/no community data/i)).toBeInTheDocument();
    expect(within(screen.getByTestId("band-unranked")).getByText("Anubis")).toBeInTheDocument();
  });

  it("navigates when an entry card is clicked", () => {
    render(<TierList gods={gods} items={items} />);
    fireEvent.click(screen.getByText("Ra"));
    expect(window.location.hash).toBe(toHash.god("Ra"));
  });

  it("shows an empty state with a clear-filters button when nothing matches", () => {
    render(<TierList gods={gods} items={items} />);
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "zzzznope" } });
    expect(screen.getByText(/no gods match/i)).toBeInTheDocument();
    fireEvent.click(screen.getByText(/clear filters/i));
    expect(screen.getByText("Ymir")).toBeInTheDocument();
  });
});
