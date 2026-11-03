/** Global navigation for the match-first chrome.
 *
 * One set of destinations, two shapes:
 *  - phone: a bottom tab bar — Match · Gods · Tiers · More — inside thumb
 *    reach, padded for the home indicator. "More" opens a sheet holding the
 *    full draft board, the reading routes, help, and the fan-project line.
 *  - desktop (lg+): a slim top bar carrying everything flat, because a mouse
 *    has no thumb to save.
 *
 * "Match" is home: the board with your god and the enemy team, and the build
 * under it. "Gods" is browsing — the list and every god's own page.
 */
import { useState, type ReactNode } from "react";
import { toHash } from "../../lib/useHashRoute";
import { relativeDate } from "../../lib/relativeDate";
import { GodsGlyph, MatchGlyph, MoreGlyph, TiersGlyph } from "./art";
import { Sheet } from "./Sheet";

export type NavTab = "match" | "gods" | "tiers" | "more";
export type MoreLink = "draft" | "items" | "patch" | "method";

const MORE_LINKS: { key: MoreLink; label: string; href: string; blurb: string }[] = [
  { key: "draft", label: "Draft board", href: toHash.draft(), blurb: "Both teams in full, with the threat table" },
  { key: "items", label: "Items", href: toHash.items(), blurb: "What each item's stats are worth in gold" },
  { key: "patch", label: "Patch notes", href: toHash.patch(), blurb: "What changed, and what it moved" },
  { key: "method", label: "Method", href: toHash.method(), blurb: "How the model chooses a six" },
];

/** The wordmark in the new voice: a violet kite and the name in the
 *  condensed face. The kite is the model's own mark, as before. */
export function Mark({ size = 22 }: { size?: number }) {
  return (
    <span role="img" aria-label="ichor" className="inline-flex items-center gap-1.5 leading-none">
      <span aria-hidden="true" className="mark inline-block bg-accent"
        style={{ height: size * 0.82, width: size * 0.82 * 0.587 }} />
      <span aria-hidden="true" className="font-cond font-extrabold text-ink" style={{ fontSize: size }}>ichor</span>
    </span>
  );
}

interface AppNavProps {
  active: NavTab;
  /** Sub-destination under More, for the desktop bar's current marker. */
  activeMore?: MoreLink;
  rosterHref: string;
  /** "Match · Ra" on desktop once your slot has a god. */
  matchGod?: string;
  onHelp: () => void;
  dataUpdated?: string;
  dataPatch?: string;
  /** Dev-only affordances, rendered on desktop only. */
  devSlot?: ReactNode;
}

const freshness = (updated?: string, patch?: string) =>
  updated ? `Updated ${relativeDate(updated)}${patch ? ` · ${patch}` : ""}` : null;

export function AppNav({ active, activeMore, rosterHref, matchGod, onHelp, dataUpdated, dataPatch, devSlot }: AppNavProps) {
  const [moreOpen, setMoreOpen] = useState(false);
  const stamp = freshness(dataUpdated, dataPatch);

  const primary: { key: Exclude<NavTab, "more">; label: string; href: string; Glyph: typeof MatchGlyph }[] = [
    { key: "match", label: "Match", href: toHash.home(), Glyph: MatchGlyph },
    { key: "gods", label: "Gods", href: rosterHref, Glyph: GodsGlyph },
    { key: "tiers", label: "Tiers", href: toHash.tiers(), Glyph: TiersGlyph },
  ];

  return (
    <>
      {/* Desktop: slim top bar. */}
      <header className="sticky top-0 z-40 hidden border-b border-line bg-ground/95 backdrop-blur-sm lg:block">
        <nav aria-label="Main" className="mx-auto flex h-14 max-w-[1240px] items-center gap-1 px-6">
          <a href={toHash.home()} aria-label="ichor — your match" className="press mr-5 flex h-11 items-center">
            <Mark />
          </a>
          {primary.map(({ key, label, href }) => (
            <a key={key} href={href} aria-current={active === key ? "page" : undefined}
              className={`press relative flex h-14 items-center px-3 font-cond text-[19px] font-bold uppercase ${
                active === key ? "text-ink after:absolute after:inset-x-3 after:bottom-0 after:h-0.5 after:bg-accent" : "text-muted hover:text-ink"}`}>
              {label}{key === "match" && matchGod ? <span className="ml-1.5 text-quiet">· {matchGod}</span> : null}
            </a>
          ))}
          <span aria-hidden="true" className="mx-2 h-5 w-px bg-line" />
          {MORE_LINKS.map(({ key, label, href }) => (
            <a key={key} href={href} aria-current={activeMore === key ? "page" : undefined}
              className={`press relative flex h-14 items-center px-2.5 text-[15px] font-medium ${
                activeMore === key ? "text-ink after:absolute after:inset-x-2.5 after:bottom-0 after:h-0.5 after:bg-accent" : "text-muted hover:text-ink"}`}>
              {label}
            </a>
          ))}
          <div className="ml-auto flex items-center gap-3">
            {stamp && (
              <span data-testid="header-freshness" title={dataUpdated} className="text-cap text-quiet">{stamp}</span>
            )}
            {devSlot}
            <button type="button" onClick={onHelp} aria-label="Help and credits"
              className="press flex h-10 items-center rounded-full border border-line px-3.5 text-note font-semibold text-muted hover:border-quiet hover:text-ink">
              Help
            </button>
          </div>
        </nav>
      </header>

      {/* Phone: bottom tab bar. */}
      <nav aria-label="Tabs" className="safe-bottom fixed inset-x-0 bottom-0 z-40 border-t border-line bg-ground/95 backdrop-blur-sm lg:hidden">
        <ul className="grid grid-cols-4">
          {primary.map(({ key, label, href, Glyph }) => (
            <li key={key}>
              <a href={href} aria-current={active === key ? "page" : undefined}
                className={`press relative flex h-16 flex-col items-center justify-center gap-0.5 font-cond text-[15px] font-bold uppercase ${
                  active === key ? "text-ink before:absolute before:inset-x-6 before:top-0 before:h-0.5 before:bg-accent" : "text-quiet"}`}>
                <Glyph size={22} />{label}
              </a>
            </li>
          ))}
          <li>
            <button type="button" onClick={() => setMoreOpen(true)} aria-haspopup="dialog"
              className={`press relative flex h-16 w-full flex-col items-center justify-center gap-0.5 font-cond text-[15px] font-bold uppercase ${
                active === "more" ? "text-ink before:absolute before:inset-x-6 before:top-0 before:h-0.5 before:bg-accent" : "text-quiet"}`}>
              <MoreGlyph size={22} />More
            </button>
          </li>
        </ul>
      </nav>

      {moreOpen && (
        <Sheet title="More" onClose={() => setMoreOpen(false)} testId="more-sheet">
          <ul className="divide-y divide-line">
            {MORE_LINKS.map(({ key, label, href, blurb }) => (
              <li key={key}>
                <a href={href} onClick={() => setMoreOpen(false)}
                  aria-current={activeMore === key ? "page" : undefined}
                  className="press flex min-h-14 flex-col justify-center py-2">
                  <span className={`font-cond text-row font-bold ${activeMore === key ? "text-accent" : "text-ink"}`}>{label}</span>
                  <span className="text-note text-muted">{blurb}</span>
                </a>
              </li>
            ))}
            <li>
              <button type="button" onClick={() => { setMoreOpen(false); onHelp(); }}
                className="press flex min-h-14 w-full flex-col justify-center py-2 text-left">
                <span className="font-cond text-row font-bold text-ink">Help</span>
                <span className="text-note text-muted">What the words and numbers mean, and credits</span>
              </button>
            </li>
          </ul>
          <p className="mt-4 text-cap text-quiet">
            {stamp && <>{stamp}. </>}A fan project — not affiliated with Hi-Rez.
          </p>
        </Sheet>
      )}
    </>
  );
}
