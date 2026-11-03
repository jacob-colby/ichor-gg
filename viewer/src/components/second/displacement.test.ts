import { describe, it, expect } from "vitest";
import { answeredThreats, displacement, displacementText } from "./displacement";
import type { DraftConfig } from "../../types";

const cfg = {
  tag_bonus: { healers: { "anti-heal": 2 }, lockdown: { "cc-immunity": 1 }, tanks: { penetration: 1 } },
  stat_bonus: { magical: { "Magical Protection": 1 }, tanks: { Penetration: 0.6 } },
} as unknown as DraftConfig;

describe("displacement — a swap in a player's words", () => {
  it("names the threat a channel answers, from the draft config's own tables", () => {
    const d = displacement({ added: "Divine Ruin", removed: "Spear of the Magus", bonus: 0.1, reason: "anti-heal" }, cfg,
      { healers: ["Aphrodite", "Baron Samedi"] });
    expect(displacementText(d)).toBe("Divine Ruin replaces Spear of the Magus · answers healing");
  });

  it("names only threats the entered enemies actually pose", () => {
    expect(answeredThreats("anti-heal, Magical Protection", cfg, { healers: ["Hel"] })).toEqual(["healers"]);
    expect(answeredThreats("anti-heal, Magical Protection", cfg, { healers: ["Hel"], magical: ["Hel"] }))
      .toEqual(["healers", "magical"]);
  });

  it("falls back to what the item brings when no posed threat claims it", () => {
    const d = displacement({ added: "Obsidian Shard", removed: "Soul Gem", bonus: 0.1, reason: "damage vs their build" }, cfg, {});
    expect(d.why).toBe("brings more damage into this team");
  });

  it("never prints a bonus", () => {
    const d = displacement({ added: "X", bonus: 0.12 }, cfg, {});
    expect(displacementText(d)).toBe("X comes in");
  });
});
