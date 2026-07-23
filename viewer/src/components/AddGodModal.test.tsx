import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { AddGodModal } from "./AddGodModal";

describe("AddGodModal", () => {
  it("lists roster gods, marks tracked, and adds an untracked one", () => {
    const onAdd = vi.fn();
    render(<AddGodModal roster={[{ name: "Ymir" }, { name: "Thor" }]} tracked={["Ymir"]} onAdd={onAdd} onClose={() => {}} />);
    expect(screen.getByText("Ymir")).toBeInTheDocument();
    expect(screen.getByText(/tracked/i)).toBeInTheDocument();
    // tracked god's button is disabled
    expect(screen.getByRole("button", { name: /Ymir/i })).toBeDisabled();
    fireEvent.change(screen.getByPlaceholderText(/search gods/i), { target: { value: "thor" } });
    fireEvent.click(screen.getByRole("button", { name: /Add Thor/i }));
    expect(onAdd).toHaveBeenCalledWith("Thor");
  });
});
