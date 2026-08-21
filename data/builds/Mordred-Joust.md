---
type: smite-build
god: Mordred
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Stygian Anchor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  - Erosion
  flex_slots:
  - Stygian Anchor
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Stygian Anchor:
      total: 0.56
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.81
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.96
    Erosion:
      total: 0.61
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Heartseeker
  - Rod of Tahuti
  - Erosion
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Erosion
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
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
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.36
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.75
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.94
    Triton's Conch:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Rod of Tahuti
  - Erosion
  - Soul Gem
  flex_slots:
  - Erosion
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.66
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.34
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.58
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Toxic Blade
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
    Toxic Blade:
      total: 0.58
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.71
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.7
    Soul Gem:
      total: 0.74
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.9
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Toxic Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Soul Gem
  flex_slots:
  - Stone of Binding
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Stone of Binding:
      total: 0.62
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.7
    Toxic Blade:
      total: 0.62
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.77
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.54
    Void Shield:
      total: 0.67
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.87
    Void Stone:
      total: 0.66
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.87
    Soul Gem:
      total: 0.77
      efficiency: 0.57
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
      total: 0.63
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.8
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
    Riptalon:
      total: 0.61
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.72
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.79
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
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Erosion
  - Soul Gem
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
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
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Rod of Tahuti
  - Erosion
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Erosion
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Off-type Intelligence build — this kit scales on it (efficiency + fit).
    Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.35
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  - Erosion
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Toxic Blade
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
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.54
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.62
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.76
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.87
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.62
    Triton's Conch:
      total: 0.56
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Stygian Anchor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  - Erosion
  flex_slots:
  - Stygian Anchor
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Stygian Anchor:
      total: 0.56
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.81
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.96
    Erosion:
      total: 0.61
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
---
