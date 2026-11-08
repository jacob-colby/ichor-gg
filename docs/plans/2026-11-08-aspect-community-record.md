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
| How much of the aggregate is in the feed? | 81–96% per god; 85% of aspect matches in each of OB45, OB46 and OB47, and 71% in OB44, whose first 2.5 days had aged out | Every aspect feed walked to the end of retention, compared with the split index |
| How deep does it go? | A rolling 45 days. Nothing predated 2026-09-24 17:09Z at the first probe, and nothing predated 23:09Z the same day at 23:24Z on 11-08, after the backfill. | Cursor jumps on Izanami, then a walk to a short page. Each floor is 45.0 days before its reading, and both are two days into OB44, so the floor is not a patch boundary. |
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
- **Backfill:** 3,766 requests plus 95 discovery pages, at about 2.95 s each
  once latency is included, with no retries. It ran in two passes: 1,636 for
  OB46 and OB47, then 2,130 for OB45 and OB44.

## 2. What was built

* **`data/Analysis/aspect_matches/<window>/<god-slug>.jsonl`**: one match per line.
  - Each line holds items, starter and relic as slugs, plus role, rank,
    placement, enemy slugs and timestamp.
  - There are no player names, and the match GUID is hashed (the first 16 hex
    of its SHA-256). The raw GUID links to a public tracker.gg page that names
    all ten players.
  - `_meta.json` holds the window registry, the aspect list per god, and
    `complete_from`. `_aggregate.json` holds the split index per window.
* **The backfill:** all 86 aspect feeds of 81 gods walked to the end of
  retention, so OB44 (in part), OB45, OB46 and OB47.
  - That is 36,947 matches: 36,137 aspect matches and an 810-match no-aspect
    sample. 13.0 MB on disk.
  - Every feed ended on a short page. The floor was measured after the last
    feed was walked, at 2026-09-24 23:09:08Z, and recorded as `complete_from`.
    The 69 older records that the earliest-walked feeds still reached were
    dropped, so every feed is cut at the same instant.
  - OB44 carries `partial_from`, because its first 2.5 days had aged out at
    the source. The note header names it.
  - The first pass (OB46 and OB47) fit the 2.5 h limit. The second pass ran
    while the PR waited on #127, and landed as its own data commit.
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
OB45 holds exactly 30, and OB44 17. The rule reaches back one window only,
to the last closed, so OB45 is not read. At about 1.6 matches a day he cannot
count on 30 inside one 14-day patch.

**Pooled over the store's four windows** it is 74 matches. They are 57% Mid
and 27% Jungle, and buy:
- Rod of Tahuti 81%, Book of Thoth 73%, Chronos' Pendant 58% and Obsidian Shard 57%;
- starter: Bluestone Brooch 34%, Archmage's Gem 27%;
- relic: Purification Beads 61%, Aegis of Acceleration 35%.

**The 73 matches the probe could attribute are 28 players** (counted once,
before names were dropped; the store cannot count them). One of them
played 22 (30%), and the top three played 49%. His no-aspect OB47 matches
are 89% Jungle, on Transcendence, Heartseeker and Bumba's Hammer.

The record says what Jacob said, Mid on a magical build. Under the repo's own
floor, it does not say it for any single patch.

## 4. Depth: gods × aspect matches stored (2026-11-08)

65 of 86 aspect feeds carry a shown entry: 35 from the newest window and 30
from the last closed one. 21 feeds are below the minimum, and 5 of those are
The Morrigan's copied aspects. **32 of the 65 shown entries are a role shift.**

Adding OB45 and OB44 changed no entry, because the rule reads only the newest
window and the last closed one. **9 of the 21 below-minimum aspects reach 30
in OB45 or OB44, and 13 reach it pooled.** Several were played far more two
patches ago: Jormungandr 104 in OB45 against 24 in OB46, Chronos 84 against
28. Sorted by the four-window total.

| God | Aspect | OB47 | OB46 | OB45 | OB44 | Entry | Role shift |
|---|---|--:|--:|--:|--:|---|---|
| Thor | Aspect of Thunderstruck | 163 | 654 | 1004 | 714 | ob47 (newest) | — |
| Hel | Aspect of Divergence | 82 | 332 | 963 | 788 | ob47 (newest) | — |
| Cernunnos | Aspect of Strife | 64 | 515 | 671 | 741 | ob47 (newest) | — |
| Bacchus | Aspect of Revelry | 386 | 659 | 521 | 221 | ob47 (newest) | Support → Solo |
| Nike | Aspect of Victorious Conquest | 202 | 900 | 614 | 0 | ob47 (newest) | Solo → Jungle |
| Aphrodite | Aspect of Heartbreak | 163 | 518 | 577 | 0 | ob47 (newest) | — |
| Gilgamesh | Aspect of Shamash | 88 | 247 | 383 | 284 | ob47 (newest) | — |
| Ratatoskr | Aspect of the Thickbark | 211 | 372 | 221 | 169 | ob47 (newest) | Jungle → Solo |
| Thanatos | Aspect of Reaping | 85 | 231 | 269 | 372 | ob47 (newest) | — |
| Baron Samedi | Aspect of Hysteria | 124 | 240 | 244 | 234 | ob47 (newest) | — |
| Athena | Aspect of War | 101 | 208 | 328 | 201 | ob47 (newest) | Support → Jungle |
| Hou Yi | Aspect of the Mark | 19 | 200 | 382 | 207 | ob46 (last closed) | — |
| Ishtar | Aspect of the Passionate Storm | 69 | 259 | 245 | 235 | ob47 (newest) | Carry → Solo |
| Artio | Aspect of the Denmother | 52 | 215 | 287 | 218 | ob47 (newest) | — |
| Ares | Aspect of Reverberation | 51 | 160 | 210 | 347 | ob47 (newest) | — |
| Khepri | Aspect of Laceration | 59 | 191 | 235 | 229 | ob47 (newest) | — |
| Loki | Aspect of Agony | 63 | 235 | 217 | 197 | ob47 (newest) | Jungle → Solo |
| Sol | Aspect of Conflagration | 84 | 178 | 210 | 216 | ob47 (newest) | — |
| Susano | Aspect of the Storm Front | 48 | 272 | 355 | 0 | ob47 (newest) | Jungle → Support |
| Izanami | Aspect of the Sickle | 543 | 0 | 0 | 0 | ob47 (newest) | Carry → Mid |
| Neith | Aspect of Wind | 58 | 217 | 145 | 122 | ob47 (newest) | — |
| Sylvanus | Aspect of Grover's Wrath | 42 | 188 | 199 | 107 | ob47 (newest) | Support → Solo |
| Morgan Le Fay | Aspect of the Cursed Crown | 69 | 158 | 141 | 158 | ob47 (newest) | Mid → Solo |
| Ne Zha | Aspect of Righteous Flame | 78 | 146 | 140 | 139 | ob47 (newest) | Jungle → Support |
| Anhur | Aspect of Pride | 51 | 132 | 145 | 166 | ob47 (newest) | — |
| Xing Tian | Aspect of Relentless Spite | 29 | 129 | 129 | 191 | ob46 (last closed) | — |
| Kukulkan | Aspect of the Squall | 50 | 144 | 124 | 152 | ob47 (newest) | Mid → Solo |
| Hachiman | Aspect of the Steel Wind | 84 | 154 | 120 | 111 | ob47 (newest) | Carry → Jungle |
| Scylla | Aspect of the Devourer | 49 | 123 | 108 | 121 | ob47 (newest) | Mid → Support |
| Kali | Aspect of Unbound Destruction | 24 | 104 | 135 | 137 | ob46 (last closed) | Jungle → Carry |
| Nemesis | Aspect of Justice | 40 | 125 | 144 | 63 | ob47 (newest) | Jungle → Solo |
| Kuzenbo | Aspect of Spirits | 140 | 207 | 0 | 0 | ob47 (newest) | Support → Solo |
| The Morrigan | Aspect of Mischief | 24 | 123 | 81 | 112 | ob46 (last closed) | Mid → Carry |
| Ah Puch | Aspect of the Death March | 36 | 144 | 60 | 95 | ob47 (newest) | Mid → Solo |
| Charon | Aspect of the Tollkeeper | 12 | 60 | 97 | 136 | ob46 (last closed) | Support → Mid |
| Artemis | Aspect of the Wild | 14 | 96 | 91 | 95 | ob46 (last closed) | — |
| Cu Chulainn | Aspect of the Warped | 37 | 112 | 55 | 90 | ob47 (newest) | — |
| Bastet | Aspect of the Watchful Pride | 47 | 121 | 66 | 48 | ob47 (newest) | Jungle → Support |
| Eset | Aspect of the Lifewarden | 19 | 82 | 97 | 76 | ob46 (last closed) | Mid → Support |
| Vulcan | Aspect of Fortification | 37 | 94 | 78 | 48 | ob47 (newest) | Mid → Solo |
| Guan Yu | Aspect of the General | 14 | 76 | 62 | 86 | ob46 (last closed) | — |
| Sun Wukong | Aspect of Transformation | 26 | 50 | 73 | 84 | ob46 (last closed) | — |
| Agni | Aspect of Combustion | 16 | 48 | 85 | 83 | ob46 (last closed) | Mid → Carry |
| Pele | Aspect of Obsidian | 15 | 46 | 89 | 77 | ob46 (last closed) | Jungle → Solo |
| Chaac | Aspect of Fulmination | 13 | 44 | 74 | 87 | ob46 (last closed) | — |
| Poseidon | Aspect of the Trident | 44 | 56 | 54 | 62 | ob47 (newest) | Mid → Carry |
| Yemoja | Aspect of Downpour | 5 | 75 | 78 | 56 | ob46 (last closed) | Support → Mid |
| Achilles | Aspect of Prowess | 26 | 48 | 67 | 70 | ob46 (last closed) | — |
| Xbalanque | Aspect of the Nightstalker | 25 | 71 | 52 | 62 | ob46 (last closed) | Carry → Mid |
| Bellona | Aspect of Vindication | 4 | 40 | 79 | 79 | ob46 (last closed) | — |
| Ganesha | Aspect of the Triumphant | 24 | 59 | 74 | 40 | ob46 (last closed) | — |
| Osiris | Aspect of the Fragmented | 18 | 45 | 43 | 72 | ob46 (last closed) | — |
| Ra | Aspect of Thermotherapy | 11 | 44 | 52 | 65 | ob46 (last closed) | Mid → Support |
| Merlin | Aspect of Pandemonium | 9 | 51 | 41 | 64 | ob46 (last closed) | — |
| Discordia | Aspect of the Gilded Victor | 15 | 49 | 60 | 39 | ob46 (last closed) | Mid → Carry |
| Cabrakan | Aspect of the Rotund Jotunn | 10 | 31 | 53 | 61 | ob46 (last closed) | — |
| Fenrir | Aspect of Loyalty | 11 | 31 | 52 | 57 | ob46 (last closed) | Jungle → Support |
| Hun Batz | Aspect of Disruption | 18 | 46 | 38 | 48 | ob46 (last closed) | — |
| Chiron | Aspect of the Heroic Tutor | 9 | 58 | 31 | 44 | ob46 (last closed) | — |
| Nox | Aspect of Silent Night | 126 | 0 | 0 | 0 | ob47 (newest) | — |
| Nut | Aspect of the Cosmos | 6 | 37 | 39 | 43 | ob46 (last closed) | — |
| Hecate | Aspect of Ruin | 14 | 39 | 33 | 35 | ob46 (last closed) | — |
| Sobek | Aspect of Prey | 4 | 38 | 32 | 21 | ob46 (last closed) | Support → Solo |
| Ravana | Aspect of the Rakshasa King | 17 | 35 | 20 | 21 | ob46 (last closed) | — |
| Danzaburou | Aspect of Fellowship | 9 | 47 | 14 | 20 | ob46 (last closed) | — |
| Jormungandr | Aspect of the Unyielding | 10 | 24 | 104 | 53 | below minimum |  |
| Ix Chel | Aspect of the Mother's Light | 10 | 24 | 54 | 68 | below minimum |  |
| Chronos | Aspect of Relativity | 7 | 28 | 84 | 26 | below minimum |  |
| Mordred | Aspect of Rage | 6 | 23 | 45 | 53 | below minimum |  |
| Nu Wa | Aspect of Shining Mist | 6 | 23 | 46 | 37 | below minimum |  |
| Atlas | Aspect of the Unburdened | 2 | 25 | 37 | 28 | below minimum |  |
| Apollo | Aspect of Harmony | 17 | 26 | 14 | 32 | below minimum |  |
| Cerberus | Aspect of Souls | 6 | 28 | 24 | 27 | below minimum |  |
| Tsukuyomi | Aspect of Mangetsu | 6 | 21 | 30 | 17 | below minimum |  |
| Amaterasu | Aspect Of Valor | 4 | 18 | 14 | 33 | below minimum |  |
| Cupid | Aspect of Love | 3 | 15 | 27 | 7 | below minimum |  |
| Da Ji | Aspect of Ferocity | 3 | 8 | 13 | 14 | below minimum |  |
| Horus | Aspect of the Falcon | 1 | 9 | 10 | 16 | below minimum |  |
| Geb | Aspect of Calamity | 4 | 13 | 6 | 5 | below minimum |  |
| Rama | Aspect of Precision | 3 | 7 | 9 | 4 | below minimum |  |
| Hercules | Aspect of Preservation | 2 | 9 | 6 | 0 | below minimum |  |
| The Morrigan | Aspect of Victorious Conquest | 1 | 0 | 1 | 0 | below minimum |  |
| The Morrigan | Aspect of Agony | 0 | 1 | 0 | 0 | below minimum |  |
| The Morrigan | Aspect of Laceration | 0 | 0 | 1 | 0 | below minimum |  |
| The Morrigan | Aspect of Spirits | 1 | 0 | 0 | 0 | below minimum |  |
| The Morrigan | Aspect of Thunderstruck | 0 | 0 | 1 | 0 | below minimum |  |

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
- **It counts matches, not players.** The 73 Mangetsu matches the probe could
  attribute are 28 people, and one of them played 30%.
- **Whether to pool windows is the first decision.** Pooling would give 13
  more aspects an entry, Tsukuyomi among them, at the cost of mixing patches.
- **It is Obsidian+ only.** `rank` is stored, so Master+ (rank ≥ 4400) is
  recoverable.
- **Slots are inventory slots, not purchase order.**

## 6. A lead for the draft feature: per-match matchups

Every stored record carries the five enemy gods and the outcome.
- **Now:** 36,947 records, which is 184,735 god-vs-god outcome pairs, in
  24,032 distinct matches. 8,969 of those matches are seen from two or more
  gods, and they join on the hashed `m`.
- **Accumulation:** about 800 aspect matches a day plus the 810-match
  no-aspect sample, so about 8,000 pairs a day.
- **Bias:** it is skewed to aspect players, so it is not the population.

SmiteBrain also serves a `/gods/[godSlug]/matchups` route, seen in the route
table and not probed. Nothing here builds on either.
