import { describe, it, expect, beforeEach, vi } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { DraftBoard } from "./DraftBoard";
import type { BuildNote, DraftConfig, God, Item } from "../../types";

const god = (name: string, over: Partial<God> = {}): God => ({
  type: "god", name, pantheon: "Test", role: "Carry", specializations: [], damage_type: "physical", release_date: "",
  base_stats: {}, abilities: [], aspects: [], source_url: "", last_verified: "", ...over,
}) as God;
const GODS = [god("TestGod"), god("EnemyHealer", { role: "Support", specializations: ["Healing"], damage_type: "magical" }), god("Buddy")];
const item = (name: string, tags: string[] = []): Item => ({
  name, tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [], effect_tags: tags, efficiency_tier: null,
}) as unknown as Item;
const ITEMS = [...["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"].map((n) => item(n)), item("AntiHeal", ["anti-heal"])];
const SCORES = { Alpha: 0.6, Beta: 0.59, Gamma: 0.58, Delta: 0.57, Epsilon: 0.56, Zeta: 0.55, AntiHeal: 0.4 };
const perMode = <T,>(t: T) => ({ conquest: t, joust: t, arena: t });
const GOD_ITEM_SCORES = { TestGod: perMode(SCORES), EnemyHealer: perMode({ Alpha: 0.5 }), Buddy: perMode({ Alpha: 0.3 }) };
const CORE6 = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"];
const BUILDS = ["Conquest", "Joust", "Arena"].map((m) => ({
  type: "smite-build", god: "TestGod", mode: m,
  builds: [{ source: "suggested", archetype: "model", slot_order: CORE6, flex_slots: [] }],
})) as unknown as BuildNote[];
const CFG: DraftConfig = {
  max_bonus: 0.5, per_share: 4, tag_bonus: { healers: { "anti-heal": 1 } }, stat_bonus: {}, ally_covered: -0.5, ally_gap: 0.5,
};

const atUrl = (hash: string) => window.history.replaceState(null, "", `/${hash}`);
const board = () => (
  <DraftBoard gods={GODS} items={ITEMS} builds={BUILDS} godItemScores={GOD_ITEM_SCORES} draftConfig={CFG} />
);

beforeEach(() => { localStorage.clear(); atUrl("#/draft"); });

describe("DraftBoard — the board", () => {
  it("opens with the build's own starter, the one the god page shows, not the community's favourite", () => {
    const withStarter = ["Conquest", "Joust", "Arena"].map((m) => ({
      type: "smite-build", god: "TestGod", mode: m,
      builds: [
        { source: "suggested", archetype: "model", slot_order: CORE6, flex_slots: [], starter: { base: "Seed", upgrade: "Tree" } },
        { source: "community", slot_order: [], community_starters: [{ name: "Pebble", pick_rate: 0.6, win_rate: 0.5 }] },
      ],
    })) as unknown as BuildNote[];
    localStorage.setItem("smite:draft", JSON.stringify({ mode: "conquest", allies: ["TestGod", "", "", "", ""], enemies: ["", "", "", "", ""] }));
    render(<DraftBoard gods={GODS} items={[...ITEMS, item("Seed"), item("Tree"), item("Pebble")]} builds={withStarter}
      godItemScores={GOD_ITEM_SCORES} draftConfig={CFG} />);
    const row = screen.getByTestId("draft-starter");
    expect(row).toHaveTextContent("Seed → Tree");
    expect(row).not.toHaveTextContent("Pebble");
  });

  it("names itself and teaches the empty board, with you in the violet slot", () => {
    render(board());
    expect(screen.getByRole("heading", { level: 1, name: "Draft" })).toBeInTheDocument();
    expect(screen.getByTestId("draft-claim")).toHaveTextContent(/Build for the match you.re actually in/);
    expect(screen.getByRole("button", { name: "Add your god" })).toBeInTheDocument();
    expect(screen.queryByTestId("six")).not.toBeInTheDocument();
  });

  it("puts five enemy slots in one row and four allies beside you", () => {
    render(board());
    expect(within(screen.getByTestId("team-enemy")).getAllByRole("button")).toHaveLength(5);
    expect(within(screen.getByTestId("team-ally")).getAllByRole("button")).toHaveLength(5);
    expect(screen.getByRole("button", { name: "Add enemy 5" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Add ally 2" })).toBeInTheDocument();
  });

  it("fills you from the picker sheet, then shows the god page's six", () => {
    render(board());
    fireEvent.click(screen.getByRole("button", { name: "Add your god" }));
    const sheet = within(screen.getByRole("dialog", { name: "Your god" }));
    fireEvent.click(sheet.getByRole("button", { name: "TestGod" }));
    expect(within(screen.getByTestId("six")).getAllByTestId("item-name").map((n) => n.textContent?.replace(/^\d+\. /, "")))
      .toEqual(CORE6);
    expect(screen.getByTestId("draft-claim")).toHaveTextContent(/Add an enemy/);
  });

  it("says each swap in words: what came in, what it replaced, which threat it answers", () => {
    atUrl("#/draft?m=conquest&me=TestGod&e=EnemyHealer");
    render(board());
    expect(screen.getByTestId("draft-claim")).toHaveTextContent("This team moved 1 of 6 items in TestGod’s six.");
    const line = within(screen.getByTestId("draft-changes")).getByRole("listitem");
    expect(line).toHaveAccessibleName(/^AntiHeal replaces \w+ · answers healing$/);
    // The six carries it too, ringed, with its reason on the row.
    const swapped = within(screen.getByTestId("six")).getAllByTestId("item-row").find((r) => r.dataset.swapped);
    expect(swapped).toHaveTextContent(/Swapped in for/);
  });

  it("counts what is known and says the rest will keep moving the six", () => {
    atUrl("#/draft?m=conquest&me=TestGod&e=EnemyHealer");
    render(board());
    expect(screen.getByTestId("enemies-known")).toHaveTextContent("1 of 5 enemies known");
    expect(screen.getByTestId("unknown-line")).toHaveTextContent("4 still unknown, so this six will keep moving.");
  });

  it("denominates threats by the roster and prints measured zeros once anything is scouted", () => {
    atUrl("#/draft?m=conquest&me=TestGod&e=EnemyHealer");
    render(board());
    const heal = screen.getByTestId("threat-healers");
    expect(heal).toHaveTextContent(/^1 of 5Healing — EnemyHealer/);
    expect(heal).toHaveTextContent("Answered by AntiHeal");
    expect(screen.getByTestId("threat-crit")).toHaveTextContent(/^0 of 5Crit/);
  });

  it("prints no measured zeros before anything is scouted", () => {
    atUrl("#/draft?m=conquest&me=TestGod");
    render(board());
    const threats = within(screen.getByTestId("draft-threats"));
    expect(threats.queryByTestId("threat-crit")).not.toBeInTheDocument();
    expect(threats.getByText(/Nothing scouted yet/)).toBeInTheDocument();
  });

  it("says Joust rests on the model alone and shrinks the rows to three", () => {
    atUrl("#/draft?m=joust&me=TestGod");
    render(board());
    expect(screen.getByTestId("model-only")).toHaveTextContent("No win data in Joust — model only.");
    expect(within(screen.getByTestId("team-enemy")).getAllByRole("button")).toHaveLength(3);
  });

  it("copies a link that reproduces the board", async () => {
    const writeText = vi.fn().mockResolvedValue(undefined);
    Object.assign(navigator, { clipboard: { writeText } });
    atUrl("#/draft?m=conquest&me=TestGod&e=EnemyHealer");
    render(board());
    fireEvent.click(screen.getByRole("button", { name: "Copy link" }));
    expect(writeText).toHaveBeenCalledWith(expect.stringContaining("#/draft?m=conquest&me=TestGod&e=EnemyHealer"));
    expect(await screen.findByText("Link copied")).toBeInTheDocument();
  });

  it("hands off to your god's page against this team, and to the working", () => {
    atUrl("#/draft?m=conquest&me=TestGod&e=EnemyHealer");
    render(board());
    expect(screen.getByRole("link", { name: /TestGod.s page, against this team/ })).toHaveAttribute("href", "#/god/TestGod?vs=EnemyHealer");
    expect(screen.getByTestId("method-seam")).toHaveAttribute("href", "#/method");
  });

  it("says which names a shared link could not place", () => {
    atUrl("#/draft?m=conquest&me=TestGod&e=Nobody");
    render(board());
    expect(screen.getByRole("status")).toHaveTextContent("Nobody has no scored build here");
  });
});
