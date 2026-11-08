import { describe, it, expect } from "vitest";
import raw from "../../public/index.json?raw";
import { mostPicked, transferFlags, TRANSFER_NOTE, fallbackNote } from "./mostPicked";
import type { CommunityBuildEntry, IndexData, Item } from "../types";

// Ra's Conquest record as shipped at main eef19739.
const RA: CommunityBuildEntry = {
  source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null, source_url: "",
  slot_order: [
    { name: "Spear of Desolation", pick_rate: 0.56, win_rate: 0.5,
      alternates: [{ name: "Book of Thoth", pick_rate: 0.18, win_rate: 0.42 }, { name: "Ancient Signet", pick_rate: 0.08, win_rate: 0.46 }] },
    { name: "The World Stone", pick_rate: 0.31, win_rate: 0.55,
      alternates: [{ name: "Spear of Desolation", pick_rate: 0.21, win_rate: 0.5 }, { name: "Book of Thoth", pick_rate: 0.14, win_rate: 0.42 }] },
    { name: "Rod of Tahuti", pick_rate: 0.3, win_rate: 0.57,
      alternates: [{ name: "Nimble Ring", pick_rate: 0.17, win_rate: 0.58 }, { name: "The World Stone", pick_rate: 0.11, win_rate: 0.55 }] },
    { name: "Nimble Ring", pick_rate: 0.2, win_rate: 0.58,
      alternates: [{ name: "Rod of Tahuti", pick_rate: 0.38, win_rate: 0.57 }, { name: "Obsidian Shard", pick_rate: 0.15, win_rate: 0.58 }] },
    { name: "Obsidian Shard", pick_rate: 0.24, win_rate: 0.58,
      alternates: [{ name: "Nimble Ring", pick_rate: 0.15, win_rate: 0.58 }, { name: "Rod of Tahuti", pick_rate: 0.1, win_rate: 0.57 }] },
    { name: "Blinking Abyss", pick_rate: 0.13, win_rate: 0.5,
      alternates: [{ name: "Obsidian Shard", pick_rate: 0.09, win_rate: 0.58 }, { name: "Void Shard", pick_rate: 0.08, win_rate: 0.41 }] },
  ],
};

const tagged = (name: string, effect_tags: string[]) => ({ name, effect_tags }) as unknown as Item;
const ITEMS: Record<string, Item> = {
  "Book of Thoth": tagged("Book of Thoth", ["stacking"]),
  "Blinking Abyss": tagged("Blinking Abyss", ["mobility"]),
  "Soul Locket": tagged("Soul Locket", ["stacking", "mobility"]),
  "Eye of Providence": tagged("Eye of Providence", ["ward-economy"]),
};

describe("mostPicked — ranked by each item's share at its commonest slot", () => {
  const list = mostPicked(RA);
  it("lists every item the record names, once", () => {
    expect(list).toHaveLength(9);
    expect(new Set(list.map((p) => p.name)).size).toBe(9);
  });
  it("ranks Rod of Tahuti on its 38% in slot four, not its 30% in slot three", () => {
    expect(list.slice(0, 3).map((p) => [p.name, p.pickRate, p.slot])).toEqual([
      ["Spear of Desolation", 0.56, 0], ["Rod of Tahuti", 0.38, 3], ["The World Stone", 0.31, 1],
    ]);
  });
  it("never sums an item's slots — the record can't say whether those players overlap", () => {
    expect(list.find((p) => p.name === "Book of Thoth")!.pickRate).toBe(0.18);
  });
  it("agrees with the pipeline's popular_items order on the shipped record", () => {
    expect(list.map((p) => p.name)).toEqual(["Spear of Desolation", "Rod of Tahuti", "The World Stone",
      "Obsidian Shard", "Nimble Ring", "Book of Thoth", "Blinking Abyss", "Ancient Signet", "Void Shard"]);
  });
  it("is empty without a record", () => {
    expect(mostPicked(undefined)).toEqual([]);
  });
});

describe("transferFlags — what Conquest's record doesn't describe in this mode", () => {
  const names = ["Book of Thoth", "Blinking Abyss", "Soul Locket", "Eye of Providence", "Rod of Tahuti"];
  const JOUST = { from: "Conquest", reject_tags: ["mobility"] };
  const ARENA = { from: "Conquest", reject_tags: ["stacking", "mobility"], excluded_items: ["Eye of Providence", "Eye of Erebus"] };

  it("marks nothing without a rule — Conquest, or an index that predates the export", () => {
    expect(transferFlags(names, "Conquest", undefined, ITEMS)).toEqual([]);
  });
  it("Joust: rotation items only — stacking is deliberately NOT rejected there", () => {
    const f = transferFlags(names, "Joust", JOUST, ITEMS);
    expect(f.map((x) => [x.reason, x.items])).toEqual([["mobility", ["Blinking Abyss", "Soul Locket"]]]);
    expect(f[0].note).toBe(TRANSFER_NOTE.Joust.mobility);
  });
  it("Arena: the ward items first, then each rejected tag, an item under every tag it carries", () => {
    const f = transferFlags(names, "Arena", ARENA, ITEMS);
    expect(f.map((x) => [x.reason, x.items])).toEqual([
      ["excluded", ["Eye of Providence"]],
      ["stacking", ["Book of Thoth", "Soul Locket"]],
      ["mobility", ["Blinking Abyss", "Soul Locket"]],
    ]);
  });
  it("still says something true about a tag it has no sentence for", () => {
    const f = transferFlags(["Eye of Providence"], "Arena", { reject_tags: ["ward-economy"] }, ITEMS);
    expect(f[0].note).toBe(fallbackNote("Arena", "Conquest"));
  });
});

describe("the shipped index — every rule it exports has its own sentence", () => {
  // Reads the committed index, so a reject tag added in _weights.yaml without
  // words here fails rather than falling through to the generic note.
  const index = JSON.parse(raw) as IndexData;
  it("exports Joust and Arena, and names a reason for each tag", () => {
    const t = index.community_transfer ?? {};
    expect(Object.keys(t).sort()).toEqual(["Arena", "Joust"]);
    for (const [mode, rule] of Object.entries(t)) {
      for (const tag of rule.reject_tags ?? []) expect(TRANSFER_NOTE[mode]?.[tag], `${mode}/${tag}`).toBeTruthy();
      if (rule.excluded_items?.length) expect(TRANSFER_NOTE[mode]?.excluded, `${mode}/excluded`).toBeTruthy();
    }
  });
  it("finds those tags on the shipped items, where `_tags.yaml` put them", () => {
    const count = (tag: string) => index.items.filter((i) => (i.effect_tags ?? []).includes(tag)).length;
    expect(count("stacking")).toBeGreaterThan(0);
    expect(count("mobility")).toBeGreaterThan(0);
  });
});
