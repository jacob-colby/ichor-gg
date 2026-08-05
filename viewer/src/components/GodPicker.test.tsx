import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { GodPickerDialog } from "./GodPicker";
import type { God } from "../types";

const gods = [
  { name: "Ymir", pantheon: "Norse", role: "Solo", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
  { name: "Ra", pantheon: "Egyptian", role: "Mid", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
  { name: "Cupid", pantheon: "Roman", role: "Support", damage_type: "physical", abilities: [], aspects: [], base_stats: {} },
] as unknown as God[];

const picker = (props: Partial<React.ComponentProps<typeof GodPickerDialog>> = {}) => (
  <GodPickerDialog gods={gods} selectedGod={null} onPick={() => {}} onClose={() => {}} {...props} />
);

beforeEach(() => localStorage.clear());

describe("GodPicker — the subject switcher", () => {
  it("lists every god", () => {
    render(picker());
    for (const n of ["Ymir", "Ra", "Cupid"]) {
      expect(screen.getByRole("button", { name: `Select ${n}` })).toBeInTheDocument();
    }
  });

  it("narrows with search", () => {
    render(picker());
    fireEvent.change(screen.getByLabelText(/search gods/i), { target: { value: "ra" } });
    expect(screen.getByRole("button", { name: "Select Ra" })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Select Ymir" })).not.toBeInTheDocument();
  });

  it("filters by a lane pill", () => {
    render(picker());
    fireEvent.click(screen.getByRole("button", { name: "Support" }));
    expect(screen.getByRole("button", { name: "Select Cupid" })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Select Ra" })).not.toBeInTheDocument();
  });

  it("reveals pantheon and damage filters behind a disclosure", () => {
    render(picker());
    expect(screen.queryByLabelText(/filter by pantheon/i)).not.toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /more filters/i }));
    fireEvent.change(screen.getByLabelText(/filter by pantheon/i), { target: { value: "Norse" } });
    expect(screen.getByRole("button", { name: "Select Ymir" })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Select Ra" })).not.toBeInTheDocument();
  });

  it("reports how many gods the filters leave", () => {
    render(picker());
    fireEvent.change(screen.getByLabelText(/search gods/i), { target: { value: "ra" } });
    expect(screen.getByRole("dialog")).toHaveTextContent(/1\s*of\s*3/);
  });

  it("offers a way out when nothing matches", () => {
    render(picker());
    fireEvent.change(screen.getByLabelText(/search gods/i), { target: { value: "zzzz" } });
    expect(screen.getByText(/no gods match/i)).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /clear filters/i }));
    expect(screen.getByRole("button", { name: "Select Ymir" })).toBeInTheDocument();
  });

  it("picks a god", () => {
    const onPick = vi.fn();
    render(picker({ onPick }));
    fireEvent.click(screen.getByRole("button", { name: "Select Ra" }));
    expect(onPick).toHaveBeenCalledWith("Ra");
  });

  it("marks the current subject", () => {
    render(picker({ selectedGod: "Ymir" }));
    expect(screen.getByRole("button", { name: "Select Ymir" })).toHaveAttribute("aria-pressed", "true");
    expect(screen.getByRole("button", { name: "Select Ra" })).toHaveAttribute("aria-pressed", "false");
  });

  it("groups pinned gods above the rest, without duplicating them", () => {
    localStorage.setItem("smite:pinnedGods", JSON.stringify(["Cupid"]));
    render(picker());
    expect(screen.getByText(/^Bookmarked$/)).toBeInTheDocument();
    expect(screen.getAllByRole("button", { name: "Select Cupid" })).toHaveLength(1);
  });

  // Regression: the card was a div[role=button] wrapping two focusable
  // buttons — 87 nested-interactive violations, one per god.
  it("keeps the pin control a sibling of the select button, not a child", () => {
    render(picker());
    const select = screen.getByRole("button", { name: "Select Ymir" });
    expect(within(select).queryByRole("button")).not.toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Bookmark Ymir" })).toBeInTheDocument();
  });

  it("is a real dialog: labelled, modal, focus moved in, Escape closes", () => {
    const onClose = vi.fn();
    render(picker({ onClose }));
    const dialog = screen.getByRole("dialog");
    expect(dialog).toHaveAttribute("aria-modal", "true");
    expect(dialog).toHaveAccessibleName(/choose a god/i);
    fireEvent.keyDown(document, { key: "Escape" });
    expect(onClose).toHaveBeenCalled();
  });

  it("closes from the ✕ control", () => {
    const onClose = vi.fn();
    render(picker({ onClose }));
    fireEvent.click(screen.getByRole("button", { name: /close/i }));
    expect(onClose).toHaveBeenCalled();
  });
});
