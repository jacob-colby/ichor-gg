"""The unattended stats refresh: it writes a whole patch or nothing.

Fixtures are RECORDED, not constructed: `fixtures/recorded/page_*.html` were
fetched from wiki.smite2.com by a GitHub-hosted runner on 2026-11-02 (Open
Beta 46) with the same honest User-Agent `WikiPageFetcher` sends, and
`notes_ob40/` is what the repo held for those six pages under Open Beta 40.
Between the two, Merlin's ultimate moved 15% -> 25% Intelligence scaling —
a real patch change, which is what the success case asserts.
"""
import json
import shutil
from pathlib import Path

import pytest

from smite import notes, snapshots, stats_refresh as sr

FIX = Path(__file__).parent / "fixtures" / "recorded"
TODAY = "2026-11-02"


def _page_file(page: str) -> Path:
    return FIX / f"page_{page.lower().replace(' ', '_').replace(chr(39), '')}.html"


class RecordedWiki:
    """Serves the recorded pages. `override` swaps a page's HTML; `fail_on`
    makes a page unreachable."""

    def __init__(self, override=None, fail_on=None):
        self.override = override or {}
        self.fail_on = fail_on
        self.requests = 0

    def fetch(self, page):
        self.requests += 1
        if page == self.fail_on:
            raise sr.SourceError(f"{page}: Cloudflare challenge (cf-mitigated=challenge)")
        if page in self.override:
            return self.override[page]
        return _page_file(page).read_text(encoding="utf-8")


@pytest.fixture
def root(tmp_path):
    shutil.copytree(FIX / "notes_ob40", tmp_path, dirs_exist_ok=True)
    # A hand-written line outside the WIKI block, which a refresh must keep.
    path = tmp_path / "Gods" / "Merlin.md"
    fm, body = notes.read_note(path)
    notes.write_note(path, fm, body + "\nMy own note about Merlin.\n")
    return tmp_path


def _tree(root: Path) -> dict:
    return {str(p.relative_to(root)): p.read_bytes()
            for p in sorted(root.rglob("*")) if p.is_file()}


# -- a successful refresh ---------------------------------------------------

def test_a_due_refresh_brings_the_data_to_the_wikis_patch(root):
    res = sr.run(root, RecordedWiki(), today=TODAY)

    assert res["status"] == "refreshed"
    assert res["wiki_patch"] == "Open Beta 46"
    assert "Merlin" in res["changed_gods"]
    merlin, body = notes.read_note(root / "Gods" / "Merlin.md")
    text = json.dumps(merlin["abilities"])
    assert "Damage: 0 | 90 | 120 | 150 | 180 | 220" in text
    assert "Damage: 0 | 80 | 110 | 140 | 170 | 210" not in text
    assert merlin["last_verified"] == TODAY
    assert "My own note about Merlin." in body

    patch = json.loads((root / "_patch.json").read_text())
    assert patch["patch"] == patch["data_patch"] == "Open Beta 46"
    ob46 = next(r for r in snapshots.load_patch_history(root / "_patch_history.json")
                if r["patch"] == "Open Beta 46")
    assert ob46["data_from"] == TODAY
    assert json.loads((root / sr.STATE_FILE).read_text())["last_success"] == TODAY
    assert not (root / ".stats_staging").exists()
    assert not (root / "Gods.bak").exists()


def test_a_note_whose_stats_did_not_move_is_left_byte_identical(root):
    before = (root / "Items" / "Deathbringer.md").read_bytes()
    sr.run(root, RecordedWiki(), today=TODAY)
    # last_verified is not a stat: rewriting it would make every weekly check
    # a 316-file commit that says nothing.
    assert (root / "Items" / "Deathbringer.md").read_bytes() == before


# -- the source fails -------------------------------------------------------

def test_an_unreachable_page_leaves_every_file_untouched(root):
    before = _tree(root)
    res = sr.run(root, RecordedWiki(fail_on="Deathbringer"), today=TODAY)
    assert res["status"] == "source-failed"
    assert "Deathbringer" in res["error"]
    assert _tree(root) == before


def test_an_unreachable_patch_index_leaves_every_file_untouched(root):
    before = _tree(root)
    res = sr.run(root, RecordedWiki(fail_on="Patch notes"), today=TODAY)
    assert res["status"] == "source-failed"
    assert _tree(root) == before


def test_a_cloudflare_challenge_is_a_source_error_not_a_page():
    class Resp:
        status_code = 403
        headers = {"cf-mitigated": "challenge"}
        text = "<html><title>Please wait</title></html>"

    class Session:
        headers = {}

        def get(self, url, timeout):
            return Resp()

    fetcher = sr.WikiPageFetcher(session=Session(), sleep=lambda s: None)
    with pytest.raises(sr.SourceError, match="Cloudflare"):
        fetcher.fetch("Chiron")
    assert "ichor-gg" in Session.headers["User-Agent"]


def test_a_transient_error_is_retried():
    class Resp:
        def __init__(self, code):
            self.status_code, self.headers, self.text = code, {}, "<html>ok</html>"

    class Session:
        headers = {}
        codes = [503, 200]

        def get(self, url, timeout):
            return Resp(self.codes.pop(0))

    fetcher = sr.WikiPageFetcher(session=Session(), sleep=lambda s: None)
    assert fetcher.fetch("Chiron") == "<html>ok</html>"


# -- validation fails -------------------------------------------------------

def test_a_kit_that_parses_to_empty_refuses_the_whole_patch(root):
    """The measured failure mode behind keeping the scrape manual: Ullr's
    abilities sit where the parser cannot see them, the kit reads as empty,
    and no downstream gate notices. Here it must stop everything — including
    Merlin's genuine change — not just Ullr."""
    before = _tree(root)
    broken = _page_file("Ullr").read_text(encoding="utf-8").replace('id="Abilities"', 'id="Moved"')
    res = sr.run(root, RecordedWiki(override={"Ullr": broken}), today=TODAY)
    assert res["status"] == "refused"
    assert "Ullr" in res["problems"][0]
    assert _tree(root) == before


def test_a_stat_that_does_not_parse_as_a_number_refuses(root):
    before = _tree(root)
    html = _page_file("Deathbringer").read_text(encoding="utf-8")
    assert "<b>45</b> Strength" in html
    broken = html.replace("<b>45</b> Strength", "<b>forty-five</b> Strength", 1)
    res = sr.run(root, RecordedWiki(override={"Deathbringer": broken}), today=TODAY)
    assert res["status"] == "refused", res
    assert any("does not parse" in p or "Deathbringer" in p for p in res["problems"])
    assert _tree(root) == before


def test_validate_refuses_a_mass_loss_of_stats():
    old = {f"I{i}": {"tier": 3, "cost": 100, "stats": {"Strength": "10"}} for i in range(200)}
    new = {k: dict(v, stats={}) if i < 10 else v for i, (k, v) in enumerate(old.items())}
    problems = sr.validate({}, {}, old, new)
    assert any(p.startswith("items with stats: 200 -> 190") for p in problems)


def test_validate_refuses_mass_nulls():
    gods = {f"G{i}": {"pantheon": "Greek", "role": "Mid", "damage_type": "magical"} for i in range(90)}
    new = {k: dict(v, role=None) if i < 20 else v for i, (k, v) in enumerate(gods.items())}
    assert any("role null" in p for p in sr.validate(gods, new, {}, {}))


def test_validate_allows_an_ordinary_patch():
    old = {f"I{i}": {"tier": 3, "cost": 100, "stats": {"Strength": "10"}} for i in range(200)}
    new = {k: dict(v, stats={"Strength": "15"}, cost=120) for k, v in old.items()}
    assert sr.validate({}, {}, old, new) == []


def test_a_failed_swap_puts_the_live_directories_back(root, monkeypatch):
    before = _tree(root)
    real = sr.os.replace
    calls = []

    def flaky(src, dst):
        calls.append((src, dst))
        if len(calls) == 4:  # Items: live -> backup succeeded, staged -> live fails
            raise OSError("disk full")
        return real(src, dst)

    monkeypatch.setattr(sr.os, "replace", flaky)
    with pytest.raises(OSError):
        sr.run(root, RecordedWiki(), today=TODAY)
    monkeypatch.setattr(sr.os, "replace", real)
    assert _tree(root) == before


# -- nothing to do ----------------------------------------------------------

def test_current_stats_cost_one_request_and_write_nothing(root):
    sr.run(root, RecordedWiki(), today=TODAY)
    before = _tree(root)
    wiki = RecordedWiki()
    res = sr.run(root, wiki, today="2026-11-03")
    assert res["status"] == "not-due"
    assert wiki.requests == 1  # the wiki's Patch_notes index, nothing else
    assert _tree(root) == before


def test_a_patch_the_steam_feed_missed_is_caught_from_the_wiki(root):
    """The feed's first live run found no title newer than Open Beta 26. If
    `_patch.json` never hears of a patch, the wiki's own index must still
    make the refresh due — not a week later."""
    (root / "_patch.json").write_text(json.dumps(
        {"patch": "Open Beta 40", "captured": "2026-08-01", "data_patch": "Open Beta 40"}))
    (root / sr.STATE_FILE).write_text(json.dumps({"last_success": "2026-11-01"}))
    res = sr.run(root, RecordedWiki(), today=TODAY)
    assert res["status"] == "refreshed" and res["reason"] == "wiki-patch"
    assert json.loads((root / "_patch.json").read_text())["data_patch"] == "Open Beta 46"


def test_a_weekly_check_with_nothing_new_changes_only_the_check_date(root):
    sr.run(root, RecordedWiki(), today=TODAY)
    before = _tree(root)
    res = sr.run(root, RecordedWiki(), today="2026-11-09")
    assert res["status"] == "unchanged" and res["reason"] == "weekly"
    after = _tree(root)
    assert {k for k in after if after[k] != before.get(k)} == {sr.STATE_FILE}


def test_a_patch_the_wiki_has_not_caught_up_with_costs_one_request(root):
    before = _tree(root)
    stale_index = "<html>SMITE 2 Open Beta 40 · SMITE 2 Open Beta 39</html>"
    wiki = RecordedWiki(override={"Patch notes": stale_index})
    res = sr.run(root, wiki, today=TODAY)
    assert res["status"] == "waiting-for-wiki"
    assert wiki.requests == 1
    assert _tree(root) == before


def test_dry_run_writes_nothing(root):
    before = _tree(root)
    res = sr.run(root, RecordedWiki(), today=TODAY, dry_run=True)
    assert res["status"] == "dry-run" and "Merlin" in res["changed_gods"]
    assert _tree(root) == before


def test_due_reason():
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        (d / "_patch.json").write_text(json.dumps({"patch": "Open Beta 46", "data_patch": "Open Beta 40"}))
        assert sr.due_reason(d, TODAY) == "patch"
        (d / "_patch.json").write_text(json.dumps({"patch": "Open Beta 46", "data_patch": "Open Beta 46"}))
        assert sr.due_reason(d, TODAY) == "weekly"  # never checked
        (d / sr.STATE_FILE).write_text(json.dumps({"last_success": "2026-10-30"}))
        assert sr.due_reason(d, TODAY) is None
        assert sr.due_reason(d, "2026-11-06") == "weekly"


def test_main_never_fails_the_job(monkeypatch):
    def boom(**kw):
        raise RuntimeError("bug")
    monkeypatch.setattr(sr, "run", boom)
    assert sr.main([]) == 0
