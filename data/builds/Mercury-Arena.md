---
type: smite-build
god: Mercury
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Toxic Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.65
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.84
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.84
    Tyrfing:
      total: 0.61
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.73
    The Reaper:
      total: 0.71
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.92
    Titan's Bane:
      total: 0.65
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.77
    Heartseeker:
      total: 0.65
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Titan's Bane
  - Transcendence
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: mana-stack (efficiency + fit). Arena — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.66
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.36
    Hydra's Lament:
      total: 0.57
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Reaper:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.68
    Titan's Bane:
      total: 0.54
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.53
    Heartseeker:
      total: 0.58
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - Titan's Bane
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.71
    The Reaper:
      total: 0.63
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.76
    Pendulum Blade:
      total: 0.56
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.71
    Titan's Bane:
      total: 0.57
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.61
    Heartseeker:
      total: 0.57
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Shield of the Phoenix
  - Void Stone
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Stampede
  - Void Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.62
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.77
    Shield of the Phoenix:
      total: 0.62
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.73
    Void Stone:
      total: 0.6
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.73
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.78
    Stampede:
      total: 0.62
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Heartseeker
  - The Crusher
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
    Toxic Blade:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.98
    Jotunn's Revenge:
      total: 0.78
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.89
    The Reaper:
      total: 0.76
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.68
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.87
    Titan's Bane:
      total: 0.7
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.87
    Heartseeker:
      total: 0.7
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.97
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Tyrfing
  - The Reaper
  - Riptalon
  flex_slots:
  - Golden Blade
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.6
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.72
    Lernaean Bow:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.63
    Toxic Blade:
      total: 0.69
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.92
    Tyrfing:
      total: 0.61
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.72
    The Reaper:
      total: 0.6
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.65
    Riptalon:
      total: 0.71
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.97
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Chandra's Grace
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Pendulum Blade
  flex_slots:
  - Toxic Blade
  - Arondight
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
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.55
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.64
    Chandra's Grace:
      total: 0.56
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.72
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.77
    Hydra's Lament:
      total: 0.62
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.69
    Arondight:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.49
    Pendulum Blade:
      total: 0.59
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Toxic Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.65
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.84
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.84
    Tyrfing:
      total: 0.61
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.73
    The Reaper:
      total: 0.71
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.92
    Titan's Bane:
      total: 0.65
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.77
    Heartseeker:
      total: 0.65
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
---
