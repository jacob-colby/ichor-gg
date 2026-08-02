---
type: smite-build
god: Achilles
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Runeforged Hammer
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Mystical Mail — physical protection
    swap_item: Mystical Mail
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spectral Armor:
      total: 0.56
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.57
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.76
    Stampede:
      total: 0.53
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Stampede
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Mystical Mail — physical protection
    swap_item: Mystical Mail
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.72
    Spectral Armor:
      total: 0.59
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.62
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.85
    Stampede:
      total: 0.56
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.78
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
  - Jotunn's Revenge
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.59
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.78
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.65
    Void Shield:
      total: 0.62
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.95
    Void Stone:
      total: 0.62
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.95
    The Crusher:
      total: 0.58
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.67
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.9
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
  - Jotunn's Revenge
  - Runeforged Hammer
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Mystical Mail — physical protection
    swap_item: Mystical Mail
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spectral Armor:
      total: 0.56
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.57
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.76
    Stampede:
      total: 0.53
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
---
