---
type: smite-build
god: Bacchus
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shifter's Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Shifter's Shield
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
    Eye of Providence:
      total: 0.69
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.73
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.83
    Shifter's Shield:
      total: 0.65
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.73
    Spectral Armor:
      total: 0.67
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.74
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.93
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
  - Eye of Providence
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Eye of Providence:
      total: 0.68
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.81
    Shield of the Phoenix:
      total: 0.78
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.94
    Spectral Armor:
      total: 0.68
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.69
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.74
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
      total: 0.62
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.76
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.6
    Void Shield:
      total: 0.71
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.92
    Void Stone:
      total: 0.69
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.92
    Amanita Charm:
      total: 0.81
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.95
    Erosion:
      total: 0.63
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Tyrfing
  - Bragi's Harp
  - Death Metal
  - Riptalon
  - Damaru
  - Demon Blade
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Tyrfing:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.67
    Bragi's Harp:
      total: 0.6
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.65
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Riptalon:
      total: 0.6
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    Damaru:
      total: 0.66
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.73
      efficiency: 0.45
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
  - Shifter's Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Shifter's Shield
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
    Eye of Providence:
      total: 0.69
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.73
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.83
    Shifter's Shield:
      total: 0.65
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.73
    Spectral Armor:
      total: 0.67
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.74
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.93
  starter: *id001
---
