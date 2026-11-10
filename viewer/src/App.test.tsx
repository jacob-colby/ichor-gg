import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
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

/* The Second Screen shell (direction A). The app opens on god select; one
 * navigation pattern carries every route — a top bar ("Main") from lg up and
 * a bottom tab bar ("Tabs") on a phone. jsdom renders both, so each test
 * names the one it means. These replace the Subject Frame assertions (lens
 * strip, subject header, picker dialog, draft dock), whose chrome this
 * direction removes on purpose. */
describe("App — Second Screen chrome", () => {
  it("opens on god select", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /who are you playing/i });
    const main = within(screen.getByRole("navigation", { name: "Main" }));
    expect(main.getByRole("link", { name: "Gods" })).toHaveAttribute("aria-current", "page");
    const tabs = within(screen.getByRole("navigation", { name: "Tabs" }));
    expect(tabs.getByRole("link", { name: "Gods" })).toHaveAttribute("aria-current", "page");
    expect(tabs.getByRole("button", { name: "More" })).toBeInTheDocument();
  });

  it("moves between destinations from the top bar", async () => {
    render(<App />);
    const main = within(await screen.findByRole("navigation", { name: "Main" }));
    fireEvent.click(main.getByRole("link", { name: "Items" }));
    // The redesigned Items page names itself in its h1 (a caption, never a
    // sentence) and carries the claim in the line under it.
    await waitFor(() => expect(screen.getByRole("heading", { level: 1, name: "Items" })).toBeInTheDocument());
    expect(screen.getByTestId("items-claim")).toHaveTextContent(/are underpriced/i);
  });

  it("keeps the reading routes and the fan-project line under More on a phone", async () => {
    render(<App />);
    const tabs = within(await screen.findByRole("navigation", { name: "Tabs" }));
    fireEvent.click(tabs.getByRole("button", { name: "More" }));
    const sheet = within(await screen.findByRole("dialog", { name: "More" }));
    for (const name of [/Tiers/, /Items/, /Patch notes/, /Method/]) {
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
    expect(main.getByRole("link", { name: "Draft" })).toHaveAttribute("aria-current", "page");
  });

  it("has one Gods tab, current on a god page and on the roster alike — no separate Build tab", async () => {
    atUrl(toHash.god("Chiron"));
    const { unmount } = render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    const tabs = within(screen.getByRole("navigation", { name: "Tabs" }));
    expect(tabs.queryByRole("link", { name: /Build/ })).not.toBeInTheDocument();
    expect(tabs.getAllByRole("link").map((a) => a.textContent)).toEqual(["Gods", "Draft"]);
    const gods = tabs.getByRole("link", { name: "Gods" });
    expect(gods).toHaveAttribute("aria-current", "page");
    expect(gods).toHaveAttribute("href", toHash.home());
    // The desktop bar names the god being read beside the one tab.
    expect(within(screen.getByRole("navigation", { name: "Main" })).getByRole("link", { name: /Gods · Chiron/ }))
      .toHaveAttribute("aria-current", "page");
    unmount();

    atUrl(toHash.home());
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /Who are you playing/i });
    const onRoster = within(screen.getByRole("navigation", { name: "Tabs" })).getByRole("link", { name: "Gods" });
    expect(onRoster).toHaveAttribute("aria-current", "page");
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
    expect(main.getByRole("link", { name: /^Gods/ })).toHaveAttribute("aria-current", "page");
  });
});

/* The floating dock is gone from this shell: the god page carries the enemy
 * team itself, and Draft is one tab away everywhere else. These replace the
 * dock tests and keep their point — the comp you enter is ONE shared draft. */
describe("App — the enemy team on the god page", () => {
  it("has no floating draft dock; the god page carries an enemy strip", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    expect(screen.queryByTestId("draft-dock")).not.toBeInTheDocument();
    expect(screen.getByTestId("enemy-strip")).toBeInTheDocument();
  });

  it("writes picks from the god page into the shared draft, with you in slot one", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
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

  it("switches god from the roster grid", async () => {
    render(<App />);
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
    await screen.findByRole("heading", { level: 1, name: /who are you playing/i });
    // The link carries its own label; the wordmark's `role="img"` name must
    // not leak into it and announce "ichor" a second time.
    const home = screen.getByRole("link", { name: "ichor — home" });
    expect(home).toBeInTheDocument();
    expect(screen.queryByRole("link", { name: /ichor ichor/i })).not.toBeInTheDocument();
  });
});

describe("App — chrome", () => {
  /* A + typed query: the search box became the command field (a combobox,
   * not a bare searchbox) — still exactly one field on the screen. */
  it("offers one search field on god select, for gods", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /who are you playing/i });
    expect(screen.queryAllByRole("searchbox")).toHaveLength(0);
    expect(screen.getAllByRole("combobox")).toHaveLength(1);
    expect(screen.getByPlaceholderText(/search 2 gods/i)).toBeInTheDocument();
  });

  /* Refetching a static index.json does nothing a visitor can see, so the
   * button read as broken: no result, no feedback. It is a pipeline tool. */
  it("keeps the data-reload control out of the deployed header", async () => {
    vi.stubEnv("DEV", false);
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /who are you playing/i });
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
    await screen.findByRole("heading", { level: 1, name: /who are you playing/i });
    const btn = screen.getByRole("button", { name: /reload/i });
    fireEvent.click(btn);
    // A control that runs silently is indistinguishable from a broken one.
    await waitFor(() => expect(btn).toHaveTextContent(/reloaded/i));
    vi.unstubAllEnvs();
  });

  it("redirects a retired #/gods URL to the roster board", async () => {
    atUrl("#/gods");
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /who are you playing/i });
    expect(window.location.hash).toBe("#/");
  });

  // Exact text against a pinned clock is in AppNav.test; this is the wiring.
  it("shows the data-freshness stamp compactly, with the sentence and the absolute date on hover", async () => {
    render(<App />);
    const freshness = await screen.findByTestId("header-freshness");
    const [shown, spoken] = Array.from(freshness.children);
    expect(shown.textContent).toMatch(/^Updated (today|\d+(d|w|mo))$/);
    expect(spoken.textContent).toMatch(/^Updated /);
    expect(freshness.getAttribute("title")).toMatch(/^Updated .+ \(2026-07-19\)$/);
  });

  it("omits the freshness stamp entirely when data_updated is missing", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({
      ok: true, json: () => Promise.resolve({ ...data, data_updated: undefined }),
    }));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /who are you playing/i });
    expect(screen.queryByTestId("header-freshness")).not.toBeInTheDocument();
  });

  it("appends the current patch label to the header freshness stamp when data_patch is present", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({
      ok: true, json: () => Promise.resolve({ ...data, data_patch: "Open Beta 39" }),
    }));
    const freshness = await (render(<App />), screen.findByTestId("header-freshness"));
    const [shown, spoken] = Array.from(freshness.children);
    expect(shown.textContent).toMatch(/^OB39 · (today|\d+(d|w|mo))$/);
    expect(spoken.textContent).toMatch(/^Updated .+ · Open Beta 39$/);
    expect(freshness.getAttribute("title")).toMatch(/ · Open Beta 39$/);
  });

  it("omits the patch clause from the header stamp cleanly when data_patch is absent", async () => {
    render(<App />);
    const freshness = await screen.findByTestId("header-freshness");
    expect(freshness.textContent).not.toContain("·");
    expect(freshness.getAttribute("title")).not.toContain("·");
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
    // The bar shows only "OB47 · 1d"; the sentence must not be hover-only.
    expect(within(dialog).getByTestId("legend-freshness").textContent).toMatch(/^Updated .+ \(2026-07-19\)\. $/);
  });

  // 43px of every screen, forever, for something you read once.
  it("has no permanent footer", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /who are you playing/i });
    expect(screen.queryByRole("contentinfo")).not.toBeInTheDocument();
  });
});

/* ── A + typed query ──────────────────────────────────────────────────────
 * Direction C's command field inside direction A's chrome. From lg up it is
 * the top bar's global search; on a phone it is god select's search box. */
const desktop = () => {
  Object.defineProperty(window, "matchMedia", {
    configurable: true, writable: true,
    value: (q: string) => ({
      matches: q.includes("min-width: 1024px"), media: q,
      addEventListener() {}, removeEventListener() {}, addListener() {}, removeListener() {},
    }),
  });
};
const draftStored = () => JSON.parse(localStorage.getItem("smite:draft") ?? "{}");

describe("App — the command field on desktop", () => {
  beforeEach(desktop);
  afterEach(() => { delete (window as { matchMedia?: unknown }).matchMedia; });

  const barField = () => screen.findByRole("combobox", { name: "Search a god, a matchup or an item" });

  it("sits in the top bar's search landmark, and god select has no second field", async () => {
    render(<App />);
    const field = await barField();
    expect(within(screen.getByRole("navigation", { name: "Main" })).getByRole("search")).toContainElement(field);
    expect(screen.getAllByRole("combobox")).toHaveLength(1);
  });

  it("runs a typed matchup: URL carries the enemies and mode, the shared draft holds them", async () => {
    atUrl(toHash.god("Ymir"));
    render(<App />);
    const field = await barField();
    fireEvent.change(field, { target: { value: "chiron vs ymir joust" } });
    expect(document.querySelectorAll("[data-chip='you'], [data-chip='enemy']")).toHaveLength(2);
    fireEvent.keyDown(field, { key: "Enter" });
    await waitFor(() => expect(window.location.hash).toBe("#/god/Chiron?mode=joust&vs=Ymir"));
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    await waitFor(() => expect(draftStored()).toMatchObject({ mode: "joust" }));
    await waitFor(() => expect(draftStored().enemies?.[0]).toBe("Ymir"));
    expect(draftStored().allies?.[0]).toBe("Chiron");
    // The strip shows the team the URL names, and the field is a search again.
    expect(await screen.findByRole("button", { name: "Enemy 1: Ymir. Change" })).toBeInTheDocument();
    expect(await barField()).toHaveValue("");
    expect(document.querySelector("[data-chip]")).toBeNull();
  });

  it("opens a single god's page on Enter and leaves the stored draft alone", async () => {
    localStorage.setItem("smite:draft", JSON.stringify({ mode: "conquest", allies: ["", "", "", "", ""], enemies: ["Ymir", "", "", "", ""] }));
    render(<App />);
    const field = await barField();
    fireEvent.change(field, { target: { value: "chi" } });
    fireEvent.keyDown(field, { key: "Enter" });
    await waitFor(() => expect(window.location.hash).toBe("#/god/Chiron"));
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    expect(draftStored().enemies?.[0]).toBe("Ymir");
  });

  it("offers the same recent gods when the field is empty, each opening that god's build", async () => {
    localStorage.setItem("ichor:recent-gods", JSON.stringify(["Ymir"]));
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    const field = await barField();
    fireEvent.focus(field);
    const offers = await screen.findAllByRole("option");
    expect(offers.map((o) => o.textContent)).toEqual(["ChironCarryRecent", "YmirSoloRecent"]);
    fireEvent.click(offers[1]);
    await waitFor(() => expect(window.location.hash).toBe("#/god/Ymir"));
  });

  it("filters god select from the top bar's field", async () => {
    render(<App />);
    const field = await barField();
    fireEvent.change(field, { target: { value: "ymi" } });
    await waitFor(() => expect(within(screen.getByTestId("god-grid")).getAllByRole("link").map((a) => a.getAttribute("href")))
      .toEqual(["#/god/Ymir"]));
  });

  it("opens an item in the Items shop when the text names an item and no god", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    const field = await barField();
    fireEvent.change(field, { target: { value: "rag" } });
    expect(await screen.findByRole("option", { name: /Rage/ })).toBeInTheDocument();
    fireEvent.keyDown(field, { key: "Enter" });
    await waitFor(() => expect(window.location.hash).toBe("#/items/Rage"));
  });

  /* The open field covers the whole middle of the bar — search, reading links
   * and stamp — and everything else in it steps aside. A fixed 640px open
   * width (until 2026-11-07) ended part-way across the links: Patch notes'
   * tail and Method showed beside Go at 1280–1920px, and at 1024px on a long
   * god name it ran onto Help. jsdom has no layout and can't evaluate the
   * `:has` rule in index.css, so this pins the contract the geometry rests on
   * (the geometry itself was measured in a browser, numbers in the PR):
   * the field opens to `100cqw` of the middle, which is the size container,
   * and every other control in the middle carries `under-field`. */
  it("opens over the whole middle of the bar, and everything else in it steps aside", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    const field = await barField();
    const nav = screen.getByRole("navigation", { name: "Main" });
    const middle = within(nav).getByTestId("nav-middle");
    const root = within(nav).getByTestId("command-bar");
    expect(middle).toHaveClass("@container/bar");
    expect(middle).toContainElement(root);
    expect(root).toHaveClass("w-full");
    expect(root).not.toHaveAttribute("data-command-open");
    const others = Array.from(middle.querySelectorAll("a, button, [data-testid='header-freshness']"))
      .filter((e) => !root.contains(e));
    expect(others.length).toBeGreaterThanOrEqual(5); // four reading links and the stamp
    others.forEach((e) => expect(e).toHaveClass("under-field"));
    expect(middle).not.toContainElement(within(nav).getByRole("button", { name: "Help and credits" }));

    fireEvent.change(field, { target: { value: "chi" } });
    await waitFor(() => expect(root).toHaveAttribute("data-command-open"));
    expect(root).toHaveClass("w-[100cqw]");
    expect(root).not.toHaveClass("w-full");
  });

  it("focuses the field on / and on Ctrl+K or Cmd+K, but not while typing elsewhere", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    const field = await barField();
    expect(field).not.toHaveFocus();
    fireEvent.keyDown(document.body, { key: "/" });
    expect(field).toHaveFocus();
    field.blur();
    fireEvent.keyDown(document.body, { key: "k", ctrlKey: true });
    expect(field).toHaveFocus();
    field.blur();
    fireEvent.keyDown(document.body, { key: "k", metaKey: true });
    expect(field).toHaveFocus();
    field.blur();
    // A "/" typed into another text field stays there.
    const other = document.createElement("input");
    document.body.appendChild(other);
    other.focus();
    fireEvent.keyDown(other, { key: "/" });
    expect(other).toHaveFocus();
    other.remove();
  });
});

describe("App — the command field on a phone", () => {
  const pageField = () => screen.findByRole("combobox", { name: /^Search gods, or type your god vs/ });

  it("has no field in the chrome or on the god page — the enemy strip is the enemy UI", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    expect(screen.queryByRole("combobox")).not.toBeInTheDocument();
    expect(screen.getByTestId("enemy-strip")).toBeInTheDocument();
  });

  it("filters the grid on a plain name, exactly as the search box did", async () => {
    render(<App />);
    fireEvent.change(await pageField(), { target: { value: "ymi" } });
    expect(within(screen.getByTestId("god-grid")).getAllByRole("link").map((a) => a.getAttribute("href"))).toEqual(["#/god/Ymir"]);
    await waitFor(() => expect(window.location.hash).toContain("q=ymi"));
    // No suggestion list over the grid for the first word: the grid is the list.
    expect(screen.queryByRole("option")).not.toBeInTheDocument();
  });

  it("opens the grid's first god on Enter for a plain name", async () => {
    render(<App />);
    const field = await pageField();
    fireEvent.change(field, { target: { value: "ymi" } });
    fireEvent.keyDown(field, { key: "Enter" });
    await waitFor(() => expect(window.location.hash).toBe("#/god/Ymir"));
  });

  it("turns Enter into the adapted build once the query says vs", async () => {
    render(<App />);
    const field = await pageField();
    fireEvent.change(field, { target: { value: "chiron vs ym" } });
    expect(await screen.findByRole("option", { name: /Ymir/ })).toBeInTheDocument();
    fireEvent.keyDown(field, { key: "Enter" });
    await waitFor(() => expect(window.location.hash).toBe("#/god/Chiron?vs=Ymir"));
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    expect(await screen.findByRole("button", { name: "Enemy 1: Ymir. Change" })).toBeInTheDocument();
  });

  /* Recent gods, not matchups (Jacob, 2026-11-09). A returning visitor keeps
   * their row: it is seeded from the retired query and last-god stores. */
  it("shows the recent gods above the grid, the last god first, seeded from the old stores", async () => {
    localStorage.setItem("ichor:recent-queries", JSON.stringify(["Chiron vs Ymir Joust"]));
    localStorage.setItem("ichor:last-god", "Ymir");
    render(<App />);
    const recents = within(await screen.findByTestId("recents"));
    expect(recents.getAllByRole("link").map((a) => [a.textContent, a.getAttribute("href")]))
      .toEqual([["Ymir", "#/god/Ymir"], ["Chiron", "#/god/Chiron"]]);
    expect(screen.queryByRole("link", { name: /Back to/ })).not.toBeInTheDocument();
    fireEvent.change(await pageField(), { target: { value: "y" } });
    expect(screen.queryByTestId("recents")).not.toBeInTheDocument();
  });

  it("records a god whenever its page opens, by a link or a grid card", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    const tabs = within(screen.getByRole("navigation", { name: "Tabs" }));
    fireEvent.click(tabs.getByRole("link", { name: "Gods" }));
    const first = await screen.findByTestId("recents");
    expect(within(first).getAllByRole("link").map((a) => a.textContent)).toEqual(["Chiron"]);
    fireEvent.click(within(screen.getByTestId("god-grid")).getByRole("link", { name: /Ymir/ }));
    await screen.findByRole("heading", { level: 1, name: "Ymir" });
    fireEvent.click(tabs.getByRole("link", { name: "Gods" }));
    await waitFor(() => expect(within(screen.getByTestId("recents")).getAllByRole("link").map((a) => a.textContent))
      .toEqual(["Ymir", "Chiron"]));
    expect(JSON.parse(localStorage.getItem("ichor:recent-gods") ?? "null")).toEqual(["Ymir", "Chiron"]);
  });

  it("clears the row for good: the retired stores do not bring it back", async () => {
    localStorage.setItem("ichor:recent-queries", JSON.stringify(["Chiron vs Ymir"]));
    const { unmount } = render(<App />);
    await screen.findByTestId("recents");
    fireEvent.click(screen.getByRole("button", { name: "Clear" }));
    expect(screen.queryByTestId("recents")).not.toBeInTheDocument();
    unmount();
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: /who are you playing/i });
    expect(screen.queryByTestId("recents")).not.toBeInTheDocument();
  });
});

describe("App — enemies in the god page's URL", () => {
  it("applies a linked enemy team to the strip and the shared draft, dropping unknown names", async () => {
    atUrl(`${toHash.god("Chiron")}?vs=Ymir,Nobody`);
    render(<App />);
    expect(await screen.findByRole("button", { name: "Enemy 1: Ymir. Change" })).toBeInTheDocument();
    await waitFor(() => expect(draftStored().enemies?.[0]).toBe("Ymir"));
    expect(draftStored().allies?.[0]).toBe("Chiron");
    expect(draftStored().enemies?.[1]).toBe("");
  });

  it("writes picker edits back to the address bar", async () => {
    atUrl(toHash.god("Chiron"));
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Chiron" });
    fireEvent.click(screen.getByRole("button", { name: "Add enemy 1" }));
    const sheet = await screen.findByRole("dialog", { name: /Enemy 1 of 5/ });
    fireEvent.click(within(sheet).getByRole("button", { name: "Ymir" }));
    await waitFor(() => expect(window.location.hash).toContain("vs=Ymir"));
  });
});
