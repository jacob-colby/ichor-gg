import React from "react";
import { describe, it, expect, beforeEach, vi } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { SubjectFrame } from "./SubjectFrame";
import type { God, GodTierEntry } from "../types";

const ra = { name: "Ra", pantheon: "Egyptian", role: "Mid", damage_type: "magical" } as unknown as God;

const roster = { total: 87, ranked: 69, unranked: 18 };

const frame = (props: Partial<React.ComponentProps<typeof SubjectFrame>> = {}) => (
  <SubjectFrame lens="board" roster={roster} modeLabel="Conquest" onPickGod={() => {}} {...props} />
);

beforeEach(() => { localStorage.clear(); window.location.hash = ""; });

describe("SubjectFrame — the roster is a first-class subject", () => {
  it("states what is in the index", () => {
    render(frame());
    const header = screen.getByTestId("subject-header");
    expect(header).toHaveTextContent(/All 87 gods/);
    expect(header).toHaveTextContent(/69\s*ranked against the meta/);
    expect(header).toHaveTextContent(/18\s*unranked/);
  });

  /* Inventory, not argument. The header used to carry the disputed count —
   * the same figure Home's claim makes 60px below, which spent the headline's
   * punchline before it landed. */
  it("leaves the argument to the page it sits above", () => {
    render(frame());
    const header = screen.getByTestId("subject-header");
    expect(header).not.toHaveTextContent(/disputed/i);
    expect(header).not.toHaveTextContent(/agreed/i);
  });

  /* The roster's page makes a stronger argument than a route label, so the
   * banner deliberately isn't a heading — Home keeps the h1. */
  it("does not take the h1 away from the page it sits above", () => {
    render(frame());
    expect(within(screen.getByTestId("subject-header")).queryByRole("heading")).not.toBeInTheDocument();
  });

  it("offers the five roster lenses", () => {
    render(frame());
    const nav = within(screen.getByRole("navigation", { name: /roster views/i }));
    for (const label of ["Board", "Tier list", "Items", "Draft", "Patch notes"]) {
      expect(nav.getByRole("link", { name: label })).toBeInTheDocument();
    }
  });

  it("marks the lens in view as the current page", () => {
    render(frame({ lens: "tiers" }));
    const nav = within(screen.getByRole("navigation", { name: /roster views/i }));
    expect(nav.getByRole("link", { name: "Tier list" })).toHaveAttribute("aria-current", "page");
    expect(nav.getByRole("link", { name: "Board" })).not.toHaveAttribute("aria-current");
  });

  it("opens the picker from the roster", () => {
    const onPickGod = vi.fn();
    render(frame({ onPickGod }));
    fireEvent.click(screen.getByRole("button", { name: /choose a god/i }));
    expect(onPickGod).toHaveBeenCalled();
  });
});

describe("SubjectFrame — a god is the subject", () => {
  it("gives the god the page's h1, on every lens", () => {
    render(frame({ god: ra, godName: "Ra", lens: "ranking" }));
    expect(screen.getByRole("heading", { level: 1, name: "Ra" })).toBeInTheDocument();
  });

  it("offers the four god lenses, named for the god", () => {
    render(frame({ god: ra, godName: "Ra", lens: "builds" }));
    const nav = within(screen.getByRole("navigation", { name: /Ra views/i }));
    expect(nav.getByRole("link", { name: "Builds" })).toHaveAttribute("href", "#/god/Ra");
    expect(nav.getByRole("link", { name: "Kit" })).toHaveAttribute("href", "#/god/Ra/kit");
    expect(nav.getByRole("link", { name: "Items for Ra" })).toHaveAttribute("href", "#/god/Ra/items");
    expect(nav.getByRole("link", { name: "Where Ra ranks" })).toHaveAttribute("href", "#/god/Ra/ranking");
  });

  it("offers a way back to the whole roster", () => {
    render(frame({ god: ra, godName: "Ra" }));
    expect(screen.getByRole("link", { name: /All 87 gods/ })).toHaveAttribute("href", "#/");
  });
});

/* The verdict used to live inside the builds view, so it vanished the moment
 * you looked at the kit — even though it's the one fact that's true of the god
 * on every lens. In the frame it stays put. */
describe("SubjectFrame — the verdict", () => {
  const tierEntry: GodTierEntry = {
    name: "Ra", ours: 0.47, community: 0.58, tier_ours: "C", tier_community: "A",
  };

  it("states both scores, both tiers, and which way they disagree", () => {
    render(frame({ god: ra, godName: "Ra", tierEntry }));
    const verdict = within(screen.getByTestId("god-verdict"));
    expect(verdict.getByText("0.47")).toBeInTheDocument();
    expect(verdict.getByText("0.58")).toBeInTheDocument();
    expect(verdict.getByText(/meta rates higher/i)).toBeInTheDocument();
    expect(verdict.getByText(/-0\.11/)).toBeInTheDocument();
  });

  it("says so the other way when the model rates a god above the meta", () => {
    render(frame({ god: ra, godName: "Ra", tierEntry: { ...tierEntry, ours: 0.62, tier_ours: "S" } }));
    expect(within(screen.getByTestId("god-verdict")).getByText(/we rank higher/i)).toBeInTheDocument();
  });

  it("names an unranked god as unranked rather than leaving a blank", () => {
    render(frame({ god: ra, godName: "Ra", tierEntry: { ...tierEntry, community: null, tier_community: null } }));
    const verdict = within(screen.getByTestId("god-verdict"));
    expect(verdict.getByText(/unranked/i)).toBeInTheDocument();
    expect(verdict.getByText(/no community rating for this god yet/i)).toBeInTheDocument();
  });

  it("shows it on a lens that isn't builds", () => {
    render(frame({ god: ra, godName: "Ra", lens: "kit", tierEntry }));
    expect(screen.getByTestId("god-verdict")).toBeInTheDocument();
  });

  it("omits the verdict entirely when there is no tier entry", () => {
    render(frame({ god: ra, godName: "Ra" }));
    expect(screen.queryByTestId("god-verdict")).not.toBeInTheDocument();
  });
});

/* The draft page adopts a URL draft over localStorage and persists it on
 * mount. A link carrying only this god would be a one-click way to wipe a
 * saved comp from every god page in the app, with no undo. */
describe("SubjectFrame — the draft hand-off", () => {
  const link = () => screen.getByRole("link", { name: /draft with Ra/i });

  it("seats the god with an empty board", () => {
    render(frame({ god: ra, godName: "Ra" }));
    expect(link()).toHaveAttribute("href", "#/draft?m=conquest&me=Ra");
  });

  it("keeps a comp already entered, rather than replacing it", () => {
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["Ymir", "Cupid", "", "", ""], enemies: ["Loki", "", "", "", ""],
    }));
    render(frame({ god: ra, godName: "Ra" }));
    expect(link()).toHaveAttribute("href", "#/draft?m=conquest&me=Ra&a=Ymir%2CCupid&e=Loki");
  });

  // SMITE forbids duplicates, so the god vacates whatever slot it held.
  it("moves the god out of a slot it already occupied", () => {
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["Ymir", "Ra", "", "", ""], enemies: ["Ra", "", "", "", ""],
    }));
    render(frame({ god: ra, godName: "Ra" }));
    expect(link()).toHaveAttribute("href", "#/draft?m=conquest&me=Ra&a=Ymir");
  });

  // Switching mode resizes both rows, so a Joust link would silently drop two
  // gods from a five-god Conquest comp.
  it("does not resize a saved comp to match the mode being viewed", () => {
    localStorage.setItem("smite:draft", JSON.stringify({
      mode: "conquest", allies: ["Ymir", "Cupid", "Loki", "Thor", "Odin"], enemies: ["", "", "", "", ""],
    }));
    render(frame({ god: ra, godName: "Ra", modeLabel: "Joust" }));
    const href = link().getAttribute("href")!;
    expect(href).toContain("m=conquest");
    expect(href).toContain("a=Ymir%2CCupid%2CLoki%2CThor");
  });

  it("takes the viewed mode when the board is empty", () => {
    render(frame({ god: ra, godName: "Ra", modeLabel: "Joust" }));
    expect(link()).toHaveAttribute("href", "#/draft?m=joust&me=Ra");
  });
});

/* The subject header sat at 27% of a phone screen — worse than the picker bar,
 * footer and tab bar it replaced. Tapping the portrait to change god costs no
 * width, which is what lets the one remaining button share the identity row. */
describe("SubjectFrame — changing god", () => {
  it("makes the portrait a labelled control, not decoration", () => {
    const onPickGod = vi.fn();
    render(frame({ god: ra, godName: "Ra", onPickGod }));
    const art = screen.getByRole("button", { name: /change god — currently Ra/i });
    fireEvent.click(art);
    expect(onPickGod).toHaveBeenCalled();
  });

  it("keeps an explicitly labelled control too, for where there's room", () => {
    const onPickGod = vi.fn();
    render(frame({ god: ra, godName: "Ra", onPickGod }));
    fireEvent.click(screen.getByRole("button", { name: "Change god" }));
    expect(onPickGod).toHaveBeenCalled();
  });

  it("names the roster control for what it does", () => {
    render(frame());
    expect(screen.getByRole("button", { name: /choose a god/i })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: /change god/i })).not.toBeInTheDocument();
  });
});
