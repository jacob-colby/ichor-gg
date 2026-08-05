import { describe, it, expect } from "vitest";
import { buildStandingsBoard, rateText, matchesText, stepPercent } from "./standings";
import type { GodTierEntry } from "../types";

const god = (
  name: string,
  score: number | null,
  band: GodTierEntry["tier_score"],
  role = "Jungle",
  extra: Partial<GodTierEntry> = {},
): GodTierEntry => ({ name, score, tier_score: band, role, ...extra });

describe("buildStandingsBoard", () => {
  it("ranks by measured score, best first", () => {
    const board = buildStandingsBoard([
      god("Weak", 0.42, "C"), god("Strong", 0.58, "S"), god("Mid", 0.50, "B"),
    ]);
    expect(board.lanes[0].rows.map((r) => r.name)).toEqual(["Strong", "Mid", "Weak"]);
    expect(board.ranked).toBe(3);
  });

  it("leaves a god with no sample unplaced rather than last", () => {
    // "We didn't measure this" and "this is bad" are different facts. Joust
    // and Arena have no outcome data at all, so this is every god there.
    const board = buildStandingsBoard([god("Known", 0.55, "S"), god("Unknown", null, null)]);
    expect(board.ranked).toBe(1);
    expect(board.unmeasured).toBe(1);
    expect(board.lanes[0].rows.map((r) => r.name)).toEqual(["Known"]);
    expect(board.lanes[0].unmeasured).toBe(1);
  });

  it("sums APPEARANCES, not matches — ten gods play every match", () => {
    const board = buildStandingsBoard([
      god("A", 0.55, "S", "Jungle", { matches: 300 }),
      god("B", 0.50, "B", "Jungle", { matches: 700 }),
    ]);
    expect(board.appearances).toBe(1000);
  });

  it("flags a god that performs well and is rarely played", () => {
    // Top third by score AND bottom third by play share — both numbers the
    // community's own, neither of them ours.
    const entries = [
      god("Hidden", 0.60, "S", "Jungle", { play_share: 0.01 }),
      god("Popular", 0.59, "S", "Jungle", { play_share: 0.13 }),
      god("Third", 0.55, "A", "Jungle", { play_share: 0.11 }),
      god("Fine", 0.50, "B", "Jungle", { play_share: 0.07 }),
      god("Meh", 0.45, "C", "Jungle", { play_share: 0.09 }),
      god("Weak", 0.40, "C", "Jungle", { play_share: 0.02 }),
    ];
    const board = buildStandingsBoard(entries);
    const rows = Object.fromEntries(board.lanes[0].rows.map((r) => [r.name, r]));
    expect(rows.Hidden.underplayed).toBe(true);
    expect(rows.Popular.underplayed).toBe(false);   // strong but widely played
    expect(rows.Weak.underplayed).toBe(false);      // rare but not strong
    expect(board.underplayed).toBe(1);
  });

  it("flags nobody when the sample is too small for terciles to mean anything", () => {
    // A "bottom third" of four gods is one name, and the label would be noise.
    const board = buildStandingsBoard([
      god("A", 0.60, "S", "Jungle", { play_share: 0.01 }),
      god("B", 0.50, "B", "Jungle", { play_share: 0.13 }),
    ]);
    expect(board.underplayed).toBe(0);
  });

  it("flags nobody when everyone is played equally", () => {
    // With no spread the bottom-third cut lands on the same value as the top,
    // and a naive tercile test would flag the whole top third.
    const board = buildStandingsBoard(
      [0.60, 0.58, 0.55, 0.50, 0.45, 0.40].map((s, i) =>
        god("G" + i, s, "B", "Jungle", { play_share: 0.1 })),
    );
    expect(board.underplayed).toBe(0);
  });

  it("never flags a god whose play share is unknown", () => {
    // A missing number must not read as "rare".
    const board = buildStandingsBoard([
      god("NoShare", 0.60, "S", "Jungle", {}),
      god("Low", 0.59, "S", "Jungle", { play_share: 0.01 }),
      god("C", 0.55, "A", "Jungle", { play_share: 0.11 }),
      god("D", 0.50, "B", "Jungle", { play_share: 0.09 }),
      god("E", 0.45, "C", "Jungle", { play_share: 0.12 }),
      god("F", 0.40, "C", "Jungle", { play_share: 0.13 }),
      god("G", 0.38, "C", "Jungle", { play_share: 0.14 }),
    ]);
    const rows = Object.fromEntries(board.lanes[0].rows.map((r) => [r.name, r]));
    expect(rows.NoShare.underplayed).toBe(false);
    expect(rows.Low.underplayed).toBe(true);
  });

  it("returns an empty board rather than throwing on no data", () => {
    expect(buildStandingsBoard(undefined).lanes).toEqual([]);
    expect(buildStandingsBoard([]).ranked).toBe(0);
  });
});

describe("formatting", () => {
  it("renders rates and samples the way a scoreboard would", () => {
    expect(rateText(0.5236)).toBe("52%");
    expect(rateText(null)).toBe("—");
    expect(matchesText(670)).toBe("670");
    expect(matchesText(4952)).toBe("5.0k");
    expect(matchesText(null)).toBe("—");
  });

  it("centres a rung in its cell so a mark never straddles two tiers", () => {
    expect(stepPercent(0)).toBeCloseTo(12.5);
    expect(stepPercent(3)).toBeCloseTo(87.5);
  });
});
