import { describe, it, expect } from "vitest";
import { communityLines, communitySix, noAspectBuildLine } from "./communityBuild";
import type { SideBySideData } from "../SideBySide";

// Ullr's real file, 2026-11-09: the record's slot 6 is Blinking Abyss, a
// statless relic, and the cleaning rule fills it with The Crusher.
const ULLR = ["Transcendence", "Hydra's Lament", "Jotunn's Revenge", "Heartseeker", "Titan's Bane", "The Crusher"];
const file = (over: Partial<SideBySideData> = {}) => ({
  community: { items: ULLR },
  substitutions: [
    { slot: 6, dropped: "Blinking Abyss", class: "unscoreable", used: "The Crusher", position: 6 },
    // A dropped slot the record had nothing left for: not a refill.
    { slot: 5, dropped: "Evil Eye", class: "unfinished", used: null, position: null },
  ],
  ...over,
}) as unknown as SideBySideData;

describe("communitySix", () => {
  it("is the six the head-to-head measured, with the slots the cleaning rule refilled", () => {
    expect(communitySix({ comparison: file(), mode: "conquest" })).toEqual({
      items: ULLR, borrowedFrom: null, refilled: [{ dropped: "Blinking Abyss", used: "The Crusher" }] });
  });

  it("is nothing without a comparison file: the raw record is not six finished items", () => {
    expect(communitySix({ comparison: null, mode: "conquest" })).toBeNull();
    expect(communitySix({ comparison: file({ community: { items: [] } as never }), mode: "conquest" })).toBeNull();
  });

  it("is Conquest's six off Conquest, and says it is borrowed", () => {
    expect(communitySix({ comparison: file(), mode: "joust" })?.borrowedFrom).toBe("Conquest");
    expect(communitySix({ comparison: file(), mode: "arena" })?.items).toEqual(ULLR);
  });
});

describe("communityLines", () => {
  it("says what the six is and what the cleaning refilled", () => {
    expect(communityLines(communitySix({ comparison: file(), mode: "conquest" })!, "Ullr")).toEqual([
      "What Ullr's Conquest players buy most in each slot.",
      "Where the record's slot isn't a finished item, its next finished pick fills in: Blinking Abyss → The Crusher.",
    ]);
  });

  it("is one line when nothing was refilled", () => {
    expect(communityLines(communitySix({ comparison: file({ substitutions: [] }), mode: "joust" })!, "Ra"))
      .toEqual(["What Ra's Conquest players buy most in each slot."]);
  });
});

describe("noAspectBuildLine", () => {
  it("says there is no per-aspect build, and where the any-aspect one is", () => {
    expect(noAspectBuildLine("Thermotherapy", "Ra")).toBe(
      "There's no community build for Thermotherapy yet. Switch the aspect off to see what all Ra players buy, on any aspect.");
  });
});
