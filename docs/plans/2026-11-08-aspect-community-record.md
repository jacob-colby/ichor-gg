# The per-aspect community record — verification, depth and handoff (2026-11-08)

A dated, point-in-time file; it is never updated. What is current lives in
`docs/STATE.md` §5 ("The per-aspect community record exists…") and in the
docstring of `pipeline/smite/aspect_matches.py`, which carries the evidence next
to the code it constrains.

This session was DATA, not model. It built the evidence a later session's
aspect builds will stand on, and changed no overlay, no `aspect_kit`, and no
`_weights.yaml` `aspects:` entry.

## 1. The source, verified

`https://smitebrain.com/api/trpc/builds.getBuilds?input={godSlug, role, division, aspect, lastEvaluatedBuildDate}`
is the call behind the builds page's "More Builds" button, read out of the
site's JS bundle (`chunks/D-a4bWz-.js`, tRPC client `/api/trpc`, no
transformer). Each page holds the 10 newest matches before the cursor. The
cursor is the last record's `hz_match_start_timestamp`, and it is exclusive. The
`__data.json` page only ever shows the first 10, and it ignores `page=` and
`offset=`; that is why the feed was first read as a 10-match feed.

| Question | Answer | How it was measured |
|---|---|---|
| Is `player_placement` the win? | **Yes: 1 is a win, 2 a loss.** | **Mirror test:** 14 of 14 enemy records found for six Tsukuyomi matches carry the opposite placement and list Tsukuyomi as an enemy. Within a team all five agree, and two matches mirrored 5 of 5. **The site's own rendering:** it paints `===1` green and anything else red. **Against the aggregate's `matches_won`:** see the next table. |
| How much of the aggregate is in the feed? | 81–96% per god, 85% of aspect matches in both OB46 and OB47 | Feed walked to each window's start, compared with the split index |
| How deep does it go? | About 45 days. Nothing anywhere predates 2026-09-24 17:09Z. | Cursor jumps on Izanami. That date is 45.0 days before the probe and two days into OB44, so it is not a patch boundary. One reading. |
| Does `role=` multiply it? | No. It is a strict subset. | `role=mid` returned exactly 40 of Mangetsu's 72 Master+ matches |
| Is `division` nested? | Yes: `obsidian` ⊇ `master` ⊇ `deity` | Master's 72 Mangetsu matches are all among Obsidian's 73 |
| Does "More Builds" paginate? | Yes, with the cursor above | 319 distinct Tsukuyomi OB47 matches, no duplicate at a page edge |

Feed placement-1 share against the aggregate win rate (OB47, Obsidian+):

| God | Feed share | Aggregate |
|---|---|---|
| Jing Wei | .461 | .446 |
| Atlas | .491 | .456 |
| Aladdin | .618 | .620 |
| Mordred | .644 | .626 |

Read as 1 = loss, these would run the wrong way.

**Formats.** tRPC omits a null key, so `aspect` is absent on a no-aspect record.
Item names drift in case and spacing ("Spear Of The Magus", "Aegis of
Acceleration "), so items are keyed on `detail_href`. Brawler's Ruin carries no
link at all (105 records), so it is slugged from its name. Vulcan's Aspect of
Fortification returns 7 or 8 inventory slots. The Morrigan lists five other
gods' aspects besides her own, because she copies gods. 27% of records hold an
"Empty" slot. Slot numbers are inventory slots, not a confirmed buy order.

**Budget, measured.**
- **Daily:** 217 requests a day: the newest two windows' split index, one
  no-aspect page per god, and every aspect feed walked back to the newest stored
  match. That is about 9 minutes at the 2.5 s floor, on top of the ~100 requests
  the community refresh already sends.
- **Backfill:** 1,636 requests plus 95 discovery pages, at about 2.95 s each
  once latency is included.

## 2. What was built

* **`data/Analysis/aspect_matches/<window>/<god-slug>.jsonl`**: one match per line.
  - Each line holds items, starter and relic as slugs, plus role, rank,
    placement, enemy slugs and timestamp.
  - There are no player names, and the match GUID is hashed (the first 16 hex
    of its SHA-256). The raw GUID links to a public tracker.gg page that names
    all ten players.
  - `_meta.json` holds the window registry, the aspect list per god, and
    `complete_from`. `_aggregate.json` holds the split index per window.
* **The backfill:** OB46 and OB47, complete for all 86 aspect feeds of 81 gods.
  - That is 15,699 matches: 14,889 aspect matches and an 810-match no-aspect
    sample.
  - The full 45 days measured at about 4,770 requests, about 3.9 h. The
    session's limit was 2.5 h, so the cutoff is OB46's start, recorded as
    `complete_from`.
* **`community_aspects:` in every Conquest note** that has an aspect.
  - **Window rule:** the newest patch window, unless it holds fewer than 30 of
    the aspect's matches; then the last closed window; otherwise a stated
    `below minimum` stub.
  - **The floor** is `tierlist.MIN_MATCHES`, imported rather than restated.
  - **Role shift:** said when the 95% Wilson upper bound of the base-role share
    is under one half, and the most-played role is outside the god's base
    role(s).
* **The daily job** gains a "Pull per-aspect match records" step, plus a
  terminal reporter that turns the run red when the feed is refused.
  - The feed is all-or-nothing (`FeedCollapse`), so a refusal leaves the store
    untouched and the next run's walk recovers the missed day.
* **`index.json`** does not carry `community_aspects` (`build_index.NOT_SHIPPED_BUILD_KEYS`).

## 3. Tsukuyomi, the acceptance case

**His entry is a stated `below minimum`:** OB47 has 6 Mangetsu matches, OB46 21.
At about 1.1 matches a day he cannot reach 30 inside one 14-day patch.

**Pooled over the 45 retained days** (from the probe; only OB46 and OB47 are
in the store) it is 73 matches. They are 56% Mid and 27% Jungle, and buy:
- Rod of Tahuti 81%, Book of Thoth 74%, Chronos' Pendant 58% and Obsidian Shard 58%;
- starter: Bluestone Brooch 34%, Archmage's Gem 27%;
- relic: Purification Beads 60%.

**Those 73 matches are 28 players.** One of them played 22 (30%), and the top
three played 49%. His no-aspect OB47 matches are 89% Jungle, on Transcendence,
Heartseeker and Bumba's Hammer.

The record says what Jacob said, Mid on a magical build. Under the repo's own
floor, it does not say it for any single patch.

## 4. Depth: gods × aspect matches stored (2026-11-08)

65 of 86 aspect feeds carry a shown entry: 35 from the newest window and 30
from the last closed one. 21 feeds are below the minimum, and 5 of those are
The Morrigan's copied aspects. **32 of the 65 shown entries are a role shift.**

| God | Aspect | OB47 | OB46 | Entry | Role shift |
|---|---|--:|--:|---|---|
| Nike | Aspect of Victorious Conquest | 202 | 900 | ob47 (newest) | Solo → Jungle |
| Bacchus | Aspect of Revelry | 386 | 659 | ob47 (newest) | Support → Solo |
| Thor | Aspect of Thunderstruck | 163 | 654 | ob47 (newest) | — |
| Aphrodite | Aspect of Heartbreak | 163 | 518 | ob47 (newest) | — |
| Ratatoskr | Aspect of the Thickbark | 211 | 372 | ob47 (newest) | Jungle → Solo |
| Cernunnos | Aspect of Strife | 64 | 515 | ob47 (newest) | — |
| Izanami | Aspect of the Sickle | 543 | 0 | ob47 (newest) | Carry → Mid |
| Hel | Aspect of Divergence | 82 | 332 | ob47 (newest) | — |
| Baron Samedi | Aspect of Hysteria | 124 | 240 | ob47 (newest) | — |
| Kuzenbo | Aspect of Spirits | 140 | 207 | ob47 (newest) | Support → Solo |
| Gilgamesh | Aspect of Shamash | 88 | 247 | ob47 (newest) | — |
| Ishtar | Aspect of the Passionate Storm | 69 | 259 | ob47 (newest) | Carry → Solo |
| Susano | Aspect of the Storm Front | 48 | 272 | ob47 (newest) | Jungle → Support |
| Thanatos | Aspect of Reaping | 85 | 231 | ob47 (newest) | — |
| Athena | Aspect of War | 101 | 208 | ob47 (newest) | Support → Jungle |
| Loki | Aspect of Agony | 63 | 235 | ob47 (newest) | Jungle → Solo |
| Neith | Aspect of Wind | 58 | 217 | ob47 (newest) | — |
| Artio | Aspect of the Denmother | 52 | 215 | ob47 (newest) | — |
| Sol | Aspect of Conflagration | 84 | 178 | ob47 (newest) | — |
| Khepri | Aspect of Laceration | 59 | 191 | ob47 (newest) | — |
| Hachiman | Aspect of the Steel Wind | 84 | 154 | ob47 (newest) | Carry → Jungle |
| Sylvanus | Aspect of Grover's Wrath | 42 | 188 | ob47 (newest) | Support → Solo |
| Morgan Le Fay | Aspect of the Cursed Crown | 69 | 158 | ob47 (newest) | Mid → Solo |
| Ne Zha | Aspect of Righteous Flame | 78 | 146 | ob47 (newest) | Jungle → Support |
| Hou Yi | Aspect of the Mark | 19 | 200 | ob46 (last closed) | — |
| Ares | Aspect of Reverberation | 51 | 160 | ob47 (newest) | — |
| Kukulkan | Aspect of the Squall | 50 | 144 | ob47 (newest) | Mid → Solo |
| Anhur | Aspect of Pride | 51 | 132 | ob47 (newest) | — |
| Ah Puch | Aspect of the Death March | 36 | 144 | ob47 (newest) | Mid → Solo |
| Scylla | Aspect of the Devourer | 49 | 123 | ob47 (newest) | Mid → Support |
| Bastet | Aspect of the Watchful Pride | 47 | 121 | ob47 (newest) | Jungle → Support |
| Nemesis | Aspect of Justice | 40 | 125 | ob47 (newest) | Jungle → Solo |
| Xing Tian | Aspect of Relentless Spite | 29 | 129 | ob46 (last closed) | — |
| Cu Chulainn | Aspect of the Warped | 37 | 112 | ob47 (newest) | — |
| The Morrigan | Aspect of Mischief | 24 | 123 | ob46 (last closed) | Mid → Carry |
| Vulcan | Aspect of Fortification | 37 | 94 | ob47 (newest) | Mid → Solo |
| Kali | Aspect of Unbound Destruction | 24 | 104 | ob46 (last closed) | Jungle → Carry |
| Nox | Aspect of Silent Night | 126 | 0 | ob47 (newest) | — |
| Artemis | Aspect of the Wild | 14 | 96 | ob46 (last closed) | — |
| Eset | Aspect of the Lifewarden | 19 | 82 | ob46 (last closed) | Mid → Support |
| Poseidon | Aspect of the Trident | 44 | 56 | ob47 (newest) | Mid → Carry |
| Xbalanque | Aspect of the Nightstalker | 25 | 71 | ob46 (last closed) | Carry → Mid |
| Guan Yu | Aspect of the General | 14 | 76 | ob46 (last closed) | — |
| Ganesha | Aspect of the Triumphant | 24 | 59 | ob46 (last closed) | — |
| Yemoja | Aspect of Downpour | 5 | 75 | ob46 (last closed) | Support → Mid |
| Sun Wukong | Aspect of Transformation | 26 | 50 | ob46 (last closed) | — |
| Achilles | Aspect of Prowess | 26 | 48 | ob46 (last closed) | — |
| Charon | Aspect of the Tollkeeper | 12 | 60 | ob46 (last closed) | Support → Mid |
| Chiron | Aspect of the Heroic Tutor | 9 | 58 | ob46 (last closed) | — |
| Agni | Aspect of Combustion | 16 | 48 | ob46 (last closed) | Mid → Carry |
| Discordia | Aspect of the Gilded Victor | 15 | 49 | ob46 (last closed) | Mid → Carry |
| Hun Batz | Aspect of Disruption | 18 | 46 | ob46 (last closed) | — |
| Osiris | Aspect of the Fragmented | 18 | 45 | ob46 (last closed) | — |
| Pele | Aspect of Obsidian | 15 | 46 | ob46 (last closed) | Jungle → Solo |
| Merlin | Aspect of Pandemonium | 9 | 51 | ob46 (last closed) | — |
| Chaac | Aspect of Fulmination | 13 | 44 | ob46 (last closed) | — |
| Danzaburou | Aspect of Fellowship | 9 | 47 | ob46 (last closed) | — |
| Ra | Aspect of Thermotherapy | 11 | 44 | ob46 (last closed) | Mid → Support |
| Hecate | Aspect of Ruin | 14 | 39 | ob46 (last closed) | — |
| Ravana | Aspect of the Rakshasa King | 17 | 35 | ob46 (last closed) | — |
| Bellona | Aspect of Vindication | 4 | 40 | ob46 (last closed) | — |
| Apollo | Aspect of Harmony | 17 | 26 | below minimum | |
| Nut | Aspect of the Cosmos | 6 | 37 | ob46 (last closed) | — |
| Fenrir | Aspect of Loyalty | 11 | 31 | ob46 (last closed) | Jungle → Support |
| Sobek | Aspect of Prey | 4 | 38 | ob46 (last closed) | Support → Solo |
| Cabrakan | Aspect of the Rotund Jotunn | 10 | 31 | ob46 (last closed) | — |
| Chronos | Aspect of Relativity | 7 | 28 | below minimum | |
| Cerberus | Aspect of Souls | 6 | 28 | below minimum | |
| Ix Chel | Aspect of the Mother's Light | 10 | 24 | below minimum | |
| Jormungandr | Aspect of the Unyielding | 10 | 24 | below minimum | |
| Mordred | Aspect of Rage | 6 | 23 | below minimum | |
| Nu Wa | Aspect of Shining Mist | 6 | 23 | below minimum | |
| Atlas | Aspect of the Unburdened | 2 | 25 | below minimum | |
| Tsukuyomi | Aspect of Mangetsu | 6 | 21 | below minimum | |
| Amaterasu | Aspect Of Valor | 4 | 18 | below minimum | |
| Cupid | Aspect of Love | 3 | 15 | below minimum | |
| Geb | Aspect of Calamity | 4 | 13 | below minimum | |
| Da Ji | Aspect of Ferocity | 3 | 8 | below minimum | |
| Hercules | Aspect of Preservation | 2 | 9 | below minimum | |
| Horus | Aspect of the Falcon | 1 | 9 | below minimum | |
| Rama | Aspect of Precision | 3 | 7 | below minimum | |
| The Morrigan | Aspect of Agony | 0 | 1 | below minimum | |
| The Morrigan | Aspect of Spirits | 1 | 0 | below minimum | |
| The Morrigan | Aspect of Victorious Conquest | 1 | 0 | below minimum | |
| The Morrigan | Aspect of Laceration | 0 | 0 | below minimum | |
| The Morrigan | Aspect of Thunderstruck | 0 | 0 | below minimum | |

`python -m smite.aspect_matches depth` prints the current table.

## 5. For the session that builds aspect builds from this

**Deep enough to build from: 65 aspects of 65 gods.** In those, at least 30
matches sit in one patch window, which is the floor the tier list already uses.
How the seven hand-typed overlays fare:

| Hand overlay | What the record says |
|---|---|
| Cernunnos, Chiron | Shown, no role shift |
| Agni (Combustion) | Shown; Mid → Carry 79% |
| Ra (Thermotherapy) | Shown; Mid → Support 84% |
| Morgan Le Fay (Cursed Crown) | Shown; Mid → Solo 83% |
| Chronos, Hercules | Below the minimum |

So three of the seven hand overlays describe an aspect whose players are in
another role.

**Can a role-changing aspect be expressed? Not through today's seam.**
1. **The overlay carries only stat weights.** `scoring.derived_aspect_overlay`
   refuses an aspect that flips `is_hybrid_scaler`, because that also changes
   the damage filter, which an overlay cannot say.
2. **A god's role is read from his god note.** `scoring.fit_map` takes
   `god["role"]` as tokens into `role_stats`, and the role table holds 0.7 of
   every offensive column. Nothing in the aspect path changes which role row
   applies. §4.33 measured the consequence for Tsukuyomi: even rewriting his
   whole kit to 1:2 Intelligence reaches only 0.3006.
3. **For Tsukuyomi the damage filter is NOT the barrier.** He is already a
   hybrid scaler (Intelligence share 0.475 ≥ 0.30), so Rod of Tahuti, Book of
   Thoth, Chronos' Pendant, Obsidian Shard, Polynomicon and Spear of Desolation
   all pass it. Four of his shipped archetypes already end in Rod of Tahuti. The
   barrier is the Jungle role row.

The smallest seam that could carry it is a model change, so it is a proposal
and not a recommendation:
- score the aspect build on a variant god whose `role` is the entry's
  `role_shift.role`, the way `aspect_kit.apply` already returns a variant god
  for a kit edit;
- the role would then come from the record, not from a typed constant;
- for a god who is NOT a hybrid scaler, the damage type would have to move as
  well, which is the refusal in point 1. The record's item list is the evidence
  for that, and it is not yet counted by damage type.

It also needs a guard of its own. `model_audit heldout` scores only the base-kit
Conquest `core`, so any aspect build reads `+0.0000` there by construction, and
the frozen reference builds are the only gate.

**What the record cannot tell you.**
- **It counts matches, not players.** Mangetsu's 73 matches are 28 people, and
  one of them played 30%.
- **It is Obsidian+ only.** `rank` is stored, so Master+ (rank ≥ 4400) is
  recoverable.
- **Slots are inventory slots, not purchase order.**

## 6. A lead for the draft feature: per-match matchups

Every stored record carries the five enemy gods and the outcome.
- **Now:** 15,699 records, which is 78,495 god-vs-god outcome pairs, in 9,967
  distinct matches. 3,789 of those matches are seen from two or more gods, and
  they join on the hashed `m`.
- **Accumulation:** about 800 aspect matches a day plus the 810-match
  no-aspect sample, so about 8,000 pairs a day.
- **Bias:** it is skewed to aspect players, so it is not the population.

SmiteBrain also serves a `/gods/[godSlug]/matchups` route, seen in the route
table and not probed. Nothing here builds on either.
