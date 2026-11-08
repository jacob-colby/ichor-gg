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

    def __init__(self, gods, broken=None):
        self.gods = gods                    # {slug: {"name", "aspects", "feeds": {aspect|none: [raw]}}}
        self.broken = broken or set()
        self.urls = []

    def __call__(self, url):
        self.urls.append(url)
        if url.startswith(am.INDEX_URL):
            window = re.search(r"time=(ob\d+)", url).group(1)
            w = META["windows"][window]
            return json.dumps(_index_payload(window, w["start"], w["end"]))
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


# -- the build-note entry ------------------------------------------------------

@pytest.mark.parametrize("counts, expected", [
    ({"ob47": 30, "ob46": 99}, ("ob47", "newest")),
    ({"ob47": 29, "ob46": 30}, ("ob46", "last closed")),
    ({"ob47": 5, "ob46": 29}, (None, "below minimum")),
    ({"ob47": 5, "ob46": 21, "ob45": 30}, (None, "below minimum")),   # Tsukuyomi: one step only
])
def test_the_window_rule(counts, expected):
    assert am.choose_window(counts, ["ob47", "ob46", "ob45"]) == expected


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
    assert entry["status"] == "shown" and entry["window"] == "ob47"
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
