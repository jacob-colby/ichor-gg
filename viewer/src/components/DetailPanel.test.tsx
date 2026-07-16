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

  // Regression coverage for a real bug: Chiron's actual build note has two
  // "mine" entries, and the "Reload data" button re-fetches index.json,
  // producing a brand-new object graph for the *same* god. If activeIndex
  // isn't reset on that change, two silent-bug modes are possible:
  //   1. entries shrink -> activeIndex points past the end -> no tab shows
  //      aria-selected, but content silently falls back to entries[0].
  //   2. entries reorder (same count) -> activeIndex is still "valid" but
  //      now names a different entry -> the tab bar looks unchanged while
  //      the displayed build silently switches to something else.
  // Both must instead land cleanly back on tab 0 with matching content.
  function makeThreeEntryBuild(): BuildNote {
    return {
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
          slot_order: ["Crit Path Item"],
          situational_swaps: [{ vs_tag: "heavy_cc", swap: "Crit path swap" }],
          notes: "Crit path",
        },
        {
          source: "mine",
          slot_order: ["Ability Path Item"],
          situational_swaps: [{ vs_tag: "heavy_cc", swap: "Ability path swap" }],
          notes: "Ability path",
        },
      ],
    };
  }

  it("resets to tab 0 (no stale/inconsistent selection) when the current god's entries shrink on reload", () => {
    const { rerender } = render(<DetailPanel god="Chiron" builds={[makeThreeEntryBuild()]} />);

    // Select the second "mine" tab (index 2 — the "ability path" entry).
    fireEvent.click(screen.getAllByRole("tab")[2]);
    expect(screen.getByText("Ability Path Item")).toBeInTheDocument();

    // Simulate "Reload data": same god, but the ability-path entry is gone
    // and every object is a fresh reference (as a real re-fetch produces).
    const reloaded = makeThreeEntryBuild();
    reloaded.builds = reloaded.builds.slice(0, 2); // community + crit path only
    rerender(<DetailPanel god="Chiron" builds={[reloaded]} />);

    const tabsAfter = screen.getAllByRole("tab");
    expect(tabsAfter).toHaveLength(2);
    expect(tabsAfter[0]).toHaveAttribute("aria-selected", "true");
    expect(tabsAfter[1]).toHaveAttribute("aria-selected", "false");
    expect(screen.getByText("Transcendence")).toBeInTheDocument();
    expect(screen.queryByText("Ability Path Item")).not.toBeInTheDocument();
  });

  it("resets to tab 0 (not a stale index pointing at a different entry) when entries reorder on reload", () => {
    const { rerender } = render(<DetailPanel god="Chiron" builds={[makeThreeEntryBuild()]} />);

    // Select the second "mine" tab (index 2 — the "ability path" entry).
    fireEvent.click(screen.getAllByRole("tab")[2]);
    expect(screen.getByText("Ability Path Item")).toBeInTheDocument();

    // Simulate "Reload data": same god, same entry count, but the two
    // "mine" entries have swapped position — index 2 is now the crit path,
    // not the ability path the user had selected.
    const reordered = makeThreeEntryBuild();
    const [community, mineA, mineB] = reordered.builds;
    reordered.builds = [community, mineB, mineA];
    rerender(<DetailPanel god="Chiron" builds={[reordered]} />);

    const tabsAfter = screen.getAllByRole("tab");
    expect(tabsAfter).toHaveLength(3);
    expect(tabsAfter[0]).toHaveAttribute("aria-selected", "true");
    expect(tabsAfter[2]).toHaveAttribute("aria-selected", "false");
    // Must show the community entry (post-reset), never silently the
    // crit-path entry that now happens to sit at the old index.
    expect(screen.getByText("Transcendence")).toBeInTheDocument();
    expect(screen.queryByText("Crit Path Item")).not.toBeInTheDocument();
    expect(screen.queryByText("Ability Path Item")).not.toBeInTheDocument();
  });
});
