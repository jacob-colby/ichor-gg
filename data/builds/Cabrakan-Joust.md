---
type: smite-build
god: Cabrakan
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Shield Splitter
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  flex_slots:
  - Shield Splitter
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.67
    Shield Splitter:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spectral Armor:
      total: 0.57
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.65
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.77
    Pharaoh's Curse:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spectral Armor:
      total: 0.58
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.64
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.76
    Pharaoh's Curse:
      total: 0.58
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.58
    Soul Gem:
      total: 0.7
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - The Crusher
  - Soul Gem
  flex_slots:
  - The Crusher
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
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
      total: 0.59
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
    Void Shield:
      total: 0.67
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.87
    Void Stone:
      total: 0.65
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.87
    The Crusher:
      total: 0.59
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.78
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.97
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
      total: 0.59
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.76
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.62
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.72
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.82
    Pharaoh's Curse:
      total: 0.6
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shogun's Ofuda:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Erosion
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
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
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.52
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.75
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.87
    Erosion:
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.62
    Pharaoh's Curse:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spectral Armor
  - Erosion
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Jotunn's Revenge
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.52
    Spectral Armor:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.47
    Erosion:
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.62
    Soul Gem:
      total: 0.77
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.96
    Triton's Conch:
      total: 0.56
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Shield Splitter
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  flex_slots:
  - Shield Splitter
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.67
    Shield Splitter:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spectral Armor:
      total: 0.57
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.65
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.77
    Pharaoh's Curse:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
---
