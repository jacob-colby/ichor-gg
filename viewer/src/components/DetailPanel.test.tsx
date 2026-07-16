import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { DetailPanel } from "./DetailPanel";
import type { BuildNote } from "../types";

const chironBuild: BuildNote = {
  type: "smite-build",
  god: "Chiron",
  mode: "Conquest",
  builds: [
    {
      source: "community",
      aspect: "Aspect of the Heroic Tutor",
      aspect_pick_rate: 0.09,
      aspect_win_rate: 0.45,
      slot_order: [{ name: "Transcendence", pick_rate: 0.6, win_rate: 0.49 }],
      source_url: "https://smitebrain.com/gods/chiron/",
    },
    {
      source: "mine",
      slot_order: ["Transcendence", "Devourer's Gauntlet"],
      situational_swaps: [
        { vs_tag: "physical_heavy", swap: "Qin's Sais over Deathbringer's crit slot" },
        { vs_tag: "heavy_cc", swap: "Magi's Cloak" },
      ],
      notes: "Default crit path",
    },
  ],
};

describe("DetailPanel", () => {
  it("renders one tab per available source", () => {
    render(<DetailPanel god="Chiron" builds={[chironBuild]} />);
    expect(screen.getByRole("tab", { name: /community/i })).toBeInTheDocument();
    expect(screen.getByRole("tab", { name: /mine/i })).toBeInTheDocument();
    expect(screen.queryByRole("tab", { name: /^pro$/i })).not.toBeInTheDocument();
  });

  it("shows the community tab's slot order with pick/win badges by default", () => {
    render(<DetailPanel god="Chiron" builds={[chironBuild]} />);
    expect(screen.getByText("Transcendence")).toBeInTheDocument();
    expect(screen.getByText(/60%.*49%/)).toBeInTheDocument();
  });

  it("hides the swap column for the community tab (no situational_swaps)", () => {
    render(<DetailPanel god="Chiron" builds={[chironBuild]} />);
    expect(screen.queryByText(/situational/i)).not.toBeInTheDocument();
  });

  it("switching to the mine tab shows plain item names with no pick/win badge, plus the swap column", () => {
    render(<DetailPanel god="Chiron" builds={[chironBuild]} />);
    fireEvent.click(screen.getByRole("tab", { name: /mine/i }));
    expect(screen.getByText("Devourer's Gauntlet")).toBeInTheDocument();
    expect(screen.queryByText(/%.*%/)).not.toBeInTheDocument();
    expect(screen.getByText(/situational/i)).toBeInTheDocument();
    expect(screen.getByText(/Qin's Sais over Deathbringer's crit slot/)).toBeInTheDocument();
  });

  it("clicking an archetype chip highlights the matching swap row", () => {
    render(<DetailPanel god="Chiron" builds={[chironBuild]} />);
    fireEvent.click(screen.getByRole("tab", { name: /mine/i }));
    fireEvent.click(screen.getByRole("button", { name: /heavy cc/i }));
    // Note: the swap text ("Magi's Cloak", "Qin's Sais over...") sits as a
    // trailing text node after a <span> tag label inside the row div, not in
    // its own element — a regex match lands on the row div itself (the only
    // element whose full text content contains the substring), so
    // `.closest("[data-highlighted]")` matches the element itself. An exact
    // string match here would find nothing, since no single element's full
    // text content equals just the swap text.
    expect(screen.getByText(/Magi's Cloak/).closest("[data-highlighted]")).toHaveAttribute(
      "data-highlighted",
      "true",
    );
    expect(
      screen.getByText(/Qin's Sais over Deathbringer's crit slot/).closest("[data-highlighted]"),
    ).toHaveAttribute("data-highlighted", "false");
  });

  it("shows a fallback message when the god has no build note for this mode yet", () => {
    render(<DetailPanel god="SomeNewGod" builds={[]} />);
    expect(screen.getByText(/no build data yet/i)).toBeInTheDocument();
  });
});
