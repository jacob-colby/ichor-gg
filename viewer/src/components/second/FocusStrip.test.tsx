import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import { FocusStrip } from "./FocusStrip";
import type { FocusOption } from "../../lib/focus";

const options = [
  { archetype: "model", label: "Ichor", kind: "focus" },
  { archetype: "burst", label: "Burst", kind: "focus" },
] as unknown as FocusOption[];

describe("FocusStrip", () => {
  it("keeps the aspect switch outside the sideways scroller, so a snap can never hide it", () => {
    render(<FocusStrip options={options} selected="model" onSelect={() => {}}
      aspect={<button role="switch" aria-checked={false}>Aspect</button>} />);
    const scroller = screen.getByTestId("focus-chips");
    expect(scroller.contains(screen.getByRole("switch"))).toBe(false);
    expect(scroller.contains(screen.getByText("Burst"))).toBe(true);
    expect(screen.getByRole("group", { name: "Adjust the build" }).contains(screen.getByRole("switch"))).toBe(true);
  });

  it("still shows the switch when the god has no other builds", () => {
    render(<FocusStrip options={[]} selected="model" onSelect={() => {}}
      aspect={<button role="switch" aria-checked={false}>Aspect</button>} />);
    expect(screen.getByRole("switch")).toBeTruthy();
    expect(screen.queryByTestId("focus-chips")).toBeNull();
  });
});
