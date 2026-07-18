# SMITE 2 Starter Items Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scrape SMITE 2 starter items, have the recommender pick a role-appropriate starter per god, and show it above the core in the viewer.

**Architecture:** A tunable `starters` block in `_weights.yaml` maps each base starter → its level-20 upgrade + eligible god tokens; `pick_starter(god, weights)` resolves one per god (reusing the flavor `_god_tokens` matcher); `recommend` stamps a `starter` on each suggested build; the viewer renders a STARTER line. Starters are scraped into `Items/` — the existing tier filter keeps them out of core builds.

**Tech Stack:** Python 3.10 (pytest), Vite + React 19 + TS + Vitest.

**Reference spec:** [2026-07-18-smite-starters-design.md](../specs/2026-07-18-smite-starters-design.md)

---

## File Structure
- `tools/smite/scoring.py` — add `pick_starter` (modify).
- `04. System/Data/SMITE/_weights.yaml` — add `starters` block (modify).
- `tools/smite/recommend.py` — stamp `starter` on suggested entries (modify).
- `04. System/Data/SMITE/Items/` — 24 new starter notes (generated).
- `04. System/Data/SMITE/_tags.yaml` — `[]` entries for the 24 starters (modify).
- `viewer/src/types.ts` — optional `starter` on curated entry (modify).
- `viewer/src/components/DetailPanel.tsx` — STARTER line (modify).

No change: `build_index.py`, `notes.merge_suggested_entries` (the `starter` field rides along).

---

### Task S1: `starters` config + `pick_starter`

**Files:**
- Modify: `tools/smite/scoring.py`, `04. System/Data/SMITE/_weights.yaml`
- Test: `tools/smite/tests/test_scoring.py`

- [ ] **Step 1: Write the failing test** (append)

```python
def test_pick_starter_matches_role_and_damage_type():
    weights = scoring.load_weights_default()
    weights["starters"] = [
        {"base": "Gilded Arrow", "upgrade": "Sharpshooter's Arrow",
         "damage_types": ["physical"], "match_any": ["Carry", "Sharpshooter", "Hunter"], "priority": 10},
        {"base": "Conduit Gem", "upgrade": "Archmage's Gem",
         "damage_types": ["magical"], "match_any": ["Mid", "Nuker", "Mage", "Sniper", "Carry"], "priority": 10},
        {"base": "Bumba's Golden Dagger", "upgrade": "Bumba's Spear",
         "damage_types": None, "match_any": ["Jungle", "Slayer", "Assassin"], "priority": 9},
        {"base": "Death's Toll", "upgrade": "Death's Embrace",
         "damage_types": None, "match_any": None, "priority": 1},
    ]
    phys_carry = {"damage_type": "physical", "role": "Carry", "specializations": ["Sharpshooter"]}
    mag_carry = {"damage_type": "magical", "role": "Carry Mid", "specializations": ["Sharpshooter"]}
    jungler = {"damage_type": "physical", "role": "Jungle", "specializations": ["Slayer"]}
    oddball = {"damage_type": "physical", "role": "Support", "specializations": ["Guardian"]}
    assert scoring.pick_starter(phys_carry, weights)["base"] == "Gilded Arrow"
    assert scoring.pick_starter(mag_carry, weights)["base"] == "Conduit Gem"   # magical → not Gilded
    assert scoring.pick_starter(jungler, weights)["base"] == "Bumba's Golden Dagger"
    assert scoring.pick_starter(oddball, weights)["base"] == "Death's Toll"     # default
```

- [ ] **Step 2: Run and confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -k pick_starter -v`

- [ ] **Step 3: Implement `pick_starter`** (append to `scoring.py`)

```python
def pick_starter(god, weights):
    """The role-appropriate starter for a god: highest-priority entry in the
    `starters` config whose damage_types (or null=any) include the god's damage
    type and whose match_any (or null=any) intersects the god's tokens. Returns
    {base, upgrade} or None if no starters are configured."""
    tokens = _god_tokens(god)
    dt = god.get("damage_type")
    best = None
    for s in (weights.get("starters") or []):
        dts = s.get("damage_types")
        if dts and dt not in dts:
            continue
        match_any = s.get("match_any")
        if match_any and not (tokens & set(match_any)):
            continue
        if best is None or s.get("priority", 0) > best.get("priority", 0):
            best = s
    if best is None:
        return None
    return {"base": best["base"], "upgrade": best["upgrade"]}
```

- [ ] **Step 4: Run test to verify PASS**

Run: `cd tools && python -m pytest smite/tests/test_scoring.py -v`

- [ ] **Step 5: Append the `starters` block to `04. System/Data/SMITE/_weights.yaml`**

```yaml

# ── Starters ──────────────────────────────────────────────────────────────
# The recommender stamps one starter per god: the highest-priority entry whose
# damage_types (null = any) include the god's damage type AND whose match_any
# (null = any) intersects the god's tokenized role+specs. Base → level-20
# upgrade pairs verified from the wiki. Death's Toll is the priority-1 default.
starters:
  - {base: Gilded Arrow,          upgrade: Sharpshooter's Arrow, damage_types: [physical], match_any: [Carry, Sharpshooter, Hunter], priority: 10}
  - {base: Conduit Gem,           upgrade: Archmage's Gem,       damage_types: [magical],  match_any: [Mid, Nuker, Mage, Sniper, Carry, Burst], priority: 10}
  - {base: Bumba's Golden Dagger, upgrade: Bumba's Spear,        damage_types: null,       match_any: [Jungle, Slayer, Assassin], priority: 9}
  - {base: Warrior's Axe,         upgrade: Sundering Axe,        damage_types: null,       match_any: [Solo, Warrior, Brawler, Tank, Lockdown], priority: 8}
  - {base: Death's Toll,          upgrade: Death's Embrace,      damage_types: null,       match_any: null, priority: 1}
```

- [ ] **Step 6: Verify per-god resolution on real gods**

Run: `cd tools && python -c "
from smite import scoring, recommend
w = scoring.load_weights(recommend.WEIGHTS_PATH)
for g in recommend.load_gods():
    print(g['name'], '->', scoring.pick_starter(g, w))
"`
Expected: physical carries (Chiron/Cernunnos/Ullr) → Gilded Arrow; magical mids/carries (Agni/Chronos/Morgan/Princess Bari/Ra) → Conduit Gem; Hercules → Warrior's Axe; Susano → Bumba's Golden Dagger. Note anything odd.

- [ ] **Step 7: Commit**

```bash
git add tools/smite/scoring.py tools/smite/tests/test_scoring.py "04. System/Data/SMITE/_weights.yaml"
git commit -m "feat(smite): pick_starter + starters config"
```

---

### Task S2: Scrape the 24 starters into the pool

**Files:** generated — `Items/*.md` (24 starters), icons; `_tags.yaml` (24 `[]` entries)

- [ ] **Step 1: Scrape base + upgraded starters**

Run from `tools/`:
```bash
python -c "
# -*- coding: utf-8 -*-
from smite import refresh
from smite.browser_fetch import BrowserFetcher
STARTERS = ['Selflessness','Leather Cowl','Bluestone Pendant','Vampiric Shroud','War Flag',
  'Conduit Gem','Gilded Arrow','Sands Of Time','Bumba\'s Golden Dagger','Bumba\'s Cudgel',
  \"Warrior's Axe\",\"Death's Toll\",'Heroism','War Banner','Bluestone Brooch','Hunter\'s Cowl',
  'Blood-soaked Shroud','Sharpshooter\'s Arrow','Bumba\'s Spear','Archmage\'s Gem','Sundering Axe',
  \"Death's Embrace\",'Bumba\'s Hammer','Pendulum of the Ages']
f = BrowserFetcher(refresh.DATA_ROOT / '_cache' / 'wiki')
ok, fail = [], []
for n in STARTERS:
    try:
        refresh.refresh_item(n, f); ok.append(n)
    except Exception as e:
        fail.append((n, str(e)[:60]))
refresh.refresh_builds_into()
print(f'{len(ok)} scraped, {len(fail)} failed:', fail)
"
```
Expected: 24 scraped, 0 failed. If any fail on the name form (curly apostrophe / capitalization like "Sands Of Time"), retry with the exact wiki spelling and report.

- [ ] **Step 2: Tag the 24 starters `[]` in `_tags.yaml`**

Append one `Starter Name: []` line per scraped starter (starters aren't selected by effect-tag). Then verify no untagged items remain:
```bash
cd tools && python -c "
from smite import recommend, scoring
tags = scoring.load_tags(recommend.TAGS_PATH)
missing = [i['name'] for i in recommend.load_items() if i['name'] not in tags]
print('untagged:', missing or 'none')
"
```
Expected: `untagged: none`.

- [ ] **Step 3: Confirm starters stay OUT of core builds**

Run: `cd tools && python -c "
from smite import scoring
# tier-1 base + tier-2 upgraded starters are not buildable cores
import pathlib
from smite import notes
for n in ['Gilded Arrow','Sharpshooter\'s Arrow']:
    fm,_ = notes.read_note(pathlib.Path('../04. System/Data/SMITE/Items')/f'{n}.md')
    print(n, 'tier', fm.get('tier'), 'buildable?', scoring.is_buildable(fm))
"`
Expected: both `buildable? False` (tier 1 and 2).

- [ ] **Step 4: Commit**

```bash
git add "04. System/Data/SMITE/Items/" "04. System/Data/SMITE/_assets/" "04. System/Data/SMITE/_tags.yaml"
git commit -m "chore(smite): scrape starter items into the pool"
```

---

### Task S3: Stamp `starter` on suggested builds

**Files:**
- Modify: `tools/smite/recommend.py`
- Test: `tools/smite/tests/test_recommend.py`

- [ ] **Step 1: Write the failing test** (append)

```python
def test_build_suggested_entries_stamps_starter():
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
           "specializations": ["Sharpshooter"]}
    items = [{"name": f"I{i}", "tier": 3, "cost": 2500, "stats": {"Strength": "50"}} for i in range(7)]
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    entries = recommend.build_suggested_entries(god, items, {"builds": []}, weights, {}, "Conquest")
    assert entries[0]["starter"]["base"] == "Gilded Arrow"
    assert entries[0]["starter"]["upgrade"] == "Sharpshooter's Arrow"
    assert all("starter" in e for e in entries)
```

- [ ] **Step 2: Run and confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -k stamps_starter -v`

- [ ] **Step 3: Implement** — in `build_suggested_entries`, compute the starter once and add it to each entry dict. After the `items_by_name = ...` line add:
```python
    starter = scoring.pick_starter(god, weights)
```
and in the appended entry dict add the field:
```python
        entries.append({
            "source": "suggested",
            "archetype": archetype,
            "slot_order": core,
            "situational_swaps": swaps,
            "rationale": _rationale(archetype, rows, profile),
            **({"starter": starter} if starter else {}),
        })
```

- [ ] **Step 4: Run tests to verify PASS**

Run: `cd tools && python -m pytest smite/tests/test_recommend.py -v`

- [ ] **Step 5: Commit**

```bash
git add tools/smite/recommend.py tools/smite/tests/test_recommend.py
git commit -m "feat(smite): stamp role-appropriate starter on suggested builds"
```

---

### Task S4: Viewer STARTER line

**Files:**
- Modify: `viewer/src/types.ts`, `viewer/src/components/DetailPanel.tsx`
- Test: `viewer/src/components/DetailPanel.test.tsx`

- [ ] **Step 1: Update `types.ts`** — add to `CuratedBuildEntry`:
```typescript
  starter?: { base: string; upgrade: string };
```

- [ ] **Step 2: Write the failing test** (append to `DetailPanel.test.tsx`; include the existing `mode`/`onModeChange` props)

```tsx
it("renders the starter line for a build that has one", () => {
  const builds = [{ type: "smite-build", god: "Chiron", mode: "Conquest", builds: [
    { source: "suggested", archetype: "core", slot_order: ["A"], situational_swaps: [],
      rationale: "", starter: { base: "Gilded Arrow", upgrade: "Sharpshooter's Arrow" } },
  ] }];
  render(<DetailPanel god="Chiron" godData={undefined} items={[]} builds={builds as any}
                      mode="Conquest" onModeChange={() => {}} />);
  expect(screen.getByText(/STARTER/i)).toBeInTheDocument();
  expect(screen.getByText("Gilded Arrow")).toBeInTheDocument();
  expect(screen.getByText("Sharpshooter's Arrow")).toBeInTheDocument();
});
```

- [ ] **Step 3: Run and confirm FAIL**

Run: `cd viewer && npx vitest run src/components/DetailPanel.test.tsx`

- [ ] **Step 4: Implement in `DetailPanel.tsx`** — add a STARTER block just before the `<div className="flex gap-6">` slot-order row. Use the same `Tooltip`/`ItemTooltipBody`/`iconSlug` pattern:

```tsx
      {!community && active.starter && (
        <div className="mb-4">
          <div className="mb-2 font-display text-xs font-semibold tracking-widest text-muted">STARTER</div>
          <div className="flex items-center gap-2">
            {[active.starter.base, active.starter.upgrade].map((name, i) => (
              <div key={name} className="flex items-center gap-2">
                {i === 1 && <span className="text-muted">→</span>}
                <Tooltip content={<ItemTooltipBody item={itemsByName.get(name)} name={name} />}>
                  <div className="flex items-center gap-2">
                    <img
                      src={`/icons/${iconSlug(name)}.png`}
                      alt=""
                      className="h-6 w-6 flex-none rounded bg-bg2"
                      onError={(e) => {
                        const img = e.currentTarget;
                        if (img.dataset.retried) { img.style.visibility = "hidden"; return; }
                        img.dataset.retried = "1";
                        img.src = `/icons/${iconSlug(name)}.png?r=${Date.now()}`;
                      }}
                    />
                    <span className="text-sm text-ink">{name}</span>
                  </div>
                </Tooltip>
              </div>
            ))}
          </div>
        </div>
      )}
```
(`active` is already narrowed to a curated entry under `!community`; `itemsByName`, `Tooltip`, `ItemTooltipBody`, `iconSlug` are already in scope.)

- [ ] **Step 5: Run tests + typecheck**

Run: `cd viewer && npx vitest run && npx tsc --noEmit`
Fix any existing DetailPanel test that needs the new prop; keep assertions intact.

- [ ] **Step 6: Commit**

```bash
git add viewer/src/types.ts viewer/src/components/DetailPanel.tsx viewer/src/components/DetailPanel.test.tsx
git commit -m "feat(viewer): show recommended starter above the core"
```

---

### Task S5: Full regen + browser verification

**Files:** generated — `Builds/*.md`, `Analysis/*.md`, `viewer/public/`

- [ ] **Step 1: Regenerate**

Run from `tools/`: `python -m smite.recommend --all` then `python -m smite.build_index`.

- [ ] **Step 2: Verify starters in the index**

Run: `cd .. && python -c "
import json
d=json.load(open('viewer/public/index.json',encoding='utf-8'))
for n in d['builds']:
    if n['mode']=='Conquest':
        core=next((b for b in n['builds'] if b.get('archetype')=='core'), None)
        st=core and core.get('starter')
        print(f\"{n['god']:14} {st}\")
# starters present as items with icons
names={i['name'] for i in d['items']}
assert 'Gilded Arrow' in names and 'Conduit Gem' in names, 'starters missing from items'
print('OK')
"`
Expected: each god shows a sensible {base, upgrade}; starters present in items.

- [ ] **Step 3: Both suites green**

Run: `cd tools && python -m pytest smite/tests/ -q -m "not live"` and `cd ../viewer && npx vitest run`.

- [ ] **Step 4: Browser verify**

Start the dev server, select a few gods, confirm the STARTER line shows the base → upgrade with icons + working tooltips, and that it differs sensibly by role (a mage shows Conduit Gem, a hunter Gilded Arrow). Screenshot. Fix + re-verify if needed.

- [ ] **Step 5: Commit generated output**

```bash
git add "03. Workspaces/Gaming/SMITE 2/Builds/" "04. System/Data/SMITE/Analysis/" viewer/public/
git commit -m "chore(smite): regenerate builds with starters"
```

---

## Self-Review

**Spec coverage:** scrape starters (S2), tunable role→starter config + resolver (S1), stamp on builds (S3), viewer STARTER line (S4), regen + verify (S5). All spec sections mapped.

**Placeholder scan:** none — the `starters` config carries the real verified base→upgrade pairs; the scrape list is the real 24 names.

**Type/name consistency:** `pick_starter(god, weights) → {base, upgrade}` (S1) consumed in `build_suggested_entries` (S3); `starter` field typed in `types.ts` (S4) and read in DetailPanel (S4). `_weights.yaml` `starters[].{base,upgrade,damage_types,match_any,priority}` matches what `pick_starter` reads. Starters land in `Items/` but tier 1/2 → `is_buildable` False → excluded from cores (verified S2 step 3).

**Sequencing:** config+resolver (S1) → scrape (S2) so the resolver's names resolve to real notes → stamp (S3) → viewer (S4) → regen+verify (S5).
