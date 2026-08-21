---
type: smite-build
god: Jing Wei
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Tyrfing
  - The Reaper
  - Riptalon
  - Demon Blade
  - Pharaoh's Curse
  flex_slots:
  - The Reaper
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.6
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.74
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    The Reaper:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.58
    Riptalon:
      total: 0.67
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.82
    Demon Blade:
      total: 0.63
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.87
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.53
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
      total: 0.55
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.63
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.49
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.42
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.64
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.55
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
      total: 0.58
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.71
    Tyrfing:
      total: 0.6
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.71
    Riptalon:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.78
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
  - Shield of the Phoenix
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Berserker's Shield
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.59
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.72
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.78
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.9
    Pharaoh's Curse:
      total: 0.61
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shogun's Ofuda:
      total: 0.6
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.68
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
      total: 0.7
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.93
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.47
    Riptalon:
      total: 0.74
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.97
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.57
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.67
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
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.63
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.79
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    Qin's Blade:
      total: 0.53
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.69
    Riptalon:
      total: 0.67
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.84
    Demon Blade:
      total: 0.54
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.71
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
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.52
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.58
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.41
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.57
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Toxic Blade
  - Tyrfing
  - The Reaper
  - Riptalon
  - Demon Blade
  - Pharaoh's Curse
  flex_slots:
  - The Reaper
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.6
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.74
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    The Reaper:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.58
    Riptalon:
      total: 0.67
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.82
    Demon Blade:
      total: 0.63
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.87
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: *id001
---
