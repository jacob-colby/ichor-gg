import { useState } from "react";
import { iconSlug } from "../lib/builds";

/** An item's icon, falling back to its initial when the image is missing. */
export function ItemIcon({ name, className }: { name: string; className: string }) {
  const [tries, setTries] = useState(0);
  if (tries > 1) {
    return (
      <span aria-hidden="true"
        className={`flex flex-none items-center justify-center rounded-sm bg-bg3 font-display text-label font-bold text-faint ${className}`}>
        {name.slice(0, 1)}
      </span>
    );
  }
  return (
    <img
      src={`/icons/${iconSlug(name)}.png${tries ? "?r=1" : ""}`}
      alt=""
      loading="lazy"
      onError={() => setTries((t) => t + 1)}
      className={`flex-none rounded-sm bg-bg2 object-cover ${className}`}
    />
  );
}
