---
type: smite-build
god: Ratatoskr
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
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
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Transcendence:
      total: 0.51
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.52
    The Reaper:
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.75
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.74
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.73
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Bluestone Pendant
    upgrade: Bluestone Brooch
    pick_rate: 0.44
    win_rate: 0.6284
    matches: 277
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Purification Beads
    pick_rate: 0.51
    win_rate: 0.61
    matches: 321
    basis: community
    borrowed_from: Conquest
- source: suggested
  archetype: mana-stack
  slot_order:
  - Briskberry Acorn
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  flex_slots:
  - Briskberry Acorn
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: mana-stack (efficiency + fit). Arena — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Briskberry Acorn:
      total: 0.51
      efficiency: 0.73
      win: 0.5
      pick: 0.0
      fit: 0.29
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
    Hydra's Lament:
      total: 0.59
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Reaper:
      total: 0.62
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.72
    Heartseeker:
      total: 0.61
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
  relic: *id002
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Pendulum Blade
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.72
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Reaper:
      total: 0.66
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.81
    Pendulum Blade:
      total: 0.59
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Crusher:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.76
    Avatar's Parashu:
      total: 0.61
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.76
  starter: *id001
  relic: *id002
- source: suggested
  archetype: bruiser
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Ashwhorl Acorn
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.79
      win: 0.5
      pick: 0.0
      fit: 0.44
    Briskberry Acorn:
      total: 0.64
      efficiency: 0.84
      win: 0.5
      pick: 0.0
      fit: 0.44
    Thistlethorn Acorn:
      total: 0.65
      efficiency: 0.81
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.58
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.77
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Pendulum Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Reaper:
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
    Pendulum Blade:
      total: 0.7
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.75
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.74
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.73
      efficiency: 0.45
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
  - Ashwhorl Acorn
  - Tyrfing
  - The Reaper
  - Riptalon
  flex_slots:
  - Golden Blade
  - Ashwhorl Acorn
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.62
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.79
    Toxic Blade:
      total: 0.67
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.9
    Ashwhorl Acorn:
      total: 0.61
      efficiency: 0.73
      win: 0.5
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.66
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.79
    The Reaper:
      total: 0.63
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.69
    Riptalon:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Thistlethorn Acorn
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Pendulum Blade
  flex_slots:
  - Arondight
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Thistlethorn Acorn:
      total: 0.68
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.5
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
    Arondight:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.55
    Pendulum Blade:
      total: 0.62
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Transcendence:
      total: 0.51
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.52
    The Reaper:
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.75
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.74
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.73
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
---
