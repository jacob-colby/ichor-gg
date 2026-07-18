import { describe, it, expect } from "vitest";
import {
  isCommunityEntry,
  slotItemName,
  iconSlug,
  matchingSwapIndex,
  applySwap,
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

describe("matchingSwapIndex", () => {
  it("returns the index of the swap whose vs_tag matches the selected chip", () => {
    expect(matchingSwapIndex(mineEntry.situational_swaps!, "heavy_cc")).toBe(1);
  });

  it("returns -1 when no swap matches the selected chip", () => {
    expect(matchingSwapIndex(mineEntry.situational_swaps!, "poke")).toBe(-1);
  });

  it("returns -1 when no chip is selected", () => {
    expect(matchingSwapIndex(mineEntry.situational_swaps!, null)).toBe(-1);
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
