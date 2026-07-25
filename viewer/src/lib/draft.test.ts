import { describe, it, expect, beforeEach } from "vitest";
import { renderHook, act } from "@testing-library/react";
import { useDraft } from "./draft";

const KEY = "smite:draft";

describe("useDraft", () => {
  beforeEach(() => localStorage.clear());

  it("starts empty: 4 ally slots, 5 enemy slots, all blank", () => {
    const { result } = renderHook(() => useDraft());
    expect(result.current.draft.allies).toEqual(["", "", "", ""]);
    expect(result.current.draft.enemies).toEqual(["", "", "", "", ""]);
  });

  it("setAlly places a god at the given slot without disturbing others", () => {
    const { result } = renderHook(() => useDraft());
    act(() => result.current.setAlly(1, "Ymir"));
    expect(result.current.draft.allies).toEqual(["", "Ymir", "", ""]);
    expect(result.current.draft.enemies).toEqual(["", "", "", "", ""]);
  });

  it("setEnemy places a god at the given slot without disturbing others", () => {
    const { result } = renderHook(() => useDraft());
    act(() => result.current.setEnemy(3, "Agni"));
    expect(result.current.draft.enemies).toEqual(["", "", "", "Agni", ""]);
  });

  it("clear empties both rows", () => {
    const { result } = renderHook(() => useDraft());
    act(() => result.current.setAlly(0, "Ymir"));
    act(() => result.current.setEnemy(0, "Agni"));
    act(() => result.current.clear());
    expect(result.current.draft.allies).toEqual(["", "", "", ""]);
    expect(result.current.draft.enemies).toEqual(["", "", "", "", ""]);
  });

  it("persists to localStorage under smite:draft", () => {
    const { result } = renderHook(() => useDraft());
    act(() => result.current.setAlly(0, "Ymir"));
    const raw = localStorage.getItem(KEY);
    expect(raw).not.toBeNull();
    expect(JSON.parse(raw!)).toEqual({ allies: ["Ymir", "", "", ""], enemies: ["", "", "", "", ""] });
  });

  it("round-trips through localStorage: a fresh hook picks up the persisted draft", () => {
    const { result: first } = renderHook(() => useDraft());
    act(() => first.current.setEnemy(4, "Agni"));

    const { result: second } = renderHook(() => useDraft());
    expect(second.current.draft.enemies).toEqual(["", "", "", "", "Agni"]);
  });

  it("ignores a corrupt/malformed persisted value instead of throwing", () => {
    localStorage.setItem(KEY, "not json");
    const { result } = renderHook(() => useDraft());
    expect(result.current.draft.allies).toEqual(["", "", "", ""]);
    expect(result.current.draft.enemies).toEqual(["", "", "", "", ""]);
  });
});
