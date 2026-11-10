import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, waitFor, within } from "@testing-library/react";
import { GodGrid } from "./GodGrid";
import { ItemRow } from "./ItemRow";
import type { God } from "../../types";

const gods = [
  { name: "Ra", role: "Mid" }, { name: "Ymir", role: "Support" }, { name: "Hera", role: "Mid" }, { name: "Ares", role: "Support" },
] as God[];

beforeEach(() => window.history.replaceState(null, "", "/#/"));

describe("GodGrid", () => {
  it("asks who you are playing and links every god to its page", () => {
    render(<GodGrid gods={gods} />);
    expect(screen.getByRole("heading", { level: 1, name: "Who are you playing?" })).toBeInTheDocument();
    expect(within(screen.getByTestId("god-grid")).getAllByRole("link")).toHaveLength(4);
    expect(screen.getByRole("link", { name: /^Ra/ })).toHaveAttribute("href", "#/god/Ra");
  });

  it("filters by role, with the filter in the address bar", async () => {
    render(<GodGrid gods={gods} />);
    fireEvent.click(screen.getByRole("button", { name: "Support" }));
    expect(within(screen.getByTestId("god-grid")).getAllByRole("link").map((a) => a.textContent))
      .toEqual(["AresSupport", "YmirSupport"]);
    await waitFor(() => expect(window.location.hash).toContain("role=Support"));
  });

  it("puts names that start with the query first", () => {
    render(<GodGrid gods={gods} />);
    // The search box is the command field now; a plain name still filters.
    fireEvent.change(screen.getByRole("combobox", { name: /^Search gods/ }), { target: { value: "ra" } });
    expect(within(screen.getByTestId("god-grid")).getAllByRole("link").map((a) => a.getAttribute("href")))
      .toEqual(["#/god/Ra", "#/god/Hera"]);
  });

  /* A list of gods, not matchups (Jacob, 2026-11-09): portrait and name, the
   * last god first, each reopening the god in the mode and aspect it was last
   * on, and saying so only when that isn't the default. No enemies. */
  it("lists the recent gods above the grid, each saying and linking to what a tap gives", () => {
    render(<GodGrid gods={gods} onClearRecents={() => {}} recents={[
      { god: "Ymir", mode: "conquest", aspect: false },
      { god: "Nobody", mode: "conquest", aspect: false },
      { god: "Ra", mode: "joust", aspect: true },
      { god: "Hera", mode: "conquest", aspect: true },
      { god: "Ares", mode: "arena", aspect: false },
    ]} />);
    const row = within(screen.getByTestId("recents"));
    expect(row.getAllByRole("link").map((a) => [a.textContent, a.getAttribute("href")])).toEqual([
      ["Ymir", "#/god/Ymir"],
      ["RaJoust · Aspect", "#/god/Ra?mode=joust&aspect=1"],
      ["HeraAspect", "#/god/Hera?aspect=1"],
      ["AresArena", "#/god/Ares?mode=arena"],
    ]);
    expect(screen.queryByRole("link", { name: /Back to/ })).not.toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Clear" })).toBeInTheDocument();
  });

  it("hides the recent gods while the roster is filtered", () => {
    render(<GodGrid gods={gods} recents={[{ god: "Ymir", mode: "conquest", aspect: false }]} />);
    fireEvent.click(screen.getByRole("button", { name: "Mid" }));
    expect(screen.queryByTestId("recents")).not.toBeInTheDocument();
  });
});

describe("ItemRow", () => {
  it("marks a draft swap and keeps its reason, with gold spent", () => {
    render(<ol><ItemRow position={3} name="Divine Ruin" cumulativeGold={7300} swapped
      reason={{ tone: "swap", text: "Swapped in for Spear of the Magus — brings anti-heal" }} /></ol>);
    const row = screen.getByTestId("item-row");
    expect(row).toHaveAttribute("data-swapped", "true");
    expect(row).toHaveClass("lock-in");
    expect(row).toHaveTextContent("Swapped in for Spear of the Magus — brings anti-heal");
    expect(row).toHaveTextContent("7,300");
  });
});
