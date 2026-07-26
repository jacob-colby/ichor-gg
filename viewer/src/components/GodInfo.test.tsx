import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { GodInfo } from "./GodInfo";
import type { God } from "../types";

const god = {
  type: "god", name: "Chiron", pantheon: "Greek", role: "Carry", specializations: [],
  damage_type: "physical", release_date: "2024", source_url: "", last_verified: "",
  base_stats: { health: { base: 569, per_level: 86 }, mana: { base: 322, per_level: 48 } },
  abilities: [
    { slot: "1st Ability", name: "Training Exercise", cooldown: [14], cost: [60],
      description: "Fires a volley.", details: ["Cooldown: 14", "Damage: 90"] },
  ],
  aspects: [{ name: "Aspect of the Heroic Tutor", kit_changes: "Copies damage." }],
} as unknown as God;

describe("GodInfo", () => {
  it("renders base stats, abilities, and the aspect", () => {
    render(<GodInfo god={god} />);
    expect(screen.getByText(/health/i)).toBeInTheDocument();
    expect(screen.getByText("569")).toBeInTheDocument(); // base health
    expect(screen.getByText("Training Exercise")).toBeInTheDocument();
    expect(screen.getByText("Fires a volley.")).toBeInTheDocument();
    expect(screen.getByText(/Damage: 90/)).toBeInTheDocument();
    expect(screen.getByText(/Copies damage/)).toBeInTheDocument();
  });

  it("states why a stance god has no ability order rather than dropping the section", () => {
    // Artio, Merlin and Ullr have no levelable abilities. The section used to
    // vanish, which reads as missing data rather than a fact about the kit.
    render(<GodInfo god={god} />);
    expect(screen.getByRole("heading", { name: /ability order/i })).toBeInTheDocument();
    expect(screen.getByText(/no levelable ability order/i)).toBeInTheDocument();
  });

  it("renders the ability order grid with ult levels marked and the heuristic disclaimer", () => {
    const godWithOrder = {
      ...god,
      ability_order: {
        order: [
          "1st Ability", "2nd Ability", "3rd Ability", "1st Ability", "Ultimate",
          "2nd Ability", "2nd Ability", "2nd Ability", "Ultimate", "1st Ability",
          "1st Ability", "1st Ability", "Ultimate", "3rd Ability", "3rd Ability",
          "3rd Ability", "Ultimate", "3rd Ability", "2nd Ability", "1st Ability",
        ],
        summary: { max_order: ["2nd Ability", "1st Ability", "3rd Ability"], ult_levels: [5, 9, 13, 17] },
      },
    } as unknown as God;
    render(<GodInfo god={godWithOrder} />);
    expect(screen.getByRole("heading", { name: /ability order/i })).toBeInTheDocument();
    // heuristic disclaimer, spelled out explicitly per spec D
    expect(screen.getByText(/derived from ability scaling/i)).toBeInTheDocument();
    expect(screen.getByText(/heuristic/i)).toBeInTheDocument();
    // the ult-level cells (5, 9, 13, 17) are visually marked gold
    const level5 = screen.getByText("5").closest("li")!;
    expect(level5.className).toMatch(/gold/);
    const level6 = screen.getByText("6").closest("li")!;
    expect(level6.className).not.toMatch(/gold/);
  });
});
