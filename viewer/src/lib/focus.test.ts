import { describe, it, expect } from "vitest";
import { diffSix, focusOptions, hybridEvidence, swapLead, FOCUS_ORDER, MAIN_LABEL } from "./focus";
import { dedupeIdenticalBuilds, orderBuilds } from "./builds";
import type { CuratedBuildEntry } from "../types";

const e = (archetype: string, slot_order: string[], extra: Partial<CuratedBuildEntry> = {}): CuratedBuildEntry =>
  ({ source: "suggested", archetype, slot_order, ...extra });
/** The shipped pipeline order, through the same dedupe `useDraftResult` uses. */
const strip = (entries: CuratedBuildEntry[]) => orderBuilds(dedupeIdenticalBuilds(entries)) as CuratedBuildEntry[];

// Ra, Conquest, base kit — the shipped notes at main eef19739.
const RA_CORE = ["Book of Thoth", "Spear of Desolation", "The World Stone", "Rod of Tahuti", "Obsidian Shard", "Soul Gem"];
const RA_MODEL = ["Spear of Desolation", "Spear of the Magus", "Rod of Tahuti", "Lotus Sickle", "Obsidian Shard", "Soul Gem"];
const RA_COOLDOWN = ["Chronos' Pendant", "Spear of Desolation", "Rod of Tahuti", "Lotus Sickle", "Obsidian Shard", "Soul Gem"];
const RA = strip([
  e("core", RA_CORE),
  e("mana-stack", ["Book of Thoth", "Spear of Desolation", "The World Stone", "Rod of Tahuti", "Obsidian Shard", "Lotus Sickle"]),
  e("burst", RA_CORE),
  e("bruiser", ["Kinetic Cuirass", "Spear of Desolation", "Rod of Tahuti", "Amanita Charm", "Obsidian Shard", "Soul Gem"]),
  e("anti-tank", RA_CORE),
  e("attack-speed", ["Bracer of The Abyss", "Spear of Desolation", "Bragi's Harp", "Rod of Tahuti", "Nimble Ring", "Obsidian Shard"]),
  e("cooldown", RA_COOLDOWN),
  e("model", RA_MODEL),
]);

describe("diffSix — pairs what leaves with what arrives, in buy order", () => {
  it("names Ra's cooldown swaps the way the brief does, against Balanced", () => {
    expect(diffSix(RA_CORE, RA_COOLDOWN)).toEqual([
      { removed: "Book of Thoth", added: "Chronos' Pendant" },
      { removed: "The World Stone", added: "Lotus Sickle" },
    ]);
  });
  it("is empty for the same six in any order", () => {
    expect(diffSix(RA_CORE, [...RA_CORE].reverse())).toEqual([]);
  });
  it("keeps an unpaired end when the builds differ in length", () => {
    expect(diffSix(["A", "B"], ["A", "B", "C"])).toEqual([{ removed: undefined, added: "C" }]);
  });
});

describe("focusOptions — one main six, every other build an adjustment of it", () => {
  const opts = focusOptions(RA);
  const by = (a: string) => opts.find((o) => o.archetype === a)!;

  it("puts the model's six first and calls it Ichor's six", () => {
    expect(opts[0]).toMatchObject({ archetype: "model", kind: "main", label: MAIN_LABEL, swaps: [] });
  });

  it("offers every focus, in a fixed order, even the ones that change nothing", () => {
    const focuses = opts.filter((o) => o.kind === "focus").map((o) => o.archetype);
    expect(focuses).toEqual(["cooldown", "attack-speed", "anti-tank", "bruiser", "burst", "mana-stack"]);
    // The order is FOCUS_ORDER's, not the note's (which leads with mana-stack).
    expect(focuses).toEqual(FOCUS_ORDER.filter((f) => focuses.includes(f)));
  });

  it("names every shipped focus in words, never its raw key", () => {
    expect(opts.map((o) => o.label)).toEqual(
      ["Ichor's six", "Cooldown", "Attack speed", "Anti-tank", "Bruiser", "Burst", "Mana-stack", "Balanced"]);
  });

  it("sets Balanced and Hybrid apart as answers, after the focuses", () => {
    expect(opts.at(-1)).toMatchObject({ archetype: "core", kind: "answer", label: "Balanced" });
  });

  it("measures every swap against the main six on screen", () => {
    expect(by("cooldown").swaps).toEqual([{ removed: "Spear of the Magus", added: "Chronos' Pendant" }]);
  });

  it("recovers a focus dedupe folded away, and says which build it is", () => {
    // anti-tank and burst ARE Balanced for Ra; the strip collapsed them.
    expect(RA.some((x) => x.archetype === "anti-tank")).toBe(false);
    expect(by("anti-tank")).toMatchObject({ sameAs: "Balanced", six: RA_CORE });
    expect(by("burst").sameAs).toBe("Balanced");
    expect(by("cooldown").sameAs).toBeNull();
  });

  it("drops an answer that is the main six — no chip that can never change anything", () => {
    // Joust and Arena: `core` equals `model` for 95 of 95 gods.
    const arena = focusOptions(strip([e("core", RA_MODEL), e("burst", RA_MODEL), e("model", RA_MODEL)]));
    expect(arena.map((o) => o.archetype)).toEqual(["model", "burst"]);
    expect(arena[1].sameAs).toBe(MAIN_LABEL);
  });

  it("keeps a flavor it doesn't know yet, after the known ones", () => {
    const opts2 = focusOptions(strip([e("model", RA_MODEL), e("cooldown", RA_COOLDOWN), e("lifesteal", RA_CORE)]));
    expect(opts2.map((o) => o.archetype)).toEqual(["model", "cooldown", "lifesteal"]);
  });

  it("falls back to core, then the first build, when a note has no model entry", () => {
    expect(focusOptions(strip([e("core", RA_CORE), e("cooldown", RA_COOLDOWN)]))[0].archetype).toBe("core");
    expect(focusOptions(strip([e("cooldown", RA_COOLDOWN)]))[0].archetype).toBe("cooldown");
    expect(focusOptions([])).toEqual([]);
  });

  it("says when a build is the same six bought in another order", () => {
    const o = focusOptions(strip([e("model", RA_MODEL), e("cooldown", [...RA_MODEL].reverse())]))[1];
    expect(o).toMatchObject({ swaps: [], reordered: true, sameAs: null });
  });
});

describe("swapLead — the line over the swaps reads at one swap and at five", () => {
  const opts = focusOptions(RA);
  const by = (a: string) => opts.find((o) => o.archetype === a)!;
  it("counts the swaps against the six", () => {
    expect(swapLead(by("cooldown"), "Ra", 6)).toBe("Swaps 1 of 6:");
    expect(swapLead(by("attack-speed"), "Ra", 6)).toBe(`Swaps ${by("attack-speed").swaps.length} of 6:`);
  });
  it("says the focus is another build rather than showing a duplicate", () => {
    expect(swapLead(by("burst"), "Ra", 6)).toBe("Same as Balanced for Ra. Swaps 2 of 6:");
    const arena = focusOptions(strip([e("model", RA_MODEL), e("burst", RA_MODEL)]));
    expect(swapLead(arena[1], "Ra", 6)).toBe(`Same as ${MAIN_LABEL} for Ra.`);
  });
  it("names the aspect as the thing doing the swapping", () => {
    expect(swapLead({ swaps: [{ removed: "A", added: "B" }], sameAs: null, reordered: false, six: [] }, "Ra", 6, "Thermotherapy"))
      .toBe("Thermotherapy swaps 1 of 6:");
  });
});

describe("hybridEvidence — the pipeline's reason, in words, or nothing", () => {
  const swap = { added: "Shell of Rebuke", removed: "Draconic Scale",
    reason: "community 71% win over 35 matches (vs 54% on this god), taking the model's weakest slot from Draconic Scale" };
  it("reads the record the swap fired on", () => {
    expect(hybridEvidence(swap, "Ares")).toBe("won 71% of 35 games with it (Ares wins 54%)");
    expect(hybridEvidence(swap, "Ares", "Conquest")).toBe("won 71% of 35 Conquest games with it (Ares wins 54%)");
  });
  it("drops a reason it cannot parse rather than paraphrasing it", () => {
    expect(hybridEvidence({ ...swap, reason: "something else" }, "Ares")).toBeNull();
    expect(hybridEvidence(undefined, "Ares")).toBeNull();
  });
});
