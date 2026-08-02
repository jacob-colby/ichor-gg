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
  - Riptalon
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
  - Jotunn's Revenge
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
      total: 0.63
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.63
    Lernaean Bow:
      total: 0.69
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.73
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.52
    Riptalon:
      total: 0.66
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.73
    The Crusher:
      total: 0.64
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
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
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
      total: 0.62
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.63
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.71
    Pharaoh's Curse:
      total: 0.69
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.74
    Shogun's Ofuda:
      total: 0.66
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.74
    Umbral Link:
      total: 0.62
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Lernaean Bow
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Lernaean Bow:
      total: 0.62
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.64
    Riptalon:
      total: 0.73
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.85
    The Crusher:
      total: 0.7
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.7
    Heartseeker:
      total: 0.62
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.7
    Avatar's Parashu:
      total: 0.68
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Death Metal
  - Damaru
  - Demon Blade
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.65
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.67
    Lernaean Bow:
      total: 0.71
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.77
    Death Metal:
      total: 0.65
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.66
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.73
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Pharaoh's Curse:
      total: 0.64
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.64
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
  - Jotunn's Revenge
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
      total: 0.63
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.63
    Lernaean Bow:
      total: 0.69
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.73
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.52
    Riptalon:
      total: 0.66
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.73
    The Crusher:
      total: 0.64
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
---
