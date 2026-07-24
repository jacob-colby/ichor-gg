import json

from smite import snapshots


def test_snapshot_of_maps_names_to_cost_tier_stats():
    items = [
        {"name": "Deathbringer", "cost": 2900, "tier": 3, "stats": {"Strength": "45"}},
        {"name": "Cheapo", "cost": 900, "tier": "1", "stats": {"Strength": "10"}},
        {"cost": 100, "tier": 1, "stats": {}},  # no name -> excluded
    ]

    snap = snapshots.snapshot_of(items)

    assert snap == {
        "Deathbringer": {"cost": 2900, "tier": 3, "stats": {"Strength": "45"}},
        "Cheapo": {"cost": 900, "tier": "1", "stats": {"Strength": "10"}},
    }


def test_write_snapshot_creates_dated_json_and_load_snapshot_round_trips(tmp_path):
    items = [
        {"name": "Deathbringer", "cost": 2900, "tier": 3, "stats": {"Strength": "45"}},
    ]
    snapshots_dir = tmp_path / "snapshots"

    out_path = snapshots.write_snapshot(items, "2026-07-23", snapshots_dir=snapshots_dir)

    assert out_path == snapshots_dir / "2026-07-23.json"
    assert out_path.exists()

    on_disk = json.loads(out_path.read_text(encoding="utf-8"))
    assert on_disk == {
        "Deathbringer": {"cost": 2900, "tier": 3, "stats": {"Strength": "45"}},
    }

    loaded = snapshots.load_snapshot(out_path)
    assert loaded == on_disk


def test_diff_snapshots_reports_added_removed_changed():
    old = {
        "Deathbringer": {"cost": 2900, "tier": 3, "stats": {"Strength": "45"}},
        "Rangda's Mask": {"cost": 2300, "tier": 3, "stats": {"Magical Power": "80"}},
        "Unchanged": {"cost": 1000, "tier": 2, "stats": {"Health": "100"}},
        "Gone": {"cost": 700, "tier": 1, "stats": {"Physical Power": "10"}},
    }
    new = {
        "Deathbringer": {"cost": 3000, "tier": 3, "stats": {"Strength": "45"}},
        "Rangda's Mask": {"cost": 2300, "tier": 3, "stats": {"Magical Power": "90"}},
        "Unchanged": {"cost": 1000, "tier": 2, "stats": {"Health": "100"}},
        "NewItem": {"cost": 500, "tier": 1, "stats": {"Strength": "5"}},
    }

    diff = snapshots.diff_snapshots(old, new)

    assert diff["added"] == ["NewItem"]
    assert diff["removed"] == ["Gone"]
    assert diff["changed"] == [
        {"name": "Deathbringer", "cost": [2900, 3000]},
        {"name": "Rangda's Mask", "stats": {"Magical Power": ["80", "90"]}},
    ]


def test_diff_snapshots_identical_item_absent_from_changed():
    old = {"Same": {"cost": 500, "tier": 1, "stats": {"Health": "50"}}}
    new = {"Same": {"cost": 500, "tier": 1, "stats": {"Health": "50"}}}

    diff = snapshots.diff_snapshots(old, new)

    assert diff["changed"] == []
    assert diff["added"] == []
    assert diff["removed"] == []


def test_diff_snapshots_stat_added_or_removed_on_shared_item():
    old = {"Item": {"cost": 500, "tier": 1, "stats": {"Health": "50"}}}
    new = {"Item": {"cost": 500, "tier": 1, "stats": {"Health": "50", "Strength": "10"}}}

    diff = snapshots.diff_snapshots(old, new)

    assert diff["changed"] == [
        {"name": "Item", "stats": {"Strength": [None, "10"]}}
    ]
