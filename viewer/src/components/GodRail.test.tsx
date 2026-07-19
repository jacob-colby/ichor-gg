import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { GodRail } from "./GodRail";
import type { God } from "../types";

const chiron = {
  name: "Chiron",
  pantheon: "Greek",
  role: "Hunter",
  damage_type: "Physical",
  abilities: [{ slot: 1, name: "Training Exercise" }],
} as unknown as God;

const gods: God[] = [
  chiron,
  { name: "Ullr" } as unknown as God,
];

describe("GodRail", () => {
  it("renders one entry per god", () => {
    render(<GodRail gods={gods} selectedGod={null} onSelect={() => {}} />);
    expect(screen.getByRole("button", { name: /Chiron/i })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /Ullr/i })).toBeInTheDocument();
  });

  it("calls onSelect with the god's name when clicked", () => {
    const onSelect = vi.fn();
    render(<GodRail gods={gods} selectedGod={null} onSelect={onSelect} />);
    fireEvent.click(screen.getByRole("button", { name: /Ullr/i }));
    expect(onSelect).toHaveBeenCalledWith("Ullr");
  });

  it("uses the headshot icon variant", () => {
    render(<GodRail gods={[chiron]} selectedGod={null} onSelect={() => {}} />);
    const img = screen.getByRole("img", { name: "Chiron" });
    expect(img).toHaveAttribute("src", "/icons/chiron-head.png");
  });

  it("marks the selected god's button distinctly (aria-pressed)", () => {
    render(<GodRail gods={gods} selectedGod="Chiron" onSelect={() => {}} />);
    expect(screen.getByRole("button", { name: /Chiron/i })).toHaveAttribute(
      "aria-pressed",
      "true",
    );
    expect(screen.getByRole("button", { name: /Ullr/i })).toHaveAttribute(
      "aria-pressed",
      "false",
    );
  });
});
