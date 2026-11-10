"""The per-aspect community record: the feed parser, its all-or-nothing guard,
the store, and the build-note entry. Evidence for every rule is in
`smite/aspect_matches.py`'s docstring."""
import copy
import json
import re
from pathlib import Path
from urllib.parse import unquote

import pytest

from smite import aspect_matches as am
from smite import notes, refresh

FIXTURES = Path(__file__).parent / "fixtures"
MANGETSU = {"name": "Aspect of Mangetsu", "value": "aspect-of-mangetsu"}


def _page(name):
    return (FIXTURES / name).read_text(encoding="utf-8")


def _doc(name):
    return json.loads(_page(name))


def _raw(name, i=0):
    return copy.deepcopy(_doc(name)["result"]["data"]["builds"][i])


def _text(builds, aspects=(MANGETSU,)):
    return json.dumps({"result": {"data": {"builds": builds, "availableAspects": list(aspects)}}})


# -- the parser ----------------------------------------------------------------

def test_a_recorded_page_parses_into_the_stored_shape():
    records, available, oldest = am.parse_page(
        _page("aspect_feed_tsukuyomi_mangetsu.json"), "Tsukuyomi", MANGETSU)
    assert len(records) == 10
    assert available == [MANGETSU]
    assert oldest == _doc("aspect_feed_tsukuyomi_mangetsu.json")["result"]["data"]["builds"][-1][
        "hz_match_start_timestamp"]
    for r in records:
        assert tuple(r) == am.RECORD_KEYS
        assert re.fullmatch(r"[0-9a-f]{16}", r["m"])
        assert r["aspect"] == "aspect-of-mangetsu"
        assert r["placement"] in (1, 2)
        assert len(r["items"]) == 6
        assert all(s is None or re.fullmatch(r"[a-z0-9-]+", s) for s in r["items"])
    first = records[0]
    assert first["items"][:2] == ["ancient-signet", "chronos-pendant"]
    # "Spear Of The Magus" on the source: keyed on the link, not the spelling.
    assert first["items"][4] == "spear-of-the-magus"
    assert first["starter"] == "pendulum-of-the-ages"
    assert first["enemies"] == ["xbalanque", "nemesis", "ra", "athena", "ne-zha"]


def test_a_no_aspect_record_has_no_aspect_key_and_parses_as_null():
    raw = _raw("aspect_feed_tsukuyomi_none.json")
    assert "aspect" not in raw          # tRPC omits a null key
    assert am.parse_record(raw, "Tsukuyomi", None)["aspect"] is None


def test_no_player_name_and_no_raw_guid_reach_a_record():
    raw = _raw("aspect_feed_tsukuyomi_mangetsu.json")
    raw["player_display_name"] = "Somebody Real"
    line = am._record_line(am.parse_record(raw, "Tsukuyomi", MANGETSU))
    assert "Somebody" not in line
    assert raw["hz_match_guid"] not in line
    assert raw["hz_match_guid"][:8] not in line
    assert json.loads(line)["m"] == am.match_key(raw["hz_match_guid"])


def test_the_same_match_hashes_the_same_in_every_gods_file():
    guid = "491a8e18-8141-4125-a7c1-8dffc96e66fe"
    assert am.match_key(guid) == am.match_key(guid.upper()) == am.match_key(f" {guid} ")


def test_an_unlinked_item_is_slugged_from_its_name():
    raw = _raw("aspect_feed_tsukuyomi_mangetsu.json")
    raw["items"]["3"] = {"item_name": "Brawler's Ruin", "detail_href": None}
    assert am.parse_record(raw, "Tsukuyomi", MANGETSU)["items"][2] == "brawlers-ruin"


def test_a_link_that_is_not_an_item_link_is_refused():
    raw = _raw("aspect_feed_tsukuyomi_mangetsu.json")
    raw["items"]["3"] = {"item_name": "Divine Ruin", "detail_href": "/gods/zeus"}
    with pytest.raises(am.FeedCollapse, match="not an item"):
        am.parse_record(raw, "Tsukuyomi", MANGETSU)


def test_an_empty_slot_is_kept_in_place_as_null():
    raw = _raw("aspect_feed_tsukuyomi_mangetsu.json")
    raw["items"]["6"] = {"item_name": "Empty", "detail_href": None}
    assert am.parse_record(raw, "Tsukuyomi", MANGETSU)["items"][5] is None


def test_an_inventory_wider_than_six_is_kept_whole():
    """Vulcan's Aspect of Fortification returns 7 or 8 slots."""
    raw = _raw("aspect_feed_tsukuyomi_mangetsu.json")
    raw["items"]["7"] = {"item_name": "Book of Thoth", "detail_href": "/items/book-of-thoth"}
    raw["items"]["8"] = {"item_name": "Empty", "detail_href": None}
    assert am.parse_record(raw, "Tsukuyomi", MANGETSU)["items"][6:] == ["book-of-thoth", None]


@pytest.mark.parametrize("keys", [["1", "2", "3", "4", "5"], ["1", "2", "3", "4", "5", "7"],
                                  ["0", "1", "2", "3", "4", "5"]])
def test_an_inventory_that_is_not_slots_one_to_k_is_refused(keys):
    raw = _raw("aspect_feed_tsukuyomi_mangetsu.json")
    item = raw["items"]["1"]
    raw["items"] = {k: item for k in keys}
    with pytest.raises(am.FeedCollapse, match="slots"):
        am.parse_record(raw, "Tsukuyomi", MANGETSU)


def test_an_ignored_aspect_filter_is_refused():
    raw = _raw("aspect_feed_tsukuyomi_none.json")      # a no-aspect record
    with pytest.raises(am.FeedCollapse, match="aspect filter was ignored"):
        am.parse_record(raw, "Tsukuyomi", MANGETSU)


def test_an_ignored_none_filter_is_refused():
    raw = _raw("aspect_feed_tsukuyomi_mangetsu.json")
    with pytest.raises(am.FeedCollapse, match="aspect=none was ignored"):
        am.parse_record(raw, "Tsukuyomi", None)


def test_an_ignored_god_filter_is_refused():
    raw = _raw("aspect_feed_tsukuyomi_none.json")
    with pytest.raises(am.FeedCollapse, match="godSlug filter"):
        am.parse_record(raw, "Izanami", None)


@pytest.mark.parametrize("field, value", [("hz_match_guid", None), ("hz_match_guid", "abc"),
                                          ("hz_match_start_timestamp", "yesterday"),
                                          ("player_placement", 3), ("played_role", "Jungler"),
                                          ("items", None)])
def test_a_record_missing_a_hard_field_is_refused(field, value):
    raw = _raw("aspect_feed_tsukuyomi_mangetsu.json")
    raw[field] = value
    with pytest.raises(am.FeedCollapse):
        am.parse_record(raw, "Tsukuyomi", MANGETSU)


@pytest.mark.parametrize("text", ["<html>", "{}", '{"result": {"data": {}}}',
                                  '{"error": {"message": "rate limited"}}'])
def test_a_response_that_is_not_a_page_is_refused(text):
    with pytest.raises(am.FeedCollapse):
        am.parse_page(text, "Tsukuyomi", MANGETSU)


def test_a_cursor_that_did_not_move_is_refused():
    builds = _doc("aspect_feed_tsukuyomi_mangetsu.json")["result"]["data"]["builds"]
    with pytest.raises(am.FeedCollapse, match="cursor did not move"):
        am.parse_page(_text(builds), "Tsukuyomi", MANGETSU,
                      cursor=builds[-1]["hz_match_start_timestamp"])


def test_timestamps_are_normalised_to_one_spelling():
    assert am._norm_ts("2026-11-07T05:44:58.7Z") == "2026-11-07T05:44:58.700Z"
    assert am._norm_ts("2026-11-07T05:44:58Z") == "2026-11-07T05:44:58.000Z"


def test_the_god_slug_is_the_rule_the_community_refresh_uses():
    for god in am.conquest_gods():
        assert refresh.community_url(god) == f"{refresh.SMITEBRAIN_BASE}{am.god_slug(god)}/"


# -- the walk, the store, and the guard ----------------------------------------

def _rec(t, aspect="aspect-of-mangetsu", role="Mid", placement=1, items=None, m=None,
         starter="archmages-gem", relic="purification-beads"):
    return {"m": m or am.match_key(f"00000000-0000-0000-0000-{abs(hash(t)) % 10**12:012d}"),
            "t": t, "aspect": aspect, "role": role, "rank": 5000, "placement": placement,
            "items": items or ["rod-of-tahuti", "book-of-thoth", None, None, None, None],
            "starter": starter, "relic": relic, "enemies": []}


META = {"division": "obsidian",
        "windows": {"ob46": {"start": "2026-10-20T11:48:48.610Z", "end": "2026-11-03T11:28:02.357Z"},
                    "ob47": {"start": "2026-11-03T11:30:13.083Z", "end": "2026-11-08T16:24:43.807Z"}},
        "aspects": {}}


def test_records_land_in_the_window_whose_start_precedes_them(tmp_path):
    recs = [_rec("2026-11-03T11:29:00.000Z"), _rec("2026-11-03T11:31:00.000Z")]
    added = am.store_records(tmp_path, "tsukuyomi", recs, META)
    assert added == {"ob46": 1, "ob47": 1}
    with pytest.raises(am.FeedCollapse, match="predates every known window"):
        am.store_records(tmp_path, "tsukuyomi", [_rec("2026-10-01T00:00:00.000Z")], META)


def test_the_store_is_append_only_and_deduplicated(tmp_path):
    a, b = _rec("2026-11-04T00:00:00.000Z"), _rec("2026-11-05T00:00:00.000Z")
    am.store_records(tmp_path, "tsukuyomi", [b], META)
    changed = dict(b, role="Jungle")             # the same match seen again
    assert am.store_records(tmp_path, "tsukuyomi", [a, changed], META) == {"ob47": 1}
    stored = am.load_god(tmp_path, "tsukuyomi")["ob47"]
    assert [r["t"] for r in stored] == [a["t"], b["t"]]           # oldest first
    assert stored[1]["role"] == "Mid"                              # stored copy wins


class FakeFeed:
    """Serves getBuilds pages from an in-memory feed, newest first, honouring
    the cursor the way the real endpoint does (exclusive)."""

    def __init__(self, gods, broken=None, windows=None):
        self.gods = gods                    # {slug: {"name", "aspects", "feeds": {aspect|none: [raw]}}}
        self.broken = broken or set()
        self.windows = windows or META["windows"]   # what the split index answers, per window
        self.urls = []

    def __call__(self, url):
        self.urls.append(url)
        if url.startswith(am.INDEX_URL):
            window = re.search(r"time=(ob\d+)", url).group(1)
            w = self.windows[window]
            return json.dumps(_index_payload(window, w["start"], w["end"]))
        if not url.startswith(am.FEED_URL):
            # The range selector: every window the index answers for, newest first.
            options = "".join(f'<option value="{w}">{w}</option>'
                              for w in sorted(self.windows, key=lambda w: self.windows[w]["start"],
                                              reverse=True))
            return f'<select><option value="1w">1w</option>{options}</select>'
        inp = json.loads(unquote(url.split("input=", 1)[1]))
        god = self.gods[inp["godSlug"]]
        if (inp["godSlug"], inp.get("aspect")) in self.broken:
            return '{"error": "boom"}'
        feed = god["feeds"].get(inp.get("aspect"), [])
        cursor = inp.get("lastEvaluatedBuildDate")
        rows = [b for b in feed if not cursor or b["hz_match_start_timestamp"] < cursor]
        return _text(rows[:am.PAGE_SIZE], god["aspects"])


def _index_payload(window, start, end):
    flat = [{"snapshot": 1, "selectedTime": 3}, [2],
            {"god": 4, "win_rate": 5, "matches_played": 6, "matches_won": 7, "aspect": 8,
             "start_time": 9, "end_time": 10}, window, "Tsukuyomi", 0.5, 10, 5, "None",
            ["Date", start], ["Date", end]]
    return {"type": "data", "nodes": [{"type": "data", "data": flat}]}


def _raw_at(base, t, aspect_name=None, guid_n=0):
    raw = copy.deepcopy(base)
    raw["hz_match_start_timestamp"] = t
    raw["hz_match_guid"] = f"00000000-0000-0000-0000-{guid_n:012d}"
    if aspect_name:
        raw["aspect"] = {"item_name": aspect_name, "detail_href": None}
    else:
        raw.pop("aspect", None)
    return raw


def _feed(n, start_hour, aspect_name, offset):
    base = _raw("aspect_feed_tsukuyomi_mangetsu.json")
    return [_raw_at(base, f"2026-11-0{5 + (h // 24)}T{h % 24:02d}:00:00.000Z", aspect_name, offset + h)
            for h in range(start_hour + n - 1, start_hour - 1, -1)]


def _fake(mangetsu_n=25, broken=None):
    return FakeFeed({"tsukuyomi": {"aspects": [MANGETSU],
                                   "feeds": {"aspect-of-mangetsu": _feed(mangetsu_n, 0, "Aspect of Mangetsu", 0),
                                             "none": _feed(12, 0, None, 1000)}}},
                    broken=broken)


def test_an_empty_store_walks_back_to_the_newest_window_and_writes_everything(tmp_path):
    fake = _fake()
    am.refresh(fake, ["Tsukuyomi"], tmp_path, window_ids=["ob47", "ob46"], log=lambda *_: None)
    stored = am.load_god(tmp_path, "tsukuyomi")["ob47"]
    assert sum(r["aspect"] == "aspect-of-mangetsu" for r in stored) == 25
    assert sum(r["aspect"] is None for r in stored) == am.NONE_PAGES * am.PAGE_SIZE
    meta = am.load_meta(tmp_path)
    assert meta["aspects"]["tsukuyomi"] == [MANGETSU]
    assert set(meta["windows"]) == {"ob46", "ob47"}
    assert set(am.load_aggregate(tmp_path)) == {"ob46", "ob47"}


def test_a_second_run_stops_at_the_stored_data(tmp_path):
    am.refresh(_fake(), ["Tsukuyomi"], tmp_path, window_ids=["ob47"], log=lambda *_: None)
    fake = _fake()
    am.refresh(fake, ["Tsukuyomi"], tmp_path, window_ids=["ob47"], log=lambda *_: None)
    walked = [u for u in fake.urls if "aspect-of-mangetsu" in u]
    assert len(walked) == 1                 # the newest page already reaches the store


def test_a_broken_page_anywhere_writes_nothing(tmp_path):
    am.refresh(_fake(10), ["Tsukuyomi"], tmp_path, window_ids=["ob47"], log=lambda *_: None)
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    with pytest.raises(am.FeedCollapse):
        am.refresh(_fake(25, broken={("tsukuyomi", "aspect-of-mangetsu")}), ["Tsukuyomi"],
                   tmp_path, window_ids=["ob47"], log=lambda *_: None)
    after = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    assert after == before


def test_a_source_serving_no_matches_at_all_is_refused(tmp_path):
    fake = FakeFeed({"tsukuyomi": {"aspects": [MANGETSU], "feeds": {}}})
    with pytest.raises(am.FeedCollapse, match="returned no matches at all"):
        am.refresh(fake, ["Tsukuyomi"], tmp_path, window_ids=["ob47"], log=lambda *_: None)
    assert not any(tmp_path.rglob("*.jsonl"))


def test_the_cli_exits_non_zero_on_a_refusal(monkeypatch, capsys):
    def boom(*a, **k):
        raise am.FeedCollapse("shape changed")
    monkeypatch.setattr(am, "refresh", boom)
    monkeypatch.setattr(am, "PoliteFetcher", lambda: type("F", (), {"requests": 0})())
    assert am.main(["refresh"]) == 1
    assert "::error::aspect feed refused" in capsys.readouterr().out


# -- a patch boundary the range selector has not caught up with ----------------
#
# The feed is not filtered by window: it is the newest matches, whatever patch
# they were played on. The window a record is FILED in comes from the range
# selector's windows (`window_of`), and the store is append-only. So a match
# played after a new patch opens, fetched on a run whose selector does not list
# that patch yet, must not be filed in the old window: once the new window is
# listed, `window_of` names it, and the committed store's own test
# (`test_aspect_store.test_every_committed_record_sits_in_its_own_window`)
# goes red with nothing to move the record. Modelled on OB47's real boundary
# (ob46 ends 11-03 11:28:02Z, ob47 starts 11:30:13Z; the 11-03 17:30Z refresh
# still read ob46, ending 11-02).

OB47 = {"start": "2026-11-03T11:30:13.083Z", "end": "2026-11-17T11:28:00.000Z"}
OB48_START = "2026-11-17T11:31:00.000Z"
#: Day N, 2026-11-17 17:30Z: the selector still lists ob47 (and ob46) only.
DAY_N = {"ob46": META["windows"]["ob46"], "ob47": OB47}
#: Day N+1: ob48 is listed; ob47's end is final.
DAY_N1 = {**DAY_N, "ob48": {"start": OB48_START, "end": "2026-11-18T17:00:00.000Z"}}


def _hours(day, hours):
    return [f"2026-11-{day:02d}T{h:02d}:00:00.000Z" for h in hours]


#: Mangetsu: 15 ob47 matches (the last at 11-17 10:00, before the boundary), 8
#: ob48 matches played on day N, and 7 more played after day N's run.
OB47_TIMES = _hours(3, [12, 14, 16, 18, 20]) + _hours(9, [12, 14, 16, 18, 20]) \
    + _hours(17, [6, 7, 8, 9, 10])
OB48_DAY_N = _hours(17, [12, 13, 14, 15, 16]) + ["2026-11-17T11:31:00.000Z",
                                                 "2026-11-17T11:45:00.000Z",
                                                 "2026-11-17T17:00:00.000Z"]
OB48_AFTER = _hours(18, [1, 3, 5, 7, 9, 11, 13])
NONE_OB47 = _hours(17, [5, 6, 7, 8])
NONE_OB48 = _hours(17, [12, 13, 14, 15, 16, 17]) + _hours(18, [2, 4, 6])


def _raws(times, aspect_name, offset):
    base = _raw("aspect_feed_tsukuyomi_mangetsu.json")
    ordered = sorted(times, reverse=True)                     # the feed is newest first
    return [_raw_at(base, t, aspect_name, offset + sorted(times).index(t)) for t in ordered]


def _boundary_feed(day_n1=False):
    mangetsu = OB47_TIMES + OB48_DAY_N + (OB48_AFTER if day_n1 else [])
    none = NONE_OB47 + [t for t in NONE_OB48 if day_n1 or t <= "2026-11-17T17:30:00.000Z"]
    return FakeFeed({"tsukuyomi": {"aspects": [MANGETSU],
                                   "feeds": {"aspect-of-mangetsu": _raws(mangetsu, "Aspect of Mangetsu", 0),
                                             "none": _raws(none, None, 1000)}}},
                    windows=DAY_N1 if day_n1 else DAY_N)


def _committed_store_problems(root):
    """`test_aspect_store.test_every_committed_record_sits_in_its_own_window`,
    word for word, run on a store under `root` instead of the committed one."""
    meta, problems = am.load_meta(root), []
    for path in sorted(root.glob("*/*.jsonl")):
        times = []
        for line in path.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            if am.window_of(r["t"], meta) != path.parent.name:
                problems.append((path.parent.name, path.stem, r["t"], am.window_of(r["t"], meta)))
            times.append((r["t"], r["m"]))
        if not (times == sorted(times) and len({m for _, m in times}) == len(times)):
            problems.append((path.parent.name, path.stem, "order or duplicate"))
    return problems


def _times(root, window, aspect="aspect-of-mangetsu"):
    return sorted(r["t"] for r in am.load_god(root, "tsukuyomi").get(window, [])
                  if r["aspect"] == aspect)


def test_a_boundary_the_selector_has_not_listed_strands_nothing(tmp_path):
    """The replay: day N, the selector lacks ob48 while ob48 matches are in the
    feed; day N+1, it lists ob48. The store is green after both runs, and every
    ob48 match held back on day N is in ob48 after day N+1."""
    quiet = lambda *_: None
    day_n = am.refresh(_boundary_feed(), ["Tsukuyomi"], tmp_path, log=quiet)
    assert set(am.load_meta(tmp_path)["windows"]) == {"ob46", "ob47"}
    assert _committed_store_problems(tmp_path) == []
    assert _times(tmp_path, "ob47") == sorted(OB47_TIMES)          # nothing past ob47's end
    assert "ob48" not in am.load_god(tmp_path, "tsukuyomi")
    assert day_n["held"] == len(OB48_DAY_N) + 6                    # 6: no-aspect, newest page

    day_n1 = am.refresh(_boundary_feed(day_n1=True), ["Tsukuyomi"], tmp_path, log=quiet)
    assert set(am.load_meta(tmp_path)["windows"]) == {"ob46", "ob47", "ob48"}
    assert _committed_store_problems(tmp_path) == []
    assert _times(tmp_path, "ob47") == sorted(OB47_TIMES)
    assert _times(tmp_path, "ob48") == sorted(OB48_DAY_N + OB48_AFTER)   # day N's held ones too
    assert day_n1["held"] == 0


def test_on_the_old_rule_day_n_files_ob48_matches_in_ob47(tmp_path):
    """What the hold-back prevents, pinned so it cannot quietly come back: the
    day-N feed holds matches later than every listed window's end, and
    `window_of` alone would file them in ob47."""
    meta = {"windows": DAY_N}
    assert {am.window_of(t, meta) for t in OB48_DAY_N} == {"ob47"}
    assert all(t > OB47["end"] for t in OB48_DAY_N)
    assert {am.window_of(t, {"windows": DAY_N1}) for t in OB48_DAY_N} == {"ob48"}


def test_a_match_newer_than_the_newest_windows_end_waits_for_the_next_run(tmp_path):
    """Inside one patch too: a match the feed has and the split index has not
    counted yet is held, and the next run's walk, which starts above the
    newest stored match, fetches it again."""
    quiet = lambda *_: None
    early = dict(META["windows"], ob47={**META["windows"]["ob47"], "end": "2026-11-05T09:00:00.000Z"})
    feeds = {"aspect-of-mangetsu": _feed(25, 0, "Aspect of Mangetsu", 0), "none": _feed(12, 0, None, 1000)}
    gods = {"tsukuyomi": {"aspects": [MANGETSU], "feeds": feeds}}
    first = am.refresh(FakeFeed(gods, windows=early), ["Tsukuyomi"], tmp_path, window_ids=["ob47"], log=quiet)
    assert max(_times(tmp_path, "ob47")) == "2026-11-05T09:00:00.000Z"
    assert first["held"] == 15 + 2                 # 10:00 .. 24:00 Mangetsu; the sample's 10:00, 11:00
    second = am.refresh(FakeFeed(gods), ["Tsukuyomi"], tmp_path, window_ids=["ob47"], log=quiet)
    assert len(_times(tmp_path, "ob47")) == 25 and second["held"] == 0


def test_a_newest_window_with_no_end_vouches_for_nothing_after_its_start(tmp_path):
    no_end = dict(META["windows"], ob47={**META["windows"]["ob47"], "end": None})
    assert am.known_extent({"windows": no_end}) == no_end["ob47"]["start"]
    assert am.known_extent({"windows": DAY_N}) == OB47["end"]
    assert am.known_extent({"windows": {}}) is None


def test_a_run_whose_windows_would_refile_a_stored_match_writes_nothing(tmp_path):
    """The write-time guard behind the hold-back: if SmiteBrain ever draws a
    new window's start under a match already stored (its old window's end ran
    past the boundary), the run is refused and nothing is written — the
    store keeps agreeing with its committed meta, so CI stays green and the
    refusal is the workflow's loud `rejected` path, not a red data PR."""
    quiet = lambda *_: None
    overlapping = {**DAY_N, "ob47": {**OB47, "end": "2026-11-17T17:00:00.000Z"}}
    am.refresh(FakeFeed(_boundary_feed().gods, windows=overlapping), ["Tsukuyomi"], tmp_path, log=quiet)
    assert "2026-11-17T12:00:00.000Z" in _times(tmp_path, "ob47")     # filed under the overlap
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    with pytest.raises(am.FeedCollapse, match="would refile"):
        am.refresh(_boundary_feed(day_n1=True), ["Tsukuyomi"], tmp_path, log=quiet)
    assert {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()} == before
    assert am.misfiled(tmp_path, am.load_meta(tmp_path)) == []


# -- the build-note entry ------------------------------------------------------

WINDOWS4 = ["ob47", "ob46", "ob45", "ob44"]


@pytest.mark.parametrize("counts, expected", [
    # The two branches #129 shipped, unchanged: one window, never pooled.
    ({"ob47": 30, "ob46": 99}, (["ob47"], "newest")),
    ({"ob47": 29, "ob46": 30}, (["ob46"], "last closed")),
    ({"ob47": 19, "ob46": 200, "ob45": 382}, (["ob46"], "last closed")),   # Hou Yi: not pooled
    # Below both: the newest and the last closed together first...
    ({"ob47": 5, "ob46": 25}, (["ob47", "ob46"], "pooled back")),
    # ...then one closed window at a time, and no further than needed.
    ({"ob47": 6, "ob46": 21, "ob45": 30, "ob44": 17},
     (["ob47", "ob46", "ob45"], "pooled back")),                            # Tsukuyomi, 57
    ({"ob47": 3, "ob46": 8, "ob45": 13, "ob44": 14},
     (["ob47", "ob46", "ob45", "ob44"], "pooled back")),                    # Da Ji, 38
    ({"ob47": 10, "ob46": 24, "ob45": 104}, (["ob47", "ob46"], "pooled back")),  # Jormungandr
    # Every stored window together still short: a stated stub.
    ({"ob47": 4, "ob46": 13, "ob45": 6, "ob44": 5}, ([], "below minimum")),       # Geb, 28
    ({}, ([], "below minimum")),
])
def test_the_window_rule(counts, expected):
    assert am.choose_windows(counts, WINDOWS4) == expected


def test_a_store_of_one_window_never_pools():
    assert am.choose_windows({"ob47": 29}, ["ob47"]) == ([], "below minimum")
    assert am.choose_windows({"ob47": 30}, ["ob47"]) == (["ob47"], "newest")


def test_a_pool_is_labelled_by_the_patches_it_reads():
    assert am.patch_label(["ob47"]) == "OB47"
    assert am.patch_label(["ob45", "ob46", "ob47"]) == "OB45–OB47"
    assert am.window_patch("ob47") == 47 and am.window_patch("all") is None


def test_the_minimum_is_the_tier_lists_floor():
    from smite import tierlist
    assert am.MIN_MATCHES == tierlist.MIN_MATCHES == 30


def _entry(roles, base_role="Jungle", n_items=None):
    recs = []
    t = 0
    for role, k in roles.items():
        for _ in range(k):
            t += 1
            recs.append(_rec(f"2026-11-0{4 + t // 24}T{t % 24:02d}:00:00.000Z", role=role,
                             placement=1 if t % 2 else 2))
    return am.aspect_entry("Tsukuyomi", base_role, MANGETSU, {"ob47": recs}, META, {},
                           {"rod-of-tahuti": "Rod of Tahuti", "book-of-thoth": "Book of Thoth"})


def test_a_role_shift_is_named_when_the_base_role_is_a_clear_minority():
    entry = _entry({"Mid": 18, "Jungle": 6, "Solo": 6})
    assert entry["status"] == "shown" and entry["windows"] == ["ob47"]
    assert entry["patches"] == "OB47" and entry["window_rule"] == "newest"
    assert entry["base_role_share"] == 0.2
    assert entry["role_shift"]["role"] == "Mid"
    assert "do not play Jungle" in entry["role_shift"]["says"]


def test_no_role_shift_when_the_base_role_could_still_be_half():
    # 13 of 30 is 43%; the Wilson upper bound is above one half.
    assert _entry({"Mid": 17, "Jungle": 13})["role_shift"] is None


def test_no_role_shift_when_the_base_role_leads():
    assert _entry({"Jungle": 12, "Mid": 9, "Solo": 9})["role_shift"] is None


def test_a_two_role_god_is_not_shifted_into_one_of_his_own_roles():
    """Achilles is "Solo Jungle"; his Prowess players are 94% Jungle."""
    entry = _entry({"Jungle": 29, "Mid": 1}, base_role="Solo Jungle")
    assert entry["role_shift"] is None
    assert entry["base_role_share"] == 0.97


def test_a_two_role_god_shifted_out_of_both_is_named():
    entry = _entry({"Mid": 24, "Solo": 3, "Support": 3}, base_role="Solo Support")
    assert entry["base_role_share"] == 0.2
    assert entry["role_shift"]["role"] == "Mid"
    assert "do not play Solo/Support" in entry["role_shift"]["says"]


def test_entry_items_are_shares_of_matches_with_our_spellings():
    entry = _entry({"Mid": 30})
    assert entry["items"] == [{"name": "Book of Thoth", "share": 1.0},
                              {"name": "Rod of Tahuti", "share": 1.0}]
    assert entry["matches"] == 30 and entry["wins"] == 15 and entry["win_share"] == 0.5
    assert entry["unmapped_slugs"] == ["archmages-gem", "purification-beads"]


def test_a_thin_aspect_gets_a_stated_stub_and_claims_nothing():
    entry = _entry({"Mid": 5})
    assert entry == {"aspect": "Aspect of Mangetsu", "status": "below minimum",
                     "matches_by_window": {"ob47": 5}}


def test_item_slugs_map_to_our_note_spellings():
    names = am.item_name_lookup()
    assert names["spear-of-the-magus"] == "Spear of the Magus"
    assert names["chronos-pendant"] == "Chronos' Pendant"
    assert names["brawlers-beat-stick"] == "Brawler’s Beat Stick"     # curly in our note


# -- reaching back, and the items that changed since ----------------------------

META4 = {"division": "obsidian", "aspects": {},
         "windows": {"ob44": {"start": "2026-09-22T11:33:41.157Z", "end": "2026-10-06T10:55:52.910Z"},
                     "ob45": {"start": "2026-10-06T12:26:45.817Z", "end": "2026-10-20T10:57:38.887Z"},
                     "ob46": {"start": "2026-10-20T11:48:48.610Z", "end": "2026-11-03T11:28:02.357Z"},
                     "ob47": {"start": "2026-11-03T11:30:13.083Z", "end": "2026-11-08T20:22:04.330Z"}}}
NAMES = {"rod-of-tahuti": "Rod of Tahuti", "book-of-thoth": "Book of Thoth",
         "war-flag": "War Flag", "archmages-gem": "Archmage's Gem",
         "purification-beads": "Purification Beads"}


def _pooled(counts, changes, starter="archmages-gem", relic="purification-beads"):
    by_window = {w: [_rec(f"{w}-{i}", starter=starter, relic=relic) for i in range(k)]
                 for w, k in counts.items()}
    return am.aspect_entry("Tsukuyomi", "Mid", MANGETSU, by_window, META4, {}, NAMES, changes)


def _change(slug, after, through):
    return {"slug": slug, "name": slug, "after": after, "through": through}


def _flag(entry, name, field="items"):
    return next(i for i in entry[field] if i["name"] == name).get("changed")


def test_an_item_changed_between_pooled_windows_is_flagged_with_how_many_buys_are_older():
    entry = _pooled({"ob47": 10, "ob46": 25}, [_change("rod-of-tahuti", 46, 47)])
    assert entry["windows"] == ["ob46", "ob47"] and entry["patches"] == "OB46–OB47"
    assert entry["window_rule"] == "pooled back" and entry["matches"] == 35
    assert _flag(entry, "Rod of Tahuti") == {
        "patch": "OB47", "exact": True, "older_matches": 25, "matches": 35,
        "says": "changed in OB47; 25 of the 35 matches that bought it are older"}
    assert _flag(entry, "Book of Thoth") is None


def test_a_change_at_or_before_the_oldest_window_read_is_not_flagged():
    """OB46's records already bought the OB46 version: no pooled match is older."""
    entry = _pooled({"ob47": 10, "ob46": 25},
                    [_change("rod-of-tahuti", 45, 46), _change("book-of-thoth", 40, 46)])
    assert _flag(entry, "Rod of Tahuti") is None and _flag(entry, "Book of Thoth") is None


def test_a_change_the_snapshots_cannot_place_carries_its_whole_span():
    """No item data was scraped between OB40 and OB46: the change is at one of
    OB41-OB46, so the older share is an upper bound and the flag says so."""
    entry = _pooled({"ob47": 6, "ob46": 21, "ob45": 30}, [_change("rod-of-tahuti", 40, 46)])
    flag = _flag(entry, "Rod of Tahuti")
    assert flag["patch"] == "OB41–OB46" and flag["exact"] is False
    assert (flag["older_matches"], flag["matches"]) == (30, 57)
    assert "at a patch not recorded; up to 30 of the 57" in flag["says"]


def test_a_change_inside_one_patch_is_a_lower_bound():
    entry = _pooled({"ob47": 10, "ob46": 25}, [_change("rod-of-tahuti", 47, 47)])
    flag = _flag(entry, "Rod of Tahuti")
    assert flag["patch"] == "OB47" and flag["exact"] is False
    assert flag["says"] == ("its stats moved during OB47; at least 25 of the 35 matches "
                            "that bought it are older")


def test_a_last_closed_entry_is_flagged_too():
    """Cabrakan and Osiris on 2026-11-09: one window, no pooling, and Ancient
    Signet changed after it. The flag is not a pooling rule."""
    entry = _pooled({"ob47": 5, "ob46": 40}, [_change("rod-of-tahuti", 46, 47)])
    assert entry["windows"] == ["ob46"] and entry["window_rule"] == "last closed"
    assert _flag(entry, "Rod of Tahuti")["says"] == (
        "changed in OB47; 40 of the 40 matches that bought it are older")


def test_the_newest_window_is_not_flagged_by_a_change_it_already_saw():
    entry = _pooled({"ob47": 30, "ob46": 99}, [_change("rod-of-tahuti", 46, 47)])
    assert _flag(entry, "Rod of Tahuti") is None


def test_a_changed_item_never_stops_the_walk():
    """Flag, don't stop (agreed 2026-11-09): a stop rule made visibility hinge
    on the quality of the change data, and hid Chronos' 35 matches over the
    7 that bought War Flag."""
    entry = _pooled({"ob47": 6, "ob46": 21, "ob45": 30, "ob44": 17},
                    [_change("rod-of-tahuti", 45, 46), _change("book-of-thoth", 46, 47)])
    assert entry["status"] == "shown" and entry["windows"] == ["ob45", "ob46", "ob47"]
    assert _flag(entry, "Rod of Tahuti")["older_matches"] == 30
    assert _flag(entry, "Book of Thoth")["older_matches"] == 51


def test_the_latest_change_after_the_pool_is_the_one_named():
    entry = _pooled({"ob47": 6, "ob46": 21, "ob45": 30},
                    [_change("rod-of-tahuti", 45, 46), _change("rod-of-tahuti", 46, 47)])
    flag = _flag(entry, "Rod of Tahuti")
    assert flag["patch"] == "OB47" and flag["older_matches"] == 51


def test_a_starter_and_a_relic_are_flagged_on_their_own_field():
    entry = _pooled({"ob47": 10, "ob46": 25},
                    [_change("war-flag", 46, 47), _change("purification-beads", 46, 47)],
                    starter="war-flag")
    assert _flag(entry, "War Flag", "starters")["older_matches"] == 25
    assert _flag(entry, "Purification Beads", "relics")["matches"] == 35
    assert _flag(entry, "Rod of Tahuti") is None


def _snapshot(d, day, items):
    (d / f"{day}.json").write_text(json.dumps(
        {name: {"cost": cost, "tier": 3, "stats": stats} for name, (cost, stats) in items.items()}),
        encoding="utf-8")


def test_item_changes_attributes_each_snapshot_period_by_item_data(tmp_path):
    snaps = tmp_path / "snapshots"
    snaps.mkdir()
    base = {"Rod of Tahuti": (2800, {"Intelligence": "80"}),
            "Chronos' Pendant": (2700, {"Intelligence": "60"}),
            "Brawler’s Beat Stick": (2550, {"Strength": "30"})}
    pendant = {"Chronos' Pendant": (2650, {"Intelligence": "60"})}
    _snapshot(snaps, "2026-08-01", base)
    _snapshot(snaps, "2026-08-29", {**base, **pendant, "Ancient Signet": (2600, {})})
    _snapshot(snaps, "2026-11-02", {**base, **pendant, "Ancient Signet": (2600, {}),
                                    "Rod of Tahuti": (2800, {"Intelligence": "85"})})
    _snapshot(snaps, "2026-11-03", {**base, **pendant,
                                    "Ancient Signet": (2600, {"Mana Regen": "5"}),
                                    "Rod of Tahuti": (2800, {"Intelligence": "85"}),
                                    "Brawler’s Beat Stick": (2500, {"Strength": "30"})})
    history = tmp_path / "_patch_history.json"
    history.write_text(json.dumps(
        [{"patch": "Open Beta 40", "first_seen": "2026-08-01", "data_from": "2026-08-01"}]
        + [{"patch": f"Open Beta {n}", "first_seen": f"2026-{d}", "source": "manual"}
           for n, d in ((41, "08-11"), (42, "08-25"), (43, "09-08"), (44, "09-22"), (45, "10-06"))]
        + [{"patch": "Open Beta 46", "first_seen": "2026-10-20", "source": "manual",
            "data_from": "2026-11-02"},
           {"patch": "Open Beta 47", "first_seen": "2026-11-03", "data_from": "2026-11-03",
            "source": "wiki"}]), encoding="utf-8")
    rows = am.item_changes(snaps, history)
    # A correction inside OB40 is "during" it; OB40 -> OB46 is one span with
    # five patches inside it; an ADDED item (Ancient Signet on 08-29) is not a
    # change; names are slugged the way the store slugs them.
    assert rows == [
        {"slug": "chronos-pendant", "name": "Chronos' Pendant", "after": 40, "through": 40},
        {"slug": "rod-of-tahuti", "name": "Rod of Tahuti", "after": 40, "through": 46},
        {"slug": "ancient-signet", "name": "Ancient Signet", "after": 46, "through": 47},
        {"slug": "brawlers-beat-stick", "name": "Brawler’s Beat Stick", "after": 46, "through": 47},
    ]


# -- Tsukuyomi, the acceptance case, on a frozen copy of his store --------------

TSUKUYOMI_STORE = FIXTURES / "aspect_store_tsukuyomi"


def _committed_changes_through_ob47(tmp_path):
    """The item changes the committed snapshots record up to OB47. Copied
    out so a later patch's snapshot cannot move this test: these three files
    are history and are never rewritten."""
    import shutil
    from smite import snapshots
    snaps = tmp_path / "snapshots"
    snaps.mkdir()
    for day in ("2026-08-29", "2026-11-02", "2026-11-03"):
        shutil.copy(snapshots.SNAPSHOTS_DIR / f"{day}.json", snaps)
    return am.item_changes(snaps, snapshots.PATCH_HISTORY_PATH)


def _tsukuyomi_entry(tmp_path):
    block = am.note_block("Tsukuyomi", "Jungle", TSUKUYOMI_STORE, am.load_meta(TSUKUYOMI_STORE),
                          am.load_aggregate(TSUKUYOMI_STORE), am.item_name_lookup(),
                          _committed_changes_through_ob47(tmp_path))
    (entry,) = block["aspects"]
    return entry


def test_tsukuyomi_mangetsu_pools_ob45_to_ob47_and_reads_as_a_mid_mage(tmp_path):
    """His store as it stood on 2026-11-09 (`fixtures/aspect_store_tsukuyomi`):
    OB47 6, OB46 21, OB45 30, OB44 17. Below 30 on the two-window read (27),
    so the rule reaches back to OB45 and stops there, at 57."""
    entry = _tsukuyomi_entry(tmp_path)
    assert entry["matches_by_window"] == {"ob47": 6, "ob46": 21, "ob45": 30, "ob44": 17}
    assert entry["status"] == "shown" and entry["window_rule"] == "pooled back"
    assert entry["windows"] == ["ob45", "ob46", "ob47"] and entry["patches"] == "OB45–OB47"
    assert (entry["window_start"], entry["matches"], entry["wins"]) == ("2026-10-06", 57, 32)
    assert entry["roles"][:2] == [{"role": "Mid", "matches": 32, "share": 0.56},
                                  {"role": "Jungle", "matches": 15, "share": 0.26}]
    assert entry["base_role"] == "Jungle" and entry["role_shift"]["role"] == "Mid"
    assert [(i["name"], i["share"]) for i in entry["items"][:6]] == [
        ("Rod of Tahuti", 0.86), ("Book of Thoth", 0.79), ("Chronos' Pendant", 0.72),
        ("Obsidian Shard", 0.63), ("Polynomicon", 0.33), ("Spear of Desolation", 0.23)]
    assert entry["starters"][0] == {"name": "Bluestone Brooch", "share": 0.42}
    assert entry["relics"][0] == {"name": "Purification Beads", "share": 0.6}
    # The split index summed over the same three windows, not one of them.
    assert entry["aggregate"]["aspect_matches"] == 71


def test_tsukuyomi_mangetsu_flags_what_the_snapshots_cannot_place(tmp_path):
    """Four listed items moved between Ichor's OB40 and OB46 item data, and
    nothing in the repo says at which patch. The wiki's patch notes date two
    of them (Obsidian Shard, Polynomicon) to OB44, before this pool, and name
    Rod of Tahuti's +5 Intelligence nowhere; the rule does not read the wiki,
    so all four carry the span. Nothing OB47 changed is in his build."""
    entry = _tsukuyomi_entry(tmp_path)
    flags = {i["name"]: i["changed"] for i in entry["items"] if "changed" in i}
    assert sorted(flags) == ["Obsidian Shard", "Polynomicon", "Rod of Tahuti", "Spear of the Magus"]
    assert flags["Rod of Tahuti"] == {
        "patch": "OB41–OB46", "exact": False, "older_matches": 27, "matches": 49,
        "says": "its stats moved between Ichor's OB40 and OB46 item data, at a patch not "
                "recorded; up to 27 of the 49 matches that bought it are older"}
    assert not any("changed" in i for i in entry["starters"] + entry["relics"])
