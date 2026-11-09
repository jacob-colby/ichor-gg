import { describe, it, expect } from "vitest";
import { groupStarters, starterPathLabel, starterShare } from "./starters";
import type { Item } from "../types";

const item = (name: string, tier: number, from: string[] = [], into: string[] = []): Item =>
  ({ name, tier, cost: 700, stats: {}, passive: "", builds_from: from, builds_into: into,
     effect_tags: [], efficiency_tier: null }) as unknown as Item;

const ITEMS: Record<string, Item> = Object.fromEntries([
  item("Leather Cowl", 1, [], ["Hunter's Cowl"]),
  item("Hunter's Cowl", 2, ["Leather Cowl"]),
  item("Gilded Arrow", 1, [], ["Sharpshooter's Arrow"]),
  item("Sharpshooter's Arrow", 2, ["Gilded Arrow"]),
  item("Bluestone Brooch", 2, ["Bluestone Pendant"]),
  item("Bluestone Pendant", 1, [], ["Bluestone Brooch"]),
  item("Sands Of Time", 1, [], ["Pendulum of the Ages"]),
  item("Pendulum of the Ages", 2, ["Sands Of Time"]),
  item("Conduit Gem", 1, [], ["Archmage's Gem"]),
  item("Archmage's Gem", 2, ["Conduit Gem"]),
].map((i) => [i.name, i]));

const s = (name: string, pick: number, win = 0.5) =>
  ({ name, pick_rate: pick, win_rate: win });

describe("groupStarters — an opener and its upgrade are one purchase", () => {
  it("folds both halves of a path into a single entry", () => {
    // Anhur's real row: Hunter's Cowl 31% and Leather Cowl 16% were two of his
    // three opener slots, describing one purchase at two moments.
    const out = groupStarters(
      [s("Hunter's Cowl", 0.31), s("Sharpshooter's Arrow", 0.27), s("Leather Cowl", 0.16)],
      ITEMS);
    expect(out).toHaveLength(2);
    const cowl = out.find((p) => p.rootName === "Leather Cowl")!;
    expect(cowl.base?.name).toBe("Leather Cowl");
    expect(cowl.upgrade?.name).toBe("Hunter's Cowl");
  });

  it("states a path's share as the sum of its two ends", () => {
    // SmiteBrain counts each player once, holding the base OR its upgrade —
    // a god's starter tiles sum to 98-103% of its matches on all 95 gods — so
    // the two rates are disjoint and the path is their total. This used to be
    // the larger end alone, which understated every path whose players split.
    const [path] = groupStarters([s("Hunter's Cowl", 0.31), s("Leather Cowl", 0.16)], ITEMS);
    expect(path.pick_rate).toBeCloseTo(0.47, 10);
  });

  it("reads Ra's opener as the 58% it is, not the 41% of its larger end", () => {
    // Ra's every sighting, 2026-11-08 (ob47). Sands of Time -> Pendulum of the
    // Ages is the path the pipeline stamps, at 0.58; Conduit Gem, the base of
    // the second path, is the 4th tile, so a top-3 read would also have shown
    // that path at 24%.
    const out = groupStarters([
      s("Pendulum of the Ages", 0.41, 0.53), s("Archmage's Gem", 0.24, 0.54),
      s("Sands Of Time", 0.17, 0.46), s("Conduit Gem", 0.15, 0.39),
      s("Selflessness", 0.01, 0.6), s("Hunter's Cowl", 0.007, 1.0), s("Leather Cowl", 0.005, 0.5),
    ], ITEMS);
    expect(out.map((p) => [p.rootName, Math.round(p.pick_rate * 100)])).toEqual([
      ["Sands Of Time", 58], ["Conduit Gem", 39], ["Leather Cowl", 1], ["Selflessness", 1],
    ]);
  });

  it("weights the path's win rate by each end's picks, as the pipeline does", () => {
    // Item by item a starter's win rate is survivorship — only a game that went
    // long or well reaches the upgrade — so neither end speaks for the path.
    const [path] = groupStarters([s("Pendulum of the Ages", 0.41, 0.53), s("Sands Of Time", 0.17, 0.46)], ITEMS);
    expect(path.win_rate).toBeCloseTo((0.41 * 0.53 + 0.17 * 0.46) / 0.58, 10);
    expect(path.win_rate).toBeCloseTo(0.5095, 4); // the stamp's own figure for Ra
  });

  it("ranks paths by their summed share, not by whichever end is held most", () => {
    // By the larger end the cowl leads (30% > 25%); summed, the arrow does
    // (45% > 35%). The order must match the pipeline's, or the row's first
    // chip and the stamped starter disagree about which path is #1.
    const out = groupStarters(
      [s("Hunter's Cowl", 0.30), s("Sharpshooter's Arrow", 0.25), s("Gilded Arrow", 0.20), s("Leather Cowl", 0.05)],
      ITEMS);
    expect(out.map((p) => p.rootName)).toEqual(["Gilded Arrow", "Leather Cowl"]);
  });

  it("does not double a share when the same tile arrives twice", () => {
    const [path] = groupStarters([s("Leather Cowl", 0.16), s("Leather Cowl", 0.16)], ITEMS);
    expect(path.pick_rate).toBe(0.16);
  });

  it("keeps a lone upgrade whose base nobody held", () => {
    const [path] = groupStarters([s("Bluestone Brooch", 0.4)], ITEMS);
    expect(path.base).toBeUndefined();
    expect(path.upgrade?.name).toBe("Bluestone Brooch");
    expect(path.rootName).toBe("Bluestone Pendant");
    expect(path.pick_rate).toBe(0.4);
    expect(starterPathLabel(path)).toBe("Bluestone Brooch");
  });

  it("keeps a lone base nobody upgraded", () => {
    const [path] = groupStarters([s("Leather Cowl", 0.4)], ITEMS);
    expect(path.upgrade).toBeUndefined();
    expect(path.pick_rate).toBe(0.4);
    expect(starterPathLabel(path)).toBe("Leather Cowl");
  });

  it("labels a full path with both ends", () => {
    const [path] = groupStarters([s("Hunter's Cowl", 0.31), s("Leather Cowl", 0.16)], ITEMS);
    expect(starterPathLabel(path)).toBe("Leather Cowl → Hunter's Cowl");
  });

  it("passes an unknown item through rather than dropping it", () => {
    // An opener the item index has never heard of is still a real sighting.
    const out = groupStarters([s("Mystery Trinket", 0.2)], {});
    expect(out).toHaveLength(1);
    expect(out[0].rootName).toBe("Mystery Trinket");
    expect(out[0].pick_rate).toBe(0.2);
  });

  it("terminates on a cyclic builds_from rather than hanging the render", () => {
    const cyclic: Record<string, Item> = Object.fromEntries([
      item("A", 1, ["B"]), item("B", 1, ["A"]),
    ].map((i) => [i.name, i]));
    expect(groupStarters([s("A", 0.3)], cyclic)).toHaveLength(1);
  });

  it("returns nothing for no sightings", () => {
    expect(groupStarters([], ITEMS)).toEqual([]);
  });
});

describe("starterShare — how many open with a build's starter", () => {
  const paths = groupStarters(
    [s("Pendulum of the Ages", 0.41), s("Sands Of Time", 0.17), s("Archmage's Gem", 0.24)], ITEMS);

  it("reads the pipeline's stamp when it carries the path's record", () => {
    // The stamp is summed over every sighting, so it wins over a regroup of
    // whatever subset this index carries.
    expect(starterShare({ base: "Sands Of Time", upgrade: "Pendulum of the Ages", basis: "community",
      pick_rate: 0.58, win_rate: 0.5095, matches: 240 }, [])).toBe(0.58);
  });

  it("sums the grouped record for a starter with no rate of its own", () => {
    // A build saved in the editor, or a role-table starter: a bare pair.
    expect(starterShare({ base: "Sands Of Time", upgrade: "Pendulum of the Ages" }, paths)).toBeCloseTo(0.58, 10);
  });

  it("is undefined when no player in the record opened that way", () => {
    expect(starterShare({ base: "Leather Cowl", upgrade: "Hunter's Cowl", basis: "rule" }, paths)).toBeUndefined();
  });

  it("is undefined with no starter", () => {
    expect(starterShare(undefined, paths)).toBeUndefined();
  });
});
