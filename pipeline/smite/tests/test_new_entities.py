"""`smite.new_entities`: new gods and items reach the data unattended, whole
or not at all, and only past the same gate as a stats refresh.

Runs against pages recorded from a GitHub-hosted runner on 2026-11-02
(`fixtures/recorded/new_entities/`, `.github/workflows/probe-new-entities.yml`)
on a throwaway data root. The suite and the recompute are injected, as in
`test_stats_gate`; one test runs the real model path on the new god.
"""
import json
import re
import shutil
from pathlib import Path

import pytest
import yaml
from bs4 import BeautifulSoup

from smite import new_entities as ne
from smite import recommend, refresh, scoring, stats_refresh, wiki_parser

REC = Path(__file__).resolve().parent / "fixtures" / "recorded"
NEW = REC / "new_entities"
INDEX = json.loads((NEW / "index.json").read_text(encoding="utf-8"))
TODAY = "2026-11-02"
NEW_GODS = ["Nike", "Hachiman", "Kuzenbo", "Hel"]
NEW_ITEMS = ["Lotus Sickle", "Soul Locket"]


class Fetcher:
    """Serves the recorded pages by title; anything else is a 404, which is
    what the runner got for Kumbhakarna, Heimdallr and Maman Brigitte."""

    def __init__(self, overrides=None):
        self.overrides = dict(overrides or {})
        self.calls = []

    def fetch(self, page):
        self.calls.append(page)
        if page in self.overrides:
            return self.overrides[page]
        entry = INDEX.get(page)
        if not entry or "error" in entry:
            raise stats_refresh.SourceError(f"{page}: HTTP 404")
        return (NEW / entry["file"]).read_text(encoding="utf-8")


def _page(name):
    return (NEW / INDEX[name]["file"]).read_text(encoding="utf-8")


@pytest.fixture
def root(tmp_path):
    """A data root that tracks every god on the recorded grid except the new
    ones, and the real 226 items, catalogue and weights."""
    root = tmp_path / "data"
    (root / "Gods").mkdir(parents=True)
    roster = refresh.parse_roster_names(_page("Gods"))
    new = set(NEW_GODS) | {"Nox", "Kumbhakarna", "Heimdallr", "Maman Brigitte"}
    for n in roster:
        if n not in new:
            (root / "Gods" / f"{n}.md").write_text(f"---\nname: {n}\n---\n", encoding="utf-8")
    shutil.copytree(recommend.DATA_ROOT / "Items", root / "Items")
    for f in ("_passive_classes.yaml", "_weights.yaml"):
        shutil.copy2(recommend.DATA_ROOT / f, root / f)
    return root


def _run(root, fetcher=None, checks=None, recompute=None, **kw):
    return ne.run(root, fetcher=fetcher or Fetcher(), today=TODAY,
                  checks=checks or (lambda ids: set()), recompute=recompute or (lambda: None),
                  icons=lambda *a: None, community=None, **kw)


def _catalogue(root):
    return yaml.safe_load((root / "_passive_classes.yaml").read_text(encoding="utf-8"))


def _tree(root):
    return {str(p.relative_to(root)): p.read_bytes()
            for p in sorted(root.rglob("*")) if p.is_file()}


# -- discovery -----------------------------------------------------------------

def test_the_recorded_items_index_lists_the_pool_with_tiers():
    index = ne.parse_item_index(_page("Items"))
    assert index["Lotus Sickle"] == 3 and index["Soul Locket"] == 3
    assert index.get("Deathbringer") == 3
    tracked = {p.stem for p in (recommend.DATA_ROOT / "Items").glob("*.md")}
    # The index is the wiki's whole shop: almost all of it is tracked already.
    assert len(set(index) & tracked) > 150


def test_discovery_finds_exactly_the_untracked_entities(root):
    found = ne.discover(Fetcher(), root)
    assert found["new_gods"] == ["Nike", "Kumbhakarna", "Hachiman", "Kuzenbo",
                                 "Heimdallr", "Hel", "Nox", "Maman Brigitte"]
    assert sorted(found["new_items"]) == NEW_ITEMS


def test_a_god_the_owner_removed_is_never_re_added(root):
    (root / "Gods" / "_removed").mkdir()
    (root / "Gods" / "_removed" / "nike.md").write_text("---\nname: Nike\n---\n")
    assert "Nike" not in ne.discover(Fetcher(), root)["new_gods"]


# -- a new god, end to end ---------------------------------------------------------

def test_a_new_god_is_added_whole_and_gets_builds_from_the_model(root):
    result = _run(root)
    assert result["status"] == "added"
    assert [c["name"] for c in result["kept"] if c["kind"] == "god"] == NEW_GODS

    fm, body = ne.notes.read_note(root / "Gods" / "Nike.md")
    assert fm["type"] == "smite-god" and fm["name"] == "Nike"
    assert (fm["pantheon"], fm["role"], fm["damage_type"]) == ("Greek", "Solo", "physical")
    assert len(fm["abilities"]) == 6 and fm["aspects"][0]["name"] == "Aspect of Victorious Conquest"
    assert fm["base_stats"]["health"]["base"] == 668.5
    assert fm["source_url"] == "https://wiki.smite2.com/w/Nike"
    assert "<!-- WIKI:START -->\n- Nike Basic Attack" in body
    # Hel is a stance god: both stances' abilities, the case that once read empty.
    assert len(ne.notes.read_note(root / "Gods" / "Hel.md")[0]["abilities"]) == 11

    roster = [g["name"] for g in json.loads((root / "_roster.json").read_text(encoding="utf-8"))]
    assert set(NEW_GODS) <= set(roster) and "Nox" in roster

    # The normal model path, on the real item pool: a full core, every slot buildable.
    god = ne.notes.read_note(root / "Gods" / "Nike.md")[0]
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags = scoring.load_tags(recommend.TAGS_PATH)
    entries = recommend.build_suggested_entries(god, items, {"builds": []}, weights, tags, "Conquest")
    core = [s["name"] if isinstance(s, dict) else s for s in entries[0]["slot_order"]]
    by_name = {it["name"]: it for it in items}
    assert len(core) == 6 and all(scoring.is_buildable(by_name[n], god) for n in core)


def test_the_four_live_gods_and_the_placeholder_nox(root):
    result = _run(root)
    skipped = {s["name"]: s["why"] for s in result["skipped"]}
    assert skipped["Kumbhakarna"] == "no page yet (HTTP 404)"
    assert "base stats read as zero" in skipped["Nox"]
    assert not (root / "Gods" / "Nox.md").exists()
    log = json.loads((root / ne.LOG_FILE).read_text(encoding="utf-8"))
    assert {a["name"] for a in log["added"]} == set(NEW_GODS) | set(NEW_ITEMS)
    assert any(s["name"] == "Nox" for s in log["last_run"]["skipped"])


# -- new items and the passive catalogue --------------------------------------------

def test_a_new_item_with_an_uncatalogued_passive_is_added_stat_only_and_flagged(root):
    result = _run(root)
    fm, _ = ne.notes.read_note(root / "Items" / "Lotus Sickle.md")
    assert fm["cost"] == 2150 and fm["stats"]["Intelligence"] == "40"
    assert fm["builds_from"] == ["Ring of Dispel", "Mana Tome"]
    for comp in fm["builds_from"]:
        into = ne.notes.read_note(root / "Items" / f"{comp}.md")[0]["builds_into"]
        assert "Lotus Sickle" in into and into == sorted(into)

    entry = _catalogue(root)["items"]["Lotus Sickle"]
    assert entry["uncatalogued"] is True and entry["added"] == TODAY
    assert "classes" not in entry and "priced" not in entry

    # Stat-only means stat-only: no shipped flag reprices it.
    weights = scoring.load_weights(root / "_weights.yaml")
    pool = ne._load_items(root)
    assert not any("Lotus Sickle" in ne._repriced_by(pool, weights, f) for f in ne._flag_keys(weights))

    kept = {c["name"]: c.get("passive_status") for c in result["kept"]}
    assert kept["Lotus Sickle"] == kept["Soul Locket"] == "uncatalogued"
    report = ne.report(result)
    assert "::warning::[new entities] Lotus Sickle: passive is UNCATALOGUED" in report


def test_the_comment_header_of_the_catalogue_survives_the_append(root):
    before = (root / "_passive_classes.yaml").read_text(encoding="utf-8")
    _run(root)
    after = (root / "_passive_classes.yaml").read_text(encoding="utf-8")
    assert after.startswith(before)


def _adaptive_lotus():
    """The recorded Lotus Sickle page with its passive rewritten to an
    `Adaptive Stat:` line — a clause shape the shipped flags already price."""
    html = _page("Lotus Sickle")
    passive = wiki_parser.parse_item_page(html)["passive"]
    first = passive.split(" ")[0:4]
    assert first == ["Ability", "Buffed,", "Healed,", "or"]
    return html.replace("Ability Buffed, Healed, or Shielded another Allied God",
                        "Adaptive Stat: +40 Strength or +60 Intelligence (based on highest item stat). "
                        "Ability Buffed, Healed, or Shielded another Allied God", 1)


def test_a_new_item_with_a_catalogued_passive_shape_is_classed_from_the_catalogue(root):
    fetcher = Fetcher({"Lotus Sickle": _adaptive_lotus()})
    result = _run(root, fetcher=fetcher)
    entry = _catalogue(root)["items"]["Lotus Sickle"]
    # A1 because every catalogued item `price_adaptive` alone reprices says A1 —
    # read off the file, never typed in here.
    assert entry["classes"] == ["A1"] and entry["priced"] == ["A1"]
    assert entry["auto_classified"] is True and "uncatalogued" not in entry
    assert {c["name"]: c.get("passive_status") for c in result["kept"]}["Lotus Sickle"] == "auto"


def test_the_flag_to_class_map_is_learned_from_the_catalogue():
    items = recommend.load_items()
    cat = yaml.safe_load((recommend.DATA_ROOT / "_passive_classes.yaml").read_text(encoding="utf-8"))
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    mapping = ne.flag_classes(items, cat, weights)
    assert mapping["price_adaptive"] == "A1"


def test_an_item_the_catalogue_already_names_is_catalogued_and_writes_nothing(root):
    lotus = refresh.item_note_content("Lotus Sickle", wiki_parser.parse_item_page(_page("Lotus Sickle")), "", TODAY)
    cat = {"items": {"Lotus Sickle": {"classes": ["D1"], "note": "hand-written ahead of the add"}}}
    status, entry, problem = ne.classify_passive(lotus, ne._load_items(Path(recommend.DATA_ROOT)) + [lotus],
                                                 cat, scoring.load_weights(recommend.WEIGHTS_PATH), TODAY)
    assert (status, entry, problem) == ("catalogued", None, None)


def test_a_flag_the_catalogue_cannot_name_leaves_the_item_out(root, monkeypatch):
    monkeypatch.setattr(ne, "flag_classes", lambda *a: {"price_adaptive": None})
    result = _run(root, fetcher=Fetcher({"Lotus Sickle": _adaptive_lotus()}))
    assert "does not name one clause class" in {s["name"]: s["why"] for s in result["skipped"]}["Lotus Sickle"]
    assert not (root / "Items" / "Lotus Sickle.md").exists()
    assert "Lotus Sickle" not in _catalogue(root)["items"]


# -- pages that do not parse ---------------------------------------------------------

def _ullr_without_tabs():
    """Ullr as the parser saw him before `_section_tables` entered the
    `img-tab-wrapper`: the stance tabs gone, the kit read as two names."""
    soup = BeautifulSoup((REC / "page_ullr.html").read_text(encoding="utf-8"), "html.parser")
    for d in soup.select("div.img-tab-wrapper"):
        d.decompose()
    return str(soup)


def test_the_ullr_empty_kit_shape_is_refused(root):
    ullr = wiki_parser.parse_god_page(_ullr_without_tabs())
    assert len(ullr["abilities"]) == 2
    problems = ne.god_problems(ullr)
    assert any("abilities read" in p for p in problems)
    assert any("Ullr/Merlin symptom" in p for p in problems)
    # The whole page, as recorded, is complete.
    assert ne.god_problems(wiki_parser.parse_god_page((REC / "page_ullr.html").read_text(encoding="utf-8"))) == []
    assert ne.god_problems(wiki_parser.parse_god_page((REC / "page_merlin.html").read_text(encoding="utf-8"))) == []


@pytest.mark.parametrize("override, why", [
    (_ullr_without_tabs, "incomplete: 2 abilities read"),
    (lambda: "<html><body><p>There is currently no text in this page.</p></body></html>",
     "does not parse"),
    (lambda: re.sub(r"Aspect of Victorious Conquest", "x", _page("Nike")).replace(
        "Pantheon", "Pxntheon"), "incomplete: no pantheon"),
])
def test_a_god_page_that_does_not_parse_cleanly_is_left_out(root, override, why):
    before = _tree(root)
    result = _run(root, fetcher=Fetcher({"Nike": override()}))
    assert {s["name"]: s["why"] for s in result["skipped"]}["Nike"].startswith(why)
    assert not (root / "Gods" / "Nike.md").exists()
    assert "Nike" not in [c["name"] for c in result["kept"]]
    # Everything else still went in, and nothing half-written of Nike's is anywhere.
    assert (root / "Gods" / "Hachiman.md").exists()
    assert not any("Nike" in k for k in set(_tree(root)) - set(before))


def test_an_item_page_without_stats_is_left_out(root):
    html = _page("Soul Locket")
    soup = BeautifulSoup(html, "html.parser")
    parsed = wiki_parser.parse_item_page(html)
    assert parsed["stats"]
    for k in parsed["stats"]:
        for node in soup.find_all(string=re.compile(re.escape(k))):
            node.replace_with("")
    stripped = str(soup)
    assert not wiki_parser.parse_item_page(stripped).get("stats")
    result = _run(root, fetcher=Fetcher({"Soul Locket": stripped}))
    assert "no stats" in {s["name"]: s["why"] for s in result["skipped"]}["Soul Locket"]
    assert not (root / "Items" / "Soul Locket.md").exists()
    assert "Soul Locket" not in _catalogue(root)["items"]


def test_an_unreachable_wiki_adds_nothing(root):
    class Down:
        def fetch(self, page):
            raise stats_refresh.SourceError(f"{page}: Cloudflare challenge (cf-mitigated=challenge)")
    before = _tree(root)
    assert _run(root, fetcher=Down())["status"] == "source-failed"
    assert _tree(root) == before


# -- the gate ------------------------------------------------------------------------

class Suite:
    """Fails `test_x` whenever `trigger` exists under the root."""

    def __init__(self, root, trigger, ids=("smite/tests/test_x.py::test_x",), crash=False):
        self.root, self.trigger, self.ids, self.crash = root, trigger, set(ids), crash
        self.calls = []

    def __call__(self, ids):
        on = (self.root / self.trigger).exists()
        self.calls.append((on, None if ids is None else sorted(ids)))
        if self.crash and on:
            raise RuntimeError("pytest wrote no report")
        failed = set(self.ids) if on else set()
        return failed if ids is None else failed & set(ids)


def test_a_failing_gate_keeps_that_entity_out_and_everything_else_in(root, monkeypatch, tmp_path):
    suite = Suite(root, "Items/Soul Locket.md", ids=["smite/tests/test_x.py::test_x", "gate:validate"])
    result = _run(root, checks=suite)
    assert result["status"] == "added"
    assert set(result["excluded"]) == {"Soul Locket"}
    assert "test_x" in result["excluded"]["Soul Locket"] and "gate:validate" in result["excluded"]["Soul Locket"]
    assert {c["name"] for c in result["kept"]} == set(NEW_GODS) | {"Lotus Sickle"}
    # Left out completely: no note, no catalogue entry, no back-link on its components.
    assert not (root / "Items" / "Soul Locket.md").exists()
    assert "Soul Locket" not in _catalogue(root)["items"]
    for comp in ("Soul Reliquary", "Flaming Pearl"):
        assert "Soul Locket" not in (ne.notes.read_note(root / "Items" / f"{comp}.md")[0].get("builds_into") or [])
    assert (root / "Items" / "Lotus Sickle.md").exists() and "Lotus Sickle" in _catalogue(root)["items"]
    log = json.loads((root / ne.LOG_FILE).read_text(encoding="utf-8"))
    assert log["last_run"]["excluded"][0]["name"] == "Soul Locket"
    assert "Soul Locket" not in {a["name"] for a in log["added"]}
    assert "::error::[new entities] left out Soul Locket" in ne.report(result)

    out = tmp_path / "gh_out"
    monkeypatch.setenv("GITHUB_OUTPUT", str(out))
    ne._github_outputs(result)
    assert out.read_text() == "rejected=true\n"


def test_a_failure_present_without_the_new_entities_does_not_block_them(root):
    calls = []

    def suite(ids):
        calls.append(ids)
        return {"smite/tests/test_x.py::already_red"} if ids is None else set(ids)

    result = _run(root, checks=suite)
    assert {c["name"] for c in result["kept"]} == set(NEW_GODS) | set(NEW_ITEMS)
    assert result["preexisting"] == ["smite/tests/test_x.py::already_red"]
    assert (root / "Gods" / "Nike.md").exists() and (root / "Items" / "Soul Locket.md").exists()


def test_a_failure_only_the_whole_set_causes_keeps_all_of_them_out(root):
    def suite(ids):
        together = (root / "Gods" / "Nike.md").exists() and (root / "Items" / "Lotus Sickle.md").exists()
        failed = {"smite/tests/test_x.py::t"} if together else set()
        return failed if ids is None else failed & set(ids)

    before = _tree(root)
    result = _run(root, checks=suite)
    assert result["status"] == "none-added" and result["kept"] == []
    assert set(result["excluded"]) == set(NEW_GODS) | set(NEW_ITEMS)
    after = _tree(root)
    # Only the roster file and the log moved.
    assert {k for k in set(after) | set(before) if after.get(k) != before.get(k)} == {"_roster.json", ne.LOG_FILE}


def test_a_gate_crash_puts_the_data_back_and_adds_nothing(root):
    before = _tree(root)
    result = _run(root, checks=Suite(root, "Gods/Nike.md", crash=True))
    assert result["status"] == "error" and result["kept"] == []
    after = _tree(root)
    assert {k for k in set(after) | set(before) if after.get(k) != before.get(k)} == {"_roster.json", ne.LOG_FILE}


def test_the_recompute_runs_on_each_tried_set(root):
    sets = []

    def recompute():
        sets.append(sorted(p.stem for p in (root / "Gods").glob("*.md") if p.stem in NEW_GODS))

    _run(root, checks=Suite(root, "Gods/Hel.md"), recompute=recompute)
    # all; old; each one alone; the kept set again.
    assert sets[0] == sorted(NEW_GODS) and sets[1] == []
    assert sets[-1] == sorted(["Nike", "Hachiman", "Kuzenbo"])


# -- re-running --------------------------------------------------------------------------

def test_a_re_run_adds_nothing_twice(root):
    first = _run(root)
    tree = _tree(root)
    second = _run(root)
    assert first["status"] == "added" and second["status"] == "nothing-new"
    changed = {k for k in set(tree) | set(_tree(root)) if tree.get(k) != _tree(root).get(k)}
    assert changed == {ne.LOG_FILE}
    text = (root / "_passive_classes.yaml").read_text(encoding="utf-8")
    assert text.count("\n  Lotus Sickle:") == 1
    log = json.loads((root / ne.LOG_FILE).read_text(encoding="utf-8"))
    assert sorted(a["name"] for a in log["added"]) == sorted(NEW_GODS + NEW_ITEMS)
    for comp in ("Ring of Dispel", "Mana Tome"):
        into = ne.notes.read_note(root / "Items" / f"{comp}.md")[0]["builds_into"]
        assert into.count("Lotus Sickle") == 1


def test_a_dry_run_writes_nothing(root):
    before = _tree(root)
    result = _run(root, dry_run=True)
    assert result["status"] == "dry-run"
    assert {n for _, n, _ in result["candidates"]} == set(NEW_GODS) | set(NEW_ITEMS)
    assert _tree(root) == before


# -- the community side ----------------------------------------------------------------------

class _Resp:
    def __init__(self, status):
        self.status_code = status


def _http_error(status):
    import requests
    return requests.HTTPError(f"{status}", response=_Resp(status))


def test_a_new_god_smitebrain_has_not_published_is_not_a_community_failure():
    fresh = {"builds": [{"source": "suggested"}]}
    had = {"builds": [{"source": "community"}, {"source": "suggested"}]}
    assert refresh._not_published_yet(_http_error(404), fresh)
    assert not refresh._not_published_yet(_http_error(404), had)
    assert not refresh._not_published_yet(_http_error(503), fresh)
