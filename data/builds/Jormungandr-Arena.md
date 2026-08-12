---
type: smite-build
god: Jormungandr
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Stampede
  - Spectral Armor
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spectral Armor:
      total: 0.59
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.65
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.78
    Stampede:
      total: 0.59
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.71
    Pharaoh's Curse:
      total: 0.67
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.65
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.78
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Soul Gem
  flex_slots:
  - Erosion
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spectral Armor:
      total: 0.6
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.64
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.76
    Pharaoh's Curse:
      total: 0.68
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.79
    Shogun's Ofuda:
      total: 0.66
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.74
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Void Shield
  - Void Stone
  - Erosion
  - Pharaoh's Curse
  - Soul Gem
  flex_slots:
  - Toxic Blade
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.61
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.8
    Void Shield:
      total: 0.7
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.94
    Void Stone:
      total: 0.69
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.94
    Erosion:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.67
    Pharaoh's Curse:
      total: 0.62
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.67
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
  - Golden Blade
  - Riptalon
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Erosion
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.59
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.64
    Riptalon:
      total: 0.62
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.77
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.92
    Erosion:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.67
    Pharaoh's Curse:
      total: 0.65
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.73
    Shogun's Ofuda:
      total: 0.63
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Genji's Guard
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Erosion:
      total: 0.6
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    Pharaoh's Curse:
      total: 0.63
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.69
    Shogun's Ofuda:
      total: 0.61
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
  archetype: strength
  slot_order:
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Stampede
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Arena
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Spectral Armor:
      total: 0.57
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.8
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.97
    Erosion:
      total: 0.62
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.72
    Stampede:
      total: 0.58
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.67
    Pharaoh's Curse:
      total: 0.61
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shogun's Ofuda:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Spectral Armor
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Spectral Armor:
      total: 0.56
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.53
    Erosion:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.66
    Pharaoh's Curse:
      total: 0.62
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shogun's Ofuda:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.66
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.58
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Stampede
  - Spectral Armor
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Spectral Armor:
      total: 0.59
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.65
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.78
    Stampede:
      total: 0.59
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.71
    Pharaoh's Curse:
      total: 0.67
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.65
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.78
  starter: *id001
---
