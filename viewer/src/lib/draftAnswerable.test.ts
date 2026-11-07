/** Can the draft answer a drafted threat at all?
 *
 * THE INVARIANT THIS HARNESS EXISTS FOR. `adaptFromCore` takes the shipped
 * `god_item_scores` table as its candidate pool and nothing else, so an item
 * absent from that table cannot be promoted by any bonus of any size. Every
 * channel in `draft.tag_bonus` therefore needs at least one item carrying its
 * effect tag present in every god's table, in every mode, or the overlay is
 * priced for a response it is structurally unable to make.
 *
 * WHY IT WAS MISSING UNTIL NOW. `archetypeParity.test.ts` is the only other
 * instrument that runs against the shipped index, and it checks that an
 * undrafted board equals the god page and that the draft can still introduce
 * an item the base core never held. Both passed throughout. Neither asks
 * whether an answer was AVAILABLE, so a board the draft could not respond to
 * looked exactly like one it correctly left alone, and `score_cap: 40` went on
 * vetoing the overlay on most of the roster without anything going red.
 *
 * WHAT IT MEASURED, on the shipped index at fc59d374, BEFORE `answer_keep`:
 * the best answering item sat outside the top 40 for anti-crit on 77 of 95
 * gods, penetration 40, anti-heal 36, protection-shred 26, cc-immunity 20,
 * percent-health 17 and peel 13. anti-heal is the one that mattered most:
 * `_weights.yaml` doubles its weight because it "starts far down the base
 * ranking", and on 32 gods it started past the cap, where the doubling reached
 * nothing.
 *
 * This asserts the property rather than the fix, so it stays meaningful if the
 * guarantee is ever implemented a different way.
 */
import { describe, expect, it } from "vitest";
import raw from "../../public/index.json?raw";
import type { DraftConfig, God, Item } from "../types";
import type { DraftMode } from "./draft";

const idx = JSON.parse(raw) as {
  gods: God[]; items: Item[];
  god_item_scores: Record<string, Record<string, Record<string, number>>>;
  draft: DraftConfig & { tag_bonus?: Record<string, Record<string, number>> };
};

const MODES: DraftMode[] = ["conquest", "joust", "arena"];

const tagsOf: Record<string, Set<string>> = {};
for (const it of idx.items) tagsOf[it.name] = new Set(it.effect_tags ?? []);

/** Every effect tag the overlay can pay a bonus for, read off the shipped
 *  config rather than restated here, so a new threat channel is covered the
 *  moment it is added to `draft.tag_bonus`. */
const answerTags = [
  ...new Set(
    Object.values(idx.draft.tag_bonus ?? {}).flatMap((m) => Object.keys(m ?? {})),
  ),
].sort();

/** Tables that actually ship, aspect variants included: a `<mode>:aspect`
 *  table is a candidate pool the draft's aspect toggle uses, so it is held to
 *  the same standard as the base one. */
function everyTable() {
  const out: { god: string; table: string; scores: Record<string, number> }[] = [];
  for (const g of idx.gods) {
    const perMode = idx.god_item_scores?.[g.name];
    if (!perMode) continue;
    for (const [table, scores] of Object.entries(perMode)) {
      const mode = table.split(":")[0] as DraftMode;
      if (!MODES.includes(mode)) continue;
      out.push({ god: g.name, table, scores });
    }
  }
  return out;
}

/** How many items in the whole pool carry a tag. A channel with no item at all
 *  is a config question, not a packing failure, and is reported separately. */
function poolFor(tag: string) {
  return idx.items.filter((it) => (it.effect_tags ?? []).includes(tag)).length;
}

describe("draft answerability", () => {
  it("has threat channels and tables to check", () => {
    expect(answerTags.length).toBeGreaterThan(0);
    expect(everyTable().length).toBeGreaterThan(0);
  });

  it("names a tag the item pool can actually answer", () => {
    // Guards against a tag_bonus entry whose tag is misspelled or retired:
    // every channel must have at least one item in the pool carrying it, or
    // the bonus is unreachable for every god and the config is the bug.
    const empty = answerTags.filter((t) => poolFor(t) === 0);
    expect(empty, `tag_bonus names effect tags no item carries: ${empty.join(", ")}`)
      .toEqual([]);
  });

  it("offers every god an answer to every threat channel, in every mode", () => {
    const missing: string[] = [];
    for (const { god, table, scores } of everyTable()) {
      const present = new Set<string>();
      for (const name of Object.keys(scores)) {
        for (const t of tagsOf[name] ?? []) present.add(t);
      }
      for (const tag of answerTags) {
        if (!present.has(tag)) missing.push(`${god} ${table} ${tag}`);
      }
    }
    expect(
      missing,
      `the draft cannot answer these (god, table, channel) combinations at ` +
        `all, because no item carrying that tag is in the candidate pool. ` +
        `${missing.length} of ${everyTable().length * answerTags.length} ` +
        `checked. First 12: ${missing.slice(0, 12).join(" | ")}`,
    ).toEqual([]);
  });

  it("does not pay for the guarantee with an unbounded table", () => {
    // The guarantee re-opens the cap, so it has to stay a guarantee and not
    // become a loosening. An entry past the 40th must carry an answering tag,
    // and the overflow is bounded by what the guarantee can possibly add.
    const keep = (idx.draft as { answer_keep?: number }).answer_keep ?? 2;
    const cap = (idx.draft as { score_cap?: number }).score_cap ?? 40;
    const bad: string[] = [];
    for (const { god, table, scores } of everyTable()) {
      const names = Object.keys(scores);
      if (names.length > cap + answerTags.length * keep) {
        bad.push(`${god} ${table} has ${names.length} entries`);
        continue;
      }
      for (const n of names.slice(cap)) {
        const answers = [...(tagsOf[n] ?? [])].some((t) => answerTags.includes(t));
        if (!answers) bad.push(`${god} ${table} ships ${n} past the cap untagged`);
      }
    }
    expect(bad, `First 12: ${bad.slice(0, 12).join(" | ")}`).toEqual([]);
  });
});

// How many options each channel SHOULD offer a given god is a question only
// the pipeline can answer, because it depends on `scoring.is_buildable`: the
// three `penetration` items split by damage type (Dominance and Titan's Bane
// are Strength, Obsidian Shard is Intelligence), so a magical god has exactly
// one and "two options" is impossible for them. That assertion lives in
// `pipeline/smite/tests/test_build_index.py`, which can see the filter.
