import { describe, it, expect } from "vitest";
import { render, screen, within } from "@testing-library/react";
import { GodRanking } from "./GodRanking";
import type { GodTierEntry } from "../types";

const entries: GodTierEntry[] = [
  { name: "Ymir", ours: 0.90, community: 0.30, tier_ours: "S", tier_community: "C", role: "Solo" },
  { name: "Ra", ours: 0.70, community: 0.80, tier_ours: "A", tier_community: "S", role: "Mid" },
  { name: "Agni", ours: 0.60, community: 0.60, tier_ours: "A", tier_community: "A", role: "Mid" },
  { name: "Anubis", ours: 0.40, community: null, tier_ours: "C", tier_community: null, role: "Mid" },
];

const rank = (god: string, role: string) => (
  <GodRanking god={god} role={role} entries={entries} modeLabel="Conquest" />
);

describe("GodRanking — where a god sits", () => {
  it("states the disagreement in words, both letters named", () => {
    render(rank("Ra", "Mid"));
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent(/model says\s*A.*community\s*says\s*S/is);
  });

  it("says both agree when they do", () => {
    render(rank("Agni", "Mid"));
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent(/Both put Agni at\s*A/i);
  });

  it("says the community hasn't rated an unranked god, rather than implying agreement", () => {
    render(rank("Anubis", "Mid"));
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent(/community hasn’t rated Anubis/i);
    expect(screen.getByText(/it isn’t agreement/i)).toBeInTheDocument();
  });

  it("names the gods immediately above and below on the model's scale", () => {
    render(rank("Ra", "Mid"));
    expect(screen.getByRole("link", { name: /Ymir/ })).toHaveAttribute("href", "#/god/Ymir");
    expect(screen.getByRole("link", { name: /Agni/ })).toHaveAttribute("href", "#/god/Agni");
  });

  /* Adjacent gods routinely sit within 0.005 of each other. "+0.00" would
   * assert a direction the printed figure doesn't show. */
  it("prints a vanishing gap unsigned", () => {
    const close: GodTierEntry[] = [
      { name: "Fenrir", ours: 0.534, community: 0.5, tier_ours: "S", tier_community: "S", role: "Jungle" },
      { name: "Ra", ours: 0.531, community: 0.5, tier_ours: "S", tier_community: "S", role: "Mid" },
    ];
    render(<GodRanking god="Ra" role="Mid" entries={close} modeLabel="Conquest" />);
    const above = screen.getByRole("link", { name: /Fenrir/ });
    expect(above).toHaveTextContent("0.00");
    expect(above.textContent).not.toMatch(/[+-]0\.00/);
  });

  it("says there is nothing above the top-rated god instead of leaving a blank", () => {
    render(rank("Ymir", "Solo"));
    expect(screen.getByText(/Ymir is the model’s top-rated god/i)).toBeInTheDocument();
  });

  it("gives overall, band and lane standing", () => {
    render(rank("Agni", "Mid"));
    const standing = screen.getByRole("heading", { level: 3, name: /standing/i }).parentElement!;
    expect(within(standing).getByText(/Overall/)).toBeInTheDocument();
    expect(within(standing).getByText(/In band A/)).toBeInTheDocument();
    expect(within(standing).getByText(/In Mid/)).toBeInTheDocument();
  });

  it("explains an unscored god as a coverage gap rather than a verdict", () => {
    render(<GodRanking god="Loki" role="Jungle" entries={entries} modeLabel="Joust" />);
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent(/Loki isn’t ranked in Joust/i);
    expect(screen.getByText(/coverage gap in the tier list, not a verdict/i)).toBeInTheDocument();
  });

  it("links onward to the full tier list", () => {
    render(rank("Ra", "Mid"));
    expect(screen.getByRole("link", { name: /every placement/i })).toHaveAttribute("href", "#/tiers");
  });
});
