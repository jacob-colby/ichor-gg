"""`patch_feed`: the daily job's unattended patch detector.

Two fixtures. `steam_news.json` is CONSTRUCTED to GetNewsForApp's documented
shape and pins behaviour (previews, hotfix dupes, backfill, failure). The
`recorded/steam/` responses are REAL — fetched from a GitHub runner on
2026-11-02 by `probe-steam-feed.yml` — and the tests at the bottom pin what the
feed reads from what Hi-Rez actually posts.
"""
import copy
import json
import pathlib

import pytest

from smite import patch_feed, snapshots

FIXTURE = json.loads((pathlib.Path(__file__).parent / "fixtures" / "steam_news.json")
                     .read_text(encoding="utf-8"))


@pytest.fixture
def vault(tmp_path):
    (tmp_path / "_patch_history.json").write_text(json.dumps([
        {"patch": "Open Beta 40", "first_seen": "2026-08-01", "data_from": "2026-08-01"},
        {"patch": "Open Beta 45", "first_seen": "2026-10-06", "source": "manual"},
    ]), encoding="utf-8")
    (tmp_path / "_patch.json").write_text(json.dumps(
        {"patch": "Open Beta 45", "captured": "2026-10-06", "data_patch": "Open Beta 40"}, indent=2),
        encoding="utf-8")
    return tmp_path


def _files(root):
    return {p.name: p.read_bytes() for p in root.iterdir()}


def test_parses_patch_posts_and_skips_previews_hotfix_dupes_and_events():
    posts = patch_feed.patch_posts(FIXTURE)
    assert [p["patch"] for p in posts] == ["Open Beta 45", "Open Beta 46"]
    ob45, ob46 = posts
    # The smite2.com link quoted for THIS label wins over the Steam URL and
    # over the OB45 link quoted in the same body.
    assert ob46["official_url"] == "https://www.smite2.com/news/open-beta-46-update-notes/"
    assert ob46["first_seen"] == "2026-10-19"  # notes post, not the later hotfix
    assert ob45["official_url"].startswith("https://steamstore-a.akamaihd.net/news/externalpost/")


def test_a_new_patch_closes_the_old_period_and_opens_a_new_one(vault):
    rows = patch_feed.update(vault, fetch=lambda: FIXTURE)
    assert [r["patch"] for r in rows] == ["Open Beta 46"]
    hist = json.loads((vault / "_patch_history.json").read_text())
    assert hist[-1] == {"patch": "Open Beta 46", "first_seen": "2026-10-19", "source": "steam",
                        "label_source": "title",
                        "official_url": "https://www.smite2.com/news/open-beta-46-update-notes/"}
    assert snapshots.patch_at(hist, "2026-10-18") == "Open Beta 45"
    assert snapshots.patch_at(hist, "2026-10-19") == "Open Beta 46"
    current = json.loads((vault / "_patch.json").read_text())
    # The game label moves; the label the item data reflects does not.
    assert current == {"patch": "Open Beta 46", "captured": "2026-10-19",
                       "data_patch": "Open Beta 40"}


def test_no_new_patch_changes_nothing(vault):
    payload = copy.deepcopy(FIXTURE)
    payload["appnews"]["newsitems"] = [i for i in payload["appnews"]["newsitems"]
                                       if "OB46" not in i["title"]]
    before = _files(vault)
    assert patch_feed.update(vault, fetch=lambda: payload) == []
    after = _files(vault)
    # The only write allowed is the cross-check's note of Steam's newest label.
    assert after.pop(patch_feed.STATE_FILE) is not None
    assert after == before


def test_a_duplicate_run_on_the_same_day_is_a_no_op(vault):
    patch_feed.update(vault, fetch=lambda: FIXTURE)
    after_first = _files(vault)
    assert patch_feed.update(vault, fetch=lambda: FIXTURE) == []
    assert _files(vault) == after_first


@pytest.mark.parametrize("fetch", [
    lambda: (_ for _ in ()).throw(OSError("CONNECT tunnel failed, response 403")),
    lambda: {"unexpected": "shape"},
    lambda: {"appnews": {"newsitems": []}},
])
def test_a_failed_fetch_never_raises_and_never_invents_a_patch(vault, fetch, capsys):
    before = _files(vault)
    assert patch_feed.update(vault, fetch=fetch) == []
    assert _files(vault) == before
    assert "[patch feed]" in capsys.readouterr().out


def test_main_exits_zero_even_on_a_bug(monkeypatch):
    def boom(**_):
        raise RuntimeError("bug")
    monkeypatch.setattr(patch_feed, "update", boom)
    assert patch_feed.main([]) == 0


def test_backfills_every_missed_patch_in_order(tmp_path):
    (tmp_path / "_patch_history.json").write_text(json.dumps(
        [{"patch": "Open Beta 40", "first_seen": "2026-08-01"}]))
    rows = patch_feed.update(tmp_path, fetch=lambda: FIXTURE)
    assert [r["patch"] for r in rows] == ["Open Beta 45", "Open Beta 46"]


def test_never_walks_the_label_back_or_dates_before_the_newest_row(vault):
    payload = copy.deepcopy(FIXTURE)
    for i in payload["appnews"]["newsitems"]:
        i["date"] = 1754006400  # 2025-08-01, before every recorded row
    rows = patch_feed.update(vault, fetch=lambda: payload)
    assert [(r["patch"], r["first_seen"]) for r in rows] == [("Open Beta 46", "2026-10-06")]


def test_ignores_posts_outside_the_announcements_feed(vault):
    payload = copy.deepcopy(FIXTURE)
    for i in payload["appnews"]["newsitems"]:
        i["feedname"] = "pcgamer"
    before = _files(vault)
    assert patch_feed.update(vault, fetch=lambda: payload) == []
    assert _files(vault) == before


def test_a_manual_override_beats_the_detected_link(vault):
    patch_feed.update(vault, fetch=lambda: FIXTURE)
    (vault / "_patch_links.yaml").write_text(
        "links:\n  Open Beta 46: https://www.smite2.com/news/hand-checked/\n")
    hist = snapshots.load_patch_history(vault / "_patch_history.json")
    links = snapshots.patch_links(hist, snapshots.load_patch_links(vault / "_patch_links.yaml"))
    assert links["Open Beta 46"] == "https://www.smite2.com/news/hand-checked/"
    assert snapshots.patch_links(hist)["Open Beta 46"] == \
        "https://www.smite2.com/news/open-beta-46-update-notes/"


def test_steam_urls_are_official_only_for_smite2_news():
    assert snapshots.is_official_url("https://store.steampowered.com/news/app/2437170/view/1")
    assert not snapshots.is_official_url("https://store.steampowered.com/news/app/730/view/1")
    assert not snapshots.is_official_url("https://store.steampowered.com/app/2437170/")
    assert not snapshots.is_official_url("http://store.steampowered.com/news/app/2437170/view/1")


def test_wiki_refresh_marks_data_patch_without_walking_back_the_game_label(vault):
    patch_feed.update(vault, fetch=lambda: FIXTURE)
    hist_path = vault / "_patch_history.json"
    # The wiki lags: it still says OB45 after Steam recorded OB46.
    assert snapshots.record_patch("Open Beta 45", "2026-10-21", hist_path) is True
    assert snapshots.record_patch("Open Beta 45", "2026-10-22", hist_path) is False
    hist = snapshots.load_patch_history(hist_path)
    assert snapshots.current_patch(hist) == {
        "patch": "Open Beta 46", "captured": "2026-10-19", "data_patch": "Open Beta 45"}


def test_periods_are_attributed_by_data_date_not_game_date(tmp_path):
    """The shipped store's case: two game patches landed inside a period that
    changed no item stats, because no wiki refresh ran under either."""
    d = tmp_path / "snapshots"
    d.mkdir()
    (d / "2026-08-01.json").write_text(json.dumps({"A": {"cost": 1, "tier": 1, "stats": {}}}))
    (d / "2026-08-29.json").write_text(json.dumps({"A": {"cost": 1, "tier": 1, "stats": {}},
                                                    "B": {"cost": 1, "tier": 1, "stats": {}}}))
    hist = [{"patch": "Open Beta 40", "first_seen": "2026-08-01"},
            {"patch": "Open Beta 41", "first_seen": "2026-08-11", "source": "steam"},
            {"patch": "Open Beta 42", "first_seen": "2026-08-25", "source": "steam"}]
    [period] = snapshots.build_patch_report(sorted(d.glob("*.json")), history=hist)
    assert period["crosses_patch"] is False
    assert period["patch_to"] == "Open Beta 40"
    assert period["highlights"] == []


# -- the recorded response -----------------------------------------------------

RECORDED = pathlib.Path(__file__).parent / "fixtures" / "recorded" / "steam"


def _recorded(name="announcements"):
    return json.loads((RECORDED / f"{name}.json").read_text(encoding="utf-8"))


def test_the_recording_is_the_request_the_feed_makes():
    payload = _recorded()
    items = payload["appnews"]["newsitems"]
    assert payload["appnews"]["appid"] == snapshots.STEAM_APP_ID
    assert len(items) == patch_feed.FETCH_COUNT
    assert {i["feedname"] for i in items} == {patch_feed.ANNOUNCEMENTS_FEED}


def test_root_cause_titles_stopped_carrying_the_label_after_open_beta_26():
    """What the first live run saw, reproduced: on titles alone the newest
    label in the real feed is Open Beta 26 (January 2026)."""
    titled = [int(m.group(1)) for i in _recorded()["appnews"]["newsitems"]
              for m in [patch_feed._LABEL_RE.search(i["title"])] if m]
    assert max(titled) == 26


def test_the_real_feed_yields_every_labelled_patch_in_it():
    rows = patch_feed.patch_posts(_recorded())
    got = [(r["patch"], r["first_seen"], r["label_source"]) for r in rows]
    assert got == [
        ("Open Beta 21", "2025-10-24", "title"),
        ("Open Beta 22", "2025-11-04", "notes-link"),
        ("Open Beta 23", "2025-11-18", "notes-link"),
        ("Open Beta 24", "2025-12-02", "notes-link"),
        ("Open Beta 26", "2026-01-09", "body"),
        ("Open Beta 28", "2026-02-09", "notes-link"),
        ("Open Beta 29", "2026-02-23", "notes-link"),
        ("Open Beta 30", "2026-03-10", "notes-link"),
        ("Open Beta 31", "2026-03-23", "notes-link"),
        ("Open Beta 32", "2026-04-07", "notes-link"),
        ("Open Beta 33", "2026-04-20", "notes-link"),
        ("Open Beta 36", "2026-06-01", "title"),      # "Take Flight in Update 36"
        ("Open Beta 37", "2026-06-15", "body"),       # "[h1]OB 37- Goddess Of Cats Update"
        ("Open Beta 44", "2026-09-22", "body"),       # "...during OB44", the Hel post
    ]


def test_labels_read_from_the_real_feed_are_in_game_order():
    """No body mention reads a past or future patch onto the wrong date: in
    the real feed the labels rise strictly with the post date."""
    rows = patch_feed.patch_posts(_recorded())
    days = [r["first_seen"] for r in rows]
    assert days == sorted(days) and len(set(days)) == len(days)


def test_the_real_feed_agrees_with_the_hand_recorded_history():
    """`data/_patch_history.json` holds Open Beta 41-46 by hand. Where the
    feed reads one of them, it reads the same day."""
    history = {r["patch"]: r["first_seen"] for r in
               json.loads((snapshots.DATA_ROOT / "_patch_history.json").read_text(encoding="utf-8"))}
    overlap = [r for r in patch_feed.patch_posts(_recorded()) if r["patch"] in history]
    assert overlap, "the recording should overlap the recorded history"
    for r in overlap:
        assert r["first_seen"] == history[r["patch"]], r["patch"]


def test_the_notes_link_is_the_official_url_when_the_post_quotes_one():
    rows = {r["patch"]: r for r in patch_feed.patch_posts(_recorded())}
    assert rows["Open Beta 33"]["official_url"] == "https://www.smite2.com/news/open-beta-33-update-notes/"
    assert snapshots.is_official_url(rows["Open Beta 44"]["official_url"])


def test_on_the_real_feed_with_the_real_history_nothing_is_recorded(vault):
    """Today's actual state: the history is at Open Beta 46 by hand and Steam's
    newest labelled post is 44. No row, no label walked back — and the newest
    Steam label is kept for the cross-check."""
    hist = [{"patch": f"Open Beta {n}", "first_seen": d, "source": "manual"} for n, d in
            [(44, "2026-09-22"), (45, "2026-10-06"), (46, "2026-10-20")]]
    (vault / "_patch_history.json").write_text(json.dumps(hist))
    before = (vault / "_patch_history.json").read_bytes(), (vault / "_patch.json").read_bytes()
    assert patch_feed.update(vault, fetch=_recorded) == []
    assert ((vault / "_patch_history.json").read_bytes(), (vault / "_patch.json").read_bytes()) == before
    assert patch_feed.load_state(vault) == {
        "patch": "Open Beta 44", "first_seen": "2026-09-22", "label_source": "body"}


def test_the_state_file_does_not_change_on_a_quiet_day(vault):
    patch_feed.update(vault, fetch=_recorded)
    first = (vault / patch_feed.STATE_FILE).read_bytes()
    patch_feed.update(vault, fetch=_recorded)
    assert (vault / patch_feed.STATE_FILE).read_bytes() == first


def test_the_real_feed_would_record_a_patch_from_the_body_when_one_is_new(tmp_path):
    (tmp_path / "_patch_history.json").write_text(json.dumps(
        [{"patch": "Open Beta 40", "first_seen": "2026-08-01"}]))
    rows = patch_feed.update(tmp_path, fetch=_recorded)
    assert [(r["patch"], r["label_source"]) for r in rows] == [("Open Beta 44", "body")]


def _post(title, body=""):
    return {"title": title, "contents": body, "feedname": patch_feed.ANNOUNCEMENTS_FEED,
            "date": 1760000000}


@pytest.mark.parametrize("body", [
    "Hel is here! Coming in OB47: a new jungle.",
    "Patch preview — the next update, OB47, changes jungle camps.",
    "These changes will hit PTS ahead of OB47.",
])
def test_a_body_that_previews_the_next_patch_is_not_read_as_it(body):
    assert patch_feed.post_label(_post("Unleash HEL!", "We are live on OB46. " + body)) == (46, "body")


def test_a_post_with_a_preview_title_is_never_read():
    assert patch_feed.post_label(_post("OB47 Preview", "[h1]OB47[/h1]")) is None


def test_title_beats_link_beats_body():
    body = "see https://www.smite2.com/news/open-beta-45-update-notes/ ... during OB44"
    assert patch_feed.post_label(_post("OB46 - King Kappa", body)) == (46, "title")
    assert patch_feed.post_label(_post("Unleash HEL!", body)) == (45, "notes-link")
    assert patch_feed.post_label(_post("Unleash HEL!", "during OB44")) == (44, "body")
    assert patch_feed.post_label(_post("TO VICTORY with NIKE!", "No label anywhere.")) is None


# -- the cross-check -------------------------------------------------------------

def test_the_sources_agreeing_is_a_plain_line():
    line = patch_feed.cross_check({"patch": "Open Beta 46"}, "Open Beta 46")
    assert line.startswith("[patch sources] agree")


def test_steam_behind_the_wiki_is_a_notice_naming_both():
    line = patch_feed.cross_check(
        {"patch": "Open Beta 44", "first_seen": "2026-09-22", "label_source": "body"}, "Open Beta 46")
    assert line.startswith("::notice::[patch sources] disagree")
    assert "Open Beta 44" in line and "Open Beta 46" in line


def test_steam_ahead_of_the_wiki_is_a_warning():
    line = patch_feed.cross_check({"patch": "Open Beta 47", "first_seen": "2026-11-03"}, "Open Beta 46")
    assert line.startswith("::warning::[patch sources] disagree")


def test_no_steam_state_cannot_compare_and_says_so():
    assert "cannot compare" in patch_feed.cross_check({}, "Open Beta 46")
