import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, waitFor, within } from "@testing-library/react";
import App from "../../App";
import { toHash } from "../../lib/useHashRoute";
import { SIX, THEIRS, comparison, atUrl, serve } from "./godFixtures";

beforeEach(() => {
  localStorage.clear();
  atUrl(toHash.god("Ra"));
  serve(comparison());
});

const rowNames = () => within(screen.getByTestId("six")).getAllByTestId("item-row")
  .map((r) => within(r).getByTestId("item-name").textContent?.replace(/^\d+\.\s*/, ""));

describe("God page — the answer", () => {
  it("says the comparison in one honest sentence under the header", async () => {
    render(<App />);
    const line = await screen.findByTestId("verdict-line", {}, { timeout: 2000 });
    await waitFor(() => expect(line).toHaveTextContent(
      "The community's six deals 7% more damage; survival is about even. Lotus Sickle isn't simulated yet, so the damage gap is partly unmeasured."));
  });

  it("lists Ichor's six in buy order with gold spent and a reason in words", async () => {
    render(<App />);
    await screen.findByTestId("six");
    expect(rowNames()).toEqual(SIX);
    const rows = screen.getAllByTestId("item-row");
    expect(rows[0]).toHaveTextContent("Ra's players don't buy this");
    expect(rows[0]).toHaveTextContent("2,150");
    expect(rows[1]).toHaveTextContent("55% of Ra players buy it first");
    expect(rows[1]).toHaveTextContent("4,800");
    expect(rows[5]).toHaveTextContent("worth more than it costs");
    expect(screen.getByTestId("starter")).toHaveTextContent("Conduit Gem → Archmage's Gem");
  });

  it("swaps to the community's six in place, and back", async () => {
    render(<App />);
    const show = await screen.findByRole("button", { name: /Show theirs/ });
    fireEvent.click(show);
    expect(rowNames()).toEqual(THEIRS);
    expect(screen.getByRole("heading", { name: /The community's six/ })).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /Show Ichor's/ }));
    expect(rowNames()).toEqual(SIX);
  });

  it("prints no 0-1 score anywhere on the page, even in the opened detail", async () => {
    render(<App />);
    await screen.findByRole("button", { name: /Show theirs/ });
    for (const d of document.querySelectorAll("details")) d.open = true;
    expect(screen.getByTestId("compare-detail")).toBeInTheDocument();
    expect(document.querySelector("main")!.textContent).not.toMatch(/\b0\.\d+/);
  });

  it("withholds the call when coverage fails, in words", async () => {
    serve(comparison({ verdict: "not enough simulated",
      coverage: { ichor: 0.4, community: 1, gap: 0.6, ok: false, reason: "too much unsimulated" } }));
    render(<App />);
    await waitFor(() => expect(screen.getByTestId("verdict-line")).toHaveTextContent(/isn't measured enough to call/));
    expect(screen.getByTestId("verdict-line")).not.toHaveTextContent(/%/);
  });

  it("says when a god has no comparison at all", async () => {
    serve(null);
    render(<App />);
    await waitFor(() => expect(screen.getByTestId("verdict-line")).toHaveTextContent("There's no measured comparison for Ra yet."));
    expect(screen.queryByRole("button", { name: /Show theirs/ })).not.toBeInTheDocument();
  });
});

describe("God page — controls", () => {
  it("says in one line when the aspect doesn't change the build", async () => {
    render(<App />);
    const sw = await screen.findByRole("switch", { name: /Aspect of Thermotherapy/ });
    expect(sw).toHaveAttribute("aria-checked", "false");
    fireEvent.click(sw);
    expect(screen.getByTestId("aspect-note")).toHaveTextContent(/doesn't change Ra's six/);
    await waitFor(() => expect(window.location.hash).toContain("aspect=1"));
  });

  it("puts other builds behind a disclosure and swaps the six in place", async () => {
    render(<App />);
    const other = await screen.findByTestId("other-builds");
    fireEvent.click(within(other).getByRole("button", { name: /Burst/ }));
    await waitFor(() => expect(rowNames()[5]).toBe("Book of Thoth"));
    // The comparison is for the main six only, and the sentence says so.
    expect(screen.getByTestId("verdict-line")).toHaveTextContent(/measured for Ichor's main six/);
    await waitFor(() => expect(window.location.hash).toContain("build=burst"));
  });

  it("is for browsing: no enemy team here, one way into your match", async () => {
    localStorage.setItem("smite:draft", JSON.stringify({ mode: "conquest", allies: ["Ymir"], enemies: ["Ymir"] }));
    render(<App />);
    await screen.findByTestId("six");
    // The six is the god's own, not adapted to the match's enemies.
    expect(rowNames()).toEqual(SIX);
    expect(screen.queryByTestId("enemy-strip")).not.toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /Use in my match/ }));
    await waitFor(() => expect(window.location.hash).toBe("#/"));
    const stored = JSON.parse(localStorage.getItem("smite:draft") ?? "{}");
    expect(stored.allies[0]).toBe("Ra");
    expect(stored.enemies[0]).toBe("Ymir");
  });
});
