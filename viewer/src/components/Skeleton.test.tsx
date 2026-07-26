import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { AppSkeleton, GodSidebarSkeleton, CardGridSkeleton, BuildSkeleton } from "./Skeleton";

describe("Skeletons", () => {
  it("renders the app skeleton with a sidebar and build shape", () => {
    render(<AppSkeleton />);
    expect(screen.getByTestId("app-skeleton")).toBeInTheDocument();
  });

  it("renders the requested number of god placeholders", () => {
    const { container } = render(<GodSidebarSkeleton count={8} />);
    // Count the card wrappers rather than utility classes — class names are an
    // implementation detail, the card count is the actual contract.
    expect(container.querySelectorAll(".grid > div")).toHaveLength(8);
  });

  it("hides skeletons from assistive tech", () => {
    const { container } = render(<CardGridSkeleton count={3} />);
    expect(container.firstElementChild).toHaveAttribute("aria-hidden", "true");
  });

  it("renders a build skeleton with the requested row count", () => {
    const { container } = render(<BuildSkeleton rows={4} />);
    expect(container.firstElementChild).toHaveAttribute("aria-hidden", "true");
  });
});
