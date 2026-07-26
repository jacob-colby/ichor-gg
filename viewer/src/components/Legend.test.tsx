import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { Legend } from "./Legend";

describe("Legend", () => {
  it("renders content and calls onClose when dismissed", () => {
    const onClose = vi.fn();
    render(<Legend onClose={onClose} />);
    expect(screen.getByText(/how this works/i)).toBeInTheDocument();
    expect(screen.getByText(/suggested/i)).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "Got it" }));
    expect(onClose).toHaveBeenCalled();
  });

  it("is a real dialog, labelled by its heading", () => {
    render(<Legend onClose={vi.fn()} />);
    const dialog = screen.getByRole("dialog");
    expect(dialog).toHaveAttribute("aria-modal", "true");
    expect(dialog).toHaveAccessibleName(/how this works/i);
  });

  it("moves focus into the dialog on open", () => {
    render(<Legend onClose={vi.fn()} />);
    expect(document.activeElement).toBe(screen.getByRole("heading", { name: /how this works/i }));
  });

  it("closes on Escape", () => {
    const onClose = vi.fn();
    render(<Legend onClose={onClose} />);
    fireEvent.keyDown(document, { key: "Escape" });
    expect(onClose).toHaveBeenCalled();
  });

  it("closes from the ✕ control as well as the confirm button", () => {
    const onClose = vi.fn();
    render(<Legend onClose={onClose} />);
    fireEvent.click(screen.getByRole("button", { name: /close/i }));
    expect(onClose).toHaveBeenCalled();
  });

  it("wraps Tab at the end of the dialog so focus never reaches the page behind", () => {
    render(<Legend onClose={vi.fn()} />);
    const buttons = screen.getAllByRole("button");
    const last = buttons[buttons.length - 1];
    last.focus();
    fireEvent.keyDown(document, { key: "Tab" });
    expect(document.activeElement).toBe(buttons[0]);
  });

  it("restores focus to whatever opened it", () => {
    const opener = document.createElement("button");
    document.body.appendChild(opener);
    opener.focus();

    const { unmount } = render(<Legend onClose={vi.fn()} />);
    expect(document.activeElement).not.toBe(opener);
    unmount();
    expect(document.activeElement).toBe(opener);

    opener.remove();
  });
});
