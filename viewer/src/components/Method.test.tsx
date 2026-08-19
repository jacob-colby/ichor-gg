import { describe, it, expect } from "vitest";
import { render, screen, within } from "@testing-library/react";
import { Method } from "./Method";
import type { Item, MethodData } from "../types";

const method: MethodData = {
  signals: { efficiency: 0.35, win: 0.45, pick: 0.05, fit: 0.15 },
  kit_blend: 0.3,
  underrated: { max_pick: 0.15, top_quality_frac: 0.3 },
};

const items = [
  { name: "A", stats: { Penetration: "10", Strength: "40" } },
  { name: "B", stats: { Penetration: "10%", Strength: "30" } },
  { name: "C", stats: { Strength: "20" } },
] as unknown as Item[];

const gold = { _intercept: 1933, Strength: 10.88, Penetration: 8.63, "Penetration %": 38.92 };

const page = (props = {}) => (
  <Method method={method} goldValues={gold} items={items} godCount={87} {...props} />
);

describe("Method — the numbers are the pipeline's, not the page's", () => {
  it("states the blend from the shipped weights", () => {
    render(page());
    // eff+fit = 0.50 math, win+pick = 0.50 meta — the tension the page exists
    // to be honest about.
    expect(screen.getAllByText("0.50").length).toBeGreaterThanOrEqual(2);
    expect(screen.getByText(/honest tension in the tool/i)).toBeInTheDocument();
  });

  /** Scoped to its own section: 0.30 is also the kit blend elsewhere on the
   *  page, and a page-wide match would pass for the wrong reason. */
  const threeBuilds = () =>
    within(screen.getByRole("heading", { name: /the model, the community/i }).closest("section")!);

  it("derives the model build's renormalized weights rather than restating them", () => {
    render(page());
    // 0.35/0.50 and 0.15/0.50 — never a second hardcoded constant.
    expect(threeBuilds().getByText("0.70")).toBeInTheDocument();
    expect(threeBuilds().getByText("0.30")).toBeInTheDocument();
  });

  it("follows a reweighting instead of describing the old blend", () => {
    render(page({ method: { ...method, signals: { efficiency: 0.6, win: 0.2, pick: 0.0, fit: 0.2 } } }));
    expect(screen.getByText("0.80")).toBeInTheDocument();          // math half
    expect(threeBuilds().getByText("0.75")).toBeInTheDocument();   // renormalized efficiency
  });

  it("prices each penetration column separately and counts the items behind it", () => {
    render(page());
    const table = screen.getByRole("table");
    const flat = within(table).getByText("Penetration").closest("tr")!;
    const pct = within(table).getByText("Penetration %").closest("tr")!;
    expect(within(flat).getByText("8.63")).toBeInTheDocument();
    expect(within(pct).getByText("38.92")).toBeInTheDocument();
    // Strength is on all three fixtures, each penetration column on one.
    const strength = within(table).getByText("Strength").closest("tr")!;
    expect(within(strength).getByText("3")).toBeInTheDocument();
  });

  it("marks a price fitted from too few items instead of presenting it as solid", () => {
    render(page());
    const table = screen.getByRole("table");
    const pct = within(table).getByText("Penetration %").closest("tr")!;
    expect(within(pct).getByText(/thin/i)).toBeInTheDocument();
    const strength = within(table).getByText("Strength").closest("tr")!;
    expect(within(strength).queryByText(/thin/i)).not.toBeInTheDocument();
  });

  it("never prints the intercept as a stat row", () => {
    render(page());
    expect(within(screen.getByRole("table")).queryByText("_intercept")).not.toBeInTheDocument();
    // ...but does account for it, since a stat-only receipt never adds up.
    expect(screen.getByText("1933g")).toBeInTheDocument();
  });

  it("writes the limits down rather than gesturing at them", () => {
    render(page());
    // These two entries went stale silently: crit multipliers and stat
    // conversions are priced now, and combat.py is exact and feeds the draft,
    // while the page still claimed neither existed. Asserted on the CURRENT
    // claim so the next flag flip trips a test rather than shipping a lie.
    expect(screen.getByText(/Most item passives are still unpriced/i)).toBeInTheDocument();
    expect(screen.getByText(/damage model is exact/i)).toBeInTheDocument();
    expect(screen.getAllByText(/ignores magnitude/i).length).toBeGreaterThan(0);
    expect(screen.getByText(/one mode and one skill band/i)).toBeInTheDocument();
  });

  it("renders without weights instead of inventing them", () => {
    render(<Method method={undefined} goldValues={{}} items={items} godCount={87} />);
    expect(screen.getByText(/How the model decides/i)).toBeInTheDocument();
    expect(screen.queryByRole("table")).not.toBeInTheDocument();
    expect(screen.queryByText(/honest tension/i)).not.toBeInTheDocument();
  });
});
