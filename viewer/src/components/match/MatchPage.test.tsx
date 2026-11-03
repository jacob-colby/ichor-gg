import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, waitFor, within } from "@testing-library/react";
import App from "../../App";
import { SIX, THEIRS, comparison, atUrl, serve } from "../second/godFixtures";

const seed = (allies: string[], enemies: string[] = [], mode = "conquest") =>
  localStorage.setItem("smite:draft", JSON.stringify({ mode, allies, enemies }));

beforeEach(() => {
  localStorage.clear();
  atUrl("#/");
  serve(comparison());
});

const rowNames = () => within(screen.getByTestId("six")).getAllByTestId("item-row")
  .map((r) => within(r).getByTestId("item-name").textContent?.replace(/^\d+\.\s*/, ""));

describe("Match board — empty", () => {
  it("is the slots themselves: your slot asks, five enemy slots wait, no build is faked", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Your match" });
    expect(screen.getByRole("button", { name: /Who are you playing\?/ })).toBeInTheDocument();
    expect(within(screen.getByTestId("enemy-strip")).getAllByRole("button", { name: /Add enemy/ })).toHaveLength(5);
    expect(screen.queryByTestId("item-row")).not.toBeInTheDocument();
    expect(screen.queryByTestId("verdict-line")).not.toBeInTheDocument();
  });

  it("keeps allies folded away behind one button", async () => {
    render(<App />);
    await screen.findByRole("heading", { level: 1, name: "Your match" });
    expect(screen.queryByTestId("ally-row")).not.toBeInTheDocument();
    const toggle = screen.getByRole("button", { name: "Add allies" });
    expect(toggle).toHaveAttribute("aria-expanded", "false");
    fireEvent.click(toggle);
    expect(within(screen.getByTestId("ally-row")).getAllByRole("button", { name: /Add ally/ })).toHaveLength(4);
  });
});

describe("Match board — land, your god, the enemy team, one screen", () => {
  it("picks your god from a sheet with the keyboard up, and the six fills in under the slots", async () => {
    render(<App />);
    fireEvent.click(await screen.findByRole("button", { name: /Who are you playing\?/ }));
    const sheet = await screen.findByRole("dialog", { name: "Who are you playing?" });
    const search = within(sheet).getByRole("searchbox");
    expect(search).toHaveFocus();
    fireEvent.change(search, { target: { value: "ra" } });
    fireEvent.keyDown(search, { key: "Enter" });
    await waitFor(() => expect(screen.queryByRole("dialog")).not.toBeInTheDocument());
    await screen.findByTestId("six");
    expect(rowNames()).toEqual(SIX);
    expect(screen.getByTestId("god-record")).toHaveTextContent("Tier B on 1,286 Conquest games");
    // No route change: still the board.
    expect(window.location.hash).toBe("#/");
    expect(JSON.parse(localStorage.getItem("smite:draft") ?? "{}").allies[0]).toBe("Ra");
  });

  it("adds enemies from the board without leaving it, auto-advancing slot to slot", async () => {
    seed(["Ra"]);
    render(<App />);
    await screen.findByTestId("six");
    fireEvent.click(screen.getByRole("button", { name: "Add enemy 1" }));
    const sheet = await screen.findByRole("dialog", { name: /Enemy 1 of 5/ });
    expect(within(sheet).getByRole("searchbox")).toHaveFocus();
    fireEvent.click(within(sheet).getByRole("button", { name: "Ymir" }));
    await screen.findByRole("dialog", { name: /Enemy 2 of 5/ });
    await waitFor(() => expect(JSON.parse(localStorage.getItem("smite:draft") ?? "{}").enemies[0]).toBe("Ymir"));
    fireEvent.click(screen.getByRole("button", { name: "Done" }));
    expect(screen.getByRole("button", { name: "Enemy 1: Ymir. Change" })).toBeInTheDocument();
    expect(window.location.hash).toBe("#/");
    // The six is still on the same screen under the board.
    expect(screen.getByTestId("six")).toBeInTheDocument();
  });

  it("swaps to the community's six in place, under the board", async () => {
    seed(["Ra"]);
    render(<App />);
    fireEvent.click(await screen.findByRole("button", { name: /Show theirs/ }));
    expect(rowNames()).toEqual(THEIRS);
    expect(screen.getByTestId("match-board")).toBeInTheDocument();
  });
});

describe("Match board — mode", () => {
  it("has five enemy slots in Conquest, three in Joust, and keeps the mode in the address bar", async () => {
    seed(["Ra"]);
    render(<App />);
    await screen.findByTestId("six");
    fireEvent.click(screen.getByRole("button", { name: "Joust" }));
    await waitFor(() => expect(within(screen.getByTestId("enemy-strip")).getAllByRole("button", { name: /Add enemy/ })).toHaveLength(3));
    expect(screen.getByTestId("god-record")).toHaveTextContent("No win data in Joust — model only");
    await waitFor(() => expect(window.location.hash).toBe("#/?mode=joust"));
  });

  it("opens a linked mode", async () => {
    seed(["Ra"]);
    atUrl("#/?mode=arena");
    render(<App />);
    await waitFor(() => expect(screen.getByRole("button", { name: "Arena" })).toHaveAttribute("aria-pressed", "true"));
    expect(screen.getByTestId("god-record")).toHaveTextContent("No win data in Arena — model only");
  });
});
