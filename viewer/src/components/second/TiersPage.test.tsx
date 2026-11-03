import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, within, waitFor } from "@testing-library/react";
import { TiersPage } from "./TiersPage";
import type { GodTierEntry, TierListData } from "../../types";

const g = (name: string, tier: GodTierEntry["tier_score"], win: number | null, matches: number | null, role = "Mid", share = 0.05): GodTierEntry =>
  ({ name, role, damage_type: "magical", tier_score: tier, score: tier ? win! - 0.03 : null, win_rate: win, matches, play_share: share });

const conquest = [
  g("Amaterasu", "S", 0.631, 843, "Solo", 0.06),
  g("Ra", "B", 0.53, 1286, "Mid", 0.09),
  g("Ymir", "C", 0.47, 2200, "Support", 0.12),
  g("Cupid", "S", 0.6, 300, "Carry", 0.01),
  g("Achilles", null, null, null, "Solo"),
  g("Hera", "A", 0.55, 900, "Mid", 0.07),
  g("Thor", "A", 0.54, 950, "Jungle", 0.08),
];
const unranked = conquest.map((e) => ({ ...e, tier_score: null, score: null, win_rate: null, matches: null }));
const tierlist = { gods: conquest, items: [],
  conquest: { gods: conquest, items: [], aspects: [] },
  joust: { gods: unranked, items: [], aspects: [] } } as unknown as TierListData;
const source = { division: "obsidian", window_start: "2026-10-20", window_end: "2026-11-02", matches_analyzed: 14484 };

const atUrl = (hash: string) => window.history.replaceState(null, "", `/${hash}`);
beforeEach(() => atUrl("#/tiers"));

describe("TiersPage — Conquest, ranked on real outcomes", () => {
  it("names itself and claims what it rests on, with live numbers", () => {
    render(<TiersPage tierlist={tierlist} communitySource={source} />);
    expect(screen.getByRole("heading", { level: 1, name: "Tiers" })).toBeInTheDocument();
    expect(screen.getByTestId("tiers-claim")).toHaveTextContent("6 of 7 gods placed on 6,479 Conquest god-games");
    expect(screen.getByTestId("tiers-provenance")).toHaveTextContent("14,484 Obsidian+ Conquest matches on SmiteBrain, 20 Oct–2 Nov");
  });

  it("groups gods under their band letter, best band first", () => {
    render(<TiersPage tierlist={tierlist} communitySource={source} />);
    const bands = screen.getAllByRole("heading", { level: 2 }).map((h) => h.textContent);
    expect(bands.slice(0, 4)).toEqual(["Tier S", "Tier A", "Tier B", "Tier C"]);
    expect(within(screen.getByTestId("band-S")).getByText("Amaterasu")).toBeInTheDocument();
  });

  it("shows win % and games on every placed row, and never a 0–1 score", () => {
    render(<TiersPage tierlist={tierlist} communitySource={source} />);
    const row = within(screen.getByTestId("band-S")).getByRole("link", { name: /Amaterasu/ });
    expect(row).toHaveTextContent("63%");
    expect(row).toHaveTextContent("843 games");
    expect(document.body.textContent).not.toMatch(/\b0\.\d{2,}/);
  });

  it("speaks the record in each row's accessible name and links to the god", () => {
    render(<TiersPage tierlist={tierlist} communitySource={source} />);
    const row = screen.getByRole("link", { name: /^Ra: tier B, 53% win rate over 1,286 games/ });
    expect(row).toHaveAttribute("href", "#/god/Ra");
  });

  it("keeps an unmeasured god out of the bands, in its own group", () => {
    render(<TiersPage tierlist={tierlist} communitySource={source} />);
    expect(within(screen.getByTestId("band-untiered")).getByText("Achilles")).toBeInTheDocument();
    expect(within(screen.getByTestId("band-C")).queryByText("Achilles")).not.toBeInTheDocument();
  });

  it("marks a god that wins well and is rarely played, in words", () => {
    render(<TiersPage tierlist={tierlist} communitySource={source} />);
    expect(screen.getByRole("link", { name: /Cupid.*rarely played/ })).toBeInTheDocument();
  });

  it("filters by lane from the link, and writes a lane back", async () => {
    atUrl("#/tiers?lane=Mid");
    render(<TiersPage tierlist={tierlist} communitySource={source} />);
    expect(screen.queryByText("Amaterasu")).not.toBeInTheDocument();
    expect(screen.getByText("Ra")).toBeInTheDocument();
    fireEvent.click(within(screen.getByRole("group", { name: "Filter by role" })).getByRole("button", { name: "Solo" }));
    await waitFor(() => expect(window.location.hash).toBe("#/tiers?lane=Solo"));
  });

  it("hands off to the working", () => {
    render(<TiersPage tierlist={tierlist} communitySource={source} />);
    expect(screen.getByTestId("method-seam")).toHaveAttribute("href", "#/method");
  });
});

describe("TiersPage — Joust and Arena are unranked", () => {
  it("refuses a tier in Joust and says why", () => {
    atUrl("#/tiers?mode=joust");
    render(<TiersPage tierlist={tierlist} communitySource={source} />);
    expect(screen.getByTestId("tiers-claim")).toHaveTextContent("Joust has no win data, so nothing here is ranked.");
    expect(screen.queryByTestId("band-S")).not.toBeInTheDocument();
    expect(screen.queryByText(/Tier [SABC]/)).not.toBeInTheDocument();
    expect(screen.queryByTestId("tiers-provenance")).not.toBeInTheDocument();
  });

  it("still lists every god A to Z, linking to its Joust build", () => {
    atUrl("#/tiers?mode=joust");
    render(<TiersPage tierlist={tierlist} communitySource={source} />);
    const list = within(screen.getByTestId("tiers-unranked"));
    const names = list.getAllByRole("link").map((a) => a.textContent);
    expect(names).toEqual([...names].sort((a, b) => a!.localeCompare(b!)));
    expect(list.getByRole("link", { name: "Ra" })).toHaveAttribute("href", "#/god/Ra?mode=joust");
  });

  it("treats Arena with no slice at all the same way, rather than borrowing Conquest", () => {
    atUrl("#/tiers?mode=arena");
    render(<TiersPage tierlist={tierlist} communitySource={source} />);
    expect(screen.getByTestId("tiers-claim")).toHaveTextContent(/Arena has no win data/);
    expect(screen.queryByTestId("band-S")).not.toBeInTheDocument();
  });
});
