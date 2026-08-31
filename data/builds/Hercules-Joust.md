---
type: smite-build
god: Hercules
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Stygian Anchor
  - Kinetic Cuirass
  - Shield Splitter
  - Void Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Stygian Anchor
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Stygian Anchor:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.61
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.67
    Void Shield:
      total: 0.58
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Eye of the Storm
  - Void Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Void Shield
  - Eye of the Storm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shield of the Phoenix:
      total: 0.67
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.82
    Eye of the Storm:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.65
    Void Shield:
      total: 0.58
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Stone of Binding:
      total: 0.61
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
    Avenging Blade:
      total: 0.6
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.57
    Void Shield:
      total: 0.67
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.88
    Void Stone:
      total: 0.67
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.88
    Amanita Charm:
      total: 0.77
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Riptalon
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.62
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.78
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.45
    Riptalon:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.69
    Amanita Charm:
      total: 0.74
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.83
    Pharaoh's Curse:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shogun's Ofuda:
      total: 0.57
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  - Erosion
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.46
    Shield of the Phoenix:
      total: 0.69
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.86
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Stygian Anchor
  - Kinetic Cuirass
  - Shield Splitter
  - Void Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Stygian Anchor
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Stygian Anchor:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.61
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.67
    Void Shield:
      total: 0.58
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Doublet of Binding — magical protection
    swap_item: Doublet of Binding
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.64
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.74
    Void Shield:
      total: 0.65
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.83
    Void Stone:
      total: 0.64
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.83
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.71
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  flex_slots:
  - Void Stone
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shield of the Phoenix:
      total: 0.67
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.82
    Void Shield:
      total: 0.63
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.8
    Void Stone:
      total: 0.63
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.8
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.7
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.62
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.55
    Void Shield:
      total: 0.73
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.73
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Amanita Charm:
      total: 0.8
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.95
    Erosion:
      total: 0.63
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Erosion
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.64
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.82
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.78
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.9
    Erosion:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.7
    Pharaoh's Curse:
      total: 0.64
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.64
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.78
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Void Shield
  - Void Stone
  - Freya's Tears
  - Erosion
  flex_slots:
  - Void Stone
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Shield of the Phoenix:
      total: 0.68
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.84
    Void Shield:
      total: 0.6
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.73
    Void Stone:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.59
    Erosion:
      total: 0.64
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Doublet of Binding — magical protection
    swap_item: Doublet of Binding
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.64
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.74
    Void Shield:
      total: 0.65
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.83
    Void Stone:
      total: 0.64
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.83
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.71
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
  aspect: Aspect of Preservation
---
