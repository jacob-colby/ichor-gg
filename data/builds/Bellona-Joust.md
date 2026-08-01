---
type: smite-build
god: Bellona
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
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
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
      total: 0.53
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.55
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.67
    Spectral Armor:
      total: 0.54
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.72
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.59
      efficiency: 0.39
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
  - Shield Splitter
  - Shield of the Phoenix
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
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.47
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.52
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spectral Armor:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.5
    Amanita Charm:
      total: 0.7
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.95
    Erosion:
      total: 0.52
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.65
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
  - Avenging Blade
  - The Crusher
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.57
    Void Shield:
      total: 0.58
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.88
    Void Stone:
      total: 0.59
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.88
    The Crusher:
      total: 0.54
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.66
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.88
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
  - Shield Splitter
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
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
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
      total: 0.53
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.55
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.67
    Spectral Armor:
      total: 0.54
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.72
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.59
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
---
