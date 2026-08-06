import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, within, cleanup, waitFor } from "@testing-library/react";
import { TierList } from "./TierList";
import type { GodTierEntry, ItemTierEntry } from "../types";

/* Six measured gods, so the terciles behind "rarely played" are meaningful.
 * Ymir wins most and is played least; Ra wins nearly as much and is played
 * most. Anubis has no sample at all — every god outside Conquest looks like
 * that, and the whole point of the redesign is that it isn't ranked last. */
const gods: GodTierEntry[] = [
  { name: "Ymir", score: 0.58, win_rate: 0.62, matches: 120, play_share: 0.01, tier_score: "S", role: "Solo", damage_type: "magical" },
  { name: "Ra", score: 0.56, win_rate: 0.59, matches: 900, play_share: 0.13, tier_score: "S", role: "Mid", damage_type: "magical" },
  { name: "Agni", score: 0.52, win_rate: 0.54, matches: 500, play_share: 0.11, tier_score: "A", role: "Mid", damage_type: "magical" },
  { name: "Zeus", score: 0.50, win_rate: 0.51, matches: 400, play_share: 0.09, tier_score: "B", role: "Mid", damage_type: "magical" },
  { name: "Hades", score: 0.45, win_rate: 0.47, matches: 300, play_share: 0.08, tier_score: "C", role: "Mid", damage_type: "magical" },
  { name: "Thoth", score: 0.41, win_rate: 0.43, matches: 200, play_share: 0.02, tier_score: "C", role: "Mid", damage_type: "magical" },
  { name: "Anubis", score: null, tier_score: null, role: "Mid", damage_type: "magical" },
];

const items: ItemTierEntry[] = [
  { name: "Rage", score: 0.56, win_rate: 0.58, matches: 2000, tier_score: "S", tier: 3, efficiency_tier: "undervalued", value: 0.9 },
  { name: "Book of Thoth", score: null, tier_score: null, tier: 3, efficiency_tier: "premium", value: 0.1 },
];

/** Load the page *at* a URL, rather than navigating to it: assigning
 *  `window.location.hash` queues a `hashchange`, which lands mid-test and is
 *  decoded by the URL-state hook as a filter reset. */
const atUrl = (hash: string) => window.history.replaceState(null, "", `/${hash}`);

beforeEach(() => { atUrl(""); });

describe("TierList — bands from measured outcomes", () => {
  it("buckets into the measured bands", () => {
    render(<TierList tierlist={{ gods, items }} />);
    expect(within(screen.getByTestId("band-S")).getByText("Ymir")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-A")).getByText("Agni")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-B")).getByText("Zeus")).toBeInTheDocument();
  });

  it("shows the win rate and the sample on every card", () => {
    // A card showing only a rate reads equally sure at 120 matches and at 900.
    render(<TierList tierlist={{ gods, items }} />);
    const band = within(screen.getByTestId("band-S"));
    expect(band.getByText(/62% win/)).toBeInTheDocument();
    expect(band.getByText(/120 matches/)).toBeInTheDocument();
  });

  it("never presents a model score as a ranking", () => {
    // The whole correction: our own number correlated -0.117 with real god
    // strength and must not appear as a placement anywhere.
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.queryByText(/underrated|overrated|disputed|we rank higher/i)).not.toBeInTheDocument();
  });

  it("speaks the record in each card's accessible name", () => {
    render(<TierList tierlist={{ gods, items }} />);
    const card = screen.getByRole("link", { name: /^Ymir/ });
    expect(card).toHaveAccessibleName(/S tier/);
    expect(card).toHaveAccessibleName(/62% win rate over 120 matches/);
  });

  it("marks a god that wins well and is rarely played", () => {
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByRole("link", { name: /^Ymir/ })).toHaveAccessibleName(/rarely played/i);
    expect(screen.getByRole("link", { name: /^Ra/ })).not.toHaveAccessibleName(/rarely played/i);
  });

  it("puts an entry with no sample in its own group, never in the bottom band", () => {
    render(<TierList tierlist={{ gods, items }} />);
    const untiered = within(screen.getByTestId("band-untiered"));
    expect(untiered.getByText("Anubis")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-C")).queryByText("Anubis")).not.toBeInTheDocument();
    expect(screen.getByText(/“unmeasured” and “bad” are different facts/i)).toBeInTheDocument();
  });

  it("leads the headline with the evidence it rests on", () => {
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/ranked by\s*2,420\s*tracked god-games/i);
  });

  it("summarises what is placed and what is not", () => {
    render(<TierList tierlist={{ gods, items }} />);
    const summary = within(screen.getByTestId("tier-summary"));
    expect(summary.getByText("6")).toBeInTheDocument();
    expect(summary.getByText(/1 not measured/)).toBeInTheDocument();
  });

  it("links each card to its own page", () => {
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByRole("link", { name: /^Ymir/ })).toHaveAttribute("href", "#/god/Ymir");
  });
});

describe("TierList — controls", () => {
  it("switches subject from gods to items", () => {
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.click(screen.getByRole("button", { name: "Items" }));
    expect(within(screen.getByTestId("band-S")).getByText("Rage")).toBeInTheDocument();
    expect(screen.queryByText("Ymir")).not.toBeInTheDocument();
  });

  it("narrows results with search", () => {
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.change(screen.getByLabelText(/search gods/i), { target: { value: "ymir" } });
    expect(screen.getByText("Ymir")).toBeInTheDocument();
    expect(screen.queryByText("Agni")).not.toBeInTheDocument();
  });

  it("orders a band best-first by default, and by play on request", () => {
    render(<TierList tierlist={{ gods, items }} />);
    const names = () => within(screen.getByTestId("band-S")).getAllByRole("link").map((a) => a.textContent);
    expect(names()[0]).toMatch(/Ymir/);       // 0.58 beats 0.56
    fireEvent.click(screen.getByRole("button", { name: /most played/i }));
    expect(names()[0]).toMatch(/Ra/);         // 900 matches beats 120
  });

  it("filters to only the rarely-played gods", () => {
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.click(screen.getByRole("button", { name: /only rarely played/i }));
    expect(screen.getByText("Ymir")).toBeInTheDocument();
    expect(screen.queryByText("Ra")).not.toBeInTheDocument();
  });

  it("shows an empty state with a clear-filters button when nothing matches", () => {
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.change(screen.getByLabelText(/search gods/i), { target: { value: "zzzz" } });
    expect(screen.getByText(/no gods match those filters/i)).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /clear filters/i }));
    expect(screen.getByText("Ymir")).toBeInTheDocument();
  });

  it("renders with no tierlist at all without crashing", () => {
    render(<TierList />);
    expect(screen.getByRole("heading", { level: 1 })).toBeInTheDocument();
  });
});

describe("TierList — game modes", () => {
  // Joust and Arena publish no results, so every god there is unmeasured.
  const joustGods: GodTierEntry[] = [
    { name: "Nu Wa", score: null, tier_score: null, role: "Mid", damage_type: "magical" },
    { name: "Achilles", score: null, tier_score: null, role: "Solo", damage_type: "physical" },
  ];
  const full = {
    gods, items,
    conquest: { gods, items },
    joust: { gods: joustGods, items: [] },
    arena: { gods: [{ name: "Hercules", score: null, tier_score: null, role: "Solo" } as GodTierEntry], items: [] },
  };

  it("defaults to Conquest and reads the per-mode slice", () => {
    render(<TierList tierlist={full} />);
    expect(screen.getByRole("button", { name: "Conquest" })).toHaveAttribute("aria-pressed", "true");
    expect(screen.getByText("Ymir")).toBeInTheDocument();
    expect(screen.queryByText("Nu Wa")).not.toBeInTheDocument();
  });

  it("switches to Joust and shows its own entries", () => {
    render(<TierList tierlist={full} />);
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    expect(screen.getByText("Nu Wa")).toBeInTheDocument();
    expect(screen.queryByText("Ymir")).not.toBeInTheDocument();
  });

  it("states a mode with no results as a gap, and refuses to invent a ranking", () => {
    // This is the correction: these modes used to be ranked on the site's own
    // score, which measured -0.12 against real god strength.
    render(<TierList tierlist={full} />);
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/no outcome data for this mode/i);
    expect(screen.getByText(/publishes no Joust results/i)).toBeInTheDocument();
    expect(screen.getByText(/an empty page is the more/i)).toBeInTheDocument();
    expect(screen.queryByTestId("band-S")).not.toBeInTheDocument();
  });

  it("names the mode in the coverage note rather than hardcoding one", () => {
    render(<TierList tierlist={full} />);
    fireEvent.click(screen.getByRole("button", { name: "Arena" }));
    expect(screen.getByText(/publishes no Arena results/i)).toBeInTheDocument();
    expect(screen.queryByText(/publishes no Joust results/i)).not.toBeInTheDocument();
  });

  it("falls back to the legacy flat shape when a per-mode key is absent", () => {
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    expect(screen.getByText("Ymir")).toBeInTheDocument();
  });
});

/* "The rarely-played Mid gods" is exactly what this list is for, and it was
 * unlinkable. Defaults stay out of the query so a bare `#/tiers` keeps
 * meaning what it always did. */
describe("TierList — board state lives in the URL", () => {
  it("opens on the mode, subject and order the link names", () => {
    atUrl("#/tiers?of=items&sort=matches");
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByRole("button", { name: "Items" })).toHaveAttribute("aria-pressed", "true");
    expect(screen.getByRole("button", { name: /most played/i })).toHaveAttribute("aria-pressed", "true");
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

  it("carries the rarely-played toggle", () => {
    atUrl("#/tiers?hidden=1");
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByRole("button", { name: /only rarely played/i })).toHaveAttribute("aria-pressed", "true");
    expect(screen.queryByText("Ra")).not.toBeInTheDocument();
  });

  it("is linkable across every mode", async () => {
    atUrl("#/tiers");
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.click(screen.getByRole("button", { name: "Arena" }));
    await waitFor(() => expect(window.location.hash).toBe("#/tiers?mode=arena"));
  });
});

/* Same shrink-to-fit trap as the items shelf: a flex <a> sizes to its own text
 * rather than to its grid track unless told to fill. */
describe("TierList — a card fills its grid cell", () => {
  it("stretches the card surface to its track", () => {
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByRole("link", { name: /^Ymir/ }).className).toContain("w-full");
  });
});

/* A bookmark is the reader's own mark on their own list. It highlights, and it
 * deliberately does NOT reorder — the tier list ranks on outcomes and sorting
 * a saved god upward would undo exactly that. */
describe("TierList — bookmarked gods", () => {
  beforeEach(() => localStorage.setItem("smite:pinnedGods", JSON.stringify(["Ra"])));

  it("marks a bookmarked god and leaves the rest alone", () => {
    render(<TierList tierlist={{ gods, items }} />);
    expect(screen.getByRole("link", { name: /^Ra:/ })).toHaveAccessibleName(/bookmarked/i);
    expect(screen.getByRole("link", { name: /^Ymir:/ })).not.toHaveAccessibleName(/bookmarked/i);
  });

  it("keeps gold through hover instead of losing it", () => {
    // `hover:border-line-strong` as a constant in the base string beat
    // `border-gold/40`, so a bookmarked card went grey the moment you pointed
    // at it. It now hovers to MORE gold.
    render(<TierList tierlist={{ gods, items }} />);
    const cls = screen.getByRole("link", { name: /^Ra:/ }).className;
    expect(cls).toContain("border-gold/40");
    expect(cls).toContain("hover:border-gold/70");
    expect(cls).not.toContain("hover:border-line-strong");
  });

  it("does not reorder the ranking", () => {
    render(<TierList tierlist={{ gods, items }} />);
    // Ymir outranks Ra on score and must stay first despite Ra being saved.
    const names = within(screen.getByTestId("band-S")).getAllByRole("link").map((a) => a.textContent);
    expect(names[0]).toMatch(/Ymir/);
  });

  it("never marks an item, which cannot be bookmarked", () => {
    localStorage.setItem("smite:pinnedGods", JSON.stringify(["Rage"]));
    render(<TierList tierlist={{ gods, items }} />);
    fireEvent.click(screen.getByRole("button", { name: "Items" }));
    expect(screen.getByRole("link", { name: /^Rage:/ })).not.toHaveAccessibleName(/bookmarked/i);
  });
});

/* An aspect rewrites part of a kit and often the role with it, so "Sol" and
 * "Sol with Aspect of Conflagration" are different subjects, not one row with
 * a variant. They rank on the SAME Wilson bound as everything else here: an
 * aspect's sample is derived as its god's matches times how often it's taken. */
describe("TierList — aspects as their own subject", () => {
  const aspects = [
    { name: "Loki", god: "Loki", aspect: "Aspect of Agony", role: "Jungle",
      score: 0.53, win_rate: 0.62, matches: 126, play_share: 0.28, tier_score: "S" },
    { name: "Sol", god: "Sol", aspect: "Aspect of Conflagration", role: "Mid Carry",
      score: 0.50, win_rate: 0.59, matches: 139, play_share: 0.31, tier_score: "A" },
    { name: "Achilles", god: "Achilles", aspect: "Aspect of Prowess", role: "Solo",
      score: null, win_rate: 0.40, matches: 15, play_share: 0.06, tier_score: null },
  ] as unknown as import("../types").AspectTierEntry[];
  const full = { gods, items, conquest: { gods, items, aspects } };

  it("offers Aspects beside Gods and Items", () => {
    render(<TierList tierlist={full} />);
    expect(screen.getByRole("button", { name: "Aspects" })).toBeInTheDocument();
  });

  it("names the aspect on the card, under its god", () => {
    render(<TierList tierlist={full} />);
    fireEvent.click(screen.getByRole("button", { name: "Aspects" }));
    const card = within(screen.getByTestId("band-S")).getByRole("link", { name: /^Loki/ });
    expect(card).toHaveTextContent("Loki");
    expect(card).toHaveTextContent("Agony");           // "Aspect of" is stripped
    expect(card).toHaveAttribute("href", "#/god/Loki");
  });

  it("leaves a thinly-played aspect unranked rather than bottom-ranked", () => {
    render(<TierList tierlist={full} />);
    fireEvent.click(screen.getByRole("button", { name: "Aspects" }));
    expect(within(screen.getByTestId("band-untiered")).getByText("Achilles")).toBeInTheDocument();
    expect(screen.getByText(/a rumour, not a measurement/i)).toBeInTheDocument();
  });

  it("never claims an aspect is rarely played", () => {
    // `play_share` here is a share of the GOD's games, a different denominator
    // from the roster-wide one the tercile test uses.
    render(<TierList tierlist={full} />);
    fireEvent.click(screen.getByRole("button", { name: "Aspects" }));
    expect(screen.queryByRole("button", { name: /only rarely played/i })).not.toBeInTheDocument();
  });

  it("is linkable", () => {
    atUrl("#/tiers?of=aspects");
    render(<TierList tierlist={full} />);
    expect(screen.getByRole("button", { name: "Aspects" })).toHaveAttribute("aria-pressed", "true");
  });

  it("keeps the lane filter, which an aspect inherits from its god", () => {
    render(<TierList tierlist={full} />);
    fireEvent.click(screen.getByRole("button", { name: "Aspects" }));
    fireEvent.click(screen.getByRole("button", { name: "Jungle" }));
    expect(screen.getByText("Loki")).toBeInTheDocument();
    expect(screen.queryByText("Sol")).not.toBeInTheDocument();
  });
});
