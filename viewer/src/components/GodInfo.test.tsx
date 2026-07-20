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
});
