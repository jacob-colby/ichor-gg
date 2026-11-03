/** "Updated 3 days ago · Open Beta 46", or null when the index has no date. */
import { relativeDate } from "../../lib/relativeDate";

export const freshness = (updated?: string, patch?: string) =>
  updated ? `Updated ${relativeDate(updated)}${patch ? ` · ${patch}` : ""}` : null;
