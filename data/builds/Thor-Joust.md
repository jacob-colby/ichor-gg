---
type: smite-build
god: Thor
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
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
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.55
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.76
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.9
    Erosion:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Amanita Charm
  - Erosion
  flex_slots:
  - Heartseeker
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
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
      total: 0.58
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.53
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.45
    Heartseeker:
      total: 0.52
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.67
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.71
    Erosion:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  - Amanita Charm
  - Erosion
  flex_slots:
  - Heartseeker
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
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
      total: 0.54
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.65
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.5
    Heartseeker:
      total: 0.51
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.68
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - The Crusher
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - The Crusher
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
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shield of the Phoenix:
      total: 0.64
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.72
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spectral Armor:
      total: 0.58
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.81
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.64
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Void Stone
  - Toxic Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
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
      fit: 0.84
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.66
    Void Shield:
      total: 0.65
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.84
    Void Stone:
      total: 0.64
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.84
    The Crusher:
      total: 0.68
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.72
    Amanita Charm:
      total: 0.71
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Riptalon
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Berserker's Shield
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.67
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.92
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
    Riptalon:
      total: 0.68
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.84
    Amanita Charm:
      total: 0.67
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.71
    Pharaoh's Curse:
      total: 0.58
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shogun's Ofuda:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Freya's Tears
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.69
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.81
    Hydra's Lament:
      total: 0.56
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
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
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.55
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.76
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.9
    Erosion:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
---
