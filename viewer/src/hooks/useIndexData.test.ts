import { describe, it, expect, vi, beforeEach } from "vitest";
import { renderHook, waitFor, act } from "@testing-library/react";
import { useIndexData } from "./useIndexData";

const fakeIndex = { gods: [{ name: "Chiron" }], items: [], builds: [] };

beforeEach(() => {
  vi.stubGlobal(
    "fetch",
    vi.fn().mockResolvedValue({
      ok: true,
      json: () => Promise.resolve(fakeIndex),
    }),
  );
});

describe("useIndexData", () => {
  it("fetches index.json on mount", async () => {
    const { result } = renderHook(() => useIndexData());
    await waitFor(() => expect(result.current.data).not.toBeNull());
    expect(result.current.data?.gods[0].name).toBe("Chiron");
    expect(fetch).toHaveBeenCalledWith("/index.json", { cache: "no-store" });
  });

  it("re-fetches when reload() is called", async () => {
    const { result } = renderHook(() => useIndexData());
    await waitFor(() => expect(result.current.data).not.toBeNull());

    await act(async () => {
      await result.current.reload();
    });

    expect(fetch).toHaveBeenCalledTimes(2);
  });

  it("sets an error message if the fetch fails", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ ok: false, status: 404 }));
    const { result } = renderHook(() => useIndexData());
    await waitFor(() => expect(result.current.error).not.toBeNull());
    expect(result.current.data).toBeNull();
  });
});
