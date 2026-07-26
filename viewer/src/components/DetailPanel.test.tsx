import React from "react";
import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { DetailPanel } from "./DetailPanel";
import { saveMine } from "../lib/mineStore";
import type { BuildNote, God, Item, DraftConfig } from "../types";

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
    expect((mineImages[1] as HTMLElement).style.visibility).not.toBe("hidden");
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

  it("shows the fun badge (and a dice tab marker) when a fun build's tab is active", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["X"], situational_swaps: [], rationale: "" },
      { source: "suggested", archetype: "fun-crit", fun: true, slot_order: ["Y"], situational_swaps: [], rationale: "" },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    // core tab active by default — no badge
    expect(screen.queryByText(/for fun/i)).not.toBeInTheDocument();
    const funTab = screen.getByRole("tab", { name: /fun-crit/i });
    expect(funTab).toHaveTextContent("🎲");
    fireEvent.click(funTab);
    expect(screen.getByText(/for fun/i)).toBeInTheDocument();
    expect(screen.getByText(/off-class/i)).toBeInTheDocument();
  });

  it("shows the why-this-item score breakdown in the tooltip for an item with slot_scores", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["Deathbringer"], situational_swaps: [],
        rationale: "",
        slot_scores: { Deathbringer: { total: 0.81, efficiency: 0.9, win: 0.55, pick: 0.4, fit: 0.7 } } },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    const trigger = screen.getByText("Deathbringer").closest('[tabindex="0"]')!;
    fireEvent.focus(trigger);
    expect(screen.getByText(/WHY THIS ITEM/i)).toBeInTheDocument();
    expect(screen.getByText("fit")).toBeInTheDocument();
    expect(screen.getByText("0.70")).toBeInTheDocument();
  });

  it("shows the community per-slot alternate item", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null, source_url: "u",
        slot_order: [{ name: "Transcendence", pick_rate: 0.6, win_rate: 0.5,
          alternates: [{ name: "Jotunn's Revenge", pick_rate: 0.11, win_rate: 0.71 }] }] },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    expect(screen.getByText(/or Jotunn's Revenge/i)).toBeInTheDocument();
  });

  it("shows 'off-meta' instead of a 0 pick bar when the pick signal is 0", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["Deathbringer"], situational_swaps: [],
        rationale: "",
        slot_scores: { Deathbringer: { total: 0.5, efficiency: 0.6, win: 0.5, pick: 0, fit: 0.7 } } },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    const trigger = screen.getByText("Deathbringer").closest('[tabindex="0"]')!;
    fireEvent.focus(trigger);
    expect(screen.getByText(/off-meta/i)).toBeInTheDocument();
  });

  it("does not render a why-this-item section when the entry has no slot_scores", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["Deathbringer"], situational_swaps: [], rationale: "" },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    const trigger = screen.getByText("Deathbringer").closest('[tabindex="0"]')!;
    fireEvent.focus(trigger);
    expect(screen.queryByText(/WHY THIS ITEM/i)).not.toBeInTheDocument();
  });

  it("marks suggested items missing from the community list as off-meta", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [
          { name: "A", pick_rate: 0.6, win_rate: 0.5 },
          { name: "B", pick_rate: 0.4, win_rate: 0.5 },
        ], source_url: "u" },
      { source: "suggested", archetype: "core", slot_order: ["B", "C"], situational_swaps: [], rationale: "" },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                        mode="Conquest" onModeChange={() => {}} />);
    fireEvent.click(screen.getByRole("tab", { name: /core/i }));
    const markers = screen.getAllByText("off-meta");
    expect(markers).toHaveLength(1);
    expect(screen.getByText("C").closest("div")).toHaveTextContent("off-meta");
    expect(screen.getByText("B").closest("div")).not.toHaveTextContent("off-meta");
  });

  it("does not mark fun builds or gods without community data as off-meta", () => {
    // fun build: off-class by design, marker would be noise
    const withCommunity = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [{ name: "A", pick_rate: 0.6, win_rate: 0.5 }], source_url: "u" },
      { source: "suggested", archetype: "fun-crit", fun: true, slot_order: ["Z"], situational_swaps: [], rationale: "" },
    ] }];
    const { unmount } = render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={withCommunity as any}
                        mode="Conquest" onModeChange={() => {}} />);
    fireEvent.click(screen.getByRole("tab", { name: /fun-crit/i }));
    expect(screen.queryByText("off-meta")).not.toBeInTheDocument();
    unmount();
    // no community entry at all: nothing to compare against, no marker
    const noCommunity = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["Z"], situational_swaps: [], rationale: "" },
    ] }];
    render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={noCommunity as any}
                        mode="Conquest" onModeChange={() => {}} />);
    expect(screen.queryByText("off-meta")).not.toBeInTheDocument();
  });
});

describe("DetailPanel — Draft tab", () => {
  beforeEach(() => localStorage.clear());

  const item = (name: string, tags: string[] = []): Item =>
    ({ name, tier: 3, cost: 2500, stats: {}, passive: "", builds_from: [], builds_into: [],
       effect_tags: tags, efficiency_tier: null } as unknown as Item);

  const ITEMS = [
    item("Alpha"), item("Beta"), item("Gamma"), item("Delta"), item("Epsilon"), item("Zeta"),
    item("AntiHeal", ["anti-heal"]),
  ];

  const SCORES: Record<string, number> = {
    Alpha: 0.6, Beta: 0.59, Gamma: 0.58, Delta: 0.57, Epsilon: 0.56, Zeta: 0.55, AntiHeal: 0.4,
  };
  // EnemyHealer needs its own god_item_scores entry too — the DraftBar's god
  // picker is limited to gods present in god_item_scores (the ones with a
  // derivable core), same as production.
  const GOD_ITEM_SCORES = { TestGod: SCORES, EnemyHealer: { Alpha: 0.5 } };

  // Exaggerated weights vs. production _weights.yaml — the point of this
  // fixture is a deterministic, clearly-visible promotion, not realism.
  const DRAFT_CFG: DraftConfig = {
    max_bonus: 0.5,
    per_share: 0.5,
    tag_bonus: { healers: { "anti-heal": 1 } },
    stat_bonus: {},
    ally_covered: -0.5,
    ally_gap: 0.5,
  };

  const testGod: God = {
    type: "god", name: "TestGod", pantheon: "Test", role: "Carry", specializations: [],
    damage_type: "physical", release_date: "", base_stats: {}, abilities: [], aspects: [],
    source_url: "", last_verified: "",
  } as unknown as God;

  const healerGod: God = {
    type: "god", name: "EnemyHealer", pantheon: "Test", role: "Support", specializations: ["Healing"],
    damage_type: "magical", release_date: "", base_stats: {}, abilities: [], aspects: [],
    source_url: "", last_verified: "",
  } as unknown as God;

  const testGodBuild: BuildNote = {
    type: "smite-build", god: "TestGod", mode: "Conquest",
    builds: [
      { source: "suggested", archetype: "core",
        slot_order: ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"],
        situational_swaps: [], rationale: "test core" } as any,
    ],
  };

  function renderDraftPanel() {
    return render(
      <DetailPanel
        god="TestGod"
        godData={testGod}
        items={ITEMS}
        builds={[testGodBuild]}
        mode="Conquest"
        onModeChange={() => {}}
        allGods={[testGod, healerGod]}
        godItemScores={GOD_ITEM_SCORES}
        draftConfig={DRAFT_CFG}
      />,
    );
  }

  it("shows a Draft tab when god_item_scores + draft config are present", () => {
    renderDraftPanel();
    expect(screen.getByRole("tab", { name: /draft/i })).toBeInTheDocument();
  });

  it("shows a friendly hint instead of a bogus build when the draft is empty", () => {
    renderDraftPanel();
    fireEvent.click(screen.getByRole("tab", { name: /draft/i }));
    expect(screen.getByText(/enter.*draft/i)).toBeInTheDocument();
    expect(screen.queryByText("AntiHeal")).not.toBeInTheDocument();
  });

  it("renders the comp-adapted 6-item core with a promoted item's reason once a threat is entered", () => {
    renderDraftPanel();
    fireEvent.click(screen.getByRole("tab", { name: /draft/i }));

    // Enter one enemy healer via the DraftBar mounted above the tabs.
    fireEvent.click(screen.getByLabelText("Add enemy 1"));
    fireEvent.click(screen.getByText("EnemyHealer"));

    // AntiHeal (base 0.40) should now outscore the lowest base item (Zeta,
    // 0.55) once the healer bonus (clamped to max_bonus 0.5) is applied.
    expect(screen.getByText("AntiHeal")).toBeInTheDocument();
    expect(screen.getByText(/anti-heal/i)).toBeInTheDocument();
    // Still exactly a 6-item core.
    expect(screen.getAllByText(/^(Alpha|Beta|Gamma|Delta|Epsilon|Zeta|AntiHeal)$/)).toHaveLength(6);
  });

  it("does not reset the Draft tab selection when the mode toggle changes (composes on top of it)", () => {
    const joustBuild: BuildNote = {
      type: "smite-build", god: "TestGod", mode: "Joust",
      builds: [
        { source: "suggested", archetype: "core",
          slot_order: ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"],
          situational_swaps: [], rationale: "test core" } as any,
      ],
    };
    function Harness() {
      const [mode, setMode] = React.useState("Conquest");
      return (
        <DetailPanel
          god="TestGod" godData={testGod} items={ITEMS} builds={[testGodBuild, joustBuild]}
          mode={mode} onModeChange={setMode}
          allGods={[testGod, healerGod]} godItemScores={GOD_ITEM_SCORES} draftConfig={DRAFT_CFG}
        />
      );
    }
    render(<Harness />);
    fireEvent.click(screen.getByRole("tab", { name: /draft/i }));
    expect(screen.getByRole("tab", { name: /draft/i })).toHaveAttribute("aria-selected", "true");
    fireEvent.click(screen.getByRole("button", { name: /joust/i }));
    expect(screen.getByRole("tab", { name: /draft/i })).toHaveAttribute("aria-selected", "true");
  });

  it("hides the Draft tab when god_item_scores/draft are absent (older index)", () => {
    render(
      <DetailPanel god="TestGod" godData={testGod} items={ITEMS} builds={[testGodBuild]}
                   mode="Conquest" onModeChange={() => {}} />,
    );
    expect(screen.queryByRole("tab", { name: /draft/i })).not.toBeInTheDocument();
  });
});
