import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { BuildEditor } from "./BuildEditor";
import type { Item } from "../types";

const items = [{ name: "Deathbringer" }, { name: "Rage" }] as Item[];

describe("BuildEditor", () => {
  it("saves a build via the endpoint and calls onSaved", async () => {
    const fetchMock = vi.fn().mockResolvedValue({ json: () => Promise.resolve({ ok: true }) });
    vi.stubGlobal("fetch", fetchMock);
    const onSaved = vi.fn();
    const onClose = vi.fn();
    render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                        onClose={onClose} onSaved={onSaved} />);
    fireEvent.change(screen.getByPlaceholderText(/build name/i), { target: { value: "My Build" } });
    fireEvent.change(screen.getByPlaceholderText(/search items/i), { target: { value: "Death" } });
    fireEvent.click(screen.getByText("Deathbringer"));
    fireEvent.click(screen.getByRole("button", { name: /^save$/i }));
    await waitFor(() => expect(onSaved).toHaveBeenCalled());
    const body = JSON.parse(fetchMock.mock.calls[0][1].body);
    expect(body).toMatchObject({ action: "save", god: "Chiron", mode: "Conquest",
      name: "My Build", slot_order: ["Deathbringer"] });
    vi.unstubAllGlobals();
  });

  it("blocks saving with no name and surfaces an inline error", () => {
    const fetchMock = vi.fn();
    vi.stubGlobal("fetch", fetchMock);
    render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                        onClose={() => {}} onSaved={() => {}} />);
    fireEvent.click(screen.getByRole("button", { name: /^save$/i }));
    expect(screen.getByText(/name required/i)).toBeInTheDocument();
    expect(fetchMock).not.toHaveBeenCalled();
    vi.unstubAllGlobals();
  });

  it("deletes an existing build via the endpoint", async () => {
    const fetchMock = vi.fn().mockResolvedValue({ json: () => Promise.resolve({ ok: true }) });
    vi.stubGlobal("fetch", fetchMock);
    const onSaved = vi.fn();
    render(<BuildEditor god="Chiron" mode="Conquest" items={items} starters={[]}
                        initial={{ name: "Old", slot_order: ["Rage"] }}
                        onClose={() => {}} onSaved={onSaved} />);
    fireEvent.click(screen.getByRole("button", { name: /^delete$/i }));
    await waitFor(() => expect(onSaved).toHaveBeenCalled());
    const body = JSON.parse(fetchMock.mock.calls[0][1].body);
    expect(body).toMatchObject({ action: "delete", god: "Chiron", mode: "Conquest", name: "Old" });
    vi.unstubAllGlobals();
  });
});
