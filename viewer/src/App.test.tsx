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

  it("navigates to the gods index via the nav", async () => {
    render(<App />);
    const [gods] = await screen.findAllByRole("button", { name: /^gods$/i });
    fireEvent.click(gods);
    await waitFor(() => expect(screen.getByPlaceholderText(/search gods/i)).toBeInTheDocument());
  });

  it("shows the data-freshness stamp", async () => {
    render(<App />);
    await waitFor(() => expect(screen.getByText(/Data from 2026-07-19/i)).toBeInTheDocument());
  });

  it("shows the legend on first run", async () => {
    localStorage.removeItem("smite:legend-seen");
    render(<App />);
    await waitFor(() => expect(screen.getByText(/how this works/i)).toBeInTheDocument());
  });
});
