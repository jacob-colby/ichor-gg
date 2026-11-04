"""The model audit harness: checks the scoring model as a whole system.

    python -m smite.model_audit reference            # frozen builds + verdicts: exit 1 on any change
    python -m smite.model_audit reference --write    # accept the change (say why in the PR)
    python -m smite.model_audit reference --refreeze # re-capture the frozen INPUTS too (rare)
    python -m smite.model_audit heldout              # validate metrics, tuning vs held-out, delta vs main
    python -m smite.model_audit passives             # which recommended passives never fire (~1 min)
    python -m smite.model_audit coverage             # what the model simulates, as a committed file
    python -m smite.model_audit sensitivity          # SLOW (~12 min): +/-20% on each major weight
    python -m smite.model_audit all [--slow]         # every report; --slow adds sensitivity

WHY (2026-11-03, Jacob). The fixes of that day — the Joust wave-clear
penalty, healing in the fight, the anti-heal retune, Lotus Sickle's held
tag, the Lifesteal fit weight — were each found by looking at ONE god. This
module looks at all of them at once, so a gap is found by a count rather
than by luck. IT CHANGES NOTHING: every subcommand reads the model and
writes a report. Nothing in `scoring`, `assemble`, `recommend` or
`build_index` imports it.

THE FIVE PARTS, and what each one does and does not claim:

1. REFERENCE BUILDS (`REFERENCE_GODS`, two per role). Every suggested build
   and the side-by-side verdict of the `model` build, in all three modes, for
   ten gods, recomputed on FROZEN inputs (`tests/fixtures/frozen/reference/`:
   the item pool, the ten god notes, their Conquest community entries, the
   side-by-side targets and the per-mode stack clock, captured 2026-11-03 on
   Open Beta 47) with the LIVE code, `_weights.yaml` and `_tags.yaml`. So the
   snapshot moves when the MODEL moves and never when the data refreshes —
   which matters because `stats_gate` rejects a wiki refresh that turns any
   test red (STATE.md §6, "The test gate"); a snapshot over live data would
   block every patch. `test_model_audit.py` fails on any change; the PR that
   changes it runs `reference --write` and explains the diff.

2. HELD-OUT CHECK (`split_of`). Gods split by a hash of the NAME, 30% held
   out, so the split is the same on every machine and a new god never moves
   an old one. `heldout` prints `validate`'s win-weighted coverage and pooled
   Spearman on both halves, and the same for `--base` (default `origin/main`)
   run in a git worktree on THIS tree's data (Gods, Items, builds) so the
   delta is the code and config, not the daily refresh. Read with STATE.md
   §1 in mind: both metrics have a model INPUT as their target, so the held-out
   half guards against fitting a change to the gods it was looked at on — it
   is not a leakage-free measure; `calibrate` is that.

3. PASSIVE FIRING (`passive_firing`). Every recommended build in every mode,
   from the shipped build notes, run through `side_by_side.power` with each
   simulated passive's hooks wrapped and counted: a hook FIRES when it changed
   the fight (a hit, a heal, a stack, a protection, a multiplier, a stat). A
   recommended item whose simulated passive never fires for that god, or
   whose not-simulated passive needs a capability the kit lacks
   (`kit_fit.item_needs`, the Lotus Sickle class), is listed. Report only.

4. WEIGHT SENSITIVITY (`NUDGES`, slow). Each major weight x0.8 and x1.2, every
   god's base-kit core and model rebuilt in all three modes, and the
   side-by-side verdict of every model build that changed re-judged. A
   verdict that flips under any nudge is FRAGILE.

5. COVERAGE (`coverage`). Share of buildable items whose passive is
   simulated, gods whose kit heals are simulated, aspects tuned and aspects
   simulated — written to `viewer/public/model_coverage.json` for the site and
   `data/Analysis/_model_coverage.md`.

The sanity invariants (stats never fall when an item is added, power rises
2 -> 4 -> 6, nothing NaN or accidentally zero, modes differ only through the
`modes` block) are tests, in `tests/test_model_audit.py`, on the frozen inputs.
"""
import argparse
import copy
import dataclasses
import hashlib
import json
import math
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from contextlib import contextmanager
from datetime import date
from pathlib import Path
from unittest import mock

from smite import (ability_heals, build_quality as bq, efficiency, kit_fit, passive_sim,
                   recommend, scoring, side_by_side as sbs, validate)

REPO_ROOT = Path(__file__).resolve().parents[2]
ANALYSIS = REPO_ROOT / "data" / "Analysis"
FROZEN = Path(__file__).resolve().parent / "tests" / "fixtures" / "frozen" / "reference"
SNAPSHOT_PATH = FROZEN / "snapshot.json"
COVERAGE_JSON = REPO_ROOT / "viewer" / "public" / "model_coverage.json"
MODES = tuple(recommend.MODES)

#: Two per primary role (`build_quality.primary_role`). Chosen 2026-11-03 to
#: span the verdict classes the side-by-side gives on OB47 (Ichor better,
#: community better, level, early-game, withheld, aspect not simulated) and to
#: hold the gods the day's one-god fixes were found on (Agni: Lotus Sickle in
#: Joust; Cernunnos: an aspect-tuned carry; Ymir and Atlas: Supports, where the
#: Lifesteal weight landed).
REFERENCE_GODS = {
    "Carry": ("Artemis", "Cernunnos"),
    "Mid": ("Agni", "Zeus"),
    "Solo": ("Bellona", "Chaac"),
    "Jungle": ("Fenrir", "Thanatos"),
    "Support": ("Atlas", "Ymir"),
}


def reference_names():
    return [n for pair in REFERENCE_GODS.values() for n in pair]


# ── Shared ────────────────────────────────────────────────────────────────

@contextmanager
def pricing(weights):
    """The pricing flags `_weights.yaml` turns on, for the duration."""
    before = efficiency.apply_pricing_flags(weights)
    try:
        yield
    finally:
        efficiency.restore_pricing_flags(before)


def entry_label(e):
    return e["archetype"] + (f" @ {e['aspect']}" if e.get("aspect") else "")


def community_only(note):
    return {"builds": [b for b in (note or {}).get("builds") or [] if b.get("source") == "community"]}


@contextmanager
def mode_rules(mode, minutes_per_item=None, weights=None, builds=None, items_by_name=None, gods=None):
    """`side_by_side.use_mode`, with the stack clock either derived (live
    roster) or given (frozen)."""
    um = sbs.use_mode(mode, weights if minutes_per_item is None else None, builds, items_by_name, gods)
    if minutes_per_item is not None and mode != "Conquest":
        um.values["MINUTES_PER_ITEM"] = minutes_per_item
    with um:
        yield


def verdict_for(god, conquest_note, entries, items_by_name, targets, view, mode, weights):
    """The side-by-side verdict of `entries`' model build in `mode` (the
    caller has set the mode's rules). Returns `(verdict, unwithheld)` or
    `(None, reason)`."""
    if mode == "Conquest":
        note = {"builds": community_only(conquest_note)["builds"] + list(entries)}
        row, why = sbs.compare(god, note, items_by_name, targets, view.rows(god, conquest_note))
    else:
        excluded = frozenset(((weights.get("modes") or {}).get(mode.lower()) or {})
                             .get("excluded_items") or ())
        row, why = sbs.compare(god, conquest_note, items_by_name, targets,
                               view.rows(god, {"builds": []}, mode), {"builds": list(entries)},
                               excluded)
    if row is None:
        return None, why
    return row["verdict"], row["verdict_unwithheld"]


# ── 1. Reference builds ───────────────────────────────────────────────────

def load_frozen(root=FROZEN):
    read = lambda n: json.loads((root / n).read_text(encoding="utf-8"))
    return {"items": read("items.json"), "gods": read("gods.json"),
            "notes": read("conquest_notes.json"), "context": read("context.json")}


def refreeze(root=FROZEN):
    """Capture the frozen inputs from the live data. Run only on purpose —
    a refreeze moves the snapshot for a reason that is not the model."""
    items, gods, weights, tags_map, builds = sbs.load_inputs()
    names = reference_names()
    by_name = {g["name"]: g for g in gods}
    missing = [n for n in names if n not in by_name]
    if missing:
        raise SystemExit(f"reference gods not tracked: {missing}")
    ibn = {it["name"]: it for it in items}
    mpi = {m: sbs.mode_minutes_per_item(m, weights, builds, ibn, gods) for m in MODES if m != "Conquest"}
    # The targets read the mode's rules (the attacker's window), so one per mode.
    targets = {}
    for m in MODES:
        with mode_rules(m, None, weights, builds, ibn, gods):
            targets[m] = sbs.reference_targets(gods, builds, ibn)
    root.mkdir(parents=True, exist_ok=True)
    dump = lambda n, v: (root / n).write_text(json.dumps(v, indent=1, sort_keys=True, default=_finite)
                                              + "\n", encoding="utf-8")
    dump("items.json", items)
    dump("gods.json", {n: by_name[n] for n in names})
    dump("conquest_notes.json", {n: community_only(builds.get(n)) for n in names})
    dump("context.json", {"targets": targets, "minutes_per_item": mpi, "data_patch": sbs.data_patch(),
                          "frozen_on": date.today().isoformat()})


def _finite(x):
    if isinstance(x, float) and not math.isfinite(x):
        return str(x)
    if isinstance(x, (set, frozenset, tuple)):
        return list(x)
    raise TypeError(type(x))


def _targets(ctx):
    def fix(v):
        if isinstance(v, dict):
            return {k: fix(x) for k, x in v.items()}
        if v in ("inf", "-inf", "nan"):
            return float(v)
        return v
    return fix(ctx["targets"])


def compute_reference(frozen=None, weights=None, tags_map=None):
    """`{god: {role, <mode>: {builds: {label: [items]}, verdict, verdict_unwithheld}}}`."""
    frozen = frozen or load_frozen()
    weights = weights if weights is not None else scoring.load_weights(recommend.WEIGHTS_PATH)
    tags_map = tags_map if tags_map is not None else scoring.load_tags(recommend.TAGS_PATH)
    items = frozen["items"]
    ibn = {it["name"]: it for it in items}
    notes = frozen["notes"]
    targets_by_mode = _targets(frozen["context"])
    mpi = frozen["context"]["minutes_per_item"]

    def borrowed(name, mode="Conquest"):
        return copy.deepcopy(notes.get(name)) if mode == "Conquest" else {"builds": []}

    out = {}
    with pricing(weights), mock.patch.object(recommend, "load_build_note", borrowed):
        view = sbs.ModelView(items, weights, tags_map)
        for name in reference_names():
            god = frozen["gods"][name]
            row = {"role": bq.primary_role(god)}
            for mode in MODES:
                god_build = notes[name] if mode == "Conquest" else {"builds": []}
                entries = recommend.build_suggested_entries(god, items, god_build, weights, tags_map, mode)
                with mode_rules(mode, mpi.get(mode)):
                    v, unw = verdict_for(god, notes[name], entries, ibn, targets_by_mode[mode], view,
                                         mode, weights)
                row[mode] = {"builds": {entry_label(e): list(e["slot_order"]) for e in entries},
                             "verdict": v if v is not None else f"no verdict: {unw}",
                             "verdict_unwithheld": unw if v is not None else None}
            out[name] = row
    return out


def diff_reference(old, new):
    """Human-readable lines for every build or verdict that changed."""
    lines = []
    for god in sorted(set(old) | set(new)):
        a, b = old.get(god), new.get(god)
        if a is None or b is None:
            lines.append(f"{god}: {'added' if a is None else 'removed'}")
            continue
        for mode in MODES:
            ma, mb = a.get(mode) or {}, b.get(mode) or {}
            for key in ("verdict", "verdict_unwithheld"):
                if ma.get(key) != mb.get(key):
                    lines.append(f"{god} / {mode} {key}: {ma.get(key)} -> {mb.get(key)}")
            ba, bb = ma.get("builds") or {}, mb.get("builds") or {}
            for label in sorted(set(ba) | set(bb)):
                x, y = ba.get(label), bb.get(label)
                if x == y:
                    continue
                if x is None or y is None:
                    lines.append(f"{god} / {mode} / {label}: {'new build' if x is None else 'build gone'}")
                    continue
                gone, came = [n for n in x if n not in y], [n for n in y if n not in x]
                if gone or came:
                    lines.append(f"{god} / {mode} / {label}: -{gone} +{came}")
                else:
                    lines.append(f"{god} / {mode} / {label}: order {x} -> {y}")
    return lines


def write_snapshot(snap, path=SNAPSHOT_PATH):
    ctx = load_frozen()["context"]
    doc = {"_about": ("Frozen reference builds and verdicts (smite.model_audit, part 1). "
                      "Regenerate ONLY on purpose: python -m smite.model_audit reference --write, "
                      "and explain the diff in the PR."),
           "_inputs": {"data_patch": ctx.get("data_patch"), "frozen_on": ctx.get("frozen_on")},
           "gods": snap}
    path.write_text(json.dumps(doc, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def read_snapshot(path=SNAPSHOT_PATH):
    return json.loads(path.read_text(encoding="utf-8"))["gods"]


# ── 2. Held-out check ─────────────────────────────────────────────────────

HELDOUT_PERCENT = 30


def split_of(name):
    """"heldout" or "tuning", from a hash of the god's name alone."""
    h = int(hashlib.sha256(name.encode("utf-8")).hexdigest()[:8], 16)
    return "heldout" if h % 100 < HELDOUT_PERCENT else "tuning"


def split_metrics(per_god):
    out = {}
    for part in ("tuning", "heldout"):
        sub = {n: m for n, m in per_god.items() if split_of(n) == part}
        agg = validate.aggregate(sub)
        out[part] = {"gods": len(sub), "win_weighted": agg["mean_win_weighted"],
                     "coverage": agg["mean_coverage"], "spearman": agg["pooled_spearman"],
                     "pairs": agg["pooled_n"]}
    return out


_BASE_SCRIPT = (
    "import json, sys\n"
    "from smite import validate\n"
    "per_god, _ = validate.compute()\n"
    "json.dump({k: {'coverage': v['coverage'], 'win_weighted': v['win_weighted'],"
    " 'pairs': v['pairs']} for k, v in per_god.items()}, sys.stdout)\n")

#: What `--base` overlays from THIS tree onto the base worktree, so the
#: delta isolates code + config (`_weights.yaml`, `_tags.yaml`, ...).
DATA_OVERLAY = ("Gods", "Items", "builds")


def base_per_god(ref="origin/main", overlay=True):
    """`validate.compute`'s per-god metrics at git `ref`, in a throwaway
    worktree. `overlay` copies this tree's input data over the worktree's."""
    tmp = Path(tempfile.mkdtemp(prefix="ichor-base-"))
    wt = tmp / "wt"
    subprocess.run(["git", "worktree", "add", "--detach", str(wt), ref], cwd=REPO_ROOT,
                   check=True, capture_output=True)
    try:
        if overlay:
            for d in DATA_OVERLAY:
                shutil.rmtree(wt / "data" / d, ignore_errors=True)
                shutil.copytree(REPO_ROOT / "data" / d, wt / "data" / d)
        res = subprocess.run([sys.executable, "-c", _BASE_SCRIPT], cwd=wt / "pipeline",
                             check=True, capture_output=True, text=True)
        per_god = json.loads(res.stdout)
        return {k: dict(v, pairs=[tuple(p) for p in v["pairs"]]) for k, v in per_god.items()}
    finally:
        subprocess.run(["git", "worktree", "remove", "--force", str(wt)], cwd=REPO_ROOT,
                       capture_output=True)
        shutil.rmtree(tmp, ignore_errors=True)


def heldout_report(head, base=None, base_label="origin/main"):
    fmt = lambda v: "n/a" if v is None else f"{v:.4f}"
    lines = [f"{'split':<8} {'gods':>4}  {'win-weighted':>12}  {'spearman':>8}  {'coverage':>8}"
             + ("   delta vs " + base_label + " (win-weighted / spearman)" if base else "")]
    ok = True
    for part in ("tuning", "heldout"):
        h = head[part]
        line = (f"{part:<8} {h['gods']:>4}  {fmt(h['win_weighted']):>12}  {fmt(h['spearman']):>8}  "
                f"{fmt(h['coverage']):>8}")
        if base:
            b = base[part]
            dw = h["win_weighted"] - b["win_weighted"]
            ds = (None if h["spearman"] is None or b["spearman"] is None
                  else h["spearman"] - b["spearman"])
            line += f"   {dw:+.4f} / " + ("n/a" if ds is None else f"{ds:+.4f}")
            if part == "heldout" and (dw < 0 or (ds is not None and ds < 0)):
                ok = False
                line += "   <- LOWER"
        lines.append(line)
    return lines, ok


# ── 3. Passive firing ─────────────────────────────────────────────────────

_EVENT_HOOKS = ("on_attack", "on_ability", "on_takedown", "on_hit_taken")
_VALUE_HOOKS = ("reduce_hit", "prot_bonus", "stat_bonus", "active")
_STATIC_HOOKS = ("grants", "converts", "ehp_segments", "cooldown")


def _signature(sim, arg):
    ev = arg if isinstance(arg, sbs.Event) else None
    hit = arg if isinstance(arg, dict) else None
    return (sim.dealt, round(sum(sim.by_item.values()), 9), sim.healed, sim.hp, len(sim._after),
            repr(sim.state), repr(sim.dynamic), repr(sim.shields), repr(sim.shreds),
            repr(sorted(sim.nxt.items())), repr(sorted(getattr(sim, "active_ready", {}).items())),
            None if ev is None else (ev.raw, ev.multiplier, len(ev.procs), ev.uncapped_pct_pen),
            None if hit is None else repr(sorted(hit.items())))


class FireCounter:
    """Per item: `dynamic` fires and whether any static hook had an effect."""

    def __init__(self):
        self.dynamic = Counter()
        self.static = set()
        self.hooks = defaultdict(set)

    def wrap(self, name, p):
        changes = {}
        for h in _EVENT_HOOKS + _VALUE_HOOKS + _STATIC_HOOKS:
            fn = getattr(p, h)
            if fn is not None:
                self.hooks[name].add(h)
                changes[h] = self._wrapped(name, h, fn)
        return dataclasses.replace(p, **changes) if changes else p

    def _wrapped(self, name, hook, fn):
        if hook in _EVENT_HOOKS:
            def w(sim, arg):
                before = _signature(sim, arg)
                out = fn(sim, arg)
                if _signature(sim, arg) != before:
                    self.dynamic[name] += 1
                return out
        elif hook == "reduce_hit":
            def w(sim, hit):
                out = fn(sim, hit)
                if out is not None and abs(out - 1.0) > 1e-12:
                    self.dynamic[name] += 1
                return out
        elif hook == "prot_bonus":
            def w(sim, dtype):
                out = fn(sim, dtype)
                if out:
                    self.dynamic[name] += 1
                return out
        elif hook == "stat_bonus":
            def w(sim, key, v):
                out = fn(sim, key, v)
                if out is not None and abs(out - v) > 1e-12:
                    self.dynamic[name] += 1
                return out
        elif hook == "active":
            def w(sim):
                before = _signature(sim, None)
                out = fn(sim)
                if out or _signature(sim, None) != before:
                    self.dynamic[name] += 1
                return out
        elif hook == "ehp_segments":
            def w(ctx):
                out = fn(ctx)
                if any(ep or em for _, ep, em in out or ()):
                    self.static.add(name)
                return out
        elif hook == "cooldown":
            def w(ctx):
                out = fn(ctx)
                if any(abs(v - 1.0) > 1e-12 for v in (out or {}).values()):
                    self.static.add(name)
                return out
        else:  # grants, converts
            def w(ctx):
                out = fn(ctx)
                if any(abs(v) > 1e-12 for v in (out or {}).values()):
                    self.static.add(name)
                return out
        return w


@contextmanager
def counting():
    """Patch `side_by_side.passives_for` so every Sim and stat build in the
    block reads wrapped passives; yields the counter."""
    counter = FireCounter()
    real = sbs.passives_for

    def wrapped(names, items_by_name, disabled=()):
        return [(n, counter.wrap(n, p)) for n, p in real(names, items_by_name, disabled)]

    with mock.patch.object(sbs, "passives_for", wrapped):
        yield counter


NEVER, RARE, FIRES, KIT_BLOCKED, UNSIMULATED, NO_PASSIVE = (
    "never fires", "fires rarely", "fires", "kit cannot trigger", "not simulated", "no passive")
#: A purely event-driven passive that fires at most this many times across
#: the whole `power` run (two 10s duels, two bursts, up to two fight-EHP runs)
#: is RARE. An "On Use" active legitimately fires once per run (4-6 total),
#: so this sits below that.
RARE_MAX = 2


def classify_build(god, six, items_by_name, targets, caps=None):
    """`{item: (class, fires)}` for one build at six items, game-clock stacks."""
    caps = kit_fit.capabilities(god) if caps is None else caps
    with counting() as c:
        sbs.power(god, six, items_by_name, targets)
    out, blocked_by = {}, {}
    for n in six:
        pv = passive_sim.lookup(items_by_name[n])
        needs = kit_fit.item_needs(items_by_name[n])
        blocked = [need for need in needs if not any(caps.get(x) for x in kit_fit.SATISFIES[need])]
        if pv.status == passive_sim.NO_PASSIVE:
            out[n] = (NO_PASSIVE, 0)
        elif pv.status == passive_sim.NOT_SIMULATED:
            out[n] = (UNSIMULATED, 0)
        elif n in c.static:
            out[n] = (FIRES, c.dynamic[n])
        elif c.dynamic[n] == 0:
            out[n] = (NEVER, 0)
        elif c.dynamic[n] <= RARE_MAX:
            out[n] = (RARE, c.dynamic[n])
        else:
            out[n] = (FIRES, c.dynamic[n])
        blocked_by[n] = blocked
    # Some passives are applied by NAME inside the clock, not through a hook
    # (Deathbringer's crit multiplier, Death Metal, Stygian Anchor, the
    # anti-heal table). The counter cannot see those, so anything it calls
    # never is re-checked by switching that passive off: if the run moves, it
    # fired.
    for n, (cls, fires) in list(out.items()):
        if cls == NEVER:
            worth = sbs.passive_contribution(god, six, items_by_name, targets, n)
            if any(abs(v) > 1e-9 for v in worth.values()):
                out[n] = (FIRES, fires)
    # The kit reading (`kit_fit.item_needs`) decides only where the clock
    # cannot: a passive that is not simulated, or that never fired. Where the
    # clock shows it firing, the need is on a RIDER (Soul Gem's "heal you and
    # allies within 3.2m" fires its damage and self-heal for anyone), and the
    # row carries `ally_rider` instead.
    for n, (cls, fires) in list(out.items()):
        if blocked_by.get(n):
            out[n] = (KIT_BLOCKED, fires) if cls in (UNSIMULATED, NEVER) else (cls, fires, "ally_rider")
    return out


def recommended_builds(gods, mode, load=recommend.load_build_note):
    """`[(god, archetype label, six)]` for every suggested entry in the
    shipped note, deduplicated on (god, six)."""
    seen, out = set(), []
    for g in gods:
        for e in (load(g["name"], mode) or {}).get("builds") or []:
            if e.get("source") != "suggested":
                continue
            six = [s.get("name") if isinstance(s, dict) else s for s in e.get("slot_order") or []][:6]
            key = (g["name"], tuple(six))
            if len(six) < 6 or key in seen:
                continue
            seen.add(key)
            out.append((g, entry_label(e), six))
    return out


def passive_firing(gods, items, builds, weights, modes=MODES, load=recommend.load_build_note):
    """Per mode, per (god, build): the class of every item. Returns rows."""
    ibn = {it["name"]: it for it in items}
    rows = []
    for mode in modes:
        with mode_rules(mode, None, weights, builds, ibn, gods):
            targets = sbs.reference_targets(gods, builds, ibn)
            for g, label, six in recommended_builds(gods, mode, load):
                if any(n not in ibn for n in six):
                    continue
                caps = kit_fit.capabilities(g)
                for item, res in classify_build(g, six, ibn, targets, caps).items():
                    rows.append({"mode": mode, "god": g["name"], "build": label, "item": item,
                                 "class": res[0], "fires": res[1], "ally_rider": len(res) > 2})
    return rows


def firing_summary(rows):
    """Per item: builds it is recommended in, and how many in each class."""
    by_item = {}
    for r in rows:
        e = by_item.setdefault(r["item"], {"builds": 0, "classes": Counter(), "gods": defaultdict(set)})
        e["builds"] += 1
        e["classes"][r["class"]] += 1
        e["gods"][r["class"]].add(f"{r['god']} ({r['mode']})")
    return by_item


def firing_lines(rows):
    summ = firing_summary(rows)
    flagged = {n: e for n, e in summ.items()
               if e["classes"][NEVER] or e["classes"][RARE] or e["classes"][KIT_BLOCKED]}
    order = sorted(flagged, key=lambda n: -(flagged[n]["classes"][NEVER] + flagged[n]["classes"][RARE]
                                            + flagged[n]["classes"][KIT_BLOCKED]))
    total = Counter(r["class"] for r in rows)
    lines = ["# Passive firing audit", "",
             "Generated by `python -m smite.model_audit passives`. REPORT ONLY — no weight reads it.", "",
             "Every suggested build in the shipped notes (all modes, deduplicated per god), run "
             "through `side_by_side.power` at six items on the game-clock stacks, with every "
             "simulated passive's hooks counted. A hook FIRES when it changed the fight: a hit, a "
             "heal, a stack, a protection, a multiplier or a stat. A passive whose only hooks are "
             "stat grants fires when the grant is non-zero.", "",
             f"- **never fires** — simulated, and not one hook changed anything for this god",
             f"- **fires rarely** — event-driven only, {RARE_MAX} or fewer fires across the whole run "
             "(two 10s duels, two bursts, up to two fight-to-death runs)",
             "- **kit cannot trigger** — the passive needs a capability this kit lacks "
             "(`kit_fit.item_needs`: an ally to buff/heal/shield, or allies nearby without a melee "
             "kit). The Lotus Sickle class; holds whether or not the passive is simulated", "",
             "Recommended item-slots by class: " + ", ".join(f"{k} {v}" for k, v in total.most_common()),
             "", "| Item | Recommended in | Never | Rare | Kit cannot | Status | Examples |",
             "|---|---|---|---|---|---|---|"]
    for n in order:
        e = flagged[n]
        ex = sorted(e["gods"][NEVER] | e["gods"][RARE] | e["gods"][KIT_BLOCKED])
        status = next((r["class"] for r in rows if r["item"] == n and r["class"] in (UNSIMULATED,)), "")
        lines.append(f"| {n} | {e['builds']} | {e['classes'][NEVER]} | {e['classes'][RARE]} | "
                     f"{e['classes'][KIT_BLOCKED]} | {status or 'simulated'} | "
                     f"{', '.join(ex[:6])}{' …' if len(ex) > 6 else ''} |")
    riders = Counter(r["item"] for r in rows if r.get("ally_rider"))
    lines += ["", "## Fires, but its ally-facing part cannot reach an ally on this kit", "",
              "The clock shows the passive firing; `kit_fit` reads a part of its text as needing an "
              "ally this kit cannot support. The value counted is the part that lands on our god.", "",
              "| Item | Recommended item-slots |", "|---|---|"]
    lines += [f"| {n} | {k} |" for n, k in riders.most_common()]
    unsim = sorted(((n, e["classes"][UNSIMULATED]) for n, e in summ.items() if e["classes"][UNSIMULATED]),
                   key=lambda x: -x[1])
    lines += ["", "## Recommended, passive not simulated (cannot be counted)", "",
              "| Item | Recommended item-slots |", "|---|---|"]
    lines += [f"| {n} | {k} |" for n, k in unsim]
    return lines


# ── 4. Weight sensitivity ─────────────────────────────────────────────────

def _scale_leaves(node, f):
    if isinstance(node, dict):
        return {k: _scale_leaves(v, f) for k, v in node.items()}
    if isinstance(node, (int, float)) and not isinstance(node, bool):
        return node * f
    return node


def _set(path, scale_all=False):
    def apply(w, f):
        node = w
        for k in path[:-1]:
            node = node.setdefault(k, {})
        if path[-1] not in node:
            return False
        node[path[-1]] = _scale_leaves(node[path[-1]], f) if scale_all else node[path[-1]] * f
        return True
    return apply


def _role_lifesteal(w, f):
    hit = False
    for role in ("Solo", "Support"):
        m = (w.get("role_stats") or {}).get(role) or {}
        if "Lifesteal" in m:
            m["Lifesteal"] *= f
            hit = True
    return hit


def _mode_signal(w, f):
    hit = False
    for mode in ("joust", "arena"):
        s = ((w.get("modes") or {}).get(mode) or {}).get("signals")
        if s and "efficiency" in s:
            s["efficiency"] *= f
            hit = True
    return hit


#: The major weights, each scaled x0.8 and x1.2. A signal weight is not
#: renormalised by hand: `scoring.signal_score` divides by the sum already.
NUDGES = (
    ("signals.efficiency", _set(("signals", "efficiency"))),
    ("signals.win", _set(("signals", "win"))),
    ("signals.pick", _set(("signals", "pick"))),
    ("signals.fit", _set(("signals", "fit"))),
    ("joust+arena signals.efficiency", _mode_signal),
    ("kit_blend", _set(("kit_blend",))),
    ("offmap_efficiency", _set(("offmap_efficiency",))),
    ("attack_damage_fit", _set(("attack_damage_fit",))),
    ("cap_overflow", _set(("cap_overflow",))),
    ("role_stats (every weight)", _set(("role_stats",), True)),
    ("role_stats Lifesteal (Solo, Support)", _role_lifesteal),
    ("modes.conquest.tag_bonus", _set(("modes", "conquest", "tag_bonus"), True)),
    ("modes.joust.tag_bonus", _set(("modes", "joust", "tag_bonus"), True)),
    ("modes.arena.tag_bonus", _set(("modes", "arena", "tag_bonus"), True)),
)
FACTORS = (0.8, 1.2)


def base_builds(gods, items, builds, weights, tags_map, mode):
    """`{god: (core, model)}` for the BASE kit in `mode` (no flavors, no
    aspect), through `recommend.build_suggested_entries` itself."""
    out = {}
    with pricing(weights), mock.patch.object(scoring, "eligible_flavors", lambda *a, **k: []):
        for g in gods:
            bare = dict(g, aspects=[])
            god_build = builds.get(g["name"]) if mode == "Conquest" else {"builds": []}
            entries = recommend.build_suggested_entries(bare, items, god_build or {"builds": []},
                                                        weights, tags_map, mode)
            by = {e["archetype"]: e for e in entries}
            out[g["name"]] = (tuple(by["core"]["slot_order"]) if "core" in by else (),
                              by.get("model"))
    return out


def sensitivity(gods, items, builds, weights, tags_map, nudges=NUDGES, factors=FACTORS, modes=MODES,
                progress=None):
    """Returns `(baseline, results)`; `results` is a list of
    `{nudge, factor, mode, cores_changed, models_changed, flips: [(god, before, after)]}`."""
    ibn = {it["name"]: it for it in items}
    by_name = {g["name"]: g for g in gods}

    def verdicts(w, bb, mode, only=None):
        view = sbs.ModelView(items, w, tags_map)
        out = {}
        with pricing(w), mode_rules(mode, None, w, builds, ibn, gods):
            targets = sbs.reference_targets(gods, builds, ibn)
            for name, (_, model) in bb.items():
                if (only is not None and name not in only) or model is None:
                    continue
                v, unw = verdict_for(by_name[name], builds.get(name) or {"builds": []}, [model],
                                     ibn, targets, view, mode, w)
                out[name] = (v, unw) if v is not None else (None, None)
        return out

    baseline = {}
    for mode in modes:
        bb = base_builds(gods, items, builds, weights, tags_map, mode)
        baseline[mode] = {"builds": bb, "verdicts": verdicts(weights, bb, mode)}
    results = []
    for label, apply in nudges:
        for f in factors:
            w = copy.deepcopy(weights)
            if not apply(w, f):
                continue
            for mode in modes:
                base = baseline[mode]
                bb = base_builds(gods, items, builds, w, tags_map, mode)
                cores = [n for n in bb if bb[n][0] != base["builds"][n][0]]
                models = [n for n in bb if (bb[n][1] or {}).get("slot_order")
                          != (base["builds"][n][1] or {}).get("slot_order")]
                vs = verdicts(w, bb, mode, set(models))
                flips = [(n, base["verdicts"].get(n), vs[n]) for n in models
                         if vs.get(n) != base["verdicts"].get(n)]
                results.append({"nudge": label, "factor": f, "mode": mode,
                                "cores_changed": cores, "models_changed": models, "flips": flips})
                if progress:
                    progress(f"{label} x{f} {mode}: {len(cores)} cores, {len(models)} model, "
                             f"{len(flips)} verdict flips")
    return baseline, results


def sensitivity_lines(baseline, results):
    fragile = defaultdict(list)
    for r in results:
        for god, before, after in r["flips"]:
            fragile[(god, r["mode"])].append((r["nudge"], r["factor"], before, after))
    lines = ["# Weight sensitivity", "",
             "Generated by `python -m smite.model_audit sensitivity` (slow; not in CI). Each major "
             "weight in `_weights.yaml` x0.8 and x1.2, one at a time. Every god's BASE-kit `core` and "
             "`model` rebuilt in all three modes; every `model` build that changed is re-judged by "
             "`side_by_side` (the verdict reads the model build only, so a `win`/`pick` nudge moves "
             "cores and can never flip a verdict). A verdict that flips under any nudge is "
             "**FRAGILE**. Report only.", "",
             "Verdict cells are `verdict / unwithheld verdict`.", "",
             "| Weight | x | Mode | Cores changed | Model builds changed | Verdict flips |",
             "|---|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r['nudge']} | {r['factor']:g} | {r['mode']} | {len(r['cores_changed'])} | "
                     f"{len(r['models_changed'])} | {len(r['flips'])} |")
    n_judged = {m: sum(1 for v in b["verdicts"].values() if v[0] is not None) for m, b in baseline.items()}
    lines += ["", f"## Fragile verdicts ({len(fragile)} of "
              f"{sum(n_judged.values())} god-mode verdicts)", "",
              "| God | Mode | Baseline | Flips under |", "|---|---|---|---|"]
    show = lambda v: "none" if not v or v[0] is None else f"{v[0]} / {v[1]}"
    for (god, mode), fl in sorted(fragile.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        base = baseline[mode]["verdicts"].get(god)
        what = "; ".join(f"{n} x{f:g} -> {show(a)}" for n, f, _, a in fl)
        lines.append(f"| {god} | {mode} | {show(base)} | {what} |")
    return lines, fragile


# ── 5. Coverage ───────────────────────────────────────────────────────────

def coverage(items, gods, weights):
    buildable = [it for it in items if scoring.is_buildable(it)]
    status = Counter(passive_sim.lookup(it).status for it in buildable)
    with_passive = len(buildable) - status[passive_sim.NO_PASSIVE]
    heals = [g["name"] for g in gods if ability_heals.god_self_heals(g)]
    rotations = {g["name"]: bq.ability_rotation(g) for g in gods}
    rotation_whole = [n for n, (rot, dropped) in rotations.items() if rot and not dropped]
    rotation_empty = sorted(n for n, (rot, _) in rotations.items() if not rot)
    aspects_total = sum(len(g.get("aspects") or []) for g in gods)
    tuned = sorted(n for n in (weights.get("aspects") or {}) if any(g["name"] == n for g in gods))
    return {
        "generated_by": "python -m smite.model_audit coverage",
        "data_patch": sbs.data_patch(),
        "items": {"buildable": len(buildable), "with_passive": with_passive,
                  "simulated": status[passive_sim.SIMULATED], "partial": status[passive_sim.PARTIAL],
                  "not_simulated": status[passive_sim.NOT_SIMULATED],
                  "simulated_share": (status[passive_sim.SIMULATED] + status[passive_sim.PARTIAL])
                  / with_passive if with_passive else None},
        "gods": {"tracked": len(gods), "self_heals_simulated": len(heals),
                 "self_heal_gods": sorted(heals),
                 "whole_rotation_simulated": len(rotation_whole),
                 "no_damage_rotation": rotation_empty},
        "aspects": {"total": aspects_total, "tuned": len(tuned), "tuned_gods": tuned,
                    "simulated": len(sbs.SIMULATED_ASPECTS)},
    }


def coverage_lines(c):
    i, g, a = c["items"], c["gods"], c["aspects"]
    pct = lambda x, y: f"{x / y:.0%}" if y else "n/a"
    return ["# Model coverage", "",
            f"Generated by `{c['generated_by']}` on {c['data_patch']}. The same figures are in "
            "`viewer/public/model_coverage.json` for the site.", "",
            "| What | Covered | Of | Share |", "|---|---|---|---|",
            f"| Buildable items whose passive is simulated (fully) | {i['simulated']} | {i['with_passive']} "
            f"| {pct(i['simulated'], i['with_passive'])} |",
            f"| ... simulated fully or in part | {i['simulated'] + i['partial']} | {i['with_passive']} "
            f"| {pct(i['simulated'] + i['partial'], i['with_passive'])} |",
            f"| Gods whose ability self-heals are simulated | {g['self_heals_simulated']} | {g['tracked']} "
            f"| {pct(g['self_heals_simulated'], g['tracked'])} |",
            f"| Gods whose whole damage rotation parses | {g['whole_rotation_simulated']} | {g['tracked']} "
            f"| {pct(g['whole_rotation_simulated'], g['tracked'])} |",
            f"| Gods with NO damaging ability parsed (every ability-hit passive is dead) | "
            f"{len(g['no_damage_rotation'])} | {g['tracked']} | {', '.join(g['no_damage_rotation']) or '-'} |",
            f"| Aspects tuned (`_weights.yaml` aspects) | {a['tuned']} | {a['total']} | {pct(a['tuned'], a['total'])} |",
            f"| Aspects simulated (`side_by_side.SIMULATED_ASPECTS`) | {a['simulated']} | {a['total']} "
            f"| {pct(a['simulated'], a['total'])} |", ""]


# ── CLI ───────────────────────────────────────────────────────────────────

def _cmd_reference(args):
    if args.refreeze:
        refreeze()
        print(f"re-froze inputs in {FROZEN}")
    new = compute_reference()
    if args.write or args.refreeze:
        old = read_snapshot() if SNAPSHOT_PATH.exists() else {}
        write_snapshot(new)
        changes = diff_reference(old, new)
        print(f"wrote {SNAPSHOT_PATH} ({len(changes)} change(s))")
        for line in changes:
            print("  " + line)
        return 0
    changes = diff_reference(read_snapshot(), new)
    if changes:
        print(f"REFERENCE CHANGED - {len(changes)} build/verdict change(s):")
        for line in changes:
            print("  " + line)
        print("If intended: python -m smite.model_audit reference --write, and explain it in the PR.")
        return 1
    print(f"reference builds unchanged ({len(new)} gods x {len(MODES)} modes)")
    return 0


def _cmd_heldout(args):
    per_god, _ = validate.compute()
    head = split_metrics(per_god)
    base = None
    if args.base != "none":
        base = split_metrics(base_per_god(args.base, overlay=not args.base_data))
    lines, ok = heldout_report(head, base, args.base)
    print("\n".join(lines))
    held = sorted(n for n in per_god if split_of(n) == "heldout")
    print(f"held-out gods ({len(held)}): {', '.join(held)}")
    if base is not None:
        print("held-out " + ("not lowered - PASS" if ok else "LOWERED - a model PR must not do this"))
    return 0 if ok or not args.check else 1


def _cmd_passives(args):
    items, gods, weights, tags_map, builds = sbs.load_inputs()
    with pricing(weights):
        rows = passive_firing(gods, items, builds, weights)
    out = ANALYSIS / "_passive_firing.md"
    out.write_text("\n".join(firing_lines(rows)) + "\n", encoding="utf-8")
    c = Counter(r["class"] for r in rows)
    print(f"wrote {out}: " + ", ".join(f"{k} {v}" for k, v in c.most_common()))
    return 0


def _cmd_coverage(args):
    items, gods, weights, _, _ = sbs.load_inputs()
    c = coverage(items, gods, weights)
    COVERAGE_JSON.write_text(json.dumps(c, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    (ANALYSIS / "_model_coverage.md").write_text("\n".join(coverage_lines(c)) + "\n", encoding="utf-8")
    print(f"wrote {COVERAGE_JSON} and {ANALYSIS / '_model_coverage.md'}")
    return 0


def _cmd_sensitivity(args):
    items, gods, weights, tags_map, builds = sbs.load_inputs()
    baseline, results = sensitivity(gods, items, builds, weights, tags_map,
                                    progress=lambda s: print("  " + s, flush=True))
    lines, fragile = sensitivity_lines(baseline, results)
    out = ANALYSIS / "_weight_sensitivity.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out}: {len(fragile)} fragile verdict(s)")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("reference")
    r.add_argument("--write", action="store_true")
    r.add_argument("--refreeze", action="store_true")
    h = sub.add_parser("heldout")
    h.add_argument("--base", default="origin/main", help="git ref to compare against, or 'none'")
    h.add_argument("--base-data", action="store_true",
                   help="use the base ref's own data instead of overlaying this tree's")
    h.add_argument("--check", action="store_true", help="exit 1 if the held-out split is lowered")
    sub.add_parser("passives")
    sub.add_parser("coverage")
    sub.add_parser("sensitivity")
    a = sub.add_parser("all")
    a.add_argument("--slow", action="store_true", help="also run the sensitivity sweep")
    args = ap.parse_args(argv)
    if args.cmd == "all":
        rc = 0
        for cmd, ns in (("reference", argparse.Namespace(write=False, refreeze=False)),
                        ("heldout", argparse.Namespace(base="origin/main", base_data=False, check=False)),
                        ("passives", None), ("coverage", None)) + ((("sensitivity", None),) if args.slow else ()):
            print(f"== {cmd}")
            rc |= globals()[f"_cmd_{cmd}"](ns)
        return rc
    return globals()[f"_cmd_{args.cmd}"](args)


if __name__ == "__main__":
    sys.exit(main())
