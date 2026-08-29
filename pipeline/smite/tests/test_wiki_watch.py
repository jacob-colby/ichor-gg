"""The detector that replaces a scheduled scrape.

Every case here is drawn from what the live wiki actually looked like on
2026-08-29: 92 names on the grid, 89 tracked, Ravana ready to add, Hachiman
and Hel listed with empty pages, and the patch string two releases ahead of
`data/_patch.json`.
"""
import json
import pathlib

import pytest

from smite import wiki_watch


class FakeFetcher:
    """Serves canned HTML by URL suffix; raises for anything unregistered."""

    def __init__(self, pages):
        self.pages = pages
        self.fetched = []

    def fetch(self, url, force=False):
        self.fetched.append(url)
        for suffix, html in self.pages.items():
            if url.endswith(suffix):
                return html
        raise RuntimeError(f"no page for {url}")


def _grid(*names):
    """The Gods page shape `refresh.parse_roster_names` reads."""
    cells = "".join(
        f'<span typeof="mw:File"><a href="/w/{n.replace(" ", "_")}" title="{n}"></a></span>'
        for n in names
    )
    return f"<html><body>{cells}</body></html>"


FIXTURES = pathlib.Path(__file__).parent / "fixtures"

# A real cached wiki god page (Chiron), so "parses" here means what the actual
# parser does with the actual markup rather than what a hand-written stub
# happens to satisfy. Hand-written HTML passed `parse_god_page` and returned
# zero abilities, which is exactly the HALF_PARSED state below.
GOD_PAGE = (FIXTURES / "chiron_wiki.html").read_text(encoding="utf-8")
GOD_PAGE_ABILITIES = 2

# An infobox and nothing the ability walk recognises: the Ullr/Artio/Merlin
# shape, and the reason a page that "parses" is not automatically usable.
HALF_PARSED_PAGE = (
    '<html><body><table class="infobox">'
    "<tr><th>Roles</th><td>Jungle</td></tr>"
    "</table></body></html>"
)

EMPTY_PAGE = "<html><body><p>There is currently no text in this page.</p></body></html>"
PATCH_PAGE = '<html><body><a>SMITE 2 Open Beta 42</a><a>SMITE 2 Open Beta 41</a></body></html>'


@pytest.fixture
def vault(tmp_path):
    (tmp_path / "Gods").mkdir()
    for name in ("Ra", "Ullr"):
        (tmp_path / "Gods" / f"{name}.md").write_text("---\nname: X\n---\n", encoding="utf-8")
    (tmp_path / "_roster.json").write_text(
        json.dumps([{"name": "Ra"}, {"name": "Ullr"}]), encoding="utf-8")
    (tmp_path / "_patch.json").write_text(
        json.dumps({"patch": "Open Beta 40"}), encoding="utf-8")
    return tmp_path


def test_a_new_god_with_a_real_page_is_ready_and_actionable(vault):
    fetcher = FakeFetcher({
        "/Gods": _grid("Ra", "Ullr", "Ravana"),
        "/Ravana": GOD_PAGE,
        "/Patch_notes": PATCH_PAGE,
    })

    result = wiki_watch.survey(fetcher, data_root=vault)

    assert result["roster_new"] == ["Ravana"]
    assert [p["name"] for p in result["untracked"]] == ["Ravana"]
    assert result["untracked"][0]["state"] == wiki_watch.READY
    assert result["untracked"][0]["abilities"] == GOD_PAGE_ABILITIES
    assert wiki_watch.actionable(result)
    assert "Ravana" in wiki_watch.report_markdown(result)


def test_a_roster_name_with_an_empty_page_is_reported_and_NOT_actionable(vault):
    """Hachiman and Hel. A count-based detector files these as work every
    morning until the wiki editors get round to writing them up."""
    fetcher = FakeFetcher({
        "/Gods": _grid("Ra", "Ullr", "Hachiman", "Hel"),
        "/Hachiman": EMPTY_PAGE,
        "/Hel": EMPTY_PAGE,
        "/Patch_notes": '<html><body><a>SMITE 2 Open Beta 40</a></body></html>',
    })

    result = wiki_watch.survey(fetcher, data_root=vault)

    assert {p["state"] for p in result["untracked"]} == {wiki_watch.NO_PAGE}
    assert not wiki_watch.actionable(result)
    report = wiki_watch.report_markdown(result)
    assert "Listed, but not there yet" in report
    assert "Ready to add" not in report


def test_a_patch_string_ahead_of_the_vault_is_actionable(vault):
    fetcher = FakeFetcher({
        "/Gods": _grid("Ra", "Ullr"),
        "/Patch_notes": PATCH_PAGE,
    })

    result = wiki_watch.survey(fetcher, data_root=vault)

    assert (result["patch_live"], result["patch_recorded"]) == ("Open Beta 42", "Open Beta 40")
    assert wiki_watch.actionable(result)
    assert "Open Beta 42" in wiki_watch.report_markdown(result)


def test_a_caught_up_vault_is_quiet(vault):
    fetcher = FakeFetcher({
        "/Gods": _grid("Ra", "Ullr"),
        "/Patch_notes": '<html><body><a>SMITE 2 Open Beta 40</a></body></html>',
    })

    result = wiki_watch.survey(fetcher, data_root=vault)

    assert not wiki_watch.actionable(result)


def test_a_god_leaving_the_roster_is_actionable(vault):
    fetcher = FakeFetcher({
        "/Gods": _grid("Ra"),
        "/Patch_notes": '<html><body><a>SMITE 2 Open Beta 40</a></body></html>',
    })

    result = wiki_watch.survey(fetcher, data_root=vault)

    assert result["roster_gone"] == ["Ullr"]
    assert result["tracked_gone"] == ["Ullr"]
    assert wiki_watch.actionable(result)


def test_the_probe_cap_reports_what_it_skipped_rather_than_dropping_it(vault):
    names = [f"New{i}" for i in range(5)]
    fetcher = FakeFetcher({
        "/Gods": _grid("Ra", "Ullr", *names),
        **{f"/{n}": GOD_PAGE for n in names},
        "/Patch_notes": '<html><body><a>SMITE 2 Open Beta 40</a></body></html>',
    })

    result = wiki_watch.survey(fetcher, data_root=vault, probe_limit=2)

    states = [p["state"] for p in result["untracked"]]
    assert states.count(wiki_watch.READY) == 2
    assert states.count(wiki_watch.UNPROBED) == 3
    assert "Not probed" in wiki_watch.report_markdown(result)
    assert wiki_watch.actionable(result), "an unprobed name is still a name we do not have"


def test_the_survey_writes_nothing(vault):
    """A detector that mutates what it watches has nothing to compare against
    next time — the whole reason `parse_roster_names` and
    `scrape_patch_version` were split out of their writing halves."""
    before = {p.name: p.read_bytes() for p in vault.rglob("*") if p.is_file()}
    fetcher = FakeFetcher({
        "/Gods": _grid("Ra", "Ullr", "Ravana"),
        "/Ravana": GOD_PAGE,
        "/Patch_notes": PATCH_PAGE,
    })

    wiki_watch.survey(fetcher, data_root=vault)

    assert {p.name: p.read_bytes() for p in vault.rglob("*") if p.is_file()} == before


def test_an_infobox_with_no_abilities_is_a_parser_alarm_not_a_new_god(vault):
    """The failure that used to reach the data silently. It must never read as
    "ready to add" — the answer is to fix the parser, not to scrape the god."""
    fetcher = FakeFetcher({
        "/Gods": _grid("Ra", "Ullr", "Ravana"),
        "/Ravana": HALF_PARSED_PAGE,
        "/Patch_notes": '<html><body><a>SMITE 2 Open Beta 40</a></body></html>',
    })

    result = wiki_watch.survey(fetcher, data_root=vault)

    assert result["untracked"][0]["state"] == wiki_watch.HALF_PARSED
    assert wiki_watch.actionable(result)
    report = wiki_watch.report_markdown(result)
    assert "The parser could not read these" in report
    assert "Ready to add" not in report
