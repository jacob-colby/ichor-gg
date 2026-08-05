import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { Home } from "./Home";
import type { God, GodTierEntry, IndexData, PatchPeriod } from "../types";
import { toHash } from "../lib/useHashRoute";

const gods = [
  { name: "Agni", pantheon: "Hindu", role: "Mid", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
  { name: "Zeus", pantheon: "Greek", role: "Mid", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
  { name: "Ymir", pantheon: "Norse", role: "Solo", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
] as unknown as God[];

const tierlist = {
  // Six measured gods so the terciles behind "rarely played" are meaningful.
  // Hidden wins most and is played least; Famous wins nearly as much and is
  // played most, so only one of them should ever be flagged.
  gods: [
    { name: "Hidden", role: "Solo", score: 0.60, win_rate: 0.63, matches: 120, play_share: 0.01, tier_score: "S" },
    { name: "Famous", role: "Mid", score: 0.58, win_rate: 0.60, matches: 900, play_share: 0.13, tier_score: "S" },
    { name: "Steady", role: "Mid", score: 0.52, win_rate: 0.54, matches: 500, play_share: 0.09, tier_score: "A" },
    { name: "Middling", role: "Solo", score: 0.50, win_rate: 0.51, matches: 400, play_share: 0.07, tier_score: "B" },
    { name: "Poor", role: "Mid", score: 0.44, win_rate: 0.46, matches: 300, play_share: 0.05, tier_score: "C" },
    { name: "Worst", role: "Solo", score: 0.40, win_rate: 0.42, matches: 200, play_share: 0.02, tier_score: "C" },
    { name: "Unmeasured", role: "Mid", score: null, tier_score: null },
  ] as GodTierEntry[],
  items: [],
};

function baseData(overrides: Partial<IndexData> = {}): IndexData {
  return { gods, items: [], builds: [], ...overrides };
}

beforeEach(() => {
  window.location.hash = "";
  localStorage.clear();
});

describe("Home standings board", () => {
  /* The claim used to read "The community underrates N gods", which rested on
   * our ranking out-placing theirs. It didn't: measured against real god
   * strength our score correlated -0.117. What it says now uses only the
   * community's own two figures — how much a god wins, how often it's picked. */
  it("leads with a claim built from the community's own numbers", () => {
    render(<Home data={baseData({ tierlist })} />);
    const heading = screen.getByRole("heading", { level: 1 });
    expect(heading).toHaveTextContent(/1 god win(s)? more than anyone plays them/i);
    // Never "1 gods" — the count is interpolated, so the noun has to agree.
    expect(heading).not.toHaveTextContent(/1 gods/i);
  });

  it("never claims the site disagrees with the community", () => {
    render(<Home data={baseData({ tierlist })} />);
    expect(screen.queryByText(/underrate|overrate|where we disagree|argue hardest/i)).not.toBeInTheDocument();
  });

  it("falls back to the sample size when nothing is rarely played", () => {
    const flat = {
      gods: [
        { name: "A", role: "Mid", score: 0.52, win_rate: 0.54, matches: 500, play_share: 0.10, tier_score: "S" },
        { name: "B", role: "Mid", score: 0.50, win_rate: 0.52, matches: 500, play_share: 0.10, tier_score: "B" },
      ] as GodTierEntry[],
      items: [],
    };
    render(<Home data={baseData({ tierlist: flat })} />);
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/2 gods ranked on results/i);
  });

  it("groups gods into lane columns, best first", () => {
    render(<Home data={baseData({ tierlist })} />);
    const board = within(screen.getByTestId("home-standings"));
    expect(board.getByRole("heading", { name: "Solo" })).toBeInTheDocument();
    expect(board.getByRole("heading", { name: "Mid" })).toBeInTheDocument();
    expect(board.getByRole("button", { name: /hidden/i })).toBeInTheDocument();
  });

  it("speaks the record and the sample, so a row is never a bare word", () => {
    render(<Home data={baseData({ tierlist })} />);
    const row = within(screen.getByTestId("home-standings")).getByRole("button", { name: /^hidden/i });
    expect(row).toHaveAccessibleName(/wins 63%/i);
    expect(row).toHaveAccessibleName(/over 120 matches/i);
    expect(row).toHaveAccessibleName(/played in 1% of them/i);
  });

  it("marks a god that wins well and is rarely played", () => {
    render(<Home data={baseData({ tierlist })} />);
    const board = within(screen.getByTestId("home-standings"));
    expect(board.getByRole("button", { name: /^hidden/i })).toHaveAccessibleName(/rarely played/i);
    // Famous wins about as much but is played the most — not the same claim.
    expect(board.getByRole("button", { name: /^famous/i })).not.toHaveAccessibleName(/rarely played/i);
  });

  it("navigates to the god when a row is clicked", () => {
    render(<Home data={baseData({ tierlist })} />);
    const board = within(screen.getByTestId("home-standings"));
    fireEvent.click(board.getByRole("button", { name: /^hidden/i }));
    expect(window.location.hash).toBe(toHash.god("Hidden"));
  });

  it("reports gods with no usable sample rather than hiding or ranking them", () => {
    render(<Home data={baseData({ tierlist })} />);
    const board = within(screen.getByTestId("home-standings"));
    expect(board.getByText(/1 of 7 gods have too few tracked matches/i)).toBeInTheDocument();
    expect(board.queryByRole("button", { name: /^unmeasured/i })).not.toBeInTheDocument();
  });

  it("omits the board entirely when there is no tierlist", () => {
    render(<Home data={baseData()} />);
    expect(screen.queryByTestId("home-standings")).not.toBeInTheDocument();
  });

  it("omits the board when a tierlist exists but nothing is measured", () => {
    const none = {
      gods: [
        { name: "Ymir", role: "Solo", score: null, tier_score: null },
        { name: "Zeus", role: "Mid", score: null, tier_score: null },
      ] as GodTierEntry[],
      items: [],
    };
    render(<Home data={baseData({ tierlist: none })} />);
    // No empty shell: no board, no key, no columns of nothing.
    expect(screen.queryByTestId("home-standings")).not.toBeInTheDocument();
    expect(screen.queryByText(/what actually wins/i)).not.toBeInTheDocument();
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/reasoning shown/i);
  });

  /* A row leads with the figure a reader can act on and keeps the rest within
   * reach. Three decimals per row, thirty rows to a screen, was the thing that
   * read as a statistics table instead of a tier list. */
  it("leads a row with the win rate, not with a model score", () => {
    render(<Home data={baseData({ tierlist })} />);
    const row = within(screen.getByTestId("home-standings")).getByRole("button", { name: /^hidden/i });
    expect(row).toHaveTextContent("63%");
    expect(row).not.toHaveTextContent("0.60");
  });

  it("keeps the sample reachable on hover for anyone who wants it", () => {
    render(<Home data={baseData({ tierlist })} />);
    const row = within(screen.getByTestId("home-standings")).getByRole("button", { name: /^hidden/i });
    expect(row).toHaveAttribute("title", expect.stringContaining("120 matches"));
    expect(row).toHaveAttribute("title", expect.stringContaining("1% play share"));
  });

  it("falls back to a claim it can support when nothing is measured", () => {
    render(<Home data={baseData()} />);
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/reasoning shown/i);
  });
});

describe("Home pinned", () => {
  it("renders pinned gods", () => {
    localStorage.setItem("smite:pinnedGods", JSON.stringify(["Ymir"]));
    render(<Home data={baseData()} />);
    expect(within(screen.getByTestId("home-pinned")).getByText("Ymir")).toBeInTheDocument();
  });

  it("shows an inviting prompt when there are no pinned gods", () => {
    render(<Home data={baseData()} />);
    expect(within(screen.getByTestId("home-pinned")).getByText(/bookmark a god from its page/i)).toBeInTheDocument();
  });

  it("can remove a bookmark from Home without a trip to the god page", () => {
    localStorage.setItem("smite:pinnedGods", JSON.stringify(["Ymir"]));
    render(<Home data={baseData()} />);
    const pinned = within(screen.getByTestId("home-pinned"));
    fireEvent.click(pinned.getByRole("button", { name: /remove ymir from your bookmarks/i }));
    expect(pinned.queryByText("Ymir")).not.toBeInTheDocument();
    expect(pinned.getByText(/bookmark a god from its page/i)).toBeInTheDocument();
  });
});

describe("Home patch + freshness", () => {
  it("renders the latest patch period when patch_notes is non-empty", () => {
    const patch_notes: PatchPeriod[] = [
      { from: "2026-07-17", to: "2026-07-24", added: [], removed: [], changed: [{ name: "Rage", stats: {}, verdict: "buff" }] },
      { from: "2026-07-10", to: "2026-07-17", added: [], removed: [], changed: [{ name: "Book of Thoth", stats: {}, verdict: "nerf" }] },
    ];
    render(<Home data={baseData({ patch_notes })} />);
    const patch = within(screen.getByTestId("home-patch"));
    expect(patch.getByText(/2026-07-17.*2026-07-24/)).toBeInTheDocument();
    expect(patch.getByText("Rage")).toBeInTheDocument();
    expect(patch.queryByText("Book of Thoth")).not.toBeInTheDocument();
  });

  it("omits the patch section entirely when patch_notes is empty", () => {
    render(<Home data={baseData({ patch_notes: [] })} />);
    expect(screen.queryByTestId("home-patch")).not.toBeInTheDocument();
  });

  it("shows the freshness line with the absolute date available on hover", () => {
    render(<Home data={baseData({ data_updated: "2026-07-23" })} />);
    const freshness = screen.getByTestId("home-freshness");
    expect(freshness.textContent).toMatch(/updated/i);
    expect(freshness).toHaveAttribute("title", "2026-07-23");
  });

  it("omits the freshness line when data_updated is missing", () => {
    render(<Home data={baseData()} />);
    expect(screen.queryByTestId("home-freshness")).not.toBeInTheDocument();
  });

  it("appends the current game patch to the freshness line when data_patch is present", () => {
    render(<Home data={baseData({ data_updated: "2026-07-23", data_patch: "Open Beta 39" })} />);
    expect(screen.getByTestId("home-freshness").textContent).toMatch(/^Updated .+ · Open Beta 39$/);
  });

  it("omits the patch clause cleanly when data_patch is absent", () => {
    render(<Home data={baseData({ data_updated: "2026-07-23" })} />);
    expect(screen.getByTestId("home-freshness").textContent).not.toContain("·");
  });
});

/* Nothing in the app pointed at the draft board — you met it by clicking an
 * unlabelled rail icon and guessing. It also survives across sessions, so a
 * half-entered comp is worth handing back rather than leaving parked. */
describe("Home — the draft seam", () => {
  it("invites you in when no draft is saved", () => {
    render(<Home data={baseData({ tierlist })} />);
    const seam = screen.getByTestId("home-draft");
    expect(within(seam).getByRole("heading", { level: 2 })).toHaveTextContent(/build for the match you.re in/i);
    expect(within(seam).getByRole("link", { name: /open the draft board/i }))
      .toHaveAttribute("href", toHash.draft());
  });

  /* The seam existed and was still being missed: its heading used the quietest
   * tier the system has, in the same footer stack as the pinned list and the
   * freshness line. These pin the promotion so a later tidy-up can't quietly
   * demote it again. */
  it("titles itself at section strength, not as footer chrome", () => {
    render(<Home data={baseData({ tierlist })} />);
    const seam = screen.getByTestId("home-draft");
    const heading = within(seam).getByRole("heading", { level: 2 });
    // The quiet tier is `font-mono … text-faint`; this one is the display face.
    expect(heading.className).toContain("font-display");
    expect(heading.className).toContain("text-ink");
    expect(heading.className).not.toContain("text-faint");
  });

  it("carries the primary action as a gold button, not a text link", () => {
    // The Torchlight Rule allows gold for exactly three things, and this is
    // one of them: the surface's primary action.
    render(<Home data={baseData({ tierlist })} />);
    const cta = within(screen.getByTestId("home-draft")).getByRole("link", { name: /draft board/i });
    expect(cta.className).toContain("bg-gold");
    expect(cta.className).toContain("text-bg0");
  });

  it("is a raised panel, and only wears the gold ring while a draft is live", () => {
    // Flat-Until-It-Matters: the ring is a state, not decoration.
    const { unmount } = render(<Home data={baseData({ tierlist })} />);
    expect(screen.getByTestId("home-draft").className).toContain("plane");
    expect(screen.getByTestId("home-draft").className).not.toContain("is-selected");
    unmount();

    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["Agni", "", "", "", ""], enemies: ["", "", "", "", ""],
    }));
    render(<Home data={baseData({ tierlist })} />);
    expect(screen.getByTestId("home-draft").className).toContain("is-selected");
  });

  it("shows exactly one gold you-slot in the empty-state preview", () => {
    // Gold means "this one is yours" and a board has one. Drawn on both rows
    // it said the enemy team had a you-slot too.
    const { container } = render(<Home data={baseData({ tierlist })} />);
    const seam = within(container).getByTestId("home-draft");
    const gold = seam.querySelectorAll("span[aria-hidden] > span.border-gold");
    expect(gold).toHaveLength(1);
  });

  it("hands back a draft already in progress, named and countable", () => {
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["Agni", "", "", "", ""], enemies: ["Ymir", "Zeus", "", "", ""],
    }));
    render(<Home data={baseData({ tierlist })} />);
    const seam = screen.getByTestId("home-draft");
    expect(within(seam).getByRole("heading", { level: 2 })).toHaveTextContent(/your draft in progress/i);
    expect(seam).toHaveTextContent(/1 of 5\s*allies/i);
    expect(seam).toHaveTextContent(/2 of 5\s*enemies/i);
    expect(within(seam).getByRole("link", { name: /resume draft/i }))
      .toHaveAttribute("href", "#/draft?m=conquest&me=Agni&e=Ymir%2CZeus");
  });

  // An ally-only draft adapts nothing yet; saying so is the difference between
  // a resume link and a resume link that tells you what it still needs.
  it("says what a draft still needs when only allies are entered", () => {
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "joust", allies: ["Agni", "", ""], enemies: ["", "", ""],
    }));
    render(<Home data={baseData({ tierlist })} />);
    const seam = screen.getByTestId("home-draft");
    expect(seam).toHaveTextContent(/joust/i);
    expect(seam).toHaveTextContent(/0 of 3\s*enemies/i);
    expect(seam).toHaveTextContent(/add an enemy and it starts weighing Agni.s core/i);
  });

  /* Only the first ally slot has a build behind it. A draft carrying enemies
   * but no god of your own adapts nothing, and claiming otherwise — "the build
   * already answers those picks" — described a build that doesn't exist. */
  it("does not claim a build is adapting when your own slot is empty", () => {
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["", "", "", "", ""], enemies: ["Ymir", "", "", "", ""],
    }));
    render(<Home data={baseData({ tierlist })} />);
    const seam = screen.getByTestId("home-draft");
    expect(seam).toHaveTextContent(/your own slot is empty, so there.s no build to adapt yet/i);
    expect(seam).not.toHaveTextContent(/already answers/i);
  });

  // The draft adapts one god's core, not the site. The invitation used to say
  // "every build on the site re-sorts around them".
  it("claims only what the draft board actually does", () => {
    render(<Home data={baseData({ tierlist })} />);
    const seam = screen.getByTestId("home-draft");
    expect(seam).toHaveTextContent(/re-sorts that god.s core around them/i);
    expect(seam).not.toHaveTextContent(/every build on the site/i);
  });
});
