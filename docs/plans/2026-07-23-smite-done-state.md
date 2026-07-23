# SMITE 2 Recommender — Road to "Done" Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Take the SMITE 2 build recommender from "12 gods, local, some data gaps" to a shareable, self-updating tool with accurate data, all 89 gods, a tier-list page, and a patch-notes page — against an explicit, checkable quality bar.

**Architecture:** Python scrape/score pipeline (`tools/smite/`) → `viewer/public/index.json` → static Vite/React viewer. This plan adds a data-integrity gate, a batch coverage path, an ops/freshness layer, and two new viewer pages. No architectural rewrite.

**Tech Stack:** Python (Playwright, BeautifulSoup, NNLS), pytest; Vite + React + TS + Tailwind, vitest/RTL.

---

## Quality bar (decided — this is the definition of "done")

A criterion is "done" only when its gate below passes. These are **floors**, checked automatically where possible so they don't regress.

- **Coverage:** 89/89 roster gods each have a Conquest suggested build with ≥5 items including a starter. Zero gods with an empty or failed build.
- **Mechanical item correctness (automated, per item):** every tracked item has a non-null `cost`, a non-null `tier`, and a `stats` block that is either populated or explicitly known-empty (utility glyphs). Zero unexplained blanks.
- **Mechanical build correctness (automated, per god core):** no wrong-damage-type item, includes a starter, 5–6 items, no duplicates → **0 violations**.
- **Recommendation quality (regression guard):** on the validated (has-community) subset, win-weighted coverage **≥ 0.65** AND pooled Spearman **≥ 0.35**. Today's 0.71 / 0.38 clears both; these are floors, not targets — a change may not drop below them.
- **Manual sign-off:** a 10-god spot check across roles; each top build must be defensible to Jacob. This is the subjective final gate over the mechanical ones.
- **Freshness:** auto-refresh runs weekly; the viewer freshness stamp is never > 8 days stale in normal operation. "Up to date with current patch" = within one refresh cycle of live.
- **Access:** a live URL exists, passes a mobile/responsive check, and ≥1 friend has actually loaded it.
- **Pages:** tier-list and patch-notes pages are live and pass their acceptance checks (per-phase below).

---

## File structure (what this plan touches)

- `tools/smite/wiki_parser.py` — cost fallback + glyph-tier capture (Phase 1).
- `tools/smite/data_audit.py` *(new)* — the automated data-sanity guard (Phase 1); reused as a CI-style gate everywhere after.
- `tools/smite/refresh.py` — `--roster-add-all` batch path (Phase 2); per-refresh stat snapshot (Phase 3).
- `tools/smite/snapshots.py` *(new)* — write/read per-patch item-stat snapshots (Phase 3), consumed by the patch-notes page (Phase 5).
- `tools/smite/tierlist.py` *(new)* — god + item ranking aggregation for the tier-list page (Phase 4).
- `viewer/src/…` — TierList page (Phase 4), PatchNotes page (Phase 5), route + nav wiring.
- `04. System/Project Portfolio.md` — done-state entry (Phase 0).
- `04. System/Data/SMITE/Analysis/` — audit + validation reports (generated).

---

## Phase 0 — Lock the done-state (cheap, prevents scope drift)

### Task 0.1: Write the done-state into the Project Portfolio

**Files:** Modify `04. System/Project Portfolio.md` (SMITE entry).

- [ ] Add a "Done when" block to the SMITE project entry listing the eight gates above verbatim, plus a one-line status per gate (❌/🟡/🟢 as of today).
- [ ] Commit: `docs(smite): pin done-state criteria in Project Portfolio`.

---

## Phase 1 — Data integrity & accuracy (gates everything downstream)

Wrong item costs = wrong efficiency = wrong "strong" builds, so this runs **before** the 77-god scrape (so new scrapes are captured correctly). Two confirmed parser bugs + a permanent guard.

### Task 1.1: Fix starter/base cost parsing (the blank-gold bug)

**Root cause:** starter pages populate a `Cost:` infobox row (e.g. 600) and leave `Total Cost:` blank; the parser reads only `Total Cost`. 13 items land `cost: null` and drop out of efficiency scoring.

**Files:**
- Modify: `tools/smite/wiki_parser.py:186` (the `Total Cost` branch).
- Test: `tools/smite/tests/test_wiki_parser.py`.

- [ ] **Step 1: Write the failing test.** Add a fixture infobox with a `Cost: 600` row and an empty `Total Cost:` row (mirroring Bluestone Pendant); assert `parse_item_page(html)["cost"] == 600`. Add a second case where both exist (`Cost: 800`, `Total Cost: 2600`) and assert it takes **2600** (total wins when present).
- [ ] **Step 2: Run it, confirm it fails** on the starter case (`cost is None`).
- [ ] **Step 3: Implement.** Capture both labels while iterating rows (`total_cost` from `Total Cost`, `base_cost` from `Cost`), then after the loop: `result["cost"] = total_cost if total_cost is not None else base_cost`.
- [ ] **Step 4: Run the test, confirm pass.**
- [ ] **Step 5: Commit:** `fix(smite): fall back to Cost when Total Cost is blank (starters)`.

### Task 1.2: Capture glyph/non-numeric tiers

**Root cause:** `Item Type: Glyph` (e.g. Blinking Abyss) doesn't match `Tier (\d)`, so `tier: null`.

**Files:** Modify `tools/smite/wiki_parser.py:183-185`; Test: `test_wiki_parser.py`.

- [ ] **Step 1: Failing test** — infobox `Item Type: Glyph`; assert `parse_item_page(html)["tier"] == "Glyph"` (string tier is acceptable for non-numeric tiers).
- [ ] **Step 2: Confirm fail** (`tier is None`).
- [ ] **Step 3: Implement** — if `Tier (\d)` matches, use the int; else fall back to the trailing type word (`Starter`/`Glyph`) from the `Item Type` text. Keep int tiers as ints.
- [ ] **Step 4: Confirm pass.** Also assert the existing `Tier 3` case still returns int `3` (no regression).
- [ ] **Step 5: Commit:** `fix(smite): capture glyph/starter item tiers`.

### Task 1.3: Automated data-audit guard

**Files:** Create `tools/smite/data_audit.py`; Test: `tools/smite/tests/test_data_audit.py`.

- [ ] **Step 1: Failing test** — feed a list of item dicts containing one blank-cost, one null-tier, and one absurd stat (`Max Health: 99999`); assert `audit_items(items)` returns a findings list naming each.
- [ ] **Step 2: Confirm fail** (function undefined).
- [ ] **Step 3: Implement** `audit_items(items)` → findings for: null/blank `cost`; null `tier`; empty `stats` on a non-glyph; stat value non-numeric, negative, or > 1000; tier-3 cost outside 1800–3600; duplicate names. Add `audit_gods(gods)` → gods with no suggested build / build < 5 items / missing starter / wrong-damage-type item. Add a `main()` that loads `index.json`, prints findings, exits non-zero if any.
- [ ] **Step 4: Confirm pass.**
- [ ] **Step 5: Commit:** `feat(smite): data_audit guard for item/build integrity`.

### Task 1.4: Re-scrape all items + regenerate, verify audit is clean

**Files:** generated data + reports (no code).

- [ ] Re-scrape tracked items with the fixed parser: `python -m smite.refresh --all` (from `tools/`).
- [ ] Recompute + reindex: `python -m smite.recommend --all` then `python -m smite.build_index`.
- [ ] Run the guard: `python -m smite.data_audit` — resolve every finding (expect the 13 costs now populated, Blinking Abyss tier set). Spot-check the 3700-cost tier-3 outlier against the live wiki; correct or whitelist.
- [ ] Confirm efficiency scores now exist for the 13 formerly-blank starters (they should carry an `efficiency_tier`).
- [ ] Run full suites (`pytest -m "not live"`, `npm run build`), commit generated data: `chore(smite): regenerate with corrected item costs/tiers`.

**Phase 1 gate:** `data_audit` exits 0 on items; the two mechanical item gates pass.

---

## Phase 2 — Full roster coverage (12 → 89)

### Task 2.1: Batch "add every roster god" path

**Files:** Modify `tools/smite/refresh.py` (new `--roster-add-all` flag wrapping the existing per-god `manage_gods.add` path); Test: `test_refresh.py`.

- [ ] **Step 1: Failing test** — mock the roster + add path; assert `--roster-add-all` calls add once per untracked roster god and skips already-tracked ones.
- [ ] **Step 2: Confirm fail.**
- [ ] **Step 3: Implement** — read `_roster.json`, diff against tracked gods, loop the untracked through the existing add flow with the fetcher's pacing (Cloudflare-safe), continue-on-error collecting failures, print a summary. **Log any god that fails to scrape — no silent drops.**
- [ ] **Step 4: Confirm pass.**
- [ ] **Step 5: Commit:** `feat(smite): batch-add all roster gods`.

### Task 2.2: Run the batch, fix fit-map gaps it exposes

**Files:** `04. System/Data/SMITE/_tags.yaml`, `_weights.yaml` (fit/token maps); generated data.

- [ ] Run `--roster-add-all` (expect long Playwright runtime; may need re-runs for Cloudflare failures — the continue-on-error summary drives retries).
- [ ] Run `data_audit` on gods; for each god flagged (no build / wrong-damage item / weak fit), extend the token/fit maps in the sidecars (new gods will surface gaps the current 12 never did).
- [ ] Recompute + reindex + re-run audit until `audit_gods` is clean.
- [ ] Commit config + generated data in logical chunks.

### Task 2.3: Validation regression gate

**Files:** possibly `tools/smite/validate.py` (add a `--check` mode that exits non-zero below floors); Test: `test_validate.py`.

- [ ] **Step 1: Failing test** — `validate.compute` on a stub below floors; assert `check_thresholds(agg)` returns False with the failing metric named.
- [ ] **Step 2–4:** implement `check_thresholds` (win-weighted ≥ 0.65, Spearman ≥ 0.35), wire a `--check` CLI exit code, confirm pass.
- [ ] Run live validation on all 89; confirm it clears the floors. If it doesn't, run `calibrate.py` and re-check.
- [ ] **Step 5: Commit:** `feat(smite): validation threshold gate`.

**Phase 2 gate:** 89/89 gods build; `audit_gods` clean; validation `--check` passes; manual 10-god spot check signed off.

---

## Phase 3 — Ship it live + keep it fresh + start accruing patch history

### Task 3.1: Deploy + responsive gate

- [ ] Host `viewer/` per [DEPLOY.md](viewer/DEPLOY.md) (Vercel/Cloudflare Pages, root `viewer`, build `npm run build`, output `dist`). Record the live URL in the Portfolio entry.
- [ ] Browser-verify the live URL at mobile (375px) and desktop widths — nav, Gods/Items tabs, a god page, and a build all usable on mobile. Fix any responsive breaks in the viewer, redeploy.
- [ ] Share with ≥1 friend; confirm they loaded it (satisfies the access gate).

### Task 3.2: Per-refresh stat snapshot (patch-notes prerequisite — start now so history accrues)

**Files:** Create `tools/smite/snapshots.py`; call it from `refresh_and_deploy.py`; Test: `test_snapshots.py`.

- [ ] **Step 1: Failing test** — `write_snapshot(items, date)` writes `Analysis/snapshots/<date>.json` with `{name: {cost, tier, stats}}`; `diff_snapshots(old, new)` returns per-item stat/cost deltas + added/removed items.
- [ ] **Step 2–4:** implement, confirm pass.
- [ ] Hook `write_snapshot` into `refresh_and_deploy` so every patch refresh records one. Commit. **This produces no user-visible change yet — it silently banks the history Phase 5 needs.**
- [ ] **Step 5: Commit:** `feat(smite): snapshot item stats each refresh`.

### Task 3.3: Enable weekly auto-refresh

- [ ] On the canonical git device only (see Vault Hygiene), add the weekly `refresh_and_deploy` cron from DEPLOY.md §"Keeping data fresh automatically". Verify Playwright runs headless there first.
- [ ] Confirm one end-to-end run: scrape → recompute → index → snapshot → audit → commit → push → host redeploys.

**Phase 3 gate:** live URL loads on mobile; a friend used it; cron runs weekly; snapshots accumulating.

---

## Phase 4 — Tier-list page (data mostly exists; needs a short design pass)

> Needs its own brief design note before implementation (ranking formula for gods, tie-breaks, community-vs-ours toggle semantics). Task outline:

- [ ] `tools/smite/tierlist.py` — aggregate a god ranking (from per-god scoring) and an item ranking (from efficiency + community pick/win); emit into `index.json` as `tierlist: {gods:[…], items:[…]}` with both an "ours" score and a "community" score per entry. TDD.
- [ ] `data_audit` extension: tier-list entries cover all gods/items.
- [ ] Viewer `TierList` page at `#/tiers`: S/A/B/C tier buckets, toggle **Community ↔ Our calc**, filter by role/damage/tier. Reuse existing filter helpers. TDD (vitest/RTL).
- [ ] Nav button; browser-verify both toggle modes; `npm run build` clean.

**Phase 4 gate:** page live, both ranking modes populated for all gods + items, filters work, mobile-usable.

---

## Phase 5 — Patch-notes page (depends on Phase 3 snapshots)

> Needs its own brief design note (how many patches back, buff/nerf classification thresholds). Requires ≥2 snapshots to diff, so it ships after history has accrued. Task outline:

- [ ] `tools/smite/snapshots.py` — `build_patch_report(snapshots)` → per-patch list of changed items with before/after cost + per-stat deltas, classified buff/nerf/mixed. Emit into `index.json` as `patch_notes: […]`. TDD.
- [ ] Viewer `PatchNotes` page at `#/patch`: most-recent-patch summary, per-item before→after stat rows with buff/nerf coloring, collapsible older patches. TDD.
- [ ] Nav button; browser-verify against a real two-snapshot diff; `npm run build` clean.

**Phase 5 gate:** page live, shows real before/after diffs from accrued snapshots, buff/nerf classification correct on a spot check.

---

## Phase 6 — Final done verification

- [ ] Run `data_audit` (items + gods) → 0 findings.
- [ ] Run `validate --check` → passes floors.
- [ ] Manual 10-god spot check signed off.
- [ ] Live URL: mobile + desktop pass; Gods/Items/Tiers/Patch pages all load; friend confirmed.
- [ ] Update the Portfolio done-state: all eight gates 🟢. Move SMITE to `_Completed/` per the portfolio convention.
- [ ] Update project memory (`project_smite_recommender.md`) with the final state.

---

## Notes / self-review

- **Spec coverage vs. the six user criteria:** strong-builds-all-gods → Phases 1+2; friends-use-easily → Phase 3.1; god/item/mode stats in calc → already largely done, hardened by Phase 1 (correct costs) and gated by `data_audit`; up-to-date-with-patches → Phase 3.3; patch-notes page → Phase 5; tier-list page → Phase 4. All six covered.
- **Sequencing rationale:** data integrity precedes the 77-god scrape (so it's captured right once); snapshots start in Phase 3 so Phase 5 has history to diff; deploy is early (Phase 3.1) so "friends use it" becomes real before the long tail.
- **Two features deferred to their own design pass:** tier-list and patch-notes pages have genuine design questions (ranking formula, buff/nerf thresholds) — outlined here, specced when reached rather than fabricated now.
- **Mode coverage:** "modes in calculations" is scoped to Conquest + Joust (existing). Arena/Assault are explicitly out of "done" unless you say otherwise.
