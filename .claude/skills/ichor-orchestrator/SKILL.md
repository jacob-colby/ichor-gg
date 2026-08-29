---
name: ichor-orchestrator
description: Use when planning, scoping, or reviewing work on ichor across sessions — writing a session prompt, reviewing a finished session's PR or commits, deciding what to work on next, or maintaining the standing backlog. Not for implementing a change yourself; that is what the sessions are for.
---

# Ichor orchestrator

You are the through-line between sessions. Individual sessions implement one
thing well and then lose their context; you carry the product, the backlog, and
the memory of what has already been refuted.

Three jobs: **write the prompt**, **review the result**, **keep the backlog
honest**. You do not implement. If you find yourself editing
`pipeline/smite/*.py`, you have stopped orchestrating — write a prompt instead.

Read `CLAUDE.md` and `docs/STATE.md` before any of the three.

## Session naming

`MM-DD X - Title Case Name` — e.g. `08-21 A - Price Adaptive Stats`.

The letter is **per day**, resetting at midnight: the first session on 08-21 is
`A`, the second `B`. Two sessions with the same letter on different days is
fine and expected. Use the date the session **starts**.

Midnight is **local**, not UTC. `list_sessions` stamps `lastActivityAt` in UTC,
so an evening session reads as the next day there — go by the working day, not
the stamp. Settled 2026-08-21: `G` and `H` stamped `2026-08-22T00:15Z` and
stayed `08-21`, keeping the A–H run on one day.

Name the session for the change it makes, not the symptom it chases —
`Price Adaptive Stats`, not `Fix The Executioner`. The symptom belongs in the
prompt body, where the evidence is.

## Writing a prompt

Sessions are expensive and start cold. A prompt that makes one rediscover
something you already measured has wasted most of its value.

**Carry the numbers.** Every measurement you have made goes in the prompt, with
its date. The single highest-value line in any prompt so far has been a table
of figures the session would otherwise have spent an hour reproducing.

**Say why it is not a re-run.** `docs/STATE.md` §4 holds fourteen refuted
improvements. If the work is adjacent to one, name the entry and say what is
different — otherwise the session either re-runs it or, worse, does not notice.
The strongest form of this argument is precedent: `price_crit_multipliers` and
`price_conversions` were both narrow carve-outs of the refuted `price_passives`
and both shipped ON.

**Order the work and put a checkpoint before the code.** Diagnosis first,
implementation second, and an explicit *"show me before you write model code"*
on anything whose shape is not obvious. The best result of `08-21 B` was a
diagnosis it deliberately did not act on.

**Say what not to do.** Bound the session. Naming the adjacent problem it
should leave alone is as useful as naming the one it should solve.

The standard shape:

```
<one line: what is wrong, in the product's terms>

Read CLAUDE.md and docs/STATE.md first — §1 (the coverage gate is circular)
and §4 (the negative-results register).

<WHAT IS ALREADY TRUE — every number you have, dated, so nothing is
 rediscovered>

<THE FINDING — the measurement that motivates the work>

<WHY THIS IS NOT A RE-RUN of register entry N, if it is adjacent to one>

DO THIS, IN THIS ORDER:
 1. Diagnose. STOP and show me before writing model code.
 2. ...
 3. Measure on both leakage-free splits, report core churn beside coverage.

CONSTRAINTS:
 - It may turn out the model is right. If the evidence says so, record it in
   the register rather than engineering the finding away.
 - combat.calibrate_combat stays at 0.0%; OBSERVED outranks every source.
 - Do not tune against validate.compute.
 - Gates: <current test counts>, validate --check, expert_review --check,
   data_audit.
```

**Never quote a control figure as fixed.** Say *"re-measure the control first;
the tell that yours is stale is the random-core baseline moving"*. Hardcoding
`37.7% / 38.4% vs 5.7%` guarantees a session eventually compares against a
number from a different dataset. See CLAUDE.md rule 5.

## Reviewing a session

**Verify, do not read.** The commit messages in this repo are unusually good,
which is exactly why they should not be trusted on their own. Re-run the
headline measurement yourself. Every review so far that found something found
it by re-running, not by reading.

Standing checklist, in the order things have actually gone wrong:

- **Attribution.** If a headline number moved, did the change move it, or did a
  data refresh? Check whether the random-core baseline moved too.
- **Is the flag wired?** A new pricing flag must go through
  `efficiency.apply_pricing_flags` or `calibrate` and `validate` never see it,
  and the sweep measures the flag OFF at every setting. This has shipped once.
- **Does the knob do anything?** Sweep it. `adaptive_fit` shipped as a float
  that was a boolean; every strength from 0.15 to 1.0 ran one code path, and
  the register recorded a sweep that could not have varied.
- **Was "nothing changed" provable?** `git status` cannot see untracked files,
  and `data/Analysis/*` is untracked. A no-op claim over those needs a real
  diff, not a clean status.
- **Do the gates fail loudly?** A guard that fails OPEN on a typo is worse than
  the bug it replaced. `expert_review.regressions` did, on an unrecognised
  `last_verdict`.
- **Did it claim a rejection that could never fire?** A filter that removes
  candidates already excluded upstream is inert, and saying "no rejected item
  got through" is then true and vacuous.
- **Register hygiene.** A change shipped OFF should have a §4 entry with
  numbers; a §4 entry should name a real flag.
- **Staleness.** STATE.md §7 and PRODUCT.md drift on every refresh. Test
  counts, god counts, coverage, tag coverage.

Report findings with the evidence inline, ranked by whether they change a
conclusion. Distinguish **"this is wrong"** from **"this is right and its
stated reason is wrong"** — the second has been the more common and the more
dangerous, because the reasoning outlives the change.

## Keeping the backlog honest

The register is the crown jewel: fourteen measured negatives that stop the same
work being redone. Protect it. An entry whose evidence does not support its
claim is worse than no entry, because §4 is read as settled.

**Re-check a backlog entry before you put it in a prompt.** Two of these went
stale inside a week and would have sent a session to fix something already
fixed. The check is cheap — grep for the symbol the entry names.

**Standing backlog** — carried here because sessions lose it:

- **RESOLVED 2026-08-22, kept as the worked example.** *Our Carry builds buy
  defence the community never buys.* `offmap_efficiency` shipped at 0.55 with
  `offmap_exempt: [Max Mana, Mana Regen, Health Regen]` and Berserker's Shield
  went 17 of 18 Carry `model` cores to **0 of 18** — re-verified 2026-08-29.
  Carry now reads 14 ahead / 3 behind on raw DPS at +40.3% median with
  effective health LEVEL with the community's. The path that got there is the
  reusable part: a defect found by `build_quality`, a lever measured and
  shipped OFF twice (§4.15, §4.16) because it was too blunt, and shipped only
  once two exemptions made the collateral damage vanish. Three sessions, two
  register entries, one flag.

- **The upstream sample window RESETS, and nothing warns you.** Measured
  2026-08-29: it accumulated 11 Aug to a peak of 18,716 matches on the 25 Aug
  refresh, then restarted — 888, 2,301, 3,498. Daily intake is unchanged and
  `_patch.json` did not move, so this is upstream behaviour, not a patch. The
  model is currently fitting on roughly a **fifth** of the evidence it had,
  which moved the control 43.6/39.4 → 41.3/38.2 with no code change at all.
  **Before attributing any coverage move to anyone's change, check the sample
  size**, not just the fingerprint. `doc_audit`'s "Community sample" row
  computes it.

- **The gates cannot detect a god whose kit was silently blanked.** Measured
  2026-08-29 by `08-29 B`: blanking Ullr's, Artio's and Merlin's kits and
  recomputing moves win-weighted coverage **UP** 0.2pp, `validate --check`
  PASSES, and `data_audit` reports **0** god findings. `audit_gods` checks
  outputs (build present, item count, starter, damage type) and a kitless god
  still gets a build, because `kit_stat_overlay` returns `{}` below 3 abilities
  and fit falls back to the role label. The wiki parser degrades to empty on
  everything except a missing infobox, and `merge_god_note` REPLACES the
  frontmatter — so a silent miss overwrites the only copy. This is why the
  scrape is not scheduled.

- **An item with no community record is handed its god's median win rate**
  (`scoring.god_unknown_win_rate`) and can beat an item carrying a real, lower,
  measured rate. Demonstrated 2026-08-29: Eye of Providence held Geb's slot on
  win 0.55 that was never a measurement, against Genji's Guard's measured 0.50.
  A refresh moved the median to 0.61 and Genji's to 0.64, the order flipped,
  and the objection an expert raised in August cleared by itself. The same
  absence-rendered-as-a-number family as audit finding F2.

  Measured 2026-08-21 by `08-21 H`: the community buys *exactly zero*
  protections across all 18 Carries; we buy a mean 37.8, and it is Berserker's
  Shield (2400g) in **17 of our 18 Carry cores and 0 of 18 community ones**.
  Carry is our weakest damage record of any role (12 ahead / 6 behind) and our
  strongest EHP record (18 / 0, +34.5% median). The protection is physical
  only, so against the magical burst that actually kills a Carry it buys just
  the 200 health (+9.0%, not +34.5%). `defense_affinity` and
  `archetype_scaled_stats` are mechanically excluded (viewer-side only, never
  imported by `scoring`/`assemble`/`recommend`, and `defense_affinity` reads
  0.0 for Carry regardless) — there is no defensive-preference knob to find.

  **Mechanism, verified 2026-08-22: an accounting asymmetry, not an over-valued
  defence.** `efficiency` reads Berserker's Shield at **0.681, residual −425g,
  tier `undervalued`**, while reading the community's own Carry picks as
  premium — The Executioner **+999g** (0.154), Odysseus' Bow **+316g** (0.407).
  That premium is §4.5, the passive nothing prices. Meanwhile `fit` sees only
  **one** of the item's four stats: `item["stats"]` is Attack Speed / Physical
  Protection / Max Health / Health Regen, and a Carry's merged map is Attack
  Speed 1.3 · Critical Chance 1.3 · Strength 0.92 · Lifesteal 0.5 · Penetration
  0.24 · Cooldown Rate 0.18. Physical Protection, Max Health and Health Regen
  are **neither credited nor charged**. So efficiency pays full price for stat
  mass the god cannot use, and fit does not take it back.

  Two cautions when prompting on this. **`efficiency_scores(items)` takes no
  god argument**, so "the same efficiency on all 18 Carries" is true by
  construction — the finding is that a structurally god-agnostic signal
  dominates the blend while the god-specific one is blind to three quarters of
  the item, not that the numbers happened to coincide. And **note the two stat
  key-spaces**: `efficiency.item_stat_values()` returns `Attack Speed %`,
  `item["stats"]` returns `Attack Speed`. Checking fit coverage against the
  pricing keys reports zero overlap and is wrong.

- **Multiplicative items cannot be priced.** Genie's Lamp, Shell of Rebuke's
  `+7.5% of all Stats`, The Executioner's shred. Needs a value model for
  multiplicative effects; three separate sessions have hit it.
- **The efficiency:fit split sits on a plateau and the choice within it is not
  measurable.** Corrected 2026-08-21 — this entry used to read "the `model`
  archetype ranks at 0.70 : 0.30 when 0.45 : 0.55 measures better", and that
  argument has dissolved. The sweep's argmax MOVES with the data: it was
  0.45 : 0.55, and a full run the same week put it at 0.65 : 0.35, which is
  essentially where the model archetype already sits. Both read 38.4%, and
  `calibrate.py`'s own docstring says the whole 0.15–0.65 band is one flat
  plateau with overlapping bootstrap CIs. Do not spend a session moving this
  ratio; there is no evidence to move it toward.
  What survives is the observation underneath: for some gods efficiency and fit
  point at disjoint item sets, and at any split in that band efficiency wins.
  Medusa is the worked example — her top items by efficiency score 0.10–0.40 on
  a fit map that wants Attack Speed 1.30 and Critical Chance 1.30. That is a
  question about the two signals, not about the weight between them.
- **1-stat items have 0% recall** and 42% of every coverage miss is a 1- or
  2-stat item. Register 4.11 found this while exonerating the multi-stat bias.
- **The damage model has no clock, and burst is understated by roughly 8×.**
  Corrected 2026-08-21 — this entry used to read "skips basic attacks and
  `casts_per_second`/`attacks_per_second`/`attack_dps`/`cooldown_multiplier`
  are called nowhere", and most of that is now false. `#34` made the basic
  attack count, and `build_quality` and `damage_value` between them call all
  but `cooldown_multiplier`. What survives: a rotation counts one cast of each
  ability with no basic attacks in the window, no item passives, no follow-up
  and one target, so burst measures a **median 0.12 of the target's own EHP**
  (max 0.72). That is why every kill-or-survival threshold `08-21 H` tested
  came back inert — 0 of 18 on Carry floors, 89 of 89 on Mid/Jungle kills.
  Read that as *this arithmetic cannot evaluate a threshold*, NOT as
  *thresholds do not matter in SMITE*. What would change the answer is the
  §4.12 clock or the passives, and a burst-window constant is §4.12 wearing a
  different name — it would silently become the whole metric.
- **Joust's economy constants are INFERRED**; its wiki page is a stub.
- **The penetration cap value (40) is the weakest number in `_weights.yaml`** —
  pre-2023 SMITE 1 lineage, and SMITE 1 itself moved to 32%.
- **Two thirds of shipped builds rest on no outcome data.** No source for
  per-mode outcomes exists; rechecked 2026-08-10.

## Process

Sessions should **open a PR and stop**, not self-merge — review before merge is
cheaper than review after.

**Say that in the prompt, in words.** It is a rule in this file, which the
session never reads. `08-21 G` finished its work, ran every gate, and left four
files uncommitted with no branch history and no PR, closing with "did not
commit — per the commit-only-when-asked rule." It was right to; nothing had
asked it to. A worktree cleanup would have destroyed the session. End every
prompt with an explicit *"commit to your branch and open a PR; do not merge"*.

Ask each session to close with:

```
WHAT CHANGED · MEASURED (both splits + baseline, control re-run) ·
CORE CHURN · REGISTER ENTRIES ADDED · GATES ·
WHAT I DID NOT DO AND WHY
```

That last field earns its place. The best output of `08-21 B` was a diagnosis
it declined to act on, and the best of `08-21 A` was a list of caps it refused
to add.
