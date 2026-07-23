---
type: smite-build
god: Hercules
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shield Splitter
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Shield Splitter
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Eye of Providence:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.67
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
    Shield Splitter:
      total: 0.54
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spectral Armor:
      total: 0.56
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.72
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.63
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.74
    Spectral Armor:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.72
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
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
  - Jotunn's Revenge
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.64
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.53
    Void Shield:
      total: 0.6
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 0.9
    Void Stone:
      total: 0.61
      efficiency: 0.31
      win: 0.5
      pick: 0.0
      fit: 0.9
    Amanita Charm:
      total: 0.68
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.92
    Erosion:
      total: 0.53
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Tyrfing
  - Rage
  - Bragi's Harp
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Damaru
  - Rage
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Tyrfing:
      total: 0.53
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
    Rage:
      total: 0.51
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Bragi's Harp:
      total: 0.52
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.52
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.61
      efficiency: 0.23
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Void Stone
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shield of the Phoenix
  - Void Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.8
    Void Stone:
      total: 0.59
      efficiency: 0.31
      win: 0.5
      pick: 0.0
      fit: 0.88
    Spectral Armor:
      total: 0.63
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.78
    Amanita Charm:
      total: 0.72
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.69
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.98
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Shield of the Phoenix
  - Void Shield
  - Void Stone
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Void Stone
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.79
    Void Shield:
      total: 0.54
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 0.78
    Void Stone:
      total: 0.55
      efficiency: 0.31
      win: 0.5
      pick: 0.0
      fit: 0.78
    Spectral Armor:
      total: 0.58
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.72
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.61
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Void Shield
  - Void Stone
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
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
      total: 0.56
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.7
    Void Shield:
      total: 0.65
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.66
      efficiency: 0.31
      win: 0.5
      pick: 0.0
      fit: 1.0
    Spectral Armor:
      total: 0.56
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.71
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.99
    Erosion:
      total: 0.59
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: *id001
  aspect: Aspect of Preservation
---
