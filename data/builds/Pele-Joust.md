---
type: smite-build
god: Pele
mode: Joust
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.82
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 1.0
    Hydra's Lament:
      total: 0.66
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.77
    The Reaper:
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
    Pendulum Blade:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.76
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.88
    Heartseeker:
      total: 0.65
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Pendulum Blade
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.71
    Hydra's Lament:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Reaper:
      total: 0.62
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.72
    Pendulum Blade:
      total: 0.51
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.6
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.57
    Heartseeker:
      total: 0.54
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Pendulum Blade
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Toxic Blade
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
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.53
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.63
    Jotunn's Revenge:
      total: 0.71
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.78
    Hydra's Lament:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.66
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.81
    Pendulum Blade:
      total: 0.59
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Crusher:
      total: 0.65
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shield of the Phoenix:
      total: 0.67
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spectral Armor:
      total: 0.57
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.81
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.62
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Toxic Blade
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
    Toxic Blade:
      total: 0.64
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.86
    Jotunn's Revenge:
      total: 0.82
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Reaper:
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
    Pendulum Blade:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.8
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.95
    Heartseeker:
      total: 0.68
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Jotunn's Revenge
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
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.69
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.94
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.42
    Tyrfing:
      total: 0.6
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.74
    The Reaper:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.66
    Riptalon:
      total: 0.76
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.99
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  - Pendulum Blade
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.85
    Shield of the Phoenix:
      total: 0.66
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.75
    Hydra's Lament:
      total: 0.65
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.75
    Pendulum Blade:
      total: 0.63
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.85
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.82
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 1.0
    Hydra's Lament:
      total: 0.66
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.77
    The Reaper:
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
    Pendulum Blade:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.76
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.88
    Heartseeker:
      total: 0.65
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
---
