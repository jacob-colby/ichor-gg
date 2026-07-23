import { describe, it, expect } from "vitest";
import { parseHash, toHash } from "./useHashRoute";

describe("parseHash", () => {
  it("defaults to the builds home", () => {
    expect(parseHash("")).toEqual({ view: "builds", tab: "builds" });
    expect(parseHash("#/")).toEqual({ view: "builds", tab: "builds" });
  });
  it("parses a god builds + info route", () => {
    expect(parseHash("#/god/Chiron")).toEqual({ view: "builds", god: "Chiron", tab: "builds" });
    expect(parseHash("#/god/Morgan%20Le%20Fay/info")).toEqual({ view: "builds", god: "Morgan Le Fay", tab: "info" });
  });
  it("parses the items shop + item detail", () => {
    expect(parseHash("#/items")).toEqual({ view: "items", tab: "builds" });
    expect(parseHash("#/items/Deathbringer")).toEqual({ view: "items", tab: "builds", item: "Deathbringer" });
  });
  it("parses the gods index", () => {
    expect(parseHash("#/gods")).toEqual({ view: "gods", tab: "builds" });
  });
});

describe("toHash", () => {
  it("builds encoded hashes", () => {
    expect(toHash.god("Morgan Le Fay")).toBe("#/god/Morgan%20Le%20Fay");
    expect(toHash.godInfo("Chiron")).toBe("#/god/Chiron/info");
    expect(toHash.item("Death's Toll")).toBe("#/items/Death's%20Toll"); // encodeURIComponent keeps '
    expect(toHash.items()).toBe("#/items");
  });
});
