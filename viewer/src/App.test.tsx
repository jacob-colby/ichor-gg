import { describe, it, expect, beforeEach, vi } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import App from "./App";

const data = {
  gods: [
    {
      name: "Chiron", pantheon: "Greek", role: "Carry", damage_type: "physical",
      base_stats: { health: { base: 569, per_level: 86 } }, abilities: [], aspects: [],
    },
  ],
  items: [
    { name: "Rage", tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [], effect_tags: [], efficiency_tier: "undervalued" },
  ],
  builds: [],
  starters: [],
  roster: [],
  data_updated: "2026-07-19",
};

beforeEach(() => {
  window.location.hash = "";
  localStorage.clear();
  localStorage.setItem("smite:legend-seen", "1"); // suppress first-run legend by default
  vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ ok: true, json: () => Promise.resolve(data) }));
});

describe("App routing", () => {
  // The shell renders two nav controls (desktop icon rail + mobile bottom bar),
  // so each label matches twice; clicking either navigates identically.
  it("navigates to the items shop via the nav", async () => {
    render(<App />);
    const [items] = await screen.findAllByRole("button", { name: /^items$/i });
    fireEvent.click(items);
    await waitFor(() => expect(screen.getByPlaceholderText(/search items/i)).toBeInTheDocument());
  });

  it("defaults to the home view with no god rail", async () => {
    render(<App />);
    await waitFor(() => expect(screen.getByPlaceholderText(/search gods/i)).toBeInTheDocument());
    expect(screen.queryByRole("button", { name: "Select Chiron" })).not.toBeInTheDocument();
    const [home] = await screen.findAllByRole("button", { name: /^home$/i });
    expect(home).toHaveAttribute("aria-current", "true");
  });

  it("navigates to the standalone draft page via the nav", async () => {
    render(<App />);
    const [draft] = await screen.findAllByRole("button", { name: /^draft$/i });
    fireEvent.click(draft);
    // The draft page's ally slot 1 is always labeled "You", filled or not —
    // a stable signal that the real page (not the old placeholder) rendered.
    await waitFor(() => expect(screen.getByText("You")).toBeInTheDocument());
  });

  it("navigates to the builds view via the nav, showing the god sidebar", async () => {
    render(<App />);
    const [builds] = await screen.findAllByRole("button", { name: /^builds$/i });
    fireEvent.click(builds);
    await waitFor(() => expect(screen.getByText(/select a god from the sidebar/i)).toBeInTheDocument());
    expect(screen.getByRole("button", { name: "Select Chiron" })).toBeInTheDocument();
  });

  it("no longer has a gods nav entry, and #/gods redirects to home", async () => {
    window.location.hash = "#/gods";
    render(<App />);
    expect(screen.queryAllByRole("button", { name: /^gods$/i })).toHaveLength(0);
    await waitFor(() => expect(screen.getByPlaceholderText(/search gods/i)).toBeInTheDocument());
    expect(window.location.hash).toBe("#/");
  });

  it("shows the data-freshness stamp as relative text with the absolute date on hover", async () => {
    render(<App />);
    const freshness = await screen.findByTestId("header-freshness");
    expect(freshness.textContent).toMatch(/^Updated /i);
    expect(freshness).toHaveAttribute("title", "2026-07-19");
  });

  it("omits the freshness stamp entirely when data_updated is missing", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({
      ok: true, json: () => Promise.resolve({ ...data, data_updated: undefined }),
    }));
    render(<App />);
    await waitFor(() => expect(screen.getByPlaceholderText(/search gods/i)).toBeInTheDocument());
    expect(screen.queryByTestId("header-freshness")).not.toBeInTheDocument();
  });

  it("shows a layout-shaped skeleton (not a bare Loading… string) before data arrives", () => {
    render(<App />);
    expect(screen.getByTestId("app-skeleton")).toBeInTheDocument();
    expect(screen.queryByText(/^Loading…$/)).not.toBeInTheDocument();
  });

  it("shows the legend on first run", async () => {
    localStorage.removeItem("smite:legend-seen");
    render(<App />);
    await waitFor(() => expect(screen.getByText(/how this works/i)).toBeInTheDocument());
  });
});
