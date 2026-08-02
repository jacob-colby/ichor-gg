---
type: smite-build
god: Kali
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - The Crusher
  flex_slots:
  - The Crusher
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
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.63
    Lernaean Bow:
      total: 0.55
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.73
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.5
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Reaper:
      total: 0.53
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.72
    The Crusher:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Spectral Armor
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
    Spectral Armor:
      total: 0.54
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
      total: 0.55
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.71
    Stampede:
      total: 0.51
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.68
    Pharaoh's Curse:
      total: 0.56
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.74
    Shogun's Ofuda:
      total: 0.54
      efficiency: 0.33
      win: 0.5
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Void Stone
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Avenging Blade
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.64
    Void Stone:
      total: 0.5
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Reaper:
      total: 0.6
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.85
    The Crusher:
      total: 0.57
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
    Heartseeker:
      total: 0.52
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.7
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
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - The Crusher
  flex_slots:
  - The Crusher
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.63
    Lernaean Bow:
      total: 0.55
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.73
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.5
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Reaper:
      total: 0.53
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.72
    The Crusher:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
---
