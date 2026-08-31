---
type: smite-build
god: Ravana
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Runeforged Hammer
  - Heartseeker
  - Amanita Charm
  - Erosion
  flex_slots:
  - Runeforged Hammer
  - Toxic Blade
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.55
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.73
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.58
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.76
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.87
    Erosion:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - Heartseeker
  - Amanita Charm
  - Erosion
  flex_slots:
  - Runeforged Hammer
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
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
      total: 0.62
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.49
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.43
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.49
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Void Shield
  - Heartseeker
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
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
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.56
    Void Shield:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.51
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.7
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.74
    Erosion:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Void Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shield of the Phoenix:
      total: 0.65
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.76
    Void Shield:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.61
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Toxic Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Avenging Blade:
      total: 0.62
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.75
    Toxic Blade:
      total: 0.62
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.85
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.67
    Void Shield:
      total: 0.65
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.84
    Void Stone:
      total: 0.65
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.84
    Amanita Charm:
      total: 0.72
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.78
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.68
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.89
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
    Riptalon:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.8
    Amanita Charm:
      total: 0.68
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Pharaoh's Curse:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shogun's Ofuda:
      total: 0.55
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.6
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shield of the Phoenix:
      total: 0.67
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.82
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Runeforged Hammer
  - Heartseeker
  - Amanita Charm
  - Erosion
  flex_slots:
  - Runeforged Hammer
  - Toxic Blade
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.55
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.73
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.58
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.76
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.87
    Erosion:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Runeforged Hammer
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  - Erosion
  flex_slots:
  - Runeforged Hammer
  - Titan's Bane
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
  rationale: The model's core, corrected where the community is clearly right (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.58
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.65
    Titan's Bane:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.76
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.87
    Erosion:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.62
  swaps:
  - added: Titan's Bane
    removed: Toxic Blade
    reason: Conquest community 58% win over 99 matches (vs 48% on this god), taking
      the model's weakest slot from Toxic Blade
  borrowed_from: Conquest
  starter: *id001
---
