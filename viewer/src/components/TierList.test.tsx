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
    render(<TierList tierlist={{ gods, items }} />);
    expect(within(screen.getByTestId("band-S")).getByText("Ymir")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-B")).getByText("Ra")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-C")).getByText("Anubis")).toBeInTheDocument();
    expect(screen.queryByTestId("band-A")).not.toBeInTheDocument();
  });

  it("re-buckets entries when the source toggle switches to Community", () => {
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.click(screen.getByRole("button", { name: "Community" }));
    expect(within(screen.getByTestId("band-C")).getByText("Ymir")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-A")).getByText("Ra")).toBeInTheDocument();
    expect(screen.queryByTestId("band-S")).not.toBeInTheDocument();
  });

  it("switches subject from gods to items", () => {
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByText("Ymir")).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "Items" }));
    expect(screen.queryByText("Ymir")).not.toBeInTheDocument();
    expect(screen.getByText("Rage")).toBeInTheDocument();
    expect(screen.getByText("Book of Thoth")).toBeInTheDocument();
  });

  it("narrows results with search", () => {
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "ra" } });
    expect(screen.getByText("Ra")).toBeInTheDocument();
    expect(screen.queryByText("Ymir")).not.toBeInTheDocument();
    expect(screen.queryByText("Anubis")).not.toBeInTheDocument();
  });

  it("shows the unranked group only under Community, labeled 'No community data'", () => {
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.queryByText(/no community data/i)).not.toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "Community" }));
    expect(screen.getByText(/no community data/i)).toBeInTheDocument();
    expect(within(screen.getByTestId("band-unranked")).getByText("Anubis")).toBeInTheDocument();
  });

  it("navigates when an entry card is clicked", () => {
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.click(screen.getByText("Ra"));
    expect(window.location.hash).toBe(toHash.god("Ra"));
  });

  it("shows an empty state with a clear-filters button when nothing matches", () => {
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "zzzznope" } });
    expect(screen.getByText(/no gods match/i)).toBeInTheDocument();
    fireEvent.click(screen.getByText(/clear filters/i));
    expect(screen.getByText("Ymir")).toBeInTheDocument();
  });

  it("renders with no tierlist at all (empty state, no crash)", () => {
    render(<TierList />);
    expect(screen.getByText(/no gods match/i)).toBeInTheDocument();
  });
});

describe("TierList — Conquest/Joust toggle (Task R2 follow-up)", () => {
  const joustGods: GodTierEntry[] = [
    { name: "Achilles", ours: 0.55, community: null, tier_ours: "B", tier_community: null, role: "Solo", damage_type: "physical" },
    { name: "Nu Wa", ours: 0.9, community: null, tier_ours: "S", tier_community: null, role: "Mid", damage_type: "magical" },
  ];
  const joustItems: ItemTierEntry[] = [
    { name: "Rage", ours: 0.7, community: null, tier_ours: "A", tier_community: null, tier: 3, efficiency_tier: "undervalued" },
  ];
  const full = {
    gods, items,
    conquest: { gods, items },
    joust: { gods: joustGods, items: joustItems },
  };

  it("defaults to Conquest and reads the per-mode slice", () => {
    render(<TierList tierlist={full} />);
    expect(screen.getByRole("button", { name: "Conquest" })).toHaveClass("bg-gold");
    expect(screen.getByText("Ymir")).toBeInTheDocument();
    expect(screen.queryByText("Nu Wa")).not.toBeInTheDocument();
  });

  it("switches to Joust and shows the Joust-specific entries (our calc, fully populated)", () => {
    render(<TierList tierlist={full} />);
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    expect(screen.getByText("Nu Wa")).toBeInTheDocument();
    expect(screen.getByText("Achilles")).toBeInTheDocument();
    expect(screen.queryByText("Ymir")).not.toBeInTheDocument();
    // tier_ours is fully populated for Joust — no "unranked" group under Our calc.
    expect(screen.queryByTestId("band-unranked")).not.toBeInTheDocument();
  });

  it("falls back to the legacy flat shape when a per-mode key is absent", () => {
    render(<TierList tierlist={{ gods, items }} />);
    // No `joust` key at all on this index — Joust must not crash, and (per
    // the fallback rule) shows the same flat data rather than an empty page.
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    expect(screen.getByText("Ymir")).toBeInTheDocument();
  });

  it("shows every Joust god as unranked under Community, with a factual explanatory note (0/87 coverage is real, not a bug)", () => {
    render(<TierList tierlist={full} />);
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    fireEvent.click(screen.getByRole("button", { name: "Community" }));
    expect(screen.getByText(/no community data/i)).toBeInTheDocument();
    expect(within(screen.getByTestId("band-unranked")).getByText("Achilles")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-unranked")).getByText("Nu Wa")).toBeInTheDocument();
    expect(screen.queryByTestId("band-S")).not.toBeInTheDocument();
    // The page explains why, rather than looking broken.
    expect(screen.getByText(/joust has no community/i)).toBeInTheDocument();
  });
});
