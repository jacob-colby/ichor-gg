import json
from datetime import date
from pathlib import Path
from unittest import mock
from unittest.mock import Mock

import pytest
import requests

from smite import notes, refresh, smitebrain_parser

FIXTURES = Path(__file__).parent / "fixtures"


def _write_roster(data_root, names):
    (data_root / "_roster.json").write_text(
        json.dumps([{"name": n, "thumb": ""} for n in names]), encoding="utf-8")


def test_refresh_god_writes_a_note(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "chiron_wiki.html").read_text(encoding="utf-8")

    with mock.patch("smite.refresh.requests.get") as mock_get:
        mock_get.return_value = Mock(content=b"\x89PNG\r\n\x1a\nfakepngdata", status_code=200)
        mock_get.return_value.raise_for_status = Mock()
        refresh.refresh_god("Chiron", fetcher)

    frontmatter, body = notes.read_note(tmp_path / "Gods" / "Chiron.md")
    assert frontmatter["pantheon"] == "Greek"
    assert frontmatter["source_url"] == "https://wiki.smite2.com/w/Chiron"
    assert frontmatter["last_verified"] == date.today().isoformat()
    assert "<!-- WIKI:START -->" in body


def test_refresh_item_writes_a_note(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "deathbringer_wiki.html").read_text(encoding="utf-8")

    with mock.patch("smite.refresh.requests.get") as mock_get:
        mock_get.return_value = Mock(content=b"\x89PNG\r\n\x1a\nfakepngdata", status_code=200)
        mock_get.return_value.raise_for_status = Mock()
        refresh.refresh_item("Deathbringer", fetcher)

    frontmatter, _ = notes.read_note(tmp_path / "Items" / "Deathbringer.md")
    assert frontmatter["cost"] == 2900
    assert frontmatter["builds_from"] == ["Skeggox", "Kopesh"]
    assert frontmatter["builds_into"] == []
    assert frontmatter["stats"] == {"Strength": "45", "Critical Chance": "20%"}
    assert frontmatter["last_verified"] == date.today().isoformat()


def test_refresh_builds_into_inverts_builds_from_across_items(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    notes.write_note(tmp_path / "Items" / "Deathbringer.md",
                      {"name": "Deathbringer", "builds_from": ["Executioner"], "builds_into": []}, "")
    notes.write_note(tmp_path / "Items" / "Executioner.md",
                      {"name": "Executioner", "builds_from": [], "builds_into": []}, "")

    refresh.refresh_builds_into()

    frontmatter, _ = notes.read_note(tmp_path / "Items" / "Executioner.md")
    assert frontmatter["builds_into"] == ["Deathbringer"]


def test_refresh_god_builds_writes_community_entry(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "BUILDS_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "chiron_smitebrain.html").read_text(encoding="utf-8")

    refresh.refresh_god_builds("Chiron", "Conquest", fetcher)

    frontmatter, _ = notes.read_note(tmp_path / "Chiron-Conquest.md")
    community = next(b for b in frontmatter["builds"] if b["source"] == "community")
    assert community["aspect"] == "Aspect of the Heroic Tutor"
    top = community["slot_order"][0]
    assert top["name"] == "Transcendence" and top["pick_rate"] == 0.61 and top["win_rate"] == 0.49
    assert len(community["slot_order"]) == 3  # top pick per Core slot in the fixture, not every tile
    assert community["last_verified"] == date.today().isoformat()


def test_refresh_all_reruns_every_tracked_god_item_and_build(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    monkeypatch.setattr(refresh, "BUILDS_ROOT", tmp_path / "Builds")
    (tmp_path / "Gods").mkdir()
    (tmp_path / "Items").mkdir()
    (tmp_path / "Builds").mkdir()
    notes.write_note(tmp_path / "Gods" / "Chiron.md", {"name": "Chiron"}, "")
    notes.write_note(tmp_path / "Items" / "Deathbringer.md", {"name": "Deathbringer", "builds_from": []}, "")
    notes.write_note(tmp_path / "Builds" / "Chiron-Conquest.md", {"god": "Chiron", "mode": "Conquest", "builds": []}, "")

    wiki_html = {
        "https://wiki.smite2.com/w/Chiron": (FIXTURES / "chiron_wiki.html").read_text(encoding="utf-8"),
        "https://wiki.smite2.com/w/Deathbringer": (FIXTURES / "deathbringer_wiki.html").read_text(encoding="utf-8"),
    }
    smitebrain_html = (FIXTURES / "chiron_smitebrain.html").read_text(encoding="utf-8")

    with mock.patch("smite.refresh.BrowserFetcher") as MockBrowser, \
         mock.patch("smite.refresh.CachedFetcher") as MockCached, \
         mock.patch("smite.refresh.requests.get") as mock_get:
        MockBrowser.return_value.fetch.side_effect = lambda url, force=False: wiki_html[url]
        MockCached.return_value.fetch.return_value = smitebrain_html
        mock_get.return_value = Mock(content=b"\x89PNG\r\n\x1a\nfakepngdata", status_code=200)
        mock_get.return_value.raise_for_status = Mock()

        refresh.refresh_all()

    god_frontmatter, _ = notes.read_note(tmp_path / "Gods" / "Chiron.md")
    item_frontmatter, _ = notes.read_note(tmp_path / "Items" / "Deathbringer.md")
    build_frontmatter, _ = notes.read_note(tmp_path / "Builds" / "Chiron-Conquest.md")

    assert god_frontmatter["pantheon"] == "Greek"
    assert item_frontmatter["cost"] == 2900
    assert any(b["source"] == "community" for b in build_frontmatter["builds"])


def test_refresh_all_isolates_a_single_god_failure_and_still_refreshes_the_rest(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    monkeypatch.setattr(refresh, "BUILDS_ROOT", tmp_path / "Builds")
    (tmp_path / "Gods").mkdir()
    (tmp_path / "Items").mkdir()
    (tmp_path / "Builds").mkdir()
    notes.write_note(tmp_path / "Gods" / "Chiron.md", {"name": "Chiron"}, "")
    notes.write_note(tmp_path / "Gods" / "BrokenGod.md", {"name": "BrokenGod"}, "")

    chiron_html = (FIXTURES / "chiron_wiki.html").read_text(encoding="utf-8")

    def fetch(url, force=False):
        if "BrokenGod" in url:
            raise ValueError("simulated wiki layout change")
        return chiron_html

    with mock.patch("smite.refresh.BrowserFetcher") as MockBrowser, \
         mock.patch("smite.refresh.CachedFetcher") as MockCached, \
         mock.patch("smite.refresh.requests.get") as mock_get:
        MockBrowser.return_value.fetch.side_effect = fetch
        MockCached.return_value.fetch.return_value = ""
        mock_get.return_value = Mock(content=b"\x89PNG\r\n\x1a\nfakepngdata", status_code=200)
        mock_get.return_value.raise_for_status = Mock()

        refresh.refresh_all()  # must not raise

    chiron_frontmatter, _ = notes.read_note(tmp_path / "Gods" / "Chiron.md")
    assert chiron_frontmatter["pantheon"] == "Greek"
    broken_frontmatter, _ = notes.read_note(tmp_path / "Gods" / "BrokenGod.md")
    assert broken_frontmatter == {"name": "BrokenGod"}  # untouched by the failed refresh


def test_main_refresh_without_kind_returns_1(tmp_path, monkeypatch):
    assert refresh.main(["--refresh", "Chiron"]) == 1


def test_main_all_takes_precedence_over_refresh(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    monkeypatch.setattr(refresh, "BUILDS_ROOT", tmp_path / "Builds")
    (tmp_path / "Gods").mkdir()
    (tmp_path / "Items").mkdir()
    (tmp_path / "Builds").mkdir()

    with mock.patch("smite.refresh.refresh_all") as mock_refresh_all, \
         mock.patch("smite.refresh.refresh_god") as mock_refresh_god:
        # `--all` now exits on the failure count, so the stub has to return
        # one. A bare Mock is truthy and would read as a failed refresh.
        mock_refresh_all.return_value = 0
        result = refresh.main(["--all", "--refresh", "Chiron", "--kind", "god"])

    assert result == 0
    mock_refresh_all.assert_called_once()
    mock_refresh_god.assert_not_called()


def test_refresh_god_downloads_icon(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "chiron_wiki.html").read_text(encoding="utf-8")

    with mock.patch("smite.refresh.requests.get") as mock_get:
        mock_get.return_value = Mock(content=b"\x89PNG\r\n\x1a\nfakepngdata", status_code=200)
        mock_get.return_value.raise_for_status = Mock()
        refresh.refresh_god("Chiron", fetcher)

    icon_path = tmp_path / "_assets" / "icons" / "chiron.png"
    head_path = tmp_path / "_assets" / "icons" / "chiron-head.png"
    assert icon_path.exists()
    assert head_path.exists()  # portrait + square headshot both downloaded
    assert icon_path.read_bytes() == b"\x89PNG\r\n\x1a\nfakepngdata"
    mock_get.assert_any_call(
        "https://wiki.smite2.com/images/thumb/T_Chiron%28S2%29_Default.png/280px-T_Chiron%28S2%29_Default.png?157c1",
        timeout=20,
    )
    mock_get.assert_any_call(
        "https://wiki.smite2.com/images/T_Chiron%28S2%29_Default_Icon.png",
        timeout=20,
    )
    assert mock_get.call_count == 2


def test_refresh_god_skips_icon_download_if_already_present(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    icon_path = tmp_path / "_assets" / "icons" / "chiron.png"
    icon_path.parent.mkdir(parents=True)
    icon_path.write_bytes(b"\x89PNG\r\n\x1a\n" + b"x" * 2000)
    # Both the portrait and the headshot are already present, so neither
    # downloads.
    (icon_path.parent / "chiron-head.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"x" * 2000)

    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "chiron_wiki.html").read_text(encoding="utf-8")

    with mock.patch("smite.refresh.requests.get") as mock_get:
        refresh.refresh_god("Chiron", fetcher)

    mock_get.assert_not_called()


def test_refresh_item_downloads_icon(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "deathbringer_wiki.html").read_text(encoding="utf-8")

    with mock.patch("smite.refresh.requests.get") as mock_get:
        mock_get.return_value = Mock(content=b"\x89PNG\r\n\x1a\nfakepngdata", status_code=200)
        mock_get.return_value.raise_for_status = Mock()
        refresh.refresh_item("Deathbringer", fetcher)

    icon_path = tmp_path / "_assets" / "icons" / "deathbringer.png"
    assert icon_path.exists()


def test_refresh_god_survives_a_failed_icon_download(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "chiron_wiki.html").read_text(encoding="utf-8")

    with mock.patch("smite.refresh.requests.get") as mock_get:
        mock_get.side_effect = requests.RequestException("connection reset")
        refresh.refresh_god("Chiron", fetcher)  # must not raise

    icon_path = tmp_path / "_assets" / "icons" / "chiron.png"
    assert not icon_path.exists()
    frontmatter, _ = notes.read_note(tmp_path / "Gods" / "Chiron.md")
    assert frontmatter["pantheon"] == "Greek"  # note was still written correctly


def test_refresh_item_survives_a_failed_icon_download(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "deathbringer_wiki.html").read_text(encoding="utf-8")

    with mock.patch("smite.refresh.requests.get") as mock_get:
        mock_get.return_value = Mock(status_code=404)
        mock_get.return_value.raise_for_status.side_effect = requests.HTTPError("404")
        refresh.refresh_item("Deathbringer", fetcher)  # must not raise

    icon_path = tmp_path / "_assets" / "icons" / "deathbringer.png"
    assert not icon_path.exists()
    frontmatter, _ = notes.read_note(tmp_path / "Items" / "Deathbringer.md")
    assert frontmatter["cost"] == 2900  # note was still written correctly


def test_download_icon_is_a_noop_when_image_url_is_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)

    with mock.patch("smite.refresh.requests.get") as mock_get:
        refresh._download_icon(None, "chiron")
        refresh._download_icon("", "chiron")

    mock_get.assert_not_called()
    assert not (tmp_path / "_assets" / "icons" / "chiron.png").exists()


def test_refresh_roster_add_all_returns_empty_summary_when_roster_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)

    summary = refresh.refresh_roster_add_all()

    assert summary["added"] == []
    assert summary["failed"] == []
    assert summary["skipped"] == 0
    assert summary.get("note")  # explanatory, not a crash


def test_refresh_roster_add_all_skips_tracked_and_scrapes_untracked_gods(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    (tmp_path / "Gods").mkdir()
    notes.write_note(tmp_path / "Gods" / "Chiron.md", {"name": "Chiron"}, "")
    _write_roster(tmp_path, ["Chiron", "NewGod", "AnotherGod"])

    with mock.patch("smite.refresh.BrowserFetcher") as MockBrowser, \
         mock.patch("smite.refresh.CachedFetcher") as MockCached, \
         mock.patch("smite.refresh.refresh_god") as mock_refresh_god, \
         mock.patch("smite.refresh.refresh_god_builds") as mock_refresh_builds:
        summary = refresh.refresh_roster_add_all()

    assert summary["skipped"] == 1
    assert set(summary["added"]) == {"NewGod", "AnotherGod"}
    assert summary["failed"] == []
    assert mock_refresh_god.call_count == 2
    assert mock_refresh_builds.call_count == 2
    called_names = [c.args[0] for c in mock_refresh_god.call_args_list]
    assert "Chiron" not in called_names
    # fetchers are constructed once and reused across the whole batch
    MockBrowser.assert_called_once()
    MockCached.assert_called_once()


def test_refresh_roster_add_all_ignores_removed_gods_subdir(tmp_path, monkeypatch):
    # _removed/ is where manage_gods.remove() parks retired god notes — it
    # must not count as "tracked" (top-level glob only).
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    (tmp_path / "Gods").mkdir()
    (tmp_path / "Gods" / "_removed").mkdir()
    notes.write_note(tmp_path / "Gods" / "_removed" / "OldGod.md", {"name": "OldGod"}, "")
    _write_roster(tmp_path, ["OldGod"])

    with mock.patch("smite.refresh.BrowserFetcher"), \
         mock.patch("smite.refresh.CachedFetcher"), \
         mock.patch("smite.refresh.refresh_god") as mock_refresh_god, \
         mock.patch("smite.refresh.refresh_god_builds"):
        summary = refresh.refresh_roster_add_all()

    assert summary["skipped"] == 0
    assert summary["added"] == ["OldGod"]
    mock_refresh_god.assert_called_once()


def test_refresh_roster_add_all_continues_after_a_god_failure(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    (tmp_path / "Gods").mkdir()
    _write_roster(tmp_path, ["BrokenGod", "GoodGod"])

    def fake_refresh_god(name, fetcher, force=False, allow_shrink=False):
        if name == "BrokenGod":
            raise ValueError("simulated wiki layout change")

    with mock.patch("smite.refresh.BrowserFetcher"), \
         mock.patch("smite.refresh.CachedFetcher"), \
         mock.patch("smite.refresh.refresh_god", side_effect=fake_refresh_god) as mock_refresh_god, \
         mock.patch("smite.refresh.refresh_god_builds") as mock_refresh_builds:
        summary = refresh.refresh_roster_add_all()  # must not raise

    assert summary["added"] == ["GoodGod"]
    assert len(summary["failed"]) == 1
    failed_name, failed_err = summary["failed"][0]
    assert failed_name == "BrokenGod"
    assert "simulated wiki layout change" in failed_err
    assert mock_refresh_god.call_count == 2  # both attempted despite the failure
    assert mock_refresh_builds.call_count == 1  # only for the god that didn't raise


def test_main_roster_add_all_calls_refresh_roster_add_all_and_prints_summary(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)

    with mock.patch("smite.refresh.refresh_roster_add_all") as mock_fn:
        mock_fn.return_value = {"added": ["A", "B"], "failed": [("C", "boom")], "skipped": 5}
        result = refresh.main(["--roster-add-all"])

    assert result == 0
    mock_fn.assert_called_once()
    captured = capsys.readouterr()
    assert "Added 2, failed 1, skipped 5" in captured.out
    assert "FAILED C: boom" in captured.out


# --- refresh_patch_version (Task R1: scrape the current patch version) ----

def test_refresh_patch_version_picks_highest_numbered_beta_regardless_of_order(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    # Fixture lists Open Beta 37/35/39/36/38 in that (shuffled, non-sorted)
    # document order — 39 is neither first nor last, so a naive
    # "first/last link wins" implementation would get this wrong.
    fetcher.fetch.return_value = (FIXTURES / "patch_notes_wiki.html").read_text(encoding="utf-8")

    result = refresh.refresh_patch_version(fetcher)

    assert result == {"patch": "Open Beta 39", "captured": date.today().isoformat()}
    fetcher.fetch.assert_called_once_with("https://wiki.smite2.com/w/Patch_notes", force=False)

    saved = json.loads((tmp_path / "_patch.json").read_text(encoding="utf-8"))
    assert saved == {"patch": "Open Beta 39", "captured": date.today().isoformat(),
                     "data_patch": "Open Beta 39"}


def test_refresh_patch_version_never_walks_back_a_label_the_steam_feed_recorded(tmp_path, monkeypatch):
    """The wiki lags the game. When `patch_feed` has already recorded OB40
    from Steam, a wiki that still says OB39 marks the item data as OB39's and
    leaves the game label where it is."""
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    (tmp_path / "_patch_history.json").write_text(json.dumps([
        {"patch": "Open Beta 39", "first_seen": "2026-07-14", "source": "steam"},
        {"patch": "Open Beta 40", "first_seen": "2026-07-28", "source": "steam"}]))
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "patch_notes_wiki.html").read_text(encoding="utf-8")

    refresh.refresh_patch_version(fetcher)

    saved = json.loads((tmp_path / "_patch.json").read_text(encoding="utf-8"))
    assert saved == {"patch": "Open Beta 40", "captured": "2026-07-28", "data_patch": "Open Beta 39"}


def test_refresh_patch_version_forwards_force_flag(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "patch_notes_wiki.html").read_text(encoding="utf-8")

    refresh.refresh_patch_version(fetcher, force=True)

    fetcher.fetch.assert_called_once_with("https://wiki.smite2.com/w/Patch_notes", force=True)


def test_refresh_patch_version_garbage_page_returns_none_and_leaves_existing_file_intact(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    existing = {"patch": "Open Beta 38", "captured": "2026-06-15"}
    (tmp_path / "_patch.json").write_text(json.dumps(existing), encoding="utf-8")
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "patch_notes_garbage.html").read_text(encoding="utf-8")

    result = refresh.refresh_patch_version(fetcher)

    assert result is None
    assert json.loads((tmp_path / "_patch.json").read_text(encoding="utf-8")) == existing


def test_refresh_patch_version_failed_fetch_returns_none_and_does_not_raise(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.side_effect = RuntimeError("Cloudflare challenge")

    result = refresh.refresh_patch_version(fetcher)  # must not raise

    assert result is None
    assert not (tmp_path / "_patch.json").exists()


def test_refresh_patch_version_no_existing_file_and_garbage_page_writes_nothing(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = "<html><body>nothing relevant here</body></html>"

    result = refresh.refresh_patch_version(fetcher)

    assert result is None
    assert not (tmp_path / "_patch.json").exists()


def test_refresh_all_also_refreshes_patch_version(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    monkeypatch.setattr(refresh, "BUILDS_ROOT", tmp_path / "Builds")
    (tmp_path / "Gods").mkdir()
    (tmp_path / "Items").mkdir()
    (tmp_path / "Builds").mkdir()

    with mock.patch("smite.refresh.BrowserFetcher") as MockBrowser, \
         mock.patch("smite.refresh.CachedFetcher"), \
         mock.patch("smite.refresh.refresh_patch_version") as mock_patch:
        refresh.refresh_all()

    mock_patch.assert_called_once_with(MockBrowser.return_value, force=False)


def test_main_patch_flag_calls_refresh_patch_version(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)

    with mock.patch("smite.refresh.BrowserFetcher"), \
         mock.patch("smite.refresh.refresh_patch_version") as mock_fn:
        mock_fn.return_value = {"patch": "Open Beta 39", "captured": "2026-07-26"}
        result = refresh.main(["--patch"])

    assert result == 0
    mock_fn.assert_called_once()
    captured = capsys.readouterr()
    assert "Open Beta 39" in captured.out


def test_main_patch_flag_prints_a_message_even_on_failure(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)

    with mock.patch("smite.refresh.BrowserFetcher"), \
         mock.patch("smite.refresh.refresh_patch_version") as mock_fn:
        mock_fn.return_value = None
        result = refresh.main(["--patch"])

    assert result == 0
    captured = capsys.readouterr()
    assert captured.out.strip()


def test_refresh_god_builds_skips_community_for_modes_smitebrain_lacks(tmp_path, monkeypatch):
    """SmiteBrain serves one page per god with no mode dimension, so scraping it
    for Joust stored Conquest numbers under a Joust label — the tier list then
    presented them as Joust community data. Non-covered modes must write no
    community entry at all rather than a mislabeled copy."""
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    monkeypatch.setattr(refresh, "BUILDS_ROOT", tmp_path / "builds")
    (tmp_path / "builds").mkdir(parents=True, exist_ok=True)
    calls = []

    class _F:
        def fetch(self, url, force=False):
            calls.append(url)
            return "<html></html>"

    monkeypatch.setattr(refresh.smitebrain_parser, "parse_build_page",
                        lambda html: {"aspects": [], "items": [{"name": "X", "pick_rate": 0.5}]})
    refresh.refresh_god_builds("Agni", "Joust", _F())
    assert calls == [], "must not even fetch SmiteBrain for a mode it doesn't cover"


# -- the collapse guard ------------------------------------------------------
#
# `wiki_parser.parse_god_page` raises on one thing: a missing infobox. Every
# other shape change degrades to empty, and `notes.merge_god_note` REPLACES the
# frontmatter — so a silent parse miss overwrites the only copy. Measured
# 2026-08-29: blanking Ullr, Artio and Merlin's kits moves win-weighted
# coverage 0.5530 -> 0.5552 (up), PASSes `validate --check`, and produces zero
# `data_audit` findings. Nothing downstream can catch this, so it is caught at
# the write.

def test_a_kit_that_parses_to_zero_is_refused_and_says_what_it_saw():
    with pytest.raises(refresh.ParseCollapse) as exc:
        refresh._refuse_god_collapse("Ullr", {"abilities": [1, 2, 3, 4]}, {"abilities": []})
    assert "Ullr: 4 abilities -> 0" in str(exc.value)


def test_a_shrinking_kit_is_refused_and_names_the_override():
    with pytest.raises(refresh.ParseCollapse) as exc:
        refresh._refuse_god_collapse("Merlin", {"abilities": [1] * 12}, {"abilities": [1] * 5})
    assert "Merlin: 12 abilities -> 5" in str(exc.value)
    assert "--allow-shrink" in str(exc.value)


def test_a_brand_new_god_that_parses_to_zero_is_still_refused():
    """The "half-parses a new god and commits it" case. There is no previous
    value to compare against, and zero is still not a kit."""
    with pytest.raises(refresh.ParseCollapse) as exc:
        refresh._refuse_god_collapse("Ravana", {}, {"abilities": []})
    assert "0 abilities -> 0" in str(exc.value)


def test_a_growing_or_steady_kit_writes_normally():
    refresh._refuse_god_collapse("Ra", {"abilities": [1, 2, 3]}, {"abilities": [1, 2, 3]})
    refresh._refuse_god_collapse("Ra", {"abilities": [1, 2, 3]}, {"abilities": [1, 2, 3, 4]})
    refresh._refuse_god_collapse("Ravana", {}, {"abilities": [1, 2, 3, 4, 5, 6]})


def test_an_item_losing_every_stat_is_refused():
    with pytest.raises(refresh.ParseCollapse) as exc:
        refresh._refuse_item_collapse(
            "Deathbringer", {"stats": {"Strength": "45"}, "cost": 2900},
            {"stats": {}, "cost": 2900})
    assert "Deathbringer: 1 stats -> 0" in str(exc.value)


def test_an_item_losing_a_readable_cost_is_refused():
    with pytest.raises(refresh.ParseCollapse) as exc:
        refresh._refuse_item_collapse(
            "Deathbringer", {"stats": {"Strength": "45"}, "cost": 2900},
            {"stats": {"Strength": "45"}, "cost": None})
    assert "cost 2900 -> unreadable" in str(exc.value)


def test_a_genuinely_statless_item_is_not_a_collapse():
    """Mote of Chaos and Survivor's Sash are real statless tier-2s and two of
    `data_audit`'s standing findings. Zero stats is only a defect for a god."""
    refresh._refuse_item_collapse("Mote of Chaos", {"stats": {}, "cost": 500},
                                  {"stats": {}, "cost": 500})


def test_refresh_all_exit_code_is_the_failure_count(monkeypatch, tmp_path):
    """It returned None while `main` returned 0 regardless, so a run printing
    twelve [FAILED] lines still exited clean — which made every "gate it on the
    exit code" plan for this command a no-op."""
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    monkeypatch.setattr(refresh, "BUILDS_ROOT", tmp_path / "builds")
    (tmp_path / "Gods").mkdir()
    (tmp_path / "Items").mkdir()
    (tmp_path / "builds").mkdir()
    (tmp_path / "Gods" / "Ullr.md").write_text("---\nname: Ullr\n---\n", encoding="utf-8")

    monkeypatch.setattr(refresh, "BrowserFetcher", lambda *a, **k: object())
    monkeypatch.setattr(refresh, "CachedFetcher", lambda *a, **k: object())
    monkeypatch.setattr(refresh, "refresh_patch_version", lambda *a, **k: None)
    monkeypatch.setattr(refresh, "refresh_god_index", lambda *a, **k: {})
    monkeypatch.setattr(refresh, "refresh_item_index", lambda *a, **k: 0)

    def boom(name, *a, **k):
        raise refresh.ParseCollapse(f"{name}: 4 abilities -> 0")
    monkeypatch.setattr(refresh, "refresh_god", boom)

    assert refresh.refresh_all() == 1


# ── The community window and the collapse it can cause (2026-11-05) ──────
#
# `_refuse_god_collapse` above guards the WIKI side, per note, at the write.
# The community side had no guard at all, which is how a one-day match window
# reached a commit: the daily job's one enforced gate is `validate --check`,
# and it PASSED, because its Spearman floor is window-aware by design and so
# relaxes to 0.30 for exactly the young window that did the damage.


def _window_fetcher(by_window, page_html=""):
    """A fetcher whose god-index response depends on the `time=` parameter."""
    def fetch(url, force=False):
        if "__data.json" not in url:
            return page_html
        window = next((p.split("=")[1] for p in url.split("&") if p.startswith("time=")), None)
        rows = by_window[window]
        return json.dumps({"nodes": [{"type": "data", "data": rows}]})
    f = Mock()
    f.fetch.side_effect = fetch
    return f


def _index_rows(n, start):
    """`n` god-level index rows in the shape `parse_god_index` reads."""
    return [{"god": f"God{i}", "win_rate": 0.5, "matches_played": 100,
             "matches_won": 50, "aspect": None, "start_time": start,
             "end_time": "2026-11-04T17:32:46.170Z"} for i in range(n)]


def test_the_window_chooser_steps_back_when_the_newest_patch_is_too_young(monkeypatch):
    """The 2026-11-05 measurement, as the rule sees it: ob47 covered 86 gods
    on a one-day window where ob46's closed window covered 94."""
    html = (FIXTURES / "achilles_smitebrain_thin_window.html").read_text(encoding="utf-8")
    monkeypatch.setattr(refresh.smitebrain_parser, "parse_god_index",
                        lambda payload: payload["nodes"][0]["data"])
    fetcher = _window_fetcher({"ob47": _index_rows(86, "2026-11-03T11:33:33.847Z"),
                               "ob46": _index_rows(94, "2026-10-20T11:48:48.610Z")}, html)
    assert refresh.choose_community_window(fetcher, "Achilles") == ("ob46", 94)


def test_a_tie_keeps_the_newer_window_so_the_rule_never_goes_stale(monkeypatch):
    """The reason this needs no threshold and no maintenance: the day a new
    patch's window covers as much as the one before it, it wins on the tie."""
    html = (FIXTURES / "achilles_smitebrain_thin_window.html").read_text(encoding="utf-8")
    monkeypatch.setattr(refresh.smitebrain_parser, "parse_god_index",
                        lambda payload: payload["nodes"][0]["data"])
    fetcher = _window_fetcher({"ob47": _index_rows(94, "2026-11-03T11:33:33.847Z"),
                               "ob46": _index_rows(94, "2026-10-20T11:48:48.610Z")}, html)
    assert refresh.choose_community_window(fetcher, "Achilles") == ("ob47", 94)


def test_the_window_chooser_falls_back_to_the_site_default_if_it_cannot_read():
    fetcher = Mock()
    fetcher.fetch.side_effect = RuntimeError("502")
    assert refresh.choose_community_window(fetcher, "Achilles") == (None, None)


def test_the_window_rides_every_url_the_run_touches():
    assert refresh.community_url("Cu Chulainn") == "https://smitebrain.com/gods/cu-chulainn/"
    assert refresh.community_url("Cu Chulainn", "ob46") == \
        "https://smitebrain.com/gods/cu-chulainn/?time=ob46"


def test_a_roster_wide_loss_of_complete_records_is_refused():
    before = {f"God{i}": 6 for i in range(94)}
    after = {f"God{i}": 6 for i in range(47)}
    with pytest.raises(refresh.ParseCollapse) as exc:
        refresh._refuse_community_collapse(before, after)
    assert "94 complete -> 47" in str(exc.value)
    assert "47 god(s) lost" in str(exc.value)
    assert "--allow-shrink" in str(exc.value)
    assert "choose_community_window" in str(exc.value)


def test_one_god_falling_out_is_churn_not_a_collapse():
    """The slack, and why it is one: on the eleven refreshes on record before
    2026-11-04 every god with a record had a complete one, and the count only
    ever grew. One god covers a genuine disable or rework."""
    before = {f"God{i}": 6 for i in range(94)}
    refresh._refuse_community_collapse(before, {k: v for k, v in list(before.items())[:93]})


def test_gaining_records_is_never_a_collapse():
    before = {f"God{i}": 6 for i in range(47)}
    refresh._refuse_community_collapse(before, {f"God{i}": 6 for i in range(94)})


def test_an_incomplete_record_does_not_count_as_complete(tmp_path, monkeypatch):
    """Six is the number everything downstream reads: `comparison_six` fills
    to six and `side_by_side` skips a god who does not make 6 of 6. A god
    truncated to five is therefore a LOST record, not a shorter one."""
    monkeypatch.setattr(refresh, "BUILDS_ROOT", tmp_path)
    for god, slots in (("Full", 6), ("Short", 5), ("Empty", 0)):
        notes.merge_build_note(tmp_path / f"{god}-Conquest.md", god, "Conquest",
                               {"slot_order": [{"name": f"Item{i}"} for i in range(slots)]})
    assert set(refresh.complete_community_records()) == {"Full"}


# ── The window's provenance, carried from the god index (2026-11-05) ─────
#
# `_community_items.json`'s `matches_analyzed`, `window_start` and `window_end`
# were null and empty from the day the file was written, because the ITEM index
# response carries none of them. The GOD index carries all three. Both are
# fetched with the same `time=` window in the same run, so the god index is
# where the item table's provenance comes from.


def test_the_item_index_response_carries_no_provenance_at_all():
    """The measured fact the fix rests on. Reading it off the parser's own
    required fields rather than the live site, so it cannot flake."""
    assert smitebrain_parser._ITEM_INDEX_REQUIRED == ("display_name", "win_rate",
                                                      "matches_played")
    for field in refresh.WINDOW_PROVENANCE:
        assert field not in smitebrain_parser._ITEM_INDEX_REQUIRED


def test_window_provenance_reads_the_three_fields_off_the_god_index():
    rows = [{"god": "A", "start_time": "2026-10-20T11:48:48.610Z",
             "end_time": "2026-11-03T11:09:17.233Z", "matches_analyzed": 14667},
            {"god": "B", "start_time": "2026-10-20T11:48:48.610Z",
             "end_time": "2026-11-03T11:09:17.233Z", "matches_analyzed": 14667}]
    assert refresh.window_provenance(rows) == {
        "window_start": "2026-10-20", "window_end": "2026-11-03",
        "matches_analyzed": 14667}


def test_window_provenance_is_empty_rather_than_half_filled():
    """An item-index row, which has none of the three: the result must be
    empty so the writer leaves the fields null instead of writing `""`."""
    assert refresh.window_provenance([]) == {}
    assert refresh.window_provenance([{"display_name": "Adroit Ring", "win_rate": 0.5,
                                       "matches_played": 399}]) == {}


def test_the_item_index_writes_the_provenance_it_is_handed(tmp_path, monkeypatch):
    payload = {"nodes": [{"type": "data", "data": [
        {"display_name": "Adroit Ring", "win_rate": 0.486, "matches_played": 399,
         "matches_won": 194, "use_rate": 0.005908310134454777}]}]}
    monkeypatch.setattr(refresh.smitebrain_parser, "parse_item_index",
                        lambda p: p["nodes"][0]["data"])
    fetcher = Mock()
    fetcher.fetch.return_value = json.dumps(payload)
    refresh.refresh_item_index(fetcher, tmp_path, window="ob46", provenance={
        "window_start": "2026-10-20", "window_end": "2026-11-03",
        "matches_analyzed": 14667})
    out = json.loads((tmp_path / refresh.COMMUNITY_ITEMS_FILE).read_text(encoding="utf-8"))
    assert out["window"] == "ob46"
    assert out["window_start"] == "2026-10-20"
    assert out["window_end"] == "2026-11-03"
    assert out["matches_analyzed"] == 14667
    assert "time=ob46" in fetcher.fetch.call_args[0][0]


def test_the_item_index_leaves_the_fields_null_without_provenance(tmp_path, monkeypatch):
    """No provenance must mean NULL, not an empty string or a zero — an old
    file has to stay distinguishable from one that was handed real values."""
    payload = {"nodes": [{"type": "data", "data": [
        {"display_name": "Adroit Ring", "win_rate": 0.486, "matches_played": 399,
         "matches_won": 194, "use_rate": 0.0059}]}]}
    monkeypatch.setattr(refresh.smitebrain_parser, "parse_item_index",
                        lambda p: p["nodes"][0]["data"])
    fetcher = Mock()
    fetcher.fetch.return_value = json.dumps(payload)
    refresh.refresh_item_index(fetcher, tmp_path, window="ob46")
    out = json.loads((tmp_path / refresh.COMMUNITY_ITEMS_FILE).read_text(encoding="utf-8"))
    assert out["matches_analyzed"] is None
    assert out["window_start"] is None and out["window_end"] is None


def test_the_shipped_file_now_carries_all_three():
    table = json.loads((refresh.DATA_ROOT / refresh.COMMUNITY_ITEMS_FILE)
                       .read_text(encoding="utf-8"))
    assert table["window"] == "ob46"
    assert table["matches_analyzed"] == 14667
    assert table["window_start"] == "2026-10-20"
    assert table["window_end"] == "2026-11-03"
