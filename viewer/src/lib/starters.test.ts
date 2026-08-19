import { describe, it, expect } from "vitest";
import { groupStarters, starterPathLabel } from "./starters";
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

  it("never sums the two rates", () => {
    // A player who buys the base and upgrades it is counted in BOTH rates, so
    // adding them would report an opener held more often than it is.
    const [path] = groupStarters([s("Hunter's Cowl", 0.31), s("Leather Cowl", 0.16)], ITEMS);
    expect(path.lead.pick_rate).toBe(0.31);
    expect(path.base!.pick_rate + path.upgrade!.pick_rate).toBe(0.47); // what we do NOT show
  });

  it("orders paths by their own lead rate, not by whichever half came first", () => {
    const out = groupStarters(
      [s("Leather Cowl", 0.16), s("Sharpshooter's Arrow", 0.27), s("Hunter's Cowl", 0.31)],
      ITEMS);
    expect(out.map((p) => p.lead.name)).toEqual(["Hunter's Cowl", "Sharpshooter's Arrow"]);
  });

  it("keeps a lone upgrade whose base nobody held", () => {
    const [path] = groupStarters([s("Bluestone Brooch", 0.4)], ITEMS);
    expect(path.base).toBeUndefined();
    expect(path.upgrade?.name).toBe("Bluestone Brooch");
    expect(path.rootName).toBe("Bluestone Pendant");
    expect(starterPathLabel(path)).toBe("Bluestone Brooch");
  });

  it("keeps a lone base nobody upgraded", () => {
    const [path] = groupStarters([s("Leather Cowl", 0.4)], ITEMS);
    expect(path.upgrade).toBeUndefined();
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
    expect(out[0].lead.name).toBe("Mystery Trinket");
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
