---
type: smite-build
god: Gilgamesh
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Jotunn's Revenge
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.65
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.84
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.71
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.77
    Pharaoh's Curse:
      total: 0.58
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shogun's Ofuda:
      total: 0.57
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Heartseeker
  - Hydra's Lament
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Toxic Blade:
      total: 0.57
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.41
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.66
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Pharaoh's Curse:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Shield of the Phoenix
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
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
      total: 0.63
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.81
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.78
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.9
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.6
    Pharaoh's Curse:
      total: 0.59
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shogun's Ofuda:
      total: 0.58
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
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
      total: 0.59
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.68
    Toxic Blade:
      total: 0.69
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.92
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Void Shield:
      total: 0.63
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.79
    Void Stone:
      total: 0.62
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.79
    Amanita Charm:
      total: 0.68
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.66
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.86
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.38
    Riptalon:
      total: 0.64
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.76
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.69
    Pharaoh's Curse:
      total: 0.56
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shogun's Ofuda:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Freya's Tears
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.58
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.71
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.68
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.39
    Pharaoh's Curse:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shogun's Ofuda:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Jotunn's Revenge
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.65
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.84
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.71
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.77
    Pharaoh's Curse:
      total: 0.58
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shogun's Ofuda:
      total: 0.57
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: *id001
---
