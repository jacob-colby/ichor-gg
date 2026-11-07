import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { AppNav } from "./AppNav";

/* The header stamp, against a pinned clock so the text is exact. Only `Date`
 * is faked: testing-library's timers stay real. */
beforeEach(() => {
  vi.useFakeTimers({ toFake: ["Date"] });
  vi.setSystemTime(new Date(2026, 10, 7, 12)); // 2026-11-07, local noon
});
afterEach(() => vi.useRealTimers());

const nav = (props: Partial<Parameters<typeof AppNav>[0]> = {}) =>
  render(<AppNav active="gods" onHelp={() => {}} dataUpdated="2026-11-06" dataPatch="Open Beta 47"
    search={<input aria-label="Search" />} {...props} />);

describe("AppNav freshness stamp", () => {
  it("shows the compact form in the bar, the sentence to a screen reader, and the date on hover", () => {
    nav();
    const stamp = screen.getByTestId("header-freshness");
    const [shown, spoken] = Array.from(stamp.children);
    expect(shown).toHaveTextContent(/^OB47 · 1d$/);
    expect(shown).toHaveAttribute("aria-hidden", "true");
    expect(spoken).toHaveTextContent(/^Updated yesterday · Open Beta 47$/);
    expect(spoken).toHaveClass("sr-only");
    expect(stamp).toHaveAttribute("title", "Updated yesterday (2026-11-06) · Open Beta 47");
  });

  it("leads with Updated when there is no patch label", () => {
    nav({ dataPatch: undefined });
    const [shown, spoken] = Array.from(screen.getByTestId("header-freshness").children);
    expect(shown).toHaveTextContent(/^Updated 1d$/);
    expect(spoken).toHaveTextContent(/^Updated yesterday$/);
  });

  it("is omitted when the index has no date", () => {
    nav({ dataUpdated: undefined });
    expect(screen.queryByTestId("header-freshness")).not.toBeInTheDocument();
  });

  it("keeps the whole sentence in the phone's More sheet", () => {
    nav();
    fireEvent.click(screen.getByRole("button", { name: "More" }));
    const sheet = within(screen.getByRole("dialog", { name: "More" }));
    expect(sheet.getByText(/^Updated yesterday · Open Beta 47\./)).toBeInTheDocument();
  });

  /* jsdom has no layout, so the geometry (measured in the PR at 1024–1920px)
   * can't be asserted here. What can: the stamp sits in the bar's middle with
   * the reading links, all of them marked to step aside for the open field,
   * and Help outside it, never covered. */
  it("puts the stamp and the reading links in the middle the open field covers, and Help outside it", () => {
    nav();
    const middle = screen.getByTestId("nav-middle");
    expect(middle).toHaveClass("@container/bar");
    expect(within(middle).getByRole("search")).toBeInTheDocument();
    const covered = Array.from(middle.querySelectorAll("a, [data-testid='header-freshness']"));
    expect(covered.map((e) => e.textContent)).toEqual(
      ["Tiers", "Items", "Patch notes", "Method", "OB47 · 1dUpdated yesterday · Open Beta 47"]);
    covered.forEach((e) => expect(e).toHaveClass("under-field"));
    expect(middle).not.toContainElement(screen.getByRole("button", { name: "Help and credits" }));
  });
});
