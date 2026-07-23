import { describe, it, expect } from "vitest";
import { filterGods, sortGods } from "./godFilters";
import type { God } from "../types";

const gods = [
  { name: "Ymir", pantheon: "Norse", role: "Solo", damage_type: "magical" },
  { name: "Ra", pantheon: "Egyptian", role: "Mid", damage_type: "magical" },
  { name: "Chiron", pantheon: "Greek", role: "Carry", damage_type: "physical" },
] as unknown as God[];

describe("godFilters", () => {
  it("filters by search, pantheon, role, damage type", () => {
    expect(filterGods(gods, { q: "ra" }).map((g) => g.name)).toEqual(["Ra"]);
    expect(filterGods(gods, { role: "Mid" }).map((g) => g.name)).toEqual(["Ra"]);
    expect(filterGods(gods, { pantheon: "Norse" }).map((g) => g.name)).toEqual(["Ymir"]);
    expect(filterGods(gods, { damage_type: "physical" }).map((g) => g.name)).toEqual(["Chiron"]);
    expect(filterGods(gods, {}).length).toBe(3);
  });
  it("sorts by name", () => {
    expect(sortGods(gods, "name").map((g) => g.name)).toEqual(["Chiron", "Ra", "Ymir"]);
  });
});
