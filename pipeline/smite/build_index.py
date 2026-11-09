"""Walk the SMITE data + build folders and emit one index.json for the
second-monitor viewer to fetch. Re-run after any refresh, or on demand via
the viewer's "reload data" button — no file-watcher, content only changes
on patch days."""
import json
import shutil
from pathlib import Path

import yaml

from smite import (abilities, damage_value, efficiency, notes, recommend, threat_kit,
                   scoring, snapshots, tierlist)


# Reference targets for the draft's damage overlay (B6), derived rather than
# picked: across the roster a level-20 god carries a median 76 physical / 56
# magical protection with no items, and the median protection item gives 30, so
# three of them is another ~90. "Squishy" and "three-item tank" are therefore
# roughly 70 and 170, and every real enemy sits between them.
SQUISHY_PROTECTION = 70.0
TANK_PROTECTION = 170.0

#: The `_weights.yaml` switches `efficiency.apply_pricing_flags` reads, shipped
#: as `method.pricing` so the method page can say which passives are priced.
PRICING_SWITCHES = ("price_passives", "price_stacks", "price_crit_multipliers",
                    "price_conversions", "price_adaptive", "price_stat_multipliers",
                    "price_on_hit", "price_passive_sim")


def team_config(weights):
    """`{tags, duplicate_value, modes: {Mode: {team_size, share, bonus}}}` —
    `bonus` is each team tag's UNSCALED mode bonus, `share` the scale the
    static builds applied (`scoring.team_share`)."""
    team = weights.get("team_tags") or {}
    modes = {}
    for mode in recommend.MODES:
        prof = scoring.resolve_profile(weights, mode)
        modes[mode] = {"team_size": ((weights.get("modes") or {}).get(mode.lower()) or {}).get("team_size"),
                       "share": prof["team_share"], "shares": prof.get("team_shares", {}),
                       "bonus": prof["team_tag_bonus"]}
    return {"tags": list(team.get("tags") or []),
            "duplicate_value": team.get("duplicate_value", 0.0), "modes": modes}


def community_transfer(weights):
    """`{Mode: {from, reject_tags, excluded_items}}` for every mode that
    borrows another mode's community record (`modes.<mode>.borrow_community`).

    Joust and Arena have no community record of their own, so the god page
    shows them Conquest's most-picked list, labelled as Conquest's. Which of
    those items Conquest's record does NOT describe there is already decided,
    with reasons, in `_weights.yaml`: the tags the Hybrid refuses to borrow,
    and the items the mode's shop does not sell. This ships those two lists
    verbatim so the page marks the same items the pipeline set aside, instead
    of a hand-copy of the YAML living in TypeScript. The reasons themselves are
    comments there and words in `viewer/src/lib/mostPicked.ts`; a viewer test
    fails if a tag shipped here has no sentence.

    A mode without `borrow_community` is absent, not empty: it borrows nothing,
    so there is nothing to mark. `excluded_items` ships only beside a borrow —
    it is the one other list that says "Conquest's record does not apply here".
    """
    out = {}
    for mode in recommend.MODES:
        cfg = (weights.get("modes") or {}).get(mode.lower()) or {}
        borrow = cfg.get("borrow_community")
        if not borrow:
            continue
        out[mode] = {"from": borrow.get("from", "Conquest"),
                     "reject_tags": list(borrow.get("reject_tags") or []),
                     "excluded_items": list(cfg.get("excluded_items") or [])}
    return out


def team_fit_items(gods, builds, items, weights, tags_map):
    """`{god: {mode: [item]}}` — the team-tag items whose kit fit passes
    `kit_fit.fits` against that mode's shipped core. The draft pays the "you
    are your team's carrier" delta only on these, so an anti-heal or aura
    item reaches a board only where the kit uses it."""
    from smite import kit_fit
    team = set((weights.get("team_tags") or {}).get("tags") or ())
    if not team:
        return {}
    eff, _ = efficiency.efficiency_scores(items)
    ib = {it["name"]: it for it in items}
    cands = [n for n, tg in tags_map.items() if n in ib and scoring.is_buildable(ib[n])
             and team & set(tg or ())]
    by_note = {(b.get("god"), b.get("mode")): b for b in builds}
    out = {}
    for g in gods:
        caps = kit_fit.capabilities(g)
        per = {}
        for mode in recommend.MODES:
            note = by_note.get((g.get("name"), mode)) or {}
            core = next((e.get("slot_order") for e in note.get("builds") or []
                         if e.get("source") == "suggested" and e.get("archetype") == "core"
                         and not e.get("aspect")), None) or []
            core = [c.get("name") if isinstance(c, dict) else c for c in core]
            if not core:
                continue
            fs = kit_fit.stat_fits(g, items, weights, tags_map, eff, mode)
            floor = kit_fit.fit_floor(fs, core)
            ok = sorted(n for n in cands if kit_fit.fits(g, ib[n], fs.get(n), floor, caps)[0])
            if ok:
                per[mode] = ok
        if per:
            out[g["name"]] = per
    return out


def _enrich_gods(gods, weights):
    """Attach the derived ability-leveling order to each god so the viewer's
    Info tab doesn't need the kit-scaling parser client-side. Shape:
    {"order": [20 slot names, one per level], "summary": {"max_order": [...],
    "ult_levels": [...]}} — see abilities.py. Heuristic, not scraped data."""
    for god in gods:
        order = abilities.ability_order(god, weights)
        # Gods whose kit didn't scrape any levelable abilities (stance gods:
        # Artio, Merlin, Ullr) get no key at all rather than a fabricated
        # order — the viewer hides the section instead of showing nonsense.
        if order:
            god["ability_order"] = {"order": order,
                                    "summary": abilities.summary(order, weights)}
        # What this god's kit does TO you, counted off the ability text. The
        # draft used to grade a comp by `specializations` alone, which is a
        # three-word summary of a whole kit: `Healing` is on 9 gods and 42
        # actually heal, `Crowd Control` on 8 and 80 land hard CC, and nothing
        # labels player-made walls at all. See threat_kit.py.
        god["threat_kit"] = threat_kit.god_threat_kit(god)
        # How much this god's own archetype wants PROTECTIONS, 0..1. The draft
        # applies its defensive stat bonuses in proportion to this.
        #
        # `draft.stat_bonus` is keyed on the ENEMY's damage type and was applied
        # flat, so a Hunter facing a magical comp got Magical Protection at
        # weight 1.0 against Penetration's 0.6 — the draft was answering "they
        # are magical" with "so become tankier", for a god whose entire build
        # is damage. Measured across 10 damage gods vs a 4-tank/4-magical comp:
        # protection items in the core went 12 -> 25, with Apollo and Anhur
        # both gaining Genji's Guard.
        #
        # The role map already knows the answer and is the same map that governs
        # fit, so this is consistency rather than a new opinion: Support and
        # Guardian read 1.0, Solo/Warrior/Brawler 0.5, Carry and Mid 0.0.
        role_map = scoring._role_stat_map(god, weights)
        god["defense_affinity"] = round(max(
            role_map.get("Physical Protection", 0.0),
            role_map.get("Magical Protection", 0.0)), 3)
    return gods


def popular_items(build_entry: dict) -> list:
    """Aggregate one community build entry's `slot_order` (and each slot's
    `alternates`) into a flat "what does this god's playerbase actually buy"
    list of `{name, pick_rate, win_rate}` — items, not an ordered build. An
    item seen more than once (as a slot pick here, an alternate there) is
    deduped, keeping the sighting with the highest pick_rate. Sorted by
    pick_rate descending, then name ascending so ties are deterministic.
    THE FLATTENING IS DELIBERATE HERE AND WAS A HOLE EVERYWHERE ELSE. This
    answers "what does this playerbase buy", for a panel that lists items, and
    dropping the slot is right for that question. It was the only reader of
    `slot_order` for years, so the POSITIONAL half of the record — the same
    item at different rates in slots 3, 4 and 5, slot 1 far more concentrated
    than slot 6 — reached nothing downstream, and `assemble.build_order`'s own
    docstring said "we have no real build-path data" while the data sat in the
    dict this function was reading. `scoring.slot_positions` is the other
    reading; neither replaces the other.

    Pure function over a single dict — no disk access — so it's unit-testable
    on its own; see test_build_index.py."""
    best: dict = {}
    for slot in build_entry.get("slot_order") or []:
        if not isinstance(slot, dict):
            continue
        for candidate in [slot, *(slot.get("alternates") or [])]:
            name = candidate.get("name")
            rate = candidate.get("pick_rate")
            if not name or rate is None:
                continue
            if name not in best or rate > best[name]["pick_rate"]:
                best[name] = {"name": name, "pick_rate": rate,
                              "win_rate": candidate.get("win_rate")}
    return sorted(best.values(), key=lambda i: (-i["pick_rate"], i["name"]))


def starter_options(weights, builds):
    """Every starter pair a build can carry: the `starters:` table's rows as
    they always shipped, then each other pair stamped on any build, by base.

    The build editor offers exactly this list and pre-selects the build's own
    starter by `base`. Once the starter became the community's most-picked
    path (`scoring.pick_starter`, 2026-11-08), most stamped pairs — Bluestone
    Pendant, Bumba's Cudgel, Selflessness, Sands of Time — were not table rows,
    so the editor would have opened on "No starter" and saved the build
    without one."""
    rows = list(weights.get("starters") or [])
    seen = {(r.get("base"), r.get("upgrade")) for r in rows}
    extra = set()
    for note in builds:
        for b in (note or {}).get("builds") or []:
            s = b.get("starter") or {}
            pair = (s.get("base"), s.get("upgrade"))
            if all(pair) and pair not in seen:
                extra.add(pair)
    return rows + [{"base": b, "upgrade": u} for b, u in sorted(extra)]


def _attach_popular_items(builds):
    """Attach `popular_items` (see above) to every community build entry so
    the viewer's god page can show the playerbase's most-picked items without
    re-aggregating `slot_order` client-side. Non-community entries (and gods
    with no community data at all) get no key — never a fabricated list."""
    for note in builds:
        for b in note.get("builds", []):
            if b.get("source") == "community":
                b["popular_items"] = popular_items(b)
    return builds


def _enrich_items(items, tags, eff=None):
    """Attach god-agnostic effect_tags + the efficiency verdict to each item.

    Ships the model's working, not just its label. The regression already
    computes a residual per item (`efficiency.efficiency_scores`); shipping
    only the three-bucket `tier` left the viewer able to say "Premium" but not
    *by how much*, which is the number a player actually needs to weigh an
    item's passive against its price.

    `residual` is rounded to whole gold and `predicted_cost` derived back from
    it, so `cost - predicted_cost == residual` holds exactly on screen — a
    surface that shows the arithmetic can't have it fail to add up.

    `priced_passive` is what the fit credits BEYOND the printed stats — the
    pricing flags' grants and the simulated passive columns
    (`efficiency.passive_columns`), absent when there is none. The receipt
    needs it to close: with the flags on, 87 of 193 items are priced partly on
    something their stat line does not show.

    Items outside the scored pool (non-numeric cost, tier-1 starters, and
    statless items, none of which the regression can price — see
    `efficiency.efficiency_pool`) get `None` for both, never a fabricated zero.

    `comparable` says whether the residual belongs on a ranking against every
    other item. A god-specific item's price IS meaningful — Ashwhorl Acorn
    really does give 3,211 gold of stats for 2,000 — but 86 of the 87 gods
    cannot buy it, so letting it head a global "best value" board answers a
    question nobody asked. It stays visible and priced, and sorts with its
    own kind.
    """
    if eff is None:
        eff = {}
        if efficiency.numeric_cost_items(items):
            eff, _ = efficiency.efficiency_scores(items)
    for it in items:
        it["effect_tags"] = tags.get(it["name"], [])
        scored = eff.get(it["name"])
        it["efficiency_tier"] = scored.get("tier") if scored else None
        if scored and isinstance(it.get("cost"), (int, float)):
            residual = round(scored["residual"])
            it["efficiency"] = {
                "predicted_cost": it["cost"] - residual,
                "residual": residual,
                "score": round(scored["score"], 4),
                "comparable": not it.get("god"),
            }
            passive = efficiency.passive_columns(it)
            if passive:
                it["efficiency"]["priced_passive"] = {
                    k: round(v, 3) for k, v in sorted(passive.items())}
        else:
            it["efficiency"] = None
    return items


def _flag_uncatalogued_passives(items, data_root: Path) -> None:
    """`passive_uncatalogued: true` on an item the passive catalogue holds as
    `uncatalogued` — added unattended by `smite.new_entities`, its passive
    not yet classified, so the model values it on its stat line alone. The
    viewer says so beside the passive. Absent on every other item."""
    path = data_root / "_passive_classes.yaml"
    if not path.exists():
        return
    entries = (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("items") or {}
    for it in items:
        if (entries.get(it["name"]) or {}).get("uncatalogued"):
            it["passive_uncatalogued"] = True


def draft_answer_tags(weights) -> set:
    """Every effect tag the draft overlay can promote an item for.

    Read off `draft.tag_bonus`, so adding a threat channel to the weights
    protects its answer automatically rather than needing a second edit here.
    `draft.stat_bonus` is deliberately not included: a stat bonus moves items
    the table already ranks on those stats, and there is no single answering
    item for `Magical Protection` to protect.
    """
    tags = set()
    for mapping in ((weights.get("draft") or {}).get("tag_bonus") or {}).values():
        tags.update(mapping or {})
    return tags


def _capped_with_answers(rows, cap, answer_tags, tags_map, keep):
    """The top `cap` scored items, plus the best `keep` carrying each answering
    tag wherever the cap cut them off.

    WHY THIS EXISTS. `score_cap` was set to bound the index, and as a bound on
    what can win a slot it is sound: a bounded bonus cannot promote a god's #60
    item. But this table is also the draft overlay's ENTIRE candidate pool,
    since `adaptFromCore` takes it as `base`. An answer ranked below the cap is
    therefore not merely unlikely to win a slot, it is invisible, and the draft
    cannot respond to that threat on that god at all.

    MEASURED on the shipped index at fc59d374, before this fix. The best
    answering item sat outside the top 40 for: anti-crit 77 of 95 gods,
    penetration 40, anti-heal 36, protection-shred 26, cc-immunity 20,
    percent-health 17, peel 13. Netting out the gods already holding the
    answer in their core, the cap alone accounted for 75 / 25 / 32 / 24 / 4 /
    16 / 13 of those. Not one god in any channel lacked an answer for an
    eligibility reason, so every remaining case was the cap and nothing else.

    `_weights.yaml` weights `anti-heal` at 2.0 and calls it "the highest-
    leverage counter-buy in the game", noting it "starts far down the base
    ranking (Divine Ruin is Agni's #20)". For 32 gods it started past #40,
    where no bonus of any size could reach it.

    AND NOTHING WOULD HAVE CAUGHT IT. `archetypeParity.test.ts` checks that an
    undrafted board equals the god page and that the draft can still introduce
    an item the base core never held. Both passed throughout. Nothing measured
    whether an answer was AVAILABLE, so a board the draft could not respond to
    was indistinguishable from one it correctly left alone.
    `draftAnswerable.test.ts` is that gate.

    THE OVERLAY'S PRICES ARE NOT THE PROBLEM and were not touched. Median gap
    from the weakest core slot to the best answering item is +0.031 to +0.053,
    against 0.04 available at a 2-of-5 comp and 0.08 for anti-heal: a
    calibrated knife edge that fires on a real threat and not an incidental
    one. The candidates were missing, not the prices.

    WHAT IT MOVED. Unanswerable (god, mode, channel) combinations go to zero:
    anti-heal 36 gods -> 0, anti-crit 77 -> 2, penetration 40 -> 12,
    protection-shred 26 -> 0, percent-health 17 -> 0, cc-immunity 20 -> 0,
    peel 13 -> 0. Every remaining case is a god already holding the only
    answer in their own core, which needs no alternative. Tables go from
    exactly 40 entries to 42-49, modal 44, and the index from 10,047 KB to
    10,093 KB: +46 KB, or +0.46%, against a +35 KB estimate.

    Driving the real viewer path (`deriveThreats`, `threatOverlay`,
    `adaptFromCore`) over 44 enemy comps, four structured and forty
    seeded-random with half carrying allies, across four seeds and 4,180
    boards per mode, the share of boards where the draft changes the shipped
    six rises from 32.5-37.6% to 36.5-43.9% on Conquest and from 23.0-28.5%
    to 28.5-32.3% on Joust. Arrivals move where the measurement predicted:
    Screeching Gargoyle enters the top eight on Conquest seed 1 (58 arrivals
    from outside it), Toxic Blade climbs 443 -> 466 and Divine Ruin 136 -> 143.

    NOT TO BE CONFUSED with the 14-16% in STATE.md section 5, which is a
    different measurement: that is how much turning the passive-pricing flags
    ON moves the draft's six, not how often the draft changes anything.

    Cost, measured: +1,399 entries and +35 KB on a 10,047 KB index, so +0.4%.
    Raising `score_cap` to 80 instead costs +288 KB and still leaves the tail
    of every channel unprotected, because the cap is not where the answers are.
    """
    out = {r["item"]: round(float(r["total"]), 4) for r in rows[:cap]}
    if not answer_tags or keep <= 0:
        return out
    for row in rows[cap:]:
        tags = set(tags_map.get(row["item"]) or ()) & answer_tags
        if not tags:
            continue
        # Rows arrive ranked, so the first ones past the cap carrying a tag are
        # that channel's best. An item answering two channels is kept once and
        # counts toward `keep` for both, which is exactly what the draft sees.
        for tag in tags:
            held = sum(1 for n in out if tag in (tags_map.get(n) or ()))
            if held < keep:
                out[row["item"]] = round(float(row["total"]), 4)
                break
    return out


def _god_item_scores(gods, builds, items, eff, weights, tags_map) -> dict:
    """`{god: {mode: {item: score}}}` — base item scores for the viewer's
    draft-aware re-rank, one table per mode.

    The viewer is static, so it can't re-run scoring when a comp is entered; it
    instead applies a threat overlay to these shipped totals. Capped at the top
    `draft.score_cap` items per god — a bounded bonus can't promote a god's #60
    item, so shipping the whole matrix would just bloat the index. The cap is
    then re-opened for the items that ANSWER a drafted threat, which the cap was
    silently hiding from the overlay on most of the roster: see
    `_capped_with_answers`, which carries the measurement.

    THIS USED TO BE CONQUEST-ONLY, under a draft page that has offered a Joust
    toggle the whole time. The toggle switched which build NOTE was displayed
    and left the suggested core scored by Conquest's weights, so none of the
    per-mode work reached the draft at all: `modes.joust.tag_bonus` never
    applied, and Eye of Providence — which that table penalises at -0.25 for
    exactly this reason — sat at slot 4 of Achilles' Joust core. A mode
    selector that changes the label and not the model is worse than no mode
    selector.

    Each mode is scored through its own `resolve_profile`, and against its OWN
    build note rather than Conquest's. Joust and Arena have no community note
    at all (SmiteBrain is Conquest-only), which is harmless here because both
    modes zero the `win` and `pick` weights that would read it — but passing
    Conquest's note in would create a silent dependency on those weights
    staying zero, and they are a config value, not a law.

    All three modes ship, including Arena, which is not a draft mode today: the
    whole table is 92 KB against a 5 MB index, and the alternative is encoding
    a viewer decision in the pipeline.

    A god with a hand-tuned entry under `aspects` in `_weights.yaml` also gets
    a `<mode>:aspect` table, so the draft's aspect toggle moves the build the
    same way the god page's does. Only the 7 gods with an overlay get one —
    the other 65 with an aspect have nothing to score differently, and
    emitting an identical copy would tell the viewer they did.

    A DERIVED overlay (`scoring.aspect_overlay`, `aspect_derive`) gets the
    table in a mode only where that mode's build note shipped an aspect
    family — `recommend.build_suggested_entries` emits one only if it moves a
    build, and the draft must not offer a toggle the god page withholds."""
    cap = int((weights.get("draft") or {}).get("score_cap", 40))
    keep = int((weights.get("draft") or {}).get("answer_keep", 2))
    answer_tags = draft_answer_tags(weights)
    by_god_mode = {}
    for b in builds:
        key = (b.get("god"), b.get("mode"))
        if key not in by_god_mode:
            by_god_mode[key] = b
    out = {}
    for god in gods:
        per_mode = {}
        overlay = scoring.aspect_overlay(god, items, weights)
        for mode in recommend.MODES:
            note = by_god_mode.get((god["name"], mode), {})
            # Suggested entries only: a community entry carries the aspect its
            # players picked, which says nothing about what we shipped.
            shipped = any(e.get("aspect") and e.get("source") == "suggested"
                          for e in note.get("builds") or [])
            for suffix, asp in (("", None), (":aspect", overlay)):
                if suffix and not asp:
                    continue
                if suffix and asp.get("derived") and not shipped:
                    continue
                profile = scoring.resolve_profile(weights, mode, None,
                                                  aspect_overlay=asp)
                rows = scoring.score_god_items(
                    god, items, by_god_mode.get((god["name"], mode), {}), eff,
                    weights, tags_map, profile)
                per_mode[mode.lower() + suffix] = _capped_with_answers(
                    rows, cap, answer_tags, tags_map, keep)
        out[god["name"]] = per_mode
    return out


def _god_item_damage(gods, items, weights) -> dict:
    """Per-god, per-item damage gained against a squishy and against a tank.

    B5's arithmetic, shipped where a TARGET actually exists. As a global fit
    signal it was useless — measured, and it halved the validation gate,
    because it cannot price defence. What it does that nothing else can is
    reverse an item's ranking depending on who you are hitting: on Scylla,
    Spear of Desolation gains 276 damage against 20 protection and 79 against
    250, while Void Shard climbs from 8.8 to 13.7.

    The draft is the one surface that knows the enemy, so these are the two
    endpoints and the viewer interpolates between them by how tanky the
    entered comp actually is.

    EACH COLUMN is normalised separately, against the best item for that
    target. Sharing one denominator would be the obvious thing and would be
    useless: mitigation shrinks every number against a tank, so every item
    would show a loss and the ranking would never change. What the draft needs
    is the RELATIVE shift — which items move up the order as the enemy hardens
    — and that only survives if each target is scored on its own scale.

    A god whose kit didn't parse gets no entry rather than a fabricated one;
    the overlay simply doesn't fire for them.
    """
    cap = int((weights.get("draft") or {}).get("score_cap", 40))
    # Per rotation or per second — see `damage_per_second` in _weights.yaml.
    # This is the only caller of `item_damage_gain`, so the switch is a
    # parameter rather than a module global: there is no path by which a gate
    # could measure one setting while the shipped table used the other.
    per_second = bool(weights.get("damage_per_second"))
    out = {}
    for god in gods:
        if not damage_value.ability_damage_components(god):
            continue
        pairs = {}
        for item in items:
            if not scoring.is_buildable(item, god):
                continue
            low = damage_value.item_damage_gain(god, item, SQUISHY_PROTECTION,
                                                per_second=per_second)
            high = damage_value.item_damage_gain(god, item, TANK_PROTECTION,
                                                 per_second=per_second)
            if low > 0 or high > 0:
                pairs[item["name"]] = (low, high)
        if not pairs:
            continue
        top_low = max(v[0] for v in pairs.values()) or 1.0
        top_high = max(v[1] for v in pairs.values()) or 1.0
        ranked = sorted(pairs.items(), key=lambda kv: -max(kv[1]))[:cap]
        out[god["name"]] = {n: [round(lo / top_low, 3), round(hi / top_high, 3)]
                            for n, (lo, hi) in ranked}
    return out


#: Build-note keys the viewer does not read and the index does not carry.
#: `community_aspects` (`smite.aspect_matches`, 2026-11-08) is evidence for a
#: later session's aspect builds; ~1 KB per god in an index every visitor
#: downloads, with no page that reads it yet. The session that gives it a
#: page removes it from here.
NOT_SHIPPED_BUILD_KEYS = ("community_aspects",)


def build_index(repo_root: Path) -> dict:
    """The whole index, priced with `_weights.yaml`'s pricing flags ON.

    THIS USED TO SET NONE OF THEM. `efficiency`'s pricing switches are module
    globals, `scoring.load_weights` does not set them, and `recommend` and the
    gates call `efficiency.apply_pricing_flags` themselves — so every figure
    here came from the flags-off fit while the builds came from the flags-on
    one. Measured 2026-11-05 at 4130ed90: all 193 shipped residuals matched
    flags-off and none matched flags-on; the tier shown differed from the tier
    the model uses on 59 of 193 items (Rod of Tahuti +267 on screen, -734 in
    the model); `item_gold_values` lacked the three `PASSIVE_SIM_COLUMNS`; and
    `god_item_scores` / `god_item_damage`, which the draft re-ranks with, read
    the same flags-off state. Register §4.10's failure mode.

    The flags are applied for the whole build, not just the first fit:
    `team_fit_items`, the tier list and both draft tables all read the module
    state. They are put back afterwards, because tests call this in-process
    and a leaked switch changes whatever runs next.
    `test_the_index_ships_the_fit_that_chooses_the_builds` pins both.

    WHAT TURNING THEM ON MOVED, against a flags-off rebuild of the same data
    (control fingerprint `4f63ded0872c`). `builds` and every key not listed
    here are unchanged. These moved:
      items        all 193 residuals (median |delta| 152g, max 1,001g); tier
                   on 59 (premium<->fair 36, fair<->undervalued 19, premium
                   -> undervalued 4)
      gold values  all 20 stat prices, the intercept 1,087 -> 891, and the three
                   `PASSIVE_SIM_COLUMNS` added
      draft        `god_item_scores` on all 306 tables (capped membership on
                   292); `god_item_damage` on all 95 gods; the tier list's
                   item entries (191 of 228)
    The draft starts from the shipped core and may only swap
    (viewer `adaptFromCore`), so an EMPTY board is unchanged by construction.
    Under 44 enemy comps (four structured, forty seeded-random, half with
    allies) the adapted six changes membership on 569-622 of 4,180 Conquest
    `core` boards across four seeds (622 on the first; `god_item_scores` alone
    432 of them, `god_item_damage` alone 254), and on 648-953 of 4,180 Joust
    ones. Magi's Cloak arrives ~120 fewer times across both modes and Avatar's
    Parashu 70-160 more, on every seed: Dreamer's Idol, Mantle of Discord and
    Avatar's Parashu entered far more capped pools (Parashu 22 -> 33 gods,
    Rod of Tahuti 25 -> 60) and now out-rank it among the candidates that
    clear the swap bar. Dreamer's Idol's own net arrivals are -102 to +49
    depending on the comps, so no direction is claimed for it.

    THE JOUST FIGURE WAS FIRST PUBLISHED AS 301 (7%), AND THAT WAS WRONG. The
    harness padded Joust boards to five slots, and `deriveThreats` takes the
    roster size from the slot count, so every Joust threat was diluted to
    3/5 of what the viewer's three-slot board computes. Same harness, same
    seed, sized like the viewer: 671. Dreamer's Idol's +117 needed the same
    padding. Found 2026-11-06 re-measuring on 4fc06e3f (#116 merged, control
    fingerprint `fb0eaf0f2496`, coverage unchanged), where #116 moved nothing
    in the index: main's committed index is a fresh flags-off rebuild, byte for
    byte, and the flags-on index is byte-identical to 414e4b18's, so every
    non-draft figure above reproduces exactly.

    RE-TAKEN 2026-11-06 ON d1c6f091, after #117 moved the community window to
    Open Beta 47 (2,859 matches; control `564aa7a9d6a9`, 39.2% / 36.4%), with
    the same harness sized per mode and the same four seeds. Every item-level
    figure above is unchanged, because the efficiency fit reads only the item
    notes and #117 changed none. The draft moves a little, because its scores
    read the window: capped membership changes on 294 tables, not 292, and
    Conquest `core` boards change on 566-666 of 4,180 (666 on the first seed;
    scores alone 500, damage alone 242). Joust is 648-953 again, seed for
    seed, because Joust has no community outcome data to move. Magi's Cloak
    arrives 131-155 fewer times, Avatar's Parashu 104-158 more, and Dreamer's
    Idol -55 to +69."""
    weights = scoring.load_weights(repo_root / "data" / "_weights.yaml")
    before = efficiency.apply_pricing_flags(weights)
    try:
        return _build_index(repo_root, weights)
    finally:
        efficiency.restore_pricing_flags(before)


def _build_index(repo_root: Path, weights: dict) -> dict:
    data_root = repo_root / "data"
    gods_dir = data_root / "Gods"
    items_dir = data_root / "Items"
    builds_dir = repo_root / "data" / "builds"

    def _all(dir_path: Path) -> list:
        if not dir_path.exists():
            return []
        return [notes.read_note(p)[0] for p in recommend.note_paths(dir_path)]

    tags_map = scoring.load_tags(data_root / "_tags.yaml")
    # One fit, reused: the tier list's "ours" item score has to be the same
    # continuous signal the item verdicts came from, not a second independent
    # regression. This used to run twice under a comment claiming it didn't.
    raw_items = _all(items_dir)
    eff, gold_values = ({}, {})
    if efficiency.numeric_cost_items(raw_items):
        eff, gold_values = efficiency.efficiency_scores(raw_items)
    items = _enrich_items(raw_items, tags_map, eff)
    builds = [{k: v for k, v in note.items() if k not in NOT_SHIPPED_BUILD_KEYS}
              for note in _all(builds_dir)]
    gods = _all(gods_dir)
    _enrich_gods(gods, weights)
    _attach_item_meta(items, builds, _load_community_items(data_root))
    _flag_uncatalogued_passives(items, data_root)
    _attach_popular_items(builds)
    index = {"gods": gods, "items": items, "builds": builds,
             # The fitted marginal gold price of each stat, plus the fit's
             # `_intercept` — what every item costs before a single stat is
             # counted. Both are needed for a receipt to add up to
             # predicted_cost. Rounded to 2dp — these are prices, not weights.
             "item_gold_values": {k: round(v, 2) for k, v in sorted(gold_values.items())},
             "god_item_scores": _god_item_scores(gods, builds, items, eff, weights, tags_map),
             # B6: what each item is worth against a squishy vs a tank, for the
             # one surface that knows who you are actually fighting.
             "god_item_damage": _god_item_damage(gods, items, weights),
             # The viewer re-ranks a core client-side and has to apply the same
             # sustain cap the pipeline applied when it assembled one. It used
             # to hand-copy this rule's conditions into TypeScript, where the
             # two could drift silently; shipping the rule keeps one authority.
             "draft": {**weights.get("draft", {}),
                       "lifesteal_caps": weights.get("lifesteal_caps", []),
                       # TEAM-LEVEL TAGS: what the static builds assumed about
                       # teammates, so the draft can replace the assumption
                       # with the teammates it can see (`teamTags.ts`).
                       "team": {**team_config(weights),
                                "fit_items": team_fit_items(gods, builds, items, weights, tags_map)}},
             # The method page states the model's own weights. Shipping them
             # rather than restating them in TSX means the page cannot describe
             # a blend the pipeline stopped using.
             "method": {"signals": weights.get("signals", {}),
                        "kit_blend": weights.get("kit_blend", 0.5),
                        "underrated": weights.get("underrated", {}),
                        # Which passive classes the fit prices. The page used
                        # to restate this in TSX and named two while four were
                        # on — unnoticed, because until this index shipped the
                        # flags-on fit the page showed a fit that priced none.
                        "pricing": {k: bool(weights.get(k)) for k in PRICING_SWITCHES}},
             # Mode order, so the viewer presents Conquest first rather than
             # whatever order the build filenames happened to sort in — which
             # put Arena at the head the moment it was added.
             "modes": list(recommend.MODES),
             # What Joust and Arena may borrow from Conquest's community
             # record, and what they may not: the god page marks the same
             # items in Conquest's most-picked list that the Hybrid refuses.
             "community_transfer": community_transfer(weights),
             "starters": starter_options(weights, builds),
             "roster": _load_roster(data_root),
             "data_updated": _data_updated(gods, builds),
             "tierlist": tierlist.build_tierlist(gods, builds, items, eff),
             "community_source": _community_source(builds),
             # Read snapshots under the vault being indexed, not the module-level
             # default — otherwise a tmp-vault caller (tests) would pick up the
             # real store once snapshots start accumulating.
             "patch_notes": snapshots.report_from_dir(data_root / "Analysis" / "snapshots")}
    data_patch = _load_data_patch(data_root)
    if data_patch:
        index["data_patch"] = data_patch
    return index


def _data_updated(gods, builds) -> str:
    """The most recent last_verified across gods + community builds — the real
    'data scraped on' date, so a rebuild alone doesn't churn the timestamp."""
    dates = [str(g.get("last_verified")) for g in gods if g.get("last_verified")]
    for note in builds:
        for b in note.get("builds", []):
            if b.get("source") == "community" and b.get("last_verified"):
                dates.append(str(b["last_verified"]))
    return max(dates) if dates else ""


def _load_data_patch(data_root: Path):
    """The scraped current SMITE 2 patch string (e.g. "Open Beta 39") from
    data/_patch.json (written by refresh.refresh_patch_version), or None if
    that file doesn't exist or is unreadable/malformed — the viewer omits
    the `data_patch` key entirely rather than showing a fabricated patch."""
    import json
    path = data_root / "_patch.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        patch = data.get("patch") if isinstance(data, dict) else None
        return patch if isinstance(patch, str) else None
    except Exception:
        return None


def _load_roster(data_root: Path) -> list:
    """Full SMITE 2 god roster (name + optional thumb) for the dev add-god
    modal — includes gods not yet tracked. Optional; empty if not fetched."""
    import json
    path = data_root / "_roster.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        return []


def _load_community_items(data_root):
    """The item win/loss table written by `refresh.refresh_item_index`, or {}
    before it has ever run."""
    path = data_root / "_community_items.json"
    if not path.exists():
        return {}
    try:
        return (json.loads(path.read_text(encoding="utf-8")) or {}).get("items") or {}
    except (ValueError, OSError):
        return {}


def _attach_item_meta(items, builds, community_items=None):
    """Per-item community meta.

    Prefers the item index: the item's own record against a real denominator.
    The fallback — the mean of per-god win rates over gods whose community
    build happens to list the item — is unweighted, so an item appearing in
    two builds counted as loudly as one in forty, and it inherits the aspect
    figures the god path already moved away from. `matches` is the tell: where
    it is present the score can be weighed, where it is absent it cannot.
    """
    from collections import defaultdict
    wins = defaultdict(list)
    for note in builds:
        if note.get("mode") != "Conquest":
            continue
        for b in note.get("builds", []):
            if b.get("source") != "community":
                continue
            for slot in b.get("slot_order", []):
                wr = slot.get("win_rate") if isinstance(slot, dict) else None
                if wr is not None:
                    wins[slot["name"]].append(wr)
    for it in items:
        indexed = (community_items or {}).get(it["name"])
        if indexed and indexed.get("matches_played"):
            it["meta"] = {
                "win_avg": round(indexed["win_rate"], 3),
                "matches": indexed["matches_played"],
                "matches_won": indexed.get("matches_won"),
            }
            continue
        vals = wins.get(it["name"])
        if vals:
            it["meta"] = {"win_avg": round(sum(vals) / len(vals), 3), "gods": len(vals)}


def _copy_icons(repo_root: Path, out_path: Path) -> None:
    """Copy every icon file next to the generated index.json so the viewer
    never has to reach outside its own public/ folder — a symlink would be
    fragile on Windows, and Vite's dev server doesn't serve arbitrary
    filesystem paths outside the project by default."""
    src_dir = repo_root / "data" / "_assets" / "icons"
    if not src_dir.exists():
        return
    dest_dir = out_path.parent / "icons"
    dest_dir.mkdir(parents=True, exist_ok=True)
    for icon_path in src_dir.glob("*.png"):
        shutil.copy2(icon_path, dest_dir / icon_path.name)


def _community_source(builds):
    """Provenance for the community comparison: which rank band, drawn from
    how many matches, over what window.

    A win rate without its rank band and dates is not a claim anyone can
    check — "the community" means something different in Obsidian+ than in
    Deity, and a fortnight-old window means something different the week a
    patch lands. Every god carries identical values (they come from one index
    fetch), so this belongs to the index rather than repeated 87 times.

    None before the index scrape has ever run, so the viewer can omit the line
    rather than print an empty one.
    """
    for group in builds:
        for entry in group.get("builds", []):
            if entry.get("source") == "community" and entry.get("god_division"):
                return {
                    "division": entry["god_division"],
                    "window_start": entry.get("god_window_start"),
                    "window_end": entry.get("god_window_end"),
                    "matches_analyzed": entry.get("god_matches_analyzed"),
                }
    return None


def write_index(repo_root: Path, out_path: Path) -> None:
    index = build_index(repo_root)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Frontmatter fields like `last_verified: 2026-07-16` round-trip through
    # yaml.safe_load as datetime.date objects, which json.dumps can't
    # serialize on its own — stringify anything json doesn't natively support.
    out_path.write_text(json.dumps(index, indent=2, default=str), encoding="utf-8")
    _copy_icons(repo_root, out_path)


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[2]
    write_index(repo_root, repo_root / "viewer" / "public" / "index.json")
    print("Wrote viewer/public/index.json")
