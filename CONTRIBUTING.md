# Contributing to ichor

Hey, thanks for wanting to help out! Here's the short version of how to get
changes in without any surprises.

## Getting set up

- **Viewer** (the site): `cd viewer && npm install && npm run dev`
- **Pipeline** (the Python model): work from `pipeline/`, e.g.
  `python -m smite.data_audit` to check data integrity.

The [README](README.md) has the full tour of what lives where. For the viewer,
use `npm run build` to check types, not `tsc --noEmit`. The plain `tsc` run
misses errors the project build catches.

## Before you touch the model

Read [`docs/STATE.md`](docs/STATE.md) first. It's long, but it saves a lot of
pain: it records what's been tried, measured, and deliberately left off. A few
things trip people up:

- Don't tune against `validate.compute`. Its targets are also model inputs, so
  you can "win" by deleting the model. Use `python -m smite.calibrate`.
- Check the negative-results register (§4) before re-trying an "obvious"
  improvement. Odds are it's been measured already.
- The combat model is exact. `python -m smite.calibrate_combat` should stay at
  0.0%.
- Re-measure the control before comparing against it:
  `python -m smite.calibrate --control` (about 7s), before and after your change.

## Opening a PR

- One change per PR, please.
- If your PR touches the model, paste the output of
  `python -m smite.model_audit heldout` into the description. A small drop
  (up to 0.01) is fine if you say why. A bigger one blocks the merge.
- If the frozen reference builds move, run
  `python -m smite.model_audit reference --write` and explain each changed line.
- Put the evidence for a change in the module docstring next to the code, with
  the numbers. `docs/STATE.md` is the map, not the place to copy them.

Not sure about something? Open an issue and ask. Happy to chat before you spend
time on it.
