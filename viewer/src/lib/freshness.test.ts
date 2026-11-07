import { describe, it, expect } from "vitest";
import { freshness, shortPatch } from "./freshness";
import { shortAge } from "./relativeDate";

const now = new Date(2026, 10, 7); // 2026-11-07, local

describe("shortPatch", () => {
  it("abbreviates an Open Beta label the way players write it", () => {
    expect(shortPatch("Open Beta 47")).toBe("OB47");
    expect(shortPatch("open beta 9")).toBe("OB9");
  });

  it("leaves any other label alone rather than guessing an abbreviation", () => {
    expect(shortPatch("1.0")).toBe("1.0");
    expect(shortPatch("Closed Alpha 3")).toBe("Closed Alpha 3");
  });
});

describe("shortAge", () => {
  it("says today, then days, weeks and months", () => {
    expect(shortAge("2026-11-07", now)).toBe("today");
    expect(shortAge("2026-11-06", now)).toBe("1d");
    expect(shortAge("2026-10-25", now)).toBe("13d");
    expect(shortAge("2026-10-24", now)).toBe("2w");
    expect(shortAge("2026-09-01", now)).toBe("2mo");
  });

  it("drops the age for a future or unreadable stamp instead of printing a wrong one", () => {
    expect(shortAge("2026-11-09", now)).toBeNull();
    expect(shortAge("not-a-date", now)).toBeNull();
    expect(shortAge("", now)).toBeNull();
  });
});

describe("freshness", () => {
  it("gives the bar a compact stamp and keeps the whole sentence", () => {
    expect(freshness("2026-11-06", "Open Beta 47", now)).toEqual({
      short: "OB47 · 1d",
      full: "Updated yesterday · Open Beta 47",
      title: "Updated yesterday (2026-11-06) · Open Beta 47",
    });
  });

  it("says Updated in the short form when there is no patch to lead with", () => {
    expect(freshness("2026-11-06", undefined, now)).toEqual({
      short: "Updated 1d",
      full: "Updated yesterday",
      title: "Updated yesterday (2026-11-06)",
    });
  });

  it("keeps the patch and drops the age for a future stamp", () => {
    const f = freshness("2026-11-09", "Open Beta 47", now)!;
    expect(f.short).toBe("OB47");
    expect(f.title).toBe("Updated 2026-11-09 · Open Beta 47");
  });

  it("is null without a data_updated date", () => {
    expect(freshness(undefined, "Open Beta 47", now)).toBeNull();
    expect(freshness("", "Open Beta 47", now)).toBeNull();
  });
});
