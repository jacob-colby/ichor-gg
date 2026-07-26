import { describe, it, expect } from "vitest";
import { parseHash, toHash } from "./useHashRoute";

describe("parseHash", () => {
  it("defaults to home", () => {
    expect(parseHash("")).toEqual({ view: "home", tab: "builds" });
    expect(parseHash("#/")).toEqual({ view: "home", tab: "builds" });
  });
  it("parses the draft page", () => {
    expect(parseHash("#/draft")).toEqual({ view: "draft", tab: "builds" });
  });
  it("parses the draft page with a shareable query string, ignoring it for routing", () => {
    expect(parseHash("#/draft?m=joust&me=Agni&e=Loki,Thor")).toEqual({ view: "draft", tab: "builds" });
  });
  it("parses the bare builds index (nav landing with no god picked)", () => {
    expect(parseHash("#/builds")).toEqual({ view: "builds", tab: "builds" });
  });
  it("parses a god builds + info route", () => {
    expect(parseHash("#/god/Chiron")).toEqual({ view: "builds", god: "Chiron", tab: "builds" });
    expect(parseHash("#/god/Morgan%20Le%20Fay/info")).toEqual({ view: "builds", god: "Morgan Le Fay", tab: "info" });
  });
  it("parses the items shop + item detail", () => {
    expect(parseHash("#/items")).toEqual({ view: "items", tab: "builds" });
    expect(parseHash("#/items/Deathbringer")).toEqual({ view: "items", tab: "builds", item: "Deathbringer" });
  });
  it("redirects the retired #/gods route to home", () => {
    expect(parseHash("#/gods")).toEqual({ view: "home", tab: "builds" });
  });
  it("parses the tier list", () => {
    expect(parseHash("#/tiers")).toEqual({ view: "tiers", tab: "builds" });
  });
  it("parses patch notes", () => {
    expect(parseHash("#/patch")).toEqual({ view: "patch", tab: "builds" });
  });
});

describe("toHash", () => {
  it("builds encoded hashes", () => {
    expect(toHash.home()).toBe("#/");
    expect(toHash.builds()).toBe("#/builds");
    expect(toHash.draft()).toBe("#/draft");
    expect(toHash.god("Morgan Le Fay")).toBe("#/god/Morgan%20Le%20Fay");
    expect(toHash.godInfo("Chiron")).toBe("#/god/Chiron/info");
    expect(toHash.item("Death's Toll")).toBe("#/items/Death's%20Toll"); // encodeURIComponent keeps '
    expect(toHash.items()).toBe("#/items");
    expect(toHash.tiers()).toBe("#/tiers");
    expect(toHash.patch()).toBe("#/patch");
  });
  it("no longer exposes a gods hash", () => {
    expect((toHash as Record<string, unknown>).gods).toBeUndefined();
  });
});

describe("useHashRoute redirect behavior", () => {
  it("replaces a #/gods URL in place rather than leaving it in history", async () => {
    const { useHashRoute } = await import("./useHashRoute");
    const { renderHook } = await import("@testing-library/react");
    window.location.hash = "#/gods";
    const { result } = renderHook(() => useHashRoute());
    expect(result.current).toEqual({ view: "home", tab: "builds" });
    expect(window.location.hash).toBe("#/");
  });
});
