---
type: smite-build
god: Cu Chulainn
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Berserker's Shield
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Toxic Blade
  - Tyrfing
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.64
    Lernaean Bow:
      total: 0.53
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.58
    Toxic Blade:
      total: 0.53
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: &id001
    base: Bluestone Pendant
    upgrade: Bluestone Brooch
    pick_rate: 0.87
    win_rate: 0.53
    matches: 518
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Blink Rune
    pick_rate: 0.26
    win_rate: 0.52
    matches: 155
    basis: community
    borrowed_from: Conquest
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Toxic Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.61
    Toxic Blade:
      total: 0.52
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.69
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Avenging Blade
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Screeching Gargoyle:
      total: 0.51
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.49
    Avenging Blade:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.65
    Toxic Blade:
      total: 0.6
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    The Reaper:
      total: 0.66
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.75
    Heartseeker:
      total: 0.54
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.63
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
  - Berserker's Shield
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.7
    Toxic Blade:
      total: 0.59
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.72
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
      fit: 0.59
    Riptalon:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.34
    Berserker's Shield:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Shield of the Phoenix:
      total: 0.62
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.68
    Hydra's Lament:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.4
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Berserker's Shield
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Toxic Blade
  - Tyrfing
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.64
    Lernaean Bow:
      total: 0.53
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.58
    Toxic Blade:
      total: 0.53
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
  relic: *id002
---
