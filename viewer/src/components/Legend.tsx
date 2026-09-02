import { useEffect, useRef } from "react";
import { toHash } from "../lib/useHashRoute";

function Swatch({ className }: { className: string }) {
  return <span className={`inline-block h-2 w-2 rounded-full ${className}`} />;
}

/**
 * The reference sheet, opened on demand from the `?` control.
 *
 * It used to open itself on first visit, which meant the first thing anyone
 * saw was 700 characters of body copy about a screen they weren't on. It's a
 * real dialog now: focus moves in, Tab is trapped, Escape and the backdrop
 * close it, and focus returns to whatever opened it.
 */
export function Legend({ onClose }: { onClose: () => void }) {
  const panelRef = useRef<HTMLDivElement>(null);
  const headingRef = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
    const opener = document.activeElement as HTMLElement | null;
    headingRef.current?.focus();

    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") { e.stopPropagation(); onClose(); return; }
      if (e.key !== "Tab") return;
      const focusable = panelRef.current?.querySelectorAll<HTMLElement>(
        'a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])',
      );
      if (!focusable || focusable.length === 0) return;
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      // Wrap at both ends so Tab can never reach the page behind the dialog.
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    };

    document.addEventListener("keydown", onKeyDown, true);
    return () => {
      document.removeEventListener("keydown", onKeyDown, true);
      opener?.focus?.();
    };
  }, [onClose]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" onClick={onClose}>
      <div
        ref={panelRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby="legend-title"
        className="max-h-[85vh] max-w-lg overflow-y-auto rounded-lg border border-line bg-bg1 p-5 shadow-raised"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="mb-3 flex items-start justify-between gap-4">
          <h2 id="legend-title" ref={headingRef} tabIndex={-1} className="font-display text-title font-bold text-ink focus:outline-none">
            How this works
          </h2>
          <button
            type="button"
            onClick={onClose}
            aria-label="Close"
            className="press -mr-1 -mt-1 rounded-sm px-2 py-1 text-body text-faint hover:text-ink"
          >
            ✕
          </button>
        </div>

        <div className="mb-4 flex flex-wrap gap-3 text-label text-muted">
          <span className="inline-flex items-center gap-1.5"><Swatch className="bg-under" />Model rates above the community</span>
          <span className="inline-flex items-center gap-1.5"><Swatch className="bg-premium" />Meta rates above the model</span>
          <span className="inline-flex items-center gap-1.5"><Swatch className="bg-gold" />The model&rsquo;s own signal</span>
        </div>

        {/* Every claim on this list is checked against what the app actually
            renders, not against what it used to. The 2026-08-23 audit (F3)
            found four stale strings here at once — the retired
            model-versus-meta positioning, a "Suggested" tab, a "BUILD ORDER"
            heading, and an aspect claim true for 7 gods of 73 — because this
            copy was written once and the surfaces moved underneath it. The
            tests beside this file pin each one to the string the UI renders. */}
        <ul className="flex flex-col gap-2 text-body text-muted">
          <li><b className="text-ink">Home</b> ranks gods on their own win rates in top-ranked Conquest play &mdash; never on anything this site models. <b className="text-ink">Pick a god</b> anywhere to see its builds.</li>
          <li><b className="text-ink">Model</b> is this site&rsquo;s own answer, with the community switched off. <b className="text-ink">Community</b> is SmiteBrain&rsquo;s high-elo meta. <b className="text-ink">Hybrid</b> keeps the model&rsquo;s strongest picks and lets real results fill the rest. Your saved builds are the named tabs.</li>
          <li><b className="text-ink">Balanced</b> and the flavour tabs (crit / burst / bruiser / anti-tank &hellip;) re-weight the same signals; the <b className="text-ink">Conquest / Joust / Arena</b> toggle changes mode, which re-weights the build and can drop items that mode&rsquo;s shop doesn&rsquo;t stock.</li>
          <li>The <b className="text-ink">Aspect</b> hexagon on a god&rsquo;s portrait switches to that god&rsquo;s aspect. It always changes the kit text; on most gods it leaves the six items alone, because only a few aspects have their own scoring behind them.</li>
          <li><b className="text-ink">BUY ORDER</b> is a recommended buy order; <b className="text-ink">flex</b> slots are the ones situational swaps replace.</li>
          <li>The <b className="text-ink">Items</b> shop rates every item <b className="text-under">Undervalued</b> / <b className="text-ink">Fair</b> / <b className="text-premium">Premium</b> by gold efficiency, with filters.</li>
          <li>Gods and items the community hasn&rsquo;t scored are shown <b className="text-ink">not measured</b> &mdash; never given an invented tier.</li>
          <li>Your builds save in <b className="text-ink">your browser</b> (nothing is uploaded). Scores are heuristics &mdash; a fan project, not official.</li>
        </ul>

        {/* The one thing this dialog could never answer in seven bullets, and
            the page a lost visitor is actually looking for. It was reachable
            only from the nav rail, last of six. */}
        <div className="mt-4 border-t border-line pt-3">
          <p className="text-body text-muted">
            <b className="text-ink">Every score on this site decomposes.</b> The signal weights, the
            fitted gold price of each stat, and what the model cannot see are all written down.
          </p>
          {/* On its own line rather than inline in the sentence: this is the
              control a lost visitor is meant to press, and inline it came out
              16px tall — inside SC 2.5.8's inline exception, but under the
              floor for the one link in this dialog that goes anywhere. */}
          <a
            href={toHash.method()}
            onClick={onClose}
            data-testid="legend-method-seam"
            className="press -mx-1 mt-1 inline-block rounded-sm px-1 py-1.5 text-body font-medium text-blue hover:underline"
          >
            How the model decides &rarr;
          </a>
        </div>

        {/* The footer used to hold this on every screen, forever — 43px of
            permanent chrome for a disclaimer you read once. It lives here now,
            where someone actually looking for it will look. */}
        <p className="mt-4 border-t border-line pt-3 text-small leading-relaxed text-faint">
          Build data derived from{" "}
          <a href="https://wiki.smite2.com" target="_blank" rel="noreferrer"
            className="underline decoration-line-strong underline-offset-2 hover:text-muted">wiki.smite2.com</a>
          {" "}and{" "}
          <a href="https://smitebrain.com" target="_blank" rel="noreferrer"
            className="underline decoration-line-strong underline-offset-2 hover:text-muted">SmiteBrain</a>.
          Suggested builds are heuristic — not official. A fan project, not affiliated with Hi-Rez.
        </p>

        <button type="button" onClick={onClose} className="press mt-4 rounded-md bg-gold px-4 py-1.5 text-body font-medium text-bg0">Got it</button>
      </div>
    </div>
  );
}
