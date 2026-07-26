import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { SubjectSearch } from "./SubjectSearch";
import { searchSubjects, type Hit } from "../lib/subjectSearch";
import { toHash } from "../lib/useHashRoute";
import type { God, Item } from "../types";

const gods = [
  { name: "Agni", pantheon: "Hindu", role: "Mid", damage_type: "magical" },
  { name: "Zeus", pantheon: "Greek", role: "Mid", damage_type: "magical" },
  { name: "Ymir", pantheon: "Norse", role: "Solo", damage_type: "magical" },
] as unknown as God[];

const items = [
  { name: "Rage", cost: 2500 },
  { name: "Aegis", cost: 2100 },
  { name: "Zeal", cost: 1900 },
] as unknown as Item[];

const search = () => within(screen.getByTestId("subject-search"));

beforeEach(() => { window.location.hash = ""; });

/* Four "Search gods…" fields with four behaviours became one field that
 * reaches both nouns the product has — "Rage" is as likely a thing to be
 * looking for as "Ra". */
describe("SubjectSearch — one field, both nouns", () => {
  it("finds gods and items in the same list", () => {
    render(<SubjectSearch gods={gods} items={items} />);
    fireEvent.change(search().getByRole("combobox"), { target: { value: "ze" } });
    expect(search().getByRole("option", { name: /zeus/i })).toBeInTheDocument();
    expect(search().getByRole("option", { name: /zeal/i })).toBeInTheDocument();
  });

  it("navigates to a god", () => {
    render(<SubjectSearch gods={gods} items={items} />);
    fireEvent.change(search().getByRole("combobox"), { target: { value: "zeu" } });
    fireEvent.click(search().getByRole("option", { name: /zeus/i }));
    expect(window.location.hash).toBe(toHash.god("Zeus"));
  });

  it("navigates to an item", () => {
    render(<SubjectSearch gods={gods} items={items} />);
    fireEvent.change(search().getByRole("combobox"), { target: { value: "rage" } });
    fireEvent.click(search().getByRole("option", { name: /rage/i }));
    expect(window.location.hash).toBe(toHash.item("Rage"));
  });

  it("exposes combobox semantics so the list is reachable and announced", () => {
    render(<SubjectSearch gods={gods} items={items} />);
    const input = search().getByRole("combobox");
    expect(input).toHaveAttribute("aria-expanded", "false");
    fireEvent.change(input, { target: { value: "z" } });
    expect(input).toHaveAttribute("aria-expanded", "true");
    expect(search().getByRole("listbox")).toBeInTheDocument();
    expect(screen.getByText(/\d+ results?/i)).toBeInTheDocument();
  });

  it("moves the active option with the arrow keys and submits the active one", () => {
    render(<SubjectSearch gods={gods} items={items} />);
    const input = search().getByRole("combobox");
    fireEvent.change(input, { target: { value: "z" } });   // Zeus, Zeal
    expect(search().getAllByRole("option")[0]).toHaveAttribute("aria-selected", "true");
    fireEvent.keyDown(input, { key: "ArrowDown" });
    expect(search().getAllByRole("option")[1]).toHaveAttribute("aria-selected", "true");
    fireEvent.submit(input.closest("form")!);
    expect(window.location.hash).toBe(toHash.item("Zeal"));
  });

  it("wraps the active option around both ends of the list", () => {
    render(<SubjectSearch gods={gods} items={items} />);
    const input = search().getByRole("combobox");
    fireEvent.change(input, { target: { value: "z" } });
    fireEvent.keyDown(input, { key: "ArrowUp" });
    const options = search().getAllByRole("option");
    expect(options[options.length - 1]).toHaveAttribute("aria-selected", "true");
  });

  it("says so when nothing matches instead of rendering an empty list", () => {
    render(<SubjectSearch gods={gods} items={items} />);
    fireEvent.change(search().getByRole("combobox"), { target: { value: "qqqq" } });
    expect(search().getByText(/nothing called/i)).toBeInTheDocument();
    expect(search().queryAllByRole("option")).toHaveLength(0);
  });

  it("dismisses the overlay when focus leaves the combobox", () => {
    render(<SubjectSearch gods={gods} items={items} />);
    const wrapper = screen.getByTestId("subject-search");
    fireEvent.change(within(wrapper).getByRole("combobox"), { target: { value: "zeu" } });
    expect(within(wrapper).getByRole("listbox")).toBeInTheDocument();
    fireEvent.blur(wrapper, { relatedTarget: document.body });
    expect(within(wrapper).queryByRole("listbox")).not.toBeInTheDocument();
  });

  it("clears the query on Escape", () => {
    render(<SubjectSearch gods={gods} items={items} />);
    const input = search().getByRole("combobox") as HTMLInputElement;
    fireEvent.change(input, { target: { value: "zeu" } });
    fireEvent.keyDown(input, { key: "Escape" });
    expect(input.value).toBe("");
    expect(search().queryByRole("listbox")).not.toBeInTheDocument();
  });
});

describe("searchSubjects — ranking", () => {
  it("puts an exact match first, then prefixes, then substrings", () => {
    const hits = searchSubjects(gods, [{ name: "Zea", cost: 1 }, { name: "Amazeal", cost: 1 }] as unknown as Item[], "zea");
    expect(hits.map((h: Hit) => h.name)).toEqual(["Zea", "Amazeal"]);
  });

  // The product's subject outranks its components; an exact item match still
  // surfaces, because it sorts to the top of its own group.
  it("leads with gods", () => {
    const hits = searchSubjects(gods, items, "e");
    expect(hits[0].kind).toBe("god");
    expect(hits.some((h: Hit) => h.kind === "item")).toBe(true);
  });

  it("returns nothing for an empty query rather than the whole index", () => {
    expect(searchSubjects(gods, items, "")).toEqual([]);
    expect(searchSubjects(gods, items, "   ")).toEqual([]);
  });

  it("caps the list so the overlay never becomes the page", () => {
    const many = Array.from({ length: 40 }, (_, i) => ({ name: `Aa${i}` })) as unknown as God[];
    expect(searchSubjects(many, [], "aa").length).toBeLessThanOrEqual(8);
  });
});
