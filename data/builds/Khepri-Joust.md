---
type: smite-build
god: Khepri
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
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
    Kinetic Cuirass:
      total: 0.7
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shifter's Shield:
      total: 0.61
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spectral Armor:
      total: 0.62
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.71
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.9
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Void Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Void Shield
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
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.69
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.78
    Void Shield:
      total: 0.62
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spectral Armor:
      total: 0.63
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.7
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.88
    Soul Gem:
      total: 0.75
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.92
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
  - Erosion
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
      total: 0.61
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.59
    Void Shield:
      total: 0.69
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.91
    Void Stone:
      total: 0.67
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.91
    Erosion:
      total: 0.6
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  - Erosion
  flex_slots:
  - Bracer of The Abyss
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Stygian Anchor — magical protection
    swap_item: Stygian Anchor
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.4
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.39
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.72
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.81
    Erosion:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Erosion
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Joust
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.74
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.86
    Erosion:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.61
    Pharaoh's Curse:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spectral Armor
  - Erosion
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Jotunn's Revenge
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spectral Armor:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.46
    Erosion:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.77
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.96
    Triton's Conch:
      total: 0.56
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
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
    Kinetic Cuirass:
      total: 0.7
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shifter's Shield:
      total: 0.61
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spectral Armor:
      total: 0.62
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.71
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.9
  starter: *id001
---
