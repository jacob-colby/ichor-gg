---
type: smite-build
god: Ishtar
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Dominance
  - The Reaper
  - Riptalon
  - Demon Blade
  flex_slots:
  - The Reaper
  - Dominance
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
    Toxic Blade:
      total: 0.62
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.78
    Tyrfing:
      total: 0.65
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.82
    Dominance:
      total: 0.55
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Reaper:
      total: 0.59
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    Riptalon:
      total: 0.68
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.86
    Demon Blade:
      total: 0.62
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Riptalon
  - Heartseeker
  flex_slots:
  - Tyrfing
  - Hydra's Lament
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
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Toxic Blade:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.65
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.51
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.44
    Riptalon:
      total: 0.59
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Riptalon
  - Damaru
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Damaru
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
    Toxic Blade:
      total: 0.61
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.75
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    Riptalon:
      total: 0.67
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.83
    Damaru:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.63
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Riptalon
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Riptalon
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.6
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.74
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.47
    Riptalon:
      total: 0.59
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.78
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.91
    Pharaoh's Curse:
      total: 0.61
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.67
    Shogun's Ofuda:
      total: 0.6
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Heartseeker
  flex_slots:
  - The Crusher
  - Heartseeker
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
      total: 0.71
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.96
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.51
    Riptalon:
      total: 0.75
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 1.0
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Crusher:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Demon Blade
  - Amanita Charm
  flex_slots:
  - Demon Blade
  - Qin's Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.63
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.8
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.77
    Qin's Blade:
      total: 0.54
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.7
    Riptalon:
      total: 0.68
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.85
    Demon Blade:
      total: 0.54
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.53
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.33
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.43
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.58
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Dominance
  - The Reaper
  - Riptalon
  - Demon Blade
  flex_slots:
  - The Reaper
  - Dominance
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
    Toxic Blade:
      total: 0.62
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.78
    Tyrfing:
      total: 0.65
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.82
    Dominance:
      total: 0.55
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Reaper:
      total: 0.59
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    Riptalon:
      total: 0.68
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.86
    Demon Blade:
      total: 0.62
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
---
