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
  gods: [
    { name: "Ymir", role: "Solo", ours: 0.45, community: 0.68, tier_ours: "C", tier_community: "S" },
    { name: "Zeus", role: "Mid", ours: 0.52, community: 0.5, tier_ours: "A", tier_community: "A" },
    { name: "Agni", role: "Mid", ours: 0.5, community: null, tier_ours: "B", tier_community: null },
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

describe("Home divergence board", () => {
  it("states the disagreement count against the ranked total", () => {
    render(<Home data={baseData({ tierlist })} />);
    // Ymir (C vs S) disagrees; Zeus (A vs A) doesn't; Agni is unranked.
    const heading = screen.getByRole("heading", { level: 1 });
    expect(heading).toHaveTextContent(/we disagree with the meta on\s*1 of 2\s*ranked gods/i);
  });

  it("groups gods into lane columns ranked by disagreement", () => {
    render(<Home data={baseData({ tierlist })} />);
    const board = within(screen.getByTestId("home-divergence"));
    expect(board.getByRole("heading", { name: "Solo" })).toBeInTheDocument();
    expect(board.getByRole("heading", { name: "Mid" })).toBeInTheDocument();
    expect(board.getByRole("button", { name: /ymir/i })).toBeInTheDocument();
  });

  it("names both scores and the gap on each row so the numbers aren't bare decimals", () => {
    render(<Home data={baseData({ tierlist })} />);
    const board = within(screen.getByTestId("home-divergence"));
    const row = board.getByRole("button", { name: /^ymir/i });
    expect(row).toHaveAccessibleName(/model 0\.45 \(tier C\)/i);
    expect(row).toHaveAccessibleName(/community 0\.68 \(tier S\)/i);
    expect(row).toHaveAccessibleName(/gap -0\.23/i);
  });

  it("navigates to the god when a row is clicked", () => {
    render(<Home data={baseData({ tierlist })} />);
    const board = within(screen.getByTestId("home-divergence"));
    fireEvent.click(board.getByRole("button", { name: /^ymir/i }));
    expect(window.location.hash).toBe(toHash.god("Ymir"));
  });

  it("reports gods with no community data rather than hiding them", () => {
    render(<Home data={baseData({ tierlist })} />);
    const board = within(screen.getByTestId("home-divergence"));
    expect(board.getByText(/1 of 3 gods have no community data yet/i)).toBeInTheDocument();
    // ...and never invents a row for one.
    expect(board.queryByRole("button", { name: /^agni/i })).not.toBeInTheDocument();
  });

  it("omits the board entirely when there is no tierlist", () => {
    render(<Home data={baseData()} />);
    expect(screen.queryByTestId("home-divergence")).not.toBeInTheDocument();
  });

  it("omits the board when a tierlist exists but nothing is comparable", () => {
    const allUnranked = {
      gods: [
        { name: "Ymir", role: "Solo", ours: 0.5, community: null, tier_ours: "B", tier_community: null },
        { name: "Zeus", role: "Mid", ours: 0.5, community: null, tier_ours: "B", tier_community: null },
      ] as GodTierEntry[],
      items: [],
    };
    render(<Home data={baseData({ tierlist: allUnranked })} />);
    // No empty shell: no "Where we disagree", no bar key, no columns of nothing.
    expect(screen.queryByTestId("home-divergence")).not.toBeInTheDocument();
    expect(screen.queryByText(/where we disagree/i)).not.toBeInTheDocument();
    // ...and the claim steps back to something the data supports.
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/scored by a model/i);
  });

  it("shows both source scores on a row, not just the gap", () => {
    render(<Home data={baseData({ tierlist })} />);
    const row = within(screen.getByTestId("home-divergence")).getByRole("button", { name: /^ymir/i });
    expect(row).toHaveTextContent("0.45");
    expect(row).toHaveTextContent("0.68");
    expect(row).toHaveTextContent("-0.23");
  });

  it("falls back to a claim it can support when nothing is comparable", () => {
    render(<Home data={baseData()} />);
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/scored by a model/i);
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
    expect(within(screen.getByTestId("home-pinned")).getByText(/pin a god from its page/i)).toBeInTheDocument();
  });

  it("can unpin from Home without a trip to the god page", () => {
    localStorage.setItem("smite:pinnedGods", JSON.stringify(["Ymir"]));
    render(<Home data={baseData()} />);
    const pinned = within(screen.getByTestId("home-pinned"));
    fireEvent.click(pinned.getByRole("button", { name: /unpin ymir/i }));
    expect(pinned.queryByText("Ymir")).not.toBeInTheDocument();
    expect(pinned.getByText(/pin a god from its page/i)).toBeInTheDocument();
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
    expect(within(seam).getByRole("heading", { level: 2 })).toHaveTextContent(/drafting a match/i);
    expect(within(seam).getByRole("link", { name: /open the draft board/i }))
      .toHaveAttribute("href", toHash.draft());
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
