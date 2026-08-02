---
type: smite-build
god: Xbalanque
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Riptalon
  - Demon Blade
  - Eros' Bow
  - Pharaoh's Curse
  flex_slots:
  - Eros' Bow
  - Pharaoh's Curse
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.64
    Lernaean Bow:
      total: 0.55
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.74
    Riptalon:
      total: 0.52
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.71
    Demon Blade:
      total: 0.54
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.87
    Eros' Bow:
      total: 0.51
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.63
    Pharaoh's Curse:
      total: 0.51
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Rage
  - Riptalon
  - Damaru
  - Demon Blade
  flex_slots:
  - Golden Blade
  - Rage
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Crit / auto-attack skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.6
    Lernaean Bow:
      total: 0.53
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.7
    Rage:
      total: 0.46
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.57
    Riptalon:
      total: 0.5
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.68
    Damaru:
      total: 0.49
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.54
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Umbral Link
  flex_slots:
  - Spectral Armor
  - Umbral Link
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spectral Armor:
      total: 0.53
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.7
    Pharaoh's Curse:
      total: 0.58
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.56
      efficiency: 0.33
      win: 0.5
      pick: 0.0
      fit: 0.78
    Umbral Link:
      total: 0.52
      efficiency: 0.25
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Riptalon
  - The Crusher
  flex_slots:
  - Void Shield
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.47
    Void Shield:
      total: 0.49
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.7
    Void Stone:
      total: 0.5
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.7
    Riptalon:
      total: 0.61
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.89
    The Crusher:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Riptalon
  - Demon Blade
  - Eros' Bow
  - Pharaoh's Curse
  flex_slots:
  - Eros' Bow
  - Pharaoh's Curse
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.64
    Lernaean Bow:
      total: 0.55
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.74
    Riptalon:
      total: 0.52
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.71
    Demon Blade:
      total: 0.54
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.87
    Eros' Bow:
      total: 0.51
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.63
    Pharaoh's Curse:
      total: 0.51
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
---
