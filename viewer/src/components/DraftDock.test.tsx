import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
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
  it("shows a quiet invitation instead of ten empty rings", () => {
    render(dock());
    const invite = screen.getByTestId("draft-dock");
    expect(invite).toHaveTextContent(/start a draft/i);
    expect(invite.tagName).toBe("A");
    expect(invite).toHaveAttribute("href", "#/draft");
    // No chip cluster, no chevron — this is the minimal state, not the full
    // dock with everything blank.
    expect(screen.queryByRole("button", { name: /collapse/i })).not.toBeInTheDocument();
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
 * fired — doesn't fit a panel this narrow. The dock shows only enough to
 * identify the swap and points to /draft for the rest. */
describe("DraftDock — what changed, condensed", () => {
  it("names a displaced item without the full reasoning", () => {
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["TestGod", "", "", "", ""], enemies: ["EnemyHealer", "", "", "", ""],
    }));
    render(dock());
    fireEvent.click(screen.getByRole("button", { name: /items moved/i }));
    expect(screen.getByText("AntiHeal")).toBeInTheDocument();
    expect(screen.getByText(/for Zeta/i)).toBeInTheDocument();
    // No bonus figure, no "answers" reason line — those stay on the full page.
    expect(screen.queryByText(/^\+0\.\d\d$/)).not.toBeInTheDocument();
  });

  it("links to the full board for the complete ledger", () => {
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["TestGod", "", "", "", ""], enemies: ["", "", "", "", ""],
    }));
    render(dock());
    fireEvent.click(screen.getByRole("button", { name: /default core/i }));
    expect(screen.getByRole("link", { name: /open full draft board/i })).toHaveAttribute("href", "#/draft");
  });
});
