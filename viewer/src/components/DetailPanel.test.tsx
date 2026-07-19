import React from "react";
import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { DetailPanel } from "./DetailPanel";
import { saveMine } from "../lib/mineStore";
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
  ],
};

describe("DetailPanel", () => {
  beforeEach(() => localStorage.clear());

  it("renders one tab per available source (community from note, mine from store)", () => {
    saveMine("Chiron", "Conquest", { name: "mine", slot_order: ["Transcendence"] });
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={[chironBuild]} mode="Conquest" onModeChange={() => {}} />);
    expect(screen.getByRole("tab", { name: /community/i })).toBeInTheDocument();
    expect(screen.getByRole("tab", { name: /mine/i })).toBeInTheDocument();
    expect(screen.queryByRole("tab", { name: /^pro$/i })).not.toBeInTheDocument();
  });

  it("shows the community tab's slot order with pick/win badges by default", () => {
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={[chironBuild]} mode="Conquest" onModeChange={() => {}} />);
    expect(screen.getByText("Transcendence")).toBeInTheDocument();
    expect(screen.getByText(/60%.*49%/)).toBeInTheDocument();
  });

  it("hides the swap column for the community tab (no situational_swaps)", () => {
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={[chironBuild]} mode="Conquest" onModeChange={() => {}} />);
    expect(screen.queryByText(/situational/i)).not.toBeInTheDocument();
  });

  it("switching to a stored mine tab shows plain item names with no pick/win badge", () => {
    saveMine("Chiron", "Conquest", { name: "mine", slot_order: ["Transcendence", "Devourer's Gauntlet"] });
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={[chironBuild]} mode="Conquest" onModeChange={() => {}} />);
    fireEvent.click(screen.getByRole("tab", { name: /mine/i }));
    expect(screen.getByText("Devourer's Gauntlet")).toBeInTheDocument();
    expect(screen.queryByText(/%.*%/)).not.toBeInTheDocument();
  });

  it("shows a fallback message when the god has no build note for this mode yet", () => {
    render(<DetailPanel god="SomeNewGod" godData={undefined} items={[]} builds={[]} mode="Conquest" onModeChange={() => {}} />);
    expect(screen.getByText(/no build data yet/i)).toBeInTheDocument();
  });

  it("reflows the build when a matchup chip is clicked", () => {
    const builds = [{
      type: "smite-build", god: "Chiron", mode: "Conquest",
      builds: [{
        source: "suggested", archetype: "core",
        slot_order: ["A", "B", "C"],
        situational_swaps: [{ vs_tag: "heavy_cc", swap: "Cloak — cc", swap_item: "Cloak" }],
        rationale: "x",
      }],
    }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any} mode="Conquest" onModeChange={() => {}} />);
    fireEvent.click(screen.getByRole("button", { name: /heavy cc/i }));
    expect(screen.getByText("Cloak")).toBeInTheDocument();      // added item shows
    expect(screen.getByText("C")).toHaveClass("line-through");  // removed slot struck
  });

  it("renders the rationale for a suggested build entry", () => {
    const suggestedBuild: BuildNote = {
      type: "smite-build",
      god: "Chiron",
      mode: "Conquest",
      builds: [
        {
          source: "suggested",
          archetype: "core",
          slot_order: ["Deathbringer"],
          situational_swaps: [{ vs_tag: "sustain", swap: "none — anti-heal" }],
          rationale: "Top weighted-score core.",
        },
      ],
    };
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={[suggestedBuild]} mode="Conquest" onModeChange={() => {}} />);
    expect(screen.getByRole("tab", { name: /core/i })).toBeInTheDocument();
    expect(screen.getByText(/Top weighted-score core/)).toBeInTheDocument();
  });

  // Regression coverage for a real bug found in manual browser verification
  // (Task 7): the slot-order row was keyed by index alone (`key={i}`), so
  // switching tabs — which can put a *different* item at the same slot
  // position — let React reuse the same <img> DOM node across tabs. The
  // onError handler sets `visibility: hidden` imperatively on that node with
  // nothing to undo it, so if the item that used to sit at that index had a
  // broken icon, a *working* icon that later lands at the same index stayed
  // invisible even though it loaded fine. Keying by `${name}-${i}` forces a
  // fresh <img> node whenever the item at that position changes.
  it("does not carry a stale hidden icon over to a different item that lands at the same slot index on tab switch", () => {
    const build: BuildNote = {
      type: "smite-build",
      god: "Chiron",
      mode: "Conquest",
      builds: [
        {
          source: "community",
          aspect: "Aspect of the Heroic Tutor",
          aspect_pick_rate: 0.09,
          aspect_win_rate: 0.45,
          slot_order: [
            { name: "Transcendence", pick_rate: 0.6, win_rate: 0.49 },
            { name: "BrokenIcon", pick_rate: 0.1, win_rate: 0.2 },
          ],
          source_url: "https://smitebrain.com/gods/chiron/",
        },
      ],
    };
    saveMine("Chiron", "Conquest", { name: "mine", slot_order: ["Transcendence", "Deathbringer"] });

    const { container } = render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={[build]} mode="Conquest" onModeChange={() => {}} />);

    // Simulate the second slot's icon (BrokenIcon) failing to load on the
    // community tab. Scope to slot icons (alt="") so the god headshot in the
    // header (alt={god}) doesn't offset the indices. The first error retries
    // once (cache-bust); the retry also failing is what hides the icon.
    const communityImages = container.querySelectorAll('img[alt=""]');
    fireEvent.error(communityImages[1]); // retry
    fireEvent.error(communityImages[1]); // retry failed -> hide
    expect(communityImages[1]).toHaveStyle({ visibility: "hidden" });

    // Switch to the "mine" tab, where the same slot index (1) now holds
    // Deathbringer instead.
    fireEvent.click(screen.getByRole("tab", { name: /mine/i }));

    const mineImages = container.querySelectorAll('img[alt=""]');
    expect(mineImages[1]).toHaveAttribute("src", expect.stringContaining("deathbringer"));
    // Must be a fresh node with no leftover inline visibility — not the
    // reused, still-hidden node from the community tab.
    expect(mineImages[1].style.visibility).not.toBe("hidden");
  });

  // Regression coverage for a real bug: the "Reload data" button re-fetches
  // index.json, producing a brand-new object graph for the *same* god. If
  // activeIndex isn't reset on that change, two silent-bug modes are possible:
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
        { source: "suggested", archetype: "crit", slot_order: ["Crit Path Item"], situational_swaps: [], rationale: "crit" },
        { source: "suggested", archetype: "burst", slot_order: ["Ability Path Item"], situational_swaps: [], rationale: "burst" },
      ] as any,
    };
  }

  it("resets to tab 0 (no stale/inconsistent selection) when the current god's entries shrink on reload", () => {
    const { rerender } = render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={[makeThreeEntryBuild()]} mode="Conquest" onModeChange={() => {}} />);

    // Select the second "mine" tab (index 2 — the "ability path" entry).
    fireEvent.click(screen.getAllByRole("tab")[2]);
    expect(screen.getByText("Ability Path Item")).toBeInTheDocument();

    // Simulate "Reload data": same god, but the ability-path entry is gone
    // and every object is a fresh reference (as a real re-fetch produces).
    const reloaded = makeThreeEntryBuild();
    reloaded.builds = reloaded.builds.slice(0, 2); // community + crit path only
    rerender(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={[reloaded]} mode="Conquest" onModeChange={() => {}} />);

    const tabsAfter = screen.getAllByRole("tab");
    expect(tabsAfter).toHaveLength(2);
    expect(tabsAfter[0]).toHaveAttribute("aria-selected", "true");
    expect(tabsAfter[1]).toHaveAttribute("aria-selected", "false");
    expect(screen.getByText("Transcendence")).toBeInTheDocument();
    expect(screen.queryByText("Ability Path Item")).not.toBeInTheDocument();
  });

  it("resets to tab 0 (not a stale index pointing at a different entry) when entries reorder on reload", () => {
    const { rerender } = render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={[makeThreeEntryBuild()]} mode="Conquest" onModeChange={() => {}} />);

    // Select the second "mine" tab (index 2 — the "ability path" entry).
    fireEvent.click(screen.getAllByRole("tab")[2]);
    expect(screen.getByText("Ability Path Item")).toBeInTheDocument();

    // Simulate "Reload data": same god, same entry count, but the two
    // "mine" entries have swapped position — index 2 is now the crit path,
    // not the ability path the user had selected.
    const reordered = makeThreeEntryBuild();
    const [community, mineA, mineB] = reordered.builds;
    reordered.builds = [community, mineB, mineA];
    rerender(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={[reordered]} mode="Conquest" onModeChange={() => {}} />);

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

  it("switches build set when the mode toggle changes", () => {
    const builds = [
      { type: "smite-build", god: "Chiron", mode: "Conquest",
        builds: [{ source: "suggested", archetype: "core", slot_order: ["ConItem"], situational_swaps: [], rationale: "c" }] },
      { type: "smite-build", god: "Chiron", mode: "Joust",
        builds: [{ source: "suggested", archetype: "core", slot_order: ["JoustItem"], situational_swaps: [], rationale: "j" }] },
    ];
    function Harness() {
      const [mode, setMode] = React.useState("Conquest");
      return <DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                          mode={mode} onModeChange={setMode} />;
    }
    render(<Harness />);
    expect(screen.getByText("ConItem")).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /joust/i }));
    expect(screen.getByText("JoustItem")).toBeInTheDocument();
  });

  it("renders the starter line for a build that has one", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [],
        rationale: "", starter: { base: "Gilded Arrow", upgrade: "Sharpshooter's Arrow" } },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    expect(screen.getByText(/STARTER/i)).toBeInTheDocument();
    expect(screen.getByText("Gilded Arrow")).toBeInTheDocument();
    expect(screen.getByText("Sharpshooter's Arrow")).toBeInTheDocument();
  });

  it("shows the starter line on a community build too", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [{ name: "X", pick_rate: 0.5, win_rate: 0.5 }], source_url: "u",
        starter: { base: "Gilded Arrow", upgrade: "Sharpshooter's Arrow" } },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    expect(screen.getByText(/STARTER/i)).toBeInTheDocument();
    expect(screen.getByText("Gilded Arrow")).toBeInTheDocument();
  });

  it("passes flex_slots so a swap removes the flex slot, not the last", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A", "B", "C"], flex_slots: ["A"],
        situational_swaps: [{ vs_tag: "heavy_cc", swap: "Cloak — cc", swap_item: "Cloak" }], rationale: "x" },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    fireEvent.click(screen.getByRole("button", { name: /heavy cc/i }));
    expect(screen.getByText("A")).toHaveClass("line-through");   // flex slot removed
    expect(screen.getByText("C")).not.toHaveClass("line-through");
  });

  it("shows a stored mine build as a tab (suggested still active by default)", () => {
    saveMine("Chiron", "Conquest", { name: "My New", slot_order: ["Rage"] });
    const note: BuildNote = { type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["Deathbringer"], situational_swaps: [], rationale: "" } as any,
    ] };
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={[note]}
                        mode="Conquest" onModeChange={() => {}} />);
    expect(screen.getByRole("tab", { name: /My New/i })).toBeInTheDocument();
    expect(screen.getByText(/BUILD ORDER/i)).toBeInTheDocument();  // suggested tab active
  });

  const godWithAspect = {
    type: "god", name: "Hercules", pantheon: "Roman", role: "Solo", specializations: [],
    damage_type: "physical", release_date: "", base_stats: {}, abilities: [],
    aspects: [{ name: "Aspect of Preservation", kit_changes: "Becomes an ally-heal tank." }],
    source_url: "", last_verified: "",
  } as any;

  function aspectBuild(): BuildNote {
    return { type: "smite-build", god: "Hercules", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [{ name: "X", pick_rate: 0.5, win_rate: 0.5 }], source_url: "u" } as any,
      { source: "suggested", archetype: "core", slot_order: ["BaseItem"], situational_swaps: [], rationale: "" } as any,
      { source: "suggested", archetype: "core", slot_order: ["AspectItem"], situational_swaps: [], rationale: "",
        aspect: "Aspect of Preservation" } as any,
    ] };
  }

  it("shows the Aspect toggle and swaps to the aspect build + kit banner when on", () => {
    render(<DetailPanel god="Hercules" godData={godWithAspect} items={[]} builds={[aspectBuild()]}
                        mode="Conquest" onModeChange={() => {}} />);
    // select the core tab; base build shows, aspect build hidden
    fireEvent.click(screen.getByRole("tab", { name: /core/i }));
    expect(screen.getByText("BaseItem")).toBeInTheDocument();
    expect(screen.queryByText("AspectItem")).not.toBeInTheDocument();
    // turn the aspect on — same core tab, now the aspect build + kit banner
    fireEvent.click(screen.getByRole("button", { name: /aspect/i }));
    expect(screen.getByText("AspectItem")).toBeInTheDocument();
    expect(screen.queryByText("BaseItem")).not.toBeInTheDocument();
    expect(screen.getByText(/ally-heal tank/i)).toBeInTheDocument();
    expect(screen.getByRole("tab", { name: /community/i })).toBeInTheDocument();
  });

  it("shows no Aspect toggle for a god with no aspect builds", () => {
    const builds = [{ type: "smite-build", god: "Susano", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "" },
    ] }];
    render(<DetailPanel god="Susano" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    expect(screen.queryByRole("button", { name: /^aspect/i })).not.toBeInTheDocument();
  });

  it("labels suggested tabs by archetype", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["X"], situational_swaps: [], rationale: "" },
      { source: "suggested", archetype: "crit", slot_order: ["Y"], situational_swaps: [], rationale: "" },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    expect(screen.getByRole("tab", { name: /crit/i })).toBeInTheDocument();
  });
});
