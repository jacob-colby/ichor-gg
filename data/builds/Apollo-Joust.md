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
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Tyrfing
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Tyrfing:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    The Reaper:
      total: 0.61
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Riptalon:
      total: 0.66
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.71
    Damaru:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    Demon Blade:
      total: 0.62
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.79
    Pharaoh's Curse:
      total: 0.57
      efficiency: 0.64
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
  - Riptalon
  - Damaru
  - Demon Blade
  - Pharaoh's Curse
  flex_slots:
  - Tyrfing
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
  rationale: Crit / auto-attack skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Tyrfing:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.55
    Rage:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.52
    Riptalon:
      total: 0.65
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.69
    Damaru:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.52
    Demon Blade:
      total: 0.62
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.79
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
  - Berserker's Shield
  - Shield of the Phoenix
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Berserker's Shield
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.44
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.77
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.87
    Erosion:
      total: 0.56
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.57
    Pharaoh's Curse:
      total: 0.64
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shogun's Ofuda:
      total: 0.61
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Void Shield
  - Riptalon
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Void Shield
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.59
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.55
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.5
    Void Shield:
      total: 0.55
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.6
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
    Heartseeker:
      total: 0.55
      efficiency: 0.53
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
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Tyrfing
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Tyrfing:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    The Reaper:
      total: 0.61
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Riptalon:
      total: 0.66
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.71
    Damaru:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    Demon Blade:
      total: 0.62
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.79
    Pharaoh's Curse:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.49
  starter: *id001
---
