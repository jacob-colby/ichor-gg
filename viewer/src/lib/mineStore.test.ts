import { describe, it, expect, beforeEach } from "vitest";
import { getMine, saveMine, deleteMine } from "./mineStore";

beforeEach(() => localStorage.clear());

describe("mineStore", () => {
  it("saves, reads back, and replaces by name within a god+mode", () => {
    saveMine("Chiron", "Conquest", { name: "Crit", slot_order: ["Deathbringer"] });
    expect(getMine("Chiron", "Conquest")).toEqual([{ name: "Crit", slot_order: ["Deathbringer"] }]);
    saveMine("Chiron", "Conquest", { name: "Crit", slot_order: ["Rage"] }); // replace
    expect(getMine("Chiron", "Conquest")).toEqual([{ name: "Crit", slot_order: ["Rage"] }]);
    saveMine("Chiron", "Conquest", { name: "Other", slot_order: ["X"] });
    expect(getMine("Chiron", "Conquest").map((b) => b.name)).toEqual(["Crit", "Other"]);
  });
  it("scopes builds by god and mode", () => {
    saveMine("Chiron", "Conquest", { name: "A", slot_order: [] });
    expect(getMine("Chiron", "Joust")).toEqual([]);
    expect(getMine("Ra", "Conquest")).toEqual([]);
  });
  it("deletes by name", () => {
    saveMine("Ra", "Conquest", { name: "A", slot_order: [] });
    saveMine("Ra", "Conquest", { name: "B", slot_order: [] });
    deleteMine("Ra", "Conquest", "A");
    expect(getMine("Ra", "Conquest").map((b) => b.name)).toEqual(["B"]);
  });
  it("returns [] on empty / malformed storage", () => {
    expect(getMine("Nobody", "Conquest")).toEqual([]);
    localStorage.setItem("smite:mine-builds", "not json");
    expect(getMine("Chiron", "Conquest")).toEqual([]);
  });
});
