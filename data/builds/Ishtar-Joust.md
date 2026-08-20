---
type: smite-build
god: Ishtar
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Tyrfing
  - Dominance
  - The Reaper
  - Riptalon
  - Damaru
  - Demon Blade
  flex_slots:
  - Damaru
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Tyrfing:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.66
    Dominance:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Reaper:
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.63
    Riptalon:
      total: 0.62
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.7
    Damaru:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.55
    Demon Blade:
      total: 0.61
      efficiency: 0.35
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
  - Hydra's Lament
  - The Reaper
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
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Toxic Blade:
      total: 0.5
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.57
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.45
    Hydra's Lament:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.4
    Heartseeker:
      total: 0.49
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Dominance
  - Riptalon
  - Damaru
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Tyrfing
  - Deathbringer
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Crit / auto-attack skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Tyrfing:
      total: 0.53
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.6
    Dominance:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Riptalon:
      total: 0.6
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.68
    Damaru:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.61
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.57
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
  - Erosion
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.77
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.91
    Erosion:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.61
    Pharaoh's Curse:
      total: 0.61
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.67
    Shogun's Ofuda:
      total: 0.59
      efficiency: 0.51
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
  - Heartseeker
  - Silverbranch Bow
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
      fit: 0.85
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.51
    Riptalon:
      total: 0.71
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.89
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.61
    Heartseeker:
      total: 0.56
      efficiency: 0.41
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
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Qin's Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
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
      total: 0.62
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.8
    Tyrfing:
      total: 0.61
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.77
    Qin's Blade:
      total: 0.53
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.7
    Riptalon:
      total: 0.69
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.45
    Pharaoh's Curse:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  - Pharaoh's Curse
  flex_slots:
  - Breastplate of Valor
  - Pharaoh's Curse
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.33
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.43
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.58
    Hydra's Lament:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.53
    Pharaoh's Curse:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Tyrfing
  - Dominance
  - The Reaper
  - Riptalon
  - Damaru
  - Demon Blade
  flex_slots:
  - Damaru
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Tyrfing:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.66
    Dominance:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Reaper:
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.63
    Riptalon:
      total: 0.62
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.7
    Damaru:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.55
    Demon Blade:
      total: 0.61
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
---
