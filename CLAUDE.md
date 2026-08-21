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

2. **Check the negative-results register (§4) first.** Eleven correct-looking
   improvements have been implemented, measured, and shipped off. Re-running
   them against the old metric will just reproduce the old answer.

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
