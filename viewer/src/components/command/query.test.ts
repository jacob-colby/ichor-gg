import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import {
  parseQuery, serializeQuery, queryHash, suggest, splitTail, removeSpan, godMatches, itemMatches, keepLastMode,
} from "./query";
import { readRecentGods, pushRecentGod, clearRecentGods, recentHash, recentModeWord, MAX_RECENT_GODS } from "./recents";
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
    expect(hash).toBe("#/god/Baron%20Samedi?mode=joust&aspect=1&vs=Hecate,Hou+Yi"); // commas kept literal for readable links
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

describe("keepLastMode — a second mode replaces the first", () => {
  const k = (s: string, mode?: "conquest" | "joust" | "arena") => keepLastMode(s, gods, mode);

  it("drops every mode word but the last, wherever they sit", () => {
    expect(k("ra joust arena ")).toBe("ra arena ");
    expect(k("joust ra vs ymir arena ")).toBe("ra vs ymir arena ");
    expect(k("ra conquest joust arena ")).toBe("ra arena ");
    expect(k("ra vs hecate joust ymir conquest ")).toBe("ra vs hecate ymir conquest ");
  });

  it("counts a keyword prefix as the mode word it stands for", () => {
    expect(k("ra arena jou ")).toBe("ra jou ");
    expect(p(k("ra arena jou ")).mode).toBe("joust");
  });

  it("leaves one mode, no mode, and the same mode said twice's last copy", () => {
    expect(k("ra vs ymir joust ")).toBe("ra vs ymir joust ");
    expect(k("ra vs ymir ")).toBe("ra vs ymir ");
    expect(k("")).toBe("");
    expect(k("ra joust joust ")).toBe("ra joust ");
  });

  it("re-sizes the team with the mode that is left", () => {
    // Joust keeps three; replacing it with Arena brings the fourth back.
    expect(p("ra vs hecate ymir hel zeus joust").enemies).toHaveLength(3);
    expect(p(k("ra vs hecate ymir hel zeus joust arena ")).enemies).toEqual(["Hecate", "Ymir", "Hel", "Zeus"]);
  });

  it("leaves no note behind once the text has one mode", () => {
    expect(p("ra joust arena").notes).toContain("Two modes typed — using Arena");
    expect(p(k("ra joust arena ")).notes).toEqual([]);
  });

  it("does not touch aspect words: those toggle, they do not replace", () => {
    expect(k("ra aspect aspect ")).toBe("ra aspect aspect ");
    expect(k("ra aspect joust arena ")).toBe("ra aspect arena ");
  });
});

/* One list of recent gods, not queries (Jacob, 2026-11-09): the god select
 * row, its first card (the old "Back to"), and the empty field's offers. Each
 * god keeps the mode and aspect it was last viewed in; the enemies go. */
describe("recent gods", () => {
  beforeEach(() => localStorage.clear());
  afterEach(() => vi.restoreAllMocks());
  const view = (god: string, mode: "conquest" | "joust" | "arena" = "conquest", aspect = false) => ({ god, mode, aspect });
  const names = () => readRecentGods(gods).map((e) => e.god);

  it("keeps the newest first, one entry per god, and capped", () => {
    pushRecentGod(view("Ra"), gods);
    pushRecentGod(view("Ymir"), gods);
    pushRecentGod(view("Ra"), gods);
    expect(names()).toEqual(["Ra", "Ymir"]);
    for (const g of gods) pushRecentGod(view(g.name), gods);
    expect(names()).toHaveLength(MAX_RECENT_GODS);
    expect(names()[0]).toBe("Cu Chulainn");
  });

  it("a newer visit to a god moves it up and replaces its mode and aspect", () => {
    pushRecentGod(view("Ra", "joust", true), gods);
    pushRecentGod(view("Ymir", "arena"), gods);
    expect(readRecentGods(gods)).toEqual([view("Ymir", "arena"), view("Ra", "joust", true)]);
    pushRecentGod(view("Ra"), gods);
    expect(readRecentGods(gods)).toEqual([view("Ra"), view("Ymir", "arena")]);
  });

  it("reopens the god in that mode and aspect, with the defaults left out of the link", () => {
    expect(recentHash(view("Ra"))).toBe("#/god/Ra");
    expect(recentHash(view("Ra", "joust", true))).toBe("#/god/Ra?mode=joust&aspect=1");
    expect(recentHash(view("Morgan Le Fay", "arena"))).toBe("#/god/Morgan%20Le%20Fay?mode=arena");
    expect(recentModeWord(view("Ra"))).toBeNull();
    expect(recentModeWord(view("Ra", "joust"))).toBe("Joust");
  });

  it("drops a god the roster no longer has, and anything that isn't an entry", () => {
    localStorage.setItem("ichor:recent-gods", JSON.stringify([
      view("Nobody"), { god: "Ra", mode: "duel", aspect: "yes" }, 7, { mode: "joust" }, view("Ymir", "joust"),
    ]));
    expect(readRecentGods(gods)).toEqual([view("Ra"), view("Ymir", "joust")]);
  });

  it("reads garbage as no recents", () => {
    localStorage.setItem("ichor:recent-gods", "{not json");
    expect(readRecentGods(gods)).toEqual([]);
  });

  it("seeds once from the retired stores, keeping each old query's mode and aspect", () => {
    localStorage.setItem("ichor:recent-queries",
      JSON.stringify(["Morgan Le Fay vs Ra Joust", "Ra vs Hecate Arena aspect", "zz vs Ymir", "Ra vs Zeus"]));
    // The last god has no mode or aspect of its own: Conquest, aspect off.
    localStorage.setItem("ichor:last-god", "Ymir");
    expect(readRecentGods(gods)).toEqual([view("Ymir"), view("Morgan Le Fay", "joust"), view("Ra", "arena", true)]);
    // The first write carries the seed and retires both old stores.
    expect(pushRecentGod(view("Hera"), gods).map((e) => e.god)).toEqual(["Hera", "Ymir", "Morgan Le Fay", "Ra"]);
    expect(localStorage.getItem("ichor:recent-queries")).toBeNull();
    expect(localStorage.getItem("ichor:last-god")).toBeNull();
  });

  it("seeds the last god with its old query's state when one names it, as its old card linked", () => {
    localStorage.setItem("ichor:recent-queries", JSON.stringify(["Hera vs Ymir", "Ra vs Hecate Joust aspect"]));
    localStorage.setItem("ichor:last-god", "Ra");
    expect(readRecentGods(gods)).toEqual([view("Ra", "joust", true), view("Hera")]);
  });

  it("stays clear once cleared, even with the retired stores still there", () => {
    pushRecentGod(view("Ra"), gods);
    localStorage.setItem("ichor:recent-queries", JSON.stringify(["Hera vs Ymir"]));
    clearRecentGods();
    expect(readRecentGods(gods)).toEqual([]);
  });

  it("degrades to no recents when storage is blocked", () => {
    vi.spyOn(Storage.prototype, "getItem").mockImplementation(() => { throw new Error("SecurityError"); });
    vi.spyOn(Storage.prototype, "setItem").mockImplementation(() => { throw new Error("SecurityError"); });
    expect(readRecentGods(gods)).toEqual([]);
    expect(pushRecentGod(view("Ra"), gods)).toEqual([view("Ra")]);
    expect(() => clearRecentGods()).not.toThrow();
  });
});

/* A + C: the field is the global search again, so an item name has to land
 * somewhere — but never at the expense of a god. */
describe("itemMatches", () => {
  const its = [{ name: "Rage" }, { name: "Book of Thoth" }, { name: "Deathbringer" }, { name: "Divine Ruin" }];
  const gs = [{ name: "Ra" }, { name: "Thoth" }, { name: "Ymir" }];
  it("finds an item whose first word is not a god", () => {
    expect(itemMatches("deathb", its, gs).map((i) => i.name)).toEqual(["Deathbringer"]);
    // "rage" is no god's prefix ("ra" is), so it is the item.
    expect(itemMatches("rage", its, gs).map((i) => i.name)).toEqual(["Rage"]);
    expect(itemMatches("book of th", its, gs).map((i) => i.name)).toEqual(["Book of Thoth"]);
    expect(itemMatches("ruin", its, gs).map((i) => i.name)).toEqual(["Divine Ruin"]);
  });
  it("never claims a query that starts with a god or a keyword", () => {
    expect(itemMatches("ra", its, gs)).toEqual([]);
    expect(itemMatches("thoth", its, gs)).toEqual([]);
    expect(itemMatches("joust", its, gs)).toEqual([]);
    expect(itemMatches("ar", its, gs)).toEqual([]);
  });
  it("needs two letters", () => {
    expect(itemMatches("d", its, gs)).toEqual([]);
  });
});
