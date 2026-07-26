import { describe, it, expect } from "vitest";
import { parseHash, toHash, lensHash, isRetiredPath } from "./useHashRoute";

describe("parseHash — the roster is a subject too", () => {
  it("defaults to the roster board", () => {
    expect(parseHash("")).toEqual({ lens: "board" });
    expect(parseHash("#/")).toEqual({ lens: "board" });
  });

  it("parses each roster lens", () => {
    expect(parseHash("#/tiers")).toEqual({ lens: "tiers" });
    expect(parseHash("#/items")).toEqual({ lens: "items" });
    expect(parseHash("#/draft")).toEqual({ lens: "draft" });
    expect(parseHash("#/patch")).toEqual({ lens: "patch" });
  });

  it("keeps the item deep link on the roster's items lens", () => {
    expect(parseHash("#/items/Deathbringer")).toEqual({ lens: "items", item: "Deathbringer" });
  });

  it("ignores a query string when routing", () => {
    expect(parseHash("#/draft?m=joust&me=Agni&e=Loki,Thor")).toEqual({ lens: "draft" });
    expect(parseHash("#/items/Rage?eff=premium")).toEqual({ lens: "items", item: "Rage" });
  });
});

describe("parseHash — a god and its lenses", () => {
  it("opens a god on builds", () => {
    expect(parseHash("#/god/Chiron")).toEqual({ god: "Chiron", lens: "builds" });
  });

  it("parses the three other god lenses", () => {
    expect(parseHash("#/god/Ra/kit")).toEqual({ god: "Ra", lens: "kit" });
    expect(parseHash("#/god/Ra/items")).toEqual({ god: "Ra", lens: "items" });
    expect(parseHash("#/god/Ra/ranking")).toEqual({ god: "Ra", lens: "ranking" });
  });

  it("decodes a god whose name has a space", () => {
    expect(parseHash("#/god/Morgan%20Le%20Fay")).toEqual({ god: "Morgan Le Fay", lens: "builds" });
  });

  it("falls back to builds for a lens it doesn't recognise", () => {
    expect(parseHash("#/god/Ra/sparkle")).toEqual({ god: "Ra", lens: "builds" });
  });
});

/* These links get pasted into Discord. A shell rewrite that quietly breaks
 * them is a shell rewrite that loses the audience it already has. */
describe("URLs the old tool-first shell produced still resolve", () => {
  it("keeps #/god/X/info working as the kit lens", () => {
    expect(parseHash("#/god/Morgan%20Le%20Fay/info")).toEqual({ god: "Morgan Le Fay", lens: "kit" });
  });

  it("lands the retired #/gods and #/builds on the roster board", () => {
    expect(parseHash("#/gods")).toEqual({ lens: "board" });
    expect(parseHash("#/builds")).toEqual({ lens: "board" });
  });

  it("marks exactly those two paths as retired, and nothing else", () => {
    expect(isRetiredPath("#/gods")).toBe(true);
    expect(isRetiredPath("#/builds")).toBe(true);
    expect(isRetiredPath("#/builds?q=x")).toBe(true);
    expect(isRetiredPath("#/god/Ra")).toBe(false);
    expect(isRetiredPath("#/items")).toBe(false);
    expect(isRetiredPath("#/")).toBe(false);
  });
});

describe("toHash", () => {
  it("builds encoded hashes", () => {
    expect(toHash.home()).toBe("#/");
    expect(toHash.draft()).toBe("#/draft");
    expect(toHash.god("Morgan Le Fay")).toBe("#/god/Morgan%20Le%20Fay");
    expect(toHash.godKit("Chiron")).toBe("#/god/Chiron/kit");
    expect(toHash.godItems("Chiron")).toBe("#/god/Chiron/items");
    expect(toHash.godRanking("Chiron")).toBe("#/god/Chiron/ranking");
    expect(toHash.item("Death's Toll")).toBe("#/items/Death's%20Toll"); // encodeURIComponent keeps '
    expect(toHash.items()).toBe("#/items");
    expect(toHash.tiers()).toBe("#/tiers");
    expect(toHash.patch()).toBe("#/patch");
  });

  // `#/builds` isn't a place any more — picking a god *is* the navigation.
  it("points the retired builds hash at the roster board", () => {
    expect(toHash.builds()).toBe("#/");
  });

  it("no longer exposes a gods hash", () => {
    expect((toHash as Record<string, unknown>).gods).toBeUndefined();
  });
});

describe("lensHash", () => {
  it("resolves roster lenses when there's no subject", () => {
    expect(lensHash("board")).toBe("#/");
    expect(lensHash("tiers")).toBe("#/tiers");
    expect(lensHash("draft")).toBe("#/draft");
  });

  it("resolves god lenses against the subject in view", () => {
    expect(lensHash("builds", "Ra")).toBe("#/god/Ra");
    expect(lensHash("kit", "Ra")).toBe("#/god/Ra/kit");
    expect(lensHash("items", "Ra")).toBe("#/god/Ra/items");
    expect(lensHash("ranking", "Ra")).toBe("#/god/Ra/ranking");
  });

  // The two lens vocabularies overlap on "items"; the subject decides which.
  it("reads the same lens name differently depending on the subject", () => {
    expect(lensHash("items")).toBe("#/items");
    expect(lensHash("items", "Ra")).toBe("#/god/Ra/items");
  });
});

describe("useHashRoute redirect behavior", () => {
  it("replaces a retired URL in place rather than leaving it in history", async () => {
    const { useHashRoute } = await import("./useHashRoute");
    const { renderHook } = await import("@testing-library/react");
    window.location.hash = "#/gods";
    const { result } = renderHook(() => useHashRoute());
    expect(result.current).toEqual({ lens: "board" });
    expect(window.location.hash).toBe("#/");
  });
});
