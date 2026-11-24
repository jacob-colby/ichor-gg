"""Why the community buys an item Ichor does not: its record, in four labels.

Done criterion 2 (rewritten 2026-11-23, Jacob): every item that differs on the
side-by-side shows numbers from both sides. Ichor's side is the simulator
delta `side_by_side` already prints; this is the community's side — the pick
rate, the ESTIMATED sample and the win rate against the god's own, reduced to
one of four labels, checked in this order:

  too few matches                fewer than `tierlist.MIN_MATCHES` (30)
                                 estimated matches
  below this god's average       win rate under the god's own win rate
  above average, not confidently win rate at or above it, Wilson lower bound
                                 under it
  confidently above average      Wilson lower bound at or above it

THE MATCH COUNT IS AN ESTIMATE: SmiteBrain prints no per-item denominator, so
it is pick rate x god matches, `hybrid.item_record`'s derivation. The Wilson
bound is `tierlist.wilson_lower_bound`, the same one `hybrid` and the tier list
use. Neither is re-implemented here.

IT EXPLAINS AND NEVER RANKS (Jacob, 2026-11-06: pick and win measure the
model, they do not feed it). Nothing in `scoring`, `assemble`, `recommend`,
`build_index` or `efficiency` imports this module, and
`test_item_evidence.test_nothing_in_the_model_imports_this` pins it. The
`hybrid` build's own use of the same record is a separate, older decision and
is not widened by this.

MEASURED 2026-11-24 (Conquest, window OB48 after the 11-23 refresh, 5,251 matches, control
fingerprint b8c91ef02f5d), every community-only item on the 95 Conquest
side-by-sides: 363 items — 144 too few matches, 87 below, 124 above not
confidently, 8 confident (Amaterasu / Shogun's Ofuda, Bastet / Magi's Cloak,
Hachiman / Deathbringer, Hou Yi / Deathbringer, Jing Wei / The Executioner,
Ravana / Heartseeker, Sol / Book of Thoth, Susano / Avatar's Parashu, all at
10-32% pick and 30-60 estimated matches). Of the 42 at 40%+ pick: 0 too few,
11 below, 31 above not confidently, 0 confident. 68 of the 363 are alternate
sightings, read off `side_by_side.community_rates`. Eight "below" labels are
under half a point short because SmiteBrain prints item rates to two decimals
and the god's rate is exact; the page shows the god's decimal when the two
would round equal. The day before (fingerprint 2ec7382399c8) read 364 / 179 /
71 / 109 / 5: one refresh moves these, so they are a reading, not a constant.
OB47 (2026-11-14) had 75 item
and god pairs at 40%+ pick, all with 30+ estimated matches, 41 at or above the
god's rate and one confident (Bacchus / Devourer's Gauntlet).
"""
from smite import hybrid, tierlist

TOO_FEW = "too few matches"
BELOW = "below this god's average"
ABOVE_UNSURE = "above average, not confidently"
CONFIDENT = "confidently above average"
NO_RECORD = "no community record"

#: Display order, worst evidence first, as the criterion lists them.
LABELS = (TOO_FEW, BELOW, ABOVE_UNSURE, CONFIDENT)


def community_entry(build_note):
    """The god note's community build entry, or None."""
    return next((b for b in (build_note or {}).get("builds") or []
                 if b.get("source") == "community"), None)


def label(rates, entry):
    """`{label, pick_rate, win_rate, matches, confidence, god_win_rate}` for one
    item's community `rates` (`side_by_side.community_rates`: slot or best
    alternate sighting) on the god whose community `entry` this is."""
    entry = entry or {}
    god_win = entry.get("god_win_rate")
    played_total = entry.get("god_matches_played")
    win, pick = (rates or {}).get("win_rate"), (rates or {}).get("pick_rate")
    out = {"pick_rate": pick, "win_rate": win, "matches": None, "confidence": None,
           "god_win_rate": god_win, "matches_estimated": True}
    if (not isinstance(win, (int, float)) or not isinstance(pick, (int, float)) or pick <= 0
            or not isinstance(played_total, (int, float)) or played_total <= 0
            or not isinstance(god_win, (int, float))):
        return {**out, "label": NO_RECORD}
    rec = hybrid.item_record(win, pick, played_total)
    out.update(matches=rec["matches"], confidence=rec["confidence"])
    if rec["matches"] < tierlist.MIN_MATCHES or rec["confidence"] is None:
        return {**out, "label": TOO_FEW}
    if win < god_win:
        return {**out, "label": BELOW}
    if rec["confidence"] < god_win:
        return {**out, "label": ABOVE_UNSURE}
    return {**out, "label": CONFIDENT}


def label_counts(labelled):
    """`{label: n}` over labelled items, every label present."""
    counts = {k: 0 for k in (*LABELS, NO_RECORD)}
    for x in labelled:
        counts[x["label"]] += 1
    return counts
