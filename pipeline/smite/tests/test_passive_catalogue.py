"""`data/_passive_classes.yaml` — the passive catalogue — held to the pool.

The catalogue is a hand-authored sidecar like `_tags.yaml`, and like the tags
it is only worth anything while it is COMPLETE: a buildable item whose passive
nobody has classified is exactly the item the next carve-out would miss. Three
things are pinned here, and each is a way the file could go quietly stale:

  * every god-agnostic buildable item with passive text has an entry, and the
    file names no item outside that set — a rename or a new item fails here
    rather than being silently uncatalogued;
  * every class code an entry uses is declared in the file's own vocabulary,
    with its family letter agreeing with the code;
  * an item's `priced` list agrees with what the SHIPPED pricing flags actually
    do to its stat line. This is the one that ties the document to the model:
    a carve-out that ships has to come here and say which clause it priced,
    and a `priced` claim about a clause nothing reprices is refused.

Reads the real data files rather than a fixture, because the claim being
tested is about the real pool. See docs/PASSIVES.md for the argument.

PATCH-PROOF BY CONSTRUCTION. Every check here is an invariant over whatever
`data/` holds, so a rebalance moves nothing; only a new buildable passive or a
passive REWRITTEN into a different shape needs the file touched. A rewrite is
a `variants:` entry chosen by a `match:` substring of the live text (see the
file's header), so the catalogue can be right on two patches at once — the one
on `main` and the one the daily job is about to bring in, which is what lets
`refresh-data.yml` gate a stats refresh on this suite. `test_reworked_*` below
holds both halves on the frozen Open Beta 40 items and on the live ones.
"""
import io

import yaml

from smite import build_quality, recommend, scoring

CATALOGUE_PATH = recommend.DATA_ROOT / "_passive_classes.yaml"


def _load():
    return yaml.safe_load(io.open(CATALOGUE_PATH, encoding="utf-8"))


def resolve(entry: dict, passive: str):
    """The classification that describes THIS text: the entry itself, or the
    one variant whose `match` occurs in it. None when no variant does — the
    text was reworked after the catalogue was written, i.e. uncatalogued."""
    variants = entry.get("variants")
    if not variants:
        return entry
    hits = [v for v in variants if v["match"] in (passive or "")]
    assert len(hits) <= 1, f"two variants match one text: {[v['match'] for v in hits]}"
    return hits[0] if hits else None


def _resolved(cat, items):
    by_name = {it["name"]: it for it in items}
    return {name: resolve(entry, (by_name.get(name) or {}).get("passive"))
            for name, entry in cat["items"].items()}


def _pool_with_passive(items):
    return {it["name"] for it in items
            if scoring.is_buildable(it) and (it.get("passive") or "").strip()}


def test_catalogue_covers_exactly_the_buildable_items_with_passive_text():
    cat = _load()
    items = recommend.load_items()
    pool = _pool_with_passive(items)
    entries = set(cat["items"])
    assert pool - entries == set(), f"uncatalogued: {sorted(pool - entries)}"
    assert entries - pool == set(), f"catalogued but not in the pool: {sorted(entries - pool)}"
    stale = sorted(n for n, e in _resolved(cat, items).items() if e is None)
    assert not stale, f"passive reworked, no variant describes the live text: {stale}"


def test_every_class_code_is_declared_and_carries_its_family_letter():
    cat = _load()
    vocabulary = cat["classes"]
    for code, spec in vocabulary.items():
        assert spec["family"] == code[0], f"{code} declares family {spec['family']}"
        assert spec.get("name") and spec.get("what")
    flat = []
    for name, entry in cat["items"].items():
        if entry.get("variants"):
            assert not entry.get("classes"), f"{name} has both variants and top-level classes"
            for v in entry["variants"]:
                assert v.get("match") and v.get("patch"), f"{name}: a variant needs match and patch"
                flat.append((f"{name} [{v['patch']}]", v))
        else:
            flat.append((name, entry))
    for name, entry in flat:
        classes = entry.get("classes") or []
        assert classes, f"{name} has no classes"
        unknown = [c for c in classes if c not in vocabulary]
        assert not unknown, f"{name} uses undeclared class(es) {unknown}"
        assert len(set(classes)) == len(classes), f"{name} repeats a class"
        for c in entry.get("priced") or []:
            assert c in classes, f"{name} prices {c} but does not list it"


def test_priced_clauses_agree_with_the_shipped_pricing_flags():
    cat = _load()
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    printed, priced = build_quality._stat_lines(items, weights)
    repriced = {n for n in printed if printed[n] != priced[n]}
    pool = _pool_with_passive(items)
    claimed = {n for n, e in _resolved(cat, items).items() if e and e.get("priced")}
    assert claimed == (repriced & pool), (
        f"claims pricing but the flags do not reprice: {sorted(claimed - repriced)}; "
        f"repriced by the flags but the catalogue does not say so: {sorted((repriced & pool) - claimed)}")


def test_reworked_passives_resolve_on_the_frozen_open_beta_40_items():
    """Each variant has to describe a text that existed. The Open Beta 40
    halves are checked against the frozen copy, so they keep being checked
    after `main` moves on and nothing live carries that text any more."""
    from smite.tests import frozen
    cat = _load()
    old = {it["name"]: it for it in frozen.items()}
    for name, entry in cat["items"].items():
        for v in entry.get("variants") or []:
            if v["patch"] == "Open Beta 40":
                assert resolve(entry, old[name].get("passive")) is v, name

