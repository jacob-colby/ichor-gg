/** The "Type it" chrome: the command field is the navigation.
 *
 * Desktop: a top bar — wordmark, the field (large, the widest thing in the
 * bar), and Menu. Phone: the same field docked at the bottom, inside thumb
 * reach and lifted above the keyboard, with Menu beside it. There is no tab
 * bar: everything a tab bar held is either typed ("ra vs hecate") or one
 * level down in Menu (Draft, Gods, Tiers, Items, Patch notes, Method, Help,
 * and the fan-project line). */
import type { ReactNode } from "react";
import { toHash } from "../../lib/useHashRoute";
import { Mark } from "../second/AppNav";
import { BuildGlyph, DraftGlyph, GodsGlyph, MoreGlyph } from "../second/art";
import { Sheet } from "../second/Sheet";

export type MenuKey = "build" | "draft" | "gods" | "tiers" | "items" | "patch" | "method";

export function TopBar({ field, onMenu, stamp, updated }: {
  field: ReactNode; onMenu: () => void; stamp: string | null; updated?: string;
}) {
  return (
    <header className="sticky top-0 z-40 border-b border-line bg-ground">
      <div className="mx-auto flex h-[76px] max-w-[1240px] items-center gap-6 px-6">
        <a href={toHash.home()} aria-label="ichor — home" className="press flex h-11 flex-none items-center">
          <Mark size={24} />
        </a>
        <div className="min-w-0 max-w-[760px] flex-1">{field}</div>
        <div className="ml-auto flex flex-none items-center gap-4">
          {stamp && <span data-testid="header-freshness" title={updated} className="text-cap text-quiet">{stamp}</span>}
          <MenuButton onClick={onMenu} />
        </div>
      </div>
    </header>
  );
}

export function MenuButton({ onClick, stacked = false }: { onClick: () => void; stacked?: boolean }) {
  return (
    <button type="button" onClick={onClick} aria-haspopup="dialog"
      className={`press flex flex-none items-center justify-center rounded-[14px] border border-line font-cond font-bold uppercase text-muted hover:border-quiet hover:text-ink ${
        stacked ? "h-14 w-14 flex-col gap-0 text-[13px]" : "h-11 gap-1.5 px-3.5 text-[18px]"}`}>
      <MoreGlyph size={stacked ? 20 : 18} />Menu
    </button>
  );
}

/** The phone's bottom dock. Solid ground (no backdrop blur): a blur would
 *  make this the containing block for the field's fixed scrim. */
export function Dock({ children }: { children: ReactNode }) {
  return (
    <div className="fixed inset-x-0 bottom-0 z-40 border-t border-line bg-ground px-3 pt-2 pb-[calc(8px+env(safe-area-inset-bottom))]">
      {children}
    </div>
  );
}

const LINKS: { key: MenuKey; label: string; blurb: string; href: (god?: string) => string }[] = [
  { key: "draft", label: "Draft", blurb: "The full board — allies, threats, both teams", href: () => toHash.draft() },
  { key: "gods", label: "Gods", blurb: "Every god, by face and role", href: () => toHash.home() },
  { key: "tiers", label: "Tiers", blurb: "Every god, ranked on real Conquest results", href: () => toHash.tiers() },
  { key: "items", label: "Items", blurb: "What each item's stats are worth in gold", href: () => toHash.items() },
  { key: "patch", label: "Patch notes", blurb: "What changed, and what it moved", href: () => toHash.patch() },
  { key: "method", label: "Method", blurb: "How the model chooses a six", href: () => toHash.method() },
];

export function MenuSheet({ onClose, onHelp, current, buildGod, stamp, devSlot }: {
  onClose: () => void; onHelp: () => void; current?: MenuKey; buildGod?: string; stamp: string | null; devSlot?: ReactNode;
}) {
  const icon = (k: MenuKey) => k === "draft" ? <DraftGlyph size={20} /> : k === "gods" ? <GodsGlyph size={20} /> : null;
  return (
    <Sheet title="Menu" onClose={onClose} testId="menu-sheet">
      <ul className="divide-y divide-line">
        {buildGod && (
          <li>
            <a href={toHash.god(buildGod)} onClick={onClose} aria-current={current === "build" ? "page" : undefined}
              className="press flex min-h-14 items-center gap-3 py-2">
              <span className="flex h-5 w-5 items-center justify-center text-quiet"><BuildGlyph size={20} /></span>
              <span className="min-w-0 flex-1">
                <span className={`block font-cond text-row font-bold ${current === "build" ? "text-accent" : "text-ink"}`}>Build · {buildGod}</span>
                <span className="block text-note text-muted">Back to your god&rsquo;s six</span>
              </span>
            </a>
          </li>
        )}
        {LINKS.map(({ key, label, blurb, href }) => (
          <li key={key}>
            <a href={href()} onClick={onClose} aria-current={current === key ? "page" : undefined}
              className="press flex min-h-14 items-center gap-3 py-2">
              <span className="flex h-5 w-5 items-center justify-center text-quiet">{icon(key)}</span>
              <span className="min-w-0 flex-1">
                <span className={`block font-cond text-row font-bold ${current === key ? "text-accent" : "text-ink"}`}>{label}</span>
                <span className="block text-note text-muted">{blurb}</span>
              </span>
            </a>
          </li>
        ))}
        <li>
          <button type="button" onClick={() => { onClose(); onHelp(); }} aria-label="Help and credits"
            className="press flex min-h-14 w-full items-center gap-3 py-2 text-left">
            <span className="h-5 w-5" />
            <span className="min-w-0 flex-1">
              <span className="block font-cond text-row font-bold text-ink">Help</span>
              <span className="block text-note text-muted">What the words and numbers mean, and credits</span>
            </span>
          </button>
        </li>
      </ul>
      {devSlot && <div className="mt-3 flex flex-wrap gap-2">{devSlot}</div>}
      <p className="mt-4 text-cap text-quiet">
        {stamp && <span data-testid="menu-freshness">{stamp}. </span>}A fan project — not affiliated with Hi-Rez.
      </p>
    </Sheet>
  );
}

/** A small "how to type it" line for the landing page — the grammar, shown
 *  as the chips it produces. */
export function GrammarHint() {
  const part = (t: string, cls: string) => <span className={`rounded-[8px] px-1.5 py-0.5 font-cond text-[17px] font-bold ${cls}`}>{t}</span>;
  return (
    <p className="flex flex-wrap items-center gap-x-1.5 gap-y-2 text-note text-muted">
      {part("Ra", "bg-accent/15 text-ink ring-[1.5px] ring-accent")}
      <span>you</span>
      <span className="font-cond text-[17px] font-bold text-quiet">vs</span>
      {part("Hecate", "bg-surface-2 text-ink ring-[1.5px] ring-ink")}
      {part("Ymir", "bg-surface-2 text-ink ring-[1.5px] ring-ink")}
      <span>enemies</span>
      {part("Joust", "border border-line text-muted")}
      <span>mode</span>
      {part("Aspect", "border border-line text-muted")}
    </p>
  );
}
