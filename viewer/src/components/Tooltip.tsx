import { useRef, useState, type ReactNode } from "react";

interface TooltipProps {
  content: ReactNode;
  children: ReactNode;
}

/** Hover/focus tooltip. Mouse-hover opens after a short delay; keyboard focus
 * opens immediately (a11y). Flips above the trigger and shifts horizontally so
 * it never clips at the viewport edge. role="tooltip" for screen readers. */
export function Tooltip({ content, children }: TooltipProps) {
  const [open, setOpen] = useState(false);
  const [pos, setPos] = useState<{ left: number; top: number; above: boolean }>({
    left: 0,
    top: 0,
    above: false,
  });
  const timer = useRef<number | undefined>(undefined);
  const wrapRef = useRef<HTMLSpanElement>(null);

  const place = () => {
    const el = wrapRef.current;
    if (!el) return;
    const r = el.getBoundingClientRect();
    const width = 260;
    let left = r.left + r.width / 2 - width / 2;
    left = Math.max(8, Math.min(left, window.innerWidth - width - 8));
    const above = r.top > 220;
    const top = above ? r.top - 8 : r.bottom + 8;
    setPos({ left, top, above });
    setOpen(true);
  };
  const openNow = () => place();
  const openDelayed = () => {
    timer.current = window.setTimeout(place, 150);
  };
  const hide = () => {
    window.clearTimeout(timer.current);
    setOpen(false);
  };

  return (
    <span
      ref={wrapRef}
      onMouseEnter={openDelayed}
      onMouseLeave={hide}
      onFocus={openNow}
      onBlur={hide}
      onKeyDown={(e) => e.key === "Escape" && hide()}
      className="relative inline-flex"
      tabIndex={0}
    >
      {children}
      {open && (
        <div
          role="tooltip"
          style={{ position: "fixed", left: pos.left, top: pos.top, width: 260 }}
          className={`z-50 rounded-md border border-line bg-bg2 p-3 text-small text-ink-soft shadow-card ${
            pos.above ? "-translate-y-full" : ""
          }`}
        >
          {content}
        </div>
      )}
    </span>
  );
}
