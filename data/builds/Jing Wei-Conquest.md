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
    pick_rate: 0.9
    win_rate: 0.55
    alternates:
    - name: Rage
      pick_rate: 0.02
      win_rate: 0.0
    - name: Deathbringer
      pick_rate: 0.02
      win_rate: 1.0
  - name: Dagger of Frenzy
    pick_rate: 0.69
    win_rate: 0.62
    alternates:
    - name: Tyrfing
      pick_rate: 0.1
      win_rate: 0.25
    - name: Demon Blade
      pick_rate: 0.05
      win_rate: 1.0
  - name: The Executioner
    pick_rate: 0.27
    win_rate: 0.91
    alternates:
    - name: Dominance
      pick_rate: 0.24
      win_rate: 0.3
    - name: Qin's Blade
      pick_rate: 0.12
      win_rate: 0.6
  - name: Deathbringer
    pick_rate: 0.21
    win_rate: 0.38
    alternates:
    - name: Dominance
      pick_rate: 0.18
      win_rate: 0.43
    - name: Qin's Blade
      pick_rate: 0.16
      win_rate: 0.83
  - name: Riptalon
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Deathbringer
      pick_rate: 0.22
      win_rate: 0.88
    - name: Qin's Blade
      pick_rate: 0.11
      win_rate: 0.5
  - name: Dominance
    pick_rate: 0.14
    win_rate: 0.75
    alternates:
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 1.0
    - name: Deathbringer
      pick_rate: 0.11
      win_rate: 0.67
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.69
    win_rate: 0.62
  - name: Gilded Arrow
    pick_rate: 0.29
    win_rate: 0.25
  - name: Hunter's Cowl
    pick_rate: 0.02
    win_rate: 1.0
  community_relics:
  - name: Purification Beads
    pick_rate: 0.52
    win_rate: 0.45
  - name: Aegis of Acceleration
    pick_rate: 0.48
    win_rate: 0.6
  starter_sightings:
  - name: Sharpshooter's Arrow
    pick_rate: 0.69
    win_rate: 0.62
  - name: Gilded Arrow
    pick_rate: 0.29
    win_rate: 0.25
  - name: Hunter's Cowl
    pick_rate: 0.02
    win_rate: 1.0
  relic_sightings:
  - name: Purification Beads
    pick_rate: 0.52
    win_rate: 0.45
  - name: Aegis of Acceleration
    pick_rate: 0.48
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/jing-wei/
  last_verified: '2026-11-21'
  god_win_rate: 0.5238095238095238
  god_matches_won: 22
  god_matches_played: 42
  god_division: obsidian
  god_window_start: '2026-11-17'
  god_window_end: '2026-11-21'
  god_matches_analyzed: 3178
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
    pick_rate: 0.98
    win_rate: 0.5105
    matches: 41
    basis: community
  relic:
    name: Purification Beads
    pick_rate: 0.52
    win_rate: 0.45
    matches: 22
    basis: community
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Dagger of Frenzy
  - The Executioner
  - Qin's Blade
  - Dominance
  - Demon Blade
  flex_slots:
  - Dagger of Frenzy
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Demon Blade, Lernaean Bow, Golden Blade, Tekko-Kagi, The Reaper, Hydra''s
    Lament, Musashi''s Dual Swords, Berserker''s Shield, Bloodforge, Barbed Carver,
    Silverbranch Bow, Transcendence, Runeforged Hammer, Odysseus'' Bow, Jotunn''s
    Revenge, Sun Beam Bow, The Crusher, Shield Splitter, Eye of the Storm, Avenging
    Blade, Toxic Blade, Heartseeker, Tyrfing, Rage.'
  slot_scores:
    Lernaean Bow:
      total: 0.53
      efficiency: 0.47
      win: 0.58
      pick: 0.0
      fit: 0.64
    Dagger of Frenzy:
      total: 0.54
      efficiency: 0.42
      win: 0.62
      pick: 0.94
      fit: 0.44
    The Executioner:
      total: 0.6
      efficiency: 0.3
      win: 0.91
      pick: 0.42
      fit: 0.43
    Qin's Blade:
      total: 0.62
      efficiency: 0.39
      win: 0.83
      pick: 0.27
      fit: 0.64
    Dominance:
      total: 0.62
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.64
    Demon Blade:
      total: 0.71
      efficiency: 0.36
      win: 1.0
      pick: 0.07
      fit: 0.87
  community_ordered:
  - Dagger of Frenzy
  - The Executioner
  - Qin's Blade
  - Dominance
  - Demon Blade
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
    pick_rate: 0.98
    win_rate: 0.5105
    matches: 41
    basis: community
  relic: &id002
    name: Purification Beads
    pick_rate: 0.52
    win_rate: 0.45
    matches: 22
    basis: community
- source: suggested
  archetype: mana-stack
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Transcendence
  - Qin's Blade
  - Dominance
  - Demon Blade
  flex_slots:
  - Jotunn's Revenge
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
    The Crusher, Lernaean Bow, Titan''s Bane, Arondight, Silverbranch Bow, Golden
    Blade, Transcendence, Avatar''s Parashu, Toxic Blade, Genji''s Guard, Runeforged
    Hammer, Bloodforge, Barbed Carver, Pendulum Blade, Damaru, Shield Splitter, Eye
    of the Storm, Avenging Blade, Tyrfing, Rage.'
  slot_scores:
    The Executioner:
      total: 0.58
      efficiency: 0.3
      win: 0.91
      pick: 0.42
      fit: 0.26
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.47
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.24
    Qin's Blade:
      total: 0.59
      efficiency: 0.39
      win: 0.83
      pick: 0.27
      fit: 0.42
    Dominance:
      total: 0.6
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.5
    Demon Blade:
      total: 0.66
      efficiency: 0.36
      win: 1.0
      pick: 0.07
      fit: 0.5
  community_ordered:
  - The Executioner
  - Qin's Blade
  - Dominance
  - Demon Blade
  starter: *id001
  relic: *id002
- source: suggested
  archetype: crit
  slot_order:
  - The Executioner
  - Musashi's Dual Swords
  - Qin's Blade
  - Dominance
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Musashi's Dual Swords
  - Deathbringer
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
    this god: Demon Blade, Lernaean Bow, Golden Blade, The Reaper, Musashi''s Dual
    Swords, Hydra''s Lament, Tekko-Kagi, Bloodforge, Berserker''s Shield, Barbed Carver,
    Transcendence, Runeforged Hammer, Silverbranch Bow, Jotunn''s Revenge, The Crusher,
    Odysseus'' Bow, Shield Splitter, Eye of the Storm, Sun Beam Bow, Avenging Blade,
    Heartseeker, Arondight, Tyrfing, Rage.'
  slot_scores:
    The Executioner:
      total: 0.6
      efficiency: 0.3
      win: 0.91
      pick: 0.42
      fit: 0.4
    Musashi's Dual Swords:
      total: 0.48
      efficiency: 0.38
      win: 0.58
      pick: 0.0
      fit: 0.57
    Qin's Blade:
      total: 0.62
      efficiency: 0.39
      win: 0.83
      pick: 0.27
      fit: 0.61
    Dominance:
      total: 0.61
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.6
    Demon Blade:
      total: 0.71
      efficiency: 0.36
      win: 1.0
      pick: 0.07
      fit: 0.88
    Deathbringer:
      total: 0.43
      efficiency: 0.44
      win: 0.38
      pick: 0.35
      fit: 0.57
  community_ordered:
  - The Executioner
  - Qin's Blade
  - Dominance
  - Demon Blade
  - Deathbringer
  starter: *id001
  relic: *id002
- source: suggested
  archetype: bruiser
  slot_order:
  - The Executioner
  - Berserker's Shield
  - Qin's Blade
  - Dominance
  - Demon Blade
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - The Executioner
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
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
      total: 0.58
      efficiency: 0.3
      win: 0.91
      pick: 0.42
      fit: 0.3
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.48
    Qin's Blade:
      total: 0.59
      efficiency: 0.39
      win: 0.83
      pick: 0.27
      fit: 0.47
    Dominance:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.42
    Demon Blade:
      total: 0.66
      efficiency: 0.36
      win: 1.0
      pick: 0.07
      fit: 0.52
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.7
  community_ordered:
  - The Executioner
  - Qin's Blade
  - Dominance
  - Demon Blade
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - The Executioner
  - Qin's Blade
  - The Reaper
  - Dominance
  - Tekko-Kagi
  - Demon Blade
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Demon Blade, The Reaper, Tekko-Kagi, Silverbranch Bow, The Crusher,
    Heartseeker, Titan''s Bane, Jotunn''s Revenge, Toxic Blade, Lernaean Bow, Avatar''s
    Parashu, Avenging Blade, Golden Blade, Hydra''s Lament, Berserker''s Shield, Oath-Sworn
    Spear, Transcendence, Bloodforge, Runeforged Hammer, Barbed Carver, Pendulum Blade,
    Musashi''s Dual Swords, Tyrfing, Rage.'
  slot_scores:
    The Executioner:
      total: 0.63
      efficiency: 0.3
      win: 0.91
      pick: 0.42
      fit: 0.62
    Qin's Blade:
      total: 0.6
      efficiency: 0.39
      win: 0.83
      pick: 0.27
      fit: 0.49
    The Reaper:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.56
    Dominance:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.46
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.69
    Demon Blade:
      total: 0.67
      efficiency: 0.36
      win: 1.0
      pick: 0.07
      fit: 0.58
  community_ordered:
  - The Executioner
  - Qin's Blade
  - Dominance
  - Demon Blade
  starter: *id001
  relic: *id002
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Dagger of Frenzy
  - The Executioner
  - Qin's Blade
  - Dominance
  - Demon Blade
  flex_slots:
  - Dagger of Frenzy
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Demon Blade, Golden Blade, Lernaean Bow, Silverbranch Bow, Hydra''s
    Lament, Tekko-Kagi, The Reaper, Berserker''s Shield, Sun Beam Bow, Bloodforge,
    Transcendence, Barbed Carver, Toxic Blade, Runeforged Hammer, Musashi''s Dual
    Swords, Odysseus'' Bow, Jotunn''s Revenge, The Crusher, Shield Splitter, Eye of
    the Storm, Avenging Blade, Heartseeker, Vital Amplifier, Tyrfing, Rage.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.45
      win: 0.58
      pick: 0.0
      fit: 0.65
    Dagger of Frenzy:
      total: 0.55
      efficiency: 0.42
      win: 0.62
      pick: 0.94
      fit: 0.49
    The Executioner:
      total: 0.6
      efficiency: 0.3
      win: 0.91
      pick: 0.42
      fit: 0.39
    Qin's Blade:
      total: 0.63
      efficiency: 0.39
      win: 0.83
      pick: 0.27
      fit: 0.69
    Dominance:
      total: 0.61
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.55
    Demon Blade:
      total: 0.69
      efficiency: 0.36
      win: 1.0
      pick: 0.07
      fit: 0.71
  community_ordered:
  - Dagger of Frenzy
  - The Executioner
  - Qin's Blade
  - Dominance
  - Demon Blade
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Qin's Blade
  - Dominance
  - Demon Blade
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
    Hammer, Bloodforge, Tekko-Kagi, Barbed Carver, Screeching Gargoyle, Silverbranch
    Bow, Freya''s Tears, Odysseus'' Bow, The Crusher, Eye of Erebus, Tyrfing, Rage.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.53
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.51
    Arondight:
      total: 0.51
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.41
    Qin's Blade:
      total: 0.6
      efficiency: 0.39
      win: 0.83
      pick: 0.27
      fit: 0.48
    Dominance:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.4
    Demon Blade:
      total: 0.66
      efficiency: 0.36
      win: 1.0
      pick: 0.07
      fit: 0.51
  community_ordered:
  - Qin's Blade
  - Dominance
  - Demon Blade
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
    Tekko-Kagi, The Reaper, Hydra''s Lament, Musashi''s Dual Swords, Berserker''s
    Shield, Bloodforge, Barbed Carver, Silverbranch Bow, Transcendence, Runeforged
    Hammer, Odysseus'' Bow, Jotunn''s Revenge, Sun Beam Bow, The Crusher, Shield Splitter,
    Eye of the Storm, Avenging Blade, Toxic Blade, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.45
      win: 0.58
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.53
      efficiency: 0.47
      win: 0.58
      pick: 0.0
      fit: 0.64
    Rage:
      total: 0.24
      efficiency: 0.46
      win: 0.0
      pick: 0.02
      fit: 0.54
    Tyrfing:
      total: 0.42
      efficiency: 0.53
      win: 0.25
      pick: 0.14
      fit: 0.75
    Dominance:
      total: 0.62
      efficiency: 0.47
      win: 0.75
      pick: 0.43
      fit: 0.64
    Demon Blade:
      total: 0.71
      efficiency: 0.36
      win: 1.0
      pick: 0.07
      fit: 0.87
  community_ordered:
  - Rage
  - Tyrfing
  - Dominance
  - Demon Blade
  starter: *id001
  relic: *id002
---
