import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { DraftBar } from "./DraftBar";
import type { God, ThreatModel, DraftComp } from "../types";

const god = (name: string, damage_type = "physical"): God =>
  ({ name, damage_type, specializations: [], pantheon: "", role: "",
     base_stats: {}, abilities: [], aspects: [] } as unknown as God);

const GODS = [god("Ymir"), god("Agni", "magical")];
const EMPTY_DRAFT: DraftComp = { allies: ["", "", "", ""], enemies: ["", "", "", "", ""] };
const EMPTY_THREATS: ThreatModel = {
  magical: 0, physical: 0, healers: 0, lockdown: 0, crit: 0, tanks: 0,
  enemyCount: 0, allyCovers: {}, allyAllPhysical: false,
};

describe("DraftBar", () => {
  it("renders 4 ally slots and 5 enemy slots, all empty with Add labels", () => {
    render(<DraftBar gods={GODS} draft={EMPTY_DRAFT} onSetAlly={() => {}} onSetEnemy={() => {}} onClear={() => {}} threats={EMPTY_THREATS} />);
    for (let i = 1; i <= 4; i++) expect(screen.getByLabelText(`Add ally ${i}`)).toBeInTheDocument();
    for (let i = 1; i <= 5; i++) expect(screen.getByLabelText(`Add enemy ${i}`)).toBeInTheDocument();
  });

  it("shows a filled slot's name and a Change aria-label", () => {
    const draft = { ...EMPTY_DRAFT, enemies: ["Ymir", "", "", "", ""] };
    render(<DraftBar gods={GODS} draft={draft} onSetAlly={() => {}} onSetEnemy={() => {}} onClear={() => {}} threats={EMPTY_THREATS} />);
    expect(screen.getByLabelText("Change enemy 1 (Ymir)")).toBeInTheDocument();
    expect(screen.getByText("Ymir")).toBeInTheDocument();
  });

  it("clicking an empty slot opens the god picker; picking a god fills that slot", () => {
    const onSetEnemy = vi.fn();
    render(<DraftBar gods={GODS} draft={EMPTY_DRAFT} onSetAlly={() => {}} onSetEnemy={onSetEnemy} onClear={() => {}} threats={EMPTY_THREATS} />);
    fireEvent.click(screen.getByLabelText("Add enemy 3"));
    expect(screen.getByPlaceholderText(/search/i)).toBeInTheDocument();
    fireEvent.click(screen.getByText("Ymir"));
    expect(onSetEnemy).toHaveBeenCalledWith(2, "Ymir");
  });

  it("clicking an ally slot fills the ally row, not the enemy row", () => {
    const onSetAlly = vi.fn();
    render(<DraftBar gods={GODS} draft={EMPTY_DRAFT} onSetAlly={onSetAlly} onSetEnemy={() => {}} onClear={() => {}} threats={EMPTY_THREATS} />);
    fireEvent.click(screen.getByLabelText("Add ally 2"));
    fireEvent.click(screen.getByText("Agni"));
    expect(onSetAlly).toHaveBeenCalledWith(1, "Agni");
  });

  it("filters the god picker by search text", () => {
    render(<DraftBar gods={GODS} draft={EMPTY_DRAFT} onSetAlly={() => {}} onSetEnemy={() => {}} onClear={() => {}} threats={EMPTY_THREATS} />);
    fireEvent.click(screen.getByLabelText("Add enemy 1"));
    fireEvent.change(screen.getByPlaceholderText(/search/i), { target: { value: "agn" } });
    expect(screen.getByText("Agni")).toBeInTheDocument();
    expect(screen.queryByText("Ymir")).not.toBeInTheDocument();
  });

  it("renders threat chips only for non-zero threats", () => {
    const threats = { ...EMPTY_THREATS, magical: 5, healers: 2 };
    render(<DraftBar gods={GODS} draft={EMPTY_DRAFT} onSetAlly={() => {}} onSetEnemy={() => {}} onClear={() => {}} threats={threats} />);
    expect(screen.getByText(/5 magical/)).toBeInTheDocument();
    expect(screen.getByText(/2 healer/)).toBeInTheDocument();
    expect(screen.queryByText(/physical/)).not.toBeInTheDocument();
    expect(screen.queryByText(/CC/)).not.toBeInTheDocument();
  });

  it("renders no threat chips for an all-zero threat model", () => {
    render(<DraftBar gods={GODS} draft={EMPTY_DRAFT} onSetAlly={() => {}} onSetEnemy={() => {}} onClear={() => {}} threats={EMPTY_THREATS} />);
    expect(screen.queryByText(/magical/)).not.toBeInTheDocument();
    expect(screen.queryByText(/healer/)).not.toBeInTheDocument();
  });

  it("shows a Clear button when the draft has any entry, and it calls onClear", () => {
    const onClear = vi.fn();
    const draft = { ...EMPTY_DRAFT, enemies: ["Ymir", "", "", "", ""] };
    render(<DraftBar gods={GODS} draft={draft} onSetAlly={() => {}} onSetEnemy={() => {}} onClear={onClear} threats={EMPTY_THREATS} />);
    fireEvent.click(screen.getByRole("button", { name: /clear/i }));
    expect(onClear).toHaveBeenCalled();
  });

  it("hides the Clear button when the draft is entirely empty", () => {
    render(<DraftBar gods={GODS} draft={EMPTY_DRAFT} onSetAlly={() => {}} onSetEnemy={() => {}} onClear={() => {}} threats={EMPTY_THREATS} />);
    expect(screen.queryByRole("button", { name: /clear/i })).not.toBeInTheDocument();
  });

  it("is collapsible: toggling the header hides the slot rows", () => {
    render(<DraftBar gods={GODS} draft={EMPTY_DRAFT} onSetAlly={() => {}} onSetEnemy={() => {}} onClear={() => {}} threats={EMPTY_THREATS} />);
    expect(screen.getByLabelText("Add ally 1")).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /draft/i }));
    expect(screen.queryByLabelText("Add ally 1")).not.toBeInTheDocument();
  });
});
