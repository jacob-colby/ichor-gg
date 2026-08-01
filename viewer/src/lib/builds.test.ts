import { describe, it, expect } from "vitest";
import {
  orderBuilds,
  isCommunityEntry,
  slotItemName,
  iconSlug,
  applySwap,
  tabLabel,
} from "./builds";
import type { CommunityBuildEntry, CuratedBuildEntry } from "../types";

const communityEntry: CommunityBuildEntry = {
  source: "community",
  aspect: "Aspect of the Heroic Tutor",
  aspect_pick_rate: 0.09,
  aspect_win_rate: 0.45,
  slot_order: [{ name: "Transcendence", pick_rate: 0.6, win_rate: 0.49 }],
  source_url: "https://smitebrain.com/gods/chiron/",
};

const mineEntry: CuratedBuildEntry = {
  source: "mine",
  slot_order: ["Transcendence", "Devourer's Gauntlet"],
  situational_swaps: [
    { vs_tag: "physical_heavy", swap: "Qin's Sais over Deathbringer's crit slot" },
    { vs_tag: "heavy_cc", swap: "Magi's Cloak" },
  ],
  notes: "Default crit path",
};

describe("isCommunityEntry", () => {
  it("returns true for a community entry", () => {
    expect(isCommunityEntry(communityEntry)).toBe(true);
  });

  it("returns false for a mine/pro entry", () => {
    expect(isCommunityEntry(mineEntry)).toBe(false);
  });
});

describe("slotItemName", () => {
  it("returns the plain string for a curated (mine/pro) slot entry", () => {
    expect(slotItemName("Transcendence")).toBe("Transcendence");
  });

  it("returns the .name field for a community slot entry object", () => {
    expect(slotItemName({ name: "Transcendence", pick_rate: 0.6, win_rate: 0.49 })).toBe(
      "Transcendence",
    );
  });
});

describe("iconSlug", () => {
  it("lowercases, hyphenates spaces, and strips apostrophes — matching the Python pipeline's slug convention", () => {
    expect(iconSlug("Hou Yi")).toBe("hou-yi");
    expect(iconSlug("Jotunn's Revenge")).toBe("jotunns-revenge");
    expect(iconSlug("Transcendence")).toBe("transcendence");
  });
});

describe("applySwap", () => {
  it("replaces the last (lowest-scored) slot and marks the diff", () => {
    const out = applySwap(["A", "B", "C"], "X");
    expect(out).toEqual([
      { name: "A", status: "kept" },
      { name: "B", status: "kept" },
      { name: "C", status: "removed" },
      { name: "X", status: "added" },
    ]);
  });
  it("is a no-op when swapItem is null", () => {
    expect(applySwap(["A", "B"], null)).toEqual([
      { name: "A", status: "kept" },
      { name: "B", status: "kept" },
    ]);
  });
  it("adds to an empty build", () => {
    expect(applySwap([], "X")).toEqual([{ name: "X", status: "added" }]);
  });
});

describe("tabLabel", () => {
  it("labels a suggested entry with its display name", () => {
    expect(tabLabel({ source: "suggested", archetype: "crit", slot_order: [] } as any)).toBe("Crit");
    // The three headline builds read as answers, not as internal archetype keys.
    expect(tabLabel({ source: "suggested", archetype: "model", slot_order: [] } as any)).toBe("Model");
    expect(tabLabel({ source: "suggested", archetype: "hybrid", slot_order: [] } as any)).toBe("Hybrid");
    // `core` keeps its name in the data — three systems read it — but the
    // reader meets it as one option among several, not as "the" build.
    expect(tabLabel({ source: "suggested", archetype: "core", slot_order: [] } as any)).toBe("Balanced");
  });
  it("names community plainly and a mine build by its own name", () => {
    expect(tabLabel({ source: "community", slot_order: [] } as any)).toBe("Community");
    expect(tabLabel({ source: "mine", slot_order: [] } as any)).toBe("mine");
  });
  it("falls back to 'suggested' when a suggested entry has no archetype", () => {
    expect(tabLabel({ source: "suggested", slot_order: [] } as any)).toBe("suggested");
  });
  it("labels a mine entry by its name (falling back to 'mine')", () => {
    expect(tabLabel({ source: "mine", name: "My Crit", slot_order: [] } as any)).toBe("My Crit");
    expect(tabLabel({ source: "mine", slot_order: [] } as any)).toBe("mine");
  });
});

describe("applySwap flex targeting", () => {
  it("removes the flex slot, not the last, when flexSlots is given", () => {
    const out = applySwap(["A", "B", "C", "D"], "SwapIn", ["B"]);
    const removed = out.find((s) => s.status === "removed");
    const added = out.find((s) => s.status === "added");
    expect(removed?.name).toBe("B");
    expect(added?.name).toBe("SwapIn");
    expect(out.filter((s) => s.status === "kept").map((s) => s.name)).toEqual(["A", "C", "D"]);
    // Position is load-bearing: the ledger reads row order as purchase order,
    // so the swap sits where the slot it replaces sat, not at the end.
    expect(out.map((s) => s.name)).toEqual(["A", "B", "SwapIn", "C", "D"]);
  });
  it("falls back to the last slot when no flexSlots supplied", () => {
    const out = applySwap(["A", "B", "C"], "SwapIn");
    expect(out.find((s) => s.status === "removed")?.name).toBe("C");
  });
  it("falls back to last when flex slot is not in the build", () => {
    const out = applySwap(["A", "B", "C"], "SwapIn", ["Z"]);
    expect(out.find((s) => s.status === "removed")?.name).toBe("C");
  });
});

describe("orderBuilds", () => {
  const s = (archetype: string) => ({ source: "suggested", archetype, slot_order: [] }) as never;
  const community = { source: "community", slot_order: [] } as never;

  it("leads with the three builds that answer the same question", () => {
    const got = orderBuilds([s("core"), s("crit"), s("model"), s("hybrid")], community);
    expect(got.map(tabLabel)).toEqual(["Model", "Hybrid", "Community", "Balanced", "Crit"]);
  });

  it("keeps the incoming order among everything that isn't a headline", () => {
    const got = orderBuilds([s("bruiser"), s("crit"), s("core")], undefined);
    expect(got.map(tabLabel)).toEqual(["Bruiser", "Crit", "Balanced"]);
  });

  it("omits community when the god has none — every Joust build", () => {
    const got = orderBuilds([s("model"), s("core")], undefined);
    expect(got.map(tabLabel)).toEqual(["Model", "Balanced"]);
  });
});
