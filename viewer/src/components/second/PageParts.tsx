/** The small grammar every reading route shares in the Second Screen world:
 *  a condensed name for the page, the one claim under it, a seam to another
 *  surface, and text tabs. Kept together so Tiers, Items, Patch notes, Method
 *  and the draft board cannot drift into five versions of the same header. */
import type { ReactNode } from "react";
import { ChevronGlyph } from "./art";

/** `h1` in the caption face (a name, never a sentence), then the claim at
 *  `say` — the page's one answer, with its live numbers in semibold ink. */
export function PageHead({ title, children, testId }: { title: string; children?: ReactNode; testId?: string }) {
  return (
    <header className="pt-5 lg:pt-10" data-testid={testId}>
      <h1 className="font-cond text-god font-extrabold text-ink lg:text-[68px]">{title}</h1>
      {children && (
        <div className="mt-2.5 max-w-[46ch] text-say text-muted lg:mt-4 lg:max-w-[52ch] lg:text-[21px] lg:leading-[1.36]">
          {children}
        </div>
      )}
    </header>
  );
}

/** Semibold ink inside a claim: the measured part of the sentence. Weight,
 *  never violet — the One Hue Rule. */
export const Em = ({ children }: { children: ReactNode }) => (
  <span className="font-semibold text-ink">{children}</span>
);

/** A hand-off to another surface, named in the visitor's terms. */
export function Seam({ href, children, testId }: { href: string; children: ReactNode; testId?: string }) {
  return (
    <a href={href} data-testid={testId}
      className="press inline-flex min-h-11 items-center gap-1 font-cond text-[18px] font-bold uppercase text-muted hover:text-ink">
      {children}<ChevronGlyph size={16} />
    </a>
  );
}

/** Text tabs: the top bar's own grammar (ink + a 2px violet rule under the
 *  chosen one), as an `aria-pressed` group. For a choice of WHAT to show, not
 *  a mode — the mode keeps its segmented switch. */
export function TextTabs<K extends string>({ label, options, value, onChange, className = "" }: {
  label: string;
  options: { key: K; label: string }[];
  value: K;
  onChange: (k: K) => void;
  className?: string;
}) {
  return (
    <div role="group" aria-label={label} className={`flex gap-5 border-b border-line ${className}`}>
      {options.map((o) => {
        const on = o.key === value;
        return (
          <button key={o.key} type="button" aria-pressed={on} onClick={() => onChange(o.key)}
            className={`press relative -mb-px h-11 font-cond text-[19px] font-bold uppercase transition-colors duration-150 ${
              on ? "text-ink after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-accent" : "text-muted hover:text-ink"}`}>
            {o.label}
          </button>
        );
      })}
    </div>
  );
}
