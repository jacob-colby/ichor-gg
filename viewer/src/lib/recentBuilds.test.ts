import { describe, expect, it } from "vitest";
import { ago, filterBuilds, isFiltered, NO_ASPECT, NO_FILTERS, type RecentBuild } from "./recentBuilds";

const b = (o: Partial<RecentBuild>): RecentBuild => ({
  t: "2026-11-08T00:00:00Z", win: true, role: "Mid", master: false, aspect: "Aspect of Combustion",
  patch: "ob47", items: [], starter: null, relic: null, ...o,
});
const rows = [
  b({ role: "Mid", win: true, master: true }),
  b({ role: "Carry", win: false, aspect: null }),
  b({ role: "Mid", win: false, patch: "ob46" }),
];

describe("filterBuilds", () => {
  it("passes everything with no filters", () => {
    expect(filterBuilds(rows, NO_FILTERS)).toHaveLength(3);
    expect(isFiltered(NO_FILTERS)).toBe(false);
  });
  it("filters each field, and they combine", () => {
    expect(filterBuilds(rows, { ...NO_FILTERS, role: "Mid" })).toHaveLength(2);
    expect(filterBuilds(rows, { ...NO_FILTERS, result: "loss" })).toHaveLength(2);
    expect(filterBuilds(rows, { ...NO_FILTERS, result: "win" })).toHaveLength(1);
    expect(filterBuilds(rows, { ...NO_FILTERS, master: true })).toHaveLength(1);
    expect(filterBuilds(rows, { ...NO_FILTERS, patch: "ob46" })).toHaveLength(1);
    expect(filterBuilds(rows, { ...NO_FILTERS, aspect: NO_ASPECT })).toHaveLength(1);
    expect(filterBuilds(rows, { ...NO_FILTERS, aspect: "Aspect of Combustion" })).toHaveLength(2);
    expect(filterBuilds(rows, { ...NO_FILTERS, role: "Mid", result: "loss" })).toHaveLength(1);
  });
});

describe("ago", () => {
  const now = Date.parse("2026-11-09T12:00:00Z");
  it("reads in days", () => {
    expect(ago("2026-11-09T01:00:00Z", now)).toBe("today");
    expect(ago("2026-11-08T01:00:00Z", now)).toBe("yesterday");
    expect(ago("2026-11-04T01:00:00Z", now)).toBe("5d ago");
    expect(ago("2026-11-10T01:00:00Z", now)).toBe("just now");
  });
});
