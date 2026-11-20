---
type: smite-build
god: Jing Wei
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.87
    win_rate: 0.42
    alternates:
    - name: Rage
      pick_rate: 0.03
      win_rate: 0.0
    - name: Deathbringer
      pick_rate: 0.03
      win_rate: 1.0
  - name: Dagger of Frenzy
    pick_rate: 0.63
    win_rate: 0.53
    alternates:
    - name: Tyrfing
      pick_rate: 0.1
      win_rate: 0.0
    - name: Demon Blade
      pick_rate: 0.07
      win_rate: 1.0
  - name: The Executioner
    pick_rate: 0.24
    win_rate: 0.86
    alternates:
    - name: Dominance
      pick_rate: 0.21
      win_rate: 0.0
    - name: Qin's Blade
      pick_rate: 0.14
      win_rate: 0.5
  - name: Dominance
    pick_rate: 0.25
    win_rate: 0.43
    alternates:
    - name: Deathbringer
      pick_rate: 0.21
      win_rate: 0.17
    - name: Silverbranch Bow
      pick_rate: 0.11
      win_rate: 0.33
  - name: Deathbringer
    pick_rate: 0.19
    win_rate: 0.8
    alternates:
    - name: Riptalon
      pick_rate: 0.15
      win_rate: 0.5
    - name: Qin's Blade
      pick_rate: 0.11
      win_rate: 0.33
  - name: Musashi's Dual Swords
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Dominance
      pick_rate: 0.16
      win_rate: 0.67
    - name: Hunter's Bow
      pick_rate: 0.11
      win_rate: 0.5
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.63
    win_rate: 0.42
  - name: Gilded Arrow
    pick_rate: 0.33
    win_rate: 0.3
  - name: Hunter's Cowl
    pick_rate: 0.03
    win_rate: 1.0
  community_relics:
  - name: Purification Beads
    pick_rate: 0.53
    win_rate: 0.31
  - name: Aegis of Acceleration
    pick_rate: 0.47
    win_rate: 0.5
  starter_sightings:
  - name: Sharpshooter's Arrow
    pick_rate: 0.63
    win_rate: 0.42
  - name: Gilded Arrow
    pick_rate: 0.33
    win_rate: 0.3
  - name: Hunter's Cowl
    pick_rate: 0.03
    win_rate: 1.0
  relic_sightings:
  - name: Purification Beads
    pick_rate: 0.53
    win_rate: 0.31
  - name: Aegis of Acceleration
    pick_rate: 0.47
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/jing-wei/
  last_verified: '2026-11-20'
  god_win_rate: 0.4
  god_matches_won: 12
  god_matches_played: 30
  god_division: obsidian
  god_window_start: '2026-11-17'
  god_window_end: '2026-11-20'
  god_matches_analyzed: 2341
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
    pick_rate: 0.96
    win_rate: 0.3788
    matches: 29
    basis: community
  relic:
    name: Purification Beads
    pick_rate: 0.53
    win_rate: 0.31
    matches: 16
    basis: community
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Dagger of Frenzy
  - The Executioner
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Lernaean Bow
  - Golden Blade
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
    this god: Demon Blade, Lernaean Bow, Golden Blade, Tekko-Kagi, The Reaper, Hydra''s
    Lament, Berserker''s Shield, Bloodforge, Barbed Carver, Transcendence, Runeforged
    Hammer, Odysseus'' Bow, Jotunn''s Revenge, Sun Beam Bow, The Crusher, Shield Splitter,
    Eye of the Storm, Avenging Blade, Toxic Blade, Heartseeker, Tyrfing, Rage.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.64
    Dagger of Frenzy:
      total: 0.5
      efficiency: 0.42
      win: 0.53
      pick: 0.86
      fit: 0.44
    The Executioner:
      total: 0.58
      efficiency: 0.3
      win: 0.86
      pick: 0.37
      fit: 0.43
    Demon Blade:
      total: 0.71
      efficiency: 0.36
      win: 1.0
      pick: 0.1
      fit: 0.87
    Deathbringer:
      total: 0.62
      efficiency: 0.44
      win: 0.8
      pick: 0.41
      fit: 0.54
  community_ordered:
  - Dagger of Frenzy
  - The Executioner
  - Demon Blade
  - Deathbringer
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
    pick_rate: 0.96
    win_rate: 0.3788
    matches: 29
    basis: community
  relic: &id002
    name: Purification Beads
    pick_rate: 0.53
    win_rate: 0.31
    matches: 16
    basis: community
- source: suggested
  archetype: mana-stack
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Demon Blade
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Demon
    Blade, Jotunn''s Revenge, Hydra''s Lament, The Reaper, Heartseeker, Tekko-Kagi,
    The Crusher, Lernaean Bow, Titan''s Bane, Arondight, Golden Blade, Transcendence,
    Avatar''s Parashu, Toxic Blade, Genji''s Guard, Runeforged Hammer, Bloodforge,
    Barbed Carver, Pendulum Blade, Damaru, Shield Splitter, Eye of the Storm, Avenging
    Blade, Tyrfing, Rage.'
  slot_scores:
    The Executioner:
      total: 0.55
      efficiency: 0.3
      win: 0.86
      pick: 0.37
      fit: 0.26
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.43
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.66
      efficiency: 0.36
      win: 1.0
      pick: 0.1
      fit: 0.5
    Deathbringer:
      total: 0.59
      efficiency: 0.44
      win: 0.8
      pick: 0.41
      fit: 0.34
  community_ordered:
  - The Executioner
  - Demon Blade
  - Deathbringer
  starter: *id001
  relic: *id002
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Dagger of Frenzy
  - The Executioner
  - Musashi's Dual Swords
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Lernaean Bow
  - Musashi's Dual Swords
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
    this god: Demon Blade, Lernaean Bow, Golden Blade, The Reaper, Hydra''s Lament,
    Tekko-Kagi, Bloodforge, Berserker''s Shield, Barbed Carver, Transcendence, Runeforged
    Hammer, Jotunn''s Revenge, The Crusher, Odysseus'' Bow, Shield Splitter, Eye of
    the Storm, Sun Beam Bow, Avenging Blade, Heartseeker, Arondight, Tyrfing, Rage.'
  slot_scores:
    Lernaean Bow:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Dagger of Frenzy:
      total: 0.49
      efficiency: 0.42
      win: 0.53
      pick: 0.86
      fit: 0.41
    The Executioner:
      total: 0.57
      efficiency: 0.3
      win: 0.86
      pick: 0.37
      fit: 0.4
    Musashi's Dual Swords:
      total: 0.46
      efficiency: 0.38
      win: 0.5
      pick: 0.34
      fit: 0.57
    Demon Blade:
      total: 0.71
      efficiency: 0.36
      win: 1.0
      pick: 0.1
      fit: 0.88
    Deathbringer:
      total: 0.62
      efficiency: 0.44
      win: 0.8
      pick: 0.41
      fit: 0.57
  community_ordered:
  - Dagger of Frenzy
  - The Executioner
  - Musashi's Dual Swords
  - Demon Blade
  - Deathbringer
  starter: *id001
  relic: *id002
- source: suggested
  archetype: bruiser
  slot_order:
  - The Executioner
  - Berserker's Shield
  - Kinetic Cuirass
  - Demon Blade
  - Deathbringer
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Shield of the Phoenix,
    Phoenix Feather, Yogi''s Necklace, Golden Blade, Shield Splitter, Oni Hunter''s
    Garb, Runeforged Hammer, Draconic Scale, The Reaper, Shogun''s Ofuda, Pharaoh''s
    Curse, Erosion, Genji''s Guard, Eye of Providence, Bloodforge, Midgardian Mail,
    Shifter''s Shield, Leviathan''s Hide, Lernaean Bow, Hide of the Nemean Lion, Stone
    of Binding, Ancile, Umbral Link, Avenging Blade, Tyrfing.'
  slot_scores:
    The Executioner:
      total: 0.56
      efficiency: 0.3
      win: 0.86
      pick: 0.37
      fit: 0.3
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.5
    Demon Blade:
      total: 0.66
      efficiency: 0.36
      win: 1.0
      pick: 0.1
      fit: 0.52
    Deathbringer:
      total: 0.58
      efficiency: 0.44
      win: 0.8
      pick: 0.41
      fit: 0.32
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.7
  community_ordered:
  - The Executioner
  - Demon Blade
  - Deathbringer
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - The Executioner
  - The Reaper
  - Tekko-Kagi
  - Demon Blade
  - Deathbringer
  - The Crusher
  flex_slots:
  - Tekko-Kagi
  - The Crusher
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Demon Blade, The Reaper, Tekko-Kagi, The Crusher, Heartseeker, Titan''s
    Bane, Jotunn''s Revenge, Toxic Blade, Lernaean Bow, Avatar''s Parashu, Avenging
    Blade, Golden Blade, Hydra''s Lament, Berserker''s Shield, Oath-Sworn Spear, Transcendence,
    Bloodforge, Runeforged Hammer, Barbed Carver, Pendulum Blade, Tyrfing, Rage.'
  slot_scores:
    The Executioner:
      total: 0.6
      efficiency: 0.3
      win: 0.86
      pick: 0.37
      fit: 0.62
    The Reaper:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.56
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.69
    Demon Blade:
      total: 0.67
      efficiency: 0.36
      win: 1.0
      pick: 0.1
      fit: 0.58
    Deathbringer:
      total: 0.59
      efficiency: 0.44
      win: 0.8
      pick: 0.41
      fit: 0.36
    The Crusher:
      total: 0.49
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.57
  community_ordered:
  - The Executioner
  - Demon Blade
  - Deathbringer
  starter: *id001
  relic: *id002
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Dagger of Frenzy
  - The Executioner
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Golden Blade
  - Lernaean Bow
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
    this god: Demon Blade, Golden Blade, Lernaean Bow, Hydra''s Lament, Tekko-Kagi,
    The Reaper, Berserker''s Shield, Sun Beam Bow, Bloodforge, Transcendence, Barbed
    Carver, Toxic Blade, Runeforged Hammer, Odysseus'' Bow, Jotunn''s Revenge, The
    Crusher, Shield Splitter, Eye of the Storm, Avenging Blade, Heartseeker, Vital
    Amplifier, Tyrfing, Rage.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.55
    Dagger of Frenzy:
      total: 0.5
      efficiency: 0.42
      win: 0.53
      pick: 0.86
      fit: 0.49
    The Executioner:
      total: 0.57
      efficiency: 0.3
      win: 0.86
      pick: 0.37
      fit: 0.39
    Demon Blade:
      total: 0.69
      efficiency: 0.36
      win: 1.0
      pick: 0.1
      fit: 0.71
    Deathbringer:
      total: 0.6
      efficiency: 0.44
      win: 0.8
      pick: 0.41
      fit: 0.41
  community_ordered:
  - Dagger of Frenzy
  - The Executioner
  - Demon Blade
  - Deathbringer
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Hydra's Lament
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
    + fit + win/pick). Underrated for this god: Demon Blade, Jotunn''s Revenge, Hydra''s
    Lament, Arondight, Lernaean Bow, Damaru, Genji''s Guard, Golden Blade, Breastplate
    of Valor, Chandra''s Grace, The Reaper, Berserker''s Shield, Transcendence, Runeforged
    Hammer, Bloodforge, Tekko-Kagi, Barbed Carver, Screeching Gargoyle, Freya''s Tears,
    Odysseus'' Bow, The Crusher, Eye of Erebus, Tyrfing, Rage.'
  slot_scores:
    The Executioner:
      total: 0.56
      efficiency: 0.3
      win: 0.86
      pick: 0.37
      fit: 0.31
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.51
    Arondight:
      total: 0.47
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.41
    Demon Blade:
      total: 0.66
      efficiency: 0.36
      win: 1.0
      pick: 0.1
      fit: 0.51
    Deathbringer:
      total: 0.58
      efficiency: 0.44
      win: 0.8
      pick: 0.41
      fit: 0.3
  community_ordered:
  - The Executioner
  - Demon Blade
  - Deathbringer
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Rage
  - Tyrfing
  - Dominance
  - Demon Blade
  flex_slots:
  - Golden Blade
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Tyrfing, Lernaean Bow, Demon Blade, Golden Blade, Rage,
    Tekko-Kagi, The Reaper, Hydra''s Lament, Berserker''s Shield, Bloodforge, Barbed
    Carver, Transcendence, Runeforged Hammer, Odysseus'' Bow, Jotunn''s Revenge, Sun
    Beam Bow, The Crusher, Shield Splitter, Eye of the Storm, Avenging Blade, Toxic
    Blade, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.64
    Rage:
      total: 0.24
      efficiency: 0.46
      win: 0.0
      pick: 0.03
      fit: 0.54
    Tyrfing:
      total: 0.31
      efficiency: 0.53
      win: 0.0
      pick: 0.14
      fit: 0.75
    Dominance:
      total: 0.48
      efficiency: 0.47
      win: 0.43
      pick: 0.42
      fit: 0.64
    Demon Blade:
      total: 0.71
      efficiency: 0.36
      win: 1.0
      pick: 0.1
      fit: 0.87
  community_ordered:
  - Rage
  - Tyrfing
  - Dominance
  - Demon Blade
  starter: *id001
  relic: *id002
---
