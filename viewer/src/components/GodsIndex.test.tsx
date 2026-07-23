import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { GodsIndex } from "./GodsIndex";
import type { God } from "../types";

const gods = [
  { name: "Ymir", pantheon: "Norse", role: "Solo", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
  { name: "Ra", pantheon: "Egyptian", role: "Mid", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
] as unknown as God[];

describe("GodsIndex", () => {
  it("renders a card per god and filters by search", () => {
    render(<GodsIndex gods={gods} />);
    expect(screen.getByText("Ymir")).toBeInTheDocument();
    expect(screen.getByText("Ra")).toBeInTheDocument();
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "ra" } });
    expect(screen.getByText("Ra")).toBeInTheDocument();
    expect(screen.queryByText("Ymir")).not.toBeInTheDocument();
  });
});
