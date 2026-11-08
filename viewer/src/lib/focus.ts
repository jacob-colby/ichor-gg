/** One main build, adjusted — the god page's focus control.
 *
 * The page used to end in an "Other builds" list: eleven tabs per god, each a
 * whole separate six, and a reader comparing two of them had to diff them by
 * eye. Measured on the shipped notes 2026-11-08 (main `eef19739`), the focus
 * builds differ from `core` by a median of 1–3 slots in Conquest and 2–4 in
 * Joust and Arena, and 11 to 31 of them per flavor are not different at all.
 * A list of whole sixes hides both facts. So the page now shows ONE six and
 * treats every other build as an adjustment of it: choose a focus, the six
 * changes in place, the slots that moved are marked, and one line names the
 * swaps.
 *
 * WHICH SIX IS THE MAIN ONE. `model` — the build the head-to-head measures
 * (`/side_by_side/*.json` reads `model` and nothing else; `side_by_side.py`,
 * `ARCHETYPE = "model"`), the one the verdict sentence speaks for, the one
 * "Show theirs" swaps against and the one the enemy strip adapts. In Joust
 * and Arena it IS `core` (95 of 95 gods each: both modes zero `win` and
 * `pick`, so the blend and the model rank identically). In Conquest it is not
 * (12 of 95 identical), and moving the default to `core` there would leave
 * the page's one comparison sentence describing a build that is not on
 * screen. That is a product decision, not a layout one, so it is not made
 * here.
 *
 * WHAT IS A FOCUS AND WHAT IS NOT. A focus is a lean the pipeline applies to
 * the blended score (`flavors:` in `_weights.yaml`): cooldown, attack speed,
 * anti-tank, bruiser, burst, mana-stack, and the per-god ones the god's own
 * scaling allows (crit, strength, intelligence, str-int —
 * `scoring.eligible_flavors`). `core` ("Balanced") and `hybrid` are not leans;
 * they are different ANSWERS to the same question — the blend with players'
 * win and pick rates in it, and the model corrected where players' records are
 * strong. They sit in the same control, after the focuses and set apart, and
 * only when they give a different six: `hybrid` is never emitted when it
 * would equal `model`, and `core` equals `model` by construction in two of
 * three modes, where a chip that can never change anything is padding. A
 * focus chip always shows, even when it changes nothing for this god, because
 * "what if I lean cooldown?" is a question the reader asks, and "same as
 * Ichor's six for Ra" is its answer.
 *
 * Pure. Tested in focus.test.ts.
 */
import type { CuratedBuildEntry, HybridSwap } from "../types";
import { tabLabel } from "./builds";

/** The focuses, in the order the strip shows them: the five every god has,
 *  then the two most gods have, then the per-god scaling builds. A fixed
 *  order — not the note's — so a reader who learns where Cooldown sits on
 *  Ra finds it in the same place on Ymir. */
export const FOCUS_ORDER = [
  "cooldown", "attack-speed", "anti-tank", "bruiser", "burst", "mana-stack",
  "crit", "strength", "intelligence", "str-int",
] as const;

/** Archetypes that are not focuses, in the order they follow the focuses. */
export const ANSWER_ORDER = ["core", "hybrid"] as const;

/** One slot that differs between two sixes. Paired by buy order: the first
 *  item leaving goes with the first item arriving. Either end is absent only
 *  when the two builds are different lengths. */
export interface SlotSwap { removed?: string; added?: string }

export interface FocusOption {
  archetype: string;
  label: string;
  kind: "main" | "focus" | "answer";
  six: string[];
  /** The note entry carrying these items — the deduped survivor when this
   *  archetype was collapsed into another (`dedupeIdenticalBuilds`). */
  entry: CuratedBuildEntry;
  /** What this option changes in the main six. Empty for the main build. */
  swaps: SlotSwap[];
  /** The label of the first option, in the strip's precedence (main, then
   *  the answers, then the focuses in order), that is this exact build —
   *  same items in the same order. Null when it is a build of its own. */
  sameAs: string | null;
  /** Same items as the main six, bought in a different order. */
  reordered: boolean;
}

export const MAIN_LABEL = "Ichor's six";

/** The slots that differ between `from` and `to`, paired in buy order. */
export function diffSix(from: string[], to: string[]): SlotSwap[] {
  const removed = from.filter((n) => !to.includes(n));
  const added = to.filter((n) => !from.includes(n));
  const n = Math.max(removed.length, added.length);
  return Array.from({ length: n }, (_, i) => ({ removed: removed[i], added: added[i] }));
}

const sameSequence = (a: string[], b: string[]) => a.length === b.length && a.every((x, i) => x === b[i]);

/** Every archetype name an entry answers to: its own, then the ones
 *  `dedupeIdenticalBuilds` folded into it. */
const namesOf = (e: CuratedBuildEntry) => [e.archetype ?? "", ...(e.aliases ?? [])].filter(Boolean);

/** The strip's options for one god, mode and kit, from the deduped archetype
 *  list `useDraftResult` already returns (one authority for what exists). */
export function focusOptions(archetypes: CuratedBuildEntry[], main = "model"): FocusOption[] {
  const byName = new Map<string, CuratedBuildEntry>();
  for (const e of archetypes) for (const n of namesOf(e)) if (!byName.has(n)) byName.set(n, e);
  if (!byName.size) return [];

  const mainName = byName.has(main) ? main : byName.has("core") ? "core" : namesOf(archetypes[0])[0];
  const mainEntry = byName.get(mainName)!;
  const mainSix = mainEntry.slot_order as string[];

  const labelOf = (name: string) => tabLabel({ source: "suggested", archetype: name, slot_order: [] });
  const known = new Set<string>([mainName, ...FOCUS_ORDER, ...ANSWER_ORDER]);
  // A flavor the pipeline adds later still gets a chip, after the known ones.
  const extra = [...byName.keys()].filter((n) => !known.has(n));

  const make = (archetype: string, kind: FocusOption["kind"]): FocusOption => {
    const entry = byName.get(archetype)!;
    const six = entry.slot_order as string[];
    const swaps = kind === "main" ? [] : diffSix(mainSix, six);
    return {
      archetype, kind, entry, six, swaps, sameAs: null,
      label: kind === "main" ? MAIN_LABEL : labelOf(archetype),
      reordered: kind !== "main" && swaps.length === 0 && !sameSequence(six, mainSix),
    };
  };

  const mainOpt = make(mainName, "main");
  const focuses = [...FOCUS_ORDER, ...extra].filter((n) => n !== mainName && byName.has(n)).map((n) => make(n, "focus"));
  const answers = ANSWER_ORDER.filter((n) => n !== mainName && byName.has(n)).map((n) => make(n, "answer"))
    // An answer that is the main six is not a different answer.
    .filter((o) => !sameSequence(o.six, mainSix));

  // "Same as …" reads against what came before it in precedence: the main
  // build, then the answers (Balanced is what every focus is a lean OF), then
  // earlier focuses. Answers are displayed after the focuses but outrank them
  // here, so a focus identical to Balanced says "Same as Balanced".
  const precedence = [mainOpt, ...answers, ...focuses];
  for (let i = 1; i < precedence.length; i += 1) {
    const o = precedence[i];
    const twin = precedence.slice(0, i).find((p) => sameSequence(p.six, o.six));
    if (twin) o.sameAs = twin.label;
  }
  return [mainOpt, ...focuses, ...answers];
}

/** "Players who buy it won 71% of 35 Ares games (Ares wins 54%)", from the
 *  hybrid's own swap reason, or null when the reason is not in the shape
 *  `hybrid._reason` writes. Never guessed at: an unparsed reason is dropped
 *  rather than paraphrased. */
export function hybridEvidence(swap: HybridSwap | undefined, god: string, borrowedFrom?: string): string | null {
  const m = swap?.reason.match(/(\d+)% win over (\d+) matches \(vs (\d+)% on this god\)/);
  if (!m) return null;
  const where = borrowedFrom ? `${borrowedFrom} ` : "";
  return `won ${m[1]}% of ${Number(m[2]).toLocaleString("en-US")} ${where}games with it (${god} wins ${m[3]}%)`;
}

/** The sentence over the swap list, in words. `subject` names what is doing
 *  the swapping when it is not obvious from the chip ("Thermotherapy"). */
export function swapLead(opt: Pick<FocusOption, "swaps" | "sameAs" | "reordered" | "six">, god: string,
  of: number, subject?: string): string {
  const n = opt.swaps.length;
  const who = subject ? `${subject} swaps` : "Swaps";
  if (opt.sameAs) {
    return n > 0 ? `Same as ${opt.sameAs} for ${god}. ${who} ${n} of ${of}:` : `Same as ${opt.sameAs} for ${god}.`;
  }
  if (opt.reordered) return `Same six as ${MAIN_LABEL}, bought in a different order.`;
  return `${who} ${n} of ${of}:`;
}
