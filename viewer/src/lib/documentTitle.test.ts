import { describe, it, expect } from "vitest";
import { documentTitle, SITE_TITLE } from "./documentTitle";
import type { Route } from "./useHashRoute";

const r = (o: Partial<Route>): Route => ({ view: "home", ...o } as Route);

describe("documentTitle", () => {
  it("uses the full tagline on home", () => {
    expect(documentTitle(r({ view: "home" }))).toBe(SITE_TITLE);
  });

  it("names the god on a build page", () => {
    expect(documentTitle(r({ view: "builds", god: "Agni" }))).toBe("Agni — ichor");
  });

  it("falls back to Builds with no god selected", () => {
    expect(documentTitle(r({ view: "builds" }))).toBe("Builds — ichor");
  });

  it("labels the other views", () => {
    expect(documentTitle(r({ view: "tiers" }))).toBe("Tier list — ichor");
    expect(documentTitle(r({ view: "patch" }))).toBe("Patch notes — ichor");
    expect(documentTitle(r({ view: "draft" }))).toBe("Draft — ichor");
    expect(documentTitle(r({ view: "items" }))).toBe("Items — ichor");
  });

  it("names an opened item", () => {
    expect(documentTitle(r({ view: "items", item: "Rage" }))).toBe("Rage — ichor");
  });
});
