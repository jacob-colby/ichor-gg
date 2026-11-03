/** True from the `lg` breakpoint (1024px) up — where the god page grows its
 *  second column. Rendering one layout rather than hiding the other keeps a
 *  single copy of each control in the accessibility tree. */
import { useEffect, useState } from "react";

const QUERY = "(min-width: 1024px)";
const match = () => typeof window !== "undefined" && typeof window.matchMedia === "function"
  && window.matchMedia(QUERY).matches;

export function useWide(): boolean {
  const [wide, setWide] = useState(match);
  useEffect(() => {
    if (typeof window.matchMedia !== "function") return;
    const mq = window.matchMedia(QUERY);
    const on = () => setWide(mq.matches);
    on();
    mq.addEventListener?.("change", on);
    return () => mq.removeEventListener?.("change", on);
  }, []);
  return wide;
}
