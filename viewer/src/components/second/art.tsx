/** Art and glyphs for the Second Screen surfaces.
 *
 * One stroke system for every glyph (24-unit box, 1.75 stroke, round caps), so
 * the tab bar, disclosures and the enemy strip read as one drawn set rather
 * than as unicode stand-ins. */
import { useState, type SVGProps } from "react";
import { iconSlug } from "../../lib/builds";

/** God or item art with a lettered fallback. `kind` picks the file:
 *  card = 280x420 god card art, head = 256² portrait, item = 128² icon. */
export function Art({ name, kind, className = "", eager = false }: {
  name: string; kind: "card" | "head" | "item"; className?: string; eager?: boolean;
}) {
  const [failed, setFailed] = useState(false);
  if (failed) {
    return (
      <span aria-hidden="true"
        className={`flex flex-none items-center justify-center bg-surface-3 font-cond text-row font-extrabold text-quiet ${className}`}>
        {name.slice(0, 1)}
      </span>
    );
  }
  const suffix = kind === "head" ? "-head" : "";
  return (
    <img src={`/icons/${iconSlug(name)}${suffix}.png`} alt="" loading={eager ? "eager" : "lazy"}
      decoding="async" onError={() => setFailed(true)}
      className={`flex-none bg-surface-2 object-cover ${className}`} />
  );
}

type GlyphProps = SVGProps<SVGSVGElement> & { size?: number };
function Glyph({ size = 24, children, ...rest }: GlyphProps) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor"
      strokeWidth={1.75} strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" {...rest}>
      {children}
    </svg>
  );
}

/** Two rows facing each other: the draft. */
export const DraftGlyph = (p: GlyphProps) => (
  <Glyph {...p}><path d="M3 7h3M9 7h3M15 7h3M21 7h0" /><path d="M3 17h3M9 17h3M15 17h3M21 17h0" />
    <path d="M12 10v4" /></Glyph>
);
/** A bust: the roster. */
export const GodsGlyph = (p: GlyphProps) => (
  <Glyph {...p}><circle cx="12" cy="8.5" r="3.5" /><path d="M5 20c.8-3.6 3.6-5.5 7-5.5s6.2 1.9 7 5.5" /></Glyph>
);
export const MoreGlyph = (p: GlyphProps) => (
  <Glyph {...p}><path d="M4 7h16M4 12h16M4 17h10" /></Glyph>
);
export const SearchGlyph = (p: GlyphProps) => (
  <Glyph {...p}><circle cx="11" cy="11" r="6" /><path d="m20 20-4.2-4.2" /></Glyph>
);
export const PlusGlyph = (p: GlyphProps) => <Glyph {...p}><path d="M12 6v12M6 12h12" /></Glyph>;
export const CloseGlyph = (p: GlyphProps) => <Glyph {...p}><path d="m7 7 10 10M17 7 7 17" /></Glyph>;
export const ChevronGlyph = (p: GlyphProps) => <Glyph {...p}><path d="m9 6 6 6-6 6" /></Glyph>;
export const SwapGlyph = (p: GlyphProps) => (
  <Glyph {...p}><path d="M7 7h11l-3-3M17 17H6l3 3" /></Glyph>
);
