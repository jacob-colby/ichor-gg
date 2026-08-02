---
type: smite-build
god: Ullr
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Riptalon
  - Eros' Bow
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Riptalon:
      total: 0.54
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.75
    Eros' Bow:
      total: 0.47
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.55
    Pharaoh's Curse:
      total: 0.47
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Rage
  - Riptalon
  - Damaru
  - Demon Blade
  flex_slots:
  - Damaru
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
    Lernaean Bow:
      total: 0.47
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.58
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Rage:
      total: 0.39
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.52
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.72
    Damaru:
      total: 0.42
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.43
    Demon Blade:
      total: 0.44
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
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
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.44
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.46
    Riptalon:
      total: 0.5
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.68
    The Crusher:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.43
    Eros' Bow:
      total: 0.43
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.47
    Pharaoh's Curse:
      total: 0.43
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.47
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
  - Erosion
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
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.69
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.93
    Erosion:
      total: 0.51
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.63
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shogun's Ofuda:
      total: 0.52
      efficiency: 0.33
      win: 0.5
      pick: 0.0
      fit: 0.7
    Umbral Link:
      total: 0.51
      efficiency: 0.25
      win: 0.5
      pick: 0.0
      fit: 0.77
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
  - The Crusher
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
      total: 0.46
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.52
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
      total: 0.58
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.84
    The Crusher:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Riptalon
  - Eros' Bow
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Riptalon:
      total: 0.54
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.75
    Eros' Bow:
      total: 0.47
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.55
    Pharaoh's Curse:
      total: 0.47
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
---
