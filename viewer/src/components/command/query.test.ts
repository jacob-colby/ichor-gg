import { describe, it, expect, beforeEach } from "vitest";
import { parseQuery, serializeQuery, queryHash, suggest, splitTail, removeSpan, godMatches } from "./query";
import { readRecents, pushRecent, MAX_RECENTS } from "./recents";
import { decodePageQuery } from "../second/pageState";

const gods = [
  "Ra", "Rama", "Hera", "Hecate", "Hel", "Hercules", "Hou Yi", "Ymir", "Baron Samedi", "Morgan Le Fay",
  "The Morrigan", "Vulcan", "Ares", "Artemis", "Anubis", "Zeus", "Thor", "Loki", "Neith", "Cu Chulainn",
].map((name) => ({ name, aspects: name === "Ra" ? [{ name: "Aspect of Thermotherapy" }] : [] }));

const p = (s: string, mode?: "conquest" | "joust" | "arena") => parseQuery(s, gods, mode);

describe("parseQuery — the grammar", () => {
  it("reads the first god as you and 'vs' as the start of the enemy side", () => {
    const q = p("ra vs hecate ymir");
    expect(q).toMatchObject({ you: "Ra", enemies: ["Hecate", "Ymir"], mode: null, aspect: false, notes: [] });
    expect(q.tokens.map((t) => t.kind)).toEqual(["you", "vs", "enemy", "enemy"]);
  });

  it("starts the enemy side on a second god even without 'vs'", () => {
    expect(p("ra hecate ymir")).toMatchObject({ you: "Ra", enemies: ["Hecate", "Ymir"] });
  });

  it("accepts v, versus and against for vs", () => {
    for (const w of ["v", "versus", "against", "VS."]) expect(p(`ra ${w} ymir`).enemies).toEqual(["Ymir"]);
  });

  it("is case-insensitive and ignores commas", () => {
    expect(p("RA Vs HeCaTe,YMIR JOUST")).toMatchObject({ you: "Ra", enemies: ["Hecate", "Ymir"], mode: "joust" });
  });

  it("sets the mode from a mode word anywhere, last one winning", () => {
    expect(p("joust ra vs ymir").mode).toBe("joust");
    const q = p("ra joust arena");
    expect(q.mode).toBe("arena");
    expect(q.notes).toContain("Two modes typed — using Arena");
  });

  it("toggles the aspect, and refuses it for a god without one", () => {
    expect(p("ra aspect").aspect).toBe(true);
    expect(p("ra aspect aspect").aspect).toBe(false);
    const ymir = p("ymir aspect");
    expect(ymir.aspect).toBe(false);
    expect(ymir.notes).toContain("Ymir has no aspect");
  });

  it("finishes partial names, best match first", () => {
    expect(p("baron").you).toBe("Baron Samedi");
    expect(p("samedi").you).toBe("Baron Samedi");
    expect(p("hou").you).toBe("Hou Yi");
    expect(p("yi").you).toBe("Hou Yi");
    // An exact name beats a longer name that starts with it.
    expect(p("ra").you).toBe("Ra");
    expect(p("ram").you).toBe("Rama");
    // Shortest name that starts with the word wins a tie.
    expect(p("he").you).toBe("Hel");
    expect(p("cuchulainn").you).toBe("Cu Chulainn");
  });

  it("reads multi-word names whole, and absorbs a word that re-states one", () => {
    expect(p("morgan le fay vs the morrigan")).toMatchObject({ you: "Morgan Le Fay", enemies: ["The Morrigan"] });
    const q = p("baron sam vs ra");
    expect(q).toMatchObject({ you: "Baron Samedi", enemies: ["Ra"], notes: [] });
    expect(q.tokens[0]).toMatchObject({ kind: "you", text: "baron sam", start: 0, end: 9 });
  });

  it("keeps unknown words as tokens with a reason, without breaking the rest", () => {
    const q = p("ra vs qwerty ymir");
    expect(q).toMatchObject({ you: "Ra", enemies: ["Ymir"] });
    expect(q.tokens[2]).toMatchObject({ kind: "unknown", text: "qwerty" });
    expect(q.notes).toEqual(["“qwerty” isn't a god or a mode"]);
  });

  it("ignores filler words", () => {
    expect(p("playing ra against hecate and ymir")).toMatchObject({ you: "Ra", enemies: ["Hecate", "Ymir"], notes: [] });
  });

  it("drops duplicates with a note — but a mirror after 'vs' is legal", () => {
    const dup = p("ra vs hecate hecate");
    expect(dup.enemies).toEqual(["Hecate"]);
    expect(dup.notes).toEqual(["Hecate is already on their team"]);
    const twice = p("ra ra");
    expect(twice).toMatchObject({ you: "Ra", enemies: [] });
    expect(twice.notes).toEqual(["Ra is already you"]);
    expect(p("ra vs ra").enemies).toEqual(["Ra"]);
  });

  it("caps the enemy team at the mode's size — five, or three in Joust", () => {
    const five = p("ra vs hecate ymir zeus thor loki neith");
    expect(five.enemies).toEqual(["Hecate", "Ymir", "Zeus", "Thor", "Loki"]);
    expect(five.notes).toEqual(["Only 5 enemies fit in Conquest — dropped Neith"]);
    expect(five.tokens.at(-1)).toMatchObject({ kind: "dropped", value: "Neith" });
    // The mode word may come after the enemies; the cap still follows it.
    expect(p("ra vs hecate ymir zeus thor joust").enemies).toEqual(["Hecate", "Ymir", "Zeus"]);
    // An edited Joust page keeps three slots without retyping the mode.
    expect(p("ra vs hecate ymir zeus thor", "joust").enemies).toHaveLength(3);
  });

  it("parses enemies with no god of your own", () => {
    expect(p("vs hecate ymir")).toMatchObject({ you: null, enemies: ["Hecate", "Ymir"] });
  });

  it("parses the empty string to nothing", () => {
    expect(p("   ")).toMatchObject({ you: null, enemies: [], mode: null, aspect: false, tokens: [], notes: [] });
  });

  it("resolves 'v' to vs, not Vulcan, and finishes a keyword when no god claims it", () => {
    expect(p("ra v vulc")).toMatchObject({ enemies: ["Vulcan"] });
    expect(p("ra jou").mode).toBe("joust");
    expect(p("ra asp").aspect).toBe(true);
  });
});

describe("serializeQuery / queryHash — the link reproduces the chips", () => {
  it("writes canonical text", () => {
    expect(serializeQuery(p("ra vs hec ym joust aspect"))).toBe("Ra vs Hecate Ymir Joust aspect");
    expect(serializeQuery({ you: "Ra", enemies: ["", "Ymir", ""], mode: "conquest", aspect: false })).toBe("Ra vs Ymir Conquest");
  });

  it("round-trips through the god page's own query decoder", () => {
    const hash = queryHash({ you: "Baron Samedi", enemies: ["Hecate", "Hou Yi"], mode: "joust", aspect: true });
    expect(hash).toBe("#/god/Baron%20Samedi?mode=joust&aspect=1&vs=Hecate%2CHou+Yi");
    const q = decodePageQuery(new URLSearchParams(hash.split("?")[1]));
    expect(q).toMatchObject({ mode: "joust", aspect: true, vs: ["Hecate", "Hou Yi"] });
    // Conquest and no enemies is the bare god link.
    expect(queryHash({ you: "Ra", enemies: [], mode: "conquest", aspect: false })).toBe("#/god/Ra");
    // And it re-parses to the same query.
    expect(p(serializeQuery(p("ra vs hecate ymir joust")))).toMatchObject({ you: "Ra", enemies: ["Hecate", "Ymir"], mode: "joust" });
  });
});

describe("suggest", () => {
  it("offers gods in the order the parser would pick them, labelled with their side", () => {
    const s = suggest("he", p(""), gods);
    expect(s.map((x) => x.label)).toEqual(["Hel", "Hera", "Hecate", "Hercules"]);
    expect(s[0].side).toBe("you");
    expect(suggest("he", p("ra "), gods)[0].side).toBe("enemy");
  });

  it("puts 'vs' first for 'v', then Vulcan", () => {
    expect(suggest("v", p("ra "), gods).map((x) => x.label)).toEqual(["vs", "Vulcan"]);
  });

  it("leaves out gods already on their team, and a second you before vs", () => {
    expect(suggest("hec", p("ra vs hecate "), gods)).toEqual([]);
    expect(suggest("ra", p("ra "), gods).map((x) => x.label)).toEqual(["Rama"]);
    expect(suggest("ra", p("ra vs "), gods).map((x) => x.label)).toContain("Ra");
  });

  it("offers modes and the aspect by prefix", () => {
    expect(suggest("jo", p("ra "), gods).map((x) => x.label)).toEqual(["Joust"]);
    expect(suggest("asp", p("ra "), gods).map((x) => x.label)).toEqual(["Aspect of Thermotherapy"]);
    expect(suggest("asp", p("ymir "), gods)).toEqual([]);
  });

  it("offers the next step of the grammar on an empty word", () => {
    expect(suggest("", p(""), gods)).toEqual([]);
    expect(suggest("", p("ra "), gods).map((x) => x.label)).toEqual(["vs", "Conquest", "Joust", "Arena", "Aspect of Thermotherapy"]);
    expect(suggest("", p("ra vs ymir joust "), gods).map((x) => x.label)).toEqual(["Conquest", "Arena", "Aspect of Thermotherapy"]);
  });

  it("ranks god matches", () => {
    expect(godMatches("ar", gods).map((g) => g.name)).toEqual(["Ares", "Artemis"]);
  });
});

describe("field text helpers", () => {
  it("splits off the word being typed; a trailing space commits it", () => {
    expect(splitTail("ra vs hec")).toEqual({ committed: "ra vs ", tail: "hec" });
    expect(splitTail("ra vs ")).toEqual({ committed: "ra vs ", tail: "" });
    expect(splitTail("")).toEqual({ committed: "", tail: "" });
  });

  it("removes a chip's span and tidies the gap", () => {
    const text = "ra vs hecate ymir";
    const q = p(text);
    const hec = q.tokens[2];
    expect(removeSpan(text, hec.start, hec.end)).toBe("ra vs ymir");
    expect(removeSpan(text, q.tokens[0].start, q.tokens[0].end)).toBe("vs hecate ymir");
  });
});

describe("recents", () => {
  beforeEach(() => localStorage.clear());

  it("keeps the newest first, de-duplicated, and capped", () => {
    pushRecent("Ra vs Hecate");
    pushRecent("Ymir");
    pushRecent("ra vs hecate");
    expect(readRecents()).toEqual(["ra vs hecate", "Ymir"]);
    for (let i = 0; i < 10; i += 1) pushRecent(`Ra vs ${i}`);
    expect(readRecents()).toHaveLength(MAX_RECENTS);
  });

  it("reads garbage as no recents", () => {
    localStorage.setItem("ichor:recent-queries", "{not json");
    expect(readRecents()).toEqual([]);
  });
});
