from datetime import date
from pathlib import Path
from unittest import mock
from unittest.mock import Mock

import requests

from smite import notes, refresh

FIXTURES = Path(__file__).parent / "fixtures"


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
