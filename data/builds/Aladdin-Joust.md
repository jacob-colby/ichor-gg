---
type: smite-build
god: Aladdin
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Pendulum Blade
  - The Crusher
  - Titan's Bane
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Pendulum Blade
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.77
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.9
    Pendulum Blade:
      total: 0.64
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.9
    The Crusher:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.79
    Titan's Bane:
      total: 0.63
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Heartseeker:
      total: 0.67
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.89
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
    pick_rate: 0.71
    win_rate: 0.5637
    matches: 293
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Purification Beads
    pick_rate: 0.69
    win_rate: 0.57
    matches: 285
    basis: community
    borrowed_from: Conquest
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Transcendence:
      total: 0.44
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.61
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.61
    Heartseeker:
      total: 0.61
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.57
    Soul Gem:
      total: 0.76
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.99
  starter: *id001
  relic: *id002
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Obsidian Shard
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Heartseeker
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.72
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.78
    Spear of Desolation:
      total: 0.69
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.78
    Obsidian Shard:
      total: 0.59
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.76
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shield of the Phoenix
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shield Splitter
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shield Splitter:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shield of the Phoenix:
      total: 0.66
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.75
    Amanita Charm:
      total: 0.76
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.83
    Erosion:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - The Crusher
  - Titan's Bane
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Titan's Bane
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.79
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.93
    Spear of Desolation:
      total: 0.67
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.74
    The Crusher:
      total: 0.7
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.89
    Titan's Bane:
      total: 0.68
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.89
    Heartseeker:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.99
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Silverbranch Bow
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.61
    Toxic Blade:
      total: 0.63
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.83
    Tyrfing:
      total: 0.62
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.71
    Riptalon:
      total: 0.7
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.95
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.68
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Pendulum Blade
  - Soul Gem
  flex_slots:
  - Pendulum Blade
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Chronos' Pendant:
      total: 0.61
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.65
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.85
    Hydra's Lament:
      total: 0.65
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.75
    Spear of Desolation:
      total: 0.73
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.85
    Pendulum Blade:
      total: 0.62
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.85
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Tyrfing
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Joust
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.72
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.78
    Tyrfing:
      total: 0.62
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Reaper:
      total: 0.7
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.89
    The Crusher:
      total: 0.62
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.74
    Titan's Bane:
      total: 0.61
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.74
    Heartseeker:
      total: 0.65
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
  relic: *id002
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Obsidian Shard
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Heartseeker
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.65
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.69
    Obsidian Shard:
      total: 0.6
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.61
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.76
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Pendulum Blade
  - The Crusher
  - Titan's Bane
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Pendulum Blade
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.77
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.9
    Pendulum Blade:
      total: 0.64
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.9
    The Crusher:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.79
    Titan's Bane:
      total: 0.63
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Heartseeker:
      total: 0.67
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.89
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
---
