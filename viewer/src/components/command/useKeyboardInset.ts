/** How far the on-screen keyboard covers the layout viewport, in CSS px.
 *
 * The command field lives at the bottom of a phone, and iOS Safari does not
 * resize the layout viewport for the keyboard — a `bottom: 0` dock would sit
 * under it. `visualViewport` reports the part still visible; the difference
 * is how far the dock has to lift to stay above the keys. */
import { useEffect, useState } from "react";

export function useKeyboardInset(active: boolean): number {
  const [inset, setInset] = useState(0);
  useEffect(() => {
    const vv = typeof window !== "undefined" ? window.visualViewport : null;
    if (!active || !vv) { setInset(0); return; }
    const on = () => setInset(Math.max(0, Math.round(window.innerHeight - vv.height - vv.offsetTop)));
    on();
    vv.addEventListener("resize", on);
    vv.addEventListener("scroll", on);
    return () => { vv.removeEventListener("resize", on); vv.removeEventListener("scroll", on); };
  }, [active]);
  return inset;
}
