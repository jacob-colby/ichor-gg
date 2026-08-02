---
type: smite-build
god: Hercules
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Mantle Of Discord — magical protection
    swap_item: Mantle Of Discord
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spectral Armor:
      total: 0.67
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.73
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.9
    Stampede:
      total: 0.66
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.78
    Pharaoh's Curse:
      total: 0.66
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Mystical Mail — physical protection
    swap_item: Mystical Mail
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Shield of the Phoenix:
      total: 0.72
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.82
    Spectral Armor:
      total: 0.68
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.72
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.88
    Stampede:
      total: 0.67
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.8
    Pharaoh's Curse:
      total: 0.67
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Void Shield
  - Void Stone
  - The Crusher
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.66
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.7
    Void Shield:
      total: 0.74
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.98
    Void Stone:
      total: 0.72
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.98
    The Crusher:
      total: 0.64
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.83
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.98
    Erosion:
      total: 0.65
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Death Metal
  - Damaru
  - Demon Blade
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.65
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.67
    Lernaean Bow:
      total: 0.71
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.77
    Death Metal:
      total: 0.65
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
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
    Pharaoh's Curse:
      total: 0.64
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.64
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Mantle Of Discord — magical protection
    swap_item: Mantle Of Discord
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spectral Armor:
      total: 0.67
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.73
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.9
    Stampede:
      total: 0.66
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.78
    Pharaoh's Curse:
      total: 0.66
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Pharaoh's Curse
  flex_slots:
  - Stampede
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.71
    Spectral Armor:
      total: 0.7
      efficiency: 0.66
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
      total: 0.74
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.91
    Stampede:
      total: 0.68
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.83
    Pharaoh's Curse:
      total: 0.68
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Mystical Mail — physical protection
    swap_item: Mystical Mail
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Shield of the Phoenix:
      total: 0.72
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.82
    Spectral Armor:
      total: 0.68
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.72
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.88
    Stampede:
      total: 0.67
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.8
    Pharaoh's Curse:
      total: 0.67
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.7
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
  - Erosion
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Mystical Mail — physical protection
    swap_item: Mystical Mail
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.69
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.75
    Void Shield:
      total: 0.75
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.73
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 1.0
    Spectral Armor:
      total: 0.64
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.81
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.95
    Erosion:
      total: 0.65
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Pharaoh's Curse
  flex_slots:
  - Stampede
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.71
    Spectral Armor:
      total: 0.7
      efficiency: 0.66
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
      total: 0.74
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.91
    Stampede:
      total: 0.68
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.83
    Pharaoh's Curse:
      total: 0.68
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
  aspect: Aspect of Preservation
---
