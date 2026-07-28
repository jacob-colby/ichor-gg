import json

from smite import build_index, efficiency, notes


def _make_repo(tmp_path):
    (tmp_path / "data" / "Gods").mkdir(parents=True)
    (tmp_path / "data" / "Items").mkdir(parents=True)
    (tmp_path / "data" / "builds").mkdir(parents=True)
    return tmp_path


def test_build_index_collects_gods_items_builds(tmp_path):
    repo = _make_repo(tmp_path)
    notes.write_note(repo / "data" / "Gods" / "Chiron.md",
                      {"type": "smite-god", "name": "Chiron"}, "")
    notes.write_note(repo / "data" / "Items" / "Deathbringer.md",
                      {"type": "smite-item", "name": "Deathbringer"}, "")
    notes.write_note(repo / "data" / "builds" / "Chiron-Conquest.md",
                      {"type": "smite-build", "god": "Chiron"}, "")

    index = build_index.build_index(repo)

    # Gods gain a derived ability_order (see abilities.py) only when their kit
    # has levelable abilities. This note has no `abilities` key at all, so the
    # key is absent rather than a fabricated order of empty slots.
    assert index["gods"] == [{"type": "smite-god", "name": "Chiron"}]
    # Items are enriched with god-agnostic effect_tags + the efficiency verdict;
    # this note has no cost so it can't be scored (tier None, efficiency None —
    # never a fabricated zero) and has no tags entry ([]).
    assert index["items"] == [
        {"type": "smite-item", "name": "Deathbringer", "effect_tags": [],
         "efficiency_tier": None, "efficiency": None}
    ]
    assert index["builds"] == [{"type": "smite-build", "god": "Chiron"}]


def test_build_index_empty_folders_return_empty_lists(tmp_path):
    repo = _make_repo(tmp_path)
    index = build_index.build_index(repo)
    assert index == {"gods": [], "items": [], "builds": [], "starters": [],
                     "roster": [], "data_updated": "",
                     # Per-mode tier list (Task R2) — legacy top-level
                     # gods/items kept alongside the new conquest/joust map.
                     "tierlist": {"gods": [], "items": [],
                                  "conquest": {"gods": [], "items": []},
                                  "joust": {"gods": [], "items": []}},
                     "god_item_scores": {}, "draft": {},
                     # Provenance for the community figures — None until the
                     # god-index scrape has run, never an empty dict.
                     "community_source": None,
                     # Fitted marginal gold per stat — empty with no scorable
                     # items, never absent.
                     "item_gold_values": {},
                     "patch_notes": []}


def test_write_index_creates_json_file(tmp_path):
    repo = _make_repo(tmp_path)
    notes.write_note(repo / "data" / "Gods" / "Chiron.md",
                      {"type": "smite-god", "name": "Chiron"}, "")

    out_path = tmp_path / "viewer" / "public" / "index.json"
    build_index.write_index(repo, out_path)

    assert out_path.exists()
    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert data["gods"][0]["name"] == "Chiron"


def test_write_index_serializes_bare_yaml_dates(tmp_path):
    # An unquoted YAML date literal parses via yaml.safe_load as a real
    # datetime.date object, not a string — this is what crashed json.dumps
    # before the `default=str` fix (confirmed against the real
    # Chiron-Conquest.md note, which has an unquoted last_verified: date).
    # Passing a plain Python string into write_note doesn't reproduce this:
    # yaml.safe_dump auto-quotes date-shaped strings on write, so read_note
    # reads it back as a str, never a date object. Writing raw YAML text
    # with an unquoted date and reading it back via notes.read_note is what
    # actually reconstructs the date object that broke json.dumps.
    repo = _make_repo(tmp_path)
    god_path = repo / "data" / "Gods" / "Chiron.md"
    god_path.write_text(
        "---\nname: Chiron\nlast_verified: 2026-07-16\n---\n",
        encoding="utf-8",
    )

    out_path = tmp_path / "viewer" / "public" / "index.json"
    build_index.write_index(repo, out_path)  # must not raise

    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert data["gods"][0]["last_verified"] == "2026-07-16"


def test_write_index_copies_icon_files(tmp_path):
    repo = _make_repo(tmp_path)
    icons_dir = repo / "data" / "_assets" / "icons"
    icons_dir.mkdir(parents=True)
    (icons_dir / "chiron.png").write_bytes(b"\x89PNG\r\n\x1a\nfakeicondata")

    out_path = tmp_path / "viewer" / "public" / "index.json"
    build_index.write_index(repo, out_path)

    copied_icon = out_path.parent / "icons" / "chiron.png"
    assert copied_icon.exists()
    assert copied_icon.read_bytes() == b"\x89PNG\r\n\x1a\nfakeicondata"


def test_write_index_handles_no_icons_dir_gracefully(tmp_path):
    repo = _make_repo(tmp_path)
    out_path = tmp_path / "viewer" / "public" / "index.json"

    build_index.write_index(repo, out_path)  # must not raise, even with no _assets/icons/ at all

    assert out_path.exists()


def test_enrich_items_adds_tags_and_tier():
    from smite import build_index
    items = [
        {"name": "Deathbringer", "cost": 2900, "stats": {"Strength": "45"}},
        {"name": "Cheapo", "cost": 900, "stats": {"Strength": "45"}},
    ]
    tags = {"Deathbringer": ["burst"], "Cheapo": []}
    enriched = build_index._enrich_items(items, tags)
    by = {it["name"]: it for it in enriched}
    assert by["Deathbringer"]["effect_tags"] == ["burst"]
    assert by["Cheapo"]["effect_tags"] == []
    assert by["Cheapo"]["efficiency_tier"] in {"undervalued", "fair", "premium"}


def test_build_index_exports_starters(tmp_path, monkeypatch):
    from smite import build_index
    from pathlib import Path
    result = build_index.build_index(Path(__file__).resolve().parents[3])
    assert "starters" in result
    assert isinstance(result["starters"], list)


def test_build_index_adds_per_item_meta():
    from smite import build_index
    from pathlib import Path
    result = build_index.build_index(Path(__file__).resolve().parents[3])
    metaed = [i for i in result["items"] if i.get("meta")]
    assert metaed, "expected some items to carry community meta"
    for m in (i["meta"] for i in metaed):
        assert 0.0 <= m["win_avg"] <= 1.0
        # Exactly one denominator, and they mean different things: `matches`
        # is the item's real sample size from the index, `gods` the legacy
        # count of builds listing it — which is not a sample size at all.
        # Carrying both would invite reading the weaker one as the stronger.
        assert ("matches" in m) != ("gods" in m)
        assert m.get("matches", 1) >= 1 and m.get("gods", 1) >= 1
    # The index should be supplying most of them, not the legacy fallback.
    assert sum(1 for i in metaed if "matches" in i["meta"]) > len(metaed) // 2


def test_build_index_emits_data_updated_and_roster():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    assert "data_updated" in r and isinstance(r["data_updated"], str) and r["data_updated"]
    assert "roster" in r and isinstance(r["roster"], list)


def test_build_index_emits_tierlist_with_gods_and_items():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    assert "tierlist" in r
    tl = r["tierlist"]
    # Legacy top-level shape (pre-R2) plus the new per-mode map, additive.
    assert set(tl) == {"gods", "items", "conquest", "joust"}
    assert tl["gods"] and tl["items"]
    god = tl["gods"][0]
    assert {"name", "role", "damage_type", "ours", "community", "tier_ours", "tier_community"} <= set(god)
    item = tl["items"][0]
    assert {"name", "tier", "efficiency_tier", "ours", "community", "tier_ours", "tier_community"} <= set(item)
    # The invariant is that a missing score is left unranked, never bucketed.
    # This used to assert "some god has no community tier", which held only
    # while coverage was partial — the god index now covers every god, so
    # that proxy started failing on a genuine improvement. Test the rule.
    assert all((g["community"] is None) == (g["tier_community"] is None)
               for g in tl["gods"])
    # Joust is the stable case: the community source has no Joust data at all,
    # so none of those entries may carry an invented tier.
    assert all(g["tier_community"] is None for g in tl["joust"]["gods"])
    # Legacy top level mirrors Conquest exactly.
    assert tl["gods"] == tl["conquest"]["gods"]
    assert tl["items"] == tl["conquest"]["items"]


def test_build_index_emits_joust_tierlist_shaped_like_conquest():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    tl = r["tierlist"]
    assert set(tl["joust"]) == {"gods", "items"}
    assert tl["joust"]["gods"], "expected Joust gods ranking to be non-empty against real data"
    god = tl["joust"]["gods"][0]
    assert {"name", "role", "damage_type", "ours", "community", "tier_ours", "tier_community"} <= set(god)


def test_build_index_emits_patch_notes_as_list():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    assert "patch_notes" in r
    assert isinstance(r["patch_notes"], list)


def test_build_index_reads_snapshots_under_the_given_repo_root(tmp_path):
    # patch_notes must come from the repo being indexed, not the module-level
    # default store — otherwise tests silently depend on real accumulated data.
    from smite import build_index, snapshots
    snaps = tmp_path / "data" / "Analysis" / "snapshots"
    snaps.mkdir(parents=True)
    old = [{"name": "Rage", "cost": 2500, "tier": 3, "stats": {"Critical Chance": "20%"}}]
    new = [{"name": "Rage", "cost": 2500, "tier": 3, "stats": {"Critical Chance": "25%"}}]
    snapshots.write_snapshot(old, "2026-01-01", snaps)
    snapshots.write_snapshot(new, "2026-01-08", snaps)

    report = build_index.build_index(tmp_path)["patch_notes"]
    assert [p["to"] for p in report] == ["2026-01-08"]
    assert report[0]["changed"][0]["name"] == "Rage"
    assert report[0]["changed"][0]["verdict"] == "buff"


def test_build_index_emits_ability_order_for_every_god():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    # Gods whose kit scraped no levelable abilities (stance gods) legitimately
    # carry no key — better than a fabricated Basic-Attack/Passive order. Every
    # god that DOES have one must be well-formed, and most of the roster must.
    with_order = [g for g in r["gods"] if g.get("ability_order")]
    assert len(with_order) >= len(r["gods"]) - 5, "too many gods missing an order"
    for god in with_order:
        ao = god["ability_order"]
        assert len(ao["order"]) == 20
        assert set(ao["summary"]) == {"max_order", "ult_levels"}
        assert ao["summary"]["ult_levels"] == [5, 9, 13, 17]
        assert not any(s in ("Basic Attack", "Passive") for s in ao["order"])


def test_build_index_emits_capped_god_item_scores():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    scores = r["god_item_scores"]
    assert set(scores) == {g["name"] for g in r["gods"]}
    for god, table in scores.items():
        assert 0 < len(table) <= 40, f"{god} has {len(table)} entries"
        assert all(isinstance(v, float) for v in table.values())


# --- popular_items (Task P2: most-picked community items) -----------------

def test_popular_items_aggregates_across_slots_and_alternates():
    from smite import build_index
    build_entry = {
        "source": "community",
        "slot_order": [
            {"name": "A", "pick_rate": 0.5, "win_rate": 0.5,
             "alternates": [{"name": "B", "pick_rate": 0.2, "win_rate": 0.4}]},
            {"name": "C", "pick_rate": 0.3, "win_rate": 0.6},
        ],
    }
    result = build_index.popular_items(build_entry)
    assert {i["name"] for i in result} == {"A", "B", "C"}
    by_name = {i["name"]: i for i in result}
    assert by_name["B"] == {"name": "B", "pick_rate": 0.2, "win_rate": 0.4}


def test_popular_items_dedupes_by_name_keeping_highest_pick_rate():
    from smite import build_index
    # "A" is picked outright in one slot at a low rate, but shows up as a
    # higher-rate alternate in another slot — the alternate sighting wins.
    build_entry = {
        "source": "community",
        "slot_order": [
            {"name": "A", "pick_rate": 0.1, "win_rate": 0.50},
            {"name": "C", "pick_rate": 0.3, "win_rate": 0.6,
             "alternates": [{"name": "A", "pick_rate": 0.4, "win_rate": 0.55}]},
        ],
    }
    result = build_index.popular_items(build_entry)
    by_name = {i["name"]: i for i in result}
    assert by_name["A"] == {"name": "A", "pick_rate": 0.4, "win_rate": 0.55}


def test_popular_items_sorts_by_pick_rate_desc_then_name_asc():
    from smite import build_index
    build_entry = {
        "source": "community",
        "slot_order": [
            {"name": "Zeta", "pick_rate": 0.3, "win_rate": 0.5},
            {"name": "Alpha", "pick_rate": 0.3, "win_rate": 0.5},
            {"name": "Highest", "pick_rate": 0.9, "win_rate": 0.5},
        ],
    }
    result = build_index.popular_items(build_entry)
    assert [i["name"] for i in result] == ["Highest", "Alpha", "Zeta"]


def test_popular_items_is_deterministic_regardless_of_slot_order():
    from smite import build_index
    slots_a = [
        {"name": "A", "pick_rate": 0.3, "win_rate": 0.5},
        {"name": "B", "pick_rate": 0.3, "win_rate": 0.5},
    ]
    slots_b = list(reversed(slots_a))
    result_a = build_index.popular_items({"source": "community", "slot_order": slots_a})
    result_b = build_index.popular_items({"source": "community", "slot_order": slots_b})
    assert result_a == result_b


def test_popular_items_empty_when_no_slot_order():
    from smite import build_index
    assert build_index.popular_items({"source": "community"}) == []
    assert build_index.popular_items({"source": "community", "slot_order": []}) == []
    assert build_index.popular_items({}) == []


def test_build_index_attaches_popular_items_to_community_builds():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    agni = next(n for n in r["builds"] if n.get("god") == "Agni" and n.get("mode") == "Conquest")
    community = next(b for b in agni["builds"] if b.get("source") == "community")
    assert "popular_items" in community
    items = community["popular_items"]
    assert items, "expected Agni's community popular items to be non-empty"
    rates = [i["pick_rate"] for i in items]
    assert rates == sorted(rates, reverse=True)
    assert {"name", "pick_rate", "win_rate"} <= set(items[0])


def test_build_index_non_community_builds_get_no_popular_items(tmp_path):
    from smite import build_index, notes
    repo = _make_repo(tmp_path)
    notes.write_note(repo / "data" / "builds" / "Chiron-Conquest.md",
                      {"type": "smite-build", "god": "Chiron", "mode": "Conquest",
                       "builds": [{"source": "ours", "slot_order": ["Item A"]}]}, "")
    index = build_index.build_index(repo)
    b = index["builds"][0]["builds"][0]
    assert "popular_items" not in b


# --- data_patch (Task R1: scraped patch version) ---------------------------

def test_build_index_emits_data_patch_when_patch_file_exists(tmp_path):
    from smite import build_index
    repo = _make_repo(tmp_path)
    (repo / "data" / "_patch.json").write_text(
        json.dumps({"patch": "Open Beta 39", "captured": "2026-07-26"}), encoding="utf-8")

    index = build_index.build_index(repo)

    assert index["data_patch"] == "Open Beta 39"


def test_build_index_omits_data_patch_when_patch_file_absent(tmp_path):
    from smite import build_index
    repo = _make_repo(tmp_path)

    index = build_index.build_index(repo)

    assert "data_patch" not in index


def test_build_index_omits_data_patch_when_patch_file_is_malformed(tmp_path):
    from smite import build_index
    repo = _make_repo(tmp_path)
    (repo / "data" / "_patch.json").write_text("not valid json{{{", encoding="utf-8")

    index = build_index.build_index(repo)  # must not raise

    assert "data_patch" not in index


def test_build_index_community_build_with_no_slots_gets_empty_popular_items(tmp_path):
    from smite import build_index, notes
    repo = _make_repo(tmp_path)
    notes.write_note(repo / "data" / "builds" / "Chiron-Conquest.md",
                      {"type": "smite-build", "god": "Chiron", "mode": "Conquest",
                       "builds": [{"source": "community", "slot_order": []}]}, "")
    index = build_index.build_index(repo)
    b = index["builds"][0]["builds"][0]
    assert b["popular_items"] == []


def test_enrich_items_ships_the_models_working_not_just_its_label(tmp_path):
    """The regression's residual used to be computed and dropped, leaving the
    viewer able to say "Premium" but not by how much."""
    items = [
        {"name": "Cheap", "cost": 1000, "tier": 3, "stats": {"Strength": "60"}},
        {"name": "Dear", "cost": 4000, "tier": 3, "stats": {"Strength": "60"}},
        {"name": "Mid", "cost": 2500, "tier": 3, "stats": {"Strength": "60"}},
    ]
    out = build_index._enrich_items(items, {})
    for it in out:
        eff = it["efficiency"]
        assert eff is not None, it["name"]
        # The arithmetic a player reads has to close exactly.
        assert it["cost"] - eff["predicted_cost"] == eff["residual"]
        assert isinstance(eff["residual"], int)
        assert 0.0 <= eff["score"] <= 1.0
    by = {it["name"]: it["efficiency"] for it in out}
    # Cheaper than its stats predict => negative residual, and vice versa.
    assert by["Cheap"]["residual"] < 0 < by["Dear"]["residual"]


def test_enrich_items_leaves_unscored_items_null_rather_than_zero(tmp_path):
    """Tier-1 starters are passive-priced and sit out the fit; items with no
    numeric cost can't be scored at all. Neither may be given a fake verdict."""
    items = [
        {"name": "Starter", "cost": 700, "tier": 1, "stats": {"Strength": "10"}},
        {"name": "NoCost", "cost": None, "tier": 3, "stats": {"Strength": "10"}},
        {"name": "Real", "cost": 2500, "tier": 3, "stats": {"Strength": "60"}},
        {"name": "Real2", "cost": 2600, "tier": 3, "stats": {"Strength": "62"}},
    ]
    out = {it["name"]: it for it in build_index._enrich_items(items, {})}
    assert out["Starter"]["efficiency"] is None
    assert out["Starter"]["efficiency_tier"] is None
    assert out["NoCost"]["efficiency"] is None
    assert out["Real"]["efficiency"] is not None


def test_build_index_ships_the_fitted_gold_price_of_each_stat(tmp_path):
    """Without the per-stat prices a predicted cost is asserted, not auditable."""
    repo = _make_repo(tmp_path)
    (repo / "data" / "Items").mkdir(parents=True, exist_ok=True)
    for name, cost, stat in [("A", 1000, "30"), ("B", 2000, "60"), ("C", 3000, "90")]:
        (repo / "data" / "Items" / f"{name}.md").write_text(
            f"---\ntype: smite-item\nname: {name}\ncost: {cost}\ntier: 3\n"
            f"stats:\n  Strength: '{stat}'\n---\n", encoding="utf-8")
    index = build_index.build_index(repo)
    gold = index["item_gold_values"]
    assert "Strength" in gold
    assert gold["Strength"] > 0
    assert all(round(v, 2) == v for v in gold.values())


def test_receipt_rows_reconcile_to_predicted_cost(tmp_path):
    """The shop shows a per-stat receipt summing to `predicted_cost`. That only
    closes if the fit's intercept is shipped alongside the stat prices — without
    it every item's rows fall short by exactly the intercept."""
    repo = _make_repo(tmp_path)
    (repo / "data" / "Items").mkdir(parents=True, exist_ok=True)
    for name, cost, stat in [("A", 1200, "30"), ("B", 2400, "60"), ("C", 3300, "95")]:
        (repo / "data" / "Items" / f"{name}.md").write_text(
            f"---\ntype: smite-item\nname: {name}\ncost: {cost}\ntier: 3\n"
            f"stats:\n  Strength: '{stat}'\n---\n", encoding="utf-8")
    index = build_index.build_index(repo)
    gold = index["item_gold_values"]
    assert efficiency.INTERCEPT_KEY in gold, "the intercept must ship or no receipt adds up"

    for it in index["items"]:
        eff = it["efficiency"]
        if not eff:
            continue
        rows = gold[efficiency.INTERCEPT_KEY]
        for stat, raw in (it.get("stats") or {}).items():
            rows += float(raw) * gold.get(stat, 0.0)
        assert abs(rows - eff["predicted_cost"]) <= 1.5, (
            f"{it['name']}: receipt rows {rows:.1f} vs predicted {eff['predicted_cost']}")


def test_build_index_fits_the_regression_once(tmp_path, monkeypatch):
    """The tier list's item score and the per-item verdict have to come from the
    same fit; the module used to run it twice under a comment saying it didn't."""
    repo = _make_repo(tmp_path)
    (repo / "data" / "Items").mkdir(parents=True, exist_ok=True)
    for name, cost in [("A", 1000), ("B", 2000)]:
        (repo / "data" / "Items" / f"{name}.md").write_text(
            f"---\ntype: smite-item\nname: {name}\ncost: {cost}\ntier: 3\n"
            f"stats:\n  Strength: '30'\n---\n", encoding="utf-8")

    calls = {"n": 0}
    real = efficiency.efficiency_scores

    def counting(items):
        calls["n"] += 1
        return real(items)

    monkeypatch.setattr(efficiency, "efficiency_scores", counting)
    build_index.build_index(repo)
    assert calls["n"] == 1, f"regression fit {calls['n']} times, expected 1"
