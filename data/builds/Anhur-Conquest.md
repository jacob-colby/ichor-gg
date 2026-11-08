---
type: smite-build
god: Anhur
mode: Conquest
builds:
- source: community
  aspect: Aspect of Pride
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.49
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.81
    win_rate: 0.53
    alternates:
    - name: Tyrfing
      pick_rate: 0.11
      win_rate: 0.45
    - name: Avenging Blade
      pick_rate: 0.05
      win_rate: 0.32
  - name: Dagger of Frenzy
    pick_rate: 0.58
    win_rate: 0.51
    alternates:
    - name: Tyrfing
      pick_rate: 0.11
      win_rate: 0.57
    - name: Toxic Blade
      pick_rate: 0.06
      win_rate: 0.55
  - name: Dominance
    pick_rate: 0.34
    win_rate: 0.52
    alternates:
    - name: The Executioner
      pick_rate: 0.23
      win_rate: 0.59
    - name: Odysseus' Bow
      pick_rate: 0.11
      win_rate: 0.52
  - name: The Executioner
    pick_rate: 0.23
    win_rate: 0.49
    alternates:
    - name: Riptalon
      pick_rate: 0.23
      win_rate: 0.58
    - name: Silverbranch Bow
      pick_rate: 0.14
      win_rate: 0.54
  - name: Silverbranch Bow
    pick_rate: 0.19
    win_rate: 0.56
    alternates:
    - name: Riptalon
      pick_rate: 0.18
      win_rate: 0.55
    - name: Deathbringer
      pick_rate: 0.1
      win_rate: 0.67
  - name: Deathbringer
    pick_rate: 0.13
    win_rate: 0.63
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.11
      win_rate: 0.65
    - name: Manchu Bow
      pick_rate: 0.08
      win_rate: 0.3
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.36
    win_rate: 0.6
  - name: Hunter's Cowl
    pick_rate: 0.22
    win_rate: 0.57
  - name: Gilded Arrow
    pick_rate: 0.17
    win_rate: 0.35
  source_url: https://smitebrain.com/gods/anhur/
  last_verified: '2026-11-08'
  god_win_rate: 0.5089514066496164
  god_matches_won: 199
  god_matches_played: 391
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Silverbranch Bow
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Lernaean Bow, The Reaper, Tekko-Kagi, Golden Blade,
    Demon Blade, Hydra''s Lament, Rage, The Crusher, Toxic Blade, Heartseeker, Qin''s
    Blade, Arondight, Titan''s Bane, Bloodforge, Musashi''s Dual Swords, Barbed Carver,
    Berserker''s Shield, Transcendence, Runeforged Hammer, Avatar''s Parashu, Shield
    Splitter, Eye of the Storm, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.69
    Dominance:
      total: 0.52
      efficiency: 0.47
      win: 0.52
      pick: 0.53
      fit: 0.6
    Riptalon:
      total: 0.51
      efficiency: 0.45
      win: 0.55
      pick: 0.39
      fit: 0.55
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.49
      win: 0.56
      pick: 0.41
      fit: 0.44
    Deathbringer:
      total: 0.53
      efficiency: 0.44
      win: 0.63
      pick: 0.4
      fit: 0.5
  community_ordered:
  - Tyrfing
  - Dominance
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Dominance
  - Hydra's Lament
  - Deathbringer
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Hydra''s Lament, The Reaper, Heartseeker, Tekko-Kagi, The Crusher, Lernaean
    Bow, Titan''s Bane, Arondight, Golden Blade, Toxic Blade, Rage, Transcendence,
    Avatar''s Parashu, Demon Blade, Genji''s Guard, Qin''s Blade, Runeforged Hammer,
    Bloodforge, Barbed Carver, Pendulum Blade, Damaru, Shield Splitter, Eye of the
    Storm, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.45
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.49
    Dominance:
      total: 0.5
      efficiency: 0.47
      win: 0.52
      pick: 0.53
      fit: 0.5
    Hydra's Lament:
      total: 0.49
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.42
    Deathbringer:
      total: 0.51
      efficiency: 0.44
      win: 0.63
      pick: 0.4
      fit: 0.34
  community_ordered:
  - Tyrfing
  - Dominance
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Rage
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Demon Blade
  - Rage
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Reaper, Lernaean Bow, Tekko-Kagi, Demon Blade,
    Hydra''s Lament, Rage, Golden Blade, Toxic Blade, The Crusher, Heartseeker, Qin''s
    Blade, Arondight, Titan''s Bane, Musashi''s Dual Swords, Bloodforge, Berserker''s
    Shield, Barbed Carver, Transcendence, Runeforged Hammer, Avatar''s Parashu, Shield
    Splitter, Eye of the Storm, Avenging Blade.'
  slot_scores:
    Rage:
      total: 0.48
      efficiency: 0.46
      win: 0.53
      pick: 0.0
      fit: 0.52
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.28
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.65
    Dominance:
      total: 0.51
      efficiency: 0.47
      win: 0.52
      pick: 0.53
      fit: 0.55
    Demon Blade:
      total: 0.48
      efficiency: 0.36
      win: 0.53
      pick: 0.0
      fit: 0.79
    Deathbringer:
      total: 0.54
      efficiency: 0.44
      win: 0.63
      pick: 0.4
      fit: 0.52
  community_ordered:
  - Tyrfing
  - Dominance
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    The Reaper, Genji''s Guard, Phoenix Feather, Yogi''s Necklace, Jotunn''s Revenge,
    Shield Splitter, Golden Blade, Freya''s Tears, Runeforged Hammer, Oni Hunter''s
    Garb, Breastplate of Valor, Draconic Scale, Chandra''s Grace, Shogun''s Ofuda,
    Pharaoh''s Curse, Bloodforge, Erosion, Eye of Providence, Midgardian Mail, Hydra''s
    Lament, Shifter''s Shield, Regrowth Striders, Lernaean Bow, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.14
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.47
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.58
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.47
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Tekko-Kagi
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, The Crusher, Heartseeker,
    Toxic Blade, Titan''s Bane, Lernaean Bow, Hydra''s Lament, Avatar''s Parashu,
    Golden Blade, Rage, Pendulum Blade, Demon Blade, Arondight, Qin''s Blade, Oath-Sworn
    Spear, Transcendence, Bloodforge, Runeforged Hammer, Berserker''s Shield, Barbed
    Carver, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.53
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.68
    Riptalon:
      total: 0.52
      efficiency: 0.45
      win: 0.55
      pick: 0.39
      fit: 0.68
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.49
      win: 0.56
      pick: 0.41
      fit: 0.6
    Deathbringer:
      total: 0.51
      efficiency: 0.44
      win: 0.63
      pick: 0.4
      fit: 0.36
  community_ordered:
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Dominance
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Golden Blade, Lernaean Bow, The Reaper, Toxic Blade,
    Tekko-Kagi, Qin''s Blade, Hydra''s Lament, Demon Blade, The Crusher, Rage, Heartseeker,
    Arondight, Titan''s Bane, Berserker''s Shield, Sun Beam Bow, Bloodforge, Transcendence,
    Runeforged Hammer, Barbed Carver, Musashi''s Dual Swords, Avatar''s Parashu, Shield
    Splitter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.22
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.7
    Dominance:
      total: 0.5
      efficiency: 0.47
      win: 0.52
      pick: 0.53
      fit: 0.52
    Riptalon:
      total: 0.51
      efficiency: 0.45
      win: 0.55
      pick: 0.39
      fit: 0.59
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.49
      win: 0.56
      pick: 0.41
      fit: 0.5
    Deathbringer:
      total: 0.52
      efficiency: 0.44
      win: 0.63
      pick: 0.4
      fit: 0.38
  community_ordered:
  - Tyrfing
  - Dominance
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Arondight
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Silverbranch Bow
  - Arondight
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Arondight, The Reaper, Lernaean Bow, Damaru, Genji''s Guard, Tekko-Kagi, The Crusher,
    Golden Blade, Toxic Blade, Heartseeker, Qin''s Blade, Rage, Breastplate of Valor,
    Pendulum Blade, Chandra''s Grace, Titan''s Bane, Demon Blade, Berserker''s Shield,
    Transcendence, Runeforged Hammer, Bloodforge, Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.43
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.45
    Hydra's Lament:
      total: 0.51
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.5
    Arondight:
      total: 0.48
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.4
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.49
      win: 0.56
      pick: 0.41
      fit: 0.3
    Deathbringer:
      total: 0.5
      efficiency: 0.44
      win: 0.63
      pick: 0.4
      fit: 0.29
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - The Reaper
  - Tekko-Kagi
  flex_slots:
  - The Reaper
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Lernaean Bow, The Reaper, Tekko-Kagi,
    Golden Blade, Demon Blade, Hydra''s Lament, Rage, The Crusher, Heartseeker, Qin''s
    Blade, Arondight, Titan''s Bane, Toxic Blade, Bloodforge, Musashi''s Dual Swords,
    Barbed Carver, Berserker''s Shield, Transcendence, Runeforged Hammer, Avatar''s
    Parashu, Shield Splitter, Eye of the Storm, Avenging Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.69
    Dominance:
      total: 0.52
      efficiency: 0.47
      win: 0.52
      pick: 0.53
      fit: 0.6
    The Reaper:
      total: 0.49
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.37
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Dominance
  starter: *id001
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-10-20'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of Pride
    status: shown
    window: ob47
    window_rule: newest
    window_start: '2026-11-03'
    window_end: '2026-11-08'
    matches: 51
    wins: 28
    win_share: 0.55
    aggregate:
      aspect_matches: 62
      aspect_win_rate: 0.5
      no_aspect_matches: 347
      no_aspect_win_rate: 0.507
    roles:
    - role: Carry
      matches: 44
      share: 0.86
    - role: Solo
      matches: 5
      share: 0.1
    - role: Jungle
      matches: 1
      share: 0.02
    - role: Support
      matches: 1
      share: 0.02
    base_role: Carry
    base_role_share: 0.86
    role_shift: null
    items:
    - name: Devourer's Gauntlet
      share: 0.75
    - name: The Executioner
      share: 0.57
    - name: Riptalon
      share: 0.55
    - name: Silverbranch Bow
      share: 0.53
    - name: Dagger of Frenzy
      share: 0.49
    - name: Dominance
      share: 0.49
    - name: Odysseus' Bow
      share: 0.43
    - name: Tyrfing
      share: 0.43
    starters:
    - name: Sharpshooter's Arrow
      share: 0.33
    - name: Hunter's Cowl
      share: 0.29
    - name: Leather Cowl
      share: 0.22
    relics:
    - name: purification-beads
      share: 0.61
    - name: aegis-of-acceleration
      share: 0.37
    - name: agility-relic
      share: 0.02
    matches_by_window:
      ob47: 51
      ob46: 132
    unmapped_slugs:
    - aegis-of-acceleration
    - agility-relic
    - purification-beads
---
