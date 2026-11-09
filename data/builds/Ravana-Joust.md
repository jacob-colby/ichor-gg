---
type: smite-build
god: Ravana
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
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
      total: 0.62
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.58
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.69
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: &id001
    base: Leather Cowl
    upgrade: Hunter's Cowl
    pick_rate: 0.39
    win_rate: 0.5015
    matches: 105
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Blink Rune
    pick_rate: 0.31
    win_rate: 0.51
    matches: 83
    basis: community
    borrowed_from: Conquest
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Hydra's Lament
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
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
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.52
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.37
    Transcendence:
      total: 0.39
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.28
    Hydra's Lament:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.49
    Heartseeker:
      total: 0.54
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
  relic: *id002
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.51
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.62
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.56
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.39
    The Crusher:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.5
    Heartseeker:
      total: 0.53
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
  relic: *id002
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Runeforged Hammer
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
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shield Splitter:
      total: 0.56
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.54
    Shield of the Phoenix:
      total: 0.67
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.76
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.76
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - The Crusher
  - Toxic Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.61
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.75
    Toxic Blade:
      total: 0.59
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.77
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
    The Reaper:
      total: 0.67
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.82
    The Crusher:
      total: 0.59
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.67
    Heartseeker:
      total: 0.61
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
  relic: *id002
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.59
    Toxic Blade:
      total: 0.64
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.81
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.58
    Riptalon:
      total: 0.62
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.8
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Gladiator's Shield
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Gladiator's Shield
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shield of the Phoenix:
      total: 0.69
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.82
    Gladiator's Shield:
      total: 0.55
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.67
    Hydra's Lament:
      total: 0.55
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
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
      total: 0.62
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.58
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.69
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
  relic: *id002
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Runeforged Hammer
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Hydra's Lament
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
  rationale: The model's core, corrected where the community is clearly right (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.58
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.49
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.69
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.7
  swaps:
  - added: Hydra's Lament
    removed: Shield Splitter
    reason: Conquest community 74% win over 35 matches (vs 51% on this god), taking
      the model's weakest slot from Shield Splitter
  borrowed_from: Conquest
  starter: *id001
  relic: *id002
---
