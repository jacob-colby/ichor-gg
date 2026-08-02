---
type: smite-build
god: Rama
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - The Reaper
  - Riptalon
  - Demon Blade
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Demon Blade
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
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.54
    Lernaean Bow:
      total: 0.64
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Reaper:
      total: 0.64
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.69
    Riptalon:
      total: 0.69
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Demon Blade:
      total: 0.58
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.7
    Pharaoh's Curse:
      total: 0.6
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Rage
  - Riptalon
  - Damaru
  - Demon Blade
  - Pharaoh's Curse
  flex_slots:
  - Damaru
  - Rage
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
  rationale: Crit / auto-attack skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.62
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
    Rage:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.46
    Riptalon:
      total: 0.68
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.75
    Damaru:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.46
    Demon Blade:
      total: 0.58
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.7
    Pharaoh's Curse:
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  - Avatar's Parashu
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Avatar's Parashu
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
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.46
    Riptalon:
      total: 0.64
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.68
    The Crusher:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.43
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.53
    Pharaoh's Curse:
      total: 0.55
      efficiency: 0.64
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
  - Spectral Armor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Doublet of Binding — magical protection
    swap_item: Doublet of Binding
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
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.81
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.94
    Erosion:
      total: 0.6
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.64
    Pharaoh's Curse:
      total: 0.67
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shogun's Ofuda:
      total: 0.64
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.71
    Umbral Link:
      total: 0.64
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Void Shield
  - Riptalon
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - Jotunn's Revenge
  - Void Shield
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
    Lernaean Bow:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.56
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.5
    Void Shield:
      total: 0.6
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.7
    Riptalon:
      total: 0.73
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.86
    The Crusher:
      total: 0.63
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.57
    Avatar's Parashu:
      total: 0.61
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - The Reaper
  - Riptalon
  - Demon Blade
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Demon Blade
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.54
    Lernaean Bow:
      total: 0.64
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Reaper:
      total: 0.64
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.69
    Riptalon:
      total: 0.69
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Demon Blade:
      total: 0.58
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.7
    Pharaoh's Curse:
      total: 0.6
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
---
