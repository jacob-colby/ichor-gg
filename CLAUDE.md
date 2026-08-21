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
   commit, goes stale on every `chore(data): daily community refresh`. The
   tell is the **random-core baseline moving** — it cannot depend on any model
   flag, so if it shifted, your control came from a different dataset and the
   delta you are about to attribute to your change is partly the data's. This
   has caused or nearly caused a misattribution four times; twice the session
   caught it only because it noticed the baseline.

Commands, tests and the tuning surface are in
[`docs/STATE.md` §6](docs/STATE.md). Use `npm run build`, not `tsc --noEmit` —
the latter misses errors the project reference build catches.
