"""Tests that read the LIVE community window, and what they may expect of it.

The community-data counterpart of `frozen.py`. That module exists because a
worked example read off the live `data/` is also a claim about which PATCH is
current, so a wiki refresh turned it red with no code change. This one exists
because a value read off the live community window is also a claim about which
DAY it is.

WHY IT MATTERS NOW (2026-11-07). `main` merges a pull request only when
"Pipeline suite" and "Viewer suite and build" pass on it, the ruleset has no
bypass actors, and the daily refresh is moving to a pull request of its own
(PR #120). So a test that expects a value the window moves every day does not
report stale data after it lands, as it did before: it stops the day's data
landing at all. NO TEST MAY BLOCK A DAY'S COMMUNITY DATA UNLESS THAT DATA IS
ACTUALLY WRONG.

THE WINDOW IS CUMULATIVE INSIDE A PATCH. `refresh.choose_community_window`
reads one SmiteBrain patch window (`?time=obNN`) per run, and that window keeps
the same name and start date for the whole patch while its sample grows. From
the snapshot history, not assumed:

    window  start       end         matches  builds*   builds/match
    ob46    2026-10-20  2026-10-28        -   39,429        -
    ob46    2026-10-20  2026-10-29        -   44,721        -
    ob46    2026-10-20  2026-10-30        -   50,029        -
    ob46    2026-10-20  2026-11-03   14,667   67,532     4.604
    ob47    2026-11-03  2026-11-06    2,859   12,774     4.468
    ob47    2026-11-03  2026-11-07    4,089   18,535     4.533

    * `matches_played / use_rate`, exact and unanimous across the items. The
      three provenance fields were null before b7e4fde3 (2026-11-04), so the
      early OB46 rows have the derived count only. The 11-07 row was fetched
      live; the scheduled runs of 11-05 and 11-07 computed theirs and could
      not push them (GH013).

STATE.md's hand-kept Community sample row says the same of older windows:
12,786 -> 14,126 -> 15,677 matches on three consecutive days in August.

SO EVERY EXPECTED VALUE READ OFF THE LIVE WINDOW IS ONE OF THREE KINDS.

  DAILY. Moves on every refresh: a match or build count, `window_end`, a ratio
  of two counts, any model output that reads the community signals (a core, a
  verdict, a coverage figure). NEVER PIN ONE. Write the invariant the pin stood
  for, so it still catches the failure it was written for:
    * a count: positive, and not below the floor recorded when the window was
      declared (the window only grows, so falling below it means the read is
      not the window it claims to be);
    * an end date: on or after the window's start, not before the declared
      floor, and not in the future;
    * a ratio: inside the range the physics allows, not to one decimal;
    * a figure shown to a reader: DERIVED from the shipped table in the test,
      never typed in.

  PATCH-BOUNDARY. Moves only when the window does: `window`, `window_start`,
  the window's name in a label, and anything a human wrote down about the
  window as a whole. PIN THESE LITERALLY. A pin like that fires at every patch
  boundary whatever the new window's size, so it detects CHANGE, not thinness,
  and updating it DECLARES THE NEW WINDOW ESTABLISHED. That is Jacob's call,
  not test maintenance (589e9a4e declared Open Beta 47 on 2026-11-06).

  GENUINE-ERROR-ONLY. True of every healthy window and false only when the data
  is wrong: a complete record for the gods that had one, provenance present,
  builds and matches being different quantities. The 2026-11-04 one-day window
  (6158066f: 166 items, 48 of 96 complete records) is the case this class is
  for, and it must stay red on it. Replaying the suite on that snapshot is how
  a change to a test in this class is checked.

DECLARING A NEW WINDOW moves, together and by hand: the two pins and two floors
in `test_refresh.test_the_shipped_file_now_carries_all_three`, the window name
in `test_side_by_side.test_the_shipped_label_names_the_community_window_and_its_real_size`,
and STATE.md section 7's Community sample row. Nothing restamps them for you,
and nothing should: a gate that rewrites its own expected values has stopped
being a gate.

EXPERT-REVIEW BASELINES are a model output on the live data, so they are DAILY
by this rule (the `item-overweighted` baseline flipped three times inside Open
Beta 40 on community refreshes alone: 08-29, 09-01 and 09-07). Each one names
the window it was checked on (`verdict_window`, in `data/_expert_reviews.yaml`)
and is asserted only on that data; see `test_expert_review`.

WHAT THIS DOES NOT COVER. Arithmetic on fixed inputs reads `frozen.py`. A
consecutive-day check (today's count against yesterday's, rather than against
the declared floor) needs the previous shipped file, which the CI checkout does
not have; it belongs at the write, in `refresh`, next to
`_refuse_community_collapse`.
"""
import json
from datetime import date, timedelta

from smite import refresh


def shipped_community_table() -> dict:
    """`data/_community_items.json` as the daily refresh last wrote it."""
    return json.loads((refresh.DATA_ROOT / refresh.COMMUNITY_ITEMS_FILE)
                      .read_text(encoding="utf-8"))


def latest_plausible_day() -> str:
    """The latest `window_end` a healthy table can carry: tomorrow, so a run
    that crosses midnight UTC against a clock in another zone is never red."""
    return (date.today() + timedelta(days=1)).isoformat()
