---
type: smite-build
god: Achilles
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
      fit: 0.54
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.77
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.91
    Erosion:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.66
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
      fit: 0.52
    Hydra's Lament:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.44
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
      fit: 0.72
    Erosion:
      total: 0.49
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
  - Jotunn's Revenge
  - Toxic Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
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
      fit: 0.85
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.65
    Void Shield:
      total: 0.66
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.85
    Void Stone:
      total: 0.64
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.85
    The Crusher:
      total: 0.68
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.72
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.8
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
      total: 0.68
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.92
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.68
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.83
    Amanita Charm:
      total: 0.68
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.72
    Pharaoh's Curse:
      total: 0.59
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shogun's Ofuda:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Gladiator's Shield
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Gladiator's Shield
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
      fit: 0.43
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shield of the Phoenix:
      total: 0.69
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.82
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.67
    Hydra's Lament:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.52
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
      fit: 0.54
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.77
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.91
    Erosion:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - The Crusher
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
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
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.56
    Hide of the Nemean Lion:
      total: 0.42
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.33
    The Crusher:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.77
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.91
    Erosion:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.66
  swaps:
  - added: Hide of the Nemean Lion
    removed: Runeforged Hammer
    reason: Conquest community 63% win over 44 matches (vs 47% on this god), taking
      the model's weakest slot from Runeforged Hammer
  borrowed_from: Conquest
  starter: *id001
---
