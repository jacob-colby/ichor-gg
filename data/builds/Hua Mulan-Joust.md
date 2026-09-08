---
type: smite-build
god: Hua Mulan
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Shield Splitter
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.58
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.7
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.58
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.82
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.99
    Erosion:
      total: 0.63
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.74
    Pharaoh's Curse:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  flex_slots:
  - Kinetic Cuirass
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.61
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.76
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shield of the Phoenix:
      total: 0.65
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.77
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.62
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.72
    Pharaoh's Curse:
      total: 0.59
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Toxic Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Stone of Binding
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Stone of Binding:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.69
    Toxic Blade:
      total: 0.66
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.85
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.53
    Void Shield:
      total: 0.66
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.86
    Void Stone:
      total: 0.66
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.86
    Amanita Charm:
      total: 0.75
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.85
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.42
    Shield of the Phoenix:
      total: 0.67
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.59
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Toxic Blade
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Shield Splitter
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.58
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.7
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.58
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.82
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.99
    Erosion:
      total: 0.63
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.74
    Pharaoh's Curse:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
---
