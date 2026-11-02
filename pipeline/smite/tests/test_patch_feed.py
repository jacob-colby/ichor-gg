"""`patch_feed`: the daily job's unattended patch detector.

The fixture is CONSTRUCTED to GetNewsForApp's shape, not recorded — see the
module docstring. These tests pin behaviour, not Steam's live title format.
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
    assert _files(vault) == before


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
