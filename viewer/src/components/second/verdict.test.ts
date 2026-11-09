import { describe, it, expect } from "vitest";
import { verdictSentence, verdictText, axisGap, listWords, type VerdictInput } from "./verdict";
import type { SideBySideData } from "../SideBySide";

const SIX = ["Lotus Sickle", "Spear of Desolation", "Spear of the Magus", "Rod of Tahuti", "Obsidian Shard", "Soul Gem"];

function file(over: Partial<SideBySideData> = {}, unsim: string[] = []): SideBySideData {
  const side = (items: string[], notSim: string[] = []) => ({
    items, gold: 0, mean_cooldown: null, ultimate_cooldown: null, crit_chance: 0, crit_multiplier: 0, crit_ev: 0,
    passives: items.map((item) => ({ item, status: notSim.includes(item) ? "not simulated" : "simulated", summary: "", assumptions: [] })),
    breakpoints: {},
    sustained_squishy: 0, sustained_tank: 0, burst_squishy: 0, burst_tank: 0, ehp_physical: 0, ehp_magical: 0,
  });
  return {
    god: "Ra", verdict: "community better", damage_axis: 0.9567, survival_axis: 1.0633,
    weighted_axes: [0.933, 1.0207],
    shared: [], ichor: side(SIX, unsim), community: side(["Book of Thoth"]), diffs: [], substitutions: [],
    coverage: { ichor: 0.86, community: 1, gap: 0.14, ok: true, reason: null },
    kit: { kit: "base", aspect: "Aspect of Thermotherapy", pick_rate: 0.04, win_rate: 0.59, simulated: true },
    ...over,
  } as SideBySideData;
}

const input = (d: SideBySideData | null, over: Partial<VerdictInput> = {}): VerdictInput =>
  ({ d, god: "Ra", mode: "conquest", archetype: "model", shownSix: SIX, ...over });

describe("verdictSentence", () => {
  it("says Ra's real result in player words, with the unsimulated item named", () => {
    const v = verdictSentence(input(file({}, ["Lotus Sickle"])));
    expect(v.kind).toBe("measured");
    expect(verdictText(v)).toBe(
      "The community's six deals 7% more damage; survival is about even. "
      + "Lotus Sickle isn't simulated yet, so the damage gap is partly unmeasured.");
  });

  it("reads the weighted axes when present, the raw ones otherwise", () => {
    const raw = verdictSentence(input(file({ weighted_axes: undefined })));
    // 0.9567 is inside the 5% band; 1.0633 is outside.
    expect(verdictText(raw)).toBe("Ichor's six survives 6% more; damage is about even.");
  });

  it("calls a split in Ichor's favour first", () => {
    const v = verdictSentence(input(file({ weighted_axes: [0.93, 1.08] })));
    expect(v.lead).toBe("split");
    expect(verdictText(v)).toBe("Ichor's six survives 8% more. The community's six deals 8% more damage.");
  });

  it("says both when one build wins on both axes", () => {
    const v = verdictSentence(input(file({ weighted_axes: [1.12, 1.09] })));
    expect(verdictText(v)).toBe("Ichor's six deals 12% more damage and survives 9% more.");
  });

  it("calls anything inside the band about even", () => {
    const v = verdictSentence(input(file({ weighted_axes: [1.04, 0.97] })));
    expect(v.lead).toBe("even");
    expect(verdictText(v)).toMatch(/about even on damage and on survival/);
  });

  it("honours a wider band from _meta.json", () => {
    const v = verdictSentence({ ...input(file({ weighted_axes: [1.08, 1] })), band: 0.1 });
    expect(v.lead).toBe("even");
  });

  it("withholds when coverage fails, whatever the axes say", () => {
    const v = verdictSentence(input(file({
      verdict: "not enough simulated",
      coverage: { ichor: 0.5, community: 1, gap: 0.5, ok: false, reason: "too much unsimulated" },
      weighted_axes: [1.3, 1.3],
    })));
    expect(v.kind).toBe("withheld");
    expect(verdictText(v)).toMatch(/isn't measured enough to call/);
    expect(verdictText(v)).not.toMatch(/%/);
  });

  it("withholds when coverage.ok is false even if the verdict string is a call", () => {
    const v = verdictSentence(input(file({
      verdict: "Ichor better", coverage: { ichor: 0.5, community: 1, gap: 0.5, ok: false, reason: null } })));
    expect(v.kind).toBe("withheld");
  });

  it("says the aspect isn't simulated when the community plays one", () => {
    const v = verdictSentence(input(file({ verdict: "aspect not simulated" })));
    expect(v.kind).toBe("withheld");
    expect(verdictText(v)).toMatch(/Most Ra players run Aspect of Thermotherapy.*can't simulate that aspect/);
  });

  it("does not quote a file that measured a different six", () => {
    const v = verdictSentence(input(file(), { shownSix: [...SIX.slice(0, 5), "Divine Ruin"] }));
    expect(v.kind).toBe("withheld");
  });

  it("has nothing to compare outside Conquest", () => {
    const v = verdictSentence(input(file(), { mode: "joust" }));
    expect(v.kind).toBe("none");
    expect(verdictText(v)).toMatch(/^Joust has no community build/);
  });

  it("speaks for the model six only", () => {
    expect(verdictSentence(input(file(), { archetype: "burst" })).kind).toBe("none");
  });

  it("says so when there is no file at all", () => {
    expect(verdictText(verdictSentence(input(null)))).toBe("There's no measured comparison for Ra yet.");
  });

  it("says the base-kit file doesn't cover an aspect build", () => {
    const v = verdictSentence(input(file(), { aspectBuild: "Aspect of Thermotherapy" }));
    expect(verdictText(v)).toMatch(/base kit/);
  });
});

describe("verdictSentence on the community's side", () => {
  it("reads the same measured sentence in Conquest: the measurement holds both sixes", () => {
    const ichor = verdictSentence(input(file({}, ["Lotus Sickle"])));
    const theirs = verdictSentence(input(file({}, ["Lotus Sickle"]), { side: "community" }));
    expect(verdictText(theirs)).toBe(verdictText(ichor));
  });

  it("says off Conquest whose record the borrowed six is, not that it is the model's", () => {
    const v = verdictSentence(input(file(), { mode: "arena", side: "community" }));
    expect(v.kind).toBe("none");
    expect(verdictText(v)).toBe("Arena has no community record of its own, so this is the six Ra's Conquest players buy.");
  });
});

describe("verdictSentence and the draft", () => {
  it("says the measurement predates the enemy team's swaps", () => {
    const v = verdictSentence({ ...input(file({ weighted_axes: [1.12, 1.09] })), draftSwaps: 1 });
    expect(v.tail).toBe("Measured before this team's swap.");
  });
});

describe("helpers", () => {
  it("quotes the winning side's own gap", () => {
    expect(axisGap(0.933)).toEqual({ who: "community", pct: 7 });
    expect(axisGap(1.0207)).toEqual({ who: "ichor", pct: 2 });
  });
  it("lists names in prose", () => {
    expect(listWords(["A"])).toBe("A");
    expect(listWords(["A", "B", "C"])).toBe("A, B and C");
  });
});
