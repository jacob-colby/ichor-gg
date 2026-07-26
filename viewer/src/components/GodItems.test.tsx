import { describe, it, expect } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { GodItems } from "./GodItems";
import type { Item } from "../types";

const item = (name: string, cost: number, residual: number | null = null): Item => ({
  type: "item", name, tier: 3, cost, stats: {}, passive: "",
  builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: null,
  efficiency: residual == null ? null : { predicted_cost: cost - residual, residual, score: 0.5 },
} as unknown as Item);

const items = [item("Rage", 2500, -400), item("Aegis", 2100, 300), item("Deathbringer", 3000)];
const scores = { Rage: 0.49, Aegis: 0.41, Deathbringer: 0.45 };

describe("GodItems — the ranking that had no page", () => {
  it("leads with how many items the model ranks", () => {
    render(<GodItems god="Ra" scores={scores} items={items} core={[]} />);
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent(/ranks 3 items for Ra/i);
  });

  it("orders best first and numbers the ranks", () => {
    render(<GodItems god="Ra" scores={scores} items={items} core={[]} />);
    const rows = screen.getAllByRole("listitem");
    expect(within(rows[0]).getByText("Rage")).toBeInTheDocument();
    expect(within(rows[2]).getByText("Aegis")).toBeInTheDocument();
  });

  it("carries price and the gold model's verdict on each row", () => {
    render(<GodItems god="Ra" scores={scores} items={items} core={[]} />);
    const rage = screen.getByRole("link", { name: /^Rank 1, Rage/ });
    expect(rage).toHaveTextContent("2500g");
    expect(rage).toHaveTextContent("−400g");
  });

  /* Scores across the real set span about 0.1. Saying so is the difference
   * between a ranking and a false claim of precision. */
  it("states the spread rather than implying the bars are absolute", () => {
    render(<GodItems god="Ra" scores={scores} items={items} core={[]} />);
    expect(screen.getByText(/spread of/i)).toBeInTheDocument();
    expect(screen.getByText(/not drawn from zero/i)).toBeInTheDocument();
  });

  it("marks the god's own core and can narrow to it", () => {
    render(<GodItems god="Ra" scores={scores} items={items} core={["Rage"]} />);
    expect(screen.getAllByText(/in core/i).length).toBeGreaterThan(0);
    fireEvent.click(screen.getByRole("button", { name: /only the core/i }));
    expect(screen.getByText("Rage")).toBeInTheDocument();
    expect(screen.queryByText("Aegis")).not.toBeInTheDocument();
  });

  it("says how much of the core the ranking covers", () => {
    render(<GodItems god="Ra" scores={scores} items={items} core={["Rage", "Ghost"]} />);
    expect(screen.getByText(/1 of the build’s 2/i)).toBeInTheDocument();
  });

  /* Ra's core skips rank 4. Claiming "the build takes the top six" without
   * checking would be false for most gods. */
  it("only claims the core is the top when it actually is", () => {
    render(<GodItems god="Ra" scores={scores} items={items} core={["Rage", "Deathbringer"]} />);
    expect(screen.getByText(/takes the top/i)).toBeInTheDocument();
  });

  it("says the core is not the top when it skips a rank", () => {
    render(<GodItems god="Ra" scores={scores} items={items} core={["Rage", "Aegis"]} />);
    expect(screen.getByText(/aren’t simply the top/i)).toBeInTheDocument();
    expect(screen.queryByText(/takes the top/i)).not.toBeInTheDocument();
  });

  // Counted rather than silently dropped.
  it("names a scored item the index has no entry for", () => {
    render(<GodItems god="Ra" scores={{ ...scores, Phantom: 0.44 }} items={items} core={[]} />);
    expect(screen.getByText(/1 scored item isn’t\s*in this index/i)).toBeInTheDocument();
    expect(screen.getByText(/not in index/i)).toBeInTheDocument();
  });

  it("explains an empty ranking as a coverage gap, not a verdict", () => {
    render(<GodItems god="Ra" scores={undefined} items={items} core={[]} />);
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent(/No item ranking for Ra/i);
    expect(screen.getByText(/gap in the pipeline’s coverage/i)).toBeInTheDocument();
  });

  it("names both facts in each row's accessible name", () => {
    render(<GodItems god="Ra" scores={scores} items={items} core={["Rage"]} />);
    expect(screen.getByRole("link", { name: /Rank 1, Rage, model score 0\.49, 2500 gold, in the suggested core/ }))
      .toBeInTheDocument();
  });
});
