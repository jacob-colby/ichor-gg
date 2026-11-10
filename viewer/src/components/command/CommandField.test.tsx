import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent, cleanup } from "@testing-library/react";
import { CommandField } from "./CommandField";
import type { God } from "../../types";

const god = (name: string, aspect?: string): God =>
  ({ name, role: "Mid", aspects: aspect ? [{ name: aspect }] : [] }) as unknown as God;
const GODS = [god("Ra", "Aspect of Thermotherapy"), god("Ares"), god("Artemis"), god("Hecate"), god("Ymir"), god("Hel")];

const setup = (props: Partial<Parameters<typeof CommandField>[0]> = {}) => {
  const onSubmit = vi.fn();
  render(<CommandField gods={GODS} variant="bar" label="Search" placeholder="ra vs hecate" onSubmit={onSubmit} {...props} />);
  return { field: screen.getByRole("combobox", { name: "Search" }), onSubmit };
};
const chips = (kind: string) => [...document.querySelectorAll(`[data-chip='${kind}']`)].map((c) => c.textContent);

/* A second mode replaces the first. The parser always READ the last mode as
 * the mode, but the field kept every mode word it was given, so "ra joust
 * arena" showed two mode chips and the note "Two modes typed — using Arena"
 * (before 2026-11-09). The earlier word now leaves the text when the later one
 * is committed, so one chip is left and it is the mode the query runs in. */
describe("CommandField — a second mode replaces the first", () => {
  it("typed: 'ra joust arena ' leaves one mode chip, Arena", () => {
    const { field } = setup();
    fireEvent.change(field, { target: { value: "ra joust arena " } });
    expect(chips("mode")).toEqual(["Arena"]);
    expect(chips("you")).toEqual(["Ra"]);
    expect(chips("unknown")).toEqual([]);
    expect(screen.queryByTestId("query-notes")).not.toBeInTheDocument();
  });

  it("typed a word at a time, the way a player types it", () => {
    const { field } = setup();
    for (const w of ["ra ", "joust ", "arena "]) fireEvent.change(field, { target: { value: w } });
    expect(chips("mode")).toEqual(["Arena"]);
  });

  it("picked: choosing a mode suggestion while a mode chip exists swaps it", () => {
    const { field } = setup();
    fireEvent.change(field, { target: { value: "ra joust " } });
    expect(chips("mode")).toEqual(["Joust"]);
    fireEvent.click(screen.getByRole("option", { name: /Arena/ }));
    expect(chips("mode")).toEqual(["Arena"]);
    expect(field).toHaveValue("");
  });

  it("Tab-completed: 'aren' + Tab takes Arena and drops Joust", () => {
    const { field } = setup();
    fireEvent.change(field, { target: { value: "ra joust aren" } });
    fireEvent.keyDown(field, { key: "Tab" });
    expect(chips("mode")).toEqual(["Arena"]);
  });

  it("keeps the enemies and the rest of the query, and submits the mode left on screen", () => {
    const { field, onSubmit } = setup();
    fireEvent.change(field, { target: { value: "ra vs hecate joust ymir arena " } });
    expect(chips("enemy")).toEqual(["Hecate", "Ymir"]);
    expect(chips("mode")).toEqual(["Arena"]);
    fireEvent.keyDown(field, { key: "Enter" });
    expect(onSubmit).toHaveBeenCalledWith(expect.objectContaining({ you: "Ra", enemies: ["Hecate", "Ymir"], mode: "arena" }));
  });

  it("a linked query with two modes opens on the last one", () => {
    setup({ seedText: "ra joust arena" });
    expect(chips("mode")).toEqual(["Arena"]);
  });

  it("touches only mode words: the aspect chip stays", () => {
    const { field } = setup();
    fireEvent.change(field, { target: { value: "ra aspect joust arena " } });
    expect(chips("aspect")).toEqual(["Aspect"]);
    expect(chips("mode")).toEqual(["Arena"]);
  });
});

/* Jacob, 2026-11-09: the aspect is marked with the game's orange hexagon
 * everywhere, the same `AspectHex` as the god page's switch. */
describe("CommandField — the aspect chip", () => {
  const hexes = (kind: string) => [...document.querySelectorAll(`[data-chip='${kind}'] svg[data-aspect-hex]`)]
    .map((s) => s.getAttribute("data-aspect-hex"));

  it("leads with the aspect's hexagon: filled for Aspect, the outline for No aspect", () => {
    const { field } = setup();
    fireEvent.change(field, { target: { value: "ra aspect joust " } });
    expect(chips("aspect")).toEqual(["Aspect"]);
    expect(hexes("aspect")).toEqual(["on"]);
    expect(hexes("mode")).toEqual([]);
    fireEvent.change(field, { target: { value: "no aspect " } });
    expect(chips("aspect")).toEqual(["No aspect"]);
    expect(hexes("aspect")).toEqual(["off"]);
  });

  /* Jacob, 2026-11-09: never both. The last aspect word wins, as the last
   * mode does, so the field shows the one the query runs on. */
  it("keeps one aspect chip, the last word's, however it is typed", () => {
    for (const [text, left, on] of [
      ["ra aspect no aspect ", ["No aspect"], false], ["ra no aspect aspect ", ["Aspect"], true],
      ["ra aspect aspect ", ["Aspect"], true], ["ra aspect off ", ["No aspect"], false],
    ] as const) {
      cleanup();
      const { field, onSubmit } = setup();
      fireEvent.change(field, { target: { value: text } });
      expect(document.querySelectorAll("[data-chip]").length).toBe(2);
      expect(chips("aspect")).toEqual(left);
      expect(chips("you")).toEqual(["Ra"]);
      fireEvent.keyDown(field, { key: "Enter" });
      expect(onSubmit).toHaveBeenCalledWith(expect.objectContaining({ you: "Ra", enemies: [], aspect: on }));
    }
  });

  it("'Aspect off' writes the off state itself: the on chip goes, one No aspect chip is left", () => {
    const { field } = setup();
    fireEvent.change(field, { target: { value: "ra aspect " } });
    fireEvent.click(screen.getByRole("option", { name: /Aspect off/ }));
    expect(chips("aspect")).toEqual(["No aspect"]);
    expect(field).toHaveValue("");
  });

  it("draws the hexagon on the aspect suggestion row: filled to turn it on, the outline for Aspect off", () => {
    const { field } = setup();
    const rowHex = (name: RegExp) => screen.getByRole("option", { name }).querySelector("svg[data-aspect-hex]")
      ?.getAttribute("data-aspect-hex");
    fireEvent.change(field, { target: { value: "ra asp" } });
    expect(rowHex(/Aspect of Thermotherapy/)).toBe("on");
    // No boxed "A" left beside it.
    expect(screen.getByRole("option", { name: /Aspect of Thermotherapy/ }).querySelector("span[aria-hidden='true']")?.textContent).toBe("");
    fireEvent.change(field, { target: { value: "ra aspect " } });
    expect(rowHex(/Aspect off/)).toBe("off");
    // The mode rows keep their letter.
    expect(screen.getByRole("option", { name: /Joust/ }).querySelector("svg[data-aspect-hex]")).toBeNull();
  });
});
