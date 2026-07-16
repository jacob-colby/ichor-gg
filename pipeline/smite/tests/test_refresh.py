from pathlib import Path
from unittest import mock
from unittest.mock import Mock

from smite import notes, refresh

FIXTURES = Path(__file__).parent / "fixtures"


def test_refresh_god_writes_a_note(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "chiron_wiki.html").read_text(encoding="utf-8")

    refresh.refresh_god("Chiron", fetcher)

    frontmatter, body = notes.read_note(tmp_path / "Gods" / "Chiron.md")
    assert frontmatter["pantheon"] == "Greek"
    assert frontmatter["source_url"] == "https://wiki.smite2.com/w/Chiron"
    assert "<!-- WIKI:START -->" in body


def test_refresh_item_writes_a_note(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "deathbringer_wiki.html").read_text(encoding="utf-8")

    refresh.refresh_item("Deathbringer", fetcher)

    frontmatter, _ = notes.read_note(tmp_path / "Items" / "Deathbringer.md")
    assert frontmatter["cost"] == 2900
    assert frontmatter["builds_from"] == ["Skeggox", "Kopesh"]
    assert frontmatter["builds_into"] == []


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
    assert {"name": "Transcendence", "pick_rate": 0.61, "win_rate": 0.49} in community["slot_order"]


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
         mock.patch("smite.refresh.CachedFetcher") as MockCached:
        MockBrowser.return_value.fetch.side_effect = lambda url, force=False: wiki_html[url]
        MockCached.return_value.fetch.return_value = smitebrain_html

        refresh.refresh_all()

    god_frontmatter, _ = notes.read_note(tmp_path / "Gods" / "Chiron.md")
    item_frontmatter, _ = notes.read_note(tmp_path / "Items" / "Deathbringer.md")
    build_frontmatter, _ = notes.read_note(tmp_path / "Builds" / "Chiron-Conquest.md")

    assert god_frontmatter["pantheon"] == "Greek"
    assert item_frontmatter["cost"] == 2900
    assert any(b["source"] == "community" for b in build_frontmatter["builds"])
