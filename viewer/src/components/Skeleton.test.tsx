import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { AppSkeleton, CardGridSkeleton, BuildSkeleton } from "./Skeleton";

describe("Skeletons", () => {
  it("renders the app skeleton with a sidebar and build shape", () => {
    render(<AppSkeleton />);
    expect(screen.getByTestId("app-skeleton")).toBeInTheDocument();
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
