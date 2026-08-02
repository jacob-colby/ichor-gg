---
type: smite-build
god: Sun Wukong
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Avenging Blade
  - Runeforged Hammer
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Erosion
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.61
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.59
    Runeforged Hammer:
      total: 0.64
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.8
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.93
    Erosion:
      total: 0.62
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Pharaoh's Curse:
      total: 0.66
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shogun's Ofuda:
      total: 0.62
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Kinetic Cuirass
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.67
    Shield of the Phoenix:
      total: 0.67
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.73
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.66
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.77
    Pharaoh's Curse:
      total: 0.67
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shogun's Ofuda:
      total: 0.64
      efficiency: 0.57
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
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Void Stone
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
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
      total: 0.68
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.59
    Void Shield:
      total: 0.66
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.83
    Void Stone:
      total: 0.65
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.83
    The Crusher:
      total: 0.68
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.73
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.77
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
  - Avenging Blade
  - Runeforged Hammer
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Erosion
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.61
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.59
    Runeforged Hammer:
      total: 0.64
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.8
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.93
    Erosion:
      total: 0.62
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Pharaoh's Curse:
      total: 0.66
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shogun's Ofuda:
      total: 0.62
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: *id001
---
