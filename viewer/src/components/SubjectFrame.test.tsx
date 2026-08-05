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
    expect(header).toHaveTextContent(/69\s*placed on real results/);
    expect(header).toHaveTextContent(/18\s*not measured/);
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
    const nav = within(screen.getByTestId("lens-tabs-strip"));
    for (const label of ["Board", "Gods", "Items", "Draft", "Patch Notes"]) {
      expect(nav.getByRole("link", { name: label })).toBeInTheDocument();
    }
  });

  it("marks the lens in view as the current page", () => {
    render(frame({ lens: "tiers" }));
    const nav = within(screen.getByTestId("lens-tabs-strip"));
    expect(nav.getByRole("link", { name: "Gods" })).toHaveAttribute("aria-current", "page");
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

  /* Short labels: the strip sits in the navbar with the god named directly
   * beneath it, so "Items for Ra" was restating the next line. */
  it("offers the four god lenses", () => {
    render(frame({ god: ra, godName: "Ra", lens: "builds" }));
    const nav = within(screen.getByTestId("lens-tabs-strip"));
    expect(nav.getByRole("link", { name: "Builds" })).toHaveAttribute("href", "#/god/Ra");
    expect(nav.getByRole("link", { name: "Kit" })).toHaveAttribute("href", "#/god/Ra/kit");
    expect(nav.getByRole("link", { name: "Items" })).toHaveAttribute("href", "#/god/Ra/items");
    expect(nav.getByRole("link", { name: "Ranking" })).toHaveAttribute("href", "#/god/Ra/ranking");
  });

  it("offers a way back to the whole roster", () => {
    render(frame({ god: ra, godName: "Ra" }));
    expect(screen.getByRole("link", { name: /All 87 gods/ })).toHaveAttribute("href", "#/");
  });
});

/* The verdict used to live inside the builds view, so it vanished the moment
 * you looked at the kit — even though it's the one fact that's true of the god
 * on every lens. In the frame it stays put.
 *
 * It also used to be a comparison: our score against the community's, plus a
 * verdict on the gap. That gap did not survive measurement, so what is left is
 * the record and the sample behind it. */
describe("SubjectFrame — the verdict", () => {
  const tierEntry: GodTierEntry = {
    name: "Ra", score: 0.47, win_rate: 0.52, matches: 380, play_share: 0.07, tier_score: "B",
  };

  it("states the tier, the raw rate and the sample it rests on", () => {
    render(frame({ god: ra, godName: "Ra", tierEntry }));
    const verdict = within(screen.getByTestId("god-verdict"));
    expect(verdict.getByText("B")).toBeInTheDocument();
    expect(verdict.getByText("52%")).toBeInTheDocument();
    expect(verdict.getByText("380")).toBeInTheDocument();
  });

  it("shows how often the god is actually picked", () => {
    render(frame({ god: ra, godName: "Ra", tierEntry }));
    expect(within(screen.getByTestId("god-verdict")).getByText("7%")).toBeInTheDocument();
  });

  it("says a god with no sample is unmeasured rather than leaving a blank", () => {
    render(frame({ god: ra, godName: "Ra", tierEntry: { name: "Ra", score: null, tier_score: null } }));
    expect(within(screen.getByTestId("god-verdict"))
      .getByText(/not enough tracked matches/i)).toBeInTheDocument();
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

/* Home has always told readers to "bookmark a god from its page", and there
 * was no control here to do it with — saving a god was only possible from the
 * roster grid. */
describe("SubjectFrame — bookmarking a god from its own page", () => {
  it("offers the bookmark beside the name", () => {
    render(frame({ god: ra, godName: "Ra" }));
    const btn = screen.getByRole("button", { name: /bookmark ra/i });
    expect(btn).toHaveAttribute("aria-pressed", "false");
    // Beside the name, not off in the action cluster: it marks the subject.
    expect(screen.getByRole("heading", { level: 1 }).parentElement).toContainElement(btn);
  });

  it("saves and unsaves, and says which it just did", () => {
    render(frame({ god: ra, godName: "Ra" }));
    fireEvent.click(screen.getByRole("button", { name: /bookmark ra/i }));
    const saved = screen.getByRole("button", { name: /remove ra from your bookmarks/i });
    expect(saved).toHaveAttribute("aria-pressed", "true");
    expect(JSON.parse(localStorage.getItem("smite:pinnedGods")!)).toContain("Ra");

    fireEvent.click(saved);
    expect(screen.getByRole("button", { name: /bookmark ra/i })).toHaveAttribute("aria-pressed", "false");
    expect(JSON.parse(localStorage.getItem("smite:pinnedGods")!)).not.toContain("Ra");
  });

  it("reads an existing bookmark on arrival", () => {
    localStorage.setItem("smite:pinnedGods", JSON.stringify(["Ra"]));
    render(frame({ god: ra, godName: "Ra" }));
    expect(screen.getByRole("button", { name: /remove ra from your bookmarks/i }))
      .toHaveAttribute("aria-pressed", "true");
  });
});
