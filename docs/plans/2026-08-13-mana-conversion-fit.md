# Stat conversion in the item model

_Scope written 2026-08-13. Point-in-time, per `docs/plans/` convention — not
updated after the fact. The living record is `docs/STATE.md`._

## The gap

Four items grant a stat computed from **another stat you already own**. Nothing
in the model can see that, because every signal reads an item's `stats` dict in
isolation and these items' real value is a function of the rest of the build.

| item | rule | sheet | in pools |
|---|---|---|---|
| Transcendence | +Strength = **3% of Mana from Items** | 35 Str, 250 Mana | 15 / 87 |
| Book of Thoth | +Intelligence = **5% of Mana from Items** | 30 Int, 350 Mana | 9 / 87 |
| Rod of Tahuti | +Intelligence = **25% of Intelligence from items** | 80 Int | 25 / 87 |
| Nimble Ring | **per 10 Intelligence**: +1 Attack Damage, +1% Attack Speed | 35 Int | 31 / 87 |

Three of the four appear in **zero** model cores today; Rod of Tahuti reaches 5
of 282. This is what sits underneath the one still-open expert claim.

Not in scope: the ~20 items whose passive computes *damage* from a stat
(Heartseeker, The Crusher, Polynomicon, Silverbranch Bow). Those are a damage
model problem, not a stat-conversion problem, and `damage_value` is where they
would go.

## Two cases, and they are not the same problem

**A. Conversion off a stat the build stacks anyway — LOW RISK.**
A mage builds Intelligence regardless of whether Rod of Tahuti is in the build,
so the conversion is close to deterministic and can be evaluated with almost no
knowledge of the rest of the core.

    magical gods, median Intelligence from items ....... 295
    Rod of Tahuti bonus at that median ................. +74 Intelligence
    against a sheet value of 80 ........................ +92%

Rod of Tahuti is priced at roughly **half** what it is worth to the god buying
it. Nimble Ring is the same shape, converting Intelligence into basic-attack
stats for hybrid scalers.

**B. Conversion off a stat you would only stack BECAUSE of the item —
SELF-REFERENTIAL, HIGH RISK.**
Max Mana is not something a physical carry wants. It is worth stacking only
once Transcendence is in the build, which makes the item's value depend on a
decision that depends on the item's value.

    physical gods, median Max Mana from items .......... 250
    Transcendence bonus at that median ................. +8 Strength  (+21%)

    Ullr's actual community build ...................... 1,550 Mana
      (Transcendence 250 + Hydra's 200 + Jotunn's 250 + Heartseeker 250,
       plus 600 from Transcendence's own 50-stack passive)
    Transcendence bonus there .......................... +46.5 Strength
    effective total .................................... 81.5 Strength, 2.3x sheet

**So the model is not simply wrong to rank Transcendence low in isolation.** At
a generic physical build it really is a +21% item. It is a *build archetype*,
and the thing missing is not a stat weight but the ability to notice that four
items make each other good. That is the same "item pairing" a Masters reviewer
asked for — and unlike community co-occurrence, this instance is derivable
exactly from item text rather than needing match-level data.

## Where it plugs in

`efficiency.item_stat_values` is the single point where an item becomes a vector
of stats, and it already has the `PRICE_*` flag pattern from `price_stacks` and
`price_crit_multipliers`. A conversion term belongs there — but it needs an
argument nothing at that layer has: **the rest of the build**.

Three options, cheapest first.

1. **Reference-build conversion (recommended first step).** Evaluate the
   conversion against a per-god *typical* total — the median Max Mana or
   Intelligence across that god's candidate pool, or across its community
   build. Deterministic, one pass, no fixed point. Prices case A correctly and
   case B conservatively (Transcendence gets its +21%, not its +133%).
2. **Two-pass assembly.** Assemble once, recompute conversions against the
   chosen core, reassemble. Prices case B properly. Risk: it may not converge —
   adding Transcendence raises mana's value, which pulls in more mana items,
   which raises Transcendence further. Needs an explicit iteration cap and a
   convergence test, and both arms must be reported when it oscillates.
3. **Archetype flavor.** Ship a `mana-stack` flavor alongside `crit`, `burst`
   etc., where the conversion is evaluated at full stacks. Sidesteps the fixed
   point entirely by making the archetype an explicit user choice rather than
   something the assembler has to discover. Cheapest honest way to surface
   Ullr's real build.

Option 1 and option 3 are independent and can ship together. Option 2 should
not be attempted until 1 is measured.

## Risk

This is adjacent to **negative result #5** (`price_passives`): pricing passive
grants produced visibly better prices and made the recommender worse. It is
also adjacent to #7 and #8, both of which I measured this session and shipped
off. The prior here is genuinely bad and the scope should be read with that in
mind.

Two things are different this time, and neither is proof:

- The conversion is an **exact arithmetic identity** stated in the item text,
  not an estimate of a conditional effect's uptime.
- `price_crit_multipliers` — the one experiment of this family that shipped ON
  — was also an exact identity from a measured constant, and it improved both
  splits. That is one data point, not a pattern.

## Measurement

`python -m smite.calibrate` at both splits, before and after, with the
random-core baseline stated. `validate --check` as the regression floor and
`calibrate_combat` untouched at 0.0%. The specific per-item checks that make
the result readable:

- Rod of Tahuti's residual and tier, and how many cores hold it (now 5 / 282).
- Transcendence's rank for Ullr (now 21 / 40 in Conquest, 57 in Joust) and its
  residual (now +208).
- `smite.expert_review` — the Ullr claim is the one this is aimed at, and it
  must go from `partial` to `clear` on its own terms, not by the build churning.

Ship OFF if either split regresses, and record it as the next numbered entry in
STATE.md §4 with its numbers. That is the default, not the failure case.

## Effort

Option 1 plus option 3, with tests and a measurement pass: roughly the size of
the `price_stacks` work — one session. Option 2 is its own session and should
not be bundled.
