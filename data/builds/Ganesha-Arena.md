---
type: smite-build
god: Ganesha
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Mystical Mail
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Stampede
  - Mystical Mail
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
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
      total: 0.62
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.8
    Mystical Mail:
      total: 0.58
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spectral Armor:
      total: 0.62
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.75
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.69
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 1.0
    Stampede:
      total: 0.59
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Rod of Asclepius
  - Erosion
  - Stampede
  flex_slots:
  - Kinetic Cuirass
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.78
    Spectral Armor:
      total: 0.63
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.77
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Rod of Asclepius:
      total: 0.71
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.96
    Erosion:
      total: 0.69
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.98
    Stampede:
      total: 0.61
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Shield
  - Void Stone
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Spectral Armor
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Void Shield:
      total: 0.64
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.65
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 1.0
    Spectral Armor:
      total: 0.55
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.59
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.79
    Stampede:
      total: 0.52
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Golden Blade:
      total: 0.53
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
    Lernaean Bow:
      total: 0.57
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.77
    Tyrfing:
      total: 0.52
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.54
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.53
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.61
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Mystical Mail
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Stampede
  - Mystical Mail
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
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
      total: 0.62
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.8
    Mystical Mail:
      total: 0.58
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spectral Armor:
      total: 0.62
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.75
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.69
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 1.0
    Stampede:
      total: 0.59
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
---
