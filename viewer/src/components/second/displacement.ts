/** A draft swap, in words: "Divine Ruin replaces Spear of the Magus · answers
 * healing".
 *
 * The overlay's `reason` names CHANNELS (effect tags and stats: "anti-heal,
 * Magical Protection"). A player thinks in THREATS (their healing, their
 * crowd control). The mapping is the draft config's own: a channel answers a
 * threat when `tag_bonus[threat]` or `stat_bonus[threat]` credits it — the same
 * tables `threatOverlay` scores with and `threatAnswer` matches on — and only
 * threats the entered enemies actually pose are named. When no posed threat
 * claims the channel (the damage term, "damage vs their build"), the line
 * falls back to what the item brings, in `answerWords`' vocabulary. Never a
 * bonus decimal.
 *
 * Pure. Tested in displacement.test.ts. */
import type { DraftConfig } from "../../types";
import type { CoreChange } from "../../lib/draftBuild";
import type { ThreatKey } from "../../lib/threats";
import { answerWords } from "./itemReason";
import { listWords } from "./verdict";

/** Threats as a player says them, in the order the board lists them. */
export const THREATS: { key: ThreatKey; noun: string; answer: string }[] = [
  { key: "healers", noun: "healing", answer: "anti-heal" },
  { key: "lockdown", noun: "crowd control", answer: "crowd-control immunity or peel" },
  { key: "tanks", noun: "tanks", answer: "penetration or shred" },
  { key: "crit", noun: "crit", answer: "crit protection" },
  { key: "magical", noun: "magical damage", answer: "magical protection" },
  { key: "physical", noun: "physical damage", answer: "physical protection" },
  { key: "walls", noun: "player-made walls", answer: "a relic" },
];

const channels = (reason?: string) => (reason ?? "").split(",")
  .map((c) => c.replace(/\(already covered\)/, "").trim()).filter(Boolean);

export function answeredThreats(reason: string | undefined, cfg: DraftConfig | undefined,
  culprits: Partial<Record<ThreatKey, string[]>>): ThreatKey[] {
  const ch = channels(reason);
  if (!ch.length || !cfg) return [];
  return THREATS.map((t) => t.key).filter((k) => {
    if (!(culprits[k]?.length)) return false;
    const tags = cfg.tag_bonus?.[k] ?? {};
    const stats = cfg.stat_bonus?.[k] ?? {};
    return ch.some((c) => c in tags || c in stats);
  });
}

export interface DisplacementWords {
  added: string;
  removed?: string;
  /** "answers healing", "brings penetration", or "" when nothing is known. */
  why: string;
}

export function displacement(c: CoreChange, cfg: DraftConfig | undefined,
  culprits: Partial<Record<ThreatKey, string[]>>): DisplacementWords {
  const threats = answeredThreats(c.reason, cfg, culprits);
  const nouns = threats.map((k) => THREATS.find((t) => t.key === k)!.noun);
  const brings = answerWords(c.reason);
  return {
    added: c.added,
    removed: c.removed,
    why: nouns.length ? `answers ${listWords(nouns)}` : brings ? `brings ${brings}` : "",
  };
}

/** The whole line as one string — for an accessible name or a test. */
export const displacementText = (d: DisplacementWords) =>
  `${d.added} ${d.removed ? `replaces ${d.removed}` : "comes in"}${d.why ? ` · ${d.why}` : ""}`;
