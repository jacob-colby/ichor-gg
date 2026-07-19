import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { ManageGods } from "./ManageGods";

describe("ManageGods", () => {
  it("posts an add request and calls onChanged on success", async () => {
    const fetchMock = vi.fn().mockResolvedValue({ json: () => Promise.resolve({ ok: true }) });
    vi.stubGlobal("fetch", fetchMock);
    const onChanged = vi.fn();
    render(<ManageGods onChanged={onChanged} />);
    fireEvent.change(screen.getByPlaceholderText(/add a god/i), { target: { value: "Thor" } });
    fireEvent.click(screen.getByRole("button", { name: /add/i }));
    await waitFor(() => expect(onChanged).toHaveBeenCalled());
    const [url, opts] = fetchMock.mock.calls[0];
    expect(url).toBe("/api/gods");
    expect(JSON.parse(opts.body)).toEqual({ action: "add", name: "Thor" });
    vi.unstubAllGlobals();
  });

  it("surfaces an error and does not call onChanged on failure", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ json: () => Promise.resolve({ ok: false, error: "scrape failed" }) }));
    const onChanged = vi.fn();
    render(<ManageGods onChanged={onChanged} />);
    fireEvent.change(screen.getByPlaceholderText(/add a god/i), { target: { value: "Xyz" } });
    fireEvent.click(screen.getByRole("button", { name: /add/i }));
    await waitFor(() => expect(screen.getByText(/scrape failed/i)).toBeInTheDocument());
    expect(onChanged).not.toHaveBeenCalled();
    vi.unstubAllGlobals();
  });
});
