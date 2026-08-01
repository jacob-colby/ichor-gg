---
type: smite-build
god: Horus
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Void Stone
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Void Stone
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
      fit: 0.66
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.76
    Void Stone:
      total: 0.51
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.73
    Spectral Armor:
      total: 0.56
      efficiency: 0.49
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
      total: 0.62
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
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
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.51
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spectral Armor:
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.54
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
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Screeching Gargoyle
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Screeching Gargoyle:
      total: 0.51
      efficiency: 0.33
      win: 0.5
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Void Shield:
      total: 0.59
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.9
    Void Stone:
      total: 0.6
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.9
    Amanita Charm:
      total: 0.68
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.91
    Erosion:
      total: 0.52
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.66
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
  - Bragi's Harp
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
      total: 0.52
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Rage:
      total: 0.5
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.66
    Bragi's Harp:
      total: 0.5
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.55
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.51
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.6
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Void Stone
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Void Stone
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Eye of Providence:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.66
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.76
    Void Stone:
      total: 0.51
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.73
    Spectral Armor:
      total: 0.56
      efficiency: 0.49
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
      total: 0.62
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
---
