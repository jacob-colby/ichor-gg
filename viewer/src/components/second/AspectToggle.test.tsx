import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { AspectToggle } from "./AspectToggle";

const toggle = (on: boolean, changesBuild = true, onChange = vi.fn()) => {
  render(<AspectToggle aspect="Aspect of Thermotherapy" on={on} onChange={onChange} changesBuild={changesBuild} />);
  return { sw: screen.getByRole("switch"), onChange };
};
const hexOf = (el: Element) => {
  const svg = el.querySelector("svg[data-aspect-hex]")!;
  const [outline, notch] = svg.querySelectorAll("path");
  return { svg, outline, notch };
};

/* Jacob, 2026-11-09: "The Aspect icon should always be bright orange, ideally
 * with a hexagon shape. Maybe a toggle design that fills in when enabled." */
describe("AspectToggle — the aspect's own hexagon", () => {
  it("is still a switch named for the aspect, saying when it will not move the build", () => {
    const { sw, onChange } = toggle(false, false);
    expect(sw).toHaveAccessibleName("Aspect of Thermotherapy (doesn't change the build)");
    expect(sw).toHaveAttribute("aria-checked", "false");
    expect(sw).toHaveTextContent(/^AspectThermotherapy$/);
    fireEvent.click(sw);
    expect(onChange).toHaveBeenCalledWith(true);
  });

  it("off: the orange outline, empty, on a neutral frame", () => {
    const { sw } = toggle(false);
    const { svg, outline, notch } = hexOf(sw);
    expect(svg).toHaveAttribute("data-aspect-hex", "off");
    expect(outline).toHaveAttribute("stroke", "var(--color-aspect)");
    expect(outline).toHaveAttribute("fill-opacity", "0");
    expect(notch).toHaveAttribute("opacity", "0");
    expect(sw).toHaveClass("border-line");
  });

  it("on: the same hexagon filled with the notch kept, on an ember frame, never violet", () => {
    const { sw } = toggle(true);
    const { svg, outline, notch } = hexOf(sw);
    expect(sw).toHaveAttribute("aria-checked", "true");
    expect(svg).toHaveAttribute("data-aspect-hex", "on");
    expect(outline).toHaveAttribute("stroke", "var(--color-aspect)");
    expect(outline).toHaveAttribute("fill", "var(--color-aspect)");
    expect(outline).toHaveAttribute("fill-opacity", "1");
    expect(notch).toHaveAttribute("opacity", "1");
    expect(sw).toHaveClass("border-aspect/45", "bg-aspect/12");
    expect(sw.outerHTML).not.toMatch(/accent/);
  });

  it("fills over 150ms, and not at all under reduced motion", () => {
    const { sw } = toggle(false);
    const { outline, notch } = hexOf(sw);
    for (const p of [outline, notch]) {
      expect(p).toHaveClass("duration-150", "motion-reduce:transition-none");
    }
    expect(sw).toHaveClass("motion-reduce:transition-none");
  });
});
