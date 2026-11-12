"""`aspect_agreement`: the target, the build the toggle shows, and the import
boundary. The committed store's figures move daily and are not pinned."""
import ast
from pathlib import Path

from smite import aspect_agreement as aa

PIPELINE = Path(__file__).resolve().parents[1]

NAMES = {c.lower(): c for c in "ABCDEFGHIJ"}
NAMES["component"] = "Component"
TIERS = {c: "3" for c in "ABCDEFGHIJ"}
TIERS["Component"] = "2"
ITEMS = {n: {"name": n, "tier": t, "stats": {"Strength": "10"}, "cost": 2500} for n, t in TIERS.items()}
GOD = {"name": "Testgod", "role": "Jungle", "damage_type": "physical"}


def _rec(items, aspect="aspect-of-x"):
    return {"aspect": aspect, "items": [i.lower() if i else None for i in items]}


def test_the_target_is_the_most_held_finished_items():
    records = [_rec("ABCDEF"), _rec("ABCDEG"), _rec(["A", "Component", None, "H", "I", "J"])]
    assert aa.aspect_target(records, NAMES, TIERS) == ["A", "B", "C", "D", "E", "F"]


def test_a_component_or_an_unknown_item_is_never_a_target():
    records = [_rec(["Component"] * 3 + ["A", "B", "Unknown"])] * 5
    assert aa.aspect_target(records, NAMES, TIERS) == ["A", "B"]


def test_an_item_held_twice_in_one_match_counts_once():
    records = [_rec("AAAAAB"), _rec("BCDEFG")]
    assert aa.aspect_target(records, NAMES, TIERS)[0] == "B"


def _note(aspect_build=None, shift=True, status="shown"):
    builds = [{"source": "suggested", "archetype": "core", "slot_order": list("ABCGHI")},
              {"source": "community", "slot_order": [{"name": n, "pick_rate": 0.5, "win_rate": 0.5}
                                                     for n in "ABCDEF"]}]
    if aspect_build:
        builds.append({"source": "suggested", "archetype": "core", "aspect": "Aspect of X",
                       "slot_order": list(aspect_build)})
    entry = {"aspect": "Aspect of X", "status": status, "windows": ["ob47"], "base_role": "Jungle"}
    if shift:
        entry["role_shift"] = {"role": "Mid", "share": 0.6}
    return {"builds": builds, "community_aspects": {"aspects": [entry]}}


STORED = {"ob47": [_rec("DEFGHJ")] * 40 + [_rec("ABCDEF", aspect=None)] * 40,
          "ob46": [_rec("ABCDEF")] * 40}
SLUGS = {"Aspect of X": "aspect-of-x"}


def _rows(note):
    return aa.aspect_rows(GOD, note, STORED, SLUGS, NAMES, TIERS, ITEMS)


def test_the_toggle_falls_back_to_the_base_build_when_no_aspect_build_ships():
    (row,) = _rows(_note())
    assert row["target"] == list("DEFGHJ") and row["matches"] == 40     # ob47, this aspect only
    assert row["ships_aspect_build"] is False
    assert row["shown"] == row["base"] == 2 / 6                          # G and H
    assert row["role_shift"] and row["played"] == "Mid"


def test_a_shipped_aspect_build_is_what_the_toggle_shows():
    (row,) = _rows(_note(aspect_build="DEFGHA"))
    assert row["ships_aspect_build"] and row["shown"] == 5 / 6 and row["base"] == 2 / 6


def test_the_base_build_is_also_read_against_the_gods_pooled_target():
    (row,) = _rows(_note())
    assert row["base_vs_pooled"] == 3 / 6                                # A, B, C of ABCDEF


def test_an_aspect_below_the_floor_is_left_out():
    assert _rows(_note(status="below minimum")) == []


def test_the_summary_groups_cover_every_row_once_per_split():
    rows = _rows(_note()) + _rows(_note(aspect_build="DEFGHA", shift=False))
    groups = dict(aa.summary(rows))
    assert len(groups["every shown aspect"]) == 2
    assert len(groups["played in another role"]) + len(groups["played in the base role"]) == 2
    assert len(groups["ships its own aspect build"]) == 1
    assert aa.report_lines(rows)[0].startswith("# Aspect agreement")


def test_nothing_in_the_model_imports_this():
    for mod in ("scoring", "assemble", "recommend", "build_index", "efficiency"):
        tree = ast.parse((PIPELINE / f"{mod}.py").read_text(encoding="utf-8"))
        names = {a.name for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))
                 for a in n.names}
        assert not names & {"aspect_agreement", "smite.aspect_agreement"}
