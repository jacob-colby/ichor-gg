import json
from datetime import date
from pathlib import Path
from unittest import mock
from unittest.mock import Mock

import requests

from smite import notes, refresh

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

    def fake_refresh_god(name, fetcher, force=False):
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
    assert saved == {"patch": "Open Beta 39", "captured": date.today().isoformat()}


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
