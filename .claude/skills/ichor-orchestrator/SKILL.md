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

**Say why it is not a re-run.** `docs/STATE.md` §4 holds eleven refuted
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

The register is the crown jewel: eleven measured negatives that stop the same
work being redone. Protect it. An entry whose evidence does not support its
claim is worse than no entry, because §4 is read as settled.

**Standing backlog** — carried here because sessions lose it:

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
- **The damage model skips basic attacks** (`ability_damage_components` has an
  explicit `continue`) and has no clock — `casts_per_second`,
  `attacks_per_second`, `attack_dps` and `cooldown_multiplier` are calibrated
  and called nowhere. So Attack Speed and Cooldown Rate buy no modelled damage.
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
