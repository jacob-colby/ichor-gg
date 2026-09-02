import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { AspectToggle } from "./AspectBadge";

/* F11. A geometry regression is invisible in review and invisible in jsdom,
 * which reports every box as 0×0 — so this asserts on the utilities that
 * produce the box instead, resolved to the pixels they compile to. That is
 * weaker than a rendered measurement and it catches the thing that actually
 * went wrong: the size was passed in from two call sites as `h-5 w-5`, beating
 * the component's own `h-4 w-4` in Tailwind's cascade rather than in the class
 * attribute, and nobody could see 20px in either file.
 *
 * The rendered target was measured at 24×24 in the browser at 375px after this
 * change. WCAG 2.2 SC 2.5.8 puts the floor at 24. */
const TARGET_FLOOR_PX = 24;

/** Tailwind's spacing scale, in px at the app's default root size. */
const SPACING: Record<string, number> = {
  "0.5": 2, "1": 4, "1.5": 6, "2": 8, "3": 12, "4": 16, "5": 20, "6": 24, "7": 28, "8": 32,
};

/** The button's own box, from its class list: the size utility plus padding on
 *  both edges, which is what the pointer can land on. */
function boxPx(el: Element, axis: "h" | "w"): number {
  const classes = el.className.split(/\s+/);
  const sizes = classes.filter((c) => c.startsWith(`${axis}-`) && SPACING[c.slice(2)] != null);
  // More than one is the bug this test exists for: which of them wins is
  // decided by the order Tailwind emitted them, not by anything readable here.
  expect(sizes).toHaveLength(1);
  const pad = classes.find((c) => c === "p-0.5" || c.startsWith("p-"));
  const padPx = pad ? (SPACING[pad.slice(2)] ?? 0) : 0;
  return SPACING[sizes[0].slice(2)] + (classes.includes("box-content") ? padPx * 2 : 0);
}

const toggle = (props: Partial<React.ComponentProps<typeof AspectToggle>> = {}) => (
  <AspectToggle aspectName="Aspect of Thermotherapy" on={false} onToggle={() => {}} {...props} />
);

describe("AspectToggle — the tap target", () => {
  it("is at least 24px on both axes", () => {
    render(toggle());
    const button = screen.getByRole("button");
    expect(boxPx(button, "h")).toBeGreaterThanOrEqual(TARGET_FLOOR_PX);
    expect(boxPx(button, "w")).toBeGreaterThanOrEqual(TARGET_FLOOR_PX);
  });

  it("owns its size, so no caller can shrink it below the floor", () => {
    // The regression was exactly this: both call sites sent a size, and the
    // one that won was decided in the stylesheet.
    render(toggle({ className: "h-5 w-5" }));
    expect(() => boxPx(screen.getByRole("button"), "h")).toThrow();
  });

  it("keeps the mark inside the target rather than growing it", () => {
    // The hexagon still renders at 20px — the padding is what makes the
    // difference, so the portrait looks the same as it did.
    render(toggle());
    const button = screen.getByRole("button");
    expect(button.className).toContain("p-0.5");
    expect(button.querySelector("svg")).toHaveClass("h-full", "w-full");
  });
});

describe("AspectToggle — what it says it is", () => {
  it("names the aspect in the label rather than only marking one", () => {
    render(toggle());
    expect(screen.getByRole("button", { name: /Build for the Thermotherapy aspect/i }))
      .toHaveAttribute("aria-pressed", "false");
  });

  it("says when pressing it will not move the build", () => {
    render(toggle({ changesBuild: false }));
    expect(screen.getByRole("button", { name: /no scoring overlay/i })).toBeInTheDocument();
  });

  it("does not fire whatever it is sitting on top of", () => {
    const onToggle = vi.fn();
    const onParent = vi.fn();
    render(
      <div onClick={onParent} className="relative">
        {toggle({ onToggle })}
      </div>,
    );
    fireEvent.click(screen.getByRole("button"));
    expect(onToggle).toHaveBeenCalledOnce();
    expect(onParent).not.toHaveBeenCalled();
  });
});
