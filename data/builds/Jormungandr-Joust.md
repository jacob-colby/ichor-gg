---
type: smite-build
god: Jormungandr
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Void Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Eye of Providence
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
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
      total: 0.61
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.58
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.68
    Void Shield:
      total: 0.58
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.67
    Spectral Armor:
      total: 0.62
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.67
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.78
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Eye of Providence:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.56
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spectral Armor:
      total: 0.63
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.59
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
      fit: 0.76
    Soul Gem:
      total: 0.72
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Void Shield
  - Void Stone
  - Erosion
  - Soul Gem
  flex_slots:
  - Stone of Binding
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.7
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.52
    Void Shield:
      total: 0.68
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.87
    Void Stone:
      total: 0.67
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.87
    Erosion:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.62
    Soul Gem:
      total: 0.8
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.97
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
  - Void Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Eye of Providence
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
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
      total: 0.61
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.58
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.68
    Void Shield:
      total: 0.58
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.67
    Spectral Armor:
      total: 0.62
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.67
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.78
  starter: *id001
---
