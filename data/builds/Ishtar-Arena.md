---
type: smite-build
god: Ishtar
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - The Reaper
  - Demon Blade
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
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
      total: 0.52
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.66
    Lernaean Bow:
      total: 0.56
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.76
    Tyrfing:
      total: 0.51
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Reaper:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Demon Blade:
      total: 0.54
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.87
    Amanita Charm:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
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
    Golden Blade:
      total: 0.49
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.6
    Lernaean Bow:
      total: 0.53
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.7
    Rage:
      total: 0.46
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.57
    The Reaper:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
    Damaru:
      total: 0.47
      efficiency: 0.37
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
  - Erosion
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.65
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.85
    Erosion:
      total: 0.47
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.55
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shogun's Ofuda:
      total: 0.47
      efficiency: 0.33
      win: 0.5
      pick: 0.0
      fit: 0.61
    Umbral Link:
      total: 0.52
      efficiency: 0.24
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Void Shield
  - Tekko-Kagi
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
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.51
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
      total: 0.64
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.84
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.55
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.61
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - The Reaper
  - Demon Blade
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
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
      total: 0.52
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.66
    Lernaean Bow:
      total: 0.56
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.76
    Tyrfing:
      total: 0.51
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Reaper:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Demon Blade:
      total: 0.54
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.87
    Amanita Charm:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
---
