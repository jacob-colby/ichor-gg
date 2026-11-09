"""Tests that read the LIVE community window, and what they may expect of it.

The community-data counterpart of `frozen.py`. That module exists because a
worked example read off the live `data/` is also a claim about which PATCH is
current, so a wiki refresh turned it red with no code change. This one exists
because a value read off the live community window is also a claim about which
DAY it is, and which PATCH WINDOW.

WHY IT MATTERS (2026-11-07). `main` merges a pull request only when
"Pipeline suite" and "Viewer suite and build" pass on it, the ruleset has no
bypass actors, and the daily refresh lands as a pull request of its own
(PR #120). So a test that expects a value the window moves does not report
stale data after it lands, as it did before: it stops the day's data landing
at all. NO TEST MAY BLOCK A DAY'S COMMUNITY DATA UNLESS THAT DATA IS ACTUALLY
WRONG.

A NEW WINDOW LANDS BY ITSELF (Jacob, 2026-11-08). When a new patch's community
window appears, the daily refresh lands it. Nobody declares it. The guards are
automatic, and they sit at the WRITE, in `refresh`, where the previous data is
still in hand:

  * the coverage rule, `refresh.choose_community_window`: the newest window is
    read only once it covers as many gods as the one before it (on 2026-11-04
    the one-day ob47 window covered 86 gods against ob46's 94, and the rule
    keeps ob46 on such a day);
  * the collapse refusal, `refresh._refuse_community_collapse`: no
    roster-wide loss of complete six-slot records;
  * the regression refusal, `refresh._refuse_window_regression` (2026-11-09):
    never backwards. The same window with fewer matches or an earlier end,
    or an older window, is refused before anything is written. This is the
    consecutive-day check this file used to say belonged at the write.

The first two are the guards Jacob named; the third only refuses a table
going backwards, so it can never stop a new window. Nothing in this directory
may stand between them and `main`.

THE WINDOW IS CUMULATIVE INSIDE A PATCH, AND KEEPS GROWING AFTER IT CLOSES.
`choose_community_window` reads one SmiteBrain patch window (`?time=obNN`) per
run, and that window keeps the same name and start date for the whole patch
while its sample grows. From the snapshot history, not assumed:

    window  start       end         matches  builds*   builds/match
    ob46    2026-10-20  2026-10-28        -   39,429        -
    ob46    2026-10-20  2026-10-29        -   44,721        -
    ob46    2026-10-20  2026-10-30        -   50,029        -
    ob46    2026-10-20  2026-11-03   14,667   67,532     4.604
    ob47    2026-11-03  2026-11-06    2,859   12,774     4.468
    ob47    2026-11-03  2026-11-07    4,089   18,535     4.533
    ob47    2026-11-03  2026-11-08    5,119   23,540     4.599
    ob47    2026-11-03  2026-11-09    6,302        -        -   (live, 11-09)
    ob46    2026-10-20  2026-11-03   16,195        -        -   (live, 11-09)

    * `matches_played / use_rate`, exact and unanimous across the items. The
      three provenance fields were null before b7e4fde3 (2026-11-04), so the
      early OB46 rows have the derived count only. The 11-07 row was fetched
      live; the scheduled runs of 11-05 and 11-07 computed theirs and could
      not push them (GH013). The two 11-09 rows are the god index read live
      on 2026-11-09: a CLOSED window keeps its end date and its count still
      rises (ob46, 14,667 on 11-05, 16,195 on 11-09), so "closed" is not
      "frozen", and no read on record has ever fallen.

STATE.md's hand-kept Community sample row says the same of older windows:
12,786 -> 14,126 -> 15,677 matches on three consecutive days in August.

SO EVERY EXPECTED VALUE READ OFF THE LIVE WINDOW IS ONE OF THREE KINDS, AND
ONLY THE THIRD MAY BE ASSERTED AS IT IS.

  DAILY. Moves on every refresh: a match or build count, `window_end`, a ratio
  of two counts, any model output that reads the community signals (a core, a
  verdict, a coverage figure). NEVER PIN ONE. Write the invariant the pin stood
  for, so it still catches the failure it was written for:
    * a count: positive, and not below a floor recorded for THIS window, if
      one was (the window only grows, so falling below it means the read is
      not the window it claims to be);
    * an end date: on or after the window's start, not before a floor
      recorded for this window, and not in the future;
    * a ratio: inside the range the physics allows, not to one decimal;
    * a figure shown to a reader: DERIVED from the shipped table in the test,
      never typed in.

  PATCH-BOUNDARY. Moves only when the window does: `window`, `window_start`,
  the window's name in a label, and anything a human wrote down about the
  window as a whole. NEVER PIN ONE EITHER, since Jacob's decision of
  2026-11-08. Until this change they were pinned literally, on purpose (#123
  kept them), so that moving a pin declared the new window established, and
  so every boundary stopped the daily data until someone did. Write the
  invariant that holds at EVERY boundary instead:
    * a window name is well formed (`obNN`, `window_problems`) and within one
      patch of `_patch.json`'s `data_patch`. One behind, because the chooser
      keeps the last closed window while the new one covers fewer gods (it
      would have kept ob46 on 2026-11-04, 86 gods against 94, and the old
      window on 10-07, 89 tracked gods of 90) while the wiki stats usually
      land on patch day. One ahead, because the wiki stats can land LATER than
      the community window: `data_patch` moves only when a stats refresh
      passes the stats gate, the gate exists so that a rejected refresh
      "never costs the day's community numbers", and before the stats refresh
      ran unattended (2026-11-02) `data_patch` sat at Open Beta 40 from 08-06
      to 10-30 while six windows went by. Two away either way means the
      community source or the wiki side has been stuck for a whole patch, and
      that fails;
    * start <= end <= tomorrow;
    * a label names the table's OWN window, derived from the table, never the
      current patch's;
    * a floor, or any other value recorded for one window, applies only while
      the shipped table IS that window (`test_refresh.WINDOW_FLOORS`). A new
      window starts small, so a floor carried across a boundary would block
      it. Recording one for a new window is optional and never required;
    * a hand-written doc row about the window (STATE.md section 7's Community
      sample row) is checked against the table, by #123's consistency rules,
      while its newest reading describes the shipped window. In a different
      window it is history: the test skips, and `doc_audit` reports it as a
      WARNING (a finding if the row describes a window NEWER than the data).

  GENUINE-ERROR-ONLY. True of every healthy window and false only when the data
  is wrong: a complete record for the gods that had one, provenance present,
  builds and matches being different quantities. The 2026-11-04 one-day window
  (6158066f: 166 items, 48 of 96 complete records) is the case this class is
  for, and it must stay red on it. Replaying the suite on that snapshot is how
  a change to a test in this class is checked.

THE DECLARATION CHECKLIST IS RETIRED (2026-11-09). It listed what a human moved
by hand to declare a window: the two pins and two floors in
`test_refresh.test_the_shipped_file_now_carries_all_three`, the window name in
`test_side_by_side.test_the_shipped_label_names_the_community_window_and_its_real_size`,
and STATE.md section 7's Community sample row. The first two are invariants
now and the row is a warning, so there is nothing to move, and nothing replaces
the list. Its argument — "a gate that rewrites its own expected values has
stopped being a gate" — still stands, and is why none of these is restamped by
the refresh: they are written so that there is nothing to restamp.

EXPERT-REVIEW BASELINES are a model output on the live data, so they are DAILY
by this rule (the `item-overweighted` baseline flipped three times inside Open
Beta 40 on community refreshes alone: 08-29, 09-01 and 09-07). Each one names
the window it was checked on (`verdict_window`, in `data/_expert_reviews.yaml`)
and is asserted only on that data; see `test_expert_review`.

WHAT THIS DOES NOT COVER. Arithmetic on fixed inputs reads `frozen.py`. A
consecutive-day check needs the previous shipped file, which the CI checkout
does not have; it is `refresh._refuse_window_regression`, at the write. And
nothing here, or there, judges whether a new window is DEEP enough: on the
coverage rule alone the chooser would have taken a window one day old at four
of the seven boundaries on record (the measurement is in
`choose_community_window`'s docstring). That is reported, not decided.
"""
import json
from datetime import date, timedelta

from smite import refresh, snapshots

#: How far the shipped window may sit from `_patch.json`'s `data_patch`, in
#: patches, either way. Why one each way is in the docstring.
PATCH_SLACK = 1


def shipped_community_table() -> dict:
    """`data/_community_items.json` as the daily refresh last wrote it."""
    return json.loads((refresh.DATA_ROOT / refresh.COMMUNITY_ITEMS_FILE)
                      .read_text(encoding="utf-8"))


def shipped_patch() -> dict:
    """`data/_patch.json` as the daily refresh last wrote it."""
    return json.loads((refresh.DATA_ROOT / "_patch.json").read_text(encoding="utf-8"))


def latest_plausible_day() -> str:
    """The latest `window_end` a healthy table can carry: tomorrow, so a run
    that crosses midnight UTC against a clock in another zone is never red."""
    return (date.today() + timedelta(days=1)).isoformat()


def window_problems(table: dict, patch: dict, latest: str = None, floors: dict = None) -> list:
    """What is wrong with a community table's window, one sentence each; `[]`
    when nothing is. Every rule holds at every boundary, so none of them can
    stop a new window landing, and each names the failure it is for.

    `floors` maps a window id to values recorded for it (`window_start`,
    `matches`, `window_end`). An entry applies only while `table` IS that
    window."""
    latest = latest or latest_plausible_day()
    out = []
    window = table.get("window")
    n = refresh.community_window_number(window)
    if n is None:
        out.append(f"window {window!r} is not a patch window (`obNN`): the run could "
                   "not name what it read, so the coverage rule cannot have chosen it")
    data_n = snapshots.patch_number(patch.get("data_patch") or patch.get("patch"))
    if data_n is None:
        out.append(f"_patch.json names no patch: {patch!r}")
    elif n is not None and abs(n - data_n) > PATCH_SLACK:
        out.append(f"window {window} is {n - data_n:+d} patches from data_patch Open Beta "
                   f"{data_n}; one either way is a boundary, two is a source stuck for a "
                   "whole patch")
    matches = table.get("matches_analyzed")
    if not (isinstance(matches, int) and not isinstance(matches, bool) and matches > 0):
        out.append(f"matches_analyzed {matches!r} is not a positive count")
    start, end = table.get("window_start"), table.get("window_end")
    try:
        date.fromisoformat(start), date.fromisoformat(end)
    except (TypeError, ValueError):
        out.append(f"window dates {start!r}..{end!r} are not ISO dates")
        return out
    if start > end:
        out.append(f"the window ends {end}, before it starts ({start})")
    if end > latest:
        out.append(f"the window ends {end}, after {latest}")
    floor = (floors or {}).get(window)
    if floor:
        if start != floor["window_start"]:
            out.append(f"{window} starts {start}; it was recorded starting "
                       f"{floor['window_start']}")
        if isinstance(matches, int) and matches < floor["matches"]:
            out.append(f"{matches:,} matches is below the {floor['matches']:,} {window} "
                       "already had when it was recorded; a window only grows")
        if end < floor["window_end"]:
            out.append(f"{window} ends {end}, before the {floor['window_end']} it was "
                       "recorded ending")
    return out
