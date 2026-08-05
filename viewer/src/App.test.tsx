import { describe, it, expect, beforeEach, vi } from "vitest";
import { render, screen, fireEvent, waitFor, within } from "@testing-library/react";
import App from "./App";
import { toHash } from "./lib/useHashRoute";

const data = {
  gods: [
    {
      name: "Chiron", pantheon: "Greek", role: "Carry", damage_type: "physical",
      base_stats: { health: { base: 569, per_level: 86 } }, abilities: [], aspects: [],
    },
    // A second god, so a draft-dock test can put one god in an enemy slot
    // and still have another god left to pick for the ally slot.
    {
      name: "Ymir", pantheon: "Norse", role: "Solo", damage_type: "magical",
      base_stats: {}, abilities: [], aspects: [],
    },
  ],
  items: [
    { name: "Rage", tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: "undervalued" },
  ],
  builds: [],
  starters: [],
  roster: [],
  data_updated: "2026-07-19",
  tierlist: {
    gods: [{ name: "Chiron", score: 0.47, win_rate: 0.52, matches: 380, play_share: 0.07, tier_score: "B", role: "Carry" }],
    items: [],
  },
  god_item_scores: { Chiron: { Rage: 0.49 }, Ymir: { Rage: 0.3 } },
};

const atUrl = (hash: string) => window.history.replaceState(null, "", `/${hash}`);

beforeEach(() => {
  atUrl("");
  localStorage.clear();
  vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ ok: true, json: () => Promise.resolve(data) }));
});

/* The shell's top level is a subject — the whole roster, or one god — with
 * lenses beneath it. There is no rail and no second navigation. */
describe("App — roster lenses", () => {
  it("opens on the roster board", async () => {
    render(<App />);
    await waitFor(() => expect(screen.getByTestId("subject-header")).toHaveTextContent(/All 2 gods/));
    // The strip lives in the navbar from md up; the same tabs keep their own
    // row below it. Only one is ever in the accessibility tree.
    const nav = within(screen.getByTestId("lens-tabs-bar"));
    expect(nav.getByRole("link", { name: "Board" })).toHaveAttribute("aria-current", "page");
  });

  it("moves between roster lenses", async () => {
    render(<App />);
    const nav = within(await screen.findByTestId("lens-tabs-bar"));
    fireEvent.click(nav.getByRole("link", { name: "Items" }));
    await waitFor(() => expect(
      screen.getByRole("heading", { level: 1, name: /cost less than their stats are worth/i })).toBeInTheDocument());
  });

  it("reaches the draft board, which is a roster lens rather than a god's", async () => {
    atUrl(toHash.draft());
    render(<App />);
    // The draft page's ally slot 1 is always labelled "You", filled or not.
    await waitFor(() => expect(screen.getAllByText("You")[0]).toBeInTheDocument());
    const nav = within(screen.getByTestId("lens-tabs-bar"));
    expect(nav.getByRole("link", { name: "Draft" })).toHaveAttribute("aria-current", "page");
  });

  it("shows no second navigation — the picker is a control, not a column", async () => {
    render(<App />);
    await screen.findByTestId("subject-header");
    expect(screen.queryByRole("button", { name: "Select Chiron" })).not.toBeInTheDocument();
    expect(screen.queryByRole("navigation", { name: "Main" })).not.toBeInTheDocument();
  });
});

/* The dock is the one thing meant to be visible on nearly every route — the
 * draft used to vanish the moment you left /draft, with no trace anywhere
 * else in the shell. */
describe("App — the draft dock", () => {
  it("is present on the roster board", async () => {
    render(<App />);
    await waitFor(() => expect(screen.getByTestId("draft-dock")).toBeInTheDocument());
  });

  it("is present on a god page", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await waitFor(() => expect(screen.getByTestId("draft-dock")).toBeInTheDocument());
  });

  // Showing a shrunken copy of the board you're already looking at would be a
  // second, redundant instance of the same controls.
  it("is absent on the draft page itself", async () => {
    atUrl(toHash.draft());
    render(<App />);
    await waitFor(() => expect(screen.getAllByText("You")[0]).toBeInTheDocument());
    expect(screen.queryByTestId("draft-dock")).not.toBeInTheDocument();
  });

  /* This is the bug the dock's existence created: Home's own draft seam
   * (`DraftSeam`) already calls `useDraft()` to show "your draft in
   * progress" — read-only, until now nothing else on the same page ever
   * wrote to the same draft while it was mounted. The dock is a second,
   * concurrent writer on that exact page. Without the cross-instance sync
   * added to `lib/draft.ts`, editing via the dock would leave the seam
   * showing stale data until Home remounted. */
  it("keeps Home's draft seam in sync when you edit from the dock", async () => {
    // An enemy already entered, so the dock opens in its full (not empty-
    // invitation) state and its toggle is reachable directly; a different
    // god is left free to pick for the ally slot.
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["", "", "", "", ""], enemies: ["Ymir", "", "", "", ""],
    }));
    render(<App />);
    // An enemy is already seeded, so the seam opens on its "in progress"
    // copy, not the empty invitation.
    await waitFor(() => expect(screen.getByTestId("home-draft")).toHaveTextContent(/your draft in progress/i));
    expect(screen.getByTestId("home-draft")).toHaveTextContent(/0 of \d+ allies/);

    const dockToggle = within(screen.getByTestId("draft-dock")).getByRole("button", { name: /add your god/i });
    fireEvent.click(dockToggle);
    fireEvent.click(within(screen.getByTestId("draft-dock")).getByRole("button", { name: "Add you" }));
    fireEvent.click(screen.getByRole("button", { name: "Chiron" }));

    // No remount of Home occurred — this is the same DraftSeam instance
    // picking up a write made through a sibling component's own useDraft().
    await waitFor(() => expect(screen.getByTestId("home-draft")).toHaveTextContent(/1 of \d+ allies/));
  });
});

describe("App — a god and its lenses", () => {
  it("makes the god the subject, on its own h1", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await waitFor(() => expect(screen.getByRole("heading", { level: 1, name: "Chiron" })).toBeInTheDocument());
  });

  it("carries the verdict on every lens, not just builds", async () => {
    atUrl(toHash.godKit("Chiron"));
    render(<App />);
    await waitFor(() => expect(screen.getByTestId("god-verdict")).toBeInTheDocument());
    expect(within(screen.getByTestId("god-verdict")).getByText("52%")).toBeInTheDocument();
  });

  it("opens the per-god item ranking — data no surface used to read", async () => {
    atUrl(toHash.godItems("Chiron"));
    render(<App />);
    await waitFor(() => expect(
      screen.getByRole("heading", { level: 2, name: /ranks 1 items for Chiron/i })).toBeInTheDocument());
  });

  it("opens the per-god ranking, led by the record rather than a comparison", async () => {
    atUrl(toHash.godRanking("Chiron"));
    render(<App />);
    await waitFor(() => expect(screen.getByRole("heading", { level: 2 }))
      .toHaveTextContent(/Chiron wins 52% of 380 tracked matches/i));
  });

  it("says so plainly when a link names a god this index doesn't have", async () => {
    atUrl(toHash.god("Nobody"));
    render(<App />);
    await waitFor(() => expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/No god called/i));
  });

  it("switches subject through the picker dialog", async () => {
    render(<App />);
    fireEvent.click(await screen.findByRole("button", { name: /choose a god/i }));
    const dialog = await screen.findByRole("dialog", { name: /choose a god/i });
    fireEvent.click(within(dialog).getByRole("button", { name: "Select Chiron" }));
    await waitFor(() => expect(window.location.hash).toBe(toHash.god("Chiron")));
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });
});

/* Three surfaces render the brand: the header, the loading skeleton and the
 * data-load failure screen. The failure screen still carried an "S2" square
 * from a previous identity — the one place the old mark survived, and the one
 * nobody looks at until something is already wrong. */
describe("App — the wordmark", () => {
  it("shows the ichor wordmark on the data-load failure screen, not a legacy badge", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ ok: false, status: 503 }));
    render(<App />);
    await screen.findByRole("heading", { name: /couldn.t load the build data/i });
    expect(screen.getByRole("img", { name: "ichor" })).toBeInTheDocument();
    expect(screen.queryByText("S2")).not.toBeInTheDocument();
    // The recovery this screen exists for still works.
    expect(screen.getByRole("button", { name: /try again/i })).toBeInTheDocument();
  });

  it("names the header wordmark once, not twice", async () => {
    render(<App />);
    await screen.findByTestId("subject-header");
    // The link carries its own label; the wordmark's `role="img"` name must
    // not leak into it and announce "ichor" a second time.
    const home = screen.getByRole("link", { name: "ichor — home" });
    expect(home).toBeInTheDocument();
    expect(screen.queryByRole("link", { name: /ichor ichor/i })).not.toBeInTheDocument();
  });
});

describe("App — chrome", () => {
  it("offers one search field, reaching gods and items", async () => {
    render(<App />);
    await screen.findByTestId("subject-search");
    expect(screen.getAllByRole("combobox")).toHaveLength(1);
    expect(screen.getByPlaceholderText(/search gods and items/i)).toBeInTheDocument();
  });

  /* Refetching a static index.json does nothing a visitor can see, so the
   * button read as broken: no result, no feedback. It is a pipeline tool. */
  it("keeps the data-reload control out of the deployed header", async () => {
    vi.stubEnv("DEV", false);
    render(<App />);
    await screen.findByTestId("subject-header");
    expect(screen.queryByRole("button", { name: /reload/i })).not.toBeInTheDocument();
    // The dev-only god editor goes with it.
    expect(screen.queryByRole("button", { name: /add god/i })).not.toBeInTheDocument();
    // What survives is the control a visitor actually needs.
    expect(screen.getByRole("button", { name: /help and credits/i })).toBeInTheDocument();
    vi.unstubAllEnvs();
  });

  it("reports what it did when the dev reload runs", async () => {
    vi.stubEnv("DEV", true);
    render(<App />);
    await screen.findByTestId("subject-header");
    const btn = screen.getByRole("button", { name: /reload/i });
    fireEvent.click(btn);
    // A control that runs silently is indistinguishable from a broken one.
    await waitFor(() => expect(btn).toHaveTextContent(/reloaded/i));
    vi.unstubAllEnvs();
  });

  it("redirects a retired #/gods URL to the roster board", async () => {
    atUrl("#/gods");
    render(<App />);
    await screen.findByTestId("subject-header");
    expect(window.location.hash).toBe("#/");
  });

  it("shows the data-freshness stamp as relative text with the absolute date on hover", async () => {
    render(<App />);
    const freshness = await screen.findByTestId("header-freshness");
    expect(freshness.textContent).toMatch(/^Updated /i);
    expect(freshness).toHaveAttribute("title", "2026-07-19");
  });

  it("omits the freshness stamp entirely when data_updated is missing", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({
      ok: true, json: () => Promise.resolve({ ...data, data_updated: undefined }),
    }));
    render(<App />);
    await screen.findByTestId("subject-header");
    expect(screen.queryByTestId("header-freshness")).not.toBeInTheDocument();
  });

  it("appends the current patch label to the header freshness stamp when data_patch is present", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({
      ok: true, json: () => Promise.resolve({ ...data, data_patch: "Open Beta 39" }),
    }));
    const freshness = await (render(<App />), screen.findByTestId("header-freshness"));
    expect(freshness.textContent).toMatch(/^Updated .+ · Open Beta 39$/);
  });

  it("omits the patch clause from the header stamp cleanly when data_patch is absent", async () => {
    render(<App />);
    const freshness = await screen.findByTestId("header-freshness");
    expect(freshness.textContent).not.toContain("·");
  });

  it("shows a layout-shaped skeleton (not a bare Loading… string) before data arrives", () => {
    render(<App />);
    expect(screen.getByTestId("home-skeleton")).toBeInTheDocument();
    expect(screen.queryByText(/^Loading…$/)).not.toBeInTheDocument();
  });

  it("uses the build-shell skeleton when the URL names a god", () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    expect(screen.getByTestId("app-skeleton")).toBeInTheDocument();
  });

  it("does not ambush a first-time visitor with the legend", async () => {
    render(<App />);
    await screen.findByTestId("header-freshness");
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });

  it("opens the legend on demand, carrying the attribution the footer used to hold", async () => {
    render(<App />);
    await screen.findByTestId("header-freshness");
    fireEvent.click(screen.getByRole("button", { name: /help and credits/i }));
    const dialog = await screen.findByRole("dialog");
    expect(dialog).toHaveAccessibleName(/how this works/i);
    expect(within(dialog).getByText(/not affiliated with Hi-Rez/i)).toBeInTheDocument();
  });

  // 43px of every screen, forever, for something you read once.
  it("has no permanent footer", async () => {
    render(<App />);
    await screen.findByTestId("subject-header");
    expect(screen.queryByRole("contentinfo")).not.toBeInTheDocument();
  });
});
