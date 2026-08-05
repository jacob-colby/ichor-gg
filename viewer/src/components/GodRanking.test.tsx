import { describe, it, expect } from "vitest";
import { render, screen, within } from "@testing-library/react";
import { GodRanking } from "./GodRanking";
import type { GodTierEntry } from "../types";

const entries: GodTierEntry[] = [
  { name: "Ymir", score: 0.56, win_rate: 0.60, matches: 400, play_share: 0.08, tier_score: "S", role: "Solo" },
  { name: "Ra", score: 0.52, win_rate: 0.55, matches: 380, play_share: 0.07, tier_score: "A", role: "Mid" },
  { name: "Agni", score: 0.50, win_rate: 0.53, matches: 300, play_share: 0.06, tier_score: "A", role: "Mid" },
  { name: "Anubis", score: null, tier_score: null, role: "Mid" },
];

const rank = (god: string, role: string) => (
  <GodRanking god={god} role={role} entries={entries} modeLabel="Conquest" />
);

describe("GodRanking — where a god sits", () => {
  it("leads with the record, not with a verdict about the community", () => {
    render(rank("Ra", "Mid"));
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent(/Ra wins\s*55%\s*of\s*380\s*tracked matches/i);
  });

  it("shows the tier and how often the god is picked", () => {
    render(rank("Ra", "Mid"));
    expect(screen.getByText(/tier/i)).toBeInTheDocument();
    expect(screen.getByText(/picked in/i)).toBeInTheDocument();
  });

  it("says a god with no sample is unmeasured rather than bad", () => {
    // Every god outside Conquest. The page used to fill this gap with the
    // site's own score, which measured -0.12 against real god strength.
    render(rank("Anubis", "Mid"));
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent(/Anubis isn’t measured in Conquest/i);
    expect(screen.getByText(/more honest answer/i)).toBeInTheDocument();
  });

  it("names the gods immediately above and below", () => {
    render(rank("Ra", "Mid"));
    expect(screen.getByRole("link", { name: /Ymir/ })).toHaveAttribute("href", "#/god/Ymir");
    expect(screen.getByRole("link", { name: /Agni/ })).toHaveAttribute("href", "#/god/Agni");
  });

  it("shows each neighbour's raw win rate", () => {
    render(rank("Ra", "Mid"));
    expect(screen.getByRole("link", { name: /Ymir/ })).toHaveTextContent("60%");
  });

  it("says there is nothing above the top-placed god instead of leaving a blank", () => {
    render(rank("Ymir", "Solo"));
    expect(screen.getByText(/Ymir is the highest-placed god measured/i)).toBeInTheDocument();
  });

  it("gives overall, band and lane standing", () => {
    render(rank("Agni", "Mid"));
    const standing = screen.getByRole("heading", { level: 3, name: /standing/i }).parentElement!;
    expect(within(standing).getByText(/Overall/)).toBeInTheDocument();
    expect(within(standing).getByText(/In band A/)).toBeInTheDocument();
    expect(within(standing).getByText(/In Mid/)).toBeInTheDocument();
  });

  it("explains a god missing from the mode as a coverage gap rather than a verdict", () => {
    render(<GodRanking god="Loki" role="Jungle" entries={entries} modeLabel="Joust" />);
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent(/Loki isn’t in the Joust standings/i);
    expect(screen.getByText(/coverage gap, not a verdict/i)).toBeInTheDocument();
  });

  it("states that nothing the site models enters the order", () => {
    // The page's whole correction, said where a reader can see it.
    render(rank("Ra", "Mid"));
    expect(screen.getByText(/Nothing this site models/i)).toBeInTheDocument();
  });

  it("links onward to the full tier list", () => {
    render(rank("Ra", "Mid"));
    expect(screen.getByRole("link", { name: /every placement/i })).toHaveAttribute("href", "#/tiers");
  });
});
