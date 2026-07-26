import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { DraftPage } from "./DraftPage";
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
// EnemyHealer/Buddy need their own god_item_scores entries too — the picker
// is limited to gods present in god_item_scores, same as production.
const GOD_ITEM_SCORES: Record<string, Record<string, number>> = {
  TestGod: SCORES, EnemyHealer: { Alpha: 0.5 }, Buddy: { Alpha: 0.3 },
};

// Exaggerated weights vs. production _weights.yaml — the point of this
// fixture is a deterministic, clearly visible promotion, not realism.
const DRAFT_CFG: DraftConfig = {
  max_bonus: 0.5,
  per_share: 0.5,
  tag_bonus: { healers: { "anti-heal": 1 } },
  stat_bonus: {},
  ally_covered: -0.5,
  ally_gap: 0.5,
};

beforeEach(() => {
  localStorage.clear();
  window.location.hash = "";
});

describe("DraftPage", () => {
  it("labels ally slot 1 as yours, visually distinct from the rest of the row", () => {
    render(<DraftPage gods={GODS} items={[]} builds={[]} />);
    expect(screen.getByText("You")).toBeInTheDocument();
    expect(screen.getByLabelText("Add you")).toBeInTheDocument();
  });

  it("shows a teaching empty state and renders no build while the you-slot is empty", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    expect(screen.getByText(/your standalone draft board/i)).toBeInTheDocument();
    expect(screen.queryByText("AntiHeal")).not.toBeInTheDocument();
    expect(screen.queryByText(/adapted core/i)).not.toBeInTheDocument();
  });

  it("renders the adapted core once the you-slot is filled", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    expect(screen.getByText(/adapted core/i)).toBeInTheDocument();
    expect(screen.getAllByText(/^(Alpha|Beta|Gamma|Delta|Epsilon|Zeta|AntiHeal)$/)).toHaveLength(6);
  });

  it("promotes a countering item once a threat is entered", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    fireEvent.click(screen.getByLabelText("Add enemy 1"));
    fireEvent.click(screen.getByText("EnemyHealer"));
    expect(screen.getByText("AntiHeal")).toBeInTheDocument();
  });

  it("shows threat chips expressed as a share of the entered enemies", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add enemy 1"));
    fireEvent.click(screen.getByText("EnemyHealer"));
    fireEvent.click(screen.getByLabelText("Add enemy 2"));
    fireEvent.click(screen.getByText("Buddy"));
    expect(screen.getByText(/1\/2 healers?/)).toBeInTheDocument();
  });

  it("mode toggle switches Conquest(5v5) to Joust(3v3) and truncates rather than clears", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    fireEvent.click(screen.getByLabelText("Add ally 5"));
    fireEvent.click(screen.getByText("Buddy"));
    expect(screen.getByLabelText("Change ally 5 (Buddy)")).toBeInTheDocument();

    fireEvent.click(screen.getByRole("button", { name: /joust/i }));
    expect(screen.queryByLabelText(/ally 5/)).not.toBeInTheDocument();
    expect(screen.getByLabelText("Change you (TestGod)")).toBeInTheDocument();
  });

  it("renders a Copy link button that copies the current URL to the clipboard", () => {
    const writeText = vi.fn().mockResolvedValue(undefined);
    Object.assign(navigator, { clipboard: { writeText } });
    render(<DraftPage gods={GODS} items={[]} builds={[]} />);
    fireEvent.click(screen.getByRole("button", { name: /copy link/i }));
    expect(writeText).toHaveBeenCalledWith(window.location.href);
  });

  it("keeps the shareable URL in sync (via replaceState) as the draft is entered", () => {
    window.location.hash = "#/draft";
    render(<DraftPage gods={GODS} items={[]} builds={[]} godItemScores={GOD_ITEM_SCORES} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    expect(window.location.hash).toContain("me=TestGod");
  });

  it("a URL draft wins over a saved localStorage draft on load", () => {
    localStorage.setItem("smite:draft", JSON.stringify({ mode: "conquest", allies: ["Buddy", "", "", "", ""], enemies: [] }));
    window.location.hash = "#/draft?m=conquest&me=TestGod";
    render(<DraftPage gods={GODS} items={[]} builds={[]} godItemScores={GOD_ITEM_SCORES} />);
    expect(screen.getByLabelText("Change you (TestGod)")).toBeInTheDocument();
  });

  it("ignores unknown/untracked god names from the URL", () => {
    window.location.hash = "#/draft?m=conquest&me=NotTracked";
    render(<DraftPage gods={GODS} items={[]} builds={[]} godItemScores={GOD_ITEM_SCORES} />);
    expect(screen.getByLabelText("Add you")).toBeInTheDocument();
  });
});
