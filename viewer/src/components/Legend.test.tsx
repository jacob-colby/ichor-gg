import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent, cleanup } from "@testing-library/react";
import { Legend } from "./Legend";
import { DetailPanel } from "./DetailPanel";
import { tabLabel } from "../lib/builds";
import type { Item } from "../types";

describe("Legend", () => {
  it("renders content and calls onClose when dismissed", () => {
    const onClose = vi.fn();
    render(<Legend onClose={onClose} />);
    expect(screen.getByText(/how this works/i)).toBeInTheDocument();
    expect(screen.getByText(/gold efficiency/i)).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "Got it" }));
    expect(onClose).toHaveBeenCalled();
  });

  it("is a real dialog, labelled by its heading", () => {
    render(<Legend onClose={vi.fn()} />);
    const dialog = screen.getByRole("dialog");
    expect(dialog).toHaveAttribute("aria-modal", "true");
    expect(dialog).toHaveAccessibleName(/how this works/i);
  });

  it("moves focus into the dialog on open", () => {
    render(<Legend onClose={vi.fn()} />);
    expect(document.activeElement).toBe(screen.getByRole("heading", { name: /how this works/i }));
  });

  it("closes on Escape", () => {
    const onClose = vi.fn();
    render(<Legend onClose={onClose} />);
    fireEvent.keyDown(document, { key: "Escape" });
    expect(onClose).toHaveBeenCalled();
  });

  it("closes from the ✕ control as well as the confirm button", () => {
    const onClose = vi.fn();
    render(<Legend onClose={onClose} />);
    fireEvent.click(screen.getByRole("button", { name: /close/i }));
    expect(onClose).toHaveBeenCalled();
  });

  it("wraps Tab at the end of the dialog so focus never reaches the page behind", () => {
    render(<Legend onClose={vi.fn()} />);
    const buttons = screen.getAllByRole("button");
    const last = buttons[buttons.length - 1];
    last.focus();
    fireEvent.keyDown(document, { key: "Tab" });
    expect(document.activeElement).toBe(buttons[0]);
  });

  it("restores focus to whatever opened it", () => {
    const opener = document.createElement("button");
    document.body.appendChild(opener);
    opener.focus();

    const { unmount } = render(<Legend onClose={vi.fn()} />);
    expect(document.activeElement).not.toBe(opener);
    unmount();
    expect(document.activeElement).toBe(opener);

    opener.remove();
  });

  /* The footer used to carry this on every screen, forever — 43px of permanent
   * chrome for something you read once. It has to actually be findable here. */
  it("carries the attribution and the disclaimer the footer used to hold", () => {
    render(<Legend onClose={vi.fn()} />);
    expect(screen.getByRole("link", { name: /wiki\.smite2\.com/i })).toHaveAttribute("href", "https://wiki.smite2.com");
    expect(screen.getByRole("link", { name: /smitebrain/i })).toHaveAttribute("href", "https://smitebrain.com");
    expect(screen.getByText(/not affiliated with Hi-Rez/i)).toBeInTheDocument();
  });
});

/* The 2026-08-23 audit (F3) found this dialog teaching four things that were
 * not true of the app: the model-versus-meta positioning retired on evidence
 * on 2026-08-05, a "Suggested" tab, a "BUILD ORDER" heading, and an aspect
 * claim true for 7 gods of 73. None of them were wrong when written; the
 * surfaces moved and the copy did not, and the `?` dialog is where a lost
 * visitor goes first. Each string is pinned here against the thing it
 * describes rather than against itself, so the next move breaks a test.
 */
describe("Legend — the copy describes the app that shipped", () => {
  const legendText = () => {
    render(<Legend onClose={vi.fn()} />);
    const t = screen.getByRole("dialog").textContent ?? "";
    cleanup();
    return t;
  };

  /* PRODUCT.md: "The positioning changed on 2026-08-05 and the old version
   * must not come back." Home ranks on real win rates; this dialog used to
   * open by telling the visitor it ranks by model-versus-meta disagreement. */
  it("never restores the retired model-versus-meta positioning", () => {
    expect(legendText()).not.toMatch(/how far our model and the community|meta disagree|underrate/i);
  });

  it("describes Home the way Home's own h1 describes itself", () => {
    expect(legendText()).toMatch(/never on anything this site models/i);
  });

  /* The strip reads Model / Hybrid / Community / Balanced / flavours. There
   * has never been a "Suggested" tab in the shipped shell. */
  it("names no build tab the app cannot produce", () => {
    const text = legendText();
    expect(text).not.toMatch(/Suggested/);
    for (const label of ["Model", "Community", "Hybrid", "Balanced"]) {
      expect(text).toContain(label);
    }
  });

  it("names build tabs that tabLabel actually emits", () => {
    const text = legendText();
    const emitted = [
      tabLabel({ source: "suggested", archetype: "model" } as never),
      tabLabel({ source: "suggested", archetype: "hybrid" } as never),
      tabLabel({ source: "suggested", archetype: "core" } as never),
      tabLabel({ source: "community" } as never),
    ];
    for (const label of emitted) expect(text).toContain(label);
  });

  /* The heading is "Buy order" set uppercase by CSS; the dialog said BUILD
   * ORDER. Cross-checked against the panel that renders it rather than
   * asserted twice against the same literal. */
  it("calls the ledger heading what the ledger heading is called", () => {
    expect(legendText()).toMatch(/BUY ORDER/);
    expect(legendText()).not.toMatch(/BUILD ORDER/);

    const items = [{ type: "item", name: "A", tier: 3, cost: 2650, stats: {}, passive: "",
      builds_from: [], builds_into: [], source_url: "", last_verified: "",
      effect_tags: [], efficiency_tier: null }] as unknown as Item[];
    const builds = [{ type: "smite-build", god: "Ra", mode: "Conquest", builds: [
      { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [], rationale: "" },
    ] }];
    render(<DetailPanel god="Ra" items={items} builds={builds as never}
      mode="Conquest" onModeChange={() => {}} />);
    expect(screen.getByRole("heading", { name: /buy order/i })).toBeInTheDocument();
  });

  /* 7 gods of the 73 with an aspect have a scoring overlay behind it. The
   * dialog promised all 73 a different build. It must not promise that again
   * — and it must not go the other way and claim the toggle does nothing,
   * which is false for the 7 and for the kit text on all of them. */
  it("does not promise every aspect a different build", () => {
    const text = legendText();
    expect(text).not.toMatch(/swaps to that god.s aspect build/i);
    expect(text).toMatch(/kit text/i);
    expect(text).toMatch(/leaves the six items alone|does not change the build|most gods/i);
  });

  /* The band on an unmeasured tier list reads NOT MEASURED. "Unmeasured" and
   * "bad" being different facts is PRODUCT.md Principle 3, and the word the
   * dialog teaches should be the word on the page. */
  it("uses the site's own word for an unranked entry", () => {
    expect(legendText()).toMatch(/not measured/i);
  });

  it("points at the working, in the visitor's terms", () => {
    render(<Legend onClose={vi.fn()} />);
    const seam = screen.getByTestId("legend-method-seam");
    expect(seam).toHaveAttribute("href", "#/method");
    expect(seam.textContent).not.toMatch(/^\s*method\s*(→|->)?\s*$/i);
  });

  it("closes itself on the way out, so the page behind is reachable", () => {
    const onClose = vi.fn();
    render(<Legend onClose={onClose} />);
    fireEvent.click(screen.getByTestId("legend-method-seam"));
    expect(onClose).toHaveBeenCalled();
  });
});
