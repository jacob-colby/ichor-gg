import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { Legend } from "./Legend";

describe("Legend", () => {
  it("renders content and calls onClose when dismissed", () => {
    const onClose = vi.fn();
    render(<Legend onClose={onClose} />);
    expect(screen.getByText(/how this works/i)).toBeInTheDocument();
    expect(screen.getByText(/suggested/i)).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /got it|close/i }));
    expect(onClose).toHaveBeenCalled();
  });
});
