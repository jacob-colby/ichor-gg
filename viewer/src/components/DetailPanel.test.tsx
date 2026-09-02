import React from "react";
import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { DetailPanel } from "./DetailPanel";
import { saveMine } from "../lib/mineStore";
import type { BuildNote, Item } from "../types";

/** Full-shaped Item fixture — the ledger reads cost for its gold spine, and
 * the expanded card reads tier/stats/passive/effect_tags. */
function itemFx(name: string, cost: number, extra: Partial<Item> = {}): Item {
  return {
    type: "item", name, tier: 3, cost, stats: { "Physical Power": "40" }, passive: "",
    builds_from: [], builds_into: [], source_url: "", last_verified: "",
    effect_tags: [], efficiency_tier: null, ...extra,
  } as Item;
}

const panel = (props: Partial<React.ComponentProps<typeof DetailPanel>> = {}) => (
  <DetailPanel god="Chiron" godData={undefined} items={[]} builds={[]}
    mode="Conquest" onModeChange={() => {}} {...props} />
);

/** The ledger row for an item, as a screen-reader would find it. */
const row = (name: string) => screen.getByRole("button", { name: new RegExp(`^${name}[,.]`, "i") });

const chironCommunity: BuildNote = {
  type: "smite-build", god: "Chiron", mode: "Conquest",
  builds: [{
    source: "community", aspect: "Aspect of the Heroic Tutor",
    aspect_pick_rate: 0.09, aspect_win_rate: 0.45,
    slot_order: [{ name: "Transcendence", pick_rate: 0.6, win_rate: 0.49 }],
    source_url: "https://smitebrain.com/gods/chiron/",
  }],
};

describe("DetailPanel — what opens by default", () => {
  beforeEach(() => localStorage.clear());

  it("opens on the model's build, not the community's", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [{ name: "MetaItem", pick_rate: 0.6, win_rate: 0.5 }], source_url: "u" },
      { source: "suggested", archetype: "core", slot_order: ["ModelItem"], situational_swaps: [], rationale: "" },
    ] }];
    render(panel({ builds: builds as never }));
    // The model's item is on the ledger; the community's is the comparison,
    // not the default view.
    expect(screen.getByText("ModelItem")).toBeInTheDocument();
    expect(screen.getByText(/buy order/i)).toBeInTheDocument();
  });

  it("offers the three builds and the flavors in one group, community among them", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [{ name: "X", pick_rate: 0.5, win_rate: 0.5 }], source_url: "u" },
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "" },
      { source: "suggested", archetype: "crit", slot_order: ["B"], situational_swaps: [], rationale: "" },
    ] }];
    render(panel({ builds: builds as never }));
    const group = within(screen.getByRole("group", { name: /build flavor/i }));
    expect(group.getByRole("button", { name: /balanced/i })).toHaveAttribute("aria-pressed", "true");
    expect(group.getByRole("button", { name: /crit/i })).toHaveAttribute("aria-pressed", "false");
    // Community is selectable now — a third answer the reader can hold whole,
    // not only a comparison track drawn against someone else's build.
    expect(group.getByRole("button", { name: /community/i })).toBeInTheDocument();
    // No broken tablist left behind.
    expect(screen.queryAllByRole("tab")).toHaveLength(0);
  });

  it("switches build when another flavor is pressed", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "" },
      { source: "suggested", archetype: "crit", slot_order: ["B"], situational_swaps: [], rationale: "" },
    ] }];
    render(panel({ builds: builds as never }));
    fireEvent.click(screen.getByRole("button", { name: /crit/i }));
    expect(screen.getByText("B")).toBeInTheDocument();
    expect(screen.queryByText("A")).not.toBeInTheDocument();
  });

  it("falls back to the community build when the god has no model build at all", () => {
    render(panel({ builds: [chironCommunity] }));
    expect(screen.getByText("Transcendence")).toBeInTheDocument();
    expect(screen.getByText(/slot order/i)).toBeInTheDocument();
    // The group renders whenever anything is selectable — with only a
    // community entry, that is the one button in it.
    const only = within(screen.getByRole("group", { name: /build flavor/i }));
    expect(only.getByRole("button", { name: /community/i })).toBeInTheDocument();
  });

  it("explains itself when the god has no build note for this mode yet", () => {
    render(panel({ god: "SomeNewGod", builds: [] }));
    expect(screen.getByRole("heading", { level: 2, name: "SomeNewGod" })).toBeInTheDocument();
    expect(screen.getByText(/no build data for SomeNewGod in this index yet/i)).toBeInTheDocument();
  });

  // The shell's subject header owns the h1 now — it names the god on every
  // lens, not just this one. The build view starts at level 2.
  it("starts at level 2, under the subject header's heading", () => {
    render(panel({ builds: [chironCommunity] }));
    expect(screen.queryByRole("heading", { level: 1 })).not.toBeInTheDocument();
  });
});


describe("DetailPanel — the buy ledger", () => {
  beforeEach(() => localStorage.clear());

  const items = [itemFx("A", 2650), itemFx("B", 2350), itemFx("C", 3000)];
  const withMeta = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
    { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null, source_url: "u",
      slot_order: [{ name: "A", pick_rate: 0.5, win_rate: 0.6 }, { name: "C", pick_rate: 0.3, win_rate: 0.5 }] },
    { source: "suggested", archetype: "core", slot_order: ["A", "B"], situational_swaps: [], rationale: "",
      slot_scores: {
        A: { total: 0.59, efficiency: 0.41, win: 0.6, pick: 0.51, fit: 1 },
        B: { total: 0.48, efficiency: 0.5, win: 0.5, pick: 0, fit: 0.9 },
      } },
  ] }];

  it("puts cumulative gold on every row and sums the core", () => {
    render(panel({ items, builds: withMeta as never }));
    // The spine carries the running figure on each row and the header sums it,
    // so 5,000g legitimately appears twice — the header is asserted by testid
    // rather than by a text query that can't tell the two apart.
    expect(screen.getByText("2,650g")).toBeInTheDocument();
    expect(screen.getAllByText("5,000g").length).toBe(2);      // spine row + header
    // "core", not "total" — the starter is bought first and isn't on this spine.
    expect(screen.getByTestId("ledger-total")).toHaveTextContent(/5,000g core/);
  });

  it("reports how much of the build the community agrees with", () => {
    render(panel({ items, builds: withMeta as never }));
    expect(screen.getByText(/shares 1 of 2/i)).toBeInTheDocument();
  });

  it("shows the composite score and all four axes on the row, without a hover", () => {
    render(panel({ items, builds: withMeta as never }));
    const ledgerRow = row("A");
    expect(ledgerRow).toHaveTextContent("0.59");    // total
    expect(ledgerRow).toHaveTextContent("value");
    expect(ledgerRow).toHaveTextContent("win");
    expect(ledgerRow).toHaveTextContent("pick");
    expect(ledgerRow).toHaveTextContent("fit");
  });

  it("names both sources and the gap in the row's accessible name", () => {
    render(panel({ items, builds: withMeta as never }));
    expect(row("A")).toHaveAccessibleName(/model score 0\.59/i);
    expect(row("A")).toHaveAccessibleName(/at 2,650g spent/i);
    expect(row("A")).toHaveAccessibleName(/community buys it 1st/i);
    expect(row("B")).toHaveAccessibleName(/community does not buy it/i);
  });

  /* The row used to state the order disagreement in gold — "model buys later
   * by 2,550g" — which is precise and answers a question nobody asks. A build
   * is bought in slots, so the disagreement is stated in slots. */
  it("states an order disagreement in slots, not in gold", () => {
    const shifted = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null, source_url: "u",
        slot_order: [{ name: "B", pick_rate: 0.5, win_rate: 0.6 }, { name: "A", pick_rate: 0.3, win_rate: 0.5 }] },
      { source: "suggested", archetype: "core", slot_order: ["A", "B"], situational_swaps: [], rationale: "",
        slot_scores: {
          A: { total: 0.59, efficiency: 0.41, win: 0.6, pick: 0.51, fit: 1 },
          B: { total: 0.48, efficiency: 0.5, win: 0.5, pick: 0, fit: 0.9 },
        } },
    ] }];
    render(panel({ items, builds: shifted as never }));
    expect(row("A")).toHaveTextContent(/meta buys 2nd/);
    expect(row("A")).toHaveTextContent(/model buys 1st/);
    // The gold SPINE stays — it's the ledger's axis. What goes is stating the
    // disagreement itself in gold: "model buys earlier by 2,550g".
    expect(row("A")).toHaveTextContent("2,650g");
    expect(row("A")).not.toHaveTextContent(/buys (earlier|later)/);
  });

  it("stays quiet when both orders agree on the slot", () => {
    render(panel({ items, builds: withMeta as never }));
    // A is first in both orders — there is no disagreement to report.
    expect(row("A")).toHaveTextContent(/meta buys 1st/);
    expect(row("A")).not.toHaveTextContent(/model buys/);
  });

  it("marks an item the meta doesn't buy", () => {
    render(panel({ items, builds: withMeta as never }));
    expect(row("B")).toHaveTextContent(/meta doesn.t buy this/i);
    expect(row("A")).not.toHaveTextContent(/meta doesn.t buy this/i);
    expect(screen.getAllByText("off-meta")).toHaveLength(1);
  });

  it("expands a row into full item detail on click, on every breakpoint", () => {
    const rich = [itemFx("A", 2650, { passive: "Deals bonus damage.", tier: 4 }), itemFx("B", 2350)];
    render(panel({ items: rich, builds: withMeta as never }));
    expect(screen.queryByText(/why this item/i)).not.toBeInTheDocument();

    fireEvent.click(row("A"));
    expect(screen.getByText(/why this item/i)).toBeInTheDocument();
    expect(screen.getByText(/Deals bonus damage\./)).toBeInTheDocument();
    expect(screen.getByText("Physical Power")).toBeInTheDocument();
    const cost = screen.getByText("2650g");
    expect(cost).toHaveClass("text-gold");

    fireEvent.click(row("A"));
    expect(screen.queryByText(/why this item/i)).not.toBeInTheDocument();
  });

  /* AUDIT F1. `value 0.55  win 0.55  pick 0.00  fit 0.69` is the product's
   * whole pitch and a new player has no anchor for it — no scale, no
   * direction. The definitions existed in exactly two places: a `title` on
   * these labels, and the Method page nothing linked to. A `title` needs a
   * pointer to hover, so on the phone a draft actually happens on, the four
   * numbers that carry this site had no meaning attached to them ANYWHERE.
   * The row above carries the same figures `aria-hidden` with no title at
   * all, so there was no fallback either.
   *
   * These assert the definitions are in the accessible tree as text. A fix
   * that reaches for another tooltip is the bug again, so `title` is asserted
   * absent rather than merely not required. */
  it("defines all four signals as text, reachable with no hover", () => {
    render(panel({ items, builds: withMeta as never }));
    fireEvent.click(row("A"));
    const why = screen.getByText(/why this item/i).closest("div")!.parentElement!;
    expect(why).toHaveTextContent(/stats returned per gold spent/i);
    expect(why).toHaveTextContent(/community win rate with this item on this god/i);
    expect(why).toHaveTextContent(/how often this god.s players buy it/i);
    expect(why).toHaveTextContent(/how well the item.s stats match this god.s kit/i);
  });

  it("carries no definition that only a pointer can reach", () => {
    render(panel({ items, builds: withMeta as never }));
    fireEvent.click(row("A"));
    const why = screen.getByText(/why this item/i).closest("div")!.parentElement!;
    for (const label of ["value", "win", "pick", "fit"]) {
      const el = within(why).getByText(label);
      expect(el).not.toHaveAttribute("title");
    }
  });

  /* Joust and Arena drop win and pick. A definition for a signal that is not
   * on the panel would describe a number that isn't there. */
  it("defines only the signals the mode actually measures", () => {
    const noCommunity = [{ type: "smite-build", god: "Chiron", mode: "Joust", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "",
        slot_scores: { A: { total: 0.6, efficiency: 0.5, win: 0.5, pick: 0, fit: 0.8 } } },
    ] }];
    render(panel({ items, builds: noCommunity as never, mode: "Joust" }));
    fireEvent.click(row("A"));
    const why = screen.getByText(/why this item/i).closest("div")!.parentElement!;
    expect(why).toHaveTextContent(/stats returned per gold spent/i);
    expect(why).not.toHaveTextContent(/community win rate with this item/i);
  });

  it("headlines the composite score inside the breakdown", () => {
    render(panel({ items, builds: withMeta as never }));
    fireEvent.click(row("A"));
    const why = screen.getByText(/why this item/i).closest("div")!.parentElement!;
    expect(why).toHaveTextContent("0.59");
  });

  /* F2. B is in neither the community's slot order nor any slot's alternates,
   * so the pipeline handed its row `pick 0` and `win` = this god's median. Both
   * used to print like measurements. PRODUCT.md Principle 3: "we didn't measure
   * this" and "this is bad" must never render the same way. */
  it("does not print win/pick as measurements for an item the community has no record of", () => {
    render(panel({ items, builds: withMeta as never }));
    const unrecorded = row("B");
    expect(unrecorded).toHaveTextContent("value");
    expect(unrecorded).toHaveTextContent("fit");
    expect(unrecorded).toHaveTextContent(/win\/pick not measured here/i);
    // The two numbers themselves are gone, not merely captioned.
    expect(unrecorded).not.toHaveTextContent(/win 0/);
    expect(unrecorded).not.toHaveTextContent(/pick 0/);
    expect(unrecorded).not.toHaveTextContent("0.00");
  });

  it("keeps win and pick on a row the community DOES have a record for", () => {
    render(panel({ items, builds: withMeta as never }));
    expect(row("A")).not.toHaveTextContent(/not measured here/i);
    expect(row("A")).toHaveTextContent("win");
    expect(row("A")).toHaveTextContent("pick");
  });

  /* The panel has to say which absence it is, because the score above it still
   * spent win's 0.45 weight on the stand-in. "Not measured" alone would read as
   * "computed on the other two". */
  it("names the absence and says the score still spends its weight", () => {
    render(panel({ items, builds: withMeta as never }));
    fireEvent.click(row("B"));
    const why = screen.getByText(/why this item/i).closest("div")!.parentElement!;
    expect(why).toHaveTextContent(/no community record for this item on this god/i);
    expect(why).toHaveTextContent(/still spends their weight on a stand-in/i);
    // The mode-level wording is a different fact and must not appear here.
    expect(why).not.toHaveTextContent(/no community data in this mode/i);
  });

  /* Recorded, but only as somebody else's slot alternate — a measurement, so
   * the axes stay, and the older "not in their order" copy is still the right
   * thing to say about it. */
  it("keeps the axes for an item the community records only as an alternate", () => {
    const asAlternate = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null, source_url: "u",
        slot_order: [{ name: "A", pick_rate: 0.5, win_rate: 0.6,
          alternates: [{ name: "B", pick_rate: 0.27, win_rate: 0.48 }] }] },
      { source: "suggested", archetype: "core", slot_order: ["A", "B"], situational_swaps: [], rationale: "",
        slot_scores: {
          A: { total: 0.59, efficiency: 0.41, win: 0.6, pick: 0.51, fit: 1 },
          B: { total: 0.48, efficiency: 0.5, win: 0.48, pick: 0.27, fit: 0.9 },
        } },
    ] }];
    render(panel({ items, builds: asAlternate as never }));
    expect(row("B")).not.toHaveTextContent(/not measured here/i);
    expect(row("B")).toHaveTextContent(/meta buys this 27%/);
    fireEvent.click(row("B"));
    expect(screen.getByText(/community build doesn.t include this item/i)).toBeInTheDocument();
  });

  it("shows what the community bought instead, in its own order", () => {
    render(panel({ items, builds: withMeta as never }));
    expect(screen.getByText(/what the community buys instead/i)).toBeInTheDocument();
    // C is in the community order but not the model's build.
    const link = screen.getByRole("link", { name: /^C, bought 2nd by the community/i });
    expect(link).toHaveAttribute("href", expect.stringContaining("/items/C"));
  });

  it("says so plainly when the model buys everything the community does", () => {
    const sameItems = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null, source_url: "u",
        slot_order: [{ name: "A", pick_rate: 0.5, win_rate: 0.6 }] },
      { source: "suggested", archetype: "core", slot_order: ["A", "B"], situational_swaps: [], rationale: "" },
    ] }];
    render(panel({ items, builds: sameItems as never }));
    expect(screen.getByText(/nothing — the model buys every item the community does/i)).toBeInTheDocument();
  });

  it("does not narrate a player's own build as the model's", () => {
    saveMine("Chiron", "Conquest", { name: "mine", slot_order: ["A", "C"] });
    render(panel({ items, builds: withMeta as never }));
    fireEvent.click(within(screen.getByRole("group", { name: /build flavor/i })).getByRole("button", { name: /mine/i }));
    expect(screen.queryByText(/model buys/i)).not.toBeInTheDocument();
    expect(screen.queryByText("off-meta")).not.toBeInTheDocument();
    expect(screen.queryByText(/what the community buys instead/i)).not.toBeInTheDocument();
  });

  it("does not print win/pick as measurements when there is no community data", () => {
    const noCommunity = [{ type: "smite-build", god: "Chiron", mode: "Joust", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "",
        slot_scores: { A: { total: 0.6, efficiency: 0.5, win: 0.5, pick: 0, fit: 0.8 } } },
    ] }];
    render(panel({ items, builds: noCommunity as never, mode: "Joust" }));
    expect(screen.getByText(/win\/pick not measured here/i)).toBeInTheDocument();
    fireEvent.click(row("A"));
    expect(screen.getByText(/win and pick aren.t measured here/i)).toBeInTheDocument();
  });

  it("omits the breakdown for a build with no slot_scores", () => {
    const noScores = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "" },
    ] }];
    render(panel({ items, builds: noScores as never }));
    fireEvent.click(row("A"));
    expect(screen.queryByText(/why this item/i)).not.toBeInTheDocument();
  });

  /* Two thirds of the shipped build groups are Joust and Arena, which have no
   * outcome data anywhere — the tier list has admitted that since it stopped
   * ranking them and the builds never did. "Nothing to compare against" read
   * as a missing convenience; what is missing is the evidence that the
   * ORDERING means anything, which is the one thing a buy order asserts. */
  it("says outright that a mode with no outcome data is a shortlist, not an order", () => {
    const noCommunity = [{ type: "smite-build", god: "Chiron", mode: "Joust", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "" },
    ] }];
    render(panel({ items, builds: noCommunity as never, mode: "Joust" }));
    expect(screen.getByText(/no outcome data exists for Joust/i)).toBeInTheDocument();
    expect(screen.getByText(/ordering.*unproven|unproven/i)).toBeInTheDocument();
    expect(screen.getByText(/shortlist rather than a buy order/i)).toBeInTheDocument();
    expect(screen.queryByText("off-meta")).not.toBeInTheDocument();
  });

  /* No shipped flavor sets `fun` any more — `fun-crit` was retired for focused
   * builds meant to be played. The mechanism stays tested because the entry
   * shape still carries the flag, and a build that opts out of the meta
   * comparison must not silently start being compared against it. */
  it("does not compare a fun build against the meta", () => {
    const funBuild = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [{ name: "A", pick_rate: 0.6, win_rate: 0.5 }], source_url: "u" },
      { source: "suggested", archetype: "fun-crit", fun: true, slot_order: ["B"], situational_swaps: [], rationale: "" },
    ] }];
    render(panel({ items, builds: funBuild as never }));
    fireEvent.click(screen.getByRole("button", { name: /fun-crit/i }));
    expect(screen.getByText(/for fun/i)).toBeInTheDocument();
    expect(screen.getByText(/off-class/i)).toBeInTheDocument();
    expect(screen.queryByText("off-meta")).not.toBeInTheDocument();
  });

  it("shows the community's per-slot alternates when the community build is what's rendered", () => {
    const alts = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null, source_url: "u",
        slot_order: [{ name: "Transcendence", pick_rate: 0.6, win_rate: 0.5,
          alternates: [{ name: "Jotunn's Revenge", pick_rate: 0.11, win_rate: 0.71 }] }] },
    ] }];
    render(panel({ builds: alts as never }));
    expect(screen.getByText(/or Jotunn's Revenge/i)).toBeInTheDocument();
  });

  it("shows pick/win rates on a community-rendered row", () => {
    render(panel({ builds: [chironCommunity] }));
    expect(screen.getByText(/60%\s*\/\s*49%/)).toBeInTheDocument();
  });

  it("falls back to an initial when an item icon fails twice, never a hole", () => {
    render(panel({ items, builds: withMeta as never }));
    const img = row("A").querySelector('img[alt=""]')!;
    fireEvent.error(img);                                       // retry
    fireEvent.error(row("A").querySelector('img[alt=""]')!);     // retry failed
    expect(row("A").querySelector('img[alt=""]')).toBeNull();
    expect(row("A")).toHaveTextContent("A");
  });
});

describe("DetailPanel — situational swaps", () => {
  beforeEach(() => localStorage.clear());

  const swapItems = [itemFx("Base A", 2500), itemFx("Base B", 2600), itemFx("Base C", 3000),
    itemFx("Cheap Swap", 1800), itemFx("Pricey Swap", 4200), itemFx("Equal Swap", 2950)];
  const swapBuild = (swap_item: string, flex_slots?: string[]) => ([{
    type: "smite-build", god: "Chiron", mode: "Conquest", builds: [{
      source: "suggested", archetype: "core", slot_order: ["Base A", "Base B", "Base C"],
      ...(flex_slots ? { flex_slots } : {}),
      situational_swaps: [{ vs_tag: "heavy_cc", swap: "x", swap_item }], rationale: "",
    }],
  }]);

  it("reflows the build when a matchup is selected", () => {
    render(panel({ items: swapItems, builds: swapBuild("Cheap Swap") as never }));
    fireEvent.click(screen.getByRole("button", { name: /heavy cc/i }));
    expect(screen.getByText("Cheap Swap")).toBeInTheDocument();
    expect(screen.getByText("Base C")).toHaveClass("line-through");
  });

  it("removes the flex slot rather than the last when one is marked", () => {
    render(panel({ items: swapItems, builds: swapBuild("Cheap Swap", ["Base A"]) as never }));
    fireEvent.click(screen.getByRole("button", { name: /heavy cc/i }));
    expect(screen.getByText("Base A")).toHaveClass("line-through");
    expect(screen.getByText("Base C")).not.toHaveClass("line-through");
  });

  it("keeps a swapped-out slot's gold out of the running total", () => {
    render(panel({ items: swapItems, builds: swapBuild("Cheap Swap") as never }));
    // Base A 2500 + Base B 2600 + Base C 3000 = 8100 before the swap.
    expect(screen.getByTestId("ledger-total")).toHaveTextContent(/8,100g core/);
    fireEvent.click(screen.getByRole("button", { name: /heavy cc/i }));
    // Base C's 3000 is never spent; Cheap Swap's 1800 is.
    expect(screen.getByTestId("ledger-total")).toHaveTextContent(/6,900g core/);
  });

  it("names what a swap comes in for, using applySwap's own target", () => {
    render(panel({ items: swapItems, builds: swapBuild("Cheap Swap") as never }));
    expect(screen.getByText(/in for base c/i)).toBeInTheDocument();
  });

  it("notes an order shift when the swap is materially cheaper, and the other way when dearer", () => {
    const { unmount } = render(panel({ items: swapItems, builds: swapBuild("Cheap Swap") as never }));
    expect(screen.getByText(/earlier/i)).toBeInTheDocument();
    unmount();
    render(panel({ items: swapItems, builds: swapBuild("Pricey Swap") as never }));
    expect(screen.getByText(/later/i)).toBeInTheDocument();
  });

  it("prints nothing where nothing shifts", () => {
    render(panel({ items: swapItems, builds: swapBuild("Equal Swap") as never }));
    expect(screen.getByText(/in for base c/i)).toBeInTheDocument();
    expect(screen.queryByText(/earlier/i)).not.toBeInTheDocument();
    expect(screen.queryByText(/later/i)).not.toBeInTheDocument();
  });

  it("explains a swap that has no single item to recommend", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [{
      source: "suggested", archetype: "core", slot_order: ["Base A"],
      situational_swaps: [{ vs_tag: "sustain", swap: "none — anti-heal" }], rationale: "",
    }] }];
    render(panel({ items: swapItems, builds: builds as never }));
    expect(screen.getByText(/no single item covers this/i)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /sustain/i })).toBeDisabled();
  });

  it("hides the situational column for a community build", () => {
    render(panel({ builds: [chironCommunity] }));
    expect(screen.queryByText(/situational/i)).not.toBeInTheDocument();
  });
});

describe("DetailPanel — modes, aspects, starters, mine", () => {
  beforeEach(() => localStorage.clear());

  it("switches build set when the mode toggle changes", () => {
    const builds = [
      { type: "smite-build", god: "Chiron", mode: "Conquest",
        builds: [{ source: "suggested", archetype: "core", slot_order: ["ConItem"], situational_swaps: [], rationale: "c" }] },
      { type: "smite-build", god: "Chiron", mode: "Joust",
        builds: [{ source: "suggested", archetype: "core", slot_order: ["JoustItem"], situational_swaps: [], rationale: "j" }] },
    ];
    function Harness() {
      const [mode, setMode] = React.useState("Conquest");
      return panel({ builds: builds as never, mode, onModeChange: setMode });
    }
    render(<Harness />);
    expect(screen.getByText("ConItem")).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /joust/i }));
    expect(screen.getByText("JoustItem")).toBeInTheDocument();
  });

  const godWithAspect = {
    type: "god", name: "Hercules", pantheon: "Roman", role: "Solo", specializations: [],
    damage_type: "physical", release_date: "", base_stats: {}, abilities: [],
    aspects: [{ name: "Aspect of Preservation", kit_changes: "Becomes an ally-heal tank." }],
    source_url: "", last_verified: "",
  } as never;

  const aspectBuild = () => ([{ type: "smite-build", god: "Hercules", mode: "Conquest", builds: [
    { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
      slot_order: [{ name: "X", pick_rate: 0.5, win_rate: 0.5 }], source_url: "u" },
    { source: "suggested", archetype: "core", slot_order: ["BaseItem"], situational_swaps: [], rationale: "" },
    { source: "suggested", archetype: "core", slot_order: ["AspectItem"], situational_swaps: [], rationale: "",
      aspect: "Aspect of Preservation" },
  ] }]);

  /* The control itself moved to the god's portrait, where SMITE draws it —
     see AspectBadge.tsx and SubjectFrame.test.tsx. This panel is controlled
     now, so what it owes is: given the state, show the right build. */
  it("swaps to the aspect build and shows the kit banner when the state is on", () => {
    const { rerender } = render(
      panel({ god: "Hercules", godData: godWithAspect, builds: aspectBuild() as never,
              aspectOn: false }));
    expect(screen.getByText("BaseItem")).toBeInTheDocument();
    rerender(panel({ god: "Hercules", godData: godWithAspect, builds: aspectBuild() as never,
                     aspectOn: true }));
    expect(screen.getByText("AspectItem")).toBeInTheDocument();
    expect(screen.queryByText("BaseItem")).not.toBeInTheDocument();
    expect(screen.getByText(/ally-heal tank/i)).toBeInTheDocument();
  });

  it("keeps the model build when only the community entry carries an aspect", () => {
    // Regression: the toggle used to appear for any build with an `aspect`
    // field — including community — then emptied the surface when pressed,
    // because only *suggested* aspect builds are selectable. With the control
    // on the portrait the failure mode is the same and quieter: an aspect-on
    // state must not blank a god who has no suggested aspect build.
    const communityAspectOnly = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: "Aspect of the Heroic Tutor", aspect_pick_rate: 0.09,
        aspect_win_rate: 0.45, slot_order: [{ name: "X", pick_rate: 0.5, win_rate: 0.5 }], source_url: "u" },
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "" },
    ] }];
    render(panel({ builds: communityAspectOnly as never, aspectOn: true }));
    expect(screen.getByText("A")).toBeInTheDocument();
  });

  it("shows no aspect toggle for a god with no aspect builds", () => {
    const builds = [{ type: "smite-build", god: "Susano", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "" },
    ] }];
    render(panel({ god: "Susano", builds: builds as never }));
    expect(screen.queryByRole("button", { name: /^aspect/i })).not.toBeInTheDocument();
  });

  it("renders the starter line for a suggested build and for a community one", () => {
    const starter = { base: "Gilded Arrow", upgrade: "Sharpshooter's Arrow" };
    const suggested = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "", starter },
    ] }];
    const { unmount } = render(panel({ builds: suggested as never }));
    expect(screen.getByText(/starter/i)).toBeInTheDocument();
    expect(screen.getByText("Gilded Arrow")).toBeInTheDocument();
    expect(screen.getByText("Sharpshooter's Arrow")).toBeInTheDocument();
    unmount();

    const community = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [{ name: "X", pick_rate: 0.5, win_rate: 0.5 }], source_url: "u", starter },
    ] }];
    render(panel({ builds: community as never }));
    expect(screen.getByText("Gilded Arrow")).toBeInTheDocument();
  });

  it("offers a stored mine build alongside the model's flavors", () => {
    saveMine("Chiron", "Conquest", { name: "My New", slot_order: ["Rage"] });
    const note: BuildNote = { type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["Deathbringer"], situational_swaps: [], rationale: "" } as never,
    ] };
    render(panel({ builds: [note] }));
    const group = within(screen.getByRole("group", { name: /build flavor/i }));
    expect(group.getByRole("button", { name: /My New/i })).toBeInTheDocument();
    // The model's core is still what opens.
    expect(group.getByRole("button", { name: /balanced/i })).toHaveAttribute("aria-pressed", "true");
    expect(screen.getByText("Deathbringer")).toBeInTheDocument();
  });

  it("shows a mine build's items with no meta comparison attached", () => {
    saveMine("Chiron", "Conquest", { name: "mine", slot_order: ["Transcendence", "Devourer's Gauntlet"] });
    render(panel({ builds: [chironCommunity] }));
    fireEvent.click(screen.getByRole("button", { name: /mine/i }));
    expect(screen.getByText("Devourer's Gauntlet")).toBeInTheDocument();
  });
});

describe("DetailPanel — reload resilience", () => {
  beforeEach(() => localStorage.clear());

  function threeEntries(): BuildNote {
    return { type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [{ name: "Transcendence", pick_rate: 0.6, win_rate: 0.49 }], source_url: "u" },
      { source: "suggested", archetype: "crit", slot_order: ["Crit Path Item"], situational_swaps: [], rationale: "crit" },
      { source: "suggested", archetype: "burst", slot_order: ["Burst Path Item"], situational_swaps: [], rationale: "burst" },
    ] as never };
  }

  /** The flavor control, scoped so a build named "Crit Path Item" on the
   * ledger can't be mistaken for the "crit" flavor button. */
  const flavor = (name: RegExp) =>
    within(screen.getByRole("group", { name: /build flavor/i })).getByRole("button", { name });

  it("resets to the first build when entries shrink on reload", () => {
    const { rerender } = render(panel({ builds: [threeEntries()] }));
    fireEvent.click(flavor(/burst/i));
    expect(screen.getByText("Burst Path Item")).toBeInTheDocument();

    const reloaded = threeEntries();
    reloaded.builds = reloaded.builds.slice(0, 2);
    rerender(panel({ builds: [reloaded] }));

    expect(screen.getByText("Crit Path Item")).toBeInTheDocument();
    expect(screen.queryByText("Burst Path Item")).not.toBeInTheDocument();
    expect(flavor(/crit/i)).toHaveAttribute("aria-pressed", "true");
  });

  it("resets rather than pointing a stale index at a different entry when entries reorder", () => {
    const { rerender } = render(panel({ builds: [threeEntries()] }));
    fireEvent.click(flavor(/burst/i));
    expect(screen.getByText("Burst Path Item")).toBeInTheDocument();

    const reordered = threeEntries();
    const [community, a, b] = reordered.builds;
    reordered.builds = [community, b, a];
    rerender(panel({ builds: [reordered] }));

    // Post-reset the first selectable entry wins — never silently whatever
    // now sits at the old index.
    expect(screen.getByText("Burst Path Item")).toBeInTheDocument();
    expect(flavor(/burst/i)).toHaveAttribute("aria-pressed", "true");
  });
});

describe("DetailPanel — popular items", () => {
  beforeEach(() => localStorage.clear());

  it("renders what the playerbase buys, with pick rate", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [{ name: "Transcendence", pick_rate: 0.6, win_rate: 0.5 }], source_url: "u",
        popular_items: [
          { name: "Rod of Tahuti", pick_rate: 0.42, win_rate: 0.55 },
          { name: "Book of Thoth", pick_rate: 0.2, win_rate: 0.56 },
        ] },
    ] }];
    render(panel({ builds: builds as never }));
    expect(screen.getByText(/popular items/i)).toBeInTheDocument();
    expect(screen.getByText("Rod of Tahuti")).toBeInTheDocument();
    expect(screen.getByText(/42% pick/)).toBeInTheDocument();
  });

  it("marks popular items already in the suggested core", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null,
        slot_order: [{ name: "X", pick_rate: 0.5, win_rate: 0.5 }], source_url: "u",
        popular_items: [
          { name: "CoreItem", pick_rate: 0.5, win_rate: 0.5 },
          { name: "OffCoreItem", pick_rate: 0.3, win_rate: 0.5 },
        ] },
      { source: "suggested", archetype: "core", slot_order: ["CoreItem"], situational_swaps: [], rationale: "" },
    ] }];
    render(panel({ builds: builds as never }));
    // Scoped to the popular-items list: "CoreItem" also appears on the ledger.
    const popular = within(screen.getByText(/popular items/i).closest("section")!);
    expect(popular.getByText("CoreItem").closest("li")).toHaveTextContent(/in core/i);
    expect(popular.getByText("OffCoreItem").closest("li")).not.toHaveTextContent(/in core/i);
  });

  it("renders nothing for popular items when the god has no community data", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["Z"], situational_swaps: [], rationale: "" },
    ] }];
    render(panel({ builds: builds as never }));
    expect(screen.queryByText(/popular items/i)).not.toBeInTheDocument();
  });

  it("renders the rationale for a suggested build", () => {
    const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["Deathbringer"], situational_swaps: [],
        rationale: "Top weighted-score core." },
    ] }];
    render(panel({ builds: builds as never }));
    expect(screen.getByText(/Top weighted-score core/)).toBeInTheDocument();
  });
});


/* The mode strip is derived from the notes the god actually has, so a new
 * pipeline mode reaches the page with no viewer change. That's the behaviour
 * worth pinning — it's also what would break if someone hardcoded the list. */
describe("DetailPanel — modes come from the data", () => {
  const modeItems = ["Conquest", "Joust", "Arena"].map((m) => itemFx(`${m} Item`, 2500));
  const threeModes = ["Conquest", "Joust", "Arena"].map((mode) => ({
    type: "smite-build", god: "Chiron", mode,
    builds: [{ source: "suggested", archetype: "core", slot_order: [`${mode} Item`] }],
  }));

  it("offers every mode the god has a note for", () => {
    render(panel({ items: modeItems, builds: threeModes as never, mode: "Conquest" }));
    const group = screen.getByRole("group", { name: "Game mode" });
    expect(within(group).getAllByRole("button").map((b) => b.textContent))
      .toEqual(["Conquest", "Joust", "Arena"]);
  });

  it("renders the requested mode's own build", () => {
    render(panel({ items: modeItems, builds: threeModes as never, mode: "Arena" }));
    expect(screen.getByRole("group", { name: "Game mode" })
      .querySelector('[aria-pressed="true"]')).toHaveTextContent("Arena");
    expect(screen.getByText("Arena Item")).toBeInTheDocument();
    expect(screen.queryByText("Conquest Item")).not.toBeInTheDocument();
  });

  it("orders the strip by the pipeline's list, not by filename", () => {
    // The notes arrive sorted by filename, so Arena leads. Conquest is the
    // primary mode and has to come first — this regressed the moment Arena
    // was added and no test saw it.
    render(panel({ items: modeItems, builds: threeModes as never, mode: "Conquest",
                   modeOrder: ["Conquest", "Joust", "Arena"] }));
    const group = screen.getByRole("group", { name: "Game mode" });
    expect(within(group).getAllByRole("button").map((b) => b.textContent))
      .toEqual(["Conquest", "Joust", "Arena"]);
  });

  it("keeps an unlisted mode rather than dropping it", () => {
    // Only Conquest is ranked; the rest are unknown to the order and hold
    // their original relative position, because the sort is stable. A mode
    // the pipeline forgot to list must still be reachable.
    render(panel({ items: modeItems, builds: threeModes as never, mode: "Conquest",
                   modeOrder: ["Conquest"] }));
    const group = screen.getByRole("group", { name: "Game mode" });
    expect(within(group).getAllByRole("button").map((b) => b.textContent))
      .toEqual(["Conquest", "Joust", "Arena"]);
  });

  it("falls back to the data's own order when the index ships none", () => {
    render(panel({ items: modeItems, builds: threeModes as never, mode: "Conquest" }));
    const group = screen.getByRole("group", { name: "Game mode" });
    expect(within(group).getAllByRole("button").map((b) => b.textContent))
      .toHaveLength(3);
  });

  it("hides the strip when the god has only one mode", () => {
    render(panel({ items: modeItems, builds: [threeModes[0]] as never, mode: "Conquest" }));
    expect(screen.queryByRole("group", { name: "Game mode" })).not.toBeInTheDocument();
  });
});

/* F7. The list was legitimate and unreadable: a median of 25 names against a
 * pool of 226, rendered as prose, ordering invisible, cut-off unstated, and
 * with a mean of 2.8 items already sitting in the core printed above it. */
describe("DetailPanel — underrated for this god", () => {
  beforeEach(() => localStorage.clear());

  const items = [itemFx("A", 2650), itemFx("B", 2350), itemFx("C", 3000)];
  const long = ["C", "D", "E", "F", "G", "H", "I"];
  const withUnderrated = (names: string[]) => ([{
    type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A", "B"], situational_swaps: [],
        rationale: `Top weighted-score core (efficiency + fit + win/pick). Underrated for this god: ${names.join(", ")}.` },
    ],
  }]);

  it("keeps the rationale prose and drops the run-on sentence", () => {
    render(panel({ items, builds: withUnderrated(long) as never }));
    expect(screen.getByText(/top weighted-score core/i)).toBeInTheDocument();
    expect(screen.queryByText(/underrated for this god: C, D/i)).not.toBeInTheDocument();
  });

  it("shows the top five as links, not all of them as text", () => {
    render(panel({ items, builds: withUnderrated(long) as never }));
    for (const n of ["C", "D", "E", "F", "G"]) {
      expect(screen.getByRole("link", { name: n })).toHaveAttribute("href", `#/items/${n}`);
    }
    expect(screen.queryByRole("link", { name: "H" })).not.toBeInTheDocument();
  });

  it("says how many it is showing out of how many there are", () => {
    render(panel({ items, builds: withUnderrated(long) as never }));
    const head = screen.getByRole("heading", { name: /underrated for chiron/i }).parentElement!;
    expect(head).toHaveTextContent(/5 of 7/);
    expect(head).toHaveTextContent(/rarely buy/i);
    expect(screen.getByRole("button", { name: /show all 7/i })).toBeInTheDocument();
  });

  it("hides nothing — the rest are one press away", () => {
    render(panel({ items, builds: withUnderrated(long) as never }));
    fireEvent.click(screen.getByRole("button", { name: /show all 7/i }));
    expect(screen.getByRole("link", { name: "H" })).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "I" })).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /show the top 5/i }));
    expect(screen.queryByRole("link", { name: "H" })).not.toBeInTheDocument();
  });

  /* The part that read as an error: naming the build's own items as things
   * nobody builds, directly under the build. The row already carries
   * `off-meta` for that fact. */
  it("does not name items that are already in the build above it", () => {
    render(panel({ items, builds: withUnderrated(["A", "B", "C", "D"]) as never }));
    const list = screen.getByRole("heading", { name: /underrated for chiron/i }).closest("div")!.parentElement!;
    expect(within(list).queryByRole("link", { name: "A" })).not.toBeInTheDocument();
    expect(within(list).queryByRole("link", { name: "B" })).not.toBeInTheDocument();
    expect(within(list).getByRole("link", { name: "C" })).toBeInTheDocument();
    // ...and the count is of what's left, not of what the pipeline sent.
    expect(screen.queryByRole("button", { name: /show all/i })).not.toBeInTheDocument();
  });

  /* "Underrated" is a claim, and the page that defines it was reachable only
   * from the nav rail. The Seam Rule: name the destination in the reader's
   * terms, where the claim is made. */
  it("routes to the definition of the claim", () => {
    render(panel({ items, builds: withUnderrated(long) as never }));
    expect(screen.getByRole("link", { name: /how that.s decided/i }))
      .toHaveAttribute("href", "#/method");
  });

  it("renders nothing when the rationale carries no list", () => {
    const plain = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [],
        rationale: "For fun — deliberately fights this god's kit." },
    ] }];
    render(panel({ items, builds: plain as never }));
    expect(screen.getByText(/deliberately fights this god/i)).toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /underrated/i })).not.toBeInTheDocument();
  });
});

/* F8. Chronos' Pendant on Ra reads 0.54 in Conquest and 0.62 in Joust, and
 * nothing on the page said the denominator had changed. The per-row caveat
 * names what is missing; it does not say what that does to the number beside
 * it, which is where a reader concludes the build is simply better in Joust. */
describe("DetailPanel — the score's scale across modes", () => {
  beforeEach(() => localStorage.clear());

  const items = [itemFx("A", 2650)];
  const scored = { A: { total: 0.62, efficiency: 0.5, win: 0.5, pick: 0, fit: 0.8 } };
  const joust = [{ type: "smite-build", god: "Chiron", mode: "Joust", builds: [
    { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [],
      rationale: "", slot_scores: scored },
  ] }];
  const conquest = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
    { source: "community", aspect: null, aspect_pick_rate: null, aspect_win_rate: null, source_url: "u",
      slot_order: [{ name: "A", pick_rate: 0.5, win_rate: 0.6 }] },
    { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [],
      rationale: "", slot_scores: scored },
  ] }];
  it("says the score is on a different scale where two signals are missing", () => {
    render(panel({ items, builds: joust as never, mode: "Joust" }));
    const note = screen.getByTestId("mode-scale-note");
    expect(note).toHaveTextContent(/no community data in joust/i);
    expect(note).toHaveTextContent(/own scale/i);
    expect(note).toHaveTextContent(/do not compare/i);
  });

  /* The note must not print weights. `index.json` ships only Conquest's
   * `method.signals`; Joust and Arena carry their own 0.50 / 0.50 in
   * `_weights.yaml` and it is NOT Conquest's 0.35 / 0.15 renormalised, which
   * would read 0.70 / 0.30. Measured on the running app: Spear of Desolation
   * on Ra is 0.79 in Joust, which 0.50 / 0.50 reproduces exactly and the
   * renormalisation misses by 0.09. A number the viewer cannot get right does
   * not belong in a line whose whole job is to be trusted about scale. */
  it("does not state weights the index does not ship", () => {
    render(panel({ items, builds: joust as never, mode: "Joust" }));
    expect(screen.getByTestId("mode-scale-note")).not.toHaveTextContent(/0\.\d\d\s*\/\s*0\.\d\d/);
  });

  it("says nothing in a mode where all four signals are measured", () => {
    render(panel({ items, builds: conquest as never }));
    expect(screen.queryByTestId("mode-scale-note")).not.toBeInTheDocument();
  });
});
