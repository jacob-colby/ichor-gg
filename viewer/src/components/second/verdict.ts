/** The comparison's verdict as ONE sentence a player can act on.
 *
 * The old god page led with Ichor's six and then, ~2,000px later, printed
 * "Community better" over a metric table. A player could not reconcile which
 * build to buy. This turns the same `/side_by_side/<slug>.json` the table
 * reads into the sentence that sits directly under the build.
 *
 * It reads the file; it does not re-judge it. The pipeline's own verdict and
 * coverage rule decide whether there is anything to say:
 *
 *  - `aspect not simulated` -> the community plays a kit the combat model
 *    can't run, so no call is made.
 *  - `not enough simulated`, or `coverage.ok === false` -> too much of the gold
 *    is passives the model can't simulate, so no call is made.
 *  - otherwise the weighted damage and survival axes are put into words, with
 *    anything inside the band (+-5% unless `_meta.json` says otherwise) called
 *    "about even" — the same band SideBySide.tsx tones as neutral.
 *
 * Honesty tail: any of ICHOR's six whose passive the model does not simulate
 * is named, because that item's value is missing from the number the
 * sentence just quoted ("not measured here" is not zero).
 *
 * Pure: no React, no fetch. Tested in verdict.test.ts.
 */
import type { SideBySideData } from "../SideBySide";

export type Mode = "conquest" | "joust" | "arena";

export interface VerdictPart { text: string; em?: boolean }

export interface Verdict {
  /** measured: a real call. withheld: the data exists but won't support one.
   *  none: nothing to compare (no file, other mode, other build). */
  kind: "measured" | "withheld" | "none";
  /** Who comes out ahead, for tone only. */
  lead?: "ichor" | "community" | "split" | "even";
  parts: VerdictPart[];
  /** The honesty clause, set quieter than the claim. */
  tail?: string;
}

export interface VerdictInput {
  /** The comparison file, or null when this god has none. */
  d: SideBySideData | null;
  god: string;
  mode: Mode;
  /** The archetype on screen. The file compares `model` only. */
  archetype: string;
  /** Ichor's six as shown; the sentence is withheld if the file measured a
   *  different six (a stale file must not speak for a new build). */
  shownSix: string[];
  /** Name of the aspect when the toggle is on AND moved the build — the file
   *  measures the base-kit six, so it can't speak for that one. */
  aspectBuild?: string | null;
  /** Verdict band from `_meta.json`; 0.05 when absent. */
  band?: number;
  /** Items the enemy draft swapped into the six on screen. The file measured
   *  the six BEFORE them, and the sentence must say so. */
  draftSwaps?: number;
}

export const MODE_NAME: Record<Mode, string> = { conquest: "Conquest", joust: "Joust", arena: "Arena" };

/** "Lotus Sickle", "A and B", "A, B and C". */
export function listWords(names: string[]): string {
  if (names.length <= 1) return names[0] ?? "";
  return `${names.slice(0, -1).join(", ")} and ${names[names.length - 1]}`;
}

/** Whole-percent gap for whichever side is ahead on one axis. `r` is Ichor
 *  over community. Ichor ahead: (r-1). Community ahead: (1/r - 1) — "the
 *  community's six deals 7% more" is a claim about THEIR number. */
export function axisGap(r: number): { who: "ichor" | "community"; pct: number } {
  return r >= 1
    ? { who: "ichor", pct: Math.round((r - 1) * 100) }
    : { who: "community", pct: Math.round((1 / r - 1) * 100) };
}

const SIX: Record<"ichor" | "community", string> = { ichor: "Ichor's six", community: "The community's six" };
const sameSet = (a: string[], b: string[]) =>
  a.length === b.length && a.every((x) => b.includes(x));

export function verdictSentence(input: VerdictInput): Verdict {
  const { d, god, mode, archetype, shownSix, aspectBuild } = input;
  const band = input.band ?? 0.05;

  if (mode !== "conquest") {
    return { kind: "none", parts: [{
      text: `${MODE_NAME[mode]} has no community build to measure against, so this is the model's six on its own.` }] };
  }
  if (archetype !== "model") {
    return { kind: "none", parts: [{
      text: "The head-to-head is measured for Ichor's main six, not this one." }] };
  }
  if (!d) {
    return { kind: "none", parts: [{ text: `There's no measured comparison for ${god} yet.` }] };
  }
  if (aspectBuild) {
    return { kind: "none", parts: [{
      text: `The head-to-head is measured on the base kit, so it doesn't cover the ${aspectBuild} six.` }] };
  }
  if (!sameSet(d.ichor.items, shownSix)) {
    return { kind: "withheld", parts: [{
      text: "The head-to-head was measured on an older version of this six, so it isn't quoted here." }] };
  }
  if (d.verdict === "aspect not simulated") {
    const aspect = d.kit?.aspect ?? "an aspect";
    return { kind: "withheld", parts: [{
      text: `Most ${god} players run ${aspect}, and the combat model can't simulate that aspect yet — so this isn't measured enough to call.` }] };
  }
  if (d.verdict === "not enough simulated" || d.coverage?.ok === false) {
    return { kind: "withheld", parts: [{
      text: "Too much of these two builds is passives the model can't simulate yet, so this isn't measured enough to call." }] };
  }

  const [dmg, surv] = d.weighted_axes ?? [d.damage_axis, d.survival_axis];
  const dmgEven = Math.abs(dmg - 1) <= band;
  const survEven = Math.abs(surv - 1) <= band;
  const g = axisGap(dmg);
  const s = axisGap(surv);

  let parts: VerdictPart[];
  let lead: Verdict["lead"];
  if (dmgEven && survEven) {
    lead = "even";
    parts = [{ text: "Ichor's six and the community's are " }, { text: "about even", em: true },
      { text: " on damage and on survival." }];
  } else if (survEven) {
    lead = g.who;
    parts = [{ text: `${SIX[g.who]} deals ` }, { text: `${g.pct}% more damage`, em: true },
      { text: "; survival is about even." }];
  } else if (dmgEven) {
    lead = s.who;
    parts = [{ text: `${SIX[s.who]} survives ` }, { text: `${s.pct}% more`, em: true },
      { text: "; damage is about even." }];
  } else if (g.who === s.who) {
    lead = g.who;
    parts = [{ text: `${SIX[g.who]} deals ` }, { text: `${g.pct}% more damage`, em: true },
      { text: " and survives " }, { text: `${s.pct}% more`, em: true }, { text: "." }];
  } else {
    lead = "split";
    // Ichor's advantage first: Ichor's build is the one on screen.
    parts = g.who === "ichor"
      ? [{ text: "Ichor's six deals " }, { text: `${g.pct}% more damage`, em: true }, { text: ". " },
        { text: "The community's six survives " }, { text: `${s.pct}% more`, em: true }, { text: "." }]
      : [{ text: "Ichor's six survives " }, { text: `${s.pct}% more`, em: true }, { text: ". " },
        { text: "The community's six deals " }, { text: `${g.pct}% more damage`, em: true }, { text: "." }];
  }

  const unsim = d.ichor.passives.filter((p) => p.status === "not simulated").map((p) => p.item);
  let tail: string | undefined;
  if (unsim.length) {
    const gap = !dmgEven ? "the damage gap" : !survEven ? "the survival gap" : "the result";
    tail = `${listWords(unsim)} ${unsim.length === 1 ? "isn't" : "aren't"} simulated yet, so ${gap} is partly unmeasured.`;
  }
  if (input.draftSwaps) {
    const swap = `Measured before this team's ${input.draftSwaps === 1 ? "swap" : "swaps"}.`;
    tail = tail ? `${tail} ${swap}` : swap;
  }
  return { kind: "measured", lead, parts, tail };
}

/** The sentence as plain text — for tests and accessible names. */
export function verdictText(v: Verdict): string {
  return [v.parts.map((p) => p.text).join(""), v.tail].filter(Boolean).join(" ");
}
