import { describe, it, expect } from "vitest";
import { relativeDate } from "./relativeDate";

const now = new Date(2026, 6, 25); // 2026-07-25, local

describe("relativeDate", () => {
  it("says today for the same day", () => {
    expect(relativeDate("2026-07-25", now)).toBe("today");
  });

  it("says yesterday for one day back", () => {
    expect(relativeDate("2026-07-24", now)).toBe("yesterday");
  });

  it("counts days within the first week", () => {
    expect(relativeDate("2026-07-22", now)).toBe("3 days ago");
  });

  it("rolls up to weeks and months", () => {
    expect(relativeDate("2026-07-17", now)).toBe("last week");
    expect(relativeDate("2026-07-04", now)).toBe("3 weeks ago");
    expect(relativeDate("2026-05-20", now)).toBe("2 months ago");
  });

  it("falls back to the raw date for a future stamp (clock skew)", () => {
    expect(relativeDate("2026-08-01", now)).toBe("2026-08-01");
  });

  it("handles empty and malformed input without throwing", () => {
    expect(relativeDate("", now)).toBe("");
    expect(relativeDate("not-a-date", now)).toBe("not-a-date");
  });
});
