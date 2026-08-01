---
type: smite-build
god: Pele
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.77
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 1.0
    Hydra's Lament:
      total: 0.6
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
    The Reaper:
      total: 0.72
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Pendulum Blade:
      total: 0.65
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.69
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.88
    Heartseeker:
      total: 0.58
      efficiency: 0.28
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.78
    Hydra's Lament:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.62
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.81
    Pendulum Blade:
      total: 0.53
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Crusher:
      total: 0.57
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.47
      efficiency: 0.28
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - The Reaper
  - The Crusher
  - Amanita Charm
  - Erosion
  flex_slots:
  - The Crusher
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.48
    Shield Splitter:
      total: 0.48
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Reaper:
      total: 0.56
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.67
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.68
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.92
    Erosion:
      total: 0.5
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Titan's Bane
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
    Jotunn's Revenge:
      total: 0.77
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Reaper:
      total: 0.72
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Pendulum Blade:
      total: 0.65
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.72
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.95
    Heartseeker:
      total: 0.62
      efficiency: 0.28
      win: 0.5
      pick: 0.0
      fit: 0.95
    Titan's Bane:
      total: 0.57
      efficiency: 0.28
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Death Metal
  - Damaru
  - Demon Blade
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Damaru
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
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.77
    Death Metal:
      total: 0.55
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.51
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.6
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
    Soul Gem:
      total: 0.53
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.65
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.77
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 1.0
    Hydra's Lament:
      total: 0.6
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
    The Reaper:
      total: 0.72
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Pendulum Blade:
      total: 0.65
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.69
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.88
    Heartseeker:
      total: 0.58
      efficiency: 0.28
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
---
