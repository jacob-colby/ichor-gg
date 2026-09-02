/** Guards for the Seam Rule (DESIGN.md § Named Rules) on the one destination
 *  that had no seam at all.
 *
 * The 2026-08-23 audit measured `#/`, `#/god/Ra`, `#/items`, `#/draft` and
 * `#/tiers` and found `methodLinkInBody: []` on all five: not one surface
 * linked to, or mentioned, the page holding the blend weights, the fitted
 * gold-per-point table and the model's stated blind spots. It was reachable
 * only from the nav rail, last of six — which is the exact failure the Seam
 * Rule names, and the exact way the draft board sat unlinked for a year.
 *
 * These tests exist because the draft board's fix was not guarded and this one
 * has to be. Two levels, deliberately:
 *
 *  - a RENDER assertion per surface, which is what a visitor actually gets;
 *  - a SOURCE guard, in the shape `typeRules.test.ts` uses, so a refactor that
 *    reshapes a header cannot quietly drop the link and still pass by never
 *    rendering the branch it lived in.
 *
 * The link text is asserted NOT to be the route label. A bare "Method" link
 * satisfies a string search and misses the rule, which asks for the visitor's
 * terms — so the test that would be easiest to pass is the one ruled out.
 */
import React from "react";
import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, cleanup } from "@testing-library/react";
import { Home } from "./Home";
import { ItemsShop } from "./ItemsShop";
import { DraftPage } from "./DraftPage";
import { TierList } from "./TierList";
import { DetailPanel } from "./DetailPanel";
import { Legend } from "./Legend";
import type { God, GodTierEntry, IndexData, Item } from "../types";

const gods = [
  { name: "Ra", pantheon: "Egyptian", role: "Mid", damage_type: "magical", abilities: [], aspects: [], base_stats: {} },
] as unknown as God[];

const tierGods: GodTierEntry[] = [
  { name: "Ra", score: 0.56, win_rate: 0.59, matches: 900, play_share: 0.13, tier_score: "S", role: "Mid", damage_type: "magical" },
  { name: "Ymir", score: 0.50, win_rate: 0.51, matches: 400, play_share: 0.02, tier_score: "B", role: "Solo", damage_type: "magical" },
];

const items = [
  { type: "item", name: "A", tier: 3, cost: 2650, stats: { "Physical Power": "40" }, passive: "",
    builds_from: [], builds_into: [], source_url: "", last_verified: "",
    effect_tags: [], efficiency_tier: null },
] as unknown as Item[];

const godBuilds = [{
  type: "smite-build", god: "Ra", mode: "Conquest", builds: [
    { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "",
      slot_scores: { A: { total: 0.59, efficiency: 0.41, win: 0.6, pick: 0.51, fit: 1 } } },
  ],
}];

const indexData = { gods, items: [], builds: [], tierlist: { gods: tierGods, items: [] } } as unknown as IndexData;

/** The five surfaces the audit measured, each rendered the way the shell
 *  renders it. Named by their route so a failure reads as the audit reads. */
const SURFACES: [route: string, render: () => React.ReactElement][] = [
  ["#/", () => <Home data={indexData} />],
  ["#/god/Ra", () => <DetailPanel god="Ra" items={items} builds={godBuilds as never}
    mode="Conquest" onModeChange={() => {}} />],
  ["#/items", () => <ItemsShop items={items} openItem={undefined} goldValues={{}} />],
  ["#/draft", () => <DraftPage gods={gods} items={[]} builds={[]} />],
  ["#/tiers", () => <TierList tierlist={{ gods: tierGods, items: [] }} />],
];

beforeEach(() => {
  window.history.replaceState(null, "", "/");
  localStorage.clear();
});

describe("every surface carrying the model's numbers hands off to the working", () => {
  it.each(SURFACES)("%s links to the method page", (_route, surface) => {
    render(surface());
    const seam = screen.getByTestId("method-seam");
    expect(seam).toHaveAttribute("href", "#/method");
  });

  /* The Seam Rule: "in the visitor's terms rather than as a route label". A
   * link reading "Method" would pass a link-presence check and teach nobody
   * what is behind it — the nav rail already does that, and it is why this
   * page went unvisited. */
  it.each(SURFACES)("%s names the destination as a question, not as a route", (_route, surface) => {
    render(surface());
    const text = screen.getByTestId("method-seam").textContent ?? "";
    expect(text.trim().length).toBeGreaterThan(12);
    expect(text).not.toMatch(/^\s*method\s*(→|->)?\s*$/i);
  });

  /* Five distinct surfaces asking five distinct questions. Identical copy on
   * all of them would be chrome, which is what the rule is against. */
  it("asks a different question on each surface", () => {
    const seen: string[] = [];
    for (const [, surface] of SURFACES) {
      render(surface());
      seen.push((screen.getByTestId("method-seam").textContent ?? "").trim());
      cleanup();
    }
    expect(new Set(seen).size).toBe(SURFACES.length);
  });

  /* The `?` dialog is where a lost visitor goes first, and it is the one place
   * whose whole job is "how this works". */
  it("is reachable from the help dialog too, which closes behind it", () => {
    render(<Legend onClose={() => {}} />);
    expect(screen.getByTestId("legend-method-seam")).toHaveAttribute("href", "#/method");
  });
});

/* Source-level, so a header rewrite cannot drop the seam by deleting the
 * branch that rendered it. Same technique as `typeRules.test.ts`, and for the
 * same reason: the failure being guarded is silent. */
describe("the seam survives a refactor", () => {
  const sources = import.meta.glob("./*.tsx", {
    query: "?raw", import: "default", eager: true,
  }) as Record<string, string>;

  const SURFACE_FILES = ["Home.tsx", "ItemsShop.tsx", "DraftPage.tsx", "TierList.tsx", "DetailPanel.tsx"];

  it.each(SURFACE_FILES)("%s still calls toHash.method()", (file) => {
    const source = sources[`./${file}`];
    expect(source, `${file} not found by the glob`).toBeTruthy();
    expect(source).toContain("toHash.method()");
  });

  it("reads the files it claims to, so a broken glob can't pass vacuously", () => {
    expect(Object.keys(sources).length).toBeGreaterThan(10);
  });
});
