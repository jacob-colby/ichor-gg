import { describe, it, expect } from "vitest";
import { itemReason, answerWords } from "./itemReason";
import type { CommunityBuildEntry, Item } from "../../types";

const community = {
  source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null, source_url: "",
  slot_order: [
    { name: "Spear of Desolation", pick_rate: 0.55, win_rate: 0.54,
      alternates: [{ name: "Book of Thoth", pick_rate: 0.26, win_rate: 0.51 }] },
    { name: "The World Stone", pick_rate: 0.39, win_rate: 0.54 },
    { name: "Rod of Tahuti", pick_rate: 0.35, win_rate: 0.55 },
  ],
  popular_items: [{ name: "Evil Eye", pick_rate: 0.08, win_rate: 0.52 }],
} as CommunityBuildEntry;

const ctx = { god: "Ra", mode: "conquest" as const, community };

describe("itemReason", () => {
  it("quotes the community's own slot as a share of players", () => {
    expect(itemReason("Spear of Desolation", ctx)).toEqual(
      { tone: "community", text: "55% of Ra players buy it first" });
    expect(itemReason("Rod of Tahuti", ctx).text).toBe("35% of Ra players buy it third");
  });

  it("falls back to popularity anywhere in the record", () => {
    expect(itemReason("Book of Thoth", ctx).text).toBe("26% of Ra players build it");
    expect(itemReason("Evil Eye", ctx).text).toBe("8% of Ra players build it");
  });

  it("says plainly when the community doesn't buy it", () => {
    expect(itemReason("Lotus Sickle", ctx)).toEqual({ tone: "offmeta", text: "Ra's players don't buy this" });
  });

  it("adds the price bucket only when the pipeline calls it undervalued", () => {
    const item = { name: "Soul Gem", efficiency_tier: "undervalued" } as Item;
    expect(itemReason("Soul Gem", { ...ctx, item }).text)
      .toBe("Ra's players don't buy this · worth more than it costs");
    const fair = { name: "Soul Gem", efficiency_tier: "fair" } as Item;
    expect(itemReason("Soul Gem", { ...ctx, item: fair }).text).toBe("Ra's players don't buy this");
  });

  it("labels Conquest numbers as Conquest's in other modes", () => {
    expect(itemReason("Spear of Desolation", { ...ctx, mode: "joust" }).text)
      .toBe("In Conquest, 55% of Ra players buy it first");
    expect(itemReason("Lotus Sickle", { ...ctx, mode: "arena" }).text).toBe("In Conquest, Ra's players don't buy this");
  });

  it("never prints a 0-1 score", () => {
    for (const n of ["Spear of Desolation", "Book of Thoth", "Lotus Sickle"]) {
      expect(itemReason(n, ctx).text).not.toMatch(/0\.\d/);
    }
  });

  it("explains a draft swap by what it replaced and answers", () => {
    expect(itemReason("Divine Ruin", { ...ctx,
      swap: { removed: "Spear of the Magus", reason: "anti-heal, Magical Protection (already covered)" } }))
      .toEqual({ tone: "swap", text: "Swapped in for Spear of the Magus — brings anti-heal and magical protection" });
  });

  it("is empty rather than invented when nothing is known", () => {
    expect(itemReason("X", { god: "Ra", mode: "conquest" })).toEqual({ tone: "plain", text: "" });
  });
});

describe("answerWords", () => {
  it("drops channels with no positive answer and dedupes", () => {
    expect(answerWords("Penetration, penetration, less damage vs their build")).toBe("penetration");
    expect(answerWords(undefined)).toBe("");
  });
});
