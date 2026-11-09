import { describe, it, expect, vi } from "vitest";
import { useState } from "react";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { EnemySheet } from "./EnemySheet";
import { godMatches } from "../command/query";
import type { God } from "../../types";

const god = (name: string): God => ({ name, role: "Mid" }) as unknown as God;
const GODS = ["Ra", "Rama", "Hera", "Hecate", "Hel", "Hercules", "Ymir", "Baron Samedi", "Achilles"].map(god);

/** The sheet over a team held in state, as the god page and the board hold it. */
function Harness({ start, startIndex = 0, onPick, onClose, side }: {
  start: string[]; startIndex?: number; onPick?: (i: number, n: string) => void; onClose?: () => void; side?: "enemy" | "ally";
}) {
  const [team, setTeam] = useState(start);
  const [open, setOpen] = useState(true);
  if (!open) return <p>closed: {team.join(",")}</p>;
  return (
    <EnemySheet gods={GODS} enemies={team} startIndex={startIndex} side={side}
      onPick={(i, n) => { onPick?.(i, n); setTeam((t) => t.map((x, j) => (j === i ? n : x))); }}
      onRemove={(i) => setTeam((t) => t.map((x, j) => (j === i ? "" : x)))}
      onClose={() => { onClose?.(); setOpen(false); }} />
  );
}

const field = () => screen.getByRole("searchbox");
const type = (text: string) => fireEvent.change(field(), { target: { value: text } });
/** fireEvent returns false when a handler called preventDefault. */
const tab = (opts: { shiftKey?: boolean } = {}) => !fireEvent.keyDown(document.activeElement ?? field(), { key: "Tab", ...opts });

describe("EnemySheet — a typed name and Tab, the way the search bar completes", () => {
  it("takes the top match on Tab, fills the slot and moves to the next empty one", () => {
    const onPick = vi.fn();
    render(<Harness start={["", "", "", "", ""]} onPick={onPick} />);
    expect(field()).toHaveFocus();
    type("hec");
    expect(tab()).toBe(true);
    expect(onPick).toHaveBeenCalledWith(0, "Hecate");
    expect(screen.getByRole("dialog", { name: "Enemy 2 of 5" })).toBeInTheDocument();
    expect(within(screen.getByRole("group", { name: "Enemy slots" })).getByRole("button", { name: "Slot 1: Hecate" }))
      .toBeInTheDocument();
    // The next slot starts fresh, with the keyboard still up.
    expect(field()).toHaveValue("");
    expect(field()).toHaveFocus();
  });

  it("ranks a typed word exactly as the search bar does, so Tab takes the bar's top suggestion", () => {
    const onPick = vi.fn();
    render(<Harness start={["", "", "", "", ""]} onPick={onPick} />);
    // "he": the bar puts the shortest name first (Hel); the sheet's old A–Z
    // starts-with list put Hecate first.
    expect(godMatches("he", GODS)[0].name).toBe("Hel");
    type("he");
    const gods = within(screen.getByRole("list", { name: "Gods" })).getAllByRole("button").map((b) => b.getAttribute("aria-label"));
    expect(gods).toEqual(godMatches("he", GODS).map((g) => g.name));
    tab();
    expect(onPick).toHaveBeenLastCalledWith(0, "Hel");
    // "sam" lands on a later word of a multi-word name, as it does in the bar.
    type("sam");
    tab();
    expect(onPick).toHaveBeenLastCalledWith(1, "Baron Samedi");
  });

  it("leaves Tab as navigation while nothing is typed", () => {
    const onPick = vi.fn();
    render(<Harness start={["", "", "", "", ""]} onPick={onPick} />);
    expect(tab()).toBe(false);
    type("   ");
    expect(tab()).toBe(false);
    expect(onPick).not.toHaveBeenCalled();
    expect(screen.getByRole("dialog", { name: "Enemy 1 of 5" })).toBeInTheDocument();
  });

  it("leaves Shift+Tab as navigation even with a name typed", () => {
    const onPick = vi.fn();
    render(<Harness start={["", "", "", "", ""]} onPick={onPick} />);
    type("hec");
    expect(tab({ shiftKey: true })).toBe(false);
    expect(onPick).not.toHaveBeenCalled();
  });

  it("keeps the Sheet's focus trap: Tab off the last control wraps to the first", () => {
    render(<Harness start={["", "", "", "", ""]} />);
    const dialog = screen.getByRole("dialog");
    const done = within(dialog).getByRole("button", { name: "Done" });
    done.focus();
    expect(tab()).toBe(true);
    expect(within(dialog).getByRole("button", { name: "Close" })).toHaveFocus();
  });

  it("skips a god already on the team, as the bar skips an enemy already typed", () => {
    const onPick = vi.fn();
    render(<Harness start={["Ra", "", "", "", ""]} startIndex={1} onPick={onPick} />);
    type("ra");
    tab();
    expect(onPick).toHaveBeenCalledWith(1, "Rama");
  });

  it("takes nothing when the only match is already picked, and Tab navigates", () => {
    const onPick = vi.fn();
    render(<Harness start={["Ymir", "", "", "", ""]} startIndex={1} onPick={onPick} />);
    type("ymir");
    expect(screen.getByRole("button", { name: "Ymir (already on their team)" })).toBeDisabled();
    expect(tab()).toBe(false);
    expect(onPick).not.toHaveBeenCalled();
  });

  it("fills a three-slot Joust team in three names, then closes", () => {
    const onPick = vi.fn();
    const onClose = vi.fn();
    render(<Harness start={["", "", ""]} onPick={onPick} onClose={onClose} />);
    expect(screen.getByRole("dialog", { name: "Enemy 1 of 3" })).toBeInTheDocument();
    expect(within(screen.getByRole("group", { name: "Enemy slots" })).getAllByRole("button")).toHaveLength(3);
    type("ymi"); tab();
    type("hec"); tab();
    expect(screen.getByRole("dialog", { name: "Enemy 3 of 3" })).toBeInTheDocument();
    type("ach"); tab();
    expect(onPick.mock.calls).toEqual([[0, "Ymir"], [1, "Hecate"], [2, "Achilles"]]);
    expect(onClose).toHaveBeenCalledTimes(1);
    expect(screen.getByText("closed: Ymir,Hecate,Achilles")).toBeInTheDocument();
  });

  it("re-filling an occupied slot by Tab is an edit: it closes rather than advancing", () => {
    const onClose = vi.fn();
    render(<Harness start={["Ymir", "", "", "", ""]} startIndex={0} onClose={onClose} />);
    type("hec");
    tab();
    expect(onClose).toHaveBeenCalledTimes(1);
    expect(screen.getByText("closed: Hecate,,,,")).toBeInTheDocument();
  });

  it("adds on Enter the same god Tab would", () => {
    const onPick = vi.fn();
    render(<Harness start={["", "", "", "", ""]} onPick={onPick} />);
    type("he");
    fireEvent.keyDown(field(), { key: "Enter" });
    expect(onPick).toHaveBeenCalledWith(0, "Hel");
  });

  it("works on your own team's slots on the draft board", () => {
    const onPick = vi.fn();
    render(<Harness side="ally" start={["Ra", "", "", "", ""]} startIndex={1} onPick={onPick} />);
    expect(screen.getByRole("dialog", { name: "Ally 2 of 5" })).toBeInTheDocument();
    type("ra");
    tab();
    // You are on this team, so the mirror is a duplicate here.
    expect(onPick).toHaveBeenCalledWith(1, "Rama");
  });
});
