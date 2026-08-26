---
type: smite-build
god: Anhur
mode: Conquest
builds:
- source: community
  aspect: Aspect of Pride
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.7
  slot_order:
  - name: Tyrfing
    pick_rate: 0.56
    win_rate: 0.71
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.19
      win_rate: 0.58
    - name: Avenging Blade
      pick_rate: 0.18
      win_rate: 0.73
  - name: Dagger of Frenzy
    pick_rate: 0.23
    win_rate: 0.64
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.21
      win_rate: 0.54
    - name: Riptalon
      pick_rate: 0.1
      win_rate: 0.67
  - name: The Executioner
    pick_rate: 0.22
    win_rate: 0.69
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.8
    - name: Dominance
      pick_rate: 0.15
      win_rate: 0.67
  - name: Silverbranch Bow
    pick_rate: 0.19
    win_rate: 0.73
    alternates:
    - name: The Executioner
      pick_rate: 0.19
      win_rate: 0.73
    - name: Dominance
      pick_rate: 0.14
      win_rate: 0.75
  - name: Riptalon
    pick_rate: 0.15
    win_rate: 0.63
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.2
      win_rate: 0.73
    - name: Qin's Blade
      pick_rate: 0.11
      win_rate: 0.83
  - name: Hunter's Bow
    pick_rate: 0.11
    win_rate: 0.4
    alternates:
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.67
    - name: Deathbringer
      pick_rate: 0.11
      win_rate: 1.0
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.32
    win_rate: 0.7
  - name: Hunter's Cowl
    pick_rate: 0.23
    win_rate: 0.86
  - name: Death's Embrace
    pick_rate: 0.13
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/anhur/
  last_verified: '2026-08-26'
  god_win_rate: 0.6774193548387096
  god_matches_won: 42
  god_matches_played: 62
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Qin's Blade
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Silverbranch Bow
  - Dominance
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
    this god: Jotunn''s Revenge, Lernaean Bow, Golden Blade, Tekko-Kagi, Demon Blade,
    The Reaper, Hydra''s Lament, Musashi''s Dual Swords, Heartseeker, Damaru, Rage,
    Toxic Blade, Titan''s Bane, The Crusher, Transcendence, Arondight, Runeforged
    Hammer, Berserker''s Shield, Sun Beam Bow, Barbed Carver, Avatar''s Parashu, Bloodforge,
    Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.7
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.71
      pick: 0.56
      fit: 0.71
    Dominance:
      total: 0.6
      efficiency: 0.45
      win: 0.75
      pick: 0.23
      fit: 0.6
    Qin's Blade:
      total: 0.61
      efficiency: 0.37
      win: 0.83
      pick: 0.24
      fit: 0.6
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.53
      win: 0.73
      pick: 0.32
      fit: 0.46
    Deathbringer:
      total: 0.72
      efficiency: 0.51
      win: 1.0
      pick: 0.34
      fit: 0.5
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Dominance
  - Qin's Blade
  - Deathbringer
  flex_slots:
  - Qin's Blade
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Hydra''s Lament, Lernaean Bow, Heartseeker, The Reaper, Tekko-Kagi, Golden
    Blade, Titan''s Bane, The Crusher, Transcendence, Arondight, Musashi''s Dual Swords,
    Demon Blade, Runeforged Hammer, Pendulum Blade, Toxic Blade, Avatar''s Parashu,
    Damaru, Rage, Barbed Carver, Berserker''s Shield, Breastplate of Valor, Genji''s
    Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.7
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.71
      pick: 0.56
      fit: 0.5
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.7
      pick: 0.0
      fit: 0.42
    Dominance:
      total: 0.58
      efficiency: 0.45
      win: 0.75
      pick: 0.23
      fit: 0.5
    Qin's Blade:
      total: 0.58
      efficiency: 0.37
      win: 0.83
      pick: 0.24
      fit: 0.42
    Deathbringer:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.34
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Qin's Blade
  - Musashi's Dual Swords
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Demon Blade
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
    this god: Jotunn''s Revenge, Lernaean Bow, Demon Blade, Golden Blade, Tekko-Kagi,
    The Reaper, Musashi''s Dual Swords, Hydra''s Lament, Heartseeker, Damaru, Rage,
    Toxic Blade, Titan''s Bane, The Crusher, Transcendence, Arondight, Runeforged
    Hammer, Berserker''s Shield, Sun Beam Bow, Barbed Carver, Avatar''s Parashu, Bloodforge,
    Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.7
      pick: 0.0
      fit: 0.28
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.71
      pick: 0.56
      fit: 0.66
    Qin's Blade:
      total: 0.6
      efficiency: 0.37
      win: 0.83
      pick: 0.24
      fit: 0.58
    Musashi's Dual Swords:
      total: 0.56
      efficiency: 0.46
      win: 0.7
      pick: 0.0
      fit: 0.52
    Demon Blade:
      total: 0.57
      efficiency: 0.38
      win: 0.7
      pick: 0.0
      fit: 0.79
    Deathbringer:
      total: 0.72
      efficiency: 0.51
      win: 1.0
      pick: 0.34
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Tyrfing
  - Deathbringer
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, The Reaper, Kinetic Cuirass, Golden Blade, Runeforged Hammer, Freya''s
    Tears, Genji''s Guard, Breastplate of Valor, Shifter''s Shield, Yogi''s Necklace,
    Shield Splitter, Pharaoh''s Curse, Lernaean Bow, Shogun''s Ofuda, Eye of the Storm,
    Phoenix Feather, Erosion, Eye of Providence, Draconic Scale, Chandra''s Grace,
    Hydra''s Lament, Daybreak Gavel, Stone of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.7
      pick: 0.0
      fit: 0.19
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.7
      pick: 0.0
      fit: 0.58
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.71
      pick: 0.56
      fit: 0.49
    Deathbringer:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.34
      fit: 0.32
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.7
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Qin's Blade
  - The Reaper
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - The Reaper
  - Qin's Blade
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
    for this god: Jotunn''s Revenge, The Reaper, Tekko-Kagi, Heartseeker, Titan''s
    Bane, The Crusher, Lernaean Bow, Toxic Blade, Hydra''s Lament, Golden Blade, Avatar''s
    Parashu, Pendulum Blade, Demon Blade, Musashi''s Dual Swords, Oath-Sworn Spear,
    Transcendence, Runeforged Hammer, Arondight, Damaru, Rage, Berserker''s Shield,
    Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.7
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.6
      efficiency: 0.48
      win: 0.71
      pick: 0.56
      fit: 0.54
    Qin's Blade:
      total: 0.59
      efficiency: 0.37
      win: 0.83
      pick: 0.24
      fit: 0.49
    The Reaper:
      total: 0.59
      efficiency: 0.55
      win: 0.7
      pick: 0.0
      fit: 0.55
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.73
      pick: 0.32
      fit: 0.61
    Deathbringer:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.34
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Qin's Blade
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Jotunn's Revenge
  - Dominance
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
    this god: Jotunn''s Revenge, Lernaean Bow, Golden Blade, Tekko-Kagi, The Reaper,
    Hydra''s Lament, Demon Blade, Toxic Blade, Heartseeker, Musashi''s Dual Swords,
    Sun Beam Bow, Titan''s Bane, The Crusher, Transcendence, Damaru, Rage, Runeforged
    Hammer, Berserker''s Shield, Arondight, Barbed Carver, Vital Amplifier, Avatar''s
    Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.7
      pick: 0.0
      fit: 0.22
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.71
      pick: 0.56
      fit: 0.7
    Dominance:
      total: 0.58
      efficiency: 0.45
      win: 0.75
      pick: 0.23
      fit: 0.52
    Qin's Blade:
      total: 0.61
      efficiency: 0.37
      win: 0.83
      pick: 0.24
      fit: 0.65
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.53
      win: 0.73
      pick: 0.32
      fit: 0.5
    Deathbringer:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.34
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Qin's Blade
  - Arondight
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Lernaean Bow, Arondight, The Reaper, Tekko-Kagi, Golden Blade, Heartseeker, Pendulum
    Blade, Breastplate of Valor, Demon Blade, Musashi''s Dual Swords, Genji''s Guard,
    Titan''s Bane, Toxic Blade, The Crusher, Transcendence, Runeforged Hammer, Damaru,
    Berserker''s Shield, Rage, Sun Beam Bow, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.7
      pick: 0.0
      fit: 0.43
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.71
      pick: 0.56
      fit: 0.47
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.7
      pick: 0.0
      fit: 0.5
    Qin's Blade:
      total: 0.59
      efficiency: 0.37
      win: 0.83
      pick: 0.24
      fit: 0.47
    Arondight:
      total: 0.55
      efficiency: 0.5
      win: 0.7
      pick: 0.0
      fit: 0.4
    Deathbringer:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.34
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Tekko-Kagi
  flex_slots:
  - Golden Blade
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
    Underrated for this god: Jotunn''s Revenge, Lernaean Bow, Golden Blade, Tekko-Kagi,
    Demon Blade, The Reaper, Hydra''s Lament, Musashi''s Dual Swords, Heartseeker,
    Damaru, Rage, Toxic Blade, Titan''s Bane, The Crusher, Transcendence, Arondight,
    Runeforged Hammer, Berserker''s Shield, Sun Beam Bow, Barbed Carver, Avatar''s
    Parashu, Bloodforge, Pendulum Blade.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.47
      win: 0.7
      pick: 0.0
      fit: 0.61
    Lernaean Bow:
      total: 0.59
      efficiency: 0.52
      win: 0.7
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.7
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.71
      pick: 0.56
      fit: 0.71
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.63
      pick: 0.32
      fit: 0.57
    Tekko-Kagi:
      total: 0.57
      efficiency: 0.49
      win: 0.7
      pick: 0.0
      fit: 0.55
  starter: *id001
---
