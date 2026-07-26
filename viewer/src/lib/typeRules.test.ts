/** Guards for the Measurement Rule (DESIGN.md § Typography).
 *
 * The rule it replaced — "any label, tag, or count sets in JetBrains Mono" —
 * was followed faithfully for a year and ended with 73% of the items shelf,
 * 65% of the tier list and 51% of Home set in the label face, at which point
 * mono had stopped distinguishing anything. These are source-level greps, so
 * they can't judge whether a given string is a measurement; they catch the two
 * shapes that are never one.
 *
 * Sources are read through `import.meta.glob` rather than `node:fs`: anything
 * under `src/` is compiled by `tsc -b` during `npm run build`, where Node's
 * types aren't in scope — an fs-based version typechecked clean under Vitest
 * and broke the build.
 */
import { describe, it, expect } from "vitest";

const sources = import.meta.glob("../{App.tsx,components/**/*.tsx}", {
  query: "?raw",
  import: "default",
  eager: true,
}) as Record<string, string>;

const files = Object.entries(sources).filter(([path]) => !path.endsWith(".test.tsx"));

/** Every string and template literal in the file, with its line number.
 *
 * Deliberately not "every `className=` attribute": the style constants these
 * surfaces share (`const eyebrow = "font-mono …"`) and every
 * `className={cond ? a : b}` live outside that shape, and an earlier version
 * of this test was blind to all of them.
 */
function literals(source: string): { line: number; value: string }[] {
  const out: { line: number; value: string }[] = [];
  source.split("\n").forEach((text, i) => {
    for (const m of text.matchAll(/"([^"]*)"|'([^']*)'|`([^`]*)`/g)) {
      out.push({ line: i + 1, value: m[1] ?? m[2] ?? m[3] ?? "" });
    }
  });
  return out;
}

function offenders(predicate: (classes: string[]) => boolean): string[] {
  const found: string[] = [];
  for (const [path, source] of files) {
    for (const { line, value } of literals(source)) {
      const classes = value.split(/\s+/);
      if (classes.includes("font-mono") && predicate(classes)) {
        found.push(`${path.replace("../", "src/")}:${line} — ${value.trim().slice(0, 70)}`);
      }
    }
  }
  return found;
}

describe("the Measurement Rule", () => {
  // A measurement is short. Anything set at a reading size is a sentence, and
  // a sentence in the numeral face is the exact failure this rule exists for.
  const READING_SIZES = ["text-body", "text-lead", "text-title", "text-display"];

  it("never sets mono at a reading size", () => {
    expect(offenders((c) => READING_SIZES.some((s) => c.includes(s)))).toEqual([]);
  });

  // `leading-relaxed` is only ever reached for on running copy in this app, so
  // it marks prose as reliably as anything a grep can see.
  it("never sets mono on running copy", () => {
    expect(offenders((c) => c.includes("leading-relaxed"))).toEqual([]);
  });

  it("reads the surfaces it claims to, so a broken glob can't pass vacuously", () => {
    expect(files.length).toBeGreaterThan(10);
    expect(files.some(([p]) => p.endsWith("ItemsShop.tsx"))).toBe(true);
    // The rule's live uses must be visible to the scanner, or the greps above
    // are checking an empty set.
    expect(offenders(() => true).length).toBeGreaterThan(10);
  });
});
