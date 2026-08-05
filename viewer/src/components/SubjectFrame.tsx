/* The shell's two honest levels: a subject, then lenses on it.
 *
 * The tool-first shell gave six destinations equal weight — but "Builds" was
 * really "a god", and a god could only be examined from that one route. Here
 * the subject is named at the top of every screen and its lenses sit under it,
 * so "where does Ra rank" and "what items does the model want for Ra" are one
 * click apart instead of unreachable.
 *
 * The whole roster is a subject too, and a first-class one: it keeps the
 * divergence board and the page's one claim. It is not a lobby you pass
 * through on the way to a god.
 */
import type { God, GodTierEntry } from "../types";
import { godLane, laneTextClass, godRoleTextClass, damageTextClass } from "../lib/roleAccent";
import { usePins } from "../lib/pins";
import { BookmarkIcon } from "./BookmarkIcon";
import { rateText, matchesText } from "../lib/standings";
import { encodeDraftHash, useDraft, MODE_TEAM_SIZE, type DraftMode } from "../lib/draft";
import { iconSlug } from "../lib/builds";
import { lensHash, toHash, type GodLens, type Lens, type RosterLens } from "../lib/useHashRoute";
import { useState } from "react";

const ROSTER_TABS: { lens: RosterLens; label: string }[] = [
  { lens: "board", label: "Board" },
  { lens: "tiers", label: "Gods" },
  { lens: "items", label: "Items" },
  { lens: "draft", label: "Draft" },
  { lens: "patch", label: "Patch Notes" },
  { lens: "method", label: "Method" },
];

const GOD_TABS: { lens: GodLens; label: (g: string) => string }[] = [
  { lens: "builds", label: () => "Builds" },
  { lens: "kit", label: () => "Kit" },
  { lens: "items", label: () => "Items" },
  { lens: "ranking", label: () => "Ranking" },
];

function GodArt({ name }: { name: string }) {
  const [tries, setTries] = useState(0);
  const cls = "h-11 w-11 shrink-0 rounded-lg object-cover sm:h-[52px] sm:w-[52px]";
  if (tries > 1) {
    return (
      <span aria-hidden="true" className={`${cls} flex items-center justify-center bg-bg3 font-display text-lead font-bold text-faint`}>
        {name.slice(0, 1)}
      </span>
    );
  }
  return (
    <img src={`/icons/${iconSlug(name)}-head.png${tries ? "?r=1" : ""}`} alt="" loading="lazy"
      onError={() => setTries((t) => t + 1)} className={cls} />
  );
}

/** What this god's record actually is, stated in words.
 *
 * This used to print the model's score against the community's and a verdict
 * on the gap between them. The gap was the product's headline and it did not
 * survive measurement — see `pipeline/smite/tierlist.py`. What is left is the
 * half that was always the real measurement, plus the sample behind it, which
 * is the thing a tier letter hides.
 *
 * It lives in the frame rather than the builds view because it's the one fact
 * that stays true of the god on every lens. */
function Verdict({ entry }: { entry?: GodTierEntry }) {
  if (!entry) return null;
  if (entry.score == null) {
    return (
      <p data-testid="god-verdict" className="mt-1 text-label text-muted">
        not enough tracked matches to place this god
      </p>
    );
  }
  return (
    <p data-testid="god-verdict" className="mt-1 flex flex-wrap items-baseline gap-x-3 gap-y-0.5 text-label text-faint">
      {entry.tier_score && (
        <span>tier <span className="font-mono text-gold">{entry.tier_score}</span></span>
      )}
      <span>wins <span className="font-mono text-ink-soft">{rateText(entry.win_rate)}</span></span>
      <span>over <span className="font-mono text-ink-soft">{matchesText(entry.matches)}</span> matches</span>
      {typeof entry.play_share === "number" && (
        <span>picked in <span className="font-mono text-ink-soft">{rateText(entry.play_share)}</span></span>
      )}
    </p>
  );
}

/** The lens strip on its own, so the shell can seat it in the navbar where
 *  there is room and drop it to its own row where there isn't. */
export function LensTabs({ god, lens, className = "", testId, compact = false }: {
  god?: string; lens: Lens; className?: string; testId?: string;
  /** Seated inside the navbar row, where it must not drive the row's height. */
  compact?: boolean;
}) {
  const tabs: { lens: Lens; label: string; href: string }[] = god
    ? GOD_TABS.map((t) => ({ lens: t.lens, label: t.label(god), href: lensHash(t.lens, god) }))
    : ROSTER_TABS.map((t) => ({ lens: t.lens, label: t.label, href: lensHash(t.lens) }));

  return (
    <nav aria-label={god ? `${god} views` : "Roster views"} data-testid={testId} className={className}>
      <div className="mx-auto flex w-full max-w-[1440px] items-center gap-1 overflow-x-auto">
        {tabs.map((t) => {
          const active = t.lens === lens;
          return (
            <a key={t.lens} href={t.href} aria-current={active ? "page" : undefined}
              className={`press shrink-0 whitespace-nowrap border-b-2 font-display text-small font-semibold transition-colors duration-[150ms] ease-standard ${
                compact ? "px-2.5 py-1.5" : "px-3 py-2 sm:py-2.5"} ${
                active ? "border-gold text-gold" : "border-transparent text-muted hover:text-ink"}`}>
              {t.label}
            </a>
          );
        })}
      </div>
    </nav>
  );
}

export interface SubjectFrameProps {
  /** The current subject. Absent means the whole roster. */
  god?: God;
  godName?: string;
  lens: Lens;
  /** This god's tier row for the mode in view. */
  tierEntry?: GodTierEntry;
  /** Roster headline figures, computed once by the caller from the same board
   *  Home draws, so the header and the page can't disagree. */
  roster: { total: number; ranked: number; unranked: number };
  modeLabel: string;
  onPickGod: () => void;
}

export function SubjectFrame({
  god, godName, lens, tierEntry, roster, modeLabel, onPickGod,
}: SubjectFrameProps) {
  const name = god?.name ?? godName;
  const lane = godLane(god?.role);
  const { toggle: togglePin, isPinned } = usePins();
  const saved = !!name && isPinned(name);
  const { draft, mode: savedMode } = useDraft();

  const draftHref = (subject: string) => {
    const started = draft.allies.some(Boolean) || draft.enemies.some(Boolean);
    const m: DraftMode = started ? savedMode : (modeLabel.toLowerCase() === "joust" ? "joust" : "conquest");
    const allies = draft.allies.filter((n) => n && n !== subject).slice(0, MODE_TEAM_SIZE[m] - 1);
    return encodeDraftHash(m, { allies: [subject, ...allies], enemies: draft.enemies.filter((n) => n && n !== subject) });
  };

  return (
    <>
      <div data-testid="subject-header" className="plane border-b border-line bg-bg1 px-4 py-2 sm:px-6 sm:py-3">
        <div className="mx-auto flex w-full max-w-[1440px] flex-wrap items-center gap-x-4 gap-y-1.5">
          {name ? (
            <>
              <button type="button" onClick={onPickGod}
                aria-label={`Change god — currently ${name}`}
                className="press shrink-0 rounded-lg">
                <GodArt name={name} />
              </button>
              <div className="min-w-0 flex-1">
                {/* The bookmark sits with the name because that is what it
                    marks. Home has always told readers to "bookmark a god from
                    its page" and there was no control here to do it with —
                    saving a god was only possible from the roster grid. */}
                <div className="flex min-w-0 items-center gap-1.5">
                  <h1 className="min-w-0 truncate font-display text-title font-bold leading-none text-ink">{name}</h1>
                  <button
                    type="button"
                    onClick={() => togglePin(name)}
                    aria-pressed={saved}
                    aria-label={saved ? `Remove ${name} from your bookmarks` : `Bookmark ${name}`}
                    title={saved
                      ? `Bookmarked — shows in search, the draft picker and the tier list`
                      : `Bookmark ${name} to surface it in search, the draft picker and the tier list`}
                    className={`press -my-1 flex h-8 w-8 shrink-0 items-center justify-center rounded-md transition-colors duration-[150ms] ease-standard ${
                      saved ? "text-gold hover:text-gold/80" : "text-faint hover:text-ink-soft"}`}
                  >
                    <BookmarkIcon filled={saved} size={16} />
                  </button>
                </div>
                {god && (
                  <p className="mt-1 text-small text-muted">
                    {god.pantheon}
                    {god.role && <> · <span className={godRoleTextClass(god)}>{god.role}</span></>}
                    {/* Only when the lane adds something: for most gods the role
                        *is* the lane, and printing both gave Ra
                        "Egyptian · Mid · Mid · magical". */}
                    {lane && !god.role?.includes(lane) && (
                      <> · <span className={laneTextClass(lane)}>{lane}</span></>
                    )}
                    {god.damage_type && <> · <span className={damageTextClass(god.damage_type)}>{god.damage_type}</span></>}
                  </p>
                )}
                <Verdict entry={tierEntry} />
              </div>
              <div className="flex shrink-0 flex-wrap items-center gap-2">
                <a href={draftHref(name)}
                  aria-label={`Draft with ${name}`}
                  title={draft.allies.some(Boolean) || draft.enemies.some(Boolean)
                    ? `Puts ${name} in your slot and keeps the comp you've already entered`
                    : `Opens the draft board with ${name} in your slot`}
                  className="press rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-small text-blue transition-colors duration-[150ms] ease-standard hover:border-line-strong">
                  Draft<span className="hidden sm:inline"> with {name}</span> →
                </a>
                <button type="button" onClick={onPickGod} aria-label="Change god"
                  className="press hidden rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-small text-muted hover:text-ink sm:block">
                  Change<span className="hidden sm:inline"> god</span>
                </button>
                <a href={toHash.home()}
                  className="press hidden rounded-md px-2 py-1.5 text-small text-faint hover:text-ink sm:inline-block">
                  All {roster.total} gods ↩
                </a>
              </div>
            </>
          ) : (
            <>
              <div className="min-w-0 flex-1">
                {/* Not a heading: on the roster the page's own claim is the h1,
                    and it makes a stronger argument than a route label. */}
                <p className="font-display text-lead font-bold leading-none text-ink">
                  All {roster.total} gods
                </p>
                {/* No mode word here. These counts come from the tier list's
                    Conquest slice, but the tier list has its own mode control —
                    a label the header can't see change would assert Conquest
                    over a page showing Joust. */}
                {/* Inventory, not argument. This used to carry the disputed
                    and agreed counts — the same figures the page's own claim
                    makes 60px below, which spent the headline's punchline
                    before it landed. The header says what's in the index; the
                    claim says what the model thinks of it. */}
                <p className="mt-1 flex flex-wrap items-baseline gap-x-3 gap-y-0.5 text-label text-faint">
                  {roster.ranked > 0 && (
                    <span><span className="font-mono text-ink-soft">{roster.ranked}</span> placed on real results</span>
                  )}
                  {roster.unranked > 0 && (
                    <span><span className="font-mono text-ink-soft">{roster.unranked}</span> not measured</span>
                  )}
                </p>
              </div>
              <button type="button" onClick={onPickGod}
                className="press shrink-0 rounded-md border border-line bg-bg2 px-3 py-1.5 text-small text-ink-soft hover:border-line-strong">
                Choose a god
              </button>
            </>
          )}
        </div>
      </div>

      {/* Below md the navbar has no room for these, so they keep their own
          strip; above it the shell renders them inline and this is hidden. */}
      <LensTabs god={name} lens={lens} testId="lens-tabs-strip"
        className="border-b border-line px-4 sm:px-6 lg:hidden" />
    </>
  );
}
