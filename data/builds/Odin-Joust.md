---
type: smite-build
god: Odin
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  - Erosion
  flex_slots:
  - Toxic Blade
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Stygian Anchor — magical protection
    swap_item: Stygian Anchor
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.58
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.59
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
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Heartseeker
  - Amanita Charm
  - Erosion
  flex_slots:
  - Heartseeker
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
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
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.44
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.73
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.81
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  - Erosion
  flex_slots:
  - Toxic Blade
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
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
      fit: 0.75
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shield of the Phoenix:
      total: 0.67
      efficiency: 0.57
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
  - Toxic Blade
  - Stone of Binding
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Stone of Binding:
      total: 0.63
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.71
    Toxic Blade:
      total: 0.64
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.81
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.56
    Void Shield:
      total: 0.68
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
      fit: 0.89
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
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
      total: 0.64
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.82
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.42
    Riptalon:
      total: 0.62
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.73
    Amanita Charm:
      total: 0.73
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.8
    Pharaoh's Curse:
      total: 0.58
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shogun's Ofuda:
      total: 0.57
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
      fit: 0.44
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.51
    Shield of the Phoenix:
      total: 0.69
      efficiency: 0.57
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
      fit: 0.61
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  - Erosion
  flex_slots:
  - Toxic Blade
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Stygian Anchor — magical protection
    swap_item: Stygian Anchor
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.58
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.59
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
  starter: *id001
---
