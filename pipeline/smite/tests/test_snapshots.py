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


# ---------------------------------------------------------------------------
# classify_verdict
# ---------------------------------------------------------------------------

def test_classify_verdict_buff_when_stat_rises():
    entry = {"name": "Item", "stats": {"Strength": ["10", "20"]}}
    assert snapshots.classify_verdict(entry) == "buff"


def test_classify_verdict_nerf_when_stat_falls():
    entry = {"name": "Item", "stats": {"Strength": ["20", "10"]}}
    assert snapshots.classify_verdict(entry) == "nerf"


def test_classify_verdict_cost_rise_is_nerf_inverted():
    entry = {"name": "Item", "cost": [2500, 2900]}
    assert snapshots.classify_verdict(entry) == "nerf"


def test_classify_verdict_cost_fall_is_buff_inverted():
    entry = {"name": "Item", "cost": [2900, 2500]}
    assert snapshots.classify_verdict(entry) == "buff"


def test_classify_verdict_mixed_when_signals_disagree():
    entry = {
        "name": "Item",
        "stats": {"Strength": ["10", "20"], "Health": ["100", "80"]},
    }
    assert snapshots.classify_verdict(entry) == "mixed"


def test_classify_verdict_cost_and_stat_can_combine_to_mixed():
    # cost up = nerf signal, stat up = buff signal -> mixed
    entry = {"name": "Item", "cost": [2500, 2900], "stats": {"Strength": ["10", "20"]}}
    assert snapshots.classify_verdict(entry) == "mixed"


def test_classify_verdict_adjusted_when_no_parseable_signals():
    # tier-only change, no numeric stat/cost delta info to go on
    entry = {"name": "Item", "stats": {"Passive": ["Old text", "New text"]}}
    assert snapshots.classify_verdict(entry) == "adjusted"


def test_classify_verdict_percent_strings_parse():
    entry = {"name": "Item", "stats": {"Lifesteal": ["20%", "25%"]}}
    assert snapshots.classify_verdict(entry) == "buff"


def test_classify_verdict_percent_strings_parse_nerf():
    entry = {"name": "Item", "stats": {"Lifesteal": ["25%", "20%"]}}
    assert snapshots.classify_verdict(entry) == "nerf"


def test_classify_verdict_none_side_yields_no_signal():
    # stat added (old side None) -> no directional signal, only that one
    # stat present -> nothing else to go on -> adjusted
    entry = {"name": "Item", "stats": {"Strength": [None, "10"]}}
    assert snapshots.classify_verdict(entry) == "adjusted"


def test_classify_verdict_none_side_does_not_block_other_signals():
    entry = {
        "name": "Item",
        "stats": {"Strength": [None, "10"], "Health": ["100", "80"]},
    }
    assert snapshots.classify_verdict(entry) == "nerf"


# ---------------------------------------------------------------------------
# build_patch_report / report_from_dir
# ---------------------------------------------------------------------------

def _snap(cost, stat):
    return {"Item": {"cost": cost, "tier": 3, "stats": {"Strength": stat}}}


def test_build_patch_report_returns_empty_list_with_fewer_than_two_snapshots(tmp_path):
    snapshots_dir = tmp_path / "snapshots"
    assert snapshots.build_patch_report([], limit=5) == []

    one = snapshots.write_snapshot(
        [{"name": "Item", "cost": 2500, "tier": 3, "stats": {"Strength": "10"}}],
        "2026-07-01", snapshots_dir=snapshots_dir,
    )
    assert snapshots.build_patch_report([one], limit=5) == []


def test_build_patch_report_pairs_consecutive_snapshots_newest_first(tmp_path):
    snapshots_dir = tmp_path / "snapshots"
    items_a = [{"name": "Item", "cost": 2500, "tier": 3, "stats": {"Strength": "10"}}]
    items_b = [{"name": "Item", "cost": 2500, "tier": 3, "stats": {"Strength": "20"}}]
    items_c = [{"name": "Item", "cost": 2500, "tier": 3, "stats": {"Strength": "5"}}]

    p1 = snapshots.write_snapshot(items_a, "2026-07-01", snapshots_dir=snapshots_dir)
    p2 = snapshots.write_snapshot(items_b, "2026-07-08", snapshots_dir=snapshots_dir)
    p3 = snapshots.write_snapshot(items_c, "2026-07-15", snapshots_dir=snapshots_dir)

    report = snapshots.build_patch_report([p2, p1, p3], limit=5)

    assert [p["from"] for p in report] == ["2026-07-08", "2026-07-01"]
    assert [p["to"] for p in report] == ["2026-07-15", "2026-07-08"]


def test_build_patch_report_respects_limit(tmp_path):
    snapshots_dir = tmp_path / "snapshots"
    paths = []
    for i, date in enumerate(["2026-07-01", "2026-07-08", "2026-07-15", "2026-07-22"]):
        items = [{"name": "Item", "cost": 2500 + i, "tier": 3, "stats": {"Strength": "10"}}]
        paths.append(snapshots.write_snapshot(items, date, snapshots_dir=snapshots_dir))

    report = snapshots.build_patch_report(paths, limit=2)

    assert len(report) == 2
    assert report[0]["to"] == "2026-07-22"
    assert report[1]["to"] == "2026-07-15"


def test_build_patch_report_surfaces_added_and_removed(tmp_path):
    snapshots_dir = tmp_path / "snapshots"
    old_items = [{"name": "Gone", "cost": 700, "tier": 1, "stats": {"Strength": "10"}}]
    new_items = [{"name": "NewItem", "cost": 500, "tier": 1, "stats": {"Strength": "5"}}]

    p1 = snapshots.write_snapshot(old_items, "2026-07-01", snapshots_dir=snapshots_dir)
    p2 = snapshots.write_snapshot(new_items, "2026-07-08", snapshots_dir=snapshots_dir)

    report = snapshots.build_patch_report([p1, p2], limit=5)

    assert report[0]["added"] == ["NewItem"]
    assert report[0]["removed"] == ["Gone"]


def test_build_patch_report_changed_entries_carry_verdict(tmp_path):
    snapshots_dir = tmp_path / "snapshots"
    old_items = [{"name": "Item", "cost": 2500, "tier": 3, "stats": {"Strength": "10"}}]
    new_items = [{"name": "Item", "cost": 2500, "tier": 3, "stats": {"Strength": "20"}}]

    p1 = snapshots.write_snapshot(old_items, "2026-07-01", snapshots_dir=snapshots_dir)
    p2 = snapshots.write_snapshot(new_items, "2026-07-08", snapshots_dir=snapshots_dir)

    report = snapshots.build_patch_report([p1, p2], limit=5)

    assert report[0]["changed"] == [
        {"name": "Item", "stats": {"Strength": ["10", "20"]}, "verdict": "buff"}
    ]


def test_build_patch_report_changed_sorted_by_name(tmp_path):
    snapshots_dir = tmp_path / "snapshots"
    old_items = [
        {"name": "Zeta", "cost": 2500, "tier": 3, "stats": {"Strength": "10"}},
        {"name": "Alpha", "cost": 1500, "tier": 2, "stats": {"Strength": "10"}},
    ]
    new_items = [
        {"name": "Zeta", "cost": 2500, "tier": 3, "stats": {"Strength": "20"}},
        {"name": "Alpha", "cost": 1500, "tier": 2, "stats": {"Strength": "5"}},
    ]

    p1 = snapshots.write_snapshot(old_items, "2026-07-01", snapshots_dir=snapshots_dir)
    p2 = snapshots.write_snapshot(new_items, "2026-07-08", snapshots_dir=snapshots_dir)

    report = snapshots.build_patch_report([p1, p2], limit=5)

    assert [c["name"] for c in report[0]["changed"]] == ["Alpha", "Zeta"]


def test_report_from_dir_globs_json_files_in_snapshots_dir(tmp_path):
    snapshots_dir = tmp_path / "snapshots"
    old_items = [{"name": "Item", "cost": 2500, "tier": 3, "stats": {"Strength": "10"}}]
    new_items = [{"name": "Item", "cost": 2500, "tier": 3, "stats": {"Strength": "20"}}]
    snapshots.write_snapshot(old_items, "2026-07-01", snapshots_dir=snapshots_dir)
    snapshots.write_snapshot(new_items, "2026-07-08", snapshots_dir=snapshots_dir)

    report = snapshots.report_from_dir(snapshots_dir=snapshots_dir, limit=5)

    assert len(report) == 1
    assert report[0]["from"] == "2026-07-01"
    assert report[0]["to"] == "2026-07-08"


def test_report_from_dir_empty_when_dir_missing(tmp_path):
    missing_dir = tmp_path / "does-not-exist"
    assert snapshots.report_from_dir(snapshots_dir=missing_dir, limit=5) == []


# -- write_snapshot_if_changed -----------------------------------------------
#
# The scheduled job pulls SmiteBrain only, and item cost/tier/stats are wiki
# data. An unconditional daily write banks a byte-identical file every morning;
# build_patch_report diffs consecutive pairs and keeps 5, so five quiet days
# push every real change off the report and leave the page reading "Items have
# moved 0 times across 5 refreshes".

ITEMS_A = [{"name": "Deathbringer", "cost": 2900, "tier": 3, "stats": {"Strength": "45"}}]
ITEMS_B = [{"name": "Deathbringer", "cost": 2700, "tier": 3, "stats": {"Strength": "45"}}]


def test_write_if_changed_banks_the_first_snapshot(tmp_path):
    out = snapshots.write_snapshot_if_changed(ITEMS_A, "2026-01-01", tmp_path / "snaps")
    assert out == tmp_path / "snaps" / "2026-01-01.json"


def test_write_if_changed_is_a_no_op_when_item_stats_did_not_move(tmp_path):
    snaps = tmp_path / "snaps"
    snapshots.write_snapshot(ITEMS_A, "2026-01-01", snaps)

    assert snapshots.write_snapshot_if_changed(ITEMS_A, "2026-01-02", snaps) is None
    assert [p.name for p in sorted(snaps.glob("*.json"))] == ["2026-01-01.json"]


def test_write_if_changed_banks_when_a_cost_moves(tmp_path):
    snaps = tmp_path / "snaps"
    snapshots.write_snapshot(ITEMS_A, "2026-01-01", snaps)

    out = snapshots.write_snapshot_if_changed(ITEMS_B, "2026-01-02", snaps)

    assert out == snaps / "2026-01-02.json"
    assert snapshots.load_snapshot(out)["Deathbringer"]["cost"] == 2700


def test_a_quiet_week_leaves_one_period_on_the_report(tmp_path):
    """The whole point. Seven days of an unchanged item table must still leave
    the day the cost moved as the newest period, not bury it under six empty
    ones."""
    snaps = tmp_path / "snaps"
    snapshots.write_snapshot(ITEMS_A, "2026-01-01", snaps)
    snapshots.write_snapshot_if_changed(ITEMS_B, "2026-01-02", snaps)
    for day in range(3, 10):
        snapshots.write_snapshot_if_changed(ITEMS_B, f"2026-01-{day:02d}", snaps)

    report = snapshots.report_from_dir(snaps)

    assert len(report) == 1
    assert (report[0]["from"], report[0]["to"]) == ("2026-01-01", "2026-01-02")
    assert report[0]["changed"][0]["verdict"] == "buff"


def test_a_re_run_on_the_same_day_compares_against_the_day_before(tmp_path):
    """A workflow_dispatch re-run must not compare today against itself and
    conclude nothing moved."""
    snaps = tmp_path / "snaps"
    snapshots.write_snapshot(ITEMS_A, "2026-01-01", snaps)
    snapshots.write_snapshot_if_changed(ITEMS_B, "2026-01-02", snaps)

    out = snapshots.write_snapshot_if_changed(ITEMS_B, "2026-01-02", snaps)

    assert out == snaps / "2026-01-02.json"
    assert snapshots.load_snapshot(out)["Deathbringer"]["cost"] == 2700


def test_a_same_day_re_run_that_reverts_removes_the_redundant_file(tmp_path):
    """Leaving it would put two identical snapshots next to each other, which
    is the empty period this function exists to prevent."""
    snaps = tmp_path / "snaps"
    snapshots.write_snapshot(ITEMS_A, "2026-01-01", snaps)
    snapshots.write_snapshot_if_changed(ITEMS_B, "2026-01-02", snaps)

    assert snapshots.write_snapshot_if_changed(ITEMS_A, "2026-01-02", snaps) is None
    assert [p.name for p in sorted(snaps.glob("*.json"))] == ["2026-01-01.json"]
    assert snapshots.report_from_dir(snaps) == []


def test_latest_snapshot_path_is_none_on_an_empty_store(tmp_path):
    assert snapshots.latest_snapshot_path(tmp_path / "nope") is None


# ---------------------------------------------------------------------------
# Patch labels, highlights and official links
# ---------------------------------------------------------------------------

def _write(snapshots_dir, date, items):
    return snapshots.write_snapshot(
        [{"name": n, **v} for n, v in items.items()], date, snapshots_dir=snapshots_dir)


def test_patch_at_picks_label_current_on_the_day():
    hist = [{"patch": "Open Beta 40", "first_seen": "2026-08-01"},
            {"patch": "Open Beta 41", "first_seen": "2026-08-15"}]
    assert snapshots.patch_at(hist, "2026-07-31") is None
    assert snapshots.patch_at(hist, "2026-08-01") == "Open Beta 40"
    assert snapshots.patch_at(hist, "2026-08-14") == "Open Beta 40"
    assert snapshots.patch_at(hist, "2026-09-01") == "Open Beta 41"


def test_record_patch_appends_only_on_a_new_label(tmp_path):
    path = tmp_path / "_patch_history.json"
    assert snapshots.record_patch("Open Beta 40", "2026-08-01", path) is True
    assert snapshots.record_patch("Open Beta 40", "2026-08-09", path) is False
    assert snapshots.record_patch("Open Beta 41", "2026-08-15", path) is True
    assert [r["patch"] for r in json.loads(path.read_text())] == ["Open Beta 40", "Open Beta 41"]


def test_record_patch_does_not_read_the_current_label_as_history(tmp_path):
    # refresh writes _patch.json first; a fallback read would see the new
    # label as already recorded and never write it.
    (tmp_path / "_patch.json").write_text(json.dumps({"patch": "Open Beta 41", "captured": "2026-08-15"}))
    assert snapshots.record_patch("Open Beta 41", "2026-08-15", tmp_path / "_patch_history.json") is True


def test_load_patch_history_falls_back_to_current_label(tmp_path):
    (tmp_path / "_patch.json").write_text(json.dumps({"patch": "Open Beta 40", "captured": "2026-08-01"}))
    assert snapshots.load_patch_history(tmp_path / "_patch_history.json") == [
        {"patch": "Open Beta 40", "first_seen": "2026-08-01"}]


def test_period_within_one_patch_does_not_highlight_additions(tmp_path):
    d = tmp_path / "snapshots"
    p1 = _write(d, "2026-08-01", {"A": {"cost": 100, "tier": 1, "stats": {}}})
    p2 = _write(d, "2026-08-29", {"A": {"cost": 100, "tier": 1, "stats": {}},
                                   "Axe": {"cost": 600, "tier": 1, "stats": {}}})
    hist = [{"patch": "Open Beta 40", "first_seen": "2026-08-01"}]
    [period] = snapshots.build_patch_report([p1, p2], history=hist)
    assert period["crosses_patch"] is False
    assert period["patch_from"] == period["patch_to"] == "Open Beta 40"
    assert period["added"] == ["Axe"]
    assert period["highlights"] == []


def test_highlights_rank_removed_then_added_then_by_relative_move(tmp_path):
    d = tmp_path / "snapshots"
    old = {
        "Small": {"cost": 3000, "tier": 3, "stats": {"Strength": "40"}},     # 40->42: 5%
        "Big": {"cost": 3000, "tier": 3, "stats": {"Strength": "20"}},       # 20->30: 50%
        "Pricier": {"cost": 2000, "tier": 3, "stats": {"Strength": "40"}},   # cost +25%
        "Reworded": {"cost": 2000, "tier": 3, "stats": {"Passive": "a"}},    # adjusted
        "Gone": {"cost": 2000, "tier": 3, "stats": {}},
    }
    new = {k: dict(v) for k, v in old.items() if k != "Gone"}
    new["Small"] = {"cost": 3000, "tier": 3, "stats": {"Strength": "42"}}
    new["Big"] = {"cost": 3000, "tier": 3, "stats": {"Strength": "30"}}
    new["Pricier"] = {"cost": 2500, "tier": 3, "stats": {"Strength": "40"}}
    new["Reworded"] = {"cost": 2000, "tier": 3, "stats": {"Passive": "b"}}
    new["Fresh"] = {"cost": 2800, "tier": 3, "stats": {}}
    p1, p2 = _write(d, "2026-08-01", old), _write(d, "2026-08-15", new)
    hist = [{"patch": "Open Beta 40", "first_seen": "2026-08-01"},
            {"patch": "Open Beta 41", "first_seen": "2026-08-15"}]
    [period] = snapshots.build_patch_report([p1, p2], history=hist)
    assert period["crosses_patch"] is True
    hl = period["highlights"]
    assert [(h["name"], h["change"]) for h in hl] == [
        ("Gone", "removed"), ("Fresh", "added"),
        ("Big", "buff"), ("Pricier", "nerf"), ("Small", "buff")]
    assert hl[2]["headline"] == "Strength 20 → 30"
    assert hl[3]["headline"] == "Cost 2000 → 2500"
    assert all(h["group"] == "items" for h in hl)
    mixed = {"name": "M", "stats": {"Mana": ["200", "250"], "Intelligence": ["70", "65"]}}
    assert snapshots.change_magnitude(mixed)[1] == "Mana 200 \u2192 250 (+1 more)"
    assert "official_url" not in period


def test_highlights_cap_at_limit():
    period = {"removed": [f"R{i}" for i in range(8)], "added": [], "changed": [],
              "crosses_patch": True}
    assert len(snapshots.highlights_for(period)) == snapshots.HIGHLIGHT_LIMIT


def test_official_url_only_on_crossing_period_and_only_official_hosts(tmp_path):
    (tmp_path / "_patch_links.yaml").write_text(
        "links:\n"
        "  Open Beta 41: https://www.smite2.com/news/ob41\n"
        "  Open Beta 40: https://wiki.smite2.com/w/SMITE_2_Open_Beta_40\n")
    links = snapshots.load_patch_links(tmp_path / "_patch_links.yaml")
    assert links == {"Open Beta 41": "https://www.smite2.com/news/ob41"}
    assert not snapshots.is_official_url("http://www.smite2.com/x")
    assert not snapshots.is_official_url("https://smite2.com.evil.example/x")

    d = tmp_path / "snapshots"
    a = {"A": {"cost": 100, "tier": 1, "stats": {"Strength": "1"}}}
    b = {"A": {"cost": 100, "tier": 1, "stats": {"Strength": "2"}}}
    p1, p2, p3 = _write(d, "2026-08-01", a), _write(d, "2026-08-10", b), _write(d, "2026-08-20", a)
    hist = [{"patch": "Open Beta 40", "first_seen": "2026-08-01"},
            {"patch": "Open Beta 41", "first_seen": "2026-08-15"}]
    newer, older = snapshots.build_patch_report([p1, p2, p3], history=hist, links=links)
    assert newer["official_url"] == "https://www.smite2.com/news/ob41"
    assert "official_url" not in older


def test_shipped_store_has_no_patch_crossing_yet():
    # Pins the 2026-11-02 diagnosis: the one stored period is a data-coverage
    # catch-up inside Open Beta 40, so it must not present additions as new.
    report = snapshots.report_from_dir()
    if not report:
        return
    oldest = report[-1]
    if oldest["from"] == "2026-08-01" and oldest["to"] == "2026-08-29":
        assert oldest["crosses_patch"] is False
        assert oldest["highlights"] == []
