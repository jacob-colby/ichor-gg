---
type: smite-build
god: Ratatoskr
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  flex_slots:
  - Briskberry Acorn
  - Heartseeker
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Ashwhorl Acorn:
      total: 0.74
      efficiency: 0.96
      win: 0.5
      pick: 0.0
      fit: 0.52
    Briskberry Acorn:
      total: 0.73
      efficiency: 0.94
      win: 0.5
      pick: 0.0
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.76
      efficiency: 0.92
      win: 0.5
      pick: 0.0
      fit: 0.61
    Jotunn's Revenge:
      total: 0.83
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Pendulum Blade
  - The Crusher
  flex_slots:
  - Ashwhorl Acorn
  - Briskberry Acorn
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
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Ashwhorl Acorn:
      total: 0.59
      efficiency: 0.96
      win: 0.5
      pick: 0.0
      fit: 0.22
    Briskberry Acorn:
      total: 0.58
      efficiency: 0.94
      win: 0.5
      pick: 0.0
      fit: 0.22
    Thistlethorn Acorn:
      total: 0.68
      efficiency: 0.92
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.72
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.78
    Pendulum Blade:
      total: 0.59
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Crusher:
      total: 0.64
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Kinetic Cuirass
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Ashwhorl Acorn:
      total: 0.7
      efficiency: 0.96
      win: 0.5
      pick: 0.0
      fit: 0.44
    Briskberry Acorn:
      total: 0.69
      efficiency: 0.94
      win: 0.5
      pick: 0.0
      fit: 0.44
    Thistlethorn Acorn:
      total: 0.7
      efficiency: 0.92
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.64
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.76
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
  - Pendulum Blade
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.83
      efficiency: 0.66
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
      total: 0.71
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.7
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Thistlethorn Acorn
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.7
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.99
    Ashwhorl Acorn:
      total: 0.72
      efficiency: 0.96
      win: 0.5
      pick: 0.0
      fit: 0.48
    Thistlethorn Acorn:
      total: 0.61
      efficiency: 0.92
      win: 0.5
      pick: 0.0
      fit: 0.31
    Tyrfing:
      total: 0.62
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.78
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 1.0
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Thistlethorn Acorn
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Thistlethorn Acorn:
      total: 0.78
      efficiency: 0.92
      win: 0.5
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.85
    Hydra's Lament:
      total: 0.66
      efficiency: 0.58
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
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  flex_slots:
  - Briskberry Acorn
  - Heartseeker
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Ashwhorl Acorn:
      total: 0.74
      efficiency: 0.96
      win: 0.5
      pick: 0.0
      fit: 0.52
    Briskberry Acorn:
      total: 0.73
      efficiency: 0.94
      win: 0.5
      pick: 0.0
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.76
      efficiency: 0.92
      win: 0.5
      pick: 0.0
      fit: 0.61
    Jotunn's Revenge:
      total: 0.83
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
---
