import { describe, it, expect } from "vitest";
import { buildLedger, goldText, goldGap } from "./ledger";
import { applySwap } from "./builds";
import type { Item, SlotEntry } from "../types";

const item = (name: string, cost: number): Item => ({
  type: "item", name, tier: 3, cost, stats: {}, passive: "",
  builds_from: [], builds_into: [], source_url: "", last_verified: "",
} as Item);

const map = (...items: Item[]) => new Map(items.map((i) => [i.name, i]));
const plain = (...names: string[]) => applySwap(names, null);

describe("buildLedger — the gold spine", () => {
  it("accumulates cost down the build order", () => {
    const l = buildLedger({
      preview: plain("A", "B", "C"),
      itemsByName: map(item("A", 2650), item("B", 2650), item("C", 2700)),
    });
    expect(l.rows.map((r) => r.cumulative)).toEqual([2650, 5300, 8000]);
    expect(l.totalGold).toBe(8000);
    expect(l.slots).toBe(3);
  });

  it("returns a null total rather than a wrong one when a cost is unknown", () => {
    const l = buildLedger({
      preview: plain("A", "Unknown", "C"),
      itemsByName: map(item("A", 2650), item("C", 2700)),
    });
    // The hole poisons everything downstream — a running total that silently
    // skips an item would misstate the build's cost.
    expect(l.rows.map((r) => r.cumulative)).toEqual([2650, null, null]);
    expect(l.totalGold).toBeNull();
  });

  it("excludes a swapped-out slot from the spine and includes the swapped-in one", () => {
    const items = map(item("A", 1000), item("B", 2000), item("C", 3000), item("Swap", 500));
    const l = buildLedger({
      preview: applySwap(["A", "B", "C"], "Swap"),
      itemsByName: items,
    });
    const removed = l.rows.find((r) => r.status === "removed")!;
    expect(removed.name).toBe("C");
    expect(removed.cumulative).toBeNull();
    // A(1000) + B(2000) + Swap(500) — C's 3000 never spent.
    expect(l.totalGold).toBe(3500);
    expect(l.slots).toBe(3);
  });

  it("handles an empty build without dividing by nothing", () => {
    const l = buildLedger({ preview: [], itemsByName: map() });
    expect(l.rows).toEqual([]);
    expect(l.totalGold).toBeNull();
    expect(l.slots).toBe(0);
    expect(l.hasMeta).toBe(false);
  });
});

describe("buildLedger — joining the community order", () => {
  const items = map(
    item("Spear", 2650), item("Cosmic", 2650), item("Soul Gem", 2500),
    item("Thoth", 2300), item("Tahuti", 3000),
  );
  const community: SlotEntry[] = [
    { name: "Spear", pick_rate: 0.51, win_rate: 0.6 },
    { name: "Thoth", pick_rate: 0.24, win_rate: 0.6 },
    { name: "Soul Gem", pick_rate: 0.27, win_rate: 0.58 },
  ];

  it("marks each row with where the community buys it, and its rates", () => {
    const l = buildLedger({
      preview: plain("Spear", "Cosmic", "Soul Gem"),
      itemsByName: items,
      communityOrder: community,
    });
    const [spear, cosmic, soul] = l.rows;
    expect(spear.metaPosition).toBe(1);
    expect(spear.metaPickRate).toBe(0.51);
    expect(spear.inMeta).toBe(true);

    expect(cosmic.metaPosition).toBeNull();
    expect(cosmic.inMeta).toBe(false);
    expect(cosmic.metaPickRate).toBeNull();

    expect(soul.metaPosition).toBe(3);
  });

  it("surfaces what the community buys that the model never reaches", () => {
    const l = buildLedger({
      preview: plain("Spear", "Cosmic", "Soul Gem"),
      itemsByName: items,
      communityOrder: community,
    });
    expect(l.metaOnly.map((m) => m.name)).toEqual(["Thoth"]);
    const thoth = l.metaOnly[0];
    expect(thoth.position).toBe(2);
    expect(thoth.cumulative).toBe(4950);   // 2650 + 2300, the community's own spine
    expect(thoth.pickRate).toBe(0.24);
    expect(thoth.winRate).toBe(0.6);
  });

  it("does not count a swapped-out model item as still covering a meta pick", () => {
    const l = buildLedger({
      // Soul Gem gets swapped out, so the meta's Soul Gem is now unmatched.
      preview: applySwap(["Spear", "Cosmic", "Soul Gem"], "Tahuti"),
      itemsByName: items,
      communityOrder: community,
    });
    expect(l.metaOnly.map((m) => m.name)).toEqual(["Thoth", "Soul Gem"]);
  });

  it("counts the overlap between the two orders", () => {
    const l = buildLedger({
      preview: plain("Spear", "Cosmic", "Soul Gem"),
      itemsByName: items,
      communityOrder: community,
    });
    expect(l.shared).toBe(2);
    expect(l.slots).toBe(3);
    expect(l.metaSlots).toBe(3);
    expect(l.hasMeta).toBe(true);
  });

  it("computes the community's own cumulative gold, not the model's", () => {
    const l = buildLedger({
      preview: plain("Spear", "Cosmic", "Soul Gem"),
      itemsByName: items,
      communityOrder: community,
    });
    const soul = l.rows[2];
    // Model buys Soul Gem 3rd at 2650+2650+2500 = 7800.
    expect(soul.cumulative).toBe(7800);
    // Community buys it 3rd at 2650+2300+2500 = 7450.
    expect(soul.metaCumulative).toBe(7450);
    expect(goldGap(soul)).toBe(350);
  });

  it("reports no gap when only one side buys the item", () => {
    const l = buildLedger({
      preview: plain("Spear", "Cosmic"),
      itemsByName: items,
      communityOrder: community,
    });
    expect(goldGap(l.rows[1])).toBeNull();
  });

  it("has no meta to compare against when the community order is absent or empty", () => {
    for (const communityOrder of [undefined, []]) {
      const l = buildLedger({ preview: plain("Spear"), itemsByName: items, communityOrder });
      expect(l.hasMeta).toBe(false);
      expect(l.metaTotalGold).toBeNull();
      expect(l.shared).toBe(0);
      expect(l.rows[0].inMeta).toBe(false);
    }
  });

  it("accepts a plain-string community order (non-community entry shapes)", () => {
    const l = buildLedger({
      preview: plain("Spear"),
      itemsByName: items,
      communityOrder: ["Spear", "Thoth"],
    });
    expect(l.rows[0].inMeta).toBe(true);
    expect(l.rows[0].metaPosition).toBe(1);
    expect(l.rows[0].metaPickRate).toBeNull();
  });
});

describe("buildLedger — scores and flex", () => {
  it("attaches the score for each slot and flags flex slots", () => {
    const l = buildLedger({
      preview: plain("A", "B"),
      itemsByName: map(item("A", 100), item("B", 200)),
      scores: { A: { total: 0.59, efficiency: 0.41, win: 0.6, pick: 0.51, fit: 1 } },
      flexSlots: ["B"],
    });
    expect(l.rows[0].score?.total).toBe(0.59);
    expect(l.rows[0].isFlex).toBe(false);
    expect(l.rows[1].score).toBeUndefined();
    expect(l.rows[1].isFlex).toBe(true);
  });
});

describe("goldText", () => {
  it("separates thousands and handles absent values", () => {
    expect(goldText(16550)).toBe("16,550g");
    expect(goldText(0)).toBe("0g");
    expect(goldText(null)).toBe("—");
    expect(goldText(undefined)).toBe("—");
  });
});

describe("buildLedger — items the community buys as a slot alternate", () => {
  // Ratatoskr's real shape: Thistlethorn Acorn is the community's second
  // choice in two separate slots and the headline pick in none.
  const community: SlotEntry[] = [
    { name: "Ashwhorl", pick_rate: 0.32, win_rate: 0.53,
      alternates: [{ name: "Thistlethorn", pick_rate: 0.27, win_rate: 0.48 }] },
    { name: "Jotunn", pick_rate: 0.23, win_rate: 0.46,
      alternates: [{ name: "Thistlethorn", pick_rate: 0.17, win_rate: 0.72 },
                   { name: "Ashwhorl", pick_rate: 0.40, win_rate: 0.20 }] },
  ] as unknown as SlotEntry[];

  const ledger = () => buildLedger({
    preview: plain("Ashwhorl", "Thistlethorn", "Crusher"),
    itemsByName: map(item("Ashwhorl", 2000), item("Thistlethorn", 2000), item("Crusher", 2400)),
    communityOrder: community,
  });

  it("reports the rate for an item that only ever appears as an alternate", () => {
    // The row used to say "meta doesn't buy this" while the popular-items
    // panel on the same screen reported 27% pick for the same item.
    const row = ledger().rows.find((r) => r.name === "Thistlethorn")!;
    expect(row.metaPosition).toBeNull();        // genuinely has no slot position
    expect(row.metaAlternatePickRate).toBe(0.27);   // best of its sightings
    expect(row.metaAlternateWinRate).toBe(0.48);
  });

  it("keeps the slot pick authoritative over a richer alternate sighting", () => {
    const row = ledger().rows.find((r) => r.name === "Ashwhorl")!;
    expect(row.metaPosition).toBe(1);
    expect(row.metaPickRate).toBe(0.32);          // not the 0.40 alternate
    expect(row.metaAlternatePickRate).toBeNull();
  });

  it("still says nothing for an item the community genuinely never buys", () => {
    const row = ledger().rows.find((r) => r.name === "Crusher")!;
    expect(row.inMeta).toBe(false);
    expect(row.metaAlternatePickRate).toBeNull();
  });
});
