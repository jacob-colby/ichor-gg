import { describe, it, expect, vi, beforeEach } from "vitest";
import { renderHook, act } from "@testing-library/react";
import { useDraft, decodeDraftHash, encodeDraftHash } from "./draft";

const KEY = "smite:draft";

describe("useDraft", () => {
  beforeEach(() => {
    localStorage.clear();
    window.location.hash = "";
  });

  it("starts empty: conquest mode, 5 ally slots, 5 enemy slots, all blank", () => {
    const { result } = renderHook(() => useDraft());
    expect(result.current.mode).toBe("conquest");
    expect(result.current.draft.allies).toEqual(["", "", "", "", ""]);
    expect(result.current.draft.enemies).toEqual(["", "", "", "", ""]);
  });

  it("setAlly places a god at the given slot without disturbing others", () => {
    const { result } = renderHook(() => useDraft());
    act(() => result.current.setAlly(1, "Ymir"));
    expect(result.current.draft.allies).toEqual(["", "Ymir", "", "", ""]);
    expect(result.current.draft.enemies).toEqual(["", "", "", "", ""]);
  });

  it("setEnemy places a god at the given slot without disturbing others", () => {
    const { result } = renderHook(() => useDraft());
    act(() => result.current.setEnemy(3, "Agni"));
    expect(result.current.draft.enemies).toEqual(["", "", "", "Agni", ""]);
  });

  it("clear empties both rows but keeps the current mode", () => {
    const { result } = renderHook(() => useDraft());
    act(() => result.current.setMode("joust"));
    act(() => result.current.setAlly(0, "Ymir"));
    act(() => result.current.setEnemy(0, "Agni"));
    act(() => result.current.clear());
    expect(result.current.mode).toBe("joust");
    expect(result.current.draft.allies).toEqual(["", "", ""]);
    expect(result.current.draft.enemies).toEqual(["", "", ""]);
  });

  it("persists to localStorage under smite:draft", () => {
    const { result } = renderHook(() => useDraft());
    act(() => result.current.setAlly(0, "Ymir"));
    const raw = localStorage.getItem(KEY);
    expect(raw).not.toBeNull();
    expect(JSON.parse(raw!)).toEqual({
      mode: "conquest",
      allies: ["Ymir", "", "", "", ""],
      enemies: ["", "", "", "", ""],
    });
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
    expect(result.current.draft.allies).toEqual(["", "", "", "", ""]);
    expect(result.current.draft.enemies).toEqual(["", "", "", "", ""]);
  });

  it("setMode truncates extra slots rather than clearing the draft", () => {
    const { result } = renderHook(() => useDraft());
    act(() => {
      result.current.setAlly(0, "A1");
      result.current.setAlly(1, "A2");
      result.current.setAlly(2, "A3");
      result.current.setAlly(3, "A4");
      result.current.setAlly(4, "A5");
      result.current.setEnemy(0, "E1");
      result.current.setEnemy(4, "E5");
    });
    act(() => result.current.setMode("joust"));
    expect(result.current.mode).toBe("joust");
    expect(result.current.draft.allies).toEqual(["A1", "A2", "A3"]);
    expect(result.current.draft.enemies).toEqual(["E1", "", ""]);
  });

  it("restores truncated entries when the mode grows back, so a mode switch isn't lossy", () => {
    // A Conquest→Joust→Conquest round trip used to silently destroy slots 4-5
    // with no warning and no undo.
    const { result } = renderHook(() => useDraft());
    act(() => {
      result.current.setAlly(0, "A1");
      result.current.setAlly(3, "A4");
      result.current.setAlly(4, "A5");
      result.current.setEnemy(4, "E5");
    });
    act(() => result.current.setMode("joust"));
    expect(result.current.draft.allies).toEqual(["A1", "", ""]);

    act(() => result.current.setMode("conquest"));
    expect(result.current.draft.allies).toEqual(["A1", "", "", "A4", "A5"]);
    expect(result.current.draft.enemies).toEqual(["", "", "", "", "E5"]);
  });

  it("pads with empties when growing into a mode nothing was ever truncated from", () => {
    const { result } = renderHook(() => useDraft());
    act(() => result.current.setMode("joust"));
    act(() => {
      result.current.setAlly(0, "A1");
      result.current.setMode("conquest");
    });
    expect(result.current.draft.allies).toEqual(["A1", "", "", "", ""]);
  });

  it("with syncUrl, a #/draft URL carrying god names wins over localStorage on load", () => {
    localStorage.setItem(KEY, JSON.stringify({ mode: "conquest", allies: ["LocalGod", "", "", "", ""], enemies: [] }));
    window.location.hash = "#/draft?m=joust&me=UrlGod&e=Enemy1";
    const { result } = renderHook(() => useDraft({ syncUrl: true }));
    expect(result.current.mode).toBe("joust");
    expect(result.current.draft.allies).toEqual(["UrlGod", "", ""]);
    expect(result.current.draft.enemies).toEqual(["Enemy1", "", ""]);
  });

  it("with syncUrl, a bare #/draft URL (no god names) does not clobber localStorage", () => {
    localStorage.setItem(KEY, JSON.stringify({ mode: "conquest", allies: ["LocalGod", "", "", "", ""], enemies: [] }));
    window.location.hash = "#/draft";
    const { result } = renderHook(() => useDraft({ syncUrl: true }));
    expect(result.current.draft.allies[0]).toBe("LocalGod");
  });

  it("without syncUrl, a #/draft URL is ignored and localStorage wins", () => {
    localStorage.setItem(KEY, JSON.stringify({ mode: "conquest", allies: ["LocalGod", "", "", "", ""], enemies: [] }));
    window.location.hash = "#/draft?m=joust&me=UrlGod";
    const { result } = renderHook(() => useDraft());
    expect(result.current.draft.allies[0]).toBe("LocalGod");
  });

  it("with syncUrl, entering a draft updates the URL via replaceState, never pushState", () => {
    const replaceSpy = vi.spyOn(window.history, "replaceState");
    const pushSpy = vi.spyOn(window.history, "pushState");
    window.location.hash = "#/draft";
    const { result } = renderHook(() => useDraft({ syncUrl: true }));
    act(() => result.current.setAlly(0, "Agni"));
    expect(replaceSpy).toHaveBeenCalled();
    expect(pushSpy).not.toHaveBeenCalled();
    const lastCall = replaceSpy.mock.calls.at(-1)!;
    expect(String(lastCall[2])).toContain("me=Agni");
    replaceSpy.mockRestore();
    pushSpy.mockRestore();
  });

  it("with syncUrl, unknown god names from the URL are dropped via isKnownGod", () => {
    window.location.hash = "#/draft?m=conquest&me=Bogus&a=Ymir";
    const { result } = renderHook(() =>
      useDraft({ syncUrl: true, isKnownGod: (n) => n === "Ymir" }),
    );
    expect(result.current.draft.allies).toEqual(["", "Ymir", "", "", ""]);
  });

  it("without syncUrl, changes never touch the URL hash", () => {
    window.location.hash = "#/god/Chiron";
    const { result } = renderHook(() => useDraft());
    act(() => result.current.setAlly(0, "Agni"));
    expect(window.location.hash).toBe("#/god/Chiron");
  });
});

describe("decodeDraftHash / encodeDraftHash", () => {
  it("round-trips mode + allies (incl. the you slot) + enemies", () => {
    const draft = { allies: ["Agni", "Ymir", "", "", ""], enemies: ["Loki", "Thor", "", "", ""] };
    const hash = encodeDraftHash("conquest", draft);
    const decoded = decodeDraftHash(hash);
    expect(decoded).toEqual({ mode: "conquest", allies: draft.allies, enemies: draft.enemies });
  });

  it("omits empty rows from the encoded query", () => {
    const hash = encodeDraftHash("joust", { allies: ["Agni", "", ""], enemies: ["", "", ""] });
    expect(hash).toBe("#/draft?m=joust&me=Agni");
  });

  it("returns null for a hash that isn't the draft route", () => {
    expect(decodeDraftHash("#/god/Chiron")).toBeNull();
    expect(decodeDraftHash("#/")).toBeNull();
  });

  it("returns null for a bare draft hash with no god names, so localStorage isn't clobbered", () => {
    expect(decodeDraftHash("#/draft")).toBeNull();
    expect(decodeDraftHash("#/draft?m=joust")).toBeNull();
  });

  it("drops unknown/untracked god names when isKnownGod is supplied", () => {
    const known = new Set(["Agni", "Loki"]);
    const decoded = decodeDraftHash("#/draft?m=conquest&me=Agni&a=Bogus&e=Loki,NotReal", (n) => known.has(n));
    expect(decoded?.allies[0]).toBe("Agni");
    expect(decoded?.allies[1]).toBe(""); // Bogus dropped
    expect(decoded?.enemies).toEqual(["Loki", "", "", "", ""]);
  });
});

describe("useDraft — shared links arriving without a remount", () => {
  beforeEach(() => { localStorage.clear(); window.location.hash = ""; });

  it("re-decodes when the hash changes under a mounted board", () => {
    // Opening a shared link while the app is already loaded fires hashchange,
    // not a remount — the board used to keep showing the old draft (wrong mode
    // and all) while the address bar showed the new one.
    window.location.hash = "#/draft?m=conquest&me=Agni&e=Ymir";
    const { result } = renderHook(() => useDraft({ syncUrl: true }));
    expect(result.current.draft.allies[0]).toBe("Agni");

    act(() => {
      window.location.hash = "#/draft?m=joust&me=Thor&e=Loki";
      window.dispatchEvent(new HashChangeEvent("hashchange"));
    });
    expect(result.current.mode).toBe("joust");
    expect(result.current.draft.allies[0]).toBe("Thor");
    expect(result.current.draft.enemies[0]).toBe("Loki");
  });

  it("ignores a hashchange that decodes to the draft already on screen", () => {
    window.location.hash = "#/draft?m=conquest&me=Agni";
    const { result } = renderHook(() => useDraft({ syncUrl: true }));
    const before = result.current.draft;
    act(() => window.dispatchEvent(new HashChangeEvent("hashchange")));
    // Same object identity — no needless re-render, and no feedback loop with
    // our own replaceState.
    expect(result.current.draft).toBe(before);
  });

  it("does not listen when syncUrl is off", () => {
    window.location.hash = "#/draft?m=conquest&me=Agni";
    const { result } = renderHook(() => useDraft());
    act(() => {
      window.location.hash = "#/draft?m=joust&me=Thor";
      window.dispatchEvent(new HashChangeEvent("hashchange"));
    });
    expect(result.current.draft.allies[0]).toBe("");
  });
});
