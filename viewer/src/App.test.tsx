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

/* The "Type it" shell (direction C). One command field is the navigation;
 * Menu holds every other destination. jsdom has no matchMedia, so these run
 * the phone layout: the field docked at the bottom with Menu beside it. They
 * replace direction A's tab-bar assertions ("Main" / "Tabs" / More), whose
 * chrome this direction removes on purpose, and keep their points: every
 * destination is reachable, the fan-project line is one level down, a god's
 * own views stay under the god. */
const field = () => screen.getByRole("combobox", { name: /your god, vs the enemy team/i });
const openMenu = async () => {
  fireEvent.click(screen.getByRole("button", { name: "Menu" }));
  return within(await screen.findByRole("dialog", { name: "Menu" }));
};

describe("App — the command field is the navigation", () => {
  it("opens on an empty field, with the roster below as the fallback", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /type your matchup/i });
    expect(field()).toHaveValue("");
    expect(field()).toHaveAttribute("placeholder", "ra vs hecate ymir");
    expect(within(screen.getByTestId("god-grid")).getByRole("link", { name: /Chiron/ }))
      .toHaveAttribute("href", toHash.god("Chiron"));
  });

  it("turns typed words into chips and offers gods as tappable rows", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /type your matchup/i });
    fireEvent.change(field(), { target: { value: "chi " } });
    expect(screen.getByRole("img", { name: "You: Chiron" })).toBeInTheDocument();
    fireEvent.change(field(), { target: { value: "y" } });
    const list = within(screen.getByRole("listbox", { name: "Suggestions" }));
    fireEvent.click(list.getByRole("option", { name: /Ymir/ }));
    expect(screen.getByRole("img", { name: "Enemy: Ymir" })).toBeInTheDocument();
  });

  it("goes to the god page on Enter, writes the team into the shared draft, and links the chips", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /type your matchup/i });
    fireEvent.change(field(), { target: { value: "chiron vs ym" } });
    fireEvent.keyDown(field(), { key: "Enter" });
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    expect(window.location.hash).toBe("#/god/Chiron?vs=Ymir");
    const stored = JSON.parse(localStorage.getItem("smite:draft") ?? "{}");
    expect(stored.allies?.[0]).toBe("Chiron");
    expect(stored.enemies?.[0]).toBe("Ymir");
    // The field stays as the header, showing the query as chips.
    await waitFor(() => expect(screen.getByRole("button", { name: "Enemy 1: Ymir. Change" })).toBeInTheDocument());
    expect(screen.getByRole("img", { name: "You: Chiron" })).toBeInTheDocument();
    // And the landing page remembers it.
    expect(JSON.parse(localStorage.getItem("ichor:recent-queries") ?? "[]")).toEqual(["Chiron vs Ymir"]);
  });

  it("reproduces the chips from a pasted link", async () => {
    atUrl("#/god/Chiron?mode=joust&vs=Ymir");
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    await waitFor(() => expect(screen.getByRole("button", { name: "Enemy 1: Ymir. Change" })).toBeInTheDocument());
    expect(screen.getByRole("button", { name: "Joust" })).toHaveAttribute("aria-pressed", "true");
    expect(document.querySelector("[data-chip='mode']")).toHaveTextContent("Joust");
    await waitFor(() => expect(JSON.parse(localStorage.getItem("smite:draft") ?? "{}").enemies?.[0]).toBe("Ymir"));
  });

  it("lists recent queries on the landing page, one tap from the build", async () => {
    localStorage.setItem("ichor:recent-queries", JSON.stringify(["Chiron vs Ymir"]));
    render(<App />);
    const recents = within(await screen.findByTestId("recents"));
    const row = recents.getByRole("link", { name: /Chiron/ });
    expect(row).toHaveAttribute("href", "#/god/Chiron?vs=Ymir");
  });

  it("keeps every other destination and the fan-project line under Menu", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /type your matchup/i });
    const menu = await openMenu();
    for (const name of [/Draft/, /Gods/, /Tiers/, /Items/, /Patch notes/, /Method/]) {
      expect(menu.getByRole("link", { name })).toBeInTheDocument();
    }
    expect(menu.getByRole("button", { name: /Help and credits/ })).toBeInTheDocument();
    expect(menu.getByText(/not affiliated with Hi-Rez/i)).toBeInTheDocument();
    expect(menu.getByRole("link", { name: /Gods/ })).toHaveAttribute("aria-current", "page");
  });

  it("moves between destinations from Menu", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /type your matchup/i });
    const menu = await openMenu();
    fireEvent.click(menu.getByRole("link", { name: /Items/ }));
    await waitFor(() => expect(
      screen.getByRole("heading", { level: 1, name: /cost less than their stats are worth/i })).toBeInTheDocument());
  });

  it("reaches the draft board inside the same chrome", async () => {
    atUrl(toHash.draft());
    render(<App />);
    await waitFor(() => expect(screen.getAllByText("You")[0]).toBeInTheDocument());
    expect(field()).toBeInTheDocument();
    const menu = await openMenu();
    expect(menu.getByRole("link", { name: /Draft/ })).toHaveAttribute("aria-current", "page");
  });

  it("marks Build current on a god page and points it at that god", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    const build = (await openMenu()).getByRole("link", { name: /Build · Chiron/ });
    expect(build).toHaveAttribute("aria-current", "page");
    expect(build).toHaveAttribute("href", toHash.god("Chiron"));
  });

  it("keeps a god's own views under the god, not in the menu", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    const own = within(screen.getByRole("navigation", { name: "More on Chiron" }));
    expect(own.getByRole("link", { name: "Kit" })).toHaveAttribute("href", "#/god/Chiron/kit");
    const menu = await openMenu();
    expect(menu.queryByRole("link", { name: "Kit" })).not.toBeInTheDocument();
  });

  it("does not mark the item shop current on a god's own item ranking", async () => {
    atUrl(toHash.godItems("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    const menu = await openMenu();
    expect(menu.getByRole("link", { name: /^Items/ })).not.toHaveAttribute("aria-current");
    expect(menu.getByRole("link", { name: /Build · Chiron/ })).toHaveAttribute("aria-current", "page");
  });
});

/* No floating draft dock: on a phone the field's chips ARE the enemy team
 * (tap one to change it, "+" to add), and they write into the one shared draft. */
describe("App — the enemy team on the god page", () => {
  it("has no floating draft dock and no second strip; the field carries the team", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    expect(screen.queryByTestId("draft-dock")).not.toBeInTheDocument();
    expect(screen.queryByTestId("enemy-strip")).not.toBeInTheDocument();
    await waitFor(() => expect(screen.getByRole("button", { name: "Add enemy 1" })).toBeInTheDocument());
  });

  it("writes picks from the god page into the shared draft and the link, with you in slot one", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    fireEvent.click(await screen.findByRole("button", { name: "Add enemy 1" }));
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
    await waitFor(() => expect(window.location.hash).toContain("vs=Ymir"));
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

  it("switches god from the roster grid", async () => {
    render(<App />);
    const grid = within(await screen.findByTestId("god-grid"));
    expect(grid.getByRole("link", { name: /Chiron/ })).toHaveAttribute("href", toHash.god("Chiron"));
  });
});

/* Three surfaces render the brand: the landing page, the loading skeleton and
 * the data-load failure screen. The failure screen still carried an "S2" square
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

  it("names the wordmark once, not twice", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /type your matchup/i });
    // On a phone the wordmark heads the landing page; its `role="img"` name
    // must announce "ichor" once.
    expect(screen.getAllByRole("img", { name: "ichor" })).toHaveLength(1);
    expect(screen.queryByRole("link", { name: /ichor ichor/i })).not.toBeInTheDocument();
  });
});

describe("App — chrome", () => {
  it("offers one field for gods — the command field — and no second search box", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /type your matchup/i });
    expect(screen.getAllByRole("combobox")).toHaveLength(1);
    expect(screen.queryByRole("searchbox")).not.toBeInTheDocument();
  });

  /* Refetching a static index.json does nothing a visitor can see, so the
   * button read as broken: no result, no feedback. It is a pipeline tool. */
  it("keeps the data-reload control out of the deployed menu", async () => {
    vi.stubEnv("DEV", false);
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /type your matchup/i });
    const menu = await openMenu();
    expect(menu.queryByRole("button", { name: /reload/i })).not.toBeInTheDocument();
    // The dev-only god editor goes with it.
    expect(menu.queryByRole("button", { name: /add god/i })).not.toBeInTheDocument();
    // What survives is the control a visitor actually needs.
    expect(menu.getByRole("button", { name: /help and credits/i })).toBeInTheDocument();
    vi.unstubAllEnvs();
  });

  it("reports what it did when the dev reload runs", async () => {
    vi.stubEnv("DEV", true);
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /type your matchup/i });
    const menu = await openMenu();
    const btn = menu.getByRole("button", { name: /reload/i });
    fireEvent.click(btn);
    // A control that runs silently is indistinguishable from a broken one.
    await waitFor(() => expect(btn).toHaveTextContent(/reloaded/i));
    vi.unstubAllEnvs();
  });

  it("redirects a retired #/gods URL to the roster board", async () => {
    atUrl("#/gods");
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /type your matchup/i });
    expect(window.location.hash).toBe("#/");
  });

  it("shows the data-freshness stamp as relative text with the absolute date on hover", async () => {
    render(<App />);
    const freshness = await screen.findByTestId("freshness");
    expect(freshness.textContent).toMatch(/^Updated /i);
    expect(freshness).toHaveAttribute("title", "2026-07-19");
  });

  it("omits the freshness stamp entirely when data_updated is missing", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({
      ok: true, json: () => Promise.resolve({ ...data, data_updated: undefined }),
    }));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /type your matchup/i });
    expect(screen.queryByTestId("freshness")).not.toBeInTheDocument();
  });

  it("appends the current patch label to the freshness stamp when data_patch is present", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({
      ok: true, json: () => Promise.resolve({ ...data, data_patch: "Open Beta 39" }),
    }));
    const freshness = await (render(<App />), screen.findByTestId("freshness"));
    expect(freshness.textContent).toMatch(/^Updated .+ · Open Beta 39$/);
  });

  it("omits the patch clause from the stamp cleanly when data_patch is absent", async () => {
    render(<App />);
    const freshness = await screen.findByTestId("freshness");
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
    await screen.findByTestId("freshness");
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });

  it("opens the legend on demand, carrying the attribution the footer used to hold", async () => {
    render(<App />);
    await screen.findByTestId("freshness");
    const menu = await openMenu();
    fireEvent.click(menu.getByRole("button", { name: /help and credits/i }));
    const dialog = await screen.findByRole("dialog", { name: /how this works/i });
    expect(within(dialog).getByText(/not affiliated with Hi-Rez/i)).toBeInTheDocument();
  });

  // 43px of every screen, forever, for something you read once.
  it("has no permanent footer", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /type your matchup/i });
    expect(screen.queryByRole("contentinfo")).not.toBeInTheDocument();
  });
});
