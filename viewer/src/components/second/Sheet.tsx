/** A real dialog that is a bottom sheet on a phone and a centred panel from
 * `lg` up. Modal: focus moves in, Tab is kept inside, Escape and the scrim
 * close it, and focus returns to whatever opened it.
 *
 * `initialFocus` lets a caller name the element that should take focus — the
 * enemy picker wants its search field, keyboard up, not the close button. */
import { useEffect, useId, useRef, type ReactNode, type RefObject } from "react";
import { CloseGlyph } from "./art";

export function Sheet({ title, onClose, children, initialFocus, footer, testId, wide = false }: {
  title: ReactNode;
  onClose: () => void;
  children: ReactNode;
  initialFocus?: RefObject<HTMLElement | null>;
  footer?: ReactNode;
  testId?: string;
  wide?: boolean;
}) {
  const panel = useRef<HTMLDivElement>(null);
  const titleId = useId();

  useEffect(() => {
    const opener = document.activeElement as HTMLElement | null;
    (initialFocus?.current ?? panel.current)?.focus();
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      document.body.style.overflow = prevOverflow;
      opener?.focus?.();
    };
    // Mount-only: focus moves in once, returns once.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const onKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Escape") { e.stopPropagation(); onClose(); return; }
    if (e.key !== "Tab" || !panel.current) return;
    const focusable = panel.current.querySelectorAll<HTMLElement>(
      'a[href], button:not([disabled]), input, [tabindex]:not([tabindex="-1"])');
    if (!focusable.length) return;
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-end justify-center lg:items-center" onKeyDown={onKeyDown}>
      <div className="absolute inset-0 bg-black/60" aria-hidden="true" onClick={onClose} />
      <div ref={panel} role="dialog" aria-modal="true" aria-labelledby={titleId} tabIndex={-1}
        data-testid={testId}
        className={`sheet-up relative flex max-h-[88dvh] w-full flex-col rounded-t-[var(--radius-xl)] border border-b-0 border-line bg-surface shadow-[var(--shadow-sheet)] focus:outline-none lg:max-h-[80vh] lg:rounded-[var(--radius-xl)] lg:border-b ${wide ? "lg:max-w-[640px]" : "lg:max-w-[480px]"}`}>
        <div aria-hidden="true" className="mx-auto mt-2 h-1 w-10 rounded-full bg-line lg:hidden" />
        <div className="flex items-center gap-3 px-4 pb-2 pt-2 lg:px-5 lg:pt-4">
          <h2 id={titleId} className="min-w-0 flex-1 font-cond text-head font-extrabold text-ink">{title}</h2>
          <button type="button" onClick={onClose} aria-label="Close"
            className="press -mr-2 flex h-11 w-11 items-center justify-center rounded-full text-muted hover:bg-surface-2 hover:text-ink">
            <CloseGlyph />
          </button>
        </div>
        <div className="min-h-0 flex-1 overflow-y-auto px-4 pb-4 lg:px-5">{children}</div>
        {footer && <div className="safe-bottom border-t border-line px-4 py-3 lg:px-5">{footer}</div>}
        {!footer && <div className="safe-bottom" />}
      </div>
    </div>
  );
}
