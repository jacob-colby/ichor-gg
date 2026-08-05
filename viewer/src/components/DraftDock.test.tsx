import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, within, cleanup } from "@testing-library/react";
import { DraftDock } from "./DraftDock";
import type { DraftConfig, God, Item } from "../types";

const god = (name: string, overrides: Partial<God> = {}): God =>
  ({
    type: "god", name, pantheon: "Test", role: "Carry", specializations: [],
    damage_type: "physical", release_date: "", base_stats: {}, abilities: [], aspects: [],
    source_url: "", last_verified: "", ...overrides,
  }) as God;

const testGod = god("TestGod");
const healerGod = god("EnemyHealer", { role: "Support", specializations: ["Healing"], damage_type: "magical" });
const buddyGod = god("Buddy");
const GODS = [testGod, healerGod, buddyGod];

const item = (name: string, tags: string[] = []): Item =>
  ({
    name, tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [],
    effect_tags: tags, efficiency_tier: null,
  }) as unknown as Item;

const ITEMS = [
  item("Alpha"), item("Beta"), item("Gamma"), item("Delta"), item("Epsilon"), item("Zeta"),
  item("AntiHeal", ["anti-heal"]),
];

const SCORES: Record<string, number> = {
  Alpha: 0.6, Beta: 0.59, Gamma: 0.58, Delta: 0.57, Epsilon: 0.56, Zeta: 0.55, AntiHeal: 0.4,
};
const GOD_ITEM_SCORES: Record<string, Record<string, number>> = {
  TestGod: SCORES, EnemyHealer: { Alpha: 0.5 }, Buddy: { Alpha: 0.3 },
};

const DRAFT_CFG: DraftConfig = {
  max_bonus: 0.5, per_share: 0.5,
  tag_bonus: { healers: { "anti-heal": 1 } }, stat_bonus: {},
  ally_covered: -0.5, ally_gap: 0.5,
};

const dock = () => (
  <DraftDock gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />
);

beforeEach(() => {
  localStorage.clear();
  window.location.hash = "";
});

/* The dock is the one place the draft is visible from every route except
 * /draft itself. Its whole reason to exist is stated as a claim other tests
 * exercise elsewhere (App — "no second, redundant copy on /draft" per the
 * mount guard in App.tsx); this file only tests the component in isolation. */
describe("DraftDock — nothing entered yet", () => {
  /* This used to be a link showing a *mock* of the board, which was a picture
   * of a control sitting beside the real control it was a picture of. The
   * board is small enough to just be here. */
  it("is the working board, not an advertisement for one", () => {
    render(dock());
    expect(screen.getByTestId("draft-dock")).toHaveTextContent(/start a draft/i);
    fireEvent.click(screen.getByRole("button", { name: /start a draft/i }));
    // Real slots, editable in place — no navigation to /draft required.
    expect(screen.getByRole("button", { name: "Add you" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Add enemy 1" })).toBeInTheDocument();
  });

  it("drafts a whole comp without ever leaving the page", () => {
    render(dock());
    fireEvent.click(screen.getByRole("button", { name: /start a draft/i }));
    fireEvent.click(screen.getByRole("button", { name: "Add you" }));
    fireEvent.click(screen.getByText("TestGod"));
    fireEvent.click(screen.getByRole("button", { name: "Add enemy 1" }));
    fireEvent.click(screen.getByText("EnemyHealer"));
    // The build answers the picks, in place.
    expect(screen.getByTestId("draft-dock")).toHaveTextContent(/\d+ of \d+ items moved/i);
    expect(window.location.hash).toBe("");
  });
});

describe("DraftDock — collapsed", () => {
  it("shows the same claim /draft would make, once a god is entered", () => {
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["TestGod", "", "", "", ""], enemies: ["EnemyHealer", "", "", "", ""],
    }));
    render(dock());
    // TestGod's default core includes no anti-heal item until a healer is
    // scouted; with one entered, AntiHeal should out-rank something in the
    // default core — the same computation DraftPage itself makes.
    expect(screen.getByTestId("draft-dock")).toHaveTextContent(/\d+ of \d+ items moved/i);
  });

  it("says so when your own slot is still empty", () => {
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["", "", "", "", ""], enemies: ["EnemyHealer", "", "", "", ""],
    }));
    render(dock());
    expect(screen.getByTestId("draft-dock")).toHaveTextContent(/add your god/i);
  });

  it("starts collapsed — no slots, no mode toggle visible", () => {
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["TestGod", "", "", "", ""], enemies: ["", "", "", "", ""],
    }));
    render(dock());
    expect(screen.queryByRole("group", { name: /game mode/i })).not.toBeInTheDocument();
  });
});

describe("DraftDock — expand and edit in place", () => {
  beforeEach(() => {
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["TestGod", "", "", "", ""], enemies: ["", "", "", "", ""],
    }));
  });

  it("expands to reveal every slot, editable", () => {
    render(dock());
    fireEvent.click(screen.getByRole("button", { name: /moved|default core|nothing moved/i }));
    expect(screen.getByRole("button", { name: "Change you (TestGod)" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Add ally 2" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Add enemy 1" })).toBeInTheDocument();
  });

  it("fills a slot from the dock without navigating away", () => {
    render(dock());
    fireEvent.click(screen.getByRole("button", { name: /default core/i }));
    fireEvent.click(screen.getByRole("button", { name: "Add enemy 1" }));
    fireEvent.click(screen.getByText("EnemyHealer"));
    // The picker closes and the slot reflects the pick, live.
    expect(screen.getByRole("button", { name: "Change enemy 1 (EnemyHealer)" })).toBeInTheDocument();
  });

  it("switches mode, resizing the slots shown", () => {
    render(dock());
    fireEvent.click(screen.getByRole("button", { name: /default core/i }));
    const modeGroup = within(screen.getByRole("group", { name: /game mode/i }));
    fireEvent.click(modeGroup.getByRole("button", { name: "Joust" }));
    expect(screen.getByRole("button", { name: "Add ally 3" })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Add ally 4" })).not.toBeInTheDocument();
  });

  it("clears the board from the dock", () => {
    render(dock());
    fireEvent.click(screen.getByRole("button", { name: /default core/i }));
    fireEvent.click(screen.getByRole("button", { name: /clear board/i }));
    expect(screen.getByTestId("draft-dock")).toHaveTextContent(/start a draft/i);
  });

  it("collapses on Escape and returns focus to the toggle", () => {
    render(dock());
    const toggle = screen.getByRole("button", { name: /default core/i });
    fireEvent.click(toggle);
    expect(screen.getByRole("group", { name: /game mode/i })).toBeInTheDocument();
    fireEvent.keyDown(window, { key: "Escape" });
    expect(screen.queryByRole("group", { name: /game mode/i })).not.toBeInTheDocument();
    expect(document.activeElement).toBe(toggle);
  });

  it("collapses from its own ✕ control", () => {
    render(dock());
    fireEvent.click(screen.getByRole("button", { name: /default core/i }));
    fireEvent.click(screen.getByRole("button", { name: /collapse/i }));
    expect(screen.queryByRole("group", { name: /game mode/i })).not.toBeInTheDocument();
  });
});

/* The fuller `ChangeRow` on /draft — a bar, a bonus figure, the reason it
 * fired — doesn't fit a panel this narrow. The dock carries the build itself
 * and enough to identify each swap, and points to /draft for the reasoning. */
describe("DraftDock — the build, in place", () => {
  const seed = (enemies: string[]) => localStorage.setItem("smite:draft", JSON.stringify({
    mode: "conquest", allies: ["TestGod", "", "", "", ""], enemies,
  }));

  it("shows the whole core, so its own claim is checkable here", () => {
    seed(["", "", "", "", ""]);
    render(dock());
    fireEvent.click(screen.getByRole("button", { name: /default core/i }));
    const core = screen.getByText("The default core").parentElement!;
    // Six named items, not a count of them.
    expect(within(core).getAllByRole("link")).toHaveLength(6);
    expect(within(core).getByRole("link", { name: /^Alpha/ })).toHaveAttribute("href", "#/items/Alpha");
  });

  it("marks the items the draft brought in", () => {
    seed(["EnemyHealer", "", "", "", ""]);
    render(dock());
    fireEvent.click(screen.getByRole("button", { name: /items moved/i }));
    const core = screen.getByText("Your adapted core").parentElement!;
    expect(within(core).getByRole("link", { name: /AntiHeal, added by your draft/i })).toBeInTheDocument();
    expect(within(core).queryByRole("link", { name: /^Zeta/ })).not.toBeInTheDocument();
  });

  it("names the displaced item without the full reasoning", () => {
    seed(["EnemyHealer", "", "", "", ""]);
    render(dock());
    fireEvent.click(screen.getByRole("button", { name: /items moved/i }));
    expect(screen.getByText(/for Zeta/i)).toBeInTheDocument();
    // No bonus figure, no "answers" reason line — those stay on the full page.
    expect(screen.queryByText(/^\+0\.\d\d$/)).not.toBeInTheDocument();
  });

  it("links to the full board for the complete ledger", () => {
    seed(["", "", "", "", ""]);
    render(dock());
    fireEvent.click(screen.getByRole("button", { name: /default core/i }));
    expect(screen.getByRole("link", { name: /full board/i })).toHaveAttribute("href", "#/draft");
  });
});

/* The dock floats over every route on a near-black page. Measured before this:
 * its surface sat at 1.02:1 against the page and it had NO drop shadow at all,
 * because `.plane` and `shadow-raised` both set `box-shadow` and the plane won.
 * These pin the separation so a later tidy-up can't silently flatten it. */
describe("DraftDock — it has to be visible", () => {
  const panel = () => screen.getByTestId("draft-dock").querySelector('[role="region"]')!;

  it("uses the composed dock elevation, not the shadow pair that cancelled", () => {
    render(dock());
    expect(panel().className).toContain("dock");
    // `.plane` would overwrite the drop shadow again.
    expect(panel().className).not.toContain("plane");
  });

  it("sits on the elevated surface tier, not one step off the page", () => {
    render(dock());
    expect(panel().className).toContain("bg-bg3");
    expect(panel().className).not.toContain("bg-bg1");
  });

  it("wears the gold ring only while a draft is live", () => {
    render(dock());
    expect(panel().className).not.toContain("is-live");
    cleanup();

    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["Agni", "", "", "", ""], enemies: ["", "", "", "", ""],
    }));
    render(dock());
    expect(panel().className).toContain("is-live");
  });

  it("marks one you-slot, on the ally row, even while empty", () => {
    // Keyed on index alone the gold landed on the enemy row's first slot too,
    // which said the enemy team had a you-slot.
    render(dock());
    const gold = screen.getByTestId("draft-dock").querySelectorAll("button > span > .border-gold, button > span > .ring-gold");
    expect(gold).toHaveLength(1);
  });
});
