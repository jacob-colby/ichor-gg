import { describe, it, expect } from "vitest";
import { documentTitle, SITE_TITLE } from "./documentTitle";
import type { Route } from "./useHashRoute";

const r = (o: Partial<Route>): Route => ({ lens: "board", ...o } as Route);

describe("documentTitle", () => {
  it("uses the full tagline on the roster board", () => {
    expect(documentTitle(r({ lens: "board" }))).toBe(SITE_TITLE);
  });

  it("labels the roster lenses", () => {
    expect(documentTitle(r({ lens: "tiers" }))).toBe("Tier list — ichor");
    expect(documentTitle(r({ lens: "patch" }))).toBe("Patch notes — ichor");
    expect(documentTitle(r({ lens: "draft" }))).toBe("Draft — ichor");
    expect(documentTitle(r({ lens: "items" }))).toBe("Items — ichor");
  });

  it("names an opened item", () => {
    expect(documentTitle(r({ lens: "items", item: "Rage" }))).toBe("Rage — ichor");
  });

  it("names the god on its builds lens", () => {
    expect(documentTitle(r({ god: "Agni", lens: "builds" }))).toBe("Agni — ichor");
  });

  /* A god now has four lenses. Four identical "Agni — ichor" entries in
   * history would be exactly the problem this function exists to solve. */
  it("distinguishes a god's lenses from one another", () => {
    expect(documentTitle(r({ god: "Agni", lens: "kit" }))).toBe("Agni’s kit — ichor");
    expect(documentTitle(r({ god: "Agni", lens: "items" }))).toBe("Agni’s items — ichor");
    expect(documentTitle(r({ god: "Agni", lens: "ranking" }))).toBe("Agni’s ranking — ichor");
  });

  // The subject wins over a roster lens name that happens to match.
  it("reads the items lens as the god's when a god is in view", () => {
    expect(documentTitle(r({ lens: "items" }))).toBe("Items — ichor");
    expect(documentTitle(r({ god: "Ra", lens: "items" }))).toBe("Ra’s items — ichor");
  });

  it("prefers an explicitly passed god name", () => {
    expect(documentTitle(r({ god: "Ra", lens: "builds" }), "Nu Wa")).toBe("Nu Wa — ichor");
  });
});
