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

/** A team slot's keyboard focus, drawn on its portrait tile rather than on
 *  the button around it. The button is the whole column (tile, and the name
 *  under it on the panel and the draft board) with square corners, so the
 *  global `:focus-visible` outline came out as a square box around a rounded
 *  tile — a different shape from the slot it marked. `SLOT_BUTTON` goes on
 *  the button, `SLOT_TILE_FOCUS` on the tile (filled or empty). Same 2px
 *  violet at a 2px offset as everywhere else; only where it is drawn moves. */
export const SLOT_BUTTON = "group focus-visible:outline-none";
export const SLOT_TILE_FOCUS =
  "group-focus-visible:outline-2 group-focus-visible:outline-offset-2 group-focus-visible:outline-solid group-focus-visible:outline-accent";

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
/** A tick: "this one is in the build on screen". */
export const CheckGlyph = (p: GlyphProps) => <Glyph {...p}><path d="m5 12.5 4.5 4.5L19 7.5" /></Glyph>;
export const SwapGlyph = (p: GlyphProps) => (
  <Glyph {...p}><path d="M7 7h11l-3-3M17 17H6l3 3" /></Glyph>
);

/** The aspect's mark: the pointy-top hexagon SMITE puts on an aspected
 *  portrait. The only hexagon on the site. The aspect switch (god page and
 *  draft board), the command field's aspect chip, a recent god opened with
 *  its aspect on (god select's row and the field's suggestions) and the kept
 *  routes' portrait badge all draw this one, so none of them can drift.
 *
 *  Always Aspect Ember, on and off, at rest and on hover (Jacob, 2026-11-09:
 *  "always bright orange"). The colour is set here, not taken from the
 *  caller's text colour, so no surrounding `text-muted` or hover can grey it.
 *  Off is the outline. On fills it and keeps the notch out of the middle, so
 *  "on" reads as a shape and not only as more orange. The kept badge is 20px
 *  on artwork whose colour nobody controls. The outline stays drawn in both
 *  states, so the mark is the same size either way and only the fill changes.
 *  The fill fades in over 150ms on `--ease-standard`, and with no transition
 *  under `prefers-reduced-motion`.
 *
 *  Against every plane it sits on, #ef8034 clears WCAG 1.4.11's 3:1 for a
 *  graphical object: 7.0:1 on ground (the switch, off), 6.7:1 on surface
 *  (the command field's chip, a recent card), 6.0:1 on surface-2 (a recent
 *  card on hover), 6.0:1 on the switch's on-state wash (ember at 12% over
 *  ground composites to #2b1e18). The notch (ground) on the fill is 7.0:1.
 *  The on-state border (ember at 45%) is 2.3:1, which is decoration: the
 *  fill is what says "on". The app is dark only, so that is every theme.
 *  Measured 2026-11-09 from the browser's computed colours. */
export function AspectHex({ on, className = "" }: { on: boolean; className?: string }) {
  const fade = "transition-[fill-opacity,opacity] duration-150 ease-[var(--ease-standard)] motion-reduce:transition-none";
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true" data-aspect-hex={on ? "on" : "off"} className={`flex-none ${className}`}>
      <path d="M12 1.6 21 6.8v10.4L12 22.4 3 17.2V6.8z" fill="var(--color-aspect)" fillOpacity={on ? 1 : 0}
        stroke="var(--color-aspect)" strokeWidth={2.4} strokeLinejoin="round" className={fade} />
      <path d="M12 6.4 17 9.3v5.4L12 17.6 7 14.7V9.3z" fill="var(--color-bg0)" opacity={on ? 1 : 0} className={fade} />
    </svg>
  );
}
