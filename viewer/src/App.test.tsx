import { describe, it, expect, beforeEach, vi } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import App from "./App";
import { toHash } from "./lib/useHashRoute";

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
    // Every ally slot reserves the label's height, so "You" appears once per
    // ally slot; only the first is visible.
    await waitFor(() => expect(screen.getAllByText("You")[0]).toBeInTheDocument());
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

  it("appends the current patch label to the header freshness stamp when data_patch is present", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({
      ok: true, json: () => Promise.resolve({ ...data, data_patch: "Open Beta 39" }),
    }));
    render(<App />);
    const freshness = await screen.findByTestId("header-freshness");
    expect(freshness.textContent).toMatch(/^Updated .+ · Open Beta 39$/);
  });

  it("omits the patch clause from the header stamp cleanly when data_patch is absent", async () => {
    render(<App />);
    const freshness = await screen.findByTestId("header-freshness");
    expect(freshness.textContent).not.toContain("·");
  });

  it("shows a layout-shaped skeleton (not a bare Loading… string) before data arrives", () => {
    render(<App />);
    // The default route is home, so the placeholder is shaped like home rather
    // than like the sidebar/build shell.
    expect(screen.getByTestId("home-skeleton")).toBeInTheDocument();
    expect(screen.queryByText(/^Loading…$/)).not.toBeInTheDocument();
  });

  it("uses the build-shell skeleton on a build route", () => {
    window.location.hash = toHash.builds();
    render(<App />);
    expect(screen.getByTestId("app-skeleton")).toBeInTheDocument();
  });

  it("does not ambush a first-time visitor with the legend", async () => {
    localStorage.clear();
    render(<App />);
    await screen.findByTestId("header-freshness");
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });

  it("opens the legend on demand from the help control", async () => {
    render(<App />);
    await screen.findByTestId("header-freshness");
    fireEvent.click(screen.getAllByRole("button", { name: /help/i })[0]);
    await waitFor(() => expect(screen.getByRole("dialog")).toHaveAccessibleName(/how this works/i));
  });
});
