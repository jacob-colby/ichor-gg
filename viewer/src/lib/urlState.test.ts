import { describe, it, expect, beforeEach } from "vitest";
import { renderHook, act, waitFor } from "@testing-library/react";
import { hashPath, hashQuery, queryString, keepQuery, flushQuery, useUrlState } from "./urlState";

interface F { q: string; lane?: string }
const decode = (p: URLSearchParams): F => ({ q: p.get("q") ?? "", lane: p.get("lane") ?? undefined });
const encode = (f: F) => ({ q: f.q || undefined, lane: f.lane });

function setHash(h: string) {
  window.history.replaceState(null, "", `/${window.location.search}${h}`);
}

describe("hashPath / hashQuery", () => {
  it("splits a hash carrying a query", () => {
    expect(hashPath("#/items/Bloodforge?q=blood")).toBe("#/items/Bloodforge");
    expect(hashQuery("#/items?q=blood&tier=3").get("q")).toBe("blood");
  });

  it("treats a bare hash as an empty query rather than throwing", () => {
    expect([...hashQuery("#/items").keys()]).toEqual([]);
    expect(hashQuery("").get("q")).toBeNull();
  });

  it("falls back to the root path for an empty hash", () => {
    expect(hashPath("")).toBe("#/");
  });
});

describe("queryString", () => {
  it("drops empty values so a pristine view keeps a clean URL", () => {
    expect(queryString({ q: "", lane: undefined, tier: "3" })).toBe("?tier=3");
    expect(queryString({ q: "", lane: undefined })).toBe("");
  });

  it("encodes values that need it", () => {
    expect(queryString({ q: "Nu Wa" })).toBe("?q=Nu+Wa");
  });
});

describe("keepQuery", () => {
  it("carries the live query onto a new path", () => {
    expect(keepQuery("#/items/Bloodforge", "#/items?q=blood&tier=3")).toBe("#/items/Bloodforge?q=blood&tier=3");
  });

  it("leaves a path alone when nothing is filtered", () => {
    expect(keepQuery("#/items/Bloodforge", "#/items")).toBe("#/items/Bloodforge");
  });

  it("discards a query the path itself carried, using the live one", () => {
    expect(keepQuery("#/god/Ra?stale=1", "#/god/Anubis?lane=Mid")).toBe("#/god/Ra?lane=Mid");
  });
});

describe("useUrlState", () => {
  beforeEach(() => setHash("#/items"));

  it("reads initial state out of the URL", () => {
    setHash("#/items?q=blood&lane=Mid");
    const { result } = renderHook(() => useUrlState(decode, encode));
    expect(result.current[0]).toEqual({ q: "blood", lane: "Mid" });
  });

  it("writes state back to the hash without touching the path", async () => {
    setHash("#/items/Bloodforge");
    const { result } = renderHook(() => useUrlState(decode, encode));
    act(() => result.current[1]({ q: "blood" }));
    await waitFor(() => expect(window.location.hash).toBe("#/items/Bloodforge?q=blood"));
  });

  it("clears the query entirely when every field returns to its default", async () => {
    setHash("#/items?q=blood");
    const { result } = renderHook(() => useUrlState(decode, encode));
    act(() => result.current[1]({ q: "" }));
    await waitFor(() => expect(window.location.hash).toBe("#/items"));
  });

  it("accepts an updater, like useState", async () => {
    const { result } = renderHook(() => useUrlState(decode, encode));
    act(() => result.current[1]({ q: "a" }));
    act(() => result.current[1]((prev) => ({ ...prev, lane: "Mid" })));
    expect(result.current[0]).toEqual({ q: "a", lane: "Mid" });
    await waitFor(() => expect(window.location.hash).toBe("#/items?q=a&lane=Mid"));
  });

  /* Browsers rate-limit history writes — Safari throws above 100 replaceState
   * calls per 30s — and a search box bound to the URL writes once per
   * keystroke. The state is immediate; only the address bar is queued. */
  it("coalesces a burst of edits into one history write", () => {
    setHash("#/items");
    const { result } = renderHook(() => useUrlState(decode, encode));
    const before = window.location.hash;
    act(() => { for (const q of ["s", "sp", "spe", "spea", "spear"]) result.current[1]({ q }); });
    expect(result.current[0].q).toBe("spear");
    expect(window.location.hash).toBe(before);   // nothing written yet
    act(() => flushQuery());
    expect(window.location.hash).toBe("#/items?q=spear");
  });

  // A click inside the debounce window must not compose its destination from
  // a query the address bar hasn't received yet.
  it("flushes a queued write before keepQuery reads the address bar", () => {
    setHash("#/items");
    const { result } = renderHook(() => useUrlState(decode, encode));
    act(() => result.current[1]({ q: "blood" }));
    expect(keepQuery("#/items/Bloodforge")).toBe("#/items/Bloodforge?q=blood");
  });

  /* Queueing the write opens a window in which the address bar is a step
   * behind the state. A `hashchange` landing inside it — a path change, or an
   * event queued before the edit — shows the *old* query, and adopting that
   * threw away what the visitor had just typed. */
  it("keeps a queued edit when a stale hashchange lands mid-debounce", () => {
    setHash("#/items?lane=Mid");
    const { result } = renderHook(() => useUrlState(decode, encode));
    act(() => result.current[1]({ q: "blood", lane: "Mid" }));
    act(() => window.dispatchEvent(new HashChangeEvent("hashchange")));  // URL still ?lane=Mid
    expect(result.current[0].q).toBe("blood");
    act(() => flushQuery());
    expect(window.location.hash).toBe("#/items?q=blood&lane=Mid");
  });

  // The other half of the same rule: an event that genuinely changes the query
  // is a navigation, and it must win over whatever is queued.
  it("lets a real navigation supersede a queued edit", () => {
    setHash("#/items");
    const { result } = renderHook(() => useUrlState(decode, encode));
    act(() => result.current[1]({ q: "blood" }));
    act(() => {
      setHash("#/items?q=spear");
      window.dispatchEvent(new HashChangeEvent("hashchange"));
    });
    expect(result.current[0].q).toBe("spear");
    act(() => flushQuery());
    expect(window.location.hash).toBe("#/items?q=spear");
  });

  it("writes a pending edit out when the view unmounts", () => {
    setHash("#/items");
    const { result, unmount } = renderHook(() => useUrlState(decode, encode));
    act(() => result.current[1]({ q: "blood" }));
    unmount();
    expect(window.location.hash).toBe("#/items?q=blood");
  });

  it("adopts a draft that arrives by hashchange — a pasted link", () => {
    const { result } = renderHook(() => useUrlState(decode, encode));
    act(() => {
      setHash("#/items?q=spear");
      window.dispatchEvent(new HashChangeEvent("hashchange"));
    });
    expect(result.current[0].q).toBe("spear");
  });

  // Regression: opening an item from a filtered shelf changes the path and
  // fires `hashchange` while carrying the same query. Decoding that as a reset
  // wiped the filters that produced the card the visitor just clicked.
  it("survives a path change that keeps the query", () => {
    setHash("#/items?q=blood");
    const { result } = renderHook(() => useUrlState(decode, encode));
    act(() => {
      setHash("#/items/Bloodforge?q=blood");
      window.dispatchEvent(new HashChangeEvent("hashchange"));
    });
    expect(result.current[0].q).toBe("blood");
  });

  it("does not write a query onto a URL that never had one", () => {
    setHash("#/items");
    renderHook(() => useUrlState(decode, encode));
    expect(window.location.hash).toBe("#/items");
  });
});
