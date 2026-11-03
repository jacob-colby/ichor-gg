/** A god's secondary views (kit, every item ranked, ranking) inside the new
 *  chrome: a way back to the build, the god's name as the page's h1, and the
 *  existing body underneath. */
import type { ReactNode } from "react";
import type { God } from "../../types";
import { toHash } from "../../lib/useHashRoute";
import { Art, ChevronGlyph } from "./art";

export function GodSubPage({ god, title, children }: { god: God; title: string; children: ReactNode }) {
  return (
    <div className="mx-auto w-full max-w-[1240px] px-4 pt-4 lg:px-6 lg:pt-8">
      <a href={toHash.god(god.name)}
        className="press inline-flex h-11 items-center gap-1.5 font-cond text-[17px] font-bold uppercase text-muted hover:text-ink">
        <ChevronGlyph size={16} className="rotate-180" />{god.name}&rsquo;s build
      </a>
      <div className="mt-1 flex items-center gap-3">
        <Art name={god.name} kind="head" eager className="h-12 w-12 rounded-[12px]" />
        <div>
          <h1 className="font-cond text-[40px] font-extrabold leading-[0.9] text-ink">{god.name}</h1>
          <p className="text-note text-muted">{title}</p>
        </div>
      </div>
      <div className="mt-5 pb-8">{children}</div>
    </div>
  );
}
