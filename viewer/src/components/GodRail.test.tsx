import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { GodRail } from "./GodRail";
import type { God } from "../types";

const gods: God[] = [
  { name: "Chiron" } as God,
  { name: "Ullr" } as God,
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
