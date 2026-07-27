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
  ],
  items: [
    { name: "Rage", tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: "undervalued" },
  ],
  builds: [],
  starters: [],
  roster: [],
  data_updated: "2026-07-19",
  tierlist: {
    gods: [{ name: "Chiron", ours: 0.47, community: 0.58, tier_ours: "C", tier_community: "A", role: "Carry" }],
    items: [],
  },
  god_item_scores: { Chiron: { Rage: 0.49 } },
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
    await waitFor(() => expect(screen.getByTestId("subject-header")).toHaveTextContent(/All 1 gods/));
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
    expect(within(screen.getByTestId("god-verdict")).getByText("0.47")).toBeInTheDocument();
  });

  it("opens the per-god item ranking — data no surface used to read", async () => {
    atUrl(toHash.godItems("Chiron"));
    render(<App />);
    await waitFor(() => expect(
      screen.getByRole("heading", { level: 2, name: /ranks 1 items for Chiron/i })).toBeInTheDocument());
  });

  it("opens the per-god ranking against the meta", async () => {
    atUrl(toHash.godRanking("Chiron"));
    render(<App />);
    await waitFor(() => expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent(/the community\s*says/i));
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

describe("App — chrome", () => {
  it("offers one search field, reaching gods and items", async () => {
    render(<App />);
    await screen.findByTestId("subject-search");
    expect(screen.getAllByRole("combobox")).toHaveLength(1);
    expect(screen.getByPlaceholderText(/search gods and items/i)).toBeInTheDocument();
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
