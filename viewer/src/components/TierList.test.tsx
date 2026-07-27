import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, within, cleanup, waitFor } from "@testing-library/react";
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

/** Load the page *at* a URL, rather than navigating to it: assigning
 *  `window.location.hash` queues a `hashchange`, which lands mid-test and is
 *  decoded by the URL-state hook as a filter reset. */
const atUrl = (hash: string) => window.history.replaceState(null, "", `/${hash}`);

beforeEach(() => { atUrl(""); });


describe("TierList — bands and ghosts", () => {
  it("buckets into the model's bands", () => {
    render(<TierList tierlist={{ gods, items }} />);
    expect(within(screen.getByTestId("band-S")).getByText("Ymir")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-B")).getByText("Ra")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-C")).getByText("Anubis")).toBeInTheDocument();
    expect(screen.queryByTestId("band-A")).not.toBeInTheDocument();
  });

  it("carries the community's placement on the card, with no source toggle to reach it", () => {
    render(<TierList tierlist={{ gods, items }} />);
    // Ymir: model S, community C — the disagreement is readable in place, as
    // a verdict rather than as three decimals.
    expect(screen.getByTestId("band-S")).toHaveTextContent(/underrated/i);
    // The old "Our calc / Community" toggle is gone.
    expect(screen.queryByRole("button", { name: "Community" })).not.toBeInTheDocument();
    expect(screen.queryByRole("button", { name: /our calc/i })).not.toBeInTheDocument();
  });

  it("names both placements in each card's accessible name", () => {
    render(<TierList tierlist={{ gods, items }} />);
    const ymir = screen.getByRole("link", { name: /^Ymir:/ });
    expect(ymir).toHaveAccessibleName(/we place it S, the community places it C/);
    expect(ymir).toHaveAccessibleName(/we rate it higher/);
    // The figures are demoted, not deleted.
    expect(ymir).toHaveAttribute("title", expect.stringContaining("0.90"));
    expect(ymir).toHaveAttribute("title", expect.stringContaining("0.30"));
  });

  it("marks an entry with no community rating as unranked rather than hiding it", () => {
    render(<TierList tierlist={{ gods, items }} />);
    const anubis = within(screen.getByTestId("band-C"));
    expect(anubis.getByText(/no community rating/i)).toBeInTheDocument();
    expect(screen.getByRole("link", { name: /^Anubis:/ })).toHaveAccessibleName(/the community hasn't placed it/);
    // It stays in the model's own band — never bucketed into a separate group.
    expect(screen.queryByTestId("band-unranked")).not.toBeInTheDocument();
  });

  it("says so plainly when the two sources agree", () => {
    const agreeing: GodTierEntry[] = [
      { name: "Agni", ours: 0.8, community: 0.8, tier_ours: "S", tier_community: "S", role: "Mid", damage_type: "magical" },
    ];
    render(<TierList tierlist={{ gods: agreeing, items: [] }} />);
    // Scoped to the card — the headline claim also contains "agrees with".
    expect(within(screen.getByTestId("band-S")).getByText(/^Agreed$/)).toBeInTheDocument();
  });

  /* `tierGap` is null when the model never tiered an entry, and a null gap
   * reads as zero — so a card could claim the two sources "Agreed" about a
   * placement one of them never made. */
  it("never calls an untiered entry an agreement", () => {
    const untiered: ItemTierEntry[] = [
      { name: "Ghost Starter", ours: null, community: 0.4, tier_ours: null, tier_community: "B" },
    ];
    render(<TierList tierlist={{ gods: [], items: untiered }} />);
    fireEvent.click(screen.getByRole("button", { name: "Items" }));
    const card = within(screen.getByTestId("band-untiered"));
    expect(card.getByText(/not tiered by the model/i)).toBeInTheDocument();
    expect(card.queryByText(/^Agreed$/)).not.toBeInTheDocument();
  });

  it("leads the headline with the agreement count", () => {
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/agrees with\s*0 of 2\s*god placements/i);
  });

  it("tallies agreement across the whole list", () => {
    render(<TierList tierlist={{ gods, items }} />);
    const summary = within(screen.getByTestId("tier-summary"));
    // Ymir + Ra are ranked by both; Anubis isn't. Neither pair agrees.
    expect(summary.getByText(/0 of 2/)).toBeInTheDocument();
    expect(summary.getByText(/1 we rank higher/)).toBeInTheDocument();   // Ymir S vs C
    expect(summary.getByText(/1 the meta ranks higher/)).toBeInTheDocument(); // Ra B vs A
    expect(summary.getByText(/1 unranked/)).toBeInTheDocument();
  });

  it("tallies agreement per band", () => {
    render(<TierList tierlist={{ gods, items }} />);
    expect(within(screen.getByTestId("band-S")).getByText(/1 disputed/i)).toBeInTheDocument();
    expect(within(screen.getByTestId("band-C")).getByText(/1 unranked/i)).toBeInTheDocument();
  });

  it("links each card to its own page", () => {
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByRole("link", { name: /^Ra:/ })).toHaveAttribute("href", toHash.god("Ra"));
    fireEvent.click(screen.getByRole("button", { name: "Items" }));
    expect(screen.getByRole("link", { name: /^Rage:/ })).toHaveAttribute("href", toHash.item("Rage"));
  });
});

describe("TierList — controls", () => {
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

  it("orders a band by disagreement by default, and by score on request", () => {
    const band: GodTierEntry[] = [
      { name: "Close", ours: 0.9, community: 0.88, tier_ours: "S", tier_community: "A", role: "Mid", damage_type: "magical" },
      { name: "Far", ours: 0.7, community: 0.2, tier_ours: "S", tier_community: "C", role: "Mid", damage_type: "magical" },
    ];
    render(<TierList tierlist={{ gods: band, items: [] }} />);
    const names = () => within(screen.getByTestId("band-S")).getAllByRole("link").map((a) => a.textContent);
    expect(names()[0]).toMatch(/Far/);
    fireEvent.click(screen.getByRole("button", { name: /by score/i }));
    expect(names()[0]).toMatch(/Close/);
  });

  it("filters to only the disputed entries", () => {
    const mixed: GodTierEntry[] = [
      { name: "Agreed", ours: 0.8, community: 0.8, tier_ours: "S", tier_community: "S", role: "Mid", damage_type: "magical" },
      { name: "Disputed", ours: 0.8, community: 0.2, tier_ours: "S", tier_community: "C", role: "Mid", damage_type: "magical" },
    ];
    render(<TierList tierlist={{ gods: mixed, items: [] }} />);
    fireEvent.click(screen.getByRole("button", { name: /only disputed/i }));
    expect(screen.getByText("Disputed")).toBeInTheDocument();
    expect(screen.queryByText("Agreed")).not.toBeInTheDocument();
    // The summary still describes the whole set, not the narrowed view.
    expect(within(screen.getByTestId("tier-summary")).getByText(/1 of 2/)).toBeInTheDocument();
  });

  it("explains an empty disputed view rather than claiming nothing matched", () => {
    const allAgree: GodTierEntry[] = [
      { name: "Agni", ours: 0.8, community: 0.8, tier_ours: "S", tier_community: "S", role: "Mid", damage_type: "magical" },
    ];
    render(<TierList tierlist={{ gods: allAgree, items: [] }} />);
    fireEvent.click(screen.getByRole("button", { name: /only disputed/i }));
    expect(screen.getByText(/nothing disputed here/i)).toBeInTheDocument();
    expect(screen.getByText(/agree on the one god matching those filters/i)).toBeInTheDocument();
  });

  it("stays truthful about a disputed-view miss even when other filters are on", () => {
    // Regression: the honest copy used to appear only when "only disputed" was
    // the sole filter, so search + disputed claimed "no gods match" about a
    // god that matched perfectly well and simply wasn't disputed.
    const mixed: GodTierEntry[] = [
      { name: "Hecate", ours: 0.8, community: 0.8, tier_ours: "S", tier_community: "S", role: "Mid", damage_type: "magical" },
      { name: "Loki", ours: 0.8, community: 0.2, tier_ours: "S", tier_community: "C", role: "Jungle", damage_type: "physical" },
    ];
    render(<TierList tierlist={{ gods: mixed, items: [] }} />);
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "Hecate" } });
    fireEvent.click(screen.getByRole("button", { name: /only disputed/i }));
    expect(screen.getByText(/nothing disputed here/i)).toBeInTheDocument();
    expect(screen.queryByText(/no gods match/i)).not.toBeInTheDocument();
  });

  it("shows an empty state with a clear-filters button when nothing matches", () => {
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "zzzznope" } });
    expect(screen.getByText(/no gods match/i)).toBeInTheDocument();
    fireEvent.click(screen.getByText(/clear filters/i));
    expect(screen.getByText("Ymir")).toBeInTheDocument();
  });

  it("renders with no tierlist at all without crashing", () => {
    render(<TierList />);
    expect(screen.getByText(/no gods match/i)).toBeInTheDocument();
  });

  it("does not claim zero community coverage just because a search missed", () => {
    // Regression: the fallback summary was gated on the *filtered* set, so a
    // search miss printed "0 gods · no community ratings to compare against"
    // for Conquest, which has plenty.
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "zzzznope" } });
    expect(screen.queryByText(/no community ratings to compare against/i)).not.toBeInTheDocument();
  });

  it("draws the entries it counts, including ones the model hasn't tiered", () => {
    const withStarter: ItemTierEntry[] = [
      ...items,
      { name: "Bumba's Cudgel", ours: null, community: null, tier_ours: null, tier_community: null, tier: 1, efficiency_tier: null },
    ];
    render(<TierList tierlist={{ gods, items: withStarter }} />);
    fireEvent.click(screen.getByRole("button", { name: "Items" }));
    expect(within(screen.getByTestId("band-untiered")).getByText("Bumba's Cudgel")).toBeInTheDocument();
    // The header count and the drawn cards agree.
    expect(screen.getByText("3 items")).toBeInTheDocument();
  });
});

describe("TierList — Conquest/Joust", () => {
  const joustGods: GodTierEntry[] = [
    { name: "Achilles", ours: 0.55, community: null, tier_ours: "B", tier_community: null, role: "Solo", damage_type: "physical" },
    { name: "Nu Wa", ours: 0.9, community: null, tier_ours: "S", tier_community: null, role: "Mid", damage_type: "magical" },
  ];
  const joustItems: ItemTierEntry[] = [
    { name: "Rage", ours: 0.7, community: null, tier_ours: "A", tier_community: null, tier: 3, efficiency_tier: "undervalued" },
  ];
  const full = { gods, items, conquest: { gods, items }, joust: { gods: joustGods, items: joustItems } };

  it("defaults to Conquest and reads the per-mode slice", () => {
    render(<TierList tierlist={full} />);
    expect(screen.getByRole("button", { name: "Conquest" })).toHaveAttribute("aria-pressed", "true");
    expect(screen.getByText("Ymir")).toBeInTheDocument();
    expect(screen.queryByText("Nu Wa")).not.toBeInTheDocument();
  });

  it("switches to Joust and shows the Joust-specific entries", () => {
    render(<TierList tierlist={full} />);
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    expect(screen.getByText("Nu Wa")).toBeInTheDocument();
    expect(screen.getByText("Achilles")).toBeInTheDocument();
    expect(screen.queryByText("Ymir")).not.toBeInTheDocument();
  });

  it("states the Joust community gap as a coverage fact, not a loading state", () => {
    render(<TierList tierlist={full} />);
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    // Every god still shows, in the model's own bands.
    expect(within(screen.getByTestId("band-S")).getByText("Nu Wa")).toBeInTheDocument();
    expect(screen.getByText(/doesn.t track Joust/i)).toBeInTheDocument();
    expect(screen.getByText(/real coverage gap, not a/i)).toBeInTheDocument();
    // The summary can't claim agreement it has no basis for.
    expect(within(screen.getByTestId("tier-summary")).getByText(/no community ratings to compare/i)).toBeInTheDocument();
    // ...and there's nothing to filter to.
    expect(screen.queryByRole("button", { name: /only disputed/i })).not.toBeInTheDocument();
  });

  it("falls back to the legacy flat shape when a per-mode key is absent", () => {
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    expect(screen.getByText("Ymir")).toBeInTheDocument();
  });
});

/* "The disputed Mid gods in Joust" is exactly what this list is for, and it
 * was unlinkable. Defaults stay out of the query so a bare `#/tiers` keeps
 * meaning what it always did. */
describe("TierList — board state lives in the URL", () => {
  it("opens on the mode, subject and filters the link names", () => {
    atUrl("#/tiers?of=items&sort=score");
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByRole("button", { name: "Items" })).toHaveAttribute("aria-pressed", "true");
    expect(screen.getByRole("button", { name: /by score/i })).toHaveAttribute("aria-pressed", "true");
    expect(within(screen.getByTestId("band-S")).getByText("Rage")).toBeInTheDocument();
  });

  it("restores a lane filter, ignoring a lane the app doesn't have", () => {
    atUrl("#/tiers?lane=Mid");
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByRole("button", { name: "Mid" })).toHaveAttribute("aria-pressed", "true");
    expect(screen.queryByText("Ymir")).not.toBeInTheDocument();

    cleanup();
    atUrl("#/tiers?lane=Botlane");
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByText("Ymir")).toBeInTheDocument();
  });

  it("writes only what differs from the default", async () => {
    atUrl("#/tiers");
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    await waitFor(() => expect(window.location.hash).toBe("#/tiers?mode=joust"));
    fireEvent.click(screen.getByRole("button", { name: "Conquest" }));
    await waitFor(() => expect(window.location.hash).toBe("#/tiers"));
  });

  it("carries the disputed-only toggle", () => {
    atUrl("#/tiers?disputed=1");
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByRole("button", { name: /only disputed/i })).toHaveAttribute("aria-pressed", "true");
    // Anubis has no community rating, so it is neither agreed nor disputed.
    expect(screen.queryByText("Anubis")).not.toBeInTheDocument();
  });
});
