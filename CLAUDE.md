# Working on ichor

**Read [`docs/STATE.md`](docs/STATE.md) before changing anything in the model.**
It is the living doc — current state, design decisions with their evidence, the
negative-results register, and what's left. `docs/specs/` and `docs/plans/` are
dated point-in-time files and are never updated; don't treat them as current.

Five things that are easy to get wrong here, all expanded in that file:

1. **Do not tune against `validate.compute`.** Its "coverage" and Spearman
   targets are both also model inputs, so the objective is maximised by
   deleting the model. Judge model changes with `python -m smite.calibrate`
   (leakage-free coverage against a random-core baseline). Headline coverage
   moving the *other* way is expected and is not by itself a reason to revert.

2. **Check the negative-results register (§4) first.** Twenty-six
   correct-looking improvements have been implemented and measured, and all
   but one shipped off. Re-running them against the old metric will just
   reproduce the old answer. Ten of the twenty-six are *not* "we measured this
   and it is false", and each says on its own line what it is instead. §4.13
   and §4.14 are the first two. **§4.15 is no longer a null at all — `offmap_efficiency` SHIPS
   ON at 0.55 as of 2026-08-22**, and the entry is kept in place as the
   history of how a two-gate disagreement got resolved rather than as a
   reason not to try it. §4.16 is a REFUSAL to write a constant: it says why
   mana cannot be given a fit weight on any evidence available here, and
   measures the exemption that needs none. The three are one story and must
   be read together — §4.16 amends §4.15 on two points, then a third stat
   (Health Regen, on §4.16's two mechanical tests) removed the disagreement
   and let §4.15 ship. **§4.17 is the fifth**, and is §4.16's shape applied to
   the diagnostic rather than to the model: it refuses to collapse
   `build_quality`'s two effective-health channels into one number, and says
   what the pair bounds instead. Read it before "improving" that report by
   averaging them. **§4.18 is the sixth**, and closes the §4.15–§4.16 story:
   it is §4.16's rule running the other way — the first stat the two tests
   REJECTED (Echo) — wrapped around a hypothesis that is right about which
   gods regress and wrong about why. It also says why the role that pays most
   for the off-map charge is not being wronged, so read it before turning that
   charge down for a role. §4.19 is its sequel and a plain null, but it
   corrects one row of §4.16's rule table — a stat `combat.py` prices on the
   TARGET is not a stat any instrument here reads off a build, which is what
   Plating and Dampening turn out to be — and it carries a warning worth more
   than either verdict: **`quality` rank does not decide core membership**, so
   a score-gap argument cannot show a change is safe. Rebuild the cores.
   **§4.20 is the seventh** and is the widest: the passive catalogue
   (`docs/PASSIVES.md`) refuses nine CLASSES of passive at once, each for a
   reason an earlier entry already gives, and names the carve-out to try next.
   Read it before pricing any passive — the class an item belongs to is
   already decided there.

3. **The combat model is exact — keep it that way.** `smite.calibrate_combat`
   must stay at 0.0%. Constants carry evidence tiers, and several deliberately
   contradict published sources because they were measured in-game.

4. **Evidence goes in the module docstring**, next to the code it constrains,
   with the numbers. `docs/STATE.md` is the map and links out; it should not
   accumulate copies of those numbers.

5. **Re-measure the control before you compare it.** The committed
   `data/Analysis/_calibration.md`, and any control quoted in a prompt or a
   commit, goes stale on every `chore(data): daily community refresh`. This has
   caused or nearly caused a misattribution four times, so it is a command and
   not a warning — run this first, and again after your change:

   ```bash
   cd pipeline && python -m smite.calibrate --control
   ```

   ~7s. It prints the random-core baseline, coverage at two FIXED splits, and
   an **input fingerprint** over the item set, the community builds and the
   weights. **The fingerprint is the answer** — if it differs from the one
   stamped in `_calibration.md`, that report and every number quoted from it
   describes different inputs, and the delta you are about to attribute to your
   change is partly theirs.

   Do NOT use a moving baseline as the tell. It was the old proxy for this and
   it has a false-positive mode: the printed figure is a 200-draw sample over a
   pool the model reorders, so it wobbles ±0.15pp for reasons that are not the
   data. `calibrate.exact_random_core_baseline` is the closed form if you need
   to settle it that way.

Commands, tests and the tuning surface are in
[`docs/STATE.md` §6](docs/STATE.md). Use `npm run build`, not `tsc --noEmit` —
the latter misses errors the project reference build catches.
