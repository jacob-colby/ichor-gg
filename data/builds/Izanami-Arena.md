---
type: smite-build
god: Izanami
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
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
    Lernaean Bow:
      total: 0.48
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.61
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.41
    The Reaper:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Riptalon:
      total: 0.51
      efficiency: 0.27
      win: 0.5
      pick: 0.0
      fit: 0.74
    Eros' Bow:
      total: 0.46
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.55
    Pharaoh's Curse:
      total: 0.46
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
  - The Reaper
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
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.58
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.4
    Rage:
      total: 0.39
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.43
    The Reaper:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.64
    Damaru:
      total: 0.4
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.43
    Demon Blade:
      total: 0.43
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
  - The Reaper
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
      total: 0.43
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.46
    The Reaper:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.43
    Eros' Bow:
      total: 0.42
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.47
    Pharaoh's Curse:
      total: 0.42
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - The Reaper
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Spectral Armor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    The Reaper:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.4
    Amanita Charm:
      total: 0.62
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.8
    Erosion:
      total: 0.45
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.5
    Pharaoh's Curse:
      total: 0.47
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.57
    Shogun's Ofuda:
      total: 0.45
      efficiency: 0.33
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - The Reaper
  - The Crusher
  flex_slots:
  - Void Shield
  - Avenging Blade
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
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
    The Reaper:
      total: 0.61
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
    The Crusher:
      total: 0.52
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
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
    Lernaean Bow:
      total: 0.48
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.61
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.41
    The Reaper:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Riptalon:
      total: 0.51
      efficiency: 0.27
      win: 0.5
      pick: 0.0
      fit: 0.74
    Eros' Bow:
      total: 0.46
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.55
    Pharaoh's Curse:
      total: 0.46
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
---
