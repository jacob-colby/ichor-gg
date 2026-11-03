/** One line, in words, for why an item is in the six.
 *
 * The old rows printed `value 0.57 fit 0.69 win 0.54 pick 0.55` — decimals
 * with no unit and no meaning to a player. The god page now carries two kinds
 * of number only: gold, and percent of players. Everything else is a word,
 * and a word is only used when the data actually supports it:
 *
 *  1. A draft swap says what it replaced and what it answers, from the
 *     overlay's own `reason` ("anti-heal, Magical Protection") — never a bonus.
 *  2. The community's recorded slot: "55% of Ra players buy it first".
 *  3. Seen in the community's popular items or slot alternates:
 *     "26% of Ra players build it".
 *  4. Recorded nowhere in the community data: "Ra's players don't buy this".
 *  5. A secondary clause from the pipeline's own price bucket when it is
 *     `undervalued` ("worth more than it costs"), the same bucket the item
 *     shop's Underpriced filter reads. Nothing else is claimed — no "cheapest
 *     cooldown in the pool", because no field here says so.
 *
 * Only Conquest carries community data. In Joust and Arena the line still
 * quotes Conquest — a real number about real players — and says so.
 *
 * Pure. Tested in itemReason.test.ts.
 */
import type { CommunityBuildEntry, Item } from "../../types";
import { listWords, type Mode } from "./verdict";

export interface ItemReason {
  text: string;
  /** swap: the draft put it here. community: the community buys it.
   *  offmeta: Ichor's own pick. plain: no signal either way. */
  tone: "swap" | "community" | "offmeta" | "plain";
}

export interface ReasonContext {
  god: string;
  mode: Mode;
  /** This god's Conquest community entry, when it has one. */
  community?: CommunityBuildEntry;
  item?: Item;
  /** Set when the enemy draft swapped this item in. */
  swap?: { removed?: string; reason?: string };
}

const ORDINAL = ["first", "second", "third", "fourth", "fifth", "sixth"];

/** Overlay channel -> player words. Keys are effect_tags, stat names and the
 *  damage channel's own phrase (see draftBuild `pricer`). */
const ANSWER_WORDS: Record<string, string> = {
  "anti-heal": "anti-heal",
  "cc-immunity": "crowd-control immunity",
  peel: "peel",
  "anti-crit": "crit protection",
  "protection-shred": "protection shred",
  penetration: "penetration",
  Penetration: "penetration",
  "percent-health": "percent-health damage",
  "Magical Protection": "magical protection",
  "Physical Protection": "physical protection",
  "damage vs their build": "more damage into this team",
};

/** The overlay's comma-joined `reason` as a short phrase, or "" when none of
 *  its channels are positive answers we have words for. */
export function answerWords(reason: string | undefined): string {
  if (!reason) return "";
  const words: string[] = [];
  for (const raw of reason.split(",")) {
    const key = raw.replace(/\(already covered\)/, "").trim();
    const w = ANSWER_WORDS[key];
    if (w && !words.includes(w)) words.push(w);
  }
  return listWords(words);
}

const pct = (r: number) => `${Math.round(r * 100)}%`;

export function itemReason(name: string, ctx: ReasonContext): ItemReason {
  if (ctx.swap) {
    const answers = answerWords(ctx.swap.reason);
    const head = ctx.swap.removed ? `Swapped in for ${ctx.swap.removed}` : "Added for this team";
    return { tone: "swap", text: answers ? `${head} — brings ${answers}` : head };
  }

  const where = ctx.mode === "conquest" ? "" : "In Conquest, ";
  const value = ctx.item?.efficiency_tier === "undervalued" ? "worth more than it costs" : "";
  const c = ctx.community;
  if (c) {
    const slot = c.slot_order.findIndex((s) => s.name === name);
    if (slot >= 0 && slot < ORDINAL.length) {
      return { tone: "community",
        text: `${where}${pct(c.slot_order[slot].pick_rate)} of ${ctx.god} players buy it ${ORDINAL[slot]}` };
    }
    const seen = [
      ...(c.popular_items ?? []),
      ...c.slot_order.flatMap((s) => s.alternates ?? []),
    ].filter((p) => p.name === name);
    const rate = seen.length ? Math.max(...seen.map((p) => p.pick_rate)) : 0;
    if (rate >= 0.01) {
      return { tone: "community", text: `${where}${pct(rate)} of ${ctx.god} players build it` };
    }
    const off = `${where}${ctx.god}'s players don't buy this`;
    return { tone: "offmeta", text: value ? `${off} · ${value}` : off };
  }
  if (value) return { tone: "plain", text: value[0].toUpperCase() + value.slice(1) };
  return { tone: "plain", text: "" };
}
