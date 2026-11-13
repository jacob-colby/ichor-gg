---
type: smite-build
god: Gilgamesh
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Golden Blade
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.54
    Toxic Blade:
      total: 0.58
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.71
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Leather Cowl
    upgrade: Hunter's Cowl
    pick_rate: 0.38
    win_rate: 0.6116
    matches: 131
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Purification Beads
    pick_rate: 0.31
    win_rate: 0.55
    matches: 107
    basis: community
    borrowed_from: Conquest
- source: suggested
  archetype: mana-stack
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Transcendence
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
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Toxic Blade:
      total: 0.52
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.57
    Berserker's Shield:
      total: 0.49
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
    Transcendence:
      total: 0.35
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.21
    Heartseeker:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
  relic: *id002
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Golden Blade
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.51
    Toxic Blade:
      total: 0.57
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Reaper:
      total: 0.61
      efficiency: 0.57
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
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - The Reaper
  flex_slots:
  - Void Stone
  - Void Shield
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.66
    Toxic Blade:
      total: 0.63
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.79
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Void Shield:
      total: 0.53
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.6
    Void Stone:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    The Reaper:
      total: 0.66
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.74
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
      total: 0.53
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.56
    Toxic Blade:
      total: 0.62
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.77
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.55
    Riptalon:
      total: 0.61
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.76
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.52
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.53
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.59
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.31
    Berserker's Shield:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.66
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.37
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Golden Blade
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.54
    Toxic Blade:
      total: 0.58
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.71
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
  relic: *id002
---
