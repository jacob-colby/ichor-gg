/** The command language: "ra vs hecate ymir joust aspect".
 *
 * One field is the navigation in this direction, so the parser is the router.
 * It is pure and total — every string parses to something, and anything it
 * could not place comes back as a token with a reason rather than vanishing.
 *
 * The grammar, in the order a player types it:
 *  - the first god is YOU;
 *  - "vs" (or v / versus / against) starts the enemy side — and so does a
 *    second god typed straight after you, because "ra hecate" can only mean
 *    one thing in a draft;
 *  - "conquest" / "joust" / "arena" set the mode (last one wins; the field
 *    drops the earlier word when a later one is committed — `keepLastMode`);
 *  - "aspect" toggles your god's aspect;
 *  - "and", "playing", "as" … are filler and read as nothing.
 *
 * A word resolves to a god by the same ranking the suggestions list shows, so
 * the top suggestion is always what Space or Enter will commit:
 *   exact keyword > exact name > exact word of a name ("samedi") >
 *   name starts with it (shortest first) > a word of the name starts with it >
 *   a keyword starts with it (jou → Joust).
 * Multi-word names match greedily ("baron samedi", "morgan le fay"), and a
 * word that only re-states the multi-word god just typed is absorbed into it
 * ("baron sam"), so committing one word at a time never invents a duplicate.
 */
import type { Mode } from "../second/verdict";
import { MODE_TEAM_SIZE } from "../../lib/draft";

/** What the parser needs to know about a god — a subset of `God`. */
export interface GodLike { name: string; aspects?: { name: string }[] | null }

export type TokenKind = "you" | "enemy" | "vs" | "mode" | "aspect" | "unknown" | "dropped" | "filler";

export interface QueryToken {
  kind: TokenKind;
  /** The source text this token covers. */
  text: string;
  /** The resolved value: a god's name, a mode, or nothing. */
  value?: string;
  /** Character span in the input, so a chip can be removed from the text. */
  start: number;
  end: number;
  /** Why a token was dropped or not understood, in words. */
  note?: string;
}

export interface ParsedQuery {
  you: string | null;
  enemies: string[];
  /** Null when no mode word was typed — the caller's default applies. */
  mode: Mode | null;
  aspect: boolean;
  tokens: QueryToken[];
  /** Plain-language notes about anything the parser dropped. */
  notes: string[];
}

const VS_WORDS = new Set(["vs", "vs.", "v", "v.", "versus", "against", "into"]);
const MODE_WORDS: Record<string, Mode> = { conquest: "conquest", joust: "joust", arena: "arena" };
const FILLER = new Set(["and", "&", "+", "with", "playing", "play", "as", "i'm", "im"]);
const KEYWORDS: { word: string; kind: "mode" | "aspect" | "vs"; value?: Mode }[] = [
  { word: "conquest", kind: "mode", value: "conquest" },
  { word: "joust", kind: "mode", value: "joust" },
  { word: "arena", kind: "mode", value: "arena" },
  { word: "aspect", kind: "aspect" },
  { word: "vs", kind: "vs" },
];
const MODE_LABEL: Record<Mode, string> = { conquest: "Conquest", joust: "Joust", arena: "Arena" };

/** Lowercase, and drop the punctuation people put in names ("Cu Chulainn",
 *  "Da Ji", an apostrophe) so "cuchulainn" and "cu chulainn" both land. */
const norm = (s: string) => s.toLowerCase().replace(/[^a-z0-9 ]/g, "");
const squash = (s: string) => norm(s).replace(/ /g, "");

/** How strongly a word names a god. Lower is stronger; null is no match. */
export function godRank(word: string, name: string): number | null {
  const w = squash(word);
  if (!w) return null;
  const full = squash(name);
  const words = norm(name).split(" ");
  if (full === w) return 0;
  if (words.length > 1 && words.includes(w)) return 1;
  if (full.startsWith(w)) return 2;
  if (words.some((x) => x.startsWith(w))) return 3;
  return null;
}

/** Every god a word could mean, best first (rank, then shorter, then A–Z). */
export function godMatches<G extends GodLike>(word: string, gods: G[]): G[] {
  return gods
    .map((g) => ({ g, r: godRank(word, g.name) }))
    .filter((x): x is { g: G; r: number } => x.r !== null)
    .sort((a, b) => a.r - b.r || a.g.name.length - b.g.name.length || a.g.name.localeCompare(b.g.name))
    .map((x) => x.g);
}

/** A keyword the word is a prefix of (2+ letters), when no god claims it. */
function keywordPrefix(word: string) {
  const w = word.toLowerCase();
  if (w.length < 2) return undefined;
  return KEYWORDS.find((k) => k.word.startsWith(w) && k.word !== w);
}

interface Word { text: string; lower: string; start: number; end: number }

function words(text: string): Word[] {
  const out: Word[] = [];
  for (const m of text.matchAll(/[^\s,]+/g)) {
    out.push({ text: m[0], lower: m[0].toLowerCase(), start: m.index!, end: m.index! + m[0].length });
  }
  return out;
}

/** The longest run of words (3, then 2) that spells a multi-word name exactly. */
function multiWordAt(ws: Word[], i: number, gods: GodLike[]): { god: GodLike; n: number } | null {
  for (let n = 3; n >= 2; n -= 1) {
    if (i + n > ws.length) continue;
    const phrase = squash(ws.slice(i, i + n).map((w) => w.text).join(" "));
    const god = gods.find((g) => g.name.includes(" ") && squash(g.name) === phrase);
    if (god) return { god, n };
  }
  return null;
}

/** Parse a query. `defaultMode` sizes the enemy team when no mode word is
 *  typed (a Joust page being edited keeps three slots). */
export function parseQuery(text: string, gods: GodLike[], defaultMode: Mode = "conquest"): ParsedQuery {
  const ws = words(text);
  const tokens: QueryToken[] = [];
  const notes: string[] = [];
  const enemies: string[] = [];
  let mode: Mode | null = null;
  let aspect = false;
  // Written from inside `placeGod`, so held in an object: TypeScript does not
  // follow assignments made in a closure.
  const st: { you: string | null; enemySide: boolean; last: QueryToken | null } =
    { you: null, enemySide: false, last: null };

  const placeGod = (god: GodLike, start: number, end: number, src: string) => {
    // Absorb a word that only re-states the multi-word god just placed.
    const prev = st.last;
    if (prev && prev.value === god.name && god.name.includes(" ")
      && prev.end <= start && tokens[tokens.length - 1] === prev) {
      prev.end = end;
      prev.text = text.slice(prev.start, end);
      return;
    }
    let tok: QueryToken;
    if (!st.you && !st.enemySide) {
      st.you = god.name;
      tok = { kind: "you", text: src, value: god.name, start, end };
    } else if (!st.enemySide && god.name === st.you) {
      tok = { kind: "dropped", text: src, value: god.name, start, end, note: `${god.name} is already you` };
      notes.push(tok.note!);
    } else {
      st.enemySide = true;
      if (enemies.includes(god.name)) {
        tok = { kind: "dropped", text: src, value: god.name, start, end, note: `${god.name} is already on their team` };
        notes.push(tok.note!);
      } else {
        enemies.push(god.name);
        tok = { kind: "enemy", text: src, value: god.name, start, end };
      }
    }
    tokens.push(tok);
    st.last = tok;
  };

  for (let i = 0; i < ws.length; i += 1) {
    const w = ws[i];
    const lower = w.lower;

    if (VS_WORDS.has(lower)) {
      tokens.push({ kind: "vs", text: w.text, start: w.start, end: w.end });
      st.enemySide = true; st.last = null;
      continue;
    }
    if (MODE_WORDS[lower]) {
      if (mode && mode !== MODE_WORDS[lower]) notes.push(`Two modes typed — using ${MODE_LABEL[MODE_WORDS[lower]]}`);
      mode = MODE_WORDS[lower];
      tokens.push({ kind: "mode", text: w.text, value: mode, start: w.start, end: w.end });
      st.last = null;
      continue;
    }
    if (lower === "aspect") {
      aspect = !aspect;
      tokens.push({ kind: "aspect", text: w.text, value: aspect ? "on" : "off", start: w.start, end: w.end });
      st.last = null;
      continue;
    }
    if (FILLER.has(lower)) {
      tokens.push({ kind: "filler", text: w.text, start: w.start, end: w.end });
      continue;
    }

    const multi = multiWordAt(ws, i, gods);
    if (multi) {
      const last = ws[i + multi.n - 1];
      placeGod(multi.god, w.start, last.end, text.slice(w.start, last.end));
      i += multi.n - 1;
      continue;
    }
    const god = godMatches(w.text, gods)[0];
    if (god) { placeGod(god, w.start, w.end, w.text); continue; }

    const kw = keywordPrefix(lower);
    if (kw?.kind === "mode") {
      mode = kw.value!;
      tokens.push({ kind: "mode", text: w.text, value: mode, start: w.start, end: w.end });
      st.last = null;
      continue;
    }
    if (kw?.kind === "aspect") {
      aspect = !aspect;
      tokens.push({ kind: "aspect", text: w.text, value: aspect ? "on" : "off", start: w.start, end: w.end });
      st.last = null;
      continue;
    }
    const note = `“${w.text}” isn't a god or a mode`;
    tokens.push({ kind: "unknown", text: w.text, start: w.start, end: w.end, note });
    notes.push(note);
  }

  // Aspect only means something for a god that has one.
  const you = st.you;
  if (aspect) {
    const g = gods.find((x) => x.name === you);
    if (!g?.aspects?.length) {
      aspect = false;
      for (const t of tokens) if (t.kind === "aspect") { t.kind = "dropped"; t.note = you ? `${you} has no aspect` : "Aspect needs your god first"; }
      notes.push(you ? `${you} has no aspect` : "Aspect needs your god first");
    }
  }

  // The mode is known only now, so the team size is too.
  const cap = MODE_TEAM_SIZE[mode ?? defaultMode];
  if (enemies.length > cap) {
    const over = enemies.splice(cap);
    for (const t of tokens) {
      if (t.kind === "enemy" && over.includes(t.value!)) {
        t.kind = "dropped";
        t.note = `Only ${cap} enemies fit in ${MODE_LABEL[mode ?? defaultMode]}`;
      }
    }
    notes.push(`Only ${cap} enemies fit in ${MODE_LABEL[mode ?? defaultMode]} — dropped ${over.join(", ")}`);
  }

  return { you, enemies, mode, aspect, tokens, notes };
}

/** Canonical text for a query: "Ra vs Hecate Ymir joust aspect". Conquest is
 *  written out too, so the chips always say which mode a page is on. */
export function serializeQuery(q: { you: string | null; enemies: string[]; mode: Mode | null; aspect: boolean }): string {
  const parts: string[] = [];
  if (q.you) parts.push(q.you);
  const e = q.enemies.filter(Boolean);
  if (e.length) parts.push("vs", ...e);
  if (q.mode) parts.push(MODE_LABEL[q.mode]);
  if (q.aspect) parts.push("aspect");
  return parts.join(" ");
}

/** The god page URL a query lands on: `#/god/Ra?mode=joust&aspect=1&vs=Hecate,Ymir`.
 *  Same keys and order as the god page's own query encoder, so landing there
 *  does not rewrite the address bar. */
export function queryHash(q: { you: string; enemies: string[]; mode: Mode | null; aspect: boolean }): string {
  const params = new URLSearchParams();
  if (q.mode && q.mode !== "conquest") params.set("mode", q.mode);
  if (q.aspect) params.set("aspect", "1");
  const e = q.enemies.filter(Boolean);
  if (e.length) params.set("vs", e.join(","));
  // Commas stay literal (`vs=Hecate,Ymir`): the link is read by people in
  // Discord before it is read by a browser, and both decode it the same.
  const s = params.toString().replace(/%2C/g, ",");
  return `#/god/${encodeURIComponent(q.you)}${s ? `?${s}` : ""}`;
}

/* ── Suggestions ────────────────────────────────────────────────────────── */

export type SuggestionKind = "god" | "mode" | "vs" | "aspect";
export interface Suggestion {
  kind: SuggestionKind;
  /** What the row says. */
  label: string;
  /** What tapping it writes into the field in place of the partial word. */
  insert: string;
  /** For a god: which side it would land on. */
  side?: "you" | "enemy";
  /** For a mode, the value. */
  mode?: Mode;
}

/** What the field offers for the word being typed (`tail`), given what is
 *  already committed. Ordered exactly as the parser would resolve the word. */
export function suggest(tail: string, committed: ParsedQuery, gods: GodLike[], limit = 6): Suggestion[] {
  const t = tail.trim().toLowerCase();
  const side: "you" | "enemy" = committed.you ? "enemy" : "you";
  const youGod = gods.find((g) => g.name === committed.you);
  const hasAspect = !!youGod?.aspects?.length;
  const out: Suggestion[] = [];
  const modes = (Object.keys(MODE_WORDS) as Mode[]).filter((m) => m !== committed.mode);

  if (!t) {
    // Nothing typed yet: offer the grammar's next step, never a god list.
    if (!committed.you) return [];
    if (!committed.enemies.length && !committed.tokens.some((x) => x.kind === "vs")) {
      out.push({ kind: "vs", label: "vs", insert: "vs" });
    }
    for (const m of modes) out.push({ kind: "mode", label: MODE_LABEL[m], insert: m, mode: m });
    if (hasAspect) out.push({ kind: "aspect", label: committed.aspect ? "Aspect off" : (youGod!.aspects![0].name), insert: "aspect" });
    return out.slice(0, limit);
  }

  if (VS_WORDS.has(t) && committed.you) out.push({ kind: "vs", label: "vs", insert: "vs" });
  if (MODE_WORDS[t]) out.push({ kind: "mode", label: MODE_LABEL[MODE_WORDS[t]], insert: t, mode: MODE_WORDS[t] });
  if (t === "aspect" && hasAspect) out.push({ kind: "aspect", label: youGod!.aspects![0].name, insert: "aspect" });

  const taken = new Set(committed.enemies);
  for (const g of godMatches(t, gods)) {
    if (taken.has(g.name)) continue;
    // A second Ra before "vs" would be a duplicate, not a mirror.
    if (g.name === committed.you && !committed.tokens.some((x) => x.kind === "vs")) continue;
    out.push({ kind: "god", label: g.name, insert: g.name, side });
  }
  if (t.length >= 1) {
    for (const k of KEYWORDS) {
      if (k.word === t || !k.word.startsWith(t)) continue;
      if (k.kind === "mode" && k.value !== committed.mode) out.push({ kind: "mode", label: MODE_LABEL[k.value!], insert: k.word, mode: k.value });
      if (k.kind === "aspect" && hasAspect) out.push({ kind: "aspect", label: youGod!.aspects![0].name, insert: "aspect" });
      if (k.kind === "vs" && committed.you && !VS_WORDS.has(t)) out.push({ kind: "vs", label: "vs", insert: "vs" });
    }
  }
  return out.slice(0, limit);
}

/** Split the field's text into the committed part and the word being typed.
 *  A trailing space commits: "ra vs " has an empty tail. */
export function splitTail(text: string): { committed: string; tail: string } {
  const m = /^(.*?)([^\s,]*)$/s.exec(text)!;
  return { committed: m[1], tail: m[2] };
}

/** Remove one token's span from the text, tidying the whitespace it leaves. */
export function removeSpan(text: string, start: number, end: number): string {
  return (text.slice(0, start) + text.slice(end)).replace(/\s{2,}/g, " ").replace(/^\s+/, "");
}

/** A second mode REPLACES the first: every mode word but the last leaves the
 *  text. The parser already reads the last mode as the mode; this makes the
 *  text agree, so the field shows one mode chip — the one the query runs in —
 *  rather than "Joust Arena" and a note saying Arena won. The field applies
 *  it whenever words are committed (typed, picked or Tab-completed) and to a
 *  linked `?q=`. Covers a keyword prefix ("jou") too, since that parses as a
 *  mode token. Not applied to "aspect": that word TOGGLES, so a second one
 *  means off, and keeping only the last would turn it back on. */
export function keepLastMode(text: string, gods: GodLike[], defaultMode: Mode = "conquest"): string {
  let out = text;
  for (;;) {
    const modes = parseQuery(out, gods, defaultMode).tokens.filter((t) => t.kind === "mode");
    if (modes.length < 2) return out;
    out = removeSpan(out, modes[0].start, modes[0].end);
  }
}

/* ── Items ──────────────────────────────────────────────────────────────── */

/** Items the whole text could name, best first — but only when the FIRST
 *  word is not a god or a keyword. "ra" is always Ra; "rage" is an item;
 *  "book of thoth" is an item even though its last word is a god, because the
 *  first word decides what kind of query this is. Ranking: the name starts
 *  with the text > a word of the name does > the name contains it (3+). */
export function itemMatches<I extends { name: string }>(text: string, items: I[], gods: GodLike[], limit = 4): I[] {
  const t = norm(text).replace(/\s+/g, " ").trim();
  if (t.length < 2) return [];
  const first = t.split(" ")[0];
  if (godMatches(first, gods).length || VS_WORDS.has(first) || FILLER.has(first)
    || KEYWORDS.some((k) => k.word.startsWith(first))) return [];
  const rank = (name: string) => {
    const n = norm(name);
    if (n.startsWith(t)) return 0;
    if (n.split(" ").some((w) => w.startsWith(t))) return 1;
    if (t.length >= 3 && n.includes(t)) return 2;
    return null;
  };
  return items
    .map((it) => ({ it, r: rank(it.name) }))
    .filter((x): x is { it: I; r: number } => x.r !== null)
    .sort((a, b) => a.r - b.r || a.it.name.length - b.it.name.length || a.it.name.localeCompare(b.it.name))
    .slice(0, limit)
    .map((x) => x.it);
}

/* ── God select ─────────────────────────────────────────────────────────── */

/** What the grid filters on, given the field. A plain name filters by that
 *  text; once the query has a "vs", a mode or an aspect, by your god alone. */
export function gridFilterText(text: string, q: ParsedQuery): string {
  const query = q.enemies.length || q.mode || q.aspect || q.tokens.some((t) => t.kind === "vs");
  return query ? q.you ?? "" : text.trim();
}
