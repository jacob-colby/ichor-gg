import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
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
    expect(screen.getByText(/put your god in the gold slot/i)).toBeInTheDocument();
    expect(screen.queryByText("AntiHeal")).not.toBeInTheDocument();
    expect(screen.queryByText(/adapted core/i)).not.toBeInTheDocument();
  });

  it("renders the adapted core once the you-slot is filled", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    // With no enemies entered nothing has adapted, so the list says so.
    expect(screen.getByText(/the default core/i)).toBeInTheDocument();
    expect(screen.getAllByText(/^(Alpha|Beta|Gamma|Delta|Epsilon|Zeta|AntiHeal)$/)).toHaveLength(6);
  });

  it("promotes a countering item once a threat is entered", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    fireEvent.click(screen.getByLabelText("Add enemy 1"));
    fireEvent.click(screen.getByText("EnemyHealer"));
    // Appears twice by design: once as a displacement in "What changed", once
    // in the adapted core itself.
    expect(screen.getAllByText("AntiHeal").length).toBeGreaterThan(0);
    expect(within(screen.getByTestId("draft-core")).getAllByText("AntiHeal").length).toBe(2);
  });

  it("names what a promoted item displaced, and by how much", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    fireEvent.click(screen.getByLabelText("Add enemy 1"));
    fireEvent.click(screen.getByText("EnemyHealer"));
    const core = within(screen.getByTestId("draft-core"));
    // The displaced item and the magnitude both used to be computed and
    // thrown away, leaving "swap in" with nothing to swap in for.
    // Hedged: the pairing is by rank, not a swap the assembler made.
    expect(core.getByText(/in place of/i)).toBeInTheDocument();
    expect(core.getByText("Zeta")).toBeInTheDocument();
    expect(core.getByText(/^\+0\.\d\d$/)).toBeInTheDocument();
    expect(core.getByText(/answers anti-heal/i)).toBeInTheDocument();
  });

  it("states plainly when the draft has not moved the build", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/hasn.t moved this build yet/i);
    expect(within(screen.getByTestId("draft-core")).getByText(/add an enemy and the model starts re-ranking/i)).toBeInTheDocument();
  });

  it("leads with the number of items the draft moved", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    fireEvent.click(screen.getByLabelText("Add enemy 1"));
    fireEvent.click(screen.getByText("EnemyHealer"));
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/moved\s*1 of 6\s*items/i);
  });

  it("denominates threats by the enemy roster, not by how many are entered", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    fireEvent.click(screen.getByLabelText("Add enemy 1"));
    fireEvent.click(screen.getByText("EnemyHealer"));
    const threats = within(screen.getByTestId("draft-threats"));
    // One healer of a five-slot roster is 1/5 — reading it as 1/1 let a
    // barely-started draft drive a maximal overlay.
    expect(threats.getAllByText("1/5").length).toBeGreaterThan(0);
    expect(threats.getByText("healing").previousElementSibling).toHaveTextContent("1/5");
    expect(threats.getByText(/1 of 5 enemies known/i)).toBeInTheDocument();
  });

  it("renders threats that measured zero, once anything has been scouted", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    fireEvent.click(screen.getByLabelText("Add enemy 1"));
    fireEvent.click(screen.getByText("EnemyHealer"));
    const threats = within(screen.getByTestId("draft-threats"));
    // A measured "0 of 5 crit" is a finding, so it is shown.
    expect(threats.getByText("crit")).toBeInTheDocument();
    expect(threats.getAllByText("0/5").length).toBeGreaterThan(0);
  });

  it("does not print measured zeros before anything has been scouted", () => {
    // The opposite error to the one this redesign fixed: with no enemies in,
    // "0/5 crit" is unmeasured, not measured.
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    const threats = within(screen.getByTestId("draft-threats"));
    expect(threats.queryByText("0/5")).not.toBeInTheDocument();
    expect(threats.getByText(/nothing scouted yet/i)).toBeInTheDocument();
  });

  it("does not claim the draft moved anything when only the you-slot is filled", () => {
    // A physical god alone used to trigger the all-physical penetration bonus
    // at full strength, so the page reported "moved 4 of 6 items" directly
    // above copy saying nothing had adapted yet.
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/hasn.t moved this build yet/i);
  });

  it("names the enemies behind a threat", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    fireEvent.click(screen.getByLabelText("Add enemy 1"));
    fireEvent.click(screen.getByText("EnemyHealer"));
    expect(within(screen.getByTestId("draft-threats")).getAllByText("EnemyHealer").length).toBeGreaterThan(0);
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
    // Encoded from state, not read off the address bar — the two can disagree.
    expect(writeText).toHaveBeenCalledWith(expect.stringContaining("#/draft"));
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

  /* The "You" caption used to be a reserved row above every *ally* slot. That
   * kept the ally icons level with each other and pushed the whole ally row a
   * line below the enemy row it exists to be compared against. It is a badge on
   * the slot now, so both rows share one structure and one baseline. */
  it("gives ally and enemy slots identical structure, so the rows share a baseline", () => {
    render(<DraftPage gods={GODS} items={[]} builds={[]} />);
    const ally = screen.getByLabelText("Add ally 2");
    const enemy = screen.getByLabelText("Add enemy 2");
    expect(ally.className).toBe(enemy.className);
    expect(ally.parentElement!.className).toBe(enemy.parentElement!.className);
  });

  it("marks your own slot once, without a caption row", () => {
    render(<DraftPage gods={GODS} items={[]} builds={[]} />);
    const labels = screen.getAllByText("You");
    expect(labels).toHaveLength(1);
    // A badge on the slot, not a line above it.
    expect(labels[0].className).toMatch(/absolute/);
    expect(labels[0].className).not.toMatch(/invisible/);
  });

  /* The portrait is the slot. The name used to sit inside the button under the
   * icon, costing it half its height for a label the art already carries. */
  it("gives the portrait the whole slot and keeps the name reachable", () => {
    render(<DraftPage gods={GODS} items={[]} builds={[]} godItemScores={GOD_ITEM_SCORES} />);
    fireEvent.click(screen.getByLabelText("Add ally 2"));
    fireEvent.click(screen.getByText("Buddy"));
    const slot = screen.getByLabelText("Change ally 2 (Buddy)");
    // The name is gone from the face of the slot but not from the machine:
    // it is still the accessible name and the tooltip.
    expect(slot).toHaveAttribute("title", "Buddy");
    expect(slot.textContent).not.toContain("Buddy");
  });

  it("stacks Allies and Enemies until there is room for them side by side", () => {
    render(<DraftPage gods={GODS} items={[]} builds={[]} />);
    const teams = screen.getByTestId("draft-teams");
    expect(teams.className).toMatch(/flex-col/);
    expect(teams.className).toMatch(/lg:flex-row/);
  });

  it("removes a filled ally slot via its X control without opening the god picker", () => {
    render(<DraftPage gods={GODS} items={[]} builds={[]} godItemScores={GOD_ITEM_SCORES} />);
    fireEvent.click(screen.getByLabelText("Add ally 2"));
    fireEvent.click(screen.getByText("Buddy"));
    expect(screen.getByLabelText("Change ally 2 (Buddy)")).toBeInTheDocument();

    fireEvent.click(screen.getByLabelText("Remove Buddy from allies"));
    expect(screen.getByLabelText("Add ally 2")).toBeInTheDocument();
    expect(screen.queryByText("Pick a god")).not.toBeInTheDocument(); // picker never opened
  });

  it("removes the you-slot via its X control, distinctly labeled from a plain ally slot", () => {
    render(<DraftPage gods={GODS} items={[]} builds={[]} godItemScores={GOD_ITEM_SCORES} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    fireEvent.click(screen.getByLabelText("Remove TestGod from allies"));
    expect(screen.getByLabelText("Add you")).toBeInTheDocument();
  });

  it("removes a filled enemy slot via its X control, labeled with the enemies row", () => {
    render(<DraftPage gods={GODS} items={[]} builds={[]} godItemScores={GOD_ITEM_SCORES} />);
    fireEvent.click(screen.getByLabelText("Add enemy 1"));
    fireEvent.click(screen.getByText("EnemyHealer"));
    fireEvent.click(screen.getByLabelText("Remove EnemyHealer from enemies"));
    expect(screen.getByLabelText("Add enemy 1")).toBeInTheDocument();
  });

  it("does not show a remove control on an empty slot", () => {
    render(<DraftPage gods={GODS} items={[]} builds={[]} />);
    expect(screen.queryByLabelText(/^Remove /)).not.toBeInTheDocument();
  });

  it("keeps gold off item cost — it is neither selection, primary action, nor the model's signal", () => {
    render(<DraftPage gods={GODS} items={ITEMS} builds={[]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG} />);
    fireEvent.click(screen.getByLabelText("Add you"));
    fireEvent.click(screen.getByText("TestGod"));
    screen.getAllByText("2500g").forEach((c) => expect(c).not.toHaveClass("text-gold"));
  });
});
