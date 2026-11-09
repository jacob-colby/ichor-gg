import { describe, expect, it } from "vitest";
import { fireEvent, render, screen } from "@testing-library/react";
import { RecentBuilds } from "./RecentBuilds";
import type { RecentBuild, RecentFile } from "../../lib/recentBuilds";

const NOW = Date.parse("2026-11-09T12:00:00Z");
const mk = (i: number, o: Partial<RecentBuild> = {}): RecentBuild => ({
  t: `2026-11-08T${String(i % 24).padStart(2, "0")}:00:00Z`, win: i % 2 === 0, role: i % 3 === 0 ? "Carry" : "Mid",
  master: i % 5 === 0, aspect: i % 7 === 0 ? null : "Aspect of Combustion", patch: i < 10 ? "ob47" : "ob46",
  items: ["Book of Thoth", "Rod of Tahuti"], starter: "Conduit Gem", relic: "Aegis of Acceleration", ...o,
});
const file = (n: number): RecentFile => ({
  god: "agni", kept: n, aspects: ["Aspect of Combustion"], patches: ["ob47", "ob46"], roles: ["Carry", "Mid"],
  builds: Array.from({ length: n }, (_, i) => mk(i)),
});

const rows = () => screen.queryAllByTestId("recent-row");
const pick = (label: string, value: string) =>
  fireEvent.change(screen.getByLabelText(label), { target: { value } });

describe("RecentBuilds", () => {
  it("lists the newest 20 and offers the rest", () => {
    render(<RecentBuilds god="Agni" file={file(30)} now={NOW} />);
    expect(rows()).toHaveLength(20);
    fireEvent.click(screen.getByRole("button", { name: /Show 10 more/ }));
    expect(rows()).toHaveLength(30);
  });

  it("filters by role, result, rank, patch and aspect, and says how many are left", () => {
    const f: RecentFile = { ...file(0), kept: 4, builds: [
      mk(0, { role: "Carry", win: true, master: true, patch: "ob47", aspect: "Aspect of Combustion" }),
      mk(1, { role: "Carry", win: false, master: false, patch: "ob46", aspect: null }),
      mk(2, { role: "Mid", win: true, master: false, patch: "ob47", aspect: "Aspect of Combustion" }),
      mk(3, { role: "Mid", win: false, master: true, patch: "ob46", aspect: "Aspect of Combustion" }),
    ] };
    render(<RecentBuilds god="Agni" file={f} now={NOW} />);
    expect(rows()).toHaveLength(4);
    pick("Role", "Carry"); expect(rows()).toHaveLength(2);
    pick("Result", "win"); expect(rows()).toHaveLength(1);
    pick("Role", "all"); expect(rows()).toHaveLength(2);
    pick("Result", "all"); pick("Rank", "master"); expect(rows()).toHaveLength(2);
    pick("Rank", "all"); pick("Patch", "ob46"); expect(rows()).toHaveLength(2);
    pick("Aspect", "none"); expect(rows()).toHaveLength(1);
    expect(screen.getByTestId("recent-count")).toHaveTextContent("1 of the latest 4 matches");
  });

  it("explains an empty result and clears back to everything", () => {
    render(<RecentBuilds god="Agni" file={file(5)} now={NOW} />);
    pick("Patch", "ob46");
    expect(rows()).toHaveLength(0);
    expect(screen.getByText(/None of the latest 5 matches fit those filters/)).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "Clear filters" }));
    expect(rows()).toHaveLength(5);
  });

  it("says items are held, not bought in order", () => {
    render(<RecentBuilds god="Agni" file={file(2)} now={NOW} />);
    expect(screen.getByTestId("recent-builds")).toHaveTextContent(/not the order they bought them/);
  });
});
