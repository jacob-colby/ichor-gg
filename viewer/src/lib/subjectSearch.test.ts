import { describe, it, expect } from "vitest";
import { searchSubjects } from "./subjectSearch";
import type { God, Item } from "../types";

/* Bookmarks are the reader's own shortlist. They surface in the shell's search
 * two ways: as the whole list when nothing is typed, and as a mark plus a
 * tiebreak once something is. */
describe("searchSubjects — bookmarks", () => {
  const gods = [
    { name: "Ra", role: "Mid" }, { name: "Rama", role: "Carry" },
    { name: "Ratatoskr", role: "Jungle" }, { name: "Ymir", role: "Support" },
  ] as unknown as God[];
  const items = [{ name: "Rage", cost: 2450 }] as unknown as Item[];

  it("offers the saved gods when nothing is typed, in the order they were saved", () => {
    const hits = searchSubjects(gods, items, "", ["Ymir", "Ra"]);
    expect(hits.map((h) => h.name)).toEqual(["Ymir", "Ra"]);
    expect(hits.every((h) => h.bookmarked)).toBe(true);
  });

  it("still returns nothing for an empty query with no bookmarks", () => {
    expect(searchSubjects(gods, items, "", [])).toEqual([]);
  });

  it("ignores a bookmark for a god this index doesn't have", () => {
    expect(searchSubjects(gods, items, "", ["Nobody"])).toEqual([]);
  });

  it("marks a bookmarked god among typed results", () => {
    const hits = searchSubjects(gods, items, "ra", ["Ratatoskr"]);
    expect(hits.find((h) => h.name === "Ratatoskr")!.bookmarked).toBe(true);
    expect(hits.find((h) => h.name === "Rama")!.bookmarked).toBeFalsy();
  });

  it("breaks ties toward a bookmark but never outranks a better match", () => {
    // Rama and Ratatoskr are both prefix matches; the saved one leads.
    const tied = searchSubjects(gods, items, "rat", ["Ratatoskr"]);
    expect(tied[0].name).toBe("Ratatoskr");
    // "Ra" is exact, so it wins even though Ratatoskr is the saved one.
    const exact = searchSubjects(gods, items, "ra", ["Ratatoskr"]);
    expect(exact[0].name).toBe("Ra");
  });
});
