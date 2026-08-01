---
type: smite-build
god: Apollo
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Tyrfing
  - The Reaper
  - Riptalon
  - Damaru
  - Demon Blade
  - Eros' Bow
  flex_slots:
  - Damaru
  - Eros' Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Tyrfing:
      total: 0.48
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.6
    The Reaper:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    Riptalon:
      total: 0.49
      efficiency: 0.27
      win: 0.5
      pick: 0.0
      fit: 0.71
    Damaru:
      total: 0.43
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.5
    Demon Blade:
      total: 0.5
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.79
    Eros' Bow:
      total: 0.43
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.49
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Rage
  - The Reaper
  - Damaru
  - Demon Blade
  - Eros' Bow
  flex_slots:
  - Rage
  - Eros' Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Crit / auto-attack skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Tyrfing:
      total: 0.46
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.55
    Rage:
      total: 0.44
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.52
    The Reaper:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
    Damaru:
      total: 0.44
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.52
    Demon Blade:
      total: 0.5
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.79
    Eros' Bow:
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
  - Erosion
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    The Reaper:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.54
    Spectral Armor:
      total: 0.4
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.59
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.73
    Erosion:
      total: 0.41
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.43
    Pharaoh's Curse:
      total: 0.44
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shogun's Ofuda:
      total: 0.41
      efficiency: 0.33
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Void Stone
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tekko-Kagi
  - Void Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.55
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.5
    Void Stone:
      total: 0.45
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.6
    The Reaper:
      total: 0.62
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.8
    Tekko-Kagi:
      total: 0.47
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.53
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Tyrfing
  - The Reaper
  - Riptalon
  - Damaru
  - Demon Blade
  - Eros' Bow
  flex_slots:
  - Damaru
  - Eros' Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Tyrfing:
      total: 0.48
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.6
    The Reaper:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    Riptalon:
      total: 0.49
      efficiency: 0.27
      win: 0.5
      pick: 0.0
      fit: 0.71
    Damaru:
      total: 0.43
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.5
    Demon Blade:
      total: 0.5
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.79
    Eros' Bow:
      total: 0.43
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.49
  starter: *id001
---
