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
  // One table per mode — the god page's item lens reads the mode being viewed,
  // and used to read Conquest's under all three.
  god_item_scores: {
    Chiron: { conquest: { Rage: 0.49 }, joust: { Rage: 0.49 }, arena: { Rage: 0.49 } },
    Ymir: { conquest: { Rage: 0.3 }, joust: { Rage: 0.3 }, arena: { Rage: 0.3 } },
  },
};

const atUrl = (hash: string) => window.history.replaceState(null, "", `/${hash}`);

beforeEach(() => {
  atUrl("");
  localStorage.clear();
  vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ ok: true, json: () => Promise.resolve(data) }));
});

/* The match-first shell (direction B). The app opens on the match board;
 * one navigation pattern carries every route — a top bar ("Main") from lg up
 * and a bottom tab bar ("Tabs": Match · Gods · Tiers · More) on a phone.
 * jsdom renders both, so each test names the one it means. These replace the
 * Subject Frame assertions (lens strip, subject header, picker dialog, draft
 * dock), whose chrome this direction removes on purpose. */
describe("App — match-first chrome", () => {
  it("opens on the match board, with your slot asking who you are playing", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Your match" });
    expect(screen.getByRole("button", { name: /who are you playing/i })).toBeInTheDocument();
    const main = within(screen.getByRole("navigation", { name: "Main" }));
    expect(main.getByRole("link", { name: "Match" })).toHaveAttribute("aria-current", "page");
    const tabs = within(screen.getByRole("navigation", { name: "Tabs" }));
    expect(tabs.getByRole("link", { name: "Match" })).toHaveAttribute("aria-current", "page");
    expect(tabs.getByRole("link", { name: "Gods" })).toHaveAttribute("href", "#/roster");
    expect(tabs.getByRole("link", { name: "Tiers" })).toHaveAttribute("href", toHash.tiers());
    expect(tabs.getByRole("button", { name: "More" })).toBeInTheDocument();
  });

  it("moves between destinations from the top bar", async () => {
    render(<App />);
    const main = within(await screen.findByRole("navigation", { name: "Main" }));
    fireEvent.click(main.getByRole("link", { name: "Items" }));
    await waitFor(() => expect(
      screen.getByRole("heading", { level: 1, name: /cost less than their stats are worth/i })).toBeInTheDocument());
  });

  it("keeps the reading routes and the fan-project line under More on a phone", async () => {
    render(<App />);
    const tabs = within(await screen.findByRole("navigation", { name: "Tabs" }));
    fireEvent.click(tabs.getByRole("button", { name: "More" }));
    const sheet = within(await screen.findByRole("dialog", { name: "More" }));
    for (const name of [/Draft board/, /Items/, /Patch notes/, /Method/]) {
      expect(sheet.getByRole("link", { name })).toBeInTheDocument();
    }
    expect(sheet.getByRole("button", { name: /Help/ })).toBeInTheDocument();
    expect(sheet.getByText(/not affiliated with Hi-Rez/i)).toBeInTheDocument();
  });

  it("reaches the draft board inside the same chrome", async () => {
    atUrl(toHash.draft());
    render(<App />);
    // The draft page's ally slot 1 is always labelled "You", filled or not.
    await waitFor(() => expect(screen.getAllByText("You")[0]).toBeInTheDocument());
    const main = within(screen.getByRole("navigation", { name: "Main" }));
    expect(main.getByRole("link", { name: "Draft board" })).toHaveAttribute("aria-current", "page");
  });

  it("files a god page under Gods (browsing), and names your match god on the Match tab", async () => {
    localStorage.setItem("smite:draft", JSON.stringify({ mode: "conquest", allies: ["Ymir"], enemies: [] }));
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    const tabs = within(screen.getByRole("navigation", { name: "Tabs" }));
    expect(tabs.getByRole("link", { name: "Gods" })).toHaveAttribute("aria-current", "page");
    const main = within(screen.getByRole("navigation", { name: "Main" }));
    expect(main.getByRole("link", { name: /^Match.*Ymir$/ })).toHaveAttribute("href", toHash.home());
  });

  it("keeps a god's own views under the god, not in the global bar", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    const main = within(screen.getByRole("navigation", { name: "Main" }));
    expect(main.queryByRole("link", { name: "Kit" })).not.toBeInTheDocument();
    const own = within(screen.getByRole("navigation", { name: "More on Chiron" }));
    expect(own.getByRole("link", { name: "Kit" })).toHaveAttribute("href", "#/god/Chiron/kit");
  });

  it("does not mark the item shop current on a god's own item ranking", async () => {
    atUrl(toHash.godItems("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    const main = within(screen.getByRole("navigation", { name: "Main" }));
    expect(main.getByRole("link", { name: "Items" })).not.toHaveAttribute("aria-current");
    expect(main.getByRole("link", { name: "Gods" })).toHaveAttribute("aria-current", "page");
  });
});

/* The floating dock is gone from this shell: the match board IS the draft,
 * and the full draft page sits under More. These replace the dock tests and
 * keep their point — the comp you enter is ONE shared draft. */
describe("App — the enemy team on the match board", () => {
  it("has no floating draft dock; the board carries the enemy team and the god page doesn't", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Your match" });
    expect(screen.queryByTestId("draft-dock")).not.toBeInTheDocument();
    expect(screen.getByTestId("enemy-strip")).toBeInTheDocument();
    window.location.hash = toHash.god("Chiron");
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    expect(screen.queryByTestId("enemy-strip")).not.toBeInTheDocument();
    expect(screen.queryByTestId("draft-dock")).not.toBeInTheDocument();
  });

  it("writes picks from the match board into the shared draft, with you in slot one", async () => {
    localStorage.setItem("smite:draft", JSON.stringify({ mode: "conquest", allies: ["Chiron"], enemies: [] }));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Your match" });
    fireEvent.click(screen.getByRole("button", { name: "Add enemy 1" }));
    const sheet = await screen.findByRole("dialog", { name: /Enemy 1 of 5/ });
    // Keyboard up: the search field has focus, not the close button.
    expect(within(sheet).getByRole("searchbox")).toHaveFocus();
    fireEvent.click(within(sheet).getByRole("button", { name: "Ymir" }));
    // Auto-advance to the next empty slot rather than closing.
    await screen.findByRole("dialog", { name: /Enemy 2 of 5/ });
    await waitFor(() => {
      const stored = JSON.parse(localStorage.getItem("smite:draft") ?? "{}");
      expect(stored.enemies?.[0]).toBe("Ymir");
      expect(stored.allies?.[0]).toBe("Chiron");
    });
  });
});

describe("App — a god and its views", () => {
  it("makes the god the subject, on its own h1", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await waitFor(() => expect(screen.getByRole("heading", { level: 1, name: "Chiron" })).toBeInTheDocument());
  });

  it("states the Conquest record in the header, and refuses a tier in Joust", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await waitFor(() => expect(screen.getByTestId("god-record")).toHaveTextContent("Tier B on 380 Conquest games"));
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    await waitFor(() => expect(screen.getByTestId("god-record")).toHaveTextContent("No win data in Joust — model only"));
  });

  it("reads the mode from the address bar so it can be linked", async () => {
    atUrl(`${toHash.god("Chiron")}?mode=arena`);
    render(<App />);
    await waitFor(() => expect(screen.getByRole("button", { name: "Arena" })).toHaveAttribute("aria-pressed", "true"));
    expect(screen.getByTestId("god-record")).toHaveTextContent("No win data in Arena — model only");
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
    await waitFor(() => expect(screen.getAllByRole("heading", { level: 2 })[0])
      .toHaveTextContent(/Chiron wins 52% of 380 tracked matches/i));
  });

  it("says so plainly when a link names a god this index doesn't have", async () => {
    atUrl(toHash.god("Nobody"));
    render(<App />);
    await waitFor(() => expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/No god called/i));
  });

  it("switches god from the roster grid on the Gods tab", async () => {
    atUrl("#/roster");
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Every god" });
    const grid = within(await screen.findByTestId("god-grid"));
    expect(grid.getByRole("link", { name: /Chiron/ })).toHaveAttribute("href", toHash.god("Chiron"));
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
    await screen.findByRole("heading", { level: 1, name: "Your match" });
    // The link carries its own label; the wordmark's `role="img"` name must
    // not leak into it and announce "ichor" a second time.
    const home = screen.getByRole("link", { name: "ichor — your match" });
    expect(home).toBeInTheDocument();
    expect(screen.queryByRole("link", { name: /ichor ichor/i })).not.toBeInTheDocument();
  });
});

describe("App — chrome", () => {
  it("offers one search field on the god list, for gods", async () => {
    atUrl("#/roster");
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Every god" });
    expect(screen.getAllByRole("searchbox")).toHaveLength(1);
    expect(screen.getByPlaceholderText(/search 2 gods/i)).toBeInTheDocument();
  });

  it("keeps the match board free of search until your slot is tapped", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Your match" });
    expect(screen.queryByRole("searchbox")).not.toBeInTheDocument();
  });

  /* Refetching a static index.json does nothing a visitor can see, so the
   * button read as broken: no result, no feedback. It is a pipeline tool. */
  it("keeps the data-reload control out of the deployed header", async () => {
    vi.stubEnv("DEV", false);
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Your match" });
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
    await screen.findByRole("heading", { level: 1, name: "Your match" });
    const btn = screen.getByRole("button", { name: /reload/i });
    fireEvent.click(btn);
    // A control that runs silently is indistinguishable from a broken one.
    await waitFor(() => expect(btn).toHaveTextContent(/reloaded/i));
    vi.unstubAllEnvs();
  });

  it("redirects a retired #/gods URL to home, which is the match board", async () => {
    atUrl("#/gods");
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Your match" });
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
    await screen.findByRole("heading", { level: 1, name: "Your match" });
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
    await screen.findByRole("heading", { level: 1, name: "Your match" });
    expect(screen.queryByRole("contentinfo")).not.toBeInTheDocument();
  });
});
